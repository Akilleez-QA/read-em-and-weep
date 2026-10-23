# Independent review: ten exceptional pure-V quadratic directions

Reviewed 2026-10-23 UTC separately from the author's self-check.

- Final PROOF.md SHA-256: `a62f8f6266601987fbfb2f67690a912a9eb9ccb41b04e1d8915652e545390ac4`
- verify.py SHA-256: `7b8ff495465ad873d58641efa5bc1671f2c56991af16712dd78a5bc408765d4b`
- INPUTS.json SHA-256: `9abaad801f01032ba9612a6e53ccdbc256c814bf0fd711ec6a221a1f422a5773`

Verdict: PASS on these final frozen bytes.

## Independent mathematical assessment

Read the full proof and verifier and checked their exact PR792/950 interfaces.
The proof correctly studies the genuine pure-V image quadratic map, not the
full obstruction map or the non-equivalent pure-V quotient problem.

1. The divisor sequence for a nonzero quadratic gives the exact restriction
   formula rank(T_a)=2+rank(V6 -> H0(O_{Z_a}(6))). Basepoint freeness excludes
   rank zero of restriction even on a doubled divisor. For distinct points
   the failure is precisely equality of projective images; on2p it is
   precisely failure of the differential, not just equality at the support.

2. The Wronskian transformation law has line bundle L^3 K_X^3=O12 for
   a g^2_6. Changing the section basis multiplies by its determinant, so
   the divisor is invariant, irrespective of a chosen scalar normalization.
   The Vandermonde leading coefficient proves it is nonzero in characteristic
   zero. A failed differential has vanishing sequence at least(0,2,3),
   hence weight at least2. Invariant orbit size at least12 would then
   contribute at least24, contradicting degree12. Thus the proof establishes
   everywhere immersion and all-square rank4, not merely generic behavior.

3. The normalization factorization is valid. A positive-degree morphism
   from P1 to a smooth projective curve forces genus zero by Riemann–Hurwitz.
   A cover of degree greater than one would ramify, and its derivative
   would force the derivative of the composed plane map to vanish there.
   Hence the map is birational onto its image. Distinct identified pairs
   consequently occur only over finitely many singular points. Doubled
   divisors are already excluded. This establishes finite degeneracy before
   applying intersection theory.

4. The universal degree-two divisor sequence yields a rank-two locally
   free secant bundle with presentation5 O(-1) ->7 O -> E6 and determinant
   O5. At every point the evaluation matrix has rank at least1. A unit
   pivot reduces its remaining part to the row(f,g); at a degeneracy point
   finite support means height two. In a regular local surface ring this
   is a regular sequence. Its syzygy is free rank one and its cokernel
   is R/(f,g), up to the harmless local line factor. Thus the global kernel
   is genuinely a line bundle, not a rank-one sheaf with hidden singularity.
   The determinant identity off a codimension-two set extends to give O(-5).

5. The resulting K-theory identity gives length10: the Euler characteristic
   is4χ(O)-5χ(O(-1))+χ(O(-5))=4+6. This calculates the determinantal scheme
   length without assuming reducedness or an ordinary-node model.

6. The final Section5 clarification correctly identifies the two cokernel
   sheaves canonically with7 O/(V6 O + H0(O4) O(-1)). Their zeroth
   Fitting ideals are consequently equal. Thus the secant evaluation
   degeneracy scheme is precisely the actual T_a maximal-minor scheme,
   not merely the same rank-drop set. The requested clarification is
   incorporated and independently checked.

7. The unordered-pair stabilizer has pointwise subgroup cyclic of order
   1,2,3 or5 and index at most2. The listed orbit-size superset is therefore
   valid and has minimum6. Invariance forces equal integer local lengths
   around each orbit. Total length10 allows only one orbit of size10 with
   local length1. Its pointwise stabilizer must have order3, since point
   stabilizers cannot have order6. The ten cyclic order-three subgroups
   have disjoint pairs of fixed points, giving the single20-point orbit.
   No selected actual roots or coordinates enter this classification.

8. The optional formal image-complex calculation is correct: for fixed
   rank k, tT_a has free kernel rank5-k and cokernel free rank4-k plus
   k copies of R/(t). These groups are expressly not transferred to the
   full obstruction complex, and no acyclic image cancellation is asserted.

## Supporting execution

Ran both `python verify.py` and `python -O verify.py`:76 checks pass with
byte-identical output. Both immutable input SHA-256 and Git blob checks pass.
The checker includes exact Wronskian leading determinants and weight bounds,
Euler characteristics, invariant local-length possibilities, and an A5
permutation-group calculation. These are universal symbolic/combinatorial
checks, not actual HM coefficients, points, or ranks. The local regular-
sequence and normalization arguments are established by the written proof,
not by the finite checks.

The theorem is conditional on the pinned genuine image identification.
It establishes neither existence of a compatible pure-V radical nor full
adjoint surjectivity, a source cut, or a complete original repair. This
independent review is supporting verification, not an additional new result
or a proof-assistant certificate.
