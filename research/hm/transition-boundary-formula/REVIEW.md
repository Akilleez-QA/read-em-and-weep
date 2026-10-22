# Independent review: faithful linear vertex boundary formula

## Reviewed artifact and verdict

- Artifact: `PROOF.md`, “A faithful linear vertex formula for the fifth adjoint boundary.”
- Reviewed SHA256: `145ccbe882067fe5f20ea7d6a7de7b089fcafdc69bdca33105ae44e6ed33e085`.
- Verdict: **PASS within the stated pinned-dependency scope.** No unresolved mathematical defect was found in the new comparison, ordered cocycle formula, or harmonic-order exclusion.
- This is an independent authored mathematical review, not a proof-assistant certificate or an evaluation of the actual fifth obstruction.

The final artifact includes three clarifications made during review: the correct category for physical-even objects, an explicit PR775 citation for the global total-weight bound and harmonic convention, and the exact vanishing of the total-weight-twelve overlap discrepancy. All were checked in the hash above.

## Dependency verification

The seven directly relevant proofs were fetched at their stated immutable commits. Their fetched Git blob hashes matched the local copies read during review:

| Dependency | Commit | Git blob |
| --- | --- | --- |
| PR770 | `b242300110c33627eb77ee5ab36cc81fffa359e4` | `dd0489148189fdc8dfd8d9c18dd8f2d8ea32761f` |
| PR773 | `53209eb6d4e45883ce0f31dd6d9b1c191bd6c4a3` | `a56dba203fe27dda0aebcec5a3b21dd89ba70f32` |
| PR774 | `eec909bef4a7e6998737773d5eadd0ad562e79d9` | `79b6df5441d7d9bf7038f9de5a7e1756f9ca784d` |
| PR775 | `af2fc052d3da2c4abc315dca268ed65b62f5cde5` | `131cd1ad758f234e54ef927601e7ffddb68b193d` |
| PR777 | `490337fee9e8f06fa8bf3e893ab646a37f996bf2` | `e1a3527b680aec043d55a10c0f7aa35ef34e2b9d` |
| PR778 | `e527b939f9a8f5cf8967f32048a23a9d830d77c9` | `db704f5e6b018c9c30e436d2c5ff78561c2dec7f` |
| PR779 | `89e02759fde0924a787a8f145d814aceaab93c40` | `bf73ab4134261db7789b9865bc0f2fb05e6922bb` |

This checks the interfaces used here, rather than independently reproving every foundational theorem cited by those dependencies.

## 1. The whole-cone faithfulness argument

The physical-even convention is now explicit and correct. For the finite quotient by physical inversion, invariant direct image is exact in characteristic zero, and its cohomology agrees with the positive eigenspace of the original cohomology. The positive part is not treated as an O_Q-submodule stable under odd multiplication. Equivalently, all cochain constructions can be made on a stable cover and passed to its positive summand.

PR773 supplies the actual stack-square vertex quotient and its first even relation in J-order four. Modulo J^6 there is no further even layer. Consequently the kernel A_L has the stated quotient P4 O_L(-2), with kernel J^6 O_Q(6). This does not require a homogeneous splitting of the actual square thickening.

The ambient even jet quotient has coefficient bundles O_L(6), Sym4 U tensor O_L(4), and Sym8 U tensor O_L(2). Their H1 vanishes, and global homogeneous polynomial pieces lift their global sections. The long exact restriction sequence therefore gives both claimed tail vanishings: H1(J^6 O_Q(6))_+=0 from H0 surjectivity, and H2(J^6 O_Q(6))_+=0 from H1 of the quotient and H2(O_Q(6)). The second vanishing is necessary for the asserted H1 isomorphism and has been supplied.

The conic normalization is the actual global map from PR773. Its even conic sections lift by degree-twelve cover polynomials vanishing on the vertex quotient. Thus the argument includes the whole cone rather than only a formal neighborhood of L.

For X0=[[x,0],[z2,-x]], direct trace gives u(2 f3 g5 x-f3^2 z2). Its image is precisely the actual degree-eight relation span. In every fiber, regularity of (f3,g5) forces x=z2=0 if this trace is zero. The rank-four maps are therefore fiberwise isomorphisms with the actual nonsplit transition law. The twists agree with tau:B_Q(4)→O_Q(6).

Only weight zero of a regular even adjoint can contribute to trace degree eight because N begins in weight eight. This proves commutativity of the leading-extraction/trace square. PR770, conic normalization, the tail vanishings, and the actual relation-bundle isomorphism then prove that E is an isomorphism. This is not a dimension-count substitute for map comparison.

## 2. Ordered overlap formula and transport

PR775 supplies K≥12 globally in regular adapted physical frames, with subsequent possible weights 16,20,… . PR777 removes B0 locally and transforms all remaining coefficients simultaneously. Choosing local fifth lifts with B4=0 changes the boundary only by a coboundary.

For T=T0(I+qZ+weight≥8), expansion of adjoint transport gives Ad(T0)K+q Ad(T0)[Z,K] at the required precision. With the specified boundary convention K_i−Ad(T)K_j, the correction therefore has the minus sign in (7). Terms involving transition weight at least eight and K12 start in total weight twenty, so cannot affect the weight-zero boundary after division by q^4. The K12 discrepancy is q^4-divisible because K glues on 4Q and the transition correction raises weight by four. Its quotient would have matrix weight minus four, impossible for a regular physical-even matrix, so this discrepancy vanishes identically in the ambient reference.

The local equation, coordinate substitution, and twist-twelve scalar factor are transported before harmonic extraction. Division by q^4 therefore gives physical twist four. The normal coefficient Z retains the negative ideal-line twist from PR778. Scalar factors in the bundle-frame transition do not change conjugation; this does not delete the separate line-bundle scalar transport.

The exact multiplicative ambient lift of T0 is essential and is supplied by PR778. No general harmonic lift is assumed multiplicative. The actual nonzero κ from PR779 remains present through the Z terms.

## 3. Algebra, harmonic orders, and explicit coefficients

Independent direct multiplication verifies (8) and (9), including every minus sign, factor of two, and denominator alpha or delta. In particular [Z,X] has diagonal −ell y, upper 2t y, and lower 2ell x−2t z before T0 conjugation.

The harmonic degree bound is valid for the fixed nondegenerate transverse quadratic: multiplying a homogeneous harmonic polynomial by one linear form produces only harmonic orders zero and one. Iteration over products of linear forms and linearity give D_r(p,v)=0 for r greater than the ordinary transverse degree of p, including nonharmonic p such as c^2.

All multipliers in the conjugation and commutator-conjugation formulas have transverse degree at most two. Thus B1 and A0 require impossible order-three terms. The remaining orders are exactly 2,1 for B2,B3 and 2,1,0 for A1,A2,A3.

Applying those orders to (8) and (9) reproduces every entry of M2, M1, N2, N1, N0 in (10). The upper entries vanish. A3 has y3=0, x3 of degree zero, and z3 of binary degree two, so its N0 contribution needs no harmonic correction. Every retained diagonal has binary degree zero, and every retained lower entry has binary degree two. Since the local K_i16 has no q^4 coefficient after B4=0, (11) has exactly the five displayed minus signs.

## 4. Exact quotient and limitations

The resulting class is E(delta5 K), so its vanishing is equivalent to extension of the fixed fourth lift. For classified completion changes, one must still quotient by the exact subspace E(im beta2_a). Equation (12) does so without rank assumptions, saturation, or source inversion.

The B1 exclusion concerns this full compatible linear boundary cocycle. An isolated B1 summand in the quadratic norm expression need not be a cocycle and is not shown separately exact or pointwise zero. The final text states this limitation correctly. Likewise κ≠0 does not imply a nonzero pairing with the chosen section, and no value or vanishing decision for beta4 follows from this review.

No actual coefficient, point, source instance, derivative value, or matrix rank was evaluated; no scan or large computation was used. The only machine checks were source retrieval and artifact hashes.
