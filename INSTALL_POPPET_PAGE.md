# Thread & Petal — Crochet Poppet Doll tutorial

This patch adds **one** Astro MDX crochet tutorial and its artwork to the existing `threadnpetal.com` project. It does not delete your other patterns.

## Files included

- `src/content/patterns/crochet-poppet-doll.mdx` — complete pattern, photo-led instructions, stitch tables, friendly introductory copy, FAQs, personalization and care notes
- `src/content.config.ts` — adds `poppet` to the list of supported tutorial themes
- `src/styles/global.css` — adds the new poppet theme and responsive photo gallery styles
- `public/images/tutorials/crochet-poppet-doll/` — finished-project photo and user-provided process-photo crops

## Install on Windows

1. Copy your current `crochet-blog-starter` project folder to a backup location.
2. Unzip this patch. Copy its **contents** (the `src` and `public` folders) into the root of your existing Astro project.
3. Allow Windows to **merge folders**. When asked to replace existing files, carefully review changes to `src/content.config.ts` and `src/styles/global.css` if you have customized them.
4. Run `npm run build` to check your production build, and `npm run dev` to preview locally.
5. Visit `http://localhost:4321/patterns/crochet-poppet-doll/`.
6. When satisfied, commit the changes and push to GitHub, which can trigger your Cloudflare Pages deployment.

## Technical/source notes

- Crochet pattern source: **Crocheted Poppet**, Project 26, from *Fiber Magick* by **Opal Luna** (user-provided PDF). This adaptation uses its head-and-body rounds, four independently crocheted limbs, and decorative elements. It has **not been physically tested**.
- The supplied step-photo collage shows some alternative construction details (particularly the legs), while the printed pattern sews **four separate limbs** to one head-and-torso piece. The page explicitly calls this out so a crocheter can follow the written stitches.
- The written PDF specifies an **8-inch** project, **5 mm hook**, and **4 oz / 208 yd 4-ply yarn**. Time is not given, so the page does not invent a fixed completion time.
- The user-supplied finished image is used as the full-project hero. The step-photo collage is split into cropped reference images; there are no new, artificial stitch-count "photos."
- Confirm you have permission to republish this particular *Fiber Magick* pattern before making the page public. Permissions from other pattern creators do not automatically apply.
- Button eyes and other small embellishments can be unsafe for young children. Prefer embroidery for toys given to children.

## Preview

The separate `poppet-pattern-page-preview.html` is an independent *design preview* of the visual direction. The actual Astro page is the MDX file in this patch and uses your blog's existing layout.
