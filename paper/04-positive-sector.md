# 4. Positive-sector obstruction calculation

## 4.1 Rank 33 at the invariant cone

The cone-spinor construction provides an invariant nilpotent adjoint N. The actual moving-line theorem makes every positive adjoint preserve its saturated spinor; the Ext-annihilator argument identifies every preserving adjoint with a polynomial multiple of N. Therefore

    H⁰(B_Q₀(4))₊ = N H⁰(O_Q₀(2))₊ = N(A ⊕ D5).

The kernel dimension is eight, so the 41-to-37 map has rank 33. Its cokernel is P4, of dimension four. The updated [rank theorem][R] records first-order vanishing; the following subsections explain that result and the subsequent second-order advance.

## 4.2 Why the first Bockstein is identically zero

The same centralizer argument at lower twist gives H⁰(B_Q₀(2))₊ = C N. Let ξ be the restriction connecting class of N in H¹(B)₊. Then

    ker(q₀: H¹(B)₊ → H¹(B(2))₊) = C ξ.

The actual characters are H¹(B)₊ = 1 ⊕ A ⊕ V ⊕ D5 and H¹(B(2))₊ = A ⊕ 2V ⊕ 3P4 ⊕ 4D5. Multiplication by q₀ identifies the unique source A with the unique target A. Negative quadratic multiplication therefore has a unique equivariant correction ζₐ in that source A such that

    aξ = q₀ζₐ.

For h ∈ A ⊕ D5, associativity in the actual cohomology module yields

    ahξ = h(aξ) = q₀(hζₐ).

Its class in the q₀-cokernel is zero. Thus the entire first Bockstein vanishes, including γ. The corrected vector hξ − t hζₐ satisfies

    (q₀ + ta)(hξ − t hζₐ) = −t²ahζₐ.

The canonical second Bockstein is accordingly β₂,ₐ(hξ) = −[ahζₐ] ∈ P4. Because the first Bockstein is zero, changing the first correction does not change this class. [Cyclic Rao proof][F].

## 4.3 The square filtration kills D5 at second order

The actual cone is treated through its weighted-stack square sequence, not through a guessed split vertex module. The ordinary square of the regular initial cubic/quintic pair has cover-degree Hilbert function

    1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 2, 1.

Its degree-eight relation isolates a canonical quadratic family ωₐ ∈ P4 ⊗ A*. The physical inversion parity and the ordinary-square filtration give

    β₂,ₐ(hξ) = 0      for h ∈ D5,
    β₂,ₐ(hξ) = hωₐ   for h ∈ A.

In fact, the stronger actual multiplication map D5 ⊗ H¹(B_Q₀(2))₊ → H¹(B_Q₀(4))₊ is zero. The remaining equivariant quadratic channel has only one possible scalar. At this stage of the argument that scalar is not yet known; its nonvanishing requires geometry. [Filtration proof][S].

## 4.4 The actual scalar is nonzero

The projective pullback orbit identifies the appropriate ambient deformation class with trace-free Atiyah contraction. If Dₐ is the negative SL₂ vector field corresponding to a, uniqueness of the A constituent identifies ζₐ with a nonzero scalar multiple of At_F(Dₐ).

For the regular spinor section σ, the expression σ ∧ Dσ is well-defined modulo the ordinary square of its zero ideal: changing a local lift or frame adds σ ∧ Mσ, which is quadratic in the section components. This gives a frame-independent square-shadow representative for the relevant connecting class.

The actual quintic relation gives a nonsplit extension

    0 → V O_L(−8) → P4 O_L(−6) → O_L → 0,

with nonzero class e. A splitting is excluded by the corresponding positive-to-negative line-bundle Hom vanishing. Differentiation of the relation identifies the actual obstruction, up to a common nonzero scalar and sign, as

    ωₐ = j_*(aDₐe).

The kernel of j_* is A. The universal SL₂ map controlling aDₐe is injective on the relevant sextic space; its nonzero G-image is D5, which cannot lie in the A kernel. Consequently the actual scalar is nonzero. This argument identifies the actual map before invoking representation theory. It does not assign an arbitrary nonzero coefficient to a merely permitted channel. [Full Atiyah/quintic proof][N].

## 4.5 Generic rank three and the four-or-five theorem

The resulting A-input is a nonzero multiple of h ↦ projection_P4(a²h). At a square direction a = ℓ², a kernel vector would give a sextic in the complementary V linear series divisible by ℓ⁴. That series has Wronskian degree 3(6−2) = 12. Such a sextic forces ramification weight at least two, while its group orbit has at least twelve points, requiring total weight at least 24. This contradiction proves injectivity at every square direction and hence on a nonempty open set. That open set also contains nonsquare directions, for which q₀ + ta is smooth when t ≠ 0.

Thus β₂ has generic rank three. The actual positive pencil has generic rank at least 36. Rank-nullity bounds its kernel between four and five, and semicontinuity extends the upper bound to a nonempty open set of inversion-even quadrics. Combining with Section 3 gives the total four-or-five result. [Integrated proof][G].

## 4.6 The next obstruction, without a nonvanishing claim

At a direction where β₂ has rank three, its surviving source is D5 and its target quotient P4/im β₂ is one-dimensional. For h ∈ D5, choose vₕ with q₀vₕ = ahζₐ; existence is precisely second-order vanishing on D5. Then

    (q₀ + ta)(hξ − thζₐ + t²vₕ) = t³avₕ.

The next class is [avₕ] modulo im β₂. Changing the second correction affects the q₀-cokernel through β₁ = 0; changing the first correction accounts for the quotient by im β₂. This explains the next canonical gate but does not prove it nonzero. The paper stops at the established four-or-five theorem.

## Pinned source references

[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ec080c229105457eafcd2583c8a47b362627a62e/research/hm/order-four-quadratic-load/SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c/research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md
[F]: https://github.com/Akilleez-QA/read-em-and-weep/blob/846968261441fef2cad247d22b66d37aed3f0f8f/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/04fb081d710f1d7e175f252601b96dddcd93106e/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md
[N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9f28cb10c38d7a0e29c1eb994594325fea7f22bf/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md
