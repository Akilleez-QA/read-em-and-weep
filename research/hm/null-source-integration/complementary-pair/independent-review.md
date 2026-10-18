# Independent review: complementary-pair transfer

## Verdict

**Pass for the stated symbolic finite-frame transfer and its explicitly limited scope.** No mathematical blocker was found in `PROOF.md`. The argument establishes coordinate renaming on arbitrary fixed raw ordered triples, transfers the finite polynomial-clearing property and the 217/210 degree bound, and correctly withholds equality of the two source-first alternating cochains and their full-cover values.

The distinction between arbitrary raw triples and the chosen alternating cochain is essential. The finite source artifact prescribes increasing-triple evaluation for its *cochain*. That prescription does not restrict the domain of the endpoint algebra proving polynomial clearing. Treating its finite proof as valid only on sorted triples would incorrectly discard a valid property transfer to freshly evaluated F34 triples.

Reviewed snapshots:

- `PROOF.md`: SHA256 `edf2efafdb0f1891af0c9adf02a133e683633466686813e0f8aba48f85abe6bc`.
- `test_transfer.py`: SHA256 `ef4a26e2ca59a24f612c6c05424186b82a2c307c6582d8ed98410b047722864b`.
- The three copied source files and the subsequently supplied `source-pins.json`.

## Checks and reasoning

1. **Source orientation and scalar normalization.** The copied JavaScript defines the gerbe as +(15/4) q(i,j,a) q(j,k,b), where q is the mask difference divided by the coordinate. Its `mu(F,G,a,b)` multiplies the derivative of F on the left and that of G on the right, with scalar 1/2. The finite proof and code specify the whole scalar as b minus one quarter of `tr(K20 (T12,i T01,j - T12,j T01,i))`. This matches the stated later-edge/earlier-edge order and preserves the additional trace factor. Endpoint Q and gerbe q remain separate. No matrix commutativity is assumed.

2. **Carrier invariance.** Coordinate permutation fixes every elementary coefficient e_k. Consequently it fixes each catalog rational matrix expressed in those coefficients and each individual H_c. It does not permute the carrier catalog, its matrix rows/columns, or its exceptional cases. The final proof explicitly distinguishes finite H5=v1*v3*v4 from the degree-four homogeneous equation v0*v1*v3*v4; restoring v0 is necessary. In homogeneous product coordinates the degree-one-in-each-coordinate elementary lifts, including v0=product Y_i, are individually invariant, so this correction preserves the symmetry and the assigned degree four. The added abstract control checks the restored v0 factor. The involution sends ordered coordinate pair (0,1) to (2,3), with no within-pair reversal or new sign.

3. **Coordinate and label maps.** The low-bit mask map, high-bit standard-tag map, derivative-index map, and exponent-vector map are consistent with x_i mapping to x_sigma(i). The proof defines the two bit conventions independently even though this involution happens to have the same numeric half-rotation in both encodings. Full-owner occurrence and seed labels are retained. The finite legal-factor, homogeneous legal-factor, and frame-monomial rules follow coordinatewise. The report appropriately treats these as formal frame renaming, not certification of a physical homogeneous representative.

4. **Raw ordered-triple scope.** Inspection of `DAG.core`, `DAG.tangent`, `DAG.q`, and `whole_source`, as well as the finite proof, shows no comparison or inequality involving vertex labels in the clearing argument. The inputs are endpoint matrices, binary mask bits, and positional slots. The inverse identity holds for arbitrary endpoint carriers. Thus the same factored rational identity and its degree argument apply to every fixed raw ordered triple. This is a mathematical extension of the expression's domain, not an assertion that the nonlinear expression alternates under a slot permutation. Repeated-label zero conventions, when needed for the alternating cochain, are separate.

5. **Denominator ownership.** In a trace product the slot exponents are (2,0,2) from K20, (0,3,3) from T12, and (3,3,0) from T01, summing to (5,6,5). The two derivative coordinates are distinct, so pair-legal factors occur at most once per coordinate and owner. The gerbe fits the same owned common denominator. The remaining carrier padding is (9,8,9). Coordinate renaming leaves these positional facts intact and never merges equal-valued factors owned by different occurrences.

6. **Degree bound.** The target degree is 14 times the sum of assigned carrier degrees, plus the paired-coordinate legal degrees minus two. Permuting coordinate labels therefore sends (217,217,210,210) to (210,210,217,217). The imported refinement from 218 to 217 uses only preserved metadata: exceptional carrier counts, coordinatewise zero-bit counts, entry weights, and the universal leading cancellation in `partial K - 2w rf K`. In the critical case every relevant endpoint bit is one, independently of vertex order; the gerbe factor in that coordinate vanishes, and the same tangent cancellation applies. No leading physical coefficient need be evaluated.

7. **Fresh source-first F34 property versus cochain equality.** Given a target O-increasing triple, its inverse image under sigma may be unsorted. Point 4 permits applying the raw F12 finite theorem to that inverse image, proving fresh F34 finite clearing and degree control. This does not compare the resulting raw inverse-image value with an alternatingly extended F12 value. The proof correctly reserves an exact cochain identity for the transported order O_sigma. Numeric masks 1<4 becoming 4>1 demonstrate that O_sigma and O differ. The example (1,2,4) becoming (4,8,1) is valid. An alternating extension alone cannot justify sorting inside the nonlinear formula, and the proof does not insert such a sign. It also correctly warns that sorting can change the middle owner carrying exponent six.

## Replay and provenance

`python -m unittest discover -s . -v` completed successfully: **13 tests passed**. These controls cover label involutions, elementary-symmetric subset invariance, ordered expression trees, a noncommutative negative control, ledger/padding arithmetic, coordinatewise degree metadata, abstract derivative naturality, q/Q distinction, and the source-order failure. They supplement the mathematical proof; they do not by themselves certify the physical source or establish actual non-equivalence of the two source-first cochains.

I independently computed the Git blob identifiers of the copied bytes:

- Finite proof: `806fa33f3492aac3f89431b46c9b493c0945751b`.
- Finite code: `d21bef0675234baca973dfdf8423e104e8267202`.
- Source JavaScript: `3dfed53a28b53b3c912a097971d89fc547330a5f`.

They agree with the supplied pinned manifest. The JavaScript SHA256 also matches the pin in the finite code. This verifies byte consistency with the supplied pins, not a separate GitHub commit-membership audit. The initially missing `source-pins.json` was supplied during review; that packaging observation is resolved.

## Scope retained

No copied source module was imported or executed. No physical source polynomial was expanded or evaluated, and no historical source checker was run. The primitive catalog identities, contraction authentication, and entry-degree bounds remain imported from the pinned finite construction. This review does not independently discharge physical homogeneous-frame identification, actual standard B coefficient realization, cover-order comparison, complete detector/functional transport, or any arithmetic/evaluation/admission gate.

No changes to the proof or tests were made by the reviewer.
