#!/usr/bin/env python3
"""Read-only Astro content QA for Thread & Petal. Uses Python standard library only.

Run from repository root: python3 audit_content.py
This checks source references, not crochet construction or real Google indexing.
"""
from pathlib import Path
import re
import sys

ROOT = Path('.').resolve()
CONTENT = ROOT / 'src/content'
PATT = CONTENT / 'patterns'
LESS = CONTENT / 'lessons'
if not PATT.is_dir() or not LESS.is_dir():
    sys.exit('Please run this from the Thread & Petal project root.')
pattern_files = sorted([*PATT.glob('*.mdx'), *PATT.glob('*.md')])
lesson_files = sorted([*LESS.glob('*.mdx'), *LESS.glob('*.md')])
pattern_slugs = {p.stem for p in pattern_files}
lesson_slugs = {p.stem for p in lesson_files}
issues = []
missing_credit = []
known_credits = {
 'autumn-ember-red-panda-amigurumi', 'cloudberry-lamb-amigurumi',
 'heather-highland-cow-amigurumi', 'meadow-gazelle-amigurumi',
 'milo-woodland-moose-amigurumi', 'splashy-frog-amigurumi',
 'winter-wanderer-reindeer'
}
for path in [*pattern_files, *lesson_files]:
    body = path.read_text(encoding='utf-8')
    if not re.match(r'^---\n[\s\S]+?\n---\n', body):
        issues.append((path, 'Missing or malformed YAML frontmatter'))
    for url in set(re.findall(r'/images/[\w./-]+\.(?:webp|png|jpe?g|svg)', body, flags=re.I)):
        if not (ROOT / 'public' / url.lstrip('/')).exists():
            issues.append((path, f'Missing image: {url}'))
    for raw in set(re.findall(r'\]\((/[^)\s]+)\)', body)):
        url = raw.split('#',1)[0].split('?',1)[0].strip('/')
        if url.startswith('patterns/') and url != 'patterns' and url.split('/',1)[1] not in pattern_slugs:
            issues.append((path, f'Missing pattern link: {raw}'))
        if url.startswith('learn/') and url != 'learn' and url.split('/',1)[1] not in lesson_slugs:
            issues.append((path, f'Missing lesson link: {raw}'))
    if re.search(r'^(?:<<<<<<<|=======|>>>>>>>)', body, flags=re.M):
        issues.append((path, 'Unresolved Git conflict marker'))
    if path.stem in known_credits and 'Design credit:' not in body:
        missing_credit.append(path.name)
    if 'The source skips Round 23' in body or 'source skips Round 23' in body:
        issues.append((path, 'Panda hind-leg Round 23 remains unresolved: verify against designer'))

code_old=[]
for parent in ('src',):
 for path in (ROOT/parent).rglob('*'):
    if path.is_file() and path.suffix in {'.astro','.ts','.js','.mjs','.md','.mdx'}:
        if 'threadnpetal.com' in path.read_text(encoding='utf-8'):
            code_old.append(str(path.relative_to(ROOT)))
config=ROOT/'astro.config.mjs'
if config.exists() and 'threadnpetal.com' in config.read_text(encoding='utf-8'):
    code_old.append('astro.config.mjs')
code_old=sorted(set(code_old))
blog=ROOT/'src/pages/blog/index.astro'
if blog.exists() and "getCollection('patterns'" in blog.read_text(encoding='utf-8'):
    issues.append((blog, 'Journal currently lists the same pattern collection as the library'))

print(f'Pattern articles: {len(pattern_files)} | Standalone lessons: {len(lesson_files)}')
print('Missing or broken file/MDX references and editorial flags:')
for path,problem in issues:
 print(' -', path.relative_to(ROOT), '=>', problem)
if not issues:
 print(' - None found by this source-only scan')
print('Old-domain references still in source:')
for path in code_old:
 print(' -',path)
if not code_old:
 print(' - None')
print('Adapted patterns needing a small end-of-article credit (if not manually credited elsewhere):')
for name in missing_credit:
 print(' -',name)
if not missing_credit:
 print(' - None')
print('\nNOT CHECKED: live DNS/HTTPS, Search Console, AdSense, permission documents, pattern testing, image accuracy, privacy/legal accuracy.')
print('Editorial audit finished. Fix substantive warnings before applying for AdSense.')
