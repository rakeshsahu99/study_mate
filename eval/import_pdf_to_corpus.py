#!/usr/bin/env python3
"""
=============================================================================
Utility: Import PDF Notes to Evaluation Corpus (eval/import_pdf_to_corpus.py)
=============================================================================
Quickly ingests any PDF (e.g. your subject notes, lecture slides, syllabus)
into `eval/sample_academic_corpus.json`, and outputs a ready-to-use template
for adding questions to `eval/golden_dataset.json`.

Usage:
    python eval/import_pdf_to_corpus.py "path/to/my_notes.pdf"
=============================================================================
"""

import os
import sys
import json
import argparse
import shutil

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
CORPUS_PATH = os.path.join(CURRENT_DIR, "sample_academic_corpus.json")
GOLDEN_PATH = os.path.join(CURRENT_DIR, "golden_dataset.json")

def chunk_text(text: str, max_chars: int = 500) -> list[str]:
    """Splits raw page text into natural paragraphs or sentence groups."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    current_chunk = []
    current_len = 0
    
    for p in paragraphs:
        if current_len + len(p) > max_chars and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = [p]
            current_len = len(p)
        else:
            current_chunk.append(p)
            current_len += len(p)
            
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def import_pdf(pdf_path: str, max_pages: int = 20):
    if not os.path.exists(pdf_path):
        print(f"[-] Error: File not found: {pdf_path}")
        sys.exit(1)
        
    filename = os.path.basename(pdf_path)
    print(f"[*] Reading PDF: {filename}...")

    try:
        import pymupdf
        doc = pymupdf.open(pdf_path)
    except ImportError:
        try:
            import fitz
            doc = fitz.open(pdf_path)
        except ImportError:
            import pdfplumber
            doc = pdfplumber.open(pdf_path)

    new_chunks = []
    
    # Extract pages
    try:
        # Check if pymupdf (fitz.Document)
        page_count = len(doc)
        for i in range(min(page_count, max_pages)):
            page = doc[i]
            text = page.get_text() if hasattr(page, "get_text") else page.extract_text()
            if text and text.strip():
                for c in chunk_text(text.strip()):
                    new_chunks.append({
                        "source": filename,
                        "page": i + 1,
                        "text": c
                    })
    except Exception as read_err:
        print(f"[-] Error parsing pages: {read_err}")
        sys.exit(1)

    if not new_chunks:
        print("[-] Warning: No extractable text found in this PDF (might be image-only).")
        sys.exit(1)

    print(f"[+] Extracted {len(new_chunks)} text chunks across {min(len(doc), max_pages)} pages.")

    # Load existing corpus
    if os.path.exists(CORPUS_PATH):
        # Backup
        shutil.copyfile(CORPUS_PATH, CORPUS_PATH + ".bak")
        with open(CORPUS_PATH, "r", encoding="utf-8") as f:
            corpus = json.load(f)
    else:
        corpus = []

    # Filter out duplicates if already imported
    existing_texts = {c.get("text", "") for c in corpus if c.get("source") == filename}
    added_count = 0
    for chunk in new_chunks:
        if chunk["text"] not in existing_texts:
            corpus.append(chunk)
            added_count += 1

    with open(CORPUS_PATH, "w", encoding="utf-8") as f:
        json.dump(corpus, f, indent=2)

    print(f"[+] Successfully added {added_count} new chunks to {os.path.basename(CORPUS_PATH)}!")
    print(f"    (Backup saved to {os.path.basename(CORPUS_PATH)}.bak)")

    # Print template for golden_dataset.json
    first_chunk = new_chunks[0]
    sample_page = first_chunk["page"]
    first_words = first_chunk["text"][:80].replace('"', '\\"')

    print("\n" + "=" * 75)
    print(" NEXT STEP: Add questions from this document to eval/golden_dataset.json")
    print("=" * 75)
    print("Open `eval/golden_dataset.json` and append an entry like this at the end:\n")
    sample_entry = {
        "id": f"my_notes_{filename.split('.')[0][:10].lower()}_01",
        "question": f"What key concept is discussed regarding {filename.split('.')[0]} on page {sample_page}?",
        "ground_truth_answer": f"{first_words}...",
        "expected_document": filename,
        "expected_pages": [sample_page],
        "key_facts": [w.strip() for w in first_chunk["text"].split()[:3] if len(w) > 3]
    }
    print(json.dumps([sample_entry], indent=2)[2:-2] + ",")
    print("\n" + "=" * 75)
    print(" Then run the evaluation benchmark:")
    print(' powershell -Command \'$env:PYTHONPATH="ai-service;eval;."; & "ai-service/venv/Scripts/python.exe" "eval/benchmark.py" --dataset eval/golden_dataset.json --corpus eval/sample_academic_corpus.json --mode offline --no-llm\'')
    print("=" * 75 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import PDF notes into evaluation corpus")
    parser.add_argument("pdf_path", type=str, help="Path to PDF notes file")
    parser.add_argument("--max-pages", type=int, default=20, help="Maximum pages to import")
    args = parser.parse_args()
    import_pdf(args.pdf_path, args.max_pages)
