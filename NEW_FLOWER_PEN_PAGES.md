# Four Flower Pen tutorials — website update

This update adds **four separate tutorials** (sunflower, rose, crocus, and hibiscus) from the user-supplied *Knotmonsters Flower Pens Edition* excerpt (printed book pages 55–82). The website prose is rewritten, stitch sequences/counts are retained from the provided source, and the four cover illustrations were newly created for the website. The original book photographs and their embedded watermarks **were not copied, stripped, or manipulated**.

## Routes

- `/patterns/sunflower-flower-pen/` — sunflower flower pen
- `/patterns/rose-flower-pen/` — rose flower pen
- `/patterns/crocus-flower-pen/` — crocus flower pen
- `/patterns/hibiscus-flower-pen/` — hibiscus flower pen

## Files

- `src/content/patterns/{sunflower,rose,crocus,hibiscus}-flower-pen.mdx`
- `public/images/{sunflower,rose,crocus,hibiscus}-flower-pen.png`
- `src/content.config.ts` — extends difficulty/theme fields
- `src/styles/global.css` — custom color themes

## Use

Unzip the patch at the project root, replacing the two existing configuration/style files; run `npm run dev` then `npm run build`.

## Content QA before publication

- User says they have permission to republish/monetize this source. Confirm its precise scope and keep a record.
- The source uses the undefined term **puff stitch** in the sunflower and doesn't specify how many loops/yarn-overs it involves. We do not invent this count; add a tested definition if needed.
- All four feature the same pot, soil, and 8 mm pen-cover construction; tailor the sleeve to the pen.
- The time ranges are editorial estimates, not supplied by the source. Some shaping instructions in the original (such as the exact placement of stitch joins, and the crocus leaf) are concise. **Crochet a physical sample and check the stitch counts and stability** before posting as a tested pattern.
- Each page uses newly drawn editorial art, not a photographic representation of a finished, tested sample. Replace or supplement with your own process photos when available.
- The current site name remains whatever is configured in `src/site-config.ts` (the starter ships with a sample name); update it to your real brand before going live.
