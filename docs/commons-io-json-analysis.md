# Commons IO WIT-UP JSON analysis

## Scope and method

This report answers four questions using the two supplied JSON exports. It inventories data relevant to a later, isolated study of generating JUnit tests. No test-generation model/API was invoked by the pipeline, no JUnit tests were generated or executed, and neither Java project was changed or reviewed for correctness.

Generated at `2026-10-08T22:59:06.025682+00:00`. Every record was read with ijson; DuckDB independently loaded the original arrays and its row counts were checked against the streaming counts. Derived tables preserve raw model strings and nested conditions. Candidate labels are explicit syntactic heuristics, not measurements of Java reachability or LLM effectiveness.

| Input | File | Bytes | Records |
| --- | --- | --- | --- |
| results | `witup-results-commons-io-11f0abe7a.json` | 61,463,191 | 88,303 |
| summaries | `witup-summaries-commons-io-11f0abe7a.json` | 252,491,337 | 72,419 |

The input filenames, Java signatures, exception names, and JSON field names are preserved as external values. Artifact labels associate these exports with Commons IO commit `11f0abe7a`; they do not independently prove which bytes were analyzed. No analyzed JAR or failures export was supplied.

## Answers to the four questions

- [1. What fields exist, and how do the files relate?](findings/json-schema-and-correspondence.md)
- [2. How many methods, paths, exception types, and solver verdicts appear?](findings/json-population.md)
- [3. What information supports arranging inputs and writing assertions?](findings/json-test-information.md)
- [4. Which rows are simpler candidates for an initial experiment?](findings/json-candidate-tiers.md)

See the [20-case findings](findings/case-assessment.md) and [methodology](methodology/study-scope.md) for the subsequent inspection phase.

## Limited WIT-UP source context

Inspected checkout: `646aec8f47cb5ed2b604ee38cacb44095ce89259`. Commons IO checkout metadata: `11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`. The WIT-UP revision that produced the supplied files is unknown; this checkout is an interpretation aid, not confirmed producer provenance.

Reading the export boundary was useful for the join key, grouped summaries, condition truth flags, and solver labels. Counts and the candidate inventory come from the supplied JSON files. This was a format interpretation, not a correctness review of either Java project.

- [Driver.java](../core/src/main/java/br/unb/cic/witup/Driver.java): result fields, path identifiers, summary status lookup, and output filenames.

- [SummaryRowBuilder.java](../core/src/main/java/br/unb/cic/witup/SummaryRowBuilder.java): grouping key, first path identifier, provenance alternatives, and condition conjunction.

- [SolverStatus.java](../core/src/main/java/br/unb/cic/witup/solver/SolverStatus.java): SAT, UNSAT, UNKNOWN, and MAYBE labels.

- [SymbolicConstraintSolver.java](../core/src/main/java/br/unb/cic/witup/solver/SymbolicConstraintSolver.java): solver verdict conversion and incomplete/failed task handling.

## Reproduction and derived artifacts

```powershell
uv sync --locked
uv run --locked witup-analysis analyze
uv run --locked ruff check src
uv run --locked ruff format --check src
```

The command reads the existing exports and recreates the derived tables and this report. Explicit input paths are available through `--results` and `--summaries`; use `uv run --locked witup-analysis analyze --help` for options.

- `data/processed/commons-io.duckdb`: results, summaries, joined, candidate_features, and candidates tables.
- `data/processed/results.parquet`, `summaries.parquet`, `candidates.parquet`: reusable derived datasets.
- `data/processed/statistics.json`: complete measured inventories and selected examples.

Runtime versions: Python `3.13.15`, DuckDB `1.5.6`, ijson `3.5.1`. Dependency resolution is recorded in `uv.lock`.
