# Independent audit of the canonical nilpotent lift and scalar obstruction

## Verdict and scope

The candidate is correct under the pinned PR716/717/718/721 hypotheses and their fixed B1 convention. It strengthens the earlier fixed-trace alternative to the universal scalar identity M=(u/30)Id. This review independently derives the two necessary polynomial identities and checks the covariance step. It uses only bounded universal formal-jet identities, with no chosen form coefficients, source instance, point, derivative value, or evaluated matrix rank.

## 1. Normalization

Use tau2(p,r)=p_XX r_YY-2p_XY r_XY+p_YY r_XX, and H(p)=p_XX p_YY-p_XY². Thus tau2(p,p)=2H(p). The candidate entries must be read as

x=u tau2(f,g)/112, y=-u H(f)/20, z=u H(g)/144.

Equivalently y=-u tau2(f,f)/40 and z=u tau2(g,g)/288. Interpreting Hess as the full self-transvectant would be incorrect.

Set t=Y/X and use F,G for the formal dehomogenizations. Write F1,F2,G1,G2 for formal derivatives, not evaluated data. The homogeneous chain rule gives

tau2(p_d,r_e)=d(d-1)P R2-2(d-1)(e-1)P1 R1+e(e-1)P2 R

in this chart. Consequently

x/u=(6 F G2-16 F1 G1+20 F2 G)/112,
y/u=-(6 F F2-4 F1²)/20,
z/u=(20 G G2-16 G1²)/144.

These are homogeneous polynomial entries of degrees 4,2,6 before dehomogenization, so the proposed T is a regular polynomial weight-four matrix.

## 2. Nilpotence and the obstruction

Starting independently from PR718 formulas, put

c/u²=tau2(fg,fg)/1470-tau2(f²,g²)/1350,
b_L/u=tau2(fg,Lf)/462-tau2(f²,Lg)/550.

Expanding the product derivatives in the chain-rule identity yields the polynomial identity

2FG(x/u)+G²(y/u)-F²(z/u)+c/u²=0.

It therefore proves the required first-normal nilpotence exactly, not just modulo an ideal. A second expansion yields

L(Fx+Gy)/u+b_L/u
 =F { L(F G2/40-F2 G/12)+L1(-F G1/5+F1 G/3) }.

Here L is an unspecified linear polynomial and L2=0. Thus division by f produces precisely the proposed representative of O. The independent verification script verify.py implements these two identities as polynomial identities in eight indeterminates and obtains zero residuals. Its input contains no coefficient expansion of a particular homogeneous pair.

For L=1, rehomogenization is especially important: the divided representative has degree five, whereas f g_YY and g f_YY have degree six. The correct exact degree-six identity is

X (Psi(XA0)/f)=u(f g_YY/40-g f_YY/12).

It follows immediately that X O(X)=0 in A6. There is no cancellation of X in the quotient algebra; none is needed or justified.

## 3. Covariance rigorously supplies every direction

All constructions used here commute with SL2(k) coordinate changes: tau2 is the unnormalized second transvectant, the Hessian determinant is half its diagonal value, B1 consists of transvectants with scalar degree-dependent factors, and ordinary multiplication and the ideal (f,g) commute with coordinate changes. The scalar u is retained unchanged. Matrix entries have different degrees but transform individually by their ordinary binary-form representations; this does not obstruct equivariance.

For any nonzero ell in S1, choose m in S1 with det(ell,m)=1. In the coordinates X'=ell,Y'=m, repeat the already established universal identity. The transformed f,g are again a regular pair of degrees 3,5; the canonical T transforms to the same canonical formula. Therefore

ell O(ell)=0 in A6.

The zero direction is automatic. Equivalently one may use the exact covariant identity with the constant-coefficient directional operator D_ell=a partial_Y-b partial_X for ell=aX+bY:

ell (Psi(ell A0)/f)=u(f D_ell² g/40-g D_ell² f/12).

It is the SL2 transform of the displayed X identity. Its right side lies in (f,g). This statement concerns the canonical representative; lift independence from PR717 then gives the same conclusion for every allowed nilpotent T.

## 4. Scalar conclusion and regularity

Regularity is essential to identify the reduced target with A5, to obtain the perfect multiplication pairing S1 times A5 to A6, and to use the nonzero socle generator [J]. None of these steps requires square-freeness, reducedness, or splitting of the forms.

Use the earlier identification i characterized by m i(v)=omega(v,m)[J], with omega(X,Y)=1, and M=i inverse O. The identity ell O(ell)=0 is exactly omega(Mell,ell)=0 for every ell. Polarizing implies that the bilinear pairing omega(Mv,w) is alternating. In two dimensions every alternating form is a scalar multiple of omega, so nondegeneracy gives M=lambda Id. This conclusion is structural, not a matrix-rank computation.

The independently established PR721 alternating identity gives tr M=u/15, hence lambda=u/30. Since the field has characteristic zero and u is nonzero, O=(u/30)i is an isomorphism. The rank-one alternative in the prior structure note is therefore formally exhaustive but never realized under these stronger derived identities.

## 5. Consequence and limits

If r0 is the local base class in Q8 and j:A5 to Q8 is multiplication by f, local affine cancellation is possible exactly when pi(r0)=0. In that event write j(rbar)=r0 and b=i inverse(rbar). The unique local cancelling direction is ell=-30 b/(a u). This does not compute pi(r0), prove it vanishes for the actual distinguished source, or make local directions globally realizable. Those limitations remain unchanged.

## Frozen verification scope

PROOF.md SHA256: a2c7eeb50b1e5cfafe98943c2809fa4096ba4371a89eab53063dd8489178c0ac.
verify.py SHA256: dee028c5c7260d1a313e9ca01731efe5972974d2de9d36d748c3c3519d191d65.

This is independent deductive review plus bounded symbolic verification, not proof-assistant certification. The checker verifies the two polynomial expansions; covariance, duality, the geometric inputs and cancellation implications are deductive arguments, not checker-certified statements.
