# Independent review of the portable ID0 certificate

## Decision

**Accepted for publication as a conditional mathematical/static certificate. No mathematical or portability correction is required. This is not an authenticated physical implementation, an admission record, or a value of D0.**

Reviewed 2026-10-18. The proof and original checker were independently inspected; the portable delta was then inspected before execution. No original reviewed file was edited. Only the supplied standard-library checker was executed, normally and with optimization. No repository module was imported or evaluated, and no physical owner, model, source or jet was constructed or enumerated.

## Mathematical findings

1. **Laurent iff criterion is correct.** For B=x^d C, the componentwise denominator minima ensure that no coordinate variable divides C. If A/B is Laurent, some coordinate monomial x^n clears denominators of A/C, giving C | x^n A. Unique factorization and gcd(C,x^n)=1 imply C | A. Conversely A=CQ gives A/B=x^-d Q. A nonzero constant term in C is unnecessary. Zero numerator is allowed; zero denominator is excluded.
2. **The single-divisor remainder argument is complete.** Polynomial division gives A=CQ+R with no remainder monomial divisible by LM(C). If C divides A, it divides R; a nonzero R=CH would satisfy LM(R)=LM(C)LM(H), a contradiction. Thus zero remainder is equivalent to divisibility for any admissible monomial order. The quotient is unique. One complete certificate therefore serves all targets Q[e+d]. Full certification precedes even negative-target zero answers, and local summands cannot replace the complete sum.
3. **Seed relabeling is conditionally valid.** Replacing only seed 30 by 0 preserves full-owner equality, occurrence distinctions, carrier/legal/standard fields, all specified source keys, sorting positions/parity and equality-based memoization. It does not mean hashes themselves agree. Fresh caches and unmixed owner domains are essential. Static inspection of program.py, raw_engine.py, interfaces.py, compiler.py and lift_schema.py supports the complete source/face/selector/weight induction. Full-owner distinctions must not be replaced by physical-key deduplication.
4. **ID0 is exact.** The request has scalar_map {b:0,i:5}, block Q^2 and empty base monomial. Expanding (x1*x2+x3*x4)^2 gives weights 1,2,1 and monomials (2,2,0,0), (1,1,1,1), (0,0,2,2). Pairing by the x^(-1,-1,-1,-1) coefficient gives exponents (-3,-3,-1,-1), (-2,-2,-2,-2), (-1,-1,-3,-3), and indices 8,40,72. There is no extra factorial or terminal sign from this multiplication. The old output80 is not reused.
5. **Normalization is properly conditional.** The product-chart O(-4)^4 range is [-3,-1]^4 and the dual section has coordinate degrees at most 2. Application to the actual scalar imports transport, completeness and trace orientation. One deck-product removal and internal-degree -2/tau^-4 conversion remain; tau=1 on the finite chart. Mask15 is deck character, not S4 antisymmetrization. The corrected common-frame premise A^E=-dG G^-1=-L^t is used without the superseded scalar shift.

## Imported premises and operational limits

The imported geometric obligations remain physical source/model identification, full original-frame lift and J3 closure, full-source homogeneity and regular extension on whole standard targets, all owned suffix factors, bounds 54/29/5251, raw/N14 global comparison, corrected alternating primitive and retained-sector theorem, and transport/completeness normalization. Byte hashes establish which premise texts are used, not a fresh proof of those texts. A degree formula alone does not clear poles; a global coboundary primitive is not thereby inside a numerical cutoff.

A future shared-certificate implementation still requires source-bound adapter authentication, complete transitive source closure, immutable rational/frame/Execution binding, full divisibility validation before reads, exponent/foreign-context checks, live/poisoned Execution checks at every read and weighting, exact metering of construction/retention/scans/arithmetic/scratch, and independent admission. The frozen field.py exposes repeated per-call division, not a shared-certificate API. The theorem does not authorize deleting two charged divisions from an existing admission record or promise identical budget failure traces. D0 remains unevaluated; zero D0 alone would not settle the full problem.

The AST seed test constructs and reverses its own seed-only candidate; it does not authenticate an independently supplied adapter. Absence of direct seed/occurrence attributes in selected functions is supporting evidence, not a stand-alone transitive provenance theorem. These limitations are correctly acknowledged by the proof.

## Portability review and execution

The portable checker changes only input discovery: required --source-root, repository-root/subdirectory resolution, bundle-relative source-pins.json and premise paths. The pinned source records preserve the original 23 paths, commits, hashes, Git blobs, byte sizes and URLs; only nonessential prior verification flags and unrelated manifest metadata are removed. The mathematical proof changes only reproduction instructions. Included premise files are byte-identical to the original pinned inputs. No algebra or static checks were weakened.

Both portable runs succeeded against the pinned 23-file source tree:

    python check_certificate.py --source-root /path/to/pinned/source-tree
    python -O check_certificate.py --source-root /path/to/pinned/source-tree

The reports in this review directory are byte-identical to each other and the bundled reports: 23 verified source files, 195 bounded invented polynomial products, and all physical-execution fields false. The imports remain standard-library-only. The checker reads source as data, performs no network calls and writes only its stdout report.

Inspection and a recursive text scan of the publication files found no machine-specific workspace, home or temporary paths, private-note paths, private attachment links or local thread links. Reproduction uses documented placeholder paths. This review confirms the supplied frozen files and does not claim a fresh live-repository fetch. No publication blocker was found within this scope.

## Exact public artifact pins

All source identities and immutable URLs are in source-pins.json, for repository Akilleez-QA/read-em-and-weep at commit e93cf712f9da4926a8450cc870ed45a7bfc379ab, under research/codex-swarm. Relevant source anchors are program.py potential_owners/weighted_assignment/_actual_body; interfaces.py FullOwner/sorted_source; raw_engine.py PhysicalModel/RawSource/source_and_lift; compiler.py Source/Lift; lift_schema.py closed_lift_schema; full-lift-domain/lift.py transport/domain contracts; field.py Poly.divide and Rational.laurent_coefficient. The checker verified all listed SHA256 and Git blob identities before AST processing.

SHA256 values at review:

- PROOF.md: 596c7ba7ac08086d1b6220773aa073641524294273c19bd527d9caa31aab1846
- check_certificate.py: 6d442400f8585f7b1fd64e4103ea59f0b72ca12be1138f2a86a4ea35936667c8
- source-pins.json: 8f2bc7c09722b7af794d1628ae86bf436098da074a49d878d2d86c952646c263
- README.md: 72ff3b808da28392656f6070c84d4107df2e915da931f56fc14c93dd04b9c240
- premises/COMMON_FRAME_CORRECTION.md: a88442758260f080d7c5c6d871b27522a60263cec6a8669e3956d63d7ff71bc7
- premises/PROOF.md: e43de2abc2838f2d5e31c3fd45fc9517c963e3ad9c8a605f00ec62b50263bab9
- premises/REVIEW.md: e155fa2d432bfa4e4c673fc31cd4c66dc80d2af02e1ce0683a07a80e60978f39
- premises/weighted-requests-30.json: 707663b97c3a8289d6531172a1c509e54ceccb3185a6e07f4f28153fbc119375
- Each normal/optimized checker report, both bundle and review copies: 3745a2e9c69bdd86b2fe8a693a9c34d4e5fb71c55b3e83abdfbab77938e7c881
