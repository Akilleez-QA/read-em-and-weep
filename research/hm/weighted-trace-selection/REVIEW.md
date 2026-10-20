# Independent audit: weighted selection and the trace-corrected square

## Scope convention

The assertions below concern coefficient geometry, finite-group actions and the stated coherent cohomology. References to unevaluated coordinates mean that this argument does not evaluate them; they are not a claim about the latest status of every other argument. The raw-source regularity, coefficient/character identification and raw-to-canonical class comparison are separate hypotheses wherever a source application is discussed. No first-order lifting theorem, higher-order obstruction vanishing, formal integrability or algebraicity follows merely from these coefficient statements.

## Verdict

**PASS at the stated algebraic-sheaf and imported class-comparison scope.** The weighted-selection proof and the trace-corrected-square coefficient construction are mathematically sound over characteristic zero. The projector constants, trace corrections, determinant-line factors, and cubic coefficients are correct. The statements retain their coefficient and source-comparison qualifications.

The two constructions do different jobs. Weighted selection identifies the relevant upstairs isotypic component but removes no further part of the already retained paired class. The trace-corrected square gives an explicit, everywhere regular coefficient complement and an unconditional twenty-component map. Neither construction evaluates the actual class or establishes a new vanishing or regular primitive.

The actual raw-source comparison, its H character, and the sign/constant transfer are imported from the source setup. This audit proves the abstract and coefficient-geometric assertions; it does not independently revalidate those source-specific identifications.

## 1. The weight representation and exact projector

Put Z=(P(V))^4 and A=O(1,1,1,1), with the ordinary, ungraded permutation linearization. Multiplication of linear factors gives an equivariant identification A=q*O_Y(1). There is no permutation sign in this identification.

The polarized discriminant gives three sections indexed by the unordered pair partitions. Their sum is zero. For example, on the affine root chart,

    σ12|34 = ((x1+x2)(x3+x4) - 2(x1x2+x3x4))/4.

Adding the three relabelings cancels every quadratic monomial. Coefficient comparison also shows that their span has dimension two. This is an identity of global homogeneous sections, not a calculation of any obstruction source.

S4 permutes the three partitions through S4/V4≅S3. The two-dimensional quotient of their permutation representation is its irreducible standard representation. Thus the span U of the weight orbit is Specht [2,2], with character

    (2,0,2,-1,0)

on the classes 1, (12), (12)(34), (123), (1234). In particular U*=U and U⊗sign≅U. The GL2 determinant character of the weight is a separate commuting factor; SL2 invariance does not imply S4 invariance.

For any genuinely S4-linearized cochain complex K and equivariant multiplication U⊗K→K_A, tensor-Hom adjunction shows that sign can occur in U⊗K_λ only for λ=[2,2]. Therefore, degree by degree,

    e_sign Mσ = e_sign Mσ e22,

where

    e22 = (1/12)(2 id + 2 Σ_double-transpositions g - Σ_3-cycles g).

This formula has the correct character normalization: dim(U)/|S4|=2/24. Semisimplicity of the finite group algebra applies even when the cochain spaces are infinite-dimensional.

A useful equivalent identity is

    e22 = e_V4 - e_triv - e_sign.

An even stronger immediate consequence is

    e_sign Mσ e_sign = 0.

Thus the unweighted sign component contributes identically zero to weighted sign projection. This is stronger than merely saying that weighting and sign averaging need not commute.

The same selection identity holds with e_triv in place of e_sign, because U*=U. This accounts for a consistent change between plain-coefficient and natural-canonical-form conventions.

## 2. Cochain regularity and the commutator

The displayed identity

    e_sign(σR) - σ e_sign(R)
      = (1/24) Σ_g sign(g)(gσ-σ)gR

follows directly from g(σR)=(gσ)(gR). It is an equality of regular cochains when the group acts genuinely on the sheaf and its complex. The expression involves no division by σ or by a branch equation.

If δR=0 and e_sign R=δP, multiplication by the global section σ gives

    e_sign(σR)=δ(σP)+Kσ(R),    δKσ(R)=0.

Consequently the weighted class is [Kσ(R)]. This statement furnishes no primitive for Kσ(R). The primitive P may be replaced by e_sign P, and then its entire contribution after multiplying and projecting again to sign is zero.

A cohomological permutation action alone is insufficient to justify the displayed regular cochain formula or a regular primitive. An equivariant Čech resolution or another genuine equivariant regular resolution supplies what is needed. Pullback coefficients q*B have a canonical S4-linearization from q∘g=q, irrespective of whether the original bundle B has any S4 or SL2 action. In particular no such action on HM, or on a fixed paired deformation ambient, is required. Matrix expressions must still include frame transports.

## 3. Canonical lines and the paired-sector limitation

With H0(P(V),O(1))=V*, the natural equivariant canonical line is

    ω_Z ≅ A^(-2) ⊗ (det V*)^4 ⊗ sign.

The last factor records permutation of four one-dimensional differential factors. For Y=P(Sym4 V),

    ω_Y ≅ O_Y(-5) ⊗ (det V*)^10.

These characters matter when writing equivariant identifications; the corresponding ordinary bundle degrees remain -2 on each root factor and -5 on Y. Tensoring source and target consistently by sign exchanges invariant and sign projectors but leaves [2,2] unchanged.

Let H=<(12),(34),(13)(24)>. Its order is eight, V4⊂H, and H/V4 is the order-two subgroup fixing one pair partition. Hence

    Ind_H^S4(sign|H)=sign⊕[2,2],
    Ind_H^S4(1)=1⊕[2,2].

For an H-sign vector r, e_V4 r=r and e_triv r=0, so r=e_sign r+e22 r. Once the imported sign/constant class is zero, [r]=e22[r]. Therefore the selection theorem removes nothing further from the retained paired class.

The H-sign statement must use the stripped coefficient/ordered-volume convention specified in the proof. A full geometrically pulled-back block-even canonical-form source is H-invariant; stripping the ordered root top form gives sign|H. Exchanging two dimension-two blocks is even, as required. Both conventions give the same retained [2,2] conclusion.

The H-sign slice of an upstairs [2,2]-isotypic module need not itself be S4-stable. In particular this does not assert an S4 representation on the fixed thirty-dimensional paired target. It does not distinguish its ten- and twenty-dimensional coefficient pieces.

## 4. The trace-corrected square is a global complement

Write F=m_*O_X, with rank-six algebra trace Tr_F, and let F+ be the rank-three block-even subalgebra. The proposed section

    τ=σ²-m*(Tr_F(σ²)/6)

is even, tracezero, and SL2-invariant. Rescaling σ by c rescales τ by c².

The nonvanishing proof is valid. On a generic reduced three-point fiber of the unordered-pairing algebra, let a,b,c be the values of σ. Then a+b+c=0. If τ vanished identically, all three squares would agree. Over characteristic zero, three choices of signs of a common nonzero square root cannot sum to zero; hence a=b=c=0. That would make σ vanish densely, contrary to its nonzero polynomial definition. The generic fiber argument is used only to prove nonvanishing, not to define a map by an étale formula.

There is also a direct proof of the global-complement step that does not presuppose an equivariant splitting. In

    0→L(2)→G(2)→Q(2)→0,

H0(L(2)) restricts to the nontrivial irreducible SL2 representation Sym4 V*, so it contains no invariant vector. The nonzero invariant τ cannot lie in that kernel. Its image in H0(Q(2)) is therefore nonzero. Since Q(2) is an ordinary trivial line bundle, its nonzero global section is nowhere zero. This constructs an everywhere defined splitting by τ itself.

Intrinsically, multiplication followed by trace correction gives

    W² → H0(G(2)),
    u⊗v ↦ uv-m*Tr_F(uv)/6.

It identifies Q(2) with W² and gives the regular complement W²⊗O(-2)→G. This agrees with the unique binary-form-equivariant complement: two such splittings would differ by an invariant in Hom(Q,L), and that invariant space is zero. No preferred basis of W is supplied or needed.

## 5. Twenty-component duality and exact normalization

Under finite duality, m_*ω_X=Hom(F,ω_Y), and multiplication satisfies (aλ)(b)=λ(ab). Thus

    Tr_m^ω(τλ)=λ(τ).

Evaluation on the complement is exactly the canonical dual projection, yielding

    C20 ∈ W^(-2)⊗H2(B0⊗ω_Y(2)),
    C20(τ)=Tr_m^ω(τC).

The ordinary target twist is B0(-3). The determinant factors must be retained if GL2-equivariant canonical-line identifications are used. No action on B0 is necessary, because the coefficient map already exists as a regular sheaf map.

For a general full even class,

    Tr_m^ω(τC)
      = Tr_m^ω(σ²C) - (Tr_F(σ²)/6) Tr_m^ω(C).

Vanishing of the constant class removes the correction in cohomology. A pointwise retained representative removes it at cochain level. The distinction in the proof is necessary and correctly stated.

There is no degree divisor in either weighted duality evaluation. The factors of six here belong to the algebra-trace correction or the constant inclusion. The comparison of weighted sign projection with this duality evaluation remains conditional on the imported source-specific transfer and coefficient-module compatibility; the representation theorem alone does not establish that comparison.

## 6. Cubic relation and ramification

The unit, σ, and τ give the global twisted bundle decomposition

    F+ ≅ O ⊕ W O(-1) ⊕ W² O(-2).

Replacing τ by σ² is an invertible triangular change of basis. Thus the algebra is globally generated by the line W O(-1), in the twisted sense explained in the proof.

On even elements Tr_F=2 Tr_F+. For t2=Tr_F(σ²), t3=Tr_F(σ³), Newton identities for the rank-three multiplication operator with trace zero give

    σ³-(t2/4)σ-t3/6=0.

These constants are correct. The relation follows globally from Cayley–Hamilton, including nonreduced fibers. Locally the quotient by this monic cubic has basis 1,z,z², which maps isomorphically to the established basis of F+. Hence the presentation remains valid over ramification. No nondegenerate algebra-trace pairing, inverse discriminant, or unramified extension argument is required.

## 7. Scope of the result

The audited statements use the established finite-flat coefficient geometry, splitting type G≅O(-1)⊕O(-2), and characteristic zero. The numerical dimensions 10, 20, and 30 are imported cohomology inputs. The source-specific character, closure, regularity, and comparison with upstairs End cohomology are also imported.

Subject to those inputs, both constructions are regular and canonical in the stated geometric categories. All actual weighted coordinates, source values, and the existence of weighted regular primitives remain uncomputed. No source value or obstruction coordinate is evaluated by this review.

## 8. Additional check: the square complement has the same permutation type

The complement weight also has S4 orbit type [2,2]. If σ1,σ2,σ3 are the three pairing weights, pullback of the trace correction gives

    τi=σi²-(σ1²+σ2²+σ3²)/3.

The three τi sum to zero and are permuted through S3. Their span is nonzero by the nonvanishing proof above; the zero-sum permutation quotient is irreducible, so that span is again [2,2]. Thus both the ten- and twenty-component weighted maps select the same upstairs S4 isotypic type, at different line-bundle twists. Their difference is coefficient geometry and multiplicity, not a different S4 irreducible representation.

For a₂=Tr_F(σ²)/6, the exact cochain identity is

    e_sign(σ²R)=e_sign(τ e22R)+a₂ e_sign(R).

Consequently the known sign primitive accounts only for the invariant correction term in the square weight; it does not solve the twenty-component weighted equation.

## Public comparison

The square and cubic coefficient conclusions in §§4–6 are already established in [the committed canonical cubic proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/c5fb4a0bcc3c8e35093fcfcff9a73a79a45a18e5/research/hm/cubic-reconstruction/PROOF.md). They are retained here as the complete independent review of this selection argument, including its distinct invariant-line proof and the same-isotype observation in §8, not as new obstruction-vanishing claims. The geometric sign/constant coefficient transport is supplied by [PR387](https://github.com/Akilleez-QA/read-em-and-weep/blob/e276e0e181e62a60c3ae24759b8bfed746f2492b/research/regular-trace-transport/PROOF.md); actual raw class comparison remains separate.
