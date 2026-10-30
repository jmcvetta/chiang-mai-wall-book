import argparse
import json
from pathlib import Path


RENDERER = "research/inventory/render_map.py"


def read_report(path: Path) -> dict[str, int | float | None]:
    """Load and validate one pytest-cov JSON report."""
    try:
        report = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Coverage report is unavailable or malformed: {path}: {error}")

    files = report.get("files")
    totals = report.get("totals")
    if not isinstance(files, dict) or not any(
        name.replace("\\", "/").endswith(RENDERER) for name in files
    ):
        raise SystemExit(f"Coverage report does not include {RENDERER}: {path}")
    if not isinstance(totals, dict):
        raise SystemExit(f"Coverage report has no totals object: {path}")

    statements = totals.get("num_statements")
    covered = totals.get("covered_lines")
    branches = totals.get("num_branches")
    covered_branches = totals.get("covered_branches")
    if not isinstance(statements, int) or not isinstance(covered, int):
        raise SystemExit(f"Coverage report has invalid line totals: {path}")
    if statements < 0 or covered < 0 or covered > statements:
        raise SystemExit(f"Coverage report has inconsistent line totals: {path}")
    if branches is not None and covered_branches is not None:
        if not isinstance(branches, int) or not isinstance(covered_branches, int):
            raise SystemExit(f"Coverage report has invalid branch totals: {path}")
        if branches < 0 or covered_branches < 0 or covered_branches > branches:
            raise SystemExit(f"Coverage report has inconsistent branch totals: {path}")
    else:
        branches = covered_branches = None

    percent = covered / statements * 100 if statements else None
    branch_percent = (
        covered_branches / branches * 100 if branches else None
    )
    return {
        "statements": statements,
        "covered": covered,
        "percent": percent,
        "branches": branches,
        "covered_branches": covered_branches,
        "branch_percent": branch_percent,
    }


def show(value: float | None) -> str:
    """Format a coverage percentage for Markdown."""
    return f"{value:.2f}%" if value is not None else "n/a"


def branch_totals(report: dict[str, int | float | None]) -> str:
    """Format branch totals for the coverage summary."""
    branches = report["branches"]
    covered = report["covered_branches"]
    if branches is None or covered is None:
        return "n/a"
    return f"{covered}/{branches} ({show(report['branch_percent'])})"


def main() -> None:
    """Write validated coverage totals and comparison to the job summary."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--head-report", required=True, type=Path)
    parser.add_argument("--head-revision", required=True)
    parser.add_argument("--base-report", type=Path)
    parser.add_argument("--base-revision")
    parser.add_argument("--no-base-reason")
    parser.add_argument("--summary", required=True, type=Path)
    args = parser.parse_args()

    head = read_report(args.head_report)
    lines = [
        "## Python coverage",
        "",
        "Line coverage measures production Python under `research/inventory`; it does not measure the shell sync implementation or test helpers.",
        "",
        "| Revision | Statements covered | Line coverage | Branches covered |",
        "| --- | ---: | ---: | ---: |",
        f"| Head `{args.head_revision}` | {head['covered']}/{head['statements']} | {show(head['percent'])} | {branch_totals(head)} |",
    ]

    if args.base_report:
        if not args.base_revision:
            raise SystemExit("A base revision is required with a base report")
        base = read_report(args.base_report)
        lines.insert(
            6,
            f"| Base `{args.base_revision}` | {base['covered']}/{base['statements']} | {show(base['percent'])} | {branch_totals(base)} |",
        )
        if base["statements"] == 0 or head["statements"] == 0:
            reason = "the base" if base["statements"] == 0 else "the head"
            lines.extend(
                [
                    "",
                    f"Coverage comparison unavailable: {reason} revision has no measured source statements.",
                ]
            )
        else:
            delta = head["percent"] - base["percent"]
            lines.extend(
                [
                    "",
                    f"Line coverage change: {delta:+.2f} percentage points (head minus base).",
                ]
            )
    else:
        if not args.no_base_reason:
            raise SystemExit("State why a base comparison is unavailable")
        lines.extend(["", f"Coverage comparison unavailable: {args.no_base_reason}"])

    args.summary.parent.mkdir(parents=True, exist_ok=True)
    with args.summary.open("a") as summary:
        summary.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
