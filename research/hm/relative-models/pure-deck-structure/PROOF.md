> Publication scope: Static source-character theorem and marked action extension under supplied geometric and first-order premises. No actual-source evaluation. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Genuine deck equivariance of the prescribed pure first-order lift

## Result and exact scope

**The missing deck-equivariance premise is satisfied.** For each pure pair r=(0,1) or r=(2,3), the actual prescribed first-order module, interpreted as the source's mathematical rational/regular denotation and using the accepted geometric and first-order-existence theorems, carries a genuine semilinear action of H=(Z/2)^4. It preserves the fixed classical linearization and is compatible with every local product, module overlap and triple unit. No change of the prescribed first-order transitions is needed to obtain this H-action.

This is a static transformation proof for the complete first-order transition, not just its scalar term. It closes a source-attribution/equivariance dependency. It evaluates no physical source, matrix, input, rank, operator, residual, jet, residue, determinant or detector; imports/runs no physical code; and grants no execution admission. The coefficient 15/8 is read from the source, not recomputed from a physical instance.

The two assertions are separate:

1. The theorem here supplies the genuine deck-H structure of the prescribed pure lift.
2. The imported weight-two Ext1 vanishing then gives rigidity within the H-equivariant marked lifting category. Together with the separate finite-group lifting/effectivity theorem, this permits extension to the full signed-pair group while retaining this marked H-lift, once the full-group ambient/boundary identification is fixed.

Neither assertion is mixed module existence or an evaluation of its obstruction. A single parameter for the sum of both pairs is not asserted to have one character under all of H: the theorem is on each pure axis, or their square-zero fiber-product boundary with independently transforming parameters.

## 1. Immutable sources and imported geometry

Immutable public sources (2026-10-19):

- [Raw engine at commit 4659e4425c6b5ab6b1899e6af93656ac03ff0862](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-second-order-raw-closure/inputs/raw_engine.py.txt), Git blob 34a230aedc9e6d47148195752da54c30c576f53a, SHA256 c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9.
- [First-order source/proof, same commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-second-order-raw-closure/inputs/first-order-source.md), Git blob 5f4e56252cd9a8a6eb218aceb911c95a1c330ebc, SHA256 502baffafd3e0d271f6a83e2eaf0c847b023a2bcc7e81273fbb438269492a8d6; especially §§1,3,4.
- [Raw first-order transgression, same commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-raw-first-order-transgression/PROOF.md), Git blob bcdcf5dd3925cebfd269ebb61a265823a12ffe26; especially §§1,4,5,8.
- [Raw second-order closure, same commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-second-order-raw-closure/PROOF.md), Git blob a3894976f186b3f3bfb4d4953497c468ae041b3b; §2 explicitly identifies the full pure lifts used by the frozen raw route.
- [Declared ambient at 08b73637d4136f91606aad332c46cafd064417f8](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/ambient-second-jet.md), Git blob e07d4373a7c22f7cf4502260d80dbd559d942850; §3 fixes the row-left module convention and first-order descent equation.
- [Complete reduced generator at 6032b64d3f748c7ac37cb283db4a527e49d06ac8](https://github.com/Akilleez-QA/read-em-and-weep/blob/6032b64d3f748c7ac37cb283db4a527e49d06ac8/research/hm/current-scalar-source-bridge/public_generate_hm_mask_coefficients_reduced.js), Git blob 30c0cd334c0f188f4699f853afb14740acb48a5d. Its globalBuild2.first, lines 49–53, explicitly builds K, Z=-K/2+scalar Id, and returns G Z.

The public source URLs and Git blob identifiers above bind the immutable inputs; SOURCE-PINS.json records those pins. Previously public source snapshots are not duplicated here.

Geometric/existence inputs are the previously independently accepted structural-raw-closure v2 proof and full-source-character proof, copied with their reviews into dependencies/. The former's SHA256 is 50ec1df804dc461c928dfcd8bba8d4428206e36a0b7f1686a9aa2f43731db490; the latter's is ce17740962e0f5e7dd23fd1bc3613704ea8d83a81d343827304338e2e686b94f. Structural-raw-closure §§2–6 supplies the single actual complex, actual root/quotient frames, regularity on the entire carrier/legal cover, determinant-one normalization, and the first-order equation. Full-source-character §5 and its review supply the all-standard-chart frame comparison and intrinsic deck character. These imported theorems, rather than a new arithmetic run, discharge the geometric premises retained by the older public transgression theorem.

For the transformation argument itself only the actual frame/leaf denotation is needed. First-order existence and regularity enter when interpreting the transformed formulas as a global module rather than a collection of rational expressions. This distinction is retained throughout.

## 2. Genuine classical action and stable cover

Let X=C^4, C the smooth projective curve y²=x³−x. For σ in H write ε_d(σ) in {1,-1} for its action on y_d; x_d is fixed. For a subset r set χ_r=product_(d in r) ε_d. The six projective carrier opens depend only on the symmetric x coordinates, so each is fixed by H. Both legal opens C minus infinity and C minus the three finite branch points are inversion-stable. Thus every owner open and every ordered owner intersection is H-stable. No owner permutation or Čech sorting is needed for H.

For owner i of legal mask m_i define

    η_i(σ)=product_d ε_d(σ)^(m_i,d),
    ν_i=product_d (y_d/x_d)^(m_i,d).

The actual line is N=external product O_C(O), with its canonical divisor linearization. Its invariant rational reference section gives the actual regular legal frame e_i=ν_i e_ref; hence σ(e_i)=η_i e_i. The sign is a constant, and η_i is a group character, not a point-dependent comparison unit.

On a standard product chart A, put c_iA=e_i²/ell_A=ν_i² τ_A, where τ_A is the product of infinity coordinates. This is the actual regular unit on the legal/standard intersection. Both c_iA and the projective coefficient vector v_A are H-invariant. In the e_i-powers of the complex K, all weights (-1,1,3,5) are odd; hence the deck action is the same scalar η_i on every degree's frame. The coefficient matrices of the differential and the legal split bases are invariant. This gives a genuine action on the whole complex, and hence on its degree-zero cohomology E.

In the rank-15 term the two quotient columns are, in e_i coordinates,

    I_i(v_A) diag(1,c_iA^-1).

Their coefficients are invariant, so the actual cohomology frame has scalar character η_i on BOTH columns. In rational reference coordinates these same columns are I_i D_i with D_i=diag(ν_i,ν_i^-1). Both entries of D_i also have character η_i. The all-chart expression is what validates the interpretation where the rational reference frame is not regular; no square root of τ_A is introduced and no branch coordinate is inverted illicitly.

The source's row transition is exactly

    g_ij=D_j (P_i I_j)^t D_i^-1.

Its intrinsic classical deck law in these fixed quotient frames is

    σ(g_ij)=η_j(σ)η_i(σ) g_ij.                       (2.1)

This is the original classical linearization induced by K. It is not a new line twist selected to force a parity result.

## 3. Static weight proof for every first-order coefficient

The global vector fields satisfy σ V_d σ^-1=ε_d(σ)V_d. On the finite chart this follows from V(x)=y and V(y)=(3x²−1)/2; on the infinity chart t=1/x, u=y/x² it follows from V(t)=−u and V(u)=(3t²−1)/2. These descriptions agree, so the relation respects every restriction and legal localization.

The raw primitive entries are rational expressions in v and hence invariant. All powers of ν in blocks are even. Thus the scaled U,Q in the raw blocks are invariant, V_d(U) has character ε_d, and the retained old-connection coefficient

    (m_i,d)y_d/[x_d(x_d²−1)]

has character ε_d. Consequently every one of the four blocks B_(i,d) has character ε_d. The source leaf q_(ij,d)=(m_j,d−m_i,d)y_d/x_d has the same character. This remains true on all charts because B is the actual difference of the transported split and old connections; their common frame-derivative term cancels. The old connection is never reset at infinity.

Fix the ordered pure pair r=(a,b). In raw_scalar_formula every wedge trace uses one a-block and one b-block. Every endpoint-linear term uses q_a with a b-block, or q_b with an a-block. Its final term is exactly −(15/8)q_a q_b. All terms therefore have character χ_r, with all four block traces and both endpoints retained:

    σ(s_raw,r,ij)=χ_r(σ)s_raw,r,ij.                  (3.1)

Put μ_r(H,G)=((V_a H)(V_b G)−(V_b H)(V_a G))/2. If H,G have scalar characters χ,ψ then μ_r(H,G) has character χψχ_r. The actual g^-1 has the same character η_iη_j as g; this follows either by applying σ to gg^-1=1, or directly from the source's rank-two adjugate entries. Hence

    k_r,ij=−μ_r(g_ij^-1,g_ij)/2

has character χ_r. Consequently the ENTIRE normalized first coefficient and transition correction have laws

    x_r,ij=s_raw,r,ij Id+k_r,ij,
    U_r,ij=g_ij x_r,ij,
    σ(x_r,ij)=χ_r(σ)x_r,ij,
    σ(U_r,ij)=η_i(σ)η_j(σ)χ_r(σ)U_r,ij.             (3.2)

These are symbolic transformation laws. They require no actual value, coefficient expansion, matrix multiplication or cancellation evaluation.

## 4. Why this is the actual full prescribed lift

RawSource.T alone denotes a scalar override and is not the full transition. We do not make that substitution. The full identification has three independent textual links:

1. First-order-source §3, formula (5), prescribes x=s Id−K(g)/2 and u=gx, with K(g)=μ_r(g^-1,g).
2. Its §4 identifies the complete source globalBuild2.first: scalar is the unsymmetrized all-block formula including −15q_aq_b/8, K is μ_r(g^-1,g), Z is −K/2+scalar Id, and the return value is G Z. The complete generator literally contains all of these operations and returns them as u12,u34. Its stripped y factors/jet convention is identified with the geometric invariant derivatives by that source bridge; no stripped coefficient is mistaken for the unstripped physical transition.
3. Current raw-second-order-closure §2 explicitly uses the SAME first lifts U_r=g(s_raw,r Id+k_r) in T_ij=g_ij+tU_p,ij+uU_q,ij. Thus the raw scalar is tied to that complete first-order transition, not to a freely chosen scalar-only extension.

The accepted structural-raw-closure v2 §6 establishes, on every actual common triple,

    U_r,jk g_ij+g_jk U_r,ij+μ_r(g_jk,g_ij)
        =U_r,ik+b_r,ijk g_ik,
    b_r,ijk=(15/4)q_a,ij q_b,jk.                     (4.1)

The U_r,ik term is essential and is retained. This accepted v2 equation, together with regularity and invertibility from its §§2–4, supplies the existing global pure module whose genuine H-action is now being proved.

The stage-2 HPL closed_lift_schema controls a different residual/lift construction. It neither defines nor substitutes for the first-order module transition. No HPL recurrence, scalar-solver leaf, or higher residual attribution is needed for (4.1) or for the action below.

## 5. Strict semilinear action on the ambient and module

Work on one pure axis with R_r=C[epsilon]/(epsilon²). Extend the deck action by σ(epsilon)=χ_r(σ)epsilon. The pure ambient has

    f star g=fg+epsilon μ_r(f,g),
    F_ij=id,
    A_ijk=1+epsilon b_r,ijk.

Let α_σ be the combined action on functions and epsilon. The derivative law proves

    α_σ(f star g)=α_σ(f) star α_σ(g).

Indeed applying σ to μ_r supplies χ_r, and applying σ to epsilon supplies the same sign; they cancel. The ordered gerbe b_r has character χ_r, so α_σ(A_ijk)=A_ijk. Identity overlaps are preserved. Thus this is a genuine action on the precise pure ambient presentation, including its triple units.

Define the complete prescribed pure transition

    T_ij=g_ij+epsilon U_r,ij.

By (2.1) and (3.2), the combined coefficient action has the uniform law

    α_σ(T_ij)=η_i(σ)η_j(σ)T_ij.                    (5.1)

On the local free LEFT module, represented by ROW coordinates as in the declared ambient, define

    rho_i(σ)(v)=η_i(σ) α_σ(v).                      (5.2)

Constants are central for star multiplication, so (5.2) is semilinear over α_σ. The source overlap is phi_ij(v)=v star T_ij. Formula (5.1) gives the full overlap intertwining identity

    rho_i(σ)(phi_ij(v))
      =η_i α_σ(v) star α_σ(T_ij)
      =η_j α_σ(v) star T_ij
      =phi_ij(rho_j(σ)(v)).                         (5.3)

There are no missing differentiated frame terms: η_i is constant, so all V_d(η_i) are zero. The triple module identity T_jk star T_ij=A_ijk star T_ik is (4.1); alpha fixes A and (5.3) respects that identity. At pure first order ordinary versus star multiplication of A with T agrees, because its nonconstant part is already epsilon-weighted.

Finally η_i is a character and alpha is a genuine action. Therefore

    rho_i(σ)rho_i(tau)=rho_i(στ),    rho_i(1)=id.    (5.4)

Equations (5.3)–(5.4) prove global compatibility on the algebroid module. This is an exact semilinear action, not a projective action, a weak action modulo inner units, or invariance of an isomorphism class alone. At epsilon=0, (5.2) is exactly the action on the actual classical quotient frame established in §2, so it preserves the chosen classical marking.

## 6. Globality, branch loci and transport to the comparison presentation

The owners form the actual stable carrier/legal cover. All coefficient expressions in §4 are regular on their declared intersections by the accepted first-order existence theorem. Every statement above commutes with restriction. Standard-chart changes merely re-express the same fixed owner cohomology frame: c_iA and the homogeneous primitives change together, while the intrinsic frame character η_i is unchanged. Thus the construction is global on X and includes branch and infinity strata. A dense rational-chart parity calculation alone would not establish this step; the actual all-chart frame bridge is used explicitly.

The antisymmetrizing pure gauge from the separate quantum-swap-gauge proof has Q_ij=1−(epsilon/2)c_r,ij with c_r=(15/4)q_a,ij q_b,ij. Its c_r has character χ_r, hence Q is H-invariant. Its transported module transition Q_ij^-1 star T_ij still obeys (5.1), with the SAME rho_i. Therefore passing to the symmetric pure presentation does not lose or alter the supplied H marking.

For subsequent root/Morita transport, the existing root frames obey σ(e_i)=η_i e_i with exact sign coherence. Equivariant tensor/Morita transport carries the action (5.2) along this specified root datum; it is not permission to erase spatial root transition units or to assume a different coarse atlas. The choice and effectiveness of that ambient/root comparison belong to the separate comparison theorems. The same statement applies to both pure axes. Their reductions agree with the same fixed classical action, so the square-zero fiber-product boundary inherits the action componentwise.

## 7. Rigidity consequence and precise remaining boundary

For a fixed pure ambient and fixed classical marking, the difference space of marked lifts is Ext1(E,E) tensor C epsilon, with its prescribed deck action (or its equivalent endomorphism-valued coefficient interpretation). Finite-group invariants are exact in characteristic zero. Thus the H-equivariant difference space is

    (Ext1(E,E) tensor C_chi_r)^H = Ext1(E,E)_chi_r.

The source [comment 6260553958](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260553958), directly read, imports per-deck-character dimensions by weight (79,2,0,0,0); only its weight-two zero is needed here. Under that imported Ext identification, the actual H-equivariant pure lift established above is the sole H-equivariant marked isomorphism class for that ambient. This does not say all upstairs Ext1 vanishes, choose a preferred Čech representative, or prove unique isomorphisms without the separate Ext0 condition.

The independent equivariant-module-lift-effectivity theorem, §10, now applies with its formerly missing H-equivariance hypothesis supplied: if the fixed classical boundary and the compared pure ambient carry the stated full signed-pair action, some full-group lift exists whenever an ordinary pure lift exists; H-rigidity identifies its restriction with this prescribed H-lift, and transporting the action gives a full-group action on this very marked module. The construction preserves the existing H action. This consequence uses that independent theorem, the imported weight-two Ext1 calculation, and the actual ambient/boundary comparison; none follows from character parity alone.

There is no remaining scalar-to-full-transition or H-overlap-coherence gap for the source-bound pure mathematical lift. Its geometric existence inputs and Ext table remain explicitly imported results. Higher-order module existence, mixed obstruction evaluation, retained physical values, runtime arithmetic correctness, and execution admission remain outside this theorem and unchanged.
