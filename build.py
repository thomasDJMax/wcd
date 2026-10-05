#!/usr/bin/env python3
"""Build the offline, standalone camera simulator using only Python's standard library."""
from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parent
ASSETS = {
    "__BACKGROUND_DATA__": "background.png",
    "__SUBJECT_DATA__": "subject.png",
}


def main():
    html = (ROOT / "src" / "camera-template.html").read_text(encoding="utf-8")
    for token, name in ASSETS.items():
        if token not in html:
            raise ValueError(f"Missing asset placeholder: {token}")
        data = (ROOT / "assets" / name).read_bytes()
        html = html.replace(token, "data:image/png;base64," + base64.b64encode(data).decode("ascii"))
    output = ROOT / "camera-simulator.html"
    output.write_text(html, encoding="utf-8")
    print(f"Built {output.name} ({output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
