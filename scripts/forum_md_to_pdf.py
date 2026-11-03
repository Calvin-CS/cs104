#!/usr/bin/env python3
"""
forum_md_to_pdf.py — turn a "Forum" discussion page (the same Markdown file
used to build the course website, front matter and all) into a printable PDF:
the paper a small group receives in class to annotate with their discussion
notes, per the page's own "You'll receive a paper with the discussion
questions below" instruction.

This does NOT modify or require any changes to the .md source — it reads the
existing weeks/NN/forum.md files as-is (front matter included) and adds its
own generous blank annotation space under each discussion question; no
special PDF-only markup is added to the site source.

Usage:
    python scripts/forum_md_to_pdf.py weeks/04/forum.md --out-dir weeks/04

------------------------------------------------------------------------
Expected Markdown shape (this is descriptive, not a dialect you write to)
------------------------------------------------------------------------

---
layout: week
title: "Forum N: <Topic>"        Used for the header if there's no later
week_number: N                   '# ' heading; week_number labels the page.
---

# Forum N: <Topic>                The title shown on the printed page.

One or more intro paragraphs (e.g. "Before class:" / "In class:" notes).
Inline `**bold**`, `*italic*`, `` `code` ``, and [link text](url) (the URL
is dropped, only the link text prints) are all supported.

## Discussion Questions           Recognized by name; starts the numbered,
                                   annotate-able question list.

1. First question text, one source line each.
2. Second question ...

## Submission                     Recognized by name; printed as a plain
                                   closing note, with no annotation space.

A paragraph describing what to hand in.
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
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

# ---------------------------------------------------------------------------
# Layout constants
# ---------------------------------------------------------------------------

MARGIN_LR = 0.85 * inch
MARGIN_TOP = 0.8 * inch
MARGIN_BOTTOM = 0.8 * inch
CONTENT_WIDTH = LETTER[0] - 2 * MARGIN_LR
CONTENT_HEIGHT = LETTER[1] - MARGIN_TOP - MARGIN_BOTTOM

DEFAULT_ANNOTATION_HEIGHT = 85


# ---------------------------------------------------------------------------
# Text helpers (mirrors scripts/quiz_md_to_pdf.py / pogil_md_to_pdf.py)
# ---------------------------------------------------------------------------

def xml_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


INLINE_CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_RE = re.compile(r"\*([^*]+)\*")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def inline_markup(text):
    """Escape raw text, then apply **bold**, *italic*, `code`, and
    [link text](url) (kept as plain text — no href in a printed page)."""
    text = xml_escape(text)
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return "\x00%d\x00" % (len(codes) - 1)

    text = INLINE_CODE_RE.sub(stash, text)
    text = LINK_RE.sub(lambda m: m.group(1), text)
    text = BOLD_RE.sub(lambda m: "<b>%s</b>" % m.group(1), text)
    text = ITALIC_RE.sub(lambda m: "<i>%s</i>" % m.group(1), text)
    text = re.sub(
        "\x00(\\d+)\x00",
        lambda m: '<font face="Courier" size="9.3">%s</font>' % codes[int(m.group(1))],
        text,
    )
    return text


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

RE_FRONT_KV = re.compile(r"^(\w+):\s*(.+)$")
RE_TITLE = re.compile(r"^# (.+)$")
RE_H2 = re.compile(r"^## (.+)$")
RE_QNUM = re.compile(r"^(\d+)\.\s+(.+)$")


def parse_front_matter(lines):
    """If `lines` starts with a '---' front-matter block, consume and return
    (front_matter_dict, remaining_lines). Otherwise return ({}, lines)."""
    if not lines or lines[0].strip() != "---":
        return {}, lines
    fm = {}
    i = 1
    n = len(lines)
    while i < n and lines[i].strip() != "---":
        m = RE_FRONT_KV.match(lines[i].strip())
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
        i += 1
    return fm, lines[i + 1:]


def parse(text):
    raw_lines = text.split("\n")
    front_matter, lines = parse_front_matter(raw_lines)
    n = len(lines)
    i = 0
    doc = {
        "title": front_matter.get("title"),
        "week_number": front_matter.get("week_number"),
        "intro": [],
        "questions": [],
        "submission": [],
    }
    section = "intro"  # 'intro' -> 'questions' -> 'submission'
    para_buf = []

    def flush_para():
        nonlocal para_buf
        if para_buf:
            joined = " ".join(l.strip() for l in para_buf).strip()
            para_buf = []
            if not joined:
                return
            if section == "intro":
                doc["intro"].append(joined)
            elif section == "submission":
                doc["submission"].append(joined)

    while i < n:
        line = lines[i].rstrip("\n")
        stripped = line.strip()

        if stripped == "":
            flush_para()
            i += 1
            continue

        m = RE_TITLE.match(line)
        if m and section == "intro" and not doc["questions"]:
            doc["title"] = m.group(1).strip()
            i += 1
            continue

        m = RE_H2.match(line)
        if m:
            flush_para()
            name = m.group(1).strip().lower()
            if "discussion question" in name:
                section = "questions"
            elif "submission" in name:
                section = "submission"
            i += 1
            continue

        if section == "questions":
            m = RE_QNUM.match(stripped)
            if m:
                doc["questions"].append(m.group(2).strip())
                i += 1
                continue

        para_buf.append(line)
        i += 1

    flush_para()
    return doc


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------

def build_styles():
    ss = getSampleStyleSheet()
    add = ss.add
    add(ParagraphStyle("DocTitle", fontName="Times-Bold", fontSize=15, leading=18))
    add(ParagraphStyle("Meta", fontName="Times-Roman", fontSize=11, leading=14,
                        alignment=2))
    add(ParagraphStyle("NamesLabel", fontName="Times-Roman", fontSize=11, leading=14,
                        alignment=2, spaceBefore=2))
    add(ParagraphStyle("Intro", fontName="Times-Italic", fontSize=10, leading=13,
                        spaceBefore=4, spaceAfter=4))
    add(ParagraphStyle("SectionHeading", fontName="Times-Bold", fontSize=12,
                        leading=15, spaceBefore=10, spaceAfter=4))
    add(ParagraphStyle("Question", fontName="Times-Roman", fontSize=11,
                        leading=14.5, alignment=4, spaceAfter=4))
    add(ParagraphStyle("Submission", fontName="Times-Roman", fontSize=10.5,
                        leading=13.5, alignment=4, spaceAfter=4))
    return ss


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_header(doc, styles):
    title = Paragraph(inline_markup(doc["title"] or "Forum Discussion"), styles["DocTitle"])
    right_stack = []
    if doc.get("week_number"):
        right_stack.append(Paragraph("Week %s" % doc["week_number"], styles["Meta"]))
    right_stack.append(Paragraph("Group members: " + "_" * 30, styles["NamesLabel"]))
    right_stack.append(Paragraph("_" * 42, styles["NamesLabel"]))
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


def render_question(n, text, styles):
    """One KeepTogether segment: the question, then its annotation space —
    never split across a page break."""
    return KeepTogether([
        Paragraph("<b>%d.</b> %s" % (n, inline_markup(text)), styles["Question"]),
        Spacer(1, DEFAULT_ANNOTATION_HEIGHT),
    ])


def build_pdf(doc_data, out_path):
    styles = build_styles()
    story = render_header(doc_data, styles)

    if doc_data["questions"]:
        story.append(Paragraph("Discussion Questions", styles["SectionHeading"]))
        for idx, qtext in enumerate(doc_data["questions"], start=1):
            story.append(render_question(idx, qtext, styles))

    if doc_data["submission"]:
        submission_flow = [Paragraph("Submission", styles["SectionHeading"])]
        for para in doc_data["submission"]:
            submission_flow.append(Paragraph(inline_markup(para), styles["Submission"]))
        story.append(KeepTogether(submission_flow))

    doc = BaseDocTemplate(
        str(out_path), pagesize=LETTER,
        leftMargin=MARGIN_LR, rightMargin=MARGIN_LR,
        topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
        title=doc_data["title"] or "Forum Discussion",
    )
    frame = Frame(MARGIN_LR, MARGIN_BOTTOM, CONTENT_WIDTH, CONTENT_HEIGHT, id="f")

    def _on_page(canv, doc_):
        canv.saveState()
        canv.setFont("Times-Roman", 9)
        canv.setFillColor(colors.Color(0.4, 0.4, 0.4))
        canv.drawCentredString(LETTER[0] / 2, 0.5 * inch, str(doc_.page))
        canv.restoreState()

    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=_on_page)])
    doc.build(story)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path, help="Path to the forum's .md source file")
    ap.add_argument("--out-dir", type=Path, default=None,
                     help="Directory to write the PDF into (default: source's folder)")
    args = ap.parse_args()

    text = args.source.read_text(encoding="utf-8")
    doc_data = parse(text)
    if not doc_data["title"] or not doc_data["questions"]:
        sys.exit("error: could not find a title and/or a '## Discussion Questions' list")

    out_dir = args.out_dir or args.source.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.source.stem}.pdf"
    build_pdf(doc_data, out_path)
    print(f"wrote {out_path}  ({len(doc_data['questions'])} discussion questions)")


if __name__ == "__main__":
    main()
