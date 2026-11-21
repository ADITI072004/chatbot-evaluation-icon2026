# Commercial Chatbot Evaluation: English vs. Hindi Empirical Benchmark

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Conference](https://img.shields.io/badge/ICON-2026-brightgreen.svg)](docs/ICON2026_CameraReady_Paper.pdf)
[![Paper ID](https://img.shields.io/badge/Paper%20ID-62-purple.svg)](docs/ICON2026_CameraReady_Paper.pdf)

This repository contains the complete empirical dataset, replication scripts, high-resolution figures, and camera-ready documentation for the research paper:

> **Evaluating Deployed Conversational Assistants Across English and Hindi: Empirical Discrepancies, Latency Dynamics, and Error Typologies in Commercial Indian-Language NLP**  
> **Authors**: Aditi Mishra and Deepti Vidyarthi  
> **Affiliation**: Department of Computer Science and Engineering, Defence Institute of Advanced Technology (DIAT), DRDO, Pune, India  
> **Conference**: 22nd International Conference on Natural Language Processing (ICON 2026)  
> **Track**: Track 22ICON2026 | **Paper ID**: 62  

---

## Abstract
Commercial conversational assistants powered by Large Language Models (LLMs) are widely deployed across linguistically diverse populations. However, empirical benchmarking often prioritizes high-resource Western languages, obscuring sharp cross-lingual performance asymmetries in Indic settings. This paper reports a controlled empirical audit of five prominent conversational systems—**Perplexity AI, ChatGPT-4o, Microsoft Copilot, Claude 3.5 Sonnet, and Google Gemini 1.5 Pro**—evaluated synchronously across **100 curated prompts (50 English, 50 Hindi)** spanning 10 functional task families ($N = 500$ generations). 

Through paired inferential statistics, multi-metric similarity matrices (TF-IDF cosine, sequence edit distance, character 13-gram overlap, and word trigrams), and a qualitative error taxonomy, we uncover four significant phenomena:
1. **Severe Cross-Lingual Verbosity Contraction**: Assistants lose up to 58.0% of their word volume and 66.7% of character length in Hindi relative to English prompt counterparts.
2. **Loss of Latency Differentiation**: While English shows pronounced latency divergence (Perplexity averaging 8.26s due to search-augmented overhead, $p < 10^{-5}$), Hindi latency collapses into an undifferentiated cluster (5.08s–5.50s, $p > 0.19$).
3. **Backend Coupling Anomaly**: A striking structural convergence exists between Perplexity and Copilot in English (0.781 TF-IDF cosine, 24 near-duplicate responses), which dissolves in Hindi (0.458 cosine, zero identical outputs).
4. **Asymmetric Error Typology**: Hindi generations suffer 2.58x higher failure frequency (62 observed defects vs. 24 in English), dominated by translation artifacts, ungrammatical code-mixing, and hallucinated cultural entities.

---

## Key Empirical Findings

### 1. Inferential Latency Dynamics ($N = 50$ per language)

| Comparison Pair | Language | Pplx Mean (s) | Rival Mean (s) | Diff (s) | Paired $t$-stat | $p$-value | Significance ($\alpha=0.01$) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Perplexity vs Claude | English | 8.26 | 5.03 | +3.23 | 8.01 | $1.87 \times 10^{-10}$ | **Significant** |
| Perplexity vs ChatGPT | English | 8.26 | 5.86 | +2.40 | 5.25 | $3.25 \times 10^{-6}$ | **Significant** |
| Perplexity vs Gemini | English | 8.26 | 3.97 | +4.30 | 11.11 | $5.51 \times 10^{-15}$ | **Significant** |
| Perplexity vs Copilot | English | 8.26 | 3.31 | +4.95 | 13.04 | $1.50 \times 10^{-17}$ | **Significant** |
| Perplexity vs Claude | Hindi | 5.50 | 5.29 | +0.21 | 0.46 | 0.648 | Not Significant |
| Perplexity vs ChatGPT | Hindi | 5.50 | 5.08 | +0.42 | 0.87 | 0.387 | Not Significant |
| Perplexity vs Gemini | Hindi | 5.50 | 5.19 | +0.31 | 0.69 | 0.495 | Not Significant |
| Perplexity vs Copilot | Hindi | 5.50 | 4.90 | +0.60 | 1.33 | 0.191 | Not Significant |

### 2. Multi-Metric Similarity Matrix (10 Pairwise Comparisons)

| Model Pair | English Cosine | English Edit Sim | English 13-g Jaccard | English Near-Duplicates | Hindi Cosine | Hindi Edit Sim | Hindi 13-g Jaccard | Hindi Exact Matches |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Claude vs ChatGPT | 0.558 | 0.254 | 0.122 | 4 | 0.443 | 0.347 | 0.104 | 1 |
| Claude vs Gemini | 0.609 | 0.176 | 0.089 | 2 | 0.415 | 0.214 | 0.051 | 0 |
| Claude vs Perplexity | 0.621 | 0.246 | 0.133 | 3 | 0.528 | 0.324 | 0.109 | 2 |
| Claude vs Copilot | 0.610 | 0.229 | 0.133 | 3 | 0.504 | 0.400 | 0.103 | 0 |
| ChatGPT vs Gemini | 0.518 | 0.178 | 0.081 | 1 | 0.344 | 0.179 | 0.038 | 0 |
| ChatGPT vs Perplexity | 0.604 | 0.318 | 0.175 | 4 | 0.538 | 0.433 | 0.182 | 2 |
| ChatGPT vs Copilot | 0.562 | 0.276 | 0.144 | 1 | 0.401 | 0.371 | 0.097 | 0 |
| Gemini vs Perplexity | 0.567 | 0.183 | 0.102 | 2 | 0.445 | 0.245 | 0.056 | 0 |
| Gemini vs Copilot | 0.549 | 0.160 | 0.093 | 1 | 0.331 | 0.222 | 0.034 | 0 |
| **Perplexity vs Copilot** | **0.781** | **0.585** | **0.500** | **24** | **0.458** | **0.362** | **0.084** | **0** |

### 3. Cross-Lingual Verbosity Contraction

| Model | English Mean Words | Hindi Mean Words | Word Shift (%) | English Mean Chars | Hindi Mean Chars | Char Shift (%) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Claude | 156.3 | 65.6 | **-58.0%** | 1045.0 | 348.4 | **-66.7%** |
| ChatGPT | 47.2 | 33.6 | **-29.0%** | 318.7 | 174.2 | **-45.3%** |
| Gemini | 116.6 | 125.4 | +7.5% | 749.4 | 649.6 | **-13.3%** |
| Perplexity | 79.5 | 64.0 | **-19.4%** | 529.8 | 330.7 | **-37.6%** |
| Copilot | 68.4 | 35.1 | **-48.7%** | 462.5 | 194.1 | **-58.0%** |

---

## Repository Structure

```text
chatbot-evaluation-icon2026/
├── README.md                                  # Master repository documentation (this file)
├── LICENSE                                    # Open-source MIT License
├── requirements.txt                           # Python package dependencies
├── .gitignore                                 # Git exclusion rules
├── run_all_evaluations.py                     # One-click end-to-end replication script
│
├── data/                                      # Experimental datasets and evaluation corpora
│   ├── README.md                              # Detailed data dictionary and schema
│   ├── benchmark_100_prompts.xlsx             # 100 curated prompts across 10 functional families
│   ├── chatbot_responses_500_raw.xlsx         # Raw response captures across all 5 models
│   ├── responses_500_complete_tidy.csv        # 515-row long-form tidy evaluation dataset
│   ├── english_responses_50_prompts.csv       # Wide format English test set
│   ├── hindi_responses_50_prompts.csv         # Wide format Hindi test set
│   └── comprehensive_metrics_and_statistical_tests.xlsx # 7-sheet statistical master workbook
│
├── src/                                       # Modular Python evaluation codebase
│   ├── __init__.py                            # Package initializer
│   ├── evaluate_similarity.py                 # Cosine, Levenshtein, n-gram Jaccard implementations
│   └── statistical_tests.py                   # Paired t-tests, Wilcoxon tests, Cohen's d, verbosity
│
├── figures/                                   # High-resolution vector/raster publication charts
│   ├── figure1_latency_compression.png        # Response latency boxplots across languages
│   ├── figure2_similarity_composite.png       # 2-panel pairwise similarity heatmaps
│   ├── figure3_verbosity_contraction.png      # Word & character count contraction comparison
│   └── figure4_error_typology.png             # Qualitative failure breakdown by error type
│
└── docs/                                      # Complete conference submission documents
    ├── ICON2026_CameraReady_Paper.pdf         # Final 9-page camera-ready paper (ACL format)
    ├── ICON2026_CameraReady_Paper.docx        # Editable camera-ready manuscript
    ├── Author_Response_to_Reviewers.pdf       # Point-by-point reviewer rebuttal
    ├── Summary_of_Changes_and_Revisions.pdf   # Complete revision changelog
    ├── Graphical_Evidence_Dossier.pdf         # Visual chart documentation & data logs
    ├── Benchmark_100_Prompts_Corpus.pdf       # Complete bilingual prompt dossier
    └── Verbatim_Transcripts_and_Failure_Modes.pdf # Qualitative defect transcript dossier
```

---

## Replication Quickstart

### 1. Clone & Set Up Environment
```bash
git clone https://github.com/aditimishra-nlp/chatbot-evaluation-icon2026.git
cd chatbot-evaluation-icon2026

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Full Reproduction Pipeline
Execute the master script to reproduce all statistical tables and metrics reported in the paper:
```bash
python run_all_evaluations.py
```

### 3. Run Standalone Modules
To run similarity computations or statistical tests independently:
```bash
# Evaluate multi-metric similarity matrices:
python -m src.evaluate_similarity

# Evaluate inferential tests and verbosity:
python -c "from src.statistical_tests import run_latency_tests; print(run_latency_tests('data/english_responses_50_prompts.csv'))"
```

---

## Citation
If you use this benchmark dataset, code, or findings in your research, please cite our ICON 2026 publication:

```bibtex
@inproceedings{mishra-vidyarthi-2026-evaluating,
    title = "Evaluating Deployed Conversational Assistants Across English and Hindi: Empirical Discrepancies, Latency Dynamics, and Error Typologies in Commercial Indian-Language {NLP}",
    author = "Mishra, Aditi and Vidyarthi, Deepti",
    booktitle = "Proceedings of the 22nd International Conference on Natural Language Processing (ICON 2026)",
    month = "December",
    year = "2026",
    address = "Pune, India",
    publisher = "NLP Association of India (NLPAI)",
    pages = "1--9",
    url = "https://icon2026.org/papers/paper-62.pdf"
}
```

---

## License
The code in this repository is licensed under the [MIT License](LICENSE). The dataset files and documentation are provided for academic research and reproducibility.
