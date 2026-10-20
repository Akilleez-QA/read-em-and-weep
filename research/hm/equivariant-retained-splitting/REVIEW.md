# Independent audit: binary-form-equivariant coefficient splitting

## Scope convention

The assertions below concern coefficient geometry, finite-group actions and the stated coherent cohomology. References to unevaluated coordinates mean that this argument does not evaluate them; they are not a claim about the latest status of every other argument. The raw-source regularity, coefficient/character identification and raw-to-canonical class comparison are separate hypotheses wherever a source application is discussed. No first-order lifting theorem, higher-order obstruction vanishing, formal integrability or algebraicity follows merely from these coefficient statements.

## Verdict

**PASS, with a necessary qualification to the posted noncanonicity claim.** Over characteristic zero, the actual binary-quadratic multiplication geometry supplies a unique SL₂-equivariant splitting of the canonical coefficient sequence. It is automatically GL₂-natural. Consequently it supplies an unconditional, canonical coefficient-induced projection to the twenty-dimensional retained target, relative to that binary-form geometry. No SL₂-linearization of HM is required to tensor this already constructed coefficient projector with End₀(HM).

The splitting is **not** intrinsic to a bare filtered vector bundle with the same isomorphism types and no binary-form symmetry. It does **not** prove any obstruction component vanishes, provide a primitive, or make the mixed source an invariant vector. The existing weighted-trace first-stage equation remains correct, with no factor 1/6.

Primary source audited: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276362114. Supporting public source comments: [detector formulation](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6272324961) and [complete normalized source](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716). This review makes no source-value evaluation.

## 1. Geometry and canonical linearizations

Work over a characteristic-zero field (in the application, C). Let V have dimension two. With the convention H⁰(P(Symᵈ V),O(1)) = Symᵈ V*, set

- X = P(Sym² V) × P(Sym² V),
- Y = P(Sym⁴ V),
- m(q₁,q₂) = q₁q₂.

Multiplication is GL(V)-equivariant and factor interchange commutes with GL(V). The finite locally free algebra F = m_*O_X has its geometric GL(V)-linearization. Algebra trace is equivariant. Thus F⁺ and G = ker(Tr:F⁺→O_Y) are canonically linearized. The trace normalization is Tr(1)=6.

Take as established in the source the underlying splitting type G ≅ O(-1)⊕O(-2). It follows that W = H⁰(G(1)) has dimension one. The evaluation map defines the canonical line subbundle

    i: L = W⊗O(-1) → G,
    π: G → Q = G/L,

with Q of underlying type O(-2). Evaluation is equivariant, so these are equivariant subbundle and quotient maps. There is no need to choose a basis of W or trivialize Q(2).

Every one-dimensional algebraic representation of SL(V) is trivial. In particular the character factors in W and Q(2) disappear after restriction to SL(V). Therefore

    H⁰(Hom(Q,L)) ≅ Sym⁴ V*

as SL(V)-representations, up to the harmless convention dualizing V. This representation has dimension five and contains no invariant vector. Over GL(V) a determinant-character twist must be retained; it does not change the SL(V) assertion. In the convention above, W ≅ (det V*)², Q(2) ≅ (det V*)⁴, and the translation module is Sym⁴ V*⊗(det V)². These character identifications are not needed to prove the theorem.

The subgroup SL(V) is defined without choosing a volume form: it is the kernel of the intrinsic determinant map GL(V)→G_m.

## 2. Existence, without informal averaging of an affine torsor

Apply Hom_Y(Q,-) to the canonical short exact sequence. Since

    Ext¹_Y(Q,L) = H¹(Y,Hom(Q,L)) = H¹(P⁴,O(1)) = 0,

we obtain a surjection of finite-dimensional rational SL(V)-representations

    Hom_Y(Q,G) → Hom_Y(Q,Q) = k,
    s ↦ π∘s.

Its kernel is Hom_Y(Q,L). The identity endomorphism of Q is invariant, even though Q has its own linearization. In characteristic zero, SL₂ is linearly reductive, so taking invariants is exact. Hence identity_Q has an invariant lift s. That lift satisfies πs = identity_Q and is the required equivariant splitting.

This proves the affine-fixed-point assertion algebraically. One need not attempt an infinite-group average directly on an affine variety. Equivalently, the space of splittings is the invariant fiber over 1 of the displayed equivariant linear map, and exactness of invariants produces a point in this fiber. Over C a compact-form averaging argument gives the same result, but is unnecessary.

Reference for the representation-theoretic ingredient: Brian Conrad, *Reductive Group Schemes*, proof of Proposition 5.4.1, printed pp. 173–174, for complete reducibility and right-exactness of invariants in characteristic zero; see also Exercise 1.6.11(ii) and Appendix B.2 for its cohomological background, https://math.stanford.edu/~conrad/papers/luminysga3.pdf . The proof here only uses this finite-dimensional representation-theoretic result, not a claim that all equivariant vector-bundle extensions split.

## 3. Uniqueness and GL₂ naturality

If s and s' are equivariant splittings, their difference factors through L and lies in

    Hom_Y(Q,L)^SL(V) = (Sym⁴ V*)^SL(V) = 0.

Thus s=s'. The five-dimensional affine family of ordinary splittings has exactly one SL(V)-fixed point.

For every g in GL(V), transport s using the geometric linearizations. Because SL(V) is normal in GL(V), the transported map g·s is again SL(V)-equivariant and is still a splitting of π. Uniqueness gives g·s=s. Thus the splitting is GL(V)-equivariant. The same reasoning applies to an isomorphism V→V': it transports the unique splitting to the unique splitting of the transported multiplication geometry. Consequently no binary-coordinate choice or scale of σ is built into s.

An alternative concrete construction is useful. Twist the sequence by O(2):

    0 → L(2) → G(2) → Q(2) → 0.

The induced map on global sections is surjective because H¹(L(2))=0. The six-dimensional H⁰(G(2)) has SL₂-type Sym⁴ V*⊕k. Its invariant line maps isomorphically onto H⁰(Q(2)), so evaluation of that line yields the canonical complement to L. It is the same splitting by uniqueness.

This does not produce a preferred scalar basis of Q(2), W, or their duals. It produces a preferred subbundle and projector, which is all that the detector decomposition requires.

## 4. What canonicity means, and what it does not mean

For the bare sequence 0→L→G→Q→0, ordinary splittings form a torsor under Hom_Y(Q,L), a five-dimensional vector space. There are bundle automorphisms preserving L and Q that move every ordinary splitting. Thus the original noncanonicity statement is correct if only this bare filtered-bundle data is retained.

The actual map m retains strictly more information: it is binary-form multiplication, with its natural SL₂ action. In that geometric category there is a unique equivariant splitting. Therefore the unqualified sentence “there is no unconditional canonical projection onto a twenty-dimensional complement” is too strong for the binary-form setup. It should distinguish bare filtered-bundle canonicity from canonicity relative to the specified multiplication geometry.

The result is not asserted for an arbitrary finite map having the same pushforward splitting type, an arbitrary projective-coordinate change that forgets the binary-form structure, or arbitrary positive characteristic. Reductivity alone does not give exact invariants in positive characteristic. The current proof is characteristic zero.

## 5. Tensoring with HM does not require HM equivariance

Write B₀=End₀(HM). Define coefficient projectors

    P_Q=sπ : G→G,
    P_L=identity_G-P_Q : G→G.

They are already regular O_Y-linear morphisms. Therefore identity_B₀⊗P_Q and identity_B₀⊗P_L exist for any vector bundle B₀, with no group action on B₀. Passing to cohomology gives the canonical splitting

    D₃₀ = H²(B₀⊗G) ≅ D₁₀ ⊕ D₂₀,
    D₁₀ = H²(B₀⊗L),
    D₂₀ = H²(B₀⊗Q).

For the Serre-dual coefficient sequence,

    0 → Q∨⊗ω_Y → G∨⊗ω_Y → L∨⊗ω_Y → 0,

the canonical retraction to Q∨ is s∨. Thus for every retained class C,

    C₂₀ = H²(identity_B₀⊗s∨⊗identity_ω)(C)

is defined unconditionally in T₂₀=H²(B₀⊗Q∨⊗ω_Y). The first component remains C₁₀ = H²(identity_B₀⊗i∨⊗identity_ω)(C). The two components jointly recover C. The resulting projector on the full retained target is induced by P_Q∨ = π∨s∨.

This is functorial in B₀ and compatible with pullback/transport when B₀ is transported together with the geometry. It is not a claim that the fixed HM bundle, its cohomology, or the source C carries an SL₂ representation. In particular no invariant-vector vanishing argument about C follows from the coefficient splitting.

The source’s dimensions 10, 20, 30 are used as previously established numerical inputs; the construction of the projector does not depend on those numerical values.

## 6. Weighted trace and normalization

Finite duality gives m_*ω_X ≅ Hom_Y(F,ω_Y). For λ in that Hom sheaf, the duality counit is

    Tr_m^ω(λ)=λ(1).

The F-module action is (aλ)(b)=λ(ab). Hence for the discriminant-polarization section σ,

    Tr_m^ω(σλ)=λ(σ).

This is an exact identity. There is no division by the degree six. The factor 1/6 belongs to the unrelated algebra projector F→O, a↦Tr(a)/6, used to separate the constant coefficient summand.

The invariant discriminant-polarization line W embeds in H⁰(X,O(1,1)). Algebra trace maps this equivariantly to H⁰(Y,O(1)), whose SL₂-type is Sym⁴ V*. The latter has no invariant vector, so the trace of this line is zero. Choosing a nonzero σ merely chooses a basis of W.

Intrinsic first-stage target:

    H²(B₀⊗L∨⊗ω_Y)
      = W*⊗H²(B₀⊗O(1)⊗ω_Y).

After evaluating on σ∈W, the formula is precisely

    C₁₀(σ)=Tr_m^ω(σ C) ∈ H²(B₀⊗ω_Y(1)) = H²(B₀(-4)).

If GL₂-equivariant identifications of canonical bundles are being kept, determinant-character lines must be retained in writing ω_Y as O(-5). As an ordinary sheaf and with the source's fixed conventions, the -4 twist is correct. The formula in terms of ω_Y(1) avoids any such linearization convention.

Because σ is trace-zero, this evaluation annihilates the dual constant summand. Factor interchange is even here, so the formula restricts to the stated retained even sector. It does not implicitly establish that an independently specified constant obstruction has vanished.

## 7. Regular Čech primitives and independence of choices

Let E=B₀⊗G∨⊗ω_Y, A=B₀⊗Q∨⊗ω_Y, and R=B₀⊗L∨⊗ω_Y. Use an affine cover of Y with affine finite intersections, so the Čech complex computes these coherent-sheaf cohomology groups. Let c∈Čech²(E) be a closed representative, and r its image in Čech²(R).

If the first-stage class vanishes, choose a regular p∈Čech¹(R) with δp=r. Such a p exists precisely because the class vanishes in the computed Čech cohomology. It is not furnished merely by the structure theorem.

The sheaf map E→R is surjective, and over each affine intersection its map on sections is surjective (the relevant H¹ of the quasi-coherent kernel vanishes). Therefore p lifts to a regular cochain p̃∈Čech¹(E). Then

    c'=c-δp̃

is closed and takes values in A. No division by a branch equation, inverse discriminant, or meromorphic primitive is required for this lifting step.

- Changing p̃ with fixed p changes c' by an A-valued coboundary.
- Changing p by a closed R-valued 1-cochain changes [c'] by the connecting map H¹(R)→H²(A).
- That connecting map is zero because the coefficient sequence splits as an ordinary sheaf sequence; tensoring preserves a splitting.
- Changing c by a coboundary gives the same kernel class after the corresponding adjustment.

Thus the source's conditional residual class is well-defined and independent of choices even before using the unique equivariant splitting. With the new splitting it equals the unconditional component C₂₀ whenever C₁₀=0. The additional structure defines C₂₀ also when C₁₀≠0; it does not make the conditional primitive equation soluble in that case.

Using the canonical splitting gives a canonical lift map R→E, but it still does not choose the primitive p itself. Solving the regular first-stage equation remains genuine work.

## 8. The alternating-primitive warning survives unchanged

The weight σ is not pulled back from Y. Indeed, if σ=m*a, then Tr(σ)=6a, contradicting trace-zero and σ≠0. Multiplication by σ need not commute with averaging over the larger root-permutation group. Thus a primitive for an unweighted averaged expression cannot simply be multiplied by σ to obtain the required weighted primitive. The equivariant coefficient complement does not repair that commutation failure.

## Approved corrected conclusion

The retained target has a canonical 10+20 decomposition relative to the binary-form multiplication geometry, obtained by the unique SL₂-equivariant coefficient splitting; this is GL₂-natural and does not require equivariance of HM. The first ten-component is still given by the exact weighted duality trace, with no factor 1/6. Neither component has been evaluated or proved zero. A regular primitive for the weighted ten-component remains unestablished.
