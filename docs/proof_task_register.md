# Proof task register

## Task M1: Fix the explicit approximant

Layer: conjectural \(L^2_{\rm eff}\) bridge

Target: Work only with

```math
P_N(s)=\sum_{n\le N}\mu(n)(1-n/N)n^{-s}
```

until a proof or obstruction is found.

Failure mode: triangular smoothing has a structural obstruction.

## Task M2: Derive the Mellin transform of the smoothing error

Layer: conjectural \(L^2_{\rm eff}\) bridge

Target: Express \(1-\zeta(s)P_N(s)\) as explicitly as possible in terms of sums involving \(\mu\), divisor convolutions, and smoothing tails.

Dependencies: Dirichlet convolution, partial summation, Mellin inversion.

Failure mode: expression is not tractable for mean-square estimates.

## Task M3: Low-range estimate

Layer: conjectural \(L^2_{\rm eff}\) bridge

Target: Prove \(I_N^{\rm low}\to0\) for fixed \(T_0\), or isolate the exact obstruction.

Dependencies: compact approximation of \(1/\zeta\), treatment of zeros, dominated convergence.

Failure mode: local singular behavior around zeros prevents the estimate.

## Task M4: Medium-range estimate

Layer: conjectural \(L^2_{\rm eff}\) bridge

Target: Bound

```math
\int_{T_0<|t|\le T_N}\left|\zeta(1/2+it)P_N(1/2+it)-1\right|^2{dt\over 1/4+t^2}.
```

Dependencies: mollifier mean values, large sieve, approximate functional equations.

Failure mode: known estimates do not support the length/range needed.

## Task M5: Tail estimate

Layer: conjectural \(L^2_{\rm eff}\) bridge

Target: Show \(I_N^{\rm tail}\to0\) for a defensible scale \(T_N\to\infty\).

Dependencies: second moment of zeta, Dirichlet polynomial bounds, smoothing decay.

Failure mode: tail cannot be controlled uniformly in \(N\).

## Task F1: Certified finite Gram package

Layer: certified finite theorem / finite theorem artifact

Target: Store exact formulas, finite matrices, interval bounds, and reproducibility scripts for finite NB/BD Gram computations.

Dependencies: exact rational/log formulas or interval arithmetic; no informal numerical-only certificates.

Failure mode: conditioning prevents certification at target sizes.
