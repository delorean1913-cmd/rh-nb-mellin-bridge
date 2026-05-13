# Public research question draft

## Title

Weighted \(L^2\) convergence for smoothed Möbius Nyman--Beurling approximants

## Question

Let

```math
P_N(s)=\sum_{n\le N}\mu(n)(1-n/N)n^{-s}.
```

Is it known, or does it follow from standard mollifier / Dirichlet-polynomial estimates, that

```math
{1\over 2\pi}\int_{-\infty}^{\infty}
\left|
{1-\zeta(1/2+i\tau)P_N(1/2+i\tau)
\over 1/2+i\tau}
\right|^2d\tau \to 0
```

as \(N\to\infty\)?

Equivalently, can this explicit smoothed signed Möbius polynomial be shown to approximate \(1/\zeta(s)\) in the weighted critical-line norm

```math
\|F\|^2 = {1\over 2\pi}\int_{-\infty}^{\infty}
\left|{F(1/2+i\tau)\over 1/2+i\tau}\right|^2d\tau?
```

I am not asking for verification of an RH proof. The question is whether this specific Mellin-side estimate is known, false, conditionally known, or reducible to a named open problem.

## Motivation

This estimate would be a candidate \(L^2_{\rm eff}\) bridge in the Nyman--Beurling / Báez-Duarte framework. Finite Gram diagnostics suggest that signed Möbius-type coefficients are natural candidates, but finite diagnostics are not proof-level evidence. The missing issue is a uniform asymptotic theorem.

## Desired answers

Useful answers would include any of the following.

1. A proof from known mollifier mean-value estimates.
2. A conditional proof under RH, Lindelöf, pair correlation, zero-density estimates, or another standard hypothesis.
3. A counterexample or obstruction for this specific weight.
4. A reference showing that this weighted norm convergence is equivalent to, weaker than, or stronger than a known form of the Nyman--Beurling criterion.
5. A sharper candidate smoothing \(W\) with a known Mellin-transform advantage.

## Range decomposition under consideration

A possible attack is to split the integral into

```math
|\tau|\le T_0, \qquad T_0<|\tau|\le T_N, \qquad |\tau|>T_N,
```

and prove low, medium, and tail estimates separately. The main obstruction appears to be the medium range, where one needs uniform control of \(\zeta(1/2+i\tau)P_N(1/2+i\tau)-1\).

## Public repository link

Add the GitHub repository link here after uploading:

```text
https://github.com/YOUR-USERNAME/rh-nb-mellin-bridge
```
