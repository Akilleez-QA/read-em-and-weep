# Independent whole-proof review

Verdict: PASS, with the explicit scope limitations in Section 5. This review binds the four files listed below, not an earlier draft.

Reviewed on 2026-10-23 UTC by a fresh reviewer independently reading the complete proof, the executable verifier, the manifest, the reproduction instructions, and the three cited original proofs.

## Bound artifact hashes

SHA-256:

- PROOF.md: `1bfeca9f9c2cc4f7023ba6cc579605dd06c3719823c4f460489483500c992303`
- verify.py: `0cca2e43e2f084bf2d91058ce6fdb6fd2b94dd2bc8cdba716e09571d52a81204`
- INPUTS.json: `fb2807ea1cb582b361eb47ceeb65e2cf3168322e9222aeff18a4e876073ef522`
- REPRODUCE.md: `4bbe790da351b5119d462444902aed1d03e697c29e5d62ae91501d0f7f068cab`

## Immutable-source authentication

Each original was independently fetched read-only from Akilleez-QA/read-em-and-weep using the repository path and full commit in INPUTS.json, with base64 encoding to preserve exact bytes. Decoding and comparison with the local audit input gave byte-for-byte equality, including terminal newlines. The Git blob was independently recomputed as SHA-1 of the standard Git blob header followed by the file bytes and matched both the GitHub-returned SHA and the manifest:

- CORE, commit `7cd8baebbec29ad21def1f8b30e19c707a87aed5`, 8,541 bytes, blob `3f65bbc68851837729aa9c20c526e3fb47ba8361`.
- TOP, commit `547a224a95bc16aa6642158ed2b3fd2124e026ab`, 7,011 bytes, blob `401233348055b85d397309b7b0993069c0f80899`.
- BRANCHES, commit `0d75f42c4e79654c8fbef57e6ce56a1f06cdf9a1`, 7,173 bytes, blob `6101c8d1856b55e0e770f9a4ce4c36d0702336d9`.

The cited universal sextic evaluation sequence, the saturated u channel, and the contraction sequence after twisting occur in the authenticated originals as claimed.

## Mathematical audit

1. The v channel has generic rank two: a rank-one saturated image would be an equivariant line O(e) with e at most two, forcing W' into a symmetric power of W of degree at most five, which is excluded. Its nonzero maximal minors have degree ten. A nonempty degeneracy divisor would therefore violate the minimum projective orbit size twelve. The rank-one quotient has degree twelve and no character ambiguity, giving O(12).

2. The nonzero c channel is nowhere zero by the same invariant-divisor argument in degree nine. Its quotient B has rank three, degree twelve, and degrees at least one. Equivariant splitting and central parity leave exactly the low-degree quotient atoms tested in Section 1. The W O(3) case is genuinely excluded by the nonzero composite tau c, not by a dimension count: a zero composite would factor c through W O(-1), whose indicated equivariant Hom space vanishes. All degrees of B are therefore four. Twisting by O(-4) gives the exact cohomology character difference Sym^10 W minus S tensor W, namely V.

3. Saturation of F holds on the whole product, not just for a generic auxiliary parameter. Local splitting of v and c, or equivalently their fiberwise injection, shows that F has rank three everywhere. Its locally free cokernel is flat over the auxiliary affine line. Quotienting first by c identifies the remaining relation with the graph of (t q u, v), giving the asserted extension by V O(4) with quotient O(12).

4. The composite q u is nonzero because u has generic rank two while the kernel of q has rank one. The vanishing of Hom_G(A O(2), V O(4)) makes the relevant connecting map injective. Hence delta(q u) is nonzero. Exactness of finite-group invariants in characteristic zero and equivariant Serre duality give a one-dimensional equivariant extension space. The twisted sextic evaluation sequence is a nonsplit member because there is no map from O(12) to P O(6). Endpoint scalar automorphisms identify the middle bundles of all nonzero classes. This proves both asserted fiber types without evaluating or scanning a selected parameter.

5. After adjoining O(2), all fiber degrees are positive, the rank and degree are five and twenty-six, and the invariant quotient to O(2) is unique up to scalar. The two H1 vanishings hold on every fiber. For this proper flat family they imply locally free pushforwards and arbitrary base change. Tensoring the relative diagonal resolution by the pullback of C_univ and pushing forward gives exactly the complete-evaluation sequence (8); det W=1 removes a determinant-character ambiguity. The vector-bundle quotient ensures fiberwise injectivity over the full product.

6. The H31 and E26 characters agree at both proved splitting types. Since the base has trivial G action, isotypic multiplicity sheaves are vector bundles on the affine line. They are free over C[t], so the stated global equivariant trivializations exist, noncanonically. The final invariant H0(C_t(-12)) dimensions follow directly from the two splitting types.

## Executable and reproduction audit

Both `python3 verify.py` and `python3 -O verify.py` exit successfully with the documented two-line output. The verifier uses explicit RuntimeError checks rather than removable assertions. Its arithmetic is exact over Q(sqrt(5)); its loops are bounded fixed-character checks and input authentication, not selected-instance computations. The supplied reproduction instructions reconstruct the three omitted originals from their exact commits and paths before running the verifier. The verifier does not purport to replace the geometric arguments reviewed above.

## Scope of the verdict

The result is a universal abstract counterfamily for the specified interfaces. The explicit core and the complete-evaluation pencil are attached to the same auxiliary quotient family, but compatibility with the historical HM complement choices and reduction maps is not proved and is expressly excluded from the no-go scope. Thus the result does not realize an HM family, select an actual HM coefficient, assign an actual incidence map, settle an actual row, or alter the frontier ledger.

No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix, or instance rank was evaluated in this review. No auxiliary parameter scan or unapproved large computation was performed. The only external actions were read-only retrievals of the three immutable originals; no external write or publication was made by the reviewer.
