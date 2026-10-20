# Independent audit of ADDENDUM.md

## Verdict

PASS. During the audit, the author explicitly restricted the two closing scope sentences of Section 4 to nonconstant middle image, as required by the proof. This resolves the sole clarification identified. No mathematical gap remains.

## 1. Reconstruction and exact fibers

For rank-two quotient factors a,b, write v(ab)=c a+d b. Their independent factor lines make c,d unique after representatives are chosen. Expanding the trilinear map gives the unique projective lifts a-d u and b-c u. They remain linearly independent with u, because their quotient classes are independent. Exchanging a,b gives precisely the second ordering. Thus the ordered zero fiber is a finite factor reconstruction of the compatible rank-two locus and has the same dimension.

The displayed full type III kernel has no nonzero square and has rank-two locus exactly the union of the cubic scroll S and the transverse common-factor plane P. Dense scroll compatibility therefore extends to every point of S, since compatibility is closed on the rank-two locus. A compatible S gives dimension at least two, and the full rank-two locus gives the matching upper bound.

For q=y(Ax+Bz+Cw), the correction modulo y has coordinates (alpha A, nu B, nu C). Its proportionality to (A,B,C) is exactly delta AB=delta AC=0. If delta is nonzero, this gives A=0 or B=C=0. The first is the line y span(z,w), obtained at s=0 on S; the second is xy, obtained at t=0,a=0. Thus it adds no points outside S. If delta is zero, all of P is compatible. The stated lifted common-factor rectangle in the latter case follows by direct expansion. Its polar kernel contains a three-plane, putting the middle in F.

Verdict: all assertions in Section 1 valid.

## 2. Generic scroll components and affine dimensions

The subset of middles carrying a compatible explicit type III scroll lies in the closed middle image of R. If a dense open of B has this property, all of B lies there. Hence dim B is at most one, independently of any separate middle rank-drop dimension bound.

The generic full projective zero fiber has dimension two. An individual component's generic fiber can be smaller, so the inequality dim C at most dim B+2 is the correct general statement. If the ordered scrolls dominate the component, the generic fiber is two-dimensional and equality follows.

Projectivization independently divides out the three nonzero input scalings. Over the independent projective locus the affine locus is a principal (C*)^3 bundle, giving exactly three dimensions back; closure does not change dimension. This proves the stated affine upper bound six and the exact values five or six in the scroll-dominated case.

A nonconstant middle curve avoids finite F generically, so delta is nonzero generically. The extra plane of the displayed type III kernel is compatible only over F. No boundary rank condition is used to bound the component's generic dimension.

Verdict: valid, with appropriate distinction between the full fiber and the fiber of one total-space component.

## 3. Conditional bound for the explicit kernel family

For types I and II, the cited full-kernel compatible-locus dimension bound is at most one. A middle dimension at most two then yields affine dimension at most six.

For type III, any compatible surface is dense in S or P, since those are the only two-dimensional components of its entire rank-two locus. Dense compatibility is closed on that rank-two locus. The scroll case is controlled by the middle image of R. In the plane case, the correction calculation for a transverse common-factor plane gives v(ell a)=lambda a+mu(a)ell. Its unique lifted factor line has a three-plane in its polar kernel. It therefore gives a point of the finite polar-pair locus and a middle in F, without requiring prior scroll compatibility.

Thus a two-dimensional middle image cannot generically carry a two-dimensional fiber. If its image has dimension at most one, the universal fiber bound two suffices; if the image has dimension two, the generic fiber bound one suffices. Both give total projective dimension at most three.

Verdict: valid under the separately stated dimension-at-most-two middle support hypothesis and the explicit generic full-kernel classification. No conclusion about unclassified rank-five kernels follows.

## 4. Finiteness away from F

For fixed u outside F, every pair in R_u is complementary. On a reduced irreducible projective component of that fiber, the complementary projector is globally regular and hence constant. Its image and kernel determine the pair, so the component is a point. Noetherianity makes the support finite. Over C and finite-type varieties this gives quasi-finiteness over the complement of F; properness then gives finiteness.

Any irreducible component with nonconstant middle image consequently has dimension one: its image has dimension one by the main theorem and its generic fibers have dimension zero by the preceding argument. Vertical components over F need not satisfy this argument and are correctly excluded from its earlier formulation.

Verdict: valid. Fiber reducedness, etaleness, and degree one are not implied or claimed.

## 5. Degree and boundary formula

On the normalization T of a nonconstant-middle curve component, the addition map X_T direct-sum Y_T -> V tensor O_T is an isomorphism generically. Its determinant is a nonzero section of

    det(V tensor O_T) tensor det(X_T)* tensor det(Y_T)*.

The first factor is a constant one-dimensional vector space and has degree zero. Hence the zero divisor has degree d_X+d_Y. A determinant vanishes exactly where the addition map fails to be an isomorphism, namely where X and Y fail to be complementary. The boundary lemma places its support over F.

The determinant duals of the tautological bundles are the pullbacks of the Plucker ample line bundles. Their degrees are nonnegative, and on a complete integral curve degree zero is equivalent to the associated Grassmannian map being constant. Thus a varying map forces positive total degree and a point over F. Conversely zero divisor is equivalent to both maps being constant; their generic complementarity then makes them complementary everywhere.

If the pair is constant, the reduced component is B times that pair because it is embedded in the product and its middle projection has exactly that image. Its normalization is the normalization of B and maps birationally onto B.

Verdict: valid for nonconstant-middle curve components. Repeated zeros and ramification are correctly allowed. The final paragraph now retains this hypothesis explicitly: vertical curve components over F can have determinant identically zero, in which case an effective zero divisor of a nonzero section is not defined. For a family with nonconstant middle image, its irreducible image closure in R is a curve by finiteness off F; this justifies performing the degree calculation on its normalization even if the original parameter space has larger dimension.

## Audit scope

The checks used the main proof and its finite-polar argument, the explicit full-support scroll formulas, and the transverse plane correction calculation.  This file records mathematical verification only.
