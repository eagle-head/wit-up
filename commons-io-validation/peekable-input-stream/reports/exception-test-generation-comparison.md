# Exception-Test Generation from WIT-UP JSON and Java Source

## Consolidated pilot report

Prepared for academic review on 2026-10-13 (UTC).

This report identifies what information was missing or insufficiently usable in WIT-UP JSON for Java exception-test generation, what could improve that information, and how to measure the effects. Its evidence comes from two already generated, frozen JUnit suites for Apache Commons IO's `PeekableInputStream`. Both suites were evaluated using the same paired full-suite protocol, configuration revision 4. The JSON-source suite was measured again in a new evaluation; the Java-source evaluation was reused from its verified sealed record. Each baseline was actually measured. No test was revised using execution, coverage, or mutation feedback.

The JSON-source suite contains 10 passing cases and the Java-source suite contains 20 passing cases. The corresponding suites killed 1 and 7 of the same 14 native mutants. The observed mutation-score difference is 42.86 percentage points in favor of the Java-source suite in these two observations.

The JSON inputs were sufficient to generate a passing exception-test suite without consulting production source, but the suite generated from them did not match the mutant detection achieved with Java source in this pair. Inspection of the preserved exports identifies actionable information gaps: no selected scenario describes `IOException`, while five additional Java-source detections are attributed to read-failure cases; 21 SAT candidates lacked supported public fixtures; and the selected records do not supply expected exception messages. The next research question is whether targeted improvements to the exported information can close these gaps while the generator continues to use JSON only.

Both suites were generated with GPT-6.1 Sol (`gpt-6.1-sol`), with Extra High reasoning effort (`xhigh`), in separate fresh chats without prior conversation history. The original session records and the operator's confirmation establish these generation conditions. Suite size and composition are observed outcomes of generation under each source condition. This descriptive pilot contains one generation per condition; additional generations are deferred pending feedback from Professor Rodrigo and Doctoral Student Adriano. The results characterize this pair without estimating repeatability or general superiority.

## Objective and scope

The study asks whether WIT-UP JSON provides sufficient information to generate effective Java exception tests without giving the generator production source code and, where it falls short, which information should be improved and how that improvement should be measured. The Java-source condition provides a comparison for identifying behavior and observations that the JSON-based generation missed; it is not a complete reference suite or a maximum achievable score.

Generation targeted exceptional behavior of the public constructors and declared `peek` overloads of `org.apache.commons.io.input.buffer.PeekableInputStream`. Every generated case was required to assert an exception from a target call; normal operations could only establish fixture state. Sufficiency therefore concerns executable fixtures, supported exception oracles, and detection of changes to exceptional behavior, rather than a fixed test count or line-coverage threshold.

The JSON condition used the original WIT-UP results and summaries exports. The Java-source condition used the designated production source and permitted superclass/buffer implementation. The preserved prompts specify these boundaries in full in the appendices. Generation and measurement are separate phases; evaluation supplements contribute zero additional independent generations.

Here, generation without source code means that the generator does not inspect production source, Javadoc, bytecode, decompiled code, or other target-specific behavioral material outside its assigned JSON. The build and evaluator can consume production artifacts. This pilot does not establish that the entire upstream analysis and build process operates without source availability.

## JSON information gaps, improvements, and effect measurement

The priorities below connect each gap in the selected JSON inputs to information the generator could use and an observable result to measure. The evidence column describes this pilot; the proposed additions and measurements have not been implemented or executed.

| Gap in the JSON information | What the JSON should provide | Evidence from this study | How to measure the effect of the improvement |
| --- | --- | --- | --- |
| Read-failure scenarios are absent | Supported conditions under which the input dependency throws `IOException`, an accessible way to configure that failure, and how the exception propagates through the target `peek` call. | None of the 100 selected records describes `IOException`. Five additional mutant detections in the Java-source suite are attributed to read-failure cases. | Compare unchanged JSON with JSON containing this addition: record whether supported `IOException` cases are generated and pass through target calls, which of the five associated mutant gaps close, and whether previous detections are retained. |
| Public preparation of the required state is insufficiently supported | Valid constructor arguments, relationships between capacities, initial contents and byte count, and public operation sequences that establish the required state. Identify state conditions whose reachability remains unresolved. | Symbolic conditions were present, but 21 SAT candidates lacked sufficiently supported public fixtures, including 12 `ArrayIndexOutOfBoundsException` candidates. | Track each candidate that gains a justified public fixture and an observed target exception. Record remaining unsupported states, assumptions, and any demonstrated unreachability; inspect the resulting coverage and mutant-status changes. |
| The expected exception's origin is insufficiently distinguished | A supported expected message or another observable property, such as cause, identity, or conditions that distinguish the intended validation. Include the evidence supporting each expectation. | Exception types were available, but competing validations can both throw `IllegalArgumentException`. One additional Java-source detection depends on distinguishing them by message; the selected records do not supply that message. | Check whether generated assertions distinguish the intended exception from an exception of the same type produced by another validation. Compare the line-85 boundary mutant and the shared size-guard survivor, while preserving passing outcomes on the unmutated target. |

The first content priority is to investigate and represent supported read failures, because that missing family is associated with five observed detection gaps. The next priority is to connect symbolic state to executable public setup, followed by strengthening the observations that identify the expected exception. Each proposed addition needs derivation from the permitted analysis artifacts; the cause of the current omissions and the feasibility of extracting every proposed detail remain to be investigated.

The JSON already contains constraints and propagation metadata. The improvement is to connect those facts into a usable description of **how to prepare the scenario, which target call to execute, and what to assert about its exception**. Preserve traceability from the input record to the fixture, the oracle, and the observed outcome.

To measure the added information, compare independent generations from unchanged JSON with generations receiving one addition at a time, then examine combinations. Hold the common prompt, model/settings, target, and measurement protocol fixed where reproducible. Track behavioral gains and specific mutant-status changes alongside the existing JaCoCo/PIT metrics, retaining all 14 mutants in the reported score. Repeated executions of one frozen suite do not measure variation in generation; new generations require their own preserved runs. The detailed comparisons later in this report specify the controls and limits.

## What the pilot establishes about JSON sufficiency

| Meaning of sufficient | Answer for this pilot | Evidence and boundary |
| --- | --- | --- |
| Can it support generation of executable exception tests without consulting source code? | Yes, for the generated cases. | All 10 JSON-generated cases passed; the aligned measurement detected 1 mutant. Expected exception types and fixture assumptions are traceable to the preserved records. |
| Did it support a public fixture for every selected SAT candidate? | No, in this generation. | 10 of 31 SAT candidates produced tests; 21 remained without sufficiently supported public fixtures. These are candidate associations, not measured path coverage or proof that every remaining model is publicly reachable. |
| Did the resulting suite match the observed effectiveness of the Java-source suite? | No, for this pair. | The suites detected 1 versus 7 of the same 14 mutants, despite equal JaCoCo line coverage. The Java-source suite also leaves gaps. |
| Does this establish that source code is indispensable, or that JSON cannot carry enough information? | No. | The current exports have concrete gaps, but enriched exports were not evaluated. The records also do not establish the best suite another independent generation could derive from unchanged JSON. |

The supported answer is therefore **demonstrated feasibility, with gaps in the supplied information and in the resulting suite's effectiveness**. JSON sufficiency is a question about the exported information and its use by the generator, not a conclusion about the serialization format alone. No numerical sufficiency threshold was registered before this pilot; the criteria below are proposals for future comparisons, not retrospective pass/fail gates.

## Records and preservation

| Item | WIT-UP JSON | Java source |
| --- | --- | --- |
| Generation | json-001 | java-source-001 |
| Evaluation | json-001/evaluation-001 | java-source-001/evaluation-005 |
| Recorded origin | retrospective_import | prospective |
| Generation model | GPT-6.1 Sol (`gpt-6.1-sol`) | GPT-6.1 Sol (`gpt-6.1-sol`) |
| Reasoning effort | Extra High (`xhigh`) | Extra High (`xhigh`) |
| Chat context | Separate fresh chat; no prior conversation history | Separate fresh chat; no prior conversation history |
| Executed generated cases in the aligned after phase | 10 | 20 |
| Frozen Java SHA-256 | a29b1141af4aa61b9081d22e2056f69596e5ec602062773a4618b5567c3de926 | 365a763fbc4b383087d993e659e05bf04952a4d4333a2ff16ac4417fe9eb43dd |
| Parent seal SHA-256 | 482c9deffe47d4fc69f8fee5e4380610991893d447a38fe0ca6973baece488fd | 28ac9b72af259f32261cb569e3ce65515007f3089213024d5065b60adcec9d5d |
| Evaluation seal SHA-256 | 8e2bc78d5bcca8f8bf064566a855ada4dbb840c3fb22b6b2c5063c852ff5d461 | 57d892f347416957333f373348d08d1def6a87f282769e9e78ea9b0511346c69 |

Both conditions use Commons IO commit `11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`. Before/after checkouts are distinct, and their complete tracked-file inventories match. The only added source in each after checkout is that generation's exact frozen Java file. Existing tests, production source, resource files, and checkout build configuration remain unchanged.

The production class SHA-256 is `7ab6a91f3618ccf5949692f1fc5d39b97174deab23925f872f0e31cb5a2591a1` across all eight selected measurement phases. All four PIT artifacts contain the same 14 mutant identities, including class, method, descriptor, source line, mutator, indexes, and blocks. All 23 unique project/launcher JARs have identical bytes across the two evaluations; the ordered classpaths also match after evaluation-path substitution.

## Aligned before and after results

All rows below describe the target production class, not coverage of the whole Commons IO library. Percentages are calculated from native integer counters. Before denotes a clean baseline checkout measured during the evaluation, not a claimed measurement from before generation. The historical JSON measurements used different selections and are retained separately; none of those historical values supplies this comparison table.

| Metric | JSON before | JSON after | Java before | Java after |
| --- | --- | --- | --- | --- |
| JaCoCo instruction | 0/98 (0.00%) | 77/98 (78.57%) | 0/98 (0.00%) | 77/98 (78.57%) |
| JaCoCo branch | 0/8 (0.00%) | 7/8 (87.50%) | 0/8 (0.00%) | 8/8 (100.00%) |
| JaCoCo line | 0/16 (0.00%) | 11/16 (68.75%) | 0/16 (0.00%) | 11/16 (68.75%) |
| JaCoCo complexity | 0/8 (0.00%) | 6/8 (75.00%) | 0/8 (0.00%) | 7/8 (87.50%) |
| JaCoCo method | 0/4 (0.00%) | 3/4 (75.00%) | 0/4 (0.00%) | 3/4 (75.00%) |
| JaCoCo class | 0/1 (0.00%) | 1/1 (100.00%) | 0/1 (0.00%) | 1/1 (100.00%) |
| PIT mutation score | 0/14 (0.00%) | 1/14 (7.14%) | 0/14 (0.00%) | 7/14 (50.00%) |
| PIT test strength | N/A (0/0) | 1/9 (11.11%) | N/A (0/0) | 7/10 (70.00%) |
| PIT native line coverage | 0/16 (0.00%) | 13/16 (81.25%) | 0/16 (0.00%) | 15/16 (93.75%) |
| PIT KILLED | 0 | 1 | 0 | 7 |
| PIT SURVIVED | 0 | 8 | 0 | 3 |
| PIT NO_COVERAGE | 14 | 5 | 14 | 4 |
| PIT TIMED_OUT | 0 | 0 | 0 | 0 |
| PIT RUN_ERROR | 0 | 0 | 0 | 0 |
| PIT MEMORY_ERROR | 0 | 0 | 0 | 0 |
| PIT NON_VIABLE | 0 | 0 | 0 | 0 |
| PIT cumulative mutation-test executions | 0 | 26 | 0 | 42 |

Mutation score is `KILLED / all native mutants`, retaining `NO_COVERAGE` in the denominator. Test strength is `KILLED / (KILLED + SURVIVED)`; a zero denominator is N/A even where PIT's native console displays 100%. No equivalent-mutant exclusions were introduced. A surviving mutant was not detected by a covering test; this report does not claim that every survivor represents a distinct real defect. See [PIT's outcome definitions](https://pitest.org/quickstart/basic_concepts/).

JaCoCo and PIT line coverage are separate observations and are not substituted for each other. JaCoCo's branch definition does not count exception handling as branches, so 100% branch coverage does not establish complete exceptional-behavior coverage. See [JaCoCo's counter definitions](https://www.jacoco.org/jacoco/trunk/doc/counters.html). Coverage and mutation measurements do not establish correctness against an independent specification.

## Execution outcomes

All eight selected before/after phases completed with process exit code 0 and preserved native results. The counters below were checked against the archived Surefire XML, PIT mutation XML, execution receipts, and logs.

### JUnit/Surefire with JaCoCo instrumentation

| Condition | Phase | Process exit code | Reported cases | Passed | Failures | Errors | Skips |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WIT-UP JSON | [jacoco-before](../supplements/json/001/001/executions/002/result.json) | 0 | 1541 | 1535 | 0 | 0 | 6 |
| WIT-UP JSON | [jacoco-after](../supplements/json/001/001/executions/004/result.json) | 0 | 1551 | 1545 | 0 | 0 | 6 |
| Java source | [jacoco-before](../supplements/java-source/001/005/executions/002/result.json) | 0 | 1541 | 1535 | 0 | 0 | 6 |
| Java source | [jacoco-after](../supplements/java-source/001/005/executions/004/result.json) | 0 | 1561 | 1555 | 0 | 0 | 6 |

Reported totals include six intrinsic skips in the existing project suite. Passed cases equal reported cases minus failures, errors, and skips. The generated test contributes 10 cases after for JSON and 20 after for Java source, all passed, with no failures, errors, or skips. The before measurements ran the existing project suite; zero target coverage does not mean that no project tests ran.

Native Surefire archives: [JSON before](../supplements/json/001/001/executions/002/surefire-reports.zip), [JSON after](../supplements/json/001/001/executions/004/surefire-reports.zip), [Java before](../supplements/java-source/001/005/executions/002/surefire-reports.zip), and [Java after](../supplements/java-source/001/005/executions/004/surefire-reports.zip).

### PIT validation and mutation testing

| Condition | Phase | Process exit code | Classes sent to worker | Cumulative executions against mutants | KILLED | SURVIVED | NO_COVERAGE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WIT-UP JSON | [pit-before](../supplements/json/001/001/executions/003/output.log) | 0 | 374 | 0 | 0 | 0 | 14 |
| WIT-UP JSON | [pit-after](../supplements/json/001/001/executions/005/output.log) | 0 | 375 | 26 | 1 | 8 | 5 |
| Java source | [pit-before](../supplements/java-source/001/005/executions/003/output.log) | 0 | 374 | 0 | 0 | 0 | 14 |
| Java source | [pit-after](../supplements/java-source/001/005/executions/005/output.log) | 0 | 377 | 42 | 7 | 3 | 4 |

Each PIT phase produced 14 native mutant results. Classes sent to the worker come from the log's `Sending ... test classes to minion` entry. Cumulative executions come from `Ran ... tests` and equal the sum of the mutations' `numberOfTestsRun` attributes. These are distinct from the JUnit case totals. In both before phases, PIT completed its initial coverage calculation, classified all 14 mutants as `NO_COVERAGE`, and therefore performed zero executions against mutants. That zero does not describe the initial validation/coverage stage.

PIT uses its own runner and does not emit a Surefire case/failure/error/skip summary for these invocations. Its collected results are the native counters above and the coverage and mutation metrics in the preceding section. All four processes completed with `--skipFailingTests false`; the generic `suiteCounts: null` in their execution receipts denotes the absence of a Surefire summary, not a missing PIT measurement. Infrastructure failures from other invocations are excluded from these result totals and remain in their original diagnostic records.

Native PIT mutation artifacts: [JSON before](../supplements/json/001/001/executions/003/artifacts/001-mutations.xml), [JSON after](../supplements/json/001/001/executions/005/artifacts/001-mutations.xml), [Java before](../supplements/java-source/001/005/executions/003/artifacts/001-mutations.xml), and [Java after](../supplements/java-source/001/005/executions/005/artifacts/001-mutations.xml).

## Findings and improvement opportunities

### What explains the additional mutant detections

The Java-source suite detects the one mutant detected by the JSON suite plus six additional mutants. There are no JSON-exclusive detections in this pair. The following mapping comes directly from the preserved [JSON mutation XML](../supplements/json/001/001/executions/005/artifacts/001-mutations.xml) and [Java-source mutation XML](../supplements/java-source/001/005/executions/005/artifacts/001-mutations.xml). Source line numbers refer to `PeekableInputStream.java` in the [preserved production-source archive](../runs/java-source/001/inputs/production-source.zip).

| Overload and source line | Mutation | JSON outcome | Java-source outcome | Killing case recorded by PIT for Java source |
| --- | --- | --- | --- | --- |
| `peek(byte[])`, 63 | Size guard boundary: `>` becomes `>=` | SURVIVED | KILLED | `peekArrayPropagatesReadFailureDuringRefill`, prefix length 1 |
| `peek(byte[])`, 67 | Refill condition forced false | SURVIVED | KILLED | `peekArrayPropagatesReadFailureDuringRefill`, prefix length 1 |
| `peek(byte[])`, 68 | `fillBuffer()` call removed | NO_COVERAGE | KILLED | `peekArrayPropagatesReadFailureDuringRefill`, prefix length 1 |
| `peek(byte[],int,int)`, 85 | Size guard boundary: `>` becomes `>=` | SURVIVED | KILLED | `peekSliceRejectsNegativeLength` |
| `peek(byte[],int,int)`, 89 | Refill condition forced false | SURVIVED | KILLED | `peekSlicePropagatesReadFailureBeforeInvalidSlice`, prefix length 0 |
| `peek(byte[],int,int)`, 90 | `fillBuffer()` call removed | SURVIVED | KILLED | `peekSlicePropagatesReadFailureBeforeInvalidSlice`, prefix length 0 |

Five additional detections therefore have recorded killing cases that inject an `IOException` through the public `InputStream` dependency. The [frozen Java-source test](../runs/java-source/001/evidence/test-source/PeekableInputStreamTest.java) requires that exception to propagate through the target call and checks its identity with `assertSame`. The [frozen JSON test](../runs/json/001/evidence/test-source/PeekableInputStreamTest.java) uses only empty `ByteArrayInputStream` fixtures and exception-type assertions. Its cases do not exercise the same read-failure observations. This provides a concrete fixture-level explanation for most of the measured detection difference.

The remaining additional detection shows why an exception-type assertion can be insufficient. In `peekSliceRejectsNegativeLength`, the request array length equals capacity 1 and the requested slice length is -1. The original target reaches the delegated length guard and throws `IllegalArgumentException` with `Invalid length: -1`. Changing the target size guard to `>=` instead throws `IllegalArgumentException` from the earlier size check. The type remains the same; the expected-message assertion distinguishes the two paths. This explanation is a trace through the preserved source and test, supported by PIT's recorded killing case. Messages here are source-derived characterization observations, not independently established API guarantees.

PIT records a killing test for each detected mutant, not an exhaustive list of every case that could detect it. This mapping does not measure what would happen if cases were removed, nor does it isolate the effect of test count from fixture and oracle choices. All 14 native mutants modify `peek`; none modifies a constructor. Additional constructor cases cannot explain detections of these particular mutations.

### Specific remaining gaps

Both suites leave the same three covered mutants with status `SURVIVED`. The following candidates are derived from source and test inspection; they were not implemented or executed.

| Remaining mutation | Why the existing observations can miss it | Concrete improvement candidate |
| --- | --- | --- |
| `peek(byte[])`, line 63: size guard removed | An oversized request may still produce `IllegalArgumentException` from the downstream buffer length guard. A type-only assertion can accept an exception from the wrong validation step. | Capacity 1 and a two-byte request: distinguish the original size guard using its supported message, or use a read-failing input to make an incorrectly attempted refill observable. The expected original result remains `IllegalArgumentException`. |
| `peek(byte[])`, line 67: refill boundary `<` becomes `<=` | The existing equality case uses an empty input; an extra refill does not change the asserted offset exception. | Empty comparison array, capacity 1, initially empty buffer, and an input that throws on its first read. The original skips refill and throws the delegated `IllegalArgumentException`; an erroneous refill would expose `IOException`. |
| `peek(byte[],int,int)`, line 89: refill boundary `<` becomes `<=` | The corresponding equality case does not make an extra refill observably different. | The same empty-array/read-failure fixture with offset 0 and length 0 distinguishes the delegated offset exception from a refill failure. |

The boundary transformations follow the [official PIT mutator definitions](https://pitest.org/quickstart/mutators/#CONDITIONALS_BOUNDARY). These candidates identify observable distinctions through public calls; they do not require private-state modification. Their runtime detection remains unmeasured, and no survivor is excluded or declared equivalent.

The four mutants that replace boolean returns at lines 70 and 92 are `NO_COVERAGE` in both suites. They concern successful match/mismatch results, which the generation prompts explicitly excluded. Their absence is therefore a scope observation, rather than evidence of four missing exception cases. The published mutation scores retain all 14 mutants. Studying those four return mutations would require a separately defined experiment permitting successful-return assertions.

### Where the current JSON information falls short

A read-only review of the original exports, using the verified copies in the [input backup inventory](../../../docs/input-backups.json), selected package `org.apache.commons.io.input.buffer`, class `PeekableInputStream`, and methods `<init>` or `peek`. Joining on `artifact` and `pathId` yields the same 100 consistent pairs documented in the [scenario audit](../runs/json/001/evidence/test-scenarios.json): 31 SAT and 69 UNSAT. Each export contains 49 records for each `peek` overload and 2 for the two-argument constructor; none is for the one-argument constructor. The following counts concern these selected records only.

| Exception type | All selected summary records | SAT records | SAT records associated with generated tests | SAT records left without supported fixtures |
| --- | --- | --- | --- | --- |
| `IllegalArgumentException` | 17 | 15 | 8 | 7 |
| `NullPointerException` | 58 | 4 | 2 | 2 |
| `ArrayIndexOutOfBoundsException` | 24 | 12 | 0 | 12 |
| `NegativeArraySizeException` | 1 | 0 | 0 | 0 |
| `IOException` | 0 | 0 | 0 | 0 |
| Total | 100 | 31 | 10 | 21 |

Three different problems follow from these records, and they call for different interventions:

1. **Missing scenarios.** No selected record describes `IOException`. Under the original prompt, the generator could not invent a read-failure scenario unsupported by the exports. Five additional native mutant detections are attributed to precisely that family in the Java-source suite. This motivates investigating dependency-failure modeling and export completeness. It is not a general absence of propagation metadata: 84 selected summaries already have `throwSiteKind: CALLEE_PROPAGATED` and propagation information. The missing read-failure family is established; the reason it was omitted by the producing WIT-UP version is not.
2. **Scenarios present, but public construction unsupported.** All 12 SAT `ArrayIndexOutOfBoundsException` candidates remained unrepresented. The [recorded reasons](../runs/json/001/evidence/peekable-input-stream-report.md#sat-records-without-generated-public-fixtures) include private start offsets, byte counts, capacity relationships, and matched-content conditions. Other candidates require a null private buffer or an unsupported populated state. The improvement is to connect symbolic state to valid construction and public setup sequences, and to distinguish unsupported reachability from demonstrated unreachability. More SAT records alone would not resolve this problem, and the evidence does not establish that all 21 candidates should become tests.
3. **Exception type present, but origin insufficiently distinguished.** The selected summary fields include `exceptionType`, `constraints`, `throwSiteKind`, `provenance`, and `provenances`, but no expected-message field. For example, slice path `#31` at results position 13773 and summaries position 61230 supports negative length and delegated `IllegalArgumentException`; it does not provide the `Invalid length: -1` message used by the Java-source oracle. The associated line-85 mutant preserves the exception class while changing its origin. A supported message, cause, identity, or another public observation can strengthen this distinction, depending on what the extracted information actually establishes.

These findings separate information absent from the exports from information that exists but was not converted into an effective fixture or oracle. Repeated generation with unchanged JSON can investigate the latter; it cannot legitimately supply a scenario that remains outside the allowed inputs. Expected messages derived from implementation remain characterization oracles, not independent API guarantees.

### Improvements and measurements that would answer the research question

The following comparisons are proposed diagnostic steps, not newly executed experiments. Their purpose is to discover the minimum useful information needed by a generator that continues to receive JSON instead of production source.

| Proposed comparison | What changes in the input or process | Hypothesis and observation to measure |
| --- | --- | --- |
| Repeat generation with unchanged JSON | Keep the raw exports and generation rules fixed; use independent fresh chats and checkouts. | Determine whether existing constraints and propagation metadata yield additional supported fixtures or stronger oracles across generations. Record every outcome and its spread, not only the best score. |
| Add dependency-failure information | Export supported read-failure conditions, how the dependency can be configured through an accessible API, and the exception propagated by the target. Compare with an unchanged-JSON control under the same generation rules. | Check whether generated target calls now assert `IOException`, whether the five associated mutation gaps close, and whether previously detected mutants remain detected. This is the first content improvement suggested by the observed detection gap. |
| Add public construction and state information | Supply supported constructor constraints, capacity relationships, initial state, public setup sequences, and explicit unresolved reachability. Evaluate this addition separately. | Count previously unsupported candidates that gain a justified public fixture and an observed target exception; inspect array-bounds scenarios and record cases still unsupported or established unreachable. Do not force private state to convert all SAT models. |
| Add observable exception-origin information | Supply supported messages, causes, identity relationships, or observations that distinguish competing validations. Evaluate this addition separately. | Check whether an oracle detects a wrong validation origin despite the same exception type, especially the line-85 mutation and shared size-guard survivor. Assess refill-boundary survivors with an observable public fixture. |
| Combine additions, then compare with Java source | Examine both individual contributions and combinations; retain unchanged JSON and Java source as comparison conditions. | Determine whether JSON-based generation closes the identified behavioral and mutant-detection gaps without losing existing detections. Similar scores alone do not establish equivalent scenarios, repeatability, or general source independence. |

Some additions may depend on each other: an informative oracle cannot compensate for a fixture that never reaches the relevant behavior. An addition that produces no gain in isolation may still help in combination, or the generator may have failed to use it effectively. Record those interactions instead of attributing every change to one field.

Before a new comparison, freeze the input variants, common generation instructions, planned independent-generation counts, and the decision criteria. Do not change the prompt and JSON content together when the intended claim is about one of them. If the prompt itself is improved, compare that change with unchanged JSON as a separate intervention. Retain the model and reasoning effort where reproducible, record actual settings, and keep suite size as an outcome rather than fixing it to 10 or 20.

For each generated suite, measure: compilation and executed-test outcomes; supported versus unresolved public fixtures; exception families and overloads exercised through target calls; the source of each oracle and whether exception origin is distinguishable; and the existing paired JaCoCo/PIT counters. Keep all 14 mutant identities in the reported score and compare which mutants change status. Separately explain the four normal-return mutations outside the exception-only scope. The 31 original SAT candidates remain a traceability set, not a denominator for path coverage; newly exported scenarios need their own recorded identities. Constructor behavior also requires explicit exception observations because the current 14 mutations all concern `peek`.

A proposed sign of progress is a supported, passing test for a previously missing exceptional behavior or a stronger oracle that detects a previously surviving mutation, without losing earlier detections. A claim of sufficiency needs criteria registered before the new generations and evidence across the planned repetitions; matching 7/14 on this known target alone would not prove general sufficiency. Additional targets would be needed for a claim beyond `PeekableInputStream`.

The information added to JSON needs provenance and a reproducible derivation. If fields are manually supplied after consulting Java source, label that condition as manually enriched JSON: it can test whether those facts help the generator, but does not demonstrate automatic extraction by WIT-UP or an end-to-end process without source access. Investigate whether the required information can be extracted from the permitted analyzed artifacts, and recover the analyzed-JAR identity and producing tool revision before attributing the improvement to WIT-UP. A JSON containing copied source or a ready-made test would answer a different question. Improvements designed from this pilot are exploratory on this target; later targets should not expose their reference tests or evaluation feedback to generators.

Any accepted comparison requires new reserved generations, assigned input snapshots, freezing before execution, and separately authorized evaluation supplements under the [preservation methodology](../../../docs/run-methodology.md). Existing tests and sealed runs remain the baseline evidence. These proposals do not start a generation, change WIT-UP, or execute measurements; further experimental work remains pending feedback from Professor Rodrigo and Doctoral Student Adriano.

## Conclusions

**WIT-UP JSON was sufficient to generate 10 passing exception tests without consulting production source. The resulting suite did not match the observed mutant detection of the Java-source suite: 1/14 versus 7/14. This establishes feasibility with specific gaps; it does not establish that source code is indispensable.**

The actionable result is a prioritized set of JSON improvements: represent supported read-failure scenarios absent from the selected records, connect existing symbolic conditions to constructible public fixtures, and supply observable details that distinguish the expected exception's origin. The central question is whether those additions let a generator prepare more supported scenarios and assert their exceptional outcomes effectively while continuing to receive JSON only. More informative fixtures and oracles explain specific native mutant detections; counting tests or covered lines alone does not answer whether the information is sufficient.

The next measurement should ask whether independently generated tests from each targeted JSON improvement close the identified behavioral and detection gaps under the same protocol. Separate comparisons of unchanged JSON, individual additions, and their combination can distinguish limitations of the exported information from variation in how the generator uses it. Until those comparisons are performed, enriched JSON remains a plausible improvement to evaluate, and equivalent effectiveness without generator access to source remains unestablished.

## Interpretation and pilot scope

The comparison supports a bounded observation about these two suites: their target execution coverage and detection of the same generated mutations under the recorded measurement configuration. It does not estimate an average effect, statistical significance, or a general ranking of information sources.

The prompts did not prescribe a fixed test count: the 10-versus-20 case count and the different assertions are outcomes to explain, not a protocol defect. The mutant/test mapping above identifies specific detection mechanisms. It does not quantify separate effects of source access, case count, fixture choice, and oracle strength, or establish reproduction of every symbolic internal path.

The initial generation turn in each original session records `model: gpt-6.1-sol` and `effort: xhigh`. Both session headers record Codex runtime `cli_version: 0.162.0-alpha.17.2`. Distinct session starts and initial prompts, together with the operator's confirmation, establish fresh chats without prior conversation history. The recovered evidence and exact session locators are preserved in linked annotations for [the JSON generation](../supplements/json/001/002/report.md) and [the Java-source generation](../supplements/java-source/001/006/report.md). The earlier unknown fields remain verbatim in sealed records and reproduced environment snapshots; the annotations supply the recovered facts without rewriting those records.

The JSON generation remains a retrospective import, and its original freeze timestamp was not recorded. The session's CLI version does not identify a separate desktop UI build. The analyzed WIT-UP JAR bytes and producing WIT-UP revision remain unverified. These specific provenance boundaries do not make the recovered model, reasoning effort, or fresh-chat conditions unknown.

## Diagnostics retained outside result totals

Historical JSON startup failures and exploratory PIT failures remain in the original sealed diagnostic record. Four earlier Java-source evaluations remain sealed incomplete, covering preparation parsing, skipped PIT discovery, and relative-resource/native-directory failures. Those operations do not supply the valid measurement metrics and are not counted as failures of generated cases that did not execute. Their actual process failures and any unmutated existing-test failures remain preserved.

The Java-source generation also retains two findings from a separate direct Checkstyle check of its frozen test: missing package-info.java and missing Javadoc on a private fixture constructor. They were not repaired after freezing and are separate from JUnit outcomes. The selected full-suite Maven lifecycles and PIT processes succeeded; this statement does not reclassify the separate style check as passing.

## Reproduction environment and configuration

| Component | Exact version or configuration |
| --- | --- |
| Generation model / reasoning effort | GPT-6.1 Sol (`gpt-6.1-sol`) / Extra High (`xhigh`) |
| Recorded Codex runtime (`cli_version`) | 0.162.0-alpha.17.2 |
| Java vendor/runtime | Eclipse Temurin; 1.8.0_504-b01 |
| JVM / javac | 25.504-b01 / 1.8.0_504 |
| Java source/target | 1.8 / 1.8 |
| Maven | 3.9.16; build 2bdd9fddda4b155ebf8000e807eb73fd829a51d5 |
| Commons IO / Apache Commons parent | 2.7-SNAPSHOT / 50 |
| JUnit Jupiter / Platform | 5.5.2 / 1.5.2 |
| Surefire | 2.22.2 |
| JaCoCo agent and CLI | 0.8.4 |
| PIT CLI, entry, core / JUnit 5 adapter | 1.15.2 / 1.2.2 |
| Maven dependency / help plugins | 3.6.1 / 3.5.1 |
| Python | 3.13.15 |
| PowerShell | 7.6.5 |
| OS | Microsoft Windows 10.0.26300; X64 |

Exact executable locations, flags, OS observations, and process environment values are recorded before every invocation. The commands select JDK 8 for the process and direct TEMP/TMP and the Maven repository to the evaluation's exclusive D: working directory. Dependency configuration and bytes are identical between conditions; the complete runtime inventory appears below.

```json
{
  "schemaVersion": 1,
  "protocol": "paired-full-suite",
  "configurationRevision": 4,
  "baselineCommit": "11f0abe7a3fb6954b2985ca4ab0697b2fb489e84",
  "javaRuntime": "1.8.0_504-b01",
  "javac": "1.8.0_504",
  "maven": "3.9.16",
  "surefire": "2.22.2",
  "junitJupiter": "5.5.2",
  "jacoco": "0.8.4",
  "pit": "1.15.2",
  "pitJunit5Adapter": "1.2.2",
  "targetClass": "org.apache.commons.io.input.buffer.PeekableInputStream",
  "jacocoTestSelection": "all existing project tests; add only the frozen generated file after",
  "pitTestSelection": "org.apache.commons.io.*",
  "pitSourceDiscovery": "Use the assigned checkout's src/main/java and src/test/java, with compiled outputs from its own preceding JaCoCo build.",
  "pitLauncher": "PIT 1.15.2 command-line launcher executed natively from the phase checkout; both native and Java relative fixture roots match Surefire.",
  "mutationEngine": "gregor",
  "mutators": ["DEFAULTS"],
  "threads": 1,
  "timeoutFactor": 1.25,
  "timeoutConstantMilliseconds": 3000,
  "jvmArguments": ["-Xmx256m"],
  "jacocoAppend": true,
  "jacocoFreshExecutionFileRequired": true,
  "pairing": "Identical production class bytes, configuration, and existing tests; only the frozen generated test differs.",
  "mutationScore": "KILLED / total native mutants, retaining NO_COVERAGE; zero denominator is not applicable.",
  "testStrength": "KILLED / (KILLED + SURVIVED); zero denominator is not applicable.",
  "invalidMutationStatuses": ["TIMED_OUT", "RUN_ERROR", "MEMORY_ERROR", "NON_VIABLE"],
  "baselineFailurePolicy": "Preserve diagnostics and seal the evaluation incomplete; do not change scope, skip tests, or relax gates."
}
```

### Complete runtime JAR inventory

Paths are relative to each evaluation's `maven-repository` and encode group, artifact, and exact version. The hash column is common to both evaluations. The recorded classpaths retain ordering and distinguish project Commons Lang 3.9 from launcher Commons Lang 3.12.0.

| Maven artifact path | SHA-256 | Bytes |
| --- | --- | --- |
| `com/google/guava/guava/18.0/guava-18.0.jar` | `d664fbfc03d2e5ce9cab2a44fb01f1d0bf9dfebeccc1a473b1f9ea31f79f6f99` | 2256213 |
| `com/google/jimfs/jimfs/1.1/jimfs-1.1.jar` | `c4828e28d7c0a930af9387510b3bada7daa5c04d7c25a75c7b8b081f1c257ddd` | 206691 |
| `net/bytebuddy/byte-buddy-agent/1.9.10/byte-buddy-agent-1.9.10.jar` | `8ed739d29132103250d307d2e8e3c95f07588ef0543ab11d2881d00768a5e182` | 43420 |
| `net/bytebuddy/byte-buddy/1.9.10/byte-buddy-1.9.10.jar` | `2936debc4d7b6c534848d361412e2d0f8bd06f7f27a6f4e728a20e97648d2bf3` | 3272730 |
| `org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar` | `d919d904486c037f8d193412da0c92e22a9fa24230b9d67a57855c5c31c7e94e` | 587402 |
| `org/apache/commons/commons-lang3/3.9/commons-lang3-3.9.jar` | `de2e1dcdcf3ef917a8ce858661a06726a9a944f28e33ad7f9e08bea44dc3c230` | 503880 |
| `org/apache/commons/commons-text/1.10.0/commons-text-1.10.0.jar` | `770cd903fa7b604d1f7ef7ba17f84108667294b2b478be8ed1af3bffb4ae0018` | 238400 |
| `org/apiguardian/apiguardian-api/1.1.0/apiguardian-api-1.1.0.jar` | `a9aae9ff8ae3e17a2a18f79175e82b16267c246fbbd3ca9dfbbb290b08dcfdd4` | 2387 |
| `org/junit-pioneer/junit-pioneer/0.3.0/junit-pioneer-0.3.0.jar` | `e8569ccd96843a1f1a3d5330fa731cdaf9038c1f7c5b9ba0b47cf89346357d32` | 26655 |
| `org/junit/jupiter/junit-jupiter-api/5.5.2/junit-jupiter-api-5.5.2.jar` | `249a2fdbd3931987c0298d00ca08ed248496e0fc11e0463c08c4f82e0cc79b1c` | 141766 |
| `org/junit/jupiter/junit-jupiter-engine/5.5.2/junit-jupiter-engine-5.5.2.jar` | `6d777da9876e2ef7a0336e8f098f8d74a5a64f810aa3a4a2f5f3b766ce97837b` | 219630 |
| `org/junit/jupiter/junit-jupiter-params/5.5.2/junit-jupiter-params-5.5.2.jar` | `fd49c7fd9d0f7f1e5b5f6982254cee79177fa2e76a37fdee0466e64f975567b5` | 549435 |
| `org/junit/jupiter/junit-jupiter/5.5.2/junit-jupiter-5.5.2.jar` | `72fb607d1778cb870a6e009432b51619a70b88d7056f708ab1e0aaf72ef25452` | 6161 |
| `org/junit/platform/junit-platform-commons/1.5.2/junit-platform-commons-1.5.2.jar` | `fc44afdfc0f20c85e71a66e7943281aef3bc1e0fd62d2d69a36cb6901e682c10` | 91709 |
| `org/junit/platform/junit-platform-engine/1.5.2/junit-platform-engine-1.5.2.jar` | `ff20ba4ad8c00ef17baef9c55512f9c02d9a68740f7f1ac01a9a6aa0239931f8` | 163866 |
| `org/junit/platform/junit-platform-launcher/1.5.2/junit-platform-launcher-1.5.2.jar` | `c1f6473ddd343550b42e94072aff9417ff38398f8b6bafe27b785aebcdaa660b` | 99589 |
| `org/mockito/mockito-core/3.0.0/mockito-core-3.0.0.jar` | `ae2efd8f05ceda5ed9c802a43265a95adfa885ca5535a8476a7aaa0b15b95abb` | 591095 |
| `org/objenesis/objenesis/2.6/objenesis-2.6.jar` | `5e168368fbc250af3c79aa5fef0c3467a2d64e5a7bd74005f25d8399aeb0708d` | 55684 |
| `org/opentest4j/opentest4j/1.2.0/opentest4j-1.2.0.jar` | `58812de60898d976fb81ef3b62da05c6604c18fd4a249f5044282479fc286af2` | 7653 |
| `org/pitest/pitest-command-line/1.15.2/pitest-command-line-1.15.2.jar` | `1b1d66ae14ffc162625c7c49cc4c55f9cebce49083239648ed2139b41570e5b3` | 741431 |
| `org/pitest/pitest-entry/1.15.2/pitest-entry-1.15.2.jar` | `ebcfcd29387a8c60a965a484482995330fd57a4fa9831f3b7553eb93578e2b0d` | 751223 |
| `org/pitest/pitest-junit5-plugin/1.2.2/pitest-junit5-plugin-1.2.2.jar` | `2dbf5bbbc714ff702eb2e82c047a5b44a74c47cc9171c3a7a8dc78783bf099b9` | 12724 |
| `org/pitest/pitest/1.15.2/pitest-1.15.2.jar` | `29befcf6733680375aff5089ad02dab9166aa18760f82fc085adb6c4959362b6` | 611950 |

### Invoked Maven plugins and goals

| Plugin | Version | Goal |
| --- | --- | --- |
| animal-sniffer | 1.18 | check |
| antrun | 1.8 | run |
| apache-rat | 0.13 | check |
| build-helper | 3.0.0 | parse-version |
| buildnumber | 1.4 | create |
| bundle | 4.2.1 | manifest |
| clean | 3.1.0 | clean |
| compiler | 3.8.1 | compile |
| compiler | 3.8.1 | testCompile |
| dependency | 3.6.1 | build-classpath |
| dependency | 3.6.1 | copy |
| dependency | 3.6.1 | list |
| enforcer | 3.0.0-M2 | enforce |
| help | 3.5.1 | effective-pom |
| remote-resources | 1.5 | process |
| resources | 3.1.0 | resources |
| resources | 3.1.0 | testResources |
| surefire | 2.22.2 | test |

## Commands and evaluation-specific parameters

The prescribed generation test command was `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test`. Its historical JSON supplemental result was 10 passing cases; its Java-source initial result was 20 passing cases. This evaluation did not regenerate either suite.

The following are the actual reserved commands for the selected measurements, executed from `D:/Projects/wit-up`. Each phase script, its environment assignments, and every native command is reproduced in the linked evaluation report. The common commands and resolved phase paths follow, so command parameters are not left for the reader to discover.

| Condition | Phase | Reserved command |
| --- | --- | --- |
| WIT-UP JSON | preflight | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/preflight.ps1"` |
| WIT-UP JSON | jacoco-before | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/jacoco-before.ps1"` |
| WIT-UP JSON | pit-before | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/pit-before.ps1"` |
| WIT-UP JSON | jacoco-after | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/jacoco-after.ps1"` |
| WIT-UP JSON | pit-after | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/pit-after.ps1"` |
| Java source | preflight | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/preflight.ps1"` |
| Java source | jacoco-before | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/jacoco-before.ps1"` |
| Java source | pit-before | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/pit-before.ps1"` |
| Java source | jacoco-after | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/jacoco-after.ps1"` |
| Java source | pit-after | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/pit-after.ps1"` |

| Condition | Phase | Reserved at (UTC) | Recorded at (UTC) |
| --- | --- | --- | --- |
| WIT-UP JSON | preflight | 2026-10-13T01:01:41.056505+00:00 | 2026-10-13T01:02:14.353446+00:00 |
| WIT-UP JSON | jacoco-before | 2026-10-13T01:03:04.753039+00:00 | 2026-10-13T01:06:16.599848+00:00 |
| WIT-UP JSON | pit-before | 2026-10-13T01:07:46.362553+00:00 | 2026-10-13T01:08:28.060212+00:00 |
| WIT-UP JSON | jacoco-after | 2026-10-13T01:08:52.120850+00:00 | 2026-10-13T01:11:44.532157+00:00 |
| WIT-UP JSON | pit-after | 2026-10-13T01:12:36.601361+00:00 | 2026-10-13T01:13:18.307792+00:00 |
| Java source | preflight | 2026-10-12T23:45:12.858575+00:00 | 2026-10-12T23:45:29.019738+00:00 |
| Java source | jacoco-before | 2026-10-12T23:46:20.082759+00:00 | 2026-10-12T23:49:09.297710+00:00 |
| Java source | pit-before | 2026-10-12T23:49:25.149708+00:00 | 2026-10-12T23:50:06.158356+00:00 |
| Java source | jacoco-after | 2026-10-12T23:51:06.761782+00:00 | 2026-10-12T23:53:58.618563+00:00 |
| Java source | pit-after | 2026-10-12T23:54:19.521526+00:00 | 2026-10-12T23:55:01.261218+00:00 |

### WIT-UP JSON: exact substitutions

```json
{
  "evaluationRoot": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001",
  "workingDirectory": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001",
  "javaHome": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1",
  "agentJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.agent-0.8.4-runtime.jar",
  "cliJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.cli-0.8.4-nodeps.jar",
  "phases": {
    "jacoco-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/jacoco-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/jacoco-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-before/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-before/jacoco.exec"
      }
    },
    "pit-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/pit-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/pit-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-before/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-before/linecoverage.xml"
      },
      "phaseClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-before-classpath.txt",
      "toolClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt"
    },
    "jacoco-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/jacoco-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/jacoco-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-after/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-after/jacoco.exec"
      }
    },
    "pit-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/pit-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/pit-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-after/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-after/linecoverage.xml"
      },
      "phaseClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-after-classpath.txt",
      "toolClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt"
    },
    "preflight": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/preflight.ps1",
      "scope": "Fetch and verify pinned JaCoCo tools; preserve effective POM and exact resolved project dependencies; no test execution",
      "reports": null,
      "artifacts": {
        "effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/effective-pom.xml",
        "dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependencies.txt",
        "dependency-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependency-hashes.json",
        "launcher-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt",
        "project-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/project-classpath.txt",
        "launcher-effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-effective-pom.xml",
        "launcher-dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-dependencies.txt",
        "runtime-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/runtime-hashes.json",
        "before-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-before-classpath.txt",
        "after-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-after-classpath.txt"
      }
    }
  },
  "pitLauncherPom": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml"
}
```

### WIT-UP JSON: observed preparation environment

```json
{
  "observedAt": "2026-10-13T01:00:45.7609866Z",
  "java": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\bin\\java.exe",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "openjdk version \"1.8.0_504\"",
      "OpenJDK Runtime Environment (Temurin)(build 1.8.0_504-b01)",
      "OpenJDK 64-Bit Server VM (Temurin)(build 25.504-b01, mixed mode)"
    ]
  },
  "javac": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\bin\\javac.exe",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "javac 1.8.0_504"
    ]
  },
  "maven": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16\\bin\\mvn.cmd",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "Apache Maven 3.9.16 (2bdd9fddda4b155ebf8000e807eb73fd829a51d5)",
      "Maven home: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16",
      "Java version: 1.8.0_504, vendor: Temurin, runtime: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\jre",
      "Default locale: en_US, platform encoding: Cp1252",
      "OS name: \"windows 11\", version: \"10.0\", arch: \"amd64\", family: \"windows\""
    ]
  },
  "python": {
    "executable": "D:\\Projects\\wit-up\\.venv\\Scripts\\python.exe",
    "arguments": [
      "--version"
    ],
    "exitCode": 0,
    "output": [
      "Python 3.13.15"
    ]
  },
  "os": {
    "description": "Microsoft Windows 10.0.26300",
    "version": "Microsoft Windows NT 10.0.26300.0",
    "architecture": "X64",
    "powershell": "7.6.5"
  },
  "processEnvironment": {
    "JAVA_HOME": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1",
    "PATH": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16\\bin;D:\\Projects\\wit-up\\.venv\\Scripts;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-25.0.4+101.0.LTS\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16/bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\node\\22.23.2;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\Scripts;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\uv\\0.12.23;C:\\Users\\edyko\\AppData\\Local\\mise\\shims;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\.codex\\tmp\\arg0\\codex-arg0pgGc3k;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\libheif\\libheif\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\jxrlib\\jxrlib\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\poppler\\Library\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\override;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA App\\NvDLISR;C:\\Program Files\\dotnet\\;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\platform-tools;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\emulator;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\cmdline-tools\\latest\\bin;C:\\Program Files\\GitHub CLI\\;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\cmd;C:\\Users\\edyko\\AppData\\Local\\codegraph\\current\\bin;C:\\Users\\edyko\\AppData\\Local\\Programs\\OpenAI\\Codex\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\edyko\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files\\JetBrains\\PyCharm 2026.2.1\\bin;C:\\Program Files\\JetBrains\\IntelliJ IDEA 2026.2.1\\bin;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WinGet\\Packages\\jdx.mise_Microsoft.Winget.Source_8wekyb3d8bbwe\\mise\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\fallback;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\node\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\git\\cmd;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\9a7ba4b9ea0c44a3;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\2e5e00daee91c61d",
    "MAVEN_OPTS": "-DargLine=",
    "MAVEN_ARGS": null,
    "TEMP": "D:\\Projects\\experiment-workspaces\\peekable-input-stream\\.preparation\\json-001-evaluation-001\\temp",
    "TMP": "D:\\Projects\\experiment-workspaces\\peekable-input-stream\\.preparation\\json-001-evaluation-001\\temp",
    "JAVA_TOOL_OPTIONS": null,
    "JDK_JAVA_OPTIONS": null,
    "_JAVA_OPTIONS": null
  },
  "generator": {
    "model": null,
    "settings": null,
    "applicationBuild": null,
    "reason": "This is an evaluation of preserved test bytes, not a generation. Original generation settings remain unknown in the parent record."
  }
}
```

### Java source: exact substitutions

```json
{
  "evaluationRoot": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005",
  "workingDirectory": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005",
  "javaHome": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1",
  "agentJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools/org.jacoco.agent-0.8.4-runtime.jar",
  "cliJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools/org.jacoco.cli-0.8.4-nodeps.jar",
  "phases": {
    "jacoco-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/pit-build/jacoco-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/jacoco-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-before/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-before/jacoco.exec"
      }
    },
    "pit-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/pit-build/pit-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/pit-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-before/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-before/linecoverage.xml"
      },
      "phaseClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-before-classpath.txt",
      "toolClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt"
    },
    "jacoco-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/pit-build/jacoco-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/jacoco-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-after/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-after/jacoco.exec"
      }
    },
    "pit-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/pit-build/pit-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/pit-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-after/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-after/linecoverage.xml"
      },
      "phaseClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-after-classpath.txt",
      "toolClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt"
    },
    "preflight": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/preflight.ps1",
      "scope": "Fetch and verify pinned JaCoCo tools; preserve effective POM and exact resolved project dependencies; no test execution",
      "reports": null,
      "artifacts": {
        "effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/effective-pom.xml",
        "dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependencies.txt",
        "dependency-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependency-hashes.json",
        "launcher-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt",
        "project-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/project-classpath.txt",
        "launcher-effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/launcher-effective-pom.xml",
        "launcher-dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/launcher-dependencies.txt",
        "runtime-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/runtime-hashes.json",
        "before-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-before-classpath.txt",
        "after-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-after-classpath.txt"
      }
    }
  },
  "pitLauncherPom": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml"
}
```

### Java source: observed preparation environment

```json
{
  "observedAt": "2026-10-12T23:44:07.8430530Z",
  "java": {
    "executable": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1/bin\\java.exe",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "openjdk version \"1.8.0_504\"",
      "OpenJDK Runtime Environment (Temurin)(build 1.8.0_504-b01)",
      "OpenJDK 64-Bit Server VM (Temurin)(build 25.504-b01, mixed mode)"
    ]
  },
  "javac": {
    "executable": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1/bin\\javac.exe",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "javac 1.8.0_504"
    ]
  },
  "maven": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16/bin\\mvn.cmd",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "Apache Maven 3.9.16 (2bdd9fddda4b155ebf8000e807eb73fd829a51d5)",
      "Maven home: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16",
      "Java version: 1.8.0_504, vendor: Temurin, runtime: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\jre",
      "Default locale: en_US, platform encoding: Cp1252",
      "OS name: \"windows 11\", version: \"10.0\", arch: \"amd64\", family: \"windows\""
    ]
  },
  "python": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\python.exe",
    "arguments": [
      "--version"
    ],
    "exitCode": 0,
    "output": [
      "Python 3.13.15"
    ]
  },
  "os": {
    "description": "Microsoft Windows 10.0.26300",
    "version": "Microsoft Windows NT 10.0.26300.0",
    "architecture": "X64",
    "powershell": "7.6.5"
  },
  "processEnvironment": {
    "JAVA_HOME": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1",
    "PATH": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1/bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-25.0.4+101.0.LTS\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16/bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\node\\22.23.2;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\Scripts;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\uv\\0.12.23;C:\\Users\\edyko\\AppData\\Local\\mise\\shims;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\.codex\\tmp\\arg0\\codex-arg0pgGc3k;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\libheif\\libheif\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\jxrlib\\jxrlib\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\poppler\\Library\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\override;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA App\\NvDLISR;C:\\Program Files\\dotnet\\;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\platform-tools;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\emulator;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\cmdline-tools\\latest\\bin;C:\\Program Files\\GitHub CLI\\;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\cmd;C:\\Users\\edyko\\AppData\\Local\\codegraph\\current\\bin;C:\\Users\\edyko\\AppData\\Local\\Programs\\OpenAI\\Codex\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\edyko\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files\\JetBrains\\PyCharm 2026.2.1\\bin;C:\\Program Files\\JetBrains\\IntelliJ IDEA 2026.2.1\\bin;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WinGet\\Packages\\jdx.mise_Microsoft.Winget.Source_8wekyb3d8bbwe\\mise\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\fallback;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\node\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\git\\cmd;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\9a7ba4b9ea0c44a3;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\2e5e00daee91c61d",
    "MAVEN_OPTS": "-DargLine=",
    "MAVEN_ARGS": "-Dmaven.repo.local=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/maven-repository",
    "TEMP": "D:/Projects/experiment-workspaces/peekable-input-stream/.preparation/java-source-001-evaluation-005/temp",
    "TMP": "D:/Projects/experiment-workspaces/peekable-input-stream/.preparation/java-source-001-evaluation-005/temp",
    "JAVA_TOOL_OPTIONS": null,
    "JDK_JAVA_OPTIONS": null,
    "_JAVA_OPTIONS": null
  },
  "generator": {
    "model": null,
    "settings": null,
    "applicationBuild": null,
    "reason": "This is an evaluation of preserved test bytes, not a generation. Original generation settings remain unknown in the parent record."
  }
}
```

### Common phase commands

The variables below resolve directly from each preceding substitution map: `$workingDirectory`, `$agentJar`, and `$cliJar` are top-level fields; `$phaseCheckout`, `$phaseOutput`, and `$temporaryDirectory` are that phase's `checkout`, `output`, and `temp`; `$phaseClasspathFile` and `$toolClasspathFile` are the PIT phase fields. The complete preflight commands are preserved in each evaluation report and hashed script.

```powershell
$env:JAVA_HOME = 'C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1'
$env:PATH = "$env:JAVA_HOME/bin;$env:PATH"
$env:TEMP = "$workingDirectory/temp"
$env:TMP = $env:TEMP
$env:MAVEN_ARGS = "-Dmaven.repo.local=$workingDirectory/maven-repository"
Set-Location -LiteralPath $phaseCheckout
$executionData = "$phaseOutput/jacoco.exec"
$coverageXml = "$phaseOutput/jacoco.xml"
$env:MAVEN_OPTS = "-DargLine=-javaagent:$agentJar=destfile=$executionData,append=true,includes=org.apache.commons.io.input.buffer.PeekableInputStream"
mvn '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' clean test
$classFile = "$phaseCheckout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class"
java -jar $cliJar report $executionData --classfiles $classFile --xml $coverageXml --name 'PeekableInputStream paired measurement'
```

The actual phase scripts check and record each process exit immediately, refuse reused output, and stop after a failing command. `begin` reserves the invocation before execution and `record` captures logs and native artifacts afterward.

```powershell
Set-Location -LiteralPath $phaseCheckout
$env:MAVEN_OPTS = '-DargLine='
$toolClasspath = (Get-Content -LiteralPath $toolClasspathFile -Raw).Trim()
java "-Djava.io.tmpdir=$temporaryDirectory" -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir $phaseOutput --targetClasses org.apache.commons.io.input.buffer.PeekableInputStream --targetTests 'org.apache.commons.io.*' --sourceDirs "$phaseCheckout/src/main/java" --classPathFile $phaseClasspathFile --includeLaunchClasspath false --mutationEngine gregor --mutators DEFAULTS --threads 1 --timeoutFactor 1.25 --timeoutConst 3000 --jvmArgs "-Xmx256m,-Djava.io.tmpdir=$temporaryDirectory" --outputFormats XML --timestampedReports false --exportLineCoverage true --failWhenNoMutations true --skipFailingTests false --projectBase $phaseCheckout --inputEncoding UTF-8 --outputEncoding UTF-8
```

The pinned CLI runs from the real checkout directory so existing relative-resource fixtures have the same working directory as Surefire. This resolves the recorded auxiliary-POM launch-directory problem without narrowing tests or skipping failing cases. See the [official CLI documentation](https://pitest.org/quickstart/commandline/); the pinned local CLI help and actual invocation logs establish the options used here.

## Evidence navigation

- WIT-UP JSON: [generation report](../runs/json/001/evidence/peekable-input-stream-report.md), [selected evaluation report](../supplements/json/001/001/report.md), [native executions](../supplements/json/001/001/executions/), [evaluation seal](../supplements/json/001/001/seal.json).
- Java source: [generation report](../runs/java-source/001/report.md), [selected evaluation report](../supplements/java-source/001/005/report.md), [native executions](../supplements/java-source/001/005/executions/), [evaluation seal](../supplements/java-source/001/005/seal.json).
- [Original JSON execution diagnostics](../runs/json/001/evidence/execution-diagnostics.md).
- [Registry of sealed evaluations and retained unsuccessful attempts](../README.md).

### WIT-UP JSON: complete preparation commands

The invocation wrapper selects the recorded process environment before running these commands. Its reservation and native-artifact receipts are linked above.

```powershell
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001'
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.agent:0.8.4:jar:runtime' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.cli:0.8.4:jar:nodeps' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$expectedTools = @{ 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.agent-0.8.4-runtime.jar'='1a7c1dc7280e535b9b6f383915bac5afbb9208c1af2019b4e674ca590c925c22'; 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.cli-0.8.4-nodeps.jar'='65de07ff32bcf2f945f18180d1d10cdf0e155eee2b508519bbc5f31904cd8288' }
foreach ($toolPath in $expectedTools.Keys) {
    $actualHash = (Get-FileHash -LiteralPath $toolPath -Algorithm SHA256).Hash.ToLowerInvariant()
    Write-Output "$actualHash  $toolPath"
    if ($actualHash -ne $expectedTools[$toolPath]) { throw 'Measurement tool checksum mismatch.' }
}
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$dependencyHashes = @()
foreach ($dependencyLine in Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependencies.txt') {
    $dependencyParts = $dependencyLine.Trim() -split ':', 6
    if ($dependencyParts.Count -eq 6) {
        $artifactPath = $dependencyParts[5]
        if (!(Test-Path -LiteralPath $artifactPath -PathType Leaf)) { throw "A resolved dependency is missing: $artifactPath" }
        $dependencyHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
    }
}
if ($dependencyHashes.Count -eq 0) { throw 'No resolved dependency artifacts were captured.' }
$dependencyHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependency-hashes.json' -Encoding utf8
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-DincludeScope=test' '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/project-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$toolClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt' -Raw).Trim()
$projectClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/project-classpath.txt' -Raw).Trim()
java -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport -h
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$runtimeArtifacts = @($projectClasspath -split ';') + @($toolClasspath -split ';')
$runtimeHashes = @()
foreach ($artifactPath in @($runtimeArtifacts | Select-Object -Unique)) {
    $runtimeHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
}
$runtimeHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/runtime-hashes.json' -Encoding utf8
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-before-classpath.txt' -Encoding utf8NoBOM
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-after-classpath.txt' -Encoding utf8NoBOM
exit 0
```

### WIT-UP JSON: preservation and reporting tool versions

```json
{
  "uv": [
    "uv 0.12.23 (46b84fd0b 2026-10-03 x86_64-pc-windows-msvc)"
  ],
  "git": [
    "git version 2.56.0.windows.2"
  ],
  "ruff": [
    "ruff 0.16.10"
  ],
  "pyright": [
    "pyright 1.1.414"
  ]
}
```

### Java source: complete preparation commands

The invocation wrapper selects the recorded process environment before running these commands. Its reservation and native-artifact receipts are linked above.

```powershell
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005'
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.agent:0.8.4:jar:runtime' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.cli:0.8.4:jar:nodeps' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$expectedTools = @{ 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools/org.jacoco.agent-0.8.4-runtime.jar'='1a7c1dc7280e535b9b6f383915bac5afbb9208c1af2019b4e674ca590c925c22'; 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools/org.jacoco.cli-0.8.4-nodeps.jar'='65de07ff32bcf2f945f18180d1d10cdf0e155eee2b508519bbc5f31904cd8288' }
foreach ($toolPath in $expectedTools.Keys) {
    $actualHash = (Get-FileHash -LiteralPath $toolPath -Algorithm SHA256).Hash.ToLowerInvariant()
    Write-Output "$actualHash  $toolPath"
    if ($actualHash -ne $expectedTools[$toolPath]) { throw 'Measurement tool checksum mismatch.' }
}
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$dependencyHashes = @()
foreach ($dependencyLine in Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependencies.txt') {
    $dependencyParts = $dependencyLine.Trim() -split ':', 6
    if ($dependencyParts.Count -eq 6) {
        $artifactPath = $dependencyParts[5]
        if (!(Test-Path -LiteralPath $artifactPath -PathType Leaf)) { throw "A resolved dependency is missing: $artifactPath" }
        $dependencyHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
    }
}
if ($dependencyHashes.Count -eq 0) { throw 'No resolved dependency artifacts were captured.' }
$dependencyHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependency-hashes.json' -Encoding utf8
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-DincludeScope=test' '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/project-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/launcher-effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/launcher-dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$toolClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt' -Raw).Trim()
$projectClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/project-classpath.txt' -Raw).Trim()
java -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport -h
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$runtimeArtifacts = @($projectClasspath -split ';') + @($toolClasspath -split ';')
$runtimeHashes = @()
foreach ($artifactPath in @($runtimeArtifacts | Select-Object -Unique)) {
    $runtimeHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
}
$runtimeHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/runtime-hashes.json' -Encoding utf8
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-before-classpath.txt' -Encoding utf8NoBOM
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-after-classpath.txt' -Encoding utf8NoBOM
exit 0
```

### Java source: preservation and reporting tool versions

```json
{
  "git": {
    "command": "git --version",
    "output": [
      "git version 2.56.0.windows.2"
    ],
    "exitCode": 0
  },
  "uv": {
    "command": "uv --version",
    "output": [
      "uv 0.12.23 (46b84fd0b 2026-10-03 x86_64-pc-windows-msvc)"
    ],
    "exitCode": 0
  },
  "ruff": {
    "command": "uv run --frozen ruff --version",
    "output": [
      "ruff 0.16.10"
    ],
    "exitCode": 0
  },
  "pyright": {
    "command": "uv run --frozen pyright --version",
    "output": [
      "pyright 1.1.414"
    ],
    "exitCode": 0
  }
}
```

## Appendix A: Complete frozen JSON-source Java test

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
import java.io.InputStream;

import org.junit.jupiter.api.Test;

public class PeekableInputStreamTest {

    @Test
    public void testConstructorRejectsZeroBufferSize() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final int bufferSize = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> new PeekableInputStream(input, bufferSize));
    }

    @Test
    public void testPeekArrayRejectsNullBuffer() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = null;

        // Act and Assert
        assertThrows(NullPointerException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekArrayRejectsBufferLargerThanCapacity() {
        // Arrange
        // Assume the constructor size becomes the receiver's buffer size.
        // Change modeled capacity 0 to 1 and array length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekArrayRejectsEmptyBuffer() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekSliceRejectsNullBuffer() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = null;
        final int offset = 0;
        final int length = 0;

        // Act and Assert
        assertThrows(NullPointerException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsBufferLargerThanCapacity() {
        // Arrange
        // Assume the constructor size becomes the receiver's buffer size.
        // Change modeled capacity 0 to 1 and array length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[2];
        final int offset = 0;
        final int length = 1;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsOffsetAtEmptyBufferEnd() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];
        final int offset = 0;
        final int length = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsNegativeOffset() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];
        final int offset = -1;
        final int length = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsNegativeLength() {
        // Arrange
        // Assume size 1 creates a non-null buffer with an initial byte count of 0.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[1];
        final int offset = 0;
        final int length = -1;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsLengthLargerThanCapacity() {
        // Arrange
        // Assume size 1 creates a non-null buffer of capacity 1 with an initial byte count of 0.
        // Change modeled internal capacity 0 to 1 and requested length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[1];
        final int offset = 0;
        final int length = 2;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }
}
```

## Appendix B: Complete frozen Java-source Java test

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

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

/**
 * Exception tests for the declared constructors and peek overloads.
 * Fixtures use only memory streams and require no external resources.
 */
public class PeekableInputStreamTest {

    /** Tests null input validation in the default-size constructor. */
    @Test
    public void defaultConstructorRejectsNullInput() {
        // Arrange
        final InputStream input = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> new PeekableInputStream(input));
        assertEquals("InputStream", exception.getMessage());
    }

    /** Tests that null input validation precedes invalid buffer-size validation. */
    @Test
    public void sizedConstructorRejectsNullInputBeforeInvalidBufferSize() {
        // Arrange
        final InputStream input = null;
        final int bufferSize = 0;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> new PeekableInputStream(input, bufferSize));
        assertEquals("InputStream", exception.getMessage());
    }

    /**
     * Tests both the zero boundary and the negative side of the size guard.
     * @param bufferSize the nonpositive internal buffer size
     */
    @ParameterizedTest
    @ValueSource(ints = {0, -1})
    public void sizedConstructorRejectsNonpositiveBufferSize(final int bufferSize) {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> new PeekableInputStream(input, bufferSize));
        assertEquals("Invalid buffer size: " + bufferSize, exception.getMessage());
    }

    /** Tests null array validation for the whole-array overload. */
    @Test
    public void peekArrayRejectsNullBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class, () -> stream.peek(requested));
        assertEquals("Buffer", exception.getMessage());
    }

    /** Tests null validation before slice validation. */
    @Test
    public void peekSliceRejectsNullBufferBeforeInvalidSlice() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> stream.peek(requested, -1, -1));
        assertEquals("Buffer", exception.getMessage());
    }

    /** Tests the whole-array size guard. */
    @Test
    public void peekArrayRejectsArrayLargerThanInternalBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(requested));
    }

    /** Tests that the sliced overload checks the entire array even for an empty slice. */
    @Test
    public void peekSliceRejectsOversizedArrayEvenForZeroLength() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(requested, 0, 0));
    }

    /** Tests the delegated offset guard for an empty whole array. */
    @Test
    public void peekArrayRejectsEmptyArrayAtDelegatedOffsetGuard() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[0];

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(requested));
        assertEquals("Invalid offset: 0", exception.getMessage());
    }

    /** Tests the delegated offset guard for an empty sliced array. */
    @Test
    public void peekSliceRejectsEmptyArrayAtDelegatedOffsetGuard() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[0];

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, 0));
        assertEquals("Invalid offset: 0", exception.getMessage());
    }

    /**
     * Tests both sides of offset validation before negative-length validation.
     * @param offset the negative offset or the array-length boundary
     */
    @ParameterizedTest
    @ValueSource(ints = {-1, 1})
    public void peekSliceRejectsInvalidOffsetBeforeInvalidLength(final int offset) {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, offset, -1));
        assertEquals("Invalid offset: " + offset, exception.getMessage());
    }

    /** Tests negative-length validation after a valid offset. */
    @Test
    public void peekSliceRejectsNegativeLength() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, -1));
        assertEquals("Invalid length: -1", exception.getMessage());
    }

    /** Tests the delegated length guard against internal capacity. */
    @Test
    public void peekSliceRejectsLengthLargerThanInternalBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, 2));
        assertEquals("Invalid length: 2", exception.getMessage());
    }

    /**
     * Tests original read-failure propagation immediately and after one byte is buffered.
     * @param prefixLength the number of successful one-byte reads before failure
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 1})
    public void peekArrayPropagatesReadFailureDuringRefill(final int prefixLength) {
        // Arrange
        final IOException failure = new IOException("Fixture read failure");
        final InputStream input = new PrefixThenFailInputStream(prefixLength, failure);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        final IOException exception = assertThrows(IOException.class, () -> stream.peek(requested));
        assertSame(failure, exception);
    }

    /**
     * Tests that read failures precede delegated offset and length validation.
     * @param prefixLength the number of successful one-byte reads before failure
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 1})
    public void peekSlicePropagatesReadFailureBeforeInvalidSlice(final int prefixLength) {
        // Arrange
        final IOException failure = new IOException("Fixture read failure");
        final InputStream input = new PrefixThenFailInputStream(prefixLength, failure);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        final IOException exception = assertThrows(IOException.class, () -> stream.peek(requested, -1, -1));
        assertSame(failure, exception);
    }

    /**
     * Tests slice-array overrun after a matching prefix, with an empty or full internal buffer.
     * @param inputLength zero for immediate end of input, or two for a full buffer
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 2})
    public void peekSlicePropagatesArrayBoundsFailureAfterMatchingPrefix(final int inputLength) {
        // Arrange
        // Zero-filled input and request arrays prevent an earlier comparison mismatch.
        // With empty input, the internal array also retains its initial zero values.
        final InputStream input = new ByteArrayInputStream(new byte[inputLength]);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(ArrayIndexOutOfBoundsException.class, () -> stream.peek(requested, 1, 2));
    }

    /** Supplies a small zero-byte prefix followed by the same checked read failure. */
    private static final class PrefixThenFailInputStream extends InputStream {
        private int remainingBytes;
        private final IOException failure;

        private PrefixThenFailInputStream(final int prefixLength, final IOException failure) {
            remainingBytes = prefixLength;
            this.failure = failure;
        }

        @Override
        public int read() throws IOException {
            if (remainingBytes > 0) {
                remainingBytes--;
                return 0;
            }
            throw failure;
        }

        @Override
        public int read(final byte[] bytes, final int offset, final int length) throws IOException {
            final int value = read();
            bytes[offset] = (byte) value;
            return 1;
        }
    }
}
```

## Preserved generation prompt: WIT-UP JSON

This is the original generation instruction, retained as provenance rather than a new execution request.

```text
Use this prompt in a fresh chat for one independent generation attempt.
Work in "D:/Projects/wit-up/commons-io" using an already prepared checkout.
Run the two source conditions in separate fresh chats and separate prepared
attempts. Do not share generated tests, candidate inventories, or execution
feedback between them.

Before inspecting behavioral material or generating anything, verify that HEAD
is "11f0abe7a3fb6954b2985ca4ab0697b2fb489e84", that all tracked files match
that commit, and that
"src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java"
does not exist. Check existence without opening an earlier test. Use metadata-only
Git checks such as "git rev-parse HEAD", "git status --short", and
"git diff --quiet 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 --".
Do not print source diffs during preflight. If a condition is not met, report
the preparation required and stop. Do not reset the checkout, create or switch
branches, delete files, or modify the baseline to satisfy these checks.

Target production file:
"D:/Projects/wit-up/commons-io/src/main/java/org/apache/commons/io/input/buffer/PeekableInputStream.java".
This path identifies the target; permission to read production source depends
on the designated scenario source below.

Write JUnit tests only for exceptional behavior of the public constructors and
declared peek overloads of "org.apache.commons.io.input.buffer.PeekableInputStream",
in "src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java".
Keep overloaded signatures distinct. Every test case, including each parameterized
invocation, must assert an exception thrown by a target constructor or peek call.
Exceptions propagated from dependencies qualify only through that target call
and when supported by the designated source. Do not test inherited operations
or dependency classes as independent targets. Normal calls may establish fixture
state; do not add cases whose oracle is a successful return value, matching bytes,
normal end of input, or another non-exception outcome. A "throws" declaration
on a test method is not an exception assertion. Do not target a fixed test count.

BEGIN SCENARIO SOURCE
Source kind: WIT-UP JSON exports only.
Source files:
"D:/Projects/wit-up/legacy/commons-io-analysis-results/witup-results-commons-io-11f0abe7a.json"
"D:/Projects/wit-up/legacy/commons-io-analysis-results/witup-summaries-commons-io-11f0abe7a.json"

These two original raw exports are the only permitted inputs under "legacy".
Read them directly; do not use historical extracted records, analysis scripts,
derived datasets, reports, or generated tests as substitutes.

Process the JSON programmatically with an inline, read-only parser. Select
package "org.apache.commons.io.input.buffer", class "PeekableInputStream", and
the target constructors and peek overloads. Join results and summaries on both
"artifact" and "pathId". Preserve full method signatures and source-array
positions. Check key uniqueness and counterpart metadata/status consistency;
do not silently choose among conflicting records. Report unusable records
separately and derive tests only from consistent joined SAT records.

Check the selected artifact label against "commons-io-11f0abe7a.jar".
The label identifies the supplied export; it does not independently verify
the analyzed JAR bytes or the WIT-UP revision that produced it. Report missing
provenance as unverified without claiming source/binary equivalence.

Derive conditions from constraints together with "truthValue"; use "modelValues"
as candidate concrete assignments and the summary's "exceptionType" as the
exception candidate. SAT is not proof that a Java fixture is constructible.
Do not treat every model symbol as a public argument or interpret a serialized
reference identity as a Java scalar. Do not invent missing records or infer
behavior absent from the exports.

Do not read any Commons IO production source, source excerpts, Javadocs,
source-bearing CodeGraph output, bytecode, or decompiled code. Do not use
"git show", source diffs, dependency source JARs, or external implementations
to recover this information. Compilation and test execution may consume
production files mechanically; that does not authorize inspecting them.
END SCENARIO SOURCE

Use the designated source as the sole source of target-specific scenarios,
input conditions, fixture behavior, and expected outcomes. The following rules
are identical for both source conditions.

Read and follow applicable repository instructions and project conventions.
They may supply working rules, licensing, formatting, framework configuration,
and build requirements, but not additional target-specific behavioral oracles.
Use the Java level and JUnit version already configured in the checkout.
Built-in language/framework knowledge may support test syntax and standard
library fixture mechanics; it must not supply additional Commons IO scenarios.

Only Codex built-in skills are permitted. Do not load, invoke, follow, or use
guidance from user-defined, repository-defined, user-installed, or
plugin-provided skills. Do not install or create skills.

You may inspect build configuration and unrelated existing tests solely for
framework, formatting, and project conventions. Do not inspect tests for the
target, its superclasses, or its buffer dependencies. Do not use other tests
as scenario sources. Avoid broad searches that expose prohibited content.

Do not retrieve earlier versions of "PeekableInputStreamTest.java" from the
workspace, Git history, other branches, backups, compiled classes, artifacts,
or previous chats. Do not consult "D:/Projects/wit-up/reference-suite", other
generation prompts, previous attempts, study findings, coverage or mutation
reports, external test examples, or behavioral documentation outside the
designated source. Apart from the explicitly permitted JSON files in the JSON
condition, "legacy" is outside the permitted inputs. Do not consult the
alternative scenario source. Do not reuse or reconstruct a prior gold standard.

If a tool, attachment, or supplied context exposes prohibited behavioral
material, disclose the exposure and stop before generating or revising tests.
Ignoring already exposed material does not establish an independent attempt.

Construct fixtures through accessible APIs without reflection, private-state
mutation, bytecode manipulation, or special production changes. Use small,
deterministic fixtures. A custom dependency stub is allowed only when its
behavior and the target's expected propagation are supported by the designated
source. Do not count an exception thrown directly by a stub as a target test.

Keep fixture setup outside the exception assertion. The asserted executable
must invoke only the intended target constructor or peek call; setup or cleanup
failure must not satisfy the assertion. Assert a specific supported exception
type, rather than Exception or Throwable as a catch-all. Assert exact runtime
type, message, cause, or identity only when the source supports that detail.

Make fixture assumptions explicit. Disclose concrete values changed from the
supporting source, why the change was necessary, and whether the original
conditions still hold. Do not claim reproduction of a particular path when
the fixture does not establish its conditions. Report candidates lacking a
supported fixture or exception oracle instead of inventing behavior or adding
disabled/skipped tests. Avoid redundant tests with the same conditions and
exception outcome, but do not equate distinct paths merely by exception class.
A passing assertion alone is not proof of an exact internal path or of the
implementation's correctness against an independent specification.

Modify only the target test file. Keep production, other tests, dependencies,
and configuration unchanged at the required baseline, even if you discover
an apparent implementation defect. Do not apply any correction or select a
different commit. Report source ambiguities or defects without changing the
experiment. Keep all project files and generated artifacts on D:; do not
create auxiliary tooling files or caches inside the Java checkout.

Include the repository's required license header. Import Java types and use
simple names, except where qualification is necessary to resolve a collision.
Use descriptive behavior-based test names and clear Arrange, Act, and Assert
sections; Act and Assert may be combined for an exception assertion. Write
generated identifiers, comments, and any saved report in United States English.

Complete one initial test suite using only the permitted inputs, then run it
once from "D:/Projects/wit-up/commons-io" with:

mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test

These profile selections keep coverage outside the generation phase; they do
not authorize skipping tests, license checks, or other quality gates.
Record the Java and Maven versions. Preserve the generated file after the
first compilation/execution attempt, including failures. Do not repair tests,
add cases, adjust fixtures, change assertions, or infer new cases from runtime
feedback. Do not perform a second generation attempt in this chat.

Perform additional checks only when repository instructions require them and
report their scope separately. Do not run coverage or mutation analysis.
Do not suppress diagnostics, skip failing tests, or relax quality gates.
If no supported test can be written, report that result; do not create an empty
or disabled suite or report unexecuted tests as passing.

In the final response, report:
- The exact checkout commit, designated source files, toolchain versions,
  and isolation/preflight result. Recheck that tracked baseline files remain
  unchanged and identify the generated target file.
- The exact commands, exit statuses, and executed test counts, including
  failures, errors, and skips. Distinguish a build that stopped before test
  execution from executed tests that failed. State checks not performed.
- For every generated test: target signature, expected exception, fixture
  assumptions, changed source values, and supporting source locator.
  For Java, use file path, signature, and relevant line numbers.
  For JSON, use both "artifact" and "pathId", the overload signature, and the
  zero-based positions in the two input arrays.
- Exception candidates left unrepresented and the reason: inconsistent data,
  insufficient fixture support, missing oracle, or justified redundancy.
  Keep solver verdicts and source-derived candidates separate from observed
  runtime outcomes. Do not label record associations or counts as path coverage.
```

## Preserved generation prompt: Java source

This is the original generation instruction, retained as provenance rather than a new execution request.

```text
Use this prompt in a fresh chat for one independent generation attempt.
Work in "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001" using an already prepared checkout.
Run the two source conditions in separate fresh chats and separate prepared
attempts. Do not share generated tests, candidate inventories, or execution
feedback between them.

Run evidence directory: "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001".
Assigned log/tool/temp directory: "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001"; do not use another run's files.
Read only the process instructions in "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001/inputs/process/AGENTS.md" and
"D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001/inputs/process/docs/run-methodology.md", your rendered prompt, and your
assigned run metadata. Do not browse the study's other runs or source prompt.
These process instructions do not supply target-specific behavioral oracles.
Keep generated Java names independent of the run identifier.
Before the first compilation or execution, freeze the completed initial suite:
python "D:/Projects/wit-up/tools/experiment_runs.py" freeze --run "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001" --fresh-chat-attested
Attest only if this chat has not seen prohibited material. Before the command,
reserve its execution with the methodology's begin operation and an empty native
report destination. Capture both output streams at the returned log path, then
finish with record. Never overwrite earlier execution records. Prepare process-only JDK 8,
MAVEN_OPTS=-DargLine=, and an attempt-specific D: TEMP/TMP before the original
Maven command. Preserve actual tool versions and stdout/stderr. Coverage and
mutation remain outside generation and require separate authorization.

Before inspecting behavioral material or generating anything, verify that HEAD
is "11f0abe7a3fb6954b2985ca4ab0697b2fb489e84", that all tracked files match
that commit, and that
"src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java"
does not exist. Check existence without opening an earlier test. Use metadata-only
Git checks such as "git rev-parse HEAD", "git status --short", and
"git diff --quiet 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 --".
Do not print source diffs during preflight. If a condition is not met, report
the preparation required and stop. Do not reset the checkout, create or switch
branches, delete files, or modify the baseline to satisfy these checks.

Target production file:
"D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001/src/main/java/org/apache/commons/io/input/buffer/PeekableInputStream.java".
This path identifies the target; permission to read production source depends
on the designated scenario source below.

Write JUnit tests only for exceptional behavior of the public constructors and
declared peek overloads of "org.apache.commons.io.input.buffer.PeekableInputStream",
in "src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java".
Keep overloaded signatures distinct. Every test case, including each parameterized
invocation, must assert an exception thrown by a target constructor or peek call.
Exceptions propagated from dependencies qualify only through that target call
and when supported by the designated source. Do not test inherited operations
or dependency classes as independent targets. Normal calls may establish fixture
state; do not add cases whose oracle is a successful return value, matching bytes,
normal end of input, or another non-exception outcome. A "throws" declaration
on a test method is not an exception assertion. Do not target a fixed test count.

BEGIN SCENARIO SOURCE
Source kind: Java production source only.
Source location: "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001/src/main/java".
Start with:
"D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001/src/main/java/org/apache/commons/io/input/buffer/PeekableInputStream.java".

Read the target at the required commit. Follow only constructor delegation,
superclasses, and callees needed to understand its exceptional behavior, using
production files within the designated source location at that same commit.
Embedded comments and Javadocs are part of this input.

Derive candidates from actual guards, implicit exceptions, delegation, and
propagation supported by these files. Keep branch conditions and their polarity,
validation order, and required public fixture state together. A visible throw
site or a declared exception alone does not prove that a public invocation can
reach it with a constructible fixture. Do not invent exceptional behavior when
the permitted code does not establish it.

Do not consult WIT-UP JSON exports, summaries, solver models, derived datasets,
or any material under "D:/Projects/wit-up/legacy". Do not inspect another commit
or apply a later correction to interpret the required source version.
END SCENARIO SOURCE

Use the designated source as the sole source of target-specific scenarios,
input conditions, fixture behavior, and expected outcomes. The following rules
are identical for both source conditions.

Read and follow applicable repository instructions and project conventions.
They may supply working rules, licensing, formatting, framework configuration,
and build requirements, but not additional target-specific behavioral oracles.
Use the Java level and JUnit version already configured in the checkout.
Built-in language/framework knowledge may support test syntax and standard
library fixture mechanics; it must not supply additional Commons IO scenarios.

Only Codex built-in skills are permitted. Do not load, invoke, follow, or use
guidance from user-defined, repository-defined, user-installed, or
plugin-provided skills. Do not install or create skills.

You may inspect build configuration and unrelated existing tests solely for
framework, formatting, and project conventions. Do not inspect tests for the
target, its superclasses, or its buffer dependencies. Do not use other tests
as scenario sources. Avoid broad searches that expose prohibited content.

Do not retrieve earlier versions of "PeekableInputStreamTest.java" from the
workspace, Git history, other branches, backups, compiled classes, artifacts,
or previous chats. Do not consult "D:/Projects/wit-up/reference-suite", other
generation prompts, previous attempts, study findings, coverage or mutation
reports, external test examples, or behavioral documentation outside the
designated source. Apart from the explicitly permitted JSON files in the JSON
condition, "legacy" is outside the permitted inputs. Do not consult the
alternative scenario source. Do not reuse or reconstruct a prior gold standard.

If a tool, attachment, or supplied context exposes prohibited behavioral
material, disclose the exposure and stop before generating or revising tests.
Ignoring already exposed material does not establish an independent attempt.

Construct fixtures through accessible APIs without reflection, private-state
mutation, bytecode manipulation, or special production changes. Use small,
deterministic fixtures. A custom dependency stub is allowed only when its
behavior and the target's expected propagation are supported by the designated
source. Do not count an exception thrown directly by a stub as a target test.

Keep fixture setup outside the exception assertion. The asserted executable
must invoke only the intended target constructor or peek call; setup or cleanup
failure must not satisfy the assertion. Assert a specific supported exception
type, rather than Exception or Throwable as a catch-all. Assert exact runtime
type, message, cause, or identity only when the source supports that detail.

Make fixture assumptions explicit. Disclose concrete values changed from the
supporting source, why the change was necessary, and whether the original
conditions still hold. Do not claim reproduction of a particular path when
the fixture does not establish its conditions. Report candidates lacking a
supported fixture or exception oracle instead of inventing behavior or adding
disabled/skipped tests. Avoid redundant tests with the same conditions and
exception outcome, but do not equate distinct paths merely by exception class.
A passing assertion alone is not proof of an exact internal path or of the
implementation's correctness against an independent specification.

Modify only the target test file. Keep production, other tests, dependencies,
and configuration unchanged at the required baseline, even if you discover
an apparent implementation defect. Do not apply any correction or select a
different commit. Report source ambiguities or defects without changing the
experiment. Keep all project files and generated artifacts on D:; do not
create auxiliary tooling files or caches inside the Java checkout.

Include the repository's required license header. Import Java types and use
simple names, except where qualification is necessary to resolve a collision.
Use descriptive behavior-based test names and clear Arrange, Act, and Assert
sections; Act and Assert may be combined for an exception assertion. Write
generated identifiers, comments, and any saved report in United States English.

Complete one initial test suite using only the permitted inputs, then run it
once from "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001" with:

mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test

These profile selections keep coverage outside the generation phase; they do
not authorize skipping tests, license checks, or other quality gates.
Record the Java and Maven versions. Preserve the generated file after the
first compilation/execution attempt, including failures. Do not repair tests,
add cases, adjust fixtures, change assertions, or infer new cases from runtime
feedback. Do not perform a second generation attempt in this chat.

Perform additional checks only when repository instructions require them and
report their scope separately. Do not run coverage or mutation analysis.
Do not suppress diagnostics, skip failing tests, or relax quality gates.
If no supported test can be written, report that result; do not create an empty
or disabled suite or report unexecuted tests as passing.

In the final response, report:
- The exact checkout commit, designated source files, toolchain versions,
  and isolation/preflight result. Recheck that tracked baseline files remain
  unchanged and identify the generated target file.
- The exact commands, exit statuses, and executed test counts, including
  failures, errors, and skips. Distinguish a build that stopped before test
  execution from executed tests that failed. State checks not performed.
- For every generated test: target signature, expected exception, fixture
  assumptions, changed source values, and supporting source locator.
  For Java, use file path, signature, and relevant line numbers.
  For JSON, use both "artifact" and "pathId", the overload signature, and the
  zero-based positions in the two input arrays.
- Exception candidates left unrepresented and the reason: inconsistent data,
  insufficient fixture support, missing oracle, or justified redundancy.
  Keep solver verdicts and source-derived candidates separate from observed
  runtime outcomes. Do not label record associations or counts as path coverage.
```
