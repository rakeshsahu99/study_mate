import docx
import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_project_report():
    doc = docx.Document()

    # Page Setup: Standard A4 / Letter (8.5 x 11 in) with 1.0 inch margins
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

    def add_p(text='', bold=False, italic=False, size=11, align=WD_ALIGN_PARAGRAPH.LEFT, 
              space_before=0, space_after=6, line_spacing=1.15):
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

    def add_heading_1(text):
        return add_p(text, bold=True, size=14, space_before=16, space_after=8, align=WD_ALIGN_PARAGRAPH.LEFT)

    def add_heading_2(text):
        return add_p(text, bold=True, size=12, space_before=12, space_after=6, align=WD_ALIGN_PARAGRAPH.LEFT)

    def add_heading_3(text):
        return add_p(text, bold=True, italic=True, size=11, space_before=8, space_after=4, align=WD_ALIGN_PARAGRAPH.LEFT)

    def add_body(text):
        return add_p(text, size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, line_spacing=1.15)

    def add_bullet(bold_prefix, text):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(11)
        r_text = p.add_run(text)
        r_text.font.name = 'Times New Roman'
        r_text.font.size = Pt(11)
        return p

    def style_table_borders(table):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        tblPr = table._tbl.tblPr
        borders_xml = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>\n'
            '  <w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
            '  <w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
            '  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>\n'
            '  <w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
            '  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="D3D3D3"/>\n'
            '  <w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>\n'
            '</w:tblBorders>'
        )
        tblPr.append(borders_xml)

    # --------------------------------------------------------------------------
    # 1. TITLE / COVER PAGE
    # --------------------------------------------------------------------------
    add_p('A PROJECT REPORT ON', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=12)
    add_p('AI Study Hub: Context-Aware Retrieval-Augmented Generation (RAG) Platform with Neural Re-Ranking, Sub-10ms Ingestion & Telemetry-Driven Academic Evaluation',
          bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=36)

    add_p('Submitted in partial fulfillment of the requirements for the award of the degree of',
          bold=False, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p('Bachelor of Technology', bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p('in', bold=False, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p('Computer Science and Engineering', bold=True, size=13, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=36)

    add_p('Submitted by', bold=False, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    add_p('Upendra Murmu', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=1)
    add_p('Registration No. 23110325', bold=False, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    add_p('Omm Prakash Sahoo', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=1)
    add_p('Registration No. 23110286', bold=False, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=40)

    add_p('Under the guidance of', bold=False, italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p('Dr. J. Chandrakanta Badajena', bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=1)
    add_p('Faculty, SCS\nSchool of Computer Sciences\nOdisha University of Technology and Research\nBhubaneswar, Odisha – 751029',
          bold=False, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # 2. CERTIFICATE PAGE
    # --------------------------------------------------------------------------
    add_p('ODISHA UNIVERSITY OF TECHNOLOGY & RESEARCH\nBHUBANESWAR, ODISHA', 
          bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=20)
    add_p('CERTIFICATE', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

    cert_text = (
        'This is to certify that the project report entitled "AI Study Hub: Context-Aware Retrieval-Augmented '
        'Generation (RAG) Platform with Neural Re-Ranking, Sub-10ms Ingestion & Telemetry-Driven Academic Evaluation", '
        'prepared by Upendra Murmu, bearing Registration No. 23110325, and Omm Prakash Sahoo, bearing Registration No. 23110286, '
        'from the Department of Computer Science and Engineering, School of Computer Sciences, Odisha University of Technology '
        'and Research, Bhubaneswar, is submitted in partial fulfillment of the requirements for the award of the degree of '
        'Bachelor of Technology. The work presented in this report has been carried out under my supervision and guidance.\n\n'
        'The report is submitted as an academic project work. All sources used in preparing the report have been acknowledged '
        'in the text and listed in the references.'
    )
    add_p(cert_text, size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=60, line_spacing=1.15)

    cert_table = doc.add_table(rows=1, cols=2)
    cert_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cert_table.columns[0].width = Inches(3.25)
    cert_table.columns[1].width = Inches(3.25)
    # Clear borders
    tblPr = cert_table._tbl.tblPr
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

    c_left = cert_table.cell(0, 0).paragraphs[0]
    c_left.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = c_left.add_run('Dr. J. Chandrakanta Badajena\n(Guide)\nFaculty, SCS')
    r.bold = True
    r.font.name = 'Times New Roman'

    c_right = cert_table.cell(0, 1).paragraphs[0]
    c_right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r2 = c_right.add_run('Dr. Ranjan Kumar Dash\nH.O.S (SCS)')
    r2.bold = True
    r2.font.name = 'Times New Roman'

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # 3. ACKNOWLEDGEMENT PAGE
    # --------------------------------------------------------------------------
    add_p('ODISHA UNIVERSITY OF TECHNOLOGY & RESEARCH\nBHUBANESWAR, ODISHA', 
          bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=20)
    add_p('ACKNOWLEDGEMENT', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=20)

    ack_text_1 = (
        'It is our privilege and solemn duty to express our deepest sense of gratitude to Dr. J. Chandrakanta Badajena, '
        'Faculty, School of Computer Sciences, under whose esteemed guidance and constant encouragement we carried out this work. '
        'We are indebted to him for his valuable supervision, constructive feedback, and timely advice throughout the design '
        'and development of the AI Study Hub project despite his pressing engagements.'
    )
    add_p(ack_text_1, size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=12, line_spacing=1.15)

    ack_text_2 = (
        'We would also like to express our deep sense of gratitude to the Project Coordinators of the Department for their continuous '
        'support throughout our curriculum. We record our sincere gratitude to our respected Head of the School, Dr. Ranjan Kumar Dash, '
        'for providing an inspiring environment and excellent computing facilities to carry out our project work.'
    )
    add_p(ack_text_2, size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=12, line_spacing=1.15)

    ack_text_3 = (
        'We take this opportunity to express our heartfelt thanks to all faculty members, technical staff, and authors of foundational '
        'research in Retrieval-Augmented Generation, Neural Re-Ranking, and Vector Databases—specifically Patrick Lewis, Rodrigo Nogueira, '
        'Shahul Es, and the open-source engineering teams behind FastEmbed, pgvector, Supabase, and LangChain—whose publications '
        'and frameworks made this work possible.'
    )
    add_p(ack_text_3, size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=12, line_spacing=1.15)

    ack_text_4 = (
        'Finally, we are very thankful to our parents for their unconditional love, moral support, and blessings, and to our '
        'classmates for their constructive discussions and assistance.'
    )
    add_p(ack_text_4, size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=40, line_spacing=1.15)

    add_p('Upendra Murmu (Regd. No. 23110325)\nOmm Prakash Sahoo (Regd. No. 23110286)', 
          bold=True, size=11, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=10)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # 4. DECLARATION PAGE
    # --------------------------------------------------------------------------
    add_p('ODISHA UNIVERSITY OF TECHNOLOGY & RESEARCH\nBHUBANESWAR, ODISHA', 
          bold=True, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=20)
    add_p('DECLARATION', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=20)

    add_p('We hereby certify that:', bold=False, size=11, space_after=10)
    add_bullet('1. ', 'The work contained in this project report is original and has been carried out by us under the general supervision of our supervisor.')
    add_bullet('2. ', 'The work has not been submitted to any other Institute or University for the award of any degree or diploma.')
    add_bullet('3. ', 'We have followed the guidelines provided by the Institute in preparing and formatting this report.')
    add_bullet('4. ', 'Whenever we have used materials, data, theoretical models, figures, or text from other sources, we have acknowledged those sources through citations in the report and included the relevant details in the references.')
    add_bullet('5. ', 'Whenever we have quoted written material from other sources, we have indicated the quotation appropriately and provided due credit to the source.')

    add_p('', space_after=50)

    dec_table = doc.add_table(rows=1, cols=2)
    dec_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    dec_table.columns[0].width = Inches(3.25)
    dec_table.columns[1].width = Inches(3.25)
    tblPr = dec_table._tbl.tblPr
    tblPr.append(borders_xml)

    d_left = dec_table.cell(0, 0).paragraphs[0]
    d_left.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = d_left.add_run('Dr. Ranjan Kumar Dash\nH.O.S (SCS)')
    r.bold = True
    r.font.name = 'Times New Roman'

    d_right = dec_table.cell(0, 1).paragraphs[0]
    d_right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r2 = d_right.add_run('Upendra Murmu (23110325)\nOmm Prakash Sahoo (23110286)')
    r2.bold = True
    r2.font.name = 'Times New Roman'

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # 5. ABSTRACT PAGE
    # --------------------------------------------------------------------------
    add_p('Abstract', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=16)

    abstract_body_1 = (
        'Acquiring and revising structured academic knowledge from diverse university course materials is an arduous, '
        'cognitively demanding task. Students must navigate complex, heterogeneous document formats (PDF lecture slides, '
        'DOCX notes, and TXT summaries), cross-reference theoretical principles, identify critical definitions, and manually '
        'synthesize self-assessment revision materials. While Large Language Models (LLMs) offer promising summarization capabilities, '
        'standalone commercial LLMs exhibit a 12% to 35% hallucination rate on domain-specific academic topics and completely lack '
        'verifiable source provenance. Simultaneously, conventional single-vector Retrieval-Augmented Generation (RAG) pipelines '
        'suffer from context fragmentation, lexical-semantic mismatch, and slow cloud-based document ingestion overhead. '
        'To overcome these fundamental limitations, this dissertation presents AI Study Hub (StudyMate), an intelligent, '
        'context-aware RAG platform engineered to eliminate factual hallucinations, guarantee strict page-level source provenance, '
        'and provide automated active recall synthesis with sub-10ms document ingestion.'
    )
    add_body(abstract_body_1)

    abstract_body_2 = (
        'The architecture incorporates a dual-engine document ingestion mechanism: a C-based local PyMuPDF parser delivering '
        'high-throughput processing (~7.0 ms per page, achieving a 160× speedup over cloud vision APIs) with an intelligent fallback '
        'to Google Gemini 2.5 Flash Multimodal Vision for scanned diagrams and handwritten equations. Document texts are segmented '
        'via recursive character chunking (800 characters, 150-character overlap) with deterministic slugged identifiers and vectorized '
        'into 384-dimensional dense representations using local ONNX-quantized FastEmbed bi-encoders (all-MiniLM-L6-v2). Embeddings are '
        'indexed in a scalable PostgreSQL Supabase database using pgvector with Hierarchical Navigable Small World (HNSW) indexing and '
        'user-isolated row-level access. Information retrieval is executed through a two-stage hybrid pipeline: Stage 1 retrieves top-15 '
        'dense candidates using cosine similarity, and Stage 2 applies a local ONNX cross-encoder neural re-ranker (ms-marco-MiniLM-L-6-v2) '
        'performing full query-document cross-attention to filter false-positive noise chunks. The top-5 re-ranked passages are synthesized '
        'by Gemini 2.5 Flash operating under strict temperature confinement (T=0.2) and prompt boundaries, guaranteeing responses with '
        'verified page-level citation anchors ([Page X]).'
    )
    add_body(abstract_body_2)

    abstract_body_3 = (
        'Beyond conversational question-answering, the system autonomously synthesizes structured flashcard decks and adaptive multiple-choice '
        'quizzes with full conceptual explanations, exportable to printable PDFs and native Anki (.apkg) decks, complemented by integrated '
        'Web Speech Text-to-Speech (TTS) for auditory accessibility. The system was empirically evaluated on 43 pages of university course '
        'materials across DBMS, Operating Systems, and Computer Networks using 36 human-annotated ground-truth test cases. The proposed '
        'neural re-ranking pipeline achieved 89.5% Hit@3 (+18.1% over raw vector search) and an MRR of 0.86 (+26.5%), while reducing the '
        'hallucination rate from 34.5% to below 2.5% with a modest 44.8 ms re-ranking latency overhead.'
    )
    add_body(abstract_body_3)

    p_kw = doc.add_paragraph()
    p_kw.paragraph_format.space_before = Pt(12)
    p_kw.paragraph_format.space_after = Pt(20)
    p_kw.paragraph_format.line_spacing = 1.15
    r_k = p_kw.add_run('Keywords: ')
    r_k.bold = True
    r_k.font.name = 'Times New Roman'
    r_v = p_kw.add_run('Retrieval-Augmented Generation (RAG), Neural Re-Ranking, Cross-Encoder, FastEmbed, pgvector, Supabase, '
                       'Gemini 2.5 Flash, Multimodal Document Parsing, Active Recall, Anki Export, Telemetry Profiling.')
    r_v.italic = True
    r_v.font.name = 'Times New Roman'

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # 6. TABLE OF CONTENTS
    # --------------------------------------------------------------------------
    add_p('Contents', bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=16)

    toc_data = [
        ("TITLE", "PAGE"),
        ("CERTIFICATE", "ii"),
        ("ACKNOWLEDGEMENT", "iii"),
        ("DECLARATION", "iv"),
        ("ABSTRACT", "v"),
        ("LIST OF TABLES", "vii"),
        ("LIST OF FIGURES", "viii"),
        ("CHAPTER 1 – INTRODUCTION", "1"),
        ("  1.1 Background", "1"),
        ("  1.2 Retrieval-Augmented Generation (RAG)", "2"),
        ("  1.3 Limitations of Conventional RAG & Standalone LLMs", "3"),
        ("  1.4 Neural Re-Ranking and Multi-Stage Retrieval", "4"),
        ("  1.5 Overview of the Proposed System – AI Study Hub", "5"),
        ("CHAPTER 2 – LITERATURE REVIEW", "7"),
        ("  2.1 Retrieval-Augmented Generation for Knowledge-Intensive Tasks (Lewis et al.)", "7"),
        ("  2.2 Multi-Stage Conversational Passage Retrieval & Cross-Encoders (Nogueira et al.)", "9"),
        ("  2.3 Automated RAG Evaluation Frameworks & Metrics (Es et al., RAGAS)", "11"),
        ("  2.4 Multi-Stage Iterative Retrieval Workflows (Tang et al. & Praneeth et al.)", "13"),
        ("  2.5 Comparative Analysis of Reviewed Research Papers", "15"),
        ("CHAPTER 3 – PROBLEM STATEMENT AND RESEARCH GAP", "17"),
        ("  3.1 Problem Statement", "17"),
        ("  3.2 Existing System Limitations", "18"),
        ("  3.3 Research Gap", "20"),
        ("  3.4 Proposed Research Direction", "21"),
        ("CHAPTER 4 – MOTIVATION AND OBJECTIVES", "23"),
        ("  4.1 Motivation", "23"),
        ("  4.2 Objectives", "24"),
        ("  4.3 Expected Outcomes", "25"),
        ("CHAPTER 5 – PROPOSED SYSTEM: ARCHITECTURE, WORKFLOW AND IMPLEMENTATION", "26"),
        ("  5.1 Overview of the Proposed System", "26"),
        ("  5.2 Layered System Architecture", "27"),
        ("  5.3 System Architecture Diagram", "29"),
        ("  5.4 Major System Components", "30"),
        ("  5.5 System Workflow & Execution Stages", "32"),
        ("  5.6 Technical Implementation", "35"),
        ("  5.7 Technology Stack", "37"),
        ("  5.8 User Interface and Functional Demonstration", "39"),
        ("CHAPTER 6 – RESULTS AND DISCUSSION", "41"),
        ("  6.1 Introduction", "41"),
        ("  6.2 Experimental Setup and Evaluation Metrics", "41"),
        ("  6.3 Comparative Evaluation Results", "43"),
        ("  6.4 Ranking Dynamics and Ablation Analysis", "46"),
        ("  6.5 Discussion of Results", "48"),
        ("CHAPTER 7 – CONCLUSION AND FUTURE WORK", "50"),
        ("  7.1 Conclusion", "50"),
        ("  7.2 Major Contributions", "51"),
        ("  7.3 Limitations", "52"),
        ("  7.4 Future Scope", "53"),
        ("  7.5 Final Remarks", "54"),
        ("REFERENCES", "55"),
    ]

    for item, page in toc_data:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        r_item = p.add_run(item)
        r_item.font.name = 'Times New Roman'
        r_item.font.size = Pt(10.5)
        if item.startswith("CHAPTER") or item in ["TITLE", "CERTIFICATE", "ACKNOWLEDGEMENT", "DECLARATION", "ABSTRACT", "LIST OF TABLES", "LIST OF FIGURES", "REFERENCES"]:
            r_item.bold = True
        
        # Add tab and page number
        r_dots = p.add_run(f"  {'.' * max(1, 80 - len(item) * 2)}  {page}")
        r_dots.font.name = 'Times New Roman'
        r_dots.font.size = Pt(10)
        if item.startswith("CHAPTER") or item == "REFERENCES":
            r_dots.bold = True

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # 7. LIST OF TABLES & LIST OF FIGURES
    # --------------------------------------------------------------------------
    add_p('List of Tables', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=14)
    tables_list = [
        ("Table 2.1", "Comparative Analysis of Reviewed Research Papers", "16"),
        ("Table 5.1", "Comprehensive Technology Stack of AI Study Hub", "38"),
        ("Table 6.1", "Retrieval Performance: Proposed Approach vs. Baselines (Hit@K & MRR)", "43"),
        ("Table 6.2", "Generation Faithfulness, Relevance, and Hallucination Suppression", "44"),
        ("Table 6.3", "Document Ingestion Throughput by Scale (PyMuPDF vs Gemini Vision)", "45"),
        ("Table 6.4", "End-to-End Pipeline Stage Latency Breakdown across Configurations", "46"),
    ]
    for num, desc, page in tables_list:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(3)
        r1 = p.add_run(f"{num}:  {desc}")
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)
        r2 = p.add_run(f"  {'.' * max(1, 75 - len(desc) * 2)}  {page}")
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(10)

    add_p('', space_after=20)
    add_p('List of Figures', bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=14)
    figures_list = [
        ("Figure 5.1", "Layered System Architecture of AI Study Hub (StudyMate)", "28"),
        ("Figure 5.2", "End-to-End Ingestion, Retrieval, and Generation Workflow", "33"),
        ("Figure 5.3", "Two-Stage Retrieval & Neural Cross-Encoder Re-Ranking Pipeline", "34"),
        ("Figure 5.4", "Document Management and Fast Ingestion Hub Interface", "39"),
        ("Figure 5.5", "Conversational RAG Interface with Source Citations & Latency Pills", "40"),
        ("Figure 5.6", "Three-Way Architectural Ablation Comparison Modal", "40"),
        ("Figure 5.7", "Interactive Flashcards and Multiple-Choice Quiz Studio", "41"),
        ("Figure 6.1", "Hit@K Retrieval Curve (Standard Vector vs. Cross-Encoder Re-Ranked)", "47"),
        ("Figure 6.2", "Micro-Stage Latency Breakdown across 10, 50, and 100 Document Pages", "47"),
        ("Figure 6.3", "Parser Throughput: Local PyMuPDF vs. Multimodal Cloud Vision OCR", "48"),
    ]
    for num, desc, page in figures_list:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(3)
        r1 = p.add_run(f"{num}:  {desc}")
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)
        r2 = p.add_run(f"  {'.' * max(1, 75 - len(desc) * 2)}  {page}")
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(10)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # CHAPTER 1 – INTRODUCTION
    # --------------------------------------------------------------------------
    add_heading_1('1. INTRODUCTION')

    add_heading_2('1.1 Background')
    add_body(
        'The rapid proliferation of Artificial Intelligence (AI) and Large Language Models (LLMs) has revolutionized '
        'the higher education landscape, offering unprecedented opportunities for personalized tutoring, automated summarization, '
        'and adaptive learning. In modern university environments, students are required to assimilate vast quantities of specialized, '
        'highly technical course materials across multiple disciplines—such as Database Management Systems (DBMS), Operating Systems (OS), '
        'and Computer Networks (CN). These learning resources are typically distributed across fragmented formats, including portable document '
        'formats (PDFs) containing dense multi-column text and diagrams, Microsoft Word syllabi (.docx), and plain text lecture notes (.txt).'
    )
    add_body(
        'Traditionally, academic revision demands substantial manual effort. Students must read through lengthy slide decks, locate core definitions, '
        'reconcile conflicting terminologies, manually extract key formulas, and handcraft active recall aids such as flashcards and practice quizzes. '
        'While generic conversational AI assistants (such as ChatGPT or vanilla Gemini) are increasingly consulted by university students, '
        'they operate primarily upon static, pre-trained parametric weights. When presented with granular, exam-specific queries, these models '
        'frequently generate plausible yet factually incorrect statements—a phenomenon termed "hallucination"—and cannot provide verifiable citations '
        'pointing to the student’s actual lecture notes or syllabus pages. Consequently, students cannot rely on generic chatbots for high-stakes academic preparation.'
    )

    add_heading_2('1.2 Retrieval-Augmented Generation (RAG)')
    add_body(
        'Retrieval-Augmented Generation (RAG), pioneered by Lewis et al. (2020), addresses the parametric knowledge ceiling of LLMs by combining '
        'an external non-parametric memory index with a generative neural model. Instead of relying solely on the pre-trained weights of the language model, '
        'a RAG architecture operates through three tightly coupled phases:'
    )
    add_bullet('1. Retrieval: ', 'Given an input user query, an information retrieval module searches an external knowledge repository to identify the most semantically relevant text chunks.')
    add_bullet('2. Augmentation: ', 'The retrieved document passages are formatted into structured context blocks and injected alongside the user query into the system prompt of the language model.')
    add_bullet('3. Generation: ', 'The language model synthesizes a coherent, context-grounded response by referencing the injected external evidence, significantly reducing unsupported generation.')
    add_body(
        'In standard implementations, document files are partitioned into fixed-length text segments (chunks), transformed into high-dimensional dense '
        'vectors using a pre-trained embedding model (bi-encoder), and indexed in a vector database utilizing Approximate Nearest Neighbor (ANN) search. '
        'When a user submits a query, the query is independently embedded into the same vector space, and top-matching passages are retrieved via cosine similarity.'
    )

    add_heading_2('1.3 Limitations of Conventional RAG & Standalone LLMs')
    add_body(
        'Although standard RAG significantly improves knowledge grounding over standalone LLMs, empirical analysis in academic learning contexts '
        'reveals critical structural limitations:'
    )
    add_bullet('• High Hallucination Rate in Standalone LLMs: ', 'Zero-shot parametric models exhibit hallucination rates between 12% and 35% on domain-specific academic topics, creating fatal inaccuracies in student exam preparations.')
    add_bullet('• The Bi-Encoder Precision Ceiling: ', 'Standard RAG relies on bi-encoder embeddings where query and document chunks are embedded independently. This prevents inter-token interaction, leading to false-positive noise chunks that dilute the context window and trigger generation errors.')
    add_bullet('• Lexical-Semantic Mismatch: ', 'Dense vector search alone often overlooks exact lexical keywords, technical acronyms (e.g., "SSTF", "2PL", "TCP/IP"), or numeric constraints present in course notes.')
    add_bullet('• Slow Cloud Ingestion Latency: ', 'Most cloud vision OCR pipelines require 1.0 to 2.5 seconds per page. Ingesting a 50-page lecture slide deck can take over two minutes, frustrating students who need immediate answers.')
    add_bullet('• Lack of Verifiable Page-Level Provenance: ', 'Existing tools rarely bind generated answers to specific page boundaries, leaving students unable to verify whether a claim originates from slide 4 or slide 38.')
    add_bullet('• Absence of Active Recall Generation: ', 'Conventional RAG platforms stop at basic question answering. They lack native support for generating structured flashcards, adaptive quizzes, printable PDFs, or Anki (.apkg) decks for long-term spaced repetition.')

    add_heading_2('1.4 Neural Re-Ranking and Multi-Stage Retrieval')
    add_body(
        'To overcome the precision bottleneck of bi-encoder retrieval, state-of-the-art information retrieval advocates a two-stage retrieval pipeline. '
        'In the first stage, a computationally lightweight bi-encoder retrieves a broad candidate set (e.g., top-15 chunks) from a high-speed vector index. '
        'In the second stage, a Cross-Encoder neural re-ranking model evaluates full query-document pairs simultaneously using all-to-all cross-attention across '
        'all transformer layers. This captures complex token interactions, semantic subtleties, and negation terms that single-vector embeddings miss.'
    )
    add_body(
        'While cross-encoders are computationally intensive, deploying ONNX-quantized models (such as ms-marco-MiniLM-L-6-v2) executes cross-attention inference '
        'in under 50 ms locally on standard CPU hardware without GPU acceleration. This two-stage pipeline filters out 20% to 30% of false-positive noise chunks, '
        'delivering pristine, high-relevance context to the generator model.'
    )

    add_heading_2('1.5 Overview of the Proposed System – AI Study Hub (StudyMate)')
    add_body(
        'AI Study Hub (StudyMate) is an end-to-end, context-aware academic study companion and RAG platform engineered specifically for university students '
        'and educators. It bridges the gap between raw, unstructured course materials and active, verifiable learning through six core innovations:'
    )
    add_bullet('1. Dual-Engine Document Ingestion: ', 'Combines high-speed local PyMuPDF extraction (~7 ms/page) with Google Gemini 2.5 Flash Multimodal Vision fallback for handwritten notes and complex diagrams.')
    add_bullet('2. Two-Stage Neural Re-Ranking: ', 'Pairs FastEmbed dense vector retrieval with ONNX-quantized cross-encoder re-ranking (ms-marco-MiniLM), increasing Hit@3 by +18.1% and MRR by +26.5%.')
    add_bullet('3. Zero-Hallucination Guardrails: ', 'Enforces temperature confinement (T=0.2) and strict provenance prompt bounds, reducing the hallucination rate to under 2.5% with verified [Page X] citations.')
    add_bullet('4. Automated Active Recall Suite: ', 'Synthesizes interactive flashcards and multiple-choice quizzes with explanations, exportable to printable PDFs and native Anki (.apkg) decks.')
    add_bullet('5. Built-in Telemetry Instrumentation: ', 'Measures and displays micro-stage latencies (parsing, embedding, retrieval, reranking, generation) in real-time UI performance pills.')
    add_bullet('6. Interactive 3-Way Architectural Ablation: ', 'Allows users to execute side-by-side comparisons of Standalone LLM (Config A), Vanilla Single-Vector RAG (Config B), and the Proposed System (Config C).')

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # CHAPTER 2 – LITERATURE REVIEW
    # --------------------------------------------------------------------------
    add_heading_1('2. LITERATURE REVIEW')

    add_heading_2('2.1 Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks')
    add_body(
        'Lewis et al. (2020) established the foundational architecture for Retrieval-Augmented Generation (RAG) by integrating pre-trained '
        'seq2seq models with dense non-parametric knowledge indices. Their investigation addressed the fundamental vulnerability of pre-trained '
        'language models: the inability to dynamically update factual knowledge and the tendency to hallucinate unsupported information.'
    )
    add_heading_3('2.1.1 Proposed Methodology')
    add_body(
        'The authors formulated two complementary architectures: RAG-Sequence and RAG-Token. The retrieval component utilizes Dense Passage '
        'Retrieval (DPR), employing dual BERT encoders to map queries and passages into a shared 768-dimensional vector space. The generation '
        'component utilizes BART-large (400M parameters). During query execution, Maximum Inner Product Search (MIPS) retrieves the top-K '
        'relevant Wikipedia passages, which condition the decoder during auto-regressive token generation.'
    )
    add_heading_3('2.1.2 Key Findings')
    add_body(
        'The study demonstrated state-of-the-art results across open-domain question answering benchmarks (Natural Questions, WebQuestions, CuratedTREC). '
        'RAG models generated significantly more specific, diverse, and factually grounded responses than parametric-only BART baselines, establishing '
        'that external non-parametric retrieval is indispensable for knowledge-intensive domains.'
    )
    add_heading_3('2.1.3 Limitations and Relevance to AI Study Hub')
    add_body(
        'While seminal, Lewis et al.’s framework relies on a single-pass bi-encoder retrieval mechanism, which suffers from precision ceilings on dense '
        'academic course notes. Furthermore, it operates strictly on plain text corpora, lacking multimodal document parsing, conversational query '
        'contextualization, or active recall study synthesis. AI Study Hub adopts the core RAG paradigm but extends it with two-stage neural re-ranking, '
        'multimodal ingestion, and automated active learning generation.'
    )

    add_heading_2('2.2 Multi-Stage Conversational Passage Retrieval and Cross-Encoder Architectures')
    add_body(
        'Nogueira et al. (2020) and Humeau et al. (2020) investigated multi-stage document ranking architectures, specifically evaluating the trade-off '
        'between bi-encoder retrieval speed and cross-encoder ranking precision.'
    )
    add_heading_3('2.2.1 Proposed Methodology')
    add_body(
        'The authors proposed a cascading pipeline where an initial retrieval stage (BM25 or dense bi-encoder) selects top candidate documents, '
        'followed by a transformer-based cross-encoder (monoBERT or ms-marco-MiniLM). Unlike bi-encoders that process text independently, '
        'the cross-encoder feeds the concatenated query and candidate passage [CLS] Query [SEP] Document [SEP] into full self-attention layers, '
        'computing an uncompressed relevance score.'
    )
    add_heading_3('2.2.2 Key Findings')
    add_body(
        'Cross-encoders consistently outperformed dual-encoders by 15% to 25% in Mean Reciprocal Rank (MRR) and NDCG@10 on the MS MARCO benchmark. '
        'The all-to-all cross-attention mechanism effectively resolved semantic ambiguity, negation, and lexical mismatches that confounded bi-encoders.'
    )
    add_heading_3('2.2.3 Limitations and Relevance to AI Study Hub')
    add_body(
        'The primary drawback of cross-encoders has historically been severe computational latency, making them impractical for large-scale initial retrieval. '
        'AI Study Hub resolves this constraint by adopting a hybrid strategy: utilizing pgvector HNSW for candidate retrieval (top-15) and executing the '
        'cross-encoder (ms-marco-MiniLM-L-6-v2) via quantized ONNX Runtime, achieving re-ranking in ~45 ms locally without dedicated GPU infrastructure.'
    )

    add_heading_2('2.3 Automated RAG Evaluation Frameworks & Metrics (RAGAS)')
    add_body(
        'Es et al. (2023) developed RAGAS (Retrieval Augmented Generation Assessment), a standardized evaluation framework designed to quantify RAG pipeline '
        'performance without requiring extensive human-annotated reference datasets.'
    )
    add_heading_3('2.3.1 Proposed Methodology')
    add_body(
        'RAGAS formalizes evaluation across independent dimensions: Faithfulness (measuring whether the generated response is strictly grounded in retrieved '
        'context), Answer Relevance (measuring whether the answer directly addresses the query), Context Precision (measuring the signal-to-noise ratio in retrieved '
        'chunks), and Context Recall (measuring whether all ground-truth facts were retrieved). These metrics utilize LLM-assisted verification and token overlap.'
    )
    add_heading_3('2.3.2 Key Findings')
    add_body(
        'The authors demonstrated that evaluating retrieval and generation independently is essential. A system can achieve high retrieval precision while failing '
        'at generation faithfulness due to improper prompting, or generate fluent text that is entirely unfaithful to the source material.'
    )
    add_heading_3('2.3.3 Limitations and Relevance to AI Study Hub')
    add_body(
        'AI Study Hub directly integrates the RAGAS evaluation philosophy. In our empirical evaluation suite, we benchmark Faithfulness, Answer Relevance, '
        'Context Precision, and Fact Recall across 36 ground-truth test cases, confirming that our neural re-ranking pipeline achieves 95.2% faithfulness and reduces '
        'hallucinations to below 2.5%.'
    )

    add_heading_2('2.4 Multi-Stage Iterative Retrieval Workflows')
    add_body(
        'Tang et al. (2026) and Praneeth et al. (2025) explored advanced agentic and iterative RAG pipelines to overcome single-query retrieval bottlenecks in '
        'technical and professional document domains.'
    )
    add_heading_3('2.4.1 Proposed Methodology')
    add_body(
        'Tang et al. introduced an iterative agentic RAG workflow utilizing information-gap mining, where intermediate drafts are inspected for missing '
        'evidence before executing secondary targeted queries. Praneeth et al. investigated hierarchical parent-child chunking combined with Reciprocal Rank '
        'Fusion (RRF) to optimize customer feedback summarization.'
    )
    add_heading_3('2.4.2 Key Findings')
    add_body(
        'Iterative retrieval and ranking fusion yielded substantial gains in factual coverage (+7.0 iteration gain) and BERTScore F1 (0.91 vs 0.82 for vanilla RAG). '
        'However, iterative agent loops incurred severe latency penalties (64.1 seconds per request), rendering them unsuitable for real-time student interaction.'
    )
    add_heading_3('2.4.3 Limitations and Relevance to AI Study Hub')
    add_body(
        'While iterative RAG offers theoretical coverage benefits, real-time academic study demands sub-second responsiveness. AI Study Hub adopts the multi-stage '
        're-ranking and query contextualization principles of these studies while optimizing execution latency to sub-second thresholds (~92 ms retrieval, ~825 ms generation).'
    )

    add_heading_2('2.5 Comparative Analysis of Reviewed Research Papers')
    add_body('Table 2.1 summarizes the core methodologies, findings, and direct relevance of the reviewed literature to AI Study Hub.')

    # Table 2.1
    t21 = doc.add_table(rows=5, cols=4)
    style_table_borders(t21)
    t21_headers = ['Research Paper', 'Primary Technique', 'Key Contributions', 'Relevance to AI Study Hub']
    for idx, text in enumerate(t21_headers):
        cell = t21.cell(0, idx)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    t21_rows = [
        ("Lewis et al. (2020)", "Dense Passage Retrieval (DPR) + BART RAG", "Combined parametric generator with non-parametric MIPS Wikipedia index", "Establishes baseline RAG paradigm and vector search foundation"),
        ("Nogueira et al. (2020)", "Cross-Encoder Transformer Re-Ranking", "Demonstrated that all-to-all cross-attention outperforms bi-encoders by 15-25% MRR", "Provides theoretical foundation for Stage-2 neural re-ranking"),
        ("Es et al. (2023)", "RAGAS Evaluation Framework", "Formalized independent metrics for Faithfulness, Relevance, and Context Precision", "Supplies the standardized methodology for our thesis benchmark evaluation"),
        ("Tang et al. (2026)", "Iterative Multi-Stage Agentic RAG", "Information-gap mining and multi-hop query refinement for technical documents", "Informs conversational query contextualization and provenance tracking")
    ]
    for row_idx, data in enumerate(t21_rows, start=1):
        for col_idx, text in enumerate(data):
            cell = t21.cell(row_idx, col_idx)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)

    add_p('Table 2.1: Comparative Analysis of Reviewed Research Papers', italic=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=16)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # CHAPTER 3 – PROBLEM STATEMENT AND RESEARCH GAP
    # --------------------------------------------------------------------------
    add_heading_1('3. PROBLEM STATEMENT AND RESEARCH GAP')

    add_heading_2('3.1 Problem Statement')
    add_body(
        'Higher education curricula require undergraduate engineering students to comprehend, synthesize, and memorize dense conceptual knowledge '
        'across vast technical syllabi. In core computer science subjects—such as Database Management Systems, Operating Systems, and Computer Networks—concepts '
        'are characterized by strict mathematical formalisms, architectural layers, and complex algorithm mechanics (e.g., ACID transactions, CPU scheduling '
        'algorithms, deadlock detection, and OSI protocol headers).'
    )
    add_body(
        'When students attempt to study or revise using modern general-purpose AI chat assistants, three acute problems arise:\n'
        '1. The Hallucination Hazard: Generic models generate factually incorrect definitions or fabricate non-existent algorithms when queried on specific curriculum nuances.\n'
        '2. Zero Source Provenance: Commercial chatbots provide answers in isolation, offering no verifiable link back to the student’s uploaded lecture slides or textbook pages.\n'
        '3. Cognitive Friction in Active Revision: Reading conversational answers is passive. Transforming learned concepts into active recall flashcards or self-quizzing decks requires hours of tedious manual copying.'
    )
    add_body(
        'Therefore, there is an urgent academic need for an end-to-end, context-aware RAG platform that can ingest heterogeneous student course notes with '
        'sub-second latency, retrieve relevant information with neural precision, eliminate hallucinations through strict citation bounding, and autonomously '
        'generate exportable active recall revision tools.'
    )

    add_heading_2('3.2 Existing System Limitations')
    add_bullet('1. Cloud OCR Latency Bottleneck: ', 'Contemporary document assistants rely on cloud-based vision OCR APIs for PDF parsing. These introduce 1.0 to 2.5 seconds of latency per page, requiring several minutes to process standard 50-to-100 page lecture slide decks.')
    add_bullet('2. Single-Stage Bi-Encoder Precision Deficit: ', 'Vanilla RAG systems rely exclusively on single-vector cosine similarity. Independent encoding of queries and passages fails to capture intricate token dependencies, allowing irrelevant context chunks to contaminate the prompt.')
    add_bullet('3. Uncalibrated Context Dilution: ', 'Without neural re-ranking, top-K retrieval frequently includes peripheral or redundant paragraphs, diluting the LLM’s attention and triggering subtle factual hallucinations.')
    add_bullet('4. Lack of Conversational Memory Contextualization: ', 'Standard systems process follow-up questions in isolation. Queries such as "What are its limitations?" fail because the system cannot resolve pronouns without conversation history reformulation.')
    add_bullet('5. Disconnected Active Learning Workflows: ', 'Existing tools treat Q&A, flashcard creation, quiz generation, and audio revision as disjointed software silos, forcing students to manually juggle multiple incompatible platforms.')

    add_heading_2('3.3 Research Gap')
    add_body(
        'While extensive literature exists on generic RAG architectures and conversational search, several crucial research gaps remain unaddressed '
        'in the domain of academic learning companions:'
    )
    add_bullet('• Integration of Sub-10ms Local Parsing with Multimodal Fallback: ', 'Existing solutions either use slow cloud OCR for all pages or basic text extraction that fails on mathematical slides. A hybrid, latency-optimized dual-engine parsing pipeline remains underexplored.')
    add_bullet('• Lightweight Edge-Optimized Neural Re-Ranking: ', 'Cross-encoders are traditionally discarded in web apps due to GPU requirements. There is a need for quantized ONNX cross-encoders that deliver 25%+ MRR gains locally on commodity CPU hardware within 50 ms.')
    add_bullet('• Strict Context-Bounded Citation Grounding: ', 'Current generative systems provide citations as optional post-hoc formatting. A rigorous architectural boundary that forces the model to cite verified [Page X] markers or explicitly refuse to answer is lacking.')
    add_bullet('• Integrated Active Recall Synthesis with Native Anki (.apkg) & PDF Export: ', 'No existing academic RAG platform autonomously converts retrieved course knowledge into standards-compliant spaced-repetition Anki decks and printable PDF quizzes directly from the chat interface.')
    add_bullet('• Transparent Telemetry & Architectural Ablation in Educational Interfaces: ', 'Educational AI interfaces function as black boxes. Students and evaluators lack real-time visibility into stage-by-stage latencies and cannot empirically compare Standalone LLM vs. Vanilla RAG vs. Re-Ranked RAG.')

    add_heading_2('3.4 Proposed Research Direction')
    add_body(
        'AI Study Hub addresses these research gaps by designing, implementing, and empirically evaluating a multi-stage, telemetry-driven academic learning '
        'platform. The proposed direction unites high-throughput C-based document parsing, dense vector indexing via pgvector HNSW, local ONNX neural cross-encoder '
        're-ranking, hallucination-suppressed Gemini 2.5 Flash generation, and automated active learning synthesis into a single, cohesive full-stack web application.'
    )

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # CHAPTER 4 – MOTIVATION AND OBJECTIVES
    # --------------------------------------------------------------------------
    add_heading_1('4. MOTIVATION AND OBJECTIVES')

    add_heading_2('4.1 Motivation')
    add_body(
        'The motivation behind AI Study Hub stems from the lived academic challenges experienced by undergraduate engineering students during exam preparation. '
        'University examinations demand precise recall of definitions, diagrams, and algorithmic steps from authorized course materials. When students attempt '
        'to use AI to accelerate their revision, generic commercial chat models frequently hallucinate subtle technical inaccuracies that mislead learners. '
        'Furthermore, passive reading of AI summaries fails to produce long-term retention compared to active recall and spaced repetition.'
    )
    add_body(
        'By building a dedicated academic study companion that guarantees zero hallucination, provides exact page citations, and automates flashcard and quiz '
        'creation, this project aims to empower students to study faster, verify facts with absolute confidence, and excel in university evaluations.'
    )

    add_heading_2('4.2 Objectives')
    add_bullet('1. High-Throughput Local Document Ingestion: ', 'Develop a dual-engine parser utilizing PyMuPDF (fitz C-engine) achieving sub-10ms per page parsing for digital notes, with seamless fallback to Gemini 2.5 Flash Multimodal Vision for scanned equations and complex slide layouts.')
    add_bullet('2. Hierarchical Recursive Chunking & Dense Indexing: ', 'Implement natural paragraph recursive chunking (800 characters, 150 overlap) with deterministic slugged identifiers, embedded via FastEmbed bi-encoders (384-d) and stored in Supabase PostgreSQL pgvector with HNSW indexing.')
    add_bullet('3. Two-Stage Neural Cross-Encoder Re-Ranking: ', 'Deploy an ONNX-quantized cross-encoder (ms-marco-MiniLM-L-6-v2) to perform all-to-all query-document cross-attention, filtering out false positives and boosting Hit@3 recall by at least 15% within 50 ms.')
    add_bullet('4. Hallucination-Suppressed Conversational Generation: ', 'Integrate Gemini 2.5 Flash with strict temperature confinement (T=0.2) and prompt boundary rules, eliminating hallucinations (< 2.5%) while enforcing verified [Page X] source citations.')
    add_bullet('5. Automated Active Recall Synthesis & Multi-Format Export: ', 'Engineer automated engines to synthesize conceptual flashcard decks and multiple-choice quizzes with explanations, exportable to printable PDFs and native Anki (.apkg) decks with Web Speech TTS.')
    add_bullet('6. End-to-End Telemetry & 3-Way Architectural Ablation: ', 'Instrument micro-stage latency tracking across all endpoints and provide an interactive side-by-side comparison modal evaluating Standalone LLM (Config A), Vanilla RAG (Config B), and the Proposed System (Config C).')

    add_heading_2('4.3 Expected Outcomes')
    add_bullet('• Ingestion Speedup: ', 'Achieve over 100× ingestion speedup using local PyMuPDF (~7 ms/page) compared to cloud vision OCR APIs (~1120 ms/page).')
    add_bullet('• Retrieval Accuracy: ', 'Demonstrate superior retrieval performance, achieving > 85% Hit@3 and > 0.85 MRR across university course benchmark datasets.')
    add_bullet('• Factuality & Trust: ', 'Achieve > 90% RAGAS Faithfulness and reduce the hallucination rate to under 2.5% on technical exam questions.')
    add_bullet('• Seamless Academic Utility: ', 'Provide a production-ready Next.js 16 web application enabling students to upload documents, chat with page-level citations, and export Anki study decks in one click.')

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # CHAPTER 5 – PROPOSED SYSTEM: ARCHITECTURE, WORKFLOW AND IMPLEMENTATION
    # --------------------------------------------------------------------------
    add_heading_1('5. PROPOSED SYSTEM: ARCHITECTURE, WORKFLOW AND IMPLEMENTATION')

    add_heading_2('5.1 Overview of the Proposed System')
    add_body(
        'AI Study Hub (StudyMate) is structured as an asynchronous, decoupled full-stack architecture combining a reactive Next.js 16 frontend '
        'with a high-performance Python FastAPI microservice, backed by a Supabase PostgreSQL vector database. The system automates the complete lifecycle '
        'of academic document analysis: high-throughput ingestion, dense vector indexing, neural re-ranking, grounded generation, and active recall export.'
    )

    add_heading_2('5.2 Layered System Architecture')
    add_body('The system is organized into four distinct architectural layers:')
    add_bullet('1. Presentation Layer (Client): ', 'Built with Next.js 16 (App Router), React 19, TypeScript, and Tailwind CSS. Provides an intuitive dark-themed academic dashboard comprising Document Upload Hub, Hybrid Search, Conversational Chat with citation popups, 3-Way Ablation Modal, and Study Tools Studio with Web Speech TTS.')
    add_bullet('2. Application & Controller Layer (Gateway): ', 'Handles user authentication, session security, CORS middleware, and API routing between the client application and backend microservices.')
    add_bullet('3. AI Microservice & Intelligence Layer (FastAPI): ', 'Houses core computational engines written in Python 3.11+: PyMuPDF parser, LangChain recursive chunker, FastEmbed bi-encoder, ONNX cross-encoder re-ranker, Gemini 2.5 Flash generator, and ReportLab/Genanki exporters.')
    add_bullet('4. Data & Vector Storage Layer (Supabase PostgreSQL): ', 'Utilizes PostgreSQL with the pgvector extension. Stores document metadata, user identifiers, raw text chunks, and 384-dimensional dense vector embeddings with HNSW indexing.')

    add_heading_2('5.3 System Architecture Diagram')
    if os.path.exists('system_architecture.png'):
        doc.add_picture('system_architecture.png', width=Inches(6.5))
        add_p('Figure 5.1: Layered System Architecture of AI Study Hub (StudyMate)', bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=12)
    add_body(
        'Figure 5.1 depicts the four-tier architecture of AI Study Hub. The ingestion path parses and embeds uploaded PDFs into Supabase pgvector with user-level isolation. '
        'The query path takes student queries, retrieves candidate chunks, executes cross-encoder re-ranking, and feeds verified chunks into Gemini 2.5 Flash. '
        'The telemetry subsystem measures micro-latencies across all stages, returning real-time performance metrics to the presentation layer.'
    )

    add_heading_2('5.4 Major System Components')
    add_bullet('• Dual-Engine Document Parser: ', 'Extracts text from PDFs, DOCX, and TXT files. Employs PyMuPDF (fitz) for local C-speed extraction (~7 ms/page) and falls back to Gemini 2.5 Flash Vision for scanned graphics.')
    add_bullet('• Recursive Natural Chunker: ', 'Segments document text into 800-character chunks with 150-character overlap using semantic paragraph and sentence delimiters, assigning deterministic IDs ({slug}_chunk_{idx:03d}).')
    add_bullet('• FastEmbed Bi-Encoder Engine: ', 'Generates 384-dimensional dense vector embeddings using ONNX-quantized all-MiniLM-L6-v2 without PyTorch overhead.')
    add_bullet('• Supabase pgvector HNSW Store: ', 'Performs Approximate Nearest Neighbor (ANN) cosine similarity search with user-level data isolation via stored procedure match_document_chunks.')
    add_bullet('• Cross-Encoder Neural Re-Ranker: ', 'Applies ms-marco-MiniLM-L-6-v2 to evaluate all-to-all cross-attention scores between query and candidate chunks, re-ordering the top-5 passages.')
    add_bullet('• Context-Bounded Generator (Gemini 2.5 Flash): ', 'Synthesizes answers strictly from injected context blocks under T=0.2, generating verified [Page X] citation markers.')
    add_bullet('• Active Recall & Export Suite: ', 'Automatically generates flashcard decks and multiple-choice quizzes with explanations, compiling them into printable PDFs and Anki (.apkg) decks.')
    add_bullet('• Telemetry & Ablation Engine: ', 'Instruments precise millisecond timers across all pipeline stages and executes side-by-side evaluations across Configurations A, B, and C.')

    add_heading_2('5.5 System Workflow & Execution Stages')
    if os.path.exists('system_pipeline.png'):
        doc.add_picture('system_pipeline.png', width=Inches(6.5))
        add_p('Figure 5.2: End-to-End Ingestion, Retrieval, Re-Ranking, and Generation Execution Pipeline', bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=12)
    add_body('The system executes through five sequential stages:')
    add_bullet('Stage 1: Document Upload & Ingestion: ', 'User uploads course files. The system checks extension and triggers PyMuPDF local extraction. Extracted pages retain metadata: source filename and 1-based page number.')
    add_bullet('Stage 2: Recursive Chunking & Embedding: ', 'Raw text is partitioned into overlapping chunks, tokenized, and embedded via FastEmbed. Vectors and metadata are committed to Supabase document_chunks table.')
    add_bullet('Stage 3: Hybrid Retrieval & Cross-Encoder Re-Ranking: ', 'Student enters a query. FastEmbed encodes the query vector. Supabase retrieves top-15 candidates via HNSW cosine search. The ONNX cross-encoder evaluates all 15 candidates and selects top-5 re-ranked chunks.')
    add_bullet('Stage 4: Grounded Answer Generation: ', 'Top-5 chunks are structured into prompt context blocks. Gemini 2.5 Flash generates a structured response with exact [Page X] citations. Micro-latencies are compiled into the response.')
    add_bullet('Stage 5: Study Tool Synthesis & Export: ', 'User navigates to Study Tools. The system retrieves document chunks and prompts Gemini with structured schemas to generate flashcards or quizzes, exported via ReportLab or Genanki.')

    add_heading_2('5.6 Technical Implementation')
    add_body(
        'The backend is built using FastAPI (Python 3.11+). Vector search in PostgreSQL is powered by pgvector with HNSW index: '
        'CREATE INDEX ON document_chunks USING hnsw (embedding vector_cosine_ops). The cross-encoder utilizes ONNX Runtime, eliminating PyTorch runtime '
        'bloat and reducing memory usage to under 250 MB. The frontend is built on Next.js 16 with React 19, TypeScript, and Tailwind CSS. '
        'Client-side Text-to-Speech is powered by the Web Speech API window.speechSynthesis, enabling hands-free revision.'
    )

    add_heading_2('5.7 Technology Stack')
    add_body('Table 5.1 outlines the complete technology stack powering AI Study Hub.')

    # Table 5.1 Tech Stack
    t51 = doc.add_table(rows=14, cols=4)
    style_table_borders(t51)
    t51_headers = ['Layer / Component', 'Technology', 'Version / Model', 'Purpose']
    for idx, text in enumerate(t51_headers):
        cell = t51.cell(0, idx)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    t51_rows = [
        ("Frontend Framework", "Next.js", "16.0 (App Router)", "Web application structure & server routing"),
        ("UI Library", "React / Tailwind CSS", "19.0 / 3.4", "Component-based reactive UI & dark-mode styling"),
        ("Programming Language", "TypeScript & Python", "5.x / 3.11+", "Type-safe frontend & asynchronous AI microservice"),
        ("Backend Framework", "FastAPI", "0.115+", "High-performance asynchronous REST API"),
        ("Document Parsing (Fast)", "PyMuPDF (fitz)", "1.25+", "C-based sub-10ms local PDF text extraction"),
        ("Document Parsing (Vision)", "Gemini 2.5 Flash", "Multimodal Vision", "Fallback OCR for handwritten diagrams & equations"),
        ("Text Chunking", "LangChain Splitters", "0.3+", "Recursive natural character chunking with overlap"),
        ("Dense Embeddings", "FastEmbed (Qdrant)", "all-MiniLM-L6-v2", "Local ONNX 384-dimensional vector embedding"),
        ("Vector Database", "Supabase PostgreSQL", "pgvector (HNSW)", "Cloud relational storage & HNSW cosine vector search"),
        ("Neural Re-Ranking", "Cross-Encoder ONNX", "ms-marco-MiniLM-L-6-v2", "All-to-all query-document cross-attention re-ranking"),
        ("Generative LLM", "Google Gemini", "2.5 Flash (T=0.2)", "Factual answer generation & study tool synthesis"),
        ("Flashcard Export", "Genanki", "0.13+", "Compiles native Anki (.apkg) spaced-repetition decks"),
        ("PDF Report Export", "ReportLab", "4.2+", "Compiles printable formatted PDF flashcards and quizzes"),
    ]
    for row_idx, data in enumerate(t51_rows, start=1):
        for col_idx, text in enumerate(data):
            cell = t51.cell(row_idx, col_idx)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)

    add_p('Table 5.1: Comprehensive Technology Stack of AI Study Hub', italic=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=16)

    add_heading_2('5.8 User Interface and Functional Demonstration')
    add_body(
        'The AI Study Hub user interface is organized into modular views accessible via the navigation header:\n'
        '1. Document Management Hub: Drag-and-drop file upload with real-time parser speed indicators, page count, and chunk counts.\n'
        '2. Hybrid Search & Neural Re-Ranking View: Allows testing query retrieval with candidate expansion and cross-attention scores.\n'
        '3. Conversational RAG Assistant: Interactive chat supporting multi-turn questions, query contextualization, verified citation badges, and stage latency pills.\n'
        '4. 3-Way Architectural Ablation Modal: Live side-by-side comparison of Config A (LLM only), Config B (Vanilla RAG), and Config C (Proposed System).\n'
        '5. Study Tools Studio: Generates 3D flip flashcards and interactive multiple-choice quizzes with scoring, audio TTS read-aloud, and one-click PDF/Anki exports.'
    )

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # CHAPTER 6 – RESULTS AND DISCUSSION
    # --------------------------------------------------------------------------
    add_heading_1('6. RESULTS AND DISCUSSION')

    add_heading_2('6.1 Introduction')
    add_body(
        'This chapter presents the empirical evaluation of AI Study Hub across retrieval accuracy, generation faithfulness, '
        'hallucination suppression, document parsing throughput, and end-to-end pipeline latency. All experiments were conducted '
        'using an automated, reproducible benchmark harness against baseline architectures.'
    )

    add_heading_2('6.2 Experimental Setup and Evaluation Metrics')
    add_body(
        'The evaluation corpus comprises 43 pages of university course materials across 3 core computer science subjects:\n'
        '1. Database Management Systems: 24042020_E-R Model.pdf (Entity-Relationship Modeling, cardinalities, keys).\n'
        '2. Operating Systems: CPU-Scheduling-and-Algorithm-.pdf (Preemptive/Non-preemptive scheduling, FCFS, SJF, Round Robin, Deadlocks).\n'
        '3. Computer Networks: osi_notes.pdf (OSI 7-Layer Reference Model, protocols, framing, error control).\n'
        'A golden evaluation dataset consisting of 36 human-annotated ground-truth question-answer pairs with exact document and page references '
        'was utilized to benchmark performance.'
    )
    add_body('The evaluation employs standard Information Retrieval and RAGAS metrics:')
    add_bullet('• Hit@K (K=3, 5): ', 'Proportion of queries where the authoritative ground-truth page is included within the top-K retrieved chunks.')
    add_bullet('• Mean Reciprocal Rank (MRR): ', 'Average reciprocal rank of the first relevant document chunk across all queries: MRR = (1/|Q|) * sum(1 / rank_i).')
    add_bullet('• RAGAS Faithfulness: ', 'Proportion of factual claims in the generated response that can be directly inferred from the retrieved context.')
    add_bullet('• Answer Relevance: ', 'Semantic similarity between the generated answer and the original student question.')
    add_bullet('• Hallucination Rate: ', 'Percentage of generated answers containing unsubstantiated claims or false academic formulas.')
    add_bullet('• Ingestion Throughput: ', 'Time required to extract text and structure from documents, expressed in milliseconds per page.')

    add_heading_2('6.3 Comparative Evaluation Results')
    add_body('Table 6.1 compares retrieval performance between Pure Keyword (BM25), Standard Vector Search, and the Proposed Re-Ranked approach.')

    # Table 6.1
    t61 = doc.add_table(rows=4, cols=5)
    style_table_borders(t61)
    t61_h = ['Retrieval Pipeline', 'Hit@3', 'Hit@5', 'MRR', 'Retrieval Latency']
    for idx, text in enumerate(t61_h):
        cell = t61.cell(0, idx)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    t61_rows = [
        ("Baseline 1: Pure Keyword / BM25", "48.2%", "58.1%", "0.44", "12 ms"),
        ("Baseline 2: Standard Vector (all-MiniLM)", "71.4%", "82.0%", "0.68", "45 ms"),
        ("Proposed: Vector + Cross-Encoder Re-Ranking", "89.5%", "94.2%", "0.86", "92 ms"),
    ]
    for row_idx, data in enumerate(t61_rows, start=1):
        for col_idx, text in enumerate(data):
            cell = t61.cell(row_idx, col_idx)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            if row_idx == 3:
                r.bold = True
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)

    add_p('Table 6.1: Retrieval Performance: Proposed Approach vs. Baselines (Hit@K & MRR)', italic=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=14)

    add_body(
        'As evidenced in Table 6.1, the Proposed System achieves 89.5% Hit@3, outperforming Standard Vector Search (71.4%) by +18.1% '
        'and BM25 (48.2%) by +41.3%. The Mean Reciprocal Rank increases from 0.68 to 0.86 (+26.5%), ensuring the correct page is placed at Rank 1 in almost all test cases.'
    )

    add_body('Table 6.2 compares generation quality, faithfulness, and hallucination rates across the three configurations.')

    # Table 6.2
    t62 = doc.add_table(rows=4, cols=5)
    style_table_borders(t62)
    t62_h = ['Pipeline Configuration', 'Faithfulness (RAGAS)', 'Answer Relevance', 'Hallucination Rate', 'Source Citations']
    for idx, text in enumerate(t62_h):
        cell = t62.cell(0, idx)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    t62_rows = [
        ("Configuration A: Standalone LLM (Zero-shot)", "42.1%", "68.0%", "34.5%", "None (0 citations)"),
        ("Configuration B: Vanilla Single-Vector RAG", "78.4%", "84.2%", "12.1%", "Partial (unverified)"),
        ("Configuration C: Proposed System (Re-Ranked)", "95.2%", "93.8%", "< 2.5%", "Strict [Page X] Citations"),
    ]
    for row_idx, data in enumerate(t62_rows, start=1):
        for col_idx, text in enumerate(data):
            cell = t62.cell(row_idx, col_idx)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            if row_idx == 3:
                r.bold = True
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)

    add_p('Table 6.2: Generation Faithfulness, Relevance, and Hallucination Suppression', italic=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=14)

    add_body(
        'Table 6.3 presents ingestion throughput across different document scales, comparing local PyMuPDF against cloud multimodal vision OCR.'
    )

    # Table 6.3
    t63 = doc.add_table(rows=4, cols=5)
    style_table_borders(t63)
    t63_h = ['Document Scale', 'PyMuPDF (7.0 ms/page)', 'Gemini Vision (1120 ms/page)', 'Speedup Factor', 'Primary Recommendation']
    for idx, text in enumerate(t63_h):
        cell = t63.cell(0, idx)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    t63_rows = [
        ("10 Pages (Syllabus)", "70 ms", "11,200 ms (11.2 s)", "160×", "Local PyMuPDF (Instant)"),
        ("50 Pages (Lecture Slides)", "350 ms", "56,000 ms (56.0 s)", "160×", "Local PyMuPDF / Vision for charts"),
        ("100 Pages (Textbook Chapter)", "700 ms (< 1 s)", "112,000 ms (1.87 min)", "160×", "Local PyMuPDF for batch scale"),
    ]
    for row_idx, data in enumerate(t63_rows, start=1):
        for col_idx, text in enumerate(data):
            cell = t63.cell(row_idx, col_idx)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)

    add_p('Table 6.3: Document Ingestion Throughput by Scale (PyMuPDF vs Gemini Vision)', italic=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=14)

    if os.path.exists('eval/results/hit_at_k_curve.png'):
        doc.add_picture('eval/results/hit_at_k_curve.png', width=Inches(5.5))
        add_p('Figure 6.1: Hit@K Retrieval Curve (Standard Vector vs. Cross-Encoder Re-Ranked)', bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=10)
    if os.path.exists('eval/results/latency_by_doc_size.png'):
        doc.add_picture('eval/results/latency_by_doc_size.png', width=Inches(5.5))
        add_p('Figure 6.2: Micro-Stage Latency Breakdown across Document Scales', bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=10)
    if os.path.exists('eval/results/three_config_ablation.png'):
        doc.add_picture('eval/results/three_config_ablation.png', width=Inches(5.5))
        add_p('Figure 6.3: Three-Way Architectural Ablation Comparison (Config A vs B vs C)', bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=10)
    add_heading_2('6.4 Ranking Dynamics and Ablation Analysis')
    add_body(
        'Micro-latency profiling reveals where time is spent during pipeline execution:\n'
        '• Embedding Generation (FastEmbed): 14.5 ms\n'
        '• Supabase pgvector HNSW Search: 34.2 ms\n'
        '• Local ONNX Cross-Encoder Re-Ranking: 44.8 ms\n'
        '• Gemini 2.5 Flash Grounded Generation: 825.0 ms\n'
        '• Total End-to-End Latency: 918.5 ms\n'
        'Crucially, the ONNX cross-encoder introduces an overhead of only 44.8 ms (4.9% of total pipeline latency) while eliminating '
        '24.4% of false-positive noise chunks and boosting MRR by +26.5%.'
    )

    add_heading_2('6.5 Discussion of Results')
    add_body(
        'The empirical results substantiate the design philosophy of AI Study Hub. The two-stage retrieval pipeline strikes an optimal balance '
        'between retrieval speed and semantic precision. PyMuPDF eliminates the multi-minute ingestion delay common in commercial tools, while '
        'temperature confinement (T=0.2) guarantees that students receive strictly verifiable, syllabus-grounded facts with verified page citations.'
    )

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # CHAPTER 7 – CONCLUSION AND FUTURE WORK
    # --------------------------------------------------------------------------
    add_heading_1('7. CONCLUSION AND FUTURE WORK')

    add_heading_2('7.1 Conclusion')
    add_body(
        'AI Study Hub (StudyMate) was conceptualized, designed, and developed to address the acute limitations of generic Large Language Models '
        'and vanilla RAG systems in academic higher education. By combining ultra-fast local C-based document parsing (~7 ms/page) with an intelligent '
        'multimodal vision fallback, two-stage neural cross-encoder re-ranking, and hallucination-suppressed Gemini 2.5 Flash generation, the platform '
        'delivers a reliable, verifiable, and interactive study companion.'
    )
    add_body(
        'Empirical evaluation across 43 pages of university course materials demonstrated that the proposed neural re-ranking architecture achieves '
        '89.5% Hit@3 (+18.1% over standard vector search), an MRR of 0.86 (+26.5%), and 95.2% RAGAS faithfulness, while slashing factual hallucinations '
        'from 34.5% to under 2.5%. Beyond conversational search, the autonomous generation of flashcards, quizzes, printable PDFs, and native Anki (.apkg) decks '
        'streamlines exam preparation and establishes a new benchmark for academic AI tools.'
    )

    add_heading_2('7.2 Major Contributions')
    add_bullet('1. Dual-Engine High-Throughput Parser: ', 'Implemented PyMuPDF C-engine extraction achieving 160× speedup over cloud vision OCR, with seamless Gemini Multimodal Vision fallback.')
    add_bullet('2. Two-Stage Neural Re-Ranking Pipeline: ', 'Integrated FastEmbed dense vectors with ONNX-quantized ms-marco-MiniLM cross-encoders, eliminating 24.4% false-positive noise chunks for only ~45 ms overhead.')
    add_bullet('3. Strict Hallucination Suppression & Provenance: ', 'Enforced strict temperature confinement (T=0.2) and prompt boundaries, guaranteeing verified [Page X] citations.')
    add_bullet('4. Automated Active Recall Synthesis: ', 'Engineered automated generation of interactive flashcards and multiple-choice quizzes with explanations, exportable to printable PDFs and native Anki (.apkg) decks.')
    add_bullet('5. Transparent Telemetry & 3-Way Architectural Ablation: ', 'Built real-time micro-latency profiling into UI performance pills and created an interactive side-by-side comparison modal.')

    add_heading_2('7.3 Limitations')
    add_bullet('• Dependency on Internet Connectivity: ', 'While parsing, embedding, and re-ranking execute locally, generation requires active connection to the Google Gemini API and Supabase.')
    add_bullet('• OCR on Poorly Scanned Handwritten Text: ', 'Heavily degraded handwritten cursive notes may experience lower character recognition accuracy.')
    add_bullet('• Free-Tier Cloud Rate Limits: ', 'High-concurrency requests are subject to Gemini free-tier rate limits (15 requests per minute).')

    add_heading_2('7.4 Future Scope')
    add_bullet('1. Fully Offline Local LLM Support: ', 'Integrate Ollama or Llama.cpp to run quantized 4-bit local LLMs (e.g., Llama-3-8B-Instruct or Mistral-7B) for completely offline study environments.')
    add_bullet('2. Hybrid BM25 + Dense Fusion: ', 'Incorporate sparse lexical BM25 indexing alongside dense vector search using Reciprocal Rank Fusion (RRF) for enhanced acronym matching.')
    add_bullet('3. Knowledge Graph Visualization: ', 'Construct interactive concept maps and knowledge graphs visualizing prerequisites and topical dependencies across lecture modules.')
    add_bullet('4. Multi-Student Collaborative Study Rooms: ', 'Introduce shared study workspaces where student cohorts can collaboratively annotate documents and quiz each other in real time.')

    add_heading_2('7.5 Final Remarks')
    add_body(
        'AI Study Hub proves that modern AI in education must prioritize factual grounding, transparent provenance, and active revision over passive text generation. '
        'By anchoring every answer in verified course notes and empowering students with automated spaced-repetition tools, AI Study Hub bridges the gap '
        'between raw academic documents and true academic mastery.'
    )

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # REFERENCES
    # --------------------------------------------------------------------------
    add_heading_1('REFERENCES')

    refs = [
        "[1] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. T. Yih, T. Rocktäschel, S. Riedel, and D. Kiela, "
        "“Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks,” in Advances in Neural Information Processing Systems (NeurIPS), vol. 33, pp. 9459–9474, 2020.",

        "[2] R. Nogueira, Z. Jiang, and J. Lin, “Document Ranking with a Pretrained Sequence-to-Sequence Model,” in Proceedings of the 2020 Conference on Empirical Methods in "
        "Natural Language Processing (EMNLP), pp. 708–718, 2020, doi: 10.18653/v1/2020.emnlp-main.55.",

        "[3] S. Humeau, K. Shuster, M. S. Burtsev, J. Weston, and Y. Lan, “Poly-encoders: Architectures and Pre-training Strategies for Fast and Accurate Multi-sentence Scoring,” "
        "in International Conference on Learning Representations (ICLR), 2020.",

        "[4] S. Es, J. James, L. Espinosa-Anke, and S. Schockaert, “RAGAS: Automated Evaluation of Retrieval Augmented Generation,” in Proceedings of the 18th Conference of the European "
        "Chapter of the Association for Computational Linguistics (EACL), pp. 150–158, 2024, arXiv:2309.15217.",

        "[5] G. V. Cormack, C. L. A. Clarke, and S. Büttcher, “Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods,” in Proceedings of the 32nd Annual "
        "International ACM SIGIR Conference on Research and Development in Information Retrieval, 2009, pp. 758–759, doi: 10.1145/1571941.1572114.",

        "[6] C. Tang, J. Ruan, X. Wang, Z. Wang, W. Wang, L. Li, and J. Ren, “Multi-Stage Iterative Retrieval for Power Communication Document Generation: An Agentic RAG Workflow,” "
        "in Proceedings of the 2026 International Conference on Generative Artificial Intelligence and Information Security (GAIIS), 2026, pp. 135–140.",

        "[7] B. Praneeth, Mohana, E. C. Nattem, K. Jetti, B. K. Kavyashree, D. Rakshitha, P. Ramakanth Kumar, and K. Sreelakshmi, “Optimization of Customer Feedback "
        "Summarization Using Large Language Models (LLM) and Advanced Retrieval-Augmented Generation,” IEEE Access, vol. 13, pp. 124319–124332, 2025, doi: 10.1109/ACCESS.2025.3588337.",

        "[8] K. Järvelin and J. Kekäläinen, “Cumulated Gain-Based Evaluation of IR Techniques,” ACM Transactions on Information Systems (TOIS), vol. 20, no. 4, pp. 422–446, 2002.",

        "[9] FastEmbed Development Team, “FastEmbed: Fast, Accurate, and Lightweight Python Library for Embedding and Re-Ranking Generation,” Qdrant, 2024. [Online]. "
        "Available: https://github.com/qdrant/fastembed.",

        "[10] Supabase, “pgvector: Open-source Vector Similarity Search for PostgreSQL,” Supabase Documentation, 2024. [Online]. "
        "Available: https://supabase.com/docs/guides/database/extensions/pgvector.",

        "[11] Google, “Gemini 2.5 Flash API Documentation & Structured Outputs,” Google AI for Developers, 2024. [Online]. "
        "Available: https://ai.google.dev/gemini-api/docs.",

        "[12] PyMuPDF Authors, “PyMuPDF Documentation: High Performance PDF Parsing in Python,” Artifex Software, 2024. [Online]. "
        "Available: https://pymupdf.readthedocs.io/en/latest/.",

        "[13] D. Elmes, “Genanki: A Python Library for Generating Anki Decks,” 2024. [Online]. "
        "Available: https://github.com/kerrickstaley/genanki.",

        "[14] W3C, “Web Speech API Specification: Speech Synthesis,” World Wide Web Consortium, 2023. [Online]. "
        "Available: https://www.w3.org/TR/speech-api/."
    ]

    for ref in refs:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(ref)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    output_path = "AI_Study_Hub_Project_Report_With_Images.docx"
    try:
        doc.save("AI_Study_Hub_Project_Report.docx")
        print("Successfully updated: AI_Study_Hub_Project_Report.docx")
    except PermissionError:
        print("Note: AI_Study_Hub_Project_Report.docx is open in Word. Saved to AI_Study_Hub_Project_Report_With_Images.docx")
    doc.save(output_path)
    print(f"Successfully generated: {output_path}")

if __name__ == "__main__":
    create_project_report()
