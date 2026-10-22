# Independent structural review

Verdict: PASS, conditional on the pinned geometric inputs.

Reviewed artifact: PROOF.md

SHA256: 9d8afba9e244b5a51aca54a46559ca002556fed1f4d8fb2509ae522be442f3e9

This is an independent mathematical review, not proof-assistant verification. No selected actual HM/source coefficient, point, matrix, derivative, or rank evaluation was performed.

## Checks

1. The normalization cohomology input retains H1(M,D) of dimension five. The normalization sequence, splitting of the constant complex, and Ext1 from a free module give the two-term model R^10 -> R^65 with five zero rows. The degree-one cokernel commutes with arbitrary base change. No false arbitrary base-change assertion for H0 is used.

2. Fitt_(54+r)(R1 p_* L) is intrinsic and equals I_(11-r) of that model. This fixes the scheme convention independently of bases, splitting, and presentation. Its field-valued condition is exactly h0>=r because h1=55+h0. The text correctly separates these determinantal conditions from existence of torsion sections over Artin bases.

3. The elementary Heisenberg representation argument establishes uniqueness of the irreducible representation for the fixed primitive central character. It justifies the five-copy factorization, not merely dimension divisibility. Pairwise complementarity gives nonzero two-row constants, hence I1(B)=m and I2(B)=J.

4. The block-minor argument proves equality of ideals in both directions: every nonzero minor is a balanced block product, and each such product is realized. The feasible exponents satisfy 2a+b=k and a+b<=5. The containment J⊂m² makes the term with a=max(0,k-5) contain all others. This verifies every threshold ideal, including the overlap at k=5.

5. The squarefree axis decomposition and its preservation under torus localization are correct. At an axis generic point the ideal becomes the (6-r)-th power of the eleven-variable transverse maximal ideal. The length binomial(16-r,11), including 1365 for r=1, follows by monomial counting.

6. The embedded-identity witness f=x1^4 x2^4 x3 has degree nine and survives modulo J^5 after localization. Every displayed x_i f factors into five generators of J. Therefore its proper annihilator is the maximal ideal m. This proves an embedded associated point without claiming an unsupported full primary decomposition.

## Scope

The conclusions concern the actual constant-underlying-scheme, U-fixed algebraic polarization family. They do not settle the original adjoint/source problem, higher-order adjoint claims, or algebraicity. No mathematical correction remains outstanding for this artifact hash.
