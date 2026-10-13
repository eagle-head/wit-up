# WIT-UP exception-test generation study

This study investigates whether WIT-UP JSON exports provide sufficient information
to generate effective Java exception tests without giving the generator production
source code. When the exported information falls short, the study identifies what
is missing, how that information could be improved, and how to measure the effects
of those improvements.

The current pilot compares independent JSON-only and Java-source generations for
Apache Commons IO's `org.apache.commons.io.input.buffer.PeekableInputStream` at
commit `11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`. The generated tests were
preserved unchanged and evaluated with the same paired full-suite measurement
protocol.

## Reports

- **[Read the consolidated report in English](commons-io-validation/peekable-input-stream/reports/exception-test-generation-comparison.md)**
- **[Read the consolidated report in Brazilian Portuguese](commons-io-validation/peekable-input-stream/reports/exception-test-generation-comparison.pt-BR.md)**

Both reports contain the complete frozen Java tests, measured before-and-after
JaCoCo and PIT results, exact tool and dependency versions, commands, and supporting
evidence. They prioritize the information missing from the JSON, proposed
improvements, and controlled comparisons for measuring their effects.

## Pilot findings

| Observation | WIT-UP JSON | Java source |
| --- | --- | --- |
| Passing generated cases | 10 | 20 |
| Target JaCoCo line coverage after generation | 11/16 (68.75%) | 11/16 (68.75%) |
| Target JaCoCo branch coverage after generation | 7/8 (87.50%) | 8/8 (100.00%) |
| PIT mutants detected after generation | 1/14 (7.14%) | 7/14 (50.00%) |

JSON supported generation of 10 passing exception tests without consulting
production source. The resulting suite detected fewer mutants than the
Java-source suite in this pair. This demonstrates feasibility with specific gaps;
it does not establish that source code is indispensable. There is one independent
generation per condition, so the results characterize this pilot rather than
general effectiveness or repeatability.

The main JSON improvement priorities are supported read-failure scenarios,
executable public setup for symbolic state, and observable details that distinguish
the expected exception's origin. The reports connect each priority to evidence
and proposed effect measurements. Those improvements and new comparisons have
not been executed.

## Evidence and methodology

The [run registry](commons-io-validation/peekable-input-stream/README.md) links
the original generations, evaluations, provenance annotations, and integrity
seals. Native reports and execution diagnostics remain alongside their records.
Infrastructure failures are recorded separately from generated-test outcomes and
do not supply the selected comparison metrics.

Follow the [run preservation methodology](docs/run-methodology.md),
[paired measurement protocol](docs/measurement-protocol.md), and
[repository instructions](AGENTS.md) when preparing or evaluating a generation.
Each independent generation requires its own reserved directory, checkout, fresh
chat, assigned inputs, and frozen test. Later evaluations and corrections link to
the original seal and contribute no additional independent generations.

The [JSON-only](docs/prompts/exception-test-generation-json.txt) and
[Java-source-only](docs/prompts/exception-test-generation-source.txt) files are
preparation templates. The preparer reserves a run and renders its ready-to-use
`inputs/prompt.txt` before handing it to the generator. Earlier tests, alternative
source inputs, and evaluation feedback are outside a generator's permitted inputs.

## Repository contents and local inputs

- [Python analysis source](src/) and [tests](tests/), with dependency declarations
  and the lockfile, support analysis of WIT-UP exports and run preservation.
- [Experimental records and reports](commons-io-validation/peekable-input-stream/)
  preserve the current exception-test study.
- The [reference suite](reference-suite/README.md) belongs to the earlier study
  with corrected production code. It is preserved as historical material and is
  not an input or a validated reference standard for this pilot's baseline.

The earlier study archive under `legacy/`, raw JSON exports, separate Commons IO
checkouts, and verified backups are retained locally outside the published Git
contents. Previously versioned material remains available in Git history.
The [input backup inventory](docs/input-backups.json) records local recovery
locations. The original export label identifies the intended artifact; the
analyzed JAR bytes and producing WIT-UP revision remain unverified, as described
in the reports.
