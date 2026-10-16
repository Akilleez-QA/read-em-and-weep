# Source-specific routes to killing the second-jet bracket

## Result and scope

There is an exact necessary-and-sufficient three-scalar identity for the vanishing of Omega. None of determinant one, commuting coordinate derivatives, low matrix rank, internal edgewise commutativity, elementary-symmetric pullback, or rank-one coordinate Hessians supplies those three identities universally. A shared one-dimensional Lie-algebra image, a suitable symmetry relating the two complete jet arrays, or a signed coordinate-rank cancellation would suffice. No such global identity for the actual pinned HM source is certified by the inputs reviewed here. This is an absence of a certificate, not a proof that the source fails those relations.

Nine reproducible abstract tests pass with `python test_source_second_jet_degeneracy.py`. They import no HM source modules or data and do not evaluate any physical polynomial. The pinned model was read and its bytes hashed, not evaluated or expanded. Its hash is 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926, matching the physical-current binder.

## 1. Minimal exact relations

Let the ordered cross-coordinate slots be a=(13,14,23,24), and set

    S = [[0,0,0,1],[0,0,-1,0],[0,-1,0,0],[1,0,0,0]].

Only traceless parts enter a commutator. Write the four J and H traceless jets in the basis (h,e,f), where [h,e]=2e, [h,f]=-2f, [e,f]=h. Regard J and H as 4 by 3 scalar matrices, and put C=J^t S H. Then

    8 Omega = (C_ef-C_fe) h
              +2(C_he-C_eh) e
              +2(C_fh-C_hf) f.

Thus Omega=0 if and only if C is symmetric. These three scalar equations are the exact minimal coordinate conditions: the bracket induces an isomorphism wedge^2(sl2) -> sl2 in characteristic zero. They are conditions on a cross-contraction, not a requirement that every individual bracket vanish. Omitting any component is insufficient for matrix vanishing. Scalar trace parts of H and J are irrelevant to this particular symbol, although they are relevant to the rest of M0.

The test checks this identity on all 144 pairs of single-slot sl2 basis inputs. Since both sides are bilinear, this is an exhaustive abstract bilinear verification.

## 2. Which stronger hypotheses suffice, and which fail

### Cross-edge commutativity

The four conditions [J13,H24]=[J14,H23]=[J23,H14]=[J24,H13]=0 suffice but are stronger than necessary. A single shared one-dimensional traceless subspace containing every J and H jet also suffices. For a nonzero sl2 element over the characteristic-zero function field, its sl2 centralizer is its own line. Consequently, if all cross-edge brackets [J_a,H_b] vanish and both jet families are nonzero, both families lie in a common line. If one family is zero the condition holds without restricting the other family.

Merely saying each edge's jets commute internally is insufficient. Take J13=e and H24=f, all other relevant jets zero. Both families are individually commuting, but Omega=h/8. Having rank-two transition matrices says nothing about a one-dimensional traceless jet image. Simultaneous triangularity is likewise insufficient: J13=h, H24=e gives Omega=e/4.

### Array symmetry and cancellation

J=lambda H implies Omega=0 for any scalar lambda; H may have noncommuting entries. More generally J=T H is universally sufficient when T^t S is symmetric. It is also necessary for that ansatz to give zero for every unrestricted H: the antisymmetric part of T^t S is detected by two independently assigned sl2 components. These are pointwise algebraic statements; no derivatives of lambda or T are taken inside Omega.

In particular J=H with H13=e,H24=f gives nonzero individual brackets h and -h that cancel. This disproves necessity of pairwise bracket vanishing. The antisymmetry Omega(J,H)=-Omega(H,J) does not by itself produce source cancellation. The actual two edges have different owners and source expressions; exchanging independent arrays is not an authorized relabeling of a cover sum. To use it in a detector sum requires a full sign-preserving involution on owner labels, weights, frames, selectors and coefficient demands.

### Coordinate-rank cancellation

For separable cross-coordinate arrays

    J_ij=u_i v_j X, H_ij=s_i t_j Y,
    i in {1,2}, j in {3,4},

one has

    8 Omega=(u1 s2-u2 s1)(v3 t4-v4 t3)[X,Y].

Thus a shared left coordinate factor, a shared right coordinate factor, or [X,Y]=0 suffices. Rank one of each coordinate array separately does not: independent factors can make both determinants nonzero. Rank one in the matrix-component direction for each family separately also does not, as the e/f witness already shows. Any use of a rank claim must specify which flattening, whether the factor is shared, and whether its owner/frame matches.

The source map v_k=e_k(x1,x2,x3,x4) does not force a differential rank deficit: its Jacobian is a nonzero Vandermonde up to sign on the distinct-coordinate locus. There is no generic rank-one conclusion merely from the elementary-symmetric substitution. The Hessian chain rule also has second derivatives of the substitution, so dropping these would not test the physical source.

## 3. What the pinned source binding actually supplies

The existing physical binder gives K_ab=(P_a I_b)^t and

    T_ab,i = partial_i K_ab + Q_b,i K_ab - K_ab Q_a,i,
    g_ab = D_b K_ab D_a^-1.

The exact second-jet extension needed for this question is obtained without polynomial arithmetic. Define the edge covariant derivative

    nabla_ab,j Z = partial_j Z + Q_b,j Z - Z Q_a,j,
    V_ab,ij = nabla_ab,j T_ab,i.

Then the correctly normalized second jets are

    Hbar_ij = K_ab^-1 V_ab,ij,
    Jbar_ij = K_ab^-1 K_bc^-1 V_bc,ij K_ab,
    Hphysical_ij = D_a Hbar_ij D_a^-1,
    Jphysical_ij = D_a Jbar_ij D_a^-1.

This follows by twice differentiating D_b K_ab D_a^-1. An independent abstract two-coordinate test now compares H and transported J against direct physical differentiation for (x,x), (x,y), (y,x), and (y,y), checks mixed-derivative commutation, and includes an omitted-endpoint-Q negative control. The artificial matrices and frames do not import or instantiate HM source data. In particular partial_j differentiates Q_b,i and Q_a,i as well as K and T. The actual Q are diagonal and have commuting flat coordinate derivatives, so V_ij=V_ji. That within-edge symmetry is already built into the abstract witnesses and does not imply symmetry of J^t S H. Common conjugation by D_a preserves Omega=0. The current binder is first-order; a hash-bound second-order AST extension plus a physical differentiation audit is the next small source-binding artifact, not a physical evaluation.

Under determinant-one hypotheses the exact trace identities tr(H_ij)=tr(L_i L_j), tr(J_ij)=tr(U_i U_j) are certified by the survivor audit. They do not constrain the three antisymmetric entries of the cross-Gram matrix. Maurer-Cartan relations constrain first-current derivatives and are compatible with arbitrary traceless symmetric Hessians at a zero-first-jet point. The formal determinant-one shear examples demonstrate this compatibility.

Certified same-carrier special case: the exact P_c I_c=I identity is authenticated for this same source, so a triple whose three carrier cores coincide has K_ab=K_bc=I. Its physical transitions are diagonal frame ratios; all normalized second jets are diagonal, and Omega=0. Distinct masks do not make these transitions equal or constant, but diagonality is sufficient here. This special case says nothing about distinct-carrier triples. The homogeneous-identity receipt records canonical compact-JSON SHA256 b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2; the binder records raw-file SHA256 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926. These authenticate the same model, as independently established in selected-full-owner-kernel-lowering-independent-audit.md and its 15-test audit. Both hashes were independently recomputed here by serialization/hashing only. There is no unresolved provenance mismatch. The matching external exact contraction certificate, inspected by the existing audit, authenticates PI=I and the other contraction identities without rerunning its physical checker.

Status summary:

- Certified algebraically: three-equation criterion; covariance; trace reduction under determinant one; second-derivative formula above; all abstract sufficient conditions and counterexamples.
- Impossible as universal deductions: determinant one -> Omega=0; internal edgewise commutativity -> Omega=0; separate rank one -> Omega=0; derivative-index symmetry -> Omega=0; arbitrary transition-local two-jet boundary removal.
- Unknown for the full pinned source: shared sl2 line, cross-Gram symmetry, proportional arrays, shared coordinate factors, all distinct-carrier Omega values, and actual detector annihilation. These are not ruled out by a formal nonzero example.

## 4. Detector projection is a separate and weaker target

For an ordinary trace-pairing kernel W,

    tr(W Omega)=1/8 sum epsilon tr([W,J_ij] H_kl).

This gives an exact adjoint test. For completely independent formal J/H slots, a fixed W annihilates every Omega if and only if W is scalar. Indeed one may isolate any one paired bracket, and [sl2,sl2]=sl2. For a constrained source image, weaker kernel annihilation is possible. A single matrix entry is never an injective test of a general sl2-valued Omega: lower-left entry misses the h/8 witness, while a diagonal request misses e/4. Even two entries can miss the third independent component.

The authenticated refined detector is not a pointwise entry map. It is the full linear composition

    Phi=j* [L0 + delta* H0* L1 - delta* H0* delta* Hminus1* L2],

including first-owner kernels, exact restrictions, outer partition weights, staircase signs and terminal coefficient demands. Its three terminal tensor slots comprise nine entry rows and 78 seeds; these are not automatically a basis of the local sl2 dual. Testing a chosen entry or an unweighted local jet does not establish Phi(Omega)=0 or nonzero. The complete weighted coefficient expression, or a sound symbolic annihilator certificate on its source image, is required.

The generic frame cancellation audit already allows normalized current contractions for its 78 surviving paths. Applying the same common-conjugation identity to the bound H/J commutators is legitimate once the second-order formula is verified. It does not license omitting Q or differentiating only K. Existing selector pruning is not source-specific Omega annihilation.

## 5. Next certificate and decisive failure conditions

The smallest matrix-vanishing certificate is an owner-complete, frame-correct proof of the three antisymmetric cross-Gram identities for the second-order AST above, modulo authenticated identities of the pinned source and the legal-overlap localization. It may use factored relations and need not expand a source polynomial. Include exact source hashes, complete owner labels, the rational denominator domain, and a proof that every relevant tuple is covered. If attempting only detector vanishing, replace these three equations by the complete authenticated Phi(Omega)=0 demand identity, preserving all weights and coefficient rules.

Decisive failure of a proposed source relation requires an authenticated admissible source specialization or symbolic nonzero remainder on the actual source ideal, with denominators valid. A free sl2 counterexample only defeats a claimed universal implication; it does not defeat a genuinely source-specific identity. A nonzero actual Omega would defeat its matrix-vanishing proposal, but still would not establish a nonzero detector value. A nonzero Phi(Omega) would defeat detector annihilation of this summand, but still would not establish a nonzero complete Rsharp obstruction.

Rsharp contains the rest of M0, the F K terms, and the scalar-solver-dependent E(TF) terms. Its quartic-current remainder is independent formal evidence only when H/J and E(TF) are kept opaque. Neither a killed Omega nor a surviving Omega decides cancellation across those terms. No universal-baseline no-go has been promoted here to an Rsharp no-go or to an arithmetic lower bound.
