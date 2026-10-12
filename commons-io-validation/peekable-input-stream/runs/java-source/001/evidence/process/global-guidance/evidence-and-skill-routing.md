# Evidence and skill routing

Skills remain eligible for implicit invocation. Before invoking a custom skill,
classify each material claim or deliverable by the evidence that can answer it.
Classify the claim itself, not the repository that contains it, its file extension,
or nearby technical vocabulary.

- `textual-evidence`: the claim is answered primarily by interpreting and comparing
  literature, documentation, specifications, records, or other source content.
- `system-evidence`: the claim concerns software or system behavior, correctness,
  performance, security, configuration, or another engineering property established
  from code, contracts, runtime observations, or concrete controls.
- `model-semantics`: the claim concerns the meaning or structure of a model independent
  of any rendering tool.
- `tool-artifact`: the claim concerns authoring, parsing, validating, or rendering an
  artifact in a particular tool or notation.
- `hybrid`: separate the task into its constituent claims and route each claim
  independently. Do not apply one class's workflow to the other classes.

Use the most specific available skill whose eligibility gate passes:

- Use `comprehensive-testing` only for `system-evidence` claims about test design,
  test implementation, or test-suite adequacy for observable executable behavior.
- Use `comprehensive-performance` only for `system-evidence` claims about a measurable
  runtime or resource outcome under a relevant workload.
- Use `comprehensive-security` only for `system-evidence` claims about a concrete,
  authorized target and an attacker-driven security property or control.
- Use `uml` only for `model-semantics` claims expressed in or requiring UML.
- Use `plantuml` only for `tool-artifact` claims involving PlantUML source, validation,
  runtime behavior, or rendering.
- Use `evidence-research` for `textual-evidence` claims that require source discovery,
  appraisal, comparison, synthesis, or a research-grounded conclusion. Handle a simple
  source reading directly when a full research workflow would add no value.

Apply these guards before loading a skill workflow:

1. Identify the object under study, the exact claim, and the discriminating oracle.
2. Do not invoke a skill merely because the task occurs in a repository, sources
   mention code, or words such as "test", "performance", "security", "evidence", or
   "validation" appear.
3. If a skill's eligibility gate fails, do not borrow its workflow, artifacts, or
   completion criteria. Continue directly or select a skill whose gate passes.
4. For hybrid work, apply each skill only to its eligible subclaim. A textual phase
   does not inherit code tests, benchmarks, fixtures, or engineering gates merely
   because a later phase may execute software.
5. Commands used to retrieve, search, OCR, or transform text do not convert a textual
   claim into a system claim. Their successful execution proves only the operation,
   not the truth of the source or conclusion.
6. For textual evidence, use content, citations, and precise locators to support the
   argument. Hashes and manifests may establish byte identity or provenance when that
   identity matters; they do not establish meaning, quality, relevance, or truth.
   Do not create tests, fixtures, benchmarks, or hashes as semantic proof of prose.
7. Invoke an eligible skill automatically when it materially improves the requested
   work; the user does not need to name it explicitly.
