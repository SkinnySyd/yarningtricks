# Two additional illustrated amigurumi tutorial pages

These two pages were added to the existing Astro 5/MDX website:

- `/patterns/koala-bottle-buddy/` — *Koala Bottle Buddy + Eucalyptus Glass Charms*
- `/patterns/octopus-potpourri-pal/` — *Little Octopus Scent Keeper — Crochet Amigurumi*

Content files:

- `src/content/patterns/koala-bottle-buddy.mdx`
- `src/content/patterns/octopus-potpourri-pal.mdx`

Covers:

- `public/images/koala-bottle-buddy.png` and matching editable SVG
- `public/images/octopus-potpourri-pal.png` and matching editable SVG

The pattern schema in `src/content.config.ts` now supports optional `editorialTheme` and `editorialSubtitle`. The tutorial layout (`src/pages/patterns/[...slug].astro`) has a new page intro and anchor navigation for these themed pages; their personalized styling is appended to `src/styles/global.css`. Existing tutorials and routing remain unchanged.

## To view

1. From this folder run `npm install` if dependencies are not present.
2. Run `npm run dev`.
3. Open the two URLs shown above on `http://localhost:4321`.
4. Run `npm run build` before deploying, and check the resulting pages.

## Before you publish

**Publication rights and brand:** The site owner has stated that their permission allows these two adapted crochet patterns to be published under the blog's own branding. Accordingly, the public-facing tutorial pages no longer include source-credit callouts. Keep a copy of the actual permission terms, and comply with any contractual restrictions (including attribution, trademark, modifications, or advertising requirements) that apply. The two tutorial pages retain their detailed stitch sequences and newly written editorial presentation; permission to republish does not itself establish authorship of the underlying patterns. The source publication's illustrations were not copied into this project.

**Accuracy:** Round counts and placement details were cross-checked against the supplied EPUB text, but neither project has been physically crocheted or pattern-tested in this environment. Test with yarn before offering these as final instructions.

**Brand:** Pages automatically use the site name and author configured in `src/site-config.ts`. The included covers currently say **Thread & Petal**, the starter site’s sample brand. If your real brand name differs, change the cover SVG text, re-export the PNG covers, and update `src/site-config.ts`, header, footer and social cover before launch.

**Privacy and advertising:** No AdSense setup was changed. Configure privacy, consent and ads only when ready and approved.
