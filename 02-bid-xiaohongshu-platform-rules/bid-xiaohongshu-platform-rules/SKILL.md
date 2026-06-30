---
name: bid-xiaohongshu-platform-rules
description: Check and apply Xiaohongshu/RED publishing rules for notes, image posts, video notes, covers, titles, hashtags, AIGC labeling, community norms, marketing risk, rights issues, and creator compliance. Use when Codex needs to plan, audit, resize, rewrite, or package content for Xiaohongshu publishing.
---

# Xiaohongshu Platform Rules

Use this skill for Xiaohongshu China publishing. Treat community safety, authenticity, and marketing compliance as part of the asset spec.

## Workflow

1. Identify content type: image note, video note, mixed note, live content, account profile asset, brand/commercial note.
2. Read `references/xiaohongshu.md` for specs, risk categories, and source notes.
3. Separate stable recommendations from backend-only limits. If a limit depends on account state or the web/app editor, say it needs Creator Center verification.
4. Check commercial risk: soft ads, medical/finance/education claims, exaggerated results, price/discount claims, before-after comparison, and off-platform contact guidance.
5. Check rights: portrait, brand logo, music, font, screenshot, product photo, store photo, and copied material.

## Response Pattern

Answer with:

1. recommended export sizes
2. publishing and editor limits that need verification
3. title/cover/note compliance risks
4. fixes before upload

## Reference

- `references/xiaohongshu.md`

