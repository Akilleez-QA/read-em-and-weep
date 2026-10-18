# Inert ID0 certificate and terminal integration candidate

## Status and exact delta

This is a NON-APPLIED static diff against source pin e93cf712f9da4926a8450cc870ed45a7bfc379ab. Candidate source is stored only in `.py.txt` review files. Neither candidate nor frozen modules were imported, compiled or executed. No model, source, owner, jet, rank, physical detector, local model or invented field numerical calculation was run. The artifact was not published.

Only two proposed production paths change:

1. `exact-curve-field/field.py`: add `Rational.certify_laurent`, immutable identity-bearing `LaurentContext`, and shared `LaurentCertificate`. All old definitions, including old coefficient extraction and Execution, remain unchanged.
2. `detector-realization/program.py`: append `actual_id0`. The complete old file is an identical prefix, including actual_route30, _actual_body, all guards, helper criteria, weights and imports. The first operation of actual_id0 is an unconditional direct RuntimeError. Its signature defaults allocate nothing. It does not inspect arguments or call aggregate admission before refusing.

Below that raise, unreachable text contains a nested owner generator copied from potential_owners with only its name and seed30→0 changed. The complete original _actual_body construction follows, with only the nested helper name changed. Existing require_aggregate_admission remains in both copies. The old terminal alone is replaced by creation of a frame context, one shared certificate, and exact weighted coefficient extraction. There is no separately callable new private physical body, builder callback, admission flag, token, environment switch, monkeypatchable guard call before the raise, or enabling path. Mocking aggregate admission cannot bypass the direct raise. Ordinary Python semantics, with builtins/interpreter/source unmodified, is the boundary of that claim. Deliberately extracting/recompiling unreachable source is outside it and is not authorized.

## Exact terminal

The whole original-frame signed outer sum is assembled once in the inert specification. It still uses the existing weighted_assignment, fresh per-assignment PhysicalModel, stage2 source_and_lift, X13[5][0]+X02[1][3]+X02[4][2], original unsorted-owner outer weights, parity, orientation, mask15 stripping and cache_clear finally block. No source-side Q² factor, repeated outer sum, local coefficient extraction, support shortcut, cutoff reduction or extra frame conversion is introduced.

The three exponent/weight pairs are fixed in order:

- (-3,-3,-1,-1), weight1, output8
- (-2,-2,-2,-2), weight2, output40
- (-1,-1,-3,-3), weight1, output72

Thus the requested expression is s_(5,0)[8]+2s_(5,0)[40]+s_(5,0)[72]. Explicit context labels describe the original resolution frame, degree−2 tau−4 conversion, finite tau1, full deck mask15 and ID0 L5,0 Q². Labels are immutable declarations and are NOT proof that a rational came from that physical construction. Source provenance would require the separate missing authentication/admission steps below. No API permits frame labels to serve as physical authorization.

## Shared-division mathematical argument

Let A,B belong to Q[x1,x2,x3,x4] with B nonzero, as guaranteed by the existing Rational ordinary API. Let d_i be the minimum exponent of xi over all nonzero terms of B. Then B=x^d C, and no xi divides C. Unique factorization implies gcd(C,x^m)=1 for every nonnegative monomial x^m. A/B is Laurent iff C divides A: one direction follows from A/B=x^(-d)Q; conversely, clearing the finitely many negative exponents of a Laurent expression gives C dividing a monomial times A, hence C divides A.

The added method invokes the existing full lexicographic polynomial division exactly once. That algorithm strictly descends leading monomials, moving nondivisible leading terms to the remainder, and computes A=CQ+R. For a single divisor, its remainder is zero exactly on the principal ideal (C). A nonzero remainder raises NotLaurentPolynomial, never returning a certificate or zero. No requested exponent, target support or degree enters certification. This covers residual C lacking a constant term.

After certification the retained quotient Q and d give [x^e](A/B)=[x^(e+d)]Q. Every terminal read scans that same Q. Absent targets return exact zero only after full divisibility succeeded. The three weights and additions use the SAME existing Execution's q, mul and add, so the final coefficient height and arithmetic failures are metered; native Fraction arithmetic is not used to combine the output.

## Binding, lifetime and failure

The existing frozen Rational/Poly representation and the new frozen context/certificate use ordinary Python immutable-field conventions, not a hostile-code security boundary. The certificate retains strong references to its exact rational, context, original Execution and quotient. The context retains the Execution and an immutable tuple of exact strings. Reads require `is` identity for rational and context, and identical Execution for all bound objects. Equal contents or labels do not authorize another object. The private construction seal is an ordinary module API convention; reflection, direct use of private symbols, object.__setattr__, source alteration, subclass tricks outside exact accepted types and monkeypatching are outside the guarantee.

Certification checks the existing Execution before work and after complete successful division. The new read methods check failure before reading and immediately before returning, and weighted accumulation checks again before returning. Existing ex.tick/q/mul/add operations propagate failures. Once the existing Execution is poisoned, ordinary certificate reads refuse. Already returned immutable numbers cannot be revoked. Invalid types or a non-Laurent rational are not claimed to poison the Execution, consistent with the existing implementation. Concurrency, reentrancy, malicious iterable protocols and arbitrary interpreter/OS exceptions are not modeled.

Added storage-event hooks account at an algorithmic bookkeeping level for new context/certificate references, shifts/targets and weighted temporaries. They are NOT a byte/allocator/native-integer scratch bound or a current aggregate resource-admission proof. Existing residual minimum computation and native tuple/integer operations remain as in the source algorithm; a future resource proof must include their actual costs and lifetimes. No claim of cap fit or speed follows.

## Seed-relabelling denotation premise

The proposed owner map is (30,occurrence,carrier,mask,tag)→(0,occurrence,carrier,mask,tag), with every other field and iteration order unchanged. It is injective within the old seed30 family and preserves equality patterns. FullOwner.source_key, physical_key and common_key omit seed; sorted_source uses source_key. Thus source ordering/parity and direct physical data lookups visible in the inspected code are unchanged. PhysicalModel caches are fresh per assignment and cleared by the unchanged finally block. This is a conditional structural argument, not permission to instantiate owners and not a replacement for reviewing every transitive use of owner identity in the full dependency closure. Future use must establish that no omitted dependency branches on seed or historical provenance and that all accepted domain/transport premises still apply.

## Authentication and exact remaining gaps

The original text-only preparation verified all 23 supplied frozen files against both their recorded SHA-256 and Git blob IDs at the stated pin. The validator rechecked their bytes after artifact generation. public-pins.json records every source URL and old/candidate digest; candidate.patch has its own digest. This verifies agreement with the supplied frozen manifest, not independent remote trust or a mathematical proof.

The private preparation inventory checked imports from every frozen Python file and selected old receipt dependency pins; this portable bundle contains only public source pins and text/AST validators. Its generated dependency-inventory.json records imports and availability against the supplied source root. Two old locally pinned files are absent from the frozen snapshot, but were subsequently fetched read-only at the same immutable pin into separate inspection files during preparation (not bundled):

- exact-curve-field/producer-ready.json
- source-boundary-analysis/review-independent.md

Both fetched bytes match the old receipt SHA-256 and the connector-returned Git blob ID. The frozen snapshot/manifest were not changed. The field marker explicitly limits its claim to artificial-only use and delegates physical gating to callers. The independent boundary review accepts a conditional global raw-primitive replacement theorem, preserves complete source terms and original-frame conversion, and explicitly grants no coefficient oracle or physical release. Its recorded test outcomes were read, not replayed. That review itself references additional historical proofs and pins; retrieval of the two files closes these two byte-availability edges only, not the full transitive proof closure.

Three old historical git-object payloads are listed by path/commit/digest, but not fetched or authenticated here. The compiler also names historical model/formula/comparison objects and uses runtime source-loader logic. The imported retained-sector theorem and its application to this actual global class are not re-proved here. The inventory is a static starting point, not a complete dynamic dependency closure or acceptance record. The old authentication manifests are deliberately NOT rewritten: applying this field change alone would invalidate their old digests. Such refusal is correct. No ready marker or replacement admission record is issued.

Before any future application/activation, separate authorization and independent review must establish:

1. Complete authenticated transitive source/data/theorem closure, including the separately retrieved receipt dependencies and their transitive proof links, historical model/formulas, original retained ID0 record and retained-sector theorem.
2. Seed-relabeling source equivalence, complete raw/global-boundary comparison, common54/29/5251 domain, original frame/orientation, degree conversion, J3 closure and weighted Serre pairing identification.
3. Correctness and negative controls of the actual added field API on independently invented data under an approved test boundary. The previous invented adapter's tests do not test these production additions.
4. A new source-bound ID0 algorithm and dependency manifest plus independent acceptance. Old request30 receipts cannot be relabelled or silently reused.
5. A shared-terminal cost/peak-lifetime proof including retained A/B/Q/context, residual/remainder, division scratch, coefficient lookup/weighting, native integers/Fractions, headers/allocator and outputs-before-free.
6. Separately authorized operational acceptance and explicit physical release, supported by a complete resource and lifetime proof. This artifact supplies neither.

The guard remains unconditional even if every future premise were supplied; activation would necessarily be a separately authorized, reviewed source change. No enabling mechanism is included here.

## Validation evidence and limits

`python -B validate_static.py --source-root PATH` checks bytes/AST only. It proves exact old-program prefix preservation; equality of every old field definition AST; direct first raise; no new top-level physical helper; seed-only nested owner delta; original preterminal AST equality modulo helper name; exact terminal order/weights; one division in certification; and pre/post failure-check placement. Six invented in-memory source mutations are rejected. All supplied frozen Python files are parsed for the dependency inventory, never imported. The validator uses explicit exceptions, not assert.

These finite structural checks do not prove the entire program correct, complete dependency closure, hostile-input isolation, resource admissibility or any numerical physical result. D0 remains unknown. Even an eventually authenticated D0=0 would leave nonvanishing undecided; one nonzero retained detector would suffice only under the accepted global identifications, and full residual vanishing needs all thirty authenticated retained values plus the reduction premise.
