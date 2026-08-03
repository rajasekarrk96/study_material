"""
Learning OS — Markdown pre-processing helpers.
The `markdown` package (classic Python-Markdown, not CommonMark) requires a
blank line before a list to recognize it as a new list. Curriculum content
authored without that blank line has its list items silently swallowed into
the preceding paragraph as plain text.
"""
import re
from html import escape

_LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
_MERMAID_FENCE_RE = re.compile(
    r"^[ \t]*```mermaid[ \t]*\r?\n(?P<diagram>.*?)[ \t]*```[ \t]*$",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)


def render_mermaid_blocks(text: str) -> str:
    """Convert fenced Mermaid source into elements Mermaid.js can render.

    Diagram text is HTML-escaped because the resulting block is later marked
    safe by the Jinja template after Markdown conversion.
    """
    return _MERMAID_FENCE_RE.sub(
        lambda match: (
            '\n\n<pre class="mermaid">\n'
            f'{escape(match.group("diagram").strip(), quote=False)}\n'
            "</pre>\n\n"
        ),
        text,
    )


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
