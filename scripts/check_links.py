"""Check that every relative link and anchor in the repository's markdown resolves."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)


def slug(heading: str) -> str:
    """GitHub-style heading anchor."""
    text = re.sub(r"`", "", heading.strip().lower())
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    return {slug(h) for h in HEADING.findall(path.read_text(encoding="utf-8"))}


def main() -> int:
    errors = []
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for target in LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            file_part, _, fragment = target.partition("#")
            dest = (md.parent / file_part).resolve() if file_part else md
            if not dest.exists():
                errors.append(f"{md.relative_to(ROOT)}: missing file {target}")
            elif fragment and dest.suffix == ".md" and fragment not in anchors(dest):
                errors.append(f"{md.relative_to(ROOT)}: missing anchor {target}")
    for error in errors:
        print(error)
    print(f"{'FAILED' if errors else 'OK'}: {len(errors)} broken links")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
