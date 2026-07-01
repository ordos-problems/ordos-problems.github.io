# ORdős enrichment schema (v2) — contract for research agents

Every enrichment file lives at `research/enrichment/<problem-id>.json` (staging). New problems live at `research/new/<problem-id>.json`. Files MUST be valid JSON (validate with `python3 -m json.tool` before finishing). Math uses `$...$` and `$$...$$` delimiters ONLY (KaTeX-rendered; never `\(...\)`). Escape backslashes properly in JSON (`\\mathbb`, `\\le`).

## Enrichment file fields (for existing problems)

```json
{
  "id": "<problem-id>",                    // REQUIRED, must match
  "background": "...",                      // REQUIRED. 150–400 words LaTeX prose. History, motivation, why the problem matters, the model context, connections to practice/other fields. Written for a strong grad student meeting the problem for the first time. Do NOT restate the formal problem; set the stage for it.
  "short_statement": "...",                 // optional improvement (1–3 sentences, plain-ish English)
  "full_statement": "...",                  // optional improvement. Complete, self-contained formal model + precise question. All notation defined.
  "known_results": "...",                   // REQUIRED. Updated & verified via web search as of 2026. Best bounds with authors+years, key special cases resolved, barriers.
  "status": "open|partially resolved|solution claimed|conjecture|resolved",  // REQUIRED, verified via search
  "where_posed": {                          // REQUIRED (improve existing)
    "text": "Stated in Author, 'Title', Year, Venue.",
    "url": "...",
    "quote": "verbatim sentence(s) from the source posing the problem, if findable",  // "" if not found
    "location": "e.g. Section 6, Open Problem 2 / p. 34"                              // "" if not found
  },
  "progress": {                             // REQUIRED
    "state": "none|partial|solution-claimed|resolved",
    "summary": "1–4 sentences on the latest progress incl. 2024–2026 work; empty string if none",
    "links": [{"title": "...", "url": "..."}]
  },
  "importance": 7,                          // REQUIRED int 1–10 (centrality to field, breadth of consequences)
  "difficulty": 8,                          // REQUIRED int 1–10 (10 = decades-old, resisted many attempts)
  "counterexample_suitability": "low|medium|high",   // REQUIRED: could the question plausibly be resolved by an explicit finite counterexample/construction found by search?
  "counterexample_rationale": "1–3 sentences",
  "alphaevolve_suitability": "low|medium|high",      // REQUIRED: could an evolutionary code/search loop (AlphaEvolve-style) make progress, e.g. by discovering constructions, gadgets, or improved constants?
  "alphaevolve_rationale": "1–3 sentences",
  "literature": {                           // REQUIRED
    "synthesis": "150–300 words LaTeX prose synthesizing the state of the art: main lines of attack, best current bounds and who proved them, what the remaining gap is, where new ideas seem needed.",
    "reviewed": [                           // 3–6 key papers, found/verified via search
      {"ref": "Author(s), 'Title', Venue Year", "result": "what it proves, with exact bounds where possible", "relevance": "partial-progress|solves-special-case|hardness|related-tool|survey", "url": "..."}
    ]
  },
  "agent_guidance": {                       // REQUIRED — for AI solvers
    "suitable_approaches": "2–4 sentences: plausible attack routes (LP/factor-revealing, coupling, primal-dual, explicit construction, exhaustive small-case search, ...)",
    "verification_notes": "What a correct solution must contain and how a referee/verifier agent should check it (key lemmas to verify, common failure modes, whether numerics suffice or a proof is required).",
    "machine_checkable": false               // true only if a candidate answer (e.g. counterexample, construction, or numeric certificate) could be verified by running code
  },
  "additional_refs": [ ... ],               // optional: merged list (keep existing + add new important ones)
  "tags": [ ... ],                          // optional expanded tag list
  "notes_for_maintainer": ""                // flags: e.g. "recently solved — see arXiv:XXXX", or uncertainty about a claim
}
```

## New-problem files (research/new/<id>.json)

All fields above PLUS the base fields: `id` (kebab-case slug), `title`, `collection` (one of: Operations Research, Operations Management, Management Science, Applied Probability, Computer Science, Online Algorithms & Learning, Market & Mechanism Design, Approximation & Discrepancy, Economics), `area`, `tags`, `confidence` ("high" when the statement and open status are verified against the primary source; otherwise "medium"), `short_statement`, `full_statement`, `source` `{authors,title,year,venue,url}`, `additional_refs`, `enabled: true`, and `contributor` when applicable (e.g. "Will Ma").

## Quality bar (matched to pranav-nuti.github.io/open-problems-in-or)

- The `full_statement` must be a complete model a solver could work from with zero outside context: every symbol defined, the objective/benchmark explicit, the precise open question stated.
- `known_results` and `literature.synthesis` must reflect a real 2026 web check, not memory alone. Cite authors + venue + year.
- Prefer primary sources (arXiv, DOI, conference pages) for URLs. Never invent citations: if unsure a paper exists, leave it out.
- If the problem may have been recently resolved, set status/progress accordingly and flag in `notes_for_maintainer`.
