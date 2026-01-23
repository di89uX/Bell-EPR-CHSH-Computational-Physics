# Bell–EPR–CHSH: A Computational Study of Quantum Nonlocality

## Overview
This project presents a computational investigation of the Einstein–Podolsky–Rosen (EPR) argument
and Bell–CHSH inequalities using Python-based simulations and quantum circuit models.
The goal is to compare predictions of **local hidden-variable (LHV) theories** with those of
**quantum mechanics**, and to study the effects of noise and realism on Bell inequality violations.

The project combines analytical results, Monte Carlo simulations, and a Qiskit-based quantum circuit
implementations to provide a complete and reproducible study of Bell nonlocality.

---

## Objectives
- Review the theoretical foundations of the EPR paradox and Bell’s theorem
- Implement a local hidden-variable model and verify the Bell–CHSH bound
- Compute quantum correlations analytically and via Monte Carlo methods
- Demonstrate Bell inequality violation using quantum circuit simulation (Qiskit)
- Study the effect of noise on Bell violations
- Verify the no-signalling principle through marginal probability analysis

---

## Project Structure

Bell_EPR_Com_Physics/
├── src/
│ └── models.py
│
├── Notebooks/
│ ├── Bell_EPR_Theory.ipynb
│ ├── lhv_Simulation.ipynb
│ ├── Quantum_Correlation.ipynb
│ ├── Noise and Realism.ipynb
│ └── Qiskit_CHSH.ipynb
│
├── figures/
│ ├── lhv_correlation_vs_angle.png
│ ├── correlation_vs_angle.png
│ ├── S_vs_visibility.png
│ └── absS_vs_qiskit_depolarizing.png
│
└── README.md


---

## Notebook Descriptions

### 1. `Bell_EPR_Theory.ipynb`
Provides a theoretical review of:
- The EPR argument and assumptions of locality and realism
- Bell’s formulation of hidden-variable models
- Derivation of the Bell–CHSH inequality
- Quantum mechanical predictions for entangled spin-½ systems

This notebook is primarily conceptual and contains minimal code.

---

### 2. `lhv_Simulation.ipynb`
Implements a local hidden-variable model based on Bell’s assumptions.
Key results:
- Numerical evaluation of correlation functions via Monte Carlo sampling
- Verification that the CHSH parameter satisfies  
$
  |S| \le 2
$
  for all sample sizes and measurement settings

---

### 3. `Quantum_Correlation.ipynb`
Computes quantum correlations for the singlet state:
- Exact quantum correlation: \(E_{\mathrm{QM}}(\theta) = -\cos\theta\)
- Monte Carlo simulation of quantum measurement outcomes
- Demonstration of Bell–CHSH violation:
$
  |S| = 2\sqrt{2}
$

---

### 4. `Noise and Realism.ipynb`
Studies how noise affects Bell violations using a visibility model:
- Correlations scaled as \(E_V(\theta) = V E_{\mathrm{QM}}(\theta)\)
- Identification of the critical visibility:
$
  V_{\mathrm{crit}} = \frac{1}{\sqrt{2}}
$
- Interpretation of noise as loss of entanglement or experimental imperfections

---

### 5. `Qiskit_CHSH.ipynb`
Implements the Bell–CHSH test using quantum circuits:
- Preparation of entangled two-qubit states
- Measurement along arbitrary axes via basis rotations
- Estimation of correlations from shot statistics
- Observation of Bell violation on a quantum simulator
- Inclusion of depolarising noise and degradation of $S$
- Verification of the no-signalling principle via marginal probabilities

---

## Key Results

| Model | CHSH Value |
|-----|-----------|
| Local Hidden Variables | $\abs S \approx 2.0$ |
| Quantum Mechanics (Exact) |$\absS = 2\sqrt{2}$ |
| Quantum Monte Carlo | $\absS \approx 2.8$ |
| Qiskit Simulator | $ \absS \approx 2.8$ |
| Noisy Quantum Model | $ \abs S \rightarrow 2$ |

---

## Requirements
- Python 3.9+
- NumPy
- Matplotlib
- Jupyter Notebook
- Qiskit
- Qiskit Aer

Install dependencies (if needed):
```bash
pip install numpy matplotlib jupyter qiskit qiskit-aer


