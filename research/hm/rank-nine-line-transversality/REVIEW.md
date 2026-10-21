# Independent review of actual beta-point and line first-order geometry

Verdict: accepted as a structural characteristic-zero proof, with the two wording precisions below incorporated in the frozen proof. This is an independent mathematical review, not formal proof-assistant verification. No selected actual HM/source evaluation or numerical computation was performed.

Reviewed PROOF.md SHA-256: 7d5401bec6a16c8bafd738d5dec74bf55013c415f11f19fa24d1ed20a0e22de1.

## Checked dependencies

The proof explicitly depends on PR562 at 86b643fe2adecbd321d1c8f98be84fe2082bcd10 (25 geometric beta points, rank nine everywhere on their radical lines, smooth section-incidence model) and PR561 at 7ebf187d7e45d43763bbf07436460f3c951aa8bd (exact universal beta incidence chart). Its representation convention was independently verified against the freshly fetched full-normalizer interface at 7bf725bcd857a2deb975f9ecb80fca32e7833ae0 and the HM1973 appendix character table.

## Checks

1. The dual-number graph construction is flat and functorial on the rank-two open. The zero-wedge equations imply scheme-theoretic containment in the decomposability incidence by the Plucker equations. A torsion section has normal bundle O(-5), hence no embedded first-order deformations inside Z. Recovering the image line, its Segre hyperplane, and the nondegenerate inverse pairing recovers projective k over dual numbers, not only on C-points. Thus the actual zero-wedge scheme has zero tangent at each of its already-classified 25 points. Nakayama does imply each local ring is C, so length 25 and reducedness here are justified.

2. At a beta net the differential of all wedge entries kills precisely the two skew 3-by-3 matrices: the symmetric mixed components and the three z components are detected. Thus the universal zero-wedge tangent equals the six-dimensional beta tangent. Actual zero-wedge rigidity therefore gives injectivity into the 15-dimensional beta normal space, not an unjustified surjectivity assertion.

3. The representation mismatch is decisive and valid. The even beta representation B is U'. The invariant rank-two tensor identifies the odd part of V with W'. Taking odd parts of Sym²A=V tensor U gives B tensor C=W' tensor U=6 irreducible. Therefore C is the other odd two-dimensional representation and Sym²C=U, not U'. This avoids an unsupported choice of Galois labels.

4. Parity makes the even three-dimensional actual tangent map isomorphically to the z normal space. The odd six-dimensional actual tangent injects into Sym²B tensor C=(1+5) tensor C. There is no map to C and exactly one copy of 6 in 5 tensor C. With 5=Sym⁴C and 6=Sym⁵C, this is precisely the polarization/contraction channel up to a nonzero scalar. Evaluation on any nonzero radical covector is the directional derivative Sym⁵C -> Sym⁴C, rank five in characteristic zero. This is a universal representation calculation and not a selected actual evaluation.

5. In the exact radical incidence, the three z derivatives kill the even variations, the contraction kills five of six odd variations, and the projective radical variable contributes one dimension. Hence incidence tangent dimension is two at every point of the 25 fibers. On the rank-nine neighborhood, a unit nine-by-nine minor solves the annihilator variables scheme-theoretically, identifying this incidence with the actual maximal-minor rank-drop scheme. Thus the intrinsic first-normal derivative in P4 has rank exactly two everywhere along each line.

6. Globally, the directional-derivative kernel over P(C*) is O(-5): its vector is the fifth power of the line annihilated by the tautological covector. Quotienting the incidence tangent kernel by the vertical tangent O(2) identifies this with the transverse tangent kernel. Forgetting k preserves this quotient through the scheme isomorphism. Consequently the normal-kernel line O(-5), image degree eight, and cokernel O(1) all have the stated degrees. The extension of O(-5) by O(2) splits because H¹(O(7))=0.

## Required wording precisions

- Any nonlinear elimination of the three z equations using the invertible even derivative is formal or étale local. The tangent-space computation itself only needs linear elimination and is valid directly. Avoid suggesting an unproved Zariski-coordinate polynomial elimination for the actual nonlinear family.
- The notation T_D|L must mean the kernel of the restricted ambient Jacobian, equivalently Hom_O_L(Omega_D tensor O_L,O_L). It should not silently mean the restriction of the tangent sheaf Hom_O_D(Omega_D,O_D), since restriction and duality need not commute. The current explicit definition correctly addresses this.

No smoothness, local dimension, full determinantal reducedness, normality, higher-jet lifting, or algebraicity follows from this tangent computation alone. In particular the conclusion is not transverse cutting of a smooth reduced line. The proof correctly preserves these boundaries.

## Companion

KERNEL-SPLITTING.md supplies an independently checked complementary proof that the Euler-quotient evaluation kernel on each line is O(-1) plus two O(-4)'s, as ordinary vector bundles. Together with exact derivative rank two this identifies its balanced summand with the rank-two image of the dual normal map, and reproduces the normal-kernel O(-5) by degrees.
