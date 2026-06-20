# Ordos Problems

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

The editable problem sources are:

- `build/mig_online_market.json`
- `build/mig_stoch_approx_notes.json`
- `build/new_om_or_ms.json`

The current build scripts are:

- `build/compile_v2.py`
- `build/render_math.js`
- `build/build_site_v3.py`

## Rebuild

Install dependencies once:

```bash
npm install
```

Rebuild the full static site:

```bash
npm run build
```

Preview locally:

```bash
npm run serve
```

Then open `http://localhost:4173`.

## Contributing

Contributions are welcome: new problems, better citations, source corrections, clearer exposition, additional context, or suggestions about scope and organization.

Send contributions or corrections to `akshitkumar100@gmail.com`, or open a pull request once this repository is on GitHub.

## Notes

The bibliography and open-problem descriptions are best-effort and should be verified against primary sources before citation.
