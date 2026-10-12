"""Render measured JSON inventories and bounded interpretations as Markdown."""

import json
from pathlib import Path

FIELD_MEANINGS = {
    "artifact": "External artifact label; the filename alone does not verify JAR contents.",
    "package": "Declaring package label.",
    "class": "Declaring class label.",
    "method": "Method name; `<init>` denotes a constructor.",
    "returnType": "Declared return type in the exported signature.",
    "params": "Comma-separated parameter types; parameter names are not supplied here.",
    "pathIndex": "Index within the exported method's observable path list.",
    "pathId": "Full method signature followed by # and pathIndex.",
    "status": "Solver verdict for a result row.",
    "modelValues": "Symbol names mapped to serialized solver values, not ready-made Java fixtures.",
    "exceptionType": "Exception associated with the modeled path; a later test must confirm it.",
    "throwSiteKind": "Reported origin category: direct throw, implicit exception, propagated callee exception, or rethrow.",
    "provenance": "Representative call chain recorded for the flow.",
    "provenances": "Call-chain alternatives grouped into the summary row.",
    "solverStatus": "Solver verdict attached to the summary row.",
    "constraints": "Conjunction of symbolic expressions evaluated with their truthValue flags.",
}
TIER_MEANINGS = {
    "exception_not_reported": "SAT pair with exceptionType=null; no named exception is supplied for an assertion.",
    "simple_signature_hypothesis": "SAT pair; only primitive/String parameters (or none), without detected state/call/model complexity.",
    "null_argument_hypothesis": "SAT pair; one other parameter type and an identifier-shaped true null flag. Its mapping to that argument still needs confirmation.",
    "object_fixture_required": "SAT pair; richer parameter types suggest a stream/file/object fixture.",
    "state_context_required": "SAT pair; receiver or signature-qualified state appears in expressions/model keys.",
    "call_context_required": "SAT pair; method-call syntax appears in conditions/model keys.",
    "model_reconstruction_required": "SAT pair; symbolic solver values or compound/temporary model keys need interpretation.",
    "solver_not_sat": "Both records agree, but the verdict is not SAT; retained for inventory, outside the initial candidate pool.",
    "missing_result": "No matching result supplies the solver model.",
    "join_disagreement": "Matched rows disagree on status or method metadata.",
}


def cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers: list[str], rows: list[list]) -> str:
    return "\n".join(
        [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join("---" for _ in headers) + " |",
            *("| " + " | ".join(cell(value) for value in row) + " |" for row in rows),
        ]
    )


def distribution(values: dict, denominator: int) -> str:
    return table(
        ["Value", "Rows", "Share"],
        [
            [
                f"`{key}`",
                f"{count:,}",
                f"{count / denominator:.2%}" if denominator else "n/a",
            ]
            for key, count in values.items()
        ],
    )


def write_report(stats: dict, path: Path) -> None:
    results, summaries = stats["profiles"]["results"], stats["profiles"]["summaries"]
    nr, ns = results["totals"]["rows"], summaries["totals"]["rows"]
    correspondence = stats["correspondence"]
    sections = [
        "# Commons IO WIT-UP JSON analysis",
        "## Scope and method",
        "This report answers four questions using the two supplied JSON exports. It inventories data relevant to a later, isolated study of generating JUnit tests. No test-generation model/API was invoked by the pipeline, no JUnit tests were generated or executed, and neither Java project was changed or reviewed for correctness.",
        f"Generated at `{stats['generated_at_utc']}`. Every record was read with ijson; DuckDB independently loaded the original arrays and its row counts were checked against the streaming counts. Derived tables preserve raw model strings and nested conditions. Candidate labels are explicit syntactic heuristics, not measurements of Java reachability or LLM effectiveness.",
        table(
            ["Input", "File", "Bytes", "Records"],
            [
                [
                    "results",
                    f"`{Path(results['path']).name}`",
                    f"{results['bytes']:,}",
                    f"{nr:,}",
                ],
                [
                    "summaries",
                    f"`{Path(summaries['path']).name}`",
                    f"{summaries['bytes']:,}",
                    f"{ns:,}",
                ],
            ],
        ),
        "The input filenames, Java signatures, exception names, and JSON field names are preserved as external values. Artifact labels associate these exports with Commons IO commit `11f0abe7a`; they do not independently prove which bytes were analyzed. No analyzed JAR or failures export was supplied.",
        "## 1. What fields exist, and how do the files relate?",
        "Both inputs are arrays of objects. The tables below describe the fields observed across the complete files. Presence and missing counts are measured; meanings are interpretations informed by the exporter source cited below.",
    ]
    for name, source in (("results", results), ("summaries", summaries)):
        sections.extend(
            [
                f"### {name} schema",
                table(
                    ["Field", "Observed Python types", "Present", "Missing", "Meaning"],
                    [
                        [
                            f"`{field['field']}`",
                            ", ".join(field["types"]),
                            f"{field['present']:,}",
                            f"{field['missing']:,}",
                            FIELD_MEANINGS.get(
                                field["field"], "Additional observed field."
                            ),
                        ]
                        for field in source["schema"]
                    ],
                ),
                f"Schema issue count: **{source['totals'].get('schema_issue_count', 0):,}**. Path/index disagreement count: **{source['totals'].get('path_index_mismatches', 0):,}**. Path/signature metadata disagreement count: **{source['totals'].get('path_metadata_mismatches', 0):,}**.",
            ]
        )
    sections.extend(
        [
            "### Join inventory",
            f"`exceptionType` is present in every summary, but **{summaries['totals'].get('unknown_exception_types', 0):,}** values are JSON null. This is retained as an unknown exception, not converted into an exception name or discarded. Structural validation permits this observed nullable field; the candidate inventory records its missing assertion information separately.",
            "Use **(artifact, pathId)** as the cross-file key. The full signature includes the parameter types, so overloaded methods retain separate identities. Uniqueness is checked before the join. The relation is checked for matching statuses and signature metadata.",
            table(
                ["Observation", "Count"],
                [
                    [
                        "Duplicate result keys",
                        correspondence["duplicate_keys"]["results"],
                    ],
                    [
                        "Duplicate summary keys",
                        correspondence["duplicate_keys"]["summaries"],
                    ],
                    [
                        "Summary rows with a result",
                        f"{correspondence['matched_summaries']:,}",
                    ],
                    [
                        "Summary rows without a result",
                        f"{correspondence['summaries_without_results']:,}",
                    ],
                    [
                        "Result rows without a summary",
                        f"{correspondence['results_without_summaries']:,}",
                    ],
                    [
                        "Matched status disagreements",
                        correspondence["status_mismatches"],
                    ],
                    [
                        "Matched metadata disagreements",
                        correspondence["metadata_mismatches"],
                    ],
                    [
                        "Method signatures found only in results",
                        correspondence["results_only_methods"],
                    ],
                    [
                        "Method signatures found only in summaries",
                        correspondence["summaries_only_methods"],
                    ],
                ],
            ),
            "Matched verdicts:",
            table(
                ["Summary status", "Result status", "Rows"],
                [
                    [row["solverStatus"], row["resultStatus"], f"{row['rows']:,}"]
                    for row in stats["status_matrix"]
                ],
            ),
            "Statuses among result rows without a summary:",
            table(
                ["Result status", "Rows"],
                [
                    [row["status"], f"{row['rows']:,}"]
                    for row in stats["unmatched_result_statuses"]
                ],
            ),
            "The inspected exporter produces a result per solved path and groups summary flows by (exceptionType, throwSiteKind, constraints), keeping the first path identifier and collecting provenance alternatives. This explains why equal row counts should not be assumed. The unmatched-result count is observed; attributing every unmatched row to grouping remains an interpretation because the producing WIT-UP revision and full path list are unavailable.",
            "## 2. How many methods, paths, exception types, and solver verdicts appear?",
            table(
                ["Unit", "results", "summaries"],
                [
                    ["Rows / unique cross-file path keys", f"{nr:,}", f"{ns:,}"],
                    [
                        "Full method signatures, including constructors",
                        f"{results['method_count']:,}",
                        f"{summaries['method_count']:,}",
                    ],
                    [
                        "Declaring classes",
                        f"{results['class_count']:,}",
                        f"{summaries['class_count']:,}",
                    ],
                    [
                        "Rows referring to constructors",
                        f"{results['totals'].get('constructors', 0):,}",
                        f"{summaries['totals'].get('constructors', 0):,}",
                    ],
                    [
                        "Distinct named exception types",
                        "Not exported",
                        len(summaries["exception_types"])
                        - int("<null>" in summaries["exception_types"]),
                    ],
                ],
            ),
            "These are units represented by the supplied exports, not all methods or all runtime paths in the library. Methods with no exported exception paths and analysis failures cannot be counted from these two files alone.",
            "### Result verdicts",
            distribution(results["statuses"], nr),
            "### Summary verdicts",
            distribution(summaries["statuses"], ns),
            "`SAT` means satisfiable in the encoded constraint model. `UNSAT` means unsatisfiable in that model. `UNKNOWN` is an undecided solver verdict. In the inspected implementation, `MAYBE` can record incomplete constraint handling or a failed solver task. The verdict is a prioritization input for later experiments, not evidence that a Java fixture reaches the reported exception.",
            "### Exception origins",
            distribution(summaries["throw_site_kinds"], ns),
            "### Most frequent exception types",
            distribution(dict(list(summaries["exception_types"].items())[:15]), ns),
            "The complete exception distribution is available in `data/processed/statistics.json`.",
            "`<null>` in the distribution is a display label for JSON null, not a Java exception type.",
            "### Methods with the most summary paths",
            table(
                ["Signature", "Summary paths", "SAT paths"],
                [
                    [
                        f"`{row['signature']}`",
                        f"{row['paths']:,}",
                        f"{row['sat_paths']:,}",
                    ]
                    for row in stats["methods_with_most_paths"]
                ],
            ),
            "## 3. What information supports arranging inputs and writing assertions?",
            table(
                ["Available data", "Potential use in a later test", "Boundary"],
                [
                    [
                        "Class, method, return type, parameter types",
                        "Identify the intended operation and overload",
                        "Visibility, static/instance modifiers, parameter names, constructors and fixture recipes are absent.",
                    ],
                    [
                        "constraints.symExpr and constraints.truthValue",
                        "Describe the condition a preparation should satisfy",
                        "A false truthValue negates the expression; all entries are conjoined. Strings are symbolic syntax, not executable Java.",
                    ],
                    [
                        "modelValues",
                        "Suggest scalar values and nullness assignments",
                        "Object identities, temporaries, fields, arrays and call results may require reconstruction. A model symbol is not automatically a method argument.",
                    ],
                    [
                        "exceptionType",
                        "Suggest an exception assertion on the intended operation",
                        "The same exception can arise during setup or elsewhere; exception type alone does not demonstrate the modeled scenario.",
                    ],
                    [
                        "throwSiteKind and provenance(s)",
                        "Help interpret direct, implicit and propagated flows",
                        "There is no explicit source line or runtime event trace in these records.",
                    ],
                    [
                        "solver verdict",
                        "Prioritize candidate rows while retaining uncertain rows",
                        "It does not establish constructibility, public API reachability, or intended behavior.",
                    ],
                ],
            ),
            table(
                ["Observation", "Count"],
                [
                    [
                        "Result rows with an empty model",
                        f"{results['totals'].get('empty_models', 0):,}",
                    ],
                    [
                        "SAT result rows with an empty model",
                        f"{results['totals'].get('sat_empty_models', 0):,}",
                    ],
                    [
                        "Serialized model entries",
                        f"{results['totals'].get('model_entries', 0):,}",
                    ],
                    [
                        "Model keys ending in _is_null",
                        f"{results['totals'].get('null_flag_entries', 0):,}",
                    ],
                    [
                        "Summary rows with no conditions",
                        f"{summaries['totals'].get('empty_constraints', 0):,}",
                    ],
                    [
                        "Total condition entries",
                        f"{summaries['totals'].get('constraints', 0):,}",
                    ],
                    [
                        "Condition entries with truthValue=true",
                        f"{summaries['totals'].get('true_constraints', 0):,}",
                    ],
                    [
                        "Condition entries with truthValue=false",
                        f"{summaries['totals'].get('false_constraints', 0):,}",
                    ],
                    [
                        "Summary rows with nonempty representative provenance",
                        f"{summaries['totals'].get('nonempty_provenance', 0):,}",
                    ],
                    [
                        "Summary rows with multiple provenance alternatives",
                        f"{summaries['totals'].get('multiple_provenances', 0):,}",
                    ],
                ],
            ),
            "Serialized model value kinds (denominator: model entries):",
            distribution(
                results["model_kinds"], results["totals"].get("model_entries", 0)
            ),
            "An empty model can accompany a satisfiable path with no required scalar assignments; it is not automatically missing data. This phase keeps the strings intact, including `IntValue[...]`, `BoolValue[...]` and solver expressions. Numeric encodings may represent references rather than Java numbers.",
            "The exports describe exceptional behavior. They do not supply normal return-value expectations, a complete public contract, argument-name/position mappings, or an independently validated oracle. A later exception test would initially characterize a reported scenario; correctness of that scenario requires separate evidence.",
            "## 4. Which rows are simpler candidates for an initial experiment?",
            "The following mutually exclusive labels are data-level preparation hypotheses. They are assigned in priority order: unavailable/disagreeing join or non-SAT verdict; an unreported exception type; state references; call syntax; symbolic/compound model values; basic signatures; a single-reference null hypothesis; other object fixtures. State/call flags use textual patterns, so both missed complexity and conservative false positives are possible.",
            "Basic signatures have no parameters or only primitive/String parameter types. Null hypotheses have one other parameter type and an identifier-shaped `_is_null` flag whose value is `BoolValue[value=true]`. Both require a matching SAT result and summary. Neither proves that a symbol is an argument, that an instance can be built, or that the operation is publicly accessible.",
            table(
                ["Tier", "Rows", "Share of summaries", "Rule / interpretation"],
                [
                    [
                        f"`{tier}`",
                        f"{count:,}",
                        f"{count / ns:.2%}",
                        TIER_MEANINGS[tier],
                    ]
                    for tier, count in stats["candidate_tiers"].items()
                ],
            ),
            "Preparation flags below overlap and cover all summary rows, including non-SAT rows:",
            table(
                ["Flag", "Rows"],
                [
                    [key, f"{count:,}"]
                    for key, count in stats["candidate_features"].items()
                ],
            ),
            "### Examples selected from the simpler tiers",
            "Up to six distinct method signatures per simpler tier are selected deterministically, preferring direct throws and fewer conditions/model entries. This illustrates the input data; it is not a representative effectiveness sample or an approved set of generated tests.",
        ]
    )
    for example in stats["candidate_examples"]:
        sections.extend(
            [
                f"#### `{example['pathId']}`",
                f"Tier: `{example['tier']}`; exception: `{example['exceptionType']}`; origin: `{example['throwSiteKind']}`; solver status: `{example['solverStatus']}`.",
                "```json\n"
                + json.dumps(
                    {
                        "constraints": example["constraints"],
                        "modelValues": example["modelValues"],
                    },
                    indent=2,
                    ensure_ascii=True,
                )
                + "\n```",
            ]
        )
    source = stats["source_context"]
    sections.extend(
        [
            "### What this first phase supports",
            "The inventories and example rows identify material that can be packaged for a later isolated generation experiment. Prefer a small spread of simpler signatures, null hypotheses and richer fixtures rather than taking the most frequent exception alone. Keep unavailable or complex preparations as explicit outcomes. Actual generation success, compilation, execution, scenario reproduction and assertion quality remain unmeasured.",
            "## Limited WIT-UP source context",
            f"Inspected checkout: `{source['witup'].get('commit', 'unavailable')}`. Commons IO checkout metadata: `{source['commons_io'].get('commit', 'unavailable')}`. The WIT-UP revision that produced the supplied files is unknown; this checkout is an interpretation aid, not confirmed producer provenance.",
            "Reading the export boundary was useful for the join key, grouped summaries, condition truth flags, and solver labels. Counts and the candidate inventory come from the supplied JSON files. This was a format interpretation, not a correctness review of either Java project.",
            "- [Driver.java](../core/src/main/java/br/unb/cic/witup/Driver.java): result fields, path identifiers, summary status lookup, and output filenames.",
            "- [SummaryRowBuilder.java](../core/src/main/java/br/unb/cic/witup/SummaryRowBuilder.java): grouping key, first path identifier, provenance alternatives, and condition conjunction.",
            "- [SolverStatus.java](../core/src/main/java/br/unb/cic/witup/solver/SolverStatus.java): SAT, UNSAT, UNKNOWN, and MAYBE labels.",
            "- [SymbolicConstraintSolver.java](../core/src/main/java/br/unb/cic/witup/solver/SymbolicConstraintSolver.java): solver verdict conversion and incomplete/failed task handling.",
            "## Reproduction and derived artifacts",
            "```powershell\nuv sync --locked\nuv run --locked witup-analysis analyze\nuv run --locked ruff check src\nuv run --locked ruff format --check src\n```",
            "The command reads the existing exports and recreates the derived tables and this report. Explicit input paths are available through `--results` and `--summaries`; use `uv run --locked witup-analysis analyze --help` for options.",
            "- `data/processed/commons-io.duckdb`: results, summaries, joined, candidate_features, and candidates tables.\n- `data/processed/results.parquet`, `summaries.parquet`, `candidates.parquet`: reusable derived datasets.\n- `data/processed/statistics.json`: complete measured inventories and selected examples.",
            f"Runtime versions: Python `{stats['environment']['python']}`, DuckDB `{stats['environment']['duckdb']}`, ijson `{stats['environment']['ijson']}`. Dependency resolution is recorded in `uv.lock`.",
        ]
    )
    write_report_bundle(sections, path)


def write_report_bundle(sections: list[str], path: Path) -> None:
    """Keep the original report path as an overview, with four focused findings pages."""
    starts = [
        next(
            index
            for index, text in enumerate(sections)
            if text.startswith(f"## {number}.")
        )
        for number in range(1, 5)
    ]
    context_start = sections.index("## Limited WIT-UP source context")
    example_start = sections.index("### Examples selected from the simpler tiers")
    conclusion_start = sections.index("### What this first phase supports")
    findings = path.parent / "findings"
    findings.mkdir(parents=True, exist_ok=True)
    files = (
        "json-schema-and-correspondence.md",
        "json-population.md",
        "json-test-information.md",
        "json-candidate-tiers.md",
    )
    links = []
    for number, (start, filename) in enumerate(
        zip(starts, files, strict=True), start=1
    ):
        end = starts[number] if number < 4 else context_start
        content = sections[start:end]
        if number == 4:
            content = (
                sections[start:example_start]
                + [
                    "[Initial illustrative examples](json-candidate-examples.md) are kept separately from the later 20-case inspection sample."
                ]
                + sections[conclusion_start:context_start]
            )
        title = content[0].replace("## ", "# ", 1)
        content = [
            title,
            "[Documentation index](../README.md) | [JSON analysis overview](../"
            + path.name
            + ")",
            *content[1:],
        ]
        (findings / filename).write_text("\n\n".join(content) + "\n", encoding="utf-8")
        links.append(f"- [{sections[start][3:]}](findings/{filename})")
    example_content = [
        "# Initial illustrative candidate examples",
        "[Documentation index](../README.md) | [Candidate tiers](json-candidate-tiers.md)",
        *sections[example_start + 1 : conclusion_start],
    ]
    (findings / "json-candidate-examples.md").write_text(
        "\n\n".join(example_content) + "\n", encoding="utf-8"
    )
    overview = (
        sections[: starts[0]]
        + [
            "## Answers to the four questions",
            "\n".join(links),
            "See the [20-case findings](findings/case-assessment.md) and [methodology](methodology/study-scope.md) for the subsequent inspection phase.",
        ]
        + sections[context_start:]
    )
    path.write_text("\n\n".join(overview) + "\n", encoding="utf-8")
