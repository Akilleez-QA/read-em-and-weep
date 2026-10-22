# 18. Actual cone lift and nonzero nilpotent trace

> **Current-status note (22 October 2026, 07:09 UTC):** The historical Gauss frontier below is superseded by [Chapter 21](21-gauss-closure-and-second-normal-residue.md): the entire (3,1) profile is excluded. Its five remaining possible profiles are not realizations, and SF ≥ 3 / square rank ≥ 27 remain unchanged. Chapter 21 also records the exact midpoint residue, associated-graded tangent acyclicity and the still-open affine R2/fourth comparison. Earlier proof bodies are preserved.

**Historical frontier.** This chapter retains its earlier source scope. [Chapter 19](19-actual-endpoint-values-and-last-gauss-quotient.md) supersedes its open-endpoint and Gauss status with actual endpoint values, the complete (6,2) exclusion and eleven remaining necessary K splittings in (8,2). The fourth obstruction remains open.

Through the 22 October 2026, 05:54 UTC cutoff, the actual cone lift is explicit and global, and both components of the normal trace shadow are nonzero. These are advances in the input and lift comparison, not evaluations of the endpoint P4 or fourth Bockstein. The separate rank-two Gauss branch now has two necessary quotient shapes and 42 quotient/type pairs. The general section count remains four or five.

The sources in this chapter are PR543 at 74feee620e0027d567df88d964e76cb9d7209c0c and 30bed21aac919087a4b40f4d1079997eb21d1390, with Mr. Slop’s complementary PR660 and PR661 pinned below. No later endpoint-cohomology identification, apolar representative or further Gauss reduction is included.

## 18.1 The actual nilpotent trace coefficient is nonzero

For the actual invariant normal class η, retain the full square shadow

    q(η)=δ(αe_v+βn₈),       α≠0, β≠0.

The new assertion β≠0 is proved by restriction of the actual global dual class to the first conic neighborhood 2C, not by choosing a vertex lift. Put E=G on the weighted stack X, with det E=O(2). The actual low-twist calculation gives

    H¹(E(−3))=0,
    H¹(E(−1))=1⊕V⊕T6,
    [W⊗H²(E(−4))]^G=0.

Tensoring the Hilbert–Burch resolution of I_C² by E(−1) therefore proves H¹(E(−1)I_C²)^G=0. Restriction of H¹(X,E(−1))^G to H¹(2C,E(−1)|_(2C))^G is injective. On C, balance and the actual first Serre jet give the first-layer sequence

    0 → End(W) O_C(−2) → E(−1)|_(2C) → W O_C → 0,

where these conic degrees are on its parametrizing P¹. The potential H⁰ connecting map is retained: its source W has no invariants. Hence the invariant H¹ of the middle term is exactly the identity in End(W) times the nonzero Euler class in H¹(O_C(−2)).

In an oriented regular Serre frame σ=(f,g), the dual trace map is r(v)=(gv₁+fv₂)/2 modulo (f²,g²), with its determinant and canonical frames. For v=σt it gives r(σt)=fgt, whose double-pair residue is the ordinary residue of t. Thus the actual global dual class θ has nonzero conic trace. Since its total trace annihilates global constants, its vertex component-constant functional A_θ is nonzero too. The kernel relation

    αA_θ+βB_θ=0,
    A_θ=Tr_vertex(r(θ)),    B_θ=Tr_vertex(n₈r(θ))

and α≠0 force β≠0 and B_θ≠0. The ratio β/α=−A_θ/B_θ is not evaluated numerically. [Actual restriction and residue proof][TRACE].

## 18.2 Why the section line cannot be discarded in duality

The [duality comparison][DUAL] isolates the error in identifying the Serre quotient with the full adjoint dual residue. A section-line class σt is invisible under the Serre projection but its square residue pairs nontrivially with the vertex component constant. This is a genuine degree-fourteen residue channel; retaining only the degree-six socle and its degree-eight nilpotent pairing misses it.

On U=X\C, the local-to-global extension sequence has kernel H¹(U,O_U(−2)), whose cover-degree-zero part is H¹(O_L(−2))=C. Fixing the vertex residue alone therefore does not fix the marked Serre extension on U. This does not assert that an arbitrary independent section-line change extends to X. Global conic/vertex matching fixes the actual class. Section 18.1 performs the additional global comparison needed for β≠0; the local mismatch alone does not prove it.

## 18.3 Global wedge cancellation fixes the actual correction constant

For the uniform C5 input a=z², h=X²Y², retain the absolute midpoint numerator r_mid, the absolute Atiyah numerator r_t=2ka∂z(afg), the physical equation factor ν and θ=νγ. Put r=a(r_mid−θr_t). The restriction H⁰(O(8,2))→H⁰(O_D(8,2)) is an isomorphism because its kernel line O(5,−1) has zero H⁰ and H¹. It supplies a unique global wedge polynomial w with w|_D=−r|_D.

The [explicit wedge calculation][WEDGE] constructs w=fv₂−gv₁ and checks both complete regular quintic charts under g↦g+pf. The double-cubic scalar matching, with a general scalar quartic χ, is

    r−w−2gv₁−χfg=0 modulo f².

Its unique solution in the shared normalization is

    θ=−1/12,   γ=−1/(12ν),   χ=Ak/(3Bc²).

Here A,B,c,k are the unassigned symbolic source parameters; A in this displayed scalar formula is not a representation label. This is the actual canonical γ: the constructed global boundary vanishes, negative multiplication kills the complementary Cplus contribution, and β₂(a):A→P4 is injective at this square, so the canonical correction is unique. A simultaneous change of boundary conventions must be transported throughout.

With V₀=(v₁,v₂)+(χ/2)σ, the source equals τ(V₀)/(νg²) in H⁰(M₈). The factor one-half is required by τ(σ)=2N. At this stage V₀ is a genuine degree-eight coefficient-bundle section and the kernel class has global G(4) lifts; that alone does not identify this displayed pair with a full actual lift. Sections 18.5–18.6 supply the missing comparison. Neither cancellation evaluates the fourth value.

## 18.4 The universal second-normal formula retains the first error and old connection

For binary degrees 2m,2n, the harmonic product is

    L(p)L(r)=L(pr)+qL(B₁(p,r))+q²L(B₂(p,r)) modulo q³,
    B₁(p,r)=τ₂(p,r)/[2(2m−1)(2n−1)(2m+2n−1)],
    B₂(p,r)=τ₄(p,r)/[8(2m−1)(2m−3)(2n−1)(2n−3)
                         (2m+2n−3)(2m+2n−5)].

The channels are zero when min(m,n)<1 or <2, respectively. This B₂ denotes harmonic multiplication, not the fourth Bockstein. For local formal data Ñ=L(n)+qL(t)+q²L(s), operator L(H)D+ad_(L(A)+qL(K)+q²L(J)), scalar Λ̃=L(λ)+qL(λ₁)+q²L(λ₂), and Dq=ρq, the full second error is

    R₂=HDs+(2Hρ−λ)s+[A,s]+[K,t]+[J,n]−λ₁t−λ₂n
        +B₁(H,Dt)+ρB₁(H,t)+[A,t]₁+[K,n]₁
        −B₁(λ,t)−B₁(λ₁,n)
        +B₂(H,Dn)+[A,n]₂−B₂(λ,n).

The brackets with subscript j use the jth harmonic product in matrix order. If the local square-zero equations hold and R₀=0, tangency at second order still requires

    {n,R₂}+{t,R₁}+B₁(n,R₁)+B₁(R₁,n)=0.

One cannot delete the first error merely because its cohomology class vanishes. Under a normal gauge 1+qL(B)+…, R₂ changes by [B,R₁]. After justified tangency, the new J-term disappears in the diagonal modulo (f²,g²), but the old K-terms remain:

    K₁₂t₂₁−K₂₁t₁₂+B₁(K₁₂,g²)+B₁(K₂₁,f²).

The λ₂fg scalar-line term also needs global comparison. Equation units must be retained: for q₀=νq, B_j and jth-normal inputs scale by ν^(−j), while ρ becomes ρ+Dν/ν.

These are [universal local identities][SECOND], expressly not a global midpoint extension to 3Q. The midpoint’s nonzero obstruction −c²/(4d) still prevents that extension. In particular s is not supplied as a globally available actual midpoint section, and a cone lift does not supply it.

## 18.5 The actual conic residue forces a nonzero Euler cocycle

The conic Koszul sequence O→W O(1)→I_C(2), pulled back to I_Z(2), defines the unique global pure-conic extension ξ_C. On U=X\C, its two quotient splittings differ by σ/(uv). The resulting [Euler cocycle][CONIC]

    [1/(uv)] ∈ H¹(U,O_U(−2))

is nonzero already on L=P(W), where the Euler extension cannot split. Global H¹ and H² of O_X(−2) vanish, so the actual marked extension with nonzero conic and vertex residues is

    ξ_actual=ρ_C ξ_C+ρ_v ξ_v,
    ξ_actual|_U=ρ_v ξ_v|_U+i(ρ_C[1/(uv)]),    ρ_C≠0.

The vertex residue has block weight μ²; the degree-2j kernel piece has weight μ^(−2−j). Thus there is a unique vertex eigenextension and the conic term cannot mix with higher-cover terms. This is an Ext-space weight argument, not an assumed torus action on the actual middle bundle.

In oriented frames the exact section-preserving transition correction is I+tN_C, where N_C=σσᵗJ_C, J_C=[[0,1],[−1,0]], N_C²=0 and t_x=ρ_C/z in the physical O(−2) frame. Its determinant is one and inverse is I−tN_C. This O(−2) extension cocycle is not identified without calculation with the distinct O(−1) dual-trace cocycle.

## 18.6 Completing the actual global G(4) lift

The [actual lift theorem][LIFT] first proves that the homogeneous triangular bundle is the marked vertex eigenextension. Its determinant-compatible full transition chain has weight μ², while the kernel has no μ² piece. Agreement of residues alone would not suffice. The marked identification is unique because H⁰(U,O_U(−2))=0.

Write the wedge of V₀ from Section 18.3 as Ω=Ω₀+Ω₁z+Ω₂z². In the conic orientation above the required scalar corrections are

    r_x=−ρ_C(Ω₁+Ω₂z),
    r_y=ρ_CΩ₀/z=−ρ_CΩ₀w,       w=−1/z,
    V_actual,i=V₀,i+σ_i r_i.

Both r_i have positive-cover degree eight and coefficient line O_L(0). Their equation r_y−r_x=t_xΩ has this sign because J₀=−J_C, so N_C=−n and the transition is I−tn. Since nV₀=−Ωσ and nσ=0, the correction solves the transition exactly, without discarded higher powers. It adds cover degrees eleven and thirteen to the two section entries.

The complete root-frame check puts z=Z², (X_y,Y_y)=(X/Z,Y/Z) and uses

    D_root=diag(Z^(−9),Z⁵),       det D_root=Z^(−4),
    P₀=P_y D_root P_x^(−1),      T₀^(4)=Z^(−8)P₀,
    V_actual,y=T₀^(4)(I+t_xN_C,x)V_actual,x.

Here P_x,P_y are both actual triangular regularizers. This verifies the physical determinant, twist O(4), root coordinates and all higher correction terms, not just leading degree or wedge equality. The sections are regular on both full charts. Only after that actual gluing is established does reflexive Hartogs on the smooth stack extend the section uniquely across codimension-two C. Thus it is genuinely in H⁰(X,G(4)), with wedge Ω.

The Laurent split fixes a normalization, not absolute scalar uniqueness: within degree eight, another split differs by Sym⁸W′, a nine-dimensional space of global scalar additions. This result completes the actual cone lift comparison. It does not prove that the old homogeneous K is the full actual first-normal connection; normal-order transport of the cone-frame correction remains necessary.

## 18.7 The lowest diagonal of the actual normal class is nonzero

In trace degree eight an adjoint of physical twist −2 has form [[d,0],[r,−d]]. Its actual coefficient bundle satisfies

    0 → V O_L(−10) → J_η → O_L(−2) → 0,
    J_η=P4 O_L(−8),
    q([[d,0],[r,−d]])=2fgd−f²r.

The nonsplit generator change is r↦r+2pd. Exact characters give H¹(V O(−10))^G=0 and H¹(J_η)^G=C; the diagonal map to H¹(O_L(−2)) is an isomorphism by the exact sequence, not just by equal dimensions.

The conic correction raises trace degree by eight. The only possible lower degree, six, has no invariant H¹. Hence truncation extracts a canonical actual degree-eight component. The constant e_v has zero boundary on U; the trace of this component is βδ(n₈). The actual square-ideal boundary δ(n₈) is nonzero, and Section 18.1 proves β≠0. Thus the [lowest diagonal][DIAGONAL] is a nonzero multiple of [1/(uv)], or [1/z] in the coefficient chart. This is an associated homogeneous cohomology statement, not a full homogeneous representative or an endpoint evaluation.

## 18.8 A regular commutator correction contributes in degree twelve

Each actual scalar correction r_i belongs locally to the regular ideal (f,g): it has positive degree eight, above the quotient’s socle degree six. Choose regular p,q with r=fp+gq and degrees (5,3). Then

    B=σ(p,q)−(r/2)I
     =[[(fp−gq)/2,fq],[gp,(gq−fp)/2]],
    [B,n]=rn.

Thus subtracting τ(σr)=2rn changes E_hom=[K_hom,n] to [K_hom−2B,n], with no division by f or g. Another choice changes (p,q) by ℓ(g,−f), hence B by ℓn; the remaining ambiguity centralizes n.

The [degree conclusion][COMMUTATOR] is precise: B has diagonal degree eight and off-diagonal degrees six and ten; t has off-diagonal degrees two and six. In the four old-K diagonal terms of Section 18.4, substituting −2B gives degrees 6+6, 10+2, 6+10−4 and 10+6−4, all twelve, not four. The syzygy ambiguity has the same degree. This removes this particular scalar-lift contribution from the degree-four part. It neither identifies the complete actual K nor proves that degree four alone determines the global endpoint or fourth obstruction.

## 18.9 Two complementary detection results

Mr. Slop’s [PR660][JET] concerns the four-dimensional fourth-family space Q₄ and its secant restriction R₄, of dimension three. Its one-dimensional factoring kernel T is detected exactly by the intrinsic ρ₁-valued cubic-symbol channel E₁ of the axis ideal-sheaf jet:

    (restriction, π₁jet): Q₄ → R₄⊕E₁ is an isomorphism.

The two ρ₂-valued jet channels vanish on T and factor canonically through R₄. A secant value and a full three-channel jet are compatible precisely when these two components agree under that factor map. The proof uses the degree-nine quadruple-axis exclusion and the local right inverse of the canonical map. This is not ordinary derivative evaluation, and no square datum is needed. It does not evaluate the actual fourth family or the specialized extra axis kernel.

Mr. Slop’s [PR661][ENDPOINT] instead concerns the two-dimensional quadratic endpoint family. At one C5 square a=u², its restriction to K_a=span(u⁴,u³z) is an isomorphism onto the two-dimensional stabilizer-allowed secant fiber. The canonical flag Cu⁴⊂K_a detects the symmetric channel first, then, conditional on its vanishing, the alternating channel. The full allowed square fiber has dimension four; compatibility requires its V and P4 central-isotypic projections to vanish, leaving exactly its two D5 channels. Pure-power orbit spanning proves triangular independence without selected actual-source data. Restriction is injective at every square, but the stated target dimensions and surjectivity concern C5 squares. Neither endpoint channel has been evaluated here.

## 18.10 Two Gauss quotient shapes and the unchanged frontier

The [middle-quotient theorem][MIDDLE] excludes the entire (n,e)=(6,4) case A₀=O(4)⊕W′O(−3). Exact section envelopes isolate the unique low-target isomorphism. After legitimate graph removal and equivariant evaluation lifts, the next derivative has no map to its W′O(−7) target; its rank is at most one rather than three. All ten retained pairs disappear.

The [last-low-quotient theorem][LOW] excludes the entire (8,4) case A₀=O(6)⊕W′O(−3). The exact tail and coefficient conditions leave thirteen genuine splittings, seven with a possible low-target map. Universal sextic/septic kernels and the possibly nonsplit Euler extension compute all actual next kernels. Each has zero component into W′O(−7), again contradicting rank three. All twenty-one retained pairs disappear.

The historical necessary-pair sequence is therefore

    140 → 77 → 73 → 63 → 42.

The stages are the original five-shape overlist, section envelopes, then complete exclusions of (4,2), (6,4) and (8,4). Only (6,2) and (8,2) remain in this rank-two dual-image branch, with twenty-one necessary pairs each. These are not realized geometries, probabilities or an overall search-completion percentage. The rank-one branch and whole (3,1) profile remain unresolved. Generic SF≥3 and positive-square rank≥27 are unchanged.

The actual endpoint P4 and all four fourth coefficients remain unevaluated. Generic sections remain four or five, and the last generic finite Smith exponent remains 4–31, or the cokernel is permanent. Neither the full normal-K comparison nor a global midpoint extension to 3Q follows from the actual cone lift. Original source recovery, lifting and Weil-class algebraicity remain open.

## Pinned source references

[TRACE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/74feee620e0027d567df88d964e76cb9d7209c0c/research/hm/order-four-quadratic-load/ACTUAL-NORMAL-TRACE-HAS-NONZERO-NILPOTENT-COMPONENT.md
[DUAL]: https://github.com/Akilleez-QA/read-em-and-weep/blob/74feee620e0027d567df88d964e76cb9d7209c0c/research/hm/order-four-quadratic-load/NORMAL-TRACE-DUALITY-HAS-A-SECTION-LINE-RESIDUE.md
[WEDGE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/74feee620e0027d567df88d964e76cb9d7209c0c/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-FOURTH-SOURCE-HAS-A-GLOBAL-WEDGE-CANCELLATION.md
[SECOND]: https://github.com/Akilleez-QA/read-em-and-weep/blob/74feee620e0027d567df88d964e76cb9d7209c0c/research/hm/order-four-quadratic-load/UNIVERSAL-SECOND-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-DEFECT.md
[CONIC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/30bed21aac919087a4b40f4d1079997eb21d1390/research/hm/order-four-quadratic-load/ACTUAL-CONIC-RESIDUE-FORCES-VERTEX-SERRE-COCYCLE.md
[LIFT]: https://github.com/Akilleez-QA/read-em-and-weep/blob/30bed21aac919087a4b40f4d1079997eb21d1390/research/hm/order-four-quadratic-load/ACTUAL-GLOBAL-SERRE-LIFT-FROM-THE-CONIC-COCYCLE.md
[DIAGONAL]: https://github.com/Akilleez-QA/read-em-and-weep/blob/30bed21aac919087a4b40f4d1079997eb21d1390/research/hm/order-four-quadratic-load/ACTUAL-NORMAL-CLASS-HAS-A-NONZERO-LOWEST-VERTEX-DIAGONAL.md
[COMMUTATOR]: https://github.com/Akilleez-QA/read-em-and-weep/blob/30bed21aac919087a4b40f4d1079997eb21d1390/research/hm/order-four-quadratic-load/CONIC-SCALAR-LIFT-CORRECTION-HAS-A-REGULAR-COMMUTATOR-PREIMAGE.md
[MIDDLE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/74feee620e0027d567df88d964e76cb9d7209c0c/research/hm/order-four-quadratic-load/EXTREMAL-31-MIDDLE-QUOTIENT-EXCLUSION.md
[LOW]: https://github.com/Akilleez-QA/read-em-and-weep/blob/30bed21aac919087a4b40f4d1079997eb21d1390/research/hm/order-four-quadratic-load/EXTREMAL-31-LAST-LOW-QUOTIENT-EXCLUSION.md
[JET]: https://github.com/Akilleez-QA/read-em-and-weep/blob/fe195ead045076fc27bfa95686fe13d738df694f/research/hm/secant-jet-comparison/SECANT-RESTRICTION-AND-THE-INTRINSIC-CUBIC-JET.md
[ENDPOINT]: https://github.com/Akilleez-QA/read-em-and-weep/blob/1325647fd916bf2daa71b11efeae6d52cfefa2cd/research/hm/endpoint-square-reconstruction/PROOF.md
