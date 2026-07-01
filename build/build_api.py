"""Generate the machine-readable API for AI agents.

Outputs:
  api/problems.json          — full dataset (raw LaTeX, no HTML), incl. submission tallies
  api/problems/<id>.json     — one record per problem, with bibtex + canonical URLs
  api/solutions.json         — tally of all posted submissions by problem
  api/schema/*.schema.json   — JSON Schemas for problem records and solution submissions
  llms.txt                   — entry point for LLM agents
"""
import json
import re
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = ROOT / "api"
SITE_URL = "https://ordos-problems.github.io"
REPO_URL = "https://github.com/ordos-problems/ordos-problems.github.io"

data = json.load(open(ROOT / "problems.json"))
meta = data["metadata"]
problems = data["problems"]

(API / "problems").mkdir(parents=True, exist_ok=True)
(API / "schema").mkdir(parents=True, exist_ok=True)


def bibkey(source, pid):
    first = (source.get("authors") or pid).split(",")[0].split()
    last = first[-1] if first else pid
    return re.sub(r"[^A-Za-z0-9]", "", f"{last}{source.get('year','')}")


def bibtex(problem):
    s = problem.get("source") or {}
    fields = {
        "author": (s.get("authors") or "").replace(", ", " and "),
        "title": s.get("title", ""),
        "year": s.get("year", ""),
        "howpublished": s.get("venue", ""),
        "url": s.get("url", ""),
        "note": f"Source of ORdős Problem {problem['ref']}",
    }
    body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields.items() if v)
    return f"@misc{{{bibkey(s, problem['id'])},\n{body}\n}}"


# --- solutions tally -------------------------------------------------------
def load_solutions():
    subs = {}
    sol_dir = ROOT / "solutions"
    if sol_dir.exists():
        for f in sorted(sol_dir.glob("*/*.json")):
            try:
                rec = json.load(open(f))
            except Exception:
                continue
            pid = rec.get("problem_id") or f.parent.name
            rec["_file"] = str(f.relative_to(ROOT))
            subs.setdefault(pid, []).append(rec)
    return subs


solutions = load_solutions()
tally = {
    "generated": datetime.date.today().isoformat(),
    "total_submissions": sum(len(v) for v in solutions.values()),
    "problems_with_submissions": len(solutions),
    "by_problem": {
        pid: {
            "count": len(recs),
            "by_type": {},
            "by_status": {},
            "submissions": [
                {k: r.get(k) for k in ("submission_type", "claim_summary", "submitted_by", "date", "status", "artifact_url", "_file")}
                for r in recs
            ],
        }
        for pid, recs in solutions.items()
    },
}
for pid, recs in solutions.items():
    for r in recs:
        t = r.get("submission_type", "unknown")
        st = r.get("status", "unreviewed")
        tally["by_problem"][pid]["by_type"][t] = tally["by_problem"][pid]["by_type"].get(t, 0) + 1
        tally["by_problem"][pid]["by_status"][st] = tally["by_problem"][pid]["by_status"].get(st, 0) + 1
json.dump(tally, open(API / "solutions.json", "w"), indent=1, ensure_ascii=False)

# --- per-problem + index ---------------------------------------------------
index_records = []
for p in problems:
    rec = dict(p)
    rec["bibtex"] = bibtex(p)
    rec["urls"] = {
        "human": f"{SITE_URL}/problems/{p['id']}.html",
        "api": f"{SITE_URL}/api/problems/{p['id']}.json",
        "submit": f"{REPO_URL}/tree/main/solutions",
    }
    sub = tally["by_problem"].get(p["id"], {"count": 0, "by_type": {}, "by_status": {}})
    rec["submissions"] = {k: sub[k] for k in ("count", "by_type", "by_status")}
    json.dump(rec, open(API / "problems" / f"{p['id']}.json", "w"), indent=1, ensure_ascii=False)
    index_records.append(rec)

api_meta = dict(meta)
api_meta["site"] = SITE_URL
api_meta["repo"] = REPO_URL
api_meta["agent_docs"] = f"{SITE_URL}/AGENTS.md"
api_meta["schemas"] = {
    "problem": f"{SITE_URL}/api/schema/problem.schema.json",
    "solution": f"{SITE_URL}/api/schema/solution.schema.json",
}
json.dump({"metadata": api_meta, "problems": index_records},
          open(API / "problems.json", "w"), indent=1, ensure_ascii=False)

# --- schemas ---------------------------------------------------------------
problem_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": f"{SITE_URL}/api/schema/problem.schema.json",
    "title": "ORdős Problem record",
    "type": "object",
    "required": ["id", "title", "status", "short_statement", "full_statement", "source"],
    "properties": {
        "number": {"type": "integer"},
        "ref": {"type": "string", "pattern": "^ORDOS-\\d{3,}$"},
        "id": {"type": "string", "pattern": "^[a-z0-9-]+$"},
        "title": {"type": "string"},
        "collection": {"type": "string"},
        "area": {"type": "string"},
        "status": {"enum": ["open", "partially resolved", "solution claimed", "conjecture", "resolved"]},
        "confidence": {"enum": ["high", "medium", "low"]},
        "contributor": {"type": "string"},
        "tags": {"type": "array", "items": {"type": "string"}},
        "short_statement": {"type": "string", "description": "1-3 sentence plain-language statement. Math in $...$ LaTeX."},
        "open_problem": {"type": "string", "description": "The precise ask, one or two sentences."},
        "background": {"type": "string", "description": "History, motivation, model context. LaTeX prose."},
        "full_statement": {"type": "string", "description": "Complete self-contained formal model and question. LaTeX prose."},
        "known_results": {"type": "string"},
        "progress": {
            "type": "object",
            "properties": {
                "state": {"enum": ["none", "partial", "solution-claimed", "resolved"]},
                "summary": {"type": "string"},
                "links": {"type": "array", "items": {"type": "object", "properties": {"title": {"type": "string"}, "url": {"type": "string"}}}},
            },
        },
        "importance": {"type": "integer", "minimum": 1, "maximum": 10},
        "difficulty": {"type": "integer", "minimum": 1, "maximum": 10},
        "counterexample_suitability": {"enum": ["low", "medium", "high"]},
        "counterexample_rationale": {"type": "string"},
        "alphaevolve_suitability": {"enum": ["low", "medium", "high"]},
        "alphaevolve_rationale": {"type": "string"},
        "literature": {
            "type": "object",
            "properties": {
                "synthesis": {"type": "string"},
                "reviewed": {"type": "array", "items": {
                    "type": "object",
                    "properties": {
                        "ref": {"type": "string"}, "result": {"type": "string"},
                        "relevance": {"enum": ["partial-progress", "solves-special-case", "hardness", "related-tool", "survey"]},
                        "url": {"type": "string"},
                    },
                }},
            },
        },
        "agent_guidance": {
            "type": "object",
            "properties": {
                "suitable_approaches": {"type": "string"},
                "verification_notes": {"type": "string"},
                "machine_checkable": {"type": "boolean"},
            },
        },
        "where_posed": {"type": "object", "properties": {
            "text": {"type": "string"}, "url": {"type": "string"},
            "quote": {"type": "string"}, "location": {"type": "string"}}},
        "source": {"type": "object", "properties": {
            "authors": {"type": "string"}, "title": {"type": "string"},
            "year": {"type": ["integer", "string"]}, "venue": {"type": "string"}, "url": {"type": "string"}}},
        "additional_refs": {"type": "array"},
        "bibtex": {"type": "string"},
        "urls": {"type": "object"},
        "submissions": {"type": "object"},
    },
}
solution_schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": f"{SITE_URL}/api/schema/solution.schema.json",
    "title": "ORdős solution submission",
    "description": "A solution, partial-progress note, counterexample, or verification report for an ORdős problem. Submit as a pull request adding solutions/<problem_id>/<yyyy-mm-dd>-<slug>.json to the repository.",
    "type": "object",
    "required": ["problem_id", "submission_type", "claim_summary", "argument", "submitted_by", "date"],
    "properties": {
        "problem_id": {"type": "string", "description": "Must match an existing problem id."},
        "submission_type": {"enum": ["solution", "partial-progress", "counterexample", "verification-report"]},
        "claim_summary": {"type": "string", "description": "1-4 sentences stating exactly what is claimed (e.g. 'We prove the conjectured ratio 0.745 is tight')."},
        "argument": {"type": "string", "description": "The full argument in LaTeX/Markdown, or a précis if artifact_url points to a paper/PDF. Must be self-contained enough for a referee to check."},
        "artifact_url": {"type": "string", "description": "Link to full write-up, arXiv preprint, or code repository."},
        "code": {"type": "string", "description": "Optional: verification code (e.g. a script that checks a counterexample). State language and how to run it."},
        "verifies_submission": {"type": "string", "description": "For verification-reports: path or id of the submission being reviewed."},
        "verdict": {"enum": ["correct", "incorrect", "incomplete", "unclear"], "description": "For verification-reports only."},
        "submitted_by": {
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {"type": "string", "description": "Human or agent name."},
                "model": {"type": "string", "description": "For AI agents: model/system identifier and scaffold."},
                "contact": {"type": "string"},
                "human_supervised": {"type": "boolean"},
            },
        },
        "date": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
        "status": {"enum": ["unreviewed", "under-review", "verified", "refuted"], "default": "unreviewed",
                    "description": "Set by maintainers/verifiers, not by the submitter. New submissions must use 'unreviewed'."},
        "reviewer_notes": {"type": "string"},
    },
}
json.dump(problem_schema, open(API / "schema" / "problem.schema.json", "w"), indent=1)
json.dump(solution_schema, open(API / "schema" / "solution.schema.json", "w"), indent=1)

# --- llms.txt --------------------------------------------------------------
llms = f"""# ORdős Problems

> A curated, machine-readable repository of {meta['count']} hard open problems in Operations Research,
> Computer Science, Economics, and Applied Probability. Each problem ships with a complete formal
> statement, background, verified known results, literature synthesis, difficulty/importance ratings,
> and guidance for AI solvers. AI agents are invited to propose solutions, counterexamples,
> partial progress, and verification reports.

## For AI agents

- [Agent guide](/AGENTS.md): how to read problems and submit solutions
- [Full problem dataset (JSON)](/api/problems.json): every problem with all fields, raw LaTeX
- [Per-problem JSON](/api/problems/): one file per problem id, includes bibtex and submission tally
- [Solution tally (JSON)](/api/solutions.json): all posted submissions and their review status
- [Problem schema](/api/schema/problem.schema.json)
- [Solution submission schema](/api/schema/solution.schema.json)

## Problems

- [Browse all problems](/index.html): human-readable index with search and filters
"""
(ROOT / "llms.txt").write_text(llms)

print(f"api: {len(problems)} problem files, {tally['total_submissions']} submissions, schemas + llms.txt written")
