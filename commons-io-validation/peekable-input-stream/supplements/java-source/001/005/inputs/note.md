# Measurement authorization

The user instructed this evaluation to proceed after the preceding explanation
of paired JaCoCo/PIT measurements and a final Markdown report. The following
verbatim Portuguese quotation is retained as the original authorization value:

> ja foi feito o run, siga em frente

The authorized scope is the sealed Java-source generation, its frozen test,
before/after measurements in separate baseline checkouts, and a Markdown report
with complete Java source, exact versions, commands, native results, and limits.
Infrastructure diagnostics remain separate from executed-test outcomes.

This evaluation contributes no independent generation. The original generation
and its seal must remain byte-identical. The canonical paired-full-suite plan
governs the selections; no generated or existing test may be repaired, suppressed,
or removed to obtain passing measurements.

This distinct retry uses canonical configuration revision 4: the same PIT 1.15.2 engine is launched through its CLI from each checkout's native root. The complete original suite, resources, generated test, compiler, dependencies, mutators, and quality gates are preserved; earlier diagnostic attempts remain sealed.
