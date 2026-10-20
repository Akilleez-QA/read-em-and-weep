# Source-bound square-zero physical ambient factorization

## Checked finding

**Yes for the specified upstairs mixed representative, conditional only on the source's declared geometric leaf/derivative interpretation.** On C⁴=C²₁₂×C²₃₄, over R=k[s,t]/(s²,t²), the polarized PR16 ambient is literally the external tensor product of its two first-order pair algebroids. This includes its product, overlap maps, and actual central triple units, not just their inner automorphisms or HKR classes. The current PR79 frozen mixed residual is the module defect for this same representative under the source premises described below.

This supplies the *upstairs original-ambient factorization* hypothesis in [research/hm/null-root-morita-inertia/root-morita-0719](https://github.com/Akilleez-QA/read-em-and-weep/blob/711c6bf8c6248f46d73661be8a42ede671a3712b/research/hm/null-root-morita-inertia/root-morita-0719/RESULT.md) §6. It does not identify the invariant/root-transported ambient with the independently prescribed corrected P²×P² ambient. All thirty retained obstruction values remain unknown.

## Pins and inspected evidence

Historical context: [PR1 comment 6263380151](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6263380151). The source baseline is PR79 at commit 4659e4425c6b5ab6b1899e6af93656ac03ff0862. The following deductions use static source statements, not newly executed certificates.

1. [PR16 pinned research/hm/second-order-algebroid.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md#L13-L30): factor vector fields and Moyal coefficients. Lines 52–64 define factor q,a; 93–111 split b and T; 116–137 give F=id+h²T, A=exp(hb) and actual descent identities. This is a one-parameter source, not itself a claimed two-parameter presentation.
2. The [two-parameter ambient specification](https://github.com/Akilleez-QA/read-em-and-weep/blob/9e3d8dc8525a7d11ae919dfac2126794c9bdc366/research/hm/null-literal-ambient-extension/two-parameter/RESULT.md) gives pair support, specifies μ, F and A, and checks the mixed pentagon and literal diagonal recovery. Its historical statement is [PR1 comment 6259871686](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259871686). Its existence proof is not needed beyond these explicit coefficients.
3. [PR79 research/hm/null-second-order-raw-closure/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-second-order-raw-closure/PROOF.md#L35-L82): lines 35–44 explicitly prescribe the same square-zero mixed Moyal product (its parameters t,u are renamed s,t here); 64–82 prescribe h=1+s bP+t bQ+st bP bQ and the complete ten-term module defect. Lines 135–152 establish the requisite complementary-coordinate support; 169 states the geometric derivative/localization premises.
4. [Actual inert q leaf](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-second-order-raw-closure/inputs/raw_engine.py.txt#L138): q_d is the constant mask difference times y_d/x_d. Hence it is pulled back from factor d. [First-order source](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-second-order-raw-closure/inputs/first-order-source.md#L181-L210) explains the pinned generator, distinct-coordinate jets and physical q dictionary.

Source snapshots are not duplicated here; use the exact pinned links above. These line references concern static source statements, not newly executed certificates.

## Literal factorization check

Put P=12, Q=34; D_P=V₁⊗V₂−V₂⊗V₁ and D_Q=V₃⊗V₄−V₄⊗V₃. The two factor ambients over k[s]/s² and k[t]/t² have products m_P(1+sD_P/2), m_Q(1+tD_Q/2), identity overlap maps, and units 1+s bP, 1+t bQ. Here bP=(15/4)q₁∪q₂ and bQ=(15/4)q₃∪q₄ in the short ordered representative.

On product affine charts their external tensor product is

    μ = m₀[1+sD_P/2+tD_Q/2+st D_PD_Q/4],
    F = id,
    A = (1+s bP)(1+t bQ)
      = 1+s bP+t bQ+st bP bQ.

These are exactly the supplied two-parameter coefficients reduced modulo (s²,t²): F=id+s²T_P+t²T_Q becomes id; the mixed product coefficient is m₀D_PD_Q/4. Every term of total degree at least three vanishes in R, so higher extension choices cannot change this result. On decomposable functions the multiplication is the tensor product of the two displayed factor multiplications; bilinearity then proves equality on affine product coordinate rings, with the same restriction maps. A later non-product refinement is restriction of this ambient, not a claim that its refined opens themselves are Cartesian products.

Importantly A is central **in this quotient**. For arbitrary f, the correction to (s bP)⋆f is s²μP(bP,f)+stμQ(bP,f)=0. The first term vanishes in R, the second by factor support; the analogous statement holds for t bQ. Every correction to (st bP bQ)f has degree at least three. Hence A⋆f=Af=f⋆A, including matrix-valued f by scalar identity multiplication. This does not assert bP or bQ themselves are star-central, nor centrality before imposing s²=t²=0.

The units' pentagon is their actual ordinary multiplicative cocycle identity, following from δbP=δbQ=0 and the two factor units, with the st term retained. Thus no undetected central coherence has been discarded. PR79's ordinary hT convention (PROOF.md:69) agrees with h⋆T after imposing the actual support; its generic warning remains valid without that support. With F=id this gives exactly the ten terms at lines 73–82. The source's subsequent trace projection and boundary addition are separate cochain operations, not changes of ambient product.

## Polarization identification: exact scope

An arbitrary one-parameter two-jet does not uniquely determine a two-parameter polarization. Diagonal substitution s=t=h is made on k[s,t]/(s,t)³ **before** the further quotient: it is not a ring map from R to k[h]/h³, since s²=0 would require h²=0.

There is nevertheless a useful uniqueness check. For a candidate fully deck-equivariant two-jet on the same literal cover/cochain presentation, give s character P and t character Q. Its s²,t² coefficient cochains have character zero, and its st coefficient has character P△Q. If its diagonal equals the pinned PR16 μ,F,A literally through h², projecting that quadratic coefficient onto P△Q recovers its st coefficient uniquely. Degree-one projection similarly recovers the s and t coefficients. Therefore its reduction to R is the displayed external product. This does not recover the two separate pure-square coefficients. It also does not apply to mere gauge equivalence, equality of characteristic evaluations, or an unspecified presentation. The PR79 mixed formulas provide direct additional source evidence, so the conclusion need not rest on an unproved claim that diagonal data alone specify polarization.

## Remaining hypotheses and next obligation

- The physical interpretation still imports the source's genuine product-factor derivations, commuting restrictions/localizations, valid leaf denotations and geometric frame/transition premises. Static inspection verifies the formulas and formal consequences; it does not re-execute these certificates.
- For root transport, supply the genuine product root line, factorized local unit lifts, and its full groupoid linearization/coherences. With those choices, [research/hm/null-root-morita-inertia/root-morita-0719/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/711c6bf8c6248f46d73661be8a42ede671a3712b/research/hm/null-root-morita-inertia/root-morita-0719/RESULT.md):143–176 now applies to this upstairs factorized ambient. Transported unary maps and units can have new st cross terms and must be retained.
- For descent, instantiate the actual quotient atlas, restriction-compatible equivariant overlap bimodules, compositions and residual inertia hypotheses required by [research/hm/null-strictification-gluing/invariant-gluing-0841/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/dcecef425c41063dc3ddc42f5285ee39c42e431e/research/hm/null-strictification-gluing/invariant-gluing-0841/RESULT.md):5–14 and 18–45. The abstract criterion is not those physical data.
- Identify the resulting invariant coefficient ideals, multiplication, overlap maps and actual central triple units with the proposed corrected model, through st and with compatible reduction. Equality of pure HKR classes or End bundles does not establish that identification.
- Even successful ambient identification and pure-module uniqueness do not produce a mixed module lift. No retained value or vanishing claim follows from ambient factorization.
