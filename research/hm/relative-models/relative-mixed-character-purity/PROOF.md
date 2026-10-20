> Publication scope: Uniform family purity, not a new central parity ledger; conditional actual-source identities remain explicit. Source-stage audit/checker references describe historical evidence, not fresh execution or bundled executable artifacts. Named source identities are hypotheses unless separately proved below.

# Uniform full-sign purity of the actual coefficient-family mixed residual

## 1. Result, premises, and what is new

Let k have characteristic zero, C be the smooth projective curve y²=z³−z, X=C⁴, Y=(P¹)⁴, q:X→Y the fixed product double cover, and N=⊠O_C(O). Let G=(Z/2)⁴ act on X by the four deck involutions and trivially on every coefficient parameter. Write χ_d for the d-th sign character, χ_p=χ_0χ_1, χ_q=χ_2χ_3, and χ=χ_pχ_q.

Admit precisely the homogeneous-source, root/frame, determinant, and rational-denotation premises S in the [relative obstruction theorem](../relative-obstruction-locus/PROOF.md), as explained in [SOURCE-FAMILY §§1–4,8](dependencies/SOURCE-FAMILY.md) and the complete recipe in [FIRST-LIFT-STRUCTURAL §§4–7](dependencies/FIRST-LIFT-STRUCTURAL.md). No new production-source identification or execution certificate is asserted here.

On the entire generating locus in any normalized affine chart of P(H⁰(X,N²)⁵), the SAME actual disjoint mixed residual R is a regular End(𝓔)-valued Čech cocycle of pure character χ. This holds before shrinking to the relative theorem's neighborhood B, and survives arbitrary base change. Here 𝓔=N⊗F*H is the source family's bundle. The assertion concerns this normalized same-recipe family, with the fixed physical fields and old root connections; it does not assert invariance under an unspecified parameter gauge.

Consequently, on the neighborhood B and under the additional separated premises P and D of the relative theorem, its section rχ equals the entire relative mixed class [R]. Its closed scheme Zχ is therefore exactly the relative vanishing scheme of the total mixed class, not just of one projection. For affine base changes T→B, this also says the entire absolute class of the pulled-back source cocycle vanishes exactly when T→B factors through Zχ. For general nonaffine T retain the relative-section formulation and the existing Leray caveat.

The fixed-source parity theorem [FIXED-CHARACTER §§2–5](dependencies/FIXED-CHARACTER.md) already contains the complete residual character ledger at the pinned tuple. We claim no novelty for that ledger or for central-fiber purity. The new step is to justify its hypotheses uniformly for every coefficient tuple, including the actual cover labels, target-line changes, first lifts, and correction δW, and then discharge the explicit purity boundary in the relative obstruction theorem. The dimension-free extension in SOURCE-FAMILY §8 supplies the actual regular family and closure; it did not explicitly state this equivariant conclusion.

## 2. Why every coefficient is invariant, uniformly

Put M=O_Y(1,1,1,1), so N²=q*M with its fixed natural deck linearization. The product-root decomposition is

    q_*O_X = ⊕_A O_Y(-2A).

By projection formula, the A-character global sections of N² are H⁰(Y,M⊗O_Y(-2A)). If A is nonempty one factor has degree −1 and has no sections; hence this space is zero. The invariant summand is H⁰(Y,M), of dimension 16. Thus all global coefficient sections descend to Y, with no exception among the 79 projective parameter directions. Over the universal coefficient chart the tautological sections are linear combinations of these descended sections with parameter coefficients, so are invariant as sections on X×S. Pullback to arbitrary, including nonreduced, parameter schemes preserves that identity; no generic-point argument is required.

Fix the natural linearization of N=O_X(Σ pr_d*O) with invariant rational reference section e_ref=1. A legal root label i has mask m_i and frame

    e_i = ν_i e_ref,       ν_i=∏_d(y_d/z_d)^(m_i,d).

The [product-root proof §§2–6](dependencies/PRODUCT-ROOT.md) proves these are actual regular line frames on their legal opens, including infinity. For σ∈G set η_i(σ)=∏χ_d(σ)^(m_i,d). Then σe_i=η_i e_i, and η_i is a constant sign, independent of position and parameters. Every ambient exponent −1,1,3,5 is odd, so every corresponding frame e_i^k has the SAME sign η_i.

Use a square-line frame ell=e_i² or a nonvanishing coefficient section s_p. Both are invariant. With s_j=v_j ell and c_i=e_i²/ell, both v_j and c_i are invariant functions. This holds intrinsically even where ν_i is not a regular function in the rational reference frame.

Every legal root open is deck-stable: the omitted origins and branch points are invariant divisors. Every target pivot open s_p≠0 is deck-stable. Every source carrier is pulled back from the invariant coefficient map: its equations are v_j⁵−∏v_l and v_0v_1v_3v_4, with the specified carrier and pivot labels retained. Their intersections give a cover on which G fixes every label individually. No implicit permutation of root, carrier, or target-pivot labels is allowed or needed. A labelwise deck-stable affine refinement exists via the finite quotient q×Id:X×S→Y×S: each stable open is saturated, its complementary closed set has closed image, and it is the inverse image of the corresponding quotient open. Refine that quotient open by affine opens and pull back; finite preimages are affine. Finite intersections are affine because X×S is separated. This refinement fixes its labels rather than introducing a deck permutation of affine labels.

## 3. Source frames, chart compatibility, and scalar deck transitions

Use the exact weight-zero arrays of SOURCE-FAMILY §2:

    U_0=[c⁻¹γ | I_0 | c⁻¹I_1 | c H_1 W],
    Q_0=[c H_0 ; P_0 ; c P_1 ; c⁻¹Lδ],
    U_1=[W | cη],      Q_1=[L ; c⁻¹ev],

with identity extreme arrays. The symbol η in the last display is the source primitive, not an owner sign. All their entries are invariant: each primitive is a rational homogeneous expression in invariant v on its own carrier, and c is invariant. The source-family theorem supplies regularity and the literal source identification, rather than inferring them from parity.

For a change ell'=λell, one has v'=λ⁻¹v and c'=λ⁻¹c. A primitive of weight d gains λ⁻ᵈ. Each displayed product has total weight zero, so U and Q agree exactly for the fixed root/carrier vertex. This is the previously proved variable-line chart identity, not an assertion that λ is constant. Here the chosen frames are invariant, hence λ is invariant too. Physical and parameter derivatives of the equal arrays agree, retaining every derivative of λ. A different carrier remains a different vertex with its actual transition; no carrier equality is assumed.

The two quotient columns are invariant coefficient combinations in the e_i ambient frame and thus both transform by η_i. In the common rational reference they are precisely (ν_i I_0,ν_i⁻¹I_1); both factors have the same sign η_i. Therefore the actual row transitions and their inverses obey

    σ(g_ij)=η_jη_i g_ij,       σ(g_ij⁻¹)=η_jη_i g_ij⁻¹.

The admitted determinant normalization identifies the stored adjugate with this inverse. Constant scalar signs disappear from every End conjugation. Thus the action on the matrices of normalized End cochains in these fixed physical frames is simply coefficientwise deck pullback. This action is independent of the coefficient parameter. The Čech differential, including g_ij⁻¹ Z_jk g_ij, commutes with it, since the two transition signs cancel.

This proves intrinsic equivariance of the matrix statements below. It also prevents a misleading parity argument in an unrelated frame: scalar matrix parity is being identified with the actual End action by the two-column frame law.

## 4. Raw scalar and first-lift covariance

The fixed fields satisfy σV_dσ⁻¹=χ_d(σ)V_d on both finite and infinity charts. In particular V_d takes character α to αχ_d, including when that factor was already present. The quotient rule preserves this law on every relevant localization. The fields kill parameter functions.

The fixed old-connection coefficient is α_i=(1/2)dlog h_i with h_i=∏(1−z_d⁻²)^(m_i,d). It is an invariant one-form; at infinity its retained one-factor expression is −t dt/(1−t²). Its contraction α_i,d=α_i(V_d) has character χ_d. For every one of the four ambient blocks, the actual formula

    B_i,d^l=−(V_d U_i^l)Q_i^l−k_l α_i,d Id

therefore has character χ_d. This includes both identity extreme blocks. It retains all frame derivatives and all old-connection terms.

Also q_d,ij=(m_j,d−m_i,d)y_d/z_d has character χ_d. For r=(a,b), every summand in the literal raw scalar

    s_r,ij=(1/4)Σ_l ε_l {tr(B_i,a^l B_j,b^l−B_i,b^l B_j,a^l)
      +(k_l/2)[q_a,ij tr(B_i,b^l+B_j,b^l)
                −q_b,ij tr(B_i,a^l+B_j,a^l)]}
      −(15/8)q_a,ij q_b,ij

has character χ_r=χ_aχ_b. No block, endpoint-linear term, or edge correction has been omitted.

Write L_d=g_ij⁻¹V_dg_ij and H_d=g_ij⁻¹g_jk⁻¹(V_dg_jk)g_ij. They have character χ_d. Thus k_r=[L_a,L_b]/4 has character χ_r, as does the source's equivalent adjugate derivative expression. The gerbe b_r=(15/4)q_a,ij q_b,jk and

    C_r=g_ik⁻¹ μ_r(g_jk,g_ij),       F_r=b_r−tr(C_r)/2

have character χ_r, because μ_r adds the two directional signs. Consequently the ACTUAL first lift

    U_r,ij=g_ij(s_r,ij Id+k_r,ij)

has character η_iη_jχ_r. The same statement holds for its baseline part u_r,ij=g_ij k_r,ij. No replacement of the raw scalar by a selected primitive is being made.

## 5. All slots of the mixed residual, including δW

For homogeneous matrix inputs of characters α,β, the source bidifferentials obey

    char μ_r(H,G)=αβχ_r,      char μ_pq(H,G)=αβχ.

The four terms of μ_pq differentiate in tuples (0,2;1,3), (0,3;1,2), (1,2;0,3), (1,3;0,2). Each uses all four directional signs once. Matrix order and numerical signs do not change character.

Take the COMPLETE ten-term expression D of FIRST-LIFT-STRUCTURAL (7.2). Its families are:

1. U_p,jk U_q,ij and U_q,jk U_p,ij;
2. μ_p(U_q,jk,g_ij) and μ_q(U_p,jk,g_ij);
3. μ_p(g_jk,U_q,ij) and μ_q(g_jk,U_p,ij);
4. μ_pq(g_jk,g_ij);
5. −b_p U_q,ik and −b_q U_p,ik;
6. −b_p b_q g_ik.

Every one of these ten terms has character η_iη_kχ: in the first six, η_j occurs twice; in all remaining terms the endpoint signs are already η_iη_k. Left multiplication by g_ik⁻¹ cancels these signs, so M=g_ik⁻¹D has character χ. Replacing each U_r by its exact baseline u_r=gk_r gives the SAME ledger for M0. Trace-free projection preserves χ, including the normalized scalar gerbe term even though its trace-free contribution vanishes.

The literal residual is

    R=tf(M0)+F_q k_p,ik+F_p k_q,ik+E_p(s_q)+E_q(s_p),

where

    E_(a,b)(s)=[(V_a s_jk)L_b−(V_b s_jk)L_a
                 +(V_b s_ij)H_a−(V_a s_ij)H_b]/2.

Both Fk terms have character χ. Each of the four displayed E_p(s_q) terms has character χ_qχ_aχ_b=χ, and exchanging p,q gives the other four terms. Thus the ten normalized baseline slots, two Fk slots, and eight E slots are separately full-sign. This authenticates the entire actual formula, not just an abstract obstruction or one kinetic term.

For the source's scalar-elimination identity, W=s_q k_p+s_p k_q is a χ-character End edge. Since the actual Čech differential commutes with deck action, δW has character χ. Therefore

    R=tf(M)+δW

is also an equivariant equality of the same pure cochains. Nothing depends on dropping this correction or changing representatives. The usual supplementary bookkeeping with formal star parameters of characters χ_p and χ_q makes each summand of g+tU_p+uU_q have its endpoint sign, but this is only a check; the explicit ledger above proves the claim without that shortcut.

The source-family closure theorem gives δR=0 on this exact regular cover. Purity does not need closure to hold; closure is used only to pass from this proved cochain identity σR=χ(σ)R to its cohomology class. All identities are regular family identities, valid over the parameter ring and preserved by arbitrary base change. There is no inference from vanishing at geometric points and no evaluation of any residual.

## 6. Exact consequences for the relative zero scheme and its derivative

For the neighborhood B of the relative theorem, the averaging idempotent eχ acts as identity on R itself. Thus the entire relative class is rχ in the rank-352 bundle V, and all other character projections of this particular class are zero. The ideal generated by V∨ evaluated on rχ defines precisely total relative mixed-class vanishing; introducing the total cohomology sheaf cannot add equations from the other character components of this section. The existing arbitrary-base-change statement for V gives the claimed scheme-theoretic, including Artinian, interpretation. This requires no new dimension table for the other character summands.

In these authenticated frames and cover labels the deck action is independent of the coefficient parameters. Hence eχ commutes with parameter differentiation, and dot R is automatically full-sign. One may use a full-sign primitive Q at a zero b and an equivariant first-order extension: averaging any extension is valid and preserves its central value. All terms in the corrected derivative

    D_τ=dot R−dot δ Q−δ dot Q

then have character χ. In the relative theorem's row convention,

    (dot δ Q)_ijk=[g_ij⁻¹Q_jk g_ij, a_ij],
    a_ij=g_ij⁻¹ dot g_ij,

and a_ij is invariant. This term still must be retained: parameter independence of the character projector does not make the changing Čech differential constant. The same tangent criterion T_bZχ=ker drχ_b applies to total mixed-class vanishing. In an arbitrary parameter-dependent, non-equivariant matrix gauge, the projector coordinates may vary, and that theorem's warning about differentiating the actual projection remains correct. No unrestricted identification of varying H² fibers or free H²-valued variation is asserted.

## 7. Boundaries

