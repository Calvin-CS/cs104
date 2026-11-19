#!/usr/bin/env python3
"""
pogil_md_to_pdf.py — turn a POGIL activity written in a small Markdown
dialect into a pair of PDFs styled like the ones in pogil/:

    <Name>_Student.pdf   fillable form fields, blank, for students
    <Name>_Teacher.pdf   the same layout with answers baked in (gray text)

Usage:
    python scripts/pogil_md_to_pdf.py pogil/source/Act09-Libraries.md --out-dir pogil

------------------------------------------------------------------------
Markdown dialect
------------------------------------------------------------------------

# <Activity Title>                   First line of the file: the title,
                                      shown on the page-1 cover.

One or more paragraphs of intro text right under the title (blank-line
separated, like normal Markdown paragraphs). Inline `**bold**`, `*italic*`
and `` `code` `` are all supported anywhere body text appears.

## Content Learning Objectives        Exactly these three section names
## Process Skill Goals                are recognized on page 1.
## Facilitation Notes                 Facilitation Notes is teacher-only
                                       and is dropped from the Student PDF.

- One bullet per line under Content Learning Objectives / Process Skill
  Goals. Facilitation Notes is written as plain paragraphs instead.

# Model 1: <Model Title>              Starts a new Model (new page). Models
                                       are numbered by you, not inferred.

A paragraph introducing the model.

```python
a fenced code block, shown with line numbers and light syntax coloring
```

| Header A | Header B |
|---|---|
| given cell text | {{ANSWER::id::cell::-::teacher-only answer text}} |

> A callout / boxed instruction, e.g. "Do not type anything yet!"

### Questions (15 min)                Starts a Questions block; question
                                       numbering is continuous across the
                                       whole document (not reset per Model).

1. A question that ends with an inline answer blank {{ANSWER::q1::inline::170::the answer}}
2. A question with lettered sub-parts and no blank of its own
   a) a sub-part with a short inline blank {{ANSWER::q2a::inline::-::answer}}
   b) a sub-part with a bigger writing box below it {{ANSWER::q2b::block::45::a longer
      answer, kept on one source line}}

The {{ANSWER::id::type::size::answer}} marker must appear at the very end
of the question/sub-part/table-cell text (put the whole thing on one
source line — don't wrap it).

    type   = inline  -> a short field to the right, `size` = width in points
                         (default 170 if `size` is `-`)
             block   -> a full-width box below the text, `size` = height in
                         points (default 40 if `size` is `-`)
             cell    -> fills an entire table cell (used only inside tables)

    answer = the correct answer, shown in gray in the Teacher PDF and
             ignored (left blank) in the Student PDF. Leave it empty for
             an open-ended question — the Teacher PDF then shows
             "(answers will vary)".
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
    Flowable,
    Frame,
    ListFlowable,
    ListItem,
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
MARGIN_TOP = 0.9 * inch
MARGIN_BOTTOM = 0.9 * inch
CONTENT_WIDTH = LETTER[0] - 2 * MARGIN_LR
CONTENT_HEIGHT = LETTER[1] - MARGIN_TOP - MARGIN_BOTTOM

GRAY_ANSWER = colors.Color(0.35, 0.35, 0.35)
GRAY_HEADING = colors.Color(0.45, 0.45, 0.45)
GRAY_BODY = colors.Color(0.45, 0.45, 0.45)
FIELD_BORDER = colors.Color(0.6, 0.6, 0.6)
TABLE_GRID = colors.Color(0.55, 0.55, 0.55)
TABLE_HEADER_BG = colors.Color(1, 0.98, 0.87)
CODE_BG = colors.Color(0.96, 0.96, 0.96)
CODE_BORDER = colors.Color(0.8, 0.8, 0.8)

DEFAULT_INLINE_WIDTH = 170
DEFAULT_BLOCK_HEIGHT = 40

PY_KEYWORDS = {
    "import", "from", "as", "def", "return", "if", "elif", "else", "for",
    "while", "in", "True", "False", "None", "and", "or", "not", "class",
    "with", "try", "except", "pass", "break", "continue", "is", "lambda",
}


# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------

def xml_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


INLINE_CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_RE = re.compile(r"\*([^*]+)\*")


def inline_markup(text):
    """Escape raw text, then apply **bold**, *italic*, `code` markup.

    Inline code is stashed behind placeholders before bold/italic run, so a
    literal `*` inside backticks (e.g. `` `arr * 2` ``) can never be mistaken
    for an italic marker.
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
        if m.group(1):  # comment
            out.append('<font color="#7f7f7f"><i>%s</i></font>' % esc)
        elif m.group(2):  # string literal
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
RE_MODEL = re.compile(r"^# Model (\d+):\s*(.+)$")
RE_H2 = re.compile(r"^## (.+)$")
RE_H3_Q = re.compile(r"^### Questions \(([^)]+)\)\s*$")
RE_BULLET = re.compile(r"^- (.+)$")
RE_QNUM = re.compile(r"^(\d+)\. (.+)$")
RE_SUBITEM = re.compile(r"^\s{2,}([a-z])\) (.+)$")
RE_CALLOUT = re.compile(r"^> (.+)$")
ANSWER_RE = re.compile(
    r"\{\{ANSWER::([\w\-]+)::(inline|block|cell)::([^:]*)::(.*)\}\}\s*$"
)


def parse(text):
    lines = text.split("\n")
    n = len(lines)
    i = 0
    doc = {
        "title": None,
        "intro": [],
        "objectives": [],
        "process_goals": [],
        "facilitation": [],
        "models": [],
    }
    top_section = None
    current_model = None
    qstack = None
    para_buf = []

    def flush_para():
        nonlocal para_buf
        if para_buf:
            joined = " ".join(l.strip() for l in para_buf).strip()
            para_buf = []
            if not joined:
                return
            if current_model is None:
                if top_section == "intro":
                    doc["intro"].append(joined)
                elif top_section == "facilitation":
                    doc["facilitation"].append(joined)
            else:
                current_model["blocks"].append({"type": "para", "text": joined})

    while i < n:
        line = lines[i].rstrip("\n")
        stripped = line.strip()

        if stripped == "":
            flush_para()
            i += 1
            continue

        m = RE_MODEL.match(line)
        if m:
            flush_para()
            qstack = None
            current_model = {
                "number": int(m.group(1)),
                "title": m.group(2).strip(),
                "blocks": [],
            }
            doc["models"].append(current_model)
            top_section = None
            i += 1
            continue

        m = RE_TITLE.match(line)
        if m and doc["title"] is None and current_model is None:
            doc["title"] = m.group(1).strip()
            top_section = "intro"
            i += 1
            continue

        m = RE_H2.match(line)
        if m and current_model is None:
            flush_para()
            name = m.group(1).strip()
            top_section = {
                "Content Learning Objectives": "objectives",
                "Process Skill Goals": "process_goals",
                "Facilitation Notes": "facilitation",
            }.get(name)
            i += 1
            continue

        m = RE_H3_Q.match(line)
        if m and current_model is not None:
            flush_para()
            qstack = None
            current_model["blocks"].append({"type": "qheading", "time": m.group(1).strip()})
            i += 1
            continue

        if stripped.startswith("```"):
            flush_para()
            qstack = None
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i].rstrip("\n"))
                i += 1
            i += 1
            if current_model is not None:
                current_model["blocks"].append({"type": "code", "lines": code_lines})
            continue

        if stripped.startswith("|"):
            flush_para()
            qstack = None
            table_lines = []
            while i < n and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            headers = [c.strip() for c in table_lines[0].strip("|").split("|")]
            rows = [
                [c.strip() for c in rl.strip("|").split("|")]
                for rl in table_lines[2:]
            ]
            if current_model is not None:
                current_model["blocks"].append(
                    {"type": "table", "headers": headers, "rows": rows}
                )
            continue

        m = RE_BULLET.match(line)
        if m and current_model is None:
            item = m.group(1).strip()
            if top_section == "objectives":
                doc["objectives"].append(item)
            elif top_section == "process_goals":
                doc["process_goals"].append(item)
            i += 1
            continue

        m = RE_CALLOUT.match(line)
        if m:
            flush_para()
            qstack = None
            parts = [m.group(1).strip()]
            i += 1
            while i < n and RE_CALLOUT.match(lines[i]):
                parts.append(RE_CALLOUT.match(lines[i]).group(1).strip())
                i += 1
            if current_model is not None:
                current_model["blocks"].append({"type": "callout", "text": " ".join(parts)})
            continue

        m = RE_SUBITEM.match(line)
        if m and current_model is not None and qstack is not None:
            flush_para()
            qstack["sub"].append((m.group(1), m.group(2).strip()))
            i += 1
            continue

        m = RE_QNUM.match(line)
        if m and current_model is not None:
            flush_para()
            q = {"type": "question", "text": m.group(2).strip(), "sub": []}
            current_model["blocks"].append(q)
            qstack = q
            i += 1
            continue

        para_buf.append(line)
        i += 1

    flush_para()
    return doc


# ---------------------------------------------------------------------------
# Form-field flowable
# ---------------------------------------------------------------------------

class TextFieldFlowable(Flowable):
    """A blank, fillable AcroForm text field sized like a normal flowable."""

    def __init__(self, width, height, name, multiline=False):
        super().__init__()
        self.width = width
        self.height = height
        self.name = name
        self.multiline = multiline

    def wrap(self, availWidth, availHeight):
        self.width = min(self.width, availWidth)
        return (self.width, self.height)

    def draw(self):
        self.canv.acroForm.textfield(
            name=self.name,
            value="",
            x=0,
            y=0,
            width=self.width,
            height=self.height,
            borderStyle="solid",
            borderWidth=0.75,
            borderColor=FIELD_BORDER,
            fillColor=colors.white,
            textColor=colors.black,
            fontName="Helvetica",
            fontSize=9,
            forceBorder=True,
            relative=True,
            fieldFlags="multiline" if self.multiline else "",
        )


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------

def build_styles():
    ss = getSampleStyleSheet()
    add = ss.add
    add(ParagraphStyle("DocTitle", fontName="Times-Roman", fontSize=22, leading=26,
                        alignment=1, spaceAfter=4))
    add(ParagraphStyle("H2", fontName="Times-Bold", fontSize=12.5, leading=15,
                        spaceBefore=4, spaceAfter=2))
    add(ParagraphStyle("H2Gray", fontName="Times-Bold", fontSize=12.5, leading=15,
                        spaceBefore=4, spaceAfter=2, textColor=GRAY_HEADING))
    add(ParagraphStyle("ItalicSmall", fontName="Times-Italic", fontSize=10.5,
                        leading=13, spaceAfter=3))
    add(ParagraphStyle("Body", fontName="Times-Roman", fontSize=10.5, leading=13.5,
                        alignment=4, spaceAfter=4))
    add(ParagraphStyle("BodyGray", parent=ss["Body"], textColor=GRAY_BODY))
    add(ParagraphStyle("BulletItem", parent=ss["Body"], spaceAfter=2))
    add(ParagraphStyle("ModelHeading", fontName="Times-Bold", fontSize=15,
                        leading=18, spaceBefore=2, spaceAfter=8))
    add(ParagraphStyle("QHeading", fontName="Times-Bold", fontSize=11.5, leading=14))
    add(ParagraphStyle("QHeadingRight", fontName="Times-Roman", fontSize=10.5,
                        leading=14, alignment=2))
    add(ParagraphStyle("Question", fontName="Times-Roman", fontSize=10.5,
                        leading=13.5, spaceBefore=6))
    add(ParagraphStyle("SubQuestion", parent=ss["Question"], leftIndent=18,
                        spaceBefore=3))
    add(ParagraphStyle("TableHeader", fontName="Times-Bold", fontSize=10,
                        leading=12, alignment=1))
    add(ParagraphStyle("TableCell", fontName="Courier", fontSize=9, leading=11))
    add(ParagraphStyle("Callout", fontName="Times-Bold", fontSize=10.5,
                        leading=13, alignment=1))
    add(ParagraphStyle("CodeBlock", fontName="Courier", fontSize=9, leading=11.5))
    return ss


# ---------------------------------------------------------------------------
# Rendering: page 1
# ---------------------------------------------------------------------------

def bullet_list(items, styles):
    return ListFlowable(
        [ListItem(Paragraph(inline_markup(it), styles["BulletItem"]), leftIndent=14)
         for it in items],
        bulletType="bullet", start="•", leftIndent=10,
    )


def render_page1(doc, mode, styles):
    flow = [Paragraph(inline_markup(doc["title"]), styles["DocTitle"]), Spacer(1, 10)]
    for para in doc["intro"]:
        flow.append(Paragraph(inline_markup(para), styles["Body"]))
    flow.append(Spacer(1, 4))
    flow.append(Paragraph("Content Learning Objectives", styles["H2"]))
    flow.append(Paragraph("After completing this activity, students should be able to:",
                           styles["ItalicSmall"]))
    flow.append(bullet_list(doc["objectives"], styles))
    flow.append(Spacer(1, 6))
    flow.append(Paragraph("Process Skill Goals", styles["H2"]))
    flow.append(Paragraph("During the activity, students should make progress toward:",
                           styles["ItalicSmall"]))
    flow.append(bullet_list(doc["process_goals"], styles))
    if mode == "teacher" and doc["facilitation"]:
        flow.append(Spacer(1, 6))
        flow.append(Paragraph("Facilitation Notes", styles["H2Gray"]))
        for para in doc["facilitation"]:
            flow.append(Paragraph(inline_markup(para), styles["BodyGray"]))
    return flow


# ---------------------------------------------------------------------------
# Rendering: models
# ---------------------------------------------------------------------------

def render_code_block(lines, styles):
    body_lines = []
    for idx, line in enumerate(lines, start=1):
        num = '<font color="#9a9a9a">%3d </font>' % idx
        body_lines.append(num + highlight_line(line))
    xp = XPreformatted("\n".join(body_lines), styles["CodeBlock"])
    t = Table([[xp]], colWidths=[CONTENT_WIDTH - 16])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, CODE_BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def render_callout(text, styles):
    p = Paragraph("<b>%s</b>" % inline_markup(text), styles["Callout"])
    t = Table([[p]], colWidths=[CONTENT_WIDTH])
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.75, colors.Color(0.3, 0.3, 0.3)),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def render_qheading(time_label, styles):
    left = Paragraph("<b>Questions (%s)</b>" % inline_markup(time_label), styles["QHeading"])
    right = Paragraph("Start time: " + "_" * 22, styles["QHeadingRight"])
    t = Table([[left, right]], colWidths=[CONTENT_WIDTH * 0.5, CONTENT_WIDTH * 0.5])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return t


def render_table(block, mode, styles):
    headers = block["headers"]
    rows = block["rows"]
    ncols = len(headers)
    colw = CONTENT_WIDTH / ncols
    data = [[Paragraph(inline_markup(h), styles["TableHeader"]) for h in headers]]
    for row in rows:
        rendered = []
        for cell in row:
            m = ANSWER_RE.search(cell)
            if not m:
                rendered.append(Paragraph(inline_markup(cell), styles["TableCell"]))
                continue
            field_id, ftype, size, answer = m.groups()
            if mode == "teacher":
                ans = answer.strip()
                txt = xml_escape(ans) if ans else "&nbsp;"
                rendered.append(Paragraph(
                    '<font color="#5a5a5a">%s</font>' % txt, styles["TableCell"]))
            else:
                rendered.append(TextFieldFlowable(colw - 10, 16, field_id))
        data.append(rendered)
    t = Table(data, colWidths=[colw] * ncols)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.6, TABLE_GRID),
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def place_answer(markup_text, ftype, size, field_id, answer, mode, styles, avail_width):
    """Resolve one {{ANSWER}} marker into the flowable(s) that follow the
    question/sub-part text `markup_text` (already bold-labelled markup)."""
    base_style = styles["Question"] if avail_width == CONTENT_WIDTH else styles["SubQuestion"]
    if mode == "teacher":
        ans = (answer or "").strip()
        disp = xml_escape(ans) if ans else "<i>(answers will vary)</i>"
        if ftype == "block":
            return [Paragraph(markup_text, base_style),
                    Paragraph('<font color="#5a5a5a">%s</font>' % disp, base_style)]
        return [Paragraph(markup_text + '&nbsp;&nbsp;<font color="#5a5a5a">%s</font>' % disp,
                           base_style)]
    # student
    if ftype == "block":
        height = float(size) if size not in ("", "-") else DEFAULT_BLOCK_HEIGHT
        field = TextFieldFlowable(avail_width, height, field_id, multiline=True)
        return [Paragraph(markup_text, base_style), Spacer(1, 3), field]
    width = float(size) if size not in ("", "-") else DEFAULT_INLINE_WIDTH
    field = TextFieldFlowable(width, 16, field_id)
    para = Paragraph(markup_text, base_style)
    row = Table([[para, field]], colWidths=[avail_width - width - 8, width])
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 4),
        ("RIGHTPADDING", (1, 0), (1, 0), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return [row]


def render_question(q, mode, styles, qcounter):
    n = qcounter["n"]
    qcounter["n"] += 1
    flows = []

    m = ANSWER_RE.search(q["text"] or "")
    if m:
        clean = q["text"][:m.start()].rstrip()
        markup = "<b>%d.</b> %s" % (n, inline_markup(clean))
        field_id, ftype, size, answer = m.groups()
        flows.extend(place_answer(markup, ftype, size, field_id, answer, mode, styles, CONTENT_WIDTH))
    else:
        markup = "<b>%d.</b> %s" % (n, inline_markup(q["text"] or ""))
        flows.append(Paragraph(markup, styles["Question"]))

    sub_width = CONTENT_WIDTH - 18
    for letter, subtext in q.get("sub", []):
        m = ANSWER_RE.search(subtext)
        if m:
            clean = subtext[:m.start()].rstrip()
            markup = "<b>%s)</b> %s" % (letter, inline_markup(clean))
            field_id, ftype, size, answer = m.groups()
            flows.extend(place_answer(markup, ftype, size, field_id, answer, mode, styles, sub_width))
        else:
            markup = "<b>%s)</b> %s" % (letter, inline_markup(subtext))
            flows.append(Paragraph(markup, styles["SubQuestion"]))
    return flows


def render_model(model, mode, styles, qcounter):
    flow = [
        Paragraph("Model %d&nbsp;&nbsp;&nbsp;%s" % (model["number"], inline_markup(model["title"])),
                  styles["ModelHeading"]),
    ]
    for block in model["blocks"]:
        t = block["type"]
        if t == "para":
            flow.append(Paragraph(inline_markup(block["text"]), styles["Body"]))
        elif t == "code":
            flow.append(render_code_block(block["lines"], styles))
            flow.append(Spacer(1, 6))
        elif t == "table":
            flow.append(render_table(block, mode, styles))
            flow.append(Spacer(1, 6))
        elif t == "callout":
            flow.append(render_callout(block["text"], styles))
            flow.append(Spacer(1, 6))
        elif t == "qheading":
            flow.append(render_qheading(block["time"], styles))
        elif t == "question":
            flow.extend(render_question(block, mode, styles, qcounter))
    return flow


# ---------------------------------------------------------------------------
# Page furniture + document assembly
# ---------------------------------------------------------------------------

def make_on_page(mode, title):
    def _on_page(canv, doc_):
        canv.saveState()
        canv.setFont("Times-Roman", 9)
        canv.setFillColor(colors.Color(0.4, 0.4, 0.4))
        canv.drawCentredString(LETTER[0] / 2, 0.5 * inch, str(doc_.page))
        if doc_.page == 1:
            canv.setFont("Times-Italic", 8)
            label = "Teacher Key" if mode == "teacher" else "Student Copy"
            canv.drawCentredString(LETTER[0] / 2, 0.65 * inch,
                                    "CS-104 POGIL Activity — %s (%s)" % (title, label))
        canv.restoreState()
    return _on_page


def build_pdf(doc_data, mode, out_path):
    styles = build_styles()
    qcounter = {"n": 1}
    story = render_page1(doc_data, mode, styles)
    story.append(PageBreak())
    for idx, model in enumerate(doc_data["models"]):
        story.extend(render_model(model, mode, styles, qcounter))
        if idx < len(doc_data["models"]) - 1:
            story.append(PageBreak())

    doc = BaseDocTemplate(
        str(out_path), pagesize=LETTER,
        leftMargin=MARGIN_LR, rightMargin=MARGIN_LR,
        topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
        title=doc_data["title"],
    )
    frame = Frame(MARGIN_LR, MARGIN_BOTTOM, CONTENT_WIDTH, CONTENT_HEIGHT, id="f")
    doc.addPageTemplates([
        PageTemplate(id="main", frames=[frame], onPage=make_on_page(mode, doc_data["title"]))
    ])
    doc.build(story)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path, help="Path to the activity's .md source file")
    ap.add_argument("--out-dir", type=Path, default=None,
                     help="Directory to write the two PDFs into (default: source's folder)")
    args = ap.parse_args()

    text = args.source.read_text(encoding="utf-8")
    doc_data = parse(text)
    if not doc_data["title"] or not doc_data["models"]:
        sys.exit("error: could not find a title and/or any '# Model N: ...' sections")

    out_dir = args.out_dir or args.source.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.source.stem

    student_path = out_dir / f"{stem}_Student.pdf"
    teacher_path = out_dir / f"{stem}_Teacher.pdf"
    build_pdf(doc_data, "student", student_path)
    build_pdf(doc_data, "teacher", teacher_path)
    print(f"wrote {student_path}")
    print(f"wrote {teacher_path}")


if __name__ == "__main__":
    main()
