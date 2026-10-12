# PeekableInputStream JSON-based generation assessment

[Documentation index](../README.md) | [Study log](../study-log.md) |
[JSON prompt](../prompts/unit-test-generation-json.txt) |
[Source-only assessment](peekable-input-stream-generation.md)

Initially assessed and reviewed on October 9, 2026, using existing execution
records. Supplemented on October 11 with the reconstructed JaCoCo comparison
below. The [initial report](../../data/experiments/peekable-input-stream/json-only/coverage/assessment-before-coverage.md)
and the complete generated Java block are preserved. No test, assertion, fixture,
production file, dependency, build configuration, or prompt was corrected.
Only coverage measurement and documentation were added; no mutation analysis
or additional standalone test-source Checkstyle assessment was performed.

## Outcome

The generated suite contains **12 test methods and 12 executed cases, all passing,
with no failures, errors, or skips**. The same 12 target cases passed again
during repository verification.

The later instrumented comparison reproduced all 12 target outcomes and
increased target coverage from **0/16 to 11/16 lines (68.75%)** and from
**0/8 to 7/8 branches (87.50%)**. These are structural execution counters,
separate from the symbolic-record association fraction below.

The result supports **partial feasibility for the supplied exception scenarios**:
the agent produced runnable JUnit assertions consistent with selected exported
exception types. The 12 tests are associated with
**11 distinct SAT records**; two constructor variants share one record. Eight
tests explicitly change one or more exported assignments to obtain usable
fixtures. Passing exception assertions therefore do not establish exact
reproduction of the exported models or execution paths.

The suite checks argument rejection only. It does not assert normal `peek`
results, nonconsumption, refill behavior, wraparound, or the previously corrected
EOF length defect. A passing subset is not equivalent to a complete reference
suite. Exact path reproduction, defect-detection effectiveness, and strict
isolation from prohibited context remain unestablished. These limits prevent a
claim that JSON-based generation is generally superior to source-only generation.

## Trial identity

| Item | Recorded value |
| --- | --- |
| Model and reasoning setting | User-reported **GPT-6.1 Sol Extra High**. The retrieved chat record does not independently expose these settings. |
| Generation chat | `Add PeekableInputStream tests`, ID `01a122c2-8c87-7493-8a4d-95a07cdccaab`. |
| Branch | `test/peekable-input-stream-json-generation`. |
| Generation and measurement baseline commit | `d7a3c884d07ff5f1829b09087f34dcb8043f0f64`. |
| Condition | JSON exports as the sole permitted source of target-specific scenarios, constraints, and expected outcomes; repository conventions and unrelated tests permitted for style/framework use. |
| Input artifact label | `commons-io-11f0abe7a.jar`; this label does not independently verify the analyzed JAR bytes. |
| Observed turns and writes | One completed generation turn, one target-file creation, no follow-up repair prompt or later test-source rewrite in the retrieved record. |
| Turn timing | `2026-10-09T22:25:16Z` to `2026-10-09T22:32:58Z`; recorded duration `462253 ms`, approximately 7 minutes 42 seconds. This includes inspection, JSON processing, writing, and broader verification. |
| Generated source | "D:/Projects/wit-up/commons-io/src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java". |
| Generated source SHA-256 | `5B1F644557EE4597EEA7D9902AA6390C6D8B89AC1F89ABE52BDF8D8CF95765CB`. |
| Prepared JSON prompt SHA-256 | `C30A0B9DA988EAF5F7F6E37BA99848387EE28266754CEC5167AC2DAA36AD8BD5`. |
| Tokens and cost | Unavailable in the retrieved record. |

The submitted prompt matches the prepared file's content after trimming trailing
whitespace. The hash above identifies the prepared local file, not necessarily
the exact bytes of the chat message. Git inspection at the initial assessment
found no tracked changes to production or configuration; only the generated
target test was untracked. Runtime/build records identify Temurin Java `1.8.0_504`, Maven
`3.9.16`, JUnit Jupiter `5.5.2`, and Surefire `2.22.2`.

The evidence consists of the generation chat, current generated source, original
JSON records, existing Surefire and Checkstyle reports, and the recorded command
exit statuses. Five command outputs in the retrieved chat are truncated, including
the CodeGraph response and broader build output. This is not a complete capture
of every context input or diagnostic.

## Recorded validation

The target command ran from "D:/Projects/wit-up/commons-io":

```text
mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" test
```

The agent recorded 12 passing tests. The later clean suite run again reported
12 passing cases for the target class. The archived target XML and text report
are from that later run, rather than a separate preserved copy of the first run.

The broader verification command was:

```text
mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" clean verify apache-rat:check clirr:check checkstyle:check javadoc:javadoc
```

The command returned exit code 0. Its target Surefire XML confirms 12 passed
cases with no failures, errors, or skips.
The generation agent reported successful repository verification, including
license/API checks, and retained existing compiler and Javadoc configuration
warnings. The truncated build output limits complete diagnostic reconstruction.

Coverage profiles were explicitly disabled in the original generation commands.
They produced no coverage or mutation result. The later JaCoCo assessment is
reported separately below; mutation sensitivity remains unmeasured. Test success,
assertion counts, and JSON association counts are distinct from those measurements.

The generated source has 12 `assertThrows` call sites, one per test. Constructor
tests assert the constructor invocation itself. Other tests create their stream
outside the assertion and invoke the selected `peek` overload inside it, avoiding
misclassification of a setup exception as the target method's exception.
`assertThrows` accepts the requested exception class or a subclass; these tests
do not assert an exact exception class, message, or internal origin. Passing
therefore establishes a compatible exception from the target invocation, not the
precise internal throw site or full path. It does not independently establish
that the recorded behavior is the intended public contract.

## JSON inventory and test associations

The input files are
"D:/Projects/wit-up/commons-io-analysis-results/witup-results-commons-io-11f0abe7a.json"
and
"D:/Projects/wit-up/commons-io-analysis-results/witup-summaries-commons-io-11f0abe7a.json".

A read-only check of these original files confirms 100 target result records and
100 target summaries. Each `(artifact, pathId)` key is unique and has exactly one
counterpart. Signature metadata and solver statuses agree: **31 SAT and 69 UNSAT**.
The 69 UNSAT records were not used as fixture candidates.

| Exported signature | SAT records | UNSAT records | Distinct SAT records associated with tests | Generated tests |
| --- | ---: | ---: | ---: | ---: |
| `PeekableInputStream(InputStream, int)` | 1 | 1 | 1 | 2 |
| `peek(byte[])` | 11 | 38 | 3 | 3 |
| `peek(byte[], int, int)` | 19 | 30 | 7 | 7 |
| **Total** | **31** | **69** | **11** | **12** |

These are exported exception records, not an inventory of all possible runtime
paths. The SAT summaries name 15 `IllegalArgumentException`, 4
`NullPointerException`, and 12 `ArrayIndexOutOfBoundsException` outcomes. No
generated test expects `ArrayIndexOutOfBoundsException`. SAT indicates
satisfiability in the exported analysis model; it does not by itself establish
that an accessible Java fixture can reach the modeled state. Likewise, these
UNSAT results do not prove that the API has no other ways to exhibit a behavior.

All associations below use artifact `commons-io-11f0abe7a.jar`. The following
abbreviations expand to complete exported identifiers:

- `C#n`: `<org.apache.commons.io.input.buffer.PeekableInputStream: void <init>(java.io.InputStream,int)>#n`
- `W#n`: `<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[])>#n`
- `S#n`: `<org.apache.commons.io.input.buffer.PeekableInputStream: boolean peek(byte[],int,int)>#n`

| Generated test | Associated record | Expected exception | Assignment handling |
| --- | --- | --- | --- |
| `testConstructorRejectsNegativeBufferSize` | C#0 | `IllegalArgumentException` | Uses size -1 instead of exported 0; both negate `pBufferSize > 0`. |
| `testConstructorRejectsZeroBufferSize` | C#0 | `IllegalArgumentException` | Retains exported size 0. |
| `testPeekRejectsEmptyArray` | W#9 | `IllegalArgumentException` | Keeps array length 0; changes receiver capacity 0 to 1. |
| `testPeekRejectsNullArray` | W#1 | `NullPointerException` | Preserves the true null flag; stream setup is chosen separately. |
| `testPeekRejectsOversizedArray` | W#0 | `IllegalArgumentException` | Changes array length/capacity 1/0 to 2/1, retaining length greater than capacity. |
| `testPeekSliceRejectsEmptyArray` | S#7 | `IllegalArgumentException` | Keeps array length/offset 0/0; changes capacity 0 to 1; selects unspecified comparison length 0. |
| `testPeekSliceRejectsNegativeLengthWithEmptyInput` | S#31 | `IllegalArgumentException` | Retains relevant length/capacity/offset/comparison-length literals 1/1/0/-1; assumes an empty initialized buffer. |
| `testPeekSliceRejectsNegativeOffsetForEmptyArray` | S#8 | `IllegalArgumentException` | Keeps array length 0 and offset -1; changes capacity 0 to 1; selects unspecified comparison length 0. |
| `testPeekSliceRejectsNegativeOffsetWithEmptyInput` | S#29 | `IllegalArgumentException` | Changes array length/capacity 0/0 to 1/1 and modeled buffered count -1 to assumed 0; retains offset -1. |
| `testPeekSliceRejectsNullArray` | S#1 | `NullPointerException` | Preserves the true null flag; selects unspecified offset/comparison length 0/0. |
| `testPeekSliceRejectsOffsetAtArrayEndWithEmptyInput` | S#28 | `IllegalArgumentException` | Changes array length/capacity/count/offset 0/0/-1/0 to 1/1/0/1, retaining offset at the array end and insufficient buffered bytes. |
| `testPeekSliceRejectsOversizedArray` | S#0 | `IllegalArgumentException` | Changes array length/capacity 1/0 to 2/1; selects unspecified offset/comparison length 0/1. |

The 12 tests are associated with 11 distinct SAT records, or 11/31 (35.48%) of
the candidate records. This is an association fraction, not measured path coverage
or a verified model-reproduction rate. The constructor's extra negative-size
variant does not increase the number of distinct supporting records.

## Fixture assumptions and interpretation limits

The agent explicitly assumes that constructor capacity 1 creates a non-null
buffer of that capacity and that fresh empty input has zero buffered bytes.
It chooses non-null `ByteArrayInputStream` fixtures, empty input content, and zeroed
comparison arrays where the export does not supply complete Java objects. It
does not interpret serialized reference identities as Java scalar arguments.

Eight tests explicitly alter at least one exported assignment. The remaining
four preserve the relevant literal/null assignments identified in the mapping,
but still do not reconstruct all serialized objects, intermediate symbols, or
hidden state. Exact realization of the original solver model has not been
established for any test; this is an unmeasured property, not a measured zero
reproduction rate.

The generator used a separate Python script to evaluate the associated records'
symbolic predicates against manually supplied fixture values and their
`truthValue` flags. That calculation assumes, for example, a non-null internal
buffer and a buffered count of zero; it does not obtain those values from the
running Java objects. It supports consistency with the predicates under those
assumptions, without proving that the runtime took the exported path. The comments
disclose changed assignments. The prompt permits explicit fixture assumptions
and does not require unchanged assignments, so disclosed variants are a limit
on the reproduction claim, not automatically a prompt violation.

For example, the oversized-array models export capacity 0. The generated tests
use capacity 1 and array length 2, preserving the inequality while providing a
usable stream. S#28 and S#29 similarly replace a modeled negative byte count and
zero-capacity receiver with an assumed fresh valid state. These are explicit
fixture variants, not exact reproductions of those assignments.

All assertions concern `IllegalArgumentException` or `NullPointerException` from
invalid arguments. They do not exercise the intended equality result for valid
data or establish regression sensitivity to the corrected buffer length guard.
Using empty input in an invalid-argument test does not by itself test the EOF
comparison result for valid arguments. No original-versus-corrected production
comparison was run for this suite.
The exceptions-only scope is consistent with the selected exports' available
outcomes; it cannot substitute for normal-behavior tests in the reference suite.

## Unrepresented SAT records

Twenty SAT records have no generated test association. The following reasons
were reported by the generation agent and are consistent with its reconstruction
limits. They are not proofs that every corresponding behavior is impossible
through every accessible API sequence.

| Records | Count | Reported limitation |
| --- | --- | --- |
| S#3, W#3 | 2 | Null internal buffer not established through the permitted setup information. |
| S#9, S#30, W#10, W#30 | 4 | Inconsistent stream capacity and internal buffer length. |
| S#10 | 1 | Negative-length exception overlaps S#31, but the required prebuffered state was not reconstructed. |
| S#22, S#23, S#43, S#44, W#23, W#24, W#43, W#44 | 8 | Negative internal start offsets and associated symbolic array conditions. |
| S#26, S#27, S#47, S#48 | 4 | Internal capacity, count, offset, and comparison states not reconstructed from the permitted information. |
| W#29 | 1 | Empty-array outcome overlaps W#9, but its model includes zero capacity and a negative buffered count. |

No skipped JUnit cases were used to represent these omissions. They remain
unimplemented candidate records, separately accounted for from the 12 executed
target tests.

## Repository conventions and context exposure

The archived Maven Checkstyle XML excludes the target test.
Therefore, this command does
not validate the generated test's style. Source inspection again found no method
Javadocs on the 12 tests, despite the configured `JavadocMethod` requirement when
that source is checked. This is an identified convention gap, not a recorded
Checkstyle failure for the generated file. No Checkstyle invocation targeting
test source was recorded or performed for this assessment, and no exact count
of failing style diagnostics is claimed.

The generation agent issued a restricted CodeGraph convention query for build
configuration and an unrelated test. The tool did not uniquely match the named
test and returned other files, including production snippets from
"src/main/java/org/apache/commons/io/file/PathUtils.java". The agent acknowledged
this exposure and stated that it would not use those snippets for test design.
The visible returned source was unrelated to `PeekableInputStream`; the response
was truncated, so its full contents cannot be audited from this retrieval.

This is a documented context-isolation deviation: production material entered
the generation context despite the query's explicit exclusion. The agent's stated
non-use does not prove that the context was unaffected. The visible command record
shows no deliberate target-production retrieval, skill loading, reference-suite
retrieval, study-finding consultation, or coverage/mutation analysis. Effective
skill discovery, memory, and injected instructions were not independently isolated.

The agent performed the broader build after writing the test file. It did not
rewrite failing assertions or change production to obtain success. Generating
Javadocs as a build check is recorded separately from consulting behavioral
documentation for test design; no such consultation is visible in the record.

## Comparison with the source-only trial

| Observation | Source-only trial | JSON-based trial |
| --- | --- | --- |
| User-reported model setting | GPT-6.1 Sol Extra High | GPT-6.1 Sol Extra High |
| Production baseline | d7a3c884d | d7a3c884d |
| Generated executed cases | 26 | 12 |
| Target outcome | 21 passed, 4 failures, 1 error | 12 passed, no failures or errors |
| Generated scope | Normal behavior and exceptions | Invalid-argument exceptions only |
| Supporting JSON association | Not applicable | 11 distinct SAT records, including explicit assignment variants |
| Later target line coverage | 16/16 (100.00%) | 11/16 (68.75%) |
| Later target branch coverage | 8/8 (100.00%) | 7/8 (87.50%) |
| Mutation measurement for generated output | Not performed | Not performed |
| Test-source Checkstyle validation | Not established | Not established |

The JSON output expects rejection of empty comparison arrays and passes on the
current checkout, whereas the source-only output expected acceptance and errored.
This is a concrete difference consistent with the exported exception outcomes
and the previously established contract assessment. However, the JSON trial
does not generate the source-only trial's shorter-prefix or nonempty-buffer
zero-length success expectations; it avoids those normal-return questions rather
than demonstrating that it independently resolved all of them.

Both trials use the same corrected production baseline, but the prompts differ
in permitted inputs, scope, interpretation guidance, and traceability requirements.
The JSON exports also identify the older `11f0abe7a` artifact. The actual producer
revision and analyzed JAR bytes remain unverified. A single narrower passing
trial cannot establish a general model-effectiveness improvement or attribute the
outcome solely to changing the input source. The two pass fractions describe
different selected scenarios, not performance on a common evaluation set. Turn
durations also include different validation work and are not directly comparable
measures of generation efficiency.

## Preserved evidence

During this assessment, existing execution reports were copied outside
"commons-io/target" and verified against their originals. No new test run
generated this original evidence.

- [Preserved target Surefire XML](../../data/experiments/peekable-input-stream/json-only/surefire.xml)
- [Preserved target Surefire text report](../../data/experiments/peekable-input-stream/json-only/surefire.txt)
- [Preserved Checkstyle XML](../../data/experiments/peekable-input-stream/json-only/checkstyle.xml)

The original target test was subsequently removed from the generation checkout
after its complete source was preserved in this appendix. Coverage measurement
restored that exact source only in a disposable checkout. The license header,
imports, fixture comments, 12 methods, and all 12 exception assertions remain
unchanged. No corrected alternative is included.

## Post-generation JaCoCo comparison

Coverage and test-result comparisons refer exclusively to
`org.apache.commons.io.input.buffer.PeekableInputStream` and its dedicated
test class. Before means the target test file was absent; recorded target
coverage was zero, including any possible execution by existing tests.
Complete original execution artifacts remain archived unchanged.

This October 11 measurement reconstructs the before/after states after the
original trial. It does not recover a generation-time coverage report. Before
used commit `d7a3c884d07ff5f1829b09087f34dcb8043f0f64` without the target test.
After added only the complete Java appendix, whose SHA-256 was checked against
the original value in the trial identity table. No test or fixture was edited.

Both runs used the same detached checkout,
"D:/Projects/wit-up/.worktrees/commons-io-coverage", with Temurin `1.8.0_504`,
Maven `3.9.16`, JUnit Jupiter `5.5.2`, Surefire `2.22.2`, and JaCoCo `0.8.14`.
The identical full-suite command was:

```powershell
mvn -B -Pjacoco "-Djacoco.skip=false" clean verify jacoco:report
```

Each clean build started with fresh execution data, and the before artifacts
were archived before the after build. All 398 common files under "src" and all
compiled production outputs were byte-identical. No coverage filters or test
exclusions were added. Comparing test identities and outcomes found only the
12 added passing target cases; all existing outcomes were unchanged.
The target outcomes also match the original preserved Surefire XML exactly.

| State | Target cases | Passed | Failures | Errors | Skipped | Build exit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Before: target test absent | 0 | 0 | 0 | 0 | 0 | 0 |
| After | 12 | 12 | 0 | 0 | 0 | 0 |

| Target counter | Before | After | Added covered units | Change |
| --- | ---: | ---: | ---: | ---: |
| Lines | 0/16 (0.00%) | 11/16 (68.75%) | 11 | +68.75 pp |
| Branches | 0/8 (0.00%) | 7/8 (87.50%) | 7 | +87.50 pp |
| Instructions | 0/98 (0.00%) | 77/98 (78.57%) | 77 | +78.57 pp |
| Methods, including constructors | 0/4 (0.00%) | 3/4 (75.00%) | 3 | +75.00 pp |

Percentages divide covered units by their totals; pp denotes percentage points.
The missed target lines are **49, 50, 68, 70, and 92**. The default-capacity
constructor is outside these generated cases. The whole-array overload does
not take its refill branch at line 67, leaving line 68 unexecuted. The delegated
return lines 70 and 92 also have no recorded coverage: relevant invocations
throw before a subsequent probe records their completion. Thus a missed line
does not always mean that its statement was never entered. See the
[JaCoCo exception coverage explanation](https://www.jacoco.org/jacoco/trunk/doc/faq.html).

These values are not measured reproduction rates for the 31 SAT records.
JaCoCo branch coverage does not enumerate exception paths, and coverage does
not establish oracle strength or mutation sensitivity. Several argument checks
are implemented in delegated classes outside the target denominator. See the
[counter definitions](https://www.jacoco.org/jacoco/trunk/doc/counters.html).
No normal-result assertions or additional exception tests were introduced.

The [target-only comparison](../../data/experiments/peekable-input-stream/target-coverage/comparison.json)
records target counters and outcomes. One measurement pair does not establish
repeated-run stability or mutation adequacy.

Both builds returned exit code 0; inherited coverage checks still emitted
warnings. Build success does not establish that all coverage requirements passed.
Build configuration and thresholds were unchanged. Complete original logs
preserve all diagnostics; no warning or failure was suppressed.

To reproduce, prepare the recorded baseline in a disposable checkout, measure
without the target file, archive that run, restore the exact appendix, and repeat
the same command. Compare source/class hashes and test identities before
interpreting the delta. Retain the unchanged original generated source and
separate later measurement artifacts from the original generation evidence.

- [Before target HTML](../../data/experiments/peekable-input-stream/json-only/coverage/before/jacoco/org.apache.commons.io.input.buffer/PeekableInputStream.html), [raw XML](../../data/experiments/peekable-input-stream/json-only/coverage/before/jacoco/jacoco.xml), and [raw CSV](../../data/experiments/peekable-input-stream/json-only/coverage/before/jacoco/jacoco.csv).
- [After target HTML](../../data/experiments/peekable-input-stream/json-only/coverage/after/jacoco/org.apache.commons.io.input.buffer/PeekableInputStream.html), [raw XML](../../data/experiments/peekable-input-stream/json-only/coverage/after/jacoco/jacoco.xml), and [raw CSV](../../data/experiments/peekable-input-stream/json-only/coverage/after/jacoco/jacoco.csv).
- Full logs: [before](../../data/experiments/peekable-input-stream/json-only/coverage/before/maven.log) and [after](../../data/experiments/peekable-input-stream/json-only/coverage/after/maven.log).
- Metadata and timestamps: [before](../../data/experiments/peekable-input-stream/json-only/coverage/before/run.json) and [after](../../data/experiments/peekable-input-stream/json-only/coverage/after/run.json).
- [Target test outcomes after](../../data/experiments/peekable-input-stream/json-only/coverage/after/surefire-reports/TEST-org.apache.commons.io.input.buffer.PeekableInputStreamTest.xml); the target test file was absent before.
- [Restored source](../../data/experiments/peekable-input-stream/json-only/coverage/PeekableInputStreamTest.java) and [artifact inventory](../../data/experiments/peekable-input-stream/json-only/coverage/artifact-manifest.json).

Each run also retains "jacoco.exec", every Surefire report, environment output,
source and compiled-output hash manifests, and compiled production ZIPs outside
the checkout. Raw Maven logs retain their original Windows encoding. The
initial report, original execution evidence, prompts, and the complete Java
appendix remain preserved, with no corrected test alternative.

## Appendix: complete generated Java source

```java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.commons.io.input.buffer;

import static org.junit.jupiter.api.Assertions.assertThrows;

import java.io.ByteArrayInputStream;
import java.io.IOException;

import org.junit.jupiter.api.Test;

/**
 * Exception scenarios supported by the supplied analysis records.
 *
 * Fixtures assume that a positive constructor size becomes the stream's buffer size and initializes a non-null buffer.
 * A fresh stream over an empty input is assumed to have zero buffered bytes. These internal conditions are not inspected,
 * so the tests assert the recorded exceptions without claiming exact execution-path reproduction.
 */
public class PeekableInputStreamTest {

    @Test
    public void testConstructorRejectsNegativeBufferSize() {
        final ByteArrayInputStream input = new ByteArrayInputStream(new byte[0]);
        // The exported size is zero; -1 is an explicit variant of the false "pBufferSize > 0" constraint.
        assertThrows(IllegalArgumentException.class, () -> new PeekableInputStream(input, -1));
    }

    @Test
    public void testConstructorRejectsZeroBufferSize() {
        final ByteArrayInputStream input = new ByteArrayInputStream(new byte[0]);
        assertThrows(IllegalArgumentException.class, () -> new PeekableInputStream(input, 0));
    }

    @Test
    public void testPeekRejectsEmptyArray() throws IOException {
        final byte[] expected = new byte[0];
        // Use capacity 1 instead of the exported zero-capacity receiver; the empty-array constraints still hold.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected));
        }
    }

    @Test
    public void testPeekRejectsNullArray() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(NullPointerException.class, () -> stream.peek(null));
        }
    }

    @Test
    public void testPeekRejectsOversizedArray() throws IOException {
        final byte[] expected = new byte[2];
        // Replace exported length 1/capacity 0 with length 2/capacity 1, preserving length > capacity.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected));
        }
    }

    @Test
    public void testPeekSliceRejectsEmptyArray() throws IOException {
        final byte[] expected = new byte[0];
        // Capacity 1 replaces exported capacity 0; offset 0 is still at the end of the empty array.
        // Length is unassigned in the model; use zero.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, 0, 0));
        }
    }

    @Test
    public void testPeekSliceRejectsNegativeLengthWithEmptyInput() throws IOException {
        final byte[] expected = new byte[1];
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, 0, -1));
        }
    }

    @Test
    public void testPeekSliceRejectsNegativeOffsetForEmptyArray() throws IOException {
        final byte[] expected = new byte[0];
        // Capacity 1 replaces exported capacity 0. Keep the exported offset -1; choose unassigned length zero.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, -1, 0));
        }
    }

    @Test
    public void testPeekSliceRejectsNegativeOffsetWithEmptyInput() throws IOException {
        final byte[] expected = new byte[1];
        // Replace exported array length/capacity 0 and buffered count -1 with length/capacity 1 and count 0.
        // This preserves insufficient buffered bytes and offset -1; choose unassigned length 1.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, -1, 1));
        }
    }

    @Test
    public void testPeekSliceRejectsNullArray() throws IOException {
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(NullPointerException.class, () -> stream.peek(null, 0, 0));
        }
    }

    @Test
    public void testPeekSliceRejectsOffsetAtArrayEndWithEmptyInput() throws IOException {
        final byte[] expected = new byte[1];
        // Replace exported array length/capacity 0 and buffered count -1 with length/capacity 1 and count 0.
        // Offset changes from 0 to 1 to remain at the array end; choose unassigned length 1.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, 1, 1));
        }
    }

    @Test
    public void testPeekSliceRejectsOversizedArray() throws IOException {
        final byte[] expected = new byte[2];
        // Replace exported length 1/capacity 0 with length 2/capacity 1, preserving length > capacity.
        // Offset and length are unassigned in the model; choose the first byte only.
        try (final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1)) {
            assertThrows(IllegalArgumentException.class, () -> stream.peek(expected, 0, 1));
        }
    }
}
```
