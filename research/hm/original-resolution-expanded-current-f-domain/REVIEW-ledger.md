Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

# Static audit: expanded current–F correction domain

## Verdict

The proposed occurrence vectors and the uniform bounds **C ≤ 14/8** and **QC ≤ 35/17** are valid under the imported all-chart hypotheses. Under the same physical-frame, regular-selector, character-projection, normality and full ordinary comparison premises as `null-overlap-homotopy-DOMAIN.md`, the fully compared selected coefficient **ΠQC is separately regular**. This assertion needs neither δs = F nor closure of C. It does not identify QC as a boundary or show that its pairing vanishes.

### Final-proof binding, 2026-10-18

I independently reread the final `PROOF.md` and verified its SHA256:

    65bbab34799fb1d3ef6b59b77793711e1b9a790029f18fa073f5cd9fba604a63

The affirmative ledger/Q verdict above applies to those exact bytes, especially sections 1–4. The final proof explicitly retains the physical-frame, determinant-normalization, character and all-input-degree first-face premises required by this review. Its λ = 2 fallback vector is also correct and is appropriately kept separate from the λ = 1 conclusion.

I also read the added prism section 5 against the pinned `dependencies/prism-domain.md`, section 5. No conflicting degree, occurrence, bound or character statement was found: two ambient differences give degree five on six occurrences; j and two H factors add 16/8, giving 30/16; the q = 5 prism has five ordinary weights plus one differentiated weight; and 54/29 and 53/28 respectively dominate 30/16. The missing-axis/internal-degree-minus-two typing agrees with the prism dependency. This consistency check supplements, and does not replace, the separate all-degree prism audit. No additional issue was found elsewhere in the final proof.

Here C denotes the current–F cochain below, not the differently named overlap insertion operator in `null-overlap-homotopy-PROOF.md`. The notation Π includes the intended full source-to-standard comparison; if character extraction is denoted separately, perform that extraction in the invariantly cleared finite-flat algebra before the comparison.

## 1. Literal occurrence calculation

Use the ordered original occurrences (i,j,k,l), with no merging of equal labels or equal divisors. The pair of vectors means carrier/legal clearance, with one legal allowance for each of the four legal factors at an occurrence. Product charges add at each occurrence; only sums take coordinatewise maxima.

At λ = 1, g and its implemented rank-two adjugate have 2/1 at each endpoint, while Vg has 3/2. Hence θ = g⁻¹Vg has 5/3 at each endpoint. No inverse cancellation or trace cancellation is used in this estimate.

Write M_ijk = tr(g_ik⁻¹ μ(g_jk,g_ij))/2, so F_ijk = b_ijk − M_ijk. Each expanded alternating μ summand has one differentiated factor on each edge. Thus

- M_ijk: carrier (5,6,5), legal (3,4,3).
- b_ijk: carrier (0,0,0), legal (1,2,1).
- F_ijk: carrier (5,6,5), legal (3,4,3).

For the exact row-valued expression

    C_ijkl = θ_ij F_jkl + F_ijk g_ik⁻¹ θ_kl g_ik,

the fully separated bounds are:

| Literal family | Carrier on (i,j,k,l) | Legal on (i,j,k,l) |
|---|---|---|
| θ_ij b_jkl | (5,5,0,0) | (3,4,2,1) |
| θ_ij M_jkl | (5,10,6,5) | (3,6,4,3) |
| b_ijk g_ik⁻¹ θ_kl g_ik | (4,0,9,5) | (3,2,6,3) |
| M_ijk g_ik⁻¹ θ_kl g_ik | (9,6,14,5) | (5,4,8,3) |

Every alternating summand in either M has the displayed bound. Consequently the first whole cup term has (5,10,6,5)/(3,6,4,3), and the second has (9,6,14,5)/(5,4,8,3). Their sum has

    carrier (9,10,14,5), legal (5,6,8,3),

and therefore uniform bound 14/8. In the second term the two g_ik factors are both retained: together they add (4,0,4,0)/(2,0,2,0). In particular the k carrier charge is 5 + 2 + 5 + 2 = 14, and its legal charge is 3 + 1 + 3 + 1 = 8.

F is a scalar, whereas θ is a trace-free row endomorphism in its first endpoint frame. The first term therefore needs no extra matrix transport of F. The second term uses exactly g_ik⁻¹ θ_kl g_ik to put θ_kl in the same i frame. This proves compatible typing; scalar multiplication and this transport preserve trace-freeness under the imported frame identifications. It does not justify replacing g_ik by a product of other edges.

## 2. Q and the degree

The imported Q = LHRj has Čech degree +1 and kernel bound 21/9. Its first-face insertion and pointwise H, j and regular L introduce no differentiation of the input and no degree-dependent pole increment. Applying its same kernel to this degree-three input gives a degree-four cochain on five original occurrences, with

    QC ≤ (21+14)/(9+8) = 35/17.

For comparison, the older degree-two input Z gives QZ of degree three. These are different cochain degrees. Padding the kernel bound to all five occurrences gives, if desired, the conservative position-specific vectors (21,30,31,35,26)/(9,14,15,17,12), by embedding the C vector in the four tail positions. No sharpness claim is made for that padding.

## 3. Qualifications needed for separate regularity

1. **All-chart denotation.** Use the accepted homogeneous carrier/legal bounds and actual fixed physical quotient frames, the same globally interpreted invariant derivation, and the actual scalar b and normalized μ. Arithmetic on one affine chart alone would not establish the theorem. In those frames g, θ and F agree under standard-representation changes, so C is a meromorphic row cochain of the required type.
2. **Representation and character.** The imported H and Xi laws each supply one inverse representation factor, so Q applied to representation-invariant C has the same τ⁻² law as the domain theorem. With its regular selector, the full-sign coefficient has the assigned O(−4,−4,−4,−4) law. For the actual complementary-direction correction, θ_b has character e_b, F_q has character q, conjugation by g contributes zero character, and the Q_a insertion contributes e_a. Thus e_a+e_b+q is the full character. If directions are left unspecified, do not claim purity merely from the pole ledger; regular full-character projection still makes sense.
3. **Branch-safe extraction.** Carrier/legal clearing factors are invariant. Extract the selected coefficient by the direct-summand projection in the rank-16 finite-flat curve algebra after clearing. Never implement this argument as regular division by a branch coordinate.
4. **All five occurrences and full standard target.** The ordinary comparison must supply each of the five source occurrences its own unchanged weight ρ_v = H_v⁵⁴∏_r ℓ_(v,r)²⁹ Q_v, with its original standard tag. Since 54 ≥ 35 and 29 ≥ 17, each weight divided by the uniform clearing factor is regular. The cleared coefficient must extend to the full original five-tag intersection using the imported all-chart/normality premises. Only inserted-prefix weights do not suffice; no missing chart tag may be borrowed.
5. **Repeated divisors and ordering.** Distinct occurrences with coincident divisors contribute separate factors; their divisor multiplicities add. Restrictions retain the original owner/formula data. Any alternating extension uses the already defined ordered source values and does not reconstruct this nonlinear expression on a permuted tuple.

These conditions give a regular ordinary degree-four cochain ΠQC separately from the other remainder terms. Neither δs = F, ΔZ = −C/2, an HPL closed-input identity, nor cancellation with another term is needed for this domain conclusion. Conversely, regularity alone proves none of those identities and does not permit dropping QC under Serre trace.

## Sources and review boundary

Primary audit inputs: `PROOF.md`, §§2–4,6; `null-overlap-homotopy-DOMAIN.md`; and the generic-input definition of Q in `null-overlap-homotopy-PROOF.md`. The character and comparison qualifications are also consistent with `PROOF.md`, §§2–6, and `PROOF.md`, §§1–4.

This was a read-only mathematical audit followed by creation of this review file. No source/model/matrix/polynomial instance was evaluated, no checker was run, and no was made. Imported geometric/domain premises were retained rather than re-proved.
