# Thread & Petal — Google AdSense launch checklist

Ad serving is intentionally **off** while the site is being prepared. Do not turn it on before AdSense approval and a suitable, Google-certified advertising consent management platform (CMP) are configured.

## Already implemented

- Public About, Privacy, pattern, learning and Journal pages.
- Site canonical URL and generated sitemap/robots.txt through Astro.
- An analytics-only, opt-in Google Analytics banner. **This is not a certified advertising CMP.**
- A publisher ownership meta tag in `BaseLayout.astro`, separate from ad serving.
- An optional `AdSlot.astro` component; ad activation is gated by `PUBLIC_ENABLE_ADS=true` **and** `PUBLIC_ADSENSE_CMP_READY=true`. Keep both off until the requirements are met.
- Privacy policy describes current analytics and planned (but not yet enabled) advertising.

## Next actions (require the site owner's input)

1. In AdSense, complete the **Individual** payments profile using your real legal/banking information. Do not commit private identity or tax information to the repository.
2. In **AdSense > Sites > threadnpetal.blog**, get the publisher ID formatted `ca-pub-XXXXXXXXXXXXXXXX` (16 digits).
3. Add `PUBLIC_ADSENSE_VERIFICATION_ID=ca-pub-XXXXXXXXXXXXXXXX` as a Cloudflare Pages production environment variable, then redeploy the site. This outputs a `google-adsense-account` verification meta tag without loading ads.
4. Use the correct publisher ID to add the authorized seller file at `public/ads.txt` in the format `google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0`. **Do not** publish a dummy ID or copy someone else's file. Verify `https://threadnpetal.blog/ads.txt` after deployment.
5. Set up **AdSense > Privacy & messaging** with a **Google-certified CMP** (and all required regional settings). Coordinate it with the existing Analytics preferences so users receive clear, functional consent choices. The in-house Analytics banner alone must not be presented as certified ad consent.
6. Review pattern accuracy, rights to publish all material, link functionality, accessibility, and genuinely helpful content. Confirm the sitemap is indexed correctly in Search Console, including the old .com canonical issue.
7. Submit the site for AdSense review. A Google-approved site is required before ads will serve; Google makes the approval decision.

## Only after approval and proper CMP deployment

- Configure the actual ad publisher ID with `PUBLIC_ADSENSE_CLIENT`, and a real ad unit slot `PUBLIC_ADSENSE_SLOT` if using manual `AdSlot` placements.
- Enable `PUBLIC_ADSENSE_CMP_READY=true` **only after verifying the CMP actually works**, not as a substitute for installing one.
- Set `PUBLIC_ENABLE_ADS=true` only when ready to serve.
- Test mobile ad density and cookie preference changes. Update the privacy policy from planned to active advertising before ads go live.

## Operational caution

Environment variables live in the deployment provider, not the repository. The AdSense dashboard and Cloudflare Pages settings cannot be confirmed just from GitHub source code. The `ads.txt` file is deferred until the real publisher ID is available.

## Google CMP coordination (staged, OFF by default)

Code provides a separate deployment switch, `PUBLIC_ENABLE_GOOGLE_CMP=true`, to load the AdSense publisher tag necessary for Google Privacy & messaging delivery. It is **not enabled by this commit**. Keep `PUBLIC_ENABLE_ADS` and `PUBLIC_ADSENSE_CMP_READY` unset/false.

Before enabling the switch:
- Publish the tested three-button European message in AdSense. An unpublished draft cannot render.
- Confirm **Auto ads are disabled** in AdSense (the publisher tag can also be used to deliver ads; the repository's ad-slot switch alone does not control Auto ads).
- Verify the deployed page and privacy policy in the final target markets.
- Test that the IAB TCF API is present and returns the correct `gdprApplies` signal, that European visitors see only Google's GDPR message, and that non-European visitors see the existing optional Analytics banner.
- The Analytics banner remains disabled in GDPR regions, even after an advertising consent choice. Google Analytics is **not** loaded there until a separate, explicit analytics consent mapping is implemented and legally reviewed. The existing banner still governs Google Analytics elsewhere.
- If CMP scripts are blocked or do not respond, the Analytics banner stays hidden and Analytics stays disabled (privacy-preserving fail-closed). This intentionally prioritizes not sending data without consent over analytics completeness.
- Keep footer privacy controls functional; in a confirmed GDPR region they call `googlefc.showRevocationMessage()` instead of reopening the site's separate Analytics banner.
- `PUBLIC_ENABLE_GOOGLE_CMP` is a build-time environment variable on Cloudflare Pages. A redeploy is required after changing it.
- Confirm the AdSense dashboard and Google Funding Choices developer API behavior with a real browser before treating this as a production consent integration.

## Analytics recovery with Google CMP consent mode (November 2026)

The site now listens for Google's documented `googlefc.callbackQueue` event `CONSENT_MODE_DATA_READY` and reads `getGoogleConsentModeValues()`. The earlier implementation relied on `__tcfapi` alone; it can be undefined for a visitor outside the European consent region.

**Important Google account prerequisites:** In AdSense **Privacy & messaging → European regulations → Settings → Consent mode**, check whether **Enable consent mode for advertising purposes** is enabled. To make GA4 function for European visitors who explicitly agree to Analytics, the site also needs the separate **Analytics storage consent** purpose configured. If the purposes have **NOT_CONFIGURED (4)** or **UNKNOWN (0)** statuses and no other reliable regional status exists, the script will intentionally keep Analytics blocked. These settings are in Google's account, **not** changed by this repository PR.

- EU consent-mode `GRANTED (1)` for `analytics_storage`: permits the optional GA4 tag; `DENIED (2)` keeps it off. An EU advertising grant does **not** imply Analytics consent.
- A confirmed non-applicability signal `NOT_APPLICABLE (3)` for configured consent purposes (or an explicit IAB `gdprApplies === false` answer) returns the visitor to the existing local opt-in Analytics banner. Analytics then starts **only after** the visitor explicitly accepts that banner or has an unexpired, previously accepted choice.
- `UNKNOWN (0)`, only `NOT_CONFIGURED (4)`, absent API, or blocked scripts are not permission. Tracking stays denied. No IP lookup, language guess, proxy, or ad-serving toggle is used.
- Keep `PUBLIC_ENABLE_ADS=false` and Auto ads off while approval is pending; `PUBLIC_ENABLE_GOOGLE_CMP=true` only loads the Google publisher tag for consent delivery.

**Validation:** From an ordinary non-EEA browsing session after a production redeploy, use an incognito window and confirm the local banner appears when Google's consent callback reports non-applicability; accepting should request `gtag/js?id=G-JBSY3YJZ0M` and a `google-analytics.com/g/collect` event. Rejecting must not load `gtag/js`. Use Google's published `?fc=alwaysshow&fctype=gdpr` **preview-only** parameter to inspect the European message, then verify regional production behavior in an actual eligible session. A server build cannot prove ad-tech API behavior for all visitor regions.

Docs: https://developers.google.com/funding-choices/fc-api-docs
