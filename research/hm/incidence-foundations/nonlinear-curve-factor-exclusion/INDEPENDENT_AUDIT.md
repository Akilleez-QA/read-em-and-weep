# Independent audit: nonlinear curve factor exclusion

## Verdict

Final-version verdict: PROOF.md, Sections 1–4 and the point-projection argument in Section 7, are correct over C under their stated hypotheses. The nonlinear-curve structural exclusion does not need compatibility or square avoidance. The revised proof uses the elementary annihilator-pencil argument audited below, with no ternary-web dependency. Section 7 correctly reduces compatible point-projection surfaces to the finite (1,3) rectangular incidence. The remaining two-surface-projection case is explicitly left open.

This audit checks abstract tensor arguments only. It does not independently certify the separate finite-middle theorem invoked in Section 5.

## Detailed checks

1. A nonlinear integral curve spans at least three vector dimensions, so three independent general first factors exist. The direct sum of their three-dimensional multiplier spaces has dimension at least nine. Symmetrization on U tensor E has kernel wedge²U, of dimension three. Thus the claimed contradiction with dim K=5 is valid.

2. With generic multiplier dimension two, the full projectivized multiplier incidence over a constant-rank dense open is an irreducible surface. The given ordered-factor component is dense in it. This justifies using every generic multiplier, not merely the initially chosen surface points. No globally split bundle or unsaturated kernel is being assumed.

3. In the nonplanar case, the quotient kernel is exactly l0 M_l0, so the quotient tensor space has dimension three. Failure of generic injectivity of M_l under projection is precisely l0 in M_l; because C spans E, this would force l0 E inside K and dim M_l0=4. The projected curve is nonlinear since the inverse image of a projective line under point projection is a plane through the center.

4. The projected ruled incidence genuinely has dimension two. The map C to its projected curve is nonconstant and hence generically finite. A full projective line of second factors survives over a general first factor. Multiplication of projective ordered factors has finite fibers, so its image is a surface. The possible square points do not lower the dimension: in each surviving two-dimensional multiplier space at most one projective direction is proportional to the first factor. Thus there is a dense rank-two open.

5. The ternary bounded-rank plane classification gives exactly the binary and common-factor alternatives. In the first, every first factor lies in the binary two-space. In the second, away from the fixed common factor, every second multiplier lies in its one-dimensional span. These contradict respectively nonlinearity and multiplier dimension two.

6. In the planar transverse case, K/K0 has a three-dimensional subspace of images l w, since C spans U. Therefore dim K0≤2. The inner products l n_l cannot be constant: one nonzero quadratic has only finitely many factor lines. Their pencil is consequently entirely singular. The explicit determinant calculation in Section 3 is correct. It includes pencils with square members; a two-dimensional pencil cannot consist entirely of rank-one tensors. Binary and common-factor pencils have factor images contained in finitely many lines and points, excluding C.

7. Once all multipliers lie in U, the complete surface lies in Sym²U by closure. Its span has vector dimension at least three and at most five. The dim-five branch contradicts full support. The revised dim-three branch uses bounded-rank plane factor geometry directly. The revised dim-four branch uses the annihilator-pencil radical argument detailed below. Neither requires compatibility or square avoidance.

## Elementary strengthening of Section 4

Let H be the vector span of the surface after the planar reduction. We may exclude dim H=3 or 4 without any map v.

For dim H=3, the surface is all of P(H), and H has upper rank two. If H=Sym²W, every factor lies in P(W), a line. If H=eU, the ordered-factor preimage has precisely the two components

    {e} × P(U),       P(U) × {e}.

Their first projections are respectively a point and a plane. Neither is a nonlinear curve.

For dim H=4, let A,B be a basis of the two-dimensional annihilator of H in Sym²U*. They are symmetric bilinear forms on U. Along a general first factor l in C, all products l m for m in the two-dimensional multiplier space belong to H. Thus A(l,-) and B(l,-) are dependent.

They are not both zero for general l, since otherwise the common linear kernel would contain the spanning curve C and both A and B would vanish. Hence there is a rational map

    C --> P¹,       l --> [a:b] with (aA+bB)(l,-)=0.

This map cannot be constant: a constant value would place C in the projectivized kernel of one nonzero symmetric form, a linear subspace of dimension at most one. It is therefore dominant. Every member of the pencil aA+bB is singular, by density and the determinant equation.

Apply the elementary singular-pencil classification already proved in Section 3, now in Sym²U*. A general pencil member has rank two; a pencil consisting only of rank-one forms cannot have vector dimension two.

- For a binary pencil supported on W⊂U*, its general rank-two kernel is the fixed one-dimensional annihilator W-perp⊂U.
- For a common-factor pencil e f(a,b), its general rank-two kernel lies in the fixed plane ker(e)⊂U.

Dominance of the parameter map means that general points of C lie in these generic kernels. In the binary case C would be a point, and in the common-factor case C lies in the projective line P(ker(e)). Both contradict a nonlinear spanning curve. Exceptional rank-one members need no extra treatment because the rational parameter map is dominant; their finitely many parameters cannot contain the generic point of C.

Therefore a full-support five-dimensional K⊂Sym²E, dim E=4, has no integral rank-two surface with a nonlinear curve ordered-factor projection, independently of compatibility or square avoidance.

## Recheck of revised proof and point projections

The revised Section 4 integrates the strengthening correctly. Its finite-union radical-locus argument is valid, including exceptional rank-one pencil members.

The added Section 7 point-projection argument is also correct. When M_h=E, the 3-by-4 pencil T−lambda pi has generic rank three because pi is surjective and a suitable maximal minor has nonzero cubic leading term. Its generic projective kernels therefore sweep at most a curve. A compatible surface must occur at one exceptional parameter; rank zero there would make h² compatible, so its kernel has exactly dimension three. Thus every such surface is a common-factor plane hU. Square avoidance forces h outside U. The line-preserving endomorphism of U is scalar, giving v(hm)=alpha(m)h+beta m and the stated lifted (1,3) annihilation rectangle, with the conventional residual identity f(h,u,m)=A_u(v(hm)). The cited rectangular finiteness theorem explicitly permits p=1 and q=3. The new surface-projection reduction is sound; it still does not classify the remaining case with two surface projections or families with only curve fibers.
