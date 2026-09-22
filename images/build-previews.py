"""Regenerate the README icon grids from the icon SVGs.

    python images/build-previews.py

Writes file-icons-{dark,light}.svg and product-icons-{dark,light}.svg next to
this script. Card colors come from the sidebar colors in themes/.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
FONT = "-apple-system, 'SF Pro Text', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"

THEMES = {
    "dark": {"bg": "#262626", "border": "rgba(255,255,255,0.10)",
             "label": "rgba(255,255,255,0.55)", "glyph": "rgba(255,255,255,0.85)"},
    "light": {"bg": "#ECECEC", "border": "rgba(0,0,0,0.10)",
              "label": "rgba(0,0,0,0.50)", "glyph": "rgba(0,0,0,0.75)"},
}


def load(path):
    """Return (viewBox, attrs, inner markup) with C2PA metadata stripped."""
    svg = re.sub(r"<metadata>.*?</metadata>", "", path.read_text(encoding="utf-8"), flags=re.S)
    m = re.search(r"<svg([^>]*)>(.*)</svg>", svg, re.S)
    attrs = re.sub(r'\s+xmlns(:\w+)?="[^"]*"', "", m.group(1))
    attrs = re.sub(r'\s+viewBox="[^"]*"', "", attrs)
    view_box = re.search(r'viewBox="([^"]*)"', m.group(1)).group(1)
    return view_box, attrs.strip(), m.group(2)


def grid(items, cols, cell_w, cell_h, icon, theme, glyph_color=None):
    pad = 24
    rows = -(-len(items) // cols)
    w, h = pad * 2 + cols * cell_w, pad * 2 + rows * cell_h
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" '
        f'fill="{theme["bg"]}" stroke="{theme["border"]}"/>',
    ]
    for i, (label, path) in enumerate(items):
        view_box, attrs, inner = load(path)
        x = pad + (i % cols) * cell_w
        y = pad + (i // cols) * cell_h
        color = f' color="{glyph_color}"' if glyph_color else ""
        parts.append(
            f'<svg x="{x + (cell_w - icon) / 2}" y="{y + 8}" width="{icon}" height="{icon}" '
            f'viewBox="{view_box}" {attrs}{color}>{inner}</svg>'
        )
        parts.append(
            f'<text x="{x + cell_w / 2}" y="{y + icon + 28}" text-anchor="middle" '
            f'font-family="{FONT}" font-size="11" fill="{theme["label"]}">{label}</text>'
        )
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    icons = ROOT / "fileicons" / "icons"
    first = ["folder", "folder-open", "folder-dim", "folder-dim-open", "_file"]
    rest = sorted(p.stem for p in icons.glob("*.svg") if p.stem not in first and p.stem != "_file_light")
    files = [("file" if n == "_file" else n, icons / f"{n}.svg") for n in first + rest]

    glyphs = sorted((ROOT / "producticons" / "svg").glob("*.svg"))
    products = [(p.stem, p) for p in glyphs]

    for name, theme in THEMES.items():
        (OUT / f"file-icons-{name}.svg").write_text(
            grid(files, 11, 80, 80, 32, theme), encoding="utf-8")
        (OUT / f"product-icons-{name}.svg").write_text(
            grid(products, 9, 124, 80, 28, theme, theme["glyph"]), encoding="utf-8")
    print(f"{len(files)} file icons, {len(products)} product icons")


if __name__ == "__main__":
    main()
