# Finite theorem artifact protocol

A finite theorem artifact is a reproducible finite computation whose claim is finite and rigorously checkable.

## Required fields

Each artifact should include:

- mathematical object;
- exact formula or interval method;
- input size \(N\);
- precision or rational arithmetic specification;
- code version;
- output file hash;
- verification script;
- theorem statement limited to finite \(N\).

## Recommended artifact layout

```text
finite_gram_artifacts/N_050/
  theorem_statement.md
  matrix_interval_bounds.json
  cholesky_certificate.json
  verification_script.py
  output_hashes.txt
```

## Forbidden language

Do not describe finite artifacts as proof evidence for RH. Use:

```text
finite diagnostic
finite theorem artifact
certified finite computation
```

Do not use:

```text
RH proof evidence
near proof
statistical proof
```

## Minimum verification standard

A finite Gram artifact should make it possible for another person to rerun a verifier and check the finite claim without trusting a plotted graph or an informal numerical transcript.
