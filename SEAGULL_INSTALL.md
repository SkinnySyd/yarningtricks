# Thread & Petal — Seaside Seagull article patch

## What this contains

- `src/content/patterns/seaside-seagull-amigurumi.mdx`: a complete, editorially rewritten amigurumi pattern adapted from the Scraps the Seagull pattern by Crochetbykim in Zoomigurumi 7 (2018)
- `src/components/StitchHelp.astro`: your existing pattern-to-lesson component, with a new seagull entry
- `public/images/finished-projects/seaside-seagull-amigurumi.webp`: original AI-generated seaside-style hero visualization, cropped from an original generated composition
- `public/images/tutorials/seaside-seagull-amigurumi/seagull-profile.webp` and `seagull-back.webp`: AI-generated styling angles, **not** process photographs or stitch-accuracy references

## Install

1. Copy the contents of this ZIP into the root of your latest Astro project, preserving the paths.
2. Allow the existing `src/components/StitchHelp.astro` to be overwritten (the original entries were preserved; the new pattern was appended).
3. Do **not** remove or change any of the current `src/pages/patterns` files or existing image assets.
4. Run `npm ci`, `npm run check`, `npm run build`.
5. Commit and deploy to Cloudflare Pages. The new route should be `https://threadnpetal.com/patterns/seaside-seagull-amigurumi/`.
6. Check the gallery and hero on desktop/mobile; test the pattern-to-lesson links and Pinterest save URL.

## Editorial, copyright, and reliability notes

- The article retains the original design credit and identifies the book and publisher. Thread & Petal's owner has stated that adaptation, publication, and newly generated image reinterpretation were permitted. **Keep a written license or permission record** that confirms which rights holder(s) approved this, the image-derivative permission, and whether the website may be monetized.
- Stitch counts, hook size, material colors, source size and piece construction are based on the original book's printed pattern on pp. 28-30. The book classifies this pattern as easy. The article's new explanations and layout are editorial additions.
- The publisher's photographs and original instructional diagrams are not included. The new illustrations are explicitly labeled as AI visual concepts. They may not depict every stitch, seam or dimension precisely.
- The user-facing article does not claim that Thread & Petal personally test-crocheted the finished design. Have a crocheter physically test the written instructions and replace any mismatching images before treating the tutorial as a tested pattern.
- The original printed text uses the word "row" for the wing attachment at 24, despite the shape being worked in continuous rounds. The article explains that it treats this as **round 24**.
- Source pattern describes a continuous head/body, one beak, two wings, two legs, and two tail feathers. The AI images are styling artwork, and the final toy's feet can look different from these images.
- This patch **does not modify GitHub**; copy the files into your own repository and push after review.
