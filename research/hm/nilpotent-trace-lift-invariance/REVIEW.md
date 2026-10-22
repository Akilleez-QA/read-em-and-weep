# Independent mathematical review

Verdict: PASS for the local invariance lemma. The actual square-zero input is independently verified from the pinned published chart definition and square-zero theorem, as detailed below. This is not a determination of the common obstruction map.

Frozen PROOF.md SHA256: a16391896f8707c9f2a2afba6af67d226107238d08968644c45450cfb5a01ca7.
Frozen verify.py SHA256: f345f2d74d20eb733cba291dfb68ba5428b3567e0250740327f12a21a1355f7f.

## Evidence and checks

I independently read both files and retrieved the full preceding proof directly at [PR716 commit 2a602d811b904def02bd56518fb0549e2911ff3e](https://github.com/Akilleez-QA/read-em-and-weep/blob/2a602d811b904def02bd56518fb0549e2911ff3e/research/hm/firstnormal-trace-variation/PROOF.md). Its returned Git blob SHA was e9b51b438105f9c9577da5eb9fedc812de6131e6. I ran only the inspected tiny free-symbol verifier in this directory; it printed PASS and exited zero. No actual-instance coefficients, points, derivatives, or matrix ranks were evaluated, and no GitHub writes were made.

1. For two trace-free solutions of the same first-normal square equation, subtraction is exactly {n,E}=0. Rank-two polarization converts this to tr(nE)=0. The weighted regular-pair syzygy from the pinned proof gives E=eta A with eta in S1. Conversely such additions preserve that equation. Thus the nonempty space of regular homogeneous weight-four solutions is the affine space T+K. This does not assert the same freedom for full filtered or global lifts.

2. A squared is (f squared/4) times the identity. Hence tr((eta A)(ell A))=(eta ell/2) f squared. The fixed harmonic-product terms do not change with T; the difference lies in f squared S2, a summand of the exact pinned trace image. Therefore O_T is independent of T among these solutions. Independence is in the fixed harmonic frame with n, the unit, and the product convention fixed.

3. The proposed D1 correction has zero diagonal and upper entry and quadratic lower entry eta ell/(2u), so it is a regular trace-free matrix of weight zero. Its trace pairing with n is -eta ell f squared/2, exactly the negative change in tr(TD). The sign is positive in the lower entry, and the factor 1/u is necessary. No division by either polynomial f or g occurs. Adding this correction, and subtracting it for the inverse translation, gives a bijection between solutions of the two homogeneous first-normal trace-orthogonality equations. This justifies liftability invariance at the stated local truncated level, not existence of global lifts.

4. Weight bookkeeping agrees with the pinned convention. Products nT and B1(n,n) have weight twelve; TD and the mixed B1 terms have weight eight; the correction has weight zero. The lower bounds on full filtered coefficients ensure no higher-weight term enters the selected weight-twelve equation. All matrix entries used in harmonic multiplication have even degrees; use of odd f, g, and ell in the polynomial kernel parametrization does not supply separate scalar harmonic lifts of those odd forms.

5. The source dimension two and target dimension five are inherited correctly: S1 has dimension two, while f squared S2 and k fg have dimensions three and one with zero intersection by regularity. The unit u does not alter that subspace. The change in the leading fourth-square class is a O_T(D) only under the separate coherence and leading-vertex hypotheses of PR716. It is a local variation statement; the base class is not thereby computed.

## Actual-input applicability and limits

The exact PR716 proof supplies the actual frame, grading, regular-pair description, product convention, trace-image quotient, and local variation formula. Nilpotence must not be inferred merely from coherence. It is, however, supplied by the preceding published actual construction, independently retrieved during this review:

- [Canonical square-zero lift, section 4, equation (11)](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md) proves U_a squared is zero on the actual bundle over 2Q by the monad trace certificate and rank-two Cayley-Hamilton. Returned blob SHA: 240b39cc35b02287fb135a39a1b056a05e9cfb20.
- [Exact coherence, section 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md) defines N_s=U_(s squared)/s squared on s nonzero, and N_t=U_(t squared)/t squared on t nonzero. Division by the chart unit yields N_s squared=N_t squared=0. Returned blob SHA: 72fc7b17cd750ac9f7790ae58001db29f7f09e94.
- [Third-neighborhood theorem, section 2](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md) explicitly uses that actual square-zero N_s in the harmonic expansion L(n)+qL(T), with the full actual filtered regular pair and the same lower bounds. Returned blob SHA: 66ad91bc7026203d340a7988f679caa1b98b02ce.
- [PR692, section 1](https://github.com/Akilleez-QA/read-em-and-weep/blob/858f96ba1539afb1293f31239b8761af08e46f60/research/hm/vertex-scalar-filtration/PROOF.md) retains exactly that actual harmonic-frame input. Returned blob SHA: bc9a9a2aa1b4d7343de5c4168d93bb8017e155bb.

Consequently the actual leading T satisfies the displayed weight-twelve equation, and the affine solution space is nonempty for that actual input. This resolves applicability by a specific prior theorem, not an assumption that coherence implies square-zero. For a general source a the multiplier relating U_a to the chart N_s has a q correction; one should not silently identify the fixed chart N_s with U_a/a. The chart-source definitions above avoid that error. No new global extension or frame normalization is used.

The verifier checks universal matrix identities, the correction, and elementary degree arithmetic. It does not prove regularity, syzygy completeness, the supplied harmonic-product construction, geometric nilpotence, global realization, or a rank/value of O_T; those are respectively deductive inputs or deliberately unresolved questions. Declaring all free symbols nonzero in the script does not narrow the polynomial identities in f, g, eta, ell: their displayed cancellations are identities, with only u inverted. The written proof independently supplies those identities.

In particular, this result does not prove universal vanishing, existence of all local/global completions, any Bockstein identification, or elimination of the base vertex obstruction. The warning against a polynomial-algebra splitting argument is appropriate: the actual scalar harmonic algebra is the even Veronese algebra, not a supplied deformation of all k[X,Y].

The final proof includes the explicit pinned actual-input implication above. This is an independent deductive review with a bounded symbolic check, not a proof-assistant certification.
