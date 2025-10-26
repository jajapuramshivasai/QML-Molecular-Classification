# Quantum-Kernel-Molecular-Classification

Comparing classical graph kernels and quantum-inspired embeddings for molecular classification — a project by Team The Cats Cradle.

## QPoland Global Quantum Hackathon 2025
18-Oct-2025 to 26-Oct-2025  
https://www.qaif.org/contests/qpoland-global-quantum-hackathon 

## Overview
This repository implements and evaluates classical graph kernel methods alongside a quantum-inspired feature map based on Quantum Walk (QW) principles for molecular and protein graph classification. The project compares established classical approaches (Weisfeiler-Lehman, Shortest-Path) with novel quantum-inspired methods (QURI Ego-QW, CTQW) using Support Vector Machines (SVMs) with an RBF kernel. The innovation lies in leveraging ego-graph decomposition and quantum-inspired techniques to address qubit-scaling issues, enabling efficient feature extraction that enhances classification performance on molecular structures.

## Table of Contents
- Getting Started
- Datasets
- Implementation Overview
- Evaluation Protocol
- Key Results
- Team (Key Contributors)
- Trimmed References
- Contact

## Getting Started
Clone and install dependencies:
```bash
git clone https://github.com/jajapuramshivasai/QML-Molecular-Classification.git
cd Quantum-Kernel-Molecular-Classification
pip install -r requirements.txt
jupyter notebook
```

Quick run (examples and notebooks are provided under the notebooks/ directory):
- notebooks/sub_main.ipynb — End-to-end training and evaluation on benchmark datasets
- notebooks/quantum_embeddings_demo.ipynb — Demo of the quantum-inspired embedding pipeline

## Datasets
Standard benchmark graph datasets used in experiments:
- AIDS — HIV activity screening (~2000 compounds, subsampled to 200 per class)
- PROTEINS — Protein enzyme classification (~1113 graphs, subsampled to 200 per class)
- NCI1 — Anti-cancer compound activity (~4110 compounds, subsampled to 200 per class)
- PTC-MR — Carcinogenicity prediction (~344 compounds, total used)
- MUTAG — Mutagenicity prediction (~188 compounds, total used)

(See data/ or notebooks/ for dataset download and preprocessing scripts.)

## Implementation Overview
- `extract_ego_graphs()`: Ego-graph decomposition to manage large graphs within limited qubit constraints.
- `wl_subtree_kernel()`: Weisfeiler-Lehman subtree kernel implementation.
- `shortest_path_kernel()`: Shortest-path kernel using NetworkX shortest-path statistics.
- `QuantumWalkEmbedding` / `ScalableQuantumWalkEmbedding`: Classes for CTQW and QURI Ego-QW embeddings, with classical simulation options.
- `fidelity_kernel()`: Utilizes quantum-state fidelity for Gram matrix construction via Quri Parts.
- Utilities: `mixing_matrix_quri_circuit()`, `build_trotter_circuit_for_graph()`, `trotterize_positions_amplitude()`, `quantum_state_fidelity()`.

## Evaluation Protocol
- Nested 5-fold cross-validation for robust generalization.
- Classifier: SVM with RBF kernel (scikit-learn) using extracted feature representations.
- Metrics: Mean ± standard deviation of Accuracy and F1-score across outer CV folds.
- Data Handling: Features scaled (e.g., StandardScaler) with balanced class weights in SVM training.

## Key Results (Summary)
See notebooks/sub_main.ipynb and experiment_results.json for detailed logs and per-dataset numbers. Example summary table:

| Method         | Dataset | Accuracy (Mean ± Std) | F1-score (Mean ± Std) |
|----------------|---------|-----------------------|-----------------------|
| QURI Ego-QW    | AIDS    | 0.9650 ± 0.0255       | 0.9662 ± 0.0237       |
| CTQW           | AIDS    | 0.9950 ± 0.0100       | 0.9948 ± 0.0103       |
| Shortest-Path  | AIDS    | 0.9600 ± 0.0200       | 0.9598 ± 0.0207       |
| WL Subtree     | AIDS    | 0.9300 ± 0.0245       | 0.9193 ± 0.0309       |
| QURI Ego-QW    | MUTAG   | 0.8772 ± 0.0336       | 0.8793 ± 0.0324       |
| CTQW           | MUTAG   | 0.8514 ± 0.0255       | 0.8527 ± 0.0269       |
| Shortest-Path  | MUTAG   | 0.7872 ± 0.0169       | 0.7812 ± 0.0161       |
| WL Subtree     | MUTAG   | 0.7818 ± 0.0273       | 0.7783 ± 0.0295       |

(Results vary by dataset; full details in referenced files.)

## Team — Key Contributors

| Name                  | Discord Handle         | Role / Contribution                  |
|-----------------------|------------------------|--------------------------------------|
| Dr. Sushant Tapase    | @Dr-Sushant            | -  |
| Amon Koike            | @thedaemon_AK         | - |
| Jajapuram Shiva Sai   | @frosty               | -      |
| Ramesh Makwana        | @Ramesh Makwana       | -    |

## References (Selected)
1. QURI Parts — QunaSys Inc. — https://github.com/QunaSys/quri-parts (Framework for quantum circuits.)
2. Xing Ai et al. — "Towards Quantum Graph Neural Networks: An Ego-Graph Learning Approach" — arXiv:2201.05158 (Ego-graph inspiration.)
3. N. Shervashidze et al. — "Weisfeiler-Lehman Graph Kernels" — JMLR, 2011 (WL kernel.)
4. V. Havlíček et al. — "Supervised Learning with Quantum-Enhanced Feature Spaces" — Nature, 2019 (Quantum feature maps.)
5. Andrew M. Childs — "Universal Computation by Quantum Walk" — Phys. Rev. Lett., 2009 (Quantum walk foundations.)

