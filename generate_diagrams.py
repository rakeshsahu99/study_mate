import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def create_system_architecture_diagram():
    fig, ax = plt.subplots(figsize=(12, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Color palette (Academic & Modern)
    c_client = "#E8F0FE"
    c_client_border = "#1A73E8"
    c_gateway = "#FEF7E0"
    c_gateway_border = "#F9AB00"
    c_ai = "#E6F4EA"
    c_ai_border = "#137333"
    c_db = "#FCE8E6"
    c_db_border = "#C5221F"
    c_arrow = "#3C4043"

    # Title Banner
    ax.text(50, 96, "AI Study Hub (StudyMate) - Layered System Architecture", 
            ha='center', va='center', fontsize=16, fontweight='bold', color="#202124")
    ax.text(50, 93, "High-Throughput Ingestion, Two-Stage Neural Re-Ranking & Grounded Study Synthesis", 
            ha='center', va='center', fontsize=11, fontstyle='italic', color="#5F6368")

    # 1. Presentation Layer (Top)
    r1 = patches.FancyBboxPatch((5, 75), 90, 15, boxstyle="round,pad=1,rounding_size=2", 
                                facecolor=c_client, edgecolor=c_client_border, linewidth=2)
    ax.add_patch(r1)
    ax.text(8, 87, "1. Presentation Layer (Client / User Interface)", fontsize=12, fontweight='bold', color=c_client_border)
    ax.text(8, 83, "Next.js 16 (App Router)  |  React 19  |  TypeScript  |  Tailwind CSS Dark Theme  |  Web Speech API (TTS)", fontsize=9.5, fontweight='bold', color="#202124")
    
    # Submodules inside Presentation Layer
    submodules_1 = [
        (8, 77, 24, 4.5, "Document Upload Hub\n(Drag & Drop / Telemetry)"),
        (35, 77, 28, 4.5, "Conversational RAG Chat\n(Strict [Page X] Citations)"),
        (66, 77, 26, 4.5, "3-Way Ablation Modal\n(Config A vs B vs C)"),
    ]
    for x, y, w, h, txt in submodules_1:
        box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#FFFFFF", edgecolor=c_client_border, linewidth=1)
        ax.add_patch(box)
        ax.text(x + w/2, y + h/2, txt, ha='center', va='center', fontsize=8, color="#202124")

    # Arrow 1 -> 2
    ax.annotate('', xy=(50, 68), xytext=(50, 75),
                arrowprops=dict(arrowstyle="<->", color=c_arrow, lw=2, mutation_scale=15))
    ax.text(52, 71.5, "HTTP REST API / JSON / Telemetry Headers", fontsize=8.5, color="#5F6368", fontweight='bold')

    # 2. Application & Gateway Layer
    r2 = patches.FancyBboxPatch((5, 59), 90, 9, boxstyle="round,pad=1,rounding_size=2", 
                                facecolor=c_gateway, edgecolor=c_gateway_border, linewidth=2)
    ax.add_patch(r2)
    ax.text(8, 65, "2. Application Controller & Gateway Layer", fontsize=12, fontweight='bold', color="#B06000")
    ax.text(8, 61, "Next.js Route Handlers  |  User Authentication & Session Isolation (X-User-Id)  |  CORS Middleware", fontsize=9.5, color="#202124")

    # Arrow 2 -> 3
    ax.annotate('', xy=(50, 52), xytext=(50, 59),
                arrowprops=dict(arrowstyle="<->", color=c_arrow, lw=2, mutation_scale=15))
    ax.text(52, 55.5, "Asynchronous API Proxy (FastAPI :8000)", fontsize=8.5, color="#5F6368", fontweight='bold')

    # 3. AI Microservice & Intelligence Layer
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

    # 4. Data & Vector Storage Layer
    r4 = patches.FancyBboxPatch((5, 3), 90, 13, boxstyle="round,pad=1,rounding_size=2", 
                                facecolor=c_db, edgecolor=c_db_border, linewidth=2)
    ax.add_patch(r4)
    ax.text(8, 13, "4. Data & Vector Storage Layer (Supabase PostgreSQL)", fontsize=12, fontweight='bold', color=c_db_border)
    ax.text(8, 9, "PostgreSQL 15+  |  pgvector Extension  |  HNSW Approximate Nearest Neighbor Index", fontsize=9.5, fontweight='bold', color="#202124")

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
    os.makedirs("eval/results", exist_ok=True)
    os.makedirs("public", exist_ok=True)
    
    out_paths = ["eval/results/system_architecture.png", "public/system_architecture.png", "system_architecture.png"]
    for p in out_paths:
        plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print("Generated system_architecture.png successfully")

def create_system_pipeline_diagram():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Colors
    c_bg_ingest = "#EBF5FB"
    c_bd_ingest = "#2980B9"
    c_bg_retrieval = "#EAFAF1"
    c_bd_retrieval = "#27AE60"
    c_bg_gen = "#FEF9E7"
    c_bd_gen = "#F39C12"
    c_bg_study = "#F4ECF7"
    c_bd_study = "#8E44AD"

    ax.text(50, 96, "AI Study Hub (StudyMate) - End-to-End System Execution Pipeline", 
            ha='center', va='center', fontsize=15, fontweight='bold', color="#2C3E50")
    ax.text(50, 92, "Document Ingestion, Two-Stage Neural Re-Ranking, Grounded Generation & Study Synthesis", 
            ha='center', va='center', fontsize=10.5, fontstyle='italic', color="#7F8C8D")

    # Stage 1: Ingestion Pipeline
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

    # Stage 2: Dense Indexing
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

    # Stage 3: Two-Stage Retrieval & Re-ranking
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

    # Stage 4: Grounded Generation & Study Suite
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

    # Bottom Telemetry & Ablation Bar
    box_tel = patches.FancyBboxPatch((3, 6), 94, 36, boxstyle="round,pad=1,rounding_size=2", 
                                    facecolor="#F8F9FA", edgecolor="#4A5568", linewidth=1.5, linestyle="--")
    ax.add_patch(box_tel)
    ax.text(50, 38, "STAGE 5: REAL-TIME TELEMETRY INSTRUMENTATION & 3-WAY ABLATION SUITE", 
            ha='center', va='center', fontsize=11, fontweight='bold', color="#2D3748")

    tel_cards = [
        (5, 10, 27, 24, "Micro-Latency Instrumentation\n\n• parsing_ms: ~7.0 ms/page\n• embedding_ms: 14.5 ms\n• retrieval_ms: 34.2 ms\n• reranking_ms: 44.8 ms\n• generation_ms: 825.0 ms\n• Total End-to-End: ~918 ms"),
        (36, 10, 28, 24, "3-Way Architectural Ablation\n\n• Config A: Standalone LLM (0-shot)\n  (34.5% Hallucination, 0 Citations)\n• Config B: Vanilla Vector RAG\n  (71.4% Hit@3, 0.68 MRR)\n• Config C: Proposed Re-Ranked RAG\n  (89.5% Hit@3, 0.86 MRR, <2.5% Halluc.)"),
        (68, 10, 27, 24, "Multi-Format Export & Audio\n\n• Printable PDF Flashcards & Quiz\n• Native Anki (.apkg) Decks\n  (Spaced Repetition Algorithm)\n• Browser Web Speech TTS Audio\n• False-Positive Reduction: 24.4%"),
    ]
    for x, y, w, h, t in tel_cards:
        b = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5,rounding_size=1", facecolor="#FFFFFF", edgecolor="#CBD5E0", linewidth=1)
        ax.add_patch(b)
        ax.text(x + w/2, y + h/2, t, ha='center', va='center', fontsize=7.8, color="#2D3748")

    plt.tight_layout()
    out_paths = ["eval/results/system_pipeline.png", "public/system_pipeline.png", "system_pipeline.png"]
    for p in out_paths:
        plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print("Generated system_pipeline.png successfully")

if __name__ == "__main__":
    create_system_architecture_diagram()
    create_system_pipeline_diagram()
