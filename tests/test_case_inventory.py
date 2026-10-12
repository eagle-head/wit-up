"""Behavioral checks for selection and bounded expression interpretation."""

import unittest

from witup_analysis.case_assessment import assess_case
from witup_analysis.selection import select_cases


def candidate(class_name: str, method: str, tier: str, index: int = 0) -> dict:
    parameters = "int" if tier == "simple_signature_hypothesis" else "java.io.File"
    return {
        "artifact": "example.jar",
        "package": "example",
        "class": class_name,
        "method": method,
        "params": parameters,
        "pathId": f"<example.{class_name}: void {method}({parameters})>#{index}",
        "exceptionType": "java.lang.IllegalArgumentException",
        "throwSiteKind": "DIRECT_ATHROW",
        "constraints": [],
        "modelValues": {},
        "tier": tier,
    }


class CaseInventoryChecks(unittest.TestCase):
    def givenReorderedPool_whenSelectingCases_thenSameDiverseMethodKeysAreReturned(
        self,
    ):
        # Arrange
        simple, null = "simple_signature_hypothesis", "null_argument_hypothesis"
        pool = [
            candidate("Alpha", "first", simple),
            candidate("Alpha", "first", simple, 1),
            candidate("Alpha", "second", simple),
            candidate("Beta", "first", simple),
            candidate("Gamma", "first", null),
            candidate("Delta", "first", null),
        ]
        # Act
        forward = select_cases(pool, 2)
        reverse = select_cases(list(reversed(pool)), 2)
        # Assert
        expected = [
            (item["candidate"]["artifact"], item["candidate"]["pathId"])
            for item in forward
        ]
        self.assertEqual(
            expected,
            [
                (item["candidate"]["artifact"], item["candidate"]["pathId"])
                for item in reverse
            ],
        )
        self.assertEqual(len(forward), 4)
        self.assertEqual(
            {item["candidate"]["class"] for item in forward},
            {"Alpha", "Beta", "Gamma", "Delta"},
        )
        self.assertEqual(
            len({item["candidate"]["pathId"].rsplit("#", 1)[0] for item in forward}), 4
        )

    def givenInsufficientDistinctMethods_whenSelectingCases_thenQuotaFailureIsReported(
        self,
    ):
        # Arrange
        simple, null = "simple_signature_hypothesis", "null_argument_hypothesis"
        pool = [
            candidate("Alpha", "first", simple),
            candidate("Alpha", "first", simple, 1),
            candidate("Gamma", "first", null),
            candidate("Delta", "first", null),
        ]
        # Act
        with self.assertRaises(ValueError) as raised:
            select_cases(pool, 2)
        # Assert
        self.assertIn("Insufficient distinct methods", str(raised.exception))

    def givenNegatedNullCondition_whenAssessingCase_thenTrueNullFlagAgrees(self):
        # Arrange
        summary = {
            "params": "java.io.File",
            "method": "check",
            "exceptionType": "java.lang.IllegalArgumentException",
            "throwSiteKind": "DIRECT_ATHROW",
            "constraints": [{"symExpr": "(file != null)", "truthValue": False}],
        }
        result = {
            "modelValues": {
                "file": "IntValue[value=0]",
                "file_is_null": "BoolValue[value=true]",
            }
        }
        # Act
        assessment = assess_case(summary, result, "null_argument_hypothesis")
        # Assert
        self.assertTrue(assessment["null_conditions"][0]["required_null"])
        self.assertTrue(assessment["null_conditions"][0]["model_agrees"])

    def givenTemporaryLikeSymbol_whenAssessingCase_thenArgumentBindingRemainsAmbiguous(
        self,
    ):
        # Arrange
        summary = {
            "params": "java.io.Reader",
            "method": "read",
            "exceptionType": "java.lang.NullPointerException",
            "throwSiteKind": "CALLEE_PROPAGATED",
            "constraints": [{"symExpr": "(stack_7 == null)", "truthValue": True}],
        }
        result = {
            "modelValues": {
                "stack_7": "IntValue[value=0]",
                "stack_7_is_null": "BoolValue[value=true]",
            }
        }
        # Act
        assessment = assess_case(summary, result, "null_argument_hypothesis")
        # Assert
        self.assertEqual(
            assessment["classification_review"], "initial_tier_needs_symbol_context"
        )
        self.assertEqual(
            assessment["argument_assignment"], "argument_binding_ambiguous"
        )
        self.assertEqual(
            assessment["execution_readiness"], "not_established_from_exports"
        )

    def givenContradictoryNullFlag_whenAssessingCase_thenDisagreementIsRetained(self):
        # Arrange
        summary = {
            "params": "java.io.File",
            "method": "check",
            "exceptionType": "java.lang.NullPointerException",
            "throwSiteKind": "IMPLICIT",
            "constraints": [{"symExpr": "(file == null)", "truthValue": True}],
        }
        result = {
            "modelValues": {
                "file": "IntValue[value=0]",
                "file_is_null": "BoolValue[value=false]",
            }
        }
        # Act
        assessment = assess_case(summary, result, "object_fixture_required")
        # Assert
        self.assertFalse(assessment["null_conditions"][0]["model_agrees"])
        self.assertIn("recognized_condition_and_model_disagree", assessment["gaps"])


def load_tests(
    loader: unittest.TestLoader, suite: unittest.TestSuite, pattern: str
) -> unittest.TestSuite:
    """Discover the required given/when/then method names with the standard runner."""
    loader.testMethodPrefix = "given"
    return loader.loadTestsFromTestCase(CaseInventoryChecks)
