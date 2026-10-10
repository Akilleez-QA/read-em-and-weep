# The global scalar chain map and scalar comparison

## 1. Complex, indexing, and the map

Let `K` be a locally free complex in degrees `0,1,2,3`, with ranks
`5,15,10,2`. Its differentials are `gamma`, `delta_K`, and `ev`.
The homogeneous entries are linear in `v_0,...,v_4`. On the chart `v_0=1`
these matrices are encoded in `data/model.json`; a constant monomial there
represents the homogeneous variable `v_0` in a degree-one matrix entry.

An internal degree `-2` endomorphism has blocks
`X02: K^2 -> K^0` and `X13: K^3 -> K^1`. Define

\[
L(X)=X_{02}[0,0]-X_{13}[10,0],
\]

and set `L=0` on all other internal degrees. Both selected entries have
the same line-bundle transition. The two exact homogeneous identities are

\[
\gamma[10,:]=(v_0,0,0,0,0),\qquad
\mathrm{ev}[:,0]=(v_0,0)^t.
\]

For `W:K^3 -> K^0` of degree `-3`, the graded commutator is

\[
d_{\mathrm{End}}W=(W\mathrm{ev},\gamma W).
\]

Its two selected entries are both `v_0 W[0,0]`. Hence
`L d_End=0` as a polynomial identity. This proves a chain map to the
common line bundle placed in degree `-2`: the only potentially nonzero
incoming compatibility is the one just checked, while the target
differential is zero. This is not a rule for discarding a lower component
of a total cocycle without checking it.

For a closed total lift `J` with component `J_2` in Čech degree 4 and
internal degree `-2`, the convention
`delta_Cech J_2=d_End J_3` gives

\[
\delta_{\mathrm{Cech}}L(J_2)=0.
\]

After taking the full-sign component and removing the common factor
`y_1y_2y_3y_4`, the original-frame conversion for internal degree `r` is
`tau^(r-2)`, where `tau` is the product of the inverted product-chart
coordinates. For `r=-2` this is `tau^-4`; the scalar target on
`Y=(P^1)^4` is therefore `F=O(-4,-4,-4,-4)`. The entries must be put in
this same original frame before applying `L`.

The 81 Laurent coordinates have exponents `e_i in {-3,-2,-1}`. With the
last coordinate varying fastest, their index is

\[
k=27(e_1+3)+9(e_2+3)+3(e_3+3)+(e_4+3).
\]

In the finite-model negative block they are `n[k]-n[5670+k]`.
For a dual monomial `x^m`, `m_i in {0,1,2}`, one has `e_i=-m_i-1` and
`k=sum_i (2-m_i)3^(4-i)`. In particular `m=(2,2,2,0)` has index 2.

## 2. Source hypotheses for the smaller scalar comparison

The following conditions concern the chosen geometric lift, not an
arbitrary polynomial or an arbitrary cycle of the finite model.

1. The original alternating residual is closed and is included into
   `End(K)` through compatible local contractions. A contraction has
   inclusion `I`, projection `P`, homotopy `H`, and `E=IP`, with
   `H^2=HI=PH=0` and `1-E=d_K H+H d_K`.
2. Original physical-frame transport gives the transition stated above.
   The nonlinear residual on a reordered tuple is obtained by alternating
   and transporting the same cochain, not by evaluating a new nonlinear
   formula on that tuple.
3. In the auxiliary-first order `(*,0,1,2,3,4)`, local lifting gives the
   prefix expression below. Degree `-3` has injective vertical
   differential, so no bottom vertical class remains in the comparison
   of two lifts of the same residual.
4. The completed scalar on its refined intersections has first-open
   denominator at most `v_0`, primary denominators at most `h_j^13`, and
   the legal-divisor bounds stated in the residue theorem. These bounds
   include original-frame transport. They need not bound individual
   arithmetic intermediates or a primitive relating two lifting orders.

These are the exact places where a geometric source certificate is needed.
`verify_scalar_maps.py` checks the displayed polynomial rows and all ten
matrix units in the bottom differential; it does not silently assert the
remaining source hypotheses.

## 3. Why changing the lifting order preserves the scalar class

Identify the two alternating Čech complexes before comparing their lifts.
For the two closed lifts write `z=J'-J`; its vertical-cohomology projection
in bidegree `(2,0)` is zero. Applying the old local contraction successively
removes bidegrees `(2,0)`, `(3,-1)`, `(4,-2)` by primitives of bidegrees
`(2,-1)`, `(3,-2)`, `(4,-3)`, with alternating totalization signs `+,-,+`.
The remaining `(5,-3)` component is vertically closed and is zero by
bottom injectivity. Thus `z=DW`, with `W` regular on the original refined
intersections. Applying `L` gives

\[
L(J'_2)-L(J_2)=\delta_{\mathrm{Cech}}L(W_{3,-2}).
\]

This establishes equality of classes. It asserts neither equality of
cochains nor small pole bounds for `W`. In particular the smaller weights
below are applied to the completed new scalar, never to an uncertified
order-change primitive.

## 4. Prefix sign and the carrier merger

For a surviving five-tuple with first three carriers `A<B<C`, let `M`
be its unsigned normalized two-by-two row residual on the last three
vertices. Put

\[
Z=I_B(P_BI_C)M^t(P_CH_{1,B}).
\]

Here `H_0:K^1->K^0`, `H_1:K^2->K^1`, and
`eta:K^3->K^2` are the corresponding homotopy blocks. The End contraction
`h(F)=HF+(-1)^r EFH` gives

\[
J'_2=-h_Ah_Bj_C(M),\quad
(J'_2)_{02}=-H_{0,A}Z,\quad
(J'_2)_{13}=E_A Z\eta_A.
\]

Consequently
`L(J'_2)=-(H_{0,A}Z)[0,0]-(E_AZ eta_A)[10,0]`.
If a stored residual moment already includes the leading minus, the block
signs reverse; the minus must occur exactly once.

The exact rows at both first carriers are

\[
I_0[10,:]=I_*[10,:]=0,\qquad
H_{0,0}[0,:]=H_{0,*}[0,:]=e_{10}^t/v_0.
\]

Therefore their scalar formula is the same, independent of their line mask:

\[
c_{(a,b,c,d,e)}=-Z[10,0]/v_0.
\]

A tuple containing both `*` and `0` is zero because its relevant second
anchor has `I_0[10,:]=0`. Repeated anchors vanish by `h^2=0`, and an anchor
coinciding with the included-tail carrier vanishes by `hj=0`.
Thus the scalar descends to a first open `D(v_0)` without a line refinement.
This extends the scalar only, not the local vector-bundle frame or the
full contraction.

For completeness, take `h_0=v_0^5-v_0v_1v_2v_3v_4` and the auxiliary open
`D(v_0v_1v_3v_4)`. Their union is `D(v_0)`: if `v_0` is nonzero and
`h_0=0`, then `v_1v_2v_3v_4=v_0^4` is nonzero. The remaining coarse opens
are `D(h_j)`, `h_j=v_j^5-v_0v_1v_2v_3v_4`, for `j=1,...,4`.
They cover together with `D(v_0)`, since on `v_0=0` a nonzero projective
coefficient `v_j` gives `h_j=v_j^5 != 0`.

Closedness of the extended scalar follows as a rational identity once its
coefficients are regular in these localizations. The pole hypotheses give
a regular scalar comparison. They do not license deleting tied residual
carriers from an earlier tensor formula; the separate chain projection in
[the residue theorem](residue-theorem.md) is what removes those terms in
its new coarse representative.
