# Whole-proof review of the sixteen-source opposite presentation

Verdict: ACCEPTED for the stated structural conclusions, subject to the two explicitly imported theorems. A separate reviewer read the complete final proof and verifier, freshly fetched both immutable originals, checked the actual quotient diagrams and evaluation bridges, and replayed the verifier in ordinary and optimized Python. Review completed on 2026-10-23 UTC. This is mathematical review, not proof-assistant formalization.

## Final bytes reviewed

SHA-256:

    PROOF.md
    195ce35f3bd1d91aa3bf858590980b3eb0a40a844d1ced2dcd0e45a85b915c7c
    verify.py
    f9fbe0223f96c35486e064b4184dc6704bacca89e21302646f454b50151650c3
    INPUTS.json
    e9f2e0f40532cc21ce4de01302aebfc5aca32eebdee98da1f58517eeae997ab5
    REPRODUCE.md
    78e9d51878c13826c84dcce93a7b4dbd50a0851bc588d176a973300ca03a72c3

Any change to these four files requires a corresponding review update. REVIEW.md does not hash itself.

## Fresh immutable-input authentication

The reviewer fetched each complete original by its repository path at its exact commit through the GitHub connector, rather than relying only on the author's audit copies. Each fresh UTF-8 payload matched the local audit copy byte for byte. Independently recomputing Git's SHA-1 blob identifier from `blob <byte-count>\0<content>` gave:

- INCIDENCE: commit 0201d67280fbfe0f87c84e7e726c3dc6c12bbecb, 13292 bytes, blob 7020da20437d326f2e4fdce32312a79aba770cad.
- REDUCED: commit 8c9847612b5f575b987cec9c62b72b099d745e44, 15657 bytes, blob 91dc4bc5c629e7ee3ba2694d2c05a4768b89b7ef.

INCIDENCE supplies the actual rank-six preimage, its component restrictions and unique cubic lifts, the universal sextic quotient, the nonzero weighted map, and the exhaustive necessary locally free C types. REDUCED supplies a canonical actual 26-to-31 presentation of the same C. Its historical allowance for torsion is not imported as an assertion that torsion remains: local freeness is supplied by INCIDENCE.

## Mathematical checks

1. Quotienting by the actual preimage L gives an injective source quotient and the unchanged actual C. Local freeness and saturation justify fiberwise injectivity, rather than a generic-rank argument. The W', T6 and S restrictions of L occupy different actual isotypic components; tensor Euler and dual cubic evaluation therefore give the asserted splitting type of G26.

2. The constant source is defined intrinsically as the complete-evaluation image of G26, not as a chosen direct summand. Its projection into H28 O is injective by the two verified vanishing Hom spaces. Quotienting its actual lifted image preserves all maps and gives the twenty-source presentation. Only existence, not canonicity, of the displayed target splitting is used.

3. The surviving weighted cubic line is killed in C and consequently has a unique lift through the injective twenty-source map. The quotient of the target by this line is locally free, which makes the source lift saturated. Its coefficient direction lies in the S isotypic component, giving G19 with intrinsic constant source A O. The projection of that A O to H22 O cannot vanish, because otherwise a rank-three bundle would inject into a rank-two bundle. Irreducibility then makes this projection fiberwise injective. Its potentially nonzero weighted component is explicitly retained by quotienting the actual graph. This proves the sixteen-source endpoint without an invalid splitting or discarded off-diagonal map.

4. The complete-evaluation bridges use the actual isomorphisms H0(Y)=H0(C) and H0(Y21)=H0(C), which follow from the acyclic negative sources. The constant quotients have zero evaluation kernels. Naturality therefore identifies the marked T6 and S+T6 kernels inside M_C. The imported reduced presentation itself identifies H31 with H0(C), so M_C is its actual source, not merely a matching representation. The selected coefficient targets are the actual global-section images of the weighted subbundles. The proof does not confuse injectivity of those global-section maps with injectivity of their induced sheaf maps to C, and does not identify the new marked blocks with the earlier degree-one-generated line.

5. Saturation of the surviving image is checked in all seven necessary types. In the degree-seven case, an invariant common-zero divisor cannot exist because every nonempty projective orbit has at least twelve points. In degree thirteen, the only possible common divisor has degree twelve; its defining line has trivial G-character because G is perfect, leaving the impossible W' covariant in degree one. Thus the rank-one images are everywhere surjective onto their line targets. The other four rows use identities, tensor Euler, or the dual universal sextic sequence, all with locally free quotients. The resulting image is canonical up to the harmless scalar description of its one-dimensional Hom line, and no actual row is selected.

6. The displayed representations and ranks/degrees agree throughout. In particular the final source has rank16 and degree-16; the target has rank21 and degree10; the unchanged cokernel has rank5 and degree26. The final evaluation block has source S+T6, target A+P+D and quotient W' O(5), with all embeddings inherited from the actual construction.

## Replay and scope

Both `python3 verify.py` and `python3 -O verify.py` passed after fresh-input authentication. The reviewer also independently checked the two remaining S source multiplicities, E20=E16+S, W' tensor T6=A+P+D, and the possibility of a nonzero A-to-weighted graph component. The verifier uses explicit runtime requirements, so optimization does not disable its checks.

No actual HM/source tensor, selected coefficient, point, parameter, matrix, instance rank, scan or large computation was evaluated. No external write was performed for this review. The result is an actual structural reduction and marked evaluation subblock, plus a saturated canonical image; it does not determine the actual row, the initial marked line's survival, or any unresolved actual scalar.
