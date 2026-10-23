# The positive reachable middle is the fixed-line restriction kernel

## Theorem and contribution

Let F be the actual normalized Horrocks–Mumford bundle, B=End₀(F), G=SL₂(F₅), and V the three-dimensional positive coordinate representation. Let L=P(W*) be the negative fixed line. Put

    N₂=H¹(B(2))₊, P₃=H¹(B(3))₊, N₄=H¹(B(4))₊,
    a:V⊗N₂→P₃

for actual positive linear multiplication. There is a canonical exact sequence

    V⊗N₂ --a--> P₃ --res_L--> H¹(L,B|L(3))₊ → 0,
    H¹(L,B|L(3))₊ ≅ A=Sym²W.                         (1)

Thus the actual reachable middle R=im a is exactly the restriction kernel, not merely some abstract subrepresentation of P₃. Its character and the character of its relation space E=ker a are

    R ≅ 1+3A+2V+3P+3D,             dim R=43,
    E ≅ 1+4A+4V+5P+7D,             dim E=80.          (2)

Here P in a character denotes the even four-dimensional irreducible; P₃ denotes the whole middle cohomology space of dimension 46. Isomorphisms in character formulas do not choose a canonical splitting.

There is also a stronger cancellation consequence. Split the actual positive quadratic multiplication by Sym²V=1⊕D as q₊=q_inv+q_D, and curry into V*⊗N₄. With the canonical invariant normalization of PR930, write C_inv, C_D for these curried maps. The canonical subspace

    S=C_inv(E) ⊆ im C_inv ∩ im C_D                    (3)

contains a G-subrepresentation isomorphic to

    1+3A+3V+3P+5D,                 dimension 56.      (4)

On E the two channels agree with opposite signs. This strengthens the previous dimension-53 lower bound by an additional A, and locates the forced contribution in a common image coming from actual first-arrow relations.

The result is global for the actual HM cohomology module. It assumes no c-d-f occurrence, source parameters or selected actual instance. It does not assert that the full curried image has dimension 43: the second positive arrow may have a kernel on R.

## 1. Immutable inputs

All repository paths below belong to Akilleez-QA/read-em-and-weep. Exact Git blobs and copied audit files are listed in audit-inputs/manifest.json.

1. PR930, commit f3e3319a35cdcb6f50b7a881b8ea19e7fb7da259, research/hm/positive-noninvariant-demand/PROOF.md, blob 94238a92e6ba8c2acb4eb75adfcdfedf3bacab4d. This imports and authenticates the minimal-factor theorem, the actual middle character P₃=1+4A+2V+3P+3D, and the canonical invariant-product character. It fixes the invariant normalization and the actual positive-factorization convention.

2. NEGATIVE-VERTEX-EVALUATION-SCALAR.md, commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/, blob 4d2737b94c19b84816382984db9ecb91af66ef0e. Section 1 proves the actual equivariant splitting

       F|L=O_L(3)₋ ⊕ O_L(−4)₊.                     (5)

   It is the maximal jumping-line split, not O(2)⊕O(−3). The proof uses the already established actual evaluation/minor scheme and its normal bundle; none is evaluated again here.

3. PR455, commit 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4, research/hm/twist-one-structural-vanishing/PROOF.md, blob 2881e6e4fdd1ff4fd3c1e909b00bd1a8a962a099. This proves H²B(1)=0 by the universal exterior-image estimate, normalizer symmetry and the dimension-gap argument, without an actual differential evaluation.

4. PR167, commit 063da90fc4543304e87e701cdefcc08225412f17, research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md, blob 58785a8799c43fd2c7da089d0ddc5e05822132a9. This proves H²B(t)=0 for t≥2, gives the primary section resolution and primary cohomology support used below.

5. POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md, commit eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c, research/hm/order-four-quadratic-load/, blob 019c1f31773476f0a4877d88632ce5d46fbd4b9f. Its already proved geometric result gives the canonical invariant product Q:N₂→N₄ with

       N₂=A+2V+3P+4D,  ker Q=A+D,
       im Q=2V+3P+3D.                              (6)

These are imported universal geometric and cohomological results, not newly selected coefficients, points, matrices or instance ranks. The comparison is bounded to these pinned dependencies.

## 2. The required high cohomology vanishes

For completeness, the vanishings in addition to H²B(1)=H²B(2)=0 follow directly from the pinned primary resolution. Tensoring that resolution by F*(t) gives a length-three locally free resolution of End(F)(t), whose terms, from homological degree zero, are

    E₀(t)=15F(t−3)⊕4F(t−2),
    E₁(t)=35F(t−4), E₂(t)=20F(t−5), E₃(t)=2F(t−7).

The diagonal vanishing rule for an exact resolution says that Hⁱ(End(F)(t))=0 if Hⁱ⁺ʲ(Eⱼ(t))=0 for every j. Splitting into short exact kernel sequences proves this rule; no differential rank is used.

Primary support gives H¹F(s)=0 outside s=0,1,2,3, and H⁰F(s)=0 for s<3. Since F*=F(1), Serre duality gives

    H³F(s)=H¹F(−s−4)*,
    H⁴F(s)=H⁰F(−s−4)*.

For t=0 and t=1, the groups H³E₀(t) vanish because their dual H¹ twists are negative. The groups H⁴E₁(t) are respectively 35H⁰F(0)* and 35H⁰F(−1)*, both zero. Remaining diagonal groups are above degree four. Hence H³B(0)=H³B(1)=0.

For t=0, H⁴E₀(0) is a sum of H⁰F(−1)* and H⁰F(−2)*, hence zero; all other diagonal groups are above degree four. Thus H⁴B(0)=0. The trace splitting End(F)=O⊕B transfers the vanishings to B.

We therefore have precisely the groups needed below:

    H²B(1)=H²B(2)=0,
    H³B(0)=H³B(1)=0, H⁴B(0)=0.                  (7)

## 3. Exact positive-coordinate reachability

The positive coordinate forms cut out L regularly. Their equivariant ideal Koszul resolution, tensored by B(3), is

    0 → Λ³V⊗B(0) → Λ²V⊗B(1)
      → V⊗B(2) → I_L B(3) → 0.                  (8)

Let J be the image of Λ²V⊗B(1) in V⊗B(2). Splitting (8) gives

    0 → Λ³V⊗B(0) → Λ²V⊗B(1) → J → 0,
    0 → J → V⊗B(2) → I_L B(3) → 0.              (9)

By (7), the first sequence gives H²J=0 from H²B(1)=H³B(0)=0, and H³J=0 from H³B(1)=H⁴B(0)=0. The second sequence then gives

    H¹(V⊗B(2)) ↠ H¹(I_L B(3)),
    H²(I_L B(3))=0.                              (10)

Finally the restriction sequence

    0 → I_L B(3) → B(3) → B|L(3) → 0

shows that H¹B(3)→H¹(B|L(3)) is onto and that its kernel is the image of H¹(I_L B(3)). By (10), that kernel is exactly the image of multiplication V⊗H¹B(2)→H¹B(3).

Taking inversion-positive parts is exact over C. Since V is positive, the positive part of the multiplication source is V⊗N₂. This proves the exactness in (1). In particular no higher Koszul transgression is omitted: its potentially relevant obstruction is killed by the imported H²B(1)=0.

## 4. Identify the actual restriction quotient and relation space

The two eigenline bundles in (5) are intrinsic. Their off-diagonal Hom bundles have degree 7 and −7 and physical inversion sign minus. The tracefree diagonal is O_L with sign plus. Twisting by O(3), whose physical sign on the negative fixed line is minus, yields

    B|L(3)=O_L(10)₊ ⊕ O_L(3)₋ ⊕ O_L(−4)₊.       (11)

Thus H¹(L,B|L(3))₊=H¹(O_L(−4)). Equivariant Serre duality on P(W*) identifies this with (Sym²W)*≅A; det W is trivial. There is no additional one-dimensional character because G is perfect. The quotient has dimension three.

Subtracting this A from the authenticated middle character gives the character of R in (2). To identify E, use the fixed tensor identities

    V⊗A=P+D, V⊗V=1+V+D,
    V⊗P=A+P+D, V⊗D=A+V+P+D.

Equation (6) gives

    V⊗N₂=2+7A+6V+8P+10D, dimension 123.

The actual exact sequence 0→E→V⊗N₂→R→0 then gives the second character in (2). This identifies the representation of the actual relation space without constructing its coefficients or choosing bases. It does not identify all minimal relations of the five-variable module.

## 5. Canonical common cancellation forced by these relations

Use the invariant projection ε:Sym²V→C normalized against the canonical invariant symbol q₀, so Q=q₊(q₀⊗−) and q_inv=ε⊗Q. As in PR930, ε is nondegenerate and ε♯:V→V* is an equivariant isomorphism. Therefore

    C_inv=ε♯⊗Q,
    ker C_inv=V⊗ker Q ≅ A+V+2P+2D, dimension 24.   (12)

The full actual curry C₊ is the composite b̃a, where b̃:P₃→V*⊗N₄ curries the second actual positive arrow. Hence on E=ker a,

    C₊=0,  C_D=−C_inv.                            (13)

Equations (12)–(13) prove (3) and the canonical exact sequence

    0 → E∩(V⊗ker Q) → E --C_inv--> S → 0.         (14)

Every irreducible multiplicity in E∩(V⊗ker Q) is bounded above by the corresponding multiplicity in V⊗ker Q. Subtracting (12) from the exact character of E gives

    (1+4A+4V+5P+7D)−(A+V+2P+2D)
       =1+3A+3V+3P+5D.

All coefficients are nonnegative. Semisimplicity proves the subrepresentation claim (4). The subspace S is canonical; the embedding of the abstract character in (4) need not be canonical, and equality in its lower bound is not asserted.

As a separate consistency check, im C₊ embeds into R, so its character is bounded by 1+3A+2V+3P+3D. Since im C_inv=2+6A+5V+6P+8D, the image-sum inequality of PR930 gives the same difference (4). The new content is the exact geometric reachable-middle quotient and the stronger localization (14), not merely this subtraction.

In particular q_D alone cannot have a symmetric positive-linear factorization through a single middle of dimension 46, or through R of dimension 43. The bound 56 is in V*⊗N₄=Hom(V,N₄), not in the 37-dimensional N₄ and not the image of one fixed quadratic. The actual sum still factors through R.

## 6. Remaining boundary

This determines one actual positive-linear image, its canonical quotient and the representation of its relation space using geometry. It does not determine the actual first-arrow coefficients, the second-arrow kernel, the exact intersection in (14), equality in the dimension-56 bound, or all mixed commutativity squares.

In particular no assertion im C₊=R is made. The actual second arrow may identify or kill elements of the reachable middle. No c-d-f scalar/C² decision, source exclusion, label change or source-dual pair decrement follows. No selected actual HM/source parameters, points, coefficients, derivatives, matrices or instance ranks are evaluated, and no large computation is used.
