"""Merge staged research (research/enrichment/*.json, research/new/*.json) into build/problems_source.json.

Usage: python3 build/merge_enrichment.py [--dry-run]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "build" / "problems_source.json"
ENR = ROOT / "research" / "enrichment"
NEW = ROOT / "research" / "new"

ENRICH_FIELDS = [
    "background", "known_results", "status", "progress", "importance", "difficulty",
    "counterexample_suitability", "counterexample_rationale",
    "alphaevolve_suitability", "alphaevolve_rationale",
    "literature", "agent_guidance", "notes_for_maintainer", "contributor",
]
OPTIONAL_IMPROVE = ["short_statement", "full_statement", "open_problem", "title"]
NEW_REQUIRED = ["id", "title", "collection", "area", "short_statement", "full_statement",
                "known_results", "status", "where_posed", "source", "background"]
VALID_STATUS = {"open", "partially resolved", "solution claimed", "conjecture", "resolved"}
VALID_SUIT = {"low", "medium", "high"}


def merge_refs(old, new):
    seen = {(r.get("title") or "").strip().lower() for r in old}
    out = list(old)
    for r in new or []:
        key = (r.get("title") or "").strip().lower()
        if key and key not in seen:
            seen.add(key)
            out.append(r)
    return out


def check(rec, fname, report):
    if rec.get("status") and rec["status"] not in VALID_STATUS:
        report.append(f"WARN {fname}: bad status {rec['status']!r}")
    for f in ("counterexample_suitability", "alphaevolve_suitability"):
        if rec.get(f) and str(rec[f]).lower() not in VALID_SUIT:
            report.append(f"WARN {fname}: bad {f} {rec[f]!r}")
    for f in ("importance", "difficulty"):
        if rec.get(f) is not None and not (isinstance(rec[f], int) and 1 <= rec[f] <= 10):
            report.append(f"WARN {fname}: bad {f} {rec[f]!r}")
    for f in ("background", "full_statement", "known_results"):
        v = rec.get(f, "")
        if v and ("\\(" in v or "\\[" in v):
            report.append(f"WARN {fname}: {f} uses \\(..\\) delimiters instead of $..$")


def main():
    dry = "--dry-run" in sys.argv
    src = json.load(open(SRC))
    by_id = {r["id"]: r for r in src}
    report, n_enr, n_new = [], 0, 0

    for f in sorted(ENR.glob("*.json")):
        try:
            e = json.load(open(f))
        except Exception as ex:
            report.append(f"FAIL {f.name}: invalid JSON: {ex}")
            continue
        pid = e.get("id") or f.stem
        base = by_id.get(pid)
        if not base:
            report.append(f"FAIL {f.name}: no such problem id {pid!r}")
            continue
        check(e, f.name, report)
        for k in ENRICH_FIELDS:
            if e.get(k) not in (None, "", [], {}):
                base[k] = e[k]
        for k in OPTIONAL_IMPROVE:
            if e.get(k):
                base[k] = e[k]
        if e.get("where_posed"):
            wp = dict(base.get("where_posed") or {})
            for k, v in e["where_posed"].items():
                if v:
                    wp[k] = v
            base["where_posed"] = wp
        if e.get("additional_refs"):
            base["additional_refs"] = merge_refs(base.get("additional_refs") or [], e["additional_refs"])
        if e.get("tags"):
            base["tags"] = list(dict.fromkeys((base.get("tags") or []) + e["tags"]))
        n_enr += 1

    for f in sorted(NEW.glob("*.json")):
        try:
            e = json.load(open(f))
        except Exception as ex:
            report.append(f"FAIL {f.name}: invalid JSON: {ex}")
            continue
        pid = e.get("id") or f.stem
        if pid in by_id:
            report.append(f"SKIP {f.name}: id {pid!r} already exists (treat as enrichment?)")
            continue
        missing = [k for k in NEW_REQUIRED if not e.get(k)]
        if missing:
            report.append(f"FAIL {f.name}: missing {missing}")
            continue
        check(e, f.name, report)
        e.setdefault("enabled", True)
        e.setdefault("tags", [])
        e.setdefault("confidence", "medium")
        e.setdefault("additional_refs", [])
        src.append(e)
        by_id[pid] = e
        n_new += 1

    print(f"merged {n_enr} enrichments, added {n_new} new problems -> {len(src)} total records")
    for line in report:
        print(" ", line)
    if not dry:
        json.dump(src, open(SRC, "w"), indent=2, ensure_ascii=False)
        (ROOT / "research" / "merge-report.txt").write_text("\n".join(report) or "clean")
        print("wrote", SRC)


if __name__ == "__main__":
    main()
