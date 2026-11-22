# Benchmark Dataset & Experimental Setup (`eval/dataset/`)

> **Academic Relevance:** Solves the **"Experimental Setup"** requirement for **Chapter 3 (System Methodology)** and **Chapter 4 (Experimental Evaluation)** of your Bachelor/Master thesis or project report.

Examiners will penalize vague statements such as *"we evaluated the RAG system on random PDFs downloaded from the web"*. In academic computer science evaluations, systems must be benchmarked against **curated, reproducible test corpora** with documented ground-truth answers, known page-level citations, and deterministic chunk IDs.

This directory houses the standard benchmark dataset designed specifically for the **AI Study Hub** multi-document retrieval-augmented generation (RAG) architecture.

---

## 1. Directory Structure

```text
eval/dataset/
├── documents/                                    # Standard Academic Test Documents (PDF)
│   ├── cs601_advanced_algorithms_syllabus.pdf    # Doc 1: Text-heavy syllabus & institutional policies
│   ├── multimodal_deep_learning_theory.pdf      # Doc 2: Multimodal paper with equations & structured tables
│   ├── lecture_slides_vector_search_rag.pdf     # Doc 3: Landscape slide deck (16:9 slides format)
│   └── distributed_systems_consensus_paper.pdf  # Doc 4: Dense systems paper (CAP, Paxos, Raft, Coffman)
├── ground_truth.json                            # 32 Curated Q&A pairs mapped to exact pages & chunk IDs
├── indexed_chunks.json                          # Complete pre-parsed & chunked reference corpus (46 chunks)
├── build_documents.py                           # Automated ReportLab PDF document compiler
├── generate_dataset.py                          # Automated corpus chunker & ground-truth integrity verifier
└── README.md                                    # This guide and thesis methodology documentation
```

---

## 2. Standard Academic Test Documents

The benchmark corpus consists of **4 standard academic documents** spanning different layout modalities, text densities, and visual structures:

| Document Filename | Modality & Document Type | Pages | Chunks | Key Modality & Structural Characteristics |
| :--- | :--- | :---: | :---: | :--- |
| `cs601_advanced_algorithms_syllabus.pdf` | **Text-Heavy Academic Syllabus** | 4 | 16 | Dense academic policy, prerequisites tree, multi-week algorithmic syllabus (Amortized Analysis, Network Flow, LP Duality, Randomized Algorithms, Streaming sketches, NP-reductions), grading rubrics, late submission penalties, office hours. |
| `multimodal_deep_learning_theory.pdf` | **Multimodal Equations & Tables** | 4 | 12 | Mathematical formulas (Scaled Dot-Product Attention, Multi-Head Attention, Label Smoothing loss, AdamW decoupled weight decay updates), plus two dense comparison tables: Table 1 (Architectural parameters) and Table 2 (Downstream GLUE/SQuAD v2 benchmark scores). |
| `lecture_slides_vector_search_rag.pdf` | **Slide Deck (Landscape Format)** | 6 | 9 | Landscape slides layout: Slide 1 (Title), Slide 2 (Lexical vs Dense search tradeoffs), Slide 3 (HNSW vs IVF-Flat), Slide 4 (Reciprocal Rank Fusion formula and $k=60$), Slide 5 (Cross-Encoder re-ranking), Slide 6 (RAG Triad evaluation metrics). |
| `distributed_systems_consensus_paper.pdf` | **Core Systems Research Paper** | 4 | 9 | Theoretical formulations of the FLP Impossibility Theorem, CAP Theorem, PACELC classification, Paxos vs. Raft consensus leader election timeouts (150ms–300ms), Coffman deadlock conditions, and Two-Phase Commit (2PC). |
| **Total Benchmark Corpus** | **Multi-Modal Academic Suite** | **18** | **46** | **Comprehensive coverage of text, mathematics, structured tabular data, and slide decks.** |

---

## 3. Ground Truth Specification (`ground_truth.json`)

The ground truth dataset contains **32 curated Question-Answer pairs** spanning factual recall, mathematical extraction, tabular cross-referencing, and algorithmic synthesis.

### Schema Definition
Each entry in `ground_truth.json` strictly adheres to the following JSON schema:

```json
{
  "id": "bench_01",
  "question": "What are the strict prerequisite courses required for enrolling in CS601 Advanced Algorithms?",
  "ground_truth_answer": "Enrolling in CS601 requires a grade of B or higher in CS301 (Data Structures) and CS305 (Discrete Mathematics)...",
  "expected_document": "cs601_advanced_algorithms_syllabus.pdf",
  "expected_pages": [1],
  "chunk_ids": [
    "cs601_advanced_algorithms_syllabus_chunk_001",
    "cs601_advanced_algorithms_syllabus_chunk_002"
  ],
  "key_facts": [
    "CS301",
    "Data Structures",
    "CS305",
    "Discrete Mathematics",
    "grade of B or higher"
  ],
  "query_type": "text_heavy_syllabus",
  "difficulty": "easy"
}
```

### Field Descriptions
- **`id`**: Unique benchmark query identifier (`bench_01` to `bench_32`).
- **`question`**: Realistic student/researcher query.
- **`ground_truth_answer`**: Authoritative, mathematically and factually complete reference answer.
- **`expected_document`**: Exact target document containing the ground-truth evidence.
- **`expected_pages`**: 1-indexed array of document page numbers where the answer is corroborated.
- **`chunk_ids`**: Exact deterministic chunk IDs produced by the system's text splitter (`chunk_size=800`, `chunk_overlap=150`).
- **`key_facts`**: Atomic factual phrases required in the retrieved context for complete factual recall.
- **`query_type`**: Query classification category (`text_heavy_syllabus`, `text_heavy_policy`, `text_heavy_algorithmic`, `multimodal_equation`, `multimodal_table`, `multimodal_reasoning`, `slide_deck_summary`, `slide_deck_technical`, `text_heavy_systems`).
- **`difficulty`**: Cognitive complexity level (`easy`, `medium`, `hard`).

---

## 4. Query Distribution by Modality & Task Type

To ensure unbiased evaluation, the 32 queries are partitioned across diverse task types:

| Query Type Category | Target Document | Question IDs | Count | Typical Evaluation Challenge |
| :--- | :--- | :---: | :---: | :--- |
| **Institutional Policy & Syllabus** | `cs601_advanced_algorithms_syllabus.pdf` | `bench_01, 02, 03, 10` | 4 | Exact entity matching, grade thresholds, late penalties, AI policy clauses. |
| **Algorithmic & Mathematical Proofs** | `cs601_advanced_algorithms_syllabus.pdf` | `bench_04, 05, 06, 07, 08, 09` | 6 | Duality theorems, asymptotic complexity $O(V E^2)$, approximation bounds. |
| **Mathematical Equations & Formulations** | `multimodal_deep_learning_theory.pdf` | `bench_11, 12, 13, 14, 15` | 5 | LaTeX equation grounding, variance scaling $\frac{1}{\sqrt{d_k}}$, AdamW decoupled updates. |
| **Structured Multi-Column Tables** | `multimodal_deep_learning_theory.pdf` | `bench_16, 17, 18, 19, 20` | 5 | Tabular row/column cell alignment, hyperparameter values, GLUE/SQuAD v2 percentages. |
| **Slide Deck Conceptual Summaries** | `lecture_slides_vector_search_rag.pdf` | `bench_21, 22, 27, 28` | 4 | Bullet-point summarization, vocabulary mismatch, RAG triad metrics. |
| **Slide Deck Technical Architecture** | `lecture_slides_vector_search_rag.pdf` | `bench_23, 24, 25, 26` | 4 | HNSW graph skip connections, IVF Voronoi cells, RRF formula with $k=60$. |
| **Distributed Systems Protocols** | `distributed_systems_consensus_paper.pdf` | `bench_29, 30, 31, 32` | 4 | CAP/PACELC trade-offs, Raft randomized timeouts (150ms-300ms), Coffman deadlock conditions. |
| **Total Query Distribution** | **All 4 Test Documents** | `bench_01` – `bench_32` | **32** | **Full spectrum of academic retrieval & reasoning scenarios.** |

---

## 5. How to Run the Benchmark

The dataset is integrated directly into the `eval/benchmark.py` automated evaluation harness:

```bash
# 1. Run offline benchmark against the benchmark dataset (evaluates in ~2 seconds)
python eval/benchmark.py --dataset dataset/ground_truth.json --no-llm

# 2. Run full evaluation including Gemini 2.5 Flash LLM-as-a-Judge generation metrics
python eval/benchmark.py --dataset dataset/ground_truth.json

# 3. Test vanilla single-vector baseline (Config B) without Cross-Encoder re-ranking
python eval/benchmark.py --dataset dataset/ground_truth.json --disable-reranking --no-llm
```

### Re-Compiling Documents or Verifying Ground Truth Integrity
If you modify the document texts or add new questions:
```bash
# Rebuild the 4 academic PDFs from scratch using ReportLab
python eval/dataset/build_documents.py

# Re-chunk and run automated 100% integrity verification
python eval/dataset/generate_dataset.py
```

---

## 6. How to Write This in Chapter 3 / 4 of Your Thesis

Below are copy-paste ready text and LaTeX templates for your project report or thesis:

### Markdown / Word Format for Project Report
> **Section 4.1: Experimental Setup and Benchmark Dataset**
> 
> To evaluate the retrieval and generative fidelity of the AI Study Hub architecture without bias, we constructed a dedicated academic benchmark suite comprising four standard academic documents ($18$ total pages) spanning diverse layout modalities:
> 1. **Text-Heavy Academic Specification:** A 4-page curriculum syllabus (`cs601_advanced_algorithms_syllabus.pdf`) containing dense institutional policies, prerequisite dependency graphs, weekly module outlines, and grading rubrics.
> 2. **Multimodal Scholarly Monograph:** A 4-page research document (`multimodal_deep_learning_theory.pdf`) containing mathematical formulations of scaled dot-product attention, multi-head projection tensors, and decoupled AdamW weight decay, alongside two dense comparative tables summarizing transformer model parameters and downstream reading comprehension scores.
> 3. **Slide Deck Presentation:** A 6-slide landscape document (`lecture_slides_vector_search_rag.pdf`) evaluating bullet-point parsing, vector indexing algorithms (HNSW vs. IVF-Flat), and Reciprocal Rank Fusion formulas.
> 4. **Theoretical Systems Paper:** A 4-page systems treatise (`distributed_systems_consensus_paper.pdf`) detailing consensus protocols (Paxos vs Raft), the CAP theorem, and deadlock conditions.
> 
> A ground truth dataset of $N = 32$ curated question-answer pairs was developed. Each query was mapped to its exact ground-truth source document, expected page numbers, key atomic factual statements, and deterministic chunk IDs produced by recursive character splitting ($800$-character window, $150$-character overlap).

### LaTeX Table for Chapter 4 (`thesis_dataset_table.tex`)

```latex
\begin{table}[htbp]
\centering
\caption{Characteristics of the Curated Academic Benchmark Dataset}
\label{tab:benchmark_dataset}
\begin{tabular}{llrrc}
\toprule
\textbf{Document} & \textbf{Modality / Format} & \textbf{Pages} & \textbf{Chunks} & \textbf{Ground Truth Queries} \\
\midrule
CS601 Syllabus & Text-Heavy Academic Policy & 4 & 16 & 10 (Syllabus, Policies, Complexity) \\
DL Theory Paper & Multimodal (Math \& Tables) & 4 & 12 & 10 (Formulas, Matrix Tensors, Tables) \\
IR Lecture Slides & Presentation Deck (16:9) & 6 & 9 & 8 (ANN Search, RRF, Re-ranking) \\
Distributed Systems & Theoretical Systems Paper & 4 & 9 & 4 (Consensus, CAP, Deadlocks) \\
\midrule
\textbf{Total Corpus} & \textbf{Multi-Modal Benchmark} & \textbf{18} & \textbf{46} & \textbf{32 Curated Q\&A Pairs} \\
\bottomrule
\end{tabular}
\end{table}
```

---

## 7. Examiner Viva Voce Prep: Defending Your Experimental Setup

### Q1: *"How did you choose your test dataset, and why didn't you just test on random internet PDFs?"*
> **Answer:** *"Evaluating RAG systems on random uncurated documents is academically invalid because it lacks a verifiable ground truth. Without knowing the exact target pages and chunk IDs beforehand, metrics like Context Precision@K, Mean Reciprocal Rank (MRR), and Citation Accuracy cannot be quantitatively computed. We established an experimental corpus of four distinct academic documents representing the three primary modalities encountered by university students: text-heavy syllabi, multimodal papers with formulas and tables, and landscape slide decks. This allowed us to calculate exact Hit@K, MRR, Fact Recall, and Chunk Retrieval Precision."*

### Q2: *"How do you guarantee that your chunk IDs are deterministic and reproducible?"*
> **Answer:** *"Our chunking pipeline (`ai-service/core/chunker.py`) uses a deterministic Recursive Character Text Splitter configured with an $800$-character chunk size and $150$-character overlap. Each chunk receives a deterministic slugged identifier formatted as `<document_slug>_chunk_<counter>`. When `eval/dataset/generate_dataset.py` parses the documents, it verifies that every single chunk ID referenced in `ground_truth.json` strictly exists in `indexed_chunks.json` and contains the expected factual tokens."*

### Q3: *"How does your dataset evaluate multimodal document parsing?"*
> **Answer:** *"Our document `multimodal_deep_learning_theory.pdf` contains both dense mathematical equation blocks ($\text{Attention}(Q,K,V)$ and decoupled AdamW updates) and multi-column comparison tables (Table 1 and Table 2). Queries `bench_11` through `bench_20` specifically test whether our parser can preserve table cell alignments and equation structures rather than flattening them into garbled, unsearchable character streams."*
