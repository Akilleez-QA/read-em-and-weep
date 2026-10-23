# Independent review: finite necessary remaining Gauss-rank partition

## Verdict

PASS for the theorem as stated: conditional on the separately established
generic bound `r >= 4` and the pinned actual-geometric inputs, every actual
configuration belongs to one of the 28 displayed ordered `(r,k,l)` bins.
Exactly 27 of these labels have `4 <= r <= 12`; the remaining label is
`(13,1,1)`, the successful positive-square-surjectivity stratum if attained.
The four-source refinement has 103 labels, of which 99 have `r < 13`.

This is exhaustive containment in a finite necessary overlist, not a claim
that any listed bin is realizable, not a classification of all geometry
within each bin, and not a count of all original-proof branches. The proof
does not establish `r >= 4`, actual attainment of rank 13, full-adjoint
invertibility, or repair of the original theorem. No correction is required
to the reviewed text for this bounded claim.

## Frozen artifact and authenticated originals

The complete submitted proof and verifier were read without modification.
The reviewed core SHA256 values are:

- `PROOF.md`: `4e3444e45d39cab9f45d31b8c204fa8749b076e33a5ccc55a6fe2e06d20038ed`.
- `verify.py`: `6f33bc2429e4d5d4f73b7b27c52f2e0cc0e30cb9a6ad9da5963e3e0bda3df231`.
- `RESULT.json`: `efcefc4fd0f862d93fc04b5737870592c35da07b8d02779f22c490dfec52113a`.
- `INPUTS.json`: `77806c7cb34d173c162dd1e96c9e738b4fae9e6e94459dfaec79dc4499bd0955`.

All four retained originals were independently fetched using the connected
GitHub reader at the exact immutable commit and path in `INPUTS.json`.
The fetched full contents equal the retained local bytes. Byte lengths,
SHA256 digests, computed Git blob identities, returned Git blob identities,
and exact pinned display URLs agree. `SOURCE-AUTH.json` records these
checks against the complete public originals.

The full originals reviewed were:

1. `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, commit
   `db51525015bb7c5e825833d550d08dedf6f6ea96`, especially Sections 1 and 4.
2. `RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md`, the same commit, especially
   its general changing-rank construction and degree/parity arguments.
3. `POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md`, the same commit, including
   its actual local Koszul comparison and exact kernel/cokernel sequence.
4. `research/hm/primary-terminal-slope-obstruction/PROOF.md`, commit
   `504b7eb800407dfc7e6340c98c72cdd553939f54`, including the primary
   terminal-pencil argument and four-source reduction.

Authentication is not itself proof of the source theorems. This review
checks the new deduction against these complete sources and their written
premises; it is not a new recursive audit of every transitive HM input.

## Whole-proof mathematical review

### A. Object and domain compatibility

The object is the actual rank-17 subbundle `E` of the constant
30-dimensional plane-section space `H`, not the coefficient space `M3`
of dimension 54. Its annihilator is `Q*` in `H* tensor O`. The argument
retains the original physical parameter line and one fixed determinant
rotation, so the reversed annihilator plateau is the genuine dual
construction, not an independently rotated or merely isomorphic pencil.

The four-source theorem is not restricted to generic rank three. Its
terminal-slope inclusion is proved from the actual primary graded-module
injection, socle exclusion, coefficient-pencil functoriality, and slope
quotient, before any rank-three-specific coverage claim. It can therefore
be applied here to the same `E` at generic rank at least four. Its caveat
about global rank-three coverage is not used as a missing hypothesis for
this limited four-type/quadratic-section deduction.

The physical names are consistent: `D=Sym^4 W`, `P` is the even four-space,
and `V` is the other three-space, not `A=Sym^2 W`.

### B. Canonical plateau and endpoint cases

For saturated Gauss transforms, both forward and backward rank increments
equal the generic derivative rank, and those increments are nonincreasing
away from `E`. Continuing while they equal `r` therefore defines a unique
maximal consecutive plateau. Interior kernels and forward transforms
equal their adjacent stages: the evident inclusions have equal generic
ranks and are saturated in the same bundle.

The lower and upper dimensions are exactly
`p=17-rk` and `q=13-rl`. Nonnegative dimensions give the stated rank
budgets. In the reviewed range, no `r` divides 17, so `p>0` in every bin.
A lower endpoint of derivative rank zero would be a positive-rank
constant subbundle of `E`, excluded by `H0(E)=0`. Its derivative rank
thus lies in `[1,min(r-1,p)]`.

For `q>0`, an upper endpoint of derivative rank zero would be a proper
constant bundle containing the full-span `E`, excluded by `H0(Q*)=0`.
Its derivative rank lies in `[1,min(r-1,q)]`. These are bounds, not
claims that every integer in either interval is realized.

The exceptional case `q=0` must not be removed by that argument.
Since `rl=13` and `r>=4`, it occurs only for `r=13,l=1`; the lower
rank budget then gives `k=1`. The saturated upper stage is exactly
`H tensor O`, with derivative rank zero. The proof and output correctly
retain this endpoint. Absence of invariant vectors in `H` does not
exclude a nonconstant rank-one endpoint.

### C. Persistence genuinely holds at arbitrary rank

The complete original persistence proof explicitly applies to arbitrary
generic `r`. Its use here is not an extrapolation from a rank-three title.
A nonzero section of `E(d)` supplies a saturated line `O(-e)` with
`1<=e<=d`. The inclusion remains saturated in the constant ambient by
the two locally free quotients. The universal polynomial derivative
identity shows that at most `e` forward transforms of this line reach
its constant coefficient span.

If `l>d`, that nonzero constant span lies in an interior plateau stage.
Interior constant subbundles propagate backwards through derivative
kernels into `E`, a contradiction. Thus `l<=d`. Applying the same
argument to the reversed annihilator plateau proves `k<=d` when
`H0(Q*(d))` is nonzero. The argument neither requires a horizontal
splitting nor refines the rank-r blocks into linewise osculating flags.

The actual Euler characters have genuine positive constituents:
`chi(E(3))=W'+2T6` and `chi(Q*(3))=T6-2W-S4`. Since `H1` has
nonnegative multiplicities, each asserted cubic section space is nonzero.
Consequently `k,l<=3`. Combining these inequalities with the rank budgets
gives exactly the claimed finite ranges.

### D. Source visibility and count

Twisting the four retained source splittings by two gives
`H0(E(2))=D,P,V,0`, respectively. Their dimensions are `5,4,3,0`.
Thus only D/P/V receive the improvement `l<=2`. Z lacks this argument;
it is not forced to attain `l=3`. Since `r*l<=13`, any `l=3` bin
in the reviewed range also has `r=4`. No dual quadratic section theorem
is present, so swapping the directions or asserting `k<=2` would be
unsupported. The submitted proof does neither.

The rank-by-rank coarse products are
`9,6,4,2,2,1,1,1,1,1`, summing to 28. Removing the one rank-13 label
leaves 27. Each of D/P/V loses precisely the three rank-4 labels with
`l=3`, so each has 25 labels; Z has 28. Hence the source total is
`3*25+28=103`, and removing four rank-13 labels leaves 99. These counts
are counts of ordered necessary labels only.

### E. Actual square gate and meaning of success

The gate's local calculation identifies the actual derivative with
`ker B -> coker A`, not just with an equally sized abstract map.
Its exact sequence then gives kernel dimension `17-r`, cokernel
dimension `13-r`, and square-map rank `24+r` on the generic-rank open
set. The same rank follows from either the 41-dimensional domain or
37-dimensional codomain. Therefore `r=13` is exactly generic
surjectivity for this positive-square map, conditionally if attained.

The written distinction from full-adjoint invertibility, Bockstein order,
other smoothing pencils, and original repair is correct and necessary.
The reviewed theorem makes none of those stronger conclusions.

### F. Limited determinant consistency

Regular adjacent derivative maps of equal-rank blocks give
`c_(i+1)-c_i=2r+delta_i`, with effective nonnegative `delta_i`.
Center-even determinants and the absence of nontrivial characters force
even degrees. The endpoint slope bounds are `a<=-2p`, improved to
`a<=-ceil_even(3p)` for Z; the upper bound is
`b<=-ceil_even(q)` for `q>0`, and exactly `b=0` for `q=0`.

Eliminating the first block degree gives the displayed identity with
coefficient `-rkl(k+l)` and the two weighted defect sums. Both weights
and signs have been checked independently. Integer witnesses satisfy
these limited constraints in all bins. At the full endpoint, the
zero-defect witness is `a=-82`, block degrees `28,54`, and `b=0`.

Such integers do not construct equivariant vector bundles or actual
saturated inclusions. The proof explicitly limits their role to testing
these elementary determinant/parity inequalities; that scope is sound.

## Independent controls and reproduction

The author's verifier was run from the frozen tree under ordinary
Python, optimized Python, and an unrelated working directory. All three
outputs equal the submitted `RESULT.json` byte for byte.

The separate `independent_check.py` imports no author code. It checks:

- Exact-set equality, with duplicate detection, for all 28 coarse and
  103 refined necessary labels.
- Every endpoint dimension and derivative-rank interval, including
  full-H rank zero only at `(13,1,1)`.
- All square-map dimensions and the conditional success label.
- Ordinary source rank, degree, low-twist cohomology, and quadratic
  visibility; the four source compositions are derived as four unit
  solutions after subtracting the required `b,c>=1`.
- A fresh degree-witness construction by solving the even-integer
  interval and choosing its upper endpoint, rather than copying the
  author's lower-endpoint construction.
- The full general-defect identity coefficientwise in the formal
  variables `a,c,r,delta_j` for 25 small `(k,l)` pairs.
- Eleven negative/scope controls covering cubic persistence, D versus
  Z, direction reversal, missing success endpoint, invalid ranks, and
  duplicate labels.

The independent outputs under ordinary and optimized Python agree
byte for byte and report PASS. No actual HM coefficient, parameter,
matrix, jet, rank, or local-model instance was evaluated. No historical
28/37/159-record classification was rerun.

Run:

    python3 independent_check.py
    python3 -O independent_check.py
    python3 ../verify.py

## Remaining obligation

Use this partition as a conditional roadmap only. A separately reviewed
and correctly pinned lower-bound theorem is still required to assert
that it covers all remaining actual generic ranks. Even after that
bridge, excluding the 27 bad labels or otherwise proving actual rank
13 remains new mathematics, not a consequence of these counts.

## Publication layout

Run the commands above from this `independent/` directory. The control
runner locates the theorem packet in its parent directory. Only these
package-relative locations and authentication-record descriptions were
adapted for publication; the mathematical review and its verdict are unchanged.
The conditional lower-bound theorem is now pinned in `../PUBLICATION.md`.
