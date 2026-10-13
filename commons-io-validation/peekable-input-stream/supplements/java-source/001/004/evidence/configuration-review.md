# Measurement configuration review

The original generation and three preceding evaluations remain sealed.
Evaluation 001 retained a tool-preparation parsing error; evaluation 002 retained
a skipped PIT analysis; evaluation 003 retained the full-suite unmutated baseline
failure. None contributes independent generations or substitutes for this pair.

Canonical configuration revision 3 addresses two observed tooling conditions:

- Actual source and test-source roots enable PIT's project-discovery check.
- `-Duser.dir=${analysis.checkout}` in the PIT child JVM restores the Java root
  for relative fixture paths to the same checkout used by Surefire.

The local PIT 1.15.2 bytecode shows the launch path explicitly:
`AbstractPitMojo.analyse()` passes `detectBaseDir()` into the goal strategy;
`detectBaseDir()` uses the execution Maven project's `getBasedir()`;
`EntryPoint` forwards that File into `DefaultCoverageGenerator`, which sets
`ProcessArgs.andBaseDir()`. The auxiliary POM's directory is therefore the
native launch directory. The separate `projectBase` report option does not
replace this launch argument. These pinned bytecode diagnostics are retained
in evaluations 002 and 003.

Existing resource tests, including `PathUtilsTest`, refer to
`src/test/resources/...` using Java relative paths. The revised child-JVM
property supplies that Java filesystem root at JVM startup. It does not claim
to change the subprocess's native operating-system directory. This distinction
must remain explicit if future tests use native subprocess-relative paths.

The real before/after executions determine whether the correction suffices.
Both sides retain identical dependencies, existing tests, resource bytes,
production bytes, compiled target, selectors, mutators, timeouts, and thresholds.
No assertion, test fixture, skip, or quality gate has been weakened.

The plan, protocol, auxiliary POM, authorization, exact substitutions, version
observations, and rendered phase scripts are preserved in this distinct record.
