# JSON analysis method

[Documentation index](../README.md) | [JSON findings](../commons-io-json-analysis.md)

## Complete inventory procedure

1. Read every object from each input array with ijson. Inventory top-level fields,
   observed value types, nested conditions, solver labels, model value forms,
   method signatures, classes and exception origins.
2. Retain `exceptionType: null` as an explicit data gap. Check required field
   presence, types and nested structures. Do not invent an exception name.
3. Independently load the original arrays into DuckDB and compare its row counts
   with the streaming parser counts.
4. Check `(artifact, pathId)` uniqueness before joining. Measure absent matches,
   verdict disagreements and signature metadata disagreements.
5. Save the full results, summaries and candidate tables, preserving original
   model strings and nested conditions. Export Parquet and `statistics.json`.
6. Generate four focused findings pages, with illustrative examples in a separate
   appendix. The initial examples use a different descriptive selection from the
   later 20-case inspection; they are not additional experimental observations.

The measured inventory contains 88,303 result rows and 72,419 summary rows, with
1,127 represented method signatures. All summaries have a result; there are
15,884 result rows without a summary. Matched verdicts and metadata agree.
The current exporter's grouping explains why equal row counts are not assumed,
but exact producer provenance remains unavailable.

## Preliminary candidate rule

Candidate preparation labels are mutually exclusive and applied in priority order:
missing/disagreeing result; non-SAT verdict; absent exception type; detected
receiver/signature-qualified state; call syntax; symbolic/compound model forms;
basic parameter signatures; one other parameter plus a true null flag; other
object fixtures.

Basic types include primitive types and `java.lang.String`. A basic signature may
have no parameters. A null hypothesis has one other parameter type and an
identifier-shaped `_is_null` key with `BoolValue[value=true]`. These labels do not
verify argument binding, access modifiers, invocation mode, or constructibility.

The original pattern rule recognizes some temporary forms (`_ret_`, `expr_`,
`caught_`) but does not flag `stack_7`. The later case assessment records this
limitation without modifying the original candidate pool or replacing the case.

## Condition and model interpretation

Conditions form a conjunction. Each `symExpr` must be evaluated according to its
`truthValue`; false means the expression must not hold. Model values are exported
strings. Null flags must be interpreted alongside StringValue/IntValue data; an
empty serialized string is not automatically a non-null Java argument, and a
reference encoding of zero is not automatically a Java integer input.

## Source context used in the earlier phase

Only the WIT-UP export boundary was read: Driver, SummaryRowBuilder, SolverStatus
and the relevant solver-status handling. Its checkout was
`646aec8f47cb5ed2b604ee38cacb44095ce89259`, not a confirmed producing revision.
That reading informed schema semantics and grouping interpretation; it was not a
correctness review of WIT-UP or Commons IO. Raw counts come from the JSON files.

## Checks and limits

Parser counts, join uniqueness, candidate row counts and Parquet row counts were
checked. Predicate truth counts reconcile with the total condition count.
Ruff and the uv lock check support implementation hygiene. These operations do
not establish solver soundness, runtime reachability, test adequacy, or feasibility
of test generation.
