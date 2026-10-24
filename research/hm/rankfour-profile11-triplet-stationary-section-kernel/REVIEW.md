# Independent entire-proof review: ACCEPTED

## Exact object and review scope

Verdict: **ACCEPTED**, with no mathematical or replay blocker found, for the
entire frozen `PROOF.md`, exactly 24,626 UTF-8 bytes, SHA256
`7835e0a0e6769163dca0ad2ed0a62e3c79a491dc6ebc39e5f8c988d9a9ec6de2`.

This is a new independent full-proof mathematical review, not an author
self-review, the earlier stationary-subspace audit, or a checker-only review.
I read the complete proof, both complete direct original proofs, the complete
checker, and the frozen packet's provenance and selection records. I have not
edited any frozen core file. The acceptance concerns the universal theorem
and its stated conditional application, not occurrence or exclusion of K1.

The direct originals were independently and freshly authenticated through
four read-only GitHub operations: one complete exact-commit/path file fetch
and one exact Git-blob fetch for each original. No line range was supplied.
Complete UTF-8 bytes from both operations were compared with the complete
local original, and independently measured lengths, SHA256 hashes and Git
blob hashes all agree:

| Complete original | Commit | Bytes | SHA256 | Git blob SHA1 |
| --- | --- | ---: | --- | --- |
| PR1238 seven-space ramification | `d259230fbf7259e52db267c56203a29f221da5f0` | 20687 | `25388c411411f7304afc2dc7ad6695af5a931e852ba138c45cfb7a6f708d84e3` | `0da306ac1dc4c879ced57c28e2ec3a07f027da70` |
| PR1206 shared-D | `252b967ebbfbea6fc0c6451a835ab2daff92d73b` | 8801 | `f2e5b5d8bdb0f8a156aaf38695042f204b4d3cffd1a40a4a28870bed2ef13793` | `82596d9d02147711e0d5f7953912a94fffbae684` |

Exact source paths and call arguments, plus the complete-byte comparisons,
are recorded in `REVIEW-AUTHENTICATION.json`. Raw connector responses are
local evidence only and must remain outside the selected publication. The
mathematical review below is distinct from authentication.

## Complete-source sufficiency and retained assumptions

PR1238 explicitly supplies the original dual curve Y0, its genuine constant
projection to C7*, the constant seven-space of type A+P, full projected
coefficient span, saturation, and the full-orbit vanishing sequence
(0,2,3,4,5,6,8). I checked its entire derivation, including the rank-three
actual direct sum, the exclusion of a base divisor, and the additional
projection defect e. In particular its bound 84 >= 6(12+e), combined with
invariance and the minimum orbit size, proves e=0 rather than assuming
projection preserves saturation. Its subsequent extension-type and
Wronskian conclusions are compatible with the facts imported here.

PR1206 explicitly supplies the original degree-eighteen coefficient span of
type A+V_alt+D+P and dimension fifteen. Its proof uses the actual
Harder-Narasimhan kernel E0 in F and genuine constant-span decompositions to
exclude the two disjoint-span possibilities. In the second alternative, the
resulting actual quotient O(-16) of A(-6) gives the stated contradiction.
Nothing in the present packet confuses that original curve with the
auxiliary primal degree-eighteen curve.

These two entire originals state all actual facts used in Sections 8-9;
PR1237 need not become a third direct dependency merely to repeat the
constant splitting already supplied by PR1238. All complete transitive
actual-geometric hypotheses, including source and section gates, remain
assumptions. This review does not claim to re-prove the transitive sources
or to remove the full-positive, t=0, original delta=12, residual simultaneous
rank-seven k=2, and K1 conditions.

## Universal representation and orbit arguments

The physical representation is the faithful complex determinant-one
doublet, not a characteristic-five representation. For X=P(W*) with the
lines convention, H0(O(n))=Sym^n W has the stated direction. I checked the
five A5 character rows, their irreducible realization and orthogonality,
the even recurrence, and the needed decompositions through degree eighteen.
The recurrence h_(m+1)=(chi(A)-1)h_m-h_(m-1) follows from the formal weights
-m through m. Real characters justify only dual representation types.

Finite projective stabilizers are cyclic with faithful tangent character,
so their possible orders are 1,2,3,5. The twenty-four order-five elements
give six cyclic subgroups, with disjoint pairs of fixed loci. This proves
one reduced orbit of length twelve, not merely a minimum orbit bound. The
unique invariant equation line in H12 cuts it out. A nonzero invariant
subsystem of H18 can have only this fixed divisor, and divisibility by it
would place the system in f12 H6=V_alt+P. Thus both A18 and D18 are
basepoint-free before either is used in a stationarity argument.

## Canonical first-jet quotient and its target

The tautological character alpha on the entire orbit has order ten. The
cotangent character is alpha^2, whereas the tangent character is its
inverse. Consequently O(18) has value character alpha^(-18)=mu and the
pure-derivative line has character alpha^(2-18)=mu^2. These directions are
correct. The argument uses a conjugation-compatible family on the whole
orbit, not a chosen point, eigenline, generator or numerical root of unity.

The A restriction has weights mu^(-1),1,mu and no mu^2. Equivariance
therefore forces its first-jet image into the unique mu line of the
two-dimensional fiber. Basepoint-freeness makes its value map onto and
identifies that image with L along the reduced orbit. Thus L_A, J/L_A,
the isomorphism K -> J/L_A, the torsion sheaf T and tau are canonical.
This uses only principal parts and an image over a finite reduced scheme;
it does not produce a connection or a splitting of the global jet sequence.

The induced representation of mu^2 has exactly one V_alt, D and P, by the
displayed inertia restrictions. The independent restriction/cohomology
sequence agrees: d(f12) identifies O(6)|Z12 with K, and the final
cohomology term is H1(O(-6))=H4* as representation type. The differential
of the equation is intrinsic along its reduced zero divisor. Scaling its
nonzero representative does not affect the product subspace or any of the
canonical definitions.

The product-jet formula proves injectivity on all of f12 H6, because the
restriction kernel is H0(O(-6))=0. It is stronger than a sheaf-generation
claim. In particular the P row is surjective, its kernel P0 has type P,
and it is complementary to f12 H6[P] without a choice inside the repeated
P isotypic component.

## Stationarity and surjectivity

For a basepoint-free F, restricting principal-parts evaluation to the
evaluation kernel M_F gives the intrinsic differential criterion. Its
vanishing is equivalent to the first-jet image being a value-isomorphic
line. An invariant subsystem of type A+P contains the unique A18, is
automatically basepoint-free, and therefore has that line equal to L_A.
It is stationary on the entire orbit exactly when its P copy is P0. Both
directions of the asserted uniqueness are proved.

I checked the self-contained Wronskian argument rather than treating its
arithmetic checker as a proof. For m independent sections of O(n), the
principal-parts determinant has degree m(n-m+1). The adapted local orders
are distinct; the falling-factorial determinant has nonzero Vandermonde
leading coefficient in characteristic zero. This proves nonvanishing and
weight sum(a_i-i). First-order stationarity gives weight at least m-1.
This is a universal formal local lemma and does not evaluate any selected
actual jet or source parameter.

If tau(D18)=0, the basepoint-free D18 is stationary at all twelve points.
Its Wronskian has degree 70 and contains 4Z12. The residual effective
invariant divisor would have degree 22, impossible using orbit sizes
12,20,30,60. The independent twelve-dimensional subsystem argument also
works: its Wronskian degree 84 is less than the forced 132. That argument
uses the P0 already constructed, so it does not circularly assume
surjectivity. Hence tau is onto, with exact kernel A18 direct-sum P0.

## Actual section and coefficient directions

The original inclusion O(-18) -> C* tensor O determines sigma18:C->H18.
Its annihilator quotient is canonically V18*, so the actual injection is
j18:V18*->H18. Its transpose has codomain V18**=V18, not V18*. This
correctly defines b18 in the fixed domain H18* without choosing a
self-duality of V18.

For the genuine constant inclusion k7:C7->C, the restriction is
r7=k7*:C*->C7*. Full projected coefficient span implies that
r7|V18 is onto. Transposing gives exactly
j7=sigma18 k7=j18 (r7|V18)*, hence the actual containment
Lambda7 subset Lambda15. It is not inferred merely from representation
types or from a moving quotient. The original vanishing sequence supplies
first-order stationarity, so uniqueness identifies Lambda7 with ker tau.

The original V18* has type A+V_alt+D+P. The multiplicity-one A,V_alt,D
components of H18 are therefore fully present in Lambda15. Its sole P
copy contains the already embedded P0, and equality follows by dimension.
Thus Lambda15=ker(pi_P tau). The target isotypic projection pi_P is
canonical; it does not choose a complement in the repeated source P block.
Finite-dimensional duality then gives the stated exact sequence

    0 -> T_P* --(pi_P tau)*--> H18* --b18--> V18 -> 0.

This proves the actual coefficient kernel as a subspace of its fixed
domain, not only its abstract representation type. No actual coefficient
tensor or normalization is determined.

## Independent checker and selected-only replay

I read the entire 10,489-byte checker, SHA256
`7ace5d9ecc767662380aca60d5c7773f45766d038adad2cc0735218930c93963`.
Its tests are explicit runtime requirements, not removable assertions.
Its calculations are bounded fixed-character recurrences, exact arithmetic
in Z[phi], symbolic inertia, and the displayed orbit and degree arithmetic.
It contains no source-instance evaluation or broad search.

Normal and optimized Python were independently run in the original
directory and in two newly created clean directories, each containing
exactly the eight selected files: the seven frozen core files and
FROZEN.json. The selected file lists and hashes were checked both before
and after each clean replay. All six runs exited zero with empty stderr
and identical stdout, reporting 177 checks: 22 authentication, 135 fixed
character, 8 inertia/cohomology, and 12 orbit/degree/kernel checks.
`REVIEW-REPLAY.json` records the exact commands, outputs, selections and
hashes. Neither raw connector responses nor author/reviewer reports were
present in either eight-file replay directory. The original frozen files
also remained byte-for-byte unchanged.

## Final boundary

Acceptance is for the canonical universal stationary seven-space and its
necessary conditional identification of the original degree-eighteen
coefficient kernel. It is not an occurrence theorem, K1 exclusion,
whole-profile conclusion, identification of an actual space with its dual,
determination of the whole coefficient map, higher-order branch-matching
result, or algebraicity claim. The proof retains saturation distinctions
and introduces no quotient connection, horizontal splitting, or selected
actual calculation. No changes to the frozen proof are requested.
