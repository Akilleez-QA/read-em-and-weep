# The declared expression, its sign, and the first-carrier merger

## 1. Exact data and chart

Let `Y=(P1)^4` with homogeneous coordinates `(X_i:Y_i)`. Define

\[
\prod_{i=1}^4(Y_i+X_i z)=\sum_{j=0}^4v_jz^j,
\qquad h_j=v_j^5-v_0v_1v_2v_3v_4.
\]

On `Y_i=1`, put `x_i=X_i/Y_i`. This gives `v0=1` and
`v_j=e_j(x1,x2,x3,x4)` exactly. The chart checker verifies all five coefficients
and all 16 product-chart transformations. These `v_j` are not independent
affine coordinate variables after pullback; the homogeneous primitive audit
first checks rational identities in independent `v0,...,v4`, then pulls them
back by this map.

The model supplies `gamma`, `delta`, `ev`, and six local contractions of the
four-term complex of ranks `(5,15,10,2)`. The public source bridge proves exact
rational equality of the original and reduced primitive models. Consequently
their derivatives are also equal. The audit here applies directly to the
reduced model and includes its hidden `v0` denominators. No pole certificate
for a different, unreduced denominator presentation is silently substituted.

The unsigned normalized two-by-two residual `M` is exactly the `C` emitted by
the pinned bridge generator on carriers `(2,3,4)`. Its normalized inclusion is
`j_C(M)=I_C M^t P_C`. The bundled source excerpts contain its mixed residual,
first corrections, and normalization formulas. The source-alignment checker
compares the two residual functions literally. It accounts for every difference
between their surrounding source construction and the pole evaluator:

- primary choices are joined for an upper bound;
- exact primitive and line seeds are replaced by certified bounds;
- Boolean mask bits are represented as bits rather than formal coefficients;
- the trace of a matrix product is expanded rather than computed sparsely;
- additional returned fields only supply the sparse prefix calculation.

These are bounds on the same operations, not values obtained from sample
points. Primitive seeding and the line replacement are justified separately
in [frames and poles](frames-and-poles.md).

## 2. Why the minus occurs geometrically

Use the total differential `D=delta_Cech+(-1)^q d_End`, where `q` is Čech
degree. Starting from `J0=j(M)` in bidegree `(2,0)`, the contraction recurrence
is `J1=h delta_Cech J0`, `J2=-h delta_Cech J1`, `J3=h delta_Cech J2`.
Indeed the vertical signs in Čech degrees 3 and 4 are respectively minus and
plus. Thus the second correction has one minus before any scalar constructor
is evaluated.

For the End contraction

\[
h(F)=HF+(-1)^r EFH,\qquad E=IP,
\]

the checked identities `H^2=HI=PH=0` give `h^2=hj=0`. In the auxiliary-first
ordering `(*,0,1,2,3,4)`, all non-first faces vanish after the next leading
homotopy. A surviving five-tuple with first three carriers `A<B<C` therefore
has

\[
J_2=-h_Ah_Bj_C(M),\qquad Z=E_B(I_CM^tP_C)H_{1,B},
\]

\[
(J_2)_{02}=-H_{0,A}Z,\qquad (J_2)_{13}=E_AZ\eta_A.
\]

This prefix identity is algebraic even before closedness is used. Repeated
prefix carriers vanish, including different line masks for the same carrier,
because their common-frame homotopies coincide. The residual is always the
same alternating cochain transported to the common frame. Re-evaluating a
nonlinear residual on a reordered tuple would be a different prescription.

## 3. Verified merger and prefactors

For both first carriers `0` and `*`, exact homogeneous computation gives

\[
I_A[10,:]=E_A[10,:]=0,
\qquad H_{0,A}[0,:]=e_{10}^t/v_0.
\]

Consequently

\[
L(J_2)=-Z[10,0]/v_0.
\]

A tuple containing both first carriers has zero scalar: its second distinct
anchor is carrier 0 and `E_0[10,:]=0`. Their scalar expressions agree and merge
to the first open `D(v0)`, without a line refinement. To check the covering
statement, if `v0!=0` and `h0=0`, then all `v1,...,v4` are nonzero, so the
auxiliary generator `v0 v1 v3 v4` is nonzero. If `v0=0`, at least one `v_j`
is nonzero and `h_j=v_j^5!=0`. The projective coefficient vector has no common
zero because a product of four nonzero linear polynomials is nonzero.

On the finite chart and the tuple `(0,1,2m2,3m3,4m4)`, define

\[
a=\operatorname{row}_{10}(I_1P_1I_2),\qquad
b=\operatorname{column}_0(P_2H_{1,1}).
\]

Then `c=-a M^t b`. The first primary anchor is independent of its line mask,
so its line-partition sum is one. The numerator package independently verifies
these exact prefactors, all feature moments and their full 4,096-mask coverage.
Writing `Mbar` for that complete moment contraction gives

\[
f=-a\overline M^t b,\qquad
A=f h_1^{13}h_2^{14}h_3^{14}h_4^{14}.
\]

The source residual is unsigned; this is the unique `J2` minus. The source
package's constructor test checks that the implemented transpose and sign
agree with this formula. Byte identity alone would not derive the sign.

## 4. What remains outside this package

The exact homogeneous rows also give `L d_End=0` on all ten matrix units of
the bottom differential. If the original normalized residual is a closed
geometric residual, the existing total-lift and order-change argument then
identifies the merged scalar with its scalar cohomology image.

The remaining ambient-source obligations are to specify and verify the
intended second-order algebraic algebroid, its determinant-one classical
module frames, the explicit first-order lift, and the equality of its full-sign
second-order defect with the declared unsigned residual. Those are geometric
attribution assertions. Neither the carrier merger, the pole graph, nor a
zero numerical scalar proves them.

In particular, this package proves the stated identities and regularity
properties of the declared rational expression using the pinned algebraic
source. It does not by itself assert equivalence with another central/gerbe
presentation, repair a global deformation theorem, or decide the full Ext
obstruction. The distinction does not prevent the regular-section argument
from proving degree-273 cancellation for this exact expression.
