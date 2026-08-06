"""
Learning OS Content Pipeline — Import Validator
================================================
Validates a returned contributor package before moving to review.

Usage:
    python content_pipeline/scripts/validate_import.py --package <path>
    python content_pipeline/scripts/validate_import.py --package imports/pending_review/PKG-20260806-JS-001

Run from project root.
"""
import sys
import re
import argparse
from pathlib import Path
from datetime import datetime, timezone

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"d:\My Drive\all files\PROJECT FILES\notes")
CP   = ROOT / "content_pipeline"

REQUIRED_ROOT_FILES = [
    "PACKAGE_MANIFEST.md",
    "README.md",
    "COURSE_METADATA.md",
    "STYLE_GUIDE.md",
    "NOTE_TEMPLATE.md",
    "CHECKLIST.md",
    "VALIDATION_RULES.md",
    "CONTRIBUTOR_GUIDE.md",
    "REPORT.md",
]

REQUIRED_DIRS = ["SYLLABUS", "CURRICULUM"]

STUB_THRESHOLD = 500  # bytes — files below this are stubs
MIN_INTERVIEW_QS = 3
MIN_REFERENCES = 2
CODE_BLOCK_RE = re.compile(r"```(\w*)")
H1_RE = re.compile(r"^# .+", re.MULTILINE)
INTERVIEW_RE = re.compile(r"\*\*Q\d+", re.MULTILINE)
REFERENCES_RE = re.compile(r"## References", re.MULTILINE)
METADATA_RE = re.compile(r"^> \*\*Course:\*\*", re.MULTILINE)


def check(condition: bool, msg_pass: str, msg_fail: str, issues: list, warnings: list, critical: bool = False):
    if condition:
        return True
    if critical:
        issues.append(msg_fail)
    else:
        warnings.append(msg_fail)
    return False


def validate_package(pkg_path: Path) -> dict:
    issues = []
    warnings = []
    passed = []
    stats = {}

    print(f"\n  Validating: {pkg_path.name}\n")

    # ── 1. Package exists ──────────────────────────────────────────────────
    if not pkg_path.exists():
        return {"status": "FAILED", "issues": [f"Package path does not exist: {pkg_path}"], "warnings": [], "passed": [], "stats": {}}

    # ── 2. Required root files ─────────────────────────────────────────────
    for f in REQUIRED_ROOT_FILES:
        if (pkg_path / f).exists():
            passed.append(f"Required file present: {f}")
        else:
            issues.append(f"MISSING required file: {f}")

    # ── 3. Required directories ────────────────────────────────────────────
    for d in REQUIRED_DIRS:
        if (pkg_path / d).is_dir():
            passed.append(f"Required directory present: {d}/")
        else:
            issues.append(f"MISSING required directory: {d}/")

    # ── 4. PACKAGE_MANIFEST fields ─────────────────────────────────────────
    manifest_path = pkg_path / "PACKAGE_MANIFEST.md"
    if manifest_path.exists():
        manifest = manifest_path.read_text(encoding="utf-8", errors="replace")
        for field in ["package_id:", "course_name:", "version:", "status:", "assigned_to:"]:
            if field in manifest:
                passed.append(f"Manifest field: {field}")
            else:
                warnings.append(f"Manifest missing field: {field}")

    # ── 5. CURRICULUM analysis ─────────────────────────────────────────────
    curr_dir = pkg_path / "CURRICULUM"
    if curr_dir.is_dir():
        all_files = list(curr_dir.rglob("*.md"))
        stubs = [f for f in all_files if f.stat().st_size < STUB_THRESHOLD]
        complete = [f for f in all_files if f.stat().st_size >= STUB_THRESHOLD]
        stats["total_files"]    = len(all_files)
        stats["complete_files"] = len(complete)
        stats["stubs_remaining"] = len(stubs)

        if stubs:
            issues.append(f"STUBS REMAINING: {len(stubs)} files still below {STUB_THRESHOLD} bytes")
            for s in stubs[:10]:  # show first 10
                issues.append(f"  Stub: {s.relative_to(pkg_path)}")
            if len(stubs) > 10:
                issues.append(f"  ... and {len(stubs)-10} more")
        else:
            passed.append("All curriculum files are complete (> 500 bytes)")

        # ── 6. Per-file content checks ─────────────────────────────────────
        no_h1 = []
        no_metadata = []
        no_refs = []
        no_interview = []
        code_no_lang = []
        renamed = []

        for f in complete:
            content = f.read_text(encoding="utf-8", errors="replace")

            if not H1_RE.search(content):
                no_h1.append(str(f.relative_to(pkg_path)))
            if not METADATA_RE.search(content):
                no_metadata.append(str(f.relative_to(pkg_path)))
            if not REFERENCES_RE.search(content):
                no_refs.append(str(f.relative_to(pkg_path)))

            q_count = len(INTERVIEW_RE.findall(content))
            if q_count < MIN_INTERVIEW_QS:
                no_interview.append((str(f.relative_to(pkg_path)), q_count))

            # Check code blocks
            for m in CODE_BLOCK_RE.finditer(content):
                if not m.group(1).strip():
                    code_no_lang.append(str(f.relative_to(pkg_path)))
                    break

        if no_h1:
            for p in no_h1[:5]: warnings.append(f"No H1 title: {p}")
        else:
            passed.append("All files have H1 title")

        if no_metadata:
            for p in no_metadata[:5]: warnings.append(f"No metadata blockquote: {p}")
        else:
            passed.append("All files have metadata blockquote")

        if no_refs:
            for p in no_refs[:5]: issues.append(f"No References section: {p}")
        else:
            passed.append("All files have References section")

        if no_interview:
            for p, q in no_interview[:5]:
                warnings.append(f"Only {q} interview Qs (need {MIN_INTERVIEW_QS}): {p}")
        else:
            passed.append(f"All files have >= {MIN_INTERVIEW_QS} interview questions")

        if code_no_lang:
            for p in code_no_lang[:5]: issues.append(f"Code block without language identifier: {p}")
        else:
            passed.append("All code blocks have language identifiers")

    # ── 7. CHECKLIST filled? ───────────────────────────────────────────────
    chk = pkg_path / "CHECKLIST.md"
    if chk.exists():
        chk_content = chk.read_text(encoding="utf-8", errors="replace")
        unfilled = chk_content.count("☐")
        filled = chk_content.count("☑")
        if unfilled > 0:
            warnings.append(f"CHECKLIST has {unfilled} unchecked items (☐)")
        else:
            passed.append(f"CHECKLIST fully completed ({filled} items)")

    # ── 8. REPORT.md filled? ──────────────────────────────────────────────
    rpt = pkg_path / "REPORT.md"
    if rpt.exists():
        rpt_content = rpt.read_text(encoding="utf-8", errors="replace")
        if "_(fill)_" in rpt_content or "_(fill in)_" in rpt_content:
            warnings.append("REPORT.md still has unfilled fields")
        else:
            passed.append("REPORT.md appears to be filled")

    # ── Summary ────────────────────────────────────────────────────────────
    status = "FAILED" if issues else ("WARNING" if warnings else "PASSED")

    return {
        "status":   status,
        "issues":   issues,
        "warnings": warnings,
        "passed":   passed,
        "stats":    stats,
    }


def write_report(pkg_path: Path, result: dict):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    pkg_id = pkg_path.name
    report_path = CP / "reports" / f"VALIDATION_REPORT_{pkg_id}_{today}.md"

    lines = [
        f"# Validation Report\n\n",
        f"**package_id:** {pkg_id}  \n",
        f"**date:** {today}  \n",
        f"**status:** {result['status']}  \n\n---\n\n",
        f"## Statistics\n\n",
    ]
    for k, v in result["stats"].items():
        lines.append(f"- **{k}:** {v}\n")

    if result["issues"]:
        lines.append(f"\n## Issues (Critical — {len(result['issues'])})\n\n")
        for i in result["issues"]:
            lines.append(f"- {i}\n")

    if result["warnings"]:
        lines.append(f"\n## Warnings ({len(result['warnings'])})\n\n")
        for w in result["warnings"]:
            lines.append(f"- {w}\n")

    if result["passed"]:
        lines.append(f"\n## Passed Checks ({len(result['passed'])})\n\n")
        for p in result["passed"]:
            lines.append(f"- ✅ {p}\n")

    report_path.write_text("".join(lines), encoding="utf-8")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="Validate a returned contributor package")
    parser.add_argument("--package", required=True, help="Path to the returned package")
    args = parser.parse_args()

    pkg_path = Path(args.package)
    if not pkg_path.is_absolute():
        pkg_path = ROOT / pkg_path

    result = validate_package(pkg_path)
    report_path = write_report(pkg_path, result)

    # ── Print summary ──────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"  VALIDATION: {result['status']}")
    print(f"{'='*60}")
    print(f"  Issues:   {len(result['issues'])}")
    print(f"  Warnings: {len(result['warnings'])}")
    print(f"  Passed:   {len(result['passed'])}")
    for k, v in result["stats"].items():
        print(f"  {k}: {v}")
    print(f"\n  Report: {report_path}\n")

    if result["status"] == "FAILED":
        print("  ❌ VALIDATION FAILED — Package cannot proceed to review\n")
        sys.exit(1)
    elif result["status"] == "WARNING":
        print("  ⚠️  WARNINGS — Review manually before proceeding\n")
        sys.exit(0)
    else:
        print("  ✅ VALIDATION PASSED — Package may proceed to review\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
