#  Quantum-Kernel-Molecular-Classification

**Comparing Classical Graph Kernels and Quantum-Inspired Embeddings for Molecular Classification**

*A Project by Team The Cat's Cradle*

---

## 🏆 QPoland Global Quantum Hackathon 2025

**Dates:** 18-Oct-2025 to 26-Oct-2025  
**Challenge Link:** [https://www.qaif.org/contests/qpoland-global-quantum-hackathon](https://www.qaif.org/contests/qpoland-global-quantum-hackathon)

---

## Overview and Innovation

This repository addresses the challenge of molecular classification by comparing classical graph kernels with novel, **scalable quantum-inspired feature maps**. The goal is to demonstrate that quantum-derived embeddings can generate more expressive features for Support Vector Machine (SVM) classification on complex graph-structured data.

### 💡 Core Innovation: Scalable Ego-Graph Quantum Walk

We tackle the fundamental **qubit-scaling limitation** of quantum algorithms on large molecular graphs by introducing an **ego-graph decomposition** strategy. This method extracts localized subgraphs around each node, drastically reducing the required qubit count for **Trotterized Quantum Walk (QW)** circuit simulation. This enables:

1.  **Feasibility:** Efficient feature extraction from large molecular graphs.
2.  **Accuracy:** Capturing local functional-group topology effects crucial for chemical prediction.
3.  **Versatility:** Execution via classical simulation fallbacks or on quantum backends using the **QURI Parts** framework.

---

## Table of Contents
* [Getting Started](#getting-started)
* [Datasets](#datasets)
* [Implementation Overview](#implementation-overview)
* [Evaluation Protocol](#evaluation-protocol)
* [Key Results Summary](#key-results-summary)
* [Team – Key Contributors](#team--key-contributors)
* [References](#references)

---

## Getting Started

To clone the repository and install dependencies:

```bash
git clone [https://github.com/Dr-Sushant/Quantum-Kernel-Molecular-Classification.git](https://github.com/Dr-Sushant/Quantum-Kernel-Molecular-Classification.git)
cd Quantum-Kernel-Molecular-Classification
pip install -r requirements.txt
jupyter notebook
````

### Quick Run

Example notebooks demonstrating the end-to-end pipeline are provided under the `notebooks/` directory:

  * `notebooks/experiment_pipeline.ipynb`: End-to-end training and evaluation across all datasets and methods.
  * `notebooks/quantum_embeddings_demo.ipynb`: Detailed demonstration of the Trotterized quantum-walk embedding and fidelity kernel pipeline.

-----

## Datasets

The project benchmarks performance on five standard graph classification datasets:

| Dataset | Domain | Task / Description | Size (Approx.) |
| :--- | :--- | :--- | :--- |
| **AIDS** | Chemistry | HIV activity screening | \~2,000 compounds |
| **PROTEINS** | Biology | Protein enzyme classification | \~1,113 graphs |
| **NCI1** | Chemistry | Anti-cancer compound activity | \~4,110 compounds |
| **PTC-MR** | Chemistry | Carcinogenicity prediction | \~344 compounds |
| **MUTAG** | Chemistry | Mutagenicity prediction | \~188 compounds |

*(Dataset download and preprocessing scripts are available in the `data/` or `notebooks/` directories.)*

-----

## Implementation Overview

Our implementation is structured around four main feature extraction methods and the core quantum scaling utility:

  * `extract_ego_graphs()`: Core utility for **ego-graph decomposition**, enabling scalable quantum processing.
  * **Classical Baselines:**
      * `wl_subtree_kernel()`: Implements the Weisfeiler–Lehman subtree kernel.
      * `shortest_path_kernel()`: Computes features using NetworkX shortest-path statistics.
  * **Quantum-Inspired Methods:**
      * `QuantumWalkEmbedding` / `ScalableQuantumWalkEmbedding`: Classes for constructing **Trotterized Quantum-Walk embeddings** on graphs, with classical simulation fallbacks.
      * `fidelity_kernel()`: Function utilizing **quantum-state fidelity** to construct Gram matrices from the QW embeddings, effectively defining the custom kernel.
  * **QURI Parts Integration:** Utilities such as `mixing_matrix_quri_circuit()`, `build_trotter_circuit_for_graph()`, and `trotterize_positions_amplitude()` are used to interface with the Quri Parts framework for circuit generation and simulation.

-----

## Evaluation Protocol

We employ a rigorous evaluation protocol to ensure robust and comparable results:

  * **Cross-Validation:** **10-fold stratified cross-validation** to minimize bias and variance.
  * **Classifier:** **Support Vector Machine (SVM)** from `scikit-learn` is used, taking the kernel matrices (Gram matrices) directly from our feature map implementations.
  * **Metrics:** **Accuracy** and **$F1$-score** (macro or weighted, depending on dataset balance) are reported.
  * **Reporting:** Results present the **mean and standard deviation** across all CV folds (and random seeds where applicable).

-----

## Key Results Summary

*(Note: Numeric results are dynamically generated within the notebooks/experiment\_pipeline.ipynb. The table below serves as a structured placeholder for the final report.)*

| Kernel Type | Accuracy (avg) | F1-score (avg) | Notes |
| :--- | :--- | :--- | :--- |
| **WL Kernel** | TBD | TBD | Baseline classical (Structural Motif) |
| **Shortest-Path** | TBD | TBD | Path-based baseline (Topological) |
| **Quantum-Inspired** | TBD | TBD | **Trotterized Quantum-Walk Embeddings**, scaled via Ego-Graphs |

-----

## Team – Key Contributors

| Name | Discord Handle | Role / Contribution |
| :--- | :--- | :--- |
| **Dr. Sushant Tapase** | @Dr-Sushant | Project Lead, Algorithm Design, QW Implementation |
| **Amon Koike** | @thedaemon\_AK | Quantum Circuit Implementation, QURI Parts Integration |
| **Jajapuram Shiva Sai** | @frosty | Data Preprocessing, Classical Kernel Implementations |
| **Ramesh Makwana** | @Ramesh Makwana | Evaluation Pipeline & Results Analysis |

-----

## References (Selected)

1.  **QURI Parts** — QunaSys Inc. — [https://github.com/QunaSys/quri-parts](https://github.com/QunaSys/quri-parts) (Framework used for circuits and simulation.)
2.  Xing Ai et al. — "Towards Quantum Graph Neural Networks: An Ego-Graph Learning Approach" — arXiv:2201.05158. (Inspiration for ego-graph decomposition and scalable processing.)
3.  N. Shervashidze et al. — "Weisfeiler-Lehman Graph Kernels" — JMLR, 2011. (WL-subtree kernel.)
4.  V. Havlíček et al. — "Supervised Learning with Quantum-Enhanced Feature Spaces" — Nature, 2019. (Quantum feature maps / QSVM.)
5.  Andrew M. Childs — "Universal Computation by Quantum Walk" — Phys. Rev. Lett., 2009. (Quantum-walk foundations.)
6.  Seth Lloyd — "Universal Quantum Simulators" — Science, 1996. (Trotter-Suzuki decomposition.)

<!-- end list -->

```
