# Independent whole-proof review

Review date: 2026-10-23 (UTC).

## Decision and scope

ACCEPT for the stated two-branch structural theorem. I independently read the complete final proof, its two immutable input proofs, the bounded verifier, the manifest, and the reproduction instructions. I found no mathematical gap or unqualified actual-map replacement in the stated construction. This review does not choose either branch, re-prove the upstream Horrocks–Mumford geometry, or certify an actual coefficient computation.

The new result is the actual rank-two-source presentation of Q in the nonzero branch and the rank-three-source presentation of its intrinsic quotient kernel Q3 in the zero branch, both with the same intrinsically defined positive rank-six target. It is not merely a new character presentation. No further cancellation or exclusion of an actual branch is asserted.

## Exact reviewed author bytes

The review is bound to these SHA-256 values:

- PROOF.md: `06567a2145da2bc00ff00a78585bd68582a2fd262d77cdadbe9eaa7371618523`
- verify.py: `111a6c1afb1dabd57e60cc50bc6297bcbf9e40ff130477fa5af7469fe489ac2a`
- INPUTS.json: `4aba229c8e5574ac1e548e7b6e4f1b2cba08341c63ba4ba9de7ab79d52786c9f`
- REPRODUCE.md: `50f0e8f3519912b427b4620047e1fc6983e1eb2ca4b86e0d54d583558ad24c1b`

Any change to those bytes requires renewed review. REVIEW.md is intentionally not self-hashed.

## Independent input authentication

I independently fetched both complete files through the GitHub connector at the manifest's immutable commit refs, requesting base64 and decoding the original bytes. I recomputed each Git blob SHA-1 using the `blob <length>\0` header, compared it to both the returned GitHub SHA and the manifest, and compared the decoded bytes to the local audit copy. All comparisons agreed.

1. NONSPLIT: PR1090, commit `0bbb6529ababc4a92cceacd1e4db2a0bac10d759`, path `research/hm/nonsplit-quartic-extension/PROOF.md`.
   - Original length: 9755 bytes.
   - Git blob SHA-1: `bf04957985a3fb0876e7b1dec3d58c76b66bf094`.
   - SHA-256: `60128920917b906a58350f72f4562f07da1f7b8a0f95ecb2c9156f77c1d68a4f`.
2. RESIDUAL: PR1002, commit `b691ab014afa0c546894dba5bcec396ed6694d5d`, path `research/hm/canonical-residual-pencil/PROOF.md`.
   - Original length: 7479 bytes.
   - Git blob SHA-1: `cefa5e50f10fbcfa5fb5a644571ebc6b050402b0`.
   - SHA-256: `d46e477e57e156ae05130006f2fb27d0a50c4c3fc0fa1c9f789ffdb736bd9408`.

These primary sources supply exactly the imported interfaces used in the new proof. In particular, the canonical degree-two quotient in NONSPLIT identifies its kernel with RESIDUAL's actual Q. No identification of old source subbundles or intermediate target embeddings is inferred from representation labels.

## Whole-proof checks

1. The target-kernel construction is exact. The surjection Z9 to J_r O(2) factors through the actual C, so its kernel Y8 has quotient the same Q and source O(-8)+L3. Pulling back the complete quadratic evaluation kernel yields the surjection Y8 to J_r W O(-1); its kernel Y6 is exactly the preimage of B4. Thus the positive target is defined by actual maps and does not depend on a chosen splitting.
2. The extension 0 to F to Y6 to B4 to 0 has ordinary and equivariant Ext1 zero by H1(O(4))=0. The claimed one-dimensional equivariant splitting ambiguity is correct: W' tensor Sym4 W=S+T6. The proof retains the extension rather than replacing its source maps after an arbitrary target splitting.
3. The O(-8) source projection vanishes by Sym7 W=W'+T6 and absence of W. The full L3 projection cannot vanish because that would make the globally generated Q surject onto the nonzero bundle J_r W O(-1), which has no sections. This is a valid geometric obstruction, not a genericity argument.
4. Restriction to the canonical M0 W O(-1) subbundle is a scalar map between actual multiplicity lines by Schur's lemma. If it is nonzero, the restriction is an isomorphism, h is onto, and ker h projects isomorphically to M1 O(-2). This particular complement is selected by the actual kernel; it is not an arbitrary source replacement. The kernel diagram then gives the claimed actual rank-two core.
5. If that restriction vanishes, the nonzero h factors through M1 O(-2). The unique equivariant channel to J_r W O(-1) is the Euler inclusion, with locally free cokernel J_r O. The kernel-cokernel exact sequence gives the stated five-term sequence, and then the actual rank-three-source presentation of Q3. The trivial quotient has not been appended by hand.
6. Positivity of Y6 implies Hom(Y6,O)=0 without equivariance. In the nonzero branch this forces Hom(Q,O)=0. In the zero branch exactness makes Hom(Q,O) precisely the dual of the displayed trivial multiplicity line; every such map has the same kernel Q3. The claimed equivariant splitting of Q to J_r O follows from global generation and finite-group averaging, but is not used to construct the core.
7. The old scalar gate is compared only through the actual same Q and RESIDUAL's dual complete-evaluation identification. This proves equality of the two zero loci and their complementary nonzero alternatives. It does not identify scalar coordinates or canonically identify their multiplicity lines.
8. The cokernels Q and Q3 are locally free, so the two core injections are fiberwise injective everywhere. Their weighted maps are inherited restrictions of F to C; the degree-two and trivial quotients kill F by degree. No weighted embedding or prior graph component is silently changed.
9. All displayed ranks and degrees agree: Y8 has (rank, degree)=(8,12), Y6 has (6,14), the nonzero-branch source has (2,-10), and the zero-branch source has (3,-10). The resulting quotients have (4,24) and (3,24). These balances supplement rather than substitute for the map-level argument.

## Independent bounded replays

I inspected verify.py before execution and ran, from the final package directory:

```sh
python3 verify.py
python3 -O verify.py
python3 -m py_compile verify.py
```

All commands exited successfully. Both verifier modes printed:

```text
PASS: two immutable originals; actual projection channels; Euler companion; old gate dimensions; target ambiguity; both core rank and degree balances.
No actual HM/source coefficient, point, parameter, matrix, instance rank or scan evaluated.
```

The verifier uses exact rational arithmetic in Q(sqrt(5)) on nine fixed conjugacy classes, explicit checks that remain active under Python optimization, and Git-blob authentication of the two inputs. I checked the reproduction commands and their mapping from manifest keys to audit filenames. The script does not prove the sheaf-theoretic arguments or evaluate an actual HM instance; those geometric arguments were reviewed separately above.

No selected actual coefficient, point, matrix, parameter, jet, instance rank, large computation, publication, or repository mutation was used for this review.
