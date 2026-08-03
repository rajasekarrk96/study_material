"""
Learning OS — Markdown pre-processing helpers.
The `markdown` package (classic Python-Markdown, not CommonMark) requires a
blank line before a list to recognize it as a new list. Curriculum content
authored without that blank line has its list items silently swallowed into
the preceding paragraph as plain text.
"""
import re

_LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")


def insert_blank_lines_before_lists(text: str) -> str:
    """Insert a blank line before any list item line that immediately follows
    non-list, non-blank prose, so it's recognized as a list start."""
    lines = text.split("\n")
    out = []
    for line in lines:
        if _LIST_ITEM_RE.match(line) and out and out[-1].strip() and not _LIST_ITEM_RE.match(out[-1]):
            out.append("")
        out.append(line)
    return "\n".join(out)
