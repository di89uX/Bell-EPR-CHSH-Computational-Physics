# Bell–EPR / Bell–CHSH Computational Physics Project

## Goal
This project computationally tests **local realism** by comparing:
1) a **local hidden-variable (LHV)** model (classical),
2) **quantum mechanical predictions** for an entangled singlet state, and
3) a **quantum circuit implementation (Qiskit)** of the Bell–CHSH test.

The key observable is the **CHSH parameter**:
\[
S = E(a,b) + E(a,b') + E(a',b) - E(a',b')
\]
Local realism requires \(|S|\le 2\), while quantum mechanics allows up to \(2\sqrt{2}\).

## Folder structure
- `Notebooks/` — main notebooks (theory, LHV, quantum, noise, Qiskit)
- `src/` — reusable Python functions (models, correlations, CHSH)
- `figures/` — exported plots
- `report/` — final report

## How to run
1. Install packages:
   - `pip install -r requirements.txt`
2. Open Jupyter and run notebooks in order.

## Notebooks
1. `Bell_EPR_Theory.ipynb`
2. `lhv_Simulation.ipynb`
3. `Quantum_Correlation.ipynb`
4. `Noise and Realisim.ipynb`
