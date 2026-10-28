import rss from '@astrojs/rss';
import {getCollection} from 'astro:content';
import {siteConfig} from '../site-config';
export async function GET(context) {
 const posts = (await getCollection('patterns', ({data})=>!data.draft)).sort((a,b)=>b.data.publishedDate.valueOf()-a.data.publishedDate.valueOf());
 return rss({title:siteConfig.name,description:siteConfig.description,site:context.site,items:posts.map((post)=>({title:post.data.title,description:post.data.description,pubDate:post.data.publishedDate,link:`/patterns/${post.id}/`}))});
}
