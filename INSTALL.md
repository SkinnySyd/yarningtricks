# Thread & Petal — Learn Crochet Hub

A drop-in Astro 5/MDX patch prepared against the `main` branch of `SkinnySyd/yarningtricks`, commit `eb17e36e461f7f35f89120ae32d3d03d37805d1c` (last checked October 30, 2026).

## What it adds

- **Redesigned `/learn/` hub**: a welcoming photo/illustration hero, 10-step sequence, US/UK terms reference, three existing practice projects and FAQ.
- **Nine complete new lesson pages** at `/learn/<lesson-slug>/`; the existing `/patterns/first-crochet-chain/` is lesson 2 of the sequence, to avoid creating a duplicate post.
- **Original loop-count diagrams** for US single, half double, and double crochet. These are explicitly *schematic*, not substitute photographs of hand positions.
- **Reusable MDX lesson collection**, one dynamic lesson layout, responsive styles, table of contents, next/previous navigation, and LearningResource JSON-LD.

## Install: copy these paths into your project root

```
src/content.config.ts                          (REPLACE current version)
src/pages/learn.astro                          (REPLACE current version)
src/pages/learn/[slug].astro                   (NEW)
src/content/lessons/*.mdx                      (NINE NEW)
public/images/learn/*.svg                      (THREE NEW)
```

The patch does **not** overwrite `src/pages/index.astro` or your homepage redesign, About/Privacy pages, or existing crochet patterns.

### Local test and deploy

1. Save/backup any local edits to the two replaced files.
2. Extract the ZIP at the **root** of your Astro project, keeping its directory structure. Do not copy `INSTALL.md` or the generator into `src/`.
3. Run `npm ci`, then `npm run build`. If the build succeeds, optionally run `npm run preview` and open `/learn/` and three new lessons.
4. Check `/learn/` on desktop and mobile. Test the links from lessons back to `/patterns/` and the pattern filters.
5. Commit and push to GitHub; Cloudflare Pages should deploy from your connected branch as normal.

## Important editorial review before publication

- Crochet directions are original educational prose checked against Craft Yarn Council terminology; they are **not physically test-crocheted**. Review or test step counts, yarn/material suggestions, and wording before treating as fully verified patterns.
- The existing `/patterns/first-crochet-chain/` still comes from the site's initial short starter tutorials and currently carries a **sample tutorial warning** shared with three other starter pages. Revise/test these four original patterns and then remove the warning when appropriate. This patch intentionally does not hide it.
- Source diagrams illustrate loop counts only, **not physical stitch anatomy or hook placement**. Add your own technique photos if available later.
- We don't create a fake newsletter, login system, course progress tracker, or third-party embeds. The hub contains static educational content and does not introduce analytics or advertising scripts.

## Useful reference links

- Craft Yarn Council standard crochet abbreviations / US–UK equivalents: https://craftyarncouncil.com/node/31
- Crochet hook conversion (millimeters): https://craftyarncouncil.com/standards/hooks-and-needles
- Craft Yarn Council single crochet technique: https://www.craftyarncouncil.com/node/461

## Updated pages/URL listing

- `/learn/`
- `/learn/crochet-supplies-for-beginners/`
- `/patterns/first-crochet-chain/` (existing, lesson 2)
- `/learn/single-crochet-stitch/`
- `/learn/half-double-crochet-stitch/`
- `/learn/double-crochet-stitch/`
- `/learn/crochet-straight-edges/`
- `/learn/magic-ring-crochet-in-the-round/`
- `/learn/crochet-increases-and-decreases/`
- `/learn/how-to-read-crochet-patterns/`
- `/learn/fix-crochet-mistakes-and-finish/`
