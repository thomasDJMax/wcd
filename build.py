#!/usr/bin/env python3
"""Build the offline, standalone camera simulator using only Python's standard library."""
from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parent
# WebP keeps the embedded images ~6x smaller than PNG at the same visible
# quality, which matters because everything is base64-inlined (and base64
# adds another third on top).
ASSETS = {
    "__BACKGROUND_DATA__": ("background.webp", "image/webp"),
    "__SUBJECT_DATA__": ("subject.webp", "image/webp"),
}


def main():
    html = (ROOT / "src" / "camera-template.html").read_text(encoding="utf-8")
    for token, (name, mime) in ASSETS.items():
        if token not in html:
            raise ValueError(f"Missing asset placeholder: {token}")
        data = (ROOT / "assets" / name).read_bytes()
        encoded = base64.b64encode(data).decode("ascii")
        html = html.replace(token, f"data:{mime};base64,{encoded}")
    output = ROOT / "camera-simulator.html"
    output.write_text(html, encoding="utf-8")
    print(f"Built {output.name} ({output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
