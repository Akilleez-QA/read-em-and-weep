# Canonical projective splitting and the three tautological lines

## Theorem and conventions

Work over C in the same canonical cubic setup as /research/hm/middle-surface/rank-one-open-thickening/PROOF.md and /research/hm/middle-surface/rank-one-global-splitting/PROOF.md. Put P=P(V), dim V=5, and let B=P\Z be the rank-ten open for the quadratic residual normal map. Here B denotes the **projective** open, unlike the affine punctured cone denoted B in the global-splitting reference. Let L=O_P(-1)|B.

Let X_pr be the zero scheme of the multihomogeneous equations f in P^3=P×P×P. The diagonal over B has an open neighborhood S in X_pr whose reduction is precisely that diagonal. Equivalently, S is the isolated infinitesimal component along the good diagonal; removing ambient closed sets disjoint from its support does not alter it. Then:

1. Its nilradical is canonically Ω_B, with square zero. The middle projection π2:S→B is a canonical retraction, and canonically

       O_S = O_B ⊕ Ω_B,
       (a,α)(b,β)=(ab,aβ+bα).

   This identification fixes the residual tangent by taking first input minus middle input. Under it the three projections induce

       π1*(a)=(a,da),   π2*(a)=(a,0),   π3*(a)=(a,−da).

2. In particular S is canonically the first infinitesimal neighborhood of the diagonal in B×B, with base the middle coordinate and second coordinate the first input. The third input is its canonical infinitesimal reflection. The nilbundle is Ω_B, not Ω_B(1).

3. Write L_r=πr*L and L_0=π2*L. The middle retraction gives

       Pic(S) ≅ Pic(B) ⊕ H¹(B,Ω_B).

   If local frames satisfy e_j=g_ij e_i, define c(L)=[dlog(g_ij)]. Then

       [L1]=([L], c(L)),
       [L2]=([L], 0),
       [L3]=([L], −c(L)).

   The class c(L) is nonzero. Consequently neither outer line is isomorphic to the middle line; the two outer lines are also nonisomorphic. There is a canonical isomorphism

       L1 ⊗ L3 ≅ L2^⊗2

   restricting to the identity on the reduction.

4. The all-nonzero affine thickening is the threefold frame torsor

       T = L1^× ×_S L2^× ×_S L3^×.

   Its nonsplitting is compatible with the canonical splitting of S: the frame torsors of the two outer line bundles have opposite, nontrivial infinitesimal deformation classes. The explicit frame cocycles recover exactly the previously proved affine obstruction.

The last isomorphism in (3) is the canonical one constructed from the projection maps and the local frames, not a claim that every isomorphism inducing the identity on reduction is unique.

## 1. Descent of the actual scheme structure

On the locus of three nonzero affine inputs the map

    (V\0)^3 → P^3

is a Zariski locally trivial (G_m)^3 torsor. The cubic equations are homogeneous in the three inputs, so their zero scheme descends under this torsor. Rank of the residual quadratic normal map is unchanged by these independent scalings. The exact square-zero local equations from the open-thickening theorem therefore apply on projective charts as well.

More explicitly, choose ℓ∈V* and normalize all three projective representatives by ℓ=1. Near the diagonal write them as

    (u+p, u, u−p+w),    ℓ(u)=1, ℓ(p)=ℓ(w)=0.

The exact eliminated equations of the cited proof express w as a function in (p)^2. On the rank-ten open the remaining ideal is exactly (p)^2 by coherent Nakayama. Therefore w=0 on the zero scheme and its exact chart is

    (u+p,u,u−p),    (p)^2=0.

These are actual algebraic charts, not merely tangent cones or completed rings. Their reductions are the diagonal; they glue to S. In particular there is no other component meeting the good diagonal. Each projection has image in B because its underlying topological map is the identity on B, so all three πr:S→B are well-defined.

## 2. Coordinate-free residual tangent and canonical algebra

At a diagonal point b the ambient tangent is T_bB^⊕3 and the diagonal tangent is its diagonal subspace. Identify the normal quotient with two copies of T_bB by

    (ξ1,ξ2,ξ3) ↦ (ξ1−ξ2, ξ3−ξ2).

The repeated-input derivative relation and its rank-four injectivity say that the linear equations kill the sum of these two differences. This also follows directly from the preceding exact equation whose linear term is A_u(w). Thus the residual normal kernel is canonically

    T_bB → T_bB⊕T_bB,    ξ↦(ξ,−ξ).

The dual residual conormal is Ω_bB, giving a bundle identification N≅Ω_B. In intrinsic projective notation, T_B=Hom(L,(V⊗O_B)/L), so its dual is ((V⊗O_B)/L)*⊗L=Ω_B. The affine identification with Ω_P(1) uses an actual nonzero middle vector to trivialize the extra factor L; that trivialization does not exist on B itself.

The existing morphism π2 gives an algebra splitting of O_S→O_B. Hence O_S≅O_B⊕N canonically for this specified projection. Since two morphisms agreeing on a square-zero reduction differ by a derivation, π1*−π2* and π3*−π2* are derivations O_B→N. The preceding tangent identification says their induced maps Ω_B→N are respectively identity and minus identity. The universal property of differentials proves the formulas in the theorem for every local regular function a.

The morphism (π2,π1):S→B×B annihilates the square of the diagonal ideal. It thus factors through the first infinitesimal diagonal. On reduction it is the identity, and on its conormal Ω_B it is the identity. The exact sequences of structure sheaves then prove it is an isomorphism. Swapping the two infinitesimal directions relative to the fixed middle base gives the map a↦a−da for the third projection. No coordinate-dependent choice of a connection or midpoint is needed.

## 3. Explicit projective coordinate transitions

Cover B by B_i={ℓ_i≠0}. Let u_i be the normalized tautological representative with ℓ_i(u_i)=1, and use the nilpotent vector p_i∈ker ℓ_i from Section 1. On B_i∩B_j put

    a_ij=ℓ_j(u_i),    b_ij=ℓ_j(p_i).

Here a_ij is invertible and b_ij lies in N. The exact overlap formulas are

    u_j = u_i/a_ij,
    p_j = p_i/a_ij − b_ij u_i/a_ij².

Indeed normalize u_i+p_i by a_ij+b_ij and use N²=0; the minus representative is normalized by a_ij−b_ij. These are precisely the derivative transition functions of projective coordinates. Thus p represents a tangent displacement, while its linear coordinate functions glue as Ω_B.

There are no shifts of base coordinates by nilpotents: u_j is solely a function of u_i. This is the coordinate manifestation of the global middle retraction, in contrast to the affine torus-coordinate shifts in the global-splitting reference.

## 4. Picard group and linebundle deformation cocycles

For the split square-zero algebra there is a canonical decomposition of sheaves of abelian groups

    O_S^× ≅ O_B^× × Ω_B,
    (a,α) ↦ (a,α/a),

where the second factor is additive. Taking H¹ gives the stated Picard decomposition. In particular the injection H¹(Ω_B)→Pic(S) is injective, not merely a map modulo a potentially nonzero boundary from global units: the global splitting of units kills that boundary.

For any local frames e_i of L, with e_j=g_ij e_i, the transition of πr*L is πr*(g_ij). Relative to the middle lift it is

    L1: g_ij(1+dlog g_ij),
    L2: g_ij,
    L3: g_ij(1−dlog g_ij).

This proves the three classes. It also identifies the underlying O_B-module extensions

    0→L⊗Ω_B→(π2)_*L_r→L→0

with the classes +c(L), 0, −c(L) in Ext¹_B(L,L⊗Ω_B)=H¹(B,Ω_B), using the convention that local lift differences are lift_j−lift_i. Thus the first is the usual first-jet/principal-parts extension with the indicated projection convention, and the third its opposite.

The products of the first and third transitions equal g_ij² exactly, since (dlog g_ij)^2=0 in O_S. Sending the local generator π1*e_i⊗π3*e_i to (π2*e_i)^⊗2 therefore glues. Changing e_i by any invertible local function leaves this construction unchanged, proving the canonical tensor-product isomorphism.

For the normalized projective frame e_i=u_i one has g_ij=a_ij^−1 and

    dlog(g_ij)=−b_ij/a_ij

under the identification N=Ω_B. This agrees directly with the normalized outer representatives.

## 5. Nonvanishing on the full good open

The existing saturated-image argument, recalled in Section 1 of /research/hm/middle-surface/rank-one-global-splitting/PROOF.md, proves codim_P(Z)≥2. A section of the locally free sheaf O_P(-1) over B extends uniquely across Z, by normality/reflexive extension. Consequently

    H⁰(B,O_B(-1))=H⁰(P,O_P(-1))=0.

Restrict the Euler sequence to B:

    0→Ω_B→V*⊗O_B(-1)→O_B→0.

The connecting class δ(1) is nonzero, because there is no global section of its middle term mapping to 1. To compare signs, its local lift on B_i is ℓ_i⊗u_i. On an overlap the difference of these lifts corresponds under the usual cotangent identification to dlog(a_ij). Since g_ij=a_ij^−1, this gives

    δ(1)=−c(L).

Thus c(L)≠0. In characteristic zero also 2c(L)≠0, proving the claims of pairwise nonisomorphism of the three lines. This uses only the codimension-two bound; no assumption about emptiness, smoothness, or greater codimension of Z is needed.

## 6. Exact recovery of the affine cocycle

Taking independent nonzero vectors in the three projective lines identifies the all-nonzero affine zero scheme with the threefold frame torsor stated in the theorem. In the normalized chart its tautological vectors are

    x=r1_i(u_i+p_i),
    y=r2_i u_i,
    z=r3_i(u_i−p_i),

with each r nonzero. The representative transitions in Section 3 imply the exact frame-coordinate transitions

    r1_j=r1_i(a_ij+b_ij),
    r2_j=r2_i a_ij,
    r3_j=r3_i(a_ij−b_ij).

On the reduction set s=r1/r2 and t=r3/r2; let their local lifts be S_i=r1_i/r2_i and T_i=r3_i/r2_i. Then

    S_j=S_i(1+b_ij/a_ij),
    T_j=T_i(1−b_ij/a_ij).

The actual middle vector u=y is globally defined. The affine transverse representative is p_i^aff=r2_i p_i. Put λ_i=ℓ_i/ℓ_i(u). Then

    b_ij/a_ij=λ_j(p_i^aff),
    p_j^aff=p_i^aff−λ_j(p_i^aff)u.

These are precisely the transitions of the global-splitting proof. Pullback of Ω_B to the reduced frame torsor, together with the middle frame u of q*L, identifies its nilradical with q*((V⊗O_B)/L)*. The differences λ_j−λ_i represent the connecting class e of evaluation at u, and the algebra-splitting obstruction is therefore

    e·(s∂s−t∂t).

Its nonvanishing was proved in the cited reference, so no claim that pullback preserves every cohomology class is needed here. The explicit frame calculation proves the comparison and explains why a split projective base does not give a split affine total space. The product S_iT_i is global, corresponding to cancellation of the opposite outer line deformation classes.

## Scope

All conclusions concern the universal algebraic zero scheme on the established rank-ten open. No operation, source, selected input, detector, model matrix, residue, or actual instance is evaluated. No assertion is made about the projective rank-drop locus itself, nor about new global structure beyond this open. The affine origin and zero-input boundary require separate arguments.
