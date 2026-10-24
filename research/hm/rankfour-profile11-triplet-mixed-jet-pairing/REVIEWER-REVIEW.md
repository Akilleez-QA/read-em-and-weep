# Independent entire-proof review

## Exact subject and verdict

**PASS, conditional on the retained actual-geometric hypotheses of the three complete direct inputs and their stated transitive assumptions.** This verdict concerns the ENTIRE `PROOF.md`, including the statement, every section 1–8, and the retained boundaries, not merely its executable checks or selected lemmas.

- Exact reviewed length: **14593 bytes**.
- Exact reviewed SHA256: **3e1ce0d1589d694d578796a90398cbdaf8fdf6fb340158b5098ad3f79cdfa95b**.
- No mathematical correction to these frozen bytes is required by this review.
- The mathematical conclusion is conditional: in the residual simultaneous rank-seven defect, the forced lower-column k=2 case admits the actual constant equivariant nondegenerate symmetric map `h: V -> V*` with `u = h v`. Auxiliary coefficient span fifteen and actual auxiliary jet separation through order nine follow. The embedded original P-kernel is restricted to at most two fixed universal subspaces. There is no occurrence or exclusion conclusion.

## Independent source authentication

I read the complete frozen proof and all three complete direct inputs, not excerpts. I independently fetched each input afresh through both its immutable repository path/commit and its Git blob. All six fresh responses were successful. I compared the UTF8 bytes from those two routes with the local input, checked the exact length and SHA256, recomputed Git's `blob <length>\0<bytes>` SHA1, and checked the path response's returned blob SHA. All comparisons passed.

1. `inputs/rankseven-equality.md`: commit `f5895c822322b4ddab07e51a97874d4528fb5b88`, 15139 bytes, SHA256 `a6e56f535af652d3ff437cc5041527636f601751ae24285ba1ec91670f4db7ae`, blob `6a4ef8941ee4cee131992bdf9cd7657635b058c5`.
2. `inputs/nine-jets.md`: commit `66a6bfe8dd424da58f3d775be1818d1f4f71eff1`, 12744 bytes, SHA256 `44ee429fa26b65b68b2668ce69dff219e4a4daf0a6bdaa9fac0e94aa8a631b3a`, blob `916cc6a3bc1cf8ad07e019f00a1f5ebf867311d6`.
3. `inputs/defect-capacity.md`: commit `ca235151d5d93bbead2beffa7640fbd0741aec43`, 16069 bytes, SHA256 `135c74cc09d4f1da1fcae16c330e0c9d5a9d05d615e59a2461dd532cbb91a62f`, blob `175af94697c44f3140bb2c1d04978931c255b3fe`.

The repository is `Akilleez-QA/read-em-and-weep`; the exact paths and verified links are recorded in `REVIEWER-AUTHENTICATION.json`. `REVIEWER-FRESH-FETCHES.json` contains this reviewer's independently obtained path and blob contents. Author fetch records and separate audit notes were not used as authentication or mathematical evidence. Transitive proofs were not silently promoted into newly verified results: their actual-geometric hypotheses remain retained assumptions as the frozen proof states.

## Entire mathematical audit

### Statement and section 1: actual maps and mixed incidence

The direct inputs distinguish the original degree-eighteen curve in V from the auxiliary degree-eighteen line in V*. They justify the original fifteen-dimensional coefficient system and actual four-dimensional P-kernel, the original globally separated jets through order nine, and the surviving lower-column auxiliary fourth-jet bundle. No auxiliary full-span assertion is imported.

The upper normal projection of the actual derivative on F6 is the restriction of the derivative on B6. Its vanishing on U4, supplied by the lower coherent image in the complete rank-seven input, gives `U4 subset ker beta_(B6) = B7`. The equality with the actual derivative kernel is supported by the original nine-jet input. Thus the mixed order-seven/order-four pairing vanishes as an identity along the whole base, not at selected points.

The actual coefficient maps have the correct directions: `q: E ->> V`, `r: E -> V*`, where `E = H0(O(18))*`. The second is nonzero but is not assumed onto. The fixed determinant/apolar convention is sufficient to express the small physical character identities; it does not supply an arbitrary identification of the actual V with V*.

### Section 2: rectangle to twelfth diagonal power

The rectangular vanishings provide an anchor on every total-order diagonal from zero through eleven. Differentiating the identically zero restrictions of total order n-1 gives the adjacent-sum equations on all n+1 mixed restrictions of order n. One zero anchor forces the whole order-n chain to vanish. This is valid inductively for all n <= 11, including n=11 with its boundary anchor (7,4).

Local changes of trivialization introduce only lower-order terms, which have already vanished. Vanishing of all these mixed restrictions implies vanishing of the normal Taylor coefficients of orders below twelve, so the biform belongs to the twelfth power of the diagonal ideal. The diagonal is the Cartier divisor defined by the determinant section Omega of O(1,1), yielding the global residual section of O(6,6). No quotient connection is used.

The biform is nonzero: `r*` is nonzero and composing it with the surjection q cannot annihilate it. This nonzero claim does not assume that r has full rank.

### Section 3: invariant residuals and symmetry

The fixed decomposition of `Sym6 W tensor Sym6 W` contains exactly one copy of each even symmetric power from zero to twelve. The fixed character identities give one invariant in degree twelve, one in degree zero, and none in the intermediate summands. The polarized universal f12 and Omega^6 are nonzero representatives in those two distinct summands, so they span the invariant residual space.

Exchange of the two degree-six blocks fixes the Cartan polarization, and both determinant exponents six and twelve are even. Consequently every allowed residual biform, and hence the actual biform, is symmetric. The scalars describing its two components remain unselected. In particular f12 is the fixed universal invariant, not an actual HM coefficient chosen for a computation.

### Section 4: correct adjunction and sixth transvectant

The coefficient identity is `H = r* q`, where `H(a)(b) = r(b)(q(a))`. Symmetry then gives the distinct but equal factorization `H = q* r`. The first proves that the actual K is contained in ker H; the second will later allow r to factor through q. This distinction is essential and is correctly maintained.

The degree-eighteen apolar map j is symmetric. Therefore `B = j^(-1) H` is self-adjoint for j. The proof does not confuse this with symmetry of B's matrix in an arbitrary basis.

The map from a universal degree-twelve form F to `Omega^12 Polar_(6,6)(F)` is nonzero and SL2-equivariant. There is exactly one Sym12 summand in `Sym18 tensor Sym18`. Apolar adjunction preserves this multiplicity. The sixth transvectant is another nonzero equivariant realization of that summand: its output degree is `12 + 18 - 2*6 = 18`. Thus the proportionality asserted in the proof is justified by multiplicity one, with a nonzero universal factor absorbed into alpha. Omega^18 gives the nonzero scalar identity component. If alpha vanished, nonzero B would be invertible, contrary to its containing K in its kernel. Hence alpha is nonzero.

### Section 5: genuine order six and rational kernel bound

In the displayed unnormalized transvectant, the highest-derivative coefficient from the second factor is `(-t)^k`. It cancels the transvectant sign, giving exactly the positive binomial radial sum written in equation (18). Euler homogeneity iterated with the direction held fixed gives the falling factorial `12*11*10*9*8*7` times f(t). This is nonzero in C(t), because the universal homogeneous f12 is nonzero. Multiplication by nonzero alpha and addition of a scalar order-zero term cannot remove this order-six symbol.

The rational-function Wronskian argument is valid over the differential field C(t), whose constants are C. Division by a nonzero first function converts the Wronskian to the corresponding nonzero power times the Wronskian of 1 and the ratios. Expansion reduces the induction to their derivatives. Constant linear dependence of those derivatives means a linear combination of the ratios has derivative zero and is therefore constant. This proves the stated criterion without evaluating an initial condition at a chosen point.

For seven solutions, the differential equation expresses the row of sixth derivatives as a C(t)-linear combination of lower derivative rows. The Wronskian therefore vanishes, forcing C-linear dependence. The rational solution space, and in particular the degree-at-most-eighteen polynomial kernel corresponding to E, has dimension at most six. This is a symbolic differential-order argument, not an actual matrix-rank evaluation.

### Section 6: semisimple gap and actual quotient factorization

The equivariant kernel contains the embedded irreducible K=P. If it were larger, semisimplicity would give a nonzero additional constituent in E/K. The smallest possible constituent has dimension three, so the enlarged kernel would have dimension at least seven, contradicting the order-six bound. Hence the actual kernel is exactly K and H has rank fifteen.

Now `H = q* r` and injectivity of q* imply `ker r = K`. This supplies the unique constant equivariant factorization `r = h q`. Its rank is fifteen, so h is an isomorphism. Finally `H = q* h q` and surjectivity of q descend symmetry to h. The map h is consequently constructed from the actual q and r; no independent self-duality of V or unproved auxiliary full span is substituted. The identity `u = h v` follows directly from the common universal coefficient line.

### Section 7: auxiliary jets and finite embedded-kernel restriction

A constant isomorphism commutes with the actual intrinsic differential-evaluation maps and transports saturation. Therefore every auxiliary saturated jet span is the image of the corresponding original one whenever the latter is defined. Applying the already proved original separation through order nine gives precisely the asserted auxiliary conclusion, without asserting an original tenth jet or transferring a rank-seventeen theorem.

For each scalar lambda, `T_f - lambda Id` retains the same nonzero order-six symbol, so all its eigenspaces have dimension at most six. If its two-dimensional multiplicity operator on the P-isotypic component were scalar, an entire eight-dimensional eigenspace would result. It is therefore nonscalar. A nonscalar complex endomorphism of a two-dimensional space has at most two eigenlines, also when it is not diagonalizable. Any equivariant embedded P killed by `alpha T_f + beta Id` must correspond to one of those lines. This yields at most two fixed embedded P-subspaces, independent of scaling f12. It selects no eigenvalue or eigenline and does not identify them with the retained F18 splitting alternatives or assert that either occurs.

### Section 8 and all retained boundaries

The claimed contribution is accurately limited to resolving the auxiliary coefficient-span dependency, deriving the auxiliary higher jets through order nine, and proving the necessary finite embedded-kernel restriction inside the conditional residual case. The internal derivative/incidence problem, occurrence, both main rank-seven images, original local defects, separate e9 endpoint, retained F18 alternatives, and algebraicity remain open as stated. No statement elsewhere in the frozen proof overrides these limits.

## Checker inspection and isolated replay

I read `verify.py`, `characters.py`, and `REPRODUCE.md` completely before replay. The checks use explicit runtime conditions that remain active under `-O`. The character module performs 81 fixed exact-rational McKay identities; the main verifier reports 72 checks. The thirteen symbol checks concern only the formal monomial basis of universal degree twelve and the Vandermonde/radial identity. No actual coefficients of f12 or the source system are inserted, and no selected points, jets, tensors, matrices, instance ranks, normalizations, eigenvalues, or eigenvectors are evaluated.

I copied exactly the eight files specified by `REPRODUCE.md`, with relative paths preserved, to a newly empty isolated directory. No prior outputs, caches, author fetches, reviewer records, scratch audits, or other drafts were copied. With bytecode writes disabled and PYTHONPATH empty, both `python verify.py` and `python -O verify.py` returned exit status zero, **PASS with 72 checks**, and the exact frozen proof hash above. Their result objects were identical and stderr was empty. All eight isolated files and the eight originals retained their pre-run byte hashes; the isolated directory still contained exactly those eight files afterward.

`REVIEWER-REPLAY.json` records the selected-file hashes, commands, outputs, and unchanged-byte checks. The arithmetic replay supports, but does not replace, the entire mathematical review above. No GitHub write, broad scan, large computation, quotient connection, horizontal splitting, selected actual-instance evaluation, or rank-seventeen transfer occurred in this review.
