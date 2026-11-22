import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_abstract_docx(output_path="AI_Study_Hub_Abstract.docx"):
    doc = docx.Document()

    # Standard Page Setup: Letter (8.5 x 11 in) with 1.0 inch margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)

    # Base Normal Style: Times New Roman, 11pt, pure black
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)

    # Helper function for adding styled paragraphs
    def add_p(text='', bold=False, italic=False, size=11, align=WD_ALIGN_PARAGRAPH.LEFT, 
              space_before=0, space_after=0, line_spacing=1.15):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        if text:
            run = p.add_run(text)
            run.bold = bold
            run.italic = italic
            run.font.name = 'Times New Roman'
            run.font.size = Pt(size)
            run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    # 1. Header Block (Centered)
    add_p('PROJECT REQUIREMENT DOCUMENT', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p('7th Semester', bold=False, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    # 2. Project Title (Centered, Bold, 13pt)
    add_p('AI Study Hub \u2013 Context-Aware Retrieval-Augmented Generation Platform for Multimodal Academic Learning & Automated Study Synthesis', 
          bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

    # 3. Abstract Heading (Left-aligned, Bold, 12pt)
    add_p('Abstract', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=6)

    # 4. Abstract Paragraph (Justified, 10.5pt, 1.15 line spacing)
    abstract_text = (
        "Acquiring and revising structured academic knowledge from diverse course materials is a slow, "
        "cognitively demanding process: learners must navigate fragmented document formats, manually cross-reference concepts, "
        "extract key definitions, and synthesize self-assessment materials for revision. Conventional Retrieval-Augmented "
        "Generation (RAG) systems and standard Large Language Models (LLMs) only partially address this; standalone LLMs suffer "
        "from domain hallucinations and lack page-level source provenance, while basic single-query RAG pipelines lack multi-format "
        "visual awareness, struggle with conversational continuity, and cannot automatically generate active recall study aids. "
        "The AI Study Hub is proposed as an intelligent, context-aware RAG platform and automated active learning system that "
        "streamlines document-grounded study workflows for students and educators. The platform ingests heterogeneous study resources "
        "(PDFs, DOCX, and TXT) through a dual-engine architecture: a high-throughput local parser for rapid ingestion and a Gemini 2.5 "
        "Flash multimodal vision engine for layout-aware parsing of mathematical formulas, tables, and slide decks. Documents are partitioned "
        "via hierarchical recursive character chunking and converted into dense vector representations using FastEmbed ONNX-quantized models "
        "(all-MiniLM-L6-v2), indexed in a scalable PostgreSQL/Supabase database utilizing pgvector with user-level isolation. For information "
        "retrieval, the system performs cosine similarity search augmented by a neural cross-encoder re-ranking pipeline (ms-marco-MiniLM) "
        "and Reciprocal Rank Fusion (RRF) to prioritize high-relevance candidates. A conversational RAG assistant powered by Gemini 2.5 Flash "
        "reformulates multi-turn queries, enforces strict context bounds to eliminate hallucinations, and provides verifiable page-level citation anchors. "
        "Beyond question answering, the system autonomously synthesizes structured flashcard decks and adaptive multiple-choice quizzes with explanations, "
        "exportable to printable PDFs and native Anki (.apkg) decks, complemented by integrated Web Speech Text-to-Speech (TTS) for auditory revision. "
        "The application is built on a responsive Next.js 16/TypeScript frontend with Supabase authentication and a high-performance asynchronous Python "
        "FastAPI backend. The main contribution of this project is the end-to-end integration of multimodal document ingestion, cross-encoder re-ranked retrieval, "
        "source-grounded conversational synthesis, and automated active recall generation. The project also proposes an experimental evaluation comparing a baseline "
        "LLM-only approach, a standard single-vector RAG approach, and the proposed hybrid re-ranked RAG architecture across retrieval precision, citation accuracy, "
        "answer faithfulness, and study material utility. This document is the first submission of the project and defines its requirements, scope, architecture, "
        "and implementation plan ahead of detailed design and development."
    )
    add_p(abstract_text, size=10.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=14, line_spacing=1.15)

    # 5. Keywords (Justified, 10.5pt, Italic terms)
    p_kw = doc.add_paragraph()
    p_kw.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_kw.paragraph_format.space_before = Pt(0)
    p_kw.paragraph_format.space_after = Pt(36)
    p_kw.paragraph_format.line_spacing = 1.15

    run_kw_label = p_kw.add_run('Keywords: ')
    run_kw_label.bold = True
    run_kw_label.italic = True
    run_kw_label.font.name = 'Times New Roman'
    run_kw_label.font.size = Pt(10.5)

    run_kw_text = p_kw.add_run(
        'Retrieval-Augmented Generation (RAG), Academic Study Hub, FastEmbed Embeddings, '
        'Cross-Encoder Re-Ranking, pgvector, Supabase, Gemini 2.5 Flash, Multimodal Document Parsing, '
        'Active Recall Synthesis, Anki Deck Export, Text-to-Speech Accessibility'
    )
    run_kw_text.italic = True
    run_kw_text.font.name = 'Times New Roman'
    run_kw_text.font.size = Pt(10.5)

    # 6. Bottom Signatures and Student details (2-column borderless table)
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Widths: 3.25 inches each (total 6.5 inches across 1-inch margins)
    table.columns[0].width = Inches(3.25)
    table.columns[1].width = Inches(3.25)

    # Clear borders XML
    tblPr = table._tbl.tblPr
    borders_xml = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        '  <w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
        '  <w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
        '  <w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
        '  <w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
        '  <w:insideH w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
        '  <w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
        '</w:tblBorders>'
    )
    tblPr.append(borders_xml)

    cell_left = table.cell(0, 0)
    cell_right = table.cell(0, 1)

    cell_left.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
    cell_right.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM

    # Left cell: (Signature of Guide)
    p_sig = cell_left.paragraphs[0]
    p_sig.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_sig.paragraph_format.space_before = Pt(0)
    p_sig.paragraph_format.space_after = Pt(0)
    run_sig = p_sig.add_run('(Signature of Guide)')
    run_sig.font.name = 'Times New Roman'
    run_sig.font.size = Pt(11)

    # Right cell: Authors & Semester
    p_auth = cell_right.paragraphs[0]
    p_auth.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_auth.paragraph_format.space_before = Pt(0)
    p_auth.paragraph_format.space_after = Pt(0)
    p_auth.paragraph_format.line_spacing = 1.15

    run_a1 = p_auth.add_run('Upendra Murmu (23110325)\n')
    run_a1.bold = False
    run_a1.font.name = 'Times New Roman'
    run_a1.font.size = Pt(11)

    run_a2 = p_auth.add_run('Omm Prakash Sahoo (23110286)\n')
    run_a2.bold = False
    run_a2.font.name = 'Times New Roman'
    run_a2.font.size = Pt(11)

    run_sem = p_auth.add_run('7th Semester')
    run_sem.bold = False
    run_sem.font.name = 'Times New Roman'
    run_sem.font.size = Pt(11)

    doc.save(output_path)
    print(f"Successfully generated abstract document: {output_path}")

if __name__ == "__main__":
    create_abstract_docx("AI_Study_Hub_Abstract.docx")
