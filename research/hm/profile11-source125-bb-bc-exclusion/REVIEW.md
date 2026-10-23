# Independent exact-version review of the source125 bb and bc exclusions

## Verdict and byte binding

**PASS.** I found no mathematical gap in the complete two-source argument at the exact bytes listed below. This review checks the actual bundle and connection argument, not merely the representation identities. The bounded verifier also ran successfully and independently.

Reviewed SHA256 hashes:

- `PROOF.md`: `9d0ac1a9bfbd0bb1f30b42721d456f0ee7776b215c07b52648e62f416f90758c`
- `verify.py`: `9abaa148f06f896813baa31619c49c73f784c42c2b9f44a30c6158220772af08`
- `REPRODUCE.md`: `d5d9a46d0e86266a91da76abd1a7de9aa134597cf71bfc4a8833fbece00ac8b3`

The scope is exactly source index125, stable label `G3.11.ea6bced3bddf`, with original tuples

- bb: `(0,2,0,0,0,0,0,1)`;
- bc: `(0,1,1,0,0,0,0,1)`.

This is not a review of the superseded conditional bc drafts. It does not certify other original source cuts, a complete label-coverage table, or a current frontier count.

I read the stated cf dependency, including its complete-Sym6 obstruction and connection-preserved coherent-image lemma, and the bf dependency's strict-top, first-increment, and quadratic-gap arguments. The supplied cf proof has SHA256 `4ca484460729d1873eab5e6ff1beb534927abc865b478e9bfa971ac928ded05c`, matching its existing exact-version review; its cited publication is PR882 at `ef8ed8d457494608472a2c07de776e9162b2c20f`. The supplied bf proof has SHA256 `57b6b69c9dc1229b937ca3767baaeb5ee5a080b97bca7b81a3dd01529e9d2c4b` and contains the universal P-kernel and quadratic-gap argument used here. Neither another source's exclusion nor a conditional bc branch is substituted for the present whole-source reasoning.

## 1. Forced constant A and saturated high capture

The positive pair in Q is saturated: it is a direct summand of the saturated derivative image after twisting by2. Its inverse image Epos is therefore a bundle in the actual ambient constant bundle. The exact sequence has the asserted rank19, degree−30, and Euler character `A−P−2D`.

A positive A multiplicity in this Euler character forces A in H0(Epos), irrespective of H1(Epos). Global sections of a subbundle of `H O` are genuine constant vectors in H. The chosen A is therefore an actual constant subspace, not an abstract degree-zero factor declared horizontal.

Its low component is zero because A is absent from Sym6. Its high component cannot vanish, since that would put A in H0(E)=0. A base divisor of this nonzero degree18 system would be invariant. The only positive possible degree below20 is12, and removing it would require an A in Sym6. Thus the high map is everywhere onto the already saturated O18. This is sufficient for both the exact intersection and the saturation of the projected source.

## 2. Exhaustion of the rank-two kernel

The kernel K has rank2, degree−18, no sections, and H1 character `V+2P+D`. Its complete equivariant splitting alternatives have been considered.

Because K embeds in the even constant A, a rank-two irreducible coefficient must be W or Wp at odd twist. Degree forces twist−9. The W candidate has the required H1; the Wp candidate has `1+A+V+P+D` and is impossible.

Otherwise the two coefficients are scalar. Binary icosahedral G has no nontrivial one-dimensional characters, and even central action forces even negative twists. Absence of sections and degree−18 leave exactly the four unordered pairs in the proof. Their H1 characters are respectively

- `(2,16)`: `1+A+V+P+D`;
- `(4,14)`: `1+2A+P+D`;
- `(6,12)`: `A+V+2D`;
- `(8,10)`: `V+2P+D`.

The last is not ruled out by its character, but is correctly ruled out geometrically: its O(−8) summand would need a nonzero injection into `A O`, whereas A is absent from Sym8. Consequently K is exactly `W(−9)`.

Projection by the actual A is now legitimate with no saturation correction. Its image in Q is the entire saturated O18, so the projected source has exactly the remaining saturated derivative image `O(−10)+O4`. The scalar component of K is zero by ordinary degree. Hence `E'=R+O(−10)` is an actual quotient splitting, and R is a genuine subbundle of a constant bundle, of rank14 and degree−26.

## 3. The genuine constants of R are exactly P

Since R is embedded in a constant bundle, it has no positive ordinary splitting degree. Its global sections are precisely its actual degree-zero summand C0. Removing that actual constant subspace leaves a saturated, section-free source `E''=Z+O(−10)` without changing the derivative image.

The two cohomology bounds are exact-sequence bounds, not just Euler-character comparisons:

- `C0` embeds in `H1(W(−9))=V+2P+D`;
- `H0(R(1))` embeds in `Wp+2T`, and its Wp is mandatory because the following H1 of F is exactly `2T`.

The subtraction of `C0 tensor W` from H0(R(1)) is justified by the exact twisted constant-quotient sequence and `H1(C0 O(1))=0`.

If Wp remained in H0(Z(1)), section-freeness of Z identifies a genuine top summand `Wp(−1)`. Its external derivative is zero, by the stated representation and degree vanishings. Its internal derivative has no lower-source channel, since all other source degrees are at most−1 and the target is twisted by−2. Equivalently, its nonzero linear coefficient span is the genuine constant P, using `Wp tensor W=P`, and would lie in E''. This contradicts H0(E'')=0. No claim that the original source splitting is horizontal is needed.

Thus C0 must account for the unique mandatory Wp. The tensor identities give exactly `C0=P` or `C0=V+P`: a D would introduce a forbidden S, two P's would introduce two Wp's, and the twist-zero bound permits at most one V.

At twist2, D has multiplicity exactly one in H0(R(2)) for either source. For bc this is independent of whether the V-to-V cohomology map vanishes. The alternative `C0=V+P` would inject `(V+P) tensor Sym2=V+2P+2D` into that space, an impossibility. Hence C0 is exactly P and Z has rank10, degree−26.

## 4. The linear-top contradiction is an actual projection

After subtracting the actual P constants, H0(Z(1)) is either zero or one T. If T occurs, it is the whole linear top. Strict-top makes its degree5 map to O4 nonzero and complete, with kernel `D(−2)`.

The kernel has no internal map to the remaining source, whose target degrees are at most−4, or to the retained scalar target O(−12). The actual internal/external-image lemma therefore gives an exact saturated first increment O6. The first span has rank7 and degree0, so it is genuinely constant; its coefficient is V+P. Its image in the quotient is precisely the saturated O6, and its intersection with the source is exactly `T(−1)`.

The subsequent projection thus leaves an actual section-free source of rank5 and degree−30, retaining the scalar O(−10), with only derivative target O(−10). If its highest ordinary degree exceeded−10, the entire highest block would have zero external map; strict-top excludes this. All five degrees would therefore be at most−10, contradicting degree−30. This closes the linear-top alternative and proves that every degree of Z is at most−2.

In particular, this argument does not silently replace `R+O(−10)` by a hypothetical standalone R with only the low derivative line. The scalar remains throughout. The derivative argument is applied to the actual highest block and its actual external kernel.

## 5. Actual quotient splittings for bb and both bc cases

For bb, the twist2 exact sequence gives `H0(R(2))=V+2P+D` and zero H1. Removing the actual P constants leaves quadratic coefficient P. The remaining six degrees are each at most−3 and sum to−18, so they are all−3. The twist3 Euler character identifies their coefficient as T. Thus the quotient is genuinely `Z=P(−2)+T(−3)`.

For bc, the two possibilities for the actual K-to-quartic-tail component are exhaustive.

If `u:W(−9)->V(−4)` is nonzero, its twist2 cohomology map to `H1(V(−2))=V` is nonzero, not merely allowed. By Serre duality its dual is exactly the coefficient map `V->W tensor Sym5` associated with u. Irreducibility makes this map injective and the H1 map onto. This gives the same twist2 cohomology as bb, so the same rank, degree and twist3 deductions force `P(−2)+T(−3)`.

If u is zero, K lies in the actual direct summand F0, and quotienting preserves the actual quartic direct summand. The actual constants P have zero projection into that negative summand. Thus `Z=Z0+V(−4)` with rank Z0=7, degree Z0=−14. Since all its degrees are at most−2, Z0 is pure quadratic. The twist2 character after removal of the actual P constants identifies its coefficient as V+P. The actual quotient is therefore `(V+P)(−2)+V(−4)`.

These deductions use local freeness and actual direct-summand quotients, in addition to characters. No component-zero branch or possible positive/linear degree is omitted.

## 6. The two terminal obstructions apply with the scalar retained

For `P(−2)+T(−3)+O(−10)`, strict-top and the invariant-divisor bound give the onto degree6 P system with universal kernel `V(−4)`. The kernel has no internal map into `T(−5)+O(−12)`. Hence its actual saturated rank-one first increment is O6. The quadratic rank4 alternatives are degree8 or at most3, so degree6 is impossible.

For `(V+P)(−2)+V(−4)+O(−10)`, the restated cf obstruction has the same hypotheses as the actual residual source. The complete degree6 top system has kernel `T(−3)` and zero internal image, giving first span `(Wp+T)(−1)`. Quadratic generation and nonconstancy of that first span give the genuine constant second span C of rank9 and coefficient P+D.

The quartic tail's external derivative is zero. Modulo itself, its only internal derivative channel is the top V; this lies in C. Its coherent image after projection by C is therefore preserved by the regular constant connection. The published coherent-image lemma applies to that image itself, not just its saturation: characteristic zero rules out positive elementary-divisor exponents in a connection-preserved lattice.

The resulting image is a constant bundle. An even image of rank1 or2 would be trivial and is excluded by `Hom_G(V(−4),O)=0`. A rank3 image would be an everywhere surjective equal-rank map from degree−12 to degree0, hence an impossible bundle isomorphism. Therefore the tail lies in C. The disjoint top and tail then have rank10 inside rank9 C, a contradiction. This is an actual-connection proof; no arbitrary complementary source summand is assumed horizontal.

## 7. Independent execution and reproduction audit

I inspected the exact verifier and independently ran `python3 verify.py` against the frozen package. It exited successfully with:

    PASS: 42 fixed Hom checks, exact kernel/cohomology identities, and pinned source125 bb/bc identities.
    Two source exclusions only; no whole-label coverage or current frontier count is certified by this verifier.
    No selected actual source, coefficient, parameter, point, derivative, matrix, instance rank, scan, or large computation.

The final reviewed verifier includes the author-coordinated startup guard against disabled assertions. Removing just that guard reproduces the originally supplied verifier SHA256 `a22d11ca7573720ed3290cf4ded3c9423907a35cf677e9022c8b504eb8763be0`; there are no other verifier changes. I reran the guarded version with ordinary Python and obtained the output above. I also ran `python3 -O verify.py`: it exited with status1 and the explicit message “Run without -O: this verifier requires its assertion checks to be enabled.” It did not print PASS.

Before parsing either catalog, the verifier checks its exact Git blob hash against the stated immutable input at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`:

- original source catalog: `fe0afa410d89340d3082dc814277f89fbb582c19`;
- stable-label catalog: `8b5971092f9ef762584912609fd5e9301c4e271d`.

The two tuples, source index, label, endpoints and original defect are checked against those inputs. Representation computations use exact rational arithmetic in Q(sqrt(5)); no numerical approximation or actual source map is constructed. The reproduction instructions agree with the verifier's inputs and observed output.

I also directly checked the following small, fixed universal identities, without selecting an instance: `Wp tensor W=P`, `T tensor W=D+V+P`, the two top-V scalar Hom multiplicities in the trapped-tail argument, the absence of V from Sym4, `(V+P) tensor Sym2=V+2P+2D`, and the four scalar-pair H1 characters listed above. All passed. These supplemental identities support the written audit but do not replace any geometric inference.

The verifier's opening docstring still says “one original source identity only”; this is a harmless wording residue. Its executable checks and printed scope correctly cover exactly bb and bc. No frozen file was edited for this cosmetic point.

## Review boundary

The proof establishes exactly the two displayed original source exclusions. I used only universal bundle, connection, cohomology and representation reasoning, together with bounded fixed character/Hom checks. No selected actual HM/source coefficients, parameters, points, derivative evaluations, matrices, instance rank tests, experiments, source scans or large computation were used. No publication action was taken.

The approval is bound to the three exact SHA256 values above. Changes to those bytes require a new exact-version review or an explicitly scoped review addendum. This is written mathematical review, not formal proof certification.
