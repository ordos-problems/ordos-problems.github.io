# ORdős Problems

A static website collecting hard, unsolved, research-level problems in Operations Research, Computer Science, Economics, and Applied Probability.

The intended problems have relatively clean models and concrete unresolved questions: non-tight guarantees, well-formed conjectures, missing algorithms, missing lower bounds, or unknown structural characterizations. This is not primarily a repository of open-ended modelling questions.

## Website

The site is static and can be hosted directly with GitHub Pages.

- `index.html` is the homepage.
- `problems/` contains the generated per-problem pages.
- `problems.json` is the generated problem database.

GitHub Pages setup:

1. Push this repository to GitHub.
2. Go to repository `Settings -> Pages`.
3. Set source to `Deploy from a branch`.
4. Select the `main` branch and `/ (root)`.

## Source Files

The editable problem source is:

- `build/problems_source.json`

Entries with `"enabled": false` are preserved in source but excluded from the generated website.

Problem enrichments live in:

- `research/enrichment/<problem-id>.json`

These files are merged into `build/problems_source.json` during `npm run build`. Use them for longer background, literature synthesis, progress state, difficulty/importance ratings, and AI-agent guidance without making the main source file harder to review.

Will Ma has approved inclusion of the course-notes problems. Those entries are enabled, retain their `will-ma-notes` source tag, and are also tagged with `contributed by Will Ma`.

The current build scripts are:

- `build/compile.py`
- `build/render_math.js`
- `build/build_site.py`

## Local Preview

You do not need npm to view the website locally. The checked-in files are already static HTML.

Run a simple local server from the repository root:

```bash
python3 -m http.server 4173
```

Then open `http://localhost:4173`.

Using a local server is better than double-clicking `index.html`, because root-relative assets such as `/favicon.svg` behave the same way they will on GitHub Pages.

The contribution and correction forms must be opened through `http://localhost:4173` or the live GitHub Pages site. FormSubmit will reject submissions from `file://` pages opened directly from Finder.

## Rebuild

You only need npm if you are editing the source data or templates and want to regenerate the static site.

The build uses Node only for KaTeX math pre-rendering in `build/render_math.js`. GitHub Pages and local preview do not run Node.

Install dependencies once:

```bash
npm install
```

Rebuild the full static site:

```bash
npm run build
```

## Contributing

Contributions are welcome: new problems, better citations, source corrections, clearer exposition, additional context, or suggestions about scope and organization.

Use the `Contribute` button on the website to open a structured submission form for a new problem. Each problem page also has a `Suggest edit` button that opens a prefilled correction form.

The forms are static HTML forms that post to FormSubmit and send email to `ordos.problems@gmail.com`.

- New problem submissions use the subject tag `[Problem submission]`.
- Problem corrections use the subject tag `[Correction]`.
- The first live submission may require a one-time confirmation email from FormSubmit before messages are delivered.
- In Gmail, filter subjects containing `[Problem submission]` or `[Correction]` to label contribution emails automatically.

Email fallback: `ordos.problems@gmail.com`.

Future community notes, authenticated voting, and reputation features will need either a GitHub-based comments system such as Discussions/giscus or an external backend/database. Static GitHub Pages alone cannot securely store votes, reputation, or arbitrary comments.

## Notes

The bibliography and open-problem descriptions are best-effort and should be verified against primary sources before citation.

### Literature Review

Before changing an entry's status, check the current arXiv landing page and its version history, then read the relevant theorem and model in the current full text. A search snippet or an older version is not sufficient: an earlier claim can be withdrawn while its abstract remains indexed.

Record the version, theorem or section, review date, and scope of the check in a research audit. Distinguish theorem-statement review from independent proof verification. Check the benchmark, arrival order, information available to the algorithm, input encoding, and computational model before transferring a result to an entry. Do not infer that a problem is open solely from an unsuccessful search.

Include relevant new results in `known_results`, `progress`, and the bibliography even when independent proof verification is pending. State the quantitative improvement, assumptions, full author names, paper version, and remaining question. Use `partially resolved` for a genuine residual gap or unresolved variant; a paper claiming the entire target belongs under `solution claimed`, not partial progress merely because it is a preprint. Withdrawn claims are historical context, not current progress.

The November 9 follow-up is recorded in `research/status-audit-followup-2026-11-09.json`. It corrects a withdrawn decision-tree claim and supplements the earlier audit; it is not a certification of every proof in the catalogue.

### Presentation And Checks

The catalogue uses EB Garamond headings, Figtree body text, a pale-yellow light theme, pink controls, and numbered problem cards. Five results appear per page; multiple selected tags use union semantics. Suitability rankings remain in the data for compatibility but are not displayed as the website's organizing principle.

After rebuilding, run the focused regression checks:

```bash
python3 -m unittest discover -s tests
```
