# Study documentation

This documentation records an exploratory analysis of existing WIT-UP exports for
Commons IO commit `11f0abe7a`. It supports reconstructing the work for later
reports or an article. The documentation is written in United States English;
external JSON fields, filenames, Java signatures, and serialized values retain
their original spelling.

## Reading order

1. [Study scope](methodology/study-scope.md): questions, units, evidence boundaries,
   and methodological limitations.
2. [JSON analysis method](methodology/json-analysis.md): input processing and
   checks used for the complete inventory.
3. [Case selection method](methodology/case-selection.md): the fixed 10 + 10
   purposive selection policy and its limitations.
4. [Case assessment rubric](methodology/case-assessment.md): explicit data,
   assignment hypotheses, setup gaps, and classification review.
5. [JSON analysis overview](commons-io-json-analysis.md): links to four focused
   findings documents.
6. [Case assessment findings](findings/case-assessment.md): measured sample
   composition, interpretations, and links to the 20 case records.
7. [Study log](study-log.md): what was actually done, decisions, corrections,
   and checks.
8. [Target coverage baseline](findings/unit-test-coverage-baseline.md):
   initial `PeekableInputStream` coverage and reconstructed before/after
   reference-suite coverage.
9. [Source-only generation assessment](findings/peekable-input-stream-generation.md):
   the first independent generated suite, before/after JaCoCo coverage alongside
   the preserved test failures, and complete code.
10. [JSON-based generation assessment](findings/peekable-input-stream-json-generation.md):
    exception-record associations, fixture variants, before/after JaCoCo coverage,
    execution results, and complete code.
11. [Exception-only Java-source generation assessment](findings/peekable-input-stream-source-exception-generation.md):
    the revised source trial, exception fixtures, before/after JaCoCo coverage,
    validation limits, and complete code.
12. [Exception-only JSON generation assessment](findings/peekable-input-stream-json-exception-generation.md):
    the paired JSON trial, original build blocker, later target execution and
    before/after JaCoCo coverage, source associations, and complete code.

All coverage and test-result comparisons for the generation and reference
suites report only `org.apache.commons.io.input.buffer.PeekableInputStream`
and its dedicated test class. Use the
[target-only comparison](../data/experiments/peekable-input-stream/target-coverage/comparison.json)
for current metrics. Complete original logs and reports remain archived as
execution evidence; project totals and other-class metrics are outside this
reporting scope. This rule applies to future assessments as well.

## Generation prompts

The new exception-focused pair consists of the
[Java-source prompt](prompts/exception-test-generation-source.txt) and the
[JSON-source prompt](prompts/exception-test-generation-json.txt). Their text is
identical outside the marked scenario-source block. Both require a fresh chat
and a prepared checkout that passes the preconditions in the prompt. The
[Java-source trial](findings/peekable-input-stream-source-exception-generation.md)
and the [matching JSON trial](findings/peekable-input-stream-json-exception-generation.md)
have both been assessed. The JSON report distinguishes its original precompilation
build failure from its later successful isolated coverage execution.

The earlier [source-only prompt](prompts/unit-test-generation.txt) and
[JSON prompt](prompts/unit-test-generation-json.txt) remain unchanged as records
of the completed exploratory trials.

Use the [checkout preparation procedure](methodology/generation-checkout-preparation.md)
before a future independent trial. It validates build readiness without changing
the preserved generation prompts or adding behavioral input to the generator.

## Organization and maintenance

Keep protocol and definitions in `methodology/`, aggregate observations in
`findings/`, and original-record evidence plus case-specific interpretations in
`cases/`. The overview remains a navigation document. Add a new study-log entry
when the inputs, selection rule, assessment rule, or study scope changes.

The machine-readable `data/processed/case-inventory.json` contains the selection
pool, input identities, selection policy, original parsed records, source array
locators, and assessments. The raw inputs and generated datasets remain local;
preserve them alongside the documentation when preparing a research package.

The [repository storage policy](methodology/repository-storage.md) defines which
evidence belongs in Git. JaCoCo HTML, binary execution data, compiled ZIPs, and
non-target reports remain in the complete local archive. Their local links require
that archive after a clone; versioned XML/CSV, logs, target reports, and comparisons
remain available to inspect the study's results.

## Reproduce the current phase

```powershell
uv sync --locked
uv run --locked witup-analysis analyze
uv run --locked witup-analysis inspect-cases
uv run --locked witup-analysis validate-cases
```

The analyze command builds the full JSON inventory. The inspect-cases command selects and assesses
20 records using the existing inventory and verifies their original JSON
contents. Neither command builds the Java repositories or generates tests.

```powershell
uv run --locked ruff check src tests
uv run --locked ruff format --check src tests
uv run --locked python -m unittest discover -s tests -v
uv lock --check
```

Software checks support the operation of the analysis pipeline. They do not prove
the meaning of every symbolic expression or the feasibility of a generated test.
