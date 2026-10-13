"""Render measured native evidence as a standalone Markdown report."""

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from hashlib import sha256
from pathlib import Path


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def percentage(covered, total):
    return f"{covered}/{total} ({covered / total * 100:.2f}%)" if total else "N/A"


def main(root):
    manifest = read_json(root / "run.json")
    records = {}
    for execution in manifest["executions"]:
        directory = root / execution["path"]
        request = read_json(directory / "request.json")
        result = read_json(directory / "result.json")
        records[result["phase"]] = (directory, request, result)
    source = (root / manifest["frozenTest"]["path"]).read_text(encoding="utf-8-sig")
    environment = read_json(root / "inputs/environment.json")
    substitutions = read_json(root / "evidence/substitutions.json")
    target = "org.apache.commons.io.input.buffer.PeekableInputStream"
    pairing = {}
    inventories = []
    for side in ("before", "after"):
        checkout = Path(substitutions["phases"]["jacoco-" + side]["checkout"])
        tracked = (
            subprocess.run(
                ["git", "-C", str(checkout), "ls-files", "-z"],
                capture_output=True,
                check=True,
            )
            .stdout.decode()
            .split("\0")
        )
        entries = {
            relative: sha256((checkout / relative).read_bytes()).hexdigest()
            for relative in tracked
            if relative
        }
        inventories.append(entries)
        head = subprocess.run(
            ["git", "-C", str(checkout), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        status = subprocess.run(
            ["git", "-C", str(checkout), "status", "--short"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        baseline_diff = subprocess.run(
            [
                "git",
                "-C",
                str(checkout),
                "diff",
                "--quiet",
                manifest["baselineCommit"],
                "--",
            ],
            check=False,
        ).returncode
        test = (
            checkout
            / "src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java"
        )
        pairing[side] = {
            "checkout": checkout.as_posix(),
            "head": head,
            "status": status,
            "trackedDiffExit": baseline_diff,
            "trackedFiles": entries,
            "generatedTestSHA256": sha256(test.read_bytes()).hexdigest()
            if test.is_file()
            else None,
        }
    pairing["identicalTrackedBytes"] = inventories[0] == inventories[1]
    if (
        not pairing["identicalTrackedBytes"]
        or pairing["before"]["generatedTestSHA256"] is not None
        or pairing["after"]["generatedTestSHA256"] != manifest["frozenTest"]["sha256"]
        or any(
            pairing[side]["head"] != manifest["baselineCommit"]
            or pairing[side]["trackedDiffExit"]
            for side in ("before", "after")
        )
    ):
        raise ValueError(
            "The before/after source pairing does not satisfy the frozen contract."
        )
    (root / "evidence/source-pairing.json").write_text(
        json.dumps(pairing, indent=2) + "\n", encoding="utf-8"
    )
    measurements = {}
    for phase, (directory, _, result) in records.items():
        artifacts = result["artifacts"]
        metric = {"exitCode": result["exitCode"], "suiteCounts": result["suiteCounts"]}
        if "jacoco-xml" in artifacts:
            xml = ET.parse(directory / artifacts["jacoco-xml"]["path"]).getroot()
            classes = [
                node
                for node in xml.findall(".//class")
                if node.attrib.get("name") == target.replace(".", "/")
            ]
            if len(classes) != 1:
                raise ValueError(
                    "The native JaCoCo report must contain the target exactly once."
                )
            metric["counters"] = {
                node.attrib["type"]: {
                    key: int(node.attrib[key]) for key in ("missed", "covered")
                }
                for node in classes[0].findall("counter")
            }
        if "pit-mutations" in artifacts:
            xml = ET.parse(directory / artifacts["pit-mutations"]["path"]).getroot()
            mutations = xml.findall("mutation")
            metric["mutationStatuses"] = dict(
                Counter(node.attrib["status"] for node in mutations)
            )
            metric["mutantCount"] = len(mutations)
            metric["cumulativeMutationTests"] = sum(
                int(node.attrib.get("numberOfTestsRun", "0")) for node in mutations
            )
            identities = []
            for mutation in mutations:
                indexes, blocks = mutation.find("indexes"), mutation.find("blocks")
                if indexes is None or blocks is None:
                    raise ValueError("Native PIT mutant identity is incomplete.")
                identities.append(
                    tuple(
                        mutation.findtext(field)
                        for field in (
                            "mutatedClass",
                            "mutatedMethod",
                            "methodDescription",
                            "lineNumber",
                            "mutator",
                        )
                    )
                    + (
                        ET.tostring(indexes, encoding="unicode"),
                        ET.tostring(blocks, encoding="unicode"),
                    )
                )
            metric["mutantIdentities"] = sorted(identities)
            native_log = (directory / "output.log").read_text(
                encoding="utf-8-sig", errors="replace"
            )
            line_match = re.search(
                r"Line Coverage \(for mutated classes only\): (\d+)/(\d+)", native_log
            )
            if line_match is None:
                raise ValueError("The native PIT target line summary is missing.")
            metric["lineCoverage"] = {
                "covered": int(line_match[1]),
                "total": int(line_match[2]),
            }
        if "production-class" in artifacts:
            metric["classSHA256"] = artifacts["production-class"]["sha256"]
        measurements[phase] = metric
    complete = all(
        phase in measurements and measurements[phase]["exitCode"] == 0
        for phase in ("jacoco-before", "jacoco-after", "pit-before", "pit-after")
    )
    (root / "evidence/measurement-summary.json").write_text(
        json.dumps(measurements, indent=2) + "\n", encoding="utf-8"
    )
    report = [
        "# JSON-source exception-test evaluation",
        "",
        "All four measurement processes succeeded."
        if complete
        else "This evaluation is incomplete. The available native observations are reported below; unavailable measurements remain unavailable.",
        "",
        "## Identity and scope",
        "",
        f"- Parent generation: `{manifest['parent']['path']}`; exact seal SHA-256 `{manifest['parent']['sealSHA256']}`.",
        f"- Evaluation: `{manifest['runId']}`; independent generation contribution: 0.",
        f"- Baseline commit: `{manifest['baselineCommit']}`.",
        f"- Frozen test SHA-256: `{manifest['frozenTest']['sha256']}`.",
        "- Historical authorized JDK 8 supplemental execution: 10 executed tests, 0 failures, 0 errors, 0 skips. The original generation and its diagnostics remain immutable.",
        "- The canonical paired-full-suite plan selects every existing project test on both sides and adds only the frozen generated test after. The target production class alone is measured and mutated.",
        "- The historical JSON-source record lacks exact generator settings, a machine attestation of fresh-chat isolation, and the original freeze timestamp. This measurement does not retroactively establish those facts or analyzed-JAR/WIT-UP provenance.",
        "- This evaluation uses the exact revision-4 recipes from java-source-001/evaluation-005 with only evaluation-owned paths substituted. Native measurements here replace the historical narrower-scope measurements for the consolidated comparison; the original historical evidence is preserved.",
        '- The prescribed generation command was `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test`; the historical authorized JDK 8 supplemental execution exited 0 with 10 passed tests.',
        "",
        "## Before and after JaCoCo",
        "",
        "| Counter | Before: covered / total | After: covered / total | Before missed | After missed |",
        "| --- | --- | --- | --- | --- |",
    ]
    before = measurements.get("jacoco-before", {}).get("counters", {})
    after = measurements.get("jacoco-after", {}).get("counters", {})
    for counter in ("INSTRUCTION", "BRANCH", "LINE", "COMPLEXITY", "METHOD", "CLASS"):
        left, right = before.get(counter), after.get(counter)
        left_value = (
            percentage(left["covered"], left["covered"] + left["missed"])
            if left
            else "Unavailable"
        )
        right_value = (
            percentage(right["covered"], right["covered"] + right["missed"])
            if right
            else "Unavailable"
        )
        report.append(
            f"| {counter} | {left_value} | {right_value} | {left['missed'] if left else 'Unavailable'} | {right['missed'] if right else 'Unavailable'} |"
        )
    report += [
        "",
        "The before values above come from this evaluation's native measurement, rather than an inferred baseline. JaCoCo line/branch counters and PIT line counters are separate observations. JaCoCo does not count exception handling as branches; see the [official counter definitions](https://www.jacoco.org/jacoco/trunk/doc/counters.html).",
        "",
        "## Before and after PIT",
        "",
        "| Observation | Before | After |",
        "| --- | --- | --- |",
    ]
    pit_before, pit_after = (
        measurements.get("pit-before", {}),
        measurements.get("pit-after", {}),
    )
    statuses = sorted(
        set(pit_before.get("mutationStatuses", {}))
        | set(pit_after.get("mutationStatuses", {}))
    )
    if statuses:
        for status in statuses:
            values = [
                measurement["mutationStatuses"].get(status, 0)
                if "mutationStatuses" in measurement
                else "Unavailable"
                for measurement in (pit_before, pit_after)
            ]
            report.append(f"| {status} | {values[0]} | {values[1]} |")
    for label, field in (
        ("Native mutants", "mutantCount"),
        ("Cumulative mutation-test executions", "cumulativeMutationTests"),
    ):
        report.append(
            f"| {label} | {pit_before.get(field, 'Unavailable')} | {pit_after.get(field, 'Unavailable')} |"
        )
    line_values = [
        percentage(
            measurement["lineCoverage"]["covered"], measurement["lineCoverage"]["total"]
        )
        if "lineCoverage" in measurement
        else "Unavailable"
        for measurement in (pit_before, pit_after)
    ]
    report.append(
        f"| Native target line coverage | {line_values[0]} | {line_values[1]} |"
    )
    for label, strength in (
        ("Mutation score: KILLED / total", False),
        ("Test strength: KILLED / (KILLED + SURVIVED)", True),
    ):
        values = []
        for measurement in (pit_before, pit_after):
            if "mutationStatuses" not in measurement:
                values.append("Unavailable")
            else:
                histogram = measurement["mutationStatuses"]
                killed = histogram.get("KILLED", 0)
                denominator = (
                    killed + histogram.get("SURVIVED", 0)
                    if strength
                    else measurement["mutantCount"]
                )
                values.append(percentage(killed, denominator))
        report.append(f"| {label} | {values[0]} | {values[1]} |")
    report += [
        "",
        "No mutation score or zero baseline is inferred from a failed baseline-validation process or absent native XML. PIT cumulative executions do not represent unique generated tests. Coverage and mutation scores do not establish completeness or correctness against an independent specification. See [PIT's official concepts](https://pitest.org/quickstart/basic_concepts/).",
        "The baseline console's `Test strength 100%` is PIT's zero-denominator display convention. Under the frozen protocol, 0 / (0 + 0) is not applicable, so the report records N/A and preserves the original console output. PIT target line counts above come from the native CLI summary; its per-test line-coverage XML is retained independently.",
        "",
        "## Executions and diagnostics",
        "",
        "| Phase | Process exit | Native tests | Failures | Errors | Skips | Surefire suite attribution |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for phase, (directory, request, result) in records.items():
        counts = result["suiteCounts"] or {}
        report.append(
            f"| {phase} | {result['exitCode']} | {counts.get('tests', 'Unknown')} | {counts.get('failures', 'Unknown')} | {counts.get('errors', 'Unknown')} | {counts.get('skipped', 'Unknown')} | {result['suiteOutcome']} |"
        )
        log = (directory / "output.log").read_text(
            encoding="utf-8-sig", errors="replace"
        )
        if result["exitCode"] or result["protocolProblems"]:
            diagnostics = [
                line
                for line in log.splitlines()
                if any(
                    term in line
                    for term in (
                        "did not pass",
                        "did not pass without mutation",
                        "Tests failing",
                        "tests failed",
                        "SEVERE",
                        "BUILD FAILURE",
                        "ERROR",
                        "WARNING",
                        "Skipping project",
                        "Project has either",
                    )
                )
            ]
            report += [
                "",
                f"### {phase} diagnostic",
                "",
                "```text",
                *diagnostics,
                "```",
                "",
            ]
        if result["protocolProblems"]:
            report += [
                "",
                f"Protocol problems for `{phase}`: "
                + "; ".join(result["protocolProblems"]),
                "",
            ]
    report += [
        "",
        "Surefire counts are losslessly archived per execution. Intrinsic existing skips remain visible. PIT has no Surefire report destination; its process diagnostics and native mutation artifacts are retained separately. Infrastructure operations and missing measurements are not included as failures of the 10 generated tests.",
        "",
        "## Exact toolchain and libraries",
        "",
        "| Component | Exact version or build |",
        "| --- | --- |",
        "| Java vendor | Eclipse Temurin |",
        "| Java language and bytecode target | 1.8 / 1.8 |",
        "| Java runtime | 1.8.0_504-b01 |",
        "| Java VM | 25.504-b01 |",
        "| javac | 1.8.0_504 |",
        "| Maven | 3.9.16; 2bdd9fddda4b155ebf8000e807eb73fd829a51d5 |",
        "| Commons IO | 2.7-SNAPSHOT; Apache Commons parent 50 |",
        "| JUnit Jupiter | 5.5.2 |",
        "| Surefire | 2.22.2 |",
        "| JaCoCo agent and CLI | 0.8.4 |",
        "| PIT CLI / entry / core | 1.15.2 |",
        "| PIT JUnit 5 adapter | 1.2.2 |",
        "| Maven dependency plugin used for preparation | 3.6.1 |",
        "| Maven help plugin used for preparation | 3.5.1 |",
        "| Python | 3.13.15 |",
        f"| PowerShell | {environment['os']['powershell']} |",
        f"| OS | {environment['os']['description']}; {environment['os']['architecture']} |",
        "",
        "### Complete resolved project dependency graph",
        "",
        "```text",
    ]
    preflight = records["preflight"]
    report += [
        (preflight[0] / preflight[2]["artifacts"]["dependencies"]["path"])
        .read_text(encoding="utf-8-sig")
        .rstrip(),
        "```",
        "",
        "The companion `dependency-hashes` artifact records the exact SHA-256 and byte size of every resolved project JAR. The effective-POM artifact retains inherited configuration and plugin versions. The frozen CLI POM declares the launcher dependency graph. Exact invocation flags are preserved in the plan and rendered scripts; the earlier auxiliary mutation POM remains a recipe reference and is not invoked by this pair.",
    ]
    if "launcher-dependencies" in preflight[2]["artifacts"]:
        report += [
            "",
            "### Complete PIT launcher dependency graph",
            "",
            "```text",
            (preflight[0] / preflight[2]["artifacts"]["launcher-dependencies"]["path"])
            .read_text(encoding="utf-8-sig")
            .rstrip(),
            "```",
            "",
            "The captured runtime-hashes artifact records all project and launcher JAR bytes. Launcher dependencies (including Commons Text 1.10.0 and its Commons Lang 3.12.0 dependency) are distinguished from the baseline project's Commons Lang 3.9. Classpath files preserve the actual ordered entries and before/after directory substitutions.",
        ]
    report += [
        "",
        "### Pinned PIT CLI dependency configuration",
        "",
        "```xml",
        (root / "inputs/pit-cli-pom.xml").read_text(encoding="utf-8-sig").rstrip(),
        "```",
        "",
    ]
    invoked_plugins = set()
    for directory, _, _ in records.values():
        invoked_plugins.update(
            re.findall(
                r"--- ([\w-]+):([^\s:]+):([^\s(]+)",
                (directory / "output.log").read_text(
                    encoding="utf-8-sig", errors="replace"
                ),
            )
        )
    report += [
        "",
        "### Invoked Maven plugins and goals",
        "",
        "| Plugin prefix emitted by Maven | Version | Goal |",
        "| --- | --- | --- |",
    ]
    report.extend(
        f"| {plugin} | {version} | {goal} |"
        for plugin, version, goal in sorted(invoked_plugins)
    )
    report += [
        "",
        "### Observed environment and executable locations",
        "",
        "```json",
        json.dumps(environment, indent=2),
        "```",
        "",
        "Process-only JAVA_HOME selects JDK 8, PATH prepends its bin directory, TEMP/TMP and Maven's dependency cache are on D:. Each invocation captures a fresh environment observation; the initial preparation observation above is not substituted for those observations.",
        "",
        "### Measurement configuration",
        "",
        "```json",
        (root / "inputs/measurement-plan.json")
        .read_text(encoding="utf-8-sig")
        .rstrip(),
        "```",
        "",
        "## Exact commands and substitutions",
        "",
        "The following map fixes all before/after checkout, output, tool, environment, and script paths before measurement. Each request retains the exact wrapper command, scope, timestamp, declared artifact roles, and observed environment. The wrapper reserves before execution, captures both streams, and records the process exit immediately.",
        "",
        "```json",
        json.dumps(substitutions, indent=2),
        "```",
        "",
    ]
    report += [
        "",
        "### Support tool versions",
        "",
        "```json",
        (root / "evidence/support-tool-versions.json")
        .read_text(encoding="utf-8-sig")
        .rstrip(),
        "```",
        "",
    ]
    for name in (
        "run-phase.ps1",
        "observe-environment.ps1",
        "preflight.ps1",
        "jacoco-before.ps1",
        "pit-before.ps1",
        "jacoco-after.ps1",
        "pit-after.ps1",
    ):
        report += [
            f"### {name}",
            "",
            "```powershell",
            (root / "evidence/scripts" / name).read_text(encoding="utf-8-sig").rstrip(),
            "```",
            "",
        ]
    hashes = {
        value.get("classSHA256")
        for key, value in measurements.items()
        if key != "preflight"
    }
    report += [
        "## Pairing and preservation",
        "",
        f"Observed target-class hashes: `{', '.join(sorted(value for value in hashes if value))}`.",
        "The preserved script inventory fixes rendered phase-script hashes before execution. The source-pairing inventory verifies every tracked file's raw bytes are equal in both checkouts. The before checkout contains no generated target test; the after checkout contains exactly the parent frozen bytes. Metadata-only Git checks and the manager verify the baseline and original test hash.",
        "",
        "## Complete frozen Java source",
        "",
        "```java",
        source.rstrip(),
        "```",
        "",
    ]
    left_mutants = measurements.get("pit-before", {}).get("mutantIdentities")
    right_mutants = measurements.get("pit-after", {}).get("mutantIdentities")
    if left_mutants is None or right_mutants is None:
        report += [
            "",
            "Missing native PIT XML prevents mutant-universe equality from being established.",
            "",
        ]
    elif left_mutants != right_mutants:
        raise ValueError("The before and after native mutant universes differ.")
    else:
        report += [
            "",
            f"Before and after have the same {len(left_mutants)} native mutant identities (class, method, descriptor, line, mutator, indexes, and blocks).",
            "",
        ]
    for phase in ("jacoco-before", "jacoco-after"):
        counts = measurements.get(phase, {}).get("suiteCounts")
        if counts:
            report += [
                "",
                f"`{phase}`: {counts['tests']} native reported cases, including {counts['skipped']} intrinsic skips; {counts['tests'] - counts['skipped']} non-skipped cases. These full-suite counts are separate from the 10 generated cases.",
            ]
    (root / "report.md").write_text("\n".join(report), encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {"processesSuccessful": complete, "measurements": measurements}, indent=2
        )
    )


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve())
