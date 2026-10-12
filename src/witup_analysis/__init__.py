"""Command-line entry point for analyzing existing WIT-UP exports."""

import argparse
from pathlib import Path

from witup_analysis.analysis import analyze
from witup_analysis.case_validation import validate_cases
from witup_analysis.selection import inspect_cases


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser(
        "analyze", help="Profile JSON exports and write a report"
    )
    command.add_argument(
        "--input-dir", type=Path, default=root / "commons-io-analysis-results"
    )
    command.add_argument("--results", type=Path)
    command.add_argument("--summaries", type=Path)
    command.add_argument("--output-dir", type=Path, default=root / "data" / "processed")
    command.add_argument(
        "--report", type=Path, default=root / "docs" / "commons-io-json-analysis.md"
    )
    case_command = commands.add_parser(
        "inspect-cases", help="Select and assess cases from the existing JSON inventory"
    )
    case_command.add_argument(
        "--output-dir", type=Path, default=root / "data" / "processed"
    )
    case_command.add_argument("--docs-dir", type=Path, default=root / "docs")
    case_command.add_argument("--per-stratum", type=int, default=10)
    commands.add_parser(
        "validate-cases",
        help="Verify the saved case inventory and local documentation links",
    )
    args = parser.parse_args()
    if args.command == "analyze":
        analyze(
            root,
            args.input_dir,
            args.results,
            args.summaries,
            args.output_dir,
            args.report,
        )
    elif args.command == "inspect-cases":
        inspect_cases(root, args.output_dir, args.docs_dir, args.per_stratum)
    else:
        validate_cases(root)
