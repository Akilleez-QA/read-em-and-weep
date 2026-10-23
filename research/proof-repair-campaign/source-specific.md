# Source2: fixed-HM structural obstruction campaign

Status: proposed research and verification work, not new mathematical results. This plan does not exclude source2, identify an actual endpoint/coupling, or authorize actual-instance computation. Its purpose is to turn the unusually strong necessary conditions now available into genuine tests of the **fixed original HM multiplication tensors**, by deductive theorems rather than by another abstract feasibility construction.

## 1. Boundary and success criterion

PR788 already constructs abstract constant-connection systems satisfying the known source2 flag, jet, cohomology, common-pencil, and Koszul/Gauss conditions. Repeating those axioms cannot exclude source2. A successful exclusion must identify an additional property of the fixed HM object, prove that property from pinned HM sources, and show it incompatible with a necessary source2 condition. A useful negative result is a precise theorem that a proposed invariant is already realized by all the feasible abstract systems, together with the next missing HM-specific input.

All work here fixes the original negative two-space and both pencil variables. Changing variables, separately conjugating the two arrows, using a different module with matching characters, or inferring a full-module endomorphism from a truncated-pencil endomorphism is forbidden as a proof step.

This campaign is scoped to symbolic and deductive branches. It does not lift restrictions on actual coefficients, actual parameters, points, derivatives, tensors, matrices, ranks, selected models, scans, or large instance computations. It is not approval for spending. No lane below runs an actual-instance test, including a symbolic computation on the fixed HM coefficients disguised as a universal calculation. Any future such proposal remains separately blocked pending explicit authorization and a new scope review.

Do not duplicate Mr. Slop's active zero-defect O(16) or defect-12 O(14) exclusion lanes. This campaign owns source2 interfaces only; any result bearing on those lanes is handed off as a lemma with hypotheses rather than pursued as a parallel exclusion.

## 2. Immutable dependency ledger

Repository: https://github.com/Akilleez-QA/read-em-and-weep. The following public PRs were read for this plan. Use their immutable proof files, not moving branch heads. Reviews are written deductive audits, not formal certification.

| PR | Commit | Proof path below research/hm/ | Role |
|---|---|---|---|
| 788 | 941b7b3b77dc8ae8a19b1e000dddeb0438d05db7 | source2-universal-constant-flag/PROOF.md | Abstract feasibility and common-pencil reconstruction; prevents false exclusion claims. |
| 789 | 2d1642ad40ae1111b84b50eeaca0426bfbfbb314 | source2-residual-coupling-normal-form/PROOF.md | Arbitrary residual coupling, genuine quotient, zero/nonzero classes. |
| 790 | af0e03d26da5e47d18ae732291aca46f4d448dc5 | source2-first-constant-block/PROOF.md | Genuine degree-ten splitting; Section 6 simultaneous actual-source transfer. |
| 791 | 2cd033a4a5ba549d07330427cd779364cb83c0fb | source2-pencil-endomorphism-algebra/PROOF.md | Full fixed-variable endomorphism algebra, including singular maps and opposite-algebra orientation. |
| 792 | 2f01f18960ce56b8b2a0c1260c277de3c5f916bf | source2-radical-rank-profile/PROOF.md | V-channel image pencil and cohomological injections. |
| 793 | ba9234964af5d879675d19ae97847a9475792f98 | source2-a-channel-rank/PROOF.md | A-channel image pencil and exact kernels. |
| 794 | 7fd254100b83bb03f41b776ea3119690aa51f671 | source2-radical-rank-locus/PROOF.md | Complete projective radical rank locus; distinct first D images, independent final P rows. |
| 795 | 3f811311d76914a555c7e7d0c5b887b41805aa6c | source2-radical-filtration/PROOF.md | Intrinsic radical filtration and complete degree-eight core. |

PR795 proof SHA-256: 27a8802a004cb659e1b33cae9aabaca1e8188b1382d8477cac2bb31264c40937. PR791–794 proof SHA-256 values respectively:

- 8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290
- 0d4eb3e4e9e98dd9ea8202399590f9741c06771411d5ce40e69a139c461b3798
- 7a9e75e9f1d22bb058039a94452e6edc1b788faa6e716dc5489f877346ab170a
- a256ec6cc92b1151a6551e6692cfa32cac02bceaad34c60746f51f249256cf4c

Upstream actual-source gate: PR744 at 2348d4b6fb2afd67d66b15aad6037ab92c94f076; PR751 at e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169; PR754 balanced endpoint theorem at 044add76ebb14043a0edf73171517c90b9ef0c13; PR758 at 063216038f3aefd65617651c2426721efafc7f9b. Exact paths under research/hm/order-four-quadratic-load/ are specified in PR790 §1. In particular, POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md at the PR758 pin was read: it supplies the actual middle Koszul cohomology and quotient maps, not merely matching dimensions.

## 3. Established target signature, conditional on the published source2 hypotheses

Write N=(N2,N3,N4; A_u,A_v,B_u,B_v). Its characters are

- N2=A+2V+3P+4D, dimension 41;
- N3=3W'+3S+6T, dimension 54;
- N4=2V+4P+3D, dimension 37.

The commutant consists of all G-equivariant triples e with e3 A_l=A_l e2 and e4 B_l=B_l e3, for the same l. Source2 requires precisely one of:

- T(J), dimension 4, semisimple quotient C²;
- C × T(J), dimension 5, semisimple quotient C³;

where dim J=2, J²=0, and (a,d,b)(a',d',b')=(aa',dd',a b'+d' b). Zero residual quotient coupling is the five-dimensional case. Dimension alone is not a recognition theorem for arbitrary pencils.

PR790 forces a simultaneous idempotent with image the canonical degree-ten pencil N0, dimensions (9,18,16), characters (P+D, W'+S+2T, V+2P+D), and complement dimensions (32,36,21). Existence of this truncation does not imply splitting of the full HM module or bundle.

On P(J), PR794 gives precisely three image-rank types: the V direction (5,6,4); one further direction (9,12,9); and all remaining directions (9,18,9). The image characters are (D,T,P), (P+D,W'+S+T,P+D), and (P+D,W'+S+2T,P+D), respectively. The reduced 18-dimensional determinant has divisor 12[V]+6[additional]. This is not the determinant of the full 54-dimensional square-zero operator, which is always zero. The reduced comparison projector is not a radical element.

PR795 defines intrinsic JN⊂Ann_J N⊂N with dimensions (14,18,9), (32,36,24), (41,54,37). The middle quotient K has dimensions (18,18,15) and is isomorphic, with fixed variables, to N8⊕V[2]⊕V[4]. Intrinsically set Z2=∩ker A_l^K and D4=Σim B_l^K. Then Core_J(N)=(K2/Z2,K3,D4) is N8, dimensions (15,18,12), the complete degree-eight evaluation pencil. Every nonzero first arrow of K has kernel Z2 and every nonzero second arrow has image D4. V[2] is a canonical subpencil; the last V is a canonical quotient, not a preferred complementary subspace. No scalar-normalized identification with N8 is canonical.

## 4. Deliverable contract and safe code scope

Each package produces PROBLEM.md (exact theorem target and quantifiers), PROOF.md or COUNTERARGUMENT.md, DEPENDENCIES.json (commit/path/hash/lemma uses), REVIEW.md by a different worker, and STATUS.json with one of proved / disproved / reduced-to-explicit-gap / blocked. Code, if appropriate, is a source-integrity checker, symbolic character arithmetic, abstract identity checker, or certificate-schema validator. Code does not import or evaluate actual HM instance data. No sampled model, floating-point experiment, or absent counterexample counts as proof.

Every proposed HM-specific property must carry its source and an explanation of why PR788's already-feasible abstract systems need not satisfy it. If that distinction cannot be made, downgrade the package to an interface result; do not label it an exclusion.

## 5. Parallel work packages

### S00 — Freeze the actual-source interface

Dependencies: PR790 §1 and §6, PR758 actual Gauss gate, PR791 §6–7.

Target: a commuting-diagram ledger identifying the *same* M2/M3/M4 spaces, negative two-space, group action, Koszul middle cohomology, quotient map, and boundary sign in every bridge. Audit each upstream hypothesis used to transport PR791–795 to fixed HM. Separate conditional source2 hypotheses from unconditional HM facts.

Outputs: INTERFACE.md; a graph of every identification and its variance; symbolic sign/gauge consistency tests. Acceptance: both A and B are recovered simultaneously with the fixed variables; no independent character isomorphisms replace the arrow-level proof. Falsification: locate a missing hypothesis, noncanonical coordinate change, or unproved identification and stop every dependent exclusion claim at that exact edge. Risk: treating a reviewed downstream theorem as an independent proof of its foundational inputs.

Parallel units: actual Koszul origin; first-arrow bridge; second-arrow bridge; equivariance and variance audit. Handoff: signed interface contract to every lane.

### S01 — Present the universal fixed-variable commutant problem

Dependencies: S00, PR791.

Target: write a basis-free presentation of C_HM=ker Φ inside ⊕End_G(Mi), where Φ(e) is the four intertwining defects. Use isotypic multiplicity spaces, not actual matrices. Record multiplication and restrictions functorially. Prove exactly which asserted source identities constrain Φ and which do not.

Outputs: COMMUTANT-CONTRACT.md; formal schema for a hypothetical exact certificate; certificate parser that refuses actual tensor input in this phase. Acceptance: distinguishes a vector-space nullity certificate from an algebra-isomorphism certificate, handles singular maps, and fixes both variables. Falsification: any derivation using only dimensions/characters must be rejected because PR788 realizes them.

Parallel units: Hom-space decomposition; formal relation map; algebra product contract; independent hypothesis audit.

### S02 — Seek a deductive HM commutant obstruction

Dependencies: S00–S01; newly discovered public HM structural theorems must be pinned before use.

Research target, NOT established: prove a structural property of C_HM incompatible with both T(J) and C×T(J). Candidate sufficient endpoints include a scalar-only commutant; impossibility of a nonzero square-zero two-dimensional radical with the required bimodule; or an independently proved algebra invariant incompatible with both alternatives. None is assumed true.

Outputs: one exact conditional theorem per candidate, with every additional HM premise visible; alternatively a minimal missing-premise report. Acceptance: rules out both residual classes or explicitly reports which remains. Falsification: if the same proof applies to PR788's abstract family, it cannot be an HM exclusion; locate the overstrong step. Do not infer scalar commutant from stability/simplicity of the full bundle without proving a restriction/extension theorem.

Parallel units: scalar-commutant route; radical-bimodule route; center/semisimple-factor route; adversarial abstract-feasibility audit. Handoff: obstruction theorem or explicit extension requirement to S04.

### S03 — Classify forced degree-ten idempotent embeddings

Dependencies: PR790 §7, PR791, S00.

Target: derive the exact necessary subsystem-and-retraction equations for an embedding of the canonical N0, not merely a projector with the right trace. Separate existence of an idempotent, its image character, and its image's fixed-pencil isomorphism type. Classify its allowable ambiguity abstractly using the triangular algebra, without selecting an actual projector.

Outputs: IDEMPOTENT-OBSTRUCTION.md; universal polynomial/functorial relations for inclusion i and retraction p with pi=id and simultaneous arrow intertwining; no solver run on HM coefficients. Acceptance: induced summand has (9,18,16) and the actual canonical degree-ten arrows. Falsification: a character-only projector certificate is insufficient; a splitting at a single l is insufficient; a splitting varying with l is not a constant simultaneous summand.

Parallel units: subsystem equations; retraction equations; conjugacy/ambiguity; negative audit. Handoff: exact lift problem to S04 and constraints to S08.

### S04 — Prove or delimit extension beyond the negative truncation

Dependencies: S00–S03; pinned full adjoint-module presentation, if found.

Target: define restriction from full-module endomorphisms to the two-pencil commutant and determine its image or an exact obstruction to extending the specific source2 idempotent/radical/core structure. Begin by identifying which additional graded pieces, variables, and relations are genuinely known. Do not assume every truncated endomorphism lifts.

Outputs: EXTENSION-OBSTRUCTION.md with a precise diagram or obstruction complex; a theorem of surjectivity only if proved, otherwise an explicit failure locus/unknown. Acceptance: if full-module simplicity is invoked, the extension of the relevant nontrivial endomorphism must already be proved; include the fate of idempotency after a lift. Falsification: a full-module scalar endomorphism theorem alone says nothing decisive about the larger truncated commutant.

Parallel units: presentation/source inventory; adjacent-degree extension; additional-variable compatibility; obstruction-class invariance; proof reviewer. Handoff: a proven bridge usable by S02, or a ranked list of the smallest truly HM-specific missing equations.

### S05 — Extract intrinsic radical-line recognition

Dependencies: PR792–794, S01.

Target: express the V direction and additional direction without choosing A/V generators or endpoint coordinates; distinguish set-theoretic rank loci from determinantal multiplicities. Produce an invariant criterion recognizing the exact rank/character signature from the entire algebra action.

Outputs: RADICAL-LINES.md and certificate specification. Acceptance: all three vertices participate; the full radical is identified before rank-locus reasoning; the 12+6 determinant divisor is asserted only on the reduced 18-dimensional map with the requisite identifications. Falsification: one arbitrary nilpotent pencil, two sampled directions, or a 54×54 determinant cannot certify this signature.

Parallel units: intrinsic line labels; determinantal divisor; opposite-algebra direction; character refinements. Handoff: invariant constraints to S06/S08, not a claimed numerical test.

### S06 — Use radical images and kernels as incidence obstructions

Dependencies: PR794 §§5–6, PR795 §§5–6, S05.

Target: package the *joint* incidence information missed by separate ranks. First A/V D images are distinct; final P rows are independent. Derive necessary arrow-stable sums/intersections, their characters, and exact sequences on the fixed original spaces. Seek an HM-specific incompatibility with these incidences, using only proven universal HM structure.

Outputs: INCIDENCE-OBSTRUCTION.md; symbolic dimension/character consistency checker. Acceptance: reconstruct JN and Ann_J N from the full radical and explain why ranks alone do not determine them. Falsification: coinciding-D or proportional-P reasoning invalidates the claimed dimensions even when individual ranks match. No computation of actual images/kernels occurs.

Parallel units: first-vertex D incidence; final-vertex P incidence; arrow stability; exact-sequence consistency; HM-constraint search. Handoff: intrinsic filtration to S07.

### S07 — Turn the degree-eight core into a recognition/obstruction theorem

Dependencies: PR795, S00, S06.

Target: characterize the arrow-level complete degree-eight system inside Core_J(N). Preserve the canonical construction (K2/Z2,K3,D4), not a preferred splitting. Find sufficient fixed-variable relations for recognition of N8, then isolate a genuinely HM-specific condition incompatible with that canonical subquotient, if any.

Outputs: CORE-RECOGNITION.md; universal identities coming from the exact degree-eight evaluation sequence; optional proof-oriented symbolic identity checker. Acceptance: dimensions (15,18,12) are only the first gate; require the simultaneous arrow-level isomorphism class. If an obstruction uses functoriality under a larger algebra, prove that algebra preserves the filtration and descends to the core first. Falsification: matching characters, ranks of separate arrows, or arbitrary pencil essential-surjectivity cannot recognize N8.

Parallel units: first-arrow multiplication structure; second-arrow connecting-map structure; canonical quotient/subobject distinction; full-variable compatibility search; independent audit. Handoff: core incompatibility or clearly identified missing HM lemma to S08/S09.

### S08 — Audit extra HM structures against the forced filtration

Dependencies: S00, S03, S05–S07; pinned sources for every extra structure.

Research target: inventory potential structures present in fixed HM but absent from PR788's bare reconstruction: additional multiplication directions/relations, pairings and dualities, or extra symmetries. These are candidates to verify, not assertions that a useful structure exists. Determine whether each preserves JN, Ann_J N, isolated pieces, and Core_J(N), or instead creates a nonzero obstruction to preservation.

Outputs: EXTRA-STRUCTURES.md with columns known / conditional / unavailable and a separate lemma per verified structure. Acceptance: a symmetry moving the negative two-space is not silently treated as a commutant element; invariance of the entire relevant algebra ideal must be proved. Falsification: extra structure also arising functorially on every PR788 witness yields no exclusion unless its exact HM form adds a new premise.

Parallel units: extra multiplication; duality/pairing; normalizer versus fixed commutant; ideal/filtration preservation; no-go reviewer. Handoff: only verified incompatibilities to S09.

### S09 — Assemble a minimal conditional exclusion theorem

Dependencies: S00 and at least one successful HM-specific obstruction from S02/S04/S06/S07/S08.

Target: a minimal implication chain: actual source2 hypotheses ⇒ pinned normal form ⇒ necessary invariant ⇒ contradictory independently proved fixed-HM invariant. Keep zero and nonzero residual coupling branches separate until both are closed. State the remaining frontier honestly if one branch survives.

Outputs: CONDITIONAL-EXCLUSION.md; dependency DAG; minimal-assumption table; explicit unchanged-frontier statement if no exclusion is proved. Acceptance: each premise has an immutable source or a reviewed new proof; no forbidden instance computation; no circular use of an exclusion being proved. Falsification: unresolved lift/recognition/HM identification is a blocker, not a lemma placeholder that can be hidden in exposition.

### S10 — Build adversarial feasibility and scope audits

Runs independently alongside S00–S09. Use PR788–789 deductively, without selecting/evaluating any member of the family.

Target: for every proposed obstruction, determine whether its hypotheses are satisfied by the universal feasible family. Check both coupling classes and all balanced endpoints. If they are, flag that either the obstruction is false or a missing HM-only premise must be supplied.

Outputs: OBSTRUCTION-AUDIT.md per candidate; counterargument or sharpened hypothesis. Acceptance: quantifiers over endpoint and coupling remain explicit. Falsification checks: accidentally splitting residual bundles horizontally; interpreting ordinary Ext vanishing as constant splitting; arbitrary-variable gauge; stability ⇒ truncated scalar commutant; actual numerical test hidden in a helper script. This lane can stop invalid claims immediately.

### S11 — Produce a non-computational future certificate design

Dependencies: S01, S03, S05–S07. Design only; no actual-instance execution.

Target: a staged exact verification protocol that could eventually distinguish actual HM tensors if separately authorized: fixed input provenance; full commutant; algebra multiplication/radical; canonical idempotent; radical rank divisor; joint incidence; canonical core. Explicitly mark each actual-data stage disabled. Include a proof of what a passing or failing certificate would logically imply, and identify which stages yield only necessary conditions.

Outputs: CERTIFICATE-SPEC.md and schema-only validators. Acceptance: no actual matrices, coefficients, points, or ranks are generated/read/evaluated; no solver endpoint or purchased compute is provisioned. A passing necessary-condition test cannot establish source2 realization; a failure requires exact provenance plus the actual-source bridge before it can support exclusion. Handoff: future proposal only, not executable approval.

## 6. Parallel scheduling and one-spike allocation

Wave 0: S00's four interface audits, S01's four presentation units, S10 feasibility audit, and dependency-integrity review can run independently. Freeze common conventions before downstream theorem assembly.

Wave 1: S02's structural-algebra alternatives, S03 subsystem/retraction work, S04 source inventory/extension routes, S05 intrinsic rank-line work, S06 incidence, and S07 core recognition are separate proof tasks. Each gets one primary researcher and a different reviewer. Reviewers should attack the weakest bridge, not repeat the author's exposition.

Wave 2: S08 tests genuinely additional HM structure; S04 extension lemmas are handed to S02/S03 as soon as proved; S06 feeds S07. S09 assembles only proved chains. S11 remains a design/documentation lane and cannot unblock an actual computation.

The additional big spike is a bounded research sprint whose outputs are these independently reviewable theorem packages, not a promise of exclusion. Suggested allocation by research effort: 25% fixed-HM commutant/extension, 20% subsystem/idempotent compatibility, 20% core/extra structure, 15% radical incidence, 20% independent audit and synthesis. Use available authorized capacity; these proportions do not authorize cost, services, or an unbounded job.

Stop a candidate route when it is proved to rely only on already-realized abstract axioms, its indispensable source premise cannot be established, or a reviewed counterargument defeats it. Redirect to the next distinct HM-specific interface rather than repeatedly enlarging the same abstract calculation. Stop the spike at a reviewed contradiction or a comprehensive explicit-gap report; do not substitute repeated inconclusive computation.

## 7. Handoff format and acceptance gates

Every handoff includes: theorem statement; exact hypotheses; immutable dependencies; whether it concerns all normal forms, hypothetical actual source2, or unconditional fixed HM; residual coupling coverage; fixed-variable convention; proof artifact; independent review status; remaining gap. A downstream worker may not silently strengthen any of these.

Gate A: dependencies, bridge, and conventions frozen. Gate B: candidate contains a genuine additional HM premise. Gate C: mathematical proof plus hostile review. Gate D: both coupling classes covered, or surviving class explicitly named. Gate E: root synthesis changes a source label/frontier only after the complete chain passes. Until then, the established frontier remains unchanged; the existing source2 structural results are not exclusions.

Plan prepared from public proof texts PR788–795 and the pinned original Gauss gate. No actual HM source instance, matrix, rank, parameter, point, selected model, or computation was evaluated while preparing it.
