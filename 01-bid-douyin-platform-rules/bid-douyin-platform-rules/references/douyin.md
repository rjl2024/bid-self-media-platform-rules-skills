# Douyin China Publishing Rules

Updated: 2026-06-30

Scope: Douyin China App, Douyin Creator Service Platform, Douyin Open Platform, Douyin rule center. TikTok is out of scope.

Rule of use: identify the publishing path first. App/manual publishing, OpenAPI publishing, OpenSDK sharing, H5 sharing, and live streaming do not always use the same limits.

## Content Types

| Type | Hard Specs | Compliance Focus | Notes |
|---|---|---|---|
| Short video | Open Platform publishing docs mention mp4/webm, video under 4G and within 15 minutes; upload interface details vary by endpoint | originality, authorization, no other-platform watermark, no misleading traffic diversion | Native App/PC limits may differ from OpenAPI limits |
| Image-text post | OpenAPI image upload up to 300M; create-image-text endpoint says single image up to 20M and up to 30 images per post; share solution supports 1-35 images | image review follows in-app logic; watermark and QR risks apply | Export 3:4, 4:5, 1:1, and 9:16 variants when making templates |
| Mixed image/video share | OpenSDK supports video, images, and mixed media in newer versions; count and ratio depend on SDK and Douyin version | user must publish intentionally; third-party apps must not impersonate user-created content | Useful for editing, photo, and content-sync tools |
| Long-form article | No stable official public spec found; public 2025 tests reported 300+ words, up to 4000 words, up to 10 images, no GIF, PC editor | follows normal content and vertical rules | Treat as gray/permissioned; verify in Creator Service Platform before delivery |
| Live stream | No universal media-upload size table; cover, title, speech, appearance, sound, background, stickers, avatar, and profile text are all content | live behavior rules, guest control, audience interaction management | E-commerce and life-service live streams have additional rules |
| AIGC or virtual human | Technical limits follow the media type | clear AI labeling, no infringement, no false news-like claims, virtual-human registration/real-name requirements | Commercial, medical, and product-effect content is more sensitive |

## Video

### OpenAPI Publishing

- Recommended formats: mp4 and webm.
- Publishing solution: video file under 4G and duration within 15 minutes; image under 100M.
- Chunk upload: over 50M is recommended to use chunk upload; over 300M must use chunk upload; total video size within 4G; suggested chunk size 20M and minimum 5M.
- Some endpoint pages also mention a 100MB interface-level limit. When building automation, obey the current endpoint docs and returned error codes.
- Source wording has a possible conflict around "16:9" and "vertical video"; for production, prepare both 1080x1920 vertical and 1920x1080 horizontal versions when the campaign needs both.

### OpenSDK and H5 Sharing

- Share solution supports single video, multiple videos, single image, multiple images, and mixed media in supported versions.
- Video aspect ratio in the share solution must satisfy `1/2.2 <= width/height <= 2.2`; video count 1-12; total duration greater than 1 second; mp4 and parseable file.
- Android SDK docs: mp4, YUV420P/YUVJ420P; single video and total video duration up to 60 minutes; short side under 2160 and long side under 4096; newer versions can support more videos.
- iOS older docs: media count up to 12; direct share to publish page supports single video.

### Recommended Exports

- Default vertical video: 1080x1920, 9:16.
- Horizontal video: 1920x1080, 16:9.
- Cover: prepare 3:4 or 9:16. Keep title, face, logo, and key object away from edges.
- Avoid other-platform watermarks, QR codes, phone numbers, WeChat IDs, copied subtitles, and third-party app logos.

## Images and Image-Text

### OpenAPI Image-Text

- Image upload endpoint: image size up to 300M; review logic follows in-app logic.
- Create image-text endpoint: post enters review after publishing; during review only the creator can see it.
- Single image up to 20M; up to 30 images per image-text post.
- Anchors: current public docs mention mini-program and POI anchors; do not assume multiple anchor types can be carried together.

### Share Publishing

- Share solution: image aspect ratio must satisfy `1/2.2 <= width/height <= 2.2`; image count 1-35.
- Android SDK: Douyin 12.3.0 and above supports up to 35 images; older versions support up to 12. Later docs expand some ratio handling for supported versions.
- H5 sharing is mainly for single image or single video scenarios; mobile apps should prefer SDK integration.

### Recommended Exports

- Single image or cover: 1080x1440 (3:4), 1080x1350 (4:5), 1080x1920 (9:16), or 1080x1080 (1:1).
- Multi-image post: keep a consistent ratio across all images.
- Long image: keep text large enough for mobile preview; do not assume Xiaohongshu cropping behavior matches Douyin.
- Avoid watermarks, QR codes, off-platform contact information, unauthorized portraits, trademarks, copyrighted screenshots, and repost traces.

## Long-Form Article

Public official documents found during this build did not expose a stable universal article spec. Treat article/long-form capability as account-gated or gray release.

Public 2025 tests reported:

- PC Creator Service Platform entry.
- 300+ words recommended; editor showed up to 4000 words.
- Up to 10 images; GIF unsupported.
- Published content was not always editable after publishing.
- Some Toutiao content could sync to Douyin, but not all articles would sync.

Before delivering article templates, verify the current account's Creator Service Platform entry, word limit, image count, GIF support, music support, sync behavior, and edit-after-publish behavior.

## Live Stream

- Live rules apply to host and guests.
- Cover, title, speech, clothing, action, sound, background, stickers, nickname, avatar, and profile introduction can all trigger content review.
- Hosts should control guest behavior and stop or block illegal audience interactions.
- Violations may cause stream interruption, live permission restriction, account restriction, or ban.
- Mini-program live mounting, e-commerce live, and life-service live require additional specialized rules.

## Universal Content Risks

Douyin's public rule direction emphasizes lawful, factual, positive, and rights-respecting content. Flag these risks:

- illegal activity, fraud, gambling, drugs, pornography, vulgarity, violence, terrorism
- misinformation, rumor, fake public-event content, fake expert claims
- privacy, portrait, reputation, trademark, music, font, screenshot, or copyright infringement
- exaggerated product claims, fake discounts, false scarcity, fake authority
- off-platform traffic diversion, contact harvesting, QR-code bait, private transaction guidance
- cyberbullying, humiliation, body shaming, minors-related harm
- sensitive verticals: medical, finance, education, recruitment, legal, cosmetics, food, health products

## AIGC

- Clearly label AI-generated content when it may confuse users about reality.
- The publisher is responsible for consequences caused by AI-generated output.
- Do not use AI to create or publish infringing portraits, voices, trademarks, copyrighted content, false claims, fake science, rumors, or public-event misinformation.
- Virtual-human use requires platform registration and real-name requirements where applicable; live virtual humans should follow platform interaction requirements.

## Verification Checklist

Before final delivery, verify in the live Creator Service Platform when the output depends on:

- native App/PC upload file-size and duration limits
- current image-text count, single-image size, and supported file types
- long-form article entry, word count, image count, GIF support, and edit behavior
- live cover ratio, title length, and live-room-specific restrictions
- e-commerce, life-service, medical, finance, education, or recruitment vertical rules

## Sources

- Douyin Rule Center: https://www.douyin.com/rule/
- Douyin Community Self-Discipline Convention: https://www.douyin.com/rule/policy
- Douyin AIGC platform rule and industry proposal: https://www.douyin.com/rule/billboard?id=1242800000049
- Douyin AI virtual-person governance notice: https://www.douyin.com/rule/billboard?id=1242800000102
- Douyin content publishing solution: https://open.douyin.com/platform/resource/docs/ability/content-management/douyin-publish-solution
- Douyin sharing solution: https://open.douyin.com/platform/resource/docs/ability/content-management/douyin-share-solution
- Android sharing SDK docs: https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/sdk/mobile-app/share/android
- iOS sharing docs: https://open.douyin.com/platform/resource/docs/develop/share/ios
- H5 share-to-Douyin docs: https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/sdk/web-app/h5/share-to-h5
- Image upload endpoint: https://developer.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/video-management/douyin/create-image-text/image-upload
- Create image-text endpoint: https://partner.open-douyin.com/docs/resource/zh-CN/dop/develop/openapi/video-management/douyin/create-image-text/create-image-text
- Live behavior spec: https://sf3-cdn-tos.douyinstatic.com/obj/ies-hotsoon-draft/webcast_all_anchor/webcast_ban_protocol.html
- Mini-program live mounting usage spec: https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/operation/platform-capabilities/live/usage-spec
- Public long-form test reference, non-official: https://www.woshipm.com/share/6265276.html

