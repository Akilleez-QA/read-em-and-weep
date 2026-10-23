# Independent mathematical review

## Verdict: PASS

Reviewed artifact: `PROOF.md`.

Exact reviewed SHA256:

    06fe9d6bf5f51d1d38ff5f594f93703cf91b48d6cffcf7256c3e281de631365d

Review date: 2026-10-23 UTC.

The proof establishes its stated conditional conclusion: for an actual source127 c-d-f occurrence satisfying the pinned actual-HM inputs, the **equivariant, fixed-variable represented negative-pencil algebra** has only the common scalars compatible with the one canonical invariant product Q. Consequently its positive-aggregate-compatible subalgebra is scalar as well. There is no substantial mathematical blocker or required correction in the reviewed version.

This is a review of the new deduction and the exact scopes of its six immediate inputs. It does not independently reconstruct the deeper geometric theorems imported by those inputs. In particular, the actual second-Bockstein nonvanishing remains an essential imported theorem, not a conclusion of character bookkeeping.

## 1. Authentication of all six originals

I independently calculated the ordinary Git blob identifier

    SHA1("blob " + byte_length + NUL + exact_file_bytes)

for every copied original, with no text normalization. Each equals the identifier in the pinned manifest:

- `ALGEBRA.md`: 18,095 bytes; `83f5aee293995257459229e6b323522224ce8f3d`.
- `GENERATION.md`: 11,449 bytes; `becd3300950c2379d1f03294863d8335a83a1087`.
- `BRANCH.md`: 9,135 bytes; `49a0b5ef9f6b2fa6fb5e46edd28fec4f4d73be79`.
- `DOUBLE-LINE.md`: 14,193 bytes; `a428ac4b4b8cb6b67b7b8e3b1625352468adeb05`.
- `FIRST.md`: 4,014 bytes; `fe4410bbba05060545b22ac6bc80aac8e7c62ce4`.
- `SECOND-NONZERO.md`: 10,036 bytes; `21c7af094d7088f38ab0ee8fc25b01952ea13d11`.

The originals' own cross-references, representation conventions, actual cohomology spaces, and theorem statements agree with the interface used in the proof. An initial copy-format discrepancy, consisting of an extra terminal newline, was repaired before this final review; the final files above are exact authenticated blobs. The verdict applies to the final proof hash displayed above, not the earlier draft.

## 2. Actual maps and imported scopes

1. `ALGEBRA.md`, Sections 2-4 and 6, gives the entire represented algebra, including singular endomorphisms, with multiplication `(a,b,d,w)(a',b',d',w')=(aa',bb',dd',a w'+d'w)`. Its reconstruction is covariant and simultaneous for both actual negative linear arrows. It therefore legitimately implies `e4 T_a=T_a e2` for every negative quadratic `a`: first check products of two negative linear forms and then extend linearly. No separately chosen or dualized pencil is substituted.
2. The same input identifies `N2=K3^+=H1(B(2))_+` and `N4=K5^+=H1(B(4))_+`, as well as the displayed source and target block characters. The radical action on `Y_L` is the genuine nonzero P map into `Y_F`, not merely a possible abstract arrow.
3. `GENERATION.md`, Section 2, proves the equality of actual images `Y=im q_+ + im q_-`. The parity argument works even when the degree-zero generators have differing inversion signs. Only this equality and the represented negative commutation are needed here.
4. `DOUBLE-LINE.md`, Sections 3-4, proves the equality of embedded subspaces `im q_+=im Q`. It concerns quadratics in the positive coordinate variables `Sym^2 V=1+D`, not all inversion-even quadratics. The proof uses exactly this restricted equality to replace `im q_+` in the generation identity. It does not improperly extend the positive-family unobstructedness theorem to negative directions.
5. `BRANCH.md` supplies the actual invariant-product characters and explicitly treats the graph shear in the second idempotent type. The new proof rederives the relevant classification and saturation under the single-Q hypothesis; it does not assume that Q-compatibility implies full aggregate compatibility.
6. `FIRST.md`, especially Sections 3-4, concerns precisely multiplication by `q0+t a` from `H1(B(2))_+` to `H1(B(4))_+`, where `a` is an arbitrary negative quadratic in `A=Sym^2 W`. The word "positive" in its title refers to the cohomology parity, not to restricting `a` to positive-coordinate directions. It proves the entire first Bockstein is zero and defines the second class on the original kernel.
7. `SECOND-NONZERO.md` states that the second Bockstein for this same pencil is nonzero as an A-to-P quadratic family, and zero on D. Its invariant-cone closure and uniform cubic/quintic filtration hypotheses are retained as proved geometric inputs. The new proof uses only the nonzero A-family, not a value of its scalar, pointwise nonvanishing for every `a`, a generic rank, or the deeper dependency derivations.

## 3. Single-Q algebra reduction

`D_Q` is a complex linear unital subalgebra: the intertwining equation is closed under addition, scalar multiplication, and composition. If `e2=lambda id`, negative commutation makes `e4=lambda id` on `im q_-`, while Q-compatibility gives the same on `im Q`. Their actual spanning equality forces this on all Y. The represented block action then forces `a=b=d=lambda` and `w=0`. In particular the map `D_Q -> C^2`, `e -> (a,b)`, is injective.

Its image is a complex linear subspace containing the diagonal. Hence it is either the diagonal or all of `C^2`. In the nonscalar case, the unique inverse image of `(0,1)` is idempotent because this map is an injective algebra homomorphism. Direct substitution into the actual multiplication law gives `d(d-1)=0` and `(d-1)w=0`, so the only types are exactly

    p_F=(0,1,0,0),   p_B(w)=(0,1,1,w).

The factorization `d(d-1)=0` proves this over C; the verifier checks this polynomial factorization rather than searching through numerical parameter values. The represented action also excludes a hidden middle-degree endomorphism invisible at both endpoints: the pinned faithful algebra description fixes the whole triple.

## 4. Type B exclusion, including the shear

For `p_B(w)`, the source eigenspaces are `X_F` and `X_B`. On Y its kernel is exactly `Y_F`, and its image is

    Y_B + {eta_w(z)+z : z in Y_L}.

The latter is a direct graph sum, equivariantly isomorphic to `Y_B+Y_L`. Because Q intertwines the two idempotents, it is block diagonal for these eigenspaces. The V multiplicities are therefore `1 -> 0` in the kernel block and `1 -> 2` in the image block. The image contains at most one V, contrary to the actual two V constituents. This handles every shear, including zero, and uses semisimplicity over C. No actual multiplicity matrix is evaluated.

## 5. Type F saturation and identification of the original A

For `p_F`, the Q blocks are `X_F -> Y_F+Y_L` and `X_B -> Y_B`. Their componentwise maximal image characters are respectively `V+P+D` and `V+2P+2D`. These sum to the actual image character. Since the target blocks are disjoint and each constituent multiplicity is bounded independently, equality of each total forces equality in each block. In particular, the B block has image exactly `Y_B`, not just an abstract representation of the same type, and has kernel A.

The whole X contains one A, all in `X_B`, and none in `X_F`. Consequently this B-block kernel is the actual unique A-isotypical subspace of X. It is precisely the A in the original `ker Q=A+D`. The argument does not choose an embedding of a repeated A, because no repeated A exists. Possible ambiguity in a D kernel or P image does not affect it.

Since `p_F` already lies in the negative-pencil algebra, every `T_a` carries `X_B` into `Y_B`. This is the extra preservation needed for the obstruction contradiction; Q-surjectivity alone would not suffice.

## 6. Formal lifting and the exact second-Bockstein comparison

The general surjective-block lemma is correct. If `Q:U -> Z` is onto and `T_a(U)` lies in Z, choose any linear section `s`. Then `M_a(t)s=id+t T_a s` has a formal inverse. For `k in ker(Q|U)`,

    k(t)=k-s(M_a(t)s)^(-1)M_a(t)k

has constant term k and satisfies `M_a(t)k(t)=0`. There is no convergence assumption, finite-order truncation claim, or need for an equivariant or canonical section. This establishes unobstructed formal kernel lifting inside the hypothesized block.

For the exact obstruction used in the proof, `u=-s T_a k` satisfies `Qu=-T_a k`; furthermore `T_a u` lies in `Z`, hence in `im Q`. The potential order-two error therefore has zero class in the original cokernel.

The normalization comparison in Section 4 closes the important scope issue explicitly. In `FIRST.md`, write `k=h xi` and `a xi=q0 zeta_a`. Its actual correction is `u0=-h zeta_a`, and its second class is

    beta2_a(k)=-[a h zeta_a]=[T_a u0].

The block correction and imported correction obey the same equation, so `u-u0` belongs to the original `ker Q`. Global first-Bockstein vanishing gives `[T_a(u-u0)]=0`. Thus the imported second class equals the block-zero class. This requires first vanishing on the whole kernel, which the authenticated input supplies; first vanishing only on A would not automatically justify every correction change.

With `U=X_B` and `Z=Y_B`, the argument forces vanishing on the original A for every direction a. That contradicts the imported nonzero quadratic family. Nonzero as a family is sufficient: the proof does not require nonzero for all a. Changes of harmless scalar representative of the invariant quadric, source/target equivariant coordinates, or common boundary sign cannot turn nonzero into zero.

The argument concerns exactly the two-term multiplication pencil. It does not conflate this beta2 with a higher gate, the doubled-line restriction boundary, a different geometric normal-lifting obstruction, or a chosen associated-graded proxy.

## 7. Corollary, factorization, and logical boundary

Every aggregate-compatible endomorphism is Q-compatible because q0 is one positive-coordinate quadratic; common scalars always remain. The scalar conclusion for the aggregate follows in the correct direction without asserting the converse.

The auxiliary map `psi(a tensor Qx)=pi T_a x` is well-defined because first-Bockstein vanishing kills the ambiguity from `ker Q`. It is onto because `Y=im Q+im q_-` and `q_-` is the aggregate of the `T_a`. This is an aggregate surjectivity statement, not surjectivity of one direction. It is not sufficient on its own to eliminate Type F; the nonzero second symbol is genuinely additional input.

No part of the proof forces a nonscalar compatible idempotent to exist. Eliminating both possible nonscalar types therefore excludes only an endomorphism-compatibility branch, not the c-d-f source or a source-dual pair. The conclusion is about the specified equivariant fixed-variable algebra, not an enlarged non-equivariant commutant or variable-changing symmetry algebra. The proof does not construct an actual source, force a full-module lift, change frontier counts, prove generic surjectivity, or settle algebraicity.

## 8. Independent bounded checks and replay

I performed an independent exact-byte hash check and a separate tiny character-arithmetic check of the V bottleneck, Type F saturation, unique A kernel, complementary D kernel, and total dimensions 41 and 37. These use only the pinned representation multiplicities.

I also read `verify.py` and `REPRODUCE.md` and ran both of the documented commands successfully:

    python verify.py
    python -O verify.py

Both report PASS. The checks remain active under optimization because the verifier uses explicit exceptions rather than Python assertions. Its bounded Neumann-series multiplication agrees with the general formal identity established mathematically above. The verifier is appropriately described as source-authentication and bookkeeping support, not proof-assistant formalization or a reproof of the imported geometry.

Final replayed supporting-artifact SHA256 values:

- `verify.py`: `ec377d4d6b63bbb73f9bcb49aa0e6a38c67887bdb81e3784e200975ce97b9c73`.
- `REPRODUCE.md`: `a4523b09fb2980ee06f697fcb64562cac5f8c603a04a8119baf6d2bc1a81fffe`.

No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, scans, or large computation were used. No proof edits, external publication, upstream submission, or merge were performed by this review.

## 9. Documentation-only reproduction delta review

The revised `REPRODUCE.md` explains how to reproduce a five-file package containing `PROOF.md`, `REVIEW.md`, `REPRODUCE.md`, `verify.py`, and `audit-inputs/manifest.json`, without republishing the six upstream originals. I reviewed this documentation-only delta at the supporting-artifact hash above. `PROOF.md` and `verify.py` retain their exact previously reviewed hashes; the mathematical PASS verdict is unchanged.

The example constructs each raw GitHub URL from the fixed repository, the manifest's full immutable commit, and the exact upstream path. I checked all six constructed URLs against their corresponding pinned manifest source URLs. All local destination names are the expected simple filenames under `audit-inputs`. The code reads response bytes, calculates the ordinary Git blob identifier, rejects a mismatch before writing that file, and writes binary bytes without newline or encoding normalization. Its authenticated-client fallback retains the same immutable revision and byte-authentication requirements; it does not authorize bypassing access restrictions or substituting a branch head.

I extracted and compiled the documentation's Python example without changing its code, then executed it in a fresh temporary manifest-only fixture, replacing `urlopen` solely with a local byte provider containing the six already authenticated originals. The fixture checked each requested URL and the 60-second timeout. All six resulting files matched their original bytes exactly. Both `python verify.py` and `python -O verify.py` then passed in that reconstructed package. A separate corrupted-response fixture raised the prescribed hash-mismatch exception before any source file was written.

This validates the example's syntax, exact paths, byte-preserving reconstruction, rejection behavior, and subsequent verification workflow. Live network availability or anonymous repository access was not tested or promised; the documentation explicitly identifies the network/authentication prerequisite. The delta review made no network requests, publication, or external writes. No correction is required.

## Blockers and disposition

None for the reviewed new deduction. The pinned actual geometric assumptions remain essential and inherited; their deep proofs are outside this review's assigned scope. No correction is required before using the result at that stated scope.
