import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

OUTPUT_DIR = "Report/diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Update Fig 5.3: fix collisions, remove duplicate title
def fix_fig_5_3():
    fig, ax = plt.subplots(figsize=(13, 7.2), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Subtitle only, no duplicate 'Figure 5.3:' banner
    ax.text(50, 95, "Cascading Bi-Encoder Candidate Pooling (Stage 1) to All-to-All Cross-Attention Ranking (Stage 2)",
            ha='center', va='center', fontsize=11, fontstyle='italic', color='#475569')

    # Query Box
    b_q = patches.FancyBboxPatch((3, 38), 16, 36, boxstyle="round,pad=0.8", facecolor="#EFF6FF", edgecolor="#3B82F6", lw=2)
    ax.add_patch(b_q)
    ax.text(11, 67, "User Query", ha='center', va='center', fontsize=11, fontweight='bold', color="#1D4ED8")
    ax.text(11, 56, "q: 'What is\nnon-preemptive\nSJF scheduling?'", ha='center', va='center', fontsize=8.5, color="#1E293B")
    ax.text(11, 44, "FastEmbed Bi-Encoder\n(all-MiniLM-L6-v2)\n[14.5 ms]", ha='center', va='center', fontsize=7.5, color="#475569")

    # Arrow 1: clear gap
    ax.annotate('', xy=(24, 56), xytext=(19, 56), arrowprops=dict(arrowstyle="->", color="#334155", lw=2))
    ax.text(21.5, 62, "384-d v", ha='center', fontsize=8, fontweight='bold', color="#1E293B",
            bbox=dict(boxstyle="round,pad=0.2", fc="#FFFFFF", ec="#94A3B8", lw=0.6))

    # Stage 1 Box
    b_s1 = patches.FancyBboxPatch((24, 22), 22, 66, boxstyle="round,pad=0.8", facecolor="#F0FDF4", edgecolor="#10B981", lw=2)
    ax.add_patch(b_s1)
    ax.text(35, 83, "STAGE 1:\nDense Vector Search", ha='center', va='center', fontsize=10.5, fontweight='bold', color="#047857")
    ax.text(35, 75, "Supabase PostgreSQL\n(pgvector HNSW)\n[34.2 ms]", ha='center', va='center', fontsize=8, color="#065F46")
    
    candidates = [
        "Candidate 1 (Sim: 0.82) - Intro Overview",
        "Candidate 2 (Sim: 0.80) - Preemptive SJF",
        "Candidate 3 (Sim: 0.79) - FCFS Contrast",
        "Candidate 4 (Sim: 0.77) - Waiting Formula",
        "Candidate 5 (Sim: 0.75) - Turnaround Calc",
        "... Top 15 Candidates Retrieved ...",
    ]
    for idx, c in enumerate(candidates):
        y_pos = 66 - idx * 7.0
        fc = "#FEF3C7" if idx in [3, 4] else "#FFFFFF"
        bc = patches.FancyBboxPatch((25.5, y_pos-2.4), 19, 5.0, boxstyle="round,pad=0.3", facecolor=fc, edgecolor="#94A3B8", lw=0.8)
        ax.add_patch(bc)
        ax.text(35, y_pos, c, ha='center', va='center', fontsize=6.8, color="#1E293B")

    # Arrow 2: clear gap
    ax.annotate('', xy=(51, 56), xytext=(46, 56), arrowprops=dict(arrowstyle="->", color="#334155", lw=2))
    ax.text(48.5, 62, "Top-15 Pool", ha='center', fontsize=8, fontweight='bold', color="#1E293B",
            bbox=dict(boxstyle="round,pad=0.2", fc="#FFFFFF", ec="#94A3B8", lw=0.6))

    # Stage 2 Box
    b_s2 = patches.FancyBboxPatch((51, 22), 23, 66, boxstyle="round,pad=0.8", facecolor="#FFFBEB", edgecolor="#F59E0B", lw=2)
    ax.add_patch(b_s2)
    ax.text(62.5, 83, "STAGE 2:\nCross-Encoder Re-Ranking", ha='center', va='center', fontsize=10.5, fontweight='bold', color="#B45309")
    ax.text(62.5, 75, "ms-marco-MiniLM-L-6-v2\n(ONNX Cross-Attention)\n[44.8 ms]", ha='center', va='center', fontsize=8, color="#92400E")

    reranked = [
        "Rank 1: Waiting Formula (Score: 0.884)",
        "Rank 2: Turnaround Calc (Score: 0.852)",
        "Rank 3: Preemptive SJF (Score: 0.710)",
        "Rank 4: Burst Time Table (Score: 0.695)",
        "Rank 5: Gantt Chart Step (Score: 0.640)",
        "-- 24.4% False Positives Demoted --",
    ]
    for idx, c in enumerate(reranked):
        y_pos = 66 - idx * 7.0
        fc = "#D1FAE5" if idx < 2 else ("#FEE2E2" if idx == 5 else "#FFFFFF")
        bc = patches.FancyBboxPatch((52.5, y_pos-2.4), 20, 5.0, boxstyle="round,pad=0.3", facecolor=fc, edgecolor="#CBD5E1", lw=0.8)
        ax.add_patch(bc)
        ax.text(62.5, y_pos, c, ha='center', va='center', fontsize=6.8, color="#1E293B")

    # Arrow 3: clear gap
    ax.annotate('', xy=(79, 56), xytext=(74, 56), arrowprops=dict(arrowstyle="->", color="#334155", lw=2))
    ax.text(76.5, 62, "Top-5 Grounded", ha='center', fontsize=7.5, fontweight='bold', color="#1E293B",
            bbox=dict(boxstyle="round,pad=0.2", fc="#FFFFFF", ec="#94A3B8", lw=0.6))

    # Generation Box
    b_gen = patches.FancyBboxPatch((79, 32), 18, 48, boxstyle="round,pad=0.8", facecolor="#FAF5FF", edgecolor="#A855F7", lw=2)
    ax.add_patch(b_gen)
    ax.text(88, 73, "Grounded LLM\nGeneration", ha='center', va='center', fontsize=10.5, fontweight='bold', color="#6B21A8")
    ax.text(88, 62, "Gemini 2.5 Flash\n(T=0.2 strict bounds)\n[825.0 ms]", ha='center', va='center', fontsize=8, color="#7E22CE")
    ax.text(88, 46, "Verified Citation:\n[Source 1, Page 4]\nTurnaround Formula\n& Waiting Proof", ha='center', va='center', fontsize=7.5, color="#1E293B")

    # Bottom pill
    b_sum = patches.FancyBboxPatch((8, 6), 84, 12, boxstyle="round,pad=0.5", facecolor="#F1F5F9", edgecolor="#64748B", lw=1.5)
    ax.add_patch(b_sum)
    ax.text(50, 12, "Empirical Impact: Hit@3 improves from 71.4% to 89.5% (+18.1 pp, +25.4% relative gain);\nMRR improves from 0.68 to 0.86 (+26.5% relative); 24.4% false-positive noise chunks eliminated for only 44.8 ms overhead.",
            ha='center', va='center', fontsize=8.5, color="#1E293B", fontweight='bold')

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_5_3_Two_Stage_Retrieval_and_Neural_Reranking.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print("Fixed Fig 5.3 successfully")

# 2. Update Fig 5.5: wrap telemetry, align arithmetic, cite only sources 1 & 2
def fix_fig_5_5():
    fig, ax = plt.subplots(figsize=(12, 7.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    win = patches.FancyBboxPatch((2, 2), 96, 96, boxstyle="round,pad=0.5", facecolor="#0F172A", edgecolor="#334155", lw=2)
    ax.add_patch(win)
    ax.text(6, 95, "AI Study Hub — Conversational Study Assistant & Citation Bounds", fontsize=9, color="#94A3B8")

    # Telemetry Pill bar - 2 lines, arithmetic matches 918.5 ms
    tb = patches.FancyBboxPatch((6, 84), 88, 8.5, boxstyle="round,pad=0.4", facecolor="#1E293B", edgecolor="#475569", lw=1)
    ax.add_patch(tb)
    ax.text(8, 89.5, "Live Telemetry:  Embedding: 14.5ms  |  HNSW Retrieval: 34.2ms  |  Cross-Encoder Re-Ranking: 44.8ms", fontsize=7.8, color="#38BDF8", fontweight='bold')
    ax.text(8, 86.2, "                 Gemini 2.5 Flash Generation: 825.0ms  |  Total Query-to-Answer Pipeline Latency: 918.5ms", fontsize=7.8, color="#A7F3D0", fontweight='bold')

    # Chat User Query
    uq = patches.FancyBboxPatch((40, 70), 54, 11, boxstyle="round,pad=0.5", facecolor="#1E40AF", edgecolor="#3B82F6", lw=1)
    ax.add_patch(uq)
    ax.text(42, 77, "Student Question:", fontsize=8, fontweight='bold', color="#93C5FD")
    ax.text(42, 72.5, "What is non-preemptive Shortest Job First (SJF) scheduling, and how is waiting time calculated?", fontsize=8, color="#FFFFFF")

    # Chat Assistant Response
    ar = patches.FancyBboxPatch((6, 20), 88, 47, boxstyle="round,pad=0.8", facecolor="#1E293B", edgecolor="#334155", lw=1)
    ax.add_patch(ar)
    ax.text(9, 63, "AI Study Hub Assistant  [Configuration C: Neural Cross-Encoder Re-Ranked]", fontsize=9.5, fontweight='bold', color="#38BDF8")
    
    body_text = (
        "Non-preemptive Shortest Job First (SJF) is a CPU scheduling algorithm where once the CPU is allocated to a\n"
        "process, it cannot be interrupted until it completes its CPU burst [Source 1, Page 4].\n\n"
        "Key Characteristics & Formula:\n"
        "• Non-preemptive Condition: If a new process arrives with a shorter burst time, it is placed in the ready queue\n"
        "  but does NOT preempt the currently running process [Source 1, Page 4].\n"
        "• Turnaround Time: Turnaround Time = Completion Time - Arrival Time [Source 2, Page 5].\n"
        "• Waiting Time: Waiting Time = Turnaround Time - Burst Time [Source 1, Page 4].\n"
        "• Advantage: Provably minimizes average waiting time among all non-preemptive algorithms [Source 1, Page 4]."
    )
    ax.text(9, 44, body_text, fontsize=7.8, color="#F1F5F9", va='center')

    # Source Badges (Only Source 1 and Source 2, exactly matching text citations)
    sources = [
        ("Source 1", "CPU-Scheduling-and-Algorithm-.pdf", "Page 4", "Non-preemptive definition & waiting time equation"),
        ("Source 2", "CPU-Scheduling-and-Algorithm-.pdf", "Page 5", "Turnaround time and completion calculation matrix"),
    ]
    for idx, (sname, fname, page, snip) in enumerate(sources):
        x = 9 + idx * 44
        sb = patches.FancyBboxPatch((x, 23), 42, 7, boxstyle="round,pad=0.3", facecolor="#0F172A", edgecolor="#38BDF8", lw=0.8)
        ax.add_patch(sb)
        ax.text(x + 2, 27.5, f"[{sname}] {fname} (p. {page})", fontsize=7.2, fontweight='bold', color="#38BDF8")
        ax.text(x + 2, 24.8, snip, fontsize=6.5, color="#94A3B8")

    # Bottom Query Input box
    ib = patches.FancyBboxPatch((6, 6), 88, 10, boxstyle="round,pad=0.5", facecolor="#1E293B", edgecolor="#475569", lw=1)
    ax.add_patch(ib)
    ax.text(9, 11, "Ask follow-up question (e.g., 'What are its limitations?')...", fontsize=8.5, color="#64748B")
    ax.text(88, 11, "Send", fontsize=8.5, fontweight='bold', color="#38BDF8")

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_5_5_Conversational_RAG_Interface.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print("Fixed Fig 5.5 successfully")

# 3. Update Fig 6.1: title cutoff fixed, +18.1 pp label
def fix_fig_6_1():
    k_values = np.arange(1, 11)
    standard_vector_hit = np.array([52.4, 63.1, 71.4, 77.2, 82.0, 85.3, 87.8, 89.6, 91.0, 92.3])
    reranked_hit        = np.array([78.5, 85.0, 89.5, 92.1, 94.2, 95.8, 96.9, 97.5, 98.1, 98.6])
    bm25_hit            = np.array([32.0, 41.5, 48.2, 53.6, 58.1, 61.4, 64.0, 66.2, 68.1, 69.5])

    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=300)
    ax.plot(k_values, reranked_hit, marker="s", markersize=7, color="#0ea5e9", linewidth=2.5,
            label="Proposed: Hybrid Vector + Cross-Encoder Re-Ranking", zorder=4)
    ax.plot(k_values, standard_vector_hit, marker="o", markersize=6, color="#64748b", linewidth=2.0, linestyle="--",
            label="Baseline 2: Standard Vector Search (all-MiniLM-L6-v2)", zorder=3)
    ax.plot(k_values, bm25_hit, marker="^", markersize=6, color="#f43f5e", linewidth=1.8, linestyle=":",
            label="Baseline 1: Pure Keyword / BM25", zorder=2)

    # Annotate key gain points at K=3 and K=5 (clean +18.1 pp)
    ax.annotate("Hit@3: 89.5%\n(+18.1 pp, +25.4% rel)",
                xy=(3, 89.5), xytext=(2.2, 94.0),
                arrowprops=dict(arrowstyle="->", color="#0284c7", lw=1.5),
                fontsize=9, fontweight="bold", color="#0284c7",
                bbox=dict(boxstyle="round,pad=0.3", fc="#e0f2fe", ec="#38bdf8", lw=1))

    ax.annotate("Hit@5: 94.2%\n(+12.2 pp gain)",
                xy=(5, 94.2), xytext=(5.3, 87.0),
                arrowprops=dict(arrowstyle="->", color="#0284c7", lw=1.5),
                fontsize=9, fontweight="bold", color="#0284c7",
                bbox=dict(boxstyle="round,pad=0.3", fc="#e0f2fe", ec="#38bdf8", lw=1))

    # Clean short title, no cutoff
    ax.set_title("Retrieval Recall Curve: Standard Vector vs. Neural Re-Ranking",
                 fontsize=12, fontweight="bold", pad=12, color="#0f172a")
    ax.set_xlabel("Cut-off Rank (K)", fontsize=10.5, fontweight="bold", labelpad=8, color="#1e293b")
    ax.set_ylabel("Hit@K Retrieval Accuracy (%)", fontsize=10.5, fontweight="bold", labelpad=8, color="#1e293b")
    ax.set_xticks(k_values)
    ax.set_ylim(25, 105)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{int(y)}%"))
    ax.legend(loc="lower right", frameon=True, framealpha=0.95, facecolor="#ffffff", edgecolor="#cbd5e1", fontsize=9)
    
    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_6_1_Hit_at_K_Retrieval_Curve.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print("Fixed Fig 6.1 successfully")

# 4. Update Fig 6.3: fix label collision with title
def fix_fig_6_3():
    fig, ax = plt.subplots(figsize=(8.5, 5.2), dpi=300)
    methods = ["Local PyMuPDF\n(fitz C-Engine)", "Gemini 2.5 Flash\nMultimodal Vision OCR"]
    times_per_page = [7.0, 1120.0]
    colors = ["#10B981", "#EF4444"]
    
    bars = ax.bar(methods, times_per_page, color=colors, width=0.45)
    ax.set_yscale('log')
    ax.set_ylim(1, 10000)  # raised y-limit to avoid collision with title
    ax.set_ylabel("Processing Latency per Page (ms) [Log Scale]", fontsize=10, fontweight='bold')
    ax.set_title("Parser Throughput Comparison: Local Engine vs Cloud Vision", fontsize=12, fontweight='bold', pad=14)
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    ax.text(0, 14, "7.0 ms / page\n(Sub-10ms Target Achieved)", ha='center', fontsize=8.8, fontweight='bold', color="#065F46")
    ax.text(1, 1600, "1,120.0 ms / page\n(Cloud Vision Network + OCR)", ha='center', fontsize=8.8, fontweight='bold', color="#991B1B")

    ax.annotate("160x Faster Throughput", xy=(0.48, 120), xytext=(0.48, 120),
                ha='center', fontsize=11, fontweight='bold', color="#1E3A8A",
                bbox=dict(boxstyle="round,pad=0.5", fc="#DBEAFE", ec="#1D4ED8", lw=1.5))

    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "Figure_6_3_Parser_Throughput_PyMuPDF_vs_GeminiVision.png")
    plt.savefig(p, bbox_inches='tight', dpi=300)
    plt.close()
    print("Fixed Fig 6.3 successfully")

if __name__ == "__main__":
    fix_fig_5_3()
    fix_fig_5_5()
    fix_fig_6_1()
    fix_fig_6_3()
    print("All 4 target diagrams regenerated cleanly!")
