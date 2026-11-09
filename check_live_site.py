#!/usr/bin/env python3
"""Run on your own computer after DNS/deployment to check the new domain's public URLs.
Uses only Python standard library. Does not log into or configure any service.
"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from html.parser import HTMLParser
import sys

BASE='https://threadnpetal.blog'
PATHS=[
    '/', '/patterns/', '/learn/', '/blog/', '/about/', '/privacy/',
    '/patterns/milo-woodland-moose-amigurumi/', '/patterns/heather-highland-cow-amigurumi/',
    '/robots.txt', '/sitemap-index.xml', '/rss.xml',
]
class Meta(HTMLParser):
    def __init__(self): super().__init__();self.canon=[];self.noindex=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='link' and a.get('rel','').lower()=='canonical':self.canon.append(a.get('href',''))
        if tag=='meta' and a.get('name','').lower()=='robots' and 'noindex' in a.get('content','').lower():self.noindex=True

fail=0
for path in PATHS:
    url=BASE+path
    try:
        with urlopen(Request(url,headers={'User-Agent':'ThreadAndPetalSiteAudit/1.0'}),timeout=12) as r:
            status=r.status;data=r.read(2000000).decode('utf-8','replace');final=r.geturl()
        issues=[]
        if status!=200:issues.append('HTTP '+str(status))
        if final.startswith('https://threadnpetal.com'):issues.append('redirected to old domain')
        if path.endswith('.xml') and 'threadnpetal.com' in data:issues.append('old-domain XML URLs')
        if path=='/robots.txt' and 'threadnpetal.blog/sitemap-index.xml' not in data:issues.append('wrong/missing sitemap URL')
        if path not in ('/robots.txt','/sitemap-index.xml','/rss.xml'):
            meta=Meta();meta.feed(data)
            if not meta.canon:issues.append('missing canonical')
            elif not meta.canon[0].startswith(BASE):issues.append('wrong canonical: '+str(meta.canon[0]))
            if meta.noindex:issues.append('noindex meta')
            if 'threadnpetal.com' in data:issues.append('old domain appears in HTML')
        print(('PASS' if not issues else 'FAIL')+' '+url+(' | '+'; '.join(issues) if issues else ''))
        fail+=bool(issues)
    except (HTTPError,URLError,TimeoutError,ValueError) as ex:
        print('FAIL '+url+' | '+str(ex));fail+=1
print('RESULT: '+('all checked URLs passed' if not fail else str(fail)+' issue(s); do not submit AdSense yet'))
sys.exit(bool(fail))
