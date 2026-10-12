# WIT-UP study workspace

The previous study's documentation, prompts, supplied JSON exports, derived data,
and execution artifacts are archived in [legacy](legacy/README.md). The
[archived documentation index](legacy/docs/README.md) describes those historical
results. Historical absolute paths and manifests retain their original meaning;
the [relocation manifest](legacy/archive-manifest.json) maps archived file paths.
The entire legacy directory is ignored by Git and retained locally. Previously
versioned reports and evidence remain available in Git history.

The unchanged reference test suite is retained in
[reference-suite](reference-suite/README.md).

The separate Commons IO checkout is restored to original commit
`11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`, with a detached HEAD. Its previous
branches remain available in its Git history.

The Python analysis source, tests, dependency declarations, and lockfile remain
in this workspace. The completed JSON-only PeekableInputStream generation and
its measured JaCoCo/PIT before-and-after results are documented in the
[validation report](commons-io-validation/peekable-input-stream/runs/json/001/evidence/peekable-input-stream-report.md).
The [frozen Java test](commons-io-validation/peekable-input-stream/runs/json/001/evidence/test-source/PeekableInputStreamTest.java)
and native measurement evidence accompany that report. Pipeline diagnostics are
preserved separately and excluded from the generated suite's outcome counts.

Follow the [run preservation methodology](docs/run-methodology.md) and local
[agent instructions](AGENTS.md) for every new attempt. The
[run registry](commons-io-validation/peekable-input-stream/README.md) identifies
preserved attempts and linked supplements. Each independent generation reserves a
unique directory and checkout, preserves its exact inputs, freezes any generated
test, records each execution, and seals an explicit outcome. Verified backups live
outside the repository. Later measurements and corrections are linked supplements
that retain the original generation and do not add independent samples.

Prospective evaluations follow the versioned
[paired measurement protocol](docs/measurement-protocol.md). Their before/after
selection keeps the same existing suite and adds only the frozen test afterward.
The historical imported measurements retain their original, separately described
scope. A generation-complete seal does not imply that measurements are complete.

Two independent exception-test generation prompts target the original commit:

- [JSON-only prompt](docs/prompts/exception-test-generation-json.txt), using only
  the two original raw exports retained under `legacy/commons-io-analysis-results`.
- [Java-source-only prompt](docs/prompts/exception-test-generation-source.txt),
  using the target source and necessary production callees at the same commit.

Use each prompt in a fresh chat with a separately prepared attempt: the required
HEAD, unchanged tracked baseline, and absent target test. Preserve each attempt
before preparing the next; preparation must not destroy prior results or expose
them to the next generator. Use the same Java/Maven toolchain and check build
readiness before generation. The archived checkout-preparation procedure may
inform that separate preparation, but is not a generator scenario source.

Both prompts restrict generation to exceptions from the target's constructors
and declared `peek` overloads, prohibit production changes and prior test reuse,
and freeze the generated tests before execution feedback can influence them.
The original export label identifies `11f0abe7a`; it does not independently prove
the analyzed JAR's bytes or the WIT-UP producer revision. The preserved reference
suite belongs to the earlier corrected-production study and is not an input or
a validated gold standard for this new baseline.
