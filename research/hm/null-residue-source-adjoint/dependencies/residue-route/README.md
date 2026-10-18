# Rational residue certificates: theorem and independent finite-bound audit

This portable packet contains a new conditional mathematical route, not an actual retained-test certificate. No physical ID0 value, production vanishing theorem, execution admission, or resource claim is established.

## Read order

1. `original/PROOF.md`: finite Laurent residue vanishing is equivalent to Laurent or rational divergence; exact polynomial certificate interfaces; geometric and derivative boundaries.
2. `independent/REVIEW.md`: independent acceptance, a denominator-one completeness theorem with explicit total-degree and componentwise degree bounds, and a counterexample to dropping Laurentness.
3. `logarithmic/PROOF.md` and `independent/LOGARITHMIC-REVIEW.md`: exact logarithmic-tangent parametrization and the explicit complete weighted-Euler baseline.
4. The three checkers: distinct invented examples and negative mutations only.

The independent result sharpens the original statement about arbitrary fixed search bounds: under Laurentness, denominator exponent m=1 with numerator degree at most deg(pN)+1 is complete. Failure at smaller, arbitrary bounds remains inconclusive. The original packet is retained byte-for-byte rather than silently revised. The complete bound is finite but may be computationally enormous.

Both documents require the SAME complete extracted scalar, authenticated as a finite Laurent representative of the intended class, with the fixed trace orientation. They concern ordinary x-coordinate derivatives after extraction. They do not substitute physical curve derivatives, introduce another deck division, or discharge the geometric/source premises.

## Reproduce

From this packet directory:

    sha256sum -c SHA256SUMS
    (cd original && sha256sum -c SHA256SUMS)
    python original/check.py
    python -O original/check.py
    python independent/check_independent.py
    python -O independent/check_independent.py
    python logarithmic/check.py
    python -O logarithmic/check.py

The original checker uses only Python's standard library. The independent and logarithmic checkers use SymPy, tested at version 1.14.0 (see requirements.txt). All run entirely offline without production imports or input files. Only the original checker output is JSON; the other outputs are ordinary Python dictionary text. Recorded normal and optimized outputs agree for each checker.

The checks validate only the invented identities and mutations. Mathematical completeness and the exact scope are supplied by the written arguments, not claimed as mechanically formalized proofs.

## Contents and provenance

See PROVENANCE.md. All integrity manifests use relative paths. No network fetch or publication is part of replay.
