import os
import sys
import json
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.parser import extract_text_pymupdf, benchmark_pdf_parsers
from main import execute_ablation_comparison_sync, app

def test_telemetry():
    print("=" * 60)
    print("Testing Telemetry & Latency Instrumentation Pipeline")
    print("=" * 60)

    # 1. Test PyMuPDF and Parser Throughput
    sample_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "eval", "dataset", "documents", "cs601_advanced_algorithms_syllabus.pdf"))
    assert os.path.exists(sample_pdf), f"Sample PDF not found at {sample_pdf}"

    with open(sample_pdf, "rb") as f:
        pdf_bytes = f.read()

    print("\n[1] Running Parser Throughput Benchmark on sample PDF...")
    throughput_res = benchmark_pdf_parsers(pdf_bytes, os.path.basename(sample_pdf), sample_pages=4)
    print(f"    PyMuPDF latency: {throughput_res['local_pymupdf']['latency_ms']} ms ({throughput_res['local_pymupdf']['ms_per_page']} ms/page)")
    print(f"    PyMuPDF throughput: {throughput_res['local_pymupdf']['throughput_pages_per_sec']} pages/sec")
    print(f"    Gemini Flash latency: {throughput_res['gemini_multimodal_vision']['latency_ms']} ms ({throughput_res['gemini_multimodal_vision']['ms_per_page']} ms/page)")
    print(f"    Speedup: {throughput_res['speedup_ratio']}")

    assert throughput_res["local_pymupdf"]["ms_per_page"] > 0
    assert throughput_res["throughput_comparison"]["ratio"] > 1

    # 2. Test Ablation Comparison Latency Instrumentation
    print("\n[2] Testing Ablation Comparison Latency Breakdown (Configs A, B, C)...")
    comp_res = execute_ablation_comparison_sync("What is Byzantine fault tolerance?", top_k=5)
    
    cfg_a = comp_res["configurations"]["A_standalone_llm"]
    cfg_b = comp_res["configurations"]["B_vanilla_rag"]
    cfg_c = comp_res["configurations"]["C_proposed_system"]
    
    print(f"    Config A Latency: {cfg_a['latency_ms']} ms (Gen: {cfg_a['latency']['generation_ms']} ms)")
    print(f"    Config B Latency: {cfg_b['latency_ms']} ms (Embed: {cfg_b['latency']['embedding_ms']} ms, Ret: {cfg_b['latency']['retrieval_ms']} ms, Gen: {cfg_b['latency']['generation_ms']} ms)")
    print(f"    Config C Latency: {cfg_c['latency_ms']} ms (Embed: {cfg_c['latency']['embedding_ms']} ms, Ret: {cfg_c['latency']['retrieval_ms']} ms, Re-rank: {cfg_c['latency']['reranking_ms']} ms, Gen: {cfg_c['latency']['generation_ms']} ms)")
    print(f"    Re-ranking Overhead: +{comp_res['ablation_summary']['reranking_overhead_ms']} ms")
    print(f"    Noise Reduction: {comp_res['ablation_summary']['false_positive_reduction_pct']}% noise filtered")

    assert "latency" in cfg_a
    assert "latency" in cfg_b
    assert "latency" in cfg_c
    assert "reranking_ms" in cfg_c["latency"]
    assert "reranking_overhead_ms" in comp_res["ablation_summary"]

    print("\n[3] Verifying SVG Chart Generation...")
    charts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "eval", "results"))
    lat_chart = os.path.join(charts_dir, "latency_breakdown.svg")
    tp_chart = os.path.join(charts_dir, "parser_throughput.svg")
    
    assert os.path.exists(lat_chart), f"Missing {lat_chart}"
    assert os.path.exists(tp_chart), f"Missing {tp_chart}"
    print(f"    Latency breakdown SVG verified: {os.path.getsize(lat_chart)} bytes")
    print(f"    Parser throughput SVG verified: {os.path.getsize(tp_chart)} bytes")

    print("\n[SUCCESS] All Telemetry & Latency Instrumentation tests passed cleanly!")

if __name__ == "__main__":
    test_telemetry()
