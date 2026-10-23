# Independent review: balanced sextic syzygies

Verdict: PASS. No correction required. This is a written mathematical review, not proof-assistant verification and not an additional actual-profile exclusion.

## Frozen bindings

- PROOF.md: SHA256 `2ea61681c18105cbba37e7135fc968aa9052e14eff71d963e8c374f55f041122`.
- verify.py: SHA256 `33037aac5522272aab35803c34fa7ea9bb502e8a9fbffd7aa7f7906b632f4e78`.
- RESULT.json: SHA256 `9ce764b24f07f7b1093bce917a08d366e69d0c70dfdb8ad1e969ee6f8bd8826a`.

All three complete immutable input originals were freshly retrieved independently and matched byte for byte, including Git blob SHA1 and SHA256: PR1145 proof (blob357b420e0254de52a3ae5d4510744478159a1a10), its character helper (blob0660296ed3874b59a14b1afc75da1d031c6d63a9), and the original class-character reference (blob9eb58f03edde15dd612087440d8180e9e16d1755). Full proof, provenance, checker, and reference were read.

## Mathematical verification

1. The unique nonstandard V in Sym6W consists of independent sextics. Its base divisor has degree at most6; invariance and the projective A5 minimum orbit12 exclude every nonempty base divisor. Thus evaluation is surjective as a bundle map, not only generically, and its kernel is a rank2 bundle of degree−6 with no global sections.
2. Ordinary splitting gives the three possibilities (1,5),(2,4),(3,3). In either unequal case the highest line is unique and consequently invariant. Line linearizations differ by characters; perfectness of SL2(F5) removes this ambiguity. The inherited central action is +1, whereas O(−1) has action −1. This excludes (1,5). For (2,4), the unique section of the twist by2 is trivial, contradicting the absence of a trivial constituent in V⊗Sym2W=P+D. No noncanonical equivariant splitting is substituted for this canonical-line argument.
3. After ordinary balancing, T_V(3) is trivial. Evaluation identifies it equivariantly with its two-dimensional section representation. Twisted exactness and vanishing H1 give its character V⊗Sym3W−Sym9W=W′. Hence the bundle identification W′ O(−3) is equivariant, not just ordinary.
4. Taking cohomology proves the full kernel and cokernel descriptions for every multiplier degree. At degrees0 and1 the cokernels have dimensions4 and2; at degree2 both kernel and cokernel vanish. For all degrees at least3 the kernel is W′⊗Sym^(d−3)W and the cokernel vanishes. The minimal threshold2 is therefore proved for the actual universal multiplication map, not inferred from equal source and target dimensions.
5. Polynomial syzygies are exactly global sections of the sheaf kernel in every degree. The equivariant bundle identification commutes with multiplication, giving the asserted free syzygy module W′R(−9), hence the exact graded resolution. Positive matrix degrees prove minimality. The Hilbert vector, length27 and top degree7 follow; no matrix of actual HM coefficients is used.
6. Pure powers span every symmetric power in characteristic zero, so the quadratic and higher fiber-span statements follow from surjectivity. This strengthens the universal net lemma used in PR1145 without asserting another actual geometric case exclusion.

## Reproduction

The supplied `python verify.py` and `python -O verify.py` both reproduce RESULT.json exactly:508 checks. No assertions are disabled by optimization in the active checker/helper.

The independent standard-library checker in this review directory uses exact conjugacy-class characters in Q(sqrt5), not the production McKay-product recurrence. Run:

    python independent_check.py
    python -O independent_check.py

Both produce the retained RESULT.json:958 checks, including81 orthogonality pairs, the required tensor identities, all multiplier degrees2 through29, the syzygy doublet, Hilbert vector and length. Finite controls support the proof; the bundle argument establishes the all-degree statement.

The reviewer did not evaluate actual HM/source coefficients, parameters, points, jets, tensors, instance ranks, or rerun any consumed experiment. No external state was changed. No full profile11 closure, global rank-three exclusion, full-adjoint invertibility, or original proof repair follows from this packet alone.
