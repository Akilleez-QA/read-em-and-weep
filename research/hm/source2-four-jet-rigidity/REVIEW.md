# Independent audit: universal four-jet spanning and the next source2 Gauss flag

## Verdict and immutable scope

**PASS. No substantive mathematical defect found.**

This review applies only to `PROOF.md` with SHA-256

`0378cf255b1666f3e8d03f588335a52352ba305d9765cdaea9c4965db8c2792a`.

The audit independently read the complete proof and the four cited immutable source files through the connected GitHub reader. It checked the all-point ramification argument, stabilizer characters and linearizations, actual derivative generation and saturation, full inverse-image propagation, annihilator duality, quotient extensions, and the claimed images of the induced Gauss maps. It did not select an actual source parameter, coefficient, point, derivative, matrix, or rank; perform a source-instance evaluation or parameter scan; or run a large computation. File hashes are provenance checks, not mathematical experiments. This is a written mathematical audit, not proof-assistant certification.

## 1. Source and novelty verification

The following source bytes were retrieved at their stated commits. Their SHA-256 digests are:

- PR751, commit `e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169`, `TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md`: `f7621cc508b76f8c12e52a0c5eddf067e18688a174265d930403fc8a69641026`.
- PR754, commit `044add76ebb14043a0edf73171517c90b9ef0c13`, `ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md`: `26afce66386de77a6ef3b511d9de1b3053b2a885c290bda84dccf4889562d5bc`.
- PR758, commit `063216038f3aefd65617651c2426721efafc7f9b`, `TWO-ONE-INDEX-TWO-EXACT-RESIDUAL-GAUSS-FLAG.md`: `65d1e4132f1be1d2b4323b2160d8562c28c5aa3350153b979a8e740ef40a1722`.
- PR784, commit `66aa488fb10158abcc2d35ce58b05b901d44b81a`, `research/hm/source2-second-defect-zero/PROOF.md`: `b0695ab0fbbfa9a4a4985f29c2818b15a8f6ec1977a5c2eae944d7c3b1bfe766`.

In particular, PR784's bytes match the reviewed digest asserted in the new proof. Its Section 5 gives a sheaf-surjective sequence with the full constant kernel V0 and explicitly identifies `(Q*)++` with the saturated full inverse image of `R++`. The new proof does not replace that conclusion with a generic-rank assertion.

PR751 supplies the actual rank-19 constant quotient, the actual complete degree-eight subspace V1, the exact intersection with R, and the saturated final degree-eighteen line. PR754 supplies the representation identities, including `Sym6 W = V + P` and the degree-eighteen subsystem decomposition. No abstract balanced-locus statement is being used as evidence that an actual source exists.

PR758's cited theorem concerns the backward flag of R. PR784 proves second jets and the first two forward residual transforms. Neither cited text proves the four-jet theorem or the third and fourth primal-kernel conclusions under review. Thus the stated novelty is supported relative to these sources. This is not an exhaustive repository-wide priority search.

At the 2026-10-22 audit, the current heads of PR758 and PR784 matched their cited commits. Both PRs were open drafts, not merged. This is a provenance qualification, not a defect in the conditional mathematical argument. The proof must continue to be understood as depending on the pinned written theorems, not as evidence of merge or formal certification.

## 2. The all-point Wronskian argument is valid

For ten linearly independent degree-eighteen sections, the determinant of order-nine principal-parts evaluation has degree

`10 * 18 + (0 + ... + 9) * (-2) = 90`.

At any point, an adapted basis with distinct vanishing orders `a0 < ... < a9` gives the leading Wronskian coefficient as the Vandermonde in those orders, expressed in the falling-factorial basis. It is nonzero in characteristic zero, including when some individual falling factorials vanish. Consequently the Wronskian is nonzero and its local order is exactly `sum(ai - i)`. This justifies both the global total weight and the local inequalities; no genericity assumption on the subsystem is needed.

Four-jet failure is equivalent to omitting at least one order among 0 through 4, or equivalently to `a4 >= 5`. Strict increase then forces `ai >= i + 1` for all six indices 4 through 9. Thus every failure has Wronskian weight at least 6.

The Wronskian construction is equivariant. Its zero divisor is invariant, regardless of whether one first trivializes the determinant character; the additional perfectness argument correctly makes that character trivial. The projective A5 point orbits have sizes 12, 20, 30, or 60. Hence a failure outside the size-12 orbit consumes at least `20 * 6 = 120` of the available weight 90 and is impossible. Orbitwise propagation applies to the jet-rank failure and to the local weight.

This leaves exactly the order-five stabilizer case handled in the next section. The proof does not use a rejected order-two fiber-sign argument or an unsupported claim that generic jet independence implies pointwise saturation.

## 3. The order-five character calculation retains the necessary fiber twist

For an order-ten lift g with eigenvalue lambda on the tautological line, `zeta = lambda^2` has order five. On P(W), the tangent character is `lambda^(-2)` and the cotangent character is `lambda^2`. The O(18) fiber has character `lambda^(-18) = zeta`. Therefore the order-j jet graded line has character

`lambda^(-18 + 2j) = zeta^(j + 1)`.

This is the correct twisted character, not merely the character of the local parameter. Inverting the generator consistently relabels all characters and does not affect the count.

The restrictions of A_std, V, and P are, respectively,

- `1 + zeta + zeta^(-1)`;
- `1 + zeta^2 + zeta^(-2)`;
- `zeta + zeta^2 + zeta^3 + zeta^4`.

The second formula follows by subtracting the third from Sym6 W; the third is the standard four-dimensional A5 permutation constituent on a five-cycle. Their sum has two copies of each character. The invariant vanishing filtration is exhaustive, its nonzero graded pieces are one-dimensional, and each embeds in the corresponding jet graded line. Semisimplicity for the finite cyclic stabilizer therefore proves that exactly two of the ten vanishing orders lie in each residue class modulo five.

The baseline pair in class j is `j, j + 5`, totaling 45 over all classes. If the order j in 0 through 4 is missing, the two orders in that class are at least `j + 5, j + 10`. This raises the total sum by at least 10; no decrease in another residue class can compensate because those classes retain their baseline lower bounds. Hence the local Wronskian weight is at least 10. An invariant size-12 failure orbit would contribute at least 120, again impossible.

This proves four-jet spanning everywhere for every subsystem in the stated class. Basepoint-freeness is an allowed hypothesis and is supplied in the actual-source application; no balancedness or choice of the P-multiplicity parameter is used in this proof.

## 4. Actual endpoint and residual saturation are proved, not assumed

The dual of pointwise jet-surjectivity is precisely fiberwise injectivity of the projection of the complete degree-eighteen osculating bundle `U_k^18` into the genuine final constant quotient. For k from 0 through 4 this projection is a subbundle map. Local generators `c, c', ..., c^(k)` therefore span its image without torsion or subsequent saturation.

The sequence `0 -> U_2^8 -> R -> C -> 0` is exact as a sequence of bundles by the pinned actual input. A local regular lift r of c is consequently legitimate. The degree-eight osculating leading coefficients relevant to k through 4 are 6, 5, 4, and 3, all nonzero. The Leibniz rule then gives the derivative-generated module as

`<U_(k+2)^8, r, r', ..., r^(k)>`.

After constant projection, the extra k + 1 generators are independent at every point. Together with a frame of `U_(k+2)^8`, they are independent in the actual constant ambient bundle. This is the essential pointwise statement: it proves that the generated image is a subbundle and already saturated, establishes the exact intersection with V1, and makes iteration of forward transforms legitimate. It does not rely on differentiating an arbitrary global bundle splitting.

The ranks are `2k + 4` and degrees are `2k^2 - 20k - 36`, giving the stated list through `(12, -84)`. The extension's twisting difference is 12, so its H1 vanishes. Averaging produces an equivariant bundle splitting in characteristic zero. The proof correctly does not treat this splitting as horizontal.

## 5. Full inverse images and annihilator degrees have the correct directions and signs

If F is the full inverse image of S under a constant quotient p, F contains the entire constant kernel. Every local section of S lifts to F, and differentiation commutes with p. These facts show equality of the unsaturated derivative-generated sheaves after taking full inverse image, not only equality at the generic point. Saturation also commutes with this operation because the corresponding ambient quotient sheaves are identified. Thus `F+ = p^(-1)(S+)` as saturated subbundles.

Applying this to PR784's actual full inverse image at stage two propagates to stages three and four. The resulting forward ranks are 21 and 23, with degrees -78 and -84. The original ambient space has dimension 30, so the annihilators have ranks 9 and 7.

For a saturated F in the constant dual ambient, its annihilator fits into

`0 -> ann(F) -> H tensor O -> F* -> 0`.

Consequently `deg ann(F) = deg F`, not its negative. Differentiating the original pairing gives the required annihilator/forward-transform relation at every step. This proves the asserted primal degrees -78 and -84 without any new plateau assumption.

## 6. Consecutive quotients and actual Gauss images are correct

For k = 3 and 4, exactness of the actual nested residual rows yields the quotient extension

`0 -> O(2k - 4) -> R^(k)/R^(k-1) -> O(2k - 18) -> 0`.

The complete osculating quotient formula `U_j^e/U_(j-1)^e = O(2j - e)` has the stated equivariant linearization: `W/ell` identifies with `ell*` using det W = 1. The extension has twisting difference 14 and vanishing H1, so it splits equivariantly.

Full inverse images cancel the same constant kernel at consecutive stages. Annihilator duality then dualizes, rather than negates or reorders ambiguously, the actual forward consecutive quotient. It gives

- `J3 = O(-2) + O(12)`, of degree 10;
- `J4 = O(-4) + O(10)`, of degree 6.

These degrees also equal the successive differences of the primal degrees, as required.

The induced derivative map `J_(k+1) -> J_k tensor Omega1` is well-defined and O-linear after quotienting: the Leibniz correction lies in the subbundle being quotiented out. Its kernel is exactly the next backward kernel, so it is a sheaf injection. This establishes the map from the actual flag independently of the numerical splittings.

For J3, both summands have zero Hom into the O(-12) term of `J2(-2)`. Hence the injection factors through the rank-two top subbundle `O(-2) + O(12)`. Source and target have the same degree 10, and their generically nonzero determinant is a section of O, hence a nonzero constant. The factorization is therefore an isomorphism everywhere. The high-degree rank-two subbundle is intrinsic: there are no maps from it to the lower summand, so it is independent of the choice of splitting. The remaining cokernel is O(-12), with no torsion.

The same determinant argument applies to `J4 -> J3(-2)`, where source and target both split as `O(-4) + O(10)` and have degree 6. It is an isomorphism everywhere.

## Boundary of the verdict

No correction to the reviewed proof is required. The result supplies additional necessary same-source compatibility, not a contradiction, realization, parameter selection, change to the fixed 23-label frontier, or proof of rank-three exclusion. It establishes no higher-jet claim beyond order four. The provenance qualification concerning open draft dependencies should be retained when describing publication status.
