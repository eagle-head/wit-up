"""Behavioral preservation checks using synthetic inputs and isolated D: Git fixtures."""

import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools/experiment_runs.py"
SPEC = importlib.util.spec_from_file_location("experiment_runs", MODULE_PATH)
runs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runs)
SOURCE = b"// Synthetic byte preservation fixture; not a Commons IO test.\n"
PASSING_XML = '<testsuite tests="2" failures="0" errors="0" skipped="0"/>'


class ExperimentPreservationChecks(unittest.TestCase):
    def setUp(self):
        parent = Path("D:/Projects/experiment-test-storage").resolve()
        parent.mkdir(exist_ok=True)
        storage = tempfile.TemporaryDirectory(prefix="preservation-", dir=parent)
        self.root = Path(storage.name).resolve()
        self.assertTrue(self.root.is_relative_to(parent))
        self.addCleanup(storage.cleanup)
        self.study = self.root / "study"
        self.checkout = self.root / "checkout"
        self.checkout.mkdir()
        self.git(self.checkout, "init", "--initial-branch=main")
        self.git(self.checkout, "config", "core.autocrlf", "false")
        (self.checkout / "README.md").write_text("Synthetic baseline.\n")
        (self.checkout / ".gitignore").write_text("/target/\n")
        production = self.checkout / "src/main/java/Fixture.java"
        production.parent.mkdir(parents=True)
        production.write_bytes(b"// Synthetic production snapshot.\n")
        self.git(self.checkout, "add", ".")
        self.git(
            self.checkout,
            "-c",
            "user.name=Fixture Maintainer",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-m",
            "test: establish preservation fixture",
        )
        self.commit = self.git(self.checkout, "rev-parse", "HEAD").strip()
        self.template = self.root / "prompt.txt"
        self.template.write_text(
            "Synthetic input {{CHECKOUT}} {{RUN_ROOT}} {{PROCESS_ROOT}}\n"
            "Source kind: WIT-UP JSON exports only.\n"
            "{{SOURCE_RESULTS}} {{SOURCE_SUMMARIES}}\n"
        )
        sources = []
        for role in ("results", "summaries"):
            source, backup = (
                self.root / f"{role}.json",
                self.root / f"{role}-backup.json",
            )
            source.write_text('{"synthetic": true}\n')
            shutil.copyfile(source, backup)
            sources.append(
                {
                    "role": role,
                    "path": str(source),
                    "backup": str(backup),
                    "sha256": runs.digest(source),
                }
            )
        self.environment = self.root / "environment.json"
        self.environment.write_text(
            json.dumps(
                {
                    "java": "Synthetic observation: 1.8.0_504-b01",
                    "javac": "Synthetic observation: 1.8.0_504",
                    "maven": "Synthetic observation: 3.9.16",
                    "os": "synthetic-os",
                    "processEnvironment": {"purpose": "fixture"},
                    "sourceInputs": sources,
                }
            )
        )

    def git(self, checkout, *arguments):
        return subprocess.run(
            ["git", "-C", str(checkout), *arguments],
            check=True,
            capture_output=True,
            text=True,
        ).stdout

    def prepare(self):
        return runs.initialize(
            self.study,
            "json",
            self.checkout,
            self.template,
            self.environment,
            commit=self.commit,
        )

    def frozen(self):
        run = self.prepare()
        target = self.checkout / runs.TEST_PATH
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(SOURCE)
        runs.freeze(run, fresh_chat_attested=True)
        return run

    def start(self, run, phase="generated-tests", *, reports=None, artifacts=None):
        return runs.begin(
            run,
            phase,
            "synthetic invocation",
            self.environment,
            scope="Synthetic preservation fixture only",
            reports=reports,
            artifacts=artifacts,
        )

    def finish(self, run, started, *, code=0, xml=PASSING_XML, not_started=False):
        Path(started["log"]).write_text("Synthetic process output.\n")
        if xml is not None and started["reportsDirectory"]:
            directory = Path(started["reportsDirectory"])
            directory.mkdir(parents=True, exist_ok=True)
            (directory / "TEST-fixture.xml").write_text(xml)
        return runs.record(
            run,
            started["execution"],
            code,
            tests_not_started=not_started,
            reason="Synthetic startup diagnostic establishes no test execution."
            if not_started
            else None,
        )

    def report(self, run):
        (run / "report.md").write_text(
            "# Synthetic preservation report\n\n```java\n" + SOURCE.decode() + "```\n"
        )

    def sealed(self):
        run = self.frozen()
        working = Path(runs.read_json(run / "run.json")["workingDirectory"])
        started = self.start(run, reports=working / "reports")
        self.finish(run, started)
        self.report(run)
        runs.seal(run, "report.md", outcome="generation-complete")
        return run

    def evaluation(self):
        parent = self.sealed()
        checkout = self.root / "evaluation-checkout"
        subprocess.run(
            ["git", "clone", "--no-hardlinks", str(self.checkout), str(checkout)],
            check=True,
            capture_output=True,
        )
        note = self.root / "authorization.md"
        note.write_text("# Synthetic authorization fixture\n")
        evaluation = runs.supplement(
            self.study,
            parent,
            "evaluation",
            note,
            checkout=checkout,
            environment=self.environment,
            plan=runs.REPOSITORY / "docs/measurement-plan.json",
        )
        return parent, evaluation

    def measurement_pair(
        self,
        evaluation,
        *,
        different_class=False,
        different_mutant=False,
        failed_phase=None,
    ):
        working = Path(runs.read_json(evaluation / "run.json")["workingDirectory"])
        target = "org.apache.commons.io.input.buffer.PeekableInputStream"
        for phase in runs.MEASUREMENTS:
            directory = working / phase
            directory.mkdir()
            artifacts = {"production-class": str(directory / "target.class")}
            is_coverage = phase.startswith("jacoco")
            if is_coverage:
                artifacts.update(
                    {
                        "jacoco-xml": str(directory / "jacoco.xml"),
                        "jacoco-exec": str(directory / "jacoco.exec"),
                    }
                )
            else:
                artifacts.update(
                    {
                        "pit-mutations": str(directory / "mutations.xml"),
                        "pit-linecoverage": str(directory / "linecoverage.xml"),
                    }
                )
            started = self.start(
                evaluation,
                phase,
                reports=directory / "reports" if is_coverage else None,
                artifacts=artifacts,
            )
            Path(artifacts["production-class"]).write_bytes(
                b"Different synthetic class bytes"
                if different_class and phase.endswith("after")
                else b"Synthetic class bytes"
            )
            if is_coverage:
                counters = "".join(
                    f'<counter type="{kind}" missed="0" covered="1"/>'
                    for kind in ("INSTRUCTION", "BRANCH", "LINE", "METHOD", "CLASS")
                )
                Path(artifacts["jacoco-xml"]).write_text(
                    f'<report><package name="fixture"><class name="{target.replace(".", "/")}">{counters}</class></package></report>'
                )
                Path(artifacts["jacoco-exec"]).write_bytes(b"Synthetic execution data")
            else:
                line = "2" if different_mutant and phase.endswith("after") else "1"
                Path(artifacts["pit-mutations"]).write_text(
                    '<mutations><mutation status="KILLED"><mutatedClass>'
                    + target
                    + "</mutatedClass>"
                    "<mutatedMethod>fixture</mutatedMethod><methodDescription>()V</methodDescription>"
                    f"<lineNumber>{line}</lineNumber><mutator>synthetic</mutator><indexes><index>0</index></indexes>"
                    "<blocks><block>0</block></blocks></mutation></mutations>"
                )
                Path(artifacts["pit-linecoverage"]).write_text("<coverage/>")
            self.finish(evaluation, started, code=1 if phase == failed_phase else 0)
            if phase == failed_phase:
                break
        self.report(evaluation)

    def givenDirtyCheckout_whenPreparing_thenFailureIsReservedAndCanBeSealed(self):
        # Arrange
        (self.checkout / "README.md").write_text("Changed synthetic baseline.\n")
        # Act
        with self.assertRaises(runs.PreservationError):
            self.prepare()
        run = self.study / "runs/json/001"
        self.report(run)
        runs.seal(
            run,
            "report.md",
            outcome="preflight-failed",
            reason="Tracked baseline differs.",
        )
        # Assert
        self.assertEqual(
            runs.read_json(run / "run.json")["state"], "preparation-failed"
        )
        self.assertTrue(runs.verify(run)["sealed"])

    def givenAssignedCheckout_whenPreparingAgain_thenReuseIsRejected(self):
        # Arrange
        self.prepare()
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "assigned"):
            self.prepare()

    def givenWrongSourceTag_whenPreparing_thenFailureRemainsVisible(self):
        # Arrange
        self.template.write_text("Source kind: Java production source only.\n")
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "source condition"):
            self.prepare()
        self.assertEqual(runs.list_runs(self.study)[0]["state"], "preparation-failed")

    def givenUnresolvedPlaceholder_whenPreparing_thenReservationCanBeClosed(self):
        # Arrange
        self.template.write_text(
            "Source kind: WIT-UP JSON exports only.\n{{UNKNOWN}}\n"
        )
        # Act
        with self.assertRaisesRegex(runs.PreservationError, "Unresolved"):
            self.prepare()
        run = self.study / "runs/json/001"
        self.report(run)
        runs.seal(
            run, "report.md", outcome="preflight-failed", reason="Unknown placeholder."
        )
        # Assert
        self.assertTrue(runs.verify(run)["sealed"])
        self.assertIn(
            "Unresolved",
            runs.read_json(run / "run.json")["preparationFailure"]["diagnostic"],
        )

    def givenManifestlessReservation_whenRecovering_thenBytesAndIdentifierAreRetained(
        self,
    ):
        # Arrange
        run = self.study / "runs/json/009"
        run.mkdir(parents=True)
        (run / "diagnostic.log").write_bytes(b"Partial preparation diagnostic.\n")
        # Act
        runs.recover(run, "Synthetic interrupted preparation.")
        self.report(run)
        runs.seal(
            run,
            "report.md",
            outcome="preflight-failed",
            reason="Interrupted preparation.",
        )
        new = self.prepare()
        # Assert
        self.assertEqual(new.name, "010")
        self.assertEqual(
            (run / "diagnostic.log").read_bytes(), b"Partial preparation diagnostic.\n"
        )
        self.assertTrue(runs.verify(run)["sealed"])

    def givenUnattestedChat_whenFreezing_thenAttestationIsRequired(self):
        # Arrange
        run = self.prepare()
        target = self.checkout / runs.TEST_PATH
        target.parent.mkdir(parents=True)
        target.write_bytes(SOURCE)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "fresh"):
            runs.freeze(run)
        runs.freeze(run, fresh_chat_attested=True)
        with self.assertRaisesRegex(runs.PreservationError, "unfrozen"):
            runs.freeze(run, fresh_chat_attested=True)

    def givenChangedExternalInput_whenFreezing_thenInputDriftIsRejected(self):
        # Arrange
        run = self.prepare()
        (self.root / "results.json").write_text('{"changed": true}\n')
        target = self.checkout / runs.TEST_PATH
        target.parent.mkdir(parents=True)
        target.write_bytes(SOURCE)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "scenario input changed"):
            runs.freeze(run, fresh_chat_attested=True)

    def givenChangedProcessSnapshot_whenVerifying_thenInstructionDriftIsRejected(self):
        # Arrange
        run = self.prepare()
        (run / "inputs/process/AGENTS.md").write_text("Changed process instructions.\n")
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "preserved input changed"):
            runs.verify(run)

    def givenJavaSourceCondition_whenPreparing_thenProductionBytesArePreserved(self):
        # Arrange
        self.template.write_text(
            "Source kind: Java production source only.\n{{CHECKOUT}}\n"
        )
        # Act
        run = runs.initialize(
            self.study,
            "java-source",
            self.checkout,
            self.template,
            self.environment,
            commit=self.commit,
        )
        # Assert
        with ZipFile(run / "inputs/production-source.zip") as archive:
            self.assertEqual(
                archive.read("src/main/java/Fixture.java"),
                b"// Synthetic production snapshot.\n",
            )
        self.assertFalse(runs.read_json(run / "run.json")["sourceInputs"])

    def givenPriorNativeReports_whenBeginningRetry_thenStaleDestinationIsRejected(self):
        # Arrange
        run = self.frozen()
        reports = Path(runs.read_json(run / "run.json")["workingDirectory"]) / "reports"
        started = self.start(run, reports=reports)
        self.finish(run, started)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "empty before execution"):
            self.start(run, "supplemental-tests", reports=reports)

    def givenPredatingXml_whenRecording_thenRawEvidenceIsPreservedWithoutAttribution(
        self,
    ):
        # Arrange
        run = self.frozen()
        reports = Path(runs.read_json(run / "run.json")["workingDirectory"]) / "reports"
        started = self.start(run, reports=reports)
        reports.mkdir()
        xml = reports / "TEST-fixture.xml"
        xml.write_text(PASSING_XML)
        timestamp = (
            runs.read_json(run / "executions/001/request.json")["reservedAtNs"]
            - 10_000_000_000
        )
        os.utime(xml, ns=(timestamp, timestamp))
        # Act
        result = self.finish(run, started, code=1, xml=None)
        # Assert
        self.assertEqual(result["suiteOutcome"], "unknown")
        self.assertIsNone(result["suiteCounts"])
        self.assertEqual(result["nativeCounts"]["tests"], 2)
        self.assertIn("predates", result["protocolProblems"][0])
        with ZipFile(run / "executions/001/surefire-reports.zip") as archive:
            self.assertEqual(archive.read(xml.name), xml.read_bytes())

    def givenStartupFailureThenRetry_whenRecording_thenOriginalFailureRemains(self):
        # Arrange
        run = self.frozen()
        first = self.start(run)
        # Act
        failed = self.finish(run, first, code=1, xml=None, not_started=True)
        working = Path(runs.read_json(run / "run.json")["workingDirectory"])
        retry = self.start(run, "supplemental-tests", reports=working / "retry-reports")
        passed = self.finish(run, retry)
        # Assert
        self.assertEqual(failed["suiteOutcome"], "not_started")
        self.assertEqual(passed["suiteOutcome"], "passed")
        self.assertEqual(
            runs.read_json(run / "executions/001/result.json")["exitCode"], 1
        )
        self.assertEqual(len(runs.read_json(run / "run.json")["executions"]), 2)

    def givenExecutedFailures_whenRecording_thenFailureCountsRemain(self):
        # Arrange
        run = self.frozen()
        working = Path(runs.read_json(run / "run.json")["workingDirectory"])
        started = self.start(run, reports=working / "reports")
        # Act
        result = self.finish(
            run,
            started,
            code=1,
            xml='<testsuite tests="2" failures="1" errors="0" skipped="0"/>',
        )
        # Assert
        self.assertEqual(result["suiteOutcome"], "failed")
        self.assertEqual(result["suiteCounts"]["failures"], 1)

    def givenMissingReports_whenRecording_thenCountsRemainUnknown(self):
        # Arrange
        run = self.frozen()
        started = self.start(run)
        # Act
        result = self.finish(run, started, xml=None)
        # Assert
        self.assertIsNone(result["suiteCounts"])
        self.assertEqual(result["suiteOutcome"], "unknown")

    def givenChangedCheckout_whenRecording_thenDiagnosticIsArchivedAndCompletionRejected(
        self,
    ):
        # Arrange
        run = self.frozen()
        started = self.start(run)
        (self.checkout / runs.TEST_PATH).write_bytes(b"Changed synthetic bytes.\n")
        # Act
        result = self.finish(run, started, code=1, xml=None, not_started=True)
        self.report(run)
        # Assert
        self.assertIn("frozen test", result["protocolProblems"][0])
        self.assertTrue((run / "executions/001/output.log").is_file())
        with self.assertRaises(runs.PreservationError):
            runs.seal(run, "report.md", outcome="generation-complete")
        runs.seal(
            run, "report.md", outcome="incomplete", reason="Checkout drift preserved."
        )
        self.assertTrue(runs.verify(run)["sealed"])

    def givenPreexistingCheckoutDrift_whenRecordingInfrastructure_thenDiagnosticRemains(
        self,
    ):
        # Arrange
        run = self.frozen()
        (self.checkout / runs.TEST_PATH).write_bytes(b"Changed synthetic bytes.\n")
        # Act
        started = self.start(run, "infrastructure")
        result = self.finish(run, started, code=1, xml=None, not_started=True)
        # Assert
        self.assertTrue(result["protocolProblems"])
        self.assertEqual(result["exitCode"], 1)
        self.assertTrue((run / "executions/001/output.log").exists())

    def givenRecordedLogTampering_whenVerifyingOrSealing_thenBothReject(self):
        # Arrange
        run = self.frozen()
        self.finish(run, self.start(run), code=1, xml=None, not_started=True)
        (run / "executions/001/output.log").write_text("Different diagnostic.\n")
        self.report(run)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "evidence changed"):
            runs.verify(run)
        with self.assertRaises(runs.PreservationError):
            runs.seal(
                run, "report.md", outcome="incomplete", reason="Changed evidence."
            )

    def givenRecordedArchiveTampering_whenVerifying_thenChangedBytesAreRejected(self):
        # Arrange
        run = self.frozen()
        working = Path(runs.read_json(run / "run.json")["workingDirectory"])
        self.finish(run, self.start(run, reports=working / "reports"))
        (run / "executions/001/surefire-reports.zip").write_bytes(
            b"Changed archive bytes"
        )
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "evidence changed"):
            runs.verify(run)

    def givenNoExecution_whenClaimingCompletion_thenClosureIsRejected(self):
        # Arrange
        run = self.frozen()
        self.report(run)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "one initial execution"):
            runs.seal(run, "report.md", outcome="generation-complete")

    def givenFinishedInitialInvocation_whenBeginningAnotherInitial_thenRetryPhaseIsRequired(
        self,
    ):
        # Arrange
        run = self.frozen()
        self.finish(run, self.start(run), code=1, xml=None, not_started=True)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "one initial invocation"):
            self.start(run)

    def givenFrozenSuite_whenClaimingNoSupportedTests_thenFalseOutcomeIsRejected(self):
        # Arrange
        run = self.frozen()
        self.report(run)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "cannot replace"):
            runs.seal(
                run,
                "report.md",
                outcome="no-supported-tests",
                reason="Synthetic contradictory outcome.",
            )

    def givenPendingExecution_whenClaimingCompletion_thenClosureIsRejected(self):
        # Arrange
        run = self.frozen()
        self.start(run)
        self.report(run)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "pending"):
            runs.seal(run, "report.md", outcome="generation-complete")
        runs.seal(
            run, "report.md", outcome="incomplete", reason="Execution was interrupted."
        )
        self.assertTrue(runs.verify(run)["sealed"])

    def givenCompletedGeneration_whenSealing_thenEvaluationRemainsUnestablished(self):
        # Arrange / Act
        run = self.sealed()
        # Assert
        seal = runs.read_json(run / "seal.json")
        self.assertEqual(seal["outcome"], "generation-complete")
        self.assertEqual(seal["evaluationStatus"], "not-established-in-this-record")

    def givenSealedGeneration_whenWritingOrAddingBytes_thenGuardsReject(self):
        # Arrange
        run = self.sealed()
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "sealed"):
            self.start(run)
        (run / "extra.txt").write_text("Unexpected artifact.\n")
        with self.assertRaisesRegex(runs.PreservationError, "Sealed evidence"):
            runs.verify(run)

    def givenEscapingPaths_whenCollectingOrSealing_thenPathsAreRejected(self):
        # Arrange
        run = self.frozen()
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "assigned paths"):
            self.start(run, reports=self.root / "foreign-reports")
        with self.assertRaisesRegex(runs.PreservationError, "inside"):
            runs.seal(
                run,
                "../report.md",
                outcome="incomplete",
                reason="Synthetic path check.",
            )

    def givenOwnedOperationLock_whenStartingAnotherOperation_thenConflictIsReported(
        self,
    ):
        # Arrange
        run = self.frozen()
        # Act / Assert
        with (
            runs.lock(run.parent / f".{run.name}.operation.lock"),
            self.assertRaisesRegex(runs.PreservationError, "owns the lock"),
        ):
            self.start(run)

    def givenGenerationRecord_whenStartingMeasurement_thenEvaluationIsRequired(self):
        # Arrange
        run = self.frozen()
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "evaluation supplement"):
            self.start(run, "jacoco-before")

    def givenEvaluationSupplement_whenPreparing_thenFrozenSourceAndPlanAreLinked(self):
        # Arrange / Act
        parent, evaluation = self.evaluation()
        data = runs.read_json(evaluation / "run.json")
        # Assert
        self.assertEqual(data["sampleContribution"], 0)
        self.assertEqual(
            data["parent"]["sealSHA256"], runs.digest(parent / "seal.json")
        )
        self.assertEqual((evaluation / runs.FROZEN_PATH).read_bytes(), SOURCE)
        self.assertEqual((Path(data["checkout"]) / runs.TEST_PATH).read_bytes(), SOURCE)
        self.assertEqual(
            data["measurementPlan"]["sha256"],
            runs.digest(runs.REPOSITORY / "docs/measurement-plan.json"),
        )
        self.report(evaluation)
        with self.assertRaisesRegex(runs.PreservationError, "four successful"):
            runs.seal(evaluation, "report.md", outcome="evaluation-complete")

    def givenChangedMeasurementPlan_whenPreparingEvaluation_thenConfigurationIsRejected(
        self,
    ):
        # Arrange
        parent = self.sealed()
        checkout = self.root / "evaluation"
        subprocess.run(
            ["git", "clone", str(self.checkout), str(checkout)],
            check=True,
            capture_output=True,
        )
        plan = self.root / "changed-plan.json"
        data = runs.read_json(runs.REPOSITORY / "docs/measurement-plan.json")
        data["threads"] = 8
        plan.write_text(json.dumps(data))
        note = self.root / "note.md"
        note.write_text("Synthetic approval note.\n")
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "canonical"):
            runs.supplement(
                self.study,
                parent,
                "evaluation",
                note,
                checkout=checkout,
                environment=self.environment,
                plan=plan,
            )

    def givenCompleteComparablePair_whenClosingEvaluation_thenNativeEvidenceIsRequiredAndAccepted(
        self,
    ):
        # Arrange
        _, evaluation = self.evaluation()
        self.measurement_pair(evaluation)
        # Act
        result = runs.seal(evaluation, "report.md", outcome="evaluation-complete")
        # Assert
        self.assertTrue(result["sealed"])
        self.assertEqual(
            runs.read_json(evaluation / "seal.json")["evaluationStatus"], "complete"
        )
        self.assertEqual(len(runs.read_json(evaluation / "run.json")["executions"]), 4)

    def givenDifferentProductionBytes_whenClosingEvaluation_thenComparisonIsRejected(
        self,
    ):
        # Arrange
        _, evaluation = self.evaluation()
        self.measurement_pair(evaluation, different_class=True)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "class bytes"):
            runs.seal(evaluation, "report.md", outcome="evaluation-complete")
        runs.seal(
            evaluation,
            "report.md",
            outcome="incomplete",
            reason="Production class mismatch retained.",
        )
        self.assertTrue(runs.verify(evaluation)["sealed"])

    def givenFailedMutationBaseline_whenClosingEvaluation_thenFailureRemainsIncomplete(
        self,
    ):
        # Arrange
        _, evaluation = self.evaluation()
        self.measurement_pair(evaluation, failed_phase="pit-before")
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "four successful"):
            runs.seal(evaluation, "report.md", outcome="evaluation-complete")
        runs.seal(
            evaluation,
            "report.md",
            outcome="incomplete",
            reason="Synthetic failed mutation baseline.",
        )
        result = runs.read_json(evaluation / "executions/003/result.json")
        self.assertEqual(result["exitCode"], 1)
        self.assertEqual(
            runs.read_json(evaluation / "run.json")["sampleContribution"], 0
        )

    def givenDifferentObservedRuntime_whenStartingMeasurement_thenPlanMismatchIsRejected(
        self,
    ):
        # Arrange
        _, evaluation = self.evaluation()
        environment = runs.read_json(self.environment)
        environment["java"] = "Synthetic different runtime"
        self.environment.write_text(json.dumps(environment))
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "frozen measurement plan"):
            self.start(evaluation, "jacoco-before")

    def givenAnnotation_whenBackingUpStudy_thenOriginalAndSupplementRestoreTogether(
        self,
    ):
        # Arrange
        parent = self.sealed()
        original_hash = runs.digest(parent / "seal.json")
        note = self.root / "note.md"
        note.write_text(
            "# Synthetic correction\n\nPreserved externally to the original.\n"
        )
        # Act
        annotation = runs.supplement(self.study, parent, "annotation", note)
        backup = self.root / "backups/collection.zip"
        result = runs.bundle_study(self.study, backup)
        restored = self.root / "restored-study"
        with ZipFile(backup) as archive:
            archive.extractall(restored)
        # Assert
        self.assertEqual(runs.digest(parent / "seal.json"), original_hash)
        self.assertEqual(
            runs.read_json(annotation / "run.json")["sampleContribution"], 0
        )
        self.assertTrue(result["verified"])
        self.assertEqual(len(runs.list_runs(restored)), 2)
        self.assertTrue(all(item["sealed"] for item in runs.list_runs(restored)))

    def givenDifferentMutantIdentities_whenClosingEvaluation_thenComparisonIsRejected(
        self,
    ):
        # Arrange
        _, evaluation = self.evaluation()
        self.measurement_pair(evaluation, different_mutant=True)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "mutant identities"):
            runs.seal(evaluation, "report.md", outcome="evaluation-complete")

    def givenUnsealedGeneration_whenBackingUpCollection_thenIncompleteCollectionIsRejected(
        self,
    ):
        # Arrange
        self.frozen()
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "Seal every"):
            runs.bundle_study(self.study, self.root / "backups/incomplete.zip")

    def givenExistingBackup_whenBundlingAgain_thenOverwriteIsRejected(self):
        # Arrange
        run = self.sealed()
        destination = self.root / "backups/run.zip"
        runs.bundle(run, destination)
        # Act / Assert
        with self.assertRaisesRegex(runs.PreservationError, "write-once"):
            runs.bundle(run, destination)
        self.assertEqual(
            runs.digest(destination),
            destination.with_suffix(".zip.sha256").read_text().split()[0],
        )

    def givenCrlfDefaults_whenCommittingAndCloning_thenSealedBytesSurvive(self):
        # Arrange
        run = self.sealed()
        (self.study / ".gitattributes").write_text(
            "* text=auto eol=crlf\nruns/** -text\nsupplements/** -text\n"
        )
        self.git(self.study, "init", "--initial-branch=main")
        self.git(self.study, "add", ".")
        # Act
        self.git(
            self.study,
            "-c",
            "user.name=Fixture Maintainer",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-m",
            "test: preserve sealed experiment bytes",
        )
        restored = self.root / "restored-study"
        subprocess.run(
            ["git", "clone", "--no-hardlinks", str(self.study), str(restored)],
            check=True,
            capture_output=True,
        )
        # Assert
        self.assertTrue(runs.verify(restored / "runs/json/001")["sealed"])
        self.assertEqual(
            runs.digest(run / "run.json"),
            runs.digest(restored / "runs/json/001/run.json"),
        )

    def givenRegisteredRun_whenUsingCli_thenVerificationReturnsItsIdentity(self):
        # Arrange
        run = self.sealed()
        # Act
        result = subprocess.run(
            [os.sys.executable, str(MODULE_PATH), "verify", "--run", str(run)],
            check=True,
            capture_output=True,
            text=True,
        )
        # Assert
        self.assertEqual(json.loads(result.stdout)["runId"], "json-001")


def load_tests(loader, suite, pattern):
    loader.testMethodPrefix = "given"
    return loader.loadTestsFromTestCase(ExperimentPreservationChecks)


if __name__ == "__main__":
    unittest.main()
