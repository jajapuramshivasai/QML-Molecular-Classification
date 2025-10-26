# QPoland Global Quantum Hackathon 2025 Project  
**Project Title:** Comparing Classical and Quantum-Inspired Kernels for Molecular Classification  
**Team:** The Cats Cradle  
**Date:** October 18, 2025 - October 26, 2025  
**Website:** https://www.qaif.org/contests/qpoland-global-quantum-hackathon  

## Overview  
This repository presents a comparative study of classical graph kernels and a quantum-inspired Trotterized quantum walk (QW) embedding for molecular and protein graph classification. The project leverages datasets such as AIDS, PROTEINS, NCI1, PTC-MR, and MUTAG, utilizing the QURI Parts framework to simulate quantum-inspired features. A key innovation is the ego-graph decomposition technique, which reduces qubit requirements while preserving functional-group topology, enhancing classification accuracy.

## Deliverables  
### Source Code
https://github.com/jajapuramshivasai/QML-Molecular-Classification/src

### Report link
https://jajapuramshivasai.github.io/QML-Molecular-Classification/

https://github.com/jajapuramshivasai/QML-Molecular-Classification/docs/QML-Molecular-Classification_report.pdf  

### Video link  
https://drive.google.com/file/d/1p1539dZOyex4KxVeZW4sIBkU02wZt9MJ/view?usp=sharing

### Quick Start  
1. Clone the repository and install dependencies:  
   ```bash
   git clone https://github.com/jajapuramshivasai/QML-Molecular-Classification.git
   cd QML-Molecular-Classification
   pip install -r requirements.txt
2. Run experiments:  
   - Jupyter Notebook: `jupyter notebook`  
   - Main Notebook: `notebooks/sub_main.ipynb`  
   - Demo: `notebooks/quantum_embeddings_demo.ipynb`

### Contents  
- **notebooks/**: Experiment scripts (e.g., `sub_main.ipynb`)  
- **src/**: Code for kernels, embeddings, and utilities  
- **pages/index.html**: Project report for GitHub Pages  
- **experiment_results.json**: Results and logs (if available)  

### Datasets  
- TU benchmarks (AIDS, PROTEINS, NCI1, PTC-MR, MUTAG) via PyTorch Geometric TUDataset  
- Preprocessing scripts in `notebooks/` and `src/`

### Implemented Methods  
- **Ego-QW**: QURI-inspired ego-graph quantum walk embeddings  
- **CTQW**: Continuous-time quantum walk spectral features  
- **Classical Baselines**: Weisfeiler-Lehman subtree kernel, Shortest-Path kernel  
- **Classifier**: SVM with RBF kernel, nested cross-validation for hyperparameters  

### Evaluation  
- Nested 5-fold cross-validation  
- Metrics: Mean ± std of Accuracy and F1-score  
- Features standardized, class weights balanced  
- Reproducible with fixed seeds (Python, NumPy, PyTorch)  

### Hardware/Software/Simulator Platforms
- We run our main notebook on Colab 12.7gb, CPU
- Simulator: QURI Parts to run our Quantum routines. We did not use real Quantum hardware.

### Team  
- Jajapuram Shiva Sai (@frosty)  
- Amon Koike (@thedaemon_AK)  
- Ramesh Makwana (@Ramesh Makwana)  
- Dr. Sushant Tapase (@Dr-Sushant)  

## Contribution Guide  
### Notebooks  
- Edit in Google Colab: Open `notebooks/sub_main.ipynb`, modify, and save/export to the repo.  
- Workflow:  
  1. Open in Colab via the notebook link.  
  2. Edit and run end-to-end.  
  3. Commit updated `.ipynb` with a change description.

### Website (GitHub Pages)  
- Edit `pages/index.html`.  
- Preview locally:  
  ```bash
  python3 -m http.server 8000 --directory Docs
  open http://localhost:8000/index.html
  ```
- Push changes to the default branch for updates.

### Contact  
Raise issues or PRs here, or contact team members via Discord handles.

## References

1. X. Ai et al., “Towards Quantum Graph Neural Networks: An Ego‑Graph Learning Approach,” arXiv:2201.05158v3 (2024). [HTML](https://arxiv.org/html/2201.05158v3)
2. D. Aharonov, A. Ambainis, J. Kempe, U. Vazirani, “Quantum Walks on Graphs,” STOC’01; arXiv:quant‑ph/0012090. [PDF](https://arxiv.org/pdf/quant-ph/0012090.pdf)
3. C. Kluber, “Trotterization in Quantum Theory,” arXiv:2310.13296. [PDF](https://arxiv.org/pdf/2310.13296.pdf)
4. N. Shervashidze et al., “Weisfeiler‑Lehman Graph Kernels,” JMLR 12, 2539–2561 (2011). [PDF](https://www.jmlr.org/papers/volume12/shervashidze11a/shervashidze11a.pdf)
5. K. M. Borgwardt, H.‑P. Kriegel, “Shortest‑path kernels on graphs,” ICDM 2005. [PDF](https://ethz.ch/content/dam/ethz/special-interest/bsse/borgwardt-lab/documents/papers/BorKri05.pdf)
6. PyTorch Geometric TUDataset. [docs](https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html)
7. PyTorch Geometric utils (to_networkx, conversions). [utils](https://pytorch-geometric.readthedocs.io/en/2.5.3/modules/utils.html)
8. QURI Parts simulator and states. [simulator](https://quri-parts.qunasys.com/docs/tutorials/advanced/simulator/), [states](https://quri-parts.qunasys.com/docs/tutorials/basics/states/)
9. Continuous‑time quantum walk overview. [overview](https://en.wikipedia.org/wiki/Continuous-time_quantum_walk)
10. scikit‑learn SVC and RBF kernel. [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html), [rbf_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html)
