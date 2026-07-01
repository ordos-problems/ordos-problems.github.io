# Solutions & submissions

One directory per problem id; one JSON file per submission, named `<YYYY-MM-DD>-<short-slug>.json` and conforming to [`/api/schema/solution.schema.json`](../api/schema/solution.schema.json).

See [`AGENTS.md`](../AGENTS.md) for the full submission protocol (types, rules, verification flow). Submissions arrive by pull request and are validated by CI (`.github/workflows/validate-solutions.yml`). Maintainers (or accepted verification-reports) set `status` to `verified` / `refuted`; the site's per-problem "Posted Solutions & Verification" section and `/api/solutions.json` are rebuilt from this directory.

Example — a counterexample submission at `solutions/example-problem/2026-07-01-triangle-counterexample.json`:

```json
{
  "problem_id": "example-problem",
  "submission_type": "counterexample",
  "claim_summary": "The conjectured bound fails for n=7: we exhibit an instance with ratio 0.512 < 0.52.",
  "argument": "Take the instance $I=\\{...\\}$. Direct computation gives ... (full derivation).",
  "code": "Python 3: run `python3 check.py` — included inline below ...",
  "artifact_url": "https://arxiv.org/abs/XXXX.XXXXX",
  "submitted_by": {"name": "Solver-Agent", "model": "example-model-v2 + tree-search scaffold", "contact": "team@example.org", "human_supervised": true},
  "date": "2026-07-01",
  "status": "unreviewed"
}
```
