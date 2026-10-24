# Independent entire-proof review

## Verdict and exact binding

**ACCEPT within the stated conditional scope.** No mathematical gap or required correction was found in the entire frozen proof. This verdict is bound to the 16,304-byte `PROOF.md` with SHA256

`b233db763f8c7aa78174ae85629f28f00a373f6b78b3674602f96189f6cf3d2e`.

I read the complete proof, complete checker before execution, complete provenance and README, and all four complete direct originals. I independently fetched each original by its recorded immutable repository path/ref and separately by its recorded Git blob, using eight fresh read-only GitHub connector calls. Decoded path bytes, blob bytes, and retained local bytes agree exactly for every source, with exact lengths, SHA256 values, and computed Git blob SHA1 values. Author fetch logs and author replay were not used as authentication or replay evidence.

This is an entire-proof actual-map review, not an inference from the checker's PASS. The complete transitive actual-geometric hypotheses explicitly retained by the proof remain assumptions. This review does not independently authenticate every transitive ancestor or establish the existence of the conditional geometry.

## Complete source audit

1. **PR1236, first-kernel forward closure.** I read all ten sections of the 18,052-byte original at `092fc5f31dfaa5553ee5ea687f175ecba1878a2a`. Its actual equalities `R13=R^+`, `R15=R13^+`, and `R17=ann_S(x0(X0))`, together with `R15 subset E19=ann_C(X0+Y0)` and containment of the chain in the genuine constant `S`, supply precisely the propagation and terminal-annihilator inputs used here. Its rank-two derivative and reduced degree-twelve saturation defect are not relabeled as the retained original local delta. The current proof does not depend on an unproved transfer of first-jet saturation to a projection.

2. **PR1235, first-kernel span.** I read all six sections of the 11,977-byte original at `7152e94cedbab18036b5e032d4e97934c4c061b7`. Section 2 proves the actual inclusion `Zhat5 subset R` by factoring the quotient map through `Zhat5/Zhat4=O` and using its negative target. This is the previously identified actual canonical auxiliary fifth-jet complement, not any abstract `T6(-5)` summand. Sections 3 and 5 give the genuine constant ambient character, `dim S=18`, and `C/S=V_alt`. This direct source is needed for both the embedded inclusion and the representation data.

3. **PR1226, second-kernel exclusion.** I read all seven sections of the 13,703-byte original at `c565bd8b5b65829e99bdd96a7c5f076b01050465`, including the K2-specific argument. Its Sections 1–4 precede the additional K2 assumption, which is introduced only in Section 5. Those earlier sections construct the actual lifted scalar line in `K^-`, prove its coefficient dimension eleven, and show that constant restriction `p` is an isomorphism between its genuine coefficient spaces. They identify the actual lifted jets by differentiating embedded subbundles and killing the possible `H(-2)` row, rather than differentiating the inverse of `p|K^-`. Thus the complete lifted auxiliary flag used in this K1 theorem does not import K2 or its later contradiction.

4. **PR1206, shared D.** I read all six sections of the 8,801-byte original at `252b967ebbfbea6fc0c6451a835ab2daff92d73b`. Its `U`, `C10`, and `V` are the present original dual `X0`, `V10`, and `V_alt`. The full original excludes both disjoint-span alternatives and proves `C10=A+V+D`, of dimension eleven, with its degree-ten coefficient map an isomorphism. Therefore original degree-ten completeness is prior work on a broader branch. The current proof correctly imports it and does not claim it as new. The original degree-eighteen curve remains distinct from both degree-ten curves.

The current proof's named inputs are explicitly present in these complete originals, including the canonical lifted-flag identification retained by PR1235. PR1205 is not needed as a fifth direct source for an assertion otherwise absent from this packet. The original constructions and their transitive assumptions are still retained; this is not an attempt to replace them with abstract type information.

## Actual-map and invariant-theoretic audit

### Auxiliary propagation and constant span

For actual embedded subbundles `A subset B` of a constant bundle, local derivatives of sections of `A` lie in the coherent forward span of `B`; saturation preserves the inclusion when the receiving forward span is saturated. Applying this twice to `Zhat5 subset R` gives `Zhat6 subset R13` and `Zhat7 subset R15`. The latter is consequently annihilated by the original dual `X0`. This argument neither differentiates an inverse bundle map nor installs a connection on a quotient.

The coefficient span of `Zhat5` is exactly `Z`: it contains the original lifted scalar line, and all its derivatives lie in the genuine constant coefficient space of that line. Since `R subset S O`, this proves the actual constant inclusion `Z subset S`.

### Diagonal ideal and invariant factorization

The scalar pairing of the two equivariant degree-ten inclusions is a section of `O(10,10)`. Triviality of the scalar character group makes it invariant after either scalar-line presentation is chosen; changing a presentation only changes an overall nonzero scalar. The complete seventh-jet annihilation says that the restriction in the second variable vanishes through derivative order seven at every diagonal point. In characteristic zero this is precisely membership in the eighth power of the diagonal ideal.

This initially proves order **at least eight**, not exact multiplicity eight. The diagonal is an effective Cartier divisor with invariant determinant equation `Delta`, so division by `Delta^8` is global, regular, and invariant, with remaining bidegree `(2,2)`. The physical identity `Sym2 W tensor Sym2 W=1+A+D` has exactly one trivial summand. Its invariant line is generated by `Delta^2`. Therefore `F=c Delta^10`; after nonvanishing is proved below, the diagonal multiplicity is exactly ten. No actual point or jet is evaluated in this argument.

### Nonzero pairing and coefficient-map directions

If `c=0`, the entire biform vanishes and hence the pairing of all coefficient vectors of `V10` with all coefficient vectors of `Z` is zero. This would place an eleven-space in the ten-dimensional annihilator of another eleven-space in the genuine paired 21-dimensional ambient. The dimensional contradiction is valid without an actual coefficient matrix or instance-rank calculation.

The proof writes the coefficient domains before making self-dual representation identifications: `a_orig:H10* -> V10 subset C*`, its actual constant projection `a:H10* -> S*`, restriction `rho:S* -> Z*`, and `z:H10* -> Z`. Both `a_orig` and `z` are isomorphisms onto their already complete spans. The determinant biform of degree ten is a nondegenerate pairing of the two coefficient domains, as its universal complementary-monomial coefficients are nonzero in characteristic zero. Consequently `rho a` is an isomorphism, `a` is injective, and restriction `V10 -> Z*` is an isomorphism. There is no reversed dual map or identification of the distinct original and auxiliary curves.

### Canonical actual constant splitting

Restriction `q:C -> V10*` is onto, and `q|Z` is an isomorphism by the perfect coefficient pairing. Thus `(q|Z)^(-1) q` is a map of actual constant equivariant vector spaces and a retraction onto `Z`. Its kernel is exactly `ann_C(V10)`. This proves the canonical actual decomposition, relative to the given actual pair, rather than merely an isomorphism of representations or a Birkhoff splitting.

Because `Z subset S`, that retraction preserves `S`, giving `S=Z direct-sum (S intersect ann_C(V10))`. The intersection has dimension seven. Subtracting the fixed semisimple characters gives `Kappa=A+V_alt+P` and `C7=A+P`. Those final representation labels are only isomorphism types; the actual direct sums themselves were already constructed without choosing irreducible copies, coefficients, or a scalar normalization.

### Terminal bundle and immediate derivative kernel

The established `Delta^10` pairing annihilates the ninth auxiliary jets at every point. Perfectness makes the restriction of every nonzero `X0` fiber to `Z` nonzero, so its kernel in `Z O` has rank ten. The rank-ten `Zhat9` is saturated in `Z O`; its inclusion into that kernel is therefore equality. Combined with the genuine constant split of `S` and the imported exact terminal annihilator, this proves the actual equality `R17=Zhat9 direct-sum C7 O`.

The derivative of `Zhat9` kills `Zhat8`. Its induced last-graded map is `O(8) -> O(8)` and is nonzero because the actual forward span is `Zhat10=Z O`. A nonzero endomorphism of this line bundle is an everywhere isomorphism. Hence its actual derivative kernel is exactly `Zhat8`. The ambient decomposition is constant, so the other summand has zero normal derivative and cannot cancel a derivative in the `Z` summand. Thus `R17^-=Zhat8 direct-sum C7 O` as actual embedded subbundles. The ranks and degrees are respectively `(17,-10)` and `(16,-18)`. No arbitrary bundle splitting is declared horizontal, and no longer backward chain is asserted.

## Independent selected-only replay

Before executing it, I inspected every line of `verify_packet.py`. It only imports standard-library modules, reads the whole frozen proof and four source files plus `INPUTS.json`, and performs fixed universal character and dimension/order calculations. Its `require` function raises `RuntimeError`; there is no assertion whose removal would weaken optimized execution. It has no external calls, file writes, selected actual-instance evaluation, or large search.

I independently copied exactly the nine files listed in `FROZEN.json` into a new isolated directory. The freeze manifest itself, author reports, source-fetch logs, reviewer reports, publication manifest, and caches were not included. Normal Python and `python -O` both returned code zero, no stderr, and identical stdout:

`PASS: 85 bounded checks (21 whole-file authentication; 35 universal character; 29 fixed dimension/order checks).`

Every selected file had its recorded hash before copying. All isolated hashes and the isolated file list were unchanged after each run; every original frozen selected hash and the freeze manifest bytes were also unchanged afterward. Full fresh-source authentication is recorded in `REVIEWER-AUTHENTICATION.json`; both exact replay outputs and before/after hashes are recorded in `REVIEWER-REPLAY.json`. Each report is bound to the exact proof SHA256 above.

## Scope and research contribution

The accepted new step is the nonzero universal pairing between the prior complete original dual curve and the distinct complete auxiliary primal curve, completeness after the actual projection to `S*`, the canonical constant retraction and seven-space complement, and the two terminal actual-bundle identifications. The retained assumptions remain full-positive triplet, original `t=0`, local `delta=12`, residual simultaneous rank-seven `k=2`, and remaining original `K1` with complete transitive source hypotheses.

This does not exclude or realize K1, establish the conditional geometry, prove a whole-profile conclusion, produce new original degree-eighteen higher jets, or establish algebraicity. No selected actual coefficients, parameters, points, jets, tensors, matrices, instance ranks, or scalar normalizations were evaluated. No external or GitHub write, merge, upstream submission, or local Codex action was performed. Frozen files were not modified.
