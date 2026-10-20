# Ordinary quadratic Yoneda products cannot detect the full-deck [22] component

## Result

For the stipulated pullback bundle E on X=C^4, let G=(Z/2)^4 be the deck group and let S4 permute the four factors. In characteristic zero, the deck-invariant component of the image of the ordinary polarized quadratic obstruction map

    Q: Sym² Ext¹_X(E,E) → Ext²_X(E,E),
    Q(a,b) = a∘b + b∘a

has zero S4-isotypic component of type [22]. The normalization of Q by a factor of 1/2 is immaterial.

Consequently its Serre pairing with every full-deck-character [22] class in Ext² is zero. This includes non-invariant first-order deformations: the assertion is not restricted to the known 79-dimensional invariant family.

This is an exclusion of ordinary polarized quadratic Yoneda detectors. It does not assert that the retained obstruction class vanishes, that all quadratic products vanish, or that ordered products of invariant classes vanish separately. It says nothing about higher operations or detectors not arising from this quadratic map.

## Inputs

Write Y=(P¹)^4, σ:Y→P⁴ for the symmetric quotient, F=End H, and L_S=O_Y(−2 on S, 0 elsewhere). The inputs already independently established are:

1. H is the specified classical HM bundle. Stability gives H⁰(F(t))=0 for t<0. The verified classical cohomology theorem gives H¹(F(t))=0 for t≤−2.
2. The invariant Ext¹ dimension is 79, and the smooth full-coefficient family has injective Kodaira–Spencer map of dimension 79, with image in invariant Ext¹. Thus it exhausts invariant Ext¹.
3. The natural G⋊S4 action on End E is the pullback action: the line-bundle factor in E cancels under End. On P⁴ the factor permutations act trivially, since σ is the symmetric quotient.

References are ../pair-character-vanishing/PROOF.md, ../projective-target-directions/INVARIANT-EXT-STRUCTURAL-REDUCTION.md, ../projective-target-directions/FULL-COEFFICIENT-FAMILY.md, and ../hm-presentation-independent/PROOF.md. No historical total Ext¹ dimension is used.

## 1. Pushforward splitting for every nonempty proper character

Put B_S=σ_*L_S and r=|S|, with 1≤r≤3. Finite flatness of σ gives a vector bundle of rank 24. Projection formula and Künneth give

    H^j(B_S(n)) = H^j(Y, O(n−2 on S, n elsewhere)).

For n≥2 only degree zero occurs. For n=1 or −1 all groups vanish. At n=0 the sole group is H^r(B_S)=k. For n≤−2 only degree four occurs. Thus the sole intermediate cohomology of all twists is H^r(B_S)=k.

The Euler exterior-power sequences

    0 → Ω^i → O(−i)^{binom(5,i)} → Ω^{i−1} → 0

for 1≤i≤r, with Ω⁰=O, and H^j(B_S(i))=0 for j>0 and i≥1, show by successive connecting maps that

    Hom(Ω^r,B_S) → H^r(B_S)

is surjective. Choose f_S inducing a nonzero map on H^r. Naturality identifies its image under these connecting maps with H^r(f_S) applied to the canonical Euler class generating H^r(Ω^r).

Finite duality gives, as underlying bundles,

    B_S^*(−5) ≅ B_{S^c}.

Choose independently f_{S^c}:Ω^{4−r}→B_{S^c} by the same construction. Dualizing and twisting by −5 gives

    g_S:B_S → (Ω^{4−r})^*(−5) ≅ Ω^r.

By Serre duality H^r(g_S) is dual to the nonzero H^{4−r}(f_{S^c}), so H^r(g_Sf_S) is nonzero. Since End(Ω^r)=k, the composite is a nonzero scalar times the identity, and f_S splits. The simplicity statement follows, for example, by the same Euler sequences and the acyclicity of Ω^r(i) for 1≤i≤r.

Therefore

    B_S ≅ Ω^r ⊕ R_S.

The remainder has no intermediate cohomology in any twist. Horrocks' splitting criterion makes R_S a sum of line bundles. Since H⁰(B_S(1))=0, every summand is O(−a) with a≥2.

The complementary lift is important: B_S is not being identified with its own shifted dual when r=1 or 3. No equivariant self-duality or multiplicative compatibility of the splitting is assumed.

For r=4 there is no intermediate cohomology at all, and H⁰(B_S(1))=0. Hence B_S itself is a sum of O(−a), a≥2. More explicitly B_all=σ_*O_Y⊗O(−2), but the multiplicities are unnecessary.

## 2. Only singleton nontrivial characters contribute to Ext¹

The character formula and projection formula give

    V_S := Ext¹_X(E,E)_{χ_S} = H¹(P⁴,F⊗B_S).

Every line-bundle summand above contributes zero by H¹(F(−a))=0 for a≥2. Thus, for 1≤r≤3,

    V_S ≅ H¹(F⊗Ω^r),

and V_all=0.

For r=2, tensoring 0→Ω²→O(−2)^10→Ω¹→0 with F gives H¹(F⊗Ω²)=0: H⁰(F⊗Ω¹)=0 because F⊗Ω¹ injects into F(−1)^5, and H¹(F(−2))=0. This also gives H⁰(F⊗Ω²)=0 because it injects into F(−2)^10.

For r=3, use

    0 → F⊗Ω³ → F(−3)^10 → F⊗Ω² → 0.

The two groups H⁰(F⊗Ω²) and H¹(F(−3)) vanish, so H¹(F⊗Ω³)=0.

Accordingly the only possible nontrivial character contributions are singletons. Write

    U = H¹(P⁴,F⊗Ω¹).

No dimension of U is needed.

## 3. The singleton stabilizer acts trivially

Fix S={1}. Its stabilizer in S4 is S3, permuting the other three factors. Künneth identifies the unique intermediate generator with

    H¹(P¹,O(−2)) ⊗ H⁰(P¹,O) ⊗ H⁰(P¹,O) ⊗ H⁰(P¹,O).

The S3 action is trivial: the permuted factors all have cohomological degree zero, so there is no Koszul sign. Equip Ω¹ on P⁴ with the trivial S3 action; the quotient base is fixed pointwise.

Average the lift f_S over S3. Its H¹ map remains the same nonzero map because the generator is fixed. The averaged lift still splits as an underlying bundle by the preceding argument. Tensoring with F and taking H¹ yields an S3-equivariant isomorphism U→V_S, since the underlying complementary line-bundle summands have zero H¹ after tensoring with F. The action on U is trivial: both F and Ω¹ carry trivial S3 action on P⁴.

It follows that, as an S4 representation,

    V_noninv = ⊕_{i=1}^4 V_{ {i} }
             ≅ Ind_{S3}^{S4}(U_trivial)
             ≅ U ⊗ k^4_perm.

This is also compatible with the G-grading: the ith copy of U has deck character χ_i. Transport the chosen lift by permutations to make this identification; stabilizer invariance makes the transport independent of the chosen permutation.

## 4. The invariant quadratic source has no new [22]

Put V_0=Ext¹(E,E)^G and V=V_0⊕⊕_i V_i. Because all deck characters have order two, a product of two characters is trivial precisely when they are equal. Therefore

    (Sym² V)^G = Sym² V_0 ⊕ ⊕_{i=1}^4 Sym² V_i.

There are no invariant cross terms V_0⊗V_i or V_i⊗V_j with i≠j. The second summand, with its S4 action, is

    Sym² U ⊗ k^4_perm
      ≅ Sym² U ⊗ ([4] ⊕ [31]),

where S4 acts trivially on Sym² U. It has no [22] constituent. Equivariance and semisimplicity imply that its image under Q also has no [22] constituent. No formula for multiplication in a pushforward splitting is needed.

On the first summand Q vanishes identically. Indeed every v∈V_0 is the tangent of a curve in the smooth 79-dimensional coefficient family, so its ordinary second-order obstruction v∘v is zero. Polarizing (v+w)∘(v+w) gives v∘w+w∘v=0. The equality of tangent spaces comes from the independently established invariant dimension and the injective 79-dimensional family.

Thus the [22] projection of the deck-invariant quadratic image is zero. This remains true for arbitrary sums of invariant and non-invariant first-order deformations: the other cross terms have nontrivial deck character and cannot contribute to that projection.

## 5. Serre duality and the full-deck character

On X=C^4, the one-dimensional H⁴(O_X) carries deck character χ_all and S4 character sgn. Each elliptic involution acts by −1 on H¹(O_C), and permuting four degree-one factors contributes the Koszul sign.

The trace/Serre pairing is equivariant and perfect:

    Ext²(E,E) × Ext²(E,E) → H⁴(O_X) ≅ k_{χ_all⊗sgn}.

Hence the full-deck-character subspace pairs only with the deck-invariant subspace. In S4 type, [22] is self-dual and [22]⊗sgn≅[22]. Therefore a full-deck [22] class can pair only with the invariant [22] component of a detector. That component is zero for every Q-image by Section 4.

## 6. Audit boundaries and ordered products

The smooth family kills the symmetric combination of two invariant degree-one products, not each ordered product separately. An ordered product a∘b for invariant a,b may have an alternating contribution. This proof does not exclude a [22] component in that alternating contribution. Thus one must not replace Q by the full ordered map V⊗V→Ext² without a new argument.

For completeness, the deck-invariant ordered products sourced entirely by non-invariant classes still come from ⊕_i(V_i⊗V_i)≅(U⊗U)⊗k^4_perm, which also lacks [22]. The unaddressed ordered-product possibility is the invariant-invariant alternating sector.

The argument is additive cohomology plus equivariance and the existence of an actual smooth family. It does not use multiplicative splitting, the historical singleton dimension, source-level primitive choices, numerical ranks, coefficient specializations, point or jet evaluations, or any residual/detector execution. It does not establish higher-order unobstructedness outside the invariant family. All conclusions are for the stipulated characteristic-zero data and their base changes.
