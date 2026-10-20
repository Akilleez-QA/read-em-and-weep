# Independent mathematical review

Verdict: PASS for PROOF.md with SHA256

    e85b89c73c1a354721d053190d6b4455754146bc92e3060951bba8363b5ec55b

This verdict covers the edition containing the punctured Cayley curve with no nonzero exceptional parameter in its domain. It is a mathematical review, not formal machine verification. The earlier results are used with the exact dependency commits listed in the proof.

## Checks

1. The orthogonal Lie algebra is the exterior square of the transported five-dimensional representation. Its SL2 decomposition is Sym6 direct sum Sym2. The embedded Lie algebra is the unique Sym2 summand. Here the transported SL2 subgroup means the image of SL2, whose central kernel does not affect the representation or Lie algebra argument.

2. The projective tangent map is equivariant, vanishes on Sym2, and has either zero or injective restriction on Sym6. The zero possibility would make the projective line invariant under connected SO5. Semisimplicity then makes the vector invariant. Transitivity on the smooth quadric, together with the nontrivial positive degree of O_Q(3) on a line, excludes a nonzero invariant section. Consequently the projective orbit has dimension seven and its stabilizer dimension three.

3. The projective bad-factor locus has dimension at most five by the pinned PR459 result. Its pullback through the orbit map has dimension at most eight, since every nonempty fiber is a coset of the three-dimensional projective stabilizer. This establishes a closed exceptional envelope of codimension at least two, without assuming invariance of the HM bundle or of W_Q.

4. Outside this envelope, W intersect (u,v_h)_5 vanishes. Smoothness makes u irreducible, and the nonzero restricted cubic makes the pair coprime. The hypothesis excluding component lines from Q eliminates the residual map's common-line kernel. The residual quotient therefore vanishes, and uM1=M3 eliminates the primary part. This proves full Q5 vanishing, not merely residual vanishing, under the stated fixed-quadratic hypotheses.

5. The Cayley formulas are mutually inverse on the stated principal opens. The skew relation gives orthogonality; similarity of A and -A^t gives equality of the two determinants and hence determinant one. The exceptional subset in the ten-dimensional Lie algebra chart has dimension at most eight. Its nonzero radial image has closure of dimension at most eight in P9. Choosing a direction outside that closure excludes every nonzero multiple in the exceptional subset. The resulting curve is regular on the determinant principal open containing zero, preserves u exactly, and is good at every nonzero parameter in that domain. Its excluded determinant roots form a finite set.

## Scope

There is no special-fiber conclusion at zero, no selected original HM/source-instance evaluation, and no inference of first-order escape, torsion length, lower-order vanishing, module lifting, or quantization algebraicity. The fixed quadratic must lie in the stated good open. The proof does not assert that this has been verified for the original quadratic. No substantive correction is required.
