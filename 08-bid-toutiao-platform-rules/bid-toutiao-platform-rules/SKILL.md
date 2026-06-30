---
name: bid-toutiao-platform-rules
description: Check and apply Toutiao and Toutiaohao publishing rules for articles, micro-posts, videos, small videos, questions and answers, columns, covers, titles, images, content-commerce cards, AIGC labeling, copyright, originality, community norms, and creator compliance. Use when Codex needs to plan, audit, resize, rewrite, or package content for Toutiao publishing.
---

# Toutiao Platform Rules

Use this skill for Toutiao China and Toutiaohao creator workflows. Treat Toutiao article publishing, micro-posts, videos, small videos, questions and answers, paid columns, and content-commerce as different routes.

## Workflow

1. Identify the publishing route: Toutiaohao article, micro-post, video, small video, Q&A, column, content-commerce, or paid content.
2. Read `references/toutiao.md` for specs, platform risks, and source notes.
3. Check title, cover, source attribution, originality, content vertical, AIGC disclosure, copyright, and commerce claims.
4. Mark upload-size, duration, image count, title length, and account-permission fields as "verify in Toutiaohao backend" unless the user provides a current backend screenshot.

## Required Checks

- Media specs: cover ratio, image readability, video orientation, format, size, duration, and backend editor prompts.
- Article integrity: title accuracy, source citation, factual support, reprint permission, originality, and no misleading compilation.
- Distribution risk: clickbait title, fake breaking news, rumor amplification, public-event speculation, vulgarity, low-quality aggregation.
- Commerce risk: product efficacy, price, discount, affiliate link, e-commerce card, private transaction, and advertising disclosure.
- AIGC risk: generated people, generated news-like facts, generated evidence, synthesized voice, or AI images that may confuse readers.

## Response Pattern

Answer with:

1. recommended publishing form and export settings
2. title, cover, and body risks
3. copyright/source/originality risks
4. commerce and sensitive-vertical risks
5. backend-verification items

## Reference

- `references/toutiao.md`
