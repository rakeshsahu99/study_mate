import io
import random
import genanki
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


def export_flashcards_anki(flashcards: list, title: str = "AI Study Hub Flashcards") -> bytes:
    """
    Generates a native Anki deck (.apkg file) containing flashcards.
    """
    model_id = random.randrange(1000000000, 2000000000)
    deck_id = random.randrange(1000000000, 2000000000)
    
    style = """
    .card {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 18px;
        text-align: center;
        color: #1e293b;
        background-color: #f8fafc;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #cbd5e1;
    }
    .question {
        font-weight: 600;
        color: #4f46e5;
        font-size: 20px;
    }
    .answer {
        margin-top: 15px;
        color: #334155;
        font-size: 16px;
        line-height: 1.5;
    }
    hr {
        border: none;
        border-top: 1px solid #e2e8f0;
        margin: 18px 0;
    }
    """
    
    model = genanki.Model(
        model_id,
        'AI Study Hub Flashcard Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'}
        ],
        templates=[
            {
                'name': 'Flashcard',
                'qfmt': '<div class="card"><div class="question">{{Question}}</div></div>',
                'afmt': '<div class="card"><div class="question">{{Question}}</div><hr><div class="answer">{{Answer}}</div></div>',
            }
        ],
        css=style
    )
    
    deck = genanki.Deck(deck_id, title)
    for fc in flashcards:
        front = fc.get("front", "").replace("\n", "<br>")
        back = fc.get("back", "").replace("\n", "<br>")
        note = genanki.Note(model=model, fields=[front, back])
        deck.add_note(note)
        
    buffer = io.BytesIO()
    genanki.Package(deck).write_to_file(buffer)
    return buffer.getvalue()


def export_quiz_anki(quiz_questions: list, title: str = "AI Study Hub Quiz Deck") -> bytes:
    """
    Generates a native Anki deck (.apkg file) from quiz questions.
    """
    model_id = random.randrange(1000000000, 2000000000)
    deck_id = random.randrange(1000000000, 2000000000)
    
    style = """
    .card {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 16px;
        text-align: left;
        color: #1e293b;
        background-color: #ffffff;
        padding: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
    }
    .question {
        font-weight: bold;
        color: #4f46e5;
        font-size: 18px;
        margin-bottom: 12px;
    }
    .options {
        margin: 10px 0;
        line-height: 1.6;
    }
    .answer {
        margin-top: 15px;
        color: #059669;
        font-weight: bold;
    }
    .explanation {
        margin-top: 8px;
        color: #475569;
        font-style: italic;
    }
    hr {
        border: none;
        border-top: 1px solid #cbd5e1;
        margin: 15px 0;
    }
    """
    
    model = genanki.Model(
        model_id,
        'AI Study Hub Quiz Model',
        fields=[
            {'name': 'QuestionAndOptions'},
            {'name': 'AnswerAndExplanation'}
        ],
        templates=[
            {
                'name': 'Quiz Card',
                'qfmt': '<div class="card">{{QuestionAndOptions}}</div>',
                'afmt': '<div class="card">{{QuestionAndOptions}}<hr>{{AnswerAndExplanation}}</div>',
            }
        ],
        css=style
    )
    
    deck = genanki.Deck(deck_id, title)
    for q in quiz_questions:
        question_text = q.get("question", "").replace("\n", "<br>")
        options = q.get("options", [])
        correct_idx = q.get("correct_idx", 0)
        explanation = q.get("explanation", "").replace("\n", "<br>")
        
        opt_html = "<br>".join([f"<b>{chr(65+i)}.</b> {opt}" for i, opt in enumerate(options)])
        front_content = f'<div class="question">{question_text}</div><div class="options">{opt_html}</div>'
        
        correct_opt_text = options[correct_idx] if 0 <= correct_idx < len(options) else ""
        back_content = f'<div class="answer">Correct Answer: {chr(65+correct_idx)}. {correct_opt_text}</div><div class="explanation">Rationale: {explanation}</div>'
        
        note = genanki.Note(model=model, fields=[front_content, back_content])
        deck.add_note(note)
        
    buffer = io.BytesIO()
    genanki.Package(deck).write_to_file(buffer)
    return buffer.getvalue()


def export_flashcards_pdf(flashcards: list, title: str = "AI Study Hub - Flashcards") -> bytes:
    """
    Builds a printable PDF document containing flashcards in styled boxes.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#4f46e5'),
        alignment=1,
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=12,
        textColor=colors.HexColor('#64748b'),
        alignment=1,
        spaceAfter=15
    )
    q_label_style = ParagraphStyle(
        'QLabel',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#4f46e5'),
        spaceAfter=4
    )
    a_label_style = ParagraphStyle(
        'ALabel',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#059669'),
        spaceBefore=6,
        spaceAfter=2
    )
    a_text_style = ParagraphStyle(
        'AText',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155')
    )
    
    story = [
        Paragraph(title, title_style),
        Paragraph("Generated by AI Study Hub RAG System", subtitle_style),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor('#e2e8f0'), spaceAfter=15)
    ]
    
    for idx, fc in enumerate(flashcards, 1):
        front = fc.get("front", "")
        back = fc.get("back", "")
        
        card_elements = [
            Paragraph(f"Flashcard #{idx}: {front}", q_label_style),
            Paragraph("Answer / Explanation:", a_label_style),
            Paragraph(back, a_text_style)
        ]
        
        card_table = Table([[card_elements]], colWidths=[540])
        card_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
            ('PADDING', (0,0), (-1,-1), 10),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        
        story.append(card_table)
        story.append(Spacer(1, 12))
        
    doc.build(story)
    return buffer.getvalue()


def export_quiz_pdf(quiz_questions: list, title: str = "AI Study Hub - Practice Quiz") -> bytes:
    """
    Builds a printable PDF document containing quiz questions and an Answer Key.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#4f46e5'),
        alignment=1,
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=12,
        textColor=colors.HexColor('#64748b'),
        alignment=1,
        spaceAfter=15
    )
    q_title_style = ParagraphStyle(
        'QTitle',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4
    )
    opt_style = ParagraphStyle(
        'OptStyle',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155'),
        leftIndent=10
    )
    ans_key_header_style = ParagraphStyle(
        'AnsKeyHeader',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#4f46e5'),
        spaceBefore=15,
        spaceAfter=10
    )
    ans_key_item_style = ParagraphStyle(
        'AnsKeyItem',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=8
    )
    
    story = [
        Paragraph(title, title_style),
        Paragraph("Generated by AI Study Hub RAG System", subtitle_style),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor('#e2e8f0'), spaceAfter=15)
    ]
    
    for idx, q in enumerate(quiz_questions, 1):
        q_text = q.get("question", "")
        options = q.get("options", [])
        
        q_flowables = [
            Paragraph(f"Question {idx}: {q_text}", q_title_style),
            Spacer(1, 4)
        ]
        
        for o_idx, opt in enumerate(options):
            opt_letter = chr(65 + o_idx)
            q_flowables.append(Paragraph(f"<b>[{opt_letter}]</b>  {opt}", opt_style))
            q_flowables.append(Spacer(1, 2))
            
        q_box = Table([[q_flowables]], colWidths=[540])
        q_box.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ffffff')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
            ('PADDING', (0,0), (-1,-1), 10),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(q_box)
        story.append(Spacer(1, 10))
        
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e1'), spaceBefore=10, spaceAfter=10))
    story.append(Paragraph("Answer Key & Rationale Explanations", ans_key_header_style))
    
    for idx, q in enumerate(quiz_questions, 1):
        correct_idx = q.get("correct_idx", 0)
        options = q.get("options", [])
        correct_letter = chr(65 + correct_idx) if 0 <= correct_idx < len(options) else "?"
        correct_text = options[correct_idx] if 0 <= correct_idx < len(options) else ""
        explanation = q.get("explanation", "")
        
        ans_str = f"<b>Q{idx}: [{correct_letter}] {correct_text}</b><br/><font color='#475569'><i>Explanation:</i> {explanation}</font>"
        story.append(Paragraph(ans_str, ans_key_item_style))
        story.append(Spacer(1, 4))
        
    doc.build(story)
    return buffer.getvalue()
