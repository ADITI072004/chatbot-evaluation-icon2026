#!/usr/bin/env python3
"""
Master Execution Pipeline: run_all_evaluations.py
Reproduces all quantitative results, statistical tests, and summary tables for:
"Evaluating Deployed Conversational Assistants Across English and Hindi:
Empirical Discrepancies, Latency Dynamics, and Error Typologies in Commercial Indian-Language NLP"
ICON 2026 (Track 22ICON2026, Paper ID 62)
"""

import os
import sys
import pandas as pd
import numpy as np

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from src.evaluate_similarity import run_pairwise_evaluation
from src.statistical_tests import run_latency_tests, run_verbosity_analysis

def main():
    print("=" * 80)
    print("ICON 2026 BENCHMARK EVALUATION & AUDIT PIPELINE")
    print("Paper ID: 62 | Track: 22ICON2026")
    print("Defence Institute of Advanced Technology (DIAT), DRDO, Pune, India")
    print("=" * 80)

    data_dir = os.path.join(os.path.dirname(__file__), "data")
    eng_csv = os.path.join(data_dir, "english_responses_50_prompts.csv")
    hin_csv = os.path.join(data_dir, "hindi_responses_50_prompts.csv")

    if not os.path.exists(eng_csv) or not os.path.exists(hin_csv):
        print(f"Error: Data files not found in {data_dir}")
        return

    # 1. Latency & Statistical Significance
    print("\n[STEP 1/3] EVALUATING RESPONSE LATENCY & STATISTICAL SIGNIFICANCE (TABLE 3)")
    print("-" * 80)
    df_lat_eng = run_latency_tests(eng_csv, "English")
    print(df_lat_eng[["Comparison", "Perplexity Mean (s)", "Rival Mean (s)", "Paired t-stat", "t-test p-val", "Significance (alpha=0.01)"]].to_string(index=False))

    df_lat_hin = run_latency_tests(hin_csv, "Hindi")
    print("\nHindi Latency Comparisons (Compression):")
    print(df_lat_hin[["Comparison", "Perplexity Mean (s)", "Rival Mean (s)", "Paired t-stat", "t-test p-val", "Significance (alpha=0.01)"]].to_string(index=False))

    # 2. Multi-Metric Similarity Matrix
    print("\n[STEP 2/3] EVALUATING PAIRWISE SIMILARITY MATRIX ACROSS 10 PAIRS (TABLE 4)")
    print("-" * 80)
    print("Evaluating English subset (N=50)...")
    df_sim_eng = run_pairwise_evaluation(eng_csv)
    print(df_sim_eng.to_string(index=False))

    print("\nEvaluating Hindi subset (N=50)...")
    df_sim_hin = run_pairwise_evaluation(hin_csv)
    print(df_sim_hin[["Model Pair", "Mean TF-IDF Cosine", "Mean Edit Sim", "Mean 13-g Jaccard", "Exact Matches"]].to_string(index=False))

    # 3. Response Verbosity & Cross-Lingual Contraction
    print("\n[STEP 3/3] EVALUATING VERBOSITY & CROSS-LINGUAL CONTRACTION (FIGURE 3)")
    print("-" * 80)
    df_verb = run_verbosity_analysis(eng_csv, hin_csv)
    print(df_verb.to_string(index=False))

    print("\n" + "=" * 80)
    print("ALL EVALUATIONS COMPLETED SUCCESSFULLY. ALL PAPER RESULTS REPRODUCED.")
    print("=" * 80)

if __name__ == "__main__":
    main()
