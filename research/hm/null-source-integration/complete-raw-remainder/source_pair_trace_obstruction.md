# A source-bound symbolic obstruction to the closed-K shortcut

Independent review of the source-frame linkage is requested and pending.

## Result and limits

On the original all-finite common legal open, the necessary identity A_j=19u_ij from the affine-mask reduction fails for the actual carrier pair (0,1). Consequently at least one repeated-last-carrier triple (0,1,1), with suitable legal masks, has a nonzero target-pair contraction of Lambda=delta K. Thus K is not closed on the full source cover, and the proposed H1 shortcut that removes K/4 on that basis is unavailable.

This is a rational-function argument from the pinned I/P entries and their degrees. No actual source point, polynomial specialization, numerical jet, Omega, detector, or global obstruction was evaluated. It does NOT prove that the complete E(K) term cannot cancel or be a boundary by another identity. It does not determine Rsharp. It is conditional on the already stated identification of the source Lambda diagnostic with its finite common-frame realization, which is the explicit review dependency.

## 1. Exact source rows determine the two reference connections

Use the canonical model SHA-256 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926, copied at PR90 779c1f7604db6fd48ce6e389b30a96f7aebef9f7. Coordinates are v0=1 and (v1,v2,v3,v4). Put t=v1 and work over F=Q(v2,v3,v4).

The source denominators are

    d0=t*v2*v3*v4-1,
    d1=-t^5+t*v2*v3*v4.

For Gamma_c^0=P_c^0 dI_c^0, the supports of the P row and I column intersect as follows (matrix indices zero-based):

- Carrier 0: diagonal entries intersect only at ambient rows 0 and 5, respectively; both corresponding I entries equal 1. Off-diagonal intersections are empty.
- Carrier 1: diagonal entries intersect only at rows 1 and 6; corresponding I entries equal 1 and t. At row 6 the matching P entry equals 1/t. Off-diagonal intersections are empty.

These equalities are exact sparse term identities: the numerator of I_1[6,1] is t*d1, and that of P_1[1,6] is d1/t. Therefore

    Gamma_0^0=0,
    Gamma_1^0=diag(0,dt/t).                              (1)

There is no ignored derivative of a nonconstant I entry supported by P: the listed intersections exhaust the relevant supports.

## 2. The weighted trace identity has an incompatible leading term

Let K=P_0^0 I_1^0 be the column transition. For this pair,

    Q^0=K Gamma_1^0 K^-1-dK K^-1,
    A_1=tr(tf(Q^0) K h K^-1), h=diag(1,-1).

Since tr(h)=0, tracefree projection does not alter this pairing. Cyclicity gives

    A_1=-dt/t-tr(K^-1 dK h).                             (2)

The putative closed-K identity requires A_1=19 dt/t. We show instead that, in the t direction,

    A_1(partial_t)=-1/t+O(t^-2),
    (A_1-19dt/t)(partial_t)=-20/t+O(t^-2) != 0.           (3)

All orders below are formal at t=infinity over F. They are not a numerical limit or an assertion about regularity on the physical infinity chart.

The sparse supports and numerator degrees give

    K00=O(t), K01=O(1), K10=O(1), K11=O(t^-2).            (4)

The contributing ambient row indices and degree bounds are:

    K00: row1 -> 1, row4 -> -2, row7 -> -1;
    K01: row4 -> 0, row7 -> -1;
    K10: row1 -> 0, row4 -> -4, row5 -> -2, row7 -> -2;
    K11: row4 -> -2, row5 -> -2, row7 -> -2.

The unique leading terms in the bounded off-diagonal entries give

    K01=v2*v4/v3+O(t^-1),
    K10=-v3/(v2*v4)+O(t^-1).

Hence det(K)=1+O(t^-1), independently of using the already accepted unit-determinant identity. In particular K is invertible over F(t), its inverse entries have the orders obtained from its adjugate, and

    (K^-1 partial_t K)00
       =(K11 partial_t K00-K01 partial_t K10)/det(K)
       =O(t^-2).

A bounded rational function has derivative O(t^-2), which is used for K10. Also tr(K^-1 partial_t K)=partial_t log(det K)=O(t^-2). Therefore tr(K^-1 partial_t K h)=O(t^-2), proving (3). No possible cancellation among lower-order source terms can remove the coefficient -20 of t^-1 in (3).

## 3. Pullback to the actual product and choice of a legal mask

The elementary-symmetric map (x0,x1,x2,x3) -> (v1,v2,v3,v4) is dominant and generically etale in characteristic zero: its Jacobian is, up to sign, the Vandermonde product of coordinate differences. Consequently the nonzero rational one-form F=A_1-19dlog(v1) remains nonzero after pullback to Q(x0,x1,x2,x3), and after the elliptic algebraic extension. The common legal finite open is dense, so F has some nonzero dx_b component there.

For the target pair containing b, choose its other coordinate a. The nonzero rational frame factor r_a=(x_a^2+1)/(2x_a(x_a^2-1)) gives a nonzero contraction of F wedge r_a dx_a in that pair. Choose the first vertex on carrier0, the second on carrier1 with mask0, and the third on carrier1 with mask2^a. The two carrier1 vertices are distinct, both are legal on the common open, and the repeated-last-carrier formula gives

    Lambda=F wedge(ell_j-ell_k)=-F wedge r_a dx_a.

Its relevant physical pair contraction has the additional nonzero factor y_c*y_d. Thus at least one such actual source triple has Lambda_p or Lambda_q nonzero as a rational function. This existence argument chooses no numerical point and makes no source-value claim at the fixed Omega point.

## 4. Reproducible structural check and remaining review

The companion checker authenticates the model bytes, compares exact sparse metadata for the unit/t/inverse-t entries, verifies all support intersections, the displayed degree bounds and unique leading numerator terms. It never calls a polynomial evaluator or substitutes a source point. The mathematical deductions from those checks are (1)-(3) and the dense-open pullback argument above.

Independent review should particularly check the link from the finite common ambient I/P realization to the original Lambda formula and the coefficient 19 from the prior weighted trace reduction. The structural source-row and degree argument itself does not need the proposed physical launcher or any extension of its execution contract. Failure of this one shortcut leaves the complete obstruction problem open.

## 5. The same family has Omega identically zero

For the repeated carrier1 edge with masks 0 and 2^a, its rational carrier core is P_1^0 I_1^0=I. Hence B=g_jk=D_k D_j^-1 is diagonal and depends on only coordinate x_a (and its curve coordinate y_a). Every cross slot used in Omega differentiates two distinct coordinates, so V_c V_d B=0 for those slots. Thus every transported J_cd=0, and Omega=0 identically on this family.

This sharpens the scope: the failure of the closed-K criterion occurs on an actual-source family where the second-jet Omega shortcut itself holds. It demonstrates that proving Omega=0 would still not justify deleting K by the proposed closed-scalar/H1 argument. It does not demonstrate a nonzero complete remainder or failure of a different boundary cancellation.
