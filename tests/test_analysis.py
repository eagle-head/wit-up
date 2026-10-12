"""Check scalar query observations with an isolated in-memory database."""

import unittest

import duckdb

from witup_analysis.analysis import scalar


class ScalarQueryChecks(unittest.TestCase):
    def givenAggregateQuery_whenReadingScalar_thenObservedCountIsReturned(self):
        # Arrange
        with duckdb.connect() as connection:
            query = "SELECT count(*) FROM (VALUES (1), (2), (3))"
            # Act
            observed = scalar(connection, query)
        # Assert
        self.assertEqual(observed, 3)

    def givenQueryWithoutRows_whenReadingScalar_thenMissingObservationIsReported(self):
        # Arrange
        with duckdb.connect() as connection:
            query = "SELECT 1 WHERE FALSE"
            # Act / Assert
            with self.assertRaisesRegex(ValueError, "returned no row"):
                scalar(connection, query)


def load_tests(loader, suite, pattern):
    loader.testMethodPrefix = "given"
    return loader.loadTestsFromTestCase(ScalarQueryChecks)


if __name__ == "__main__":
    unittest.main()
