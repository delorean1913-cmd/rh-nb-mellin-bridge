# Status

Date: 2026-05-13

## Summary

This repository is in the analytic-bridge phase. The main task is to prove or disprove a Mellin-side estimate for one explicit smoothed signed Möbius approximant family.

No proof of RH is claimed.

## Layer table

| Item | Layer | Status | Notes |
|---|---|---|---|
| Closed-form NB Gram finite computations | Certified finite theorem / finite theorem artifact | In progress | Store reproducible finite outputs under `finite_gram_artifacts/` and exact certificates under `certificates/`. |
| Smoothed Möbius Mellin estimate for \(P_N\) | Conjectural \(L^2_{\rm eff}\) bridge | Open | This is the central missing theorem. |
| Low / medium / tail range decomposition of \(I_N\) | Conjectural \(L^2_{\rm eff}\) bridge | Drafted as a proof task | See `docs/mellin_bridge_outline.md`. |
| RH implication through BD/NB | RH implication through BD/NB | Conditional only | Not available unless the bridge and limiting argument are proved. |

## Active candidate family

```math
P_N(s)=\sum_{n\le N}\mu(n)(1-n/N)n^{-s}.
```

The triangular smoothing is chosen as the baseline because it is explicit, simple, and keeps the candidate focused. Other smoothings can be tested later only if this one fails or a proof obstruction is isolated.

## Current proof task

Prove, disprove, or sharply reformulate:

```math
{1\over 2\pi}\int_{-\infty}^{\infty}
\left|
{1-\zeta(1/2+i\tau)P_N(1/2+i\tau)
\over 1/2+i\tau}
\right|^2d\tau \to 0.
```

## Failure modes

The task fails if any of the following is established.

1. A nonzero lower bound for the liminf of the integral.
2. A zero-induced obstruction showing that the chosen \(P_N\) cannot approximate \(1/\zeta\) in the weighted critical-line norm.
3. A mean-value obstruction showing the medium range cannot be controlled with this smoothing.
4. A tail obstruction showing smoothing does not produce enough decay uniformly in \(N\).

Failure is useful if it is formulated as a precise lemma or counterexample.
