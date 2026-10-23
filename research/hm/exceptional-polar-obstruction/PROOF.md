# A nonzero two-dimensional exceptional-polar obstruction and the vertex scalar

Work over C. This is structural mathematics, not formal proof-assistant verification. No selected actual HM/source coefficient, point, parameter, derivative, matrix or instance rank is evaluated.

## 1. Exact inputs and statement

Repository Akilleez-QA/read-em-and-weep; INPUTS.json records exact original bytes and immutable locations.

- PR934, commit8c9847612b5f575b987cec9c62b72b099d745e44, research/hm/reduced-opposite-pencil/PROOF.md: X=Bl_R(P4), p:X→P4, π:X→T=P(W*), exceptional divisor E, vertex section Z≅L disjoint from E, π*O(1)=p*O(1)(-E); B=End0 F; π_*p*B(3)=A O(-6), π_*(I_Zp*B(3))=W O(-7), and 0→O(10)→D_vert→C→0.
- PR948, commitd1d5ca5915b734d018665c2b02a4426c8225d799, research/hm/opposite-bundle-classification/PROOF.md: C is a bundle with complete-evaluation characters E26=2W+W'+2S+2T6 and H31=1+3A+V+2P+2D; k=dim H0(C(-12))^G≤1; the vertex extension class is its connecting functional δ:H0(C(-12))^G→H1(O(-2))^G=C.
- HYPERPLANE-SQUARE-SURVIVORS.md, research/hm/order-four-quadratic-load/, commitdb51525015bb7c5e825833d550d08dedf6f6ea96: stable equivariant plane Steiner sequence 0→A O_R(-3)→D O_R(-2)→F_R→0; inversion is scalar positive on F_R.
- SHARPEST-BOUND.md, research/conductor-normalization/sharper-hm-regularity/, commit063da90fc4543304e87e701cdefcc08225412f17: primary section resolution and cohomology of F, and H2B(t)=0 for t≥2.
- POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md, research/hm/order-four-quadratic-load/, commiteeb1a11799ca38a60c37f6ba96f263ef8e20dd1c: H0B(4)=0; H1(B(4))_+=2V+4P+3D. Only these ambient cohomology statements are used, not any source-specific or cone-smoothing inference.

G=SL2(F5); V=Sym2 W', A=Sym2 W, D=Sym4 W, P is the even four-space. The center has positive action on B_R, and all named irreducibles are self-dual. Current PR1 was read through comment6362450612; source2/source126 compatibility and the four-pair ledger are separate.

We construct actual coherent sheaves K_j, supported on a finite thickening of R, and prove:

(a) H1(K10)^G is canonically a two-dimensional vector space, while H0(K10)^G=H2(K10)^G=0.

(b) There is an actual, canonical, NONZERO connecting map between two-dimensional spaces

    σ: (Sym10 W ⊗ Sym2 D)^G → H1(K10)^G.         (1)

Its kernel is canonically H0(C(-12))^G. Thus rank σ is one or two. Rank two excludes all five extension-capable types of PR948. Rank one leaves exactly a one-dimensional candidate space, on which the further actual vertex functional δ decides the extension.

(c) The lower exceptional filtration contains actual connecting maps

    α:C→C,     β:C²→coker α,

with rank α+rank β=1. They cannot both be zero. There is an exact sequence

    0→ker α→H1(K10)^G→ker β→0.                  (2)

No splitting of this sequence is asserted. This proves additional actual nonvanishing of an internal geometric transgression, without choosing which one.

(d) The remaining vertex functional is exactly the p-Leray differential from H0(K12)^G to H2(I_LB(-9))^G=C. Equivalently, its dual is the codimension-three vertex Gysin map into H3(P4,I_R^11 B(4))^G.

This is a geometric reduction to an actual nonzero two-space obstruction followed by a scalar. It neither selects the actual rank nor computes δ.

## 2. Plane cohomology, derived without a split-neighborhood assumption

Taking the symmetric square of the Steiner resolution and using B_R=Sym2 F_R(1) gives an exact length-two resolution

    0→A O_R(-5)→(A⊗D) O_R(-4)→Sym2 D O_R(-3)→B_R→0.  (3)

Here Λ²A≅A. Stability gives H0(B_R(t))=0 for t≤0. We also need H0(B_R(1))=0, which is not a consequence of stability alone.

At twist1, (3) identifies this section space with the kernel of the actual map Λ²A⊗V→A⊗D induced by the Steiner coefficient β0:A⊗V→D. A tensor in Λ²A⊗V is a three-by-three matrix after choosing a volume form on A. Every nonzero kernel tensor must have matrix rank three: a rank-one tensor can be written (a1∧a2)⊗v1, and vanishing of its image forces β0(a1,v1)=β0(a2,v1)=0; a rank-two tensor can be written (a2∧a3)⊗v1+(a3∧a1)⊗v2 with v1,v2 independent, and vanishing forces β0(a3,v1)=β0(a3,v2)=0. Both contradict the fiberwise injectivity of the Steiner A→D map at a nonzero v. These normal forms are universal linear algebra, not assignments to actual coefficients.

A linear space of square matrices whose every nonzero member is invertible has dimension at most one over C: any pencil through an invertible member and an independent member has a singular nonzero member by its determinant polynomial. But Λ²A⊗V=A⊗V=P+D has no one-dimensional subrepresentation. Its invariant kernel must therefore be zero. This proves H0(B_R(1))=0.

The remaining computations follow directly from (3), ordinary cohomology of O_P2(t), and Serre duality B_R*=B_R, ω_R=O_R(-3). They give:

    H0(B_R(2))=A,          H1(B_R(2))=0,
    H0(B_R(3))=Sym2 D=1+P+2D, H1(B_R(3))=0,
    H0(B_R(4))=(Sym2 D⊗V)-(A⊗D), H1(B_R(4))=0;
    H1(B_R(1))=A+V,
    H1(B_R(0))=V+P+D,
    H1(B_R(-1))=A+V+P+D.

The minus sign in H0(B_R(4)) is a representation-ring identity for an actual cokernel, not a chosen complementary subspace. The preceding three H1 identities use H0=H2=0, so their Euler characters determine the actual characters. Duality supplies twists -3,-5,-7 used below.

## 3. The actual exceptional-polar filtration

For j≥0 define

    K_j=R1 p_*[p*B(-9)⊗O_X(jE)].

The fibers of p have dimension at most one. For every j≥0, p_*O_X(jE)=O_P4; K0=K1=0. The normal bundle is N_(R/P4)=W*⊗O_R(1), with det W=1. The exceptional divisor is P(N), and O_E(E) is its relative O(-1). The exact divisor sequences and relative P1 cohomology give actual short exact sequences of sheaves on P4

    0→K_(j-1)→K_j→i_*G_j→0,  j≥2,
    G_j=Sym^(j-2)W⊗B_R(j-9).                    (4)

This formula retains the O_R(j) from Sym^(j-2)N⊗det N. Omitting it would change every twist. K_j need not be an O_R-module or split into its graded pieces; it is supported on a thickening. We use (4), not a direct-sum replacement.

The center acts on G_j by (-1)^j, so odd layers have no invariant cohomology. Exactness of finite-group invariants allows us to pass through odd steps without changing invariant cohomology. Section2 and the fixed irreducible characters give the following complete invariant-cohomology table for the even layers; all unlisted groups are zero:

    j=2: none;
    j=4: H2(G4)^G=C;
    j=6: H1(G6)^G=C;
    j=8: H1(G8)^G=C²;
    j=10: none;
    j=12: H0(G12)^G=C².                         (5)

For example, H2G4 invariants are (Sym2W⊗H0B_R2*)^G=(A⊗A)^G; H1G6 invariants are (D⊗(V+P+D))^G; H1G8 uses Sym6W=V+P; G10 has H1 character Sym8W⊗(A+V), with Sym8W=P+D, giving no invariant. G12 uses Sym10W=A+V+D and Sym2D=1+P+2D, giving two. For G2 the only possible group is H2 with character H0B_R4*, whose trivial multiplicity is zero. verify.py checks these exact fixed-character calculations.

It follows first that H0(K10)^G=0 and χ_G(K10)=1−1−2=−2.

## 4. Global geometry kills the remaining H2 and forces internal transgression

Put

    M=p*B(3)⊗π*O_T(-12)=p*B(-9)⊗O_X(12E).       (6)

Its only nonzero p-direct images are p_*M=B(-9) and R1p_*M=K12.

For completeness, H3B(t)=0 for t=2,3,4 follows from the primary tensor section resolution: its H3 diagonal consists of H3(15F(t-3)+4F(t-2)) and H4(35F(t-4)); these dualize to H1F(-t-1), H1F(-t-2), and H0F(-t), all zero. Likewise H4B(2)=H4B(3)=0. Together with H2B(2)=H2B(3)=0, the universal incidence sequence proves R2π_*p*B(3)=R3π_*p*B(3)=0. Consequently H3(X,M)=0, since the base T has dimension one.

The p-Leray spectral sequence has only rows q=0,1. Its exact sequence at degree three gives

    H3(X,M)→H2(K12)→H4(B(-9)).

The left term is zero, and the right term is H0(B(4))*=0 by the pinned ambient theorem. Hence H2(K12)=0. The top layer G12 has invariant H1 and H2 zero, so (4) gives H2(K10)^G=0. Its invariant Euler characteristic now gives

    dim H1(K10)^G=2.                             (7)

This argument is global and does not infer vanishing from disjointness of R and L.

In the following notation the canonical invariant-cohomology isomorphisms across the odd steps identify K5 with K4, K7 with K6, and K9 with K8; no isomorphism of those sheaves is asserted. The lower exact sequences give a canonical map α:H1(G6)^G→H2(K4)^G, both one-dimensional, and identify H1(K6)^G=ker α, H2(K6)^G=coker α. The next boundary is β:H1(G8)^G=C²→H2(K6)^G. Passing through the acyclic invariant G10 layer proves (2) and H2(K10)^G=coker β=0. Thus β is onto and

    rank α+rank β=1.                             (8)

Either α is an isomorphism, or α=0 and β is a nonzero surjection. Both cannot vanish. These are statements about actual filtered connecting maps.

## 5. The actual nonzero two-space boundary identifies the candidate space

Taking the top boundary in (4) yields σ in (1), with

    ker σ=H0(K12)^G,
    coker σ=H1(K12)^G.                           (9)

No splitting of K12 is chosen. On P4, Serre duality and Section4 give H1B(-9)=H3B(4)*=0 and H2B(-9)=H2B(4)*=0. Therefore p-Leray identifies H1(X,M) canonically with H0(K12).

On T, the actual π_*M is A O(-18), and the positive part of R1π_*M is C(-12). The invariant H1 of A O(-18) is Hom_G(A,Sym16W)=0 because Sym16W=V+P+2D. Thus π-Leray gives a canonical identification

    H0(K12)^G ≅ H1(X,M)^G ≅ H0(C(-12))^G.       (10)

By PR948 its dimension k is zero or one. Both source and target of σ have dimension two, so σ is nonzero and rank σ=2−k. This is an actual geometric nonvanishing theorem; it does not choose a matrix, scalar, or instance rank.

Sequence (2) also gives a two-stage description retaining all extension information. Project σ to ker β⊂C² and call this σ4. On ker σ4, its image lies canonically in ker α⊂H1(K10)^G; call that restricted map σ6. Then ker σ consists exactly of the vectors killed by both successive obstructions. This does not assert maps to chosen complements or a split sum.

## 6. The vertex adds precisely the actual extension scalar

Let M_Z=I_Z M. Since Z is disjoint from E, p_*M_Z=I_LB(-9) and R1p_*M_Z=K12. The latter identification is natural, not merely an equality of associated gradeds. The fixed-line splitting is

    B|L(-9)=O_L(-2)_+⊕O_L(-9)_-⊕O_L(-16)_+.

It has no global sections. The ambient vanishings above and the ideal restriction sequence give H1(I_LB(-9))=0 and H2(I_LB(-9))≅H1(B|L(-9)). Its invariant part is C: H1O(-2) contributes one and Sym14W has no invariant.

Thus the p-Leray five-term sequence identifies H1(X,M_Z)^G with the kernel of the actual differential

    d2:H0(K12)^G→H2(I_LB(-9))^G=C.             (11)

On π, the section bundle is W O(-19), whose H1 invariants are Hom_G(W,Sym17W)=0. Therefore H1(X,M_Z)^G≅H0(D_vert(-12))^G.

Naturality identifies (11) with PR948's δ, using (10). More explicitly, compare 0→M_Z→M→M|Z→0 with 0→I_LB(-9)→B(-9)→B|L(-9)→0 under p. The ambient H1,H2 vanishings identify the p-Leray transgression with the restriction H1(X,M)→H1(B|L(-9)); under π the same restriction descends to the boundary of 0→O(-2)→D_vert(-12)→C(-12)→0. The other positive vertex summand O(-16) has no invariant H1. Consistent boundary conventions give the same map; an overall sign is immaterial.

Hence the complete geometric test is: first take the kernel of the actual nonzero two-space σ; if it is zero the vertex extension splits automatically; if it is a line, test its map d2 to C. Nonzero d2 gives the nonsplit case; zero d2 gives the split case. No claim that d2 vanishes because R and L are disjoint is made.

## 7. Equivalent Gysin form and boundary

There is an equivalent coordinate-free interpretation. Since ω_X=p*O(-4)⊗π*O(-1), Serre duality identifies H1(X,M_Z)* with Ext3_X(I_Z,N), where N=p*B(4)⊗O(-11E). As R^q p_*O(-11E)=0 for q>0, H3(X,N)=H3(P4,I_R^11B(4)). The regular codimension-three immersion Z has N_(Z/X)=V⊗O_L(1), so N|Z⊗det N_(Z/X)=B|L(7). Its H1 vanishes; its invariant H0 is exactly C from the O_L(0) summand, since Sym14W has no invariant. Local duality and the ideal sequence therefore give

    C --g--> H3(P4,I_R^11B(4))^G
      →H0(D_vert(-12))^{G,*}→0,
    H3(P4,I_R^11B(4))^G ≅ (ker σ)*.             (12)

The map g is the actual codimension-three Gysin class and is dual to d2. This is not a presumed self-duality of D_vert; ordinary relative duality changes B(3) to a different twist.

The new result is a forced nonzero two-dimensional exceptional-polar obstruction and a forced nonzero lower transgression, with exact filtered and Gysin descriptions of the still-missing scalar. It does not choose rank σ, prove g nonzero, determine an actual PR948 row, evaluate a selected instance, remove a source pair, or assert physical normal order12. All -12 twists here are on the parameter line.
