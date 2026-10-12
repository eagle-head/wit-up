"""Verify record traceability, selection replay, and documentation links."""

import json
import re
from datetime import UTC, datetime
from pathlib import Path

import duckdb

from witup_analysis.analysis import records
from witup_analysis.reporting import table
from witup_analysis.selection import original_records, select_cases, sha256


def validate_cases(root: Path) -> dict:
    output = root / "data" / "processed"
    inventory = json.loads((output / "case-inventory.json").read_text(encoding="utf-8"))
    cases = inventory["cases"]
    keys = [
        (case["identity"]["artifact"], case["identity"]["path_id"]) for case in cases
    ]
    if (
        len(keys) != len(set(keys))
        or len(cases) != 2 * inventory["selection_policy"]["per_stratum"]
    ):
        raise ValueError("Selected keys or stratum quotas are invalid")
    signatures = {key[1].rsplit("#", 1)[0] for key in keys}
    if len(signatures) != len(keys):
        raise ValueError("Multiple selected paths refer to the same method signature")
    original_count = 0
    for kind, identity in inventory["inputs"].items():
        path = root / identity["project_relative_path"]
        if (
            path.stat().st_size != identity["bytes"]
            or sha256(path) != identity["sha256"]
        ):
            raise ValueError(f"Input byte identity changed: {path}")
        originals = original_records(path, set(keys))
        field = "original_result" if kind == "results" else "original_summary"
        for case, key in zip(cases, keys, strict=True):
            if (
                originals[key]["record"] != case[field]
                or originals[key]["array_record_number"]
                != case["source_records"][kind]["array_record_number"]
            ):
                raise ValueError(
                    f"Original record or array locator differs: {kind}, {key}"
                )
            original_count += 1
    for relative, expected in inventory["analysis_code"].items():
        if sha256(root / relative) != expected:
            raise ValueError(
                f"Recorded analysis code or lockfile changed: {relative}; regenerate the inventory"
            )
    connection = duckdb.connect(str(output / "commons-io.duckdb"), read_only=True)
    try:
        pool = records(
            connection,
            """SELECT * FROM candidates WHERE tier IN
            ('simple_signature_hypothesis','null_argument_hypothesis') ORDER BY artifact,pathId""",
        )
    finally:
        connection.close()
    for row in pool:
        row["modelValues"] = json.loads(row["modelValues"])
    saved_pool = {
        (row["artifact"], row["path_id"], row["stratum"])
        for row in inventory["selection_pool"]
    }
    if saved_pool != {(row["artifact"], row["pathId"], row["tier"]) for row in pool}:
        raise ValueError(
            "The saved selection frame differs from the current derived table"
        )
    replay = select_cases(
        list(reversed(pool)), inventory["selection_policy"]["per_stratum"]
    )
    replay_keys = [
        (item["candidate"]["artifact"], item["candidate"]["pathId"]) for item in replay
    ]
    if replay_keys != keys:
        raise ValueError("Selection replay differs from the saved case order")
    validation_path = root / "docs" / "findings" / "case-validation.md"
    validation_path.write_text(
        "# Case validation record\n\n[Documentation index](../README.md)\n",
        encoding="utf-8",
    )
    documents = [root / "README.md", *sorted((root / "docs").rglob("*.md"))]
    checked_links = 0
    for document in documents:
        for link in re.findall(
            r"\[[^\]]*\]\(([^\)]+)\)", document.read_text(encoding="utf-8")
        ):
            if re.match(r"[a-zA-Z]+://", link) or link.startswith("#"):
                continue
            target = link.split("#", 1)[0]
            if target and not (document.parent / target).resolve().is_file():
                raise ValueError(f"Broken local documentation link: {document}, {link}")
            checked_links += 1
    recognized = [
        item
        for case in cases
        for item in case["assessment"]["null_conditions"]
        + case["assessment"]["numeric_conditions"]
    ]
    result = {
        "validated_at_utc": datetime.now(UTC).isoformat(),
        "selected_cases": len(cases),
        "distinct_methods": len(signatures),
        "original_records_and_array_locators_checked": original_count,
        "input_byte_identities_checked": len(inventory["inputs"]),
        "analysis_code_and_lock_identities_checked": len(inventory["analysis_code"]),
        "selection_pool_rows": len(pool),
        "reversed_pool_replay_matches": True,
        "markdown_documents_checked": len(documents),
        "local_links_checked": checked_links,
        "recognized_conditions": len(recognized),
        "recognized_condition_disagreements": sum(
            item["model_agrees"] is False for item in recognized
        ),
        "unsupported_conditions": sum(
            "condition_syntax_outside_assessment_subset" in case["assessment"]["gaps"]
            for case in cases
        ),
    }
    content = [
        "# Case validation record",
        "[Documentation index](../README.md)",
        f"Completed at `{result['validated_at_utc']}` using `uv run --locked witup-analysis validate-cases`.",
        "## Completed data and documentation checks",
        table(
            ["Check", "Observed result"],
            [
                [name, value]
                for name, value in result.items()
                if name != "validated_at_utc"
            ],
        ),
        "The command rejects changed source inputs, mismatched parsed records or array locators, changed recorded rule/lock files, changed selection-frame membership, non-reproducible selection, duplicate method observations, incorrect total quotas, and broken local documentation links. Recognized-condition disagreements are measured observations, not silently removed cases.",
        "## Software checks",
        "Five focused Python behavioral checks cover input-order independence and class diversity, quota failure, false-truth null interpretation, retained temporary-symbol ambiguity, and preserved condition/model disagreement. They are checks of the analysis software, not JUnit tests or evidence of Java reachability.",
        "```powershell\nuv run --locked ruff check src tests\nuv run --locked ruff format --check src tests\nuv run --locked python -m unittest discover -s tests -v\nuv lock --check\n```",
        "## Interpretation boundary",
        "Byte identity proves which input bytes were inspected. Replay and source-record checks support traceability and pipeline operation. Predicate agreement covers only recognized null/integer comparisons. None establishes a complete fixture, runtime behavior, intended public contract, test-generation success, or scientific representativeness.",
    ]
    validation_path.write_text("\n\n".join(content) + "\n", encoding="utf-8")
    (output / "case-validation.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2), flush=True)
    return result
