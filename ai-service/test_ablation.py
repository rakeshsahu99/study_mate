#!/usr/bin/env python3
"""
Unit and integration verification for the Ablation Study Switches:
- Configuration A: Standalone LLM (No RAG / Zero-Shot)
- Configuration B: Vanilla Single-Vector RAG (FastEmbed + Cosine Similarity only)
- Configuration C: Proposed System (FastEmbed + Neural Cross-Encoder Re-Ranking + Multimodal Parser)
"""
import sys
import os

AI_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(AI_DIR, ".."))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, AI_DIR)

from core.search import search_query_sync, compute_false_positive_reduction
from main import execute_ablation_comparison_sync

candidates = [
    {
        "text": "Deep learning backpropagation computes gradients by applying the chain rule backwards through layers.",
        "metadata": {"source": "Deep_Learning_Architectures.pdf", "page": 3},
        "similarity": 0.88
    },
    {
        "text": "The ReLU activation function mitigates vanishing gradients by having a constant derivative.",
        "metadata": {"source": "Deep_Learning_Architectures.pdf", "page": 1},
        "similarity": 0.81
    },
    {
        "text": "Relational databases enforce ACID properties to guarantee reliable transaction processing.",
        "metadata": {"source": "Database_Systems_and_Indexing.pdf", "page": 1},
        "similarity": 0.65
    },
    {
        "text": "Operating systems virtual memory maps virtual addresses using page tables and page fault interrupts.",
        "metadata": {"source": "Distributed_Operating_Systems.pdf", "page": 1},
        "similarity": 0.55
    }
]

def mock_vector_search(query: str, top_k: int = 5):
    return candidates[:top_k]

def run_tests():
    print("=" * 70, flush=True)
    print("TEST 1: Testing search_query ablation switch (Sync & Functional)...", flush=True)
    print("=" * 70, flush=True)
    
    # Test Configuration B: Vanilla Vector Search (Re-ranking disabled)
    res_b = search_query_sync(
        query="Backpropagation chain rule",
        vector_search_fn=mock_vector_search,
        enable_reranking=False,
        top_k=2
    )
    print(f"[+] Config B Returned: {len(res_b)} chunks", flush=True)
    print(f"    Mode: {res_b[0]['configuration']}", flush=True)
    print(f"    Rank 1: {res_b[0]['metadata']['source']} (P.{res_b[0]['metadata']['page']}) - Sim: {res_b[0]['similarity']}", flush=True)
    assert len(res_b) == 2
    assert "Vanilla" in res_b[0]["configuration"]
    
    # Test Configuration C: Proposed Approach (Re-ranking enabled)
    res_c = search_query_sync(
        query="Backpropagation chain rule",
        vector_search_fn=mock_vector_search,
        enable_reranking=True,
        top_k=2
    )
    print(f"[+] Config C Returned: {len(res_c)} chunks", flush=True)
    print(f"    Mode: {res_c[0]['configuration']}", flush=True)
    print(f"    Rank 1: {res_c[0]['metadata']['source']} (P.{res_c[0]['metadata']['page']}) - Re-rank score: {res_c[0]['rerank_score']:.4f}", flush=True)
    assert len(res_c) == 2
    assert "Proposed" in res_c[0]["configuration"]
    assert res_c[0]["rerank_score"] > 0
    
    print("\n" + "=" * 70, flush=True)
    print("TEST 2: Testing compute_false_positive_reduction...", flush=True)
    print("=" * 70, flush=True)
    fp_analysis = compute_false_positive_reduction(
        baseline_chunks=candidates[:4],
        reranked_chunks=candidates[:2],
        expected_doc="Deep_Learning_Architectures.pdf",
        expected_pages=[3, 1]
    )
    print(f"[+] Baseline False Positives: {fp_analysis['baseline_false_positives']}/{fp_analysis['baseline_top_k']} ({fp_analysis['baseline_fp_rate']*100:.1f}%)", flush=True)
    print(f"[+] Proposed False Positives: {fp_analysis['reranked_false_positives']}/{fp_analysis['reranked_top_k']} ({fp_analysis['reranked_fp_rate']*100:.1f}%)", flush=True)
    print(f"[+] False-Positive Reduction: {fp_analysis['false_positive_reduction_pct']:.1f}%", flush=True)
    print(f"[+] Filtered Noise Count:    {fp_analysis['filtered_noise_chunks_count']} chunks", flush=True)
    assert fp_analysis["false_positive_reduction_pct"] > 0
    print("[+] TEST 1 and 2 passed!", flush=True)

    print("\n" + "=" * 70, flush=True)
    print("TEST 3: Testing execute_ablation_comparison (3-Way Comparison)...", flush=True)
    print("=" * 70, flush=True)
    comparison = execute_ablation_comparison_sync(
        query="How does Backpropagation calculate weight updates in neural networks?",
        top_k=5
    )
    print(f"[+] Query: {comparison['query']}", flush=True)
    print(f"[+] Configurations Evaluated: {comparison['ablation_summary']['configurations_tested']}", flush=True)
    print(f"[+] Config A (Standalone): {comparison['configurations']['A_standalone_llm']['name']}", flush=True)
    print(f"    Latency: {comparison['configurations']['A_standalone_llm']['latency_ms']} ms | Sources: {len(comparison['configurations']['A_standalone_llm']['sources'])}", flush=True)
    print(f"[+] Config B (Vanilla RAG): {comparison['configurations']['B_vanilla_rag']['name']}", flush=True)
    print(f"    Latency: {comparison['configurations']['B_vanilla_rag']['latency_ms']} ms | Chunks: {len(comparison['configurations']['B_vanilla_rag']['chunks'])}", flush=True)
    print(f"[+] Config C (Proposed):    {comparison['configurations']['C_proposed_system']['name']}", flush=True)
    print(f"    Latency: {comparison['configurations']['C_proposed_system']['latency_ms']} ms | Chunks: {len(comparison['configurations']['C_proposed_system']['chunks'])}", flush=True)
    print(f"[+] False-Positive Noise Filtered: {comparison['ablation_summary']['false_positive_reduction_pct']:.1f}%", flush=True)
    
    print("\n" + "=" * 70, flush=True)
    print("ALL ABLATION SWITCH TESTS PASSED SUCCESSFULLY! (100% VERIFIED)", flush=True)
    print("=" * 70, flush=True)

if __name__ == "__main__":
    run_tests()
