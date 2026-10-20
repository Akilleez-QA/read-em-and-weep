# Final public-text publication check

Review date: 2026-10-20 UTC. Result: passes within the scope below.

## Exact reviewed bytes

- PROOF.md SHA-256: `3c79b91763608c78e3e50a38cdfe6d753cd73583f85613dd8d4df48b74a308b6`
- PLUCKER-LEMMA.md SHA-256: `250d11cede78b7cfa0647f9e63f33100e11c5b3f20adfbd5a679819efa035ecb`
- Imported twist-three-reduction/PROOF.md SHA-256: `114adf003fbf14dc8ea4cd597731fb7e0df4899dbf397e8fbc7732823179831c`
- Imported twist-three-reduction/INPUTS.md SHA-256: `834f2bfba295bd7405a91f2d106b6aabe4cbbae469cc48e238b2ea016fd62c15`
- hn_arithmetic.py SHA-256: `8edfe95e0e6864e7bec762ba695ec19a29cf20fdfc08ee4deb8b025988a86830`
- audit_arithmetic.py SHA-256: `d51f90560428fd2277cde5bd557f36451908a2847a4fd88f263024c488bbfd18`
- Compared original PROOF.md SHA-256: `c28cbf3c492e82da32e38fd1c465ddcf848fe80f3c2b2ddc31378dd186cdb86a`

These hashes identify the final public proof and dependencies, rather than the earlier mathematical audit's target. Any later change to a reviewed proof or lemma requires this check to be renewed.

## Checks performed

1. Read the entire final public proof and its self-contained Plücker lemma, and compared the proof with the stated original. Mathematical statements and their conditional scope are preserved. Public links replace private dependencies; the negative-H¹ input now cites the primary proposition directly.
2. Verified the Plücker line criterion using contraction spans after quotienting by the common intersection. The ensuing star-or-top argument gives span dimension at most m+s, including the separate s=0 case. This suffices for the determinant-degree-one exclusions without assuming a chosen HM matrix rank.
3. Checked the mod-5 Riemann–Roch calculation, saturation/reflexivity of the first HN piece, the determinant and full-span exclusions, and all six first-piece arithmetic candidates before the c₂ exclusions. The positivity argument for a globally generated torsionfree quotient is valid: general rank-minus-one sections have no codimension-one degeneracy; at every point of codimension at least two, depth(O)≥2 and depth(Q)≥1 force quotient depth≥1. The quotient is therefore rank-one torsionfree, with effective codimension-two second Chern class.
4. Checked all five residual profiles and their congruence-rounded Bogomolov lower bounds by hand. Each gives ch₂(K)≤3/2, so t=0 independently of semistability; the semistable case uses the separate discriminant and 5-divisibility argument. The short scripts contain only finite rank/determinant/congruence arithmetic, not geometric-instance evaluation.
5. Reopened Chen's primary arXiv paper, Theorem 1.14 (printed p.9) and Proposition 5.2 (printed pp.31–32). On smooth P⁴ the identity resolution applies to the reflexive semistable sheaves in question. The equality-case filtration has projectively flat quotients of the same slope. Simply connected P⁴ and integral line-bundle slopes exclude slope −1/3; the integer-slope final quotients split as asserted. Passing a torsionfree HN quotient to its reflexive hull preserves semistability, while its effective defect can only decrease the discriminant. No general-plane semistability premise is used.
6. Visually inspected the primary Decker–Schreyer printed-p.218 proposition and its normalization paragraph. It states H¹(End(F)(u))=0 for u≤−2 for the classical normalized HM bundle. Trace splitting supplies the stated B vanishing. Checked the codimension-three Ext vanishings, exact dual-evaluation sequence, and contradiction from a nonzero map K→O(−1) or O(−2). The proof obtains t=0 before this step, so it is not circular.
7. Checked c₁,c₂,c₃ of B(3), the projective-bundle top-intersection value −585, and the resulting nonempty defect conclusion. This proves only a defect supported in dimension at most one, not necessarily a curve.

## Limits

No mathematical correction to PROOF.md or PLUCKER-LEMMA.md was needed. This review is not a formal proof certificate, and does not assert that the conditional fifteen-section branch actually occurs. It proves no cubic vanishing and evaluates no HM differential, source, cofactor, pairing, or selected instance. The imported twist-three reduction is separately checked at the hashes above; the numerical twist-two prerequisite remains the pinned dependency described in PROVENANCE.md. No external service was changed.
