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

The October 9 baseline and selection findings below are preserved as historical
observations. A separate October 11 reference-suite comparison later in this
document uses the corrected production baseline shared by the generation trials.
Its new artifacts do not replace or recover the deleted original baseline files.

## Measurement

Measured on October 9, 2026, on branch `test/reference-suite`, with production
and test source unchanged from commit
`11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`. Build configuration includes the
previously prepared JaCoCo and JVM argument changes.

The existing Maven Surefire suite completed successfully: **1,541 tests reported,
0 failures, 0 errors, and 6 skipped tests**. The skipped tests remain part of the
record; no test exclusions or coverage filters were added for this measurement.
The run used Temurin `8.0.504+1`, Maven `3.9.16`, JUnit Jupiter `5.5.2`, Surefire
`2.22.2`, and JaCoCo `0.8.14` on Windows.

Coverage was collected in a new "target/coverage/unit-tests.exec" file, separate
from earlier integration checks. JaCoCo reported 161 classes and 148 source files
with executable lines. Project line coverage was 5,430 / 6,087 lines; branch
coverage was 2,511 / 2,910 branches. These counters describe this run and its
platform, including the six skipped tests.

## Ranking and eligibility

Aggregate coverage by Java source file, including its nested classes. Sort by
exact line coverage ascending, then missed lines descending, then source path
ascending. Display percentages rounded to two decimal places.

Review the lowest-ranked files for implemented observable behavior. Constant-only
types, declarations without implementations, empty callbacks, exception shells,
and compatibility facades are unsuitable targets for this shortlist. Declaration
kind alone is insufficient: a default interface method or an abstract class can
implement relevant behavior.

The first eight files in the unfiltered ranking were inspected through CodeGraph;
five were retained. This is a candidate selection screen, not a correctness review
or a complete assessment of assertion quality. The full coverage report retains
every measured file.

## Five lowest-coverage files with implemented behavior

| Rank | Source file | Lines covered | Line coverage | Branches covered | Branch coverage | Implemented behavior |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [PeekableInputStream.java](../../commons-io/src/main/java/org/apache/commons/io/input/buffer/PeekableInputStream.java) | 0 / 16 | 0.00% | 0 / 8 | 0.00% | Buffered prefix inspection without consuming bytes; input checks and refill. |
| 2 | [IOConsumer.java](../../commons-io/src/main/java/org/apache/commons/io/function/IOConsumer.java) | 0 / 5 | 0.00% | 0 / 0 | Not applicable | Ordered composition, null rejection, and exception propagation in `andThen`. |
| 3 | [AbstractCharacterFilterReader.java](../../commons-io/src/main/java/org/apache/commons/io/input/AbstractCharacterFilterReader.java) | 5 / 16 | 31.25% | 2 / 10 | 20.00% | Character filtering and bulk-read compaction. |
| 4 | [CircularByteBuffer.java](../../commons-io/src/main/java/org/apache/commons/io/input/buffer/CircularByteBuffer.java) | 25 / 74 | 33.78% | 12 / 58 | 20.69% | Buffer state, wraparound, capacity checks, bulk reads/writes, and peeking. |
| 5 | [AccumulatorPathVisitor.java](../../commons-io/src/main/java/org/apache/commons/io/file/AccumulatorPathVisitor.java) | 11 / 24 | 45.83% | 1 / 12 | 8.33% | Path accumulation, normalization, equality, and relative-path operations. |

`IOConsumer` was retained because its default method implements a documented
operation; it is not a declaration-only interface. JaCoCo reports no branches
for it. This does not mean that null and exception scenarios are absent, since
exception handling is not included in JaCoCo's branch counter.
See the [JaCoCo counter definitions](https://www.jacoco.org/jacoco/trunk/doc/counters.html).

## Interpretation of the deficits

- `PeekableInputStream`: both constructors and both `peek` overloads were entirely
  unexecuted. It is the leading small candidate for a subsequent reference suite.
- `IOConsumer`: both `andThen` and its composed operation were unexecuted. Its
  contract provides a small alternative centered on order and failure propagation.
- `AbstractCharacterFilterReader`: all 11 executable lines in the bulk-read
  overload were missed; the constructor and single-character read were exercised.
- `CircularByteBuffer`: bulk read, single-byte add, peek, clear, and several
  capacity operations were entirely unexecuted. It offers more stateful scenarios
  and a larger preparation scope than the first two candidates.
- `AccumulatorPathVisitor`: the 13 missed lines are the BigInteger factory,
  `equals`, and `hashCode`. Its visitation and relative-path methods were executed,
  so its deficit is concentrated in ancillary behavior and decision alternatives.

Lower-ranked files screened out before reaching five candidates:

| File | Line coverage | Reason |
| --- | --- | --- |
| `FileCleaner.java` | 14.29% | Deprecated facade delegating operations to `FileCleaningTracker`. |
| `TailerListenerAdapter.java` | 14.29% | Empty callback extension hooks. |
| `FileExistsException.java` | 33.33% | Constructors initialize only the exception message or superclass. |

## WIT-UP context for the later study

A read-only query of the previously derived summaries found the following records:

| Class | Summary paths | Method signatures | SAT summary paths |
| --- | --- | --- | --- |
| `PeekableInputStream` | 100 | 3 | 31 |
| `IOConsumer` | 1 | 1 | 1 |
| `AbstractCharacterFilterReader` | 17 | 2 | 1 |
| `CircularByteBuffer` | 73 | 9 | 41 |
| `AccumulatorPathVisitor` | 45 | 5 | 38 |

The query matched the fully qualified declaring class in `pathId`. The derived
database is "data/processed/commons-io.duckdb" relative to the study workspace root.
SAT counts describe encoded models, not confirmed Java execution. This shortlist
does not select a final experimental target or establish generation feasibility.

## Reproduction and artifacts

Start with a fresh coverage data file; preserve previous measurements separately
before repeating the run. Maven launches separate test processes, so coverage
must accumulate across those processes.

```powershell
Set-Location -LiteralPath "D:/Projects/wit-up/commons-io"
mise exec -- mvn --batch-mode --no-transfer-progress -Pjacoco "-Djacoco.destFile=target/coverage/unit-tests.exec" "-Djacoco.dataFile=target/coverage/unit-tests.exec" test org.jacoco:jacoco-maven-plugin:0.8.14:report
Copy-Item -LiteralPath "target/site/jacoco/jacoco.xml" -Destination "target/coverage/unit-tests-jacoco.xml"
mise exec -- python "target/coverage/summarize_coverage.py"
```

Original artifact locations, relative to the Commons IO checkout:

- JaCoCo HTML report: "target/site/jacoco/index.html".
- Retained JaCoCo XML report: "target/coverage/unit-tests-jacoco.xml".
- Full unit-test log: "target/coverage/unit-tests.log".
- Source-file inventory and eligibility decisions: "target/coverage/source-file-coverage.json".
- Coverage summary script: "target/coverage/summarize_coverage.py".

A later clean build during source-only generation removed these artifact
directories, including the summary script. These are historical locators, not
currently available files. The measurements above remain the original baseline;
no coverage run was repeated when moving this document. The script would need to
be restored before repeating the complete reproduction procedure. See the
[generation assessment](peekable-input-stream-generation.md) for the subsequent
artifact-availability record.

Coverage indicates execution, not the strength of assertions. The subsequent
reference-suite phase assessed behavioral scenarios and mutation sensitivity
separately, as recorded in the study log.

## Reconstructed reference-suite coverage comparison

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
were added. The existing case identities and outcomes, including the six skips,
were unchanged; exactly 34 passing reference cases were added.

| State | Suite XML files | Reported cases | Passed | Failures | Errors | Skipped | Build exit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Before | 136 | 1,541 | 1,535 | 0 | 0 | 6 | 0 |
| After | 137 | 1,575 | 1,569 | 0 | 0 | 6 | 0 |

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

| Delegated class | Lines before | Lines after | Branches before | Branches after |
| --- | ---: | ---: | ---: | ---: |
| CircularBufferInputStream | 34/47 (72.34%) | 44/47 (93.62%) | 15/22 (68.18%) | 18/22 (81.82%) |
| CircularByteBuffer | 25/74 (33.78%) | 43/74 (58.11%) | 12/58 (20.69%) | 29/58 (50.00%) |

Project line coverage changed from 5,430/6,087 (89.21%) to 5,474/6,087 (89.93%),
and branches from 2,508/2,910 (86.19%) to 2,539/2,910 (87.25%). The observed
deltas are +44 covered lines (+0.72 pp) and +31 branches (+1.07 pp).
`FileEntry`, outside the restored fixtures, gained three covered branches and
one covered instruction. The entire global delta is not attributed to the
reference tests. The [comparison JSON](../../data/experiments/peekable-input-stream/reference-suite/coverage/comparison.json)
preserves all counters, method details, source lines, and class-level changes.
One pair does not establish repeated-run stability of every project counter.

The before build emitted five inherited coverage-rule warnings; after emitted
four. Project-wide class, method, line, and complexity requirements remained
unmet afterward. Commons Parent 50 already sets
`commons.jacoco.haltOnFailure=false`; the setting and thresholds were unchanged.
Build exit 0 therefore does not mean that every coverage requirement passed.
Complete logs retain the existing skips, compiler diagnostics, and detached
checkout branch-information warning. No diagnostic was suppressed.

To reproduce, use the recorded corrected baseline without the target test,
run the command, and archive all artifacts before cleaning. Restore the exact
reference blob, verify its hash, and repeat. Compare source/class bytes and
test identities before interpreting the delta. This later procedure does not
recreate the earlier target-selection ranking or original production revision.

- [Before HTML](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/jacoco/index.html), [XML](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/jacoco/jacoco.xml), and [CSV](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/jacoco/jacoco.csv).
- [After HTML](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/jacoco/index.html), [XML](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/jacoco/jacoco.xml), and [CSV](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/jacoco/jacoco.csv).
- Full logs: [before](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/maven.log) and [after](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/maven.log).
- Metadata and timestamps: [before](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/run.json) and [after](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/run.json).
- Test identities and outcomes: [before](../../data/experiments/peekable-input-stream/reference-suite/coverage/before/suite-summary.json) and [after](../../data/experiments/peekable-input-stream/reference-suite/coverage/after/suite-summary.json).
- [Unchanged reference source](../../data/experiments/peekable-input-stream/reference-suite/coverage/PeekableInputStreamTest.java) and [artifact inventory](../../data/experiments/peekable-input-stream/reference-suite/coverage/artifact-manifest.json).

Each run additionally retains "jacoco.exec", every Surefire report, environment
output, source and compiled-output hash manifests, and compiled production ZIPs
outside the checkout. Raw Maven logs retain their original Windows encoding.
The active generation branch and its test file were not used for these builds.
