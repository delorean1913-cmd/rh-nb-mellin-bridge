# RH NB Mellin Bridge

This repository is a public working package for a narrow Nyman--Beurling / Báez-Duarte research program.
It does **not** claim a proof of the Riemann Hypothesis.

The active question is whether one can prove a uniform Mellin-side estimate strong enough to force the BD/NB finite-section error to zero.
The current candidate family is a smoothed signed Möbius Dirichlet polynomial.

## Current target

Let

```math
P_N(s)=\sum_{n\le N}\mu(n)\,W(n/N)n^{-s},
```

where the baseline weight in this repository is

```math
W(x)=(1-x)_+.
```

The conjectural bridge is the estimate

```math
I_N := {1\over 2\pi}\int_{-\infty}^{\infty}
\left|
{1-\zeta(1/2+i\tau)P_N(1/2+i\tau)
\over 1/2+i\tau}
\right|^2d\tau \to 0.
```

This is the **conjectural \(L^2_{\rm eff}\) bridge**. Until it is proved, the project has no RH proof.

## Three-layer status discipline

Everything in this repository is classified as exactly one of the following.

1. **Certified finite theorem / finite theorem artifact.**
   A rigorous finite computation, exact Gram or Cholesky certificate, finite matrix identity, reproducible finite diagnostic, or finite Schur-gain contract.

2. **Conjectural \(L^2_{\rm eff}\) bridge.**
   A proposed asymptotic Mellin theorem, still open unless fully proved.

3. **RH implication through BD/NB.**
   A conditional implication available only after the bridge is converted into a theorem and the limiting mechanism is proved.

Finite diagnostics guide the search. They are not proof-level evidence for RH.

## Repository layout

```text
README.md                         Project overview
STATUS.md                         Current layer-separated status
QUESTION.md                       Public research question draft
PROJECT_SCOPE.md                  What belongs here and what does not
UPLOAD_INSTRUCTIONS.md            Browser-only GitHub upload steps
docs/                             Proof program notes and protocols
src/                              Small reproducible finite-diagnostic scripts
finite_gram_artifacts/             Place for finite Gram artifacts and summaries
certificates/                     Place for exact or interval certificates
notes/                            Open lemmas and working notes
.github/ISSUE_TEMPLATE/           Issue templates for proof tasks/artifacts
```

## Run the small smoke test

```bash
python src/run_smoke_test.py
```

Optional finite diagnostic:

```bash
python src/mellin_integral_diagnostic.py --N 20 --T 20 --steps 400
```

This numerical integral is only a finite diagnostic. It is not a proof.

## What not to upload

Do not upload copyrighted books, journal PDFs, private notes that are not yours to share, passwords, API keys, tokens, email addresses, or unreviewed files titled as a final proof.

## Recommended public framing

The public question should be framed as:

> Does the smoothed Möbius approximant \(P_N\) satisfy the weighted Mellin \(L^2\) convergence above? If not, what known obstruction prevents it?

Do not ask reviewers to verify an RH proof.
