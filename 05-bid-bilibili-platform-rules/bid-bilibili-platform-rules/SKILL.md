---
name: bid-bilibili-platform-rules
description: Check and apply Bilibili publishing rules for videos, covers, titles, tags, descriptions, subtitles, articles, dynamic posts, AIGC labeling, copyright, community norms, and creator compliance. Use when Codex needs to plan, audit, resize, rewrite, or package content for Bilibili publishing.
---

# Bilibili Platform Rules

Use this skill for Bilibili China content. Bilibili upload specs can depend on account status, creator backend, and current upload page; verify limits in the live submission page.

## Workflow

1. Identify content type: video, series, article, dynamic post, live, course, commercial content.
2. Read `references/bilibili.md`.
3. Check cover, title, tag, category, copyright, music, footage, subtitles, and AIGC disclosure.
4. Mark upload-size and duration limits as backend-verification items unless the user provides a current upload-page screenshot.

## Response Pattern

Give export recommendations, submission metadata guidance, content risks, and backend-verification items.

## Reference

- `references/bilibili.md`

