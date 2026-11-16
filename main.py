#!/usr/bin/env python3
"""Audit CSS custom property declarations and var() references."""
import argparse
import re
from collections import Counter
from pathlib import Path

def audit_css(source: str):
    cleaned = re.sub(r"/\*.*?\*/", "", source, flags=re.S)
    definitions = re.findall(r"(--[A-Za-z0-9_-]+)\s*:", cleaned)
    references = re.findall(r"var\(\s*(--[A-Za-z0-9_-]+)", cleaned)
    counts = Counter(definitions)
    defined, used = set(definitions), set(references)
    return {
        "duplicates": sorted(name for name,count in counts.items() if count > 1),
        "undefined": sorted(used - defined),
        "unused": sorted(defined - used),
        "definitions": len(definitions),
        "references": len(references),
    }

def main():
    parser = argparse.ArgumentParser(description="Find duplicate, undefined, and unused CSS tokens.")
    parser.add_argument("css", type=Path)
    parser.add_argument("--strict-unused", action="store_true")
    args = parser.parse_args()
    try:
        report = audit_css(args.css.read_text(encoding="utf-8"))
    except OSError as exc:
        parser.error(str(exc))
    for key in ("duplicates", "undefined", "unused"):
        print(f"{key.title()}:")
        for item in report[key] or ["none"]:
            print(f"  - {item}" if item != "none" else "  none")
    print(f"\nDefinitions: {report['definitions']} | var() references: {report['references']}")
    return 1 if report["undefined"] or report["duplicates"] or (args.strict_unused and report["unused"]) else 0
if __name__ == "__main__":
    raise SystemExit(main())
