
# QPoland Global Quantum Hackathon 2025 Project  
**Project Title:** Comparing Classical and Quantum-Inspired Kernels for Molecular Classification  
**Team:** The Cats Cradle  
**Date:** October 18, 2025 - October 26, 2025  
**Website:** https://www.qaif.org/contests/qpoland-global-quantum-hackathon  

## Overview  
This repository presents a comparative study of classical graph kernels and a quantum-inspired Trotterized quantum walk (QW) embedding for molecular and protein graph classification. The project leverages datasets such as AIDS, PROTEINS, NCI1, PTC-MR, and MUTAG, utilizing the QURI Parts framework to simulate quantum-inspired features. A key innovation is the ego-graph decomposition technique, which reduces qubit requirements while preserving functional-group topology, enhancing classification accuracy.

## Repository Details  
- **Project Site:** https://jajapuramshivasai.github.io/QML-Molecular-Classification/  
- **Source Code:** https://github.com/jajapuramshivasai/QML-Molecular-Classification  

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
  python3 -m http.server --directory . 8000 &
  open http://localhost:8000/pages/
  ```
- Push changes to the default branch for updates.

### Contact  
Raise issues or PRs here, or contact team members via Discord handles.

## References  
- QURI Parts: https://github.com/QunaSys/quri-parts  
```
