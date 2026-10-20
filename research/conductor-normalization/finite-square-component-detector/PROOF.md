# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 08 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# A finite 8C detector for the square-component restriction

## Result

Work over C. Let Y=P^4, F the normalized HM bundle, B=End_0(F), and G=B(-1), where this twist is ambient. Let i:W=P^2→Y be the square-quadratic embedding, with i*O_Y(1)=O_W(2). Write

    E=i*F, B_W=End_0(E), G_W=i*G=B_W(-2),
    H=G_W^∨⊗ω_W=B_W(-1), X=8C⊂W, k:X→Y.

All W-twists below are plane twists. Then

    T_X=H^0(X,H|X) ≅ H^0(W,H) ≅ H^2(W,G_W)^∨.       (1)

There is an explicit, canonical finite-detector map

    Δ_X:T_X→H^2(Y,B(-4))=H^2(Y,G)^∨                 (2)

whose image is the image of the transpose of the actual component restriction r_W:H^2(Y,G)→H^2(W,G_W). In particular,

    r_W(η)=0 ⇔ ⟨η,Δ_X(s)⟩_Y=0 for every s∈T_X.     (3)

The construction below resolves the finite-section extension requirement by a proved isomorphism and a cochain procedure. It does not assert that the ambient class η restricts usefully to X: H^2(X,G|X)=0. The Gysin step, and its possible kernel, remain essential.

An additional structural bound is

    dim T_X ∈ {0,3,10},
    h^1(X,H|X)=360+dim T_X ∈ {360,363,370}.          (4)

No alternative in (4), actual component rank, source value, or HM matrix is evaluated.

## 1. Exact finite determinacy

The imported global-plane argument gives

    H^1(W,End(E)(t))=0 for t≥14,
    H^0(W,End(E)(s))=0 for s<−14.

In characteristic zero, End(E)=O_W⊕B_W, and the trace pairing restricts nondegenerately to B_W. Thus the same vanishings apply to B_W, and B_W^∨=B_W. Since X has ideal O_W(-16), restriction of H gives

    0→B_W(-17) --q^8→ B_W(-1)→H|X→0,             (5)

where q is an equation of the conic. Its left term has H^0=0. Serre duality gives

    H^1(B_W(-17))^∨=H^1(B_W(14))=0.

Therefore the restriction map ρ:H^0(W,H)→T_X is an isomorphism. Every actual section on X extends uniquely; there is no further formal-neighborhood obstruction after order eight in this section-extension problem. This statement concerns H-sections, not a splitting of E|X. It is compatible with the separate nonsplitting theorem at 9C.

The isomorphism is constructive. On a finite affine cover of W, lift s∈T_X to H-sections s_i. On overlaps write s_j−s_i=q^8 a_ij, interpreted invariantly using the divisor line bundle. The a_ij form a Čech one-cocycle of B_W(-17). Its H^1 vanishes, so choose b_i with a_ij=b_j−b_i. Then s_i−q^8 b_i glue to the global lift s̃. Choices cannot change s̃, since their difference is a global section of B_W(-17), which vanishes. These are finite covers and finite cochain equations; the affine section modules themselves need not be finite-dimensional. A finite-dimensional implementation may instead use the usual graded resolutions and cohomology complexes on projective space. No infinite jet tower is needed.

## 2. Dual map and ambient Ext realization

Serre duality on W gives the first duality identification in (1). On Y,

    G^∨⊗ω_Y=B(-4),
    H^2(Y,G)^∨=H^2(Y,B(-4)).

Let u:G→i_*G_W be restriction. Duality for the regular codimension-two embedding gives

    Ext^2_Y(i_*G_W,ω_Y)=H^0(W,H),
    Ext^3_Y(i_*G_W,ω_Y)=H^1(W,H).

Here Ext denotes global Ext. Indeed the only nonzero sheaf Ext degree is two, equal to i_*H, so the local-to-global spectral sequence has only one row. Equivalently i^!ω_Y=ω_W[-2]. The embedding is regular because W and Y are smooth; it need not be a global complete intersection. Adjunction gives det N_{W/Y}=O_W(7), since i*ω_Y=O_W(-10) and ω_W=O_W(-3).

Define

    Δ_X = u^* ∘ ρ^{-1},                            (6)

with ρ^{-1} viewed in Ext^2_Y(i_*G_W,ω_Y). The pullback u^* lands in Ext^2_Y(G,ω_Y)=H^2(Y,B(-4)). Naturality of proper duality says exactly

    ⟨η,Δ_X(s)⟩_Y = ⟨r_W(η),ρ^{-1}(s)⟩_W.       (7)

This identity fixes all signs and the normalization of the identifications. Consequently Δ_X=r_W^∨ρ^{-1}; (3) follows by perfect duality. Rank Δ_X=rank r_W≤min(10,dim T_X). The cofactor image J in the preceding filtration is annihilated by these detectors because J⊂ker r_W, so im Δ_X lies in J^⊥=ker α under the earlier transpose convention.

## 3. Finite-support Yoneda formula

There is a useful intrinsic realization of the inverse ρ, rather than merely naming it. Put

    Q=i_*G_W, Q'=i_*(G_W(16)),
    D=k_*[G_W(16)|X]=k_*[B_W(14)|X].

The divisor extension is

    e_X: 0→Q→Q'→D→0.                              (8)

Because ω_X=O_X(13), codimension-three duality identifies

    Ext^3_Y(D,ω_Y)
      =H^0(X,(B_W(14)|X)^∨⊗ω_X)
      =H^0(X,B_W(-1)|X)=T_X.                       (9)

The relevant part of the contravariant Ext long exact sequence of (8) is

    Ext^2_Y(Q',ω_Y)→Ext^2_Y(Q,ω_Y)
       --∂_e→Ext^3_Y(D,ω_Y)→Ext^3_Y(Q',ω_Y).

The outside terms are respectively H^0(W,B_W(-17)) and H^1(W,B_W(-17)), hence both zero. Thus ∂_e is an isomorphism. Under duality-compatible adjunction conventions it is exactly ρ. This can also be checked on a local Koszul resolution: adding q^8 to a local regular sequence for W gives the Koszul resolution for X, and its connecting map is the restriction of the adjunction coefficient.

A finite section s therefore corresponds to an Ext^3 class ξ_s for the sheaf D on X. There is a UNIQUE Ext^2 class γ_s for Q such that

    γ_s composed with e_X = ξ_s,
    Δ_X(s)=u^*(γ_s).                                (10)

Composition here is Yoneda splicing, with (8) in Ext^1_Y(D,Q). Formula (10) is an exact division operation by the fixed divisor extension, justified by the two vanishings; it introduces neither an unspecified choice of extension nor a further obstruction space. In an injective, locally free, or Čech-resolution model, solve the corresponding boundary equation and then precompose with u. Solutions differ by a class in Ext^2(Q',ω_Y), which is zero. Local Koszul choices and cochain primitives may differ, but the resulting Ext class and pairing do not.

## 4. Dependencies that remain, and those that are resolved

The required finite data are the ACTUAL sheaf H|X on the actual nonreduced 8C, including its transition functions and all extension layers, not its associated graded on C. Equation (5) eliminates the existence and ambiguity problems for extending its global sections to W. Equation (10) provides an equivalent Ext construction from finite-support classes.

Nevertheless the detector map also uses the actual embedding W→Y, the ambient coefficient bundle B, the divisor extension (8), and the ambient restriction u. The abstract vector space T_X, a list of splitting degrees on C, or Euler characteristics alone do not determine u^* or its rank. The divisor extension is global W-data, albeit fixed and canonically specified here; (10) is not a formula using only a restriction of η to the curve. The construction removes an infinite-neighborhood dependency and resolves the global-section lifting problem, but it does not replace the ambient Gysin map by a curve restriction or determine its image without the ambient data.

No additional choice of a retraction X→C, normal coordinate, preferred section lift, or cohomology complement is required. Changing q by a scalar changes a presentation of (8), not its intrinsic divisor inclusion and restriction identifications.

## 5. Detector dimensions without actual matrices

First RR alone gives a useful exact equality. For E, c_1=-2h and c_2=16h². Consequently B_W has rank three, c_1=0, c_2=60h², and

    χ(B_W(t))=(3/2)(t²+3t+2)−60.

From (5), χ(H|X)=χ(B_W(-1))−χ(B_W(-17))=−60−300=−360. Since X has dimension one,

    h^1(H|X)=360+h^0(H|X).                         (11)

For a sharper bound, use the independently audited saturated-line argument from the global exclusion audit. Every saturated rank-one subsheaf O_W(a)⊂E satisfies a≤1: its quotient is I_Z(-2-a), with length Z=a²+2a+16; global generation of E(8) implies global generation of I_Z(6-a). Two general generating sections of degree 6-a have no common curve and contain Z, giving a²+2a+16≤(6-a)² and thus 14a≤20. Negative degree or degree zero cannot be exceptions to this argument: global generation would be impossible, or would force Z empty, respectively.

If 0≠f:E→E(-1), its trace and determinant vanish because H^0(O(-1))=H^0(O(-2))=0. Twisted Cayley–Hamilton gives f(-1)f=0. Its saturated kernel is a line bundle O(a), and the image is contained in O(a-1)⊂E(-1). Hence f induces a nonzero map

    I_Z(-2-a)→O(a-1).

Since Hom(I_Z,O_W)=O_W on the smooth surface, this map is a section of O(2a+1). Therefore a≥0, so a is 0 or 1.

There is at most one saturated subsheaf of E having nonnegative degree. If O(b) is another, b≥0, its composite to I_Z(-2-a) is zero, since H^0(I_Z(-2-a-b))=0. It therefore lies in O(a); saturation of both inclusions forces equality. Thus all nonzero maps E→E(-1) have this same kernel line. Conversely every section of O(2a+1) yields such a map by composing the quotient E→I_Z(-2-a), multiplication into O(a-1), and the inclusion into E(-1). These maps are automatically trace-free. Consequently, if such a line exists,

    H^0(B_W(-1))≅H^0(O_W(2a+1)),

of dimension 3 for a=0 or 10 for a=1; otherwise H^0(B_W(-1))=0. This proves (4). The isomorphism uses a choice of identification of the kernel line with O(a); the dimension statement is intrinsic. No stability or simplicity of E is assumed.

The case dim T_X=0 would force r_W=0. In the other cases r_W may still have any smaller rank consistent with the actual Gysin map. Existence of 3 or 10 detector parameters is not proof that their ambient functionals are independent.

## Dependencies and scope

- prerequisite global-conic-splitting-exclusion, document PROOF.md (see the unit INPUTS.md): exact pulled-back resolution, global generation and the H^1 bound.
- prerequisite global-conic-splitting-exclusion, document AUDIT.md (see the unit INPUTS.md): saturated-line bound, rederived above for the sharper detector dimension claim.
- prerequisite component-gluing-detector, document PROOF.md (see the unit INPUTS.md): actual component restriction, source A of dimension ten, and cofactor filtration.
