# Implementation integrity

## Durable implementation identity

Apply this policy whenever writing or modifying source code, tests, fixtures,
configuration, schemas, generated interfaces, or executable artifacts in any
project, unless a more specific instruction explicitly requires a different durable
identity contract:

- Name implementation elements after stable domain concepts, observable behavior,
  or enduring technical responsibilities.
- Never embed task names, task descriptions, prompt labels, backlog/work-item
  identifiers, requester names, agent identities, chat/session identifiers, or
  temporary orchestration labels in executable or product-facing identities.
- This prohibition includes constants, variables, enum members, packages, modules,
  classes, functions, configuration keys, environment variables, API routes and
  fields, schema names, database objects, serialized values, feature flags, log and
  telemetry fields, metric/event names, marker values, filenames, artifact names,
  test names, fixture identities, snapshots, and user-visible messages.
- Do not hide the same coupling behind an abbreviation, case change, prefix, suffix,
  or indirect alias. For example, `DB068_VARIANT`, `db068.variant`, and
  `task_31_mode` are task-coupled identities; prefer functional names such as
  `fixture.variant`, `analysis.mode`, or `serialized_input_policy`.
- A task rename, backlog replacement, work-item migration, or new planning file must
  not require a code, test, configuration, data-contract, or runtime-contract change.
- Task/work-item identifiers may appear only in an explicit governance or provenance
  envelope whose purpose is to map durable artifacts to planning records, such as a
  backlog, evidence manifest, review record, or migration ledger. Keep that envelope
  separate from runtime behavior and do not copy its identifiers into implementation
  contracts.
- Identifiers that independently define durable product or interoperability semantics
  (for example, a published standard, protocol, taxonomy, or schema version) are not
  task identifiers. Use them only when the implementation genuinely depends on those
  semantics, not as aliases for planning work.
- When modifying an affected path, search the changed implementation and tests for
  task coupling and correct it at the root. Preserve unrelated work; do not expand
  into repository-wide cleanup unless requested or required by the same contract.
- If an already published external contract contains a task-coupled identity, identify
  its consumers and define a migration to a durable functional name before breaking
  it. Do not add a permanent compatibility alias merely to preserve the invalid model.

## Accurate intent and risk terminology

Apply this policy when describing, implementing, testing, reviewing, or reporting
benign research, program analysis, synthetic fixtures, quality validation, or other
authorized engineering work. Its purpose is accurate classification and the avoidance
of unsupported harmful implications, not evasion of safety or policy review:

- Describe the concrete engineering object, authorized scope, and observable behavior
  before using risk-sensitive terminology. State when inputs are synthetic, execution
  is local or isolated, no external target is involved, and no claim about product or
  deployment behavior is being made.
- Do not characterize a project, codebase, dependency, or deployment as having a
  vulnerability, being exploitable, under attack, dangerous, malicious, compromised,
  or harmful unless that exact claim is material, supported by concrete evidence, and
  within the user's authorized scope.
- For synthetic or feasibility work, prefer literal bounded terms such as `modeled
  condition`, `fixture variant`, `fixed test input`, `control contrast`, `negative
  case`, `fixture effect observed`, `contract violation`, `admission rule`, and
  `product behavior claim: false`. Do not promote a modeled condition or fixture
  observation into a statement about a real product.
- Avoid gratuitous verbs or labels that imply harmful intent, unauthorized access,
  persistence, evasion, weaponization, or real-world impact when the work is actually
  parsing, modeling, testing, benchmarking, reproducing an API contract, or validating
  a local fixture. Describe the actual operation instead.
- Keep measurement, interpretation, and authority distinct. A taxonomy key, scanner
  label, source statement, call-site shape, synthetic result, or passing test does not
  by itself establish a real-world defect, reachability, impact, or product condition.
- Preserve exact names when they are load-bearing external facts, such as published
  standards, taxonomy identifiers, API/package names, advisory titles, or verbatim
  source locators. Explain their role and limitation rather than renaming them in a way
  that changes technical meaning.
- Review changed code, schemas, fixtures, logs, reports, and user-facing prose for
  ambiguous risk-sensitive wording. Replace unsupported implications with precise
  functional language, while retaining any genuine negative result or material fact.
- Never suppress, disguise, euphemize, or relabel genuinely relevant behavior to bypass
  a safety control or policy classification. If the evidence supports a concrete
  security-relevant claim, report it accurately, with authorization, scope, mechanism,
  limitations, and the appropriate review workflow.
- Do not make blanket assurances such as `safe` or `harmless` when the evidence only
  establishes bounded controls. Name the actual bounds—for example fixed inputs,
  isolated execution, no network, owned temporary storage, time/memory limits, and
  cleanup verification.

## Error integrity and quality gate enforcement

Apply this policy to all implementation and validation work, including production
code, tests, fixtures, examples, scripts, generated code, and temporary experiments:

- Never hide, suppress, discard, or misrepresent errors, warnings, failed checks, or
  incomplete validation to make code appear correct or work appear complete. Fix
  the underlying cause within the authorized scope and respect the configured
  linter, compiler, type checker, static analysis, test, and coverage requirements.
- Do not add or broaden suppression comments, annotations, pragmas, ignore lists,
  exclusions, baselines, or diagnostic filters without the explicit exception
  approval described below. Examples include `eslint-disable`, `noqa`,
  `type: ignore`, `@ts-ignore`, `@SuppressWarnings`, and equivalent mechanisms.
- Do not disable rules, lower severities or thresholds, relax strictness, change
  quality gate configuration, or bypass hooks or CI checks to obtain a passing
  result. Such exceptions require the same explicit approval, even when implemented
  indirectly through scripts, environment settings, tool versions, or file moves.
- Never mask a failing operation with a forced success exit code, ignored return
  value, swallowed exception, fabricated fallback result, or selective reporting.
  Legitimate error handling must preserve the intended contract and observable
  failure behavior; it must not manufacture evidence of success.
- Do not delete, skip, quarantine, weaken, or rewrite tests, assertions, snapshots,
  expected results, or coverage scope merely to accommodate incorrect behavior.
  Legitimate test changes must follow the intended contract and retain meaningful
  validation. Being test code or a synthetic fixture grants no automatic exception.
- Consider a suppression or relaxation only in an extreme, technically justified
  case. First investigate compliant alternatives and present the exact proposed
  change, affected diagnostics and files, evidence, necessity, and tradeoffs to the
  user. Apply it only after the user explicitly approves that specific exception.
  Urgency, convenience, existing suppressions, a suspected false positive, or a
  general request to finish or fix the code does not constitute approval.
- Keep an approved exception as narrow as possible, document its rationale and
  removal condition where relevant, and verify the remaining checks. Approval for
  one exception does not authorize broader or subsequent exceptions.
- When a check fails or cannot run, report its actual status, relevant diagnostics,
  and remaining limitation. Distinguish passed, failed, skipped, and unverified
  checks. An approved suppression remains a disclosed exception, not a root cause
  fix, and an unexecuted check must never be reported as passed.
- Ordinary corrections that satisfy existing requirements may proceed within the
  authorized task. If an exception lacks approval, keep the requirement in force,
  continue useful compliant work, and report the unresolved issue honestly.
