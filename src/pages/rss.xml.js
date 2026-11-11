import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { siteConfig } from '../site-config';

export async function GET(context) {
  const [patterns, journal] = await Promise.all([
    getCollection('patterns', ({ data }) => !data.draft),
    getCollection('journal', ({ data }) => !data.draft),
  ]);
  const items = [
    ...patterns.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.publishedDate,
      link: '/patterns/' + post.id + '/',
    })),
    ...journal.map((article) => ({
      title: article.data.title,
      description: article.data.description,
      pubDate: article.data.publishedDate,
      link: '/blog/' + article.id + '/',
    })),
  ].sort((a, b) => b.pubDate.valueOf() - a.pubDate.valueOf());
  return rss({
    title: siteConfig.name,
    description: siteConfig.description,
    site: context.site,
    items,
  });
}
