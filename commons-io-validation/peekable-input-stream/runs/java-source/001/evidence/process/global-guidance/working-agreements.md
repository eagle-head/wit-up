# Global instructions

Keep this file limited to durable, cross-repository working agreements. Put
repository-specific paths, versions, commands, capabilities, and acceptance rules
in the closest applicable repository `AGENTS.md`. Keep operational detail in its
owning document and link to that document instead of copying it here.

<!-- CODEGRAPH_START -->
## CodeGraph

In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE `rg`, `Get-ChildItem`, or reading files when you need to understand or locate code:

- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops plain-text search can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.

If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
<!-- CODEGRAPH_END -->

## Language for local materials and chat

- Write all new or materially revised local project content stored outside chat in United States English.
- This rule applies to source code identifiers, code comments, documentation, diagrams, configuration, schemas, tests, fixtures, commit messages, logs, generated text, and other artifacts stored locally.
- Chat and other conversational responses have no fixed language. Respond in the language and regional variety used by the user unless the user requests another language. Preserve established technical terms when translating them would be inaccurate, ambiguous, or unnatural.
- Preserve non-English text in local project content only when it is a load-bearing external value, such as an exact protocol field, quoted source passage, legal name, or compatibility fixture. Explain the exception in United States English within the relevant local material.

## Java imports and type references

- In handwritten Java source, import each referenced type and use its simple name. Do not write a fully qualified type name inline in a declaration, expression, pattern, annotation, cast, generic signature, constructor call, or static member access merely to avoid an import.
- Use an inline fully qualified type name only when qualification is necessary to disambiguate colliding simple type names. A qualified class name represented as data rather than as a Java type reference—including an exception type name in a string, serialized value, reflection key, diagnostic, compiler output, or compatibility fixture—is outside this rule.
- When modifying Java, review the affected scope for violations and use the repository's import, formatting, and static-analysis gates. When the configured toolchain provides a suitable rule, prefer structural enforcement over relying only on manual review.

## Project storage

- Store all source-code projects, repositories, worktrees, project documentation, and project-generated artifacts on the `D:` drive.
- Use `D:\Projects` as the default root for new projects unless the user specifies another path on `D:`.
- Never create, clone, copy, check out, or migrate a project or worktree to the `C:` drive.
- Reserve the `C:` drive for installed applications and unavoidable application or operating-system state, such as files managed under `AppData`; do not treat those locations as project storage.
- If a task starts in a project or workspace on `C:`, do not add project files there. Report the conflict and use or request a destination on `D:` before making project changes.

## Expo MCP Server use

- Before relying on Expo MCP Server, read the current
  [Expo MCP documentation](https://docs.expo.dev/mcp/), the closest applicable
  repository instructions, and any runbook they reference. Repository-owned
  documentation is authoritative for project versions, commands, patches, required
  capabilities, recovery procedures, and evidence boundaries.
- An enabled MCP configuration, a running Metro listener, or an ADB device does not
  establish that a required Expo MCP capability works. Verify the exact capability
  with the smallest suitable observation before depending on it.
- Unless the closest repository instructions define a broader contract, treat Expo
  MCP output as development observation or diagnosis rather than a test result or
  acceptance evidence. If a required capability is absent or fails, preserve the
  diagnostic and either restore the connection or use a suitable observation method
  allowed by the repository. Block only work that materially requires the unavailable
  capability.

## Referenced global policies

Keep detailed, reusable policies in focused references so unrelated tasks do not
load every procedure. Read the applicable reference before taking work in its scope:

- Before selecting or invoking a custom skill, classifying evidence, or designing an
  evidence workflow, read the
  [evidence and skill routing policy](guidance/evidence-and-skill-routing.md).
- Before implementation, validation, or review involving source code, tests,
  fixtures, configuration, schemas, generated or executable artifacts, durable
  identities, or risk-sensitive claims, read the
  [implementation integrity policy](guidance/implementation-integrity.md).
- Before creating, renaming, selecting, or publishing a branch, or before creating a
  commit, read the [Git conventions](guidance/git-conventions.md).

These references are part of the global instructions. If a required reference
cannot be read, do not invent or relax its rules. Report the unavailable reference
and continue only with work outside its scope.

## Always-on core rules

- Name durable artifacts after stable domain concepts and observable responsibilities,
  never after tasks, work items, requesters, agents, sessions, or orchestration tools.
- Preserve truthful diagnostics. Never hide failures, weaken quality gates, or use
  suppressions and exclusions without the narrowly scoped explicit approval required
  by the implementation integrity policy.
- Distinguish synthetic or isolated observations from claims about real products,
  deployments, targets, or impact.
- Derive branch names and commit messages solely from the semantic purpose of the
  change. Operational provenance and creator identity are never naming semantics.
