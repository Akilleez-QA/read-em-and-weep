# Simultaneous residue interpolation without restriction injectivity

## Result and distinct contribution

This lemma removes injectivity of polynomial restriction from the simultaneous-residue construction, and corrects both its polynomial target and common-contained-line kernel when restrictions have nonzero kernels. PR458 §§1–4 and PR463 §§2–3 give the special cases with injective restrictions; they do not contain these ambiguity quotients or kernel corrections. The underlying weighted-residue mechanism is theirs. This is a dependency reduction and extension, not a new original-pair vanishing result.

Everything below is symbolic. No selected HM/source coefficients, multiplication matrices, or rank experiments are used.

## 1. A residue model with the rightmost term retained

Let E=F(3) be the positive HM bundle, B=End₀(F), V=H⁰E, D=det V, and let C be the disjoint union of the transverse evaluation-degeneracy lines. The evaluation cokernel is i_*L with L of degree −1 on each line. Retain the exact complementary-minor resolution and its induced duality

0→D O(−5)→Λ²V O→V⊗E→Sym²E→i_*L²→0,
ω_C⊗L⁻²≅D*O_C.

For 1≤d≤6 the normalized monad gives H²F(d−2)=H³F(d−2)=0. Also H⁰L²(d−5)=0 and H⁴O(d−5)=0. Splitting the resolution into three short exact sequences yields

0→V⊗H¹F(d−2)→H¹B(d)→H¹L²(d−5)
  →D⊗H⁴O(d−10)→H²B(d)→0.                     (1)

The first map is the actual primary cup product and is injective. Write P_d for its image and N_d=H¹B(d)/P_d. Duality of the resolution identifies the transpose of the middle boundary with ordinary restriction, retaining the same D* for every d. Therefore

N_d*≅D*⊗coker[S_{5−d}→H⁰O_C(5−d)],
H²B(d)*≅D*⊗ker[S_{5−d}→H⁰O_C(5−d)].          (2)

No H²B(d) vanishing was used. Naturality under polynomial multiplication gives multiplication on these restriction cokernels in the reverse direction.

The primary vanishing assertion used here does not require a table: for s≥0, Ω²(s+2) has only degree-zero cohomology or is acyclic, and Ω²(1) is acyclic at s=−1. Apply the two normalized-monad short exact sequences and line-bundle cohomology. Thus (1) follows directly from the monad and evaluation geometry.

## 2. Simultaneous kernel with no uniqueness of representatives

Put S=C[x₀,...,x₄], I=⊕_{j≥0}H⁰I_C(j), H_j=H⁰O_C(j), and res_j:S_j→H_j. Fix nonzero forms u∈S_a and v∈S_b and an integer r≥0. Define

W_r(u,v)=ker[H_r/res_r S_r → (H_{r+a}/res_{r+a}S_{r+a})⊕(H_{r+b}/res_{r+b}S_{r+b})],
[λ]↦([uλ],[vλ]).                                  (3)

This is well-defined because multiplication by a global form takes restrictions of global forms to restrictions of global forms. Equivalently, λ admits f∈S_{r+a}, g∈S_{r+b} with res f=u|C·λ and res g=v|C·λ. Such f,g need not be unique: their full ambiguity is I_{r+a}⊕I_{r+b}.

When r+max(a,b)≤4, (2) applies to the target degree n=5−r and both source degrees n−a,n−b. Consequently

[H¹B(n)/(P_n+uH¹B(n−a)+vH¹B(n−b))]*≅D*⊗W_r(u,v).       (4)

The full fixed-pair quotient still has an exact primary subquotient P_n/(P_n∩U), where U=uH¹B(n−a)+vH¹B(n−b). Formula (4) does not remove it.

The cases (a,b,r)=(2,3,0) and (2,3,1) recover the degree-five and degree-four residual models. The case (4,3,0), replacing u by a squared quadratic, gives the corresponding squared-quadratic degree-five residual model without a quartic-restriction injectivity premise.

## 3. Correct polynomial target

Let J=(u,v). For representatives as above, h=vf−ug lies in (I∩J)_{r+a+b}. Altering f by α∈I_{r+a} and g by β∈I_{r+b} changes h by vα−uβ. Thus the exact ambiguity space is

A_r=vI_{r+a}+uI_{r+b}=(IJ)_{r+a+b}.                (5)

Altering λ by res p, p∈S_r, permits changing (f,g) by (up,vp), which leaves h unchanged. Hence the canonical map is

Φ_r:W_r(u,v)→((I∩J)/IJ)_{r+a+b},
[λ]↦[vf−ug].                                    (6)

One generally cannot replace the quotient target by (I∩J)_{r+a+b}. Already λ=0 permits f=α∈I_{r+a}, g=0, producing the representative vα; the same input also permits f=g=0. This is a formal ambiguity demonstration, not a selected-instance computation.

## 4. Exact common-contained-line kernel

Now assume gcd(u,v)=1. Let C₀ consist of the k component lines on which both restrictions vanish identically, and let K_r⊂H_r be the sections supported on C₀. Then

ker Φ_r = K_r/(K_r∩res_r S_r).                    (7)

Proof: if Φ_r([λ])=0, write vf−ug=vα−uβ with α∈I_{r+a}, β∈I_{r+b}. Replace f,g by f−α,g−β. Then vf=ug identically. Coprimality in S implies f=up and g=vp for a common p∈S_r. On every component outside C₀ at least one of u,v is nonzero, and the component's section ring is a domain; hence λ−res p vanishes there. Thus its class has a representative in K_r. Conversely a section in K_r has uλ=vλ=0 on all C, so f=g=0 is permitted and Φ_r vanishes. Quotienting by the precisely stated intersection proves (7).

Moreover

K_r∩res_r S_r = res_r((I:J)_r),
dim ker Φ_r = k(r+1)−dim(I:J)_r+dim I_r.            (8)

Indeed res p is supported on C₀ iff its products by both u and v vanish on C, equivalently p∈I:J. The restriction kernel on that colon subspace is I_r. Each common line contributes r+1 sections. This also handles the edge case where every line is common contained: diagonal/global restrictions then genuinely subtract from the supported space.

Thus there is an exact sequence

0→K_r/(K_r∩res S_r)→W_r(u,v)→im Φ_r→0.            (9)

## 5. Avoidance gives the full corrected target

If C∩V(u,v)=∅, the restrictions u_l,v_l on each component are coprime binary forms. For any h∈(I∩J)_{r+a+b}, choose h=vf−ug with the required degrees. Restricting gives v_l f_l=u_l g_l. Coprimality implies f_l=u_l λ_l and g_l=v_l λ_l for a degree-r section λ_l. These assemble on disjoint C and give an element of W_r mapping to [h]. Hence Φ_r is surjective. There are no common-contained lines, so (7) gives injectivity. Therefore

W_r(u,v)≅((I∩J)/IJ)_{r+a+b}.                     (10)

No injectivity of any res_j is needed. This also explains representation-independence in the converse: the quotient (IJ) absorbs choices coming from ideal sections, while global coprimality absorbs choices by the ordinary Koszul syzygy (up,vp).

## 6. Specialization, removed dependencies, and limits

If I_{r+a}=I_{r+b}=0, the denominator in (6) vanishes. Moreover (I:J)_r=0 because u is nonzero and up∈I_{r+a}=0 forces p=0; also I_r=0. Then the kernel is precisely K_r of dimension k(r+1). These are PR458's k-dimensional and PR463's 2k-dimensional statements for r=0,1. Under avoidance their unquotiented intersection descriptions are recovered.

Removed for (3)–(10): all injectivity assumptions for polynomial restriction; the B-twist vanishing claims previously used to establish those assumptions; all numerical residue dimensions; unique polynomial representative assumptions; quintic/sextic dimension or saturation computations; normalizer representation arguments. The algebraic lemma (3), (5)–(10) itself needs only disjoint projective lines, and gcd(u,v)=1 for its kernel/avoidance portions.

Still required for the actual cohomological identification (4): transverse evaluation geometry, the complementary-minor resolution and its duality, and the normalized-monad vanishings proving (1). These geometric inputs remain explicitly required; the abstract algebraic lemma is independent of them. For an actual selected pair, avoidance, primary coverage, and the resulting intersection quotient remain to be established; no original-pair value or full proof repair follows here.

Comparison sources:
- PR457: https://github.com/Akilleez-QA/read-em-and-weep/blob/961694c4f3c805f0d58508811a42da4030dce7a6/research/hm/fixed-cubic-interpolation/PROOF.md
- PR458: https://github.com/Akilleez-QA/read-em-and-weep/blob/b46c3b48a8b10a7d0656fde247f2c3f258d1fd23/research/hm/pair-interpolation/PROOF.md
- PR463: https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md

## 7. Single-cubic corollary with the missing correction retained

For a nonzero cubic v let Z=C∩V(v) scheme-theoretically and let k count contained component lines. The residual degree-five cubic defect, without an injectivity hypothesis, is

dim coker[N₂ --v→ N₅] = h⁰I_Z(3)−h⁰I_C(3)+k−1.

To prove it, the admissible tuple space maps onto res(S₃)∩vH⁰O_C with k-dimensional kernel. The polynomial preimage of that intersection is H⁰I_Z(3), because divisibility on each noncontained line retains the scheme multiplicities, while a contained line imposes vanishing on the entire component. Restriction has kernel H⁰I_C(3). Finally quotient the tuple space by diagonal constants. If v vanishes on every component, Z=C and the answer is 25−1=24, as required for the zero map. PR457's formula follows on imposing h⁰I_C(3)=0.
