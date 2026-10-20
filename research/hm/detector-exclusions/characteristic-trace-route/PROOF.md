# Ordinary characteristic traces cannot detect the retained obstruction

## Scope and result

This is a formal cohomological calculation for the established carrier E=N⊗f*H on X=C^4, in characteristic zero. The source-bound first-lift identities and mixed-class identification are imported from FIRST-LIFT-STRUCTURAL §§5–8 and MIXED-GAUGE-DESCENT §§1–2 in the mathematical inputs cited below.

The proposed scalar characteristic test

  ι_pι_q ch₄(E) − 2 [(ι_p ch₂(E))/2][(ι_q ch₂(E))/2]

is identically zero. This is a rank-two Chern-class and product-cohomology identity, not a computation of the mixed obstruction. The actual source gerbes bind to the NEGATIVE of the displayed first scalar characteristic classes in the stated Atiyah convention. This sign does not change their mixed product.

There is a useful strict limit to this exclusion: ordinary trace of the actual trace-free obstruction is zero, and its higher Atiyah-trace maps with k≥2 vanish by dimension or character. The k=1 Atiyah-trace target survives the deck-character test alone, but two additional established symmetries exclude it: it contains no S₄ type [22], and inversion acts negatively on its entirety. Consequently all these ordinary Atiyah-trace maps vanish on the retained [22] sector, and also on the actual inversion-positive mixed class under the imported source-transport premises. The naive scalar expression is not asserted to be a categorical necessary condition.

## 1. Cohomology and conventions

Let n_i be the pullback of c₁(O_C(O)) from factor i, n=Σ_i n_i=c₁(N), and η_i=ι_{V_i}n_i∈H¹(X,O_X). Use the ordinary cup product with exterior multiplication of forms to represent classes in H^a(Ω^b). In particular n_i²=0 and the n_i commute, whereas the η_i anticommute. Normalize pair contraction by ι_(a,b)=ι_{V_b}ι_{V_a}. On the ordered exterior form directions 0,1,2,3, disjoint pair contractions commute and their composite has positive sign.

Thus

  ι_(a,b)(n²)=2η_aη_b,
  ι_pι_q(n⁴)=24η₀η₁η₂η₃,

where p=(0,1), q=(2,3). These follow by expanding abstract cohomology classes; no coordinate values are involved.

## 2. Chern identities and cancellation

The established normalization is c₁(H)=−h, c₂(H)=4h², f*h=2n. Twisting a rank-two bundle F by N gives c₁(F⊗N)=c₁(F)+2n and c₂(F⊗N)=c₂(F)+nc₁(F)+n². Therefore

  c₁(E)=0,  c₂(E)=16n²−2n²+n²=15n².

The formal Chern roots ±x of a rank-two determinant-trivial bundle give ch₂=−c₂ and ch₄=c₂²/12. Hence

  ch₂(E)=−15n²,  ch₄(E)=75n⁴/4.

Put β_r=(ι_r ch₂)/2. Then β_p=−15η₀η₁, β_q=−15η₂η₃, and

  ι_pι_q ch₄=450η₀η₁η₂η₃=2β_pβ_q.

Equivalently, ι_pι_q ch₄=(ι_p ch₂)(ι_q ch₂)/2. No nonzero scalar detector can be extracted from this difference. This is only an exclusion of this specific characteristic expression; its vanishing implies neither exactness nor nonvanishing of any End(E)-valued obstruction.

## 3. Bind the source gerbe, rather than assume its normalization

Write A^E for the source's column-frame connection-difference Čech representative. Declare the Atiyah-class convention in which ch₂(E)=½[tr(A^E∧A^E)]. Reversing the sign of the Atiyah class itself does not change this formula. The source proves

  C_r=g_ik^−1 μ_r(g_jk,g_ij),
  ι_r tr(A^E∧A^E)=−2 tr(C_r),
  δs_raw,r=b_r−tr(C_r)/2.

Consequently, in cohomology,

  [b_r]=[tr(C_r)]/2=−¼ι_r[tr(A^E∧A^E)]
       =−(ι_r ch₂(E))/2=−β_r.

This is a binding obtained from the actual source identities, not an identification of unrelated scalar classes. Thus the same formal cancellation can be written

  ι_pι_q ch₄(E)−2[b_p][b_q]=0.

It is a statement about cohomology classes, not equality of raw Čech cochains. In particular the raw b_p b_q term at one triple in the source curvature is not thereby identified with the cup product in H⁴(O_X): those have different Čech degrees. The mixed curvature M is an End-valued Čech 2-cocycle, and its trace-free projection is bound to the actual R only by [R]=tf([M]). No map from that actual obstruction to this characteristic polynomial is proved here.

For a check on normalization, the source uses q_d=2θ(V_d), b_(a,b)=15q_a∪q_b/4 and the old line connection difference −θ. Thus n=[−θ] in this convention, η_d=−[q_d]/2, and [b_r]=15η_aη_b, agreeing with the equation above.

## 4. What the ordinary Atiyah-trace maps could still see

For a trace-free class z∈H²(X,End₀(E)), define the usual algebraically well-defined maps

  τ_k(z)=tr(z∪At(E)^k)/k! ∈ H^(k+2)(X,Ω_X^k).

These are maps of ordinary cohomology, with a fixed consistent cup/sign convention. No theorem asserting that these expressions are necessary conditions for this noncommutative gerbe deformation is assumed.

The deck group is (Z/2)^4. E has its established deck linearization, so its Atiyah class and each τ_k are equivariant. Each factor inversion acts by −1 on its holomorphic one-form and on H¹(O_C). The actual source class has full-sign character χ_all by the established mixed-character purity theorem. On X,

  H^a(Ω_X^b) ≅ Λ^a H¹(O_X) ⊗ Λ^b H⁰(Ω_X¹).

A basis term indexed by subsets A,B has deck character χ_(A symmetric-difference B).

For k=0, τ₀(z)=tr(z)=0 by trace-freeness.
For k=2, the target is H⁴(Ω²), whose characters are χ_(all symmetric-difference B)=χ_(B-complement) with |B|=2. None is χ_all. Thus τ₂(z)=0 for every full-sign z.
For k≥3, H^(k+2)(Ω^k)=0 because dim X=4.
For k=1, H³(Ω¹)_χ_all has dimension FOUR: choose B={j} and A=all\{j}. Therefore character and dimension do not force τ₁(z) to vanish.

This rigorously rules out all the ordinary τ_k except τ₁ as detectors of this full-sign trace-free class. The surviving τ₁ requires actual Atiyah–obstruction cup-product information or a separately justified structural identity. Chern classes alone supply neither. Contracting a zero τ_k cannot restore information. The next section resolves the remaining τ₁ map on the sectors relevant to this task by additional symmetries.

## 5. The surviving map is also blind to the remaining obstruction

### 5.1 Entire retained [22] sector

At the original symmetric coefficient tuple, E has its natural S₄ factor-permutation linearization: N is the external tensor product of four identical lines and f is symmetric. Thus At(E) and τ₁ are S₄-equivariant. Let W be the four-dimensional permutation representation. The full-sign part of H³(Ω¹) is the diagonal complementary-index subspace of Λ³W⊗W. Since Λ³W≅sgn⊗W*, its complementary-index basis transforms as sgn times the permutation representation. Therefore

  H³(Ω¹)_χ_all ≅ sgn⊗W ≅ [1111] ⊕ [211].

Explicitly choose η_[omit j]⊗ω_j and multiply by (−1)^j; these four basis elements are permuted with the common factor sgn(σ). There is no [22] summand. Complete reducibility in characteristic zero now gives

  τ₁|_(H²(End₀ E)_χ_all,[22]) = 0.

Together with §4, EVERY τ_k vanishes on this entire [22]-isotypic component. The established retained-sector theorem identifies the D₈-epsilon sign-kernel with [22]_epsilon⊗M. Therefore this theorem annihilates the whole retained 30-dimensional space, its 12-dimensional inversion-positive subspace, and indeed the entire 60-dimensional [22]-isotypic component. These dimensions are quoted from the audited inversion-eigenspace theorem, not computed anew here. Application to the actual retained source class keeps that theorem's explicit source-membership/comparison premises.

### 5.2 Alternative: actual inversion-positive class, without S₄ membership

Work over C or after extending the ground field to contain i; vanishing descends by faithful field extension. The audited projective-inversion theorem gives a*E≅E⊗Q with Q²≅O_X. In characteristic zero At(Q)=0: the tensor-square identity gives 2At(Q)=At(O)=0. Naturality and the tensor-product formula for Atiyah classes therefore identify a*At(E) with At(E) under the induced End isomorphism. Consequently every τ_k is equivariant for this projective, line-twisted inversion; no ordinary E≅a*E lift is being assumed.

On each elliptic factor a*ω=iω for ω=dx/y. Equivariant Serre duality on the curve gives a* on H¹(O_C) equal to i^(-1)=−i (translation contributes no change). Thus on the entire H³(Ω¹) of the product, a acts as

  (−i)³·i = −1.

The actual weighted-root-gerbe transport theorem proves a*[R]=[R], under its named source identity premises. Equivariance then forces τ₁([R])=−τ₁([R]), hence τ₁([R])=0. In fact, for every nonzero target H^(k+2)(Ω^k), the same product argument gives eigenvalue (−i)^(k+2)i^k=−1. Inversion alone therefore annihilates this whole trace family on every inversion-positive class. This excludes τ₁ on the actual full-sign class even without using D₈ membership or sign-kernel identification. The result does not assert that R itself vanishes: it says the ordinary Atiyah-trace family cannot detect it.

These are pure representation-theoretic annihilation statements for genuine cohomology maps, so no categorical necessity theorem is needed. They do not identify any historical scalar selector or jet detector with a τ_k. More refined noncommutative characteristic maps are not covered.

## 6. Inputs and boundary

Mathematical inputs (immutable bindings are in DEPENDENCIES.md):
- `dependencies/relative-mixed-character-purity/dependencies/FIRST-LIFT-STRUCTURAL.md`
- `dependencies/pair-character-vanishing/MIXED-GAUGE-DESCENT.md`
- `dependencies/pair-character-vanishing/PROOF.md`
- `dependencies/relative-mixed-character-purity/PROOF.md`, §§1–4
- `dependencies/inversion-eigenspaces/PROOF.md`, §§1,4–7, and `dependencies/inversion-eigenspaces/AUDIT.md`
- `dependencies/retained-sector-structural/PROOF.md` and `dependencies/retained-sector-structural/SOURCE-BINDING-ADDENDUM.md`
- `dependencies/inversion-projective-lift/PROOF.md` and `dependencies/inversion-projective-lift/ROOT-GERBE-TRANSPORT.md`

The carrier's Chern data and full-sign purity are established inputs to this bounded task. The proof above does not recompute them from any source/model instance. No categorical quantization or semiregularity theorem is invoked: importing one without matching its deformation functor, scalar-gerbe normalization, degree, and signs would not justify turning the polynomial identity into a necessary condition on R. This note excludes the proposed scalar expression and the specified ordinary trace maps only; it does not exclude every possible characteristic-class or noncommutative cyclic-homology method.
