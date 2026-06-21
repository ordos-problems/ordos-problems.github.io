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

Entries with `"enabled": false` are preserved in source but excluded from the generated website. The Will Ma course-notes problems are currently disabled this way pending permission; setting them back to `"enabled": true` will include them in the next rebuild.

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
