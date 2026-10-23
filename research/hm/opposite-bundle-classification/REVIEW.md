# Independent whole-proof mathematical review

Date: 2026-10-23. Verdict: **PASS, with no mathematical correction required.** This is an independent mathematical/code review, not formal proof-assistant verification. No publication or actual HM/source instance evaluation was performed.

## Scope and dependency authentication

I read the entire PROOF.md and final verify.py, PR934's reduced-pencil proof, PR938's source-character derivation, and PR945's exceptional-exhaustion proof. The freshly fetched audit-inputs/PR934.md, PR938.md and PR945.md are byte-for-byte equal to the local dependency proofs reviewed. The final verifier authenticates their Git blob identities against INPUTS.json. I use PR938 only for its Sections 1–2 source/target interface; none of its now-excluded conditional nonzero-torsion alternatives enters this argument.

The imported statements supply precisely: a locally free, globally generated rank-five degree-26 C; its equivariant 26-to-31 presentation with the stated E and H; and the actual equivariant vertex extension by O(10). The new result is conditional on those established statements and does not re-prove all their historical dependencies.

## Geometric and homological checks

1. **Equivariant splitting.** The maximal ordinary-degree block is the canonical evaluation image of H0(C(-d_max)) O(d_max). Its ordinary complementary sequence splits; averaging a right inverse over the finite group preserves the right-inverse equation. Induction therefore gives the stated equivariant decomposition. The center condition and nonnegative degrees follow respectively from the standard O(1) linearization and global generation.

2. **Complete evaluation and its source.** H0 and H1 of O(-1) vanish, so the presentation identifies H with H0(C), not merely their characters. For O(d), multiplication by the tautological kernel line identifies the evaluation kernel with Sym^(d-1)W O(-1); det W=1 removes any determinant twist. Tensoring by each multiplicity representation gives both character equations. Conversely those equations identify the complete-evaluation source and target with E and H as actual representations. Thus every enumerated bundle really gives an abstract fiberwise-injective linear pencil, rather than only a numerical candidate.

3. **Invariant Ext bound.** Finite-group invariants are exact in characteristic zero; equivariant extensions are the invariant ordinary Ext classes. Serre duality gives the displayed Sym^(d-12) formula with the standard canonical linearization. Rank/degree/parity reduce all potentially contributing atoms to O(12), O(24), and W O(13). Their contributions are one each. The degree budget excludes coexistence except two O(12)'s; those are excluded by the target's single trivial summand, since H0(O(12)) contains a trivial summand. This proves the bound without presupposing the final enumeration.

4. **Explicit nonsplit extensions.** Sequence (2) is Euler evaluation twisted by eleven. Dualizing the O(2) evaluation sequence and twisting by twelve gives (3), including its A and W linearizations. For (4), Sym7 W contains W' once; the resulting two sections have no common zero, because any nonempty invariant base divisor has degree at least twelve whereas their degree is seven. Projective point stabilizers are cyclic and A5 has no cyclic subgroup larger than order five. The kernel is O(-7) with no extra character because G is perfect. Twisting by seventeen gives the asserted sequence. Each middle bundle has different ordinary splitting from its split alternative, proving the extension class nonzero.

5. **Middle-bundle uniqueness.** Each nonzero invariant Ext space is one-dimensional. Rescaling the kernel identifies nonzero classes' middle bundles equivariantly. The zero-Ext complementary summands split off. The three replacement rules therefore give every nonsplit middle bundle for the five starred rows. Adding the same complementary summands cannot erase the difference between the ordinary split and nonsplit degree multisets.

6. **Single lifting obstruction.** Section 6 correctly identifies the Serre pairing with the twisted extension connecting map to H1(O(-2)), a trivial one-dimensional representation. Exactness of invariants and H0(O(-2))=0 identify invariant sections of D_vert(-12) with its kernel. On a starred row both the invariant section domain and invariant Ext are one-dimensional, so the stated split/nonzero criterion follows. Unstarred rows require no test because Ext vanishes. No actual boundary map or section is evaluated.

7. **Necessary versus sufficient scope.** Actual C must occur on the list; every listed type and either vertex-extension alternative available for it occurs abstractly with this precise E/H interface. This does not construct an HM realization or compatibility with omitted incidence/multiplication data. The proof consistently states that boundary. In particular it neither selects the actual row/scalar nor changes a source ledger.

## Independent finite replay

I wrote review_verify.py independently of the nine-class arithmetic in verify.py. It uses integer affine-E8 McKay adjacency for tensoring by W, with edges

    1—W—A—S—D—T,  T—V,  T—P—W'.

The recurrence for multiplication by Sym^d W acts on each irreducible basis vector. This avoids Q(sqrt5) character evaluations entirely. The independent search enumerates all unordered atom multisets subject first to rank five and degree 26, with no source/target character pruning; only afterward does it test both character vectors. It also parses the full literal list from PROOF.md and compares exact sets, not merely counts.

Observed output:

    PASS independent McKay/rank-degree enumeration: 48 unpruned atoms; 277 rank-degree candidates; 21 types; starred rows [8, 9, 11, 16, 21]

The replay passes normally and under python -O, with explicit checks retained in optimized mode. The replay also checks invariant dimensions in degrees 0,2,...,14, the Sym7 W identity, and every resulting Ext dimension. Separately I ran final verify.py both normally and with python -O. Both runs pass the full 21-list, 45/646/21 bounded-search counts, five starred rows, structural invariant bound, degree-seven covariant, three Euler identities, target-only negative control, and immutable dependency hashes.

These are bounded calculations of abstract fixed-group representation characters. They do not evaluate any actual HM/source coefficient, point, parameter, derivative, matrix, or instance rank. Geometric exactness and nonsplitting are supplied by the proof above, not inferred merely from Euler-character identities.

## Exact reviewed file identities

SHA256:

- PROOF.md: 2bf246913d0eb0456b7939b73ccc09d83baac4d39b5b9841e151afab221803d8
- verify.py: 7c12148e0acddf8e74ac25191f75b4498d73ae27e3bd33c22d4b64a63d1bda3a
- review_verify.py: 1d32b927b95740a9a1ce355b6d97893a62efd66c5deed533237ddbf41c63e343

No edits to PROOF.md were made by the reviewer. An early draft verifier omitted checks claimed in the proof; the final reviewed version adds them and resolves that temporary discrepancy. No unresolved mathematical finding remains.

- REPRODUCE.md: e176d40994614deef26ee8b61db91b393e94a597ee98d9afb24dcb4faaf4eb99

- INPUTS.json: a09f86ab36560adafd7a9fec912450881e657cead84fb28443d2c08a8eb4fd5a
