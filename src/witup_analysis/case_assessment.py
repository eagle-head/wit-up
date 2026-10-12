"""Assess exported information without resolving Java source or creating tests."""

import re

from witup_analysis.profiling import WRAPPER, candidate_features

NULL_CONDITION = re.compile(r"^\(\s*([A-Za-z_$][\w$]*)\s*(==|!=)\s*null\s*\)$")
TEMPORARY_SYMBOL = re.compile(r"^(?:stack_\d+|expr_\d+|_ret_\d+|caught_.+)$")
NUMERIC_CONDITION = re.compile(
    r"^\(\s*([A-Za-z_$][\w$]*)\s*(>=|<=|>|<|==|!=)\s*(-?\d+)\s*\)$"
)


def assess_case(summary: dict, result: dict, initial_tier: str) -> dict:
    model = result["modelValues"]
    null_conditions, numeric_conditions = [], []
    gaps, observations = [], []
    for condition in summary["constraints"]:
        text, truth = condition["symExpr"], condition["truthValue"]
        match = NULL_CONDITION.fullmatch(text)
        if match:
            symbol, operator = match.groups()
            required_null = truth == (operator == "==")
            flag = model.get(symbol + "_is_null")
            actual_null = {
                "BoolValue[value=true]": True,
                "BoolValue[value=false]": False,
            }.get(flag)
            null_conditions.append(
                {
                    "symbol": symbol,
                    "original_expression": text,
                    "truth_value": truth,
                    "required_null": required_null,
                    "model_null_flag": flag,
                    "model_agrees": None
                    if actual_null is None
                    else actual_null == required_null,
                }
            )
        numeric = NUMERIC_CONDITION.fullmatch(text)
        if numeric:
            symbol, operator, bound = numeric.groups()
            wrapped = WRAPPER.fullmatch(model.get(symbol, ""))
            if wrapped and wrapped.group(1) == "IntValue":
                value, bound = int(wrapped.group(2)), int(bound)
                matches = {
                    ">=": value >= bound,
                    "<=": value <= bound,
                    ">": value > bound,
                    "<": value < bound,
                    "==": value == bound,
                    "!=": value != bound,
                }
                numeric_conditions.append(
                    {
                        "symbol": symbol,
                        "original_expression": text,
                        "truth_value": truth,
                        "model_value": value,
                        "model_agrees": matches[operator] == truth,
                    }
                )
    parameters = summary["params"].split(",") if summary["params"] else []
    symbols = [key for key in model if not key.endswith("_is_null")]
    temporary_symbols = [
        symbol for symbol in symbols if TEMPORARY_SYMBOL.fullmatch(symbol)
    ]
    if parameters:
        gaps.append("formal_parameter_names_and_symbol_bindings_not_exported")
    if len(parameters) > 1:
        gaps.append("multi_parameter_assignment_not_verified")
    if parameters and not model:
        gaps.append("concrete_argument_values_not_reported")
    if summary["method"] != "<init>":
        gaps.extend(
            [
                "static_or_instance_invocation_not_exported",
                "receiver_or_static_setup_not_determined",
            ]
        )
    gaps.extend(
        [
            "accessibility_not_exported",
            "runtime_exception_site_not_verified",
            "public_contract_oracle_not_supplied",
        ]
    )
    if temporary_symbols:
        gaps.append("temporary_like_symbol_cannot_be_bound_to_argument_from_export")
        observations.append(
            "A temporary-like symbol is visible in the model. Its origin and relationship to formal parameters are not established by these JSON records."
        )
    if summary["throwSiteKind"] == "CALLEE_PROPAGATED":
        gaps.append("propagated_call_context_not_reconstructed")
    if any(
        condition["model_agrees"] is False
        for condition in [*null_conditions, *numeric_conditions]
    ):
        gaps.append("recognized_condition_and_model_disagree")
    elif any(condition["model_agrees"] is None for condition in null_conditions):
        gaps.append("nullness_model_flag_not_reported")
    if len(null_conditions) + len(numeric_conditions) != len(summary["constraints"]):
        gaps.append("condition_syntax_outside_assessment_subset")
    if not parameters:
        assignment = "no_formal_arguments"
    elif not model:
        assignment = "argument_choices_not_exported"
    elif temporary_symbols:
        assignment = "argument_binding_ambiguous"
    elif len(parameters) == 1:
        assignment = "single_argument_assignment_hypothesis"
    else:
        assignment = "multiple_argument_assignment_hypothesis"
    null_true = [item["symbol"] for item in null_conditions if item["required_null"]]
    for symbol in null_true:
        value = model.get(symbol)
        if value and value.startswith("StringValue["):
            observations.append(
                f"The null flag for {symbol} requires null even though its serialized StringValue contains text; use both pieces of information together."
            )
        elif value and value.startswith("IntValue["):
            observations.append(
                f"The serialized integer for {symbol} is a symbolic reference value in this null condition; it is not an instruction to pass a Java integer."
            )
    recomputed = candidate_features(summary, model)["tier"]
    if recomputed != initial_tier:
        classification = "stored_rule_disagreement"
    elif temporary_symbols:
        classification = "initial_tier_needs_symbol_context"
    else:
        classification = "initial_tier_retained_with_setup_gaps"
    return {
        "assessment_kind": "rule-derived export inspection",
        "initial_tier": initial_tier,
        "recomputed_tier": recomputed,
        "classification_review": classification,
        "argument_assignment": assignment,
        "reported_exception": summary["exceptionType"],
        "null_conditions": null_conditions,
        "numeric_conditions": numeric_conditions,
        "temporary_like_symbols": temporary_symbols,
        "observations": observations,
        "gaps": list(dict.fromkeys(gaps)),
        "execution_readiness": "not_established_from_exports",
        "inference_boundary": "Argument assignments are hypotheses; the export does not supply a complete Java invocation or an independently verified test oracle.",
    }
