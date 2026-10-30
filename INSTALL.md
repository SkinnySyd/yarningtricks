# Thread & Petal — Editorial Homepage Redesign

## Install

1. Extract this ZIP into the root of your Astro repository (`SkinnySyd/yarningtricks`).
2. Replace **only** `src/pages/index.astro` with the included file.
3. No changes to `global.css`, content schemas, other pages, or images are needed.
4. Run `npm ci` then `npm run build` in your project.
5. Visit the homepage on desktop and mobile; click the category filters and all featured pattern links.
6. Commit and push to `main` after reviewing.

## What's new

- Editorial home hero showing **existing finished-project photos**, not stock art.
- Featured six patterns selected from actual published MDX entries.
- Four clickable category tiles, including Amigurumi; counts reflect published content.
- Four-flower pen showcase with dedicated tutorial links.
- Three-step beginner welcome and a clear link to `/learn/` (no unbuilt lesson routes).
- Global, brand-centered welcome that doesn't invent a team or founder biography.
- Responsive layouts, descriptive image alt text, lazy loading below the fold, and reduced-motion support.
- Self-contained page styling scoped in `src/pages/index.astro`.

## Notes

- This patch does **not** change content, pattern correctness, photos, site analytics, legal disclosures, or ad settings.
- Photos are sourced from existing `public/images/...` repository files. Some source project imagery is edited or stylized; no photos are presented as independently verified original craft photography.
- No live deployment was changed.
