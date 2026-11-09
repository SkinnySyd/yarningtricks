#!/usr/bin/env python3
"""Optional editorial fix: add a short, factual source-designer credit to 7 MDX patterns.

This script never changes crochet instructions, headers, shared components or images.
Dry-run by default. Execute from the repo root. Requires no packages.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import sys

CREDITS = {
    'autumn-ember-red-panda-amigurumi.mdx': '*Design credit: Adapted from **Rusty the Red Panda** by **Josephine Wu** (A Morning Cup of Jo Creations), published in **Zoomigurumi 3**.*',
    'cloudberry-lamb-amigurumi.mdx': '*Design credit: Adapted from **Cuddles the Lamb** by **Little Muggles (Amy Lin)**, published in **Zoomigurumi 3**.*',
    'heather-highland-cow-amigurumi.mdx': '*Design credit: Adapted from **Hilda the Highland Cow** by **Moji-Moji Design (Janine Holmes)**, published in **Zoomigurumi 9**.*',
    'meadow-gazelle-amigurumi.mdx': '*Design credit: Adapted from **Audrey Gazelle** by **Yan Schenkel**, published in **Animal Friends of Pica Pau** (Meteoor Books, 2017).*',
    'milo-woodland-moose-amigurumi.mdx': '*Design credit: Adapted from **Monty the Moose** by **LittleAquaGirl**, published in **Zoomigurumi 7**.*',
    'splashy-frog-amigurumi.mdx': '*Design credit: Adapted from **Víctor Frog** by **Yan Schenkel**, published in **Animal Friends of Pica Pau** (Meteoor Books, 2017).*',
    'winter-wanderer-reindeer.mdx': '*Design credit: Adapted from **Noel the Reindeer** by **Hello Yellow Yarn (MJ Carlos)**, published in **Zoomigurumi 7**.*',
}


def add_credit(original: str, credit: str) -> str:
    if not original.startswith('---\n') or not re.match(r'\A---\n[\s\S]*?\n---\n', original):
        raise ValueError('MDX frontmatter is missing or malformed')
    # Skip if a credit was manually added or the exact line exists already.
    if re.search(r'(?i)(?:\*\s*)?(?:design credit|original(?:ly)? designed by)\s*:', original):
        return original
    if credit in original:
        return original
    trimmed = original.rstrip()
    # Follow the existing Thread & Petal pattern of a quiet source line beneath a divider.
    if not trimmed.endswith('---'):
        trimmed += '\n\n---'
    return trimmed + '\n\n' + credit + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Write changes (defaults to dry-run)')
    parser.add_argument('--root', default='.', help='Repository root (default: current directory)')
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not (root / 'src/content/patterns').is_dir():
        print('ERROR: Run from the Astro repository root.', file=sys.stderr)
        return 2
    changes = []
    try:
        for name, credit in CREDITS.items():
            path = root / 'src/content/patterns' / name
            if not path.exists():
                raise FileNotFoundError(f'Expected article not found: {name}')
            before = path.read_text(encoding='utf-8')
            if re.search(r'^(<<<<<<<|=======|>>>>>>>)', before, flags=re.M):
                raise ValueError(f'Unresolved Git merge markers in {name}')
            after = add_credit(before, credit)
            if after != before:
                print(('ADD CREDIT ' if args.apply else 'WOULD ADD CREDIT ') + name)
                changes.append((path, after))
            else:
                print('ALREADY CREDITED ' + name)
    except (ValueError, OSError) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        return 2
    if args.apply:
        for path, after in changes:
            path.write_text(after, encoding='utf-8')
        print(f'Added {len(changes)} source credits. Review git diff before committing.')
    else:
        print(f'Dry run: {len(changes)} articles would be updated. Use --apply to write.')
    print('Permission and crochet test verification remain separate tasks.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
