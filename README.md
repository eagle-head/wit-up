# WIT-UP JSON Analysis

Analyze the existing Commons IO WIT-UP results and summaries to prepare a later,
isolated study of generating JUnit tests. This phase profiles the JSON data and
produces a Markdown report. It does not call an LLM or generate Java tests.

## Setup

The project was initialized with `uv init --app --package`, using the installed
Python 3.13.15 interpreter. uv owns the environment, dependency declarations,
Python pin, package scaffolding, and lockfile.

```powershell
uv sync --locked
uv run --locked witup-analysis analyze
uv run --locked witup-analysis inspect-cases
uv run --locked witup-analysis validate-cases
```

Keep `pyproject.toml`, `.python-version`, and `uv.lock` together. Use `uv add`,
`uv remove`, and `uv lock` to manage dependencies. The root is a packaged Python
application, not a uv workspace containing the two external Java repositories.

## Layout

```text
src/witup_analysis/             Analysis application
docs/README.md                 Documentation index
docs/methodology/              Scope, selection, and assessment procedures
docs/findings/                 Focused JSON and case findings
docs/cases/                    One evidence document per selected case
data/processed/                Derived DuckDB, Parquet, and statistics files
commons-io-analysis-results/    Supplied raw JSON files
core/                          Existing WIT-UP checkout
commons-io/                    Existing target checkout
```

The report answers:

1. What fields exist, and how do the files relate?
2. How many methods, paths, exception types, and solver verdicts appear?
3. What information supports arranging inputs and writing assertions?
4. Which rows are simpler candidates for an initial experiment?

The raw filenames and Java identifiers are preserved as external values. The
program checks join-key uniqueness, metadata and verdict correspondence, and
independent parser row counts. Preparation labels are documented heuristics;
they do not establish Java reachability or LLM feasibility.

The follow-up command selects 10 cases from each simpler stratum using a
deterministic diversity rule and inspects their original parsed records. It
retains input byte identities, array locators, selection reasons, hypotheses,
and information gaps in `data/processed/case-inventory.json`. See the
[documentation index](docs/README.md) and [study log](docs/study-log.md) for the
methodology actually applied. The sample is exploratory and not representative.

## Explore the derived data

JupyterLab is an optional dependency group, separate from the analysis runtime:

```powershell
uv run --locked --group notebooks jupyter lab
```

Within a notebook, read the derived database without rebuilding the pipeline:

```python
import duckdb

connection = duckdb.connect("data/processed/commons-io.duckdb", read_only=True)
connection.sql("SELECT tier, count(*) FROM candidates GROUP BY tier").show()
connection.close()
```

## Checks

```powershell
uv run --locked ruff check src tests
uv run --locked ruff format --check src tests
uv run --locked python -m unittest discover -s tests -v
uv lock --check
```

The local uv cache and project environment are on different drives, so uv may
report that it copies package files instead of hardlinking them. The analysis
environment and all project outputs are on D:.

The limited WIT-UP source consultation concerns its JSON export format. Its
current checkout is not assumed to be the version that produced the inputs.
The analysis has no dependency on building either Java project.

## Git storage

Version the analysis code, dependency files, documentation, prompts, and selected
textual experiment evidence. Keep supplied raw exports, separate Java checkouts,
derived datasets, caches, rendered coverage reports, and binary measurement
archives outside this Git repository. The complete original experiment archive
remains local; ignoring a file does not back it up or delete it.

See the [repository storage policy](docs/methodology/repository-storage.md) for
the exact selection, preserved diagnostic evidence, and restoration requirements
after a clone.

Before an independent Java test-generation attempt, follow the
[checkout preparation procedure](docs/methodology/generation-checkout-preparation.md).
Keep Python tool caches in this root project and validate the Java license gate
before opening the generation chat.
