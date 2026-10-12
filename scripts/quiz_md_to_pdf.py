#!/usr/bin/env python3
"""
quiz_md_to_pdf.py — turn a paper quiz written in a small Markdown dialect
into a clean, printable PDF (no fillable fields — this is meant to be
printed and answered with a pen), styled like the course's existing
quiz1a.docx/quiz1b.docx etc. in practices/.

Usage:
    python scripts/quiz_md_to_pdf.py weeks/03/quiz01.md --out-dir weeks/03

    A single source file can hold TWO versions of a quiz (see [[VERSION A]]
    below) — in that case this writes two PDFs, one per version, named
    <stem>a.pdf and <stem>b.pdf (e.g. quiz01.md -> quiz01a.pdf, quiz01b.pdf).
    A source file with no [[VERSION ...]] blocks writes a single <stem>.pdf,
    as before.

------------------------------------------------------------------------
Markdown dialect
------------------------------------------------------------------------

# <Quiz Title>                      First line: shown bold, top-left.

meta: <term/semester text>          Shown top-right, opposite the title,
                                     on the same header line.

One paragraph of intro text under the header (e.g. the standard
"this is an in-class, closed-book quiz..." notice).

## Q (<N> points)                   Starts a new question, numbered
                                     automatically (1., 2., ...) with its
                                     point value shown, e.g. "1. (4 points)".

Prose for the question. Inline `**bold**`, `*italic*`, and `` `code` ``
are all supported.

```python
a fenced code block, shown in monospace, no line numbers
```

[[BLANK height=140]]                Blank vertical writing space (in
                                     points) for a handwritten answer.
                                     Omit `height=NN` for a default of 60.

[[PAIRS]]                           A 2-column grid of short expressions,
EX: >>> 'a' + 'b' -> 'ab'           each with blank space below it for a
>>> 4 ** 2                          written answer. A line prefixed with
>>> 9 % 5                           "EX: " is a worked example instead —
[[/PAIRS]]                          its answer (after "->") is printed in
                                     italics rather than left blank.

[[VERSION A]] ... [[/VERSION]]      Marks content that belongs ONLY to
[[VERSION B]] ... [[/VERSION]]      version A (or B) of the quiz — wrap
                                     around a paragraph, a code block, a
                                     [[BLANK]], a [[PAIRS]] block, or any
                                     mix of these. Content outside any
                                     [[VERSION ...]] block is shared by
                                     both versions. These never nest, and
                                     each [[VERSION X]] must be closed with
                                     [[/VERSION]] before the next one opens.
                                     A file with no [[VERSION ...]] blocks
                                     at all produces a single, un-suffixed
                                     PDF, exactly as before.
------------------------------------------------------------------------
"""

import argparse
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    XPreformatted,
)

# ---------------------------------------------------------------------------
# Layout constants
# ---------------------------------------------------------------------------

MARGIN_LR = 0.85 * inch
MARGIN_TOP = 0.8 * inch
MARGIN_BOTTOM = 0.8 * inch
CONTENT_WIDTH = LETTER[0] - 2 * MARGIN_LR
CONTENT_HEIGHT = LETTER[1] - MARGIN_TOP - MARGIN_BOTTOM

CODE_BG = colors.Color(0.96, 0.96, 0.96)
CODE_BORDER = colors.Color(0.8, 0.8, 0.8)
DEFAULT_BLANK_HEIGHT = 60
DEFAULT_PAIR_BLANK_HEIGHT = 34

PY_KEYWORDS = {
    "import", "from", "as", "def", "return", "if", "elif", "else", "for",
    "while", "in", "True", "False", "None", "and", "or", "not", "class",
    "with", "try", "except", "pass", "break", "continue", "is", "lambda",
}


# ---------------------------------------------------------------------------
# Text helpers (mirrors scripts/pogil_md_to_pdf.py)
# ---------------------------------------------------------------------------

def xml_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


INLINE_CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_RE = re.compile(r"\*([^*]+)\*")


def inline_markup(text):
    """Escape raw text, then apply **bold**, *italic*, `code` markup.

    Inline code is stashed behind placeholders before bold/italic run, so a
    literal `*` inside backticks can never be mistaken for an italic marker.
    """
    text = xml_escape(text)
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return "\x00%d\x00" % (len(codes) - 1)

    text = INLINE_CODE_RE.sub(stash, text)
    text = BOLD_RE.sub(lambda m: "<b>%s</b>" % m.group(1), text)
    text = ITALIC_RE.sub(lambda m: "<i>%s</i>" % m.group(1), text)
    text = re.sub(
        "\x00(\\d+)\x00",
        lambda m: '<font face="Courier" size="9.3">%s</font>' % codes[int(m.group(1))],
        text,
    )
    return text


TOKEN_RE = re.compile(
    r"(#.*$)|(\"[^\"]*\"|'[^']*')|(\b[a-zA-Z_][a-zA-Z0-9_]*\b)"
)


def highlight_line(line):
    """Light Python syntax coloring for one line of code (returns markup)."""
    out = []
    pos = 0
    for m in TOKEN_RE.finditer(line):
        out.append(xml_escape(line[pos:m.start()]))
        text = m.group(0)
        esc = xml_escape(text)
        if m.group(1):
            out.append('<font color="#7f7f7f"><i>%s</i></font>' % esc)
        elif m.group(2):
            out.append('<font color="#2e8b2e">%s</font>' % esc)
        elif m.group(3) and text in PY_KEYWORDS:
            out.append('<font color="#c9640c">%s</font>' % esc)
        else:
            out.append(esc)
        pos = m.end()
    out.append(xml_escape(line[pos:]))
    return "".join(out)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

RE_TITLE = re.compile(r"^# (.+)$")
RE_META = re.compile(r"^meta:\s*(.+)$")
RE_QHEAD = re.compile(r"^## Q \((\d+) points?\)\s*(.*)$")
RE_BLANK = re.compile(r"^\[\[BLANK(?:\s+height=(\d+))?\s*\]\]$")
RE_PAIRS_START = re.compile(r"^\[\[PAIRS\]\]$")
RE_PAIRS_END = re.compile(r"^\[\[/PAIRS\]\]$")
RE_EXAMPLE = re.compile(r"^EX:\s*(.+?)\s*->\s*(.+)$")
RE_VERSION_START = re.compile(r"^\[\[VERSION\s+([A-Za-z])\]\]$")
RE_VERSION_END = re.compile(r"^\[\[/VERSION\]\]$")


def parse(text):
    lines = text.split("\n")
    n = len(lines)
    i = 0
    doc = {"title": None, "meta": "", "intro": [], "questions": []}
    current_q = None
    current_version = None  # None = shared by all versions; else 'A', 'B', ...
    para_buf = []

    def flush_para():
        nonlocal para_buf
        if para_buf:
            joined = " ".join(l.strip() for l in para_buf).strip()
            para_buf = []
            if not joined:
                return
            if current_q is None:
                doc["intro"].append(joined)
            else:
                current_q["blocks"].append(
                    {"type": "para", "text": joined, "version": current_version})

    while i < n:
        line = lines[i].rstrip("\n")
        stripped = line.strip()
        lineno = i + 1

        if stripped == "":
            flush_para()
            i += 1
            continue

        m = RE_TITLE.match(line)
        if m and doc["title"] is None:
            doc["title"] = m.group(1).strip()
            i += 1
            continue

        m = RE_META.match(line)
        if m:
            doc["meta"] = m.group(1).strip()
            i += 1
            continue

        m = RE_QHEAD.match(line)
        if m:
            flush_para()
            if current_version is not None:
                sys.exit(f"error: line {lineno}: new question started before "
                         f"[[/VERSION]] closed [[VERSION {current_version}]]")
            current_q = {"points": int(m.group(1)), "title": m.group(2).strip(), "blocks": []}
            doc["questions"].append(current_q)
            i += 1
            continue

        m = RE_VERSION_START.match(stripped)
        if m:
            flush_para()
            if current_version is not None:
                sys.exit(f"error: line {lineno}: [[VERSION {m.group(1)}]] opened while "
                         f"[[VERSION {current_version}]] is still open — these don't nest")
            current_version = m.group(1).upper()
            i += 1
            continue

        if RE_VERSION_END.match(stripped):
            flush_para()
            if current_version is None:
                sys.exit(f"error: line {lineno}: [[/VERSION]] with no matching [[VERSION ...]]")
            current_version = None
            i += 1
            continue

        if stripped.startswith("```"):
            flush_para()
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i].rstrip("\n"))
                i += 1
            i += 1
            if current_q is not None:
                current_q["blocks"].append(
                    {"type": "code", "lines": code_lines, "version": current_version})
            continue

        m = RE_BLANK.match(stripped)
        if m:
            flush_para()
            height = int(m.group(1)) if m.group(1) else DEFAULT_BLANK_HEIGHT
            if current_q is not None:
                current_q["blocks"].append(
                    {"type": "blank", "height": height, "version": current_version})
            i += 1
            continue

        if RE_PAIRS_START.match(stripped):
            flush_para()
            items = []
            i += 1
            while i < n and not RE_PAIRS_END.match(lines[i].strip()):
                item_line = lines[i].strip()
                if item_line:
                    ex = RE_EXAMPLE.match(item_line)
                    if ex:
                        items.append({"expr": ex.group(1).strip(), "answer": ex.group(2).strip()})
                    else:
                        items.append({"expr": item_line, "answer": None})
                i += 1
            i += 1  # skip [[/PAIRS]]
            if current_q is not None:
                current_q["blocks"].append(
                    {"type": "pairs", "items": items, "version": current_version})
            continue

        para_buf.append(line)
        i += 1

    flush_para()
    if current_version is not None:
        sys.exit(f"error: file ended with [[VERSION {current_version}]] still open "
                  f"(missing [[/VERSION]])")
    return doc


def versions_used(doc):
    """Return the sorted set of version letters ('A', 'B', ...) actually used
    in doc, or an empty set if the file has no [[VERSION ...]] blocks at all."""
    return sorted({
        block["version"]
        for q in doc["questions"]
        for block in q["blocks"]
        if block.get("version")
    })


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------

def build_styles():
    ss = getSampleStyleSheet()
    add = ss.add
    add(ParagraphStyle("QuizTitle", fontName="Times-Bold", fontSize=15, leading=18))
    add(ParagraphStyle("QuizMeta", fontName="Times-Roman", fontSize=11, leading=14,
                        alignment=2))
    add(ParagraphStyle("QuizName", fontName="Times-Roman", fontSize=11, leading=14,
                        alignment=2, spaceBefore=2))
    add(ParagraphStyle("Intro", fontName="Times-Italic", fontSize=10, leading=13,
                        spaceBefore=6, spaceAfter=8))
    add(ParagraphStyle("QHeading", fontName="Times-Bold", fontSize=11, leading=14,
                        spaceBefore=8, spaceAfter=3))
    add(ParagraphStyle("Body", fontName="Times-Roman", fontSize=11, leading=14.5,
                        alignment=4, spaceAfter=4))
    add(ParagraphStyle("PairExpr", fontName="Courier", fontSize=10, leading=13))
    add(ParagraphStyle("PairAnswer", fontName="Times-Italic", fontSize=9, leading=11,
                        textColor=colors.Color(0.4, 0.4, 0.4)))
    add(ParagraphStyle("CodeBlock", fontName="Courier", fontSize=9.5, leading=12))
    return ss


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_header(doc, styles):
    title = Paragraph(inline_markup(doc["title"]), styles["QuizTitle"])
    right_stack = [Paragraph(inline_markup(doc["meta"]), styles["QuizMeta"])] if doc["meta"] else []
    right_stack.append(Paragraph("Name: " + "_" * 30, styles["QuizName"]))
    header = Table(
        [[title, right_stack]],
        colWidths=[CONTENT_WIDTH * 0.45, CONTENT_WIDTH * 0.55],
    )
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    flow = [header]
    for para in doc["intro"]:
        flow.append(Paragraph(inline_markup(para), styles["Intro"]))
    return flow


def render_code_block(lines, styles):
    body = "\n".join(highlight_line(l) for l in lines)
    xp = XPreformatted(body, styles["CodeBlock"])
    t = Table([[xp]], colWidths=[CONTENT_WIDTH - 16])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, CODE_BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def render_pairs(items, styles):
    ncols = 2
    colw = CONTENT_WIDTH / ncols
    rows = []
    row = []
    for item in items:
        cell_flow = [Paragraph(inline_markup(item["expr"]), styles["PairExpr"])]
        if item["answer"] is not None:
            cell_flow.append(Paragraph(
                inline_markup(item["answer"]) + "  <i>&mdash; example answer</i>",
                styles["PairAnswer"]))
        else:
            cell_flow.append(Spacer(1, DEFAULT_PAIR_BLANK_HEIGHT))
        row.append(cell_flow)
        if len(row) == ncols:
            rows.append(row)
            row = []
    if row:
        while len(row) < ncols:
            row.append("")
        rows.append(row)
    t = Table(rows, colWidths=[colw] * ncols)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def render_question(n, q, styles, version=None):
    """Render one question as a list of SEGMENTS (each a list of flowables),
    keeping only blocks shared by all versions (block["version"] is None)
    plus blocks tagged for the requested `version` letter. Pass version=None
    to render every block (used for single-version files, where no block
    ever has a version tag anyway).

    A new segment starts right after each [[BLANK]] (the natural end of one
    self-contained prompt + its answer space) and always right after the
    question heading if no blank has appeared yet. The caller wraps each
    segment in KeepTogether so a page break can only ever fall BETWEEN
    segments — never in the middle of a prompt, a code block, or between a
    prompt and its own answer space.
    """
    points = q["points"]
    unit = "point" if points == 1 else "points"
    segments = []
    current = [Paragraph("%d. (%d %s)" % (n, points, unit), styles["QHeading"])]
    for block in q["blocks"]:
        block_version = block.get("version")
        if block_version is not None and block_version != version:
            continue
        t = block["type"]
        if t == "para":
            current.append(Paragraph(inline_markup(block["text"]), styles["Body"]))
        elif t == "code":
            current.append(render_code_block(block["lines"], styles))
            current.append(Spacer(1, 4))
        elif t == "blank":
            current.append(Spacer(1, block["height"]))
            segments.append(current)
            current = []
        elif t == "pairs":
            current.append(render_pairs(block["items"], styles))
    if current:
        segments.append(current)
    return segments


# ---------------------------------------------------------------------------
# Page furniture + document assembly
# ---------------------------------------------------------------------------

def make_on_page():
    def _on_page(canv, doc_):
        canv.saveState()
        canv.setFont("Times-Roman", 9)
        canv.setFillColor(colors.Color(0.4, 0.4, 0.4))
        canv.drawCentredString(LETTER[0] / 2, 0.5 * inch, str(doc_.page))
        canv.restoreState()
    return _on_page


def build_pdf(doc_data, out_path, version=None):
    styles = build_styles()
    story = render_header(doc_data, styles)
    for idx, q in enumerate(doc_data["questions"], start=1):
        for segment in render_question(idx, q, styles, version=version):
            story.append(KeepTogether(segment))

    doc = BaseDocTemplate(
        str(out_path), pagesize=LETTER,
        leftMargin=MARGIN_LR, rightMargin=MARGIN_LR,
        topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
        title=doc_data["title"],
    )
    frame = Frame(MARGIN_LR, MARGIN_BOTTOM, CONTENT_WIDTH, CONTENT_HEIGHT, id="f")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=make_on_page())])
    doc.build(story)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path, help="Path to the quiz's .md source file")
    ap.add_argument("--out-dir", type=Path, default=None,
                     help="Directory to write the PDF into (default: source's folder)")
    args = ap.parse_args()

    text = args.source.read_text(encoding="utf-8")
    doc_data = parse(text)
    if not doc_data["title"] or not doc_data["questions"]:
        sys.exit("error: could not find a title and/or any '## Q (...)' questions")

    total_points = sum(q["points"] for q in doc_data["questions"])
    n_questions = len(doc_data["questions"])

    out_dir = args.out_dir or args.source.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    versions = versions_used(doc_data)
    if versions:
        for letter in versions:
            out_path = out_dir / f"{args.source.stem}{letter.lower()}.pdf"
            build_pdf(doc_data, out_path, version=letter)
            print(f"wrote {out_path}  ({n_questions} questions, {total_points} points, "
                  f"version {letter})")
    else:
        out_path = out_dir / f"{args.source.stem}.pdf"
        build_pdf(doc_data, out_path)
        print(f"wrote {out_path}  ({n_questions} questions, {total_points} points)")


if __name__ == "__main__":
    main()
