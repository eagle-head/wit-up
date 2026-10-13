# PIT source-discovery correction

Configuration revision 1 pointed the auxiliary POM's main/test source directories
to absent empty directories under `analysis.build`. The real baseline compiled
classes existed, but PIT 1.15.2 skipped the project with the diagnostic
`Project has either no tests or no production code.` Its exit status was 0 and no
mutation or line-coverage XML was emitted. That evaluation is sealed incomplete.

The local pinned plugin descriptor and disassembled AbstractPitMojo establish
the project-admission check and preserve its native diagnostic. They are retained
in evaluation 002. A requested upstream tagged-source URL was unavailable (404);
the diagnosis relies on the actual local plugin and execution, rather than an
assumed current implementation.

Revision 2 points main/test source directories at the assigned checkout's real
`src/main/java` and `src/test/java`. The mutation goal still consumes the class
outputs of that side's preceding full-suite JaCoCo build. The correction changes
source discovery only. It does not alter production or test bytes, suite selectors,
dependencies, compiler target, mutation operators, thresholds, skips, or timeouts.
Before/after configuration is identical. Native XML remains mandatory; process
exit zero alone cannot establish a PIT result.

Earlier evaluations, original generation inputs, and their seals are preserved.
This separately reserved evaluation captures the corrected plan, protocol, POM,
paths, commands, environment, and native evidence before claiming completion.
