# Review of the one-channel top-obstruction criterion

Verdict: PASS for the bounded claim stated in PROOF.md. Review completed on 2026-10-23 UTC. This review binds the exact four files listed below, not an earlier draft or any later revision.

## Fresh source authentication

The reviewer independently fetched each original from Akilleez-QA/read-em-and-weep by the exact commit and path in INPUTS.json, read its relevant statements, recomputed its Git-blob identity, and compared its bytes with the package's reconstructed audit input. All four matched:

- CORE: 3f65bbc68851837729aa9c20c526e3fb47ba8361.
- AMPLE: 3f68598d395b2672462e5529994e4f7788be2f94.
- BRANCHES: 6101c8d1856b55e0e770f9a4ce4c36d0702336d9.
- QUOTIENT: 4666dacbbe7c4d68b25e80d65af37ea80f3592be.

CORE supplies the actual fiberwise-injective core and its one-dimensional channels. BRANCHES Section4 directly supplies the intrinsic zero-branch decomposition Q=O⊕Q3. QUOTIENT Section6 directly supplies the canonical exact sequence 0→Q→C→O(2)→0. AMPLE Section6 directly supplies ker σ=H0(C(-12))^G, the two-dimensional source and target of σ, and the equivalence of rank one with row9. AMPLE Sections5–6 also state that rank two forces equivariant vertex splitting and that rank one does not decide the vertex scalar. These are imported interfaces; this audit is not a recursive reproof of all earlier packages.

The preliminary draft's indirect attribution of the Q-to-C comparison was corrected during review. The final package pins its direct original and separately pins the zero-branch splitting. No outstanding provenance issue remains for the claim reviewed here.

## Mathematical checks

1. The saturated rank-one factor obstruction is valid: after twisting by -1, a saturated line in S O has degree at most zero, and the required source Hom tests only symmetric powers of degrees0..4 (or a negative twist). All are impossible for W'. A nonzero universal block therefore has generic rank two.
2. The maximal minors have degree eight. Their common-zero divisor is invariant and has degree at most eight; the orbit bound twelve therefore excludes every rank-drop point. This proves a bundle quotient, rather than merely a generically exact complex.
3. The quotient has rank two and degree ten. Global generation after twisting by -1 bounds both degrees below by one. For an unbalanced equivariant splitting, the two line summands have even degree by the central action and absence of characters. The only possible pairs are (2,8) and (4,6), and the displayed Hom vanishings exclude both. Equivariant splitting here is valid: ordinary splitting can be made equivariant by averaging over the finite group. The cohomology computation after twisting by -4 distinguishes the balanced multiplicity W' from W correctly.
4. The universal exact sequence with quotient W' O(5) proves that the invariant H1 map after twisting by -12 is an isomorphism. Both neighboring quotient cohomology groups vanish. Thus the nonzero pairing is proved by exactness, not inferred from matching dimensions.
5. The actual core's negative twists have no H0. Exactness of finite-group invariants and the three additional H1 vanishings leave precisely the actual block coefficient times this universal isomorphism. The subsequent identification with H0(C(-12))^G uses the authenticated exact quotient sequence and, in the zero branch, the authenticated splitting. No connecting homomorphism is discarded.
6. If the actual block vanished in the zero branch, restriction to its source summand would give an everywhere-injective map between rank-two bundles of degrees -6 and6. Such a map would be an isomorphism, which is impossible. The argument uses fiberwise injectivity of the actual core.
7. The zero/nonzero criterion is independent of all permitted inherited presentation choices because it equals the intrinsic condition H0(C(-12))^G≠0 for every such presentation. This does not claim that the coefficient or its normalization is canonical. The stated rank-σ and vertex conclusions follow exactly from AMPLE.

No mathematical correction is required in the bound files. The result does not evaluate the actual block, select the actual remaining row, decide the vertex scalar, or exclude an additional C row.

## Reproduction checks

The reviewer inspected verify.py and ran both commands successfully against the freshly authenticated inputs:

```sh
python3 verify.py
python3 -O verify.py
```

Both returned exit code0 and the documented PASS output for four immutable inputs, the balanced-quotient identities, the two surviving invariant cohomology lines, and all other invariant H1 vanishings. Checks remain active under optimization because they use explicit exceptions rather than removable assert statements. The arithmetic is exact in Q(sqrt(5)), over nine fixed character classes and the displayed bounded symmetric powers. REPRODUCE.md correctly explains reconstruction of omitted source bytes and the distinction between arithmetic checks and mathematical proof.

No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank was evaluated during this review. No large computation or external write was performed.

## Bound final bytes

SHA-256:

```text
7fe1a5b893a64b67c45be1241f61bc293212bb775ca56a3fe9d97c64e8b4f6dd  PROOF.md
fb9aee9e0fa808216f0aa2dc23168ec9fa35d8e2dd2b7cbac2b30f380332c454  verify.py
82504cb1dff8ce46e02532382e8138ed52409a31159dd7b2ce5cb2a4489a3115  INPUTS.json
1c98f9e4597ed4b87dc9ca8d326e2e73218013d5aa59e7b7e97d86204f2a76c9  REPRODUCE.md
```

Any change to a bound file requires a new review or an explicit revalidation of that change. REVIEW.md is intentionally not self-hashed.
