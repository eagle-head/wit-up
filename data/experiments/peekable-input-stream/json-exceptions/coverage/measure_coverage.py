"""Measure the unchanged exception suite and preserve all original build statuses."""

import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path("D:/Projects/wit-up")
REPO = ROOT / ".worktrees/commons-io-coverage"
CONDITION = ROOT / "data/experiments/peekable-input-stream/json-exceptions"
OUTPUT = CONDITION / "coverage"
HELPER = ROOT / "data/experiments/peekable-input-stream/coverage-comparison/measure_coverage.py"
BASE = "d7a3c884d07ff5f1829b09087f34dcb8043f0f64"
TARGET = Path("src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java")
SOURCE_SHA256 = "C8FCE4484A2B0A8620DB781029F9BDC698FB69ED5AD15F015F2BED1ED98A5536"
context = {"__file__": str(HELPER), "__name__": "coverage_capture"}
exec(compile(HELPER.read_text(encoding="utf-8"), str(HELPER), "exec"), context)
context["REPO"] = REPO
digest = context["digest"]
write_json = context["write_json"]
maven = context["maven"]
now = context["now"]
arguments = context["ARGS"]

assert REPO.resolve().is_relative_to((ROOT / ".worktrees").resolve())
assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip() == BASE
assert not subprocess.check_output(["git", "status", "--porcelain"], cwd=REPO).strip()
assert not (REPO / TARGET).exists()
assert digest(CONDITION / "PeekableInputStreamTest.java") == SOURCE_SHA256
assert not any((OUTPUT / phase).exists() for phase in ("before", "after"))
results = []
for phase in ("before", "after"):
    if phase == "after":
        shutil.copy2(CONDITION / "PeekableInputStreamTest.java", REPO / TARGET)
        assert digest(REPO / TARGET) == SOURCE_SHA256
    run = OUTPUT / phase
    run.mkdir(parents=True)
    metadata = {
        "condition": "json-exceptions",
        "phase": phase,
        "baseline_commit": BASE,
        "working_directory": REPO.as_posix(),
        "maven_executable": context["MAVEN"],
        "java_home": context["JAVA"],
        "arguments": arguments,
        "started_at_utc": now(),
        "target_test_exists": (REPO / TARGET).exists(),
        "original_generation_build_status": "Failed before compilation at Apache RAT",
        "isolated_measurement": True,
        "local_ruff_cache_present": (REPO / ".ruff_cache").exists(),
    }
    if phase == "after":
        metadata["target_test_sha256"] = digest(REPO / TARGET)
    write_json(run / "run.json", metadata)
    environment_exit = maven(["--version"], run / "environment.log")
    if environment_exit:
        raise RuntimeError(f"Maven environment command failed: {environment_exit}")
    print(f"{now()} Starting {phase} coverage measurement", flush=True)
    metadata["exit_code"] = maven(arguments, run / "maven.log")
    metadata["completed_at_utc"] = now()
    write_json(run / "run.json", metadata)
    print(f"{now()} {phase} Maven exit: {metadata['exit_code']}", flush=True)
    if not (REPO / "target/site/jacoco/jacoco.xml").exists():
        if not (REPO / "target/jacoco.exec").is_file():
            raise RuntimeError("No execution data; inspect the preserved failed-build log.")
        report_arguments = ["-B", "-Pjacoco", "-Djacoco.skip=false", "jacoco:report"]
        report = {"arguments": report_arguments, "started_at_utc": now()}
        report["exit_code"] = maven(report_arguments, run / "report-only.log")
        report["completed_at_utc"] = now()
        metadata["report_only_command"] = report
        write_json(run / "run.json", metadata)
        if report["exit_code"]:
            raise RuntimeError("Coverage reporting failed; original build status remains recorded.")
    context["capture"](run)
    results.append({"phase": phase, "build_exit_code": metadata["exit_code"]})
    write_json(OUTPUT / "execution-summary.json", results)
    print(f"{now()} Archived {phase} measurement", flush=True)
assert digest(REPO / TARGET) == SOURCE_SHA256
print("Both measurements archived; original checkout was not used for execution.", flush=True)
raise SystemExit(1 if any(row["build_exit_code"] for row in results) else 0)

