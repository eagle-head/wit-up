"""Consolidate two preserved evaluations without changing their frozen inputs."""

import json
import re
import runpy
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def ratio(numerator, denominator):
    return (
        f"{numerator}/{denominator} ({100 * numerator / denominator:.2f}%)"
        if denominator
        else "N/A (0/0)"
    )


def collect(root, study):
    manifest = read_json(root / "run.json")
    parent = study / manifest["parent"]["path"]
    generation = read_json(parent / "run.json")
    measurements = read_json(root / "evidence/measurement-summary.json")
    records = {}
    for entry in manifest["executions"]:
        directory = root / entry["path"]
        result = read_json(directory / "result.json")
        if result["exitCode"] or result["protocolProblems"]:
            raise ValueError("A selected measurement execution is not successful.")
        records[result["phase"]] = {
            "directory": directory,
            "result": result,
            "request": read_json(directory / "request.json"),
            "environment": read_json(directory / "environment.json"),
        }
    for phase in ("jacoco-before", "pit-before", "jacoco-after", "pit-after"):
        if phase not in records or measurements[phase]["exitCode"]:
            raise ValueError("The selected evaluation lacks a complete pair.")
    generated = []
    archive = records["jacoco-after"]["directory"] / "surefire-reports.zip"
    with ZipFile(archive) as reports:
        for name in reports.namelist():
            if not name.endswith(".xml"):
                continue
            suite = ET.fromstring(reports.read(name))
            if suite.attrib.get("name") != (
                "org.apache.commons.io.input.buffer.PeekableInputStreamTest"
            ):
                continue
            if any(
                int(suite.attrib.get(key, "0"))
                for key in ("failures", "errors", "skipped")
            ):
                raise ValueError(
                    "Generated test failures or skips require explicit reporting."
                )
            generated = [node.attrib["name"] for node in suite.findall("testcase")]
            if len(generated) != int(suite.attrib["tests"]):
                raise ValueError("Generated native case counts disagree.")
    if not generated:
        raise ValueError(
            "The generated suite is missing from native Surefire evidence."
        )
    return {
        "root": root,
        "manifest": manifest,
        "parent": parent,
        "generation": generation,
        "metrics": measurements,
        "records": records,
        "generatedCases": generated,
        "substitutions": read_json(root / "evidence/substitutions.json"),
    }


def artifact(data, role):
    preflight = data["records"]["preflight"]
    return preflight["directory"] / preflight["result"]["artifacts"][role]["path"]


def dependencies(data):
    return {
        item["path"].replace("\\", "/").split("/maven-repository/", 1)[1]: item
        for item in read_json(artifact(data, "runtime-hashes"))
    }


def main():
    json_root = Path(__file__).resolve().parents[2]
    study = json_root.parents[3]
    repository = study.parents[1]
    java_root = study / "supplements/java-source/001/005"
    manager = runpy.run_path(str(repository / "tools/experiment_runs.py"))
    for root in (json_root, java_root):
        if not manager["verify"](root)["sealed"]:
            raise ValueError("The consolidated report requires sealed evaluations.")
        if read_json(root / "seal.json")["outcome"] != "evaluation-complete":
            raise ValueError("A selected evaluation is not complete.")
    data = [collect(root, study) for root in (json_root, java_root)]
    labels = ["WIT-UP JSON", "Java source"]
    if read_json(json_root / "inputs/measurement-plan.json") != read_json(
        java_root / "inputs/measurement-plan.json"
    ):
        raise ValueError("The measurement plans differ.")
    runtime = [dependencies(item) for item in data]
    if {key: value["sha256"] for key, value in runtime[0].items()} != {
        key: value["sha256"] for key, value in runtime[1].items()
    }:
        raise ValueError("The measured runtime artifacts differ.")
    class_hashes = {
        metric["classSHA256"]
        for item in data
        for phase, metric in item["metrics"].items()
        if phase != "preflight"
    }
    mutant_sets = [
        item["metrics"][phase]["mutantIdentities"]
        for item in data
        for phase in ("pit-before", "pit-after")
    ]
    if len(class_hashes) != 1 or any(
        value != mutant_sets[0] for value in mutant_sets[1:]
    ):
        raise ValueError("The production class or native mutant universe differs.")
    generated_counts = [len(item["generatedCases"]) for item in data]
    killed = [
        item["metrics"]["pit-after"]["mutationStatuses"].get("KILLED", 0)
        for item in data
    ]
    total = len(mutant_sets[0])
    score_difference = 100 * (killed[1] - killed[0]) / total
    report = [
        "# Exception-Test Generation from WIT-UP JSON and Java Source",
        "",
        "## Consolidated pilot report",
        "",
        f"Prepared for academic review on {datetime.now(UTC).date().isoformat()} (UTC).",
        "",
        "This report compares two already generated, frozen JUnit suites for Apache Commons IO's `PeekableInputStream`. Both suites were evaluated using the same paired full-suite protocol, configuration revision 4. The JSON-source suite was measured again in a new evaluation; the Java-source evaluation was reused from its verified sealed record. Each baseline was actually measured. No test was revised using execution, coverage, or mutation feedback.",
        "",
        f"The JSON-source suite contains {generated_counts[0]} passing cases and the Java-source suite contains {generated_counts[1]} passing cases. The corresponding suites killed {killed[0]} and {killed[1]} of the same {total} native mutants. The observed mutation-score difference is {score_difference:.2f} percentage points in favor of the Java-source suite in these two observations.",
        "",
        "This is a descriptive pilot comparison of one recorded generation per source condition. Measurement controls are aligned; generation controls are not fully established for the historical JSON record. Unknown model/settings and isolation metadata, different suite sizes, and the absence of independent repetitions prevent attributing the difference solely to the source condition or claiming general superiority.",
        "",
        "## Objective and scope",
        "",
        "The question is how two frozen suites generated from different permitted information sources behave under the same execution, coverage, and mutation measurement configuration. Generation targeted exceptional behavior of the public constructors and declared `peek` overloads of `org.apache.commons.io.input.buffer.PeekableInputStream`. Every generated case was required to assert an exception from a target call; normal operations could only establish fixture state.",
        "",
        "The JSON condition used the original WIT-UP results and summaries exports. The Java-source condition used the designated production source and permitted superclass/buffer implementation. The preserved prompts specify these boundaries in full in the appendices. Generation and measurement are separate phases; evaluation supplements contribute zero additional independent generations.",
        "",
        "## Records and preservation",
        "",
        "| Item | WIT-UP JSON | Java source |",
        "| --- | --- | --- |",
    ]
    for label, values in (
        ("Generation", [item["generation"]["runId"] for item in data]),
        ("Evaluation", [item["manifest"]["runId"] for item in data]),
        ("Recorded origin", [item["generation"]["origin"] for item in data]),
        ("Executed generated cases in the aligned after phase", generated_counts),
        (
            "Frozen Java SHA-256",
            [item["manifest"]["frozenTest"]["sha256"] for item in data],
        ),
        (
            "Parent seal SHA-256",
            [item["manifest"]["parent"]["sealSHA256"] for item in data],
        ),
        (
            "Evaluation seal SHA-256",
            [
                sha256((item["root"] / "seal.json").read_bytes()).hexdigest()
                for item in data
            ],
        ),
    ):
        report.append(f"| {label} | {values[0]} | {values[1]} |")
    report += [
        "",
        "Both conditions use Commons IO commit `11f0abe7a3fb6954b2985ca4ab0697b2fb489e84`. Before/after checkouts are distinct, and their complete tracked-file inventories match. The only added source in each after checkout is that generation's exact frozen Java file. Existing tests, production source, resource files, and checkout build configuration remain unchanged.",
        "",
        f"The production class SHA-256 is `{next(iter(class_hashes))}` across all eight selected measurement phases. All four PIT artifacts contain the same {total} mutant identities, including class, method, descriptor, source line, mutator, indexes, and blocks. All 23 unique project/launcher JARs have identical bytes across the two evaluations; the ordered classpaths also match after evaluation-path substitution.",
        "",
        "## Aligned before and after results",
        "",
        "All rows below describe the target production class, not coverage of the whole Commons IO library. Percentages are calculated from native integer counters. Before denotes a clean baseline checkout measured during the evaluation, not a claimed measurement from before generation. The historical JSON measurements used different selections and are retained separately; none of those historical values supplies this comparison table.",
        "",
        "| Metric | JSON before | JSON after | Java before | Java after |",
        "| --- | --- | --- | --- | --- |",
    ]
    for counter in ("INSTRUCTION", "BRANCH", "LINE", "COMPLEXITY", "METHOD", "CLASS"):
        values = []
        for item in data:
            for phase in ("jacoco-before", "jacoco-after"):
                counts = item["metrics"][phase]["counters"][counter]
                values.append(
                    ratio(counts["covered"], counts["covered"] + counts["missed"])
                )
        report.append(f"| JaCoCo {counter.lower()} | " + " | ".join(values) + " |")
    for label, kind in (
        ("PIT mutation score", "score"),
        ("PIT test strength", "strength"),
        ("PIT native line coverage", "line"),
    ):
        values = []
        for item in data:
            for phase in ("pit-before", "pit-after"):
                metric = item["metrics"][phase]
                histogram = metric["mutationStatuses"]
                numerator = histogram.get("KILLED", 0)
                denominator = metric["mutantCount"]
                if kind == "strength":
                    denominator = numerator + histogram.get("SURVIVED", 0)
                elif kind == "line":
                    numerator = metric["lineCoverage"]["covered"]
                    denominator = metric["lineCoverage"]["total"]
                values.append(ratio(numerator, denominator))
        report.append(f"| {label} | " + " | ".join(values) + " |")
    for status in (
        "KILLED",
        "SURVIVED",
        "NO_COVERAGE",
        "TIMED_OUT",
        "RUN_ERROR",
        "MEMORY_ERROR",
        "NON_VIABLE",
    ):
        values = [
            str(item["metrics"][phase]["mutationStatuses"].get(status, 0))
            for item in data
            for phase in ("pit-before", "pit-after")
        ]
        report.append(f"| PIT {status} | " + " | ".join(values) + " |")
    values = [
        str(item["metrics"][phase]["cumulativeMutationTests"])
        for item in data
        for phase in ("pit-before", "pit-after")
    ]
    report.append(
        "| PIT cumulative mutation-test executions | " + " | ".join(values) + " |"
    )
    report += [
        "",
        "Mutation score is `KILLED / all native mutants`, retaining `NO_COVERAGE` in the denominator. Test strength is `KILLED / (KILLED + SURVIVED)`; a zero denominator is N/A even where PIT's native console displays 100%. No equivalent-mutant exclusions were introduced. A surviving mutant was not detected by a covering test; this report does not claim that every survivor represents a distinct real defect. See [PIT's outcome definitions](https://pitest.org/quickstart/basic_concepts/).",
        "",
        "JaCoCo and PIT line coverage are separate observations and are not substituted for each other. JaCoCo's branch definition does not count exception handling as branches, so 100% branch coverage does not establish complete exceptional-behavior coverage. See [JaCoCo's counter definitions](https://www.jacoco.org/jacoco/trunk/doc/counters.html). Coverage and mutation measurements do not establish correctness against an independent specification.",
        "",
        "## Execution outcomes",
        "",
        "| Condition | Phase | Process exit | Native Surefire cases | Failures | Errors | Skips |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for label, item in zip(labels, data, strict=True):
        for phase in ("jacoco-before", "pit-before", "jacoco-after", "pit-after"):
            result = item["records"][phase]["result"]
            counts = result["suiteCounts"] or {}
            report.append(
                f"| {label} | {phase} | {result['exitCode']} | {counts.get('tests', 'Not emitted')} | {counts.get('failures', 'Not emitted')} | {counts.get('errors', 'Not emitted')} | {counts.get('skipped', 'Not emitted')} |"
            )
    report += [
        "",
        "The six intrinsic skips belong to the existing project suite. Neither generated suite has failures, errors, or skips in its native after-phase Surefire XML. PIT performs its own unmutated-test validation and emits native mutation artifacts, but no Surefire suite totals; those totals are not invented. Cumulative mutation-test executions are not unique generated cases, independent samples, or the size of PIT's unmutated baseline.",
        "",
        "## Interpretation and limits",
        "",
        "The comparison supports a bounded observation about these two suites: their target execution coverage and detection of the same generated mutations under the recorded measurement configuration. It does not estimate an average effect, statistical significance, or a general ranking of information sources.",
        "",
        "The historical JSON generation report records ten tests supported by ten SAT records, with other candidates lacking supported public fixtures. That generation report also records fixture adaptations and limits on reproducing exact internal paths. The Java-source generation report records assertions on supported exception messages, validation order, and propagated exceptions. These are recorded differences between the actual suites; their causal contribution to the measured score difference has not been isolated.",
        "",
        "Exact generator model, settings, and application build are unknown for both records. The JSON run is a retrospective import with unavailable freeze time and no retained machine attestation of fresh-chat isolation; the Java-source run has prospective metadata and a true fresh-chat attestation. The analyzed WIT-UP JAR bytes and producing WIT-UP revision remain unverified. Uniform measurements do not repair those historical generation-provenance gaps.",
        "",
        "## Diagnostics retained outside result totals",
        "",
        "Historical JSON startup failures and exploratory PIT failures remain in the original sealed diagnostic record. Four earlier Java-source evaluations remain sealed incomplete, covering preparation parsing, skipped PIT discovery, and relative-resource/native-directory failures. Those operations do not supply the valid measurement metrics and are not counted as failures of generated cases that did not execute. Their actual process failures and any unmutated existing-test failures remain preserved.",
        "",
        "The Java-source generation also retains two findings from a separate direct Checkstyle check of its frozen test: missing package-info.java and missing Javadoc on a private fixture constructor. They were not repaired after freezing and are separate from JUnit outcomes. The selected full-suite Maven lifecycles and PIT processes succeeded; this statement does not reclassify the separate style check as passing.",
        "",
        "## Reproduction environment and configuration",
        "",
        "| Component | Exact version or configuration |",
        "| --- | --- |",
        "| Java vendor/runtime | Eclipse Temurin; 1.8.0_504-b01 |",
        "| JVM / javac | 25.504-b01 / 1.8.0_504 |",
        "| Java source/target | 1.8 / 1.8 |",
        "| Maven | 3.9.16; build 2bdd9fddda4b155ebf8000e807eb73fd829a51d5 |",
        "| Commons IO / Apache Commons parent | 2.7-SNAPSHOT / 50 |",
        "| JUnit Jupiter / Platform | 5.5.2 / 1.5.2 |",
        "| Surefire | 2.22.2 |",
        "| JaCoCo agent and CLI | 0.8.4 |",
        "| PIT CLI, entry, core / JUnit 5 adapter | 1.15.2 / 1.2.2 |",
        "| Maven dependency / help plugins | 3.6.1 / 3.5.1 |",
        "| Python | 3.13.15 |",
        "| PowerShell | 7.6.5 |",
        "| OS | Microsoft Windows 10.0.26300; X64 |",
        "",
        "Exact executable locations, flags, OS observations, and process environment values are recorded before every invocation. The commands select JDK 8 for the process and direct TEMP/TMP and the Maven repository to the evaluation's exclusive D: working directory. Dependency configuration and bytes are identical between conditions; the complete runtime inventory appears below.",
        "",
        "```json",
        (json_root / "inputs/measurement-plan.json")
        .read_text(encoding="utf-8-sig")
        .rstrip(),
        "```",
        "",
        "### Complete runtime JAR inventory",
        "",
        "Paths are relative to each evaluation's `maven-repository` and encode group, artifact, and exact version. The hash column is common to both evaluations. The recorded classpaths retain ordering and distinguish project Commons Lang 3.9 from launcher Commons Lang 3.12.0.",
        "",
        "| Maven artifact path | SHA-256 | Bytes |",
        "| --- | --- | --- |",
    ]
    report.extend(
        f"| `{key}` | `{value['sha256']}` | {value['bytes']} |"
        for key, value in sorted(runtime[0].items())
    )
    report += [
        "",
        "### Invoked Maven plugins and goals",
        "",
        "| Plugin | Version | Goal |",
        "| --- | --- | --- |",
    ]
    plugins = set()
    for item in data:
        for record in item["records"].values():
            plugins.update(
                re.findall(
                    r"--- ([\w-]+):([^\s:]+):([^\s(]+)",
                    (record["directory"] / "output.log").read_text(
                        encoding="utf-8-sig", errors="replace"
                    ),
                )
            )
    report.extend(
        f"| {plugin} | {version} | {goal} |"
        for plugin, version, goal in sorted(plugins)
    )
    report += [
        "",
        "## Commands and evaluation-specific parameters",
        "",
        'The prescribed generation test command was `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test`. Its historical JSON supplemental result was 10 passing cases; its Java-source initial result was 20 passing cases. This evaluation did not regenerate either suite.',
        "",
        "The following are the actual reserved commands for the selected measurements, executed from `D:/Projects/wit-up`. Each phase script, its environment assignments, and every native command is reproduced in the linked evaluation report. The common commands and resolved phase paths follow, so command parameters are not left for the reader to discover.",
        "",
        "| Condition | Phase | Reserved command |",
        "| --- | --- | --- |",
    ]
    for label, item in zip(labels, data, strict=True):
        for phase, record in item["records"].items():
            report.append(f"| {label} | {phase} | `{record['request']['command']}` |")
    report += [
        "",
        "| Condition | Phase | Reserved at (UTC) | Recorded at (UTC) |",
        "| --- | --- | --- | --- |",
    ]
    for label, item in zip(labels, data, strict=True):
        for phase, record in item["records"].items():
            report.append(
                f"| {label} | {phase} | {record['request']['reservedAt']} | {record['result']['recordedAt']} |"
            )
    for label, item in zip(labels, data, strict=True):
        report += [
            "",
            f"### {label}: exact substitutions",
            "",
            "```json",
            json.dumps(item["substitutions"], indent=2),
            "```",
            "",
            f"### {label}: observed preparation environment",
            "",
            "```json",
            json.dumps(read_json(item["root"] / "inputs/environment.json"), indent=2),
            "```",
        ]
    report += [
        "",
        "### Common phase commands",
        "",
        "The variables below resolve directly from each preceding substitution map: `$workingDirectory`, `$agentJar`, and `$cliJar` are top-level fields; `$phaseCheckout`, `$phaseOutput`, and `$temporaryDirectory` are that phase's `checkout`, `output`, and `temp`; `$phaseClasspathFile` and `$toolClasspathFile` are the PIT phase fields. The complete preflight commands are preserved in each evaluation report and hashed script.",
        "",
        "```powershell",
        "$env:JAVA_HOME = 'C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1'",
        '$env:PATH = "$env:JAVA_HOME/bin;$env:PATH"',
        '$env:TEMP = "$workingDirectory/temp"',
        "$env:TMP = $env:TEMP",
        '$env:MAVEN_ARGS = "-Dmaven.repo.local=$workingDirectory/maven-repository"',
        "Set-Location -LiteralPath $phaseCheckout",
        '$executionData = "$phaseOutput/jacoco.exec"',
        '$coverageXml = "$phaseOutput/jacoco.xml"',
        '$env:MAVEN_OPTS = "-DargLine=-javaagent:$agentJar=destfile=$executionData,append=true,includes=org.apache.commons.io.input.buffer.PeekableInputStream"',
        "mvn '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' clean test",
        '$classFile = "$phaseCheckout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class"',
        "java -jar $cliJar report $executionData --classfiles $classFile --xml $coverageXml --name 'PeekableInputStream paired measurement'",
        "```",
        "",
        "The actual phase scripts check and record each process exit immediately, refuse reused output, and stop after a failing command. `begin` reserves the invocation before execution and `record` captures logs and native artifacts afterward.",
        "",
        "```powershell",
        "Set-Location -LiteralPath $phaseCheckout",
        "$env:MAVEN_OPTS = '-DargLine='",
        "$toolClasspath = (Get-Content -LiteralPath $toolClasspathFile -Raw).Trim()",
        'java "-Djava.io.tmpdir=$temporaryDirectory" -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir $phaseOutput --targetClasses org.apache.commons.io.input.buffer.PeekableInputStream --targetTests \'org.apache.commons.io.*\' --sourceDirs "$phaseCheckout/src/main/java" --classPathFile $phaseClasspathFile --includeLaunchClasspath false --mutationEngine gregor --mutators DEFAULTS --threads 1 --timeoutFactor 1.25 --timeoutConst 3000 --jvmArgs "-Xmx256m,-Djava.io.tmpdir=$temporaryDirectory" --outputFormats XML --timestampedReports false --exportLineCoverage true --failWhenNoMutations true --skipFailingTests false --projectBase $phaseCheckout --inputEncoding UTF-8 --outputEncoding UTF-8',
        "```",
        "",
        "The pinned CLI runs from the real checkout directory so existing relative-resource fixtures have the same working directory as Surefire. This resolves the recorded auxiliary-POM launch-directory problem without narrowing tests or skipping failing cases. See the [official CLI documentation](https://pitest.org/quickstart/commandline/); the pinned local CLI help and actual invocation logs establish the options used here.",
        "",
        "## Evidence navigation",
        "",
    ]
    for label, item in zip(labels, data, strict=True):
        relative = item["root"].relative_to(study).as_posix()
        parent = item["parent"].relative_to(study).as_posix()
        original_report = (
            "evidence/peekable-input-stream-report.md"
            if label == "WIT-UP JSON"
            else "report.md"
        )
        report.append(
            f"- {label}: [generation report](../{parent}/{original_report}), [selected evaluation report](../{relative}/report.md), [native executions](../{relative}/executions/), [evaluation seal](../{relative}/seal.json)."
        )
    report += [
        "- [Original JSON execution diagnostics](../runs/json/001/evidence/execution-diagnostics.md).",
        "- [Registry of sealed evaluations and retained unsuccessful attempts](../README.md).",
        "",
    ]
    for label, item in zip(labels, data, strict=True):
        report += [
            f"### {label}: complete preparation commands",
            "",
            "The invocation wrapper selects the recorded process environment before running these commands. Its reservation and native-artifact receipts are linked above.",
            "",
            "```powershell",
            (item["root"] / "evidence/scripts/preflight.ps1")
            .read_text(encoding="utf-8-sig")
            .rstrip(),
            "```",
            "",
            f"### {label}: preservation and reporting tool versions",
            "",
            "```json",
            (item["root"] / "evidence/support-tool-versions.json")
            .read_text(encoding="utf-8-sig")
            .rstrip(),
            "```",
            "",
        ]
    report += ["## Appendix A: Complete frozen JSON-source Java test", ""]
    sources = []
    for index, item in enumerate(data):
        if index:
            report += ["## Appendix B: Complete frozen Java-source Java test", ""]
        source = (
            (item["parent"] / item["generation"]["frozenTest"]["path"])
            .read_text(encoding="utf-8-sig")
            .rstrip()
        )
        sources.append(source)
        report += ["```java", source, "```", ""]
    for label, item in zip(labels, data, strict=True):
        report += [
            f"## Preserved generation prompt: {label}",
            "",
            "This is the original generation instruction, retained as provenance rather than a new execution request.",
            "",
            "```text",
            (item["parent"] / item["generation"]["prompt"]["path"])
            .read_text(encoding="utf-8-sig")
            .rstrip(),
            "```",
            "",
        ]
    destination = study / "reports/exception-test-generation-comparison.md"
    destination.parent.mkdir(exist_ok=True)
    if destination.exists():
        raise ValueError("Refuse to overwrite an existing consolidated report.")
    content = "\n".join(report)
    if re.findall(r"```java\n(.*?)\n```", content, flags=re.DOTALL) != sources:
        raise ValueError("The consolidated Java code blocks are incomplete or differ.")
    destination.write_text(content, encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {
                "report": str(destination),
                "generatedCases": generated_counts,
                "killedMutants": killed,
                "mutantUniverse": total,
                "productionClassHashes": sorted(class_hashes),
                "sha256": sha256(destination.read_bytes()).hexdigest(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
