# BID 自媒体平台规则 Skills

这是一个面向 Codex 的国内主流自媒体平台规则 Skill 交付包，覆盖抖音、小红书、微信视频号、微信公众号、B站、快手、微博、今日头条。

## 包含的 Skill

| 平台 | Skill 名称 | 适用内容 |
|---|---|---|
| 抖音 | `bid-douyin-platform-rules` | 视频、图文、直播、AIGC、OpenAPI/SDK |
| 小红书 | `bid-xiaohongshu-platform-rules` | 笔记、图文、视频、封面、种草合规 |
| 微信视频号 | `bid-wechat-channels-platform-rules` | 视频、图片、直播、微信生态链接 |
| 微信公众号 | `bid-wechat-official-account-rules` | 文章、封面、素材、群发、转载授权 |
| B站 | `bid-bilibili-platform-rules` | 视频、封面、标题、标签、简介、版权 |
| 快手 | `bid-kuaishou-platform-rules` | 短视频、直播、电商、商品宣称 |
| 微博 | `bid-weibo-platform-rules` | 图文、视频、长文、话题、舆情敏感内容 |
| 今日头条 | `bid-toutiao-platform-rules` | 文章、微头条、视频、小视频、问答、专栏、内容电商 |

## 安装

把需要的平台 Skill 文件夹复制到本机 Codex Skills 目录：

```powershell
$srcRoot = "I:\闲鱼发布产品库\063005自媒体平台规则skill发布包"
$dstRoot = "$env:USERPROFILE\.codex\skills"
New-Item -ItemType Directory -Force -Path $dstRoot | Out-Null

Get-ChildItem -Directory $srcRoot | ForEach-Object {
  Get-ChildItem -Directory $_.FullName | Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") } | ForEach-Object {
    Copy-Item $_.FullName (Join-Path $dstRoot $_.Name) -Recurse -Force
  }
}
```

安装后重启 Codex 客户端，然后用 `$bid-douyin-platform-rules`、`$bid-xiaohongshu-platform-rules` 等名称调用。

## 使用说明

根目录的 `安装教程和使用说明.html` 是完整客户版说明，可离线打开。每个平台目录中也有独立压缩包 `*-skill.zip`。根目录还提供整体压缩包 `BID自媒体平台规则skill发布包.zip`。

## 规则时效提醒

平台后台的上传大小、时长、张数、封面比例等限制会随账号权限和产品版本变化。正式发布前，应在对应创作者后台或规则中心复核。

## 验证

本地已执行：

- 8 个 Skill 均通过 `quick_validate.py`
- 抖音媒体检查脚本通过 `python -m py_compile`
- 8 个平台独立 zip 和整体 zip 已重新生成
