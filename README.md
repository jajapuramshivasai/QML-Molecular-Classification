# QML-Molecular-Classification

Comparing classical graph kernels and quantum-inspired embeddings for molecular classification — a project by Team The Cats Cradle.

## QPoland Global Quantum Hackathon 2025
18-Oct-2025 to 26-Oct-2025  
https://www.qaif.org/contests/qpoland-global-quantum-hackathon 

## Overview
This repository implements and evaluates classical graph-kernel methods and a quantum-inspired (Trotterized quantum walk) kernel for molecular and protein graph classification. The goal is to compare classical approaches (Weisfeiler–Lehman, shortest-path, RBF/linear/polynomial kernels) with scalable quantum-walk-based embeddings that can be simulated classically or executed on quantum backends via QURI Parts.

Innovation: fixing qubit-scaling issues by using ego-graph decomposition to drastically reduce required qubit count while still capturing functional-group topology effects; this enables efficient, accurate feature extraction from molecular graphs and therefore improves classification performance.

# Quantum-Kernel-Molecular-Classification

repo for comparing classical graph-kernel baselines with quantum‑inspired quantum-walk (QW) embeddings for molecular and protein graph classification.

Project site (pages/index.html): https://jajapuramshivasai.github.io/QML-Molecular-Classification/  
Source page: https://github.com/jajapuramshivasai/QML-Molecular-Classification/blob/main/pages/index.html

Quick start
1. Clone and install
   ```bash
   git clone https://github.com/jajapuramshivasai/QML-Molecular-Classification.git
   cd QML-Molecular-Classification
   pip install -r requirements.txt
   ```
2. Open examples and reproduce experiments
   - Jupyter: jupyter notebook
   - Notebooks: notebooks/sub_main.ipynb (end-to-end), notebooks/quantum_embeddings_demo.ipynb (demo)

What’s inside
- notebooks/: reproducible experiments and demos (main entry: notebooks/sub_main.ipynb)
- src/: implementation code for kernels, embeddings, and utilities
- pages/index.html: project report used for the GitHub Pages site
- experiment_results.json: per-run results and logs (if present)

Datasets (TU benchmarks via PyTorch Geometric TUDataset)
- AIDS, PROTEINS, NCI1, PTC-MR, MUTAG (preprocessing and sampling scripts in notebooks/ and src/)

Implemented methods (high level)
- Ego‑QW: QURI‑inspired ego‑graph quantum‑walk embeddings (Trotterized circuits, observables aggregated across centers/times)
- CTQW: full‑graph continuous‑time quantum‑walk spectral features
- Classical baselines: Weisfeiler–Lehman subtree kernel, Shortest‑Path kernel
- Classifier: SVM with RBF kernel and nested cross‑validation for hyperparameter selection

Evaluation
- Nested 5‑fold CV (outer) with inner hyperparameter grid for SVM
- Report mean ± std of Accuracy and F1 over outer folds
- Features standardized and class weights balanced for SVM training
- Reproducibility: fixed seeds for Python / NumPy / PyTorch; parameters controlled in notebooks

Representative results
- Example numbers and plots are shown on the project page and in notebooks/sub_main.ipynb. Replace placeholders with your computed statistics when re-running experiments.

Team
- Jajapuram Shiva Sai — @frosty  
- Amon Koike — @thedaemon_AK  
- Ramesh Makwana — @Ramesh Makwana  
- Dr. Sushant Tapase — @Dr-Sushant

References and resources
- QURI Parts simulator: https://github.com/QunaSys/quri-parts  
- See the project page for full references to WL kernels, shortest-path kernels, CTQW literature and other cited works.

Contact
- Open an issue or PR on this repository, or reach contributors via the Discord handles above.


Contributing
- Notebooks
  - Quick edit in Colab: open the notebook (for example notebooks/sub_main.ipynb) in Google Colab, make edits, test, and save/export the updated notebook back to the repo or send a PR.
  - Recommended workflow:
    1. Open the notebook link and click "Open in Colab".
    2. Edit cells and run end-to-end to confirm results.
    3. Commit updated .ipynb with a short description of changes.

- Website (GitHub Pages)
  - To change the website, edit pages/index.html in this repository.
  - To preview locally, run a simple HTTP server from the repository root:
    ```bash
    python3 -m http.server --directory . 8000 &
    # then open:
    # http://localhost:8000/pages/
    ```
  - After changes, push to the default branch; GitHub Pages will publish the updates at the project site above.

Thank you for contributing — open an issue or PR with ideas, bug reports, or improvements.