# Quantum-Kernel-Molecular-Classification

Comparing classical graph kernels and quantum-inspired embeddings for molecular classification — a project by Team The Cats Cradle.

## QPoland Global Quantum Hackathon 2025
18-Oct-2025 to 26-Oct-2025  
https://www.qaif.org/contests/qpoland-global-quantum-hackathon 

## Overview
This repository implements and evaluates classical graph-kernel methods and a quantum-inspired (Trotterized quantum walk) kernel for molecular and protein graph classification. The goal is to compare classical approaches (Weisfeiler–Lehman, shortest-path, RBF/linear/polynomial kernels) with scalable quantum-walk-based embeddings that can be simulated classically or executed on quantum backends via QURI Parts.

Innovation: fixing qubit-scaling issues by using ego-graph decomposition to drastically reduce required qubit count while still capturing functional-group topology effects; this enables efficient, accurate feature extraction from molecular graphs and therefore improves classification performance.

## Table of contents
- Getting started
- Datasets
- Implementation overview
- Evaluation protocol
- Key results
- Team (Key contributors)
- Trimmed references
- Contact

## Getting started
Clone and install dependencies:
```bash
git clone https://github.com/Dr-Sushant/Quantum-Kernel-Molecular-Classification.git
cd Quantum-Kernel-Molecular-Classification
pip install -r requirements.txt
jupyter notebook
```

Quick run (examples and notebooks are provided under the notebooks/ directory):
- notebooks/experiment_pipeline.ipynb — end-to-end training and evaluation on example datasets
- notebooks/quantum_embeddings_demo.ipynb — demo of the Trotterized quantum-walk embedding pipeline

## Datasets
Common benchmark graph datasets used in experiments:
- AIDS — HIV activity screening (~2000 compounds)
- PROTEINS — Protein enzyme classification (~1113 graphs)
- NCI1 — Anti-cancer compound activity (~4110 compounds)
- PTC-MR — Carcinogenicity prediction (~344 compounds)
- MUTAG — Mutagenicity prediction (~188 compounds)

(See data/ or notebooks/ for dataset download and preprocessing scripts.)

## Implementation overview
- extract_ego_graphs(): Ego-graph decomposition to allow processing large graphs with limited qubit budgets.
- wl_subtree_kernel(): Weisfeiler–Lehman subtree kernel implementation.
- shortest_path_kernel(): Shortest-path kernel using NetworkX shortest-path statistics.
- QuantumWalkEmbedding / ScalableQuantumWalkEmbedding: Classes to build Trotterized quantum-walk embeddings; includes classical simulation fallbacks.
- fidelity_kernel(): Uses quantum-state fidelity to build Gram matrices from embeddings.
- Utilities: mixing_matrix_quri_circuit(), build_trotter_circuit_for_graph(), trotterize_positions_amplitude(), quantum_state_fidelity().

## Evaluation protocol
- 10-fold stratified cross-validation.
- Classifier: SVM (scikit-learn) with kernel matrices supplied from each method.
- Metrics: Accuracy and F1-score (macro and/or weighted depending on dataset balance).
- Repeats: Report averages and standard deviations across folds (and random seeds where applicable).

## Key results (summary)
See notebooks/experiment_pipeline.ipynb and results/ for full logs and per-dataset numbers. Example summary table:

| Kernel Type      | Accuracy (avg) | F1-score (avg) | Notes |
|------------------|----------------|----------------|-------|
| WL Kernel        | TBD            | TBD            | Baseline classical |
| Shortest-Path    | TBD            | TBD            | Path-based baseline |
| Quantum-Inspired | TBD            | TBD            | Trotterized quantum-walk embeddings; scalable via ego-graphs |

(Replace "TBD" with numeric results from notebooks/experiment_pipeline.ipynb; results vary by dataset and hyperparameters.)

## Team — Key contributors

| Name                  | Discord Handle         | Role / Contribution |
|-----------------------|------------------------|---------------------|
| Dr. Sushant Tapase    | @Dr-Sushant            | - |
| Amon Koike            | @thedaemon_AK         | -|
| Jajapuram Shiva  Sai  | @frosty               | - |
| Ramesh Makwana        | @Ramesh Makwana       | - |

## references(selected) 

-------------
1. QURI Parts — QunaSys Inc. — https://github.com/QunaSys/quri-parts (Framework used for circuits and simulation.)

2. Xing Ai, Luzhe Sun, Junchi Yan, Zhihong Zhang, Edwin R. Hancock — "Towards Quantum Graph Neural Networks: An Ego-Graph Learning Approach" — arXiv:2201.05158. (Inspiration for ego-graph decomposition and scalable processing.)

3. N. Shervashidze et al. — "Weisfeiler-Lehman Graph Kernels" — JMLR, 2011. (WL-subtree kernel.)

4. V. Havlíček et al. — "Supervised Learning with Quantum-Enhanced Feature Spaces" — Nature, 2019. (Quantum feature maps / QSVM.)

5. Andrew M. Childs — "Universal Computation by Quantum Walk" — Phys. Rev. Lett., 2009. (Quantum-walk foundations.)

6. Seth Lloyd — "Universal Quantum Simulators" — Science, 1996. (Trotter-Suzuki decomposition.)
-------------

