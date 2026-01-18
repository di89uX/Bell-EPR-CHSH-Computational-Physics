# src/models.py
import numpy as np


# Local hidden-variable (LHV)

def lhv_A(theta: float, lam: np.ndarray) -> np.ndarray:
    """Deterministic local outcome at Alice: ±1."""
    return np.sign(np.cos(theta - lam))


def lhv_B(theta: float, lam: np.ndarray) -> np.ndarray:
    """Deterministic local outcome at Bob: ±1 (anti-correlated for same settings)."""
    return -np.sign(np.cos(theta - lam))


def lhv_correlation(theta1: float, theta2: float, N: int = 200_000, seed: int | None = 42) -> float:
    """
    Monte Carlo estimate of E(theta1, theta2) for the LHV model.
    """
    rng = np.random.default_rng(seed)
    lam = rng.uniform(0.0, 2*np.pi, N)
    A = lhv_A(theta1, lam)
    B = lhv_B(theta2, lam)
    return float(np.mean(A * B))


# Quantum correlations

def qm_correlation_exact(theta1: float, theta2: float) -> float:
    """Exact singlet correlation: E = -cos(theta1 - theta2)."""
    return float(-np.cos(theta1 - theta2))


def qm_correlation_mc(theta1: float, theta2: float, N: int = 200_000, seed: int | None = 123) -> float:
    """
    Monte Carlo sampling of ±1 outcomes consistent with singlet correlations.
    We generate (A,B) with P(B = A) and P(B = -A) implied by E = -cos(theta).
    """
    rng = np.random.default_rng(seed)
    theta = theta1 - theta2

    # For singlet: E = <AB> = -cos(theta)
    # Let p_same = P(A=B), p_diff = P(A!=B).
    # Then E = p_same - p_diff = 2*p_same - 1  => p_same = (1+E)/2
    E = -np.cos(theta)
    p_same = (1 + E) / 2  # = (1 - cos(theta))/2 = sin^2(theta/2)

    A = rng.choice([-1, 1], size=N)  # Alice outcomes random ±1
    same = rng.random(size=N) < p_same
    B = np.empty_like(A)
    B[same] = A[same]
    B[~same] = -A[~same]

    return float(np.mean(A * B))


# CHSH helper

def chsh(E_ab: float, E_abp: float, E_apb: float, E_apbp: float) -> float:
    """Compute CHSH S value: E(a,b)+E(a,b')+E(a',b)-E(a',b')."""
    return float(E_ab + E_abp + E_apb - E_apbp)


def chsh_standard_angles():
    """
    Standard angle set that yields maximal quantum violation:
    a=0, a'=pi/2, b=pi/4, b'=-pi/4
    """
    a = 0.0
    ap = np.pi / 2
    b = np.pi / 4
    bp = -np.pi / 4
    return a, ap, b, bp
