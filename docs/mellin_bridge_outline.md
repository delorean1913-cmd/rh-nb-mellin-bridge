# Mellin bridge outline

## Target theorem

For

```math
P_N(s)=\sum_{n\le N}\mu(n)(1-n/N)n^{-s},
```

prove or disprove

```math
I_N={1\over 2\pi}\int_{-\infty}^{\infty}
\left|
{1-\zeta(1/2+i\tau)P_N(1/2+i\tau)
\over 1/2+i\tau}
\right|^2d\tau \to 0.
```

Layer: **conjectural \(L^2_{\rm eff}\) bridge**.

## Dependencies

Likely tools:

- Mellin transforms;
- Dirichlet polynomial mean values;
- mollifier estimates;
- approximate functional equations;
- large sieve inequalities;
- zero-density estimates;
- zero-free regions;
- short-interval variance estimates;
- known NB/BD equivalences.

## Proposed decomposition

Choose two auxiliary scales \(T_0\) and \(T_N\), then write

```math
I_N = I_N^{\rm low}+I_N^{\rm med}+I_N^{\rm tail}.
```

### Low range

```math
|\tau|\le T_0.
```

Goal: prove compact-range convergence after handling zero neighborhoods and the fact that \(P_N\) is only a finite approximation to \(1/\zeta\).

Failure mode: compact convergence is blocked by critical-line zeros or by insufficient smoothing.

### Medium range

```math
T_0<|\tau|\le T_N.
```

Goal: prove a uniform mean-square estimate for

```math
\zeta(1/2+i\tau)P_N(1/2+i\tau)-1.
```

This is probably the main obstruction.

Failure mode: current mollifier estimates do not cover the necessary length/range combination.

### Tail range

```math
|\tau|>T_N.
```

Goal: use the denominator \(|1/2+i\tau|^{-2}\), bounds for \(\zeta\), and the smoothing of \(P_N\) to show the tail is negligible.

Failure mode: the Dirichlet polynomial grows too much on average or lacks enough smoothing.

## Output standard

A successful task must produce one of:

1. a proved lemma;
2. a counterexample;
3. a named obstruction;
4. a sharper conjecture with reduced assumptions;
5. a certified finite theorem artifact.
