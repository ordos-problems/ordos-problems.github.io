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

Send contributions or corrections to `ordos.problems@gmail.com`, or open a pull request once this repository is on GitHub.

## Notes

The bibliography and open-problem descriptions are best-effort and should be verified against primary sources before citation.
