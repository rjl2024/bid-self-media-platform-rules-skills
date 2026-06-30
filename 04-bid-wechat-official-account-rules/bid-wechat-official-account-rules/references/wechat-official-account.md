# WeChat Official Account Publishing Rules

Updated: 2026-06-30

Scope: WeChat Official Account articles, assets, drafts, mass sending, and API material management.

## Recommended Specs

| Type | Practical Export | Notes |
|---|---|---|
| Article cover | 900x383 for main cover; also prepare square crop | Common public-account practice; verify current editor preview. |
| In-article image | Width 900-1080 px | Keep text large enough for mobile reading. |
| Share card thumbnail | Prepare a clear square crop | Avoid unreadable title text in thumbnail. |
| Video/audio material | Follow current backend/API prompt | API material limits differ by temporary/permanent material type. |

## API Material Notes

Official API docs expose material upload constraints such as temporary image, voice, video, and thumb media limits. These are API workflow limits and should not be blindly applied to manual article editing.

When using API:

- read the current WeChat official documentation for temporary/permanent material upload
- distinguish image, voice, video, thumb, article draft, and mass-send endpoints
- handle media ID expiration and permanent material count limits

## Article Compliance Checks

- Respect reprint, original content, portrait, trademark, font, screenshot, and image copyright.
- Avoid illegal medical, finance, investment, education, recruitment, legal, health-product, cosmetics, and food claims.
- Avoid misleading title bait, fake official tone, fake authority, fake urgency, fake scarcity, and fabricated data.
- External links and QR codes should follow WeChat platform restrictions and account capability.
- AIGC content that may mislead readers about real facts, people, evidence, or product results should be labeled.

## Backend Verification Items

Verify in the official-account backend before final delivery:

- current title length and summary length
- current cover crop behavior
- image/video/audio upload size and supported formats
- external link and mini-program insertion permissions
- original/reprint/paid-content account capabilities

## Sources

- WeChat Official Account Platform: https://mp.weixin.qq.com/
- WeChat official account developer docs: https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html
- Temporary material API docs: https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/New_temporary_materials.html
- Permanent material API docs: https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Adding_Permanent_Assets.html
- Mass message and draft docs: https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Batch_Sends_and_Originality_Checks.html
- China generative AI labeling reference: https://www.cac.gov.cn/

