# Native PIT launcher review

This evaluation uses configuration revision 4. Four prior evaluations remain
sealed incomplete with their original commands, native output, and diagnostics.
They do not supply the final pair's metrics or additional independent generations.

The auxiliary Maven plugin starts its test subprocess in the auxiliary POM's
native directory. The pinned bytecode trace is retained in evaluations 002/003.
An override of Java `user.dir` improved NIO paths but did not restore the native
relative paths used by `java.io` tests; evaluation 004 preserves that observation.
The CLI runs natively from each phase's real checkout, which supplies both roots.

The engine, CLI, and entry JARs are all PIT 1.15.2. The adapter remains 1.2.2 and
the JUnit Platform launcher remains 1.5.2, matching the artifact automatically
added by the Maven plugin for this project's JUnit 5.5.2 graph. Launcher and
project dependency graphs, classpaths, and every JAR hash are preserved.

The before/after classpath files start with their own compiled production/test
directories, followed by identical project and launcher artifacts. The project
dependency graph retains Commons Lang 3.9; the launcher graph has Commons Text
1.10.0 and Commons Lang 3.12.0. Actual ordered paths are retained rather than
claiming that the two library versions are interchangeable.

The selected target remains the exact PeekableInputStream production class.
The test selector remains `org.apache.commons.io.*` on both sides. DEFAULTS,
Gregor, one worker, timeout factor 1.25, timeout constant 3000 ms, and -Xmx256m
remain fixed. Failing-test skipping is explicitly false. Baseline validation is
active. No production, test, resource, dependency declaration, or assertion in
the Java checkouts was changed. Only the original frozen test is present after.

The first valid CLI baseline succeeded, generated 14 NO_COVERAGE mutants, and
reported 0/16 target lines. Its complete native XML and output were captured.
The after observation is reported independently in the final Markdown report: 7 KILLED, 3 SURVIVED, 4 NO_COVERAGE, and 15/16 target lines. Both native baseline validations succeeded.

Preservation tooling now snapshots the canonical CLI dependency POM as an input.
The added synthetic test changes that preserved input and verifies that the
manager rejects it. A static definite-assignment diagnostic was corrected with
an explicit required-plan check, without suppressions or reduced checker rules.
