# Execution Diagnostics



This separate record preserves unsuccessful operations and build warnings. They are excluded from the ten-test suite outcome totals. No failed operation is classified as a successful test or mutation analysis.



| Completed (UTC−04:00) | JDK | Exit | Stage | Observation |
| --- | --- | --- | --- | --- |
| 2026-10-12T15:16:10-04:00 | Temurin 25.0.4.1+1 | 1 | maven-bundle-plugin:4.2.1:manifest | ConcurrentModificationException at TreeMap.callMappingFunctionWithCheck, reached from aQute.bnd.osgi.Jar.putResource |
| 2026-10-12T15:23:12-04:00 | Temurin 1.8.0\_504-b01 | 0 | Build diagnosis through process-classes | No test execution; build diagnosis only. |
| 2026-10-12T15:27:30-04:00 | Temurin 1.8.0\_504-b01 | 1 | Surefire fork startup | Error: Could not find or load main class $\{argLine\} |



[Original infrastructure record](../infrastructure/execution-record.json) · [Raw Surefire startup diagnostic](../infrastructure/surefire-jdk8-argline/2026-10-12T15-27-30_390.dumpstream)



## Exploratory full-project PIT validation



Two attempts selected all existing tests with org.apache.commons.io.\* while the generated test was absent. PIT rejected the unmutated test baseline. The first attempt reported 31 failing cases; explicitly setting the original project base directory left 30 failing cases in the second attempt. The remaining cause was not established. The full-project PIT result is unsuccessful, and no global mutation score is claimed. No existing test was edited, skipped, or weakened to resolve these failures.



[First attempt log](../infrastructure/pit-baseline-directory/maven.log) · [Original-root retry log](../infrastructure/pit-full-suite-baseline/maven-original-root.log) · [Full-project configuration](../infrastructure/pit-full-suite-baseline/pit-full-suite-pom.xml) · [Initial baseline orchestration record](baseline-execution.json)



The later successful PIT comparison uses the same generated-test filter in both phases. Its before result measures the absence of that suite, and its after result measures the contribution of those ten tests. It does not resolve or replace the unsuccessful full-project validation. The initial orchestration record therefore correctly retains BaselinePITExit = 1 even though the final targeted before measurement has exit code 0.



## Warnings retained in successful Maven runs



The checkout has a detached HEAD, so buildnumber reports that branch detection failed and records UNKNOWN. Compiler output reports existing unchecked operations and deprecated API usage. The full baseline Surefire run reports six existing skipped cases. These messages remain in the raw Maven logs; they were not suppressed.



The original JDK 25 output was recorded in the conversation; a separate raw log for that first failure was not archived. The JSON record retains its diagnostic without claiming a complete raw transcript.
