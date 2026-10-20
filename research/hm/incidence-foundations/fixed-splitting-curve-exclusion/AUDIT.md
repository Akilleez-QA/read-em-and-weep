# Independent audit: fixed splitting and moving splitting

## Verdict

The fixed-splitting lemma is valid. The stronger moving-splitting result is audited separately in STRONGER_AUDIT.md.

## Fixed splitting: weights and rank

Let T be a smooth projective integral curve with nonconstant middle map and tautological line U of degree −d, where d>0. Fix complementary X,Y of dimensions 2,3. The established injection argument gives u outside X and Y. Set a=P_Xu, b=P_Yu. Both are nonzero and independent, with u=a+b.

Outer symmetry and cyclic zero give

    f(a,u,b)=A_a(b)+A_b(a).

These two repeated values are independent. Indeed, if A_a(b)=λA_b(a), trilinearity and cyclic zero give A_(a+λb)(b)=0, contradicting injection since b and a+λb are independent. Thus the displayed cubic never vanishes. In particular the rectangular rank is exactly one, without requiring the finite-polar theorem for this step.

The constant-rank map U⊗(X⊗Y)→J⊗O_T has image a line subbundle M, with locally free cokernel. Twisting its surjection onto M by U* shows that M⊗U* is globally generated, so deg M+d≥0. The cubic above defines a nowhere-zero map U^⊗3→M, an isomorphism of line bundles. Thus deg M=−3d, contradicting the preceding inequality. All three copies of U are essential: both projections a,b are linear in the representative u.
