# Study repository instructions

Read [the run preservation methodology](docs/run-methodology.md) before
preparing, generating, executing, measuring, comparing, committing, moving, or
cleaning up experimental runs. It owns the directory layout, exact toolchain,
phase boundaries, preservation commands, and acceptance checks.

- Assign each independent generation its own source condition, run directory,
  prepared checkout, and fresh chat. Reserve it with `tools/experiment_runs.py`.
  Never recycle a directory or share a checkout between runs.
- Deliver only the rendered `inputs/prompt.txt` and its permitted inputs to the
  generator. A generator must not inspect this repository's earlier run evidence,
  reference tests, comparison results, or the alternative source prompt.
- Preserve and use the assigned snapshots of process instructions and scenario
  inputs. Verify live inputs before freezing and executing.
- Freeze the generated test before its first compilation or execution. After
  freezing, do not repair, augment, rename, or regenerate it from execution feedback.
- Reserve every invocation with `begin` before running its command, then finish
  it with `record`. Native report destinations must start empty. Record initial
  executions and supplemental executions separately. Preserve
  failed operations and genuine executed-test failures. Infrastructure failures
  do not become failures of tests that never executed.
- Run JaCoCo and PIT only in the separately authorized measurement phase. Keep
  each phase's output in a linked evaluation supplement with its frozen canonical
  measurement plan. Measure baselines; do not infer zero.
- Verify and seal each completed or explicitly incomplete attempt. Sealed run
  contents are immutable by workflow. Corrections belong in a separate annotation
  or linked evaluation supplement with the parent's exact seal hash. A supplement
  never adds an independent generation. Generation and evaluation completion have
  separate evidence requirements.
- Follow the methodology's commit and backup procedure. Do not stage generated
  caches or presentation assets. Never clean up unsealed evidence or hide diagnostics.
- After adding a supplement, create a new verified collection backup containing
  both original generations and supplements. Recover partial reservations explicitly.
- Keep all project artifacts and backups on D:. Write new local materials in
  United States English. Run identifiers belong in provenance metadata and folder
  names, not Java test identifiers or application behavior.

Isolation here is procedural. A fresh chat and checkout do not create a filesystem
access-control boundary. Disclose prohibited exposure and stop generation if it occurs.
