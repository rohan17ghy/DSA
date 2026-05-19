"""Export .excalidraw JSON to Obsidian Ex-1674_Complementary.md (full plugin format)."""
import json
import re
from pathlib import Path

try:
    import lzstring
except ImportError:
    raise SystemExit("pip install lzstring")

ROOT = Path(r"c:\Code\DSA\Notes")
SRC = ROOT / "Excalidraw" / "Line-Sweep-1674-Complementary.excalidraw"
DST = ROOT / "LineSweep" / "Ex-1674_Complementary.md"

WARNING = (
    "==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== "
    "You can decompress Drawing data with the command palette: "
    "'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'"
)


def text_lines_from_json(data: dict) -> list[str]:
    lines = []
    for el in data.get("elements", []):
        if el.get("isDeleted") or el.get("type") != "text":
            continue
        txt = (el.get("text") or el.get("originalText") or "").strip()
        if not txt:
            continue
        eid = el.get("id", "")
        # One line per text element; multiline text stays on one block line
        for part in txt.split("\n"):
            part = part.strip()
            if part:
                lines.append(f"{part} ^{eid}")
                break  # Obsidian uses first line + id; avoid duplicate ids
        else:
            lines.append(f" ^{eid}")
    return lines


def wrap_base64(b64: str, width: int = 76) -> str:
    return "\n".join(b64[i : i + width] for i in range(0, len(b64), width))


def main():
    raw = SRC.read_text(encoding="utf-8")
    data = json.loads(raw)
    text_section = "\n".join(text_lines_from_json(data))
    compressed = lzstring.LZString.compressToBase64(raw)
    wrapped = wrap_base64(compressed)

    body = f"""---
excalidraw-plugin: parsed
tags: [excalidraw]

---
{WARNING}


# Excalidraw Data

## Text Elements
{text_section}

%%
## Drawing
```compressed-json
{wrapped}
```
%%
"""
    DST.write_text(body, encoding="utf-8")
    print("wrote", DST)
    print("text elements:", len(text_section.splitlines()))
    print("compressed chars:", len(compressed))


if __name__ == "__main__":
    main()
