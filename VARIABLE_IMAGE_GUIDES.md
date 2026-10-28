# Full-project heroes + flexible step-photo sequences

## What changed
Every licensed tutorial now shows a full finished-project image **beside its page title**. The older illustrated covers remain available in the pattern-library cards, while the article uses a larger photographic or photo-style project view.

Below the header, image galleries are **variable length**, not fixed at three. Photos and diagrams also appear directly after the instruction section they explain:

- **Sunflower pen:** flower-center and back, leaves, 3 pen sleeve views, 9 pot rounds, soil diagram, final assembly.
- **Rose pen:** 4 rose/petal close-ups, calyx/leaves, pen sleeve, pot rounds, soil diagram, finished piece.
- **Crocus pen:** 3 flower stages, green leaves, pen sleeve, pot rounds, soil diagram, final piece.
- **Hibiscus pen:** 4 petal/center views, green base, pen sleeve, pot rounds, soil diagram, final piece.
- **Koala:** ear finishing, paws and eucalyptus charm photos.
- **Octopus:** arm construction, face embroidery and scented pouch photos.

The number of visuals per section is driven by what is useful for the pattern.

## Image sources & reliability
The four flower-project hero views and other flower images are newly generated photo-style illustrations cropped from compositions created for this blog. They are **not** photographs of actual finished test projects and should not be treated as stitch-by-stitch proof. The pot rounds and green sleeve are likewise illustrated process examples; the stitch tables are authoritative.

For the octopus hero, an unwatermarked finished-project **photograph supplied in the EPUB** is used. Other koala/octopus construction photos are from the user-supplied EPUBs and have not had watermarks erased. The koala hero is a separately generated photo-style illustration.

**No marked flower-PDF photo crops are shipped or displayed.** We used new visuals instead of disguising or editing the book's watermark. For a fully photo-accurate instructional course, add unwatermarked licensed photographs of your physically made project at the corresponding stages.

## Installation
Back up your current project folder. Extract `crochet-variable-image-guide-patch.zip` and drag its contents into your existing Astro project root, merging folders. Windows will ask before overwriting same-name files. Test with `npm run build` followed by `npm run dev`.

No older koala, octopus or original pattern documents are deleted by this patch. The updated templates and `.mdx` files are included; unrelated pages remain untouched. If you edited `src/styles/global.css` or the six tutorial `.mdx` files locally, compare changes rather than blindly replace them.

## Cleaning unused marked assets from an existing installation

If you installed the earlier flower photo patch, those older WebP files may remain in your `public` folder even though the new pages no longer reference them. After making a backup and merging the patch, run from the Astro project root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\remove-obsolete-flower-photos.ps1
```

The script targets only 19 obsolete previously-shipped flower photo crops, not new photos or MDX tutorials. It can be rerun safely.
