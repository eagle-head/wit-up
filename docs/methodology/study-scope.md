# Study scope

[Documentation index](../README.md)

## Objective and present question

The long-term objective is to examine whether an LLM can create JUnit tests from
WIT-UP results. The present phase asks a narrower question: **what information do
the existing exports provide for selecting and preparing a later generation
experiment, and what information is missing?**

The full inventory answers four questions: field structure and cross-file
correspondence; counts of methods, paths, exception types and verdicts; available
input/assertion information; and preliminary simpler candidate rows. The
subsequent inspection assesses 20 selected records against those data boundaries.

## Inputs and units

The source inputs are the existing results and summaries JSON arrays labeled
`commons-io-11f0abe7a.jar`. A record is located by `(artifact, pathId)`, and a method
is the full signature before the final `#pathIndex`. Constructors are included
and identified by `<init>`. Paths within one method are related observations, so
the selected sample contains at most one path per full method signature.

The initial simpler pool contains 221 paths: 65 simple-signature hypotheses and
156 single-reference null hypotheses. This is a heuristic subset of 16,166 SAT
summaries, not a random population sample. The complete inventory and excluded
tiers remain available; exclusion from this small inspection does not establish
that a case is unsuitable for generation.

## Boundaries and role of evidence

Raw record content supports statements about what was exported. Data labels,
field presence, integer comparisons and null flags support bounded
interpretations. The export does not establish public accessibility, object
construction, runtime exception locations, or intended behavior from an
independent public contract. SAT remains an encoded-model verdict.

No test-generation model/API is invoked by the pipeline in this phase. No Java
tests are written or run. The Java repositories are not reviewed or modified.
The earlier phase consulted the WIT-UP export boundary to interpret fields; no
Java source is consulted for the 20-case assessment. The producing WIT-UP revision
is unknown, and the artifact filename does not independently verify JAR bytes.

## Practical methodological standard

This is an exploratory, descriptive case inspection, not a preregistered study,
systematic review, randomized experiment, or estimate of LLM effectiveness.
The practical minimum applied here is:

- State the question, source inputs, observation units and inclusion criteria.
- Make selection reproducible and retain every selected case, including ambiguity.
- Separate explicit exported data, interpretations and unresolved information.
- Preserve original parsed records, precise locators, byte identities and rules.
- Report denominators, selection bias, unavailable evidence and actual checks.
- Record changes and observations without rewriting earlier choices as if they
  had been planned before the data were inspected.

## Assessment procedure and limitations

Case labels and recognized-expression checks follow documented rules. The
assessment combines these checks with a qualitative inspection of the selected
records. No independent assessment, blinding, or inter-rater agreement
measurement was performed. The findings describe exported information and
preparation gaps; test-generation effectiveness remains unmeasured.

## Stopping rule

Stop this phase when 10 cases per initial stratum have traceable source records,
documented assessments, retained gaps, and a reproducible inventory. Do not seek
extra cases merely to improve the apparent completeness of preparations. Reopen
the protocol if inputs, quotas, rules, or the later experiment's question change.
