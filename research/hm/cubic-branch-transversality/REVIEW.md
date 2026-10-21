# Independent mathematical review

**Verdict: PASS.** The conclusions follow from the stated predecessor theorems. No mathematical correction is required. This is an independent structural review, not a machine-checked proof or a re-verification of the original geometric source.

Reviewed `PROOF.md` SHA256: `efe5fe70443bbc77c3a2efd0f761c320fc7cc384f878123bf6bc860363dc05cd`.

Reviewed the complete `PROOF.md`, with particular attention to Sections 2–3 and 6–7, against the supplied joint-character, fixed-direction, primary-conductor, and conductor-blowup proofs. No GitHub fetch, selected source coefficient, matrix, point evaluation, numerical rank test, or computer algebra was used.

## Checks

1. **Blowup differential.** Dividing the universal cubic expansion by `3t` gives the displayed local lift. At the exceptional mark, the three exceptional derivatives are `q(u^2 w_m)` and the normal derivative is `q(u v^2)`. Adding the value line gives precisely the five generators in equation (1). The normal generator is nonzero directly by PR610 Section 5 with the indices interchanged: `q(L_i L_j^2)=q(L_j^2 L_i)`. Thus this step does not assume unramifiedness to prove tangent injectivity.

2. **Universal character supports.** The affine relabeling changes joint labels by the displayed invertible affine transformation; no geometric symmetry is being assumed. For the representative paired marks `(0,1)` and `(4,3)`, both five-element support lists are correct. Their intersection consists exactly of `(1,1)`. The one-dimensional target weight spaces and nonvanishing establish both dimensions five and intersection equal to the common value line. Passing to `Hom(ell_y, W*/ell_y)` therefore gives zero intersection of the four-dimensional projective tangent images. Restricting through the smooth closed immersion `Y -> M` proves the same assertion for the two-dimensional surface tangent images.

3. **Completed image ring.** Finite completion preserves the normalization inclusion and splits the completed normalization into its two smooth factors. Injective differentials make each completed ambient-to-branch map surjective. The kernels satisfy `I_1+I_2=m` by the stated cotangent-space calculation and Nakayama argument. The two-ideal exact sequence then proves the fiber-product ring, rather than merely predicting it from tangent dimensions. All points involved are closed complex points, as needed for residue field `C`.

4. **Conductor and local invariants.** The residue-difference cokernel has length one and annihilator the maximal ideal. Faithful-flat descent gives the reduced conductor downstairs and the reduced 120-point ideal upstairs. The local-cohomology argument proves depth one for dimensions two and four. The displayed powers of the maximal ideal and length formula give multiplicity two and embedding dimension `2d`. The text correctly distinguishes the point ideal from an invertible ideal or divisor.

5. **Global cohomology.** Global normalization functions are constants and map to zero in the residue-difference quotient. The resulting additional sixty dimensions in `H^1` and the unchanged higher cohomology follow from the exact sequence. Blowup invariance of structure-sheaf cohomology gives exactly `(1,60,0,0,0)` for `V` and `(1,60,4)` for `T`.

6. **Riemann–Roch and Hilbert polynomials.** On the surface, `H_X.K_X=15`, `E_Y^2=-60`, and the mixed intersections vanish, so `D_Y.K_Y=45+60=105`. Surface Riemann–Roch followed by subtraction of the length-sixty quotient gives the asserted `P_T`. On the ambient blowup, the successive exceptional quotients are `O_(P3)(j)` for `0 <= j < n`; their Euler characteristics sum to `binom(n+3,4)` for each of thirty centers. This proves the asserted `P_V` without any fat-point independence assumption. Polynomial continuation to all integer twists is valid. Constant terms agree with the independently obtained Euler characteristics, and the ambient leading coefficient is `51/24`.

## Boundary

The proof establishes transverse branch images, the completed local algebras, conductors, normalization defects, cohomology, and Hilbert polynomials. It appropriately makes no assertion identifying the full scheme-theoretic singular locus with the reduced conductor, and does not advance the separate full-adjoint, prescribed-source, higher-lifting, or algebraicity gates.
