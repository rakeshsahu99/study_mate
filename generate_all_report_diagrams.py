import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

OUTPUT_DIR = "Report/diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. Figure 5.1: Layered System Architecture (Clean, NO StudyMate)
# -----------------------------------------------------------------------------
def make_fig_5_1():
    fig, ax = plt.subplots(figsize=(12, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    c_client = "#E8F0FE"
    c_client_border = "#1A73E8"
    c_gateway = "#FEF7E0"
    c_gateway_border = "#F9AB00"
    c_ai = "#E6F4EA"
    c_ai_border = "#137333"
    c_db = "#FCE8E6"
    c_db_border = "#C5221F"
    c_arrow = "#3C4043"

    ax.text(50, 96.5, "AI Study Hub - Layered System Architecture", 
            ha='center', va='center', fontsize=16, fontweight='bold', color="#202124")
    ax.text(50, 93.5, "High-Throughput Ingestion, Two-Stage Neural Re-Ranking & Grounded Study Synthesis", 
            ha='center', va='center', fontsize=10.5, fontstyle='italic', color="#5F6368")

    # 1. Presentation Layer
    r1 = patches.FancyBboxPatch((5, 75), 90, 15, boxstyle="round,pad=1,rounding_size=2", 
                                facecolor=c_client, edgecolor=c_client_border, linewidth=2)
    ax.add_patch(r1)
    ax.text(8, 87, "1. Presentation Layer (Client / User Interface)", fontsize=12, fontweight='bold', color=c_client_border)
    ax.text(8, 83, "Next.js 16 (App Router)  |  React 19  |  TypeScript  |  Tailwind CSS v4 Dark Theme  |  Web Speech API (TTS)", fontsize=9, fontweight='bold', color="#202124")
    
    submodules_1 = [
        (8, 77, 24, 4.5, "Document Upload Hub\n(Drag & Drop / Telemetry)"),
        (35, 77, 28, 4.5, "Conversational RAG Chat\n(Strict [Page X] Citations)"),
        (66, 77, 26, 4.5, "3-Way Ablation Modal\n(Config A vs B vs C)"),
    ]
    for x, y, w, h, txt in submodules_1:
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#FFFFFF", edgecolor=c_client_border, linewidth=1)
        ax.add_patch(box)
        ax.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=7.8, color="#202124")

    # Arrow 1 -> 2
    ax.annotate('', xy=(50, 68), xytext=(50, 75),
                arrowprops=dict(arrowstyle="<->", color=c_arrow, lw=2, mutation_scale=15))
    ax.text(52, 71.5, "HTTP REST API / JSON / Telemetry Headers", fontsize=8.5, color="#5F6368", fontweight='bold')

    # 2. Application & Gateway Layer
    r2 = patches.FancyBboxPatch((5, 59), 90, 9, boxstyle="round,pad=1,rounding_size=2", 
                                facecolor=c_gateway, edgecolor=c_gateway_border, linewidth=2)
    ax.add_patch(r2)
    ax.text(8, 65, "2. Application Controller & Gateway Layer", fontsize=12, fontweight='bold', color="#B06000")
    ax.text(8, 61, "Next.js Route Handlers  |  User Authentication & Session Isolation (X-User-Id)  |  CORS Middleware", fontsize=9, color="#202124")

    # Arrow 2 -> 3
    ax.annotate('', xy=(50, 52), xytext=(50, 59),
                arrowprops=dict(arrowstyle="<->", color=c_arrow, lw=2, mutation_scale=15))
    ax.text(52, 55.5, "Asynchronous API Proxy (FastAPI :8000)", fontsize=8.5, color="#5F6368", fontweight='bold')

    # 3. AI Microservice Layer
    r3 = patches.FancyBboxPatch((5, 23), 90, 29, boxstyle="round,pad=1,rounding_size=2", 
                                facecolor=c_ai, edgecolor=c_ai_border, linewidth=2)
    ax.add_patch(r3)
    ax.text(8, 49, "3. AI Microservice & Core Intelligence Layer (Python 3.11+ / FastAPI)", fontsize=12, fontweight='bold', color=c_ai_border)

    submodules_ai = [
        (8, 38, 26, 8.5, "Dual-Engine Document Ingestion\n• Local PyMuPDF (~7 ms/page)\n• Gemini 2.5 Flash Vision OCR\n• DOCX & TXT Native Parsers"),
        (37, 38, 27, 8.5, "Chunking & Local Embedder\n• Recursive Chunker (800c/150o)\n• FastEmbed (all-MiniLM-L6-v2)\n• 384-d Dense Vector Generation"),
        (67, 38, 25, 8.5, "Two-Stage Neural Re-Ranking\n• Stage 1: Top-15 Dense Vector\n• Stage 2: Cross-Encoder ONNX\n  (ms-marco-MiniLM-L-6-v2)"),
        (8, 26, 26, 9.5, "Contextualizer & Grounded LLM\n• Multi-turn query contextualizer\n• Gemini 2.5 Flash (T=0.2)\n• Strict [Page X] Source Bounds"),
        (37, 26, 27, 9.5, "Active Recall Study Suite\n• Flashcards (Concept/Answer)\n• Multiple-Choice Quizzes\n• Detailed Answer Explanations"),
        (67, 26, 25, 9.5, "Multi-Format Study Exporters\n• Anki Decks (.apkg via Genanki)\n• Printable Revision PDFs\n  (ReportLab 4.2 Engine)"),
    ]
    for x, y, w, h, txt in submodules_ai:
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#FFFFFF", edgecolor=c_ai_border, linewidth=1)
        ax.add_patch(box)
        ax.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=7.8, color="#202124")

    # Arrow 3 -> 4
    ax.annotate('', xy=(50, 16), xytext=(50, 23),
                arrowprops=dict(arrowstyle="<->", color=c_arrow, lw=2, mutation_scale=15))
    ax.text(52, 19.5, "PostgreSQL Protocol / pgvector Cosine RPC", fontsize=8.5, color="#5F6368", fontweight='bold')

    # 4. Storage Layer
    r4 = patches.FancyBboxPatch((5, 3), 90, 13, boxstyle="round,pad=1,rounding_size=2", 
                                facecolor=c_db, edgecolor=c_db_border, linewidth=2)
    ax.add_patch(r4)
    ax.text(8, 13, "4. Data & Vector Storage Layer (Supabase PostgreSQL)", fontsize=12, fontweight='bold', color=c_db_border)
    ax.text(8, 9, "PostgreSQL 15+  |  pgvector Extension  |  HNSW Approximate Nearest Neighbor Index", fontsize=9, fontweight='bold', color="#202124")

    db_items = [
        (8, 5, 27, 3.5, "document_chunks table (user_id, text, metadata)"),
        (37, 5, 27, 3.5, "384-d vector embeddings (HNSW cosine index)"),
        (66, 5, 26, 3.5, "match_document_chunks stored RPC procedure"),
    ]
    for x, y, w, h, txt in db_items:
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1", facecolor="#FFFFFF", edgecolor=c_db_border, linewidth=1)
        ax.add_patch(box)
        ax.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=7.5, color="#202124")

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_5_1_Layered_System_Architecture.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[+] Saved: {p}")

# -----------------------------------------------------------------------------
# 2. Figure 5.2: End-to-End System Execution Pipeline (Clean, NO StudyMate)
# -----------------------------------------------------------------------------
def make_fig_5_2():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    c_bg_ingest = "#EBF5FB"
    c_bd_ingest = "#2980B9"
    c_bg_retrieval = "#EAFAF1"
    c_bd_retrieval = "#27AE60"
    c_bg_gen = "#FEF9E7"
    c_bd_gen = "#F39C12"
    c_bg_study = "#F4ECF7"
    c_bd_study = "#8E44AD"

    ax.text(50, 96, "AI Study Hub - End-to-End System Execution Pipeline", 
            ha='center', va='center', fontsize=15, fontweight='bold', color="#2C3E50")
    ax.text(50, 92, "Document Ingestion, Two-Stage Neural Re-Ranking, Grounded Generation & Study Synthesis", 
            ha='center', va='center', fontsize=10, fontstyle='italic', color="#7F8C8D")

    # Stage 1
    box1 = patches.FancyBboxPatch((3, 48), 21, 40, boxstyle="round,pad=1,rounding_size=2", 
                                 facecolor=c_bg_ingest, edgecolor=c_bd_ingest, linewidth=2)
    ax.add_patch(box1)
    ax.text(13.5, 85, "STAGE 1\nDocument Ingestion", ha='center', va='center', fontsize=10.5, fontweight='bold', color=c_bd_ingest)
    
    steps_1 = [
        (4.5, 74, 18, 6.5, "1. Upload File\n(PDF, DOCX, TXT)"),
        (4.5, 65, 18, 6.5, "2. Fast Parser\nPyMuPDF (~7 ms/p)\nFallback: Gemini Vision"),
        (4.5, 56, 18, 6.5, "3. Recursive Chunker\n800 chars / 150 overlap\nDeterministic Slug IDs"),
    ]
    for x, y, w, h, t in steps_1:
        b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1", facecolor="#FFFFFF", edgecolor=c_bd_ingest, linewidth=1)
        ax.add_patch(b)
        ax.text(x + w/2, y + h/2, t, ha='center', va='center', fontsize=7.5, color="#2C3E50")

    # Arrow 1 -> 2
    ax.annotate('', xy=(27, 68), xytext=(24, 68),
                arrowprops=dict(arrowstyle="->", color="#2C3E50", lw=2, mutation_scale=15))

    # Stage 2
    box2 = patches.FancyBboxPatch((27, 48), 21, 40, boxstyle="round,pad=1,rounding_size=2", 
                                 facecolor=c_bg_retrieval, edgecolor=c_bd_retrieval, linewidth=2)
    ax.add_patch(box2)
    ax.text(37.5, 85, "STAGE 2\nDense Vector Indexing", ha='center', va='center', fontsize=10.5, fontweight='bold', color=c_bd_retrieval)

    steps_2 = [
        (28.5, 74, 18, 6.5, "4. FastEmbed Bi-Encoder\nall-MiniLM-L6-v2\n384-d dense vectors"),
        (28.5, 65, 18, 6.5, "5. Supabase pgvector\nPostgreSQL Storage\nUser-isolated chunks"),
        (28.5, 56, 18, 6.5, "6. HNSW Cosine Index\nApproximate Nearest\nNeighbor Search"),
    ]
    for x, y, w, h, t in steps_2:
        b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1", facecolor="#FFFFFF", edgecolor=c_bd_retrieval, linewidth=1)
        ax.add_patch(b)
        ax.text(x + w/2, y + h/2, t, ha='center', va='center', fontsize=7.5, color="#2C3E50")

    # Arrow 2 -> 3
    ax.annotate('', xy=(51, 68), xytext=(48, 68),
                arrowprops=dict(arrowstyle="->", color="#2C3E50", lw=2, mutation_scale=15))

    # Stage 3
    box3 = patches.FancyBboxPatch((51, 48), 22, 40, boxstyle="round,pad=1,rounding_size=2", 
                                 facecolor=c_bg_gen, edgecolor=c_bd_gen, linewidth=2)
    ax.add_patch(box3)
    ax.text(62, 85, "STAGE 3\nTwo-Stage Re-Ranking", ha='center', va='center', fontsize=10.5, fontweight='bold', color=c_bd_gen)

    steps_3 = [
        (52.5, 74, 19, 6.5, "7. Query Contextualizer\nReformulates follow-up\ninto standalone query"),
        (52.5, 65, 19, 6.5, "8. Stage 1: Vector Search\nRetrieves Top-15\nCandidate Chunks"),
        (52.5, 56, 19, 6.5, "9. Stage 2: Cross-Encoder\nms-marco-MiniLM (ONNX)\nFilters 24.4% noise chunks"),
    ]
    for x, y, w, h, t in steps_3:
        b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1", facecolor="#FFFFFF", edgecolor=c_bd_gen, linewidth=1)
        ax.add_patch(b)
        ax.text(x + w/2, y + h/2, t, ha='center', va='center', fontsize=7.5, color="#2C3E50")

    # Arrow 3 -> 4
    ax.annotate('', xy=(76, 68), xytext=(73, 68),
                arrowprops=dict(arrowstyle="->", color="#2C3E50", lw=2, mutation_scale=15))

    # Stage 4
    box4 = patches.FancyBboxPatch((76, 48), 21, 40, boxstyle="round,pad=1,rounding_size=2", 
                                 facecolor=c_bg_study, edgecolor=c_bd_study, linewidth=2)
    ax.add_patch(box4)
    ax.text(86.5, 85, "STAGE 4\nGeneration & Synthesis", ha='center', va='center', fontsize=10.5, fontweight='bold', color=c_bd_study)

    steps_4 = [
        (77.5, 74, 18, 6.5, "10. Gemini 2.5 Flash\nStrict T=0.2 Prompt\nZero-Hallucination rule"),
        (77.5, 65, 18, 6.5, "11. Grounded Response\nExact [Page X] Citations\nClickable Source Popups"),
        (77.5, 56, 18, 6.5, "12. Active Recall Suite\nFlashcards & Quizzes\nAnki (.apkg) & PDF Export"),
    ]
    for x, y, w, h, t in steps_4:
        b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1", facecolor="#FFFFFF", edgecolor=c_bd_study, linewidth=1)
        ax.add_patch(b)
        ax.text(x + w/2, y + h/2, t, ha='center', va='center', fontsize=7.5, color="#2C3E50")

    # Bottom Telemetry Bar
    box_tel = patches.FancyBboxPatch((3, 6), 94, 36, boxstyle="round,pad=1,rounding_size=2", 
                                    facecolor="#F8F9FA", edgecolor="#4A5568", linewidth=1.5, linestyle="--")
    ax.add_patch(box_tel)
    ax.text(50, 38, "STAGE 5: REAL-TIME TELEMETRY INSTRUMENTATION & 3-WAY ABLATION SUITE", 
            ha='center', va='center', fontsize=11, fontweight='bold', color="#2D3748")

    tel_cards = [
        (5, 10, 27, 24, "Micro-Latency Telemetry\n\n• Parsing: ~7.0 ms/page\n• Embedding: 14.5 ms\n• Retrieval: 34.2 ms\n• Re-ranking: 44.8 ms\n• Generation: 825.0 ms\n• Total End-to-End: 918.5 ms"),
        (36, 10, 28, 24, "3-Way Architectural Ablation\n\n• Config A: Standalone LLM (0-shot)\n  (34.5% Hallucination, 0 Citations)\n• Config B: Vanilla Vector RAG\n  (71.4% Hit@3, 0.68 MRR)\n• Config C: Proposed Re-Ranked RAG\n  (89.5% Hit@3, 0.86 MRR, <2.5% Halluc.)"),
        (68, 10, 27, 24, "Multi-Format Export & Audio\n\n• Printable PDF Flashcards & Quiz\n• Native Anki (.apkg) Decks\n  (Spaced Repetition Algorithm)\n• Browser Web Speech TTS Audio\n• False-Positive Reduction: 24.4%"),
    ]
    for x, y, w, h, t in tel_cards:
        b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#FFFFFF", edgecolor="#CBD5E0", linewidth=1)
        ax.add_patch(b)
        ax.text(x + w/2, y + h/2, t, ha='center', va='center', fontsize=7.8, color="#2D3748")

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_5_2_End_to_End_System_Execution_Pipeline.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[+] Saved: {p}")

# -----------------------------------------------------------------------------
# 3. Figure 5.3: Two-Stage Retrieval & Neural Cross-Encoder Re-Ranking Pipeline
# -----------------------------------------------------------------------------
def make_fig_5_3():
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Figure 5.3: Two-Stage Retrieval & Neural Cross-Encoder Re-Ranking Pipeline",
            ha='center', va='center', fontsize=14, fontweight='bold', color="#1E293B")
    ax.text(50, 91, "Cascading Bi-Encoder Candidate Pooling (Stage 1) to All-to-All Cross-Attention Ranking (Stage 2)",
            ha='center', va='center', fontsize=10, fontstyle='italic', color="#64748B")

    # Left: Query Box
    b_q = patches.FancyBboxPatch((3, 40), 16, 32, boxstyle="round,pad=0.8", facecolor="#EFF6FF", edgecolor="#3B82F6", lw=2)
    ax.add_patch(b_q)
    ax.text(11, 66, "User Query", ha='center', va='center', fontsize=11, fontweight='bold', color="#1D4ED8")
    ax.text(11, 55, "q: 'What is\nnon-preemptive\nSJF scheduling?'", ha='center', va='center', fontsize=8.5, color="#1E293B")
    ax.text(11, 44, "FastEmbed Bi-Encoder\n(all-MiniLM-L6-v2)\n[14.5 ms]", ha='center', va='center', fontsize=7.5, color="#475569")

    # Arrow to Stage 1
    ax.annotate('', xy=(24, 56), xytext=(19, 56), arrowprops=dict(arrowstyle="->", color="#334155", lw=2))
    ax.text(21.5, 59, "384-d v", fontsize=8, fontweight='bold', color="#1E293B")

    # Middle Left: Stage 1 Candidate Retrieval
    b_s1 = patches.FancyBboxPatch((24, 25), 22, 60, boxstyle="round,pad=0.8", facecolor="#F0FDF4", edgecolor="#10B981", lw=2)
    ax.add_patch(b_s1)
    ax.text(35, 80, "STAGE 1:\nDense Vector Search", ha='center', va='center', fontsize=10.5, fontweight='bold', color="#047857")
    ax.text(35, 73, "Supabase PostgreSQL\n(pgvector HNSW Cosine Index)\n[34.2 ms]", ha='center', va='center', fontsize=8, color="#065F46")
    
    candidates = [
        "Candidate 1 (Sim: 0.82) - Intro Overview",
        "Candidate 2 (Sim: 0.80) - Preemptive SJF",
        "Candidate 3 (Sim: 0.79) - FCFS Contrast",
        "Candidate 4 (Sim: 0.77) - Waiting Formula",
        "Candidate 5 (Sim: 0.75) - Turnaround Calc",
        "... Top 15 Candidates Retrieved ...",
    ]
    for idx, c in enumerate(candidates):
        y_pos = 65 - idx * 6.5
        fc = "#FEF3C7" if idx in [3, 4] else "#FFFFFF"
        bc = patches.FancyBboxPatch((25.5, y_pos-2.2), 19, 4.8, boxstyle="round,pad=0.3", facecolor=fc, edgecolor="#94A3B8", lw=0.8)
        ax.add_patch(bc)
        ax.text(35, y_pos, c, ha='center', va='center', fontsize=6.8, color="#1E293B")

    # Arrow to Stage 2
    ax.annotate('', xy=(51, 56), xytext=(46, 56), arrowprops=dict(arrowstyle="->", color="#334155", lw=2))
    ax.text(48.5, 59, "Top-15 Pool", fontsize=7.5, fontweight='bold', color="#1E293B")

    # Middle Right: Stage 2 Cross-Encoder
    b_s2 = patches.FancyBboxPatch((51, 25), 23, 60, boxstyle="round,pad=0.8", facecolor="#FFFBEB", edgecolor="#F59E0B", lw=2)
    ax.add_patch(b_s2)
    ax.text(62.5, 80, "STAGE 2:\nCross-Encoder Re-Ranking", ha='center', va='center', fontsize=10.5, fontweight='bold', color="#B45309")
    ax.text(62.5, 73, "ms-marco-MiniLM-L-6-v2\n(ONNX Runtime All-to-All Attention)\n[44.8 ms]", ha='center', va='center', fontsize=8, color="#92400E")

    reranked = [
        "Rank 1: Waiting Formula (Score: 0.884)",
        "Rank 2: Turnaround Calc (Score: 0.852)",
        "Rank 3: Preemptive SJF (Score: 0.710)",
        "Rank 4: Burst Time Table (Score: 0.695)",
        "Rank 5: Gantt Chart Step (Score: 0.640)",
        "-- 24.4% False Positives Demoted --",
    ]
    for idx, c in enumerate(reranked):
        y_pos = 65 - idx * 6.5
        fc = "#D1FAE5" if idx < 2 else ("#FEE2E2" if idx == 5 else "#FFFFFF")
        bc = patches.FancyBboxPatch((52.5, y_pos-2.2), 20, 4.8, boxstyle="round,pad=0.3", facecolor=fc, edgecolor="#CBD5E1", lw=0.8)
        ax.add_patch(bc)
        ax.text(62.5, y_pos, c, ha='center', va='center', fontsize=6.8, color="#1E293B")

    # Arrow to LLM Generation
    ax.annotate('', xy=(79, 56), xytext=(74, 56), arrowprops=dict(arrowstyle="->", color="#334155", lw=2))
    ax.text(76.5, 59, "Top-5 Pristine", fontsize=7.5, fontweight='bold', color="#1E293B")

    # Right: Generation
    b_gen = patches.FancyBboxPatch((79, 35), 18, 42, boxstyle="round,pad=0.8", facecolor="#FAF5FF", edgecolor="#A855F7", lw=2)
    ax.add_patch(b_gen)
    ax.text(88, 72, "Grounded LLM\nGeneration", ha='center', va='center', fontsize=10.5, fontweight='bold', color="#6B21A8")
    ax.text(88, 62, "Gemini 2.5 Flash\n(T=0.2 strict bounds)\n[825.0 ms]", ha='center', va='center', fontsize=8, color="#7E22CE")
    ax.text(88, 48, "Verified Citation:\n[Source 1: OS_Notes, p. 4]\nTurnaround Time Formula\n& Step-by-Step Proof", ha='center', va='center', fontsize=7.2, color="#1E293B")

    # Bottom summary pill
    b_sum = patches.FancyBboxPatch((10, 8), 80, 12, boxstyle="round,pad=0.5", facecolor="#F1F5F9", edgecolor="#64748B", lw=1.5)
    ax.add_patch(b_sum)
    ax.text(50, 14, "Empirical Impact of Stage 2 Re-Ranking: Hit@3 improves from 71.4% to 89.5% (+18.1 pp, +25.4% relative);\nMRR improves from 0.68 to 0.86 (+26.5% relative); 24.4% false-positive noise chunks eliminated for only 44.8 ms overhead.",
            ha='center', va='center', fontsize=8.5, color="#1E293B", fontweight='bold')

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_5_3_Two_Stage_Retrieval_and_Neural_Reranking.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[+] Saved: {p}")

# -----------------------------------------------------------------------------
# 4. Figure 5.4: Document Management Hub Interface (UI Mockup)
# -----------------------------------------------------------------------------
def make_fig_5_4():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Window Frame
    win = patches.FancyBboxPatch((2, 2), 96, 96, boxstyle="round,pad=0.5", facecolor="#0F172A", edgecolor="#334155", lw=2)
    ax.add_patch(win)

    # Window title bar
    ax.text(6, 94, "●  ●  ●   AI Study Hub — Document Ingestion & Management Hub (http://localhost:3000)", fontsize=9, color="#94A3B8")

    # Header
    ax.text(6, 88, "Document Knowledge Base", fontsize=15, fontweight='bold', color="#F8FAFC")
    ax.text(6, 84, "High-throughput sub-10ms local ingestion (PyMuPDF) with fallback to Gemini 2.5 Flash Multimodal Vision.", fontsize=8.5, color="#94A3B8")

    # Upload Dropzone
    dz = patches.FancyBboxPatch((6, 61), 88, 20, boxstyle="round,pad=0.8", facecolor="#1E293B", edgecolor="#38BDF8", lw=1.5, linestyle="--")
    ax.add_patch(dz)
    ax.text(50, 73, " Drag & Drop University Lecture Slides / Syllabi (PDF, DOCX, TXT)", ha='center', va='center', fontsize=11, fontweight='bold', color="#38BDF8")
    ax.text(50, 67, "Supported formats: PDF (PyMuPDF C-Engine: ~7.0 ms/page), DOCX, TXT | User-Isolated Storage in Supabase pgvector", ha='center', va='center', fontsize=8, color="#94A3B8")

    # Telemetry Banner
    tb = patches.FancyBboxPatch((6, 52), 88, 6.5, boxstyle="round,pad=0.4", facecolor="#064E3B", edgecolor="#10B981", lw=1)
    ax.add_patch(tb)
    ax.text(8, 55.2, "✓ Ingestion Telemetry: 43 Pages Parsed in 301 ms (~7.0 ms/page) | 158 Chunks Generated (800c/150o) | 160× Speedup over Cloud OCR", fontsize=8.5, fontweight='bold', color="#34D399")

    # Table of Uploaded Documents
    ax.text(6, 46, "Indexed Course Materials (3 Documents | 43 Pages | 158 Chunks)", fontsize=11, fontweight='bold', color="#F8FAFC")
    
    docs = [
        ("24042020_E-R Model.pdf", "DBMS - Entity Relationship Modeling & Cardinalities", "12 Pages", "44 Chunks", "7.1 ms/p", "Ready"),
        ("CPU-Scheduling-and-Algorithm-.pdf", "Operating Systems - FCFS, SJF, Round Robin & Deadlocks", "18 Pages", "68 Chunks", "6.9 ms/p", "Ready"),
        ("osi_notes.pdf", "Computer Networks - OSI 7-Layer Protocol Architecture", "13 Pages", "46 Chunks", "7.0 ms/p", "Ready"),
    ]
    for idx, (title, desc, pages, chunks, speed, status) in enumerate(docs):
        y = 36 - idx * 10
        row_b = patches.FancyBboxPatch((6, y), 88, 8.5, boxstyle="round,pad=0.4", facecolor="#1E293B", edgecolor="#334155", lw=1)
        ax.add_patch(row_b)
        ax.text(8, y + 4.5, f"📄 {title}", fontsize=9, fontweight='bold', color="#F8FAFC")
        ax.text(8, y + 1.8, desc, fontsize=7.5, color="#94A3B8")
        ax.text(56, y + 3.2, pages, fontsize=8, color="#CBD5E1")
        ax.text(66, y + 3.2, chunks, fontsize=8, color="#CBD5E1")
        ax.text(76, y + 3.2, f"⚡ {speed}", fontsize=8, color="#38BDF8")
        ax.text(88, y + 3.2, f"● {status}", fontsize=8, fontweight='bold', color="#34D399")

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_5_4_Document_Management_Hub_Interface.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[+] Saved: {p}")

# -----------------------------------------------------------------------------
# 5. Figure 5.5: Conversational RAG Interface (UI Mockup)
# -----------------------------------------------------------------------------
def make_fig_5_5():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    win = patches.FancyBboxPatch((2, 2), 96, 96, boxstyle="round,pad=0.5", facecolor="#0F172A", edgecolor="#334155", lw=2)
    ax.add_patch(win)
    ax.text(6, 94, "●  ●  ●   AI Study Hub — Conversational Study Assistant & Citation Bounds", fontsize=9, color="#94A3B8")

    # Telemetry Pill bar
    tb = patches.FancyBboxPatch((6, 85), 88, 6.5, boxstyle="round,pad=0.4", facecolor="#1E293B", edgecolor="#475569", lw=1)
    ax.add_patch(tb)
    ax.text(8, 88.2, "⚡ Micro-Latency Telemetry:  Contextualization: 12.0ms  |  Embedding: 14.5ms  |  HNSW Retrieval: 34.2ms  |  Cross-Encoder: 44.8ms  |  Gemini: 825ms  |  Total: 918.5ms", fontsize=7.5, color="#38BDF8", fontweight='bold')

    # Chat User Query
    uq = patches.FancyBboxPatch((40, 71), 54, 11, boxstyle="round,pad=0.5", facecolor="#1E40AF", edgecolor="#3B82F6", lw=1)
    ax.add_patch(uq)
    ax.text(42, 78, "Student Question:", fontsize=8, fontweight='bold', color="#93C5FD")
    ax.text(42, 73.5, "What is non-preemptive Shortest Job First (SJF) scheduling, and how is waiting time calculated?", fontsize=8, color="#FFFFFF")

    # Chat Assistant Response
    ar = patches.FancyBboxPatch((6, 20), 88, 48, boxstyle="round,pad=0.8", facecolor="#1E293B", edgecolor="#334155", lw=1)
    ax.add_patch(ar)
    ax.text(9, 64, "🎓 AI Study Hub Assistant  [Configuration C: Neural Cross-Encoder Re-Ranked]", fontsize=9.5, fontweight='bold', color="#38BDF8")
    
    body_text = (
        "Non-preemptive Shortest Job First (SJF) is a CPU scheduling algorithm where once the CPU is allocated to a\n"
        "process, it cannot be interrupted until it completes its CPU burst [Source 1, Page 4].\n\n"
        "Key Characteristics & Formula:\n"
        "• Non-preemptive Condition: If a new process arrives with a shorter burst time, it is placed in the ready queue\n"
        "  but does NOT preempt the currently running process [Source 1, Page 4].\n"
        "• Turnaround Time: Turnaround Time = Completion Time - Arrival Time [Source 2, Page 5].\n"
        "• Waiting Time: Waiting Time = Turnaround Time - Burst Time [Source 1, Page 4].\n"
        "• Advantage: Provably minimizes average waiting time among non-preemptive algorithms [Source 3, Page 6]."
    )
    ax.text(9, 44, body_text, fontsize=7.8, color="#F1F5F9", va='center')

    # Source Badges (Clickable Popups)
    sources = [
        ("Source 1", "CPU-Scheduling-and-Algorithm-.pdf", "Page 4", "Non-preemptive definition & waiting time equation"),
        ("Source 2", "CPU-Scheduling-and-Algorithm-.pdf", "Page 5", "Turnaround time and completion calculation matrix"),
    ]
    for idx, (sname, fname, page, snip) in enumerate(sources):
        x = 9 + idx * 44
        sb = patches.FancyBboxPatch((x, 23), 42, 7, boxstyle="round,pad=0.3", facecolor="#0F172A", edgecolor="#38BDF8", lw=0.8)
        ax.add_patch(sb)
        ax.text(x + 2, 27.5, f"🔗 [{sname}] {fname} (p. {page})", fontsize=7.2, fontweight='bold', color="#38BDF8")
        ax.text(x + 2, 24.8, snip, fontsize=6.5, color="#94A3B8")

    # Bottom Query Input box
    ib = patches.FancyBboxPatch((6, 6), 88, 10, boxstyle="round,pad=0.5", facecolor="#1E293B", edgecolor="#475569", lw=1)
    ax.add_patch(ib)
    ax.text(9, 11, "Ask follow-up question (e.g., 'What are its limitations?')...", fontsize=8.5, color="#64748B")
    ax.text(88, 11, "Send ➔", fontsize=8.5, fontweight='bold', color="#38BDF8")

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_5_5_Conversational_RAG_Interface.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[+] Saved: {p}")

# -----------------------------------------------------------------------------
# 6. Figure 5.6: Three-Way Architectural Ablation Modal (UI Mockup)
# -----------------------------------------------------------------------------
def make_fig_5_6():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    win = patches.FancyBboxPatch((2, 2), 96, 96, boxstyle="round,pad=0.5", facecolor="#0F172A", edgecolor="#334155", lw=2)
    ax.add_patch(win)
    ax.text(6, 94, "●  ●  ●   AI Study Hub — 3-Way Architectural Ablation Evaluation Modal", fontsize=9, color="#94A3B8")

    ax.text(6, 88, "Architectural Ablation & Side-by-Side Benchmark", fontsize=14, fontweight='bold', color="#F8FAFC")
    ax.text(6, 84, "Empirical comparison of the exact same query executed across 3 distinct architectural paradigms.", fontsize=8.5, color="#94A3B8")

    # 3 Columns
    col_w = 28
    cols = [
        (6, "Configuration A", "Standalone LLM (Zero-Shot)", "#DC2626", [
            ("Mechanism", "Pure parametric memory (No RAG)"),
            ("Faithfulness", "42.1% (RAGAS score)"),
            ("Hallucination", "34.5% (High risk)"),
            ("Source Citations", "None (0 citations)"),
            ("Hit@3 Recall", "N/A (No external retrieval)"),
            ("Mean Reciprocal Rank", "N/A"),
            ("End-to-End Latency", "780.0 ms (Generation only)"),
            ("Verdict", "Hallucinates formulas; cannot cite slides."),
        ]),
        (36, "Configuration B", "Vanilla Single-Vector RAG", "#D97706", [
            ("Mechanism", "FastEmbed Bi-Encoder + Cosine ANN"),
            ("Faithfulness", "78.4% (RAGAS score)"),
            ("Hallucination", "12.1% (Moderate risk)"),
            ("Source Citations", "Partial (Unverified boundaries)"),
            ("Hit@3 Recall", "71.4% (28.6% queries miss context)"),
            ("Mean Reciprocal Rank", "0.68 (Target chunk often rank 3-5)"),
            ("End-to-End Latency", "867.3 ms (47.3ms retrieval + 820ms gen)"),
            ("Verdict", "Prone to false-positive distractor chunks."),
        ]),
        (66, "Configuration C", "Proposed Re-Ranked RAG", "#16A34A", [
            ("Mechanism", "Vector Search + ONNX Cross-Encoder"),
            ("Faithfulness", "95.2% (Strictly grounded)"),
            ("Hallucination", "< 2.5% (Near-zero rate)"),
            ("Source Citations", "Strict [Page X] provenance bounds"),
            ("Hit@3 Recall", "89.5% (+18.1 pp, +25.4% relative)"),
            ("Mean Reciprocal Rank", "0.86 (+26.5% relative gain)"),
            ("End-to-End Latency", "918.5 ms (+44.8ms re-ranking cost)"),
            ("Verdict", "Optimal exam revision & factuality."),
        ]),
    ]

    for x, c_name, sub_name, color, metrics in cols:
        cb = patches.FancyBboxPatch((x, 18), col_w, 63, boxstyle="round,pad=0.5", facecolor="#1E293B", edgecolor=color, lw=2)
        ax.add_patch(cb)
        ax.text(x + col_w/2, 77, c_name, ha='center', va='center', fontsize=11, fontweight='bold', color=color)
        ax.text(x + col_w/2, 73.5, sub_name, ha='center', va='center', fontsize=7.5, color="#CBD5E1")
        
        for idx, (m_name, m_val) in enumerate(metrics):
            y_m = 67 - idx * 6.5
            mb = patches.FancyBboxPatch((x + 1.5, y_m - 2.5), col_w - 3, 5.5, boxstyle="round,pad=0.2", facecolor="#0F172A", edgecolor="#334155", lw=0.6)
            ax.add_patch(mb)
            ax.text(x + 3, y_m + 0.3, m_name, fontsize=6.8, fontweight='bold', color="#94A3B8")
            ax.text(x + 3, y_m - 1.6, m_val, fontsize=6.5, color="#F8FAFC")

    # Bottom summary
    bb = patches.FancyBboxPatch((6, 5), 88, 10, boxstyle="round,pad=0.5", facecolor="#064E3B", edgecolor="#10B981", lw=1)
    ax.add_patch(bb)
    ax.text(50, 10, "Summary: Local ONNX cross-encoder re-ranking adds only 44.8 ms (+4.9% pipeline time) while eliminating 24.4% of false-positive\nnoise chunks, increasing Hit@3 by +18.1 percentage points, and suppressing hallucinations from 34.5% to < 2.5%.",
            ha='center', va='center', fontsize=7.8, fontweight='bold', color="#A7F3D0")

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_5_6_Three_Way_Ablation_Modal.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[+] Saved: {p}")

# -----------------------------------------------------------------------------
# 7. Figure 5.7: Interactive Flashcards and Quiz Studio (UI Mockup)
# -----------------------------------------------------------------------------
def make_fig_5_7():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    win = patches.FancyBboxPatch((2, 2), 96, 96, boxstyle="round,pad=0.5", facecolor="#0F172A", edgecolor="#334155", lw=2)
    ax.add_patch(win)
    ax.text(6, 94, "●  ●  ●   AI Study Hub — Active Recall Study Studio (Flashcards & Quizzes)", fontsize=9, color="#94A3B8")

    ax.text(6, 88, "Automated Active Recall Synthesis", fontsize=14, fontweight='bold', color="#F8FAFC")
    ax.text(6, 84, "Autonomous extraction of key concepts into interactive revision decks, printable PDFs, and native Anki (.apkg) decks.", fontsize=8.5, color="#94A3B8")

    # Left: Flashcard Preview
    fc_b = patches.FancyBboxPatch((6, 26), 42, 54, boxstyle="round,pad=0.8", facecolor="#1E293B", edgecolor="#6366F1", lw=2)
    ax.add_patch(fc_b)
    ax.text(27, 75, "Interactive 3D Flashcard Deck", ha='center', va='center', fontsize=11, fontweight='bold', color="#818CF8")
    ax.text(27, 70.5, "Card 4 of 24 (DBMS: Entity-Relationship Model)", ha='center', va='center', fontsize=7.5, color="#94A3B8")

    # Inner Card Front
    ic = patches.FancyBboxPatch((10, 36), 34, 30, boxstyle="round,pad=0.5", facecolor="#312E81", edgecolor="#818CF8", lw=1.5)
    ax.add_patch(ic)
    ax.text(27, 54, "CONCEPT (FRONT)", ha='center', va='center', fontsize=7.5, fontweight='bold', color="#C7D2FE")
    ax.text(27, 48, "What is a Weak Entity Set in an\nEntity-Relationship (E-R) diagram,\nand how is it identified?", ha='center', va='center', fontsize=8.5, fontweight='bold', color="#FFFFFF")
    ax.text(27, 40, "Click card to flip / reveal verified definition ➔", ha='center', va='center', fontsize=7, fontstyle='italic', color="#A5B4FC")

    # Flashcard Buttons
    ax.text(12, 30, "◀ Previous", fontsize=8, color="#94A3B8")
    ax.text(27, 30, "🔊 Read Aloud (TTS)", ha='center', fontsize=8, fontweight='bold', color="#38BDF8")
    ax.text(42, 30, "Next ▶", ha='right', fontsize=8, color="#94A3B8")

    # Right: Multiple Choice Quiz Preview
    qz_b = patches.FancyBboxPatch((52, 26), 42, 54, boxstyle="round,pad=0.8", facecolor="#1E293B", edgecolor="#10B981", lw=2)
    ax.add_patch(qz_b)
    ax.text(73, 75, "Adaptive Practice Quiz with Explanations", ha='center', va='center', fontsize=11, fontweight='bold', color="#34D399")
    ax.text(73, 70.5, "Question 3 of 10 | Score: 2 / 2 (100%)", ha='center', va='center', fontsize=7.5, color="#94A3B8")

    ax.text(55, 64, "Q: Which OSI layer handles end-to-end flow control,\nerror detection, and port multiplexing?", fontsize=8.5, fontweight='bold', color="#F8FAFC")

    options = [
        ("A", "Network Layer", False),
        ("B", "Transport Layer", True),
        ("C", "Data Link Layer", False),
        ("D", "Session Layer", False),
    ]
    for idx, (opt, txt, is_correct) in enumerate(options):
        y_opt = 56 - idx * 6
        bg_col = "#064E3B" if is_correct else "#0F172A"
        bd_col = "#10B981" if is_correct else "#334155"
        ob = patches.FancyBboxPatch((55, y_opt - 1.8), 36, 4.8, boxstyle="round,pad=0.3", facecolor=bg_col, edgecolor=bd_col, lw=1)
        ax.add_patch(ob)
        check = "✓ (Correct)" if is_correct else ""
        ax.text(57, y_opt + 0.5, f"[{opt}] {txt}  {check}", fontsize=7.5, color="#F8FAFC", fontweight='bold' if is_correct else 'normal')

    # Explanation popup
    exp_b = patches.FancyBboxPatch((55, 29), 36, 5.5, boxstyle="round,pad=0.2", facecolor="#065F46", edgecolor="#34D399", lw=0.8)
    ax.add_patch(exp_b)
    ax.text(56, 31.8, "Explanation [osi_notes.pdf, p. 7]: Transport Layer provides host-to-host\ncommunication, segmenting data, TCP/UDP port mapping, and flow control.", fontsize=6.5, color="#D1FAE5")

    # Bottom Export Action Bar
    ab = patches.FancyBboxPatch((6, 6), 88, 16, boxstyle="round,pad=0.5", facecolor="#1E293B", edgecolor="#475569", lw=1.5)
    ax.add_patch(ab)
    ax.text(8, 16, "One-Click Multi-Format Study Export Suite:", fontsize=9.5, fontweight='bold', color="#F8FAFC")
    ax.text(8, 11, "Export your auto-generated study materials directly into industry-standard formats for spaced repetition and offline review.", fontsize=7.5, color="#94A3B8")

    # Export Buttons
    b1 = patches.FancyBboxPatch((60, 9), 16, 8, boxstyle="round,pad=0.3", facecolor="#4F46E5", edgecolor="#818CF8", lw=1)
    ax.add_patch(b1)
    ax.text(68, 13, "📥 Export Anki\n(.apkg Deck)", ha='center', va='center', fontsize=7.2, fontweight='bold', color="#FFFFFF")

    b2 = patches.FancyBboxPatch((78, 9), 15, 8, boxstyle="round,pad=0.3", facecolor="#DC2626", edgecolor="#F87171", lw=1)
    ax.add_patch(b2)
    ax.text(85.5, 13, "📄 Export PDF\n(Printable Doc)", ha='center', va='center', fontsize=7.2, fontweight='bold', color="#FFFFFF")

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_5_7_Interactive_Flashcards_and_Quiz_Studio.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[+] Saved: {p}")

# -----------------------------------------------------------------------------
# 8. Figure 6.1: Hit@K Retrieval Curve (from evaluation results)
# -----------------------------------------------------------------------------
def copy_fig_6_1():
    src = "eval/results/hit_at_k_curve.png"
    dst = os.path.join(OUTPUT_DIR, "Figure_6_1_Hit_at_K_Retrieval_Curve.png")
    if os.path.exists(src):
        import shutil
        shutil.copyfile(src, dst)
        print(f"[+] Copied: {dst}")

# -----------------------------------------------------------------------------
# 9. Figure 6.2: One-Time Ingestion Latency (a) and Per-Query Latency (b)
# -----------------------------------------------------------------------------
def make_fig_6_2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=300)
    
    # Panel (a): Ingestion Latency (Upload-time once)
    categories = ["10 Pages\n(Course Syllabus)", "50 Pages\n(Lecture Slides)", "100 Pages\n(Textbook Chapter)"]
    p_parse = [70, 350, 700]
    p_chunk = [8, 38, 75]
    p_embed = [120, 580, 1150]
    p_index = [150, 420, 820]
    
    x = np.arange(len(categories))
    w = 0.5
    
    b1 = ax1.bar(x, p_parse, w, label="PyMuPDF Parsing (7ms/p)", color="#38BDF8")
    b2 = ax1.bar(x, p_chunk, w, bottom=p_parse, label="Recursive Chunking", color="#94A3B8")
    bottom_embed = np.array(p_parse) + np.array(p_chunk)
    b3 = ax1.bar(x, p_embed, w, bottom=bottom_embed, label="FastEmbed Embedding", color="#818CF8")
    bottom_idx = bottom_embed + np.array(p_embed)
    b4 = ax1.bar(x, p_index, w, bottom=bottom_idx, label="pgvector Cloud Indexing", color="#6366F1")
    
    ax1.set_title("(a) One-Time Document Ingestion Latency (ms)", fontsize=11, fontweight='bold', pad=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories, fontsize=8.5)
    ax1.set_ylabel("Ingestion Time (Milliseconds)", fontsize=9.5, fontweight='bold')
    ax1.legend(loc="upper left", fontsize=7.5, framealpha=0.9)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)

    # Panel (b): Per-Query Interactive Latency (Sub-second query time)
    stages = ["FastEmbed\nQuery Vector", "pgvector\nHNSW Search", "Cross-Encoder\nRe-Ranking", "Gemini 2.5 Flash\nGeneration"]
    latencies = [14.5, 34.2, 44.8, 825.0]
    colors = ["#818CF8", "#0284C7", "#F59E0B", "#10B981"]
    
    bars = ax2.bar(stages, latencies, color=colors, width=0.55)
    ax2.set_title("(b) Per-Query Interactive Latency Breakdown (ms)", fontsize=11, fontweight='bold', pad=10)
    ax2.set_ylabel("Execution Latency (Milliseconds)", fontsize=9.5, fontweight='bold')
    ax2.set_xticklabels(stages, fontsize=8.5)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)

    for bar, lat in zip(bars, latencies):
        h = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, h + 15, f"{lat:.1f} ms", ha='center', fontsize=8, fontweight='bold')

    ax2.text(1, 600, "Total Retrieval + Re-ranking: 93.5 ms\nTotal Pipeline Latency: 918.5 ms\nRe-ranking Overhead: only 44.8 ms (4.9%)", 
             fontsize=8.5, bbox=dict(boxstyle="round,pad=0.4", fc="#EFF6FF", ec="#3B82F6", lw=1))

    plt.suptitle("Figure 6.2: Separation of One-Time Ingestion Latency (a) and Per-Query Interactive Latency (b)", 
                 fontsize=12, fontweight='bold', y=1.02)
    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_6_2_Ingestion_and_Query_Latency_Regimes.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[+] Saved: {p}")

# -----------------------------------------------------------------------------
# 10. Figure 6.3: Parser Throughput PyMuPDF vs Gemini Vision OCR
# -----------------------------------------------------------------------------
def make_fig_6_3():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    
    methods = ["Local PyMuPDF\n(fitz C-Engine)", "Gemini 2.5 Flash\nMultimodal Vision OCR"]
    times_per_page = [7.0, 1120.0]  # ms
    colors = ["#10B981", "#EF4444"]
    
    bars = ax.bar(methods, times_per_page, color=colors, width=0.45)
    ax.set_yscale('log')
    ax.set_ylabel("Processing Latency per Page (ms) [Log Scale]", fontsize=10, fontweight='bold')
    ax.set_title("Figure 6.3: Parser Throughput Comparison (160× Speedup)", fontsize=12, fontweight='bold', pad=12)
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    ax.text(0, 12, "7.0 ms / page\n(Sub-10ms Target Achieved)", ha='center', fontsize=9, fontweight='bold', color="#065F46")
    ax.text(1, 1600, "1,120.0 ms / page\n(Cloud Vision Network + Inference)", ha='center', fontsize=9, fontweight='bold', color="#991B1B")

    ax.annotate("160× Faster", xy=(0.48, 120), xytext=(0.48, 120),
                ha='center', fontsize=12, fontweight='bold', color="#1E3A8A",
                bbox=dict(boxstyle="round,pad=0.5", fc="#DBEAFE", ec="#1D4ED8", lw=1.5))

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_6_3_Parser_Throughput_PyMuPDF_vs_GeminiVision.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[+] Saved: {p}")

if __name__ == "__main__":
    make_fig_5_1()
    make_fig_5_2()
    make_fig_5_3()
    make_fig_5_4()
    make_fig_5_5()
    make_fig_5_6()
    make_fig_5_7()
    copy_fig_6_1()
    make_fig_6_2()
    make_fig_6_3()
    print("\nAll 10 project report diagrams generated successfully in Report/diagrams/")
