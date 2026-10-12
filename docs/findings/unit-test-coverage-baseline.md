<!--
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements. See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Unit-test coverage baseline

[Documentation index](../README.md) | [Study log](../study-log.md)

The October 9 baseline below concerns the selected target,
`org.apache.commons.io.input.buffer.PeekableInputStream`. A separate October 11
comparison uses the corrected production baseline shared by the generation trials.
The original selection document remains archived; current reporting is limited
to the target class. Later measurements do not recover deleted original files.

## Measurement

Measured on October 9, 2026, on branch `test/reference-suite`, with production
and test source unchanged from commit
`11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`. Build configuration already included
the prepared JaCoCo and JVM argument changes.

The existing suite ran successfully with Temurin `8.0.504+1`, Maven `3.9.16`,
JUnit Jupiter `5.5.2`, Surefire `2.22.2`, and JaCoCo `0.8.14` on Windows.
There was no dedicated target test. Coverage was collected in a fresh
"target/coverage/unit-tests.exec" file, separate from earlier integration checks.

| Selected target | Covered lines | Line coverage | Covered branches | Branch coverage |
| --- | ---: | ---: | ---: | ---: |
| [PeekableInputStream.java](../../commons-io/src/main/java/org/apache/commons/io/input/buffer/PeekableInputStream.java) | 0/16 | 0.00% | 0/8 | 0.00% |

Both constructors and both declared `peek` overloads had no recorded coverage.
The existing tests therefore supplied no measured indirect coverage of the
target. Its small size, uncovered behavior, argument checks, and refill behavior
motivated its selection for the reference suite.

## WIT-UP context for the target

The derived summaries contain 100 target paths, three method signatures, and
31 SAT summary paths. The query matched the fully qualified declaring class
in `pathId` in "data/processed/commons-io.duckdb". SAT counts describe encoded
models, not confirmed Java execution or coverage.

## Historical reproduction and artifact availability

The original measurement command, executed inside
"D:/Projects/wit-up/commons-io", was:

```powershell
mise exec -- mvn --batch-mode --no-transfer-progress -Pjacoco "-Djacoco.destFile=target/coverage/unit-tests.exec" "-Djacoco.dataFile=target/coverage/unit-tests.exec" test org.jacoco:jacoco-maven-plugin:0.8.14:report
```

A later clean build removed the original execution data, report, log, and
summary script. The original target HTML location was
"target/site/jacoco/org.apache.commons.io.input.buffer/PeekableInputStream.html";
the copied XML location was "target/coverage/unit-tests-jacoco.xml".
These are historical locators, not currently available files. The
[archived selection document](../../data/experiments/peekable-input-stream/reference-suite/coverage/assessment-before-coverage.md)
preserves the complete earlier procedure and inventory. The new comparison
below has its own retained evidence and does not replace the original run.

Coverage indicates execution, not assertion strength. The reference-suite
phase assessed behavioral scenarios and mutation sensitivity separately.

## Reconstructed reference-suite coverage comparison

Coverage and test-result comparisons refer exclusively to
`org.apache.commons.io.input.buffer.PeekableInputStream` and its dedicated
test class. Before means the target test file was absent; recorded target
coverage was zero, including any possible execution by existing tests.
Complete original execution artifacts remain archived unchanged.

Measured on October 11, 2026, at the user's request to supplement every test-suite
assessment with before/after coverage. The [earlier document](../../data/experiments/peekable-input-stream/reference-suite/coverage/assessment-before-coverage.md)
is preserved. This comparison uses corrected production at
`d7a3c884d07ff5f1829b09087f34dcb8043f0f64`, the common generation baseline.
It is separate from the historical October 9 baseline on `11f0abe7a`; none of
the original measurements above were replaced.

Before contained the existing repository suite without the target test. After
added the exact reference test blob from
`256fa0d0e19247ce41a084125a57fbd487029704`. Git comparison confirmed that this
file is the only difference between those two committed trees. Its SHA-256 is
`5E6C3A6E1319CBB82F7A845EDF4D5ABF06EA1AEF4D61F7C61179372B03AD0745`.
No tests, assertions, fixtures, production, or configuration were edited.

Both runs used the detached checkout
"D:/Projects/wit-up/.worktrees/commons-io-coverage", Temurin `1.8.0_504`, Maven
`3.9.16`, JUnit Jupiter `5.5.2`, Surefire `2.22.2`, and JaCoCo `0.8.14`:

```powershell
mvn -B -Pjacoco "-Djacoco.skip=false" clean verify jacoco:report
```

Each run began with fresh execution data. The before artifacts were archived
before the after clean build. All 398 common files under "src" and all compiled
production outputs were byte-identical. No coverage filters or test exclusions
were added. Existing case identities and outcomes were unchanged; exactly
34 passing reference cases were added.

| State | Target cases | Passed | Failures | Errors | Skipped | Build exit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Before: target test absent | 0 | 0 | 0 | 0 | 0 | 0 |
| After | 34 | 34 | 0 | 0 | 0 | 0 |

| Target counter | Before | After | Added covered units | Change |
| --- | ---: | ---: | ---: | ---: |
| Lines | 0/16 (0.00%) | 16/16 (100.00%) | 16 | +100.00 pp |
| Branches | 0/8 (0.00%) | 8/8 (100.00%) | 8 | +100.00 pp |
| Instructions | 0/98 (0.00%) | 98/98 (100.00%) | 98 | +100.00 pp |
| Methods, including constructors | 0/4 (0.00%) | 4/4 (100.00%) | 4 | +100.00 pp |

Percentages divide covered units by their totals; pp denotes percentage points.
The 34 passing cases and full target coverage reproduce the recorded reference
values in a new execution. **They do not recover the original deleted artifacts.**
The historical 14/14 mutation result was not remeasured. Branch coverage does
not enumerate exception paths, and full coverage alone does not establish
oracle quality or the absence of defects.

The [target-only comparison](../../data/experiments/peekable-input-stream/target-coverage/comparison.json)
records target counters and outcomes. One measurement pair does not establish
repeated-run stability or mutation adequacy.

Both builds returned exit code 0; inherited coverage checks still emitted
warnings. Build success does not establish that all coverage requirements passed.
Build configuration and thresholds were unchanged. Complete original logs
preserve all diagnostics; no warning or failure was suppressed.

To reproduce, use the recorded corrected baseline without the target test,
run the command, and archive all artifacts before cleaning. Restore the exact
reference blob, verify its hash, and repeat. Compare source/class bytes and
test identities before interpreting the delta. This later procedure does not
recreate the earlier target-selection ranking or original production revision.

- [Before target HTML](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/jacoco/org.apache.commons.io.input.buffer/PeekableInputStream.html), [raw XML](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/jacoco/jacoco.xml), and [raw CSV](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/jacoco/jacoco.csv).
- [After target HTML](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/jacoco/org.apache.commons.io.input.buffer/PeekableInputStream.html), [raw XML](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/jacoco/jacoco.xml), and [raw CSV](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/jacoco/jacoco.csv).
- Full logs: [before](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/maven.log) and [after](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/maven.log).
- Metadata and timestamps: [before](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/run.json) and [after](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/run.json).
- [Target test outcomes after](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/surefire-reports/TEST-org.apache.commons.io.input.buffer.PeekableInputStreamTest.xml); the target test file was absent before.
- [Unchanged reference source](../../data/experiments/peekable-input-stream/reference-suite/coverage/PeekableInputStreamTest.java) and [artifact inventory](../../data/experiments/peekable-input-stream/reference-suite/coverage/artifact-manifest.json).

Each run additionally retains "jacoco.exec", every Surefire report, environment
output, source and compiled-output hash manifests, and compiled production ZIPs
outside the checkout. Raw Maven logs retain their original Windows encoding.
The active generation branch and its test file were not used for these builds.
