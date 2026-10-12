"""Write a short case overview and one auditable document per selected path."""

import json
from pathlib import Path

from witup_analysis.reporting import table


def write_case_documents(inventory: dict, docs_dir: Path) -> None:
    cases_dir, findings_dir = docs_dir / "cases", docs_dir / "findings"
    cases_dir.mkdir(parents=True, exist_ok=True)
    findings_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for case in inventory["cases"]:
        summary, assessment = case["original_summary"], case["assessment"]
        filename = Path(case["document"]).name
        operation = (
            "constructor" if summary["method"] == "<init>" else summary["method"]
        )
        rows.append(
            [
                f"[{summary['class']}.{operation}](../cases/{filename})",
                case["selection"]["stratum"],
                summary["exceptionType"],
                summary["throwSiteKind"],
                assessment["classification_review"],
            ]
        )
        sections = [
            f"# `{case['identity']['path_id']}`",
            "[Documentation index](../README.md) | [Case findings](../findings/case-assessment.md) | [Assessment rubric](../methodology/case-assessment.md)",
            "## Record identity and selection",
            table(
                ["Property", "Value"],
                [
                    ["Artifact", f"`{case['identity']['artifact']}`"],
                    ["Initial stratum", f"`{case['selection']['stratum']}`"],
                    ["Selection order", case["selection"]["order"]],
                    [
                        "Novel dimensions when selected",
                        ", ".join(case["selection"]["new_dimensions"]) or "None",
                    ],
                    [
                        "Result locator",
                        f"`{case['source_records']['results']['filename']}`, array record {case['source_records']['results']['array_record_number']}",
                    ],
                    [
                        "Summary locator",
                        f"`{case['source_records']['summaries']['filename']}`, array record {case['source_records']['summaries']['array_record_number']}",
                    ],
                ],
            ),
            "Array record numbers are 1-based. The artifact/pathId pair is the semantic locator. Input byte identities are recorded in `data/processed/case-inventory.json`. The source records below preserve parsed values; whitespace and object-key ordering are not byte-for-byte copies.",
            "## Explicit exported information",
            table(
                ["Property", "Exported value"],
                [
                    [
                        "Parameter types",
                        f"`{summary['params']}`"
                        if summary["params"]
                        else "No formal parameters",
                    ],
                    ["Reported exception", f"`{summary['exceptionType']}`"],
                    ["Reported origin", f"`{summary['throwSiteKind']}`"],
                    [
                        "Summary / result verdict",
                        f"{summary['solverStatus']} / {case['original_result']['status']}",
                    ],
                    ["Condition entries", len(summary["constraints"])],
                    ["Model entries", len(case["original_result"]["modelValues"])],
                ],
            ),
            "### Original parsed result",
            "```json\n"
            + json.dumps(case["original_result"], indent=2, ensure_ascii=True)
            + "\n```",
            "### Original parsed summary",
            "```json\n" + json.dumps(summary, indent=2, ensure_ascii=True) + "\n```",
            "## Rule-derived interpretation",
            table(
                ["Dimension", "Assessment"],
                [
                    ["Argument assignment", assessment["argument_assignment"]],
                    [
                        "Initial classification review",
                        assessment["classification_review"],
                    ],
                    ["Execution readiness", assessment["execution_readiness"]],
                ],
            ),
            assessment["inference_boundary"],
        ]
        if assessment["null_conditions"]:
            sections.extend(
                [
                    "### Nullness conditions",
                    table(
                        [
                            "Symbol",
                            "Expression",
                            "truthValue",
                            "Required null",
                            "Model agrees",
                        ],
                        [
                            [
                                item["symbol"],
                                f"`{item['original_expression']}`",
                                item["truth_value"],
                                item["required_null"],
                                item["model_agrees"],
                            ]
                            for item in assessment["null_conditions"]
                        ],
                    ),
                ]
            )
        if assessment["numeric_conditions"]:
            sections.extend(
                [
                    "### Integer conditions",
                    table(
                        [
                            "Symbol",
                            "Expression",
                            "truthValue",
                            "Model value",
                            "Model agrees",
                        ],
                        [
                            [
                                item["symbol"],
                                f"`{item['original_expression']}`",
                                item["truth_value"],
                                item["model_value"],
                                item["model_agrees"],
                            ]
                            for item in assessment["numeric_conditions"]
                        ],
                    ),
                ]
            )
        if assessment["observations"]:
            sections.append(
                "\n".join(
                    "- " + observation for observation in assessment["observations"]
                )
            )
        sections.extend(
            [
                "## Information gaps retained for later work",
                "\n".join(f"- `{gap}`" for gap in assessment["gaps"]),
                "These gaps concern exported information. They are not findings about correctness, accessibility, or runtime behavior of the Java implementation. No Java source was inspected for this case.",
            ]
        )
        (cases_dir / filename).write_text(
            "\n\n".join(sections) + "\n", encoding="utf-8"
        )
    counts = inventory["summary"]
    qualitative = []
    if any(case["assessment"]["numeric_conditions"] for case in inventory["cases"]):
        qualitative.append(
            "Integer predicates retain their truth flags and model values, including negated comparisons."
        )
    if any(case["assessment"]["observations"] for case in inventory["cases"]):
        qualitative.append(
            "The linked records document how null flags relate to serialized strings or reference encodings."
        )
    if counts["gaps"].get("concrete_argument_values_not_reported"):
        qualitative.append(
            "Some signatures require arguments even though their models supply no values; later argument choices would be additional assumptions."
        )
    if counts["gaps"].get(
        "temporary_like_symbol_cannot_be_bound_to_argument_from_export"
    ):
        qualitative.append(
            "A temporary-like model symbol has clear nullness but an unresolved relationship to formal arguments; it remains in the sample."
        )
    sections = [
        "# Case assessment findings",
        "[Documentation index](../README.md) | [Selection method](../methodology/case-selection.md) | [Assessment rubric](../methodology/case-assessment.md)",
        f"Generated at `{inventory['generated_at_utc']}`. This is a purposive data-inspection sample: **{counts['cases']} paths**, **{counts['methods']} distinct method signatures**, and **{counts['classes']} declaring classes**. The quotas are {inventory['selection_policy']['per_stratum']} cases from each initial stratum. Selection and original input records are retained in `data/processed/case-inventory.json`.",
        "## Cases",
        table(
            [
                "Case document",
                "Initial stratum",
                "Reported exception",
                "Origin",
                "Classification review",
            ],
            rows,
        ),
        "## Assessment outcomes",
        table(
            ["Outcome", "Cases"],
            [[name, count] for name, count in counts["assessment_outcomes"].items()],
        ),
        "The initial labels describe exported shape. A retained label does not mean that a complete invocation is available. Ambiguities remain in the selected sample and are reported as separate outcomes.",
        "## Reported exceptions",
        table(
            ["Exception", "Cases"],
            [[name, count] for name, count in counts["exception_types"].items()],
        ),
        "## Reported origins",
        table(
            ["Origin", "Cases"],
            [[name, count] for name, count in counts["throw_site_kinds"].items()],
        ),
        "## Information gaps",
        table(
            ["Gap", "Cases"], [[name, count] for name, count in counts["gaps"].items()]
        ),
        "Gap counts overlap. Denominator: the selected cases only. These observations cannot be extrapolated to the 221-path candidate pool, the full SAT population, or the library.",
        "## Qualitative inspection of the selected records",
        " ".join(qualitative)
        + " Numeric/null consistency checks validate only the recognized expression subset; they do not validate the complete solver encoding.",
        "The exported exception supplies a candidate assertion target for each selected case. Ordinary-method invocation mode, accessibility, runtime exception location and an independent public-contract oracle remain unresolved. Constructors expose an operation signature, but public accessibility and formal parameter bindings are still absent from these records.",
        "## Supported conclusion and next boundary",
        "The sample provides traceable material for a later isolated generation experiment and reveals concrete preparation ambiguities. Execution readiness is not established from these exports. No LLM generation rate, compilation rate, exception reproduction rate, or test quality was measured. Keep this inventory fixed when defining that later experiment; changes to selection or assessment should be recorded as protocol revisions.",
    ]
    (findings_dir / "case-assessment.md").write_text(
        "\n\n".join(sections) + "\n", encoding="utf-8"
    )
