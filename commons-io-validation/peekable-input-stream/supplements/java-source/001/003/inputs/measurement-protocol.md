# Paired measurement protocol

This is the canonical prospective `paired-full-suite` configuration in
[measurement-plan.json](measurement-plan.json). It is a new comparison stratum:
the historical imported measurement used different suite selections and must not
be pooled with this configuration. The recipe contains no observed target results.

Run measurements only in an authorized evaluation supplement. Freeze the plan,
authorization note, environment, and rendered commands before executing any phase.
Use two checkouts at the recorded baseline: a clean before checkout under the
evaluation's assigned working directory, and the evaluation checkout containing
the exact frozen test. Preserve metadata-only Git checks for both. Existing tests,
dependencies, compiler settings, and production files must match in both checkouts.
Do not modify generated tests in response to any result.

The same full existing suite is selected on both sides. Only the frozen generated
test is added after. A baseline failure makes the pair incomplete; it does not
authorize switching to a narrower passing selection. Never count an infrastructure
failure as an executed-test failure or as a zero measurement.

## Environment and preparation

Use Temurin runtime `1.8.0_504-b01`, javac `1.8.0_504`, Maven `3.9.16`, the unchanged
baseline's Surefire `2.22.2`, and JUnit Jupiter `5.5.2`. Capture actual version
output, executable locations, effective POM, resolved dependencies, OS, and process
environment in the evaluation. Capture an environment JSON before each invocation.
The preservation manager records that observation; it does not infer it from PATH.

Set process-only `JAVA_HOME`, PATH, and D: TEMP/TMP. All paths below are parameters
resolved to this evaluation's assigned directories, never historical run paths.
Keep the declared report and measurement destinations absent or empty before
`begin`. If a previous invocation left reports, first record it, then move those
reports to that invocation's working archive using native PowerShell with verified
absolute paths. Do not erase unrecorded output to satisfy preparation.

Fetch tools into the evaluation's working `tools` directory with these commands
from its checkout; preserve their logs and hashes as preflight records:

```powershell
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.agent:0.8.4:jar:runtime' "-DoutputDirectory=$toolDirectory"
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.cli:0.8.4:jar:nodeps' "-DoutputDirectory=$toolDirectory"
```

Expected SHA-256: agent
`1a7c1dc7280e535b9b6f383915bac5afbb9208c1af2019b4e674ca590c925c22`, CLI
`65de07ff32bcf2f945f18180d1d10cdf0e155eee2b508519bbc5f31904cd8288`.
Reject mismatches. Render and save the four phase scripts before starting. Use the
same recipe for before and after with only checkout and output paths substituted.
Save a table of all substitutions and the complete commands, including environment
assignments; command logs alone are not a substitute for configuration provenance.

## JaCoCo before and after

For each side, assign `$phaseCheckout`, a new `$phaseOutput`, `$agentJar`, and
`$cliJar`. Run this script from `$phaseCheckout`. The reserved execution's
`output.log` must capture the entire script's stdout and stderr. Record the Maven
exit status immediately; record the CLI exit status separately in the log. The
script's exit code is the first failing command, or zero only when both succeed.

```powershell
$ErrorActionPreference = 'Stop'
$executionData = Join-Path $phaseOutput 'jacoco.exec'
$coverageXml = Join-Path $phaseOutput 'jacoco.xml'
if ((Test-Path -LiteralPath $executionData) -or (Test-Path -LiteralPath $coverageXml)) {
    throw 'Measurement output already exists.'
}
New-Item -ItemType Directory -Path $phaseOutput -Force | Out-Null
$env:MAVEN_OPTS = "-DargLine=-javaagent:$agentJar=destfile=$executionData,append=true,includes=org.apache.commons.io.input.buffer.PeekableInputStream"
mvn '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' clean test
$mavenExit = $LASTEXITCODE
Write-Output "Maven exit code: $mavenExit"
if ($mavenExit -ne 0) { exit $mavenExit }
$classFile = Join-Path $phaseCheckout 'target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class'
java -jar $cliJar report $executionData --classfiles $classFile --xml $coverageXml --name 'PeekableInputStream paired measurement'
$reportExit = $LASTEXITCODE
Write-Output "JaCoCo report exit code: $reportExit"
exit $reportExit
```

`append=true` combines forks within this one invocation only; every phase starts
with an absent execution file. Register its native Surefire directory with `begin`.
Declare artifact roles `production-class`, `jacoco-xml`, and `jacoco-exec`. Their
paths are snapshotted when recording the execution. Preserve the full-suite XML
ZIP including genuine failures and existing intrinsic skips.

## PIT before and after

Use [pit-analysis-pom.xml](pit-analysis-pom.xml), copied into the evaluation inputs.
Both sides use that identical POM and the compiled outputs from their own preceding
JaCoCo build. Its source and test-source directories point to the assigned
checkout's actual `src/main/java` and `src/test/java`. PIT checks source discovery
before using compiled outputs; empty auxiliary source directories cause a skipped
analysis even when its Maven process exits zero. Require native mutation and line
coverage XML to establish that analysis occurred. Configuration revision 2 fixes
that discovery without changing test selection or mutators. Preserve any earlier
skipped analysis as an incomplete evaluation rather than reporting zero metrics.
The POM has no compilation or test execution lifecycle shortcuts;
PIT performs its unmutated-test baseline normally. Select every existing project
test using `org.apache.commons.io.*` on both sides. Do not add failure suppressions,
excluded tests, alternate selectors, or changed thresholds.

Set `$analysisPom`, `$phaseCheckout`, `$phaseOutput`, `$phaseBuild`, and
`$temporaryDirectory` to the recorded per-evaluation paths. Reserve an execution
with no Surefire directory: PIT does not produce Surefire reports for its mutation
execution. Declare `production-class`, `pit-mutations`, and `pit-linecoverage`
artifact roles. The class file already exists from the corresponding JaCoCo phase.

```powershell
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp -f $analysisPom "-Danalysis.checkout=$phaseCheckout" "-Danalysis.output=$phaseOutput" "-Danalysis.build=$phaseBuild" "-Danalysis.temp=$temporaryDirectory" org.pitest:pitest-maven:1.15.2:mutationCoverage
$pitExit = $LASTEXITCODE
Write-Output "PIT exit code: $pitExit"
exit $pitExit
```

Never execute the after JaCoCo clean build before recording all artifacts needed
by that side. A clean before checkout stays separate from the after checkout.
The evaluator verifies both source inventories and target class hashes, plus the
mutant identity tuples (class, method, descriptor, line, mutator, indexes, blocks).
The manager checks target class and mutant equality at evaluation completion.

## Reporting and acceptance

Record all commands and failures, even if no metrics were emitted. An authorized
retry is a new linked evaluation; preserve the unsuccessful pair as incomplete.
Generation counts remain unchanged. No baseline is inferred from absent tests.

Report JaCoCo covered/missed/total counters for the target class separately from
PIT's line counters. Report the complete PIT status histogram, mutation score
`KILLED / total mutants`, and test strength `KILLED / (KILLED + SURVIVED)`. A zero
denominator is not applicable, not 100%. Unexpected mutation statuses prevent a
complete comparable pair and remain visible. Keep unique test counts separate
from PIT's cumulative executions. Coverage and mutation scores are observations,
not evidence that the suite is a complete specification.

Completion requires all four successful phases, unchanged frozen Java, native
artifacts, comparable class bytes and mutant sets, and a Markdown report with the
full Java source and exact before/after counts. Otherwise close as `incomplete`
with a reason. This recipe has been structurally validated; a future real
execution must establish its own runtime result. No new Commons IO measurement
was performed while implementing the preservation protocol.
