# Independent review of the balanced label's complete source exhaustion

## Verdict and frozen version

**PASS: the stated stable-label exclusion follows from a complete, correctly matched exhaustion.** No mathematical correction to the reviewed version is required.

Reviewed manuscript: `BALANCED-LABEL-TEN-SOURCE-EXHAUSTION.md`.

Frozen SHA256:

    f55f5a6f1c06b0fd80db3a571f0ede56337100cd8d646a60f6cee0db768f8934

The conclusion is precisely that the original-zero-defect profile-(1,1) label

    G3.11.73682b4c817f, source_index=72,
    A_q=O(-10)+W O(5), B_q=W O(-7)+O(8)

has no actual realization under the pinned actual-bundle and Gauss-profile hypotheses. All ten tuples in its original necessary source list are covered. This review makes no global frontier-count assertion and no conclusion about other stable labels or the global HM completion problem.

The review was completed on 2026-10-23. It independently checks the immutable input bytes, the exact original list, bundle decoding, rank and degree, every branch partition, and the applicability and noncircularity of the cited structural exclusions. The long descent is used as a pinned previously reviewed theorem; its precise entry interface and its final actual-quotient contradiction were inspected rather than assumed from a title or an author's summary.

## 1. Original-source identity and completeness

The original-data snapshot is commit `db51525015bb7c5e825833d550d08dedf6f6ea96` of `Akilleez-QA/read-em-and-weep`, in [research/hm/order-four-quadratic-load](https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load).

Git blob hashes were recomputed from the supplied exact file bytes, using the Git blob header as well as the contents. They agree with the pins:

- `one-one-endpoint-necessary-pairs.json`: `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`: `8b5971092f9ef762584912609fd5e9301c4e271d`.
- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`: `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.

The unique stable-label entry in the original frontier's `cases` list has the stated ID, profile `11`, `original_defect=0`, and `source_index=72`. The ordered quotient data agree with entry 72 of the necessary-pair list, after the harmless reordering of the two A summands. Entry 72 is zero-based; it has total degrees `a=0`, `b=-6`, and `defect=0`.

The frontier record also preserves an earlier provenance field `source_commit=4c147e95217f0900fa13f195662d95e933412c3c`. That historical field is not being confused with the immutable audit snapshot `db51525015bb7c5e825833d550d08dedf6f6ea96`.

The exact `compatible_E_types` array of entry 72 is, in order:

    ff (0,0,0,0,0,2,0,1)
    ef (0,0,0,0,1,1,0,1)
    ee (0,0,0,0,2,0,0,1)
    cf (0,0,1,0,0,1,0,1)
    ce (0,0,1,0,1,0,0,1)
    cc (0,0,2,0,0,0,0,1)
    bf (0,1,0,0,0,1,0,1)
    be (0,1,0,0,1,0,0,1)
    bc (0,1,1,0,0,0,0,1)
    bb (0,2,0,0,0,0,0,1).

These are exactly the nonnegative solutions with `a=d=g=0`, `h=1`, and `b+c+e+f=2`. Equality was checked against the full original array, not merely membership of the ten displayed tuples. There is no omitted eleventh tuple and no duplicated tuple.

Completeness has the appropriate necessary, not sufficient, meaning. Sections 2–3 of the original splitting proof give every possible actual equivariant splitting. Section 5 of the original endpoint-pair proof states the necessary compatibility filters and records every compatible primal type for each retained pair. Hence every actual realization of this fixed label must use one of the ten listed sources. No claim that any compatible source is realizable is needed.

## 2. Full decoding and the strict-top starting point

The original splitting formula gives

    R_2=(c+g+h-1)V+(d+e+g+h)P+(f+g)D.

Specializing the exact tuples therefore gives

    E=(cV+(e+1)P+fD) O(-2)+bT O(-3)+cV O(-4)
      +eWp O(-5)+f O(-8)+O(-10).

In particular, increasing e adds both `P O(-2)` and `Wp O(-5)`. Omitting the former would give an incorrect bundle and invalidate the source accounting; the manuscript does not omit it.

With dimensions `dim V=3`, `dim P=4`, `dim D=5`, `dim T=6`, and `dim Wp=2`, direct bundle arithmetic gives

    rank E=5+6(b+c+e+f)=17,
    degree E=-18-18(b+c+e+f)=-54.

These identities hold separately for all ten original tuples. Their top coefficient dimensions, in the original order, are

    14, 13, 12, 12, 11, 10, 9, 8, 7, 4.

Strict-top injectivity gives

    R_2=H0(E(2)) -> H0(A_q(2))=H0(W O(7))=V+2P+D.

The negative `O(-10)` quotient contributes no sections at this twist. In particular, the top map is never zero: every listed top coefficient is nonzero and its section map is injective. This excludes the otherwise implicit generic-rank-zero branch before any rank-one/rank-two partition is used.

The three old strict-top prunings are individually correct:

- ff has `P+2D`, which cannot inject because the target has only one D.
- ee has `3P`, which cannot inject because the target has only two P copies.
- cc has `2V+P`, which cannot inject because the target has only one V.

They remain in the exhaustion only to cover the original complete list. They are not new source-pair removals.

## 3. Exact dependency versions

The following SHA256 hashes were recomputed and agree with the cited versions. The linked paths are immutable public proof locations.

- P814, [rank-two polar proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md), commit `1f94be65b3a470a1b594e61d56df7f6057c9d907`: `f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc`.
- R814, [rank-one bb exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/RANK-ONE-TOP-EXCLUSION.md), same commit: `2f480884b26a089bcd6f3633e75e790472cc493d9908dd83f0497c6b1fbe8d50`.
- PR819, [bf quartic subsystem](https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BF-SUBSYSTEM.md), commit `03fee9278072f9ac00a5fcee5deb04b7fce61ae5`: `087d0b78196b7c0d5e773375e603359450e0e9fb0ebb3003734c44eea4e133b9`.
- PR819, [bb cubic torsion subsystem](https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BALANCED-TORSION-CUBIC-SUBSYSTEM.md), same commit: `b1a6b94b0e1a7cce942af8e52d4bcc59317ce9d8c6823610e5d288da0c62429f`.
- PR821, [onto rank-four top subsystem classification](https://github.com/Akilleez-QA/read-em-and-weep/blob/0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f/research/hm/profile11-onto-rank-four-top/ONTO-RANK-FOUR-TOP-SUBSYSTEMS.md), commit `0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f`: `87244e453597105dffb298743c1725ac29b00c8b8dc1cafad37f55235c81ea34`.
- P823, [third backward quotient](https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-THIRD-BACKWARD-QUOTIENT.md), commit `399abe93debe71232f0b7808fc8f1a5582118708`: `16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0`.
- P823, [finite backward descent](https://github.com/Akilleez-QA/read-em-and-weep/blob/399abe93debe71232f0b7808fc8f1a5582118708/research/hm/profile11-balanced-bf-backward-exclusion/BF-FINITE-BACKWARD-DESCENT.md), same commit: `9558490385822a4d559d555c4f3372fd594e7ef0f504454da0707d962cf9fd49`.
- P828, [horizontal projected-lattice exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/ae077cbe42d65cde27d65ce88923dc35851b6952/research/hm/profile11-horizontal-quotient-exclusion/HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md), commit `ae077cbe42d65cde27d65ce88923dc35851b6952`: `a637a5ba2c69b460bd2e058ea26100b4d2830e1b4f72fd823bae1dbba6e8701a`.
- P836, [onto-bb exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/c6b6ec427e5690055c18c181fad39efd6624cc83/research/hm/profile11-onto-bb-exclusion/ONTO-BB-SOURCE-EXCLUSION.md), commit `c6b6ec427e5690055c18c181fad39efd6624cc83`: `4fbecacfb401cad0b82f3e5990d56fc0da65af6b493596ea6a8cadce16d8ca98`.
- P838, [balanced bb torsion exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/8b9e7affe6906ead2927fb251e6b64b886020030/research/hm/profile11-balanced-bb-torsion-exclusion/BALANCED-BB-TORSION-DESCENT-EXCLUSION.md), commit `8b9e7affe6906ead2927fb251e6b64b886020030`: `db935dd621f64b9336727919f4af4710ceeac03f432d567c9530db9ba5eb10e8`.
- Pbc, [balanced bc exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/5951b547d07afe052bc6f823a3ac2b5f29963114/research/hm/profile11-balanced-bc-exclusion/BALANCED-BC-BACKWARD-EXCLUSION.md), PR839, commit `5951b547d07afe052bc6f823a3ac2b5f29963114`: `64e55ab01aa6811d9a87ea73282512633c807aeb8a29f9be2f3636f652303288`.

The common earlier derivative-image and first-polar inputs are PR796 at `d2b43060c83328dd5118aee6b9288fcfa0c873ac` and PR799 at `2172e4a7abbbe232f9f448bea6fa01dee7927460`; their supplied proof bytes have Git blob IDs `46a0de762000f21182f6d3168f3ecfd63adaf75f` and `a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1`. These match the dependency manifest. The PR802 restatement at `e484640a6565c278321bf6557860262c1ac1b7df` has supplied Git blob `98a1bd6123e148476da0b997d879aecbf885ec97`; no new theorem from that restatement is needed to fill a branch.

## 4. Direct-source exclusions ef, cf, ce, be

For balanced `U=W O(5)`, a saturated equivariant line has even degree at most four and hence at most seven twist-two sections. The top dimensions of ef, cf, ce, and be exceed seven. Thus their top images have rank two. For a rank-two image I with torsion length delta in U, global generation of I(2) gives

    dim R_2 <= h0(I(2))=16-delta.

Since each relevant top dimension exceeds four, delta is less than twelve. The invariant-divisor minimum makes delta zero. Thus the onto hypotheses in P814 and P828 are actually forced, not additional assumptions.

P814 proves zero internal derivative for all four sources and applies its actual constant-projection polar lemma. In ef, its required `O(4)->W O(7)` is zero equivariantly. In ce, its required `O(8)->W O(7)` is zero by degree. In be, its required `O(14)->W O(7)` is zero by degree. These are entire-source exclusions in the balanced label, not merely some top-map branches.

For cf, P814 instead supplies the actual constant P, the projected standard `Sym^9 W O(-1)` system, and the full constant span of dimension fifteen. P828 applies to this exact source and both relevant labels. Its negative-endpoint removal gives the exact first span of rank eighteen and degree -30. Projection through the genuine constant span produces a full-rank, connection-preserved coherent image of degree -20 in a constant bundle. The horizontal-lattice lemma proves that this image has no divisor defect, contradicting its negative degree. The result does not presume that an arbitrary generic full-rank projection is saturated.

Balanced ce is assigned once, to P814. P828's additional ce statement concerns the split label; it neither supplies an extra balanced source nor creates another removal to count here.

## 5. Complete bf coverage

For bf the top coefficient is `P+D`, of dimension nine. The same balanced line bound forces rank two; the generation estimate gives delta at most seven and hence zero. Therefore the top map is onto in every possible bf realization.

P814's exhaustive small-kernel calculation leaves internal derivative image either zero or saturated `O(-10)`. It excludes the zero case by the polar requirement `O(12)->W O(7)`. This is not by itself a whole-source exclusion, and the manuscript correctly supplies the complementary dependency.

For every nonzero internal channel, PR819's bf theorem gives the actual quartic V subsystem and `K_1/K_2=W O(3)`, where `K_i=E^{(-i)}`. This includes every nonzero combination of the permitted quintic and scalar internal components: the theorem assumes only that the internal image is nonzero, not that one selected component is nonzero. P823's preliminary quartic argument then proves `K_2/K_3=W O(1)` and its third-quotient theorem supplies the exact next quotient. The finite descent contradicts the final negative horizontal kernel.

Thus top rank zero, top rank one, nonsaturated rank-two top images, zero internal derivative, and every nonzero internal derivative have all been covered. No bf branch survives.

## 6. Complete bc coverage, including its lower channel

The bc top coefficient is `V+P`, of dimension seven. Rank zero is excluded by strict-top. P814 excludes rank two; since its top dimension exceeds four, a rank-two top map is automatically onto, as required by that proof.

For rank one, the seven section dimensions force its saturated image to be `O(4)` inside `W O(5)`. The map from `V+P=Sym^6 W` is the complete degree-six evaluation, so its raw image is already all `O(4)`. There is no unexamined top divisor correction.

Pbc handles both possibilities for the lower `T O(-3)` map into the Euler quotient `O(6)`:

1. If that channel is zero, `H0(K_1(3))=2T`. Its twelve top sections force the full saturated `W O(3)` first backward image.
2. If it is nonzero, the exact cohomology budget forces `K_1=T O(-3)+(V+P) O(-4)+O(-8)`. Its top T either fills `W O(3)` or fills the Euler `O(2)`. In the latter case a nonzero P quotient channel fills the complement. If the P channel vanishes, the remaining scalar quotient channel is either zero or nonzero. These give respectively raw image `O(2)` or raw image `O(2)+O(-8)` with defect twelve. Their next kernels both violate strict-top into the actual next target. The defective image is not silently replaced by its saturation.

Hence both lower-channel alternatives give exactly `K_1/K_2=W O(3)`. The forced V top of K_2 then gives `K_2/K_3=W O(1)`. Pbc establishes the common source-free descent interface described below. There is no missing zero-lower-T branch or defective first-backward branch.

## 7. Complete bb coverage

Here `F=P O(-2)` has rank four. Rank zero is impossible. R814 excludes every rank-one top image for the balanced target: only the saturated Euler `O(4)` line can occur, and its exact kernel has zero internal derivative, giving the forbidden quadratic Gauss-gap case.

For generic rank two, one cannot reuse the `dim R_2>4` saturation argument. Let delta be the top-image torsion length. Generation and strict-top give

    4 <= h0(I(2))=16-delta,

so `0<=delta<=12`. A positive invariant divisor has degree at least twelve. Consequently the only possibilities are onto (`delta=0`) or defect twelve. In the latter case I has rank two, degree -2, and `H0(I(2))=P`. Among the generated-after-twist-two equivariant possibilities `O(-2)+O`, `W O(-1)`, and `Wp O(-1)`, only the last has this section character. Thus the exceptional branch is precisely `I=Wp O(-1)`, as stated.

For the onto branch, PR821's exhaustive classification gives two actual constant-span alternatives: the nine-dimensional degree-eight system and the twelve-dimensional P-conic system. P836 excludes both, not merely the first. Its second argument retains every necessary splitting of the positive-endpoint transform, then uses the actual linear top's constant-span dimension contradiction. Thus P836 covers the full onto branch.

For defect twelve, PR819 identifies the exact defective image and cubic Wp subsystem. P838 proves the necessary backward interface without importing an onto hypothesis or a bf quartic construction. In particular, its first section-image argument uses surjectivity of `E'->W O(5)` to force both T multiplicity lines: if only the already-present top T image occurred, global generation would make E' map into the proper defective image I. It then forces `W O(3)` and `W O(1)` as the first two backward quotients and reaches the common finite descent.

The bb possibilities are therefore exhausted by R814, P836, and P838, with the positive top-image defect explicitly retained until the dedicated torsion proof applies.

## 8. Shared descent interface and dependency independence

For bf, bc, and torsion bb, the entry data for the source-independent part of P823 are exactly

    rank K_3=10, degree K_3=-62, maxdeg K_3<=-5,
    derivative target W O(-1),
    H1(K_3(4))=A+P+D, chi_G(K_3(5))=-W.

The kernels are successive actual derivative kernels in the same constant ambient bundle, so they are saturated and satisfy the strict-top theorem. These geometric hypotheses are essential and are present in all three applications. The profile-(1,1) bound on the first backward endpoint is at most two; no false rank-three endpoint assumption is introduced.

From Section 1 onward, the third-quotient proof uses just these inputs, equivariance, and the actual connection. Its necessary K_3 list retains all four types, including `S O(-5)+P O(-6)+W O(-9)`. It proves the actual quotient `K_3/K_4=W O(-1)` rather than assuming saturation. The subsequent finite descent depends on those four types and that quotient, not on which of the three initial sources supplied them.

The terminal raw image is

    K_6/K_7=O(-8)+O(-18) inside W O(-7),
    K_7=W O(-9).

Its determinant defect is twelve and is retained. The next derivative targets `O(-10)+O(-20)`, not `W O(-9)`. Every map from `W O(-9)` to this actual target vanishes by ordinary degrees. Therefore K_7 is a negative saturated horizontal subbundle, which is impossible in characteristic zero. This checks the decisive shared contradiction and the correctness of both transfers to the finite descent.

The dependency graph is noncircular. The bf route uses PR819 and P823; bc and torsion bb independently establish their entry data before using P823. Neither needs the other source exclusion, the onto-bb exclusion, or the present full-label conclusion. P836 uses PR821's onto classification, not the torsion exclusion. P828 uses P814's forced actual subsystem, not the label conclusion. Thus the assembly does not use a full-label exclusion to prove one of its own missing cases.

## 9. Final completeness statement and limits

In the exact original order the ten assignments are

    ff: existing strict-top pruning;
    ef: P814;
    ee: existing strict-top pruning;
    cf: P828;
    ce: P814, once;
    cc: existing strict-top pruning;
    bf: forced rank-two top, then P814 zero-channel / PR819+P823 nonzero-channel;
    be: P814;
    bc: P814 rank-two / Pbc rank-one;
    bb: R814 rank-one / P836 onto rank-two / P838 defect-twelve rank-two.

Every assignment has the same label, original defect, actual source tuple, and bundle decoding as its input. No omitted top rank, internal channel, divisor correction, or lower quotient channel was found. The original necessary-list completeness therefore turns these source contradictions into the claimed exclusion of **G3.11.73682b4c817f**.

The verification involved immutable file hashing, equality of the supplied finite source list, universal bundle rank/degree arithmetic, and structural proof/interface inspection. No selected actual HM/source coefficients, parameters, points, evaluated derivatives, matrices, instance ranks, selected models, experiments, scans, or unapproved large computation were used. No external state was changed. The old strict-top prunings are not counted again, and no arithmetic beyond this one stable-label exclusion is asserted.
