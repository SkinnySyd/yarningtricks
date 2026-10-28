# Pumpkin Halloween Candy Bag — Astro page update

Adds a dedicated pumpkin candy bag tutorial to your existing Astro pattern library. The pattern includes an actual finished-project photo at the top and stage-specific visual guides, rather than a fixed number of gallery images.

## Install

1. **Back up your existing project folder** first.
2. Open `crochet-pumpkin-bag-page-patch.zip` and drag the **contents** (`src/` and `public/`) into your current Astro project's root folder.
3. Windows will merge those folders. Select **Replace** only for `src/content.config.ts` and `src/styles/global.css` after checking for your custom changes; only those two existing files need replacing in the patch. All other files are new.
4. In a terminal within your project: `npm run dev`, then visit `http://localhost:4321/patterns/pumpkin-halloween-candy-bag/`.
5. Before publishing, run `npm run build`.

## What is in the page

- Full-project photographed bag beside the article title, plus an extra finished-bag view.
- Six original teaching illustrations for base, ribbing, narrowing, rim, handle and assembly.
- Materials, hook size, size, full original stitch counts (foundation through round 22), handle rows 1–4 and sewing instructions.
- Source author and photo credit retained in the article; please verify that your use rights cover this distinct source, before publishing.

## Content integrity

The PDF/EPUB source spells out some FPdc placement/repeats very tersely, potentially ambiguously. The article preserves the printed sequence and printed totals instead of inventing corrections. **Test the construction physically before publishing as a validated pattern.** The diagram images are explanatory, not proof of the exact stitch counts.

## Design notes

This change adds `pumpkin` to the theme enum and scoped CSS for an orange autumn theme. It does not alter the site title or brand settings (`src/site-config.ts`).

## Build validation

Frontmatter and all image paths were checked. `npm install`/`npm run build` could not be run here due to npm registry DNS issues (EAI_AGAIN). Run the production build on your computer before publishing.
