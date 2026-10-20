# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: finite square-component detector

## Verdict

The finite detector construction is valid for X=8C, including the ambient Ext degrees and all plane twists. The optional dimension conclusion is also valid: its full detector space has dimension 0, 3, or 10. None of these statements evaluates the actual component restriction map or selects which dimension occurs for the particular bundle.

The Riemann–Roch constant is **360**, not 384:

    h¹(X,H|X)=360+h⁰(X,H|X).

This audit treats the previously established exact section resolution and geometric identification of the square component as inputs. It independently checks their claimed consequences here.

## 1. Restriction to the finite thickening

Let E=i*F on W=P², B_W=End₀(E), G_W=B_W(-2), and H=B_W(-1), with all displayed twists on W being plane twists. The ambient restriction G=B(-1)→i_*G_W is correct because i*O_Y(1)=O_W(2). The trace pairing on B_W is nondegenerate over C, so B_W is self-dual.

The supplied resolution gives H¹(End(E)(t))=0 for t≥14, and global generation of End(E)(14). Since End(E)=O⊕B_W, the same H¹ vanishing holds for B_W. The dual evaluation injection End(E)→O(14)^N gives H⁰(B_W(-17))=0. Serre duality gives

    H¹(B_W(-17))*=H¹(B_W(14))=0.

The Cartier divisor X=8C has ideal O_W(-16). Thus

    0→B_W(-17)→H→H|X→0

induces an isomorphism

    res_X:H⁰(W,H) → H⁰(X,H|X).

This is a vector-space isomorphism, not an algebra assertion: H is a negatively twisted endomorphism bundle. It uses the actual bundle on the entire thickening, not only its reduced-conic splitting or freely chosen infinitesimal coefficients.

## 2. Ambient Ext realization

Write k:X→Y for the composite closed immersion and D=k_*(B_W(14)|X). The exact sequence is

    0→i_*G_W→i_*(G_W(16))→D→0.

Here (16) means a plane twist inside i_*, not an ambient twist. The right-hand bundle is B_W(14), as required. Apply global Ext_Y(-,ω_Y). The relevant segment is

    Ext²_Y(i_*G_W(16),ω_Y)
      →Ext²_Y(i_*G_W,ω_Y)
      --δ→Ext³_Y(D,ω_Y)
      →Ext³_Y(i_*G_W(16),ω_Y).

Serre duality on the smooth fourfold Y, followed by cohomology of a closed pushforward, identifies the outside terms with

    H²(W,B_W(14))* = H⁰(W,B_W(-17)),
    H¹(W,B_W(14))* = H¹(W,B_W(-17)),

respectively. Both vanish, so δ is an isomorphism. These are global Ext groups; confusing them with individual sheaf-Ext groups would invalidate the argument.

The middle terms identify as

    Ext²_Y(i_*G_W,ω_Y)=H²(W,G_W)*=H⁰(W,H),
    Ext³_Y(D,ω_Y)=H¹(X,B_W(14)|X)*=H⁰(X,H|X).

For the last equality X is a Gorenstein plane divisor of degree16, so ω_X=O_X(13); consequently (B_W(14)|X)^∨⊗ω_X=B_W(-1)|X. Nonreducedness creates no obstruction to this duality.

Under compatible Serre-duality and Cartier-adjunction/residue conventions, δ is res_X. Equivalently, δ is the transpose of the cohomological boundary H¹(X,B_W(14)|X)→H²(W,G_W). Defining the Yoneda connecting map and residue trace compatibly fixes its sign. If a different convention changes that comparison by a common minus sign, it must be carried consistently through δ⁻¹; no kernel, image, rank, or vanishing criterion changes.

Let u:G→i_*G_W be ambient restriction. Precomposition gives

    u*:Ext²_Y(i_*G_W,ω_Y)→Ext²_Y(G,ω_Y).

Naturality of Serre duality identifies u* with r_W*, the transpose of r_W:H²(Y,G)→H²(W,G_W). Since ω_Y=O_Y(-5), B is self-dual, and G is locally free,

    Ext²_Y(G,ω_Y)=H²(Y,G^∨⊗ω_Y)=H²(Y,B(-4)).

Therefore the finite detector is u*∘δ⁻¹ on Ext³_Y(D,ω_Y), or equivalently r_W*∘res_X⁻¹ on H⁰(X,H|X). No normal-coordinate splitting or choice of a lift is needed. Its image is the actual square-component detector image. The finite space alone does not determine whether that ambient map is zero or its rank.

## 3. Optional dimension sharpening

The auxiliary saturated-line bound a≤1 is sound. For a saturated line O(a)⊂E the torsion-free quotient is I_Z(-2-a), where

    length(Z)=16+a(a+2).

The saturated rank-one subsheaf is a line bundle: on the smooth surface it is reflexive, by the depth lemma applied to the torsion-free quotient. Global generation of E(8) implies that I_Z(6-a) is globally generated. Put d=6-a. This forces d≥0; d=0 would force Z empty, contradicting the displayed positive length. Two general generating sections with no common curve give length(Z)≤d², hence 14a≤20 and a≤1.

Suppose φ:E→E(-1) is nonzero. Its trace and determinant lie respectively in H⁰(O(-1)) and H⁰(O(-2)), and therefore vanish. Twisted Cayley–Hamilton gives φ(-1)∘φ=0. Its generic rank is one. The saturated kernel K=O(a) has quotient Q=I_Z(-2-a), and nilpotence yields the factorization

    E→Q→O(a-1)→E(-1).

Since Hom(I_Z,O)=O on the smooth surface, a nonzero middle map requires a section of O(2a+1). Therefore a≥0; together with the bound, a is 0 or1.

There is at most one saturated line of degree≥0 in E. If two such lines were generically distinct, their wedge would be a nonzero section of O(-2-a-b), impossible. If they are generically identical, saturation makes them equal. Thus this K is shared by every nonzero negative-one-twist endomorphism. Conversely, every map Q→K(-1) defines such an endomorphism, and the composition is injective on the Hom space. Consequently

    H⁰(W,End(E)(-1)) ≅ Hom(Q,K(-1))
                         ≅ H⁰(W,O(2a+1)).

Every map has trace zero, so this equals H⁰(W,B_W(-1)). A chosen identification K≅O(a) is enough for the displayed line-bundle description; the dimension conclusion requires no such choice. Hence

    h⁰(W,H)=h⁰(X,H|X) ∈ {0,3,10}.

If the space is nonzero, the unique destabilizing saturated line has degree0 or1 and dimensions3 or10 respectively. Conversely existence of either such line supplies the nonzero maps through the factorization. This is a structural alternative, not a determination of which case occurs for E. In particular it does not determine rank(r_W).

## 4. Riemann–Roch check

For B_W one has rank3, c₁=0, and c₂=4c₂(E)-c₁(E)²=60. Thus

    χ(B_W(t))=3(t+1)(t+2)/2-60.

The restriction sequence gives

    χ(X,H|X)=χ(B_W(-1))-χ(B_W(-17))=-60-300=-360.

Since X has dimension one, this yields h¹=360+h⁰. Independently, the degree16 plane divisor has arithmetic genus105 and H|X has degree−48, giving χ=−48+3(1−105)=−360. The possible h¹ dimensions are therefore 360,363,370.

## Scope

No HM matrix, selected rank, explicit conic splitting type, component value, or source instance was evaluated.
