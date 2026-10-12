"""Select a deterministic, diverse inventory and retain original JSON records."""

import hashlib
import json
import os
import re
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

import duckdb
import ijson

from witup_analysis.analysis import records
from witup_analysis.case_assessment import assess_case
from witup_analysis.case_reporting import write_case_documents
from witup_analysis.profiling import candidate_features

STRATA = ("simple_signature_hypothesis", "null_argument_hypothesis")
DIMENSIONS = ("class", "exception", "origin", "parameters", "operation", "conditions")


def dimensions(row: dict) -> tuple:
    return (
        row["package"] + "." + row["class"],
        row["exceptionType"],
        row["throwSiteKind"],
        row["params"],
        "constructor" if row["method"] == "<init>" else "method",
        len(row["constraints"]),
    )


def select_cases(pool: list[dict], per_stratum: int = 10) -> list[dict]:
    """Greedily prefer unseen data dimensions, with fixed lexical tie breakers."""
    if per_stratum < 1:
        raise ValueError("The per-stratum quota must be positive")
    keys = [(row["artifact"], row["pathId"]) for row in pool]
    if len(keys) != len(set(keys)):
        raise ValueError("Candidate pool contains duplicate artifact/pathId keys")
    seen = {dimension: set() for dimension in DIMENSIONS}
    seen_signatures = set()
    selected = []
    for stratum in STRATA:
        available = [row for row in pool if row["tier"] == stratum]
        signatures = {row["pathId"].rsplit("#", 1)[0] for row in available}
        if len(signatures - seen_signatures) < per_stratum:
            raise ValueError(
                f"Insufficient distinct methods in {stratum} for quota {per_stratum}"
            )
        for _ in range(per_stratum):
            eligible = [
                row
                for row in available
                if row["pathId"].rsplit("#", 1)[0] not in seen_signatures
            ]

            def rank(row: dict) -> tuple:
                novelty = tuple(
                    -int(value not in seen[name])
                    for name, value in zip(DIMENSIONS, dimensions(row), strict=True)
                )
                return novelty + (
                    len(row["constraints"]),
                    len(row["modelValues"]),
                    row["artifact"],
                    row["pathId"],
                )

            choice = min(eligible, key=rank)
            values = dimensions(choice)
            selected.append(
                {
                    "candidate": choice,
                    "selection": {
                        "order": len(selected) + 1,
                        "stratum": stratum,
                        "new_dimensions": [
                            name
                            for name, value in zip(DIMENSIONS, values, strict=True)
                            if value not in seen[name]
                        ],
                        "tie_breakers": {
                            "constraint_count": len(choice["constraints"]),
                            "model_value_count": len(choice["modelValues"]),
                            "artifact": choice["artifact"],
                            "path_id": choice["pathId"],
                        },
                    },
                }
            )
            seen_signatures.add(choice["pathId"].rsplit("#", 1)[0])
            for name, value in zip(DIMENSIONS, values, strict=True):
                seen[name].add(value)
    return selected


def original_records(path: Path, wanted: set[tuple]) -> dict:
    """Store a 1-based array locator and reject ambiguous original record keys."""
    found = {}
    with path.open("rb") as handle:
        for position, row in enumerate(ijson.items(handle, "item"), start=1):
            key = (row["artifact"], row["pathId"])
            if key in wanted:
                if key in found:
                    raise ValueError(f"Duplicate selected key in {path}: {key}")
                found[key] = {"array_record_number": position, "record": row}
    if set(found) != wanted:
        raise ValueError(
            f"Selected records are missing from {path}: {wanted - set(found)}"
        )
    return found


def sha256(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def case_filename(summary: dict) -> str:
    operation = "constructor" if summary["method"] == "<init>" else summary["method"]
    parameters = summary["params"].replace("[]", "-array") or "no-parameters"
    value = f"{summary['package']}.{summary['class']}-{operation}-{parameters}-path-{summary['pathIndex']}"
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") + ".md"


def inspect_cases(
    root: Path, output_dir: Path, docs_dir: Path, per_stratum: int = 10
) -> dict:
    output_dir, docs_dir = output_dir.resolve(), docs_dir.resolve()
    for destination in (output_dir, docs_dir):
        if os.name == "nt" and destination.drive.upper() != "D:":
            raise ValueError(f"Project outputs must remain on D: {destination}")
    statistics_path = output_dir / "statistics.json"
    statistics = json.loads(statistics_path.read_text(encoding="utf-8"))
    connection = duckdb.connect(str(output_dir / "commons-io.duckdb"), read_only=True)
    try:
        pool = records(
            connection,
            """SELECT * FROM candidates
            WHERE tier IN ('simple_signature_hypothesis','null_argument_hypothesis')
            ORDER BY artifact,pathId""",
        )
    finally:
        connection.close()
    for row in pool:
        row["modelValues"] = json.loads(row["modelValues"])
        if (
            row["solverStatus"] != "SAT"
            or row["resultStatus"] != "SAT"
            or not row["hasResult"]
            or not row["metadataMatches"]
            or row["exceptionType"] is None
        ):
            raise ValueError(f"Ineligible candidate in derived pool: {row['pathId']}")
        if candidate_features(row, row["modelValues"])["tier"] != row["tier"]:
            raise ValueError(
                f"Stored classification differs from current rules: {row['pathId']}"
            )
    actual_counts = Counter(row["tier"] for row in pool)
    expected_counts = {
        stratum: statistics["candidate_tiers"][stratum] for stratum in STRATA
    }
    if dict(actual_counts) != expected_counts:
        raise ValueError(
            f"Candidate counts differ from the measured inventory: {dict(actual_counts)} versus {expected_counts}"
        )
    selected = select_cases(pool, per_stratum)
    wanted = {
        (item["candidate"]["artifact"], item["candidate"]["pathId"])
        for item in selected
    }
    originals = {}
    identities = {}
    for kind in ("results", "summaries"):
        path = Path(statistics["profiles"][kind]["path"])
        originals[kind] = original_records(path, wanted)
        identities[kind] = {
            "filename": path.name,
            "project_relative_path": path.relative_to(root).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
    cases = []
    filenames = set()
    for item in selected:
        candidate = item["candidate"]
        key = (candidate["artifact"], candidate["pathId"])
        result, summary = (
            originals[name][key]["record"] for name in ("results", "summaries")
        )
        for field, value in summary.items():
            if candidate[field] != value:
                raise ValueError(
                    f"Derived summary differs from original: {key}, {field}"
                )
        if (
            result["modelValues"] != candidate["modelValues"]
            or result["status"] != candidate["resultStatus"]
        ):
            raise ValueError(f"Derived result differs from original: {key}")
        for field in (
            "artifact",
            "package",
            "class",
            "method",
            "returnType",
            "params",
            "pathIndex",
            "pathId",
        ):
            if result[field] != summary[field]:
                raise ValueError(f"Original joined metadata disagrees: {key}, {field}")
        filename = case_filename(summary)
        if filename in filenames:
            raise ValueError(f"Case document filename collision: {filename}")
        filenames.add(filename)
        cases.append(
            {
                "identity": {"artifact": key[0], "path_id": key[1]},
                "selection": item["selection"],
                "source_records": {
                    name: {
                        "filename": identities[name]["filename"],
                        "array_record_number": originals[name][key][
                            "array_record_number"
                        ],
                    }
                    for name in ("results", "summaries")
                },
                "original_result": result,
                "original_summary": summary,
                "assessment": assess_case(summary, result, candidate["tier"]),
                "document": f"cases/{filename}",
            }
        )
    summary_counts = {
        "cases": len(cases),
        "methods": len(
            {case["identity"]["path_id"].rsplit("#", 1)[0] for case in cases}
        ),
        "classes": len(
            {
                case["original_summary"]["package"]
                + "."
                + case["original_summary"]["class"]
                for case in cases
            }
        ),
        "strata": dict(Counter(case["selection"]["stratum"] for case in cases)),
        "exception_types": dict(
            Counter(case["original_summary"]["exceptionType"] for case in cases)
        ),
        "throw_site_kinds": dict(
            Counter(case["original_summary"]["throwSiteKind"] for case in cases)
        ),
        "assessment_outcomes": dict(
            Counter(case["assessment"]["classification_review"] for case in cases)
        ),
        "gaps": dict(
            Counter(gap for case in cases for gap in case["assessment"]["gaps"])
        ),
    }
    inventory = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(UTC).isoformat(),
        "inputs": identities,
        "environment": statistics["environment"],
        "analysis_code": {
            name: sha256(root / name)
            for name in (
                "src/witup_analysis/selection.py",
                "src/witup_analysis/case_assessment.py",
                "src/witup_analysis/case_reporting.py",
                "src/witup_analysis/profiling.py",
                "uv.lock",
            )
        },
        "selection_policy": {
            "version": 1,
            "method": "deterministic purposive diversity selection",
            "per_stratum": per_stratum,
            "stratum_order": list(STRATA),
            "novelty_priority": list(DIMENSIONS),
            "tie_breakers": [
                "constraint_count",
                "model_value_count",
                "artifact",
                "path_id",
            ],
            "one_path_per_method": True,
            "pool_counts": expected_counts,
        },
        "selection_pool": [
            {
                "artifact": row["artifact"],
                "path_id": row["pathId"],
                "stratum": row["tier"],
            }
            for row in pool
        ],
        "summary": summary_counts,
        "cases": cases,
    }
    (output_dir / "case-inventory.json").write_text(
        json.dumps(inventory, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )
    write_case_documents(inventory, docs_dir)
    print(json.dumps(summary_counts, indent=2), flush=True)
    return inventory
