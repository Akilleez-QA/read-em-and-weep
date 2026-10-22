# 12. The explicit harmonic cochain and the two-gate coefficient reduction

**Current status.** The reductions below retain their stated scope. [Section 15](15-third-vanishing-and-fourth-frontier.md) now evaluates both actual cubic channels as zero; the two-dimensional space of allowed channels is not itself zero.

The trace-free family normal form in this chapter concerns the preceding uncorrected input. It must not be imposed on the corrected fourth source, whose parameter trace is forced nonzero. See [Chapter 16](16-canonical-fourth-input-and-complete-test.md).

## 12.1 What is now explicit

The global operator quotient and lower multiplication were identified in Section 10. The next accepted results give an explicit leading actual normal cochain and a smaller coefficient problem. They do not evaluate its cohomology class. The two-dimensional final cubic-gate space was already known; neither the new formula nor trace-free normalization removes one of its channels.

Fix the two standard charts of L=P(W), a global W′ basis, and the associated root-line frames. Write the local physical equation as q₀=νq, with q=xz−y². The corrected cone operator has the form

    O = H D_a + 𝒜,     H = k a h,
    𝒜 = [[b,c],[d,−b]],     P = [[1,0],[p,1]],

where P is the actual quintic-generator transition and p retains its base line factor. The displayed b,c,d are coefficients of the source connection 𝒜_i; the discrepancy K below is in the target j-frame. Let L_harm denote harmonic lift, and let ℬ denote the proved degree-dependent first product correction:

    L_harm(u)L_harm(v) = L_harm(uv)+q L_harm(ℬ(u,v)) mod q².

This ℬ is not the adjoint bundle B. The actual transport is 𝒜′=P𝒜P⁻¹−H(D_aP)P⁻¹. If its harmonic discrepancy is qK, then the [transition theorem][HT] gives

    K₁₂ = 0,                     K₁₁ = ℬ(p,c),
    K₂₁ = −2ℬ(p,b)+ℬ(p²,c)+ℬ(p,p)c+ℬ(H,D_ap),
    K₂₂ = −K₁₁.

In particular the term ℬ(p,p)c is essential: the ordinary square of a harmonic lift is not the harmonic lift of the square. Each ℬ uses its own input degrees.

For the target matrix N_j=[[f g_j,−f²],[g_j²,−f g_j]], with g_j=g_i+pf, the actual degree-eight square-ideal cochain in the physical equation frame is

    ν⁻¹ tr(N_jK)
      = ν⁻¹ {2f g_j ℬ(p,c)
          − f²[−2ℬ(p,b)+ℬ(p²,c)+ℬ(p,p)c+ℬ(H,D_ap)]}.

Using g_i instead of g_j in the trace would require the extra term 2pf²K₁₁; the source connection coefficients must not be changed silently to target coefficients. It is valued in P4 O_L(−4). Its class belongs to the twelve-dimensional lower quotient of Section 10.8; contraction by a gives the third-value target, with the fixed boundary sign and subsequent actual second-symbol quotient still retained.

## 12.2 Why this is the actual cochain, with all frame corrections retained

On a pure triangular overlap, the corrected Hessian primitive cancels the whole normal nilpotent discrepancy: if m is the Hessian covariance term, the actual primitives satisfy u_j−u_i=m. Thus L_harm(P) is an explicit reference transition preserving the corrected symbol to first normal order. This statement would fail for the bare, uncorrected Hessian formula.

After the established local normal conjugations, a difference from this reference transition centralizes N. Regularity of the pair f,g makes its tracefree centralizer the regular multiples of N, and such a discrepancy has zero trace pairing because N²=0. For a correction Q not yet proved centralizing, the scalar frame term cannot be dropped. In the ordinary local convention with H D_aN+[𝒜,N]=λN, its shadow is

    (λ − H r₀ − H D_a) tr(NQ),     r₀ = D_aq₀/q₀.

The global vector field's natural action on the physical equation does not imply r₀=0 in every local frame.

Diagonal generator changes and root-line scalars commute with harmonic lifting in this chosen presentation; their derivative and determinant compensators also lift exactly. Their harmonic discrepancies are therefore zero, not omitted. The physical ν⁻¹ remains. An additional regular cone stabilizer I+tN changes the weighted connection only in order at least twelve. Its first-normal discrepancy, paired with N, has cover order at least sixteen, so it cannot affect this degree-eight cochain. This is a degree bound, not an all-degree stabilizer cancellation or an identification with an arbitrary triangular extension. [Actual-frame comparison][HT].

## 12.3 The upper connection has a squared factor and one quartic map

The two entries needed above are fixed by the actual operator. Decompose uniquely

    H D_af = m f+n g,     c=−n,     b=Λ/2−m.

The uniqueness follows from coprimality and the absence of a degree-minus-one syzygy. Here Λ is the effective scalar in the chosen determinant/spinor frame, including its natural line-action correction. It must not be replaced silently by the global physical scalar. The Hessian primitive is no longer an additional unknown in the square-shadow formula. [Entry identification][HT].

On the actual smooth cubic support D, put κ=(d_Lf)/g, a section of O_D(−2,6). If ρ is the fixed nonzero normalization identifying a with its projective vector field, the [squared-factor theorem][UF] proves

    c = −kρ a² n_h,
    n_h = the unique polynomial extension of hκ to O_Y(2,6).

The extra a comes from the projective Hamiltonian action D_a(z)=2a(1,z) in a standard chart. The restriction kernel O_Y(−1,3) is acyclic, so the extension is unique. The actual map factors as

    D5 O_L → V O_L(2) → V O_L(6),
       kernel W′ O_L(−3)     second map M_κ.

Multiplication by the nonzero ramification section κ on the integral curve is generically invertible. Its equivariant Hom space is one-dimensional, so M_κ is the unique nonzero quartic channel up to its fixed scalar. Its determinant has degree twelve. The minimum orbit size forces its zero scheme to be one reduced twelve-point orbit, with rank two there and rank three elsewhere. These ranks describe M_κ after factoring a², not the additional zeros introduced by a chosen a². The diagonal term b and its effective scalar correction remain indispensable; the squared upper entry alone does not determine the cohomology class. [Section 13](13-canonical-diagonal-and-vector-cochain.md) now identifies the actual Gram composite, fixes that diagonal by the canonical residue inverse, and reduces the shadow to a vector cochain without evaluating its class.

## 12.4 Trace-free normalization does not eliminate a cubic gate

The identity D_(a²)=2aD_a makes the actual vector-field symbol, and therefore its Atiyah cocycle, factor through Sym⁴W=D5 rather than all of Sym²A=1⊕D5. The residue correction is linear in that symbol. Equivariant linear choices thus give a trace-free quadratic parameter representative. With its two corrected end actions fixed, the remaining zero-symbol ambiguity is a global scalar multiple of N; it extends using the actual midpoint lift and has zero normal obstruction. This is a normalization of actual operators, not a sheaf-splitting assumption. [Trace-free normal form][TF].

Its effect on the final gate must be kept separate. Let T:D5→P4⊗A be the unique nonzero equivariant D5 inclusion. With the invariant form on A, the family

    K_T(a,h) = a⊗⟨a,T(h)⟩ − ⟨a,a⟩T(h)

has zero contraction with a, but quadratic parameter trace −2T(h). Adding a suitable multiple removes any trace coefficient without changing the cubic output. Thus the five-dimensional trace-free reduced family still maps onto the same two-dimensional cubic-gate space, with a three-dimensional kernel. This trace-free normalization evaluates no actual coefficient and proves neither final channel zero on its own; the later evaluation is in Section 15.

## 12.5 The actual family kernel and exact coefficient reductions

Over P=P(A), let R⊂C be the intrinsic eighteen-dimensional common kernel from Section 10.8. The actual lower family C O_P→P4 O_P(1) is onto everywhere. Its kernel 𝒦 fits into

    0 → R O_P → 𝒦 → P4⊗Ω¹_P(1) → 0.

An equivariant linear splitting of C→C/R gives a bundle splitting, not a canonical one. Thus rank 𝒦=26, c₁(𝒦)=−4H and c₂(𝒦)=10H². The constant factor has underlying bundle 18 O_P; R is not eighteen copies of the trivial group representation. [Family theorem][FG].

Let Σ be the established length-twenty-four second-symbol degeneracy scheme. Pulling back its exact presentation

    0 → A O_P(−1) → P4 O_P(1) → I_Σ(7) → 0

along contraction gives the intrinsic sheaf kernel 𝒠 with

    0 → P4⊗Ω¹_P(1) → 𝒠 → A O_P(−1) → 0.

It splits as a bundle because H¹(Ω¹_P(2))=0. The later PR651 result makes this splitting uniquely equivariant relative to the actual second symbol, as detailed below; this does not make the distinct rank-twenty-six splitting above canonical. The bundle 𝒠 remains locally free at Σ, with c₁=−7H and c₂=25H². Its inclusion in the trivial twelve-bundle is not a subbundle at Σ: its fiber must not be replaced by the pointwise inverse image of a degenerate second-symbol fiber.

The vanishing H¹(𝒠(2))=0 proves surjectivity on the equivariant coefficient spaces. Their exact dimension reductions are

    general quadratic families:      11 → 6 → 2,   kernels 5 and 4;
    trace-free representatives:       9 → 5 → 2,   kernels 4 and 3.

In the six-space, three kernel coefficients are invisible already under contraction and one is removed by the second-symbol image. The kernel itself is canonical; PR651 below makes its three-plus-one division canonical in the equivariant category. The final two-space is the previously established cubic gate, not a new count. A nonzero reduced family can still lie in the kernel, and even a zero third gate would leave higher gates to examine.

## 12.6 Unique equivariant splitting and an exact no-obstruction normal form

Mr. Slop's [PR651][NF] strengthens the preceding family-kernel description. Differences of equivariant splittings of 𝒠 are measured by

    Hom_Γ(A, P4⊗H⁰(Ω¹_P(2)))
      = Hom_Γ(A, P4⊗Λ²A*) = 0,

since Λ²A*=A and P4⊗A=V⊕P4⊕D5, with V distinct from A. Thus the splitting of the rank-eleven sheaf kernel is uniquely equivariant for the given actual second symbol β.

It has an explicit lift. With β(a,b) quadratic in a and linear in b, put

    ℒ(a,b)(v) = ½ (d/dt)|_(t=0) β(a+tv,b).

Here b is held fixed before substituting any b=B_par(a,h). Euler's identity gives ℒ(a,b)(a)=β(a,b). This is not the total derivative of β(a,B_par(a,h)), and it retains β's actual nonzero scalar without selecting or evaluating it.

An equivariant quadratic lower family 𝓡(a,h) has identically zero third class exactly when it has the unique form

    𝓡(a,h)(v) = ℒ(a,B_par(a,h))(v)+S(a,h)(a,v),

where B_par∈A and S∈P4⊗Λ²A* are linear in a and h. Uniqueness of the skew term follows from the Koszul sequence: its only ambiguity is Hom_Γ(D5,P4⊗Λ³A*)=0. This is uniqueness for a whole equivariant polynomial family, not an isolated direction, a nonequivariant lift, or a chosen complement of 𝒠 in the trivial twelve-bundle.

The B_par channel is one-dimensional, represented by the second binary transvectant (a,h)₂; the skew part supplies three channels invisible under contraction. Their free scalars are not actual operator values. At a second-symbol fiber of rank r, the image of 𝒠 in the twelve-space has dimension 8+r, not necessarily eleven. The canonical bundle splitting therefore does not remove the earlier degeneracy qualification.

This normal form identifies precisely the four-dimensional ineffective subspace of the six-space. The two remaining allowed cubic coefficients were already known; this normal-form result evaluates or eliminates neither. Section 15 now proves both actual coefficients zero. Its application to the operator retains the corrected reduced-part subtraction of [Section 11.4](11-cubic-support-and-nilpotent-torsion.md#114-corrected-first-normal-extraction-equals-the-last-vertex-jet).

## 12.7 Conditional fixed-divisor classification for a nonzero third gate

Mr. Slop's [PR652][FD] classifies every **nonzero** equivariant third symbol in the established two-space. Its inputs include scheme-theoretic disjointness of the length-twenty-four second-symbol scheme Σ from the discriminant conic C=(δ=0). No nonzero actual third symbol is assumed.

If the symbol has nonzero restriction to C, it has no fixed divisor: the restricted system is basepoint-free, while every plane curve meets C. If its restriction vanishes, it is a nonzero multiple of δτ, where τ is the unique degree-seven primitive channel. The latter is basepoint-free on C. Otherwise its binary degree-fourteen components would have an invariant common factor of degree twelve, giving an impossible D5 injection into Sym²W. Thus the complete fixed divisor in this branch is exactly C with multiplicity one; there are no other failure curves.

After removing that divisor, let B_base be the finite base scheme of the primitive degree-d system, where d=9 or 7 respectively. It contains Σ scheme-theoretically, is disjoint from C, and satisfies

    24 ≤ length(B_base) ≤ d²−d−2,
    length(B_base) ≤ 70 or 40,
    length(I_Σ/I_(B_base)) ≤ 46 or 16.

The last bounds are excess lengths, including additional thickness at Σ, not lengths of a claimed disjoint residual subscheme. The original image ideal in the discriminant-divisible branch is δ I_(B_base).

For the bound, two general primitive sections form a degree-(d,d) complete intersection. Residual duality and the five independent sections force its residual scheme to have length at least d+2. Equality at the preceding bound d+1 would force that residual scheme into a line; both degree-d equations would then contain the line, contradicting their choice with no common component. This argument retains nonreduced finite schemes. The primitive evaluation kernel is locally free of rank four, with c₁=−dH and c₂=d²−length(B_base), but its inclusion is not a subbundle at basepoints.

For the actual third gate, this nonvanishing antecedent is now excluded by [Section 15](15-third-vanishing-and-fourth-frontier.md). The classification remains valid for nonzero elements of the allowed equivariant space, not for an actual constructed failure locus. At points of Σ the target is an ideal sheaf, not a line bundle; no fiber rank is inferred there. The theorem neither evaluates either coefficient nor resolves the four-versus-five alternative.

## 12.8 Remaining task and evidence

The actual leading cochain, squared upper factor, exact coefficient reductions and conditional fixed-divisor classification are now available. Section 13 gives the canonical diagonal and vector representative. The formerly unresolved final class is now proved zero in [Section 15](15-third-vanishing-and-fourth-frontier.md), retaining cancellation with the diagonal and scalar terms and the actual second-symbol quotient. The remaining task is fourth and later order, not the third residue sum. The nonzero quintic extension, nonzero quartic map and surjective lower multiplication do not supply that evaluation.

The published sources below have independent geometric and actual-frame audits, with universal verifiers for identities, characters and degree arithmetic. They do not use selected HM coefficients or actual-instance rank evaluations and are not proof-assistant certificates. Generic SF ≥ 3, square rank ≥ 27 and the four-or-five section theorem remain unchanged; the separate formal-type frontier is updated in Section 4.13.

## Pinned source references

[HT]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ebc38deccf2d0abcdd7b185c73dd57bae8682f59/research/hm/order-four-quadratic-load/ACTUAL-NORMAL-OPERATOR-SQUARE-SHADOW-BY-HARMONIC-TRANSITION.md
[UF]: https://github.com/Akilleez-QA/read-em-and-weep/blob/d7a6ad65f2142d39fbacc01784b7620fc3a9e42c/research/hm/order-four-quadratic-load/ACTUAL-CONE-UPPER-CONNECTION-HAS-A-SQUARED-FACTOR.md
[TF]: https://github.com/Akilleez-QA/read-em-and-weep/blob/d7a6ad65f2142d39fbacc01784b7620fc3a9e42c/research/hm/order-four-quadratic-load/ACTUAL-QUADRATIC-OPERATOR-HAS-A-TRACE-FREE-NORMAL-FORM.md
[FG]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ebc38deccf2d0abcdd7b185c73dd57bae8682f59/research/hm/order-four-quadratic-load/ACTUAL-LOWER-MAP-FAMILY-KERNEL-AND-SIX-TO-TWO-GATE.md

[NF]: https://github.com/Akilleez-QA/read-em-and-weep/blob/b19ee9b0c995c037b37bfe6e71a51f95847cac11/research/hm/negative-sector-operator/PROOF.md

[FD]: https://github.com/Akilleez-QA/read-em-and-weep/blob/be1ee19ed15918d6907aa01bbadb25d738b3a3f1/research/hm/third-symbol-fixed-divisors/PROOF.md
