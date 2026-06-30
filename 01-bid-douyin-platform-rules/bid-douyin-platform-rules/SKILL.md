---
name: bid-douyin-platform-rules
description: Check and apply Douyin China platform publishing rules for short videos, image-text posts, images, long-form articles, live-stream assets, OpenAPI/OpenSDK sharing, AIGC labeling, watermarks, copyright, and content safety. Use when Codex needs to plan, audit, resize, validate, or rewrite content for Douyin publishing, including asset specs, file-size limits, aspect ratios, wording risks, or creator compliance checks.
---

# Douyin Platform Rules

Use this skill to answer or audit Douyin publishing requirements. Treat Douyin China and TikTok as different platforms; this skill covers Douyin China only.

## Workflow

1. Identify the publishing path before giving specs:
   - Douyin App or Creator Service Platform manual upload
   - Douyin OpenAPI direct publishing
   - OpenSDK or H5 share-to-Douyin
   - Douyin live stream
   - Douyin e-commerce or life-service content
2. Identify the content type:
   - short video, image-text post, standalone image, long-form article, live cover, account profile asset, AIGC or virtual-human content
3. Read `references/douyin.md` for the current rule table and source notes.
4. If the user provides local media files, run `scripts/check_douyin_media.py` to inspect size, dimensions, ratio, and obvious spec risks.
5. Separate hard rules from operating recommendations:
   - Hard rules: upload size, duration, count, format, platform policy, explicit bans.
   - Recommendations: export size, safe zone, cover layout, title density, reusable template sizes.
6. Flag uncertain or account-gated items as "needs Creator Service Platform verification" instead of presenting them as stable official rules.

## Required Checks

Always check these before approving Douyin content:

- Publishing path: App/manual, OpenAPI, SDK/H5 share, live, e-commerce/life-service.
- Media specs: format, file size, duration, width/height, aspect ratio, image count or video count.
- Platform risk: other-platform watermark, QR code, contact method, off-platform traffic diversion, misleading interaction bait, copied or unauthorized material.
- Rights risk: portrait rights, trademarks, music, footage, fonts, screenshots, third-party logos.
- Sensitive verticals: medical, finance, education, recruitment, legal, minors, health products, cosmetics, food claims, investment claims.
- AIGC: whether the content uses AI-generated people, voices, scenes, news-like claims, product effects, or virtual humans; require clear labeling when applicable.

## Media Inspection

For a local file or folder, run:

```bash
python scripts/check_douyin_media.py "path/to/file-or-folder"
```

The script reports:

- file size
- image dimensions and aspect ratio when Pillow is available
- video duration, dimensions, codec, and pixel format when `ffprobe` is available
- likely Douyin recommendation matches and obvious warnings

The script is an aid, not a substitute for official platform review. Use the reference file for policy decisions.

## Response Pattern

When answering users, prefer this compact structure:

1. "For your publishing path, use these hard limits..."
2. "Recommended export settings..."
3. "Risks to fix before upload..."
4. "Items that need live backend verification..."

If the user asks for a complete rule pack, produce a table grouped by content type and include source links from `references/douyin.md`.

## Reference Files

- `references/douyin.md`: Douyin rules, hard specs, operating recommendations, risk checklist, and source links.

