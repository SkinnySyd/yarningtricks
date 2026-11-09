# Thread & Petal · main-domain migration + content review

Prepared on **9 November 2026**, using the current public `SkinnySyd/yarningtricks` GitHub **main** source at commit `5f0af5313898ad39610137893304cf9a61e3a0f8`.

**Primary domain:** `https://threadnpetal.blog` (no `www`).

This ZIP contains **standalone scripts and reports only**. It does not replace any existing `.astro`, `.mdx`, image, or shared component file. The scripts make targeted edits to files **in your own checkout** only when explicitly run with `--apply`. There are no GitHub, Spaceship, Cloudflare, or Google account changes in this ZIP.

## Step 1 — finish the Astro migration

1. Extract the ZIP. Copy the four `.py` files beside the `package.json` file of your local Thread & Petal repo.
2. In that repository folder, run:

```bash
python3 apply_migration.py
python3 apply_migration.py --apply
```

On Windows, substitute `py` for `python3`.

3. Review changed files with `git diff`. This script targets **six** existing files:

| File | What the script does |
|---|---|
| `astro.config.mjs` | Changes the fallback Astro `site` to `https://threadnpetal.blog` |
| `src/site-config.ts` | Changes the contact email to `contact@threadnpetal.blog` (**must be tested** before publishing) |
| `src/pages/privacy.astro` | Changes old-domain links and updates its review date and email-service description; read the whole policy for factual accuracy |
| `src/pages/learn/[slug].astro` | Changes the hardcoded LearningResource structured-data provider URL |
| `.env.example` | Documents the new `SITE_URL` and optional AdSense ownership-verification ID |
| `src/layouts/BaseLayout.astro` | Adds optional `google-adsense-account` verification meta tag, **without enabling ad serving** |

Do not change DNS records with this script. It does not affect any crochet pattern, pictures, or `StitchHelp.astro`.

4. **Before deploying**, send a real test email to `contact@threadnpetal.blog` from another mailbox. The MX/TXT records in the Cloudflare screenshot are not proof that the address has a working route. If email is not ready, configure a working address in `src/site-config.ts` first.
5. Review `src/pages/privacy.astro`: the file says the operator is an individual based in Morocco and mentions Cloudflare Web Analytics. Keep those statements only if accurate; update them if your actual operation/services differ. The code patch cannot know this.
6. Test, commit, and deploy:

```bash
npm ci
npm run check
npm run build
git diff --check
```

Then commit/push through your normal GitHub workflow.

7. In **Cloudflare's production build environment** (not just Worker runtime secrets), set `SITE_URL=https://threadnpetal.blog`, and trigger a **new build**. That variable takes precedence over the fallback in `astro.config.mjs`.

## Step 2 — verify the deployed apex domain

Run:

```bash
python3 check_live_site.py
```

This requests the home page, pattern library, learn, journal, About, Privacy, two newer patterns, robots, sitemap and RSS. It reports old-domain canonical links and `noindex` signals. The check needs working Internet access on **your** computer. It cannot be run against an unconnected custom domain.

Manually check HTTPS and images from your phone and desktop. Inspect a pattern page's source for `<link rel="canonical" href="https://threadnpetal.blog/...">`.

The `www` hostname is optional for your preferred canonical address; if it still has a DNS issue, **do not point canonical tags at `www`**. You can troubleshoot its redirect separately. The primary `https://threadnpetal.blog/` must itself be reachable for the AdSense review.

If the old `.com` domain is still yours, permanently redirect **each old path to the matching new path** and use Search Console Change of Address when eligible. If you no longer control `.com`, redirects cannot be installed there; update any Pinterest/profile links you control.

## Step 3 — review and improve the articles

Read `CONTENT_REVIEW.md` for the actual audit results.

For a quick repository source check run:

```bash
python3 audit_content.py
```

Seven adapted patterns are missing a concise designer credit at the bottom. To add credits **without touching any crochet rounds**:

```bash
python3 optional_add_credits.py
python3 optional_add_credits.py --apply
```

Review `git diff` after running. This optional script changes **only those seven MDX files**. It does not add a designer credit to any image, edit the common page layout, or claim you own the original designs.

**Important:** Crediting a designer is not a substitute for permission. Confirm the right to adapt and monetize each relevant source design. Stop presenting the **Woodland Panda** as a complete tested pattern until missing hind-leg Round 23 is verified; if it cannot be verified, temporarily set `draft: true` in that MDX frontmatter.

## Step 4 — only then set up Google

- Create or verify a **Google Search Console Domain property** for `threadnpetal.blog`, add its DNS TXT verification record in Cloudflare, and submit `https://threadnpetal.blog/sitemap-index.xml`.
- Check that at least the homepage, About, Privacy, one Learn lesson, and several patterns have no indexing or crawl errors.
- Add the site in AdSense when reachable and content-reviewed. If the AdSense account offers **meta-tag ownership verification**, enter **the actual** `ca-pub-...` ID as Cloudflare's **production build** environment variable `PUBLIC_ADSENSE_VERIFICATION_ID`; redeploy. This inserts the ownership meta tag via the patch. Never invent an ID.
- Keep `PUBLIC_ENABLE_ADS=false` until your site has approval and the required privacy/consent setup. Update the Privacy Policy before turning on ads. Use AdSense's exact ads.txt record when provided.

**No arbitrary pattern count or fixed traffic number guarantees approval.** Google evaluates content quality, accessibility, and compliance.

Official guidance:
- https://support.google.com/adsense/answer/9724
- https://support.google.com/adsense/answer/7299563
- https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
- https://support.google.com/webmasters/answer/9370220
