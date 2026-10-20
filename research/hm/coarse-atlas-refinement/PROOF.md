# Explicit central descent, its gerbe sign, and derived reduction compatibility

## Result and scope

For the stipulated algebraic differential pair ambient and its independent two-pair external product modulo (s²,t²), the effective invariant affine Morita atlas is already established in [PR130](https://github.com/Akilleez-QA/read-em-and-weep/blob/d8d4a4a096431ad1506b0b847b72b0aeeeceda7f/research/hm/null-effective-atlas/RESULT.md). We do not claim that existence theorem as new. This refinement supplies an explicit central-cochain presentation, fixes the direction and sign of the resulting gerbe, and verifies the invariant-frame and coefficient-reduction hypotheses needed by the bounded joint algebra–module equation model.

The derived-reduction lemma in §6 connects the positive geometric construction to the negative synthetic ramification test: on the actual invariant-frame category, the natural derived reduction comparison is an isomorphism, without assuming that the cover algebra is flat over its invariant algebra. This is not true on arbitrary equivariant modules, as the separately proved sign-character example shows.

No global module is produced, no module obstruction is evaluated, and no same-pair second order or all-order conclusion follows. Claims about what these results establish should not be read as a current status report on other work.

## 1. Exact public premises and conventions

Work over C. Let C be y²=x³−x with origin O at infinity, X=C² and G=(Z/2)²⋊S₂. The map p:X→Y=P² is the quotient through (P¹)²→Sym²(P¹). It is finite with geometric orbit fibers. The root N=O_C(O)⊠O_C(O), its genuine group action, square N²=p*O(1), and frames 1,y/x are established in [PR126, classical root §§2–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/classical-root/RESULT.md). Their group-arrow frame multipliers are constants ±1.

The actual algebraic differential external product, not a product of unrelated completed stalks, is stipulated in [PR126, factorization](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/physical-factorization/RESULT.md). Its geometric derivative, localization and leaf interpretations remain source premises. The exact ordered-to-antisymmetric gauge and strict pair action are [PR127, §§1–5](https://github.com/Akilleez-QA/read-em-and-weep/blob/0050df8fa957b9f7f5e1b21137c63bffc646a1eb/research/hm/null-pair-swap-coherence/RESULT.md). The pure parameter ε has character χ(g)=product of inversion signs times pair permutation sign.

Use the two inversion-stable affine root opens W₀=C\{O} and W₁=C\{(0,0),(1,0),(−1,0)}, their four pair products, and the full ordered Čech nerve: G transports labels without sorting tuple positions. For the three standard quotient affines U_a, put V_a=p⁻¹U_a. All finite intersections V_A are affine and G-stable. Intersections of the root cover with V_A are affine, since X is separated. Consequently the resulting finite Čech complexes compute cohomology of quasi-coherent layers on V_A and are exact in positive degrees. Averaging preserves their differentials.

Pure root transport uses star inverses and the inverse-gauge convention. If e_j=ℓ_ij e_i, then

    F^N_ij=Ad_star(ℓ_ij⁻¹),
    C^N_ijk=ℓ_ij⁻¹ star ℓ_jk⁻¹ star (1+ε b̄_ijk) star ℓ_ik.

The exact composition convention is F^N_ij F^N_jk=Ad(C^N_ijk)F^N_ik.

## 2. An upstairs global algebra with a retained central gerbe

The classical ℓ are an actual line cocycle, so C^N=1+c with c in I=εO_X. Every such element is central at pure order: any correction to multiplying εf is divisible by ε²=0. Thus Ad(C^N)=id and the F^N are an ordinary exact algebra-gluing cocycle. They glue a global sheaf algebra D^N with

    I²=0,   I central,   D^N/I=O_X.

No central embedding O_X→D^N or global additive splitting is asserted. Conjugation is identity on the ideal and classical reduction. Because the root-frame group multipliers are constants ±1, they are star-central; their ratios cancel from both F^N and C^N. Hence the strict signed action glues on D^N. The algebroid pentagon is exactly δc=0 in the weighted G-equivariant sheaf I.

The algebroid has therefore not been replaced by the globally neutral module category of D^N: its possibly nonzero central gerbe c remains part of its data.

## 3. Actual regular cochains and the same-sign gerbe comparison

On V_a choose a regular cochain β^a with δ_iβ^a=c. This exists by affine Čech exactness, not formal completion. Average it to be G-invariant. The central units Q^a=1+β^a have δ×Q^a=C^N. The inverse-convention gauge by Q^a leaves F^N unchanged and sends the triple unit to 1.

A denominator-clearing realization is available on any finite principal refinement D(f_l) of an affine Spec R. Choose N so all f_l^N c_lij extend to D(f_i f_j), and choose a_l with Σ a_l f_l^N=1. Then β_ij=Σ a_l f_l^N c_lij has δβ=c. There are finitely many sections, so a common N exists; the unit-ideal identity follows because the principal opens cover. A translated refinement and averaging make the construction equivariant. The cohomological argument already supplies β on the original affine-intersection cover, so no synchronization of formal refinements is needed.

Fix overlap orientation by P_ab tensor M_b→M_a. Since T^a=(Q^a)⁻¹T^orig, its transition factor is Q^b/Q^a, not its inverse. Put

    d^ab=β^b−β^a,     L^ab_ij=1+d^ab_ij.

The actual regular (D^N,D^N)-bimodule P_ab has section equation

    p_i=L^ab_ij F^N_ij(p_j).

The identity δ_i d^ab=0 proves its exact gluing. Its reduction is canonically O_X with ordinary action; its classical inertia is therefore trivial on every branch stratum. Its inverse is P_ba, and I P_ab is canonically I. Multiplication gives associative, equivariant maps P_ab tensor P_bc→P_ac because L^ab L^bc=L^ac.

On V_ab choose invariant regular zero-cochains ℓ^ab satisfying

    ℓ^ab_i−ℓ^ab_j=d^ab_ij.

Again H¹=0 and averaging supply them. Then e^ab_i=1+ℓ^ab_i is a global invariant generator of P_ab, a central local unit in every root chart. Choose ℓ^aa=0 and ℓ^ba=−ℓ^ab.

Let A=(p_*D^N)^G and J=(p_*I)^G. On quotient affines, H¹(V,I)=0 and averaging prove that A→O_Y is surjective. Thus 0→J→A→O_Y→0 is an exact square-zero extension. The invariant overlaps Q_ab=(p_*P_ab)^G are A e_ab. Their composition coefficient is

    k_abc=1+γ_abc,
    γ_abc=ℓ^ab_i+ℓ^bc_i−ℓ^ac_i ∈ J(U_abc).

The expression is independent of root index i since d^ab+d^bc=d^ac. Cancellation proves γ_abc+γ_acd=γ_bcd+γ_abd. Since J²=0, this is the exact multiplicative quadruple coherence, not just its first-order approximation.

The sign of its class can be checked in the double Čech complex. With quotient degree p and D=δ_a+(−1)^pδ_i, the cochains have δ_iβ=c, δ_aβ=d, δ_iℓ=−d and δ_aℓ=γ. Hence

    Dβ=d+c,   Dℓ=γ+d,   c+Dℓ−Dβ=γ.

The downstairs gerbe is the original class under the natural cohomology identification, not its negative. This is the explicit orientation-sensitive refinement of the already public effective-atlas construction. Gluing module stacks with these actual overlaps and compositions supplies its ordinary Zariski effectiveness; a global generator is neither asserted nor needed.

## 4. Coefficient marking and the exact mixed ideal

The volume character, unlike root fiber inertia, is χ. Multiplication εf↦fΩ identifies I with ω_X after fixing Ω. The normalized invariant canonical descent is already proved through all ramification in [PR128, §§1–3](https://github.com/Akilleez-QA/read-em-and-weep/blob/64b6c62a23db6189186896285c956133608ad3c7/research/hm/null-invariant-coefficient-ideal/RESULT.md): J≅ω_Y=O(-3). Its form-descent convention is inverse pullback, equivalently (1/8)Tr_p. The unnormalized duality trace is eight times this map. We use the same marking; the bare character alone does not choose its scalar.

Apply §§1–3 independently to the z and h pairs. On each of the nine quotient product affines, use the prescribed algebraic differential external product, with its localization data on arbitrary opens. The section tensor identity follows on the finite product root cover: a glued section satisfies the two degree-zero Čech kernel conditions, and tensoring vector spaces over C preserves those kernels. Thus

    Γ(V_z×V_h,D_mix)=Γ(V_z,D_z) tensor_C Γ(V_h,D_h).

The same argument applies to the overlap bimodules and coefficient submodules. Product Reynolds is the tensor of the two Reynolds projectors. Therefore on the actual chosen affine atlas, compatibly with its restrictions and full compositions,

    A_mix=A_z external A_h,    Q_mix=Q_z external Q_h.

This is not an assertion that rectangles form a basis of the entire algebraic product topology or that arbitrary invariant balanced tensors commute.

For the stable pure ideals downstairs put

    i=J_z external A_h,    j=A_z external J_h.

Over the field C, choose vector-space complements to the two J on each affine section space. The four tensor summands show directly that

    i intersection j=ij=ji=k=J_z external J_h=O(-3,-3),
    i²=j²=0,    (i+j)k=k(i+j)=0.

Products span the indicated mixed tensor: j_z tensor j_h=(j_z tensor 1)(1 tensor j_h). These identifications commute with restrictions and the actual overlaps, so they are sheaf-ideal identities, independent of the auxiliary complements. In particular

    0→k→A_mix→(A_mix/i) ×_(A_mix/(i+j)) (A_mix/j)→0

is exact. The two-axis fiber product is A_mix/k, not A_mix. The pure ideals i,j are not themselves line bundles: their pure quotients are O(-3,0), O(0,-3), and their common mixed layer is k. The full product of the factor triple units retains its mixed term. These are the concrete hypotheses of [PR235, §§4–6](https://github.com/Akilleez-QA/read-em-and-weep/blob/01247d95275c87f7b35a121a3a67f4d96375c41c/research/hm/relative-models/external-morita-descent/PROOF.md), now instantiated rather than left as unspecified atlas inputs.

## 5. Supplied modules: quotient-open frames and all coefficient reductions

Take a supplied finite locally free D-module with a strict compatible G-action and trivial classical inertia, where D is a pure D^N or the mixed product chart. The nilpotent ideal K has quasi-coherent O_X-layers: pure K²=0; mixed K³=0 with two pure degree-one layers and one mixed degree-two layer. This verifies [PR232, Theorem 2B](https://github.com/Akilleez-QA/read-em-and-weep/blob/6920f9061a2366cdd649c350ee9b8855eab48b3d/research/hm/relative-models/global-equivariant-module-descent/PROOF.md).

For clarity, its actual frame argument is short. Classical trivial-inertia descent gives an invariant frame of M/KM over the inverse image of a sufficiently small affine quotient open. The sheaf KM has a finite filtration with quasi-coherent layers, so H¹(KM)=0 there. Lift the frame and average. In any existing local D-frame its coefficient matrix is invertible modulo K, hence invertible by nilpotence. This gives an invariant D-frame over the entire quotient-open inverse image, not an unrelated collection of completed-stalk frames.

In that frame N=(p_*M)^G=A^r. Frame changes and equivariant morphisms have coefficients in A, proving full faithfulness and gluing. Conversely extension of A^r supplies the invariant frame. The invariant overlap generators of §3 make the local equivalences commute with the actual balanced compositions, so the equivalences glue for the algebroid module problem.

Every relevant coefficient ideal I (pure, mixed or sum) has the finite quasi-coherent filtration just exhibited. Therefore p_*D→p_*(D/I) is surjective on an affine basis and, with J_I=(p_*I)^G, (p_*(D/I))^G=A/J_I. In invariant frames,

    (p_*(IM))^G=J_I N,
    (p_*(M/IM))^G=N/J_I N.

This also applies to modules that are not external products. The construction assumes a supplied module with the stated action. It does not equip an unknown deformation with an action or produce a module lift of the designated carrier.

## 6. Derived comparison lemma: positive closure and sharp exclusion

Keep the setting of §5 and a stable ideal I with its verified section-surjectivity. For a finite locally free strict equivariant D-module M with trivial classical inertia, let N=(p_*M)^G and J_I=(p_*I)^G. There is a natural comparison from invariant reduction to cover reduction,

    α_M: (A/J_I) tensor_A^L N
           → (p_*((D/I) tensor_D^L M))^G.             (D)

This is a sheaf-local assertion; the right side is computed using the free D-module M, so its derived reduction is concentrated in degree zero. No assertion about exact pushforward of arbitrary noncentral modules is needed.

**Lemma.** The map (D) is a quasi-isomorphism, is concentrated in degree zero on both sides, and is compatible with the pure, mixed and sum coefficient reductions and the atlas compositions.

**Proof.** On a quotient-open invariant frame M=D^r and N=A^r. The left side is (A/J_I)^r. The right side is ((p_*(D/I))^G)^r=(A/J_I)^r. The natural map sends each basis vector to itself, hence is the identity in these coordinates. It commutes with changes of invariant frame because those matrices have entries in A; it therefore glues. The same coefficientwise calculation commutes with nested ideal quotients, the invariant overlap generators and their composition coefficients. This proves all assertions. No flatness of D over A was used. ∎

This is exactly why the sign-character obstruction does not reopen the effective atlas. Its internal comparisons have canonical trivial classical inertia; the supplied modules in §5 expressly satisfy the same condition. In contrast the [ordinary ramification guard](https://github.com/Akilleez-QA/read-em-and-weep/blob/2c387062518fec4044568fe638760343b87cc25f/research/hm/null-ramification-guard/ramified-descent-0644/RESULT.md) has negative inertia, so it lies outside this frame category. Its invariant module P has positive Tor equal to R/(x) in every degree, and the full derived-comparison fiber is computed in the companion derived-ramification proof. Derived reduction records that failure rather than repairing it.

## 7. Exact contribution to the bounded joint model

This establishes the effective geometric atlas, the retained nilpotent coefficient square, the actual invariant overlaps, their same-sign gerbe, and reduction-compatible supplied-module transport under the explicit algebraic source premises. These are the geometric inputs needed before writing the joint equations in affine frames.

It does not by itself identify an independently chosen mixed ambient. The full pair comparison is already [PR131, §§2–6](https://github.com/Akilleez-QA/read-em-and-weep/blob/1c5ccbd7e2e5e1532fdcdd13ba4734ab65247252/research/hm/null-actual-pair-comparison/RESULT.md): its chart and arrow gauges identify the full pair with the explicit corrected presentation, preserving reduction and the normalized band, rather than merely its characteristic image. Tensoring those exact pair equivalences identifies the stipulated external product with the external product of that corrected presentation and retains all mixed units. It does not identify a separately chosen nonexternal mixed correction or a frozen module two-jet.

Accordingly the geometric atlas dependency is closed. A broader joint-model specialization must still bind its exact marked corrected model, complete prescribed pure boundary, ambient source residual and obstruction-band comparison. Those are separate inputs, not consequences of the synthetic Tor calculation or of affine atlas existence. No unconditional closure of those additional dependencies is claimed here.
