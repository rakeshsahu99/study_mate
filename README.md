<div align="center">

# 🎓 StudyMate (AI Study Hub)
### *Context-Aware Retrieval-Augmented Generation (RAG) Platform with Neural Re-Ranking, Sub-10ms Ingestion & Telemetry-Driven Academic Evaluation*

[![Next.js 16](https://img.shields.io/badge/Frontend-Next.js%2016%20App%20Router-black?logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%20Python%203.11+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Supabase pgvector](https://img.shields.io/badge/Vector%20Store-Supabase%20pgvector-3ECF8E?logo=supabase)](https://supabase.com/)
[![Gemini 2.5 Flash](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-4285F4?logo=google)](https://aistudio.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

*An end-to-end intelligent academic study companion and major project dissertation platform engineered to eliminate LLM hallucinations, guarantee strict source provenance citations, and deliver real-time performance on complex university course materials.*

---

</div>

## 📌 Executive Summary & Key Highlights

Standard Large Language Models (LLMs) and vanilla single-vector RAG pipelines frequently suffer from factual hallucinations (12–35%) and context dilution when queried on dense university notes. **StudyMate** solves this via a modern three-stage hybrid retrieval architecture combined with local hardware acceleration and granular telemetry:

1. **⚡ Ultra-Fast Local Document Ingestion (PyMuPDF):**  
   Local parsing achieves **~7 ms per page** (160× faster than cloud vision OCR) with automatic fallback to **Gemini 2.5 Flash Multimodal Vision** for image-heavy slides and handwritten equations.
2. **🧠 Two-Stage Neural Re-Ranking Pipeline:**  
   First-stage dense bi-encoder candidate retrieval via FastEmbed (`BAAI/bge-small-en-v1.5` or `all-MiniLM-L6-v2`) followed by high-precision cross-attention neural re-ranking (`cross-encoder/ms-marco-MiniLM-L-6-v2` via ONNX Runtime). Increases Hit@3 recall by **+18.1%** and Mean Reciprocal Rank (MRR) by **+26.5%**.
3. **🛡️ Hallucination Suppression (< 2.5% Hallucination Rate):**  
   Strict temperature confinement ($T=0.2$) and strict system boundary prompts guarantee that answers are strictly grounded in retrieved passages with verified page-level citations (`[Page X]`).
4. **⏱️ End-to-End Telemetry Instrumentation:**  
   Every API endpoint measures and returns micro-stage latencies (`parsing_ms`, `embedding_ms`, `retrieval_ms`, `reranking_ms`, `generation_ms`), surfaced directly in the UI as real-time performance pills.
5. **🔬 Interactive 3-Way Architectural Ablation:**  
   A dedicated side-by-side comparison modal directly demonstrates the difference between:
   * **Configuration A:** Standalone LLM (Zero-shot / Pure parametric memory)
   * **Configuration B:** Vanilla Single-Vector RAG (FastEmbed + Cosine Similarity only)
   * **Configuration C:** Proposed System (Vector Retrieval + Neural Cross-Encoder Re-Ranking)
6. **🎙️ Study Synthesis & Audio Suite:**  
   Instant generation of flashcards, interactive quizzes with score tracking, one-click export to **PDF** and **Anki (.apkg)** decks, and Web Speech API **Text-to-Speech (TTS)** voice read-aloud.

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph INGESTION["1. Document Ingestion Pipeline"]
        A["Course PDF / Slide Deck"] --> B{"Parser Strategy"}
        B -->|"Digital Text (< 10ms/page)"| C["PyMuPDF C-Engine"]
        B -->|"Handwritten / Complex Visuals"| D["Gemini 2.5 Flash Multimodal Vision"]
        C --> E["Recursive Character Chunker (400-500 chars)"]
        D --> E
        E --> F["FastEmbed Bi-Encoder (all-MiniLM-L6-v2)"]
        F --> G["Supabase PostgreSQL (pgvector HNSW)"]
    end

    subgraph QUERY["2. Two-Stage Retrieval & Generation Pipeline"]
        H["Student Natural Language Query"] --> I["Query Contextualizer / History"]
        I --> J["Stage 1: Dense Vector Search (Top-15 Candidates)"]
        G -.-> J
        J --> K["Stage 2: Cross-Encoder Neural Re-Ranker (ms-marco-MiniLM-L-6-v2)"]
        K --> L["Top-5 Re-Ranked Grounded Chunks"]
        L --> M["Gemini 2.5 Flash (T=0.2 + Citation Constraints)"]
        M --> N["Grounded Response with Verified [Page X] Citations"]
    end

    subgraph TELEMETRY["3. Telemetry & User Interface"]
        N --> O["Next.js 16 UI: Chat Assistant, Flashcards, Quiz, Audio TTS"]
        K -.-> P["Stage Latency Pill: parsing, retrieval, reranking, generation"]
        P --> O
    end
```

---

## 📊 Empirical Thesis Benchmark Results

The system was evaluated using an automated evaluation harness on **43 pages of university course materials** across 3 core computer science subjects ([project_pdfs/](project_pdfs/)):
* `24042020_E-R Model.pdf` (DBMS - Entity Relationship Modeling)
* `CPU-Scheduling-and-Algorithm-.pdf` (Operating Systems - CPU Scheduling & Deadlocks)
* `osi_notes.pdf` (Computer Networks - OSI 7-Layer Reference Model)

### Table 1: Retrieval Performance (Your Approach vs. Baselines)
| Model / Pipeline | Hit@3 | Hit@5 | MRR (Mean Reciprocal Rank) | Latency (ms) | Key Architectural Mechanism |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Baseline 1: Pure Keyword / BM25** | 48.2% | 58.1% | 0.44 | 12 ms | Sparse exact lexical token frequency matching |
| **Baseline 2: Standard Vector Search (`all-MiniLM-L6-v2`)** | 71.4% | 82.0% | 0.68 | 45 ms | Dense bi-encoder cosine similarity (pgvector HNSW) |
| **Proposed: Hybrid Vector + Cross-Encoder Re-Ranking** | **89.5%** | **94.2%** | **0.86** | **92 ms** | **All-to-all query-document cross-attention (`ms-marco-MiniLM-L-6-v2`)** |

### Table 2: Generation Faithfulness & Hallucination Rate
| Pipeline Configuration | Faithfulness (RAGAS) | Answer Relevance | Hallucination Rate | Source Provenance Citations |
| :--- | :---: | :---: | :---: | :--- |
| **LLM Only (Zero-shot Gemini)** | 42.1% | 68.0% | 34.5% | None (0 citations, pure parametric memory) |
| **Standard Vector RAG** | 78.4% | 84.2% | 12.1% | Partial (unverified chunk boundaries) |
| **Proposed RAG with Citation Bounds** | **95.2%** | **93.8%** | **< 2.5%** | **Strict page-level citations (`[Page X]`) + provenance bounds** |

### Table 3: Ingestion Throughput by Document Scale
| Document Scale | PyMuPDF Ingestion (7.0 ms/page) | Gemini 2.5 Flash Vision (1120 ms/page) | Speedup Factor | Primary Recommendation |
| :--- | :---: | :---: | :---: | :--- |
| **10 Pages (Course Syllabus)** | **70 ms** | 11,200 ms (11.2 s) | **160×** | Local PyMuPDF (Instant) |
| **50 Pages (Lecture Slides)** | **350 ms** | 56,000 ms (56.0 s) | **160×** | Local PyMuPDF default / Gemini for charts |
| **100 Pages (Textbook Chapter)** | **700 ms (< 1s)** | 112,000 ms (1.87 min) | **160×** | Local PyMuPDF for batch scale |

---

## 🛠️ Tech Stack & Prerequisites

* **Node.js**: v18.17+ or v20+ (`npm` or `pnpm`)
* **Python**: v3.10+ (v3.11 or v3.12 recommended)
* **Vector Database**: [Supabase](https://supabase.com) (Free tier PostgreSQL with `pgvector`)
* **LLM API Key**: [Google Gemini API Key](https://aistudio.google.com) (Free tier available)

---

## 🚀 Step-by-Step Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/rakeshsahu99/study_mate.git
cd study_mate
```

---

### Step 2: Configure Supabase Database (Vector Store)

1. Create a free account at [Supabase](https://supabase.com) and create a new project.
2. Open the **SQL Editor** in your Supabase dashboard and run the following script:

```sql
-- 1. Enable pgvector extension
create extension if not exists vector;

-- 2. Create document_chunks table
create table if not exists document_chunks (
    id bigserial primary key,
    user_id uuid not null,
    filename text not null,
    page_number int not null,
    text_content text not null,
    embedding vector(384),
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 3. Create HNSW index for high-speed approximate nearest neighbor cosine search
create index if not exists document_chunks_embedding_idx 
on document_chunks 
using hnsw (embedding vector_cosine_ops);

-- 4. Create vector matching stored procedure (RPC)
create or replace function match_document_chunks (
    query_embedding vector(384),
    match_threshold float,
    match_count int,
    filter_user_id uuid,
    filter_filename text default 'all'
)
returns table (
    id bigint,
    filename text,
    page_number int,
    text_content text,
    similarity float
)
language plpgsql
as $$
begin
    return query
    select
        dc.id,
        dc.filename,
        dc.page_number,
        dc.text_content,
        1 - (dc.embedding <=> query_embedding) as similarity
    from document_chunks dc
    where dc.user_id = filter_user_id
      and (filter_filename = 'all' or dc.filename = filter_filename)
      and 1 - (dc.embedding <=> query_embedding) > match_threshold
    order by dc.embedding <=> query_embedding
    limit match_count;
end;
$$;
```

---

### Step 3: Setup Environment Variables

#### 1. Frontend Environment (`.env.local` in project root)
Copy `.env.example` to `.env.local`:
```bash
cp .env.example .env.local
```
Fill in your Supabase credentials:
```env
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-anon-key
NEXT_PUBLIC_AI_SERVICE_URL=http://localhost:8000
```

#### 2. Backend Environment (`ai-service/.env`)
Copy `ai-service/.env.example` to `ai-service/.env`:
```bash
cp ai-service/.env.example ai-service/.env
```
Fill in your Gemini and Supabase service keys:
```env
GEMINI_API_KEY=your_gemini_api_key_from_aistudio
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
```

---

### Step 4: Run the Backend Microservice (FastAPI)

In your first terminal:
```bash
cd ai-service

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Backend API docs will be live at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Step 5: Run the Frontend (Next.js)

In a second terminal (from project root):
```bash
# Install frontend dependencies
npm install

# Start development server
npm run dev
```
Open your browser at: **[http://localhost:3000](http://localhost:3000)**

---

### Alternative: Run with Docker Compose
If you have Docker installed, you can spin up both frontend and backend in one command:
```bash
docker compose up --build
```

---

## 🧪 Running Automated Evaluation & Generating Thesis Charts

To independently verify all retrieval metrics and recreate the 300 DPI publication charts:

### 1. Run the Evaluation Benchmark (Offline or Live)
```bash
# Set Python path to include ai-service and eval
# Windows PowerShell:
$env:PYTHONPATH="ai-service;eval;."
& "ai-service/venv/Scripts/python.exe" "eval/benchmark.py" --dataset eval/golden_dataset.json --corpus eval/sample_academic_corpus.json --mode offline --no-llm

# Linux/macOS:
PYTHONPATH="ai-service:eval:." python eval/benchmark.py --dataset eval/golden_dataset.json --corpus eval/sample_academic_corpus.json --mode offline --no-llm
```

### 2. Regenerate High-Resolution Matplotlib/Seaborn Charts
```bash
# Windows PowerShell:
$env:PYTHONPATH="ai-service;eval;."
& "ai-service/venv/Scripts/python.exe" "eval/generate_publication_charts.py"

# Linux/macOS:
PYTHONPATH="ai-service:eval:." python eval/generate_publication_charts.py
```

Generated publication artifacts are stored in `eval/results/`:
* `hit_at_k_curve.png` (300 DPI Line Chart: Hit@K vs K from 1 to 10)
* `latency_by_doc_size.png` (300 DPI Stacked Bar Chart: Stage latencies across document sizes)
* `evaluation_table.md` (Markdown tables for Chapter 5 of project report)
* `retrieval_comparison.svg`, `three_config_ablation.svg`, `generation_metrics.svg`

---

## 📁 Repository Directory Structure

```
study_mate/
├── app/                          # Next.js 16 App Router Frontend
│   ├── page.tsx                  # Main single-page interactive UI (Chat, Hub, Flashcards, Quiz)
│   ├── layout.tsx                # Root layout & font injection
│   └── globals.css               # Tailored dark-mode academic theme
├── ai-service/                   # FastAPI Python Microservice
│   ├── main.py                   # FastAPI application & telemetry endpoints
│   ├── requirements.txt          # Python dependencies (PyMuPDF, FastEmbed, ONNX, etc.)
│   ├── core/
│   │   ├── parser.py             # PyMuPDF fast local extractor + Gemini Vision OCR
│   │   ├── chunker.py            # Natural paragraph recursive text chunker
│   │   ├── embedder.py           # FastEmbed dense bi-encoder embeddings
│   │   ├── search.py             # Cross-Encoder neural re-ranking (ms-marco-MiniLM)
│   │   ├── generator.py          # Gemini 2.5 Flash grounded prompt & study synthesis
│   │   ├── supabase_db.py        # pgvector HNSW client & RPC executor
│   │   └── exporter.py           # Anki (.apkg) & PDF study material exporters
│   ├── test_telemetry.py         # Unit tests for latency instrumentation
│   └── test_ablation.py          # Unit tests for 3-way ablation comparison
├── eval/                         # Comprehensive Academic Benchmark Suite
│   ├── benchmark.py              # Automated evaluation harness (Hit@K, MRR, Context Precision)
│   ├── golden_dataset.json       # 36 human-annotated ground-truth test cases
│   ├── sample_academic_corpus.json # 158 indexed chunks from course notes
│   ├── build_user_notes_benchmark.py # Ingestion utility for course notes
│   ├── generate_publication_charts.py # Matplotlib/Seaborn 300 DPI chart generator
│   ├── generate_telemetry_charts.py   # Pure SVG telemetry visualizer
│   └── results/                  # Publication figures (PNG, SVG) & Markdown tables
├── project_pdfs/                 # Reference student course notes (DBMS, OS, CN)
├── .github/workflows/ci.yml      # GitHub Actions CI build & test pipeline
├── docker-compose.yml            # Multi-container local orchestration
├── Dockerfile.frontend           # Production Next.js Dockerfile
├── .env.example                  # Frontend environment template
└── README.md                     # Project documentation
```

---

## 📡 REST API Reference

| Endpoint | Method | Description | Key Latency Metrics Returned |
| :--- | :---: | :--- | :--- |
| `/upload` | `POST` | Upload and chunk PDF/DOCX into vector store | `parsing_ms`, `embedding_ms`, `total_ms` |
| `/search` | `POST` | Dense vector retrieval + Cross-Encoder re-rank | `retrieval_ms`, `reranking_ms`, `total_ms` |
| `/chat` | `POST` | Multi-turn contextual chat with grounded citations | `parsing_ms`, `retrieval_ms`, `reranking_ms`, `generation_ms` |
| `/study-materials` | `POST` | Generate flashcards and multiple-choice quizzes | `generation_ms`, `total_ms` |
| `/ablation/compare` | `POST` | 3-way comparative evaluation (Config A vs B vs C) | Comparative MRR, Context Precision, Latency |
| `/telemetry/breakdown` | `GET` | Micro-breakdown of average stage latency | Stage percentages across requests |
| `/telemetry/parsers/compare` | `POST` | Direct benchmark: PyMuPDF vs Gemini Vision | Parsing speedup factor (e.g. ~160×) |

---

## 📜 Academic Attribution & License

This project was built and submitted as a **Major Project Dissertation Deliverable** for the Bachelor of Technology (B.Tech) degree in Computer Science & Engineering.

Released under the [MIT License](LICENSE). Contributions, issues, and forks are welcome!
