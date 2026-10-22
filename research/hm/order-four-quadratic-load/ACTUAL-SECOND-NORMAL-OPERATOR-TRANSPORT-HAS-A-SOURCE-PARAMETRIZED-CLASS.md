# The next operator transport has a source-parametrized cohomology class

## Result and boundary

Fix the ACTUAL first-normal operator and bundle data, including their source, determinant, and full first-normal connection markings, and fix the prescribed harmonic symbol/scalar completion through q². On the two vertex charts the weight-zero coefficient of its second-normal adjoint transport defect is a genuine cocycle in

    J_eta(4) = P4 O_L(-4),
    H1(J_eta(4)) = P4 tensor A = V+P4+D5.                 (1)

It is independent of arbitrary second-normal lifts of the bundle transitions. Its value remains to be calculated from the fixed first-normal data. Scalar square constraints do not detect it. A source-parametrized equivariant family in this twelve-dimensional target need not vanish, even though the target has no invariant vector.

This is an associated-coefficient obstruction on the vertex cover. It does not construct a global third-neighborhood midpoint bundle, identify the fixed source with an arbitrary homogeneous lift, or evaluate the fourth Bockstein. Its comparison to that last quotient still requires the actual chain normalization.

Sources: ACTUAL-NEXT-WEIGHT-SEPARATES-MIDPOINT-NORMALIZATION-FROM-ENDPOINT-TRANSPORT.md, ACTUAL-LEADING-NEXT-ERROR-HAS-A-CANONICAL-AFFINE-TRANSPORT.md, and ACTUAL-LOWEST-NORMAL-CONNECTION-HAS-AN-EXPLICIT-NEXT-ERROR-TERM.md. The harmonic product convention is that of UNIVERSAL-SECOND-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-DEFECT.md.

## 1. Exact coefficient bundle and scalar separation

The cone connection has physical twist six. Consequently its q² coefficient has twist two. A weight-zero trace-free coefficient has cover degrees (0,-2;2,0); the upper entry vanishes. Its marked coefficient sequence is

    0 -> V O_L(-6) -> J_eta(4) -> O_L(2) -> 0,           (2)

obtained by twisting the already identified nonsplit J_eta sequence by four. Thus J_eta(4)=P4 O_L(-4), not a split diagonal-plus-lower bundle. Its H0 is zero and its H1 is P4 tensor Sym²W, of dimension twelve. No actual-instance rank is involved.

Weight-zero scalar q² symbol or scalar-eigenvalue defects have coefficient O_L(2), whose H1 is zero. Therefore these scalar *classes* can be removed before forming the adjoint class. This does not set their local coefficients to zero: H0(O_L(2)) has dimension three, and their actual values must be fixed by the prescribed symbol/scalar marking. The determinant marking removes the trace of the connection; it does not remove a trace-free element of (1).

## 2. Why the adjoint coefficient is an actual cocycle

Work first in a common physical-q frame, with Dq=rho q. After fixing the scalar symbol transport, write

    T_P(A)=P A P^-1-H(DP)P^-1,
    A_j=T_Pij(A_i)+q² a_ij mod q³.                     (3)

Here products are actual products of local third-neighborhood lifts, not uncorrected products of cone restrictions. First-normal compatibility is part of the fixed input. The a_ij in (3) is a genuine coefficient of that defect.

Around a cycle i->j->k->i, let P_ki P_jk P_ij=I+q² C mod q³. Composing (3) gives exactly

    sum_cycle transported a = H0(D+2rho)C+[A0,C].       (4)

The regular adjoint C has minimum chain weight minus two; its scalar part has minimum zero. The fixed cone operator H0,A0 starts at weight four. Thus (4) starts at weight two, and its weight-zero coefficient vanishes. This proves that a_ij,0 is a cocycle without assuming a globally glued third-neighborhood bundle. Full ordinary stabilizers start at eight, so they cannot mix a lower regular a coefficient into weight zero.

Changing a lifted transition to (I+q² C_ij)P_ij changes a_ij by the right side of (4), hence does not change a_ij,0 at all. Changing local operator lifts by q² b_i changes a_ij,0 by delta b_0. This proves that (1) is a well-defined class of the fixed first-normal data relative to the prescribed symbol/scalar completion. It does not assert independence from an arbitrary change of that completion. No claim of vanishing follows from this construction.

On q_j=u_ij q_i, second-normal coefficients carry u_ij^-2 and rho_j=rho_i+Dlog u_ij. This is why 2rho occurs in (4). All physical coefficient-line connections remain in D.

## 3. The trace-blind term and the remaining actual calculation

This defect contributes to the next error by

    h2 Dn+[a2,n]-lambda2 n.                             (5)

For n=σ σ^t J, n²=0, differentiation and cyclic trace give

    tr(n Dn)=0,  tr(n[a2,n])=0,  tr(n²)=0.              (6)

Thus every term in (5) is invisible to the scalar differentiated-square constraint. The known nonzero chi and its exact apolar normalization cannot determine (1).

For a source-parametrized family, absence of a trivial summand in P4 tensor A is irrelevant to automatic vanishing. Only a parameter-free invariant cocycle would vanish for that reason. One must retain the parameter representation in the invariant Hom space.

## 4. Explicit low transport and the cone centralizer warning

Let P0 be the marked homogeneous triangular/root transition, whose harmonic inverse is exact, and put Q0=P0^-1. Define

    F_P(K)=B1(P,K)Q0+B1(PK,Q0),
    G2_P(A)=B2(P,A)Q0+B1(B1(P,A),Q0)+B2(PA,Q0).        (7)

These are the first and second harmonic conjugation coefficients. Full ordinary high stabilizers do not affect the weight-zero coefficient considered here. Let the endpoint transition have first-normal factor I+q eta0, with eta0 the FULL marked normal cocycle. Use A4 and K0 already transported through P0, including their derivative and determinant terms. The additional endpoint second-normal connection transport at weight zero is

    E_eta=[eta0,K0]+B1(eta0,A4)-B1(A4,eta0)
          -H1(D+rho)eta0-B1(H0,(D+rho)eta0).           (8)

For the prescribed homogeneous symbol, H0 has weight four and H1 has weight zero. Quadratic eta0 terms first occur at weight four and are absent from (8). Explicitly the omitted conjugation/derivative contribution is `-eta0 A4 eta0+A4 eta0²+H0((D+rho)eta0)eta0`; its determinant scalar is also at weight four. The remaining expression (8) is trace-free, so determinant transport does not conceal another weight-zero adjoint term. If the chosen local connection has no q² coefficient, the defect convention (3) gives

    a_ij,0 = -tf( F_P0(K4)+G2_P0(A0,8)+E_eta )         (9)

for these retained terms. Extra source/scalar coefficients, if not already fixed, must be added rather than silently set to zero. The homogeneous midpoint A4,K0 alone give no weight-zero second-normal term. Formula (9) still requires the CONIC-SELECTED actual K4, not an arbitrary splitting of its affine vertex cocycle.

A0,8 cannot be omitted merely because a cone operator is unique modulo ell n. Although the explicit patched cone representative has only A4 followed by a weight-twelve correction, another allowed marked cone representative can contain ell n8. For a base scalar ell, adding ell Nhat to a midpoint first-normal operator changes A0,8 by ell n8 and K4 by ell T4. The frozen mismatch convention gives

    F_P(T4)+G2_P(n8)=-Z0,
    Delta a_0=ell Z0.                                 (10)

Thus this ambiguity is known apolar data after ell is fixed, not zero raw transport. In fact [Z0]=-(B lambda/4)[eta_ap], with the previously fixed equation-line normalization. The marked source must say which ell occurs.

Only if ell arises by multiplying a lower-operator centralizer, ell=a rho_source, is the familiar final-quotient dismissal licensed by the ambient chain: v_h changes by rho_source xi, w_h by rho_source zeta_a, and a w_h changes by beta2_a(rho_source). This removes that restricted change in the FINAL second-symbol quotient, not in the raw class (1). An arbitrary ell in H0(O_Q(4)) need not be divisible by a and is not covered by that argument.

## 5. Representation interface, not actual coefficient values

For the multiplied cubic source family, the parameter representation is Sym³A tensor D5. Exact characters give

    Sym³A tensor D5 = 3A+3V+3P4+4D5.

The space of equivariant maps from this representation to (1) therefore has dimension ten. This counts universal channels, not ten freely selectable actual coefficients.

Contracting the final A factor of P4 tensor A with the direction a produces raw quartic P4 families. This map is onto: polarization, equivalently one fourth of the derivative of a quartic homogeneous family, is an equivariant right inverse by Euler's identity. There are five such raw channels. The single beta2-factor channel is the one already identified in FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md. Quotienting it leaves four channels and a six-dimensional kernel of this universal representation map. Identifying the actual transport class (1) with the actual next division under this map remains a separate chain comparison, not a consequence of the dimension count.

## Reproduction

Run python verify_second_normal_operator_transport_class.py. It checks generic matrix transport, the trace-blind identities, coefficient twists and the nonsplit-bundle cohomology arithmetic, exact character multiplicities, and the universal polarization identity, and the full eta-dependent second-normal ordered transport including its determinant weight. All source coefficients remain unassigned; no actual-instance matrices or rank evaluations are used. Earlier frozen files are unchanged.
