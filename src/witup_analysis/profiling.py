"""Inventory every JSON record without loading either source array into memory."""

import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import ijson

COMMON_TYPES = {
    "artifact": str,
    "package": str,
    "class": str,
    "method": str,
    "returnType": str,
    "params": str,
    "pathIndex": int,
    "pathId": str,
}
RESULT_TYPES = {**COMMON_TYPES, "status": str, "modelValues": dict}
SUMMARY_TYPES = {
    **COMMON_TYPES,
    "exceptionType": str,
    "throwSiteKind": str,
    "provenance": list,
    "provenances": list,
    "solverStatus": str,
    "constraints": list,
}


def has_expected_type(row: dict, field: str, required_type: type, kind: str) -> bool:
    """Keep observed unknown exception types as data gaps, while requiring the field."""
    if field not in row:
        return False
    if kind == "summaries" and field == "exceptionType" and row[field] is None:
        return True
    return type(row[field]) is required_type


WRAPPER = re.compile(r"^(\w+Value)\[value=(.*)\]$", re.DOTALL)
IDENTIFIER = re.compile(r"^[A-Za-z_$][\w$]*$")
CALL = re.compile(r"[A-Za-z_$][\w$]*\s*\(")
BASIC_TYPES = {
    "boolean",
    "byte",
    "short",
    "int",
    "long",
    "float",
    "double",
    "char",
    "java.lang.String",
}


def model_kind(value: Any) -> str:
    if not isinstance(value, str):
        return type(value).__name__
    match = WRAPPER.fullmatch(value)
    return match.group(1) if match else "solver_expression"


def candidate_features(summary: dict, model: dict) -> dict:
    """Describe data-level complexity; these labels do not prove Java reachability."""
    expressions = [item["symExpr"] for item in summary["constraints"]]
    keys = list(model)
    receiver_state = any(re.search(r"\bthis\b", text) for text in [*expressions, *keys])
    static_state = any(re.search(r"<[^>]+:.*>", text) for text in expressions)
    calls = any(CALL.search(text) for text in [*expressions, *keys])
    symbolic_values = any(
        model_kind(value) == "solver_expression" for value in model.values()
    )
    complex_keys = any(
        not IDENTIFIER.fullmatch(key) or key.startswith(("_ret_", "expr_", "caught_"))
        for key in keys
    )
    parameters = summary["params"].split(",") if summary["params"] else []
    basic = all(parameter in BASIC_TYPES for parameter in parameters)
    null_flags = [
        key
        for key, value in model.items()
        if key.endswith("_is_null")
        and value == "BoolValue[value=true]"
        and IDENTIFIER.fullmatch(key)
    ]
    if receiver_state or static_state:
        tier = "state_context_required"
    elif calls:
        tier = "call_context_required"
    elif symbolic_values or complex_keys:
        tier = "model_reconstruction_required"
    elif basic:
        tier = "simple_signature_hypothesis"
    elif len(parameters) == 1 and null_flags:
        tier = "null_argument_hypothesis"
    else:
        tier = "object_fixture_required"
    return {
        "tier": tier,
        "constraint_count": len(expressions),
        "model_value_count": len(model),
        "parameter_count": len(parameters),
        "receiver_state": receiver_state,
        "static_state": static_state,
        "method_calls": calls,
        "symbolic_values": symbolic_values,
        "complex_model_keys": complex_keys,
    }


def profile(path: Path, kind: str) -> dict:
    expected = RESULT_TYPES if kind == "results" else SUMMARY_TYPES
    fields = Counter()
    types = defaultdict(Counter)
    nested_fields = defaultdict(Counter)
    statuses, exceptions, throws, model_kinds = (
        Counter(),
        Counter(),
        Counter(),
        Counter(),
    )
    artifacts, methods, classes = set(), set(), set()
    totals = Counter()
    issues = []

    def issue(index: int, message: str) -> None:
        totals["schema_issue_count"] += 1
        if len(issues) < 10:
            issues.append({"record_index": index, "message": message})

    with path.open("rb") as handle:
        while True:
            character = handle.read(1)
            if not character:
                raise ValueError(f"Empty JSON input: {path}")
            if character not in b" \t\r\n":
                break
        if character != b"[":
            raise ValueError(f"Expected a top-level JSON array: {path}")
        handle.seek(0)
        for index, row in enumerate(ijson.items(handle, "item"), start=1):
            totals["rows"] += 1
            if not isinstance(row, dict):
                issue(index, "Record is not an object")
                continue
            for field, value in row.items():
                fields[field] += 1
                types[field][type(value).__name__] += 1
            for field, required_type in expected.items():
                if not has_expected_type(row, field, required_type, kind):
                    issue(
                        index, f"Expected {field} to have type {required_type.__name__}"
                    )
            if not all(
                has_expected_type(row, field, value_type, kind)
                for field, value_type in expected.items()
            ):
                continue
            artifacts.add(row["artifact"])
            classes.add((row["package"], row["class"]))
            signature, separator, path_index = row["pathId"].rpartition("#")
            methods.add(signature)
            expected_id = (
                f"<{row['package']}.{row['class']}: {row['returnType']} "
                f"{row['method']}({row['params']})>#{row['pathIndex']}"
            )
            if (
                not separator
                or not path_index.isdigit()
                or int(path_index) != row["pathIndex"]
            ):
                totals["path_index_mismatches"] += 1
            if expected_id != row["pathId"]:
                totals["path_metadata_mismatches"] += 1
            totals["constructors"] += row["method"] == "<init>"
            if kind == "results":
                statuses[row["status"]] += 1
                model = row["modelValues"]
                totals["empty_models"] += not model
                totals["model_entries"] += len(model)
                totals["sat_empty_models"] += row["status"] == "SAT" and not model
                for key, value in model.items():
                    model_kinds[model_kind(value)] += 1
                    totals["null_flag_entries"] += key.endswith("_is_null")
                    if not isinstance(value, str):
                        issue(index, f"Model value for {key} is not a string")
            else:
                statuses[row["solverStatus"]] += 1
                exceptions[
                    row["exceptionType"]
                    if row["exceptionType"] is not None
                    else "<null>"
                ] += 1
                totals["unknown_exception_types"] += row["exceptionType"] is None
                throws[row["throwSiteKind"]] += 1
                totals["constraints"] += len(row["constraints"])
                totals["empty_constraints"] += not row["constraints"]
                totals["nonempty_provenance"] += bool(row["provenance"])
                totals["multiple_provenances"] += len(row["provenances"]) > 1
                totals["provenance_chains"] += len(row["provenances"])
                for constraint in row["constraints"]:
                    if not isinstance(constraint, dict):
                        issue(index, "Constraint is not an object")
                        continue
                    nested_fields["constraints"].update(constraint.keys())
                    if (
                        not isinstance(constraint.get("symExpr"), str)
                        or type(constraint.get("truthValue")) is not bool
                    ):
                        issue(
                            index,
                            "Constraint requires a string symExpr and boolean truthValue",
                        )
                    else:
                        totals["true_constraints"] += constraint["truthValue"]
                        totals["false_constraints"] += not constraint["truthValue"]
                if not all(isinstance(value, str) for value in row["provenance"]):
                    issue(index, "provenance contains a non-string value")
                if not all(
                    isinstance(chain, list)
                    and all(isinstance(value, str) for value in chain)
                    for chain in row["provenances"]
                ):
                    issue(index, "provenances is not a list of string lists")
    return {
        "path": str(path.resolve()),
        "bytes": path.stat().st_size,
        "artifacts": sorted(artifacts),
        "method_count": len(methods),
        "class_count": len(classes),
        "totals": dict(totals),
        "schema": [
            {
                "field": field,
                "present": fields[field],
                "missing": totals["rows"] - fields[field],
                "types": dict(types[field]),
            }
            for field in fields
        ],
        "nested_fields": {key: dict(value) for key, value in nested_fields.items()},
        "statuses": dict(statuses.most_common()),
        "exception_types": dict(exceptions.most_common()),
        "throw_site_kinds": dict(throws.most_common()),
        "model_kinds": dict(model_kinds.most_common()),
        "schema_issues": issues,
    }
