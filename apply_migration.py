#!/usr/bin/env python3
"""Targeted, idempotent domain migration for Thread & Petal Astro repository.

Run from the project root: python3 apply_migration.py --apply
No DNS, Cloudflare or AdSense account settings are modified by this script.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import sys

OLD = 'threadnpetal.com'
NEW = 'threadnpetal.blog'
FILES = [
    'astro.config.mjs',
    'src/site-config.ts',
    'src/pages/privacy.astro',
    'src/pages/learn/[slug].astro',
    '.env.example',
    'src/layouts/BaseLayout.astro',
]

def transform(path: str, content: str) -> str:
    s = content
    if path in {'astro.config.mjs', 'src/site-config.ts', 'src/pages/privacy.astro', 'src/pages/learn/[slug].astro'}:
        s = s.replace(OLD, NEW)
    if path == '.env.example':
        s = s.replace('SITE_URL=https://yourdomain.com', 'SITE_URL=https://threadnpetal.blog')
        # Site verification without enabling actual ad serving.
        if 'PUBLIC_ADSENSE_VERIFICATION_ID=' not in s:
            s += '\n# Optional: add only the ca-pub-... ID Google gives you, to verify ownership without displaying ads.\nPUBLIC_ADSENSE_VERIFICATION_ID=\n'
    if path == 'src/pages/privacy.astro':
        s = s.replace("const updatedOn = 'October 29, 2026';", "const updatedOn = 'November 9, 2026';")
        s = s.replace('datetime="2026-10-29"', 'datetime="2026-11-09"')
        old_email = ('<p>Our domain uses <strong>Cloudflare Email Routing</strong> to forward incoming messages to our designated email inbox. '
                     'The provider that hosts that destination inbox also processes messages as part of delivering our email service.</p>')
        new_email = ('<p>Messages are delivered through the email service configured for our domain and the inbox provider we use. '
                     'These services process correspondence to deliver and receive emails.</p>')
        s = s.replace(old_email, new_email)
    if path == 'src/layouts/BaseLayout.astro':
        anchor = 'const adClient = import.meta.env.PUBLIC_ADSENSE_CLIENT;'
        extra = "const adsenseVerificationId = import.meta.env.PUBLIC_ADSENSE_VERIFICATION_ID || '';"
        if extra not in s:
            if anchor not in s:
                raise ValueError(f'Layout changed: expected anchor missing from {path}')
            s = s.replace(anchor, anchor+'\n'+extra)
        meta = '  {adsenseVerificationId && <meta name="google-adsense-account" content={adsenseVerificationId} />}'
        if meta not in s:
            anchor2 = '  <link rel="canonical" href={canonical} />'
            if anchor2 not in s:
                raise ValueError(f'Layout changed: expected canonical anchor missing from {path}')
            s = s.replace(anchor2, anchor2+'\n'+meta)
    return s

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Actually edit files; without this flag, dry-run only')
    parser.add_argument('--root', default='.', help='Astro project root (default: current directory)')
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not (root / 'package.json').exists() or not (root / 'src/pages/privacy.astro').exists():
        print('ERROR: Run inside the Thread & Petal repository root (package.json must be here).', file=sys.stderr)
        return 2
    changes = []
    try:
        for name in FILES:
            target = root/name
            if not target.is_file():
                raise FileNotFoundError(f'Missing expected repo file: {name}')
            before = target.read_text(encoding='utf-8')
            after = transform(name,before)
            if before != after:
                changes.append((target,name,after))
                print(('UPDATE ' if args.apply else 'WOULD UPDATE ') + name)
            else:
                print('UNCHANGED ' + name)
    except (OSError,ValueError) as exc:
        print('ERROR: '+str(exc),file=sys.stderr)
        return 2
    if args.apply:
        for target,name,after in changes:
            target.write_text(after,encoding='utf-8')
        print(f'Updated {len(changes)} files. Review with git diff, build and deploy.')
    else:
        print(f'Dry run: {len(changes)} files would change. Re-run with --apply to make edits.')
    print('IMPORTANT: Confirm that contact@threadnpetal.blog actually receives email before deploying.')
    print('Verify that the Privacy Policy operator/location, analytics and email-service statements match reality.')
    print('Cloudflare SITE_URL, DNS, Search Console and AdSense must be configured separately.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
