# Generation checkout preparation

[Documentation index](../README.md) | [Repository storage](repository-storage.md)

## Responsibility and scope

Prepare the Java checkout before opening an independent generation chat. The
prepared generation prompts remain fixed experimental inputs. Environment
readiness belongs to this preparation procedure and does not require changing
the scenario-source rules or authorizing the generator to repair build failures.

The generation agent still checks its prompt's required HEAD, unchanged tracked
baseline, and absent target test. If those preconditions fail, it reports the
preparation required and stops as instructed.

## Keep local tooling in its owning project

Run Python analysis and Ruff commands from "D:/Projects/wit-up", where the Python
project and cache belong. Keep Ruff's ".ruff_cache" outside
"D:/Projects/wit-up/commons-io". When invoking Python checks from another working
directory is necessary, explicitly direct their cache to the owning Python
project instead of creating local tooling files in the Java checkout.

Before a generation attempt, inspect the actual checkout contents as well as
Git status. A tool's own cache ignore file can hide its directory from Git
status even when Apache RAT still scans that directory. A clean tracked diff
alone therefore does not establish that the license gate can run.

If unrelated tooling state is present in the Java checkout, preserve the
required original diagnostics and bytes, then relocate that state to its owning
project or a local evidence archive outside the checkout. Verify the exact
source and destination paths before moving anything. Do not delete evidence or
modify tests, production source, license headers, or build exclusions to obtain
a passing result.

## License-gate preflight

After preparing the requested baseline and confirming that the target test is
absent, run the configured RAT check from the Java checkout:

```powershell
Set-Location -LiteralPath "D:/Projects/wit-up/commons-io"
mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" apache-rat:check
```

Retain the command, exit status, and RAT diagnostic when it fails. Resolve
environment problems during preparation, and repeat this check before launching
generation. Do not disable RAT, use skip flags, add broad exclusions, or relax
license checks. The preflight checks the existing baseline; the generated test
must still pass the normal build checks after creation.

Use the same recorded Java and Maven toolchain for the compared conditions.
Archive the preflight output outside the Java checkout so it does not itself
become an unexpected input to the license scan. Reconfirm HEAD, tracked source
and configuration, and absence of the target test after preparation.

## Preserve experimental identity

Do not edit completed generation prompts to describe an environment correction.
Record the correction and any later execution in the study log with its own
timestamp and command. Keep original failed generation outcomes separate from
later successful validation; a later pass does not retroactively change the
original run.

This procedure supplies working rules and build readiness only. It supplies no
target-specific exception scenarios, fixtures, assertions, prior test results,
coverage values, or reference-suite behavior to the generator.
