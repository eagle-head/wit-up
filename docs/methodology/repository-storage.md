# Repository storage and experiment evidence

[Documentation index](../README.md) | [Study log](../study-log.md)

## Scope

The Git repository at "D:/Projects/wit-up" owns the Python analysis application,
study documentation, prompts, and selected experiment evidence. The checkouts
in "core" and "commons-io" are separate repositories and remain excluded here.
This policy changes Git selection only; it does not delete or rewrite evidence,
test results, production source, or quality-gate configuration.

## Content to version

| Content | Reason |
| --- | --- |
| "src", "tests", "pyproject.toml", ".python-version", and "uv.lock" | Analysis implementation, its tests, and reproducible dependencies. |
| ".gitignore", "README.md", and "docs" | Repository boundaries, methodology, findings, study history, and the exact generation prompts. |
| Archived generated Java files and earlier report snapshots | Preserve each original attempt and the reference suite without relying on the target checkout's current branch. |
| Comparison, assessment, preparation, and verification JSON | Record target counters, input associations, conditions, and actual outcomes. |
| Original source and artifact hash manifests | Identify captured bytes, including evidence intentionally stored outside Git. |
| Maven and generation logs, environment output, and command metadata | Preserve commands, failures, warnings, toolchain identity, and timestamps. These logs are study evidence rather than disposable application logs. |
| JaCoCo XML and CSV for each before/after run | Retain the original textual counters used to verify the target-class comparison. |
| Dedicated target Surefire XML and text reports | Retain the actual case names, assertions' outcomes, failures, errors, and skips for "PeekableInputStreamTest". |
| Measurement scripts and extracted target JSON records | Retain the measurement procedure and precise source locators. |

Complete raw XML and summary files can contain additional execution data. Current
study comparisons still report only the selected target class. Storage scope and
the denominator of a reported metric are separate decisions.

## Content retained locally outside Git

| Content | Reason and preservation requirement |
| --- | --- |
| ".venv", Python bytecode, ".ruff_cache", and editor state | Installed dependencies or local caches; rebuild them with the declared tools. |
| ".worktrees", "core", and "commons-io" | Temporary or independent checkouts; manage their history in their owning repositories. |
| "commons-io-analysis-results" | Supplied large raw exports. Preserve the input files separately and match their recorded identities before reproducing analysis. |
| "data/processed" | Derived DuckDB, Parquet, and inventory outputs produced by the analysis commands. |
| Experiment JaCoCo HTML and rendering assets | Generated browsing views; the original XML/CSV and current comparisons remain versionable. |
| Experiment "jacoco.exec" files | Binary execution evidence. Keep the captured originals in the local archive; rerunning does not guarantee identical evidence. |
| Experiment "production-classes.zip" files | Compiled-output archives. Preserve them locally with their versioned hash manifests. |
| Non-target Surefire reports and process dumps | Complete execution evidence outside the target reporting scope. Keep the originals locally; Maven logs and captured summaries retain broader execution diagnostics. |

The experiment exclusions in ".gitignore" are scoped to
"data/experiments/peekable-input-stream". They keep the target report exceptions
and JaCoCo XML/CSV explicit. Do not replace them with a blanket exclusion of
"data", all JSON, all XML, or all logs: that would omit the study's supporting
evidence from the repository.

## Preservation and clone behavior

Ignoring an artifact is not a backup. Keep the complete local experiment archive,
including excluded binaries, HTML, and non-target reports, when preparing a
research backup or transfer. Do not alter historical manifests to remove ignored
entries or claim that a new execution recovers an original artifact.

A clone contains the selected textual evidence. It does not contain the supplied
raw exports, external Java checkouts, or excluded archive files. Links to local
JaCoCo HTML and compiled archives become usable only after restoring that local
evidence. Use the versioned XML/CSV and target comparisons to inspect coverage
without the HTML archive. Full artifact-manifest verification requires restoring
every referenced file; absent local-only files are not a successful verification.

Restore the separate Commons IO checkout and its recorded baseline commits, and
the raw input exports, before reproducing a Java measurement or input analysis.
The Python lockfile alone does not supply those inputs.

## Review result on October 12, 2026

The initial Git inventory contained 6,496 untracked files totaling 102,190,865
bytes. None of those files was already tracked in this root repository.

The scoped exclusions remove 6,260 original paths from Git's candidate list:
3,510 HTML/rendering files, 2,730 non-target Surefire reports and dumps, ten binary
execution files, and ten compiled-output ZIPs. All excluded files remain on disk.
The existing 236 retained paths total approximately 16.35 MB; this policy document
adds one further candidate. All code, documentation, prompts, target results,
textual coverage evidence, logs, and manifests remain available for commit.

No staging, commit, push, deletion, test execution, or Commons IO modification
is part of this storage review.
