# Spike burn: execution and verification closeout

Frozen research cutoff: **2026-10-23 04:52:27 UTC**, through PR **#911**. This report inventories published results and their evidence; it does not restart execution, merge PRs, or certify the original repair. Counts are scoped to the public campaign window, not all repository history.

## 1. Bottom line

The burn produced substantial bounded research, usable supporting Lean algebra, and safer verification infrastructure. It did **not** produce a complete Horrocks–Mumford/Weil-class repair, an actual fixed-HM source2 exclusion, an authenticated/evaluated physical response, or an end-to-end Lean proof of the main target.

- **108 open draft PRs**, **108 distinct published head commits**, after the public startup notice and through #911. Each PR's current metadata reports one commit relative to its own base. This is a publication inventory, not a total of every local/transient commit, independent theorem, successful experiment, or distinct underlying mathematical idea.
- **13 Lean packages / 66 distinct checked supporting declarations.** This closeout independently fetched all 13 final source files, their axiom outputs and verification records. Every fetched source SHA256 matches its verification record. There are 70 printed axiom entries but only 66 unique declarations because #883 rechecks four declarations from #879.
- Runtime work reached reviewed initialization, namespace/factory equivalence, and a reported completed **primitive-CG prerequisite unit**, but **not** completion of all 55 harmonic plus 10 trace maps, the eight-prerequisite aggregate, sparse/dense full-source verification, or a selected actual-HM experiment.
- Written mathematical progress and frontier accounting must remain separate from Lean certification. The final frontier totals belong to the companion frozen-frontier reconciliation; this document does not infer missing pair counts from individual proof announcements.

The [campaign plan #805](https://github.com/Akilleez-QA/read-em-and-weep/pull/805) explicitly says that PR counts, reviews and elapsed compute are not substitutes for checked mathematical results.

## 2. Window and publication inventory

The public [startup notice](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6354195527) is timestamped **00:12:44 UTC**. That is the earliest verified public announcement of this burn, not an independently established first CPU/process start. The frozen cutoff is **04:52:27 UTC**, an elapsed public coordination window of **4 hours 39 minutes 43 seconds**.

- First PR opened after that notice: [#804](https://github.com/Akilleez-QA/read-em-and-weep/pull/804), **00:16:15 UTC**.
- Campaign plan [#805](https://github.com/Akilleez-QA/read-em-and-weep/pull/805): **00:18:24 UTC**. Counting from the plan rather than startup gives **107 PRs, #805–#911**.
- Last included PR: [#911](https://github.com/Akilleez-QA/read-em-and-weep/pull/911), created **04:52:03 UTC**, [announced at 04:52:26 UTC](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6357675476), immediately before the cutoff. Its near-cutoff arrival is included explicitly rather than silently omitted.
- The four earlier date-local PRs #800–#803 are context, not included in the 108-PR post-startup count.
- All #804–#911 were open drafts and unmerged at inventory time. Branch-prefix attribution is **22 codex / 26 null / 60 mr-slop**. This reflects repository branch naming, not independent verification of the number of people, agents, or simultaneously running workers.

Primary-deliverable classification, assigning each PR exactly once:

| Primary purpose | Count | PRs |
|---|---:|---|
| Written mathematical research | 70 | All remaining #804–#911 after the categories below; includes deductions, conditional interfaces, reductions, feasible-family constructions and failed-route certificates, not 70 independent completed theorems |
| Frontier accounting and integration | 15 | #807, #832, #833, #837, #843, #849, #851, #855, #857, #863, #886, #890, #898, #899, #910 |
| Supporting Lean formalization | 13 | #852, #853, #864, #865, #871, #872, #873, #878, #879, #880, #883, #896, #902 |
| Runtime, compiler and regression infrastructure | 6 | #812, #824, #827, #831, #835, #841 |
| Plan, evidence correction and candidate handoff | 4 | #805, #809, #810, #820 |
| **Total** | **108** | **#804–#911 inclusive** |

These are accounting categories, not mutually exclusive technical properties: for example, the campaign plan and frontier packages also contain tests, and written proof packages may contain bounded arithmetic diagnostics. The separate `PUBLICATION-INVENTORY.csv` records every title, timestamp, head SHA, category, branch prefix and PR link.

## 3. Evidence levels and closeout method

This report distinguishes:

1. **Metadata directly re-read for closeout.** PR creation timestamps, heads, bases, draft/open state and commit counts were fetched through the repository connector.
2. **Published execution evidence directly inspected.** Lean source files, verification JSON and axiom outputs were fetched at immutable head SHAs. Local read-only arithmetic/string/hash checks established source-hash agreement and distinct declaration counts. The closeout did **not** rerun Lean, install tools, start the swarm, or replay mathematical jobs.
3. **Written deduction and review evidence.** PR bodies, immutable proof references and public coordination reports document deductions and independent written reviews. This supports accurate attribution of what was proved/reviewed, but is not a new full ancestry audit or proof-assistant certification.
4. **Readiness, static, synthetic or conditional evidence.** Successful import/equivalence/synthetic tests establish only their stated scope. A partial log, empty log, disabled execution lock, absent actual input or supplied theorem premise remains an open gate.

All 13 Lean packages report a source compilation and a separate importing axiom check on the **same** pinned toolchain. No package claims Comparator or an independent second kernel. A separate importing check is useful verification, not an independent implementation of Lean's kernel.

## 4. Execution chronology and substantive pivots

### 00:12–00:49: ownership, conditional interfaces and a failed route closed

The startup reserved non-overlapping dependency and source-interface work, with the existing source-exclusion lane retained by its owner. A prospective residual-extension task was retired immediately after [#804](https://github.com/Akilleez-QA/read-em-and-weep/pull/804) supplied the actual degree-28 argument; the [pivot notice](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6354259789) says no new theorem draft on that duplicate exclusion was produced.

The principal early source2 results were:

- [#808](https://github.com/Akilleez-QA/read-em-and-weep/pull/808): the conditional equivariant fixed-pencil commutant map has domain dimension 113 and target dimension 153; adding three weighted vertex traces gives the stated conditional 156×113 rank-111 radical extractor. These are structural/representation deductions under pinned hypotheses, **not an evaluated actual HM rank**.
- [#811](https://github.com/Akilleez-QA/read-em-and-weep/pull/811): negative-pencil invariance throughout the specified nonzero three-channel monad torus, using a common negative-variable scale and graded rescaling. This does not transfer truncated endomorphisms to the full five-variable module.
- [#812](https://github.com/Akilleez-QA/read-em-and-weep/pull/812): a universal formal compiler retaining all 153 tensor coordinates as indeterminates, with independent polynomial replay rather than a specialized source test.
- [#815](https://github.com/Akilleez-QA/read-em-and-weep/pull/815): weight-16 affine square compatibility retaining the full qZ correction and the exact missing physical response block. It isolates, rather than supplies, the authenticated contractions/response rows and corrected source value.
- [#818](https://github.com/Akilleez-QA/read-em-and-weep/pull/818): the actual Euler relation forces scalar full-module endomorphisms, so proper source2 projectors and nonzero radical maps cannot lift. **Nonextension is expected and is not a source2 contradiction.** The distinct positive-quadratic filtration criterion remains conditional on a further extension premise.

[Plan update #820](https://github.com/Akilleez-QA/read-em-and-weep/pull/820) records retirement of the invalid projector/radical-to-full-module exclusion strategy. It preserves the useful negative result rather than relabeling the route failure as exclusion.

### 00:29–01:35: candidate preservation and bounded readiness

[#810](https://github.com/Akilleez-QA/read-em-and-weep/pull/810) publishes the previously local candidate interface with **86 files: 80 mathematical payload files plus six manifest/evidence documents**, and a **67-file minimum executable/hash closure**. Static hash completeness did not turn it into a source solution.

Inherited evidence was explicitly corrected:

- q65's old coefficient log stops after **27 harmonic checks**, has no trace checks and no exit receipt.
- Sparse-adapter and polarization logs were empty.
- The dense-bridge log lacked its terminal skew-pair PASS. [#809](https://github.com/Akilleez-QA/read-em-and-weep/pull/809) corrects that status to **PARTIAL**.
- A separate completed independent audit is version/hash-specific; it cannot replace the missing producer run or transfer to changed dependencies.

The work therefore extracted explicit factories and reviewed execution contracts instead of launching historical top-level generators or old family solves. Detailed readiness outcomes are in §6.

### 01:38 onward: switch from diagnostic expansion toward Lean

The [01:38:20 coordination message](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6355303054) reports a clarification toward Lean, says two static diagnostic units had terminated, and freezes further diagnostic expansion while small formal units are selected. This report treats that as a **collaborator-reported change of direction**, not independent evidence of the originating instruction.

The first published Lean packages were [#852](https://github.com/Akilleez-QA/read-em-and-weep/pull/852) at **02:08:34** and [#853](https://github.com/Akilleez-QA/read-em-and-weep/pull/853) at **02:09:34**. The last was [#902](https://github.com/Akilleez-QA/read-em-and-weep/pull/902) at **04:25:00**. Subsequent work increasingly checked exact written interfaces and refused unnecessary generic wrapper PRs where pinned mathlib already supplied the algebra; see the [04:31 follow-up](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6357426637).

### Parallel written research: important new boundaries, not actual evaluation

The following sequence materially refined what a valid physical source completion must establish:

- [#816](https://github.com/Akilleez-QA/read-em-and-weep/pull/816): typed nonclosed frame-transfer defects, with the failure of a map to commute with differentials retained.
- [#866](https://github.com/Akilleez-QA/read-em-and-weep/pull/866): mixed contractions create exactly the normalization defect −a³hη; paired changes cancel it. In its broader setting gluing only makes η global and does not remove the abstract 13-dimensional reconstruction ambiguity. It did not construct 13 realized HM freedoms.
- [#889](https://github.com/Akilleez-QA/read-em-and-weep/pull/889): under prior coherent equivariant cubic-family authentication, the error family has ten channels and two full source-family observations separate them. The unrestricted 13-dimensional trace space is not thereby reduced for arbitrary packets.
- [#891](https://github.com/Akilleez-QA/read-em-and-weep/pull/891): exact conditional observation kernels and a generic separating parameter, without selecting or evaluating an actual parameter.
- [#894](https://github.com/Akilleez-QA/read-em-and-weep/pull/894): supplied-source membership must precede trace normalization. Canonical/compared b and prescribed W leave **27 compatibility slots**; allowing b to vary leaves **28**. The compatible W cohomology-family fiber is **7-dimensional**. Ten trace channels cannot certify the full membership defect.
- [#900](https://github.com/Akilleez-QA/read-em-and-weep/pull/900): full cohomology-family observations separate the canonical defect sector, with missing-channel weights 8/8/11 and axis/square image dimensions 16/19 over eight shared channels. This is not compression through ten trace coordinates.
- [#903](https://github.com/Akilleez-QA/read-em-and-weep/pull/903): even regular complex-algebraic nonlinear maps from the full 27-dimensional defect sector to ten scalars retain a zero fiber of local dimension at least 17. Restricted-admissibility or nonholomorphic procedures are outside that theorem.
- [#904](https://github.com/Akilleez-QA/read-em-and-weep/pull/904): compatible W changes leave the actual source response unchanged; full norm equality is on **4Q**, and response equality is on **Q**, not in the ambient or fifth-order neighborhood. The row descends only to res_Q(dC⁰₄), not arbitrary ambient S. Thus W freedom cannot tune the response or absorb an unrelated normalization mismatch.
- [#908](https://github.com/Akilleez-QA/read-em-and-weep/pull/908): a constructive W-free source-leg route. Exactness of global complexes gives im(d_Q)=res_Q(im d₄); solve on the cone, lift the primitive globally, then recover closed W=(S−dE)/q. This does not authenticate an unrelated prescribed W and does not eliminate the full lower ambient y or physical contraction/marking obligations.
- [#909](https://github.com/Akilleez-QA/read-em-and-weep/pull/909): a **stronger, conditional realized subclass** with regular full-cover, same-contraction tensor compatibility has η=aξ, with ξ in Sym¹²(U)⊗O(−2). If η glues, cancellation and section vanishing force η=0. This removes separate calibration only in that subclass; it does not contradict the earlier unrestricted ambiguity, prove gluing, or authenticate the packet.

Selected reported test outcomes include #866: **115 checks / 16 negative controls**, #889: **122 / 5**, #894: **127 / 7**, #904: **66 / 8**, and #908: **108 / 8**, in normal and optimized Python modes where specified. These are **bounded diagnostics accompanying written arguments**, not Lean theorem counts, actual source tests, or an end-to-end proof.

The structural research also retained genuine feasible abstract families. In particular [#869](https://github.com/Akilleez-QA/read-em-and-weep/pull/869) and [#876](https://github.com/Akilleez-QA/read-em-and-weep/pull/876) prevent continuing to treat the same necessary conditions as a contradiction. Abstract feasibility is not fixed-HM realization, but it is a valid reason to move the next question to actual-source compatibility.

## 5. Lean deliverables: exact count, scope and remaining premises

Pinned toolchain in all 13 inspected verification records:

- Lean **4.34.1**, compiler commit **5045d0056413266e57c625dcd7c365b10e377c52**.
- mathlib **d13f23b723b8a846827a245b89c10fc7d3f11612**.
- Final source SHA256 matched the fetched immutable source in **13/13** packages.
- Each package records successful source compilation and successful importing/axiom check.
- Distinct audited declaration count: **7+10+4+3+3+3+3+3+4+6+12+4+4 = 66**.
- All listed axiom closures are subsets of **propext, Classical.choice, Quot.sound**. #879 uses only propext and Quot.sound.
- A lexical scan of the fetched final sources after block-comment removal found no `sorry`. This scan supplements, and does not replace, the published compilation and axiom evidence.

| PR | New checked declarations | Module | Formalized result | Not supplied |
|---|---:|---|---|---|
| [#852](https://github.com/Akilleez-QA/read-em-and-weep/pull/852) | 7 | [SourceTraceFactorization](https://github.com/Akilleez-QA/read-em-and-weep/blob/4829a53c90f5e9213d7fd197e781acb1649a6e7c/lean/OAI/AlgebraicGeometry/HorrocksMumford/SourceTraceFactorization.lean) | Conditional kernel-to-image factorization; uniqueness on range(d); exactness and same-source independence. | Does not supply actual monad exactness, physical response, or graded source data. |
| [#853](https://github.com/Akilleez-QA/read-em-and-weep/pull/853) | 10 | [Source2TraceKernel](https://github.com/Akilleez-QA/read-em-and-weep/blob/a0834508e3a1772763f28ca88edd98e3d161319c/lean/OAI/AlgebraicGeometry/HorrocksMumford/Source2TraceKernel.lean) | Five reconstruction identities, two trace-coordinate injectivity results, and three composition-kernel results. | Actual HM normal form and diagonal map remain to be identified; not an arbitrary-pencil radical theorem. |
| [#864](https://github.com/Akilleez-QA/read-em-and-weep/pull/864) | 4 | [FirstNormalCorrection](https://github.com/Akilleez-QA/read-em-and-weep/blob/827c5300d377ff59a64c01f34ba4d409975e22b5/lean/OAI/AlgebraicGeometry/HorrocksMumford/FirstNormalCorrection.lean) | Both triangular frame inverses, full conjugated first-normal commutator, and trace cancellation for 2×2 matrices. | No physical-frame identification, global gluing, coefficient extraction, or source solvability. |
| [#865](https://github.com/Akilleez-QA/read-em-and-weep/pull/865) | 3 | [QuadraticProjectorCompatibility](https://github.com/Akilleez-QA/read-em-and-weep/blob/80f241711bcd3a053268de6a83c8aee68403ebbf/lean/OAI/AlgebraicGeometry/HorrocksMumford/QuadraticProjectorCompatibility.lean) | Two-off-diagonal-block criterion, image/kernel criterion, and family version for supplied idempotents and a linear map. | No actual positive quadratic action, extension, or source2 exclusion. |
| [#871](https://github.com/Akilleez-QA/read-em-and-weep/pull/871) | 3 | [NonclosedFrameTransfer](https://github.com/Akilleez-QA/read-em-and-weep/blob/ef90f1edc66488be999ff85e69c6fd8409045f85/lean/OAI/AlgebraicGeometry/HorrocksMumford/NonclosedFrameTransfer.lean) | Typed nonclosed transfer defect with ten module types; closed limit; exact-cochain projection. | Actual complexes, contractions, markings, twists, and physical rows are inputs, not constructed. |
| [#872](https://github.com/Akilleez-QA/read-em-and-weep/pull/872) | 3 | [FrameTransferCocycle](https://github.com/Akilleez-QA/read-em-and-weep/blob/4f10e244cb4dc28438ed1fcba7877df79e83d465/lean/OAI/AlgebraicGeometry/HorrocksMumford/FrameTransferCocycle.lean) | Transition composition, inverse-pair identities, and typed triple-overlap defect cocycle. | Not global sheaf descent or construction of physical contractions. |
| [#873](https://github.com/Akilleez-QA/read-em-and-weep/pull/873) | 3 | [HeterogeneousAffineSourceResponse](https://github.com/Akilleez-QA/read-em-and-weep/blob/73359dd41f3729cfb6da2207b6d282a3489294f2/lean/OAI/AlgebraicGeometry/HorrocksMumford/HeterogeneousAffineSourceResponse.lean) | Norm defect, equality iff multiplication-kernel membership, and stronger equality under explicit injectivity. | Distinct trace/norm modules preserved; physical transports and source-image realization remain inputs. |
| [#878](https://github.com/Akilleez-QA/read-em-and-weep/pull/878) | 3 | [TensorProjectorCompatibility](https://github.com/Akilleez-QA/read-em-and-weep/blob/5af660702fafabb26c8f7897b1c4ba5caa7d590e/lean/OAI/AlgebraicGeometry/HorrocksMumford/TensorProjectorCompatibility.lean) | Actual abstract id⊗p construction, idempotence, all-slice/bundled equivalence, and cross-term criterion. | Actual HM projector, Sym² realization, and cross-term vanishing remain unconstructed. |
| [#879](https://github.com/Akilleez-QA/read-em-and-weep/pull/879) | 4 | [PencilCommutant](https://github.com/Akilleez-QA/read-em-and-weep/blob/634ca192ab8f64cf3d779a9194382e1458cdad7a/lean/OAI/AlgebraicGeometry/HorrocksMumford/PencilCommutant.lean) | Unrestricted tensor-pencil defect, full kernel equations, identity and composition closure. | No actual equivariant representations, 113/153 dimensions, rank, or exclusion. |
| [#880](https://github.com/Akilleez-QA/read-em-and-weep/pull/880) | 6 | [MixedNormalizationAdapter](https://github.com/Akilleez-QA/read-em-and-weep/blob/a2bfde025e55aca072366e1b565af761293bcac5/lean/OAI/AlgebraicGeometry/HorrocksMumford/MixedNormalizationAdapter.lean) | Full-range comparison, source-only cone error, paired cancellation, mixed defect/compensation, and equality criteria. | Physical/global comparison and correct normalization are supplied certificates; source rows accept only S−qW in the certified differential image. |
| [#883](https://github.com/Akilleez-QA/read-em-and-weep/pull/883) | 12 new | [PencilCommutantEquivariant](https://github.com/Akilleez-QA/read-em-and-weep/blob/4b9baa6d39e32fe4cfec59a65ced59cb93186847/lean/OAI/AlgebraicGeometry/HorrocksMumford/PencilCommutantEquivariant.lean) | Supplied-action End_G/Hom_G restriction, kernel/comap and ambient-intersection criteria; equivariance/action helpers. | All actions and both tensor-equivariance hypotheses explicit; no actual HM identification, dimension or rank. |
| [#896](https://github.com/Akilleez-QA/read-em-and-weep/pull/896) | 4 | [SourceFamilyMultiplier](https://github.com/Akilleez-QA/read-em-and-weep/blob/979b82f3ddac3bf291685523b0b61d8e6d7b02e8/lean/OAI/AlgebraicGeometry/HorrocksMumford/SourceFamilyMultiplier.lean) | Varying quartic multiplication on homogeneous binary forms; degree-16 quadratic observation; response injectivity; nonzero cubic scalar weight. | No representation dimensions, two-orbit geometry, coherent physical family, or calibration. |
| [#902](https://github.com/Akilleez-QA/read-em-and-weep/pull/902) | 4 | [MultiplicityFreeCyclicSupport](https://github.com/Akilleez-QA/read-em-and-weep/blob/68d7daa27700918702c395cf788caeaa7ae83d3e/lean/OAI/AlgebraicGeometry/HorrocksMumford/MultiplicityFreeCyclicSupport.lean) | Schur/coordinate helpers and exact cyclic support for three pairwise nonisomorphic simple modules; cyclic span is top iff every coordinate is nonzero. | Actual decomposition, group-algebra/orbit-span application, dimensions, generic-open existence, and physical packet remain separate. |

The word **declarations** is intentional. #883's 12 includes action/membership/evaluation helpers and rechecks four earlier declarations without increasing the total. #896 includes one evaluation formula plus three result theorems. #902 includes two helpers plus two cyclic-support results. Definitions, repeated imports, axiom printouts, and dependent applications are not counted as new independent mathematical theorems.

Every package includes a source file plus README, review, importing check, axiom output, hashes and verification JSON. Their theorem statements remain conditional and reusable; putting them in a Horrocks–Mumford namespace does not instantiate their actual geometric premises.

## 6. Runtime and verification readiness: what actually passed

| Artifact / evidence | Positive result | Boundary / remaining gate |
|---|---|---|
| [#810 candidate handoff](https://github.com/Akilleez-QA/read-em-and-weep/pull/810) | 86-file static inventory; all 80 frozen payload hashes preserved | Candidate completeness only; historical producer logs remain partial/empty |
| [#824 bounded supervisor](https://github.com/Akilleez-QA/read-em-and-weep/pull/824) | Nine independently run synthetic fixtures, including timeout, sampled-RSS stop and cleanup behavior | No hard address-space cap; no aggregate CPU cap; no guaranteed RSS overshoot bound; not a mathematical verifier |
| [Namespace-only smoke report](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6354836168) | Exit 0; all 80 hashes and 26 error schemas retained; terminal marker explicitly says downstream checks remain unrun | No historical generator, source solve or q65 family map |
| [#827 receipt contract](https://github.com/Akilleez-QA/read-em-and-weep/pull/827) | 65 stable IDs (55 harmonic + 10 trace), eight prerequisite groups; 22 negative metadata cases; synthetic 73-receipt CLI audit | Production execution lock disabled; synthetic complete coverage is not executed mathematical coverage |
| [#831 explicit shared factories](https://github.com/Akilleez-QA/read-em-and-weep/pull/831) | 144 exports; 116 closure bindings; 20 lexical assertions retained; six static tests; bounded factory smoke passed | No family loop, graded-module construction, actual source solve or q65/sparse verification in this PR |
| [#835 explicit initializer](https://github.com/Akilleez-QA/read-em-and-weep/pull/835) | 150 outer names, 32 nested names, 46 bindings and 40 formal probes matched; six extraction tests passed | Sparse integration, full attribute equivalence, constructor bypass/tripwire gates and downstream verification remain distinct |
| [Ordinary runtime + primitive-CG report](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6355131493) | Ordinary API/binding/default-builder/cold-cache graded-module smoke passed. Primitive-CG unit checked five tensor spaces, 15 inclusions, 38 ordered cross-zero identities and five reconstructions; exit 0 and final Q65_UNIT_COMPLETE marker reported | This is one global prerequisite unit, not 65 completed maps. At that report, portable publication awaited a documentation-pin compatibility fix; aggregate unlock remained disabled. No later published aggregate completion is established here |
| [#841 full-CLI adversarial regressions](https://github.com/Akilleez-QA/read-em-and-weep/pull/841) | 76 expected outcomes: five synthetic controls and 71 exact adversarial rejections, independently reproduced | A forged-producer probe explicitly preserves the producer-trust boundary; receipt acceptance is not proof of a producer's mathematics |
| [#812 formal commutant compiler](https://github.com/Akilleez-QA/read-em-and-weep/pull/812) | Six tests; all 113 unknown directions; independent formal replay of 17,628 coefficient entries; broken sign/symbol/trace controls rejected | All 153 tensor entries remain indeterminates; no actual tensor authentication, common-pencil compatibility or actual instance rank |

The [aggregation review](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6355027458) records a crucial wiring distinction: `validate_receipts` checks metadata, while the full CLI separately checks actual log bytes and the final nonblank completion marker. Calling only the metadata helper is not complete evidence validation.

### Limits, failures and repairs retained honestly

The published supervisor defaults were **60 CPU seconds per process, 75 wall seconds, sampled aggregate RSS 1.5 GiB**. Those are limits for individual bounded jobs, not measured campaign resource totals. The plan's separate 90-minute review envelope and two-heavy-job ceiling were proposed scheduling defaults, explicitly not proof of the external run's actual configuration.

Reported and retained failures include:

- Unsupported hard address-space limiting, replaced by an explicitly weaker sampled process-group RSS guard rather than a claim of equivalent enforcement.
- A PID-reuse race repaired before supervisor publication by retaining the leader until signaling completed.
- Two initializer reviewer-harness failures preserved in #835, with no candidate mismatch reported.
- An unnecessary documentation hash pin blocking q65 runtime publication compatibility; successful original receipts were kept immutable rather than rewritten as if they executed a later package.
- Lean memory failures before import reduction/module-mode compilation; the [first Lean result report](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6355554816) says the same RSS guard was retained.
- Missing dependency-cache and elaboration repairs in later Lean modules; warnings are documented rather than silently presented as clean runs.
- #896's first attempt needed a noncomputable definition; #902's first attempt needed explicit false elimination, a dependent-module argument and an endomorphism type annotation. Their published verification records retain the failed source/logs and final successful repairs.

A resource stop, dependency failure, or incomplete log is inconclusive about a mathematical claim. Conversely, successful bounded compilation is not evidence of actual-HM realization.

## 7. What remained unfinished at the cutoff

1. **Main result:** no complete checked repair, no end-to-end Lean proof, no global higher-integrability conclusion. The actual fourth boundary modulo the second-symbol image and the higher lifting target remain open; neither rho16 nor beta4 was evaluated.
2. **Actual-source identification:** actual HM representations/tensors/actions, their equivariance, exact cohomology identifications and the relevant source2 realization remain separate from generic commutant and trace algebra.
3. **Physical response realization:** actual contractions/markings, full lower ambient y, gluing, compatible normalization and full-source membership still need to be supplied together. #908 and #909 sharpen the route but do not instantiate all premises.
4. **Prescribed-W versus W-free distinction:** #908 constructs a compatible W via a source-leg route; it does not validate an arbitrary supplied W. #894's membership gate remains for that problem.
5. **Geometric formalization gap:** supporting Lean modules have not formalized all actual cone/coefficient realizations, representation/dimension calculations, source-exclusion proofs, or the complete chain to the withdrawn target.
6. **q65/source verification gap:** no evidenced aggregate completion of all 65 maps and eight prerequisites, sparse/dense full A/B/U/c checks, or actual-instance solve. Preserve all historical partial/empty logs and successful narrow receipts without promoting one into another.
7. **Accounting timing:** [#910](https://github.com/Akilleez-QA/read-em-and-weep/pull/910) was the last integrated checkpoint at cutoff: 178 necessary pairs with four registered labels, explicitly excluding #907 from that bounded snapshot. #911 then supplied separate whole-label exhaustion immediately before cutoff. Final reconciled pair/label totals must come from the companion integration, not casual subtraction here.
8. **Review depth:** newer packet reviews authenticate exact local inputs and bounded claims; they inherit some deeper ancestry. “Independent written review passed” is not synonymous with every ancestor independently replayed or Lean-certified.

No future execution is implied by this unfinished list.

## 8. Unknowns and claims deliberately not made

- The technical cause of the reported stall is **not established** by the public evidence inspected. Lack of a new publication is not proof of a dead process, resource exhaustion or a mathematical impasse.
- No reliable campaign-wide cost, CPU-hour, memory-time, worker-count, or utilization total is available from this inventory. Individual smoke/compile receipts cannot be added into such a total without a complete run ledger.
- The public startup timestamp does not prove the precise first process start; the frozen cutoff does not by itself prove the exact termination time of every descendant.
- The 108 unique PR heads do not count private, abandoned, overwritten, or unpushed commits.
- No merges, upstream solution submission, selected actual coefficients/points/ranks, or complete-repair announcement is evidenced by these deliverables.
- This execution-inventory audit performed metadata, source-byte, hash and count checks only. It did not rerun Lean or the stopped mathematical jobs. Separate closeout accounting replay and documentation publication are recorded in the status paper.

## 9. Reproducible public inventory

- [PUBLICATION-INVENTORY.csv](data/PUBLICATION-INVENTORY.csv): complete #804–#911 publication index with immutable heads and primary-purpose categories.
- [Lean verification index](data/lean-verification-index.json): immutable source hashes and artifact paths for the thirteen packages.
- [Final burn metrics](data/burn-closeout.json): exact separate counters and their scope.

The source and receipt links above lead to the underlying public immutable records. No private runtime data or credentials are included. The final frontier is reconciled separately in [PR912](https://github.com/Akilleez-QA/read-em-and-weep/pull/912), after the research cutoff.
