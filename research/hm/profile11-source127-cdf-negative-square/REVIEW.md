# Independent review of the c-d-f negative-square package

## Verdict and exact object reviewed

PASS for the stated conditional theorem and its evidence boundary. I read the entire frozen proof, both original dependency proofs, the reproduction note and the complete verifier. The review is not an instance calculation, a formal proof certificate, or an independent re-proof of every ancestor of the two pinned dependencies.

Review performed on 2026-10-23 UTC. The following SHA-256 values bind this verdict to the exact reviewed bytes:

| File | SHA-256 |
| --- | --- |
| PROOF.md | c52e1e13f81d891a8dc835b37ec47b225e64882a79c9ba4a462d09dc9c43f058 |
| verify.py | f83d5937ad510c7e0354af3209d872b90ce81ed172c36af94126c6412dd7ca8c |
| REPRODUCE.md | 2b317aefe962b755ff699ad5970f2455fe9262bc62afd8807efa708b0c0dcd43 |
| audit-inputs/manifest.json | 9dbbe139c7e51b0f9a1776622b9cbd4b8a9cdaf67d89db3f35b9f911a4cfda94 |
| audit-inputs/ALGEBRA.md | 0d740d6f70de924b0442af71cb37e050165efbe9ab984a76f0e1e40b5d27a599 |
| audit-inputs/GENERATION.md | af574b04eb9d96a1117f8cfee327429bb9e38b4bad3932db4f45af849d4480a2 |

The frozen proof and verifier were not edited in this review. Reproduction inputs are local copies for verification, not proposed new mathematical results.

## Source authentication and current coordination boundary

Both dependencies were fetched directly through the GitHub connector at their specified commit and path, not inferred from a local filename or from a PR title. For each, the returned original UTF-8 content was compared byte-for-byte with the local input. Both comparisons returned true. Computing the Git blob digest from those returned bytes and independently from the local files gave the recorded object hashes:

1. [PR924 original proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/c6c25eaf0e5a67c27eee7c3ba4f000df55997692/research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md), 18,095 bytes, Git blob `83f5aee293995257459229e6b323522224ce8f3d`. Section 1 supplies the actual constant ambient normal form and quotient blocks. Section 4 supplies the simultaneous covariant identification with both original negative tensors using one determinant convention. Section 6 independently records the cohomology characters of the three target blocks.
2. [PR925 original proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2be52725fe471efdc64d74bd87702b581f9f6a48/research/hm/profile11-source127-cdf-positive-generation/PROOF.md), 11,449 bytes, Git blob `becd3300950c2379d1f03294863d8335a83a1087`. Section 2 proves the equality of the two actual aggregate images by applying the actual degree-zero cover to the parity-factorization identity. It does not rely on a chosen positive quadratic or a relation-free replacement of the actual module.

I also read [current PR1](https://github.com/Akilleez-QA/read-em-and-weep/pull/1), its complete current one-file patch, and the latest relevant discussion. Its head was `2531056eae05fdf31e8fb4ca3affc5907073ad73`; it was open, draft and unmerged. The latest returned discussion entry was [the PR925 handoff](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6358710621), updated 2026-10-23 06:13:03 UTC. That handoff expressly identifies this negative-square/cokernel/restricted-syzygy slice as separate from full-module minimal relations and asserts no actual-instance evaluation or frontier decrement. The reviewed proof respects that boundary. No discussion comment was used as a substitute for a mathematical dependency or as permission to publish.

## Mathematical audit

### 1. The product is the actual simultaneous product

The key dependency is stronger than character agreement. Under the single fixed determinant convention, PR924 Section 4 identifies both maps on the same actual spaces and variables:

    A_t(s)=t s,   B_t(u)=delta(t u).

It follows on every symbolic decomposable quadratic that

    B_u A_v(s)=delta(u v s).

Consequently the aggregate actual map is exactly `q_-=delta mu`, not a separately chosen isomorphic product. The scalar symmetry relation is inherited from ordinary multiplication. No variable, point, source parameter or actual tensor entry is evaluated.

From `H0(E)=0` and `H1(H O)=0`, the bundle sequence gives the exact sequence

    0 -> H -> H0(Q) -> N4 -> 0.

This uses cohomology of the actual inclusion and quotient, rather than replacing them by abstract representations.

### 2. The six-term sequence is exact without choosing complements

Write `U=Sym2(W) tensor N2`, `Y=H0(Q)` and identify `H` with `ker(delta)` in `Y`. Then

    Z=mu^(-1)(H),
    H_minus=H intersect im(mu),
    Pi=Y/(H+im(mu)).

The restriction `mu:Z->H` has kernel `ker(mu)` and image exactly `H_minus`. The map `H->Y/im(mu)` has kernel exactly `H_minus`; its cokernel is `Pi`. These statements prove every junction in the displayed six-term sequence. They also prove the two shorter exact sequences with dimensions `72/93/21` and `9/16/7`. No saturation statement, character subtraction or semisimple complement is doing the work of this exactness argument.

### 3. The image and its intersection with H use actual block sequences

The pinned ambient normal form makes the three bundle sequences actual direct summands. Multiplication onto `H0(O(18))` and `S tensor H0(O(7))` is surjective by binary-monomial factorization. The degree-one quotient summand contributes no source because `H0(O(-1))=0`. Therefore `im(mu)` is exactly the first two quotient-section blocks, of dimension `19+4*8=51`.

The injection of the constant space is block diagonal in this normal form. Its intersection with those first two quotient blocks is consequently exactly `C10 direct-sum C11`, of dimension 21. In particular the calculation is not the unsupported inference that a subspace with the same character must equal those blocks. Quotienting gives image dimension 30 and character `V+3P+3D`.

The remaining quotient has dimension seven and character `H1(O(-8))=Sym6(W)=V+P`, using the invariant determinant identification and the usual self-duality of these binary-group representations. Equivalently, the exact sequence with middle term `H0(Q_L)` has characters

    P+D -> (Wp+T) tensor W -> V+P,

and dimensions `9 -> 16 -> 7`. The identity `Sym7(W) tensor W=Sym8(W)+Sym6(W)` checks this result; it is not its exactness proof.

### 4. Restricted kernel and character arithmetic

The universal top-product map at degrees 18 and 7 has the other two Clebsch-Gordan summands as kernel. Thus

    ker(mu)=Sym16(W)+Sym14(W)
                + S tensor (Sym5(W)+Sym3(W)).

Its dimension is `17+15+4*(6+4)=72`. Adding the exact preimage of the 21-dimensional constant intersection yields `dim(Z)=93`, not 72.

The four character expansions in Section 4 are compatible with the fixed binary-icosahedral character table. Their sums give

    ker(mu)=1+3A+4V+5P+6D,
    H_minus=2A+2V+P+D,
    Z=1+5A+6V+6P+7D.

The independent dimension sums are `1+9+12+20+30=72` and `1+15+18+24+35=93`. The product source has character `1+5A+7V+9P+10D` and dimension 123; subtracting the proven image gives the same kernel character. The target has dimension 37, giving the exact four-term dimension pattern

    0 -> 93 -> 123 -> 37 -> 7 -> 0.

Semisimplicity over C permits a representation splitting of the short exact sequences, but it does not specify a distinguished splitting or the embedding of `Z` in the product source. The proof explicitly retains this distinction.

### 5. The positive conclusion is only the justified aggregate conclusion

PR925's actual equality `N4=im(q_+)+im(q_-)`, followed by the intrinsic quotient by `im(q_-)`, proves the aggregate surjection to `Pi`. This conclusion remains valid in the presence of module relations because generation is used through the actual equivariant cover.

The intrinsic objects are `im(q_-)`, `Z`, `Pi`, `H_minus` and their exact maps. The identification of `Pi` with a particular scalar-target complement `N4,L` uses the chosen normal form and is not promoted to a distinguished complement. Nor does aggregate surjectivity choose one positive quadratic or determine the other target components of `q_+`.

Finally, `Z` is exactly the kernel of the restricted symmetric-negative quadratic action on `N2=K3^+`. It is neither the entire quadratic-action kernel on `K3` nor the minimal relation space for the five-variable degree-zero presentation. The proof makes no unjustified identification with either of those larger or differently defined objects. It does not choose between the positive-compatible scalar and C^2 alternatives, establish a full-window/full-module lift, realize the abstract family by the actual HM module, or exclude any source, source-dual pair or stable label.

## Bounded execution and limits

I inspected the full checker before executing it. It uses only the Python standard library, two authenticated dependency files, a fixed nine-class character table and exact arithmetic in Q(sqrt(5)). There are no shell invocations, network calls, selected-instance data, searches over source parameters or large matrix computations in it. Its `require` checks remain active under optimization.

Both commands were executed with a ten-second timeout, and both returned exit code zero:

    python3 verify.py
    python3 -O verify.py

Each printed:

    PASS: exact immutable inputs; fixed character table; two universal product kernels;
    72/93/21 relation sequence; 9/16/7 cokernel sequence; 123/30/37/7 dimensions.
    The written proof/review establishes actual-map naturality and exactness.

The checker verifies character arithmetic, dimensions and its stated omission controls. It does not itself prove the actual simultaneous-map identification, block intersection, six-term exactness or degree-zero generation. Those obligations were reviewed in the written argument and its pinned dependency interfaces above. No formal proof-system validation, cumulative ancestor-suite replay or actual-HM evaluation was performed or is claimed.

No mathematical correction is required for this frozen version. The theorem is a useful exact conditional compatibility interface, not a complete solution or a frontier reduction. No remote repository write, external publication, merge or upstream submission was made during this review.
