#!/usr/bin/env python3
"""
Smoothed signed Möbius Dirichlet-polynomial approximants.

Layer: finite diagnostic support code.

This script does not prove any asymptotic theorem. It provides a small,
reproducible implementation of the current candidate family

    P_N(s) = sum_{n<=N} mu(n) W(n/N) n^{-s}

with W(x) = (1-x)_+ by default.
"""

from __future__ import annotations

import argparse
from typing import List

import mpmath as mp


def mobius_sieve(N: int) -> List[int]:
    """Return mu[0..N] using a standard linear sieve."""
    if N < 1:
        return [0] * (N + 1)

    mu = [0] * (N + 1)
    mu[1] = 1
    primes: List[int] = []
    is_composite = [False] * (N + 1)

    for i in range(2, N + 1):
        if not is_composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            v = i * p
            if v > N:
                break
            is_composite[v] = True
            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]

    return mu


def triangular_weight(n: int, N: int) -> mp.mpf:
    """W(n/N) = (1 - n/N)_+ for 1 <= n <= N."""
    if n > N:
        return mp.mpf("0")
    return mp.mpf(1) - mp.mpf(n) / mp.mpf(N)


def quadratic_weight(n: int, N: int) -> mp.mpf:
    """Optional stronger smoothing W(n/N) = (1 - n/N)^2_+."""
    w = triangular_weight(n, N)
    return w * w


def P_N(s: complex, N: int, weight: str = "triangular", dps: int = 50) -> mp.mpc:
    """Evaluate P_N(s) by direct summation."""
    if N < 1:
        raise ValueError("N must be positive")
    mp.mp.dps = dps
    mu = mobius_sieve(N)
    total = mp.mpc(0)

    if weight == "triangular":
        W = triangular_weight
    elif weight == "quadratic":
        W = quadratic_weight
    else:
        raise ValueError("weight must be 'triangular' or 'quadratic'")

    ss = mp.mpc(s)
    for n in range(1, N + 1):
        if mu[n] == 0:
            continue
        total += mu[n] * W(n, N) * mp.power(n, -ss)
    return total


def zeta_mollifier_error(s: complex, N: int, weight: str = "triangular", dps: int = 50) -> mp.mpc:
    """Return 1 - zeta(s) P_N(s)."""
    mp.mp.dps = dps
    ss = mp.mpc(s)
    return 1 - mp.zeta(ss) * P_N(ss, N=N, weight=weight, dps=dps)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate smoothed Möbius P_N(s).")
    parser.add_argument("--N", type=int, default=20)
    parser.add_argument("--sigma", type=float, default=0.5)
    parser.add_argument("--t", type=float, default=14.134725141734693)
    parser.add_argument("--weight", choices=["triangular", "quadratic"], default="triangular")
    parser.add_argument("--dps", type=int, default=50)
    args = parser.parse_args()

    s = mp.mpc(args.sigma, args.t)
    p = P_N(s, args.N, args.weight, args.dps)
    err = zeta_mollifier_error(s, args.N, args.weight, args.dps)
    print(f"N={args.N}")
    print(f"s={s}")
    print(f"weight={args.weight}")
    print(f"P_N(s)={mp.nstr(p, 20)}")
    print(f"1 - zeta(s) P_N(s)={mp.nstr(err, 20)}")


if __name__ == "__main__":
    main()
