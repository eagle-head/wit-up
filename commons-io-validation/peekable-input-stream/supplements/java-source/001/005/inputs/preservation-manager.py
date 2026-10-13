"""Reserve, freeze, record, and preserve experimental evidence without running Maven."""

import argparse
import json
import os
import shutil
import subprocess
import xml.etree.ElementTree as ET
from contextlib import contextmanager
from datetime import UTC, datetime
from functools import wraps
from hashlib import file_digest, sha256
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

REPOSITORY = Path(__file__).resolve().parents[1]
DEFAULT_STUDY = REPOSITORY / "commons-io-validation/peekable-input-stream"
BASELINE = "11f0abe7a3fb6954b2985ca4ab0697b2fb489e84"
TEST_PATH = (
    "src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java"
)
FROZEN_PATH = "evidence/test-source/PeekableInputStreamTest.java"
CONDITIONS = ("json", "java-source")
SOURCE_TAGS = {
    "json": "Source kind: WIT-UP JSON exports only.",
    "java-source": "Source kind: Java production source only.",
}
PHASES = (
    "preflight",
    "generated-tests",
    "supplemental-tests",
    "infrastructure",
    "jacoco-before",
    "jacoco-after",
    "pit-before",
    "pit-after",
)
MEASUREMENTS = PHASES[4:]
OUTCOMES = (
    "generation-complete",
    "evaluation-complete",
    "incomplete",
    "no-supported-tests",
    "contaminated",
    "preflight-failed",
    "annotation",
)
PROCESS_FILES = (
    "AGENTS.md",
    "docs/run-methodology.md",
    "docs/measurement-protocol.md",
    "docs/measurement-plan.json",
    "docs/pit-analysis-pom.xml",
)


class PreservationError(ValueError):
    """The requested operation violates the evidence contract."""


def now():
    return datetime.now(UTC).isoformat(timespec="microseconds")


def digest(path):
    with Path(path).open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def write_json(path, data, *, exclusive=False):
    path = Path(path)
    output = path if exclusive else path.with_name(path.name + ".tmp")
    with output.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(data, indent=2, ensure_ascii=True) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    if not exclusive:
        output.replace(path)


def require_d(path):
    result = Path(path).resolve()
    if result.drive.upper() != "D:":
        raise PreservationError("Project and backup storage must be on D:.")
    return result


def inside(root, relative):
    root = Path(root).resolve()
    result = (root / relative).resolve()
    if result == root or not result.is_relative_to(root):
        raise PreservationError("Artifact path must stay inside its record directory.")
    return result


def inventory(root, *, exclude_seal=True):
    root = Path(root)
    files = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or getattr(path.lstat(), "st_file_attributes", 0) & 0x400:
            raise PreservationError("Evidence must not contain reparse points.")
        if path.is_file() and not (exclude_seal and path == root / "seal.json"):
            files.append(
                {
                    "path": path.relative_to(root).as_posix(),
                    "bytes": path.stat().st_size,
                    "sha256": digest(path),
                }
            )
    return files


def git(checkout, *arguments):
    result = subprocess.run(
        ["git", "-C", str(checkout), *arguments],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        raise PreservationError(result.stderr.strip() or "Git check failed.")
    return result.stdout.strip()


def check_checkout(checkout, commit, *, absent=False, frozen_hash=None):
    checkout = require_d(checkout)
    if git(checkout, "rev-parse", "HEAD") != commit:
        raise PreservationError("Checkout HEAD does not match the fixed baseline.")
    git(checkout, "diff", "--quiet", commit, "--")
    status = git(checkout, "status", "--porcelain", "--untracked-files=all")
    allowed = "?? " + TEST_PATH if frozen_hash else ""
    if status and status != allowed:
        raise PreservationError("Checkout contains changes outside the target test.")
    source = checkout / TEST_PATH
    if absent and source.exists():
        raise PreservationError("An earlier target test is present.")
    if frozen_hash and (not source.is_file() or digest(source) != frozen_hash):
        raise PreservationError("The checkout test differs from the frozen test.")
    return checkout


@contextmanager
def lock(path):
    path = require_d(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        write_json(path, {"pid": os.getpid(), "createdAt": now()}, exclusive=True)
    except FileExistsError as error:
        raise PreservationError(f"An operation owns the lock: {path}") from error
    try:
        yield
    finally:
        path.unlink()


def locked(operation):
    @wraps(operation)
    def guarded(run, *args, **kwargs):
        run = require_d(run)
        with lock(run.parent / f".{run.name}.operation.lock"):
            return operation(run, *args, **kwargs)

    return guarded


def load_run(run):
    run = require_d(run)
    data = read_json(run / "run.json")
    if data.get("recordKind", "generation") == "generation":
        condition, sequence = run.parent.name, run.name
        identity = f"{condition}-{sequence}"
    else:
        condition, sequence = run.parent.parent.name, run.parent.name
        identity = f"{condition}-{sequence}/{data['recordKind']}-{run.name}"
    if (data["condition"], data["sequence"], data["runId"]) != (
        condition,
        sequence,
        identity,
    ):
        raise PreservationError("The record identity does not match its directory.")
    return run, data


def writable_run(run):
    run, data = load_run(run)
    if (run / "seal.json").exists():
        raise PreservationError(
            "A sealed record cannot be modified; create a supplement."
        )
    return run, data


def snapshot(run, source, relative):
    source = require_d(source)
    target = inside(run, relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    expected = digest(source)
    with source.open("rb") as original, target.open("xb") as output:
        shutil.copyfileobj(original, output)
    if digest(target) != expected or digest(source) != expected:
        raise PreservationError("An input changed while being preserved.")
    return {"path": relative, "sha256": expected, "originalPath": source.as_posix()}


def observed_environment(path):
    data = read_json(path)
    for field in ("java", "javac", "maven", "os", "processEnvironment"):
        if not data.get(field):
            raise PreservationError(f"Record the observed {field} before proceeding.")
    return data


def next_directory(parent):
    parent.mkdir(parents=True, exist_ok=True)
    values = [int(p.name) for p in parent.iterdir() if p.is_dir() and p.name.isdigit()]
    result = parent / f"{max(values, default=0) + 1:03d}"
    result.mkdir()
    return result


def check_sources(data):
    for source in data.get("sourceInputs", []):
        for key in ("originalPath", "preservedPath"):
            if digest(require_d(source[key])) != source["sha256"]:
                raise PreservationError(f"A scenario input changed: {source[key]}")


def live_check(data):
    check_sources(data)
    frozen = data.get("frozenTest")
    check_checkout(
        data["checkout"],
        data["baselineCommit"],
        absent=not frozen,
        frozen_hash=frozen["sha256"] if frozen else None,
    )


def initialize(study, condition, checkout, template, environment, *, commit=BASELINE):
    if condition not in CONDITIONS:
        raise PreservationError("Unknown source condition.")
    study, checkout = require_d(study), require_d(checkout)
    with lock(study / ".preparation.lock"):
        for existing in list((study / "runs").glob("*/*/run.json")) + list(
            (study / "supplements").glob("*/*/*/run.json")
        ):
            other = read_json(existing).get("checkout")
            if other and require_d(other) == checkout:
                raise PreservationError("A checkout cannot be assigned to two records.")
        run = next_directory(study / "runs" / condition)
        data = {
            "schemaVersion": 2,
            "recordKind": "generation",
            "runId": f"{condition}-{run.name}",
            "condition": condition,
            "sequence": run.name,
            "createdAt": now(),
            "origin": "prospective",
            "state": "preparing",
            "baselineCommit": commit,
            "checkout": checkout.as_posix(),
            "frozenTest": None,
            "preservedInputs": [],
            "sourceInputs": [],
            "executions": [],
            "isolation": {"freshChat": None, "enforcement": "procedural"},
        }
        write_json(run / "run.json", data, exclusive=True)
        try:
            check_checkout(checkout, commit, absent=True)
            working = checkout.parent / ".working" / data["runId"]
            working.mkdir(parents=True, exist_ok=False)
            data["workingDirectory"] = working.as_posix()
            template_copy = snapshot(run, template, "inputs/template.txt")
            data["preservedInputs"].append(template_copy)
            environment_copy = snapshot(run, environment, "inputs/environment.json")
            data["environment"] = environment_copy
            env = observed_environment(run / environment_copy["path"])
            data["generator"] = env.get(
                "generator",
                {
                    "model": None,
                    "settings": None,
                    "reason": "Generator settings were not observable.",
                },
            )
            for relative in PROCESS_FILES:
                data["preservedInputs"].append(
                    snapshot(run, REPOSITORY / relative, "inputs/process/" + relative)
                )
            data["preservedInputs"].append(
                snapshot(run, Path(__file__), "inputs/preservation-manager.py")
            )
            for index, source in enumerate(env.get("additionalInstructions", [])):
                data["preservedInputs"].append(
                    snapshot(run, source, f"inputs/additional/{index:03d}.txt")
                )
            replacements = {
                "{{CHECKOUT}}": checkout.as_posix(),
                "{{RUN_ROOT}}": run.as_posix(),
                "{{STUDY_REPOSITORY}}": REPOSITORY.as_posix(),
                "{{PROCESS_ROOT}}": (run / "inputs/process").as_posix(),
                "{{WORKING_ROOT}}": working.as_posix(),
            }
            if condition == "json":
                sources = env.get("sourceInputs", [])
                if len(sources) != 2 or {s.get("role") for s in sources} != {
                    "results",
                    "summaries",
                }:
                    raise PreservationError(
                        "Provide exactly the results and summaries input snapshots."
                    )
                for source in sources:
                    item = {
                        "role": source["role"],
                        "originalPath": require_d(source["path"]).as_posix(),
                        "preservedPath": require_d(source["backup"]).as_posix(),
                        "sha256": source["sha256"],
                    }
                    if item["originalPath"] == item["preservedPath"]:
                        raise PreservationError(
                            "Raw inputs require a separate verified backup."
                        )
                    data["sourceInputs"].append(item)
                    replacements["{{SOURCE_" + source["role"].upper() + "}}"] = item[
                        "preservedPath"
                    ]
                check_sources(data)
            else:
                archive = run / "inputs/production-source.zip"
                git(
                    checkout,
                    "archive",
                    "--format=zip",
                    f"--output={archive}",
                    commit,
                    "src/main/java",
                )
                data["preservedInputs"].append(
                    {"path": "inputs/production-source.zip", "sha256": digest(archive)}
                )
            prompt = (run / template_copy["path"]).read_text(encoding="utf-8-sig")
            if SOURCE_TAGS[condition] not in prompt or any(
                tag in prompt for key, tag in SOURCE_TAGS.items() if key != condition
            ):
                raise PreservationError(
                    "The prompt source condition does not match the record."
                )
            for token, value in replacements.items():
                prompt = prompt.replace(token, value)
            if "{{" in prompt or "}}" in prompt:
                raise PreservationError(
                    "Unresolved prompt placeholders; attempt reserved."
                )
            (run / "inputs/prompt.txt").write_text(
                prompt, encoding="utf-8", newline="\n"
            )
            data["prompt"] = {
                "path": "inputs/prompt.txt",
                "sha256": digest(run / "inputs/prompt.txt"),
                "templateSHA256": template_copy["sha256"],
            }
            data["state"] = "prepared"
        except (OSError, ValueError, KeyError) as error:
            data["state"] = "preparation-failed"
            data["preparationFailure"] = {"recordedAt": now(), "diagnostic": str(error)}
            write_json(run / "run.json", data)
            raise PreservationError(
                f"Preparation failed; preserve {run}: {error}"
            ) from error
        write_json(run / "run.json", data)
    return run


@locked
def recover(run, reason):
    if (
        not reason.strip()
        or not run.is_dir()
        or (run / "run.json").exists()
        or (run / "seal.json").exists()
    ):
        raise PreservationError(
            "Recovery requires an existing manifestless reservation and a reason."
        )
    if run.parent.name not in CONDITIONS or not run.name.isdigit():
        raise PreservationError("Recover only a reserved source-condition directory.")
    existing = inventory(run)
    data = {
        "schemaVersion": 2,
        "recordKind": "generation",
        "runId": f"{run.parent.name}-{run.name}",
        "condition": run.parent.name,
        "sequence": run.name,
        "state": "preparation-failed",
        "origin": "reservation-recovery",
        "createdAt": None,
        "recoveredAt": now(),
        "recoveryReason": reason,
        "preservedInputs": existing,
        "frozenTest": None,
        "executions": [],
    }
    write_json(run / "run.json", data, exclusive=True)
    return verify(run)


@locked
def freeze(run, *, fresh_chat_attested=False):
    run, data = writable_run(run)
    verify(run)
    if data["state"] != "prepared" or data.get("frozenTest"):
        raise PreservationError("Only a prepared, unfrozen generation can be frozen.")
    if not fresh_chat_attested:
        raise PreservationError(
            "The generator must attest to a fresh, uncontaminated chat."
        )
    check_sources(data)
    source = require_d(data["checkout"]) / TEST_PATH
    expected = digest(source)
    check_checkout(data["checkout"], data["baselineCommit"], frozen_hash=expected)
    data["frozenTest"] = snapshot(run, source, FROZEN_PATH)
    data["frozenTest"]["frozenAt"] = now()
    data["state"] = "frozen"
    data["isolation"]["freshChat"] = True
    write_json(run / "run.json", data)
    return data["frozenTest"]


def assigned_path(run, data, path):
    path = require_d(path)
    roots = [run] + [
        require_d(data[k]) for k in ("checkout", "workingDirectory") if data.get(k)
    ]
    if not any(path.is_relative_to(root) for root in roots):
        raise PreservationError("Evidence must come from this record's assigned paths.")
    return path


@locked
def begin(
    run, phase, command, environment, *, reports=None, scope=None, artifacts=None
):
    run, data = writable_run(run)
    verify(run)
    if data.get("schemaVersion") != 2 or data.get("recordKind") == "annotation":
        raise PreservationError(
            "Use an evaluation supplement for historical or annotated records."
        )
    if phase not in PHASES or not command.strip() or not scope or not scope.strip():
        raise PreservationError(
            "Provide a supported phase, exact command, and explicit scope."
        )
    if phase not in ("preflight", "infrastructure") and not data.get("frozenTest"):
        raise PreservationError("Freeze the suite before execution.")
    if phase in MEASUREMENTS and data.get("recordKind") != "evaluation":
        raise PreservationError(
            "Measurements require a separately authorized evaluation supplement."
        )
    if any(not item.get("resultSHA256") for item in data["executions"]):
        raise PreservationError("Finish the pending execution before starting another.")
    prior_phases = [
        read_json(run / item["path"] / "request.json")["phase"]
        for item in data["executions"]
    ]
    if phase == "generated-tests" and (
        data.get("recordKind") != "generation" or phase in prior_phases
    ):
        raise PreservationError(
            "A generation has one initial invocation; use supplemental-tests for an authorized retry."
        )
    if phase in MEASUREMENTS and phase in prior_phases:
        raise PreservationError(
            "Reserve a new linked evaluation for a measurement retry."
        )
    problems = []
    try:
        live_check(data)
    except (PreservationError, OSError) as error:
        if phase != "infrastructure":
            raise
        problems.append(str(error))
    env = observed_environment(environment)
    if phase in MEASUREMENTS:
        plan = read_json(inside(run, data["measurementPlan"]["path"]))
        for observed, pinned in (
            ("java", "javaRuntime"),
            ("javac", "javac"),
            ("maven", "maven"),
        ):
            if plan[pinned] not in str(env[observed]):
                raise PreservationError(
                    f"Observed {observed} does not match the frozen measurement plan."
                )
    report_path = assigned_path(run, data, reports) if reports else None
    if (
        report_path
        and report_path.exists()
        and (not report_path.is_dir() or any(report_path.iterdir()))
    ):
        raise PreservationError(
            "Native report destination must be empty before execution; archive prior output first."
        )
    artifact_paths = {
        role: assigned_path(run, data, path).as_posix()
        for role, path in (artifacts or {}).items()
    }
    for role, path in artifact_paths.items():
        if role != "production-class" and Path(path).exists():
            raise PreservationError(
                "Measurement output destinations must not already exist."
            )
    execution = next_directory(run / "executions")
    environment_copy = snapshot(execution, environment, "environment.json")
    request = {
        "phase": phase,
        "command": command,
        "scope": scope,
        "reservedAt": now(),
        # Compare filesystem timestamps with the same clock used by native output.
        # Windows wall-clock nanoseconds can be ahead of its file timestamp clock.
        "reservedAtNs": (execution / "environment.json").stat().st_mtime_ns,
        "reportsDirectory": report_path.as_posix() if report_path else None,
        "artifacts": artifact_paths,
        "environment": environment_copy,
        "checkout": data.get("checkout"),
        "initialProblems": problems,
        "planSHA256": data.get("measurementPlan", {}).get("sha256"),
        "observedJava": env["java"],
        "observedMaven": env["maven"],
    }
    write_json(execution / "request.json", request, exclusive=True)
    data["executions"].append(
        {
            "path": execution.relative_to(run).as_posix(),
            "requestSHA256": digest(execution / "request.json"),
            "resultSHA256": None,
        }
    )
    write_json(run / "run.json", data)
    return {
        "execution": execution.name,
        "log": str(execution / "output.log"),
        "reportsDirectory": request["reportsDirectory"],
        "reservedAt": request["reservedAt"],
    }


def xml_counts(content):
    root = ET.fromstring(content)
    if root.tag != "testsuite":
        raise PreservationError("Expected a native Surefire testsuite document.")
    counts = {
        key: int(root.attrib[key]) for key in ("tests", "failures", "errors", "skipped")
    }
    if (
        min(counts.values()) < 0
        or sum(counts[k] for k in ("failures", "errors", "skipped")) > counts["tests"]
    ):
        raise PreservationError("Invalid native Surefire counts.")
    return counts


@locked
def record(run, execution, exit_code, *, tests_not_started=False, reason=None):
    run, data = writable_run(run)
    verify(run)
    relative = "executions/" + str(execution)
    entries = [item for item in data["executions"] if item["path"] == relative]
    if len(entries) != 1 or entries[0].get("resultSHA256"):
        raise PreservationError("Select an unfinished reserved execution.")
    entry = entries[0]
    directory = inside(run, relative)
    request = read_json(directory / "request.json")
    log = directory / "output.log"
    if not log.is_file():
        raise PreservationError(
            "Capture stdout and stderr in the reserved output.log first."
        )
    if tests_not_started and not reason:
        raise PreservationError(
            "Explain the log evidence establishing that tests did not start."
        )
    problems = list(request["initialProblems"])
    try:
        live_check(data)
    except (PreservationError, OSError) as error:
        problems.append(str(error))
    reports = []
    if request["reportsDirectory"]:
        report_directory = assigned_path(run, data, request["reportsDirectory"])
        reports = sorted(report_directory.glob("TEST-*.xml"))
    counts, native = None, []
    if reports:
        counts = dict.fromkeys(("tests", "failures", "errors", "skipped"), 0)
        with ZipFile(
            directory / "surefire-reports.zip", "x", compression=ZIP_DEFLATED
        ) as archive:
            for path in reports:
                assigned_path(run, data, path)
                content = path.read_bytes()
                archive.writestr(path.name, content)
                native.append(
                    {
                        "name": path.name,
                        "source": path.as_posix(),
                        "sha256": sha256(content).hexdigest(),
                    }
                )
                if path.stat().st_mtime_ns < request["reservedAtNs"]:
                    problems.append(
                        f"Native report predates this execution: {path.name}"
                    )
                try:
                    values = xml_counts(content)
                    for key in counts:
                        counts[key] += values[key]
                except (ValueError, KeyError, ET.ParseError) as error:
                    problems.append(f"Unreadable native report {path.name}: {error}")
        if tests_not_started:
            problems.append(
                "Native reports conflict with the tests-not-started observation."
            )
    elif tests_not_started:
        counts = dict.fromkeys(("tests", "failures", "errors", "skipped"), 0)
    artifacts = {}
    for role, original in request["artifacts"].items():
        source = assigned_path(run, data, original)
        if not source.is_file():
            problems.append(f"Missing declared artifact: {role}")
            continue
        if (
            role != "production-class"
            and source.stat().st_mtime_ns < request["reservedAtNs"]
        ):
            problems.append(f"Artifact predates this execution: {role}")
        artifacts[role] = snapshot(
            directory, source, f"artifacts/{len(artifacts):03d}-{source.name}"
        )
    outcome = (
        "not_started"
        if tests_not_started
        else "failed"
        if counts and (counts["failures"] or counts["errors"])
        else "passed"
        if counts and counts["tests"] > counts["skipped"]
        else "not_executed"
        if counts
        else "unknown"
    )
    if problems:
        # Preserve raw observations while refusing to attribute invalid evidence to this invocation.
        attributed_counts, outcome = None, "unknown"
    else:
        attributed_counts = counts
    result = {
        "phase": request["phase"],
        "recordedAt": now(),
        "exitCode": exit_code,
        "suiteCounts": attributed_counts,
        "nativeCounts": counts,
        "suiteOutcome": outcome,
        "testsNotStarted": tests_not_started,
        "observationReason": reason,
        "protocolProblems": problems,
        "nativeReports": native,
        "artifacts": artifacts,
        "logSHA256": digest(log),
        "requestSHA256": entry["requestSHA256"],
        "files": inventory(directory),
    }
    write_json(directory / "result.json", result, exclusive=True)
    entry["resultSHA256"] = digest(directory / "result.json")
    write_json(run / "run.json", data)
    return result


def verify_executions(run, data):
    expected = {item["path"] for item in data.get("executions", [])}
    actual = (
        {p.relative_to(run).as_posix() for p in (run / "executions").iterdir()}
        if (run / "executions").exists()
        else set()
    )
    if actual != expected:
        raise PreservationError(
            "Unregistered or missing execution evidence; preserve and recover explicitly."
        )
    for item in data.get("executions", []):
        directory = inside(run, item["path"])
        if digest(directory / "request.json") != item["requestSHA256"]:
            raise PreservationError("An execution request changed.")
        request = read_json(directory / "request.json")
        env = request["environment"]
        if digest(inside(directory, env["path"])) != env["sha256"]:
            raise PreservationError("An execution environment changed.")
        if not item.get("resultSHA256"):
            if (directory / "result.json").exists():
                raise PreservationError(
                    "A result exists without its receipt; inspect interrupted recording."
                )
            continue
        if digest(directory / "result.json") != item["resultSHA256"]:
            raise PreservationError("An execution receipt changed.")
        result = read_json(directory / "result.json")
        files = [f for f in inventory(directory) if f["path"] != "result.json"]
        if (
            files != result["files"]
            or digest(directory / "output.log") != result["logSHA256"]
        ):
            raise PreservationError(
                "Recorded execution evidence changed, disappeared, or gained files."
            )


def verify(run, *, live=False):
    run, data = load_run(run)
    for key in (
        "prompt",
        "environment",
        "frozenTest",
        "measurementPlan",
        "authorization",
    ):
        value = data.get(key)
        if value and digest(inside(run, value["path"])) != value["sha256"]:
            raise PreservationError(f"The recorded {key} changed.")
    for value in data.get("preservedInputs", []):
        if digest(inside(run, value["path"])) != value["sha256"]:
            raise PreservationError(f"A preserved input changed: {value['path']}")
    if data.get("schemaVersion") == 2:
        verify_executions(run, data)
    if data.get("parent"):
        parent = inside(run.parents[3], data["parent"]["path"])
        verify(parent)
        if digest(parent / "seal.json") != data["parent"]["sealSHA256"]:
            raise PreservationError("The supplement's preserved parent seal differs.")
    if (run / "seal.json").exists():
        seal_data = read_json(run / "seal.json")
        if seal_data["runId"] != data["runId"] or inventory(run) != seal_data["files"]:
            raise PreservationError(
                "Sealed evidence changed, disappeared, or gained files."
            )
    if live:
        live_check(data)
    return {
        "runId": data["runId"],
        "sealed": (run / "seal.json").exists(),
        "state": data.get("state"),
        "files": len(inventory(run)),
    }


def completed_executions(run, data):
    if any(not item.get("resultSHA256") for item in data.get("executions", [])):
        raise PreservationError("Finish pending executions before claiming completion.")
    return [
        (
            read_json(run / item["path"] / "request.json"),
            read_json(run / item["path"] / "result.json"),
        )
        for item in data.get("executions", [])
    ]


def check_generation_completion(run, data):
    if data.get("recordKind") != "generation" or not data.get("frozenTest"):
        raise PreservationError("Generation completion requires a frozen generation.")
    executions = completed_executions(run, data)
    initial = [
        result
        for request, result in executions
        if request["phase"] == "generated-tests"
    ]
    if len(initial) != 1 or any(result["protocolProblems"] for _, result in executions):
        raise PreservationError(
            "Completion requires one initial execution and valid preserved evidence."
        )
    if initial[0]["suiteOutcome"] == "unknown":
        raise PreservationError(
            "Unknown initial execution evidence requires an incomplete outcome."
        )
    live_check(data)


def check_evaluation_completion(run, data):
    if data.get("recordKind") != "evaluation":
        raise PreservationError(
            "Evaluation completion requires an evaluation supplement."
        )
    live_check(data)
    executions = completed_executions(run, data)
    selected = {}
    for request, result in executions:
        if request["phase"] in MEASUREMENTS:
            if request["phase"] in selected:
                raise PreservationError(
                    "A measurement retry requires a new linked evaluation, preserving the incomplete pair."
                )
            selected[request["phase"]] = result
        if result["protocolProblems"]:
            raise PreservationError(
                "Evaluation evidence has unresolved protocol problems."
            )
    if set(selected) != set(MEASUREMENTS) or any(
        r["exitCode"] != 0 for r in selected.values()
    ):
        raise PreservationError(
            "Complete evaluation requires four successful measurement phases."
        )
    classes, mutant_sets = set(), []
    for phase, result in selected.items():
        required = (
            {"production-class", "jacoco-xml", "jacoco-exec"}
            if phase.startswith("jacoco")
            else {"production-class", "pit-mutations", "pit-linecoverage"}
        )
        if not required.issubset(result["artifacts"]):
            raise PreservationError(
                f"Missing native measurement artifacts for {phase}."
            )
        classes.add(result["artifacts"]["production-class"]["sha256"])
        entry = next(
            item
            for item in data["executions"]
            if read_json(run / item["path"] / "result.json")["phase"] == phase
        )
        base = run / entry["path"]
        if phase.startswith("jacoco"):
            if result["suiteOutcome"] != "passed":
                raise PreservationError(
                    "JaCoCo requires an executed, passing baseline or augmented suite."
                )
            root = ET.parse(base / result["artifacts"]["jacoco-xml"]["path"]).getroot()
            target = read_json(inside(run, data["measurementPlan"]["path"]))[
                "targetClass"
            ].replace(".", "/")
            classes_in_report = root.findall(".//class")
            target_classes = [
                node for node in classes_in_report if node.attrib.get("name") == target
            ]
            if root.tag != "report" or len(target_classes) != 1:
                raise PreservationError("JaCoCo native class counters are required.")
            counters = {
                node.attrib.get("type"): node.attrib
                for node in target_classes[0].findall("counter")
            }
            if not {"INSTRUCTION", "BRANCH", "LINE", "METHOD", "CLASS"}.issubset(
                counters
            ):
                raise PreservationError("JaCoCo native target counters are incomplete.")
            for counter in counters.values():
                if min(int(counter["missed"]), int(counter["covered"])) < 0:
                    raise PreservationError("JaCoCo counters must be nonnegative.")
        else:
            coverage = ET.parse(
                base / result["artifacts"]["pit-linecoverage"]["path"]
            ).getroot()
            if coverage.tag != "coverage":
                raise PreservationError("PIT native line coverage is required.")
            root = ET.parse(
                base / result["artifacts"]["pit-mutations"]["path"]
            ).getroot()
            mutations = root.findall("mutation")
            if root.tag != "mutations" or not mutations:
                raise PreservationError("PIT native mutants are required.")
            if any(
                m.attrib.get("status") not in {"KILLED", "SURVIVED", "NO_COVERAGE"}
                for m in mutations
            ):
                raise PreservationError(
                    "PIT contains incomplete or exceptional mutation outcomes."
                )
            identities = set()
            for mutation in mutations:
                indexes = mutation.find("indexes")
                blocks = mutation.find("blocks")
                if indexes is None or blocks is None:
                    raise PreservationError(
                        "PIT mutant identity requires indexes and blocks metadata."
                    )
                identity = tuple(
                    mutation.findtext(key)
                    for key in (
                        "mutatedClass",
                        "mutatedMethod",
                        "methodDescription",
                        "lineNumber",
                        "mutator",
                    )
                ) + (ET.tostring(indexes), ET.tostring(blocks))
                identities.add(identity)
            if len(identities) != len(mutations):
                raise PreservationError(
                    "Duplicate PIT mutant identities cannot establish a comparable pair."
                )
            mutant_sets.append(identities)
    if len(classes) != 1 or mutant_sets[0] != mutant_sets[1]:
        raise PreservationError(
            "Before and after class bytes or mutant identities differ."
        )


@locked
def seal(run, report, *, outcome="generation-complete", reason=None):
    run, data = writable_run(run)
    verify(run)
    if outcome not in OUTCOMES:
        raise PreservationError(
            "Use an explicit generation, evaluation, or incomplete outcome."
        )
    report = inside(run, report)
    if not report.is_file() or report.suffix.lower() != ".md":
        raise PreservationError(
            "A Markdown report is required, including negative outcomes."
        )
    if outcome == "generation-complete":
        check_generation_completion(run, data)
    elif outcome == "evaluation-complete":
        check_evaluation_completion(run, data)
    elif not reason or not reason.strip():
        raise PreservationError(
            "An incomplete or annotation outcome requires a reason."
        )
    if outcome == "annotation" and data.get("recordKind") != "annotation":
        raise PreservationError(
            "Only an annotation supplement can use the annotation outcome."
        )
    if outcome == "preflight-failed" and data.get("state") not in (
        "preparing",
        "preparation-failed",
    ):
        raise PreservationError(
            "The preflight-failed outcome requires a failed preparation."
        )
    if outcome == "no-supported-tests":
        if (
            data.get("recordKind") != "generation"
            or data.get("frozenTest")
            or data.get("executions")
        ):
            raise PreservationError(
                "No-supported-tests cannot replace an observed generation or execution."
            )
        live_check(data)
    if outcome in ("generation-complete", "evaluation-complete"):
        source = (
            inside(run, data["frozenTest"]["path"])
            .read_text(encoding="utf-8-sig")
            .strip()
        )
        if source not in report.read_text(encoding="utf-8-sig"):
            raise PreservationError(
                "The report must include the complete frozen Java source."
            )
    write_json(
        run / "seal.json",
        {
            "schemaVersion": 2,
            "runId": data["runId"],
            "sealedAt": now(),
            "outcome": outcome,
            "reason": reason,
            "evaluationStatus": "complete"
            if outcome == "evaluation-complete"
            else "not-established-in-this-record",
            "report": report.relative_to(run).as_posix(),
            "files": inventory(run),
        },
        exclusive=True,
    )
    return verify(run)


def supplement(
    study, parent, kind, note, *, checkout=None, environment=None, plan=None
):
    study, parent = require_d(study), require_d(parent)
    if kind not in ("annotation", "evaluation") or not verify(parent)["sealed"]:
        raise PreservationError("A supplement must reference a sealed generation.")
    _, original = load_run(parent)
    if (
        original.get("recordKind", "generation") != "generation"
        or parent != study / "runs" / original["condition"] / original["sequence"]
    ):
        raise PreservationError("Reference the original generation inside this study.")
    if kind == "evaluation":
        if (
            not original.get("frozenTest")
            or checkout is None
            or environment is None
            or plan is None
        ):
            raise PreservationError(
                "Evaluation requires frozen source, its own checkout, environment, plan, and authorization note."
            )
        checkout = check_checkout(checkout, original["baselineCommit"], absent=True)
        observed_environment(environment)
        selected_plan = read_json(plan)
        if selected_plan != read_json(REPOSITORY / "docs/measurement-plan.json"):
            raise PreservationError(
                "Use the versioned canonical measurement plan; review configuration changes separately."
            )
    with lock(study / ".preparation.lock"):
        if checkout:
            for item in list((study / "runs").glob("*/*/run.json")) + list(
                (study / "supplements").glob("*/*/*/run.json")
            ):
                if (
                    read_json(item).get("checkout")
                    and require_d(read_json(item)["checkout"]) == checkout
                ):
                    raise PreservationError(
                        "A checkout cannot be assigned to two records."
                    )
        run = next_directory(
            study / "supplements" / original["condition"] / original["sequence"]
        )
        data = {
            "schemaVersion": 2,
            "recordKind": kind,
            "runId": f"{original['runId']}/{kind}-{run.name}",
            "condition": original["condition"],
            "sequence": original["sequence"],
            "state": "preparing",
            "origin": "supplement",
            "createdAt": now(),
            "sampleContribution": 0,
            "baselineCommit": original["baselineCommit"],
            "parent": {
                "path": parent.relative_to(study).as_posix(),
                "sealSHA256": digest(parent / "seal.json"),
            },
            "preservedInputs": [],
            "frozenTest": None,
            "executions": [],
        }
        write_json(run / "run.json", data, exclusive=True)
        try:
            data["authorization"] = snapshot(run, note, "inputs/note.md")
            if kind == "evaluation":
                if checkout is None:
                    raise PreservationError("Evaluation checkout is required.")
                data["checkout"] = checkout.as_posix()
                working = (
                    checkout.parent
                    / ".working"
                    / f"{original['runId']}-evaluation-{run.name}"
                )
                working.mkdir(parents=True, exist_ok=False)
                data["workingDirectory"] = working.as_posix()
                data["environment"] = snapshot(
                    run, environment, "inputs/environment.json"
                )
                data["measurementPlan"] = snapshot(
                    run, plan, "inputs/measurement-plan.json"
                )
                data["preservedInputs"].append(
                    snapshot(run, Path(__file__), "inputs/preservation-manager.py")
                )
                data["preservedInputs"].append(
                    snapshot(
                        run,
                        REPOSITORY / "docs/measurement-protocol.md",
                        "inputs/measurement-protocol.md",
                    )
                )
                data["preservedInputs"].append(
                    snapshot(
                        run,
                        REPOSITORY / "docs/pit-analysis-pom.xml",
                        "inputs/pit-analysis-pom.xml",
                    )
                )
                if selected_plan.get("configurationRevision", 1) >= 4:
                    data["preservedInputs"].append(
                        snapshot(
                            run,
                            REPOSITORY / "docs/pit-cli-pom.xml",
                            "inputs/pit-cli-pom.xml",
                        )
                    )
                data["frozenTest"] = snapshot(
                    run, parent / original["frozenTest"]["path"], FROZEN_PATH
                )
                target = checkout / TEST_PATH
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open("xb") as output:
                    output.write((run / FROZEN_PATH).read_bytes())
                data["state"] = "frozen"
            else:
                snapshot(run, note, "report.md")
                data["state"] = "annotation"
        except (OSError, ValueError, KeyError) as error:
            data["state"] = "preparation-failed"
            data["preparationFailure"] = {"recordedAt": now(), "diagnostic": str(error)}
            write_json(run / "run.json", data)
            raise PreservationError(
                f"Supplement preparation failed; preserve {run}: {error}"
            ) from error
        write_json(run / "run.json", data)
    if kind == "annotation":
        seal(
            run,
            "report.md",
            outcome="annotation",
            reason="Preserved linked annotation; see inputs/note.md.",
        )
    return run


def archive_files(files, destination):
    destination = require_d(destination)
    if destination.is_relative_to(REPOSITORY):
        raise PreservationError("Keep backup copies outside the study repository.")
    checksum = destination.with_suffix(destination.suffix + ".sha256")
    if destination.exists() or checksum.exists():
        raise PreservationError("Backup destinations are write-once.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(
        destination, "x", compression=ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name, path in sorted(files.items()):
            archive.write(path, name)
    with ZipFile(destination) as archive:
        if set(archive.namelist()) != set(files) or archive.testzip() is not None:
            raise PreservationError("Backup inventory verification failed.")
        for name, path in files.items():
            if sha256(archive.read(name)).hexdigest() != digest(path):
                raise PreservationError("Backup byte verification failed.")
    return destination, checksum


def finish_backup(destination, checksum):
    value = digest(destination)
    with checksum.open("x", encoding="utf-8", newline="\n") as output:
        output.write(f"{value}  {destination.name}\n")
    return {"backup": str(destination), "sha256": value, "verified": True}


def bundle(run, destination):
    run = require_d(run)
    if not verify(run)["sealed"]:
        raise PreservationError("Seal and verify before backing up.")
    files = {p.relative_to(run).as_posix(): p for p in run.rglob("*") if p.is_file()}
    destination, checksum = archive_files(files, destination)
    verify(run)
    return finish_backup(destination, checksum)


def record_directories(study):
    return sorted(
        [
            p
            for pattern in ("runs/*/*", "supplements/*/*/*")
            for p in Path(study).glob(pattern)
            if p.is_dir()
        ]
    )


def list_runs(study):
    return [
        verify(path)
        if (path / "run.json").exists()
        else {
            "runId": path.relative_to(study).as_posix(),
            "sealed": False,
            "state": "incomplete-reservation",
            "diagnostic": "Use recover with an explicit reason before closing.",
        }
        for path in record_directories(study)
    ]


def bundle_study(study, destination):
    study = require_d(study)
    with lock(study / ".preparation.lock"):
        records = record_directories(study)
        if not records or any(not verify(path)["sealed"] for path in records):
            raise PreservationError(
                "Seal every generation and supplement before the collection backup."
            )
        files = {
            p.relative_to(study).as_posix(): p
            for record_dir in records
            for p in record_dir.rglob("*")
            if p.is_file()
        }
        destination, checksum = archive_files(files, destination)
        for record_dir in records:
            verify(record_dir)
        return finish_backup(destination, checksum)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study-root", type=Path, default=DEFAULT_STUDY)
    sub = parser.add_subparsers(dest="operation", required=True)
    init = sub.add_parser("init")
    init.add_argument("--condition", choices=CONDITIONS, required=True)
    init.add_argument("--checkout", type=Path, required=True)
    init.add_argument("--prompt-template", type=Path, required=True)
    init.add_argument("--environment", type=Path, required=True)
    for name in (
        "freeze",
        "begin",
        "record",
        "seal",
        "verify",
        "bundle",
        "recover",
        "supplement",
    ):
        command = sub.add_parser(name)
        command.add_argument("--run", type=Path, required=True)
        if name == "freeze":
            command.add_argument("--fresh-chat-attested", action="store_true")
        elif name == "begin":
            command.add_argument("--phase", choices=PHASES, required=True)
            command.add_argument("--command", required=True)
            command.add_argument("--environment", type=Path, required=True)
            command.add_argument("--reports", type=Path)
            command.add_argument("--scope", required=True)
            command.add_argument(
                "--artifacts",
                type=Path,
                help="JSON object mapping artifact roles to paths",
            )
        elif name == "record":
            command.add_argument("--execution", required=True)
            command.add_argument("--exit-code", type=int, required=True)
            command.add_argument("--tests-not-started", action="store_true")
            command.add_argument("--reason")
        elif name == "seal":
            command.add_argument("--report", required=True)
            command.add_argument("--outcome", choices=OUTCOMES, required=True)
            command.add_argument("--reason")
        elif name == "verify":
            command.add_argument("--live", action="store_true")
        elif name == "bundle":
            command.add_argument("--destination", type=Path, required=True)
        elif name == "recover":
            command.add_argument("--reason", required=True)
        elif name == "supplement":
            command.add_argument(
                "--kind", choices=("annotation", "evaluation"), required=True
            )
            command.add_argument("--note", type=Path, required=True)
            command.add_argument("--checkout", type=Path)
            command.add_argument("--environment", type=Path)
            command.add_argument("--plan", type=Path)
    sub.add_parser("list")
    collection = sub.add_parser("bundle-study")
    collection.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.operation == "init":
            result = initialize(
                args.study_root,
                args.condition,
                args.checkout,
                args.prompt_template,
                args.environment,
            )
        elif args.operation == "freeze":
            result = freeze(args.run, fresh_chat_attested=args.fresh_chat_attested)
        elif args.operation == "begin":
            result = begin(
                args.run,
                args.phase,
                args.command,
                args.environment,
                reports=args.reports,
                scope=args.scope,
                artifacts=read_json(args.artifacts) if args.artifacts else None,
            )
        elif args.operation == "record":
            result = record(
                args.run,
                args.execution,
                args.exit_code,
                tests_not_started=args.tests_not_started,
                reason=args.reason,
            )
        elif args.operation == "seal":
            result = seal(
                args.run, args.report, outcome=args.outcome, reason=args.reason
            )
        elif args.operation == "verify":
            result = verify(args.run, live=args.live)
        elif args.operation == "bundle":
            result = bundle(args.run, args.destination)
        elif args.operation == "bundle-study":
            result = bundle_study(args.study_root, args.destination)
        elif args.operation == "recover":
            result = recover(args.run, args.reason)
        elif args.operation == "supplement":
            result = supplement(
                args.study_root,
                args.run,
                args.kind,
                args.note,
                checkout=args.checkout,
                environment=args.environment,
                plan=args.plan,
            )
        else:
            result = list_runs(args.study_root)
        print(json.dumps(result, indent=2, default=str))
    except (OSError, ValueError, KeyError, TypeError, ET.ParseError) as error:
        parser.exit(1, f"Preservation failed: {error}\n")


if __name__ == "__main__":
    main()
