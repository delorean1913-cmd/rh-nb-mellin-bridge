#!/usr/bin/env python3
"""
Finite diagnostic for the truncated weighted Mellin integral.

Layer: finite diagnostic.

This computes a crude trapezoidal approximation to

    (1/2pi) int_{-T}^{T} |(1 - zeta(1/2+it) P_N(1/2+it))/(1/2+it)|^2 dt.

It is not a proof and is not intended for large-scale certified computation.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import mpmath as mp

# Allow running as a script from repository root.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from mobius_approximant import zeta_mollifier_error  # noqa: E402


def integrand(t: mp.mpf, N: int, weight: str, dps: int) -> mp.mpf:
    s = mp.mpc(mp.mpf("0.5"), t)
    err = zeta_mollifier_error(s, N=N, weight=weight, dps=dps)
    denom = abs(s) ** 2
    return (abs(err) ** 2) / denom / (2 * mp.pi)


def truncated_integral(N: int, T: float, steps: int, weight: str, dps: int) -> mp.mpf:
    if steps < 10:
        raise ValueError("steps must be at least 10")
    if steps % 2 == 1:
        steps += 1
    mp.mp.dps = dps
    Tm = mp.mpf(T)
    h = (2 * Tm) / steps
    total = mp.mpf("0")
    for k in range(steps + 1):
        t = -Tm + k * h
        factor = mp.mpf("0.5") if k in (0, steps) else mp.mpf("1")
        total += factor * integrand(t, N=N, weight=weight, dps=dps)
    return h * total


def main() -> None:
    parser = argparse.ArgumentParser(description="Crude finite diagnostic for truncated Mellin integral.")
    parser.add_argument("--N", type=int, default=20)
    parser.add_argument("--T", type=float, default=20.0)
    parser.add_argument("--steps", type=int, default=400)
    parser.add_argument("--weight", choices=["triangular", "quadratic"], default="triangular")
    parser.add_argument("--dps", type=int, default=30)
    args = parser.parse_args()

    val = truncated_integral(args.N, args.T, args.steps, args.weight, args.dps)
    print("Layer: finite diagnostic")
    print("This truncated numerical integral is not a proof.")
    print(f"N={args.N}, T={args.T}, steps={args.steps}, weight={args.weight}, dps={args.dps}")
    print(f"truncated_integral={mp.nstr(val, 20)}")


if __name__ == "__main__":
    main()
