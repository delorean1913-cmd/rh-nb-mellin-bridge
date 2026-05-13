#!/usr/bin/env python3
"""Small smoke tests for the starter code."""

from __future__ import annotations

from mobius_approximant import mobius_sieve, P_N
import mpmath as mp


def main() -> None:
    mu = mobius_sieve(10)
    expected = [0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1]
    assert mu == expected, f"unexpected mu values: {mu}"

    p = P_N(mp.mpc(2, 0), N=10, dps=50)
    assert abs(p) > 0

    print("Smoke test passed.")
    print("Layer: finite diagnostic support code.")


if __name__ == "__main__":
    main()
