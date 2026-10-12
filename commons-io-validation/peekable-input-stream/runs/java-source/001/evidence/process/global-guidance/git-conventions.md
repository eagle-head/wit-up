# Git conventions

## Default branch policy

Apply these defaults whenever creating, renaming, selecting, or publishing a Git
branch in any project, unless a more specific instruction explicitly defines a
different branch policy:

- Write branch names in English.
- Use concise, descriptive, outcome-based names in lowercase kebab-case, optionally
  prefixed by a semantic category such as `feat/`, `fix/`, `docs/`, `refactor/`,
  `test/`, or `chore/`.
- Derive the branch name exclusively from the actual change and its durable purpose.
- Apply the same semantic test to every path segment, including prefixes and
  namespaces. Each segment must describe the change's stable category, domain, or
  outcome and must be justifiable from the diff alone.
- Treat automatic naming conventions from tools, runtimes, workspaces, or
  orchestration systems as non-authoritative. Do not adopt a default segment that
  records operational provenance instead of describing the change.
- Never include task names, task descriptions, prompt labels, work-item names or
  identifiers, requester names, agent names, or the identity of whoever requested
  the change. Describe what the branch accomplishes, not which task initiated it.
- Reject any segment that would remain unchanged across unrelated work merely to
  identify its creator, execution environment, account, session, or coordinating
  system. Remove that segment before creating, renaming, committing on, or
  publishing the branch.
- Before the first commit and before every push, inspect the current branch name. Do
  not commit on or publish a nonconforming branch; rename it first. If a
  nonconforming branch is already published, verify its consumers and obtain any
  required authorization before rewriting or deleting the remote reference.
- Do not create a branch merely to represent a chat, session, agent run, or temporary
  orchestration step.

## Default commit policy

Apply these defaults whenever the user asks for a Git commit in any project, unless
a more specific instruction explicitly defines a different commit policy:

- Write commit messages in English.
- Create semantic, atomic commits. Each commit must represent one coherent change
  and be independently understandable and reviewable.
- Use the Conventional Commits format by default (`feat:`, `fix:`, `docs:`,
  `refactor:`, `test:`, `chore:`, and similar semantic types), with a concise,
  imperative subject. Add a body when needed to explain motivation, constraints, or
  noteworthy behavior.
- Derive the commit message exclusively from the actual change and its purpose.
- Never include task names, task descriptions, prompt labels, work-item names,
  requester names, agent names, or the identity of whoever requested the change in
  the commit subject or body. Describe what the change accomplishes, not who asked
  for it or which task initiated it.
- Do not combine unrelated changes into one commit. When the working tree contains
  unrelated user changes, commit only the files or hunks that belong to the requested
  logical change and preserve the rest.
