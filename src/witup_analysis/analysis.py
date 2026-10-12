"""Build reproducible derived tables and answer the four data questions."""

import json
import os
import subprocess
import sys
from collections import Counter
from datetime import UTC, datetime
from importlib.metadata import version
from pathlib import Path

import duckdb

from witup_analysis.profiling import candidate_features, profile
from witup_analysis.reporting import write_report

COMMON_COLUMNS = """artifact: 'VARCHAR', package: 'VARCHAR', class: 'VARCHAR',
method: 'VARCHAR', returnType: 'VARCHAR', params: 'VARCHAR',
pathIndex: 'BIGINT', pathId: 'VARCHAR'"""
RESULT_COLUMNS = COMMON_COLUMNS + ", status: 'VARCHAR', modelValues: 'JSON'"
SUMMARY_COLUMNS = (
    COMMON_COLUMNS
    + """, exceptionType: 'VARCHAR', throwSiteKind: 'VARCHAR',
provenance: 'VARCHAR[]', provenances: 'VARCHAR[][]', solverStatus: 'VARCHAR',
constraints: 'STRUCT(symExpr VARCHAR, truthValue BOOLEAN)[]'"""
)
FEATURE_COLUMNS = {
    "artifact": "VARCHAR",
    "pathId": "VARCHAR",
    "tier": "VARCHAR",
    "constraintCount": "INTEGER",
    "modelValueCount": "INTEGER",
    "parameterCount": "INTEGER",
    "receiverState": "BOOLEAN",
    "staticState": "BOOLEAN",
    "methodCalls": "BOOLEAN",
    "symbolicValues": "BOOLEAN",
    "complexModelKeys": "BOOLEAN",
}


def git_revision(directory: Path) -> dict:
    if not (directory / ".git").exists():
        return {"available": False}
    result = subprocess.run(
        ["git", "-C", str(directory), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    return {"available": True, "commit": result.stdout.strip()}


def select_input(explicit: Path | None, directory: Path, pattern: str) -> Path:
    if explicit is not None:
        path = explicit.resolve()
        if not path.is_file():
            raise FileNotFoundError(path)
        return path
    matches = sorted(directory.glob(pattern))
    if len(matches) != 1:
        raise ValueError(
            f"Expected one {pattern} in {directory}; found {len(matches)}. Supply an explicit path."
        )
    return matches[0].resolve()


def records(connection: duckdb.DuckDBPyConnection, query: str) -> list[dict]:
    cursor = connection.execute(query)
    names = [column[0] for column in cursor.description]
    return [dict(zip(names, row, strict=True)) for row in cursor.fetchall()]


def scalar(connection: duckdb.DuckDBPyConnection, query: str) -> int:
    row = connection.execute(query).fetchone()
    if row is None:
        raise ValueError("Scalar query returned no row.")
    return row[0]


def analyze(
    root: Path,
    input_dir: Path,
    results_path: Path | None,
    summaries_path: Path | None,
    output_dir: Path,
    report_path: Path,
) -> None:
    results_path = select_input(results_path, input_dir, "witup-results-*.json")
    summaries_path = select_input(summaries_path, input_dir, "witup-summaries-*.json")
    output_dir, report_path = output_dir.resolve(), report_path.resolve()
    for destination in (output_dir, report_path):
        if os.name == "nt" and destination.drive.upper() != "D:":
            raise ValueError(
                f"Project outputs must remain on the D: drive: {destination}"
            )
    profiles = {}
    for kind, path in (("results", results_path), ("summaries", summaries_path)):
        print(f"Profiling all records in {path.name}", flush=True)
        profiles[kind] = profile(path, kind)
        if profiles[kind]["totals"].get("schema_issue_count", 0):
            raise ValueError(
                f"Invalid {kind} schema: {profiles[kind]['schema_issues']}"
            )
    if profiles["results"]["artifacts"] != profiles["summaries"]["artifacts"]:
        raise ValueError("Input files refer to different artifact sets")
    output_dir.mkdir(parents=True, exist_ok=True)
    connection = duckdb.connect(str(output_dir / "commons-io.duckdb"))
    try:
        connection.execute("SET threads = 4")
        for name, path, columns in (
            ("results", results_path, RESULT_COLUMNS),
            ("summaries", summaries_path, SUMMARY_COLUMNS),
        ):
            connection.execute(
                f"CREATE OR REPLACE TABLE {name} AS SELECT * FROM read_json(?, format='array', columns={{{columns}}})",
                [str(path)],
            )
            count = scalar(connection, f"SELECT count(*) FROM {name}")
            if count != profiles[name]["totals"]["rows"]:
                raise ValueError(f"Independent parser counts differ for {name}")
        duplicate_counts = {
            name: scalar(
                connection,
                f"SELECT count(*) FROM (SELECT artifact, pathId FROM {name} GROUP BY ALL HAVING count(*) > 1)",
            )
            for name in ("results", "summaries")
        }
        if any(duplicate_counts.values()):
            raise ValueError(f"Join keys are not unique: {duplicate_counts}")
        connection.execute("""
            CREATE OR REPLACE TABLE joined AS
            SELECT s.*, r.status AS resultStatus, r.modelValues,
                   r.pathId IS NOT NULL AS hasResult,
                   (s.package = r.package AND s.class = r.class AND s.method = r.method
                    AND s.returnType = r.returnType AND s.params = r.params
                    AND s.pathIndex = r.pathIndex) AS metadataMatches
            FROM summaries s LEFT JOIN results r USING (artifact, pathId)
        """)
        correspondence = {
            "duplicate_keys": duplicate_counts,
            "matched_summaries": scalar(
                connection, "SELECT count(*) FROM joined WHERE hasResult"
            ),
            "summaries_without_results": scalar(
                connection, "SELECT count(*) FROM joined WHERE NOT hasResult"
            ),
            "results_without_summaries": scalar(
                connection,
                "SELECT count(*) FROM results r ANTI JOIN summaries s USING (artifact,pathId)",
            ),
            "status_mismatches": scalar(
                connection,
                "SELECT count(*) FROM joined WHERE hasResult AND solverStatus <> resultStatus",
            ),
            "metadata_mismatches": scalar(
                connection,
                "SELECT count(*) FROM joined WHERE hasResult AND NOT metadataMatches",
            ),
            "results_only_methods": scalar(
                connection,
                """SELECT count(*) FROM (
                SELECT DISTINCT regexp_replace(pathId, '#[0-9]+$', '') AS signature FROM results
                EXCEPT SELECT DISTINCT regexp_replace(pathId, '#[0-9]+$', '') FROM summaries)""",
            ),
            "summaries_only_methods": scalar(
                connection,
                """SELECT count(*) FROM (
                SELECT DISTINCT regexp_replace(pathId, '#[0-9]+$', '') AS signature FROM summaries
                EXCEPT SELECT DISTINCT regexp_replace(pathId, '#[0-9]+$', '') FROM results)""",
            ),
        }
        print("Classifying data-level preparation requirements", flush=True)
        connection.execute("""CREATE OR REPLACE TABLE candidate_features (
            artifact VARCHAR, pathId VARCHAR, tier VARCHAR, constraintCount INTEGER,
            modelValueCount INTEGER, parameterCount INTEGER, receiverState BOOLEAN,
            staticState BOOLEAN, methodCalls BOOLEAN, symbolicValues BOOLEAN, complexModelKeys BOOLEAN
        )""")
        cursor = connection.cursor()
        cursor.execute("""SELECT artifact, pathId, params, constraints, modelValues, solverStatus,
                         resultStatus, hasResult, metadataMatches, exceptionType FROM joined""")
        tier_counts, feature_counts = Counter(), Counter()
        connection.execute("BEGIN TRANSACTION")
        while batch := cursor.fetchmany(2000):
            features_batch = []
            for (
                artifact,
                path_id,
                params,
                constraints,
                raw_model,
                summary_status,
                result_status,
                has_result,
                metadata_matches,
                exception_type,
            ) in batch:
                model = json.loads(raw_model) if raw_model is not None else {}
                features = candidate_features(
                    {"params": params, "constraints": constraints}, model
                )
                if not has_result:
                    features["tier"] = "missing_result"
                elif not metadata_matches or summary_status != result_status:
                    features["tier"] = "join_disagreement"
                elif summary_status != "SAT" or result_status != "SAT":
                    features["tier"] = "solver_not_sat"
                elif exception_type is None:
                    features["tier"] = "exception_not_reported"
                tier_counts[features["tier"]] += 1
                feature_counts.update(
                    {
                        key: int(value)
                        for key, value in features.items()
                        if isinstance(value, bool)
                    }
                )
                features_batch.append(
                    {
                        "artifact": artifact,
                        "pathId": path_id,
                        "tier": features["tier"],
                        "constraintCount": features["constraint_count"],
                        "modelValueCount": features["model_value_count"],
                        "parameterCount": features["parameter_count"],
                        "receiverState": features["receiver_state"],
                        "staticState": features["static_state"],
                        "methodCalls": features["method_calls"],
                        "symbolicValues": features["symbolic_values"],
                        "complexModelKeys": features["complex_model_keys"],
                    }
                )
            connection.execute(
                """INSERT INTO candidate_features
                SELECT item.* FROM unnest(from_json(?, ?)) AS batch(item)""",
                [json.dumps(features_batch), json.dumps([FEATURE_COLUMNS])],
            )
        connection.execute("COMMIT")
        cursor.close()
        connection.execute("""CREATE OR REPLACE TABLE candidates AS
            SELECT j.*, f.* EXCLUDE (artifact,pathId)
            FROM joined j JOIN candidate_features f USING (artifact,pathId)""")
        status_matrix = records(
            connection,
            "SELECT solverStatus, resultStatus, count(*) AS rows FROM joined GROUP BY ALL ORDER BY rows DESC",
        )
        examples = records(
            connection,
            """SELECT artifact, pathId, exceptionType, throwSiteKind, params,
            solverStatus, modelValues, to_json(constraints) AS constraints, tier,
            constraintCount, modelValueCount
            FROM (SELECT * FROM candidates
            WHERE tier IN ('simple_signature_hypothesis','null_argument_hypothesis')
            QUALIFY row_number() OVER (PARTITION BY regexp_replace(pathId, '#[0-9]+$', '') ORDER BY constraintCount, pathId) = 1
            )
            QUALIFY row_number() OVER (PARTITION BY tier ORDER BY
                CASE throwSiteKind WHEN 'DIRECT_ATHROW' THEN 0 WHEN 'IMPLICIT' THEN 1 ELSE 2 END,
                constraintCount, modelValueCount, pathId) <= 6
            ORDER BY CASE throwSiteKind WHEN 'DIRECT_ATHROW' THEN 0 WHEN 'IMPLICIT' THEN 1 ELSE 2 END,
                     constraintCount, modelValueCount, pathId""",
        )
        for example in examples:
            example["modelValues"] = json.loads(example["modelValues"])
            example["constraints"] = json.loads(example["constraints"])
        for table in ("results", "summaries", "candidates"):
            connection.table(table).write_parquet(
                str(output_dir / f"{table}.parquet"), compression="zstd"
            )
        method_rows = records(
            connection,
            """SELECT regexp_replace(pathId, '#[0-9]+$', '') AS signature,
            count(*) AS paths, count(*) FILTER (WHERE solverStatus='SAT') AS sat_paths
            FROM summaries GROUP BY ALL ORDER BY paths DESC, signature LIMIT 15""",
        )
        missing_statuses = records(
            connection,
            """SELECT r.status, count(*) AS rows
            FROM results r ANTI JOIN summaries s USING (artifact,pathId)
            GROUP BY ALL ORDER BY rows DESC""",
        )
        statistics = {
            "generated_at_utc": datetime.now(UTC).isoformat(),
            "environment": {
                "python": sys.version.split()[0],
                "duckdb": version("duckdb"),
                "ijson": version("ijson"),
            },
            "source_context": {
                "witup": git_revision(root / "core"),
                "commons_io": git_revision(root / "commons-io"),
            },
            "profiles": profiles,
            "correspondence": correspondence,
            "status_matrix": status_matrix,
            "unmatched_result_statuses": missing_statuses,
            "candidate_tiers": dict(tier_counts.most_common()),
            "candidate_features": dict(feature_counts),
            "candidate_examples": examples,
            "methods_with_most_paths": method_rows,
        }
        (output_dir / "statistics.json").write_text(
            json.dumps(statistics, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
        )
        write_report(statistics, report_path)
        print(
            json.dumps(
                {
                    "report": str(report_path),
                    "results": profiles["results"]["totals"]["rows"],
                    "summaries": profiles["summaries"]["totals"]["rows"],
                    "correspondence": correspondence,
                    "candidate_tiers": statistics["candidate_tiers"],
                },
                indent=2,
            ),
            flush=True,
        )
    finally:
        connection.close()
