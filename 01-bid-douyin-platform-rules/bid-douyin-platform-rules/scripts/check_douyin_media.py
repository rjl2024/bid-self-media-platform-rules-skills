#!/usr/bin/env python3
"""Inspect local media files against common Douyin publishing specs."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
VIDEO_EXTS = {".mp4", ".webm", ".mov", ".m4v"}


def human_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.2f} {unit}"
        value /= 1024
    return f"{size} B"


def ratio_label(width: int, height: int) -> str:
    if not width or not height:
        return "unknown"
    ratio = width / height
    presets = {
        "9:16": 9 / 16,
        "3:4": 3 / 4,
        "4:5": 4 / 5,
        "1:1": 1,
        "16:9": 16 / 9,
    }
    best = min(presets.items(), key=lambda item: abs(item[1] - ratio))
    if abs(best[1] - ratio) < 0.025:
        return best[0]
    return f"{ratio:.3f}:1"


def inspect_image(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {"kind": "image"}
    try:
        from PIL import Image  # type: ignore
    except Exception:
        result["warning"] = "Pillow is not installed; dimensions unavailable."
        return result

    with Image.open(path) as im:
        width, height = im.size
        result.update(
            {
                "format": im.format,
                "width": width,
                "height": height,
                "ratio": ratio_label(width, height),
            }
        )
    return result


def ffprobe(path: Path) -> dict[str, Any]:
    if not shutil.which("ffprobe"):
        return {"warning": "ffprobe is not installed; video metadata unavailable."}

    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,codec_name,pix_fmt,duration",
        "-show_entries",
        "format=duration",
        "-of",
        "json",
        str(path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if proc.returncode:
        return {"warning": proc.stderr.strip() or "ffprobe failed."}
    return json.loads(proc.stdout or "{}")


def inspect_video(path: Path) -> dict[str, Any]:
    data = ffprobe(path)
    result: dict[str, Any] = {"kind": "video"}
    if "warning" in data:
        result.update(data)
        return result

    streams = data.get("streams") or []
    stream = streams[0] if streams else {}
    fmt = data.get("format") or {}
    width = int(stream.get("width") or 0)
    height = int(stream.get("height") or 0)
    duration = stream.get("duration") or fmt.get("duration")
    duration_s = float(duration) if duration not in (None, "N/A") else None
    result.update(
        {
            "codec": stream.get("codec_name"),
            "pixel_format": stream.get("pix_fmt"),
            "width": width or None,
            "height": height or None,
            "ratio": ratio_label(width, height) if width and height else None,
            "duration_seconds": round(duration_s, 3) if duration_s is not None else None,
        }
    )
    return result


def warnings_for(path: Path, meta: dict[str, Any], size: int) -> list[str]:
    warnings: list[str] = []
    ext = path.suffix.lower()

    if meta["kind"] == "image":
        if size > 20 * 1024 * 1024:
            warnings.append("Image exceeds 20MB create-image-text single-image limit.")
        if size > 300 * 1024 * 1024:
            warnings.append("Image exceeds 300MB OpenAPI image-upload limit.")
        width = meta.get("width")
        height = meta.get("height")
        if width and height:
            ratio = width / height
            if ratio < 1 / 2.2 or ratio > 2.2:
                warnings.append("Image ratio is outside common OpenSDK share ratio range 1/2.2 to 2.2.")

    if meta["kind"] == "video":
        if ext not in {".mp4", ".webm"}:
            warnings.append("OpenAPI docs recommend mp4 or webm; SDK share commonly expects mp4.")
        if size > 4 * 1024 * 1024 * 1024:
            warnings.append("Video exceeds 4G Open Platform publishing reference limit.")
        duration = meta.get("duration_seconds")
        if duration and duration > 15 * 60:
            warnings.append("Video exceeds 15-minute Open Platform publishing reference limit.")
        width = meta.get("width")
        height = meta.get("height")
        if width and height:
            ratio = width / height
            if ratio < 1 / 2.2 or ratio > 2.2:
                warnings.append("Video ratio is outside common OpenSDK share ratio range 1/2.2 to 2.2.")
            if min(width, height) >= 2160 or max(width, height) >= 4096:
                warnings.append("Video is near or above Android SDK side-length guidance.")

    return warnings


def inspect_path(path: Path) -> dict[str, Any] | None:
    ext = path.suffix.lower()
    if ext not in IMAGE_EXTS and ext not in VIDEO_EXTS:
        return None

    size = path.stat().st_size
    meta = inspect_image(path) if ext in IMAGE_EXTS else inspect_video(path)
    return {
        "path": str(path),
        "size_bytes": size,
        "size": human_size(size),
        **meta,
        "warnings": warnings_for(path, meta, size),
    }


def iter_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return [p for p in target.rglob("*") if p.is_file()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect media against common Douyin specs.")
    parser.add_argument("target", help="Media file or folder to inspect")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    target = Path(args.target)
    if not target.exists():
        print(f"Not found: {target}", file=sys.stderr)
        return 2

    results = [item for p in iter_files(target) if (item := inspect_path(p))]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    if not results:
        print("No supported image/video files found.")
        return 0

    for item in results:
        print(f"\n{item['path']}")
        print(f"  kind: {item['kind']}")
        print(f"  size: {item['size']}")
        for key in ["format", "codec", "pixel_format", "width", "height", "ratio", "duration_seconds"]:
            if item.get(key) is not None:
                print(f"  {key}: {item[key]}")
        if item["warnings"]:
            print("  warnings:")
            for warning in item["warnings"]:
                print(f"    - {warning}")
        else:
            print("  warnings: none")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

