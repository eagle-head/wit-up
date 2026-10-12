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
