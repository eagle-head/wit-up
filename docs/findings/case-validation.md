# Case validation record

[Documentation index](../README.md)

Completed at `2026-10-08T23:30:45.651422+00:00` using `uv run --locked witup-analysis validate-cases`.

## Completed data and documentation checks

| Check | Observed result |
| --- | --- |
| selected_cases | 20 |
| distinct_methods | 20 |
| original_records_and_array_locators_checked | 40 |
| input_byte_identities_checked | 2 |
| analysis_code_and_lock_identities_checked | 5 |
| selection_pool_rows | 221 |
| reversed_pool_replay_matches | True |
| markdown_documents_checked | 35 |
| local_links_checked | 123 |
| recognized_conditions | 18 |
| recognized_condition_disagreements | 0 |
| unsupported_conditions | 0 |

The command rejects changed source inputs, mismatched parsed records or array locators, changed recorded rule/lock files, changed selection-frame membership, non-reproducible selection, duplicate method observations, incorrect total quotas, and broken local documentation links. Recognized-condition disagreements are measured observations, not silently removed cases.

## Software checks

Five focused Python behavioral checks cover input-order independence and class diversity, quota failure, false-truth null interpretation, retained temporary-symbol ambiguity, and preserved condition/model disagreement. They are checks of the analysis software, not JUnit tests or evidence of Java reachability.

```powershell
uv run --locked ruff check src tests
uv run --locked ruff format --check src tests
uv run --locked python -m unittest discover -s tests -v
uv lock --check
```

## Interpretation boundary

Byte identity proves which input bytes were inspected. Replay and source-record checks support traceability and pipeline operation. Predicate agreement covers only recognized null/integer comparisons. None establishes a complete fixture, runtime behavior, intended public contract, test-generation success, or scientific representativeness.
