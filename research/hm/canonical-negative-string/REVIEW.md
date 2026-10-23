# Independent whole-proof review

Verdict: PASS for the theorem and the stated scope of PROOF.md. This is an independent mathematical review with a bounded arithmetic replay, not a formal proof-assistant certificate. The review accepts the four cited mathematical results as immutable inputs; it does not recursively re-prove all of their antecedents.

## Exact reviewed artifacts

Reviewed on 2026-10-23. This verdict binds the following SHA-256 hashes:

| Artifact | SHA-256 |
|---|---|
| PROOF.md | `6c2f23ce2110ee91b05631e1e31932a5fe5ecb36e86731cb5e79518879f7b67d` |
| verify.py | `693938dfeef8d570c9785a90df91184417e6649e308243048ec1ff63166fbb58` |
| INPUTS.json | `60244f615d1f81aafba727cda64b048ef0c95e760e345fc178b99777bdd84e16` |
| REPRODUCE.md | `6ff5f27005d12461416520635b908f39e2f46b9b82f0122c14d14d80cc41df49` |

## Fresh input authentication

I separately fetched all four originals from Akilleez-QA/read-em-and-weep through the GitHub connector at the exact commits and paths in INPUTS.json. For each result I checked the connector's blob SHA, independently recomputed the Git blob hash from its returned UTF-8 bytes, and compared those bytes with the corresponding local audit-input. All three checks agreed:

| Input | Authenticated Git blob SHA-1 |
|---|---|
| STEINER | `098af4cb145229e6c450dbe863eda8a01a2cace5` |
| SYMMETRIC | `0b6f5a6fb20c75116ebdb06d4af2bc3be64ad241` |
| ACTUAL | `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3` |
| QUADRIC | `019c1f31773476f0a4877d88632ce5d46fbd4b9f` |

STEINER supplies both the actual nonzero W-to-A symmetric multiplication block and the current normalized-monad K-class. SYMMETRIC supplies h0(F(3))=4 and the actual natural symmetric-square isomorphism. ACTUAL explicitly supplies the exact bundle presentation of E, with the displayed M3 and M4 representations. QUADRIC explicitly states the required ambient H0(B(4)) vanishing. The present argument does not depend on QUADRIC's subsequent rank-33 derivation or on a conjectured rank of a new map.

## Mathematical checks

1. **Actual degree-five sections.** The K-class calculation uses the current monad labels, not a different normalization. Its twist-three terms have no positive cohomology: this is immediate for the nonnegative line-bundle terms and the usual exterior Euler/Bott calculation for Omega2(5). Equivalently, hypercohomology of this acyclic three-term monad can contribute only in degrees zero and one. Thus the Euler identity P-W is genuinely [H0]-[H1]. Semisimplicity makes the P multiplicity in H0 at least one; its dimension four and the independently supplied h0=4 force H0(F(3))=P. The natural symmetric-square isomorphism then gives H0(B(5))=Sym2 P=1+P+D, entirely center-even. No Euler characteristic of B(5) is substituted for its section representation. The determinant identification is compatible with the equivariant structures because SL2(F5) has no nontrivial one-dimensional characters.

2. **Both joint-negative kernels.** The two negative coordinates form the regular sequence defining the positive plane. Tensoring its Koszul sequence by the locally free B(k+2) gives precisely the displayed short exact sequence. The possible kernel on H1(B(k)) comes from H0(I_R B(k+2)). At k=2 this group vanishes by its inclusion in H0(B(4)). At k=3 only its odd part is required, and this embeds in the already proved zero odd part of H0(B(5)). Taking parity components is exact. The resulting statements concern the simultaneous two-coordinate map, not injectivity of either individual multiplication map. The proof correctly does not claim unrestricted degree-three injectivity.

3. **Canonical symmetric descendants.** The initial alternating relation in W tensor U1 vanishes by STEINER. Commutativity of the actual polynomial-ring action propagates every multiple of this relation. The binary Koszul presentation of the positive-degree symmetric module therefore factors its degree-d descendants through Sym^d W. This is an actual-map factorization, not merely a character identification. If f3 vanished, all of U2 would lie in the first joint kernel; if f4 vanished, all of U3 would lie in the odd second joint kernel. Both are impossible. Irreducibility of Sym3 W and Sym4 W then makes f3 and f4 injective. Rescaling the initial identification rescales all descendants together, proving that their actual image subspaces and their multiplication structure are canonical.

4. **Inherited 50-to-33 quotient.** The selected S O(-1) maps into the selected D O by the binary cubic multiplication map. It is fiberwise injective, with quotient O(4). Since the original 54-to-37 map is onto everywhere, this subcomplex has zero intersection with E; quotienting it preserves E as the kernel and preserves surjectivity. The quotient source has rank50 and target rank33. A constant equivariant complement to U4 identifies the latter with O(4) plus (2V+4P+2D) O. Such a complement exists by finite-group semisimplicity, but is correctly not called canonical. This quotient is taken from the original maps, not reconstructed from rank and degree.

5. **Forced six-direction quintic functional.** For any such target splitting, the induced projection from the quotient source to O(4) is onto. Equivariant Hom identifies its coefficient space with Hom_G(3W'+2S+6T6, Sym5 W), so it is a nonzero functional on the six T6 multiplicity directions and is zero on the other irreducible blocks. A direction on which that functional is nonzero contributes the complete quintic evaluation T6 O(-1) to O(4). Its universal kernel is D O(-2); the five unused T6 directions and the W', S blocks remain O(-1)-twisted. Choosing the multiplicity complement is legitimate and makes no assertion about a selected actual coefficient value.

6. **Inherited weighted presentation.** Taking the kernel of the target projection leaves a surjection to (2V+4P+2D) O with exactly the original E as kernel. The source is D O(-2) plus (3W'+2S+5T6) O(-1), rank49 and degree -54; the target has rank32 and degree zero. Consequently E retains rank17 and degree -54. The construction retains all remaining actual off-diagonal maps and does not infer a splitting of E from this presentation.

## Verifier and scope

I read verify.py and freshly ran both `python3 verify.py` and `python3 -O verify.py`. Both completed successfully with the documented output. The checks use exact rational arithmetic in Q(sqrt(5)), nine fixed character classes, representation identities, and elementary rank/degree bookkeeping. The validation conditions are explicit runtime requirements and therefore remain active under Python optimization. Fresh input authentication also confirmed the actual original bytes used by both runs.

The checker does not prove symmetric-square exhaustion, Koszul exactness, actual commutativity, or preservation of kernels in the diagrams; those are the mathematical arguments reviewed above. REPRODUCE.md accurately distinguishes these responsibilities and explains reconstruction of the omitted immutable originals while preserving their bytes.

No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix, instance rank, source-pair scan, or large computation was evaluated during this review. The result proves the canonical W-to-A-to-S-to-D string and the inherited weighted presentation before any remaining source-pair choice. It neither excludes a remaining source-pair alternative nor settles an opposite-bundle type, smoothing, vertex scalar, source realization, or the original algebraicity goal. These limitations match the proof's stated contribution.
