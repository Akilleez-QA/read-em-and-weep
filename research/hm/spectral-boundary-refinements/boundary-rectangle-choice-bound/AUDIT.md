# Independent audit: fixed-polar choice bound

## Verdict

PROOF.md is correct: for a fixed independent rank-two polar pair, the actual boundary rectangular choices number 0, 1, or 3. The result is unconditional under the stated tensor hypotheses and does not depend on global rectangular or polar finiteness. No assertion that all three cardinalities are realized, and no scheme multiplicity conclusion, is justified or claimed.

## Descent and diagonal nonvanishing

The polar has independent values on h and u, so L is nonzero, H=P^{-1}(L) has dimension four, and u is outside H. Outer symmetry makes both h slots vanish modulo L on H; hence β descends to E=H/Ch. If β(e,e)=0, a lift v gives an L-valued binary quadratic on span(h,v). It is nonzero at h but necessarily has a projective zero over C. That zero contradicts repeated-input injection because u is outside H. This proves diagonal nonvanishing without assuming existence of a rectangle for the pair.

## Elementary nondegenerate-member check

The final proof correctly removes Bertini. Choose a scalar member q₀ of maximal rank r. If r<3, choose a nonzero radical vector k and an r-dimensional nondegenerate subspace W. All members q₀+tq₁ have rank at most r, so their restrictions to W⊕Ck have identically zero determinant. At t=0 the block matrix is diag(q₀|W,0); its determinant's linear coefficient is exactly det(q₀|W)q₁(k,k). Terms using off-diagonal blocks require at least two factors of t and cannot contribute. Thus every scalar member vanishes on (k,k), contradicting β-diagonal nonvanishing. The r=0 case is the same one-by-one determinant with the empty determinant interpreted as one.

A maximum rank exists because the possible ranks form a finite set; no compactness or genericity is needed. If J or K is infinite-dimensional, only the at-most-six-dimensional span of β-values matters. Consequently the proof supplies the nonsingular scalar member without any additional theorem or finiteness assumption.

## Eigenline correspondence and cardinality

A rectangle is exactly a β-orthogonal direct splitting E=a⊕B of ranks one and two. For a nonsingular scalar member q, necessarily B=a^⊥ and a is nonisotropic. The β-orthogonality is equivalent to a being invariant under every q-selfadjoint T_λ. Conversely, any common eigenline is nonisotropic, since an isotropic eigenvector would make every scalar coordinate of β(v,v) zero. Thus it yields a unique rectangle.

The operators need not commute. If two distinct common eigenlines had the same complete eigenvalue functional, their span would be a common eigenspace and would contain a nonzero q-isotropic vector over C, violating diagonal nonvanishing. Distinct eigenvalue functionals imply orthogonality by selfadjointness. The resulting nonisotropic orthogonal lines are linearly independent, so at most three exist.

Given two, their span is q-nondegenerate and invariant under every T_λ. Selfadjointness makes its one-dimensional orthogonal complement invariant under every T_λ as well. This produces a third distinct common eigenline and rules out exactly two.

With three, all off-diagonal β-values vanish. A dependence between the three diagonal β-values would admit complex square roots of its coefficients, producing a nonzero diagonal zero of β. Their asserted independence is therefore correct.

## Relation to the full finiteness theorem

This argument provides an alternative to projective quotient-projector rigidity for the boundary: the finite-polar theorem and the bound of three choices imply at most 3|D| boundary triples. It does not itself bound complementary triples, for which the determinant-pole argument remains necessary. The statements concern support rather than scheme length.

Abstract mathematical verification only; no numerical instance is evaluated.

## Status of this record

This is a historical mathematical audit, not a new formal verification or a new execution of tests.
