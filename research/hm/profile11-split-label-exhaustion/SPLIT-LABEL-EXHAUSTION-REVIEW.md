# Independent review of the split label's complete source exhaustion

## Verdict, exact version, and scope

**PASS.** The manuscript proves the stated stable-label exclusion by exhausting the complete original necessary source list. No mathematical correction is required to this exact version.

Reviewed manuscript: `SPLIT-LABEL-TEN-SOURCE-EXHAUSTION.md`.

Frozen SHA256:

    8a36d8f64036a690648fd7cc14d8c5ea73406ecf2d106bea4db7638c80b21d9e

The conclusion concerns exactly the original-zero-defect profile-(1,1) label

    G3.11.863639aa192e, source_index=69,
    A_q=O(-10)+O(4)+O(6),
    B_q=O(-8)+O(-6)+O(8).

The review was completed on 2026-10-23. It independently checks the original input identity, ordered ten-tuple list, full bundle decoding, rank and degree, all source and channel partitions, exact actual-connection interfaces, and dependency noncircularity. The final manuscript was reread after its immutable split-bundle links were inserted, and its frozen hash was recomputed. This verdict is not an assertion about any other stable label or the global HM completion problem.

## 1. Original data and exact list completeness

The original-data snapshot is commit `db51525015bb7c5e825833d550d08dedf6f6ea96` of `Akilleez-QA/read-em-and-weep`, under [research/hm/order-four-quadratic-load](https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load).

The Git blob hashes were independently recomputed from the exact supplied file bytes, including the Git blob header. They are:

- `one-one-endpoint-necessary-pairs.json`: `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`: `8b5971092f9ef762584912609fd5e9301c4e271d`.
- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`: `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.

The unique stable-label record has the stated ID, profile `11`, `original_defect=0`, and `source_index=69`. Its A and B arrays agree exactly with zero-based entry 69 of the necessary-pairs file. That entry has degree fields `a=0`, `b=-6`, and `defect=0`. The record's historical `source_commit=4c147e95217f0900fa13f195662d95e933412c3c` is not being confused with the immutable snapshot used for this audit.

The full `compatible_E_types` array of entry 69 is, in its original order:

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

Equality of the entire ordered array with the manuscript's list was checked, not merely membership of individual tuples. These are exactly the nonnegative solutions with `a=d=g=0`, `h=1`, and `b+c+e+f=2`. There is no duplicate or omitted tuple.

The necessary-list interpretation is sufficient for the conclusion. The original actual-splitting theorem gives every possible actual equivariant source type, and Section 5 of the endpoint-pair theorem records every source satisfying its necessary filters for each retained pair. Therefore every actual realization of this fixed label must use a listed source. Neither the manuscript nor this review assumes that a formally compatible source is realizable.

## 2. Bundle decoding and the strict-top starting point

The original formula is

    R_2=(c+g+h-1)V+(d+e+g+h)P+(f+g)D.

Specializing the ten tuples gives exactly

    E=(cV+(e+1)P+fD) O(-2)+bT O(-3)+cV O(-4)
      +eWp O(-5)+f O(-8)+O(-10).

Thus each e contributes both `P O(-2)` and `Wp O(-5)`. The manuscript retains the essential extra P.

Using dimensions `dim V=3`, `dim P=4`, `dim D=5`, `dim T=6`, and `dim Wp=2`, direct arithmetic gives

    rank E=5+6(b+c+e+f)=17,
    deg E=-18-18(b+c+e+f)=-54.

These identities were checked separately for all ten tuples. Their top coefficient dimensions, in the original order, are

    14,13,12,12,11,10,9,8,7,4.

The original strict-top lemma gives

    H0(E(2)) -> H0(A_q(2))=Sym6 W+Sym8 W=V+2P+D

injectively. The negative quotient summand contributes no sections at this twist. All ten top coefficients are nonzero, so generic top rank zero is excluded before the rank-one/rank-two case divisions.

The three inherited strict-top exclusions are correct: ff has `P+2D`, ee has `3P`, and cc has `2V+P`, exceeding respectively the D, P, and V multiplicities of the target. Their inclusion in the list proves original-list completeness; they are not counted again as new removals.

## 3. Exact structural dependencies and the public split pin

The supplied bytes of every dependency below were hashed and match the SHA256 values cited in the manuscript:

- P814, [rank-two polar proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md), commit `1f94be65b3a470a1b594e61d56df7f6057c9d907`: `f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc`.
- R814, [rank-one bb exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/RANK-ONE-TOP-EXCLUSION.md), the same commit: `2f480884b26a089bcd6f3633e75e790472cc493d9908dd83f0497c6b1fbe8d50`.
- P826, [split-ce exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/96734783c561c2baca8f91d69772318446898f06/research/hm/profile11-split-ce-constant-span-exclusion/SPLIT-CE-CONSTANT-SPAN-EXCLUSION.md), commit `96734783c561c2baca8f91d69772318446898f06`: `e3c1cb16be8ed7714cb2c3d5f6a3ba9f7da85567aa5a53e100b2d3458fc977bd`.
- P828, [horizontal projected-lattice exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/ae077cbe42d65cde27d65ce88923dc35851b6952/research/hm/profile11-horizontal-quotient-exclusion/HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md), commit `ae077cbe42d65cde27d65ce88923dc35851b6952`: `a637a5ba2c69b460bd2e058ea26100b4d2830e1b4f72fd823bae1dbba6e8701a`.
- P830, [split-bf rank-two nonzero-channel exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/620d5598ccc19e5e1c458a4cddb0d3a0709d83c3/research/hm/profile11-split-bf-rank-two-exclusion/SPLIT-BF-RANK-TWO-NONZERO-CHANNEL.md), commit `620d5598ccc19e5e1c458a4cddb0d3a0709d83c3`: `d762e23c6b402bf8bfd62160e310ecacf601a910d47f6a3e278cd8a3806657f6`.
- PR821, [onto-top classification](https://github.com/Akilleez-QA/read-em-and-weep/blob/0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f/research/hm/profile11-onto-rank-four-top/ONTO-RANK-FOUR-TOP-SUBSYSTEMS.md), commit `0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f`: `87244e453597105dffb298743c1725ac29b00c8b8dc1cafad37f55235c81ea34`.
- P836, [onto-bb exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/c6b6ec427e5690055c18c181fad39efd6624cc83/research/hm/profile11-onto-bb-exclusion/ONTO-BB-SOURCE-EXCLUSION.md), commit `c6b6ec427e5690055c18c181fad39efd6624cc83`: `4fbecacfb401cad0b82f3e5990d56fc0da65af6b493596ea6a8cadce16d8ca98`.

Psplit is the immutable PR844 bundle at commit `c86ed140ecd1371d2881727094f56230bdd04b85`, in [research/hm/profile11-split-backward-exclusion](https://github.com/Akilleez-QA/read-em-and-weep/tree/c86ed140ecd1371d2881727094f56230bdd04b85/research/hm/profile11-split-backward-exclusion):

- [SPLIT-BACKWARD-DESCENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c86ed140ecd1371d2881727094f56230bdd04b85/research/hm/profile11-split-backward-exclusion/SPLIT-BACKWARD-DESCENT.md): `ee1096f2368fee248792c35feeb3c689a134b8e1a84934c9699575fbe920ee1a`.
- [SPLIT-BC-SOURCE-EXCLUSION.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c86ed140ecd1371d2881727094f56230bdd04b85/research/hm/profile11-split-backward-exclusion/SPLIT-BC-SOURCE-EXCLUSION.md): `22910f2176448710de765823ee872bcb43ead8e300a9ebdf65e6a16b0307f40e`.
- [SPLIT-BF-BACKWARD-INTERFACE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c86ed140ecd1371d2881727094f56230bdd04b85/research/hm/profile11-split-backward-exclusion/SPLIT-BF-BACKWARD-INTERFACE.md): `b5924ec48fe1dd7583b37d75d47b8ef1ec3f0b3a589744349ebf924c08de4a61`.
- [SPLIT-BF-SOURCE-COROLLARY.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c86ed140ecd1371d2881727094f56230bdd04b85/research/hm/profile11-split-backward-exclusion/SPLIT-BF-SOURCE-COROLLARY.md): `3f7aec33779fe0a1e85069cd734ecbe9bbe44ba956ffcde0c4a42852c51ead48`.

The repository directory at this exact commit was read independently. Its four proof-file Git blob IDs are, in the same order,

    3a2a3f955d293a81558d61df4645109fa8276151,
    5423da2cc6c821781ef10642aa05c3afe7064085,
    64cd906a2c19ad32b6661cacab315109301f074f,
    5118d87b1af4f9d0be2c16da0465bf00a9579f1b.

Each matches the independently computed Git blob hash of the reviewed file. The final manuscript's four direct links agree with those returned immutable public locations. No publication placeholder remains.

The supporting quartic construction in PR819, commit `03fee9278072f9ac00a5fcee5deb04b7fce61ae5`, has `BF-SUBSYSTEM.md` SHA256 `087d0b78196b7c0d5e773375e603359450e0e9fb0ebb3003734c44eea4e133b9`. Its Sections 2–3 were inspected to confirm that P830 imports only the profile-free linear-kernel and quartic-evaluation construction, not its later balanced quotient. The PR823 bounded-support references at commit `399abe93debe71232f0b7808fc8f1a5582118708` have SHA256 `16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0` and `9558490385822a4d559d555c4f3372fd594e7ef0f504454da0707d962cf9fd49`; their supplied hashes also agree. The split theorem rederives its own split images and does not borrow a balanced-target conclusion.

## 4. Direct whole-source exclusions ef, cf, ce, and be

For ef, ce, and be, strict-top injectivity identifies their two-dimensional P multiplicity space with the two P occurrences in `Sym6 W+Sym8 W`. A constant change among the two source P copies separates the O(4) and O(6) rows. Each nonzero irreducible system is basepoint-free because its degree is below twelve, the least positive invariant-divisor degree. Thus the top map is onto in each case.

For cf, V can reach only O(4) and D only O(6). Strict-top makes both rows nonzero, and their degrees six and eight make them basepoint-free. The top map is again onto. These are actual surjectivity conclusions, not additional hypotheses.

P814 establishes the zero internal derivative in these four sources. Its polar lemma excludes ef by the required equivariant `O(4)->O(6)+O(8)`, whose degree-two and degree-four invariant spaces vanish. It excludes be by the required `O(14)` subline, impossible by ordinary degree. Thus both are entire-source exclusions.

For cf, P814 instead forces the actual constant P and projected standard `Sym9 W O(-1)` subsystem. P828 applies to this exact source and split label. After removal of the negative endpoint, projection through the genuine constant span produces a full-rank coherent image of degree -20 in a constant rank-four bundle. Its preservation by the actual connection forces the image to be saturated and constant, contradicting its degree. No generic full-rank projection is assumed to be saturated without this differential argument.

For ce, P814 forces the actual constant D and projected standard `Sym7 W O(-1)` subsystem. P826 computes the full constant span and exact intersection, producing an injective rank-five sheaf map of degree -22 into a constant rank-five bundle. Its determinant would be a nonzero invariant of degree 22, whereas

    Sym22 W=2A+V+P+2D

has no invariant. The determinant argument retains, rather than discards, any torsion cokernel. The degree-22 character was independently recomputed. The manuscript assigns ce once to P826. P828's alternative proof of the same ce exclusion is not another source removal.

## 5. Complete bf and bc branch coverage

### 5.1 bf

The top coefficient is `P+D`, of dimension nine. In rank two, an image I with determinant defect delta satisfies

    9 <= h0(I(2))=16-delta.

Hence delta is at most seven, and invariance forces delta zero. P814's complete internal-image partition is zero or saturated `O(-10)`. The zero case is excluded by the polar obstruction. P830 covers every nonzero combination of the quintic and scalar internal channels, not merely one selected component. It forces the quartic V subsystem and the actual quotient `F/F^-=V O`; an onto map from this quotient to `O(4)+O(6)` cannot exist because its O(4) row is zero equivariantly. Rank two is completely excluded.

In rank one, the nine independent top sections force the saturated line to have degree at least six. It is therefore the O(6) direct summand, and the map is the full degree-eight evaluation system. Its kernel is `(Wp+T) O(-3)`.

The bf interface removes the negative endpoint and shows the lower T-to-O(4) channel is nonzero: a lone degree-twelve scalar section cannot be everywhere onto. The exact cohomology budget then forces

    K1=(Wp+T) O(-3)+V O(-4)+Wp O(-5)+O(-8).

The lower-support possibilities were independently checked. Its Wp top row supplies the entire O(4) derivative summand. Any nonzero complementary row from T, V, or Wp supplies the full O(2) summand. If all are zero, the raw quotient is O(4) and

    K2=(2V+P) O(-4)+Wp O(-5)+O(-8).

The next actual target is O(2), whose twist-four sections `V+P` cannot contain `2V+P`. Thus the exact quotient is necessarily `K1/K2=O(2)+O(4)`, with no hidden divisor correction. Section 7 below verifies its transfer to the universal theorem. Rank one is consequently excluded as well.

### 5.2 bc

The seven-dimensional top coefficient is `V+P`. In rank two the same generation estimate gives delta at most nine and therefore zero. P814's rank-two bc exclusion applies with its onto hypothesis established.

In rank one, a saturated equivariant line has even degree at most six. Degree six is the direct O(6) summand and fails strict-top because `Sym8=P+D` has no V. Degrees at most two have fewer than seven twist-two sections. Degree four is therefore forced. Its off-diagonal map to O(6) vanishes because there is no degree-two invariant. The actual image is the complete O(4) sextic system.

The bc proof then exhausts the lower `T O(-3)->O(6)` channel:

1. If zero, `H0(K1(3))=2T`. These twelve independent top sections cannot factor through an equivariant rank-one image in `O(2)+O(4)`. Rank-two generation gives delta at most two, hence zero. The endpoint rank bound at most two forbids an additional O(-12) component once both positive direct summands are contained.
2. If nonzero, the cohomology budget forces `K1=T O(-3)+(V+P) O(-4)+O(-8)`. All maps to O(-12) vanish by degree. The nonzero top T derivative has exactly three patterns: both positive rows, only O(2), or only O(4).

Both nonzero rows force rank two; a rank-one saturation could not project to both rows. The defect bound is less than twelve, so the image is full. If the T top supplies only O(2), a nonzero P-to-O(4) row completes the target. If that row vanishes, the final scalar row is either zero or a nonzero multiple of f12. The respective raw images are `O(2)` and `O(2)+O(-8)`. Their next kernels have top `V+P+D`, while the next actual target has only D at twist four. Both alternatives are impossible. In particular, the length-twelve defect is retained and the latter next target is `O(0)+O(-10)`, not the saturation's twist.

If T supplies only O(4), its exact kernel is `V O(-4)+Wp O(-5)`. Any nonzero V or P sextic row to O(2) completes the target. If both vanish, the remaining scalar row is zero because degree ten has no invariant. The next kernel has top `2V+P`, which cannot inject into `V+P`. The extensions used for this kernel have ordinary cohomology degrees at least -1, in the correct subbundle-minus-quotient orientation, and therefore split.

Thus both lower-T alternatives and every top-T/defect branch force exactly `K1/K2=O(2)+O(4)`. The universal split theorem then excludes rank one. There is no omitted zero-lower-channel branch.

## 6. Complete bb coverage

Here the top coefficient is P of dimension four. R814 excludes both possible rank-one images for the split target: the O(4) sextic line and O(6) octic line. Both are basepoint-free. The former gives the forbidden quadratic Gauss-gap case; the latter gives an actual constant D projection whose remaining top would inject `2T` into `Wp+T`. Rank zero was already excluded.

For rank two, the dimension-four case must not inherit the stronger saturation argument used for bf and bc. The correct bound is

    4 <= h0(I(2))=16-delta,

so only delta zero or twelve is possible. For delta twelve, I has rank two, degree -2, and twist-two section representation exactly P. The center-even rank-two bundles of degree -2 generated after twist two are `O(-2)+O`, `W O(-1)`, and `Wp O(-1)`. The first two have section character `1+A`; only the last has P. Therefore the defective image would have to be `Wp O(-1)`.

Its map to O(4) is identically zero because Wp is absent from `Sym5=T`. Its map to `O(4)+O(6)` consequently has generic rank at most one, contradicting the rank-two assumption. This is the split-specific reason the defect-twelve branch is impossible. No balanced torsion exclusion is substituted.

The top is therefore onto. PR821 gives exactly two actual constant-span alternatives: the nine-dimensional degree-eight evaluation system and the twelve-dimensional P-conic system. P836 excludes both. The first contradicts the quotient degree of an actual preserved horizontal lattice. The second uses the complete bounded support of the positive-endpoint transform, then the actual linear top's constant-span dimension bound. It is not an exclusion of only the first span type. Thus rank one, onto rank two, and defective rank two are all covered for bb.

## 7. Exact shared interface, split descent, and independence

Both rank-one source proofs establish, before invoking the source-free theorem,

    K1/K2=O(2)+O(4),
    rank K2=12, deg K2=-60, maxdeg K2<=-4,
    chi_G(K2(4))=V-A,
    chi_G(K2(5))=-W+Wp+2T.

These Euler characters follow from exact subtraction of the quotient characters `V+2P+D` and `Wp+S+2T` from those of K1. They do not presume an additional H1 vanishing.

The geometric condition is also present, not merely the abstract characters. Since K1 is saturated in the same constant ambient bundle, the quotient of `H O/K2` by `K1/K2` is the locally free `H O/K1`. Thus

    (K1/K2)(-2)=O(0)+O(2)

is an actual subbundle of `(H O/K2)(-2)`. Gauss factorization identifies the induced map from K2 with its actual derivative through this monomorphic target inclusion. Its kernel and raw image are therefore precisely the actual ones. Every later kernel is saturated in the original constant bundle even when its derivative image is defective in its target. The maximal profile-(1,1) endpoint gives derivative rank at most two, and the outward ranks do not increase. These are all the universal theorem's hypotheses.

The split descent was inspected independently, including its non-balanced branches. At the initial interface a V top row supplies all O(2). Rank one leads to exactly two necessary small-support types, both contradicted by strict-top. A rank-two defect has raw image `O(2)+O(-d)`; invariance and the H1 budget force any positive d to be twelve, where the character is the nongenuine `A-V`. Thus the first quotient is exactly `O(0)+O(2)`.

The following K3 support has eleven supported lower blocks, eight necessary types, and four strict-top survivors. These lists were independently recovered by bounded character recurrence, parity, and the stated small H1 budget. The four survivors include `T O(-5)+(V+1) O(-8)`, which yields the essential new split branch

    K4=D O(-6)+O(-8)+Wp O(-11).

The separate-row, basepoint-free and Ext arguments force the subsequent full split quotients; the new branch is not dropped. At the terminal steps both possible f12 defects are retained:

- In the surviving b branch the raw image is `O(-8)+O(-18)`, leaving the actual kernel `W O(-9)`. Its next target is `O(-10)+O(-20)`, so every derivative component vanishes by degree. A negative saturated horizontal kernel is impossible.
- In the new d branch a nonzero f12 row gives raw image `O(-4)+O(-18)` and kernel `(A+1) O(-8)`. The next target is `O(-6)+O(-20)`, whose twist-eight sections are only A, violating strict-top. The zero-f12 alternative is separately contradicted by the same missing trivial coefficient.

In neither case is the defective image replaced by its saturation to form the next derivative target. This checks the precise part of the descent most sensitive to torsion and to the change from balanced to split targets.

The dependency graph is noncircular. The bf and bc initial arguments independently establish the actual interface; the universal theorem assumes neither source exclusion nor a full-label exclusion. Its earlier references supply bounded characters, evaluation kernels, and actual-kernel principles, not a balanced quotient. P830 uses only the profile-free quartic construction before its split contradiction. P826 and P828 use P814's forced actual constant subsystems. P836 uses PR821's onto classification, not the present label conclusion. No missing case is proved by assuming the conclusion it is needed to establish.

## 8. Final exhaustion and verification boundary

In the exact original order the complete assignments are

    ff: inherited strict-top exclusion;
    ef: P814;
    ee: inherited strict-top exclusion;
    cf: P828;
    ce: P826, once;
    cc: inherited strict-top exclusion;
    bf: P814/P830 for rank two, Psplit for rank one;
    be: P814;
    bc: P814 for rank two, Psplit for rank one;
    bb: R814 for rank one, PR821 for the defect, P836 for onto rank two.

Each assignment matches the original tuple, label, quotient pair, and original defect. No unexamined top rank, internal channel, lower T channel, constant-span alternative, or divisor correction remains. Since every actual realization must lie in this necessary list, the exclusion of **G3.11.863639aa192e** follows.

The audit used immutable file hashes, equality of a fixed finite list, universal bundle arithmetic, bounded abstract representation identities, and structural actual-connection arguments. No selected actual HM/source coefficients, parameters, points, evaluated derivatives, matrices, instance ranks, selected-model experiments, scans, or unapproved large computation were used. No external state was changed. The three inherited prunings are not recounted, ce is not double-counted, and no frontier arithmetic or conclusion beyond this one stable label is asserted.
