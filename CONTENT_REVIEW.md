# Thread & Petal — Content-quality audit

**Repository scanned:** `SkinnySyd/yarningtricks`, `main` @ `5f0af5313898ad39610137893304cf9a61e3a0f8` (8 November 2026). Review prepared 9 November 2026. This is a **source-code audit, not a live crawl, test crochet, copyright license review or guarantee of AdSense acceptance**.

## What looks good

- **24 pattern articles** under `src/content/patterns/` and **9 standalone lessons** under `src/content/lessons/`.
- All 24 patterns have a metadata frontmatter block and local article image references resolve to files in the repository in the scan.
- No Git conflict markers found in the 24 pattern articles.
- The 9 lesson MDX articles have their internal pattern/lesson links pointing to existing source slugs (20 links scanned).
- Responsive site scaffolding has **Home, Patterns, Learn, Journal, About, Privacy, contact footer link, RSS, robots/sitemap generation, SEO and schema markup**.
- The latest checked Cloudflare build status was **successful**; that does not prove that the new `.blog` domain is accessible or properly indexed.
- Existing display advertising is **off by default** (`PUBLIC_ENABLE_ADS=false`). Keep it off while preparing for review.

## Prioritized issues

### P0 — Main-domain identity and public accessibility

`astro.config.mjs`, `src/pages/learn/[slug].astro`, `src/pages/privacy.astro`, `src/site-config.ts`, and `.env.example` still contain `.com` or old placeholder host values at this commit. Deploy the accompanying domain patch, **set the Cloudflare production BUILD variable `SITE_URL` to `https://threadnpetal.blog`**, redeploy, and verify actual page-source canonicals and sitemap URLs. The screenshot of DNS records does not prove live HTTPS or indexing. `www` is a separate redirect problem; the canonical apex website should work without it.

### P0 — Incomplete Panda construction

`src/content/patterns/woodland-panda-amigurumi.mdx` explicitly says: **“The source skips Round 23 after Round 22; this gap has not been invented or assumed here.”** This is responsible reporting, but the published crochet instructions remain incomplete. Confirm the missing round with the designer/source or temporarily switch its frontmatter to `draft: true` and hide it. **Do not infer its missing stitches.**

### P1 — Provenance, commercial permissions and editorial value

Seven adapted articles end without the short source-designer credit line used elsewhere:

1. `autumn-ember-red-panda-amigurumi.mdx` — Rusty the Red Panda, Josephine Wu, *Zoomigurumi 3*.
2. `cloudberry-lamb-amigurumi.mdx` — Cuddles the Lamb, Little Muggles/Amy Lin, *Zoomigurumi 3*.
3. `heather-highland-cow-amigurumi.mdx` — Hilda the Highland Cow, Moji-Moji Design/Janine Holmes, *Zoomigurumi 9*.
4. `meadow-gazelle-amigurumi.mdx` — Audrey Gazelle, Yan Schenkel, *Animal Friends of Pica Pau*.
5. `milo-woodland-moose-amigurumi.mdx` — Monty the Moose, LittleAquaGirl, *Zoomigurumi 7*.
6. `splashy-frog-amigurumi.mdx` — Víctor Frog, Yan Schenkel, *Animal Friends of Pica Pau*.
7. `winter-wanderer-reindeer.mdx` — Noel the Reindeer, Hello Yellow Yarn/MJ Carlos, *Zoomigurumi 7*.

An optional, idempotent script in this ZIP can add those **seven footer lines only**, with no changes to the pattern instructions. Other source-based pages (e.g., Toucan and Seagull) include attribution in body text, but check consistent crediting across the whole site. Attribution is not itself a copyright permission or a guarantee of 'original content' under Google's standards. Keep your actual written publication/monetization permissions privately documented.

The beginner lessons and adapted patterns could benefit from more demonstrable original value: **real step photos of the maker's hands or clear illustrated stitch diagrams, tips from actual test-crochet results, specific yarn quantities where known, difficulty notes and meaningful troubleshooting**. Do not claim a pattern was physically tested unless it was. Image renders are illustrations, not evidence of physical tests.

### P1 — The Journal duplicates the Pattern Library

`src/pages/blog/index.astro` currently calls `getCollection('patterns')` and renders the same `PatternCard` items used on `/patterns/`. This is functional navigation but little distinct editorial value. After the domain migration stabilizes, make Journal a real educational section with original projects or standalone essays, such as:

- **Choosing yarn and a hook for amigurumi:** fiber tradeoffs, stitch density, real swatch comparisons, sizing.
- **Stuffing and closing crochet animals:** where to add stuffing, facial alignment, weak seams and secure finishing.
- **Fixing uneven rounds and color changes:** counted examples, photos of actual mistakes, checklists.

Keep the pattern library as the collection of patterns; don't publish duplicate rewritten copies of them just to increase post count.

### P2 — Short starter pages and lessons

Most of your recent patterns are detailed. Four older starter patterns are relatively brief (about **537–673** words): `crochet-flower`, `simple-yarn-bookmark`, `first-crochet-chain`, and `granny-square-coaster`. The nine standalone lesson files are roughly **488–754 words** each. Short instructions are not inherently low quality; prioritize **completeness, step visuals and usefulness**, not a word-count quota. Expand only where an actual beginner question or missing step warrants it.

### P2 — About, Privacy, contact and transparency

- Confirm that the About/Privacy descriptions accurately describe the real website operator and location. The current Privacy Policy names an individual in Morocco; **do not retain that claim if it isn't accurate**.
- The Privacy Policy mentions Cloudflare Web Analytics and Email Routing; verify those features are really configured in your current domain account.
- Test the address that appears in the site's footer (`contact@threadnpetal.blog` after migration). The DNS MX records alone do not prove forwarding works.
- Update cookie/privacy disclosures and use an appropriate Google-certified CMP for regulated traffic before enabling advertising. Leave ads off until then.
- `src/site-config.ts` currently has no Pinterest profile URL. Optional for AdSense but useful for brand trust and linking social Pins back to your site.

## Recommended order

**First:** deploy new-domain code, configure build-time `SITE_URL`, test email and actual site. **Second:** verify the Panda round, add missing credits, audit permissions and proofread instructions. **Third:** create genuinely distinct Journal content and improve any thin or unclear tutorials. **Fourth:** verify domain ownership and sitemap in Search Console, then apply for AdSense.

Official guidance:
- https://support.google.com/adsense/answer/7299563
- https://support.google.com/adsense/answer/9724
- https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
