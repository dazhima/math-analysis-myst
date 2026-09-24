#!/usr/bin/env python3
"""Static integrity checks for the generated Obsidian/MyST vault."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LECTURES = ROOT / "lectures"
ASSETS = ROOT / "assets"


def main() -> int:
    errors: list[str] = []
    files = sorted(LECTURES.glob("L*.md"))
    svgs = sorted(ASSETS.glob("*.svg"))
    if len(files) != 18:
        errors.append(f"expected 18 lecture files, found {len(files)}")
    if len(svgs) != 79:
        errors.append(f"expected 79 SVG figures, found {len(svgs)}")

    index = (ROOT / "index.md").read_text()
    for label in re.findall(r"\[([^\]]+)\]\(lectures/L\d\d\.md\)", index):
        if "$" in label:
            errors.append(f"index.md: math delimiter inside link label: {label}")

    forbidden = {
        "conversion marker": r"MYST(?:BLOCK|FIGURE|ANCHOR|PROBLEMS)",
        "GitHub-only math fence": r"``` math|\$`",
        "private LaTeX macro": r"\\(?:N|Z|Q|R|eps|abs|dd|kk|cl|name|pnbd|fpart|diffstar|dstar|starone|startwo|starthree|st)(?![A-Za-z])",
        "PDF layout command": r"\\(?:textwidth|linewidth|centering|hfill|vspace|begin\{(?:figure|tikzpicture|center|tabular|problems)\})",
        "nested display environment": r"\\begin\{(?:equation|align\*?|gather\*)\}",
        "unsupported math command": r"\\(?:toprule|midrule|bottomrule|qedhere|ensuremath)(?![A-Za-z])",
    }

    total_images = 0
    total_callouts = 0
    for path in files:
        text = path.read_text()
        for label, pattern in forbidden.items():
            for match in re.finditer(pattern, text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path.name}:{line}: {label}")

        # Dollar parity is a useful first-line guard against an unclosed formula.
        no_escaped = re.sub(r"\\\$", "", text)
        display_lines = re.findall(r"(?m)^(?:> )*[ \t]*\$\$[ \t]*$", no_escaped)
        if len(display_lines) % 2:
            errors.append(f"{path.name}: odd number of display-math delimiters")
        inline = re.sub(r"(?m)^(?:> )*[ \t]*\$\$[ \t]*$", "", no_escaped)
        if inline.count("$") % 2:
            errors.append(f"{path.name}: odd number of inline-math delimiters")

        ids = set(re.findall(r'<span id="([^"]+)"></span>', text))
        links = re.findall(r"\]\(#([^)]+)\)", text)
        for target in links:
            if target not in ids:
                errors.append(f"{path.name}: unresolved internal target #{target}")

        for rel in re.findall(r"\(([^()\n]+\.svg)\)", text):
            total_images += 1
            image = (path.parent / rel).resolve()
            if not image.exists():
                errors.append(f"{path.name}: missing image {rel}")
        total_callouts += len(re.findall(r"(?m)^> \[!(?:NOTE|IMPORTANT|WARNING)\]", text))

    if total_images != 79:
        errors.append(f"expected 79 image references, found {total_images}")
    for svg in svgs:
        try:
            ET.parse(svg)
        except Exception as exc:
            errors.append(f"{svg.name}: invalid SVG XML: {exc}")

    print(f"lectures={len(files)} svg_files={len(svgs)} image_refs={total_images} callouts={total_callouts}")
    if errors:
        print("FAILED")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
