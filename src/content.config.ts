import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const patterns = defineCollection({
  loader: glob({ base: './src/content/patterns', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishedDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    category: z.enum(['Stitch guides', 'Home & decor', 'Accessories', 'Amigurumi']),
    difficulty: z.enum(['Beginner', 'Easy', 'Intermediate']),
    duration: z.string(),
    image: z.string(),
    imageAlt: z.string(),
    tags: z.array(z.string()).default([]),
    supplies: z.array(z.string()).default([]),
    featured: z.boolean().default(false),
    draft: z.boolean().default(false),
  }),
});
export const collections = { patterns };
