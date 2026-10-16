# Independent SW01 review: accept the conditional mathematics; keep source admission closed

Reviewed repository: `Akilleez-QA/read-em-and-weep`.

Reviewed commit: `9cd60c44f1cc3a732b58dcf1575be5c2539f8f17`, package [`research/codex-swarm/standard-source-witnesses/`](https://github.com/Akilleez-QA/read-em-and-weep/tree/9cd60c44f1cc3a732b58dcf1575be5c2539f8f17/research/codex-swarm/standard-source-witnesses).

## Verdict

The whole-standard extension implication is correct. The cited source-specific first-order theorem also supplies the claimed harmonic-zero implication, without calculating a harmonic coefficient again, **provided its identity and admissible-domain application are bound to the same emitted fresh source**. SW01 does not complete that binding and explicitly does not admit physical execution. I found no mathematical error in this stated conditional scope and no path from candidate hashes or proposal fields to physical admission.

This review is of the implication, the cited algebraic argument, the proposal boundary, and tiny artificial controls. It is not an independent replay of the physical model's polynomial identities, an acceptance of PH01 on behalf of its reviewer, a complete formalization of the imported proofs, or an arithmetic release.

## 1. Whole-standard extension

Use a complete owner `u=(seed, occurrence, carrier, legal_mask, standard_tag)`. For pair `p=(0,1)` or `(2,3)`, put `n_i=-2` on the pair and zero otherwise. The actual owned clearing divisor is

`C_u = H_u^14 product_(i in p) ell_ui`,

with multidegree `c_ui=14 d_u + [i in p] deg(ell_ui)`, where primary carrier degree is 5, auxiliary carrier degree is 4, and legal degrees are 1 or 3. On a three-owner tuple the necessary numerator multidegree is `D=sum_u c_u+n`. Here “multidegree D” is the homogeneous line-bundle degree; the affine polynomial can have lower actual coordinate degree, with homogenizing padding retained.

Assume (a) the **whole actual** source obeys `P_hom=(product C_u)F`, with `P_hom` a global section of `O(D)` in the intended physical frame and fresh alternating convention, and (b) each fixed weight has `rho_u=C_u q_u`, with `q_u` a regular section of `O(-c_u)` on the owner's **full standard open**. Restricting these sections to the target intersection and multiplying gives a section of `O(D-sum c_u)=O(n)`. On the source localization it equals `(product rho_u)F`. Finite summation with the fixed source signs therefore extends `Pi F` to that whole standard intersection.

This proves more than regularity after retaining all source divisors as units. In finite-frame exponents, the all-finite coordinate has lower bound 0; the all-infinity coordinate has upper bound `D_i-sum c_ui=n_i`; mixed coordinates are inverted. The exact owner-dependent D is indispensable. Replacing it by uniform 217/210 leaves a positive slack for smaller-degree owners and can fail the infinity bound.

The further statement about `B=R(K Pi+A h S Pi)F` is valid with the imported standard-map domain identities: K uses endpoint rectangle bits, S's staircases have the tensor cell's intersection, and h selects only exponents regular on its output chart. This is a conclusion for complete standard cochains, not a license to treat arbitrary raw rational pieces as regular.

Checked text: [SW01 PROOF §§1–2](https://github.com/Akilleez-QA/read-em-and-weep/blob/9cd60c44f1cc3a732b58dcf1575be5c2539f8f17/research/codex-swarm/standard-source-witnesses/PROOF.md#L5-L42), [combined-pole PROOF §§2–3](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-source-integration/combined-pole/PROOF.md), and [regular-cover transport §§2–3, 5, 7](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-proof-foundations/hm-regular-cover-transport.md).

### Concrete Qhat premise

The combined-pole identity uses the local polynomial carrier quotient, pair legal quotients `(1,0)` on finite charts and `(t,1)` at infinity, and raw complementary weights `(t^2,1-t^2)` at infinity. Conversion to the common finite frame includes exactly `product_(infinity i) x_i^(-c_ui)`. There is no second pair-character twist on Qhat and no section twist on rho. The zero finite-mask branch is defined polynomially, not by dividing zero by a vanishing equation. These precise identities must describe the emitted Qhat circuit; its name or degree declaration is insufficient.

## 2. The prior source theorem really gives harmonic zero

Distinguish the homogeneous numerator `P_hom` from the tensor harmonic projection `P_H`. The generic solver identity is

`delta T+T delta = 1-R A I P_H S Pi`.

Closedness alone does not kill the remainder: the pair line bundle has a one-dimensional degree-two harmonic component, represented by overlap exponent -1 in both pair factors and diagonal constants in the other two factors. Thus the source-specific exactness premise is essential.

The pinned [first-order-source §§2–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md#L61-L244) supplies the actual algebraic premise, rather than merely asserting vanishing. It derives the scalar from the **unsymmetrized** transgression, retains both mixed terms, uses the coefficient -30 ordinary-wedge square, converts to the ordered gerbe with the exact `-15 q_a,ij q_b,ij/8` correction, and checks the row/column trace sign. The result is

`delta s_old = (15/4) q_a cup q_b - tr(C_ab)/2 = F_ab`.

Its §4 identifies these terms with the pinned generator and keeps the physical endpoint derivatives. The argument is not “rank two implies exact,” and it does not discard the scalar trace correction because first currents are traceless.

The pinned [transition-only first-lift proof §2](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-proof-foundations/hm-transition-only-first-lift-alternative.md#L64-L105) supplies the required owned carrier14/legal1 domain for **both** F and s_old and fixes the N14 projection. Its [§§3–5](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-proof-foundations/hm-transition-only-first-lift-alternative.md#L107-L197) then gives, by chain-map composition,

`P_H S Pi s*F = P_H S Pi s*(delta s_old)`

`               = P_H delta(S Pi s*s_old) = 0`.

Consequently `delta T(s*F)=s*F`. No coefficient of s_old or harmonic scalar must be evaluated to use that implication. The existence of a regular admissible primitive is stronger evidence than a new sample or scalar recomputation.

### Order and domain are substantive application premises

For the intended fresh source order, restrict the **same physical transition/connection formulas** to increasing tuples and extend alternatingly. The displayed universal ordered first-order identity then applies on increasing triples. This is not an equality between the fresh cochain and a historical nonlinear source reevaluated after sorting. In particular the representative correction makes naive raw edge-order or cup-product symmetry unsafe.

An oracle-interface proof must identify the emitted F with precisely this fresh `b-tr(C)/2`, in the same pair, row convention, gerbe representative, physical line frames, endpoint derivatives, and common-cover pullback. It must also show that s_old and its differential belong to the very domain on which the fixed Pi/S/P_H identities are being composed. A domain for F alone is insufficient. The finite polynomial-degree transfer for F34 does not supply this cochain identification.

The [complementary-pair theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/02d0e727ffb95dfd9281906cc284c56e8bffd018/research/hm/null-source-integration/complementary-pair/PROOF.md) works with the raw formula on the unsorted inverse-image triple to transfer the finite property. PH01's direct pairwise frame theorem can then be applied without asserting a historical-order symmetry. SW01 correctly keeps those conclusions separate.

## 3. What the implementation does and does not prove

[`witnesses.py`](https://github.com/Akilleez-QA/read-em-and-weep/blob/9cd60c44f1cc3a732b58dcf1575be5c2539f8f17/research/codex-swarm/standard-source-witnesses/witnesses.py#L92-L133) recomputes owner degrees, tags, sorted owners and signs, requires exact field sets, and rejects numeric/string substitutes for Boolean admission fields. Candidate hashes have only syntax checks. `validate_proposal` always returns false for actual identity, physical execution and admission; `require_actual_admission` unconditionally raises. Those are appropriate fail-closed boundaries.

The [JSON schema](https://github.com/Akilleez-QA/read-em-and-weep/blob/9cd60c44f1cc3a732b58dcf1575be5c2539f8f17/research/codex-swarm/standard-source-witnesses/witness-schema.json) is a proposal shape. Cross-field checks require the executable validator; even those checks do not authenticate an algebraic proof or a physical coefficient callable. Neither `shape_valid` nor the true conditional-applicability flag establishes that its hypotheses hold. The final [gap registry](https://github.com/Akilleez-QA/read-em-and-weep/blob/9cd60c44f1cc3a732b58dcf1575be5c2539f8f17/research/codex-swarm/standard-source-witnesses/gap-registry.json) correctly retains the source-interface proof obligation.

## 4. Verification performed

- Fetched all 16 SW01 package files at the reviewed commit, plus the shared interface and all eight referenced proof files.
- Recomputed SHA256, byte count and Git blob identity from fetched UTF-8 bytes. All seven immutable theorem dependencies match every recorded pin; both workspace dependencies match their recorded SHA256 and byte count. Hash agreement establishes the text inspected, not the truth of its mathematics.
- Independently read the extension, quotient, transition-only exactness, and underlying first-order source derivations, with the physical-homogenization and complementary-pair scope boundaries.
- Ran all eight producer artificial tests and four non-Git independent artificial tests, normally and under `python -O`: **12/12 pass in each mode**. This includes 8,192 one-monomial tagged-intersection controls across both pairs, a tiny rational convolution, exact owner degrees, rejection of coarse-degree and common-local substitutions, field/sign/owner mutations, candidate-hash non-admission and forged admission fields.
- Replaced the checkout-dependent fifth independent test with direct fetched-byte pin verification as described above; it was not represented as a successful `git show` replay.
- Runs were bounded at 512 MiB address space, 59 CPU seconds and 60 wall seconds. Each synthetic unittest run took under one second.

No physical source polynomial was expanded, multiplied, evaluated or sampled. No physical source fibers or coefficient oracles were executed. No repository state or GitHub review was changed.

## 5. Required application handoff

The next source-interface application, including the FD01 lane identified by the integration owner, should supply one reviewed identity/domain composition, without duplicating the already proved scalar theorem:

1. **P binding:** identify the emitted whole numerator with the reviewed finite source circuit and PH01 homogeneous identity, at exact owned D and the original owners/tags. PH01 acceptance remains external to this SW01 review.
2. **Qhat binding:** identify each emitted quotient with the fixed N14 chart-unit/legality construction, one divisor-frame conversion, and the full-standard domain.
3. **Fiber/order binding:** for the actual lazy source fibers, preserve every owned occurrence, legal mask and original standard tag; implement the fixed auxiliary-first source ordering and its alternating sign; apply repeated-physical-source zero only to the pulled-back F. Distinct equal-valued factors cannot exchange owners.
4. **Primitive application:** prove the emitted fresh F is exactly the F in `delta s_old=F`, with the same gerbe/physical frame and endpoint derivatives; verify that the admissible s_old domain, its differential and all restrictions are covered by the fixed comparison maps. Then the displayed chain-map calculation discharges harmonic zero without recalculation.
5. **Separate outer acceptance:** do not promote this inner theorem to whole Rsharp/J0–J3 closure, the common54/29/5251 prism/restriction domain, detector values, a resource schedule, or execution permission. Those remain separate obligations.

The concrete missing deliverable is this application proof and source-faithful program binding, not another harmonic coefficient table or another Boolean witness.
