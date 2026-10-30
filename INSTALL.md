# Thread & Petal — Beginner patterns + two-way learning links

**Prepared against:** `SkinnySyd/yarningtricks`, `main`, commit `a2ef99bb67fe1fc72d8597e0460c9ca664f3be6c` (2026-10-30).

## What changes

- `src/content/patterns/first-crochet-chain.mdx` — fuller slip-knot, chaining, V-count and troubleshooting instructions; direct link from course step 2 to **single crochet (step 3)**.
- `src/content/patterns/simple-yarn-bookmark.mdx` — explicitly explains 26 foundations chains → 25 single crochets, which turning chain doesn't count, and consistent five-row count.
- `src/content/patterns/granny-square-coaster.mdx` — clarifies joining the rounds, traveling to the next corner with slip stitches, the chain-3 convention, and cluster/corner counts.
- `src/content/patterns/crochet-flower.mdx` — clarifies five complete petal repeats, magic-ring finishing, and troubleshooting.
- `src/components/StitchHelp.astro` — NEW reusable contextual links for all 12 existing patterns (the other 8 patterns' instructions are unchanged).
- `src/pages/patterns/[...slug].astro` — imports StitchHelp, places a lesson-help panel after supplies, and removes the outdated sample-template message.

All URLs, category metadata, image paths and original publication dates are retained. The four updated patterns have `updatedDate: 2026-10-30`.

## Install

1. Copy the included `src/` folder into the root of your local Astro project, keeping its folders. Replace the existing pattern/tutorial files and create the new `StitchHelp.astro` component.
2. Verify that your current repo already contains the Learn Crochet Hub at `/learn/` and nine lessons (it did at the commit checked).
3. Run `npm ci`, `npm run check`, and `npm run build`.
4. Preview the chain tutorial `/patterns/first-crochet-chain/`, the bookmark, granny-square coaster, tiny flower, and one advanced pattern such as `/patterns/koala-bottle-buddy/`.
5. Confirm a pattern's **Stuck on a stitch?** links open real lessons, and that the chain tutorial's **Continue to Lesson 03** link works.
6. Commit/push the files and check Cloudflare Pages' build status.

## Editorial and publishing notes

This is an **editorial/code review** of the four provided sample patterns, with their original stitch construction retained except for clarity and ordering of joined-round actions. I checked stitch terms, counts and link destinations against the source and standard crochet terminology, but **I have not physically crocheted/tested** the projects. Have a crocheter make each project exactly as written before calling any pattern 'tested'. The four original artwork files are still illustrations, not new photos.

The new help panel is intentionally **contextual**, not a redirect. Readers can click to the lesson when needed and return to the pattern using their browser's Back button. The site already has links from many lessons back to practice patterns.

## Rollback

Restore the original four MDX files and `src/pages/patterns/[...slug].astro` from GitHub, and delete `src/components/StitchHelp.astro`.
