"""
Build Benchmark PDF Documents for AI Study Hub Evaluation Suite.
Generates 4 Standard Academic Test Documents:
1. cs601_advanced_algorithms_syllabus.pdf (Text-heavy syllabus)
2. multimodal_deep_learning_theory.pdf (Multimodal paper with equations and tables)
3. lecture_slides_vector_search_rag.pdf (Slide deck in landscape format)
4. distributed_systems_consensus_paper.pdf (Core systems paper)
"""

import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether,
    HRFlowable
)

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "documents")
os.makedirs(DOCS_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# Base Styles
# -----------------------------------------------------------------------------
def get_custom_styles():
    styles = getSampleStyleSheet()
    
    # Custom adjustments
    styles.add(ParagraphStyle(
        name="DocTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=10
    ))
    styles.add(ParagraphStyle(
        name="DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#475569"),
        spaceAfter=15
    ))
    styles.add(ParagraphStyle(
        name="SectionHeader",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#1e3a8a"),
        spaceBefore=12,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name="SubSectionHeader",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#0f766e"),
        spaceBefore=8,
        spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        name="AcademicBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name="AcademicBodyBold",
        parent=styles["AcademicBody"],
        fontName="Helvetica-Bold"
    ))
    styles.add(ParagraphStyle(
        name="FormulaBox",
        parent=styles["Normal"],
        fontName="Courier-Bold",
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#1e1e24"),
        backColor=colors.HexColor("#f1f5f9"),
        borderColor=colors.HexColor("#cbd5e1"),
        borderWidth=1,
        borderPadding=6,
        spaceBefore=6,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name="SlideTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#0284c7"),
        spaceAfter=14
    ))
    styles.add(ParagraphStyle(
        name="SlideSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#334155"),
        spaceAfter=12
    ))
    styles.add(ParagraphStyle(
        name="SlideBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=17,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=10
    ))
    styles.add(ParagraphStyle(
        name="SlideBullet",
        parent=styles["SlideBody"],
        leftIndent=20,
        firstLineIndent=-12
    ))
    styles.add(ParagraphStyle(
        name="TableHeader",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=1
    ))
    styles.add(ParagraphStyle(
        name="TableCell",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#1e293b")
    ))
    styles.add(ParagraphStyle(
        name="TableCellBold",
        parent=styles["TableCell"],
        fontName="Helvetica-Bold"
    ))
    return styles

# -----------------------------------------------------------------------------
# Document 1: cs601_advanced_algorithms_syllabus.pdf (Text-Heavy)
# -----------------------------------------------------------------------------
def build_syllabus_doc(filepath: str, styles):
    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    story = []

    # PAGE 1
    story.append(Paragraph("CS601: Advanced Algorithms and Computational Complexity", styles["DocTitle"]))
    story.append(Paragraph("Department of Computer Science & Engineering | Academic Term: Autumn 2026 | Credits: 4.0", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("1. Course Administration & Prerequisites", styles["SectionHeader"]))
    story.append(Paragraph("<b>Primary Instructor:</b> Prof. Edward R. Tarjan (Office: Engineering Quad 412, Email: etarjan@university.edu)<br/>"
                           "<b>Teaching Assistants:</b> Michael Stone (Head TA), Sarah Lin, David Zhou.<br/>"
                           "<b>Lectures:</b> Mondays and Wednesdays 10:00 AM - 11:30 AM in Turing Lecture Hall (Auditorium 101).<br/>"
                           "<b>Prerequisites:</b> Strict prerequisite enforcement requires a grade of B or higher in CS301 (Data Structures) and CS305 (Discrete Mathematics). Familiarity with basic probability theory, linear algebra, and graph representations (adjacency lists vs adjacency matrices) is required.", styles["AcademicBody"]))

    story.append(Paragraph("2. Course Catalog Description & Pedagogical Goals", styles["SectionHeader"]))
    story.append(Paragraph("CS601 explores design principles, mathematical rigor, and asymptotic performance bounds of modern algorithmic frameworks. Students learn to formulate non-trivial computational problems into mathematically rigorous graph formulations, linear programs, and network flow models. Beyond polynomial-time algorithms, the course introduces amortized efficiency proofs, randomized derandomization strategies, sublinear-time streaming algorithms, and rigorous approximation algorithms with provable performance guarantees for NP-hard optimization problems.", styles["AcademicBody"]))

    story.append(Paragraph("3. Required Textbooks and Scholarly References", styles["SectionHeader"]))
    story.append(Paragraph("1. <b>CLRS:</b> Cormen, Leiserson, Rivest, and Stein. <i>Introduction to Algorithms</i>, 4th Edition, MIT Press, 2022.<br/>"
                           "2. <b>KT:</b> Kleinberg and Tardos. <i>Algorithm Design</i>, Pearson / Addison-Wesley, 2006.<br/>"
                           "3. <b>Vazirani:</b> Vijay Vazirani. <i>Approximation Algorithms</i>, Springer-Verlag, 2001.<br/>"
                           "4. <b>Motwani & Raghavan:</b> Rajeev Motwani and Prabhakar Raghavan. <i>Randomized Algorithms</i>, Cambridge University Press, 1995.", styles["AcademicBody"]))

    story.append(Paragraph("4. Academic Integrity & Artificial Intelligence Policy", styles["SectionHeader"]))
    story.append(Paragraph("All homework submissions and coding assignments must represent the original intellectual work of each individual student. Discussion of concepts in study groups is permitted, but written solutions must be drafted individually from scratch. <b>Generative AI Policy:</b> Large Language Models (LLMs) such as Gemini, ChatGPT, or Claude may only be used as tutoring assistants for conceptual explanations. Using LLMs to generate verbatim mathematical proofs, pseudo-code implementations, or homework answers constitutes academic dishonesty and will result in a course grade of F and referral to the University Disciplinary Board.", styles["AcademicBody"]))
    
    story.append(PageBreak())

    # PAGE 2
    story.append(Paragraph("CS601 Syllabus (Page 2) - Modules 1 through 4", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("Module 1: Advanced Amortized Analysis (Weeks 1-2)", styles["SectionHeader"]))
    story.append(Paragraph("This module examines operations whose worst-case individual cost is expensive but whose average cost across a sequence of operations is guaranteed to be small. We analyze three foundational techniques: the <b>Aggregate Method</b> (computing T(n)/n), the <b>Accounting / Banker's Method</b> (assigning artificial amortized charges with banked credit tokens), and the <b>Potential Method</b>. In the Potential Method, a potential function &Phi;(D) maps data structure states to real numbers, where the amortized cost a_i is defined as: a_i = c_i + &Phi;(D_i) - &Phi;(D_{i-1}). Applications include dynamic table expansion and Fibonacci Heaps (O(1) amortized decrease-key).", styles["AcademicBody"]))

    story.append(Paragraph("Module 2: Network Flow & Matching Algorithms (Weeks 3-4)", styles["SectionHeader"]))
    story.append(Paragraph("Flow networks model conservation and capacity constraints across directed graphs G=(V,E). We cover the <b>Ford-Fulkerson method</b> and the augmenting path theorem. The <b>Edmonds-Karp algorithm</b> implements augmenting path searches using Breadth-First Search (BFS) to find the shortest augmenting path in terms of edge count, guaranteeing a polynomial upper bound runtime of <b>O(V * E^2)</b>, eliminating infinite cycling or exponential runtime on irrational capacities. We prove the foundational <b>Max-Flow Min-Cut Theorem</b>: the maximum value of an s-t flow equals the minimum capacity among all cuts separating source s from sink t. Applications to bipartite matching and edge-disjoint path routing are explored.", styles["AcademicBody"]))

    story.append(Paragraph("Module 3: Linear Programming and Duality Theory (Weeks 5-6)", styles["SectionHeader"]))
    story.append(Paragraph("Linear Programming (LP) solves the optimization of a linear objective function subject to linear inequality constraints. We formulate standard form: Maximize c^T x subject to Ax &le; b and x &ge; 0. We study the <b>Simplex Algorithm</b>, slack variables, and pivot operations. While worst-case exponential on Klee-Minty cubes, Simplex is practically efficient. We formally prove <b>Weak Duality</b> (for feasible x and y, c^T x &le; b^T y) and <b>Strong Duality</b> (if the primal has an optimal solution, the dual has an optimal solution, and their objective values coincide exactly). We introduce Complementary Slackness conditions.", styles["AcademicBody"]))

    story.append(Paragraph("Module 4: Randomized Algorithms & Probabilistic Analysis (Weeks 7-8)", styles["SectionHeader"]))
    story.append(Paragraph("Randomization provides simplicity and asymptotic speedup. We differentiate between <b>Las Vegas algorithms</b> (always correct, runtime is a random variable, e.g., Randomized Quicksort achieving expected <b>O(n log n)</b> time on arbitrary inputs) and <b>Monte Carlo algorithms</b> (runtime is deterministic, output is correct with high probability, e.g., Karger's Min-Cut). We study <b>Skip Lists</b>, achieving O(log n) expected search, insertion, and deletion using probabilistic height assignments with parameter p=0.5. We cover tail bounds: Markov's Inequality, Chebyshev's Inequality, and Chernoff bounds.", styles["AcademicBody"]))

    story.append(PageBreak())

    # PAGE 3
    story.append(Paragraph("CS601 Syllabus (Page 3) - Modules 5 through 7", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("Module 5: Approximation Algorithms for NP-Hard Problems (Weeks 9-10)", styles["SectionHeader"]))
    story.append(Paragraph("When an optimization problem is NP-hard, polynomial-time algorithms cannot guarantee exact global optimality unless P=NP. We study approximation algorithms with provable approximation ratio &alpha; &ge; 1. For the <b>Vertex Cover problem</b>, a simple greedy maximal matching heuristic yields a <b>2-approximation</b> algorithm running in O(V + E) time. For the <b>Metric Traveling Salesperson Problem (Metric TSP)</b> satisfying the triangle inequality, the Minimum Spanning Tree (MST) doubling heuristic achieves a 2-approximation, while <b>Christofides Algorithm</b> combines an MST with a minimum-weight perfect matching on odd-degree vertices to achieve a <b>1.5-approximation ratio</b>. We analyze the greedy Set Cover algorithm achieving a logarithmic ratio of H(n) = O(ln n).", styles["AcademicBody"]))

    story.append(Paragraph("Module 6: NP-Completeness Reductions & Intractability (Weeks 11-12)", styles["SectionHeader"]))
    story.append(Paragraph("Complexity class P consists of languages decidable in polynomial time by a deterministic Turing Machine. Class NP consists of decision problems verifiable in polynomial time. We prove the seminal <b>Cook-Levin Theorem</b> establishing that the Boolean Satisfiability problem (SAT) is NP-Complete. We teach formal polynomial-time reduction techniques: Circuit-SAT &le;_p 3-SAT, 3-SAT &le;_p CLIQUE, CLIQUE &le;_p INDEPENDENT SET, and INDEPENDENT SET &le;_p VERTEX COVER. We discuss co-NP, NP-Hardness, and the theoretical implications of the P vs NP millennium prize problem.", styles["AcademicBody"]))

    story.append(Paragraph("Module 7: Sublinear & Streaming Algorithms (Weeks 13-14)", styles["SectionHeader"]))
    story.append(Paragraph("Big data applications require processing massive continuous streams under strict poly-logarithmic memory constraints. We analyze the <b>Count-Min Sketch</b>, a probabilistic sublinear frequency estimation table using d hash functions and w = e/&epsilon; counters. Count-Min guarantees that with probability 1 - &delta;, frequency estimates satisfy: a_i &le; a_hat_i &le; a_i + &epsilon; ||a||_1. We also study the <b>Misra-Gries heavy hitters algorithm</b> finding elements with frequency greater than N/k in O(k) memory, and <b>Reservoir Sampling</b> (Algorithm R) uniformly sampling k items from an unbounded stream of unknown length N with exact probability k/N per item.", styles["AcademicBody"]))

    story.append(PageBreak())

    # PAGE 4
    story.append(Paragraph("CS601 Syllabus (Page 4) - Assessment, Policies & Schedule", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("5. Assessment Structure & Grade Weight Distribution", styles["SectionHeader"]))
    story.append(Paragraph("Final letter grades are calculated based on cumulative performance across four distinct components. There is no grading curve; standard absolute thresholds apply (A &ge; 90%, B &ge; 80%, C &ge; 70%, D &ge; 60%, F < 60%):", styles["AcademicBody"]))

    # Grading Table
    table_data = [
        [Paragraph("Assessment Component", styles["TableHeader"]), Paragraph("Weight (%)", styles["TableHeader"]), Paragraph("Frequency / Deadline", styles["TableHeader"]), Paragraph("Core Focus & Objectives", styles["TableHeader"])],
        [Paragraph("Problem Sets (5 Homeworks)", styles["TableCellBold"]), Paragraph("25%", styles["TableCell"]), Paragraph("Bi-weekly submissions", styles["TableCell"]), Paragraph("Rigorous written proofs, amortized analysis, and LP formulations.", styles["TableCell"])],
        [Paragraph("Midterm Examination", styles["TableCellBold"]), Paragraph("25%", styles["TableCell"]), Paragraph("Week 8 (In-Class, Closed Book)", styles["TableCell"]), Paragraph("Modules 1 to 4: Network Flow, Potential Functions, LP Duality, Randomization.", styles["TableCell"])],
        [Paragraph("Research / Implementation Project", styles["TableCellBold"]), Paragraph("20%", styles["TableCell"]), Paragraph("Milestone Week 10, Final Week 14", styles["TableCell"]), Paragraph("Implementation and empirical evaluation of streaming sketches or approximation algorithms.", styles["TableCell"])],
        [Paragraph("Final Comprehensive Examination", styles["TableCellBold"]), Paragraph("30%", styles["TableCell"]), Paragraph("Finals Week (Hall 4B)", styles["TableCell"]), Paragraph("Cumulative coverage across all 7 modules with emphasis on NP-reductions and approximation.", styles["TableCell"])]
    ]
    t = Table(table_data, colWidths=[130, 65, 125, 210])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#94a3b8")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))

    story.append(Paragraph("6. Late Submission Policy & Extensions", styles["SectionHeader"]))
    story.append(Paragraph("Deadlines for problem sets are strictly enforced at 11:59 PM on designated submission dates via the online course portal. A grace penalty of <b>10% per 24-hour window</b> is assessed for late homework up to a maximum cutoff of <b>72 hours (3 days)</b>. Assignments submitted beyond 72 hours receive a grade of 0. Each student is granted two (2) free 24-hour late passes for the entire semester, usable without penalty.", styles["AcademicBody"]))

    story.append(Paragraph("7. Office Hours & Student Accommodations", styles["SectionHeader"]))
    story.append(Paragraph("<b>Instructor Office Hours:</b> Tuesdays and Thursdays from 2:00 PM to 4:00 PM in Hall 4B (Room 412).<br/>"
                           "<b>TA Problem-Solving Clinics:</b> Wednesdays and Fridays 4:00 PM to 6:00 PM in Computer Lab 2.<br/>"
                           "<b>Disability Services:</b> Students with verified accommodations through the University Center for Student Disabilities must notify the instructor during the first two weeks of class to ensure testing accommodations (1.5x/2.0x time in quiet rooms) are coordinated.", styles["AcademicBody"]))

    doc.build(story)
    print(f"[+] Successfully built: {filepath}")

# -----------------------------------------------------------------------------
# Document 2: multimodal_deep_learning_theory.pdf (Equations & Tables)
# -----------------------------------------------------------------------------
def build_multimodal_dl_doc(filepath: str, styles):
    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    story = []

    # PAGE 1
    story.append(Paragraph("Mathematical Foundations of Attention and Transformer Architectures", styles["DocTitle"]))
    story.append(Paragraph("Scholarly Monograph | AI Research Series | Department of Computer Science", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("1. Scaled Dot-Product Attention Formulation", styles["SectionHeader"]))
    story.append(Paragraph("The transformer model replaces recurrence and convolution entirely with the self-attention mechanism. The core computational building block is the <b>Scaled Dot-Product Attention</b> function. Let Query matrix Q &isin; R^{n &times; d_k}, Key matrix K &isin; R^{m &times; d_k}, and Value matrix V &isin; R^{m &times; d_v}, where n represents sequence length of queries, m represents sequence length of keys/values, and d_k is the key dimensionality.", styles["AcademicBody"]))

    story.append(Paragraph("Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V", styles["FormulaBox"]))

    story.append(Paragraph("<b>The Role of the Scaling Factor sqrt(d_k):</b> The scaling factor 1 / sqrt(d_k) is mathematically essential. Assume the components of q and k are independent random variables with zero mean and unit variance &sigma;^2 = 1. Their dot product q &middot; k = &sum;_{i=1}^{d_k} q_i k_i has mean 0 and variance d_k. For large projection dimensions (e.g., d_k = 64 or 128), the magnitude of the dot products becomes extremely large. When fed into the softmax function, large inputs cause the softmax distribution to become extremely peaked (one-hot), driving softmax gradients to near zero (gradient saturation). Dividing by sqrt(d_k) rescales the variance back to 1.0, preserving healthy gradient flow during backpropagation.", styles["AcademicBody"]))

    story.append(Paragraph("2. Multi-Head Attention Mechanism", styles["SectionHeader"]))
    story.append(Paragraph("Rather than computing a single attention function with d_model dimensional queries, keys, and values, Multi-Head Attention projects the queries, keys, and values h times with distinct learned linear projections to dimensions d_k, d_k, and d_v respectively:", styles["AcademicBody"]))

    story.append(Paragraph("MultiHead(Q, K, V) = Concat(head_1, head_2, ..., head_h) * W^O<br/>"
                           "where head_i = Attention(Q * W_i^Q, K * W_i^K, V * W_i^V)", styles["FormulaBox"]))

    story.append(Paragraph("Here parameter matrices W_i^Q &isin; R^{d_model &times; d_k}, W_i^K &isin; R^{d_model &times; d_k}, W_i^V &isin; R^{d_model &times; d_v}, and W^O &isin; R^{h*d_v &times; d_model}. Multi-head attention allows the model to attend simultaneously to information from different representation subspaces at different positions. Typically, h=8 or 16 and d_k = d_v = d_model / h.", styles["AcademicBody"]))

    story.append(PageBreak())

    # PAGE 2
    story.append(Paragraph("Mathematical Foundations (Page 2) - Loss Functions & AdamW Optimization", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("3. Optimization Objectives & Label Smoothing Regularization", styles["SectionHeader"]))
    story.append(Paragraph("For sequence generation and token classification with vocabulary size V, models minimize the Categorical Cross-Entropy loss. To prevent overconfidence and calibrate predictive probabilities, we apply <b>Label Smoothing Regularization</b> with hyperparameter &epsilon; &isin; (0, 1). The target distribution y_k is smoothed across uniform distribution U(1/V):", styles["AcademicBody"]))

    story.append(Paragraph("y'_k = (1 - &epsilon;) * y_k + (&epsilon; / V)<br/>"
                           "Loss_{LS}(y, y_hat) = - &sum;_{k=1}^V y'_k * log(y_hat_k) = (1 - &epsilon;) * Loss_{CE} + &epsilon; * D_{KL}(U || y_hat)", styles["FormulaBox"]))

    story.append(Paragraph("4. The AdamW Optimization Algorithm (Decoupled Weight Decay)", styles["SectionHeader"]))
    story.append(Paragraph("Standard Adam with L2 weight decay regularizes weights by adding &lambda; &theta; directly to the gradient vector g_t before computing moment estimates. However, Loshchilov and Hutter (2019) demonstrated that in adaptive gradient algorithms, this couples weight decay to the second moment preconditioner v_t, leading to suboptimal regularization for parameters with large gradient history. <b>AdamW</b> decouples weight decay by subtracting &lambda; &eta; &theta;_{t-1} directly during parameter update:", styles["AcademicBody"]))

    story.append(Paragraph("m_t = &beta;_1 * m_{t-1} + (1 - &beta;_1) * g_t<br/>"
                           "v_t = &beta;_2 * v_{t-1} + (1 - &beta;_2) * g_t^2<br/>"
                           "m_hat_t = m_t / (1 - &beta;_1^t),   v_hat_t = v_t / (1 - &beta;_2^t)<br/>"
                           "&theta;_t = &theta;_{t-1} - &eta;_t * ( m_hat_t / (sqrt(v_hat_t) + &epsilon;) ) - &eta;_t * &lambda; * &theta;_{t-1}", styles["FormulaBox"]))

    story.append(Paragraph("Standard hyperparameters for stable LLM pretraining are: learning rate &eta; = 1e-4, first moment exponential decay &beta;_1 = 0.9, second moment exponential decay &beta;_2 = 0.999 or 0.95, epsilon &epsilon; = 1e-8, and decoupled weight decay factor &lambda; = 0.01.", styles["AcademicBody"]))

    story.append(PageBreak())

    # PAGE 3
    story.append(Paragraph("Mathematical Foundations (Page 3) - Architectural Benchmarking", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("5. Structural Comparison of Foundational Transformer Architectures", styles["SectionHeader"]))
    story.append(Paragraph("Modern language and multimodal retrieval architectures exhibit distinct trade-offs in parameter scaling, context capacity, positional encoding schemes, and computational complexity of attention. Table 1 summarizes the architectural configurations of key foundational models:", styles["AcademicBody"]))

    # Table 1: Model Architectures
    table1_data = [
        [Paragraph("Model Architecture", styles["TableHeader"]), Paragraph("Parameters", styles["TableHeader"]), Paragraph("Context Window", styles["TableHeader"]), Paragraph("Attention Type", styles["TableHeader"]), Paragraph("Positional Encoding", styles["TableHeader"]), Paragraph("Activation Function", styles["TableHeader"])],
        [Paragraph("BERT-Large", styles["TableCellBold"]), Paragraph("340M", styles["TableCell"]), Paragraph("512 tokens", styles["TableCell"]), Paragraph("Bidirectional Full", styles["TableCell"]), Paragraph("Learned Absolute", styles["TableCell"]), Paragraph("GELU", styles["TableCell"])],
        [Paragraph("RoBERTa-Large", styles["TableCellBold"]), Paragraph("355M", styles["TableCell"]), Paragraph("512 tokens", styles["TableCell"]), Paragraph("Bidirectional Full", styles["TableCell"]), Paragraph("Learned Absolute", styles["TableCell"]), Paragraph("GELU", styles["TableCell"])],
        [Paragraph("GPT-3 (Davinci)", styles["TableCellBold"]), Paragraph("175B", styles["TableCell"]), Paragraph("2048 tokens", styles["TableCell"]), Paragraph("Causal Masked", styles["TableCell"]), Paragraph("Learned Absolute", styles["TableCell"]), Paragraph("GELU", styles["TableCell"])],
        [Paragraph("LLaMA-2-7B", styles["TableCellBold"]), Paragraph("6.7B", styles["TableCell"]), Paragraph("4096 tokens", styles["TableCell"]), Paragraph("Causal Masked (GQA)", styles["TableCell"]), Paragraph("RoPE (Rotary)", styles["TableCell"]), Paragraph("SwiGLU", styles["TableCell"])],
        [Paragraph("Mistral-7B", styles["TableCellBold"]), Paragraph("7.3B", styles["TableCell"]), Paragraph("8192 tokens", styles["TableCell"]), Paragraph("Sliding Window (SWA)", styles["TableCell"]), Paragraph("RoPE (Rotary)", styles["TableCell"]), Paragraph("SwiGLU", styles["TableCell"])],
        [Paragraph("FlashAttention-2", styles["TableCellBold"]), Paragraph("N/A (Kernel)", styles["TableCell"]), Paragraph("32K - 64K", styles["TableCell"]), Paragraph("IO-Aware Tiling", styles["TableCell"]), Paragraph("Rotary / ALiBi", styles["TableCell"]), Paragraph("Hardware Tiled", styles["TableCell"])]
    ]
    t1 = Table(table1_data, colWidths=[95, 65, 80, 100, 100, 90])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f766e")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#94a3b8")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t1)
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Key Architectural Observations:</b>", styles["SubSectionHeader"]))
    story.append(Paragraph("&bull; <b>SwiGLU Activation:</b> LLaMA-2 replaces standard GELU with SwiGLU: SwiGLU(x) = Swish_{&beta;}(x W) &otimes; (x V), requiring 3 matrix multiplies per feedforward layer but offering superior gradient propagation.<br/>"
                           "&bull; <b>Rotary Position Embeddings (RoPE):</b> Unlike absolute position embeddings which fail when evaluated on sequences longer than pretraining, RoPE incorporates relative position by rotating query and key vectors in complex 2D subspaces with rotation matrix R_{&Theta;,m}^d.", styles["AcademicBody"]))

    story.append(PageBreak())

    # PAGE 4
    story.append(Paragraph("Mathematical Foundations (Page 4) - Empirical Benchmark Results", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("6. Downstream NLP & Reading Comprehension Benchmarks", styles["SectionHeader"]))
    story.append(Paragraph("We evaluated models across foundational language understanding benchmarks: Multi-Genre Natural Language Inference (MNLI), Question Natural Language Inference (QNLI), Stanford Sentiment Treebank (SST-2), and Stanford Question Answering Dataset (SQuAD v2.0). Table 2 presents fine-tuned evaluation accuracy and exact match scores:", styles["AcademicBody"]))

    # Table 2: Benchmark Scores
    table2_data = [
        [Paragraph("Evaluation Task", styles["TableHeader"]), Paragraph("Metric", styles["TableHeader"]), Paragraph("BERT-Base", styles["TableHeader"]), Paragraph("RoBERTa-Base", styles["TableHeader"]), Paragraph("DeBERTa-v3", styles["TableHeader"]), Paragraph("Proposed RAG+CE", styles["TableHeader"])],
        [Paragraph("MNLI (Matched)", styles["TableCellBold"]), Paragraph("Accuracy (%)", styles["TableCell"]), Paragraph("84.6%", styles["TableCell"]), Paragraph("87.6%", styles["TableCell"]), Paragraph("90.2%", styles["TableCell"]), Paragraph("91.8%", styles["TableCellBold"])],
        [Paragraph("QNLI (v2)", styles["TableCellBold"]), Paragraph("Accuracy (%)", styles["TableCell"]), Paragraph("90.5%", styles["TableCell"]), Paragraph("92.8%", styles["TableCell"]), Paragraph("94.1%", styles["TableCell"]), Paragraph("95.4%", styles["TableCellBold"])],
        [Paragraph("SST-2 (Sentiment)", styles["TableCellBold"]), Paragraph("Accuracy (%)", styles["TableCell"]), Paragraph("93.5%", styles["TableCell"]), Paragraph("94.8%", styles["TableCell"]), Paragraph("95.6%", styles["TableCell"]), Paragraph("96.2%", styles["TableCellBold"])],
        [Paragraph("SQuAD v2.0", styles["TableCellBold"]), Paragraph("Exact Match (EM)", styles["TableCell"]), Paragraph("74.2%", styles["TableCell"]), Paragraph("80.5%", styles["TableCell"]), Paragraph("85.1%", styles["TableCell"]), Paragraph("88.7%", styles["TableCellBold"])],
        [Paragraph("SQuAD v2.0", styles["TableCellBold"]), Paragraph("F1 Score (%)", styles["TableCell"]), Paragraph("81.8%", styles["TableCell"]), Paragraph("86.5%", styles["TableCell"]), Paragraph("90.4%", styles["TableCell"]), Paragraph("93.1%", styles["TableCellBold"])]
    ]
    t2 = Table(table2_data, colWidths=[110, 85, 80, 80, 85, 90])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#94a3b8")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t2)
    story.append(Spacer(1, 14))

    story.append(Paragraph("<b>Analysis and Findings:</b>", styles["SubSectionHeader"]))
    story.append(Paragraph("1. <b>Disentangled Attention in DeBERTa-v3:</b> DeBERTa-v3 represents each word using two separate vectors (content and position) and computes cross-attention using disentangled matrices. This delivers a substantial 4.6% boost in SQuAD v2.0 Exact Match over RoBERTa-Base.<br/>"
                           "2. <b>Proposed Hybrid RAG with Cross-Encoder (CE):</b> Coupling dense retrieval with a cross-encoder re-ranking stage establishes state-of-the-art reading comprehension fidelity, attaining <b>88.7% Exact Match</b> and <b>93.1% F1</b> on SQuAD v2.0 by eliminating false-positive distractor paragraphs from the prompt context.", styles["AcademicBody"]))

    doc.build(story)
    print(f"[+] Successfully built: {filepath}")

# -----------------------------------------------------------------------------
# Document 3: lecture_slides_vector_search_rag.pdf (Slide Deck - Landscape)
# -----------------------------------------------------------------------------
def build_slides_doc(filepath: str, styles):
    doc = SimpleDocTemplate(
        filepath,
        pagesize=landscape(letter),
        leftMargin=50,
        rightMargin=50,
        topMargin=40,
        bottomMargin=40
    )
    story = []

    # SLIDE 1
    story.append(Paragraph("Lecture 08: High-Dimensional Vector Search & Hybrid RAG Architectures", styles["SlideTitle"]))
    story.append(Paragraph("CS680: Modern Information Retrieval and Language Systems | Stanford / MIT Guest Series", styles["SlideSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#0284c7"), spaceAfter=20))
    story.append(Paragraph("<b>Lecturer:</b> Dr. Alexander Vance, Principal AI Systems Architect<br/>"
                           "<b>Date:</b> Autumn Semester 2026<br/>"
                           "<b>Core Agenda for Today:</b>", styles["SlideBody"]))
    story.append(Paragraph("&bull; 1. Semantic Search Dilemma: Lexical (BM25) vs. Dense Vector Representations", styles["SlideBullet"]))
    story.append(Paragraph("&bull; 2. Approximate Nearest Neighbor (ANN) Indexing: HNSW Graph vs. IVF-Flat", styles["SlideBullet"]))
    story.append(Paragraph("&bull; 3. Multi-Stage Retrieval & Reciprocal Rank Fusion (RRF) Algorithms", styles["SlideBullet"]))
    story.append(Paragraph("&bull; 4. Cross-Encoder Re-Ranking Pipeline & Noise Elimination", styles["SlideBullet"]))
    story.append(Paragraph("&bull; 5. The RAG Triad Evaluation: Groundedness, Relevance, and Citation Accuracy", styles["SlideBullet"]))
    story.append(Spacer(1, 40))
    story.append(Paragraph("<i>Slide 1 of 6 &bull; CS680 Lecture Series</i>", styles["AcademicBody"]))
    story.append(PageBreak())

    # SLIDE 2
    story.append(Paragraph("Slide 2: Lexical Search vs. Dense Semantic Search", styles["SlideTitle"]))
    story.append(Paragraph("Understanding the fundamental architectural trade-offs in candidate retrieval:", styles["SlideSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=15))

    story.append(Paragraph("<b>Lexical Retrieval (BM25 / Inverted Index):</b>", styles["SlideBody"]))
    story.append(Paragraph("&bull; <b>Strength:</b> Exact keyword precision; perfect for rare part numbers, error codes, and technical identifiers.", styles["SlideBullet"]))
    story.append(Paragraph("&bull; <b>Weakness:</b> Suffers from the <i>vocabulary mismatch problem</i>; fails on synonyms (e.g., 'acute myocardial infarction' vs 'heart attack').", styles["SlideBullet"]))

    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Dense Semantic Vector Retrieval (Bi-Encoders):</b>", styles["SlideBody"]))
    story.append(Paragraph("&bull; <b>Strength:</b> Projects text into 384 or 768-dimensional dense vector space; captures abstract semantic concepts and paraphrases.", styles["SlideBullet"]))
    story.append(Paragraph("&bull; <b>Weakness:</b> Loses token-level precision; can retrieve superficially similar but factually irrelevant text chunks.", styles["SlideBullet"]))

    story.append(Paragraph("<b>Key Engineering Principle:</b> Robust academic RAG systems must utilize <i>Hybrid Search</i> combining both dense vectors and sparse BM25 indices.", styles["SlideBody"]))
    story.append(Spacer(1, 30))
    story.append(Paragraph("<i>Slide 2 of 6 &bull; CS680 Lecture Series</i>", styles["AcademicBody"]))
    story.append(PageBreak())

    # SLIDE 3
    story.append(Paragraph("Slide 3: Vector Indexing: HNSW vs. IVF-Flat", styles["SlideTitle"]))
    story.append(Paragraph("Scalability considerations for Approximate Nearest Neighbor (ANN) search:", styles["SlideSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=15))

    story.append(Paragraph("<b>Hierarchical Navigable Small World (HNSW):</b>", styles["SlideBody"]))
    story.append(Paragraph("&bull; Multi-layer geometric graph structure; upper layers have sparse, long-range skip connections for rapid navigation.", styles["SlideBullet"]))
    story.append(Paragraph("&bull; Bottom layer contains dense, localized nearest neighbor connections.", styles["SlideBullet"]))
    story.append(Paragraph("&bull; <b>Search Complexity:</b> O(log N) average query time with near 99% recall.", styles["SlideBullet"]))
    story.append(Paragraph("&bull; <b>Trade-off:</b> Substantial RAM footprint (must store bidirectional graph edge lists in memory).", styles["SlideBullet"]))

    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Inverted File Index (IVF-Flat):</b>", styles["SlideBody"]))
    story.append(Paragraph("&bull; Partitions vector space into K Voronoi cells via K-Means clustering.", styles["SlideBullet"]))
    story.append(Paragraph("&bull; Queries only search vectors inside the nearest n_probe Voronoi centroids.", styles["SlideBullet"]))
    story.append(Paragraph("&bull; <b>Trade-off:</b> Lower memory and fast build time, but lower recall if n_probe is configured too small.", styles["SlideBullet"]))
    story.append(Spacer(1, 25))
    story.append(Paragraph("<i>Slide 3 of 6 &bull; CS680 Lecture Series</i>", styles["AcademicBody"]))
    story.append(PageBreak())

    # SLIDE 4
    story.append(Paragraph("Slide 4: Multi-Stage Retrieval & Reciprocal Rank Fusion (RRF)", styles["SlideTitle"]))
    story.append(Paragraph("How to combine disparate score distributions without manual weighting:", styles["SlideSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=15))

    story.append(Paragraph("In hybrid retrieval, BM25 returns unbounded BM25 scores (e.g. [0, 45]), whereas vector databases return Cosine Similarity in [0, 1]. Directly summing these raw scores produces disastrous calibration bias.", styles["SlideBody"]))
    story.append(Paragraph("<b>Reciprocal Rank Fusion (RRF) Formula:</b>", styles["SlideBody"]))
    story.append(Paragraph("RRF_Score(d &isin; D) = &sum;_{m &isin; M} ( 1 / (k + rank_m(d)) )", styles["FormulaBox"]))

    story.append(Paragraph("<b>Why is the smoothing constant k set to 60?</b><br/>"
                           "Empirical studies by Cormack et al. proved that k = 60 prevents top-ranked items from one retriever from completely dominating the ranking if they are absent or low-ranked in another retriever. It stabilizes ranking variance across noisy academic queries.", styles["SlideBody"]))
    story.append(Spacer(1, 35))
    story.append(Paragraph("<i>Slide 4 of 6 &bull; CS680 Lecture Series</i>", styles["AcademicBody"]))
    story.append(PageBreak())

    # SLIDE 5
    story.append(Paragraph("Slide 5: Neural Cross-Encoder Re-Ranking Pipeline", styles["SlideTitle"]))
    story.append(Paragraph("The secret to eliminating 25-35% false-positive noise in the top-K context:", styles["SlideSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=15))

    story.append(Paragraph("<b>Bi-Encoder (First Stage Retrieval):</b><br/>"
                           "&bull; Query and documents are embedded into vector space completely separately: E(q) and E(d).<br/>"
                           "&bull; Cosine similarity measures angle between independent vectors. Fast (&lt;5ms) but cannot capture token-level interaction.", styles["SlideBody"]))

    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Cross-Encoder (Second Stage Re-ranking):</b><br/>"
                           "&bull; Concatenates query and candidate chunk into a single sequence: [CLS] query [SEP] chunk [SEP].<br/>"
                           "&bull; Full all-to-all cross-attention: every token in the query attends to every token in the candidate text.<br/>"
                           "&bull; <b>Outcome:</b> Significantly higher Mean Reciprocal Rank (MRR) and Context Precision.", styles["SlideBody"]))
    story.append(Spacer(1, 30))
    story.append(Paragraph("<i>Slide 5 of 6 &bull; CS680 Lecture Series</i>", styles["AcademicBody"]))
    story.append(PageBreak())

    # SLIDE 6
    story.append(Paragraph("Slide 6: Quantitative Evaluation: The RAG Triad", styles["SlideTitle"]))
    story.append(Paragraph("How to defend your system during viva voce and project defense:", styles["SlideSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=15))

    story.append(Paragraph("Examiners test whether your RAG pipeline produces trustworthy, verifiable answers:", styles["SlideBody"]))
    story.append(Paragraph("&bull; <b>1. Context Precision / Relevance:</b> Does the top-K retrieved chunk context contain only pertinent information without irrelevant distractor chunks?", styles["SlideBullet"]))
    story.append(Paragraph("&bull; <b>2. Faithfulness (Anti-Hallucination):</b> Can every single factual statement in the generated answer be directly inferred from the retrieved chunks? Penalizes external LLM parametric memory hallucination.", styles["SlideBullet"]))
    story.append(Paragraph("&bull; <b>3. Answer Relevance:</b> Does the answer directly address the user's inquiry without wandering or evasiveness?", styles["SlideBullet"]))
    story.append(Paragraph("&bull; <b>4. Citation Provenance Accuracy:</b> Do the generated citation tags (e.g. '[Lecture 08, Slide 4]') point to the exact slide/page that verified the claim?", styles["SlideBullet"]))
    story.append(Spacer(1, 30))
    story.append(Paragraph("<i>Slide 6 of 6 &bull; CS680 Lecture Series</i>", styles["AcademicBody"]))

    doc.build(story)
    print(f"[+] Successfully built: {filepath}")

# -----------------------------------------------------------------------------
# Document 4: distributed_systems_consensus_paper.pdf (Core Systems)
# -----------------------------------------------------------------------------
def build_distributed_systems_doc(filepath: str, styles):
    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    story = []

    # PAGE 1
    story.append(Paragraph("Consensus, Fault Tolerance, and Invariants in Distributed Systems", styles["DocTitle"]))
    story.append(Paragraph("Systems Research Monograph | Distributed Computing Laboratory", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("1. Fundamental Limits: The FLP Impossibility Result", styles["SectionHeader"]))
    story.append(Paragraph("In distributed systems, achieving consensus among independent computing nodes is essential for transaction processing, state machine replication, and distributed locks. However, Fischer, Lynch, and Paterson (FLP, 1985) proved the foundational <b>FLP Impossibility Theorem</b>: In an asynchronous network model, no deterministic consensus protocol can guarantee both safety (nothing bad happens) and liveness (eventually something good happens) in the presence of even a single unannounced crash failure. Practical protocols (Paxos, Raft) bypass FLP by adopting partial synchrony models with randomized election timeouts.", styles["AcademicBody"]))

    story.append(Paragraph("2. The CAP Theorem & PACELC Classification", styles["SectionHeader"]))
    story.append(Paragraph("Eric Brewer formulated the <b>CAP Theorem</b>, formally proved by Seth Gilbert and Nancy Lynch (2002). A distributed data store can simultaneously provide at most two out of three guarantees: <b>Consistency</b> (every read receives the most recent write or an error), <b>Availability</b> (every non-failing node returns a non-error response), and <b>Partition Tolerance</b> (the system continues to operate despite network partitions dropping arbitrary messages). Because network partitions are physical realities of networked hardware, distributed systems must trade off Consistency (CP systems, e.g., Spanner, HBase) vs Availability (AP systems, e.g., Cassandra, Dynamo) when a partition occurs.", styles["AcademicBody"]))
    
    story.append(Paragraph("Daniel Abadi extended CAP via the <b>PACELC Theorem</b>: If there is a Partition (P), trade off Availability (A) and Consistency (C); Else (E), trade off Latency (L) and Consistency (C).", styles["AcademicBody"]))

    story.append(PageBreak())

    # PAGE 2
    story.append(Paragraph("Distributed Systems (Page 2) - Consensus Protocols: Paxos vs. Raft", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("3. Paxos Consensus Protocol", styles["SectionHeader"]))
    story.append(Paragraph("Designed by Leslie Lamport, Paxos reaches consensus on a single value through two phases: Phase 1 (Prepare / Promise) and Phase 2 (Accept / Accepted). A proposer broadcasts a Prepare request with proposal number n. Acceptors promise not to accept proposals with numbers less than n and return the highest-numbered proposal they have already accepted. If a majority of acceptors promise, the proposer sends an Accept request with proposal number n and value v. While mathematically elegant, Multi-Paxos is notoriously difficult to understand and implement correctly in production.", styles["AcademicBody"]))

    story.append(Paragraph("4. The Raft Consensus Protocol: Understandability by Design", styles["SectionHeader"]))
    story.append(Paragraph("Ongaro and Ousterhout designed <b>Raft</b> to be understandable and equivalent in fault tolerance to Paxos. Raft decomposes consensus into three independent subproblems: <b>Leader Election</b>, <b>Log Replication</b>, and <b>Safety</b>. Raft operates in discrete terms. In Leader Election, nodes use randomized election timeouts (typically <b>150ms to 300ms</b>) to prevent split-vote deadlocks. A candidate becomes leader upon receiving votes from a majority (quorum &ge; N/2 + 1) of nodes. The leader accepts log commands from clients, appends them to its log, and issues AppendEntries RPCs. Once an entry is committed by a majority, the leader applies it to its local state machine.", styles["AcademicBody"]))

    story.append(PageBreak())

    # PAGE 3
    story.append(Paragraph("Distributed Systems (Page 3) - Concurrency Control & Deadlocks", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("5. Coffman Conditions for Deadlock", styles["SectionHeader"]))
    story.append(Paragraph("Edward G. Coffman Jr. identified four necessary and sufficient conditions that must hold simultaneously for a system deadlock to occur in resource allocation:", styles["AcademicBody"]))
    story.append(Paragraph("&bull; <b>1. Mutual Exclusion:</b> At least one resource must be held in a non-shareable mode; only one process can use the resource at any given moment.<br/>"
                           "&bull; <b>2. Hold and Wait:</b> A process must currently hold at least one resource while requesting additional resources held by other processes.<br/>"
                           "&bull; <b>3. No Preemption:</b> Resources cannot be forcibly seized; a resource can only be released voluntarily by the holding process after completing its task.<br/>"
                           "&bull; <b>4. Circular Wait:</b> A closed chain of processes {P_0, P_1, ..., P_n} exists such that P_0 waits for a resource held by P_1, P_1 waits for P_2, and P_n waits for P_0.", styles["AcademicBody"]))
    story.append(Paragraph("<b>Deadlock Prevention Strategy:</b> If any single Coffman condition is eliminated (e.g., imposing a strict global ordering on resource acquisition to eliminate circular wait), deadlocks are mathematically impossible.", styles["AcademicBody"]))

    story.append(PageBreak())

    # PAGE 4
    story.append(Paragraph("Distributed Systems (Page 4) - Distributed Transactions", styles["DocSubtitle"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=10))

    story.append(Paragraph("6. Atomic Distributed Commit: Two-Phase Commit (2PC)", styles["SectionHeader"]))
    story.append(Paragraph("Two-Phase Commit coordinates atomic transactions across multiple participating database shards. A designated Coordinator orchestrates two phases:", styles["AcademicBody"]))
    story.append(Paragraph("&bull; <b>Phase 1 (Prepare):</b> Coordinator sends PREPARE message to all cohorts. Cohorts execute the transaction locally, write undo/redo logs to non-volatile disk, and reply VOTE_COMMIT or VOTE_ABORT.<br/>"
                           "&bull; <b>Phase 2 (Commit):</b> If all cohorts vote VOTE_COMMIT, Coordinator writes GLOBAL_COMMIT to its log and sends COMMIT to cohorts. If any cohort votes VOTE_ABORT or times out, Coordinator writes GLOBAL_ABORT and instructs all cohorts to rollback.", styles["AcademicBody"]))
    story.append(Paragraph("<b>The Blocking Limitation of 2PC:</b> 2PC is a blocking protocol. If the coordinator crashes after cohorts enter the PREPARED state, cohorts are blocked indefinitely holding database locks until the coordinator recovers.", styles["AcademicBody"]))

    doc.build(story)
    print(f"[+] Successfully built: {filepath}")

def main():
    styles = get_custom_styles()
    
    syllabus_path = os.path.join(DOCS_DIR, "cs601_advanced_algorithms_syllabus.pdf")
    build_syllabus_doc(syllabus_path, styles)

    dl_path = os.path.join(DOCS_DIR, "multimodal_deep_learning_theory.pdf")
    build_multimodal_dl_doc(dl_path, styles)

    slides_path = os.path.join(DOCS_DIR, "lecture_slides_vector_search_rag.pdf")
    build_slides_doc(slides_path, styles)

    dist_path = os.path.join(DOCS_DIR, "distributed_systems_consensus_paper.pdf")
    build_distributed_systems_doc(dist_path, styles)

    print("\n[OK] All 4 benchmark academic documents generated successfully in:", DOCS_DIR)

if __name__ == "__main__":
    main()
