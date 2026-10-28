# Image-rich crochet pages — installation and image status

This update adds a “See how it comes together” picture gallery and inline photo-guide panels to all six licensed patterns (koala, octopus, sunflower, rose, crocus and hibiscus). The original generated cover illustrations stay intact.

## Install

Use the PATCH ZIP. Back up your existing site, then merge the patch contents into the project root. Only matching files get overwritten; unrelated tutorials and photos remain. Run `npm run build` and then `npm run dev` locally.

## Important image status

- The source photographs are cropped from the user's supplied EPUBs and flower PDF, not AI-fabricated explanations of stitch structure. Photo crops, web-optimized WebP encoding, branded article frames, alt text and captions are included.
- The EPUB step photos are largely watermark-free; source flower photographs **still show publisher watermarks in some crops**. This update does NOT claim to have erased or independently recreated those marks. Because the user reported permission to use images, photos are included for review, but please replace the marked flower crops with clean authorized photos before making the website public if a watermark-free result is required.
- Keep the published stitch instructions as the authority for stitch counts; photos are reference views for the construction stages. They are not a substitute for physically testing the patterns.
- Check that your license/permission covers the photograph reuse and any attribution terms. Only publish without attribution if your permission expressly allows it.

## Updated content

- `src/content/patterns/{koala-bottle-buddy,octopus-potpourri-pal,sunflower-flower-pen,rose-flower-pen,crocus-flower-pen,hibiscus-flower-pen}.mdx`
- `src/content.config.ts`
- `src/pages/patterns/[...slug].astro`
- `src/styles/global.css`
- `public/images/tutorials/` — 28 reference photo crops.

The new photo gallery CSS uses your existing pastel editorial theme variables, so the pages feel closer to the illustrated reference design without replacing your site-wide layout.
