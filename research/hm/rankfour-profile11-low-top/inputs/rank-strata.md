# A finite necessary stratification above the rank-three Gauss frontier

## 1. The statement, and what is being counted

Retain the actual geometric hypotheses and physical parameter conventions
in the four pinned originals in `INPUTS.json`. Assume separately that the
generic rank `r` of the actual second fundamental form is at least four.
That lower bound is an input to this note, not proved by this certificate.
At the coordination checkpoint retained in `COORDINATION.json`, the
nine-profile bridge to that bound was still under review.

Then `4 <= r <= 13`. For the maximal consecutive rank-`r` plateau with
`k` blocks below `E` and `l` above it, necessarily

    1 <= k <= min(3, floor(17/r)),
    1 <= l <= min(3, floor(13/r)).                         (1)

For each of the actual-source alternatives `D`, `P`, and `V`, the second
bound improves to

    1 <= l <= min(2, floor(13/r)).                         (2)

The fourth source `Z` has no quadratic sections, so that improvement is
not available for `Z`. In particular, `l=3` forces `r=4` and `Z`; the
converse is not claimed.

Here is the exact finite list of upper bounds. The directions are ordered.

| Generic SF rank r | k range | l range | l range for D/P/V | Number of coarse (k,l) bins | Positive square rank | Positive square cokernel |
|---:|---|---|---|---:|---:|---:|
| 4 | 1..3 | 1..3 | 1..2 | 9 | 28 | 9 |
| 5 | 1..3 | 1..2 | 1..2 | 6 | 29 | 8 |
| 6 | 1..2 | 1..2 | 1..2 | 4 | 30 | 7 |
| 7 | 1..2 | 1 | 1 | 2 | 31 | 6 |
| 8 | 1..2 | 1 | 1 | 2 | 32 | 5 |
| 9 | 1 | 1 | 1 | 1 | 33 | 4 |
| 10 | 1 | 1 | 1 | 1 | 34 | 3 |
| 11 | 1 | 1 | 1 | 1 | 35 | 2 |
| 12 | 1 | 1 | 1 | 1 | 36 | 1 |
| 13 | 1 | 1 | 1 | 1 | 37 | 0 |

Thus there are nine unresolved *bad rank values*, `4,...,12`, and one
successful auxiliary-map rank value, `13`, if attained. Refining by
ordered plateau lengths yields 27 necessary bad-rank bins and one
rank-13 bin, 28 in all. The source-labeled overlist has 99 bad bins and
four rank-13 source labels, 103 in all. It is a refinement of the same
overlist, not a competing count of mathematical problems.

These are finite containers for hypothetical actual configurations, not
a realization theorem, not a proof that the containers are nonempty,
and not a count of all branches in the original proof repair. Different
bins can be eliminated by the same future theorem, and a bin can conceal
further geometry. There is no meaningful completion percentage here.

## 2. Exact actual inputs and domain compatibility

Work over `C`, with `G=SL2(F5)`, on the original physical negative
parameter line `T=P(W*)`. The actual saturated sequence is

    0 -> E -> H tensor O_T -> Q -> 0,
    dim H=30, rank E=17, deg E=-54,
    rank Q*=13, deg Q*=-54.                              (3)

Here `H` is the actual plane-section space, not the 54-dimensional
coefficient space `M3`. The exact coefficient presentations are

    0 -> E  -> M3  tensor O(-1) -> M4  tensor O -> 0,
    0 -> Q* -> M3* tensor O(-1) -> M2* tensor O -> 0,

with

    M2=A+2V+3P+4D,
    M3=3W'+3S4+6T6,
    M4=2V+4P+3D.

All these representation names use the fixed physical marking:
`A=Sym^2 W`, `S4=Sym^3 W`, `D=Sym^4 W`, `T6=Sym^5 W`; `V` is the other
three-space, `P` the even four-space, and `W'` the other doublet. In
particular the source label `V` is not the representation `A`.

The imported actual facts include `H0(E(1))=0`; both `E` and `Q*` have
no nonzero constant subbundle and span their respective constant
ambients. The exact Koszul presentation gives

    H = W tensor M3 - M2 - M4 = 2A+2V+2P+2D.              (4)

Its center is even and it has no invariant vector. The Euler identities
from the same actual presentations are

    chi_G(E(3))  = W'+2T6,
    chi_G(Q*(3)) = T6-2W-S4.                             (5)

Positive irreducible multiplicities in (5) imply

    H0(E(3)) contains W'+2T6,
    H0(Q*(3)) contains T6.                               (6)

This uses `H0 = chi + H1` in the representation ring and nonnegative
`H1` multiplicities, not an assertion that `H1` vanishes.

The four-source theorem applies to this same actual `E`. Its actual
primary inclusion uses both arrows of the terminal pencil, the fixed
determinant rotation, and functoriality for the canonical slope quotient.
It establishes `W'+T6` inside the degree-minus-three coefficient module.
Intersecting with the actual splitting equations leaves exactly

    D: D O(-2)+(W'+T6)O(-3)+V O(-4)+O(-8),
    P: P O(-2)+(W'+T6)O(-3)+V O(-4)+W'O(-5),
    V: V O(-2)+(W'+T6)O(-3)+2V O(-4),
    Z: (W'+2T6)O(-3)+V O(-4).                            (7)

These necessary actual-source alternatives are not rank-three-specific.
The source proof explicitly does not establish rank-three coverage;
that caveat does not restrict its actual terminal-slope inclusion to
rank three. We use (7) only for the quadratic visibility asserted below.
We do not import a rank-three profile exclusion into rank `r>=4`.

In (3), the dual central object is `Q*=E^perp` inside `H* tensor O`, not
an arbitrarily dualized coefficient pencil. Its plateau is the actual
reversed annihilator plateau. All negative-transpose and differentiation
identifications use the same original parameter line and its one fixed
determinant convention. No separate parameter rotation, identification
of `H` with `M3`, or horizontal Birkhoff splitting is allowed.

Direct dependencies, all retained in full and hash-authenticated:

1. `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, original
   commit `db51525015bb7c5e825833d550d08dedf6f6ea96`: actual bundles,
   Euler identities, and the explicitly arbitrary-rank persistence lemma.
2. `POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md`, same original commit:
   actual square/SF identification, not merely equal dimensions.
3. `RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md`, same original commit:
   Sections 1-2 supply actual ambient character and general changing-rank
   Gauss-transform facts. Its rank-two conclusion is not imported at
   higher rank. Section 6 below proves the general determinant formula.
4. `four-sources.md`, public proof at commit
   `504b7eb800407dfc7e6340c98c72cdd553939f54`, path
   `research/hm/primary-terminal-slope-obstruction/PROOF.md`: the
   actual primary inclusion and necessary four sources, with its written
   HM prerequisites retained.

This is a conditional geometric deduction from these originals. A hash
check establishes exact source bytes, not their geometric truth or all
transitive prerequisites.

## 3. Maximal plateau, rank budgets, and endpoints

Let the generic rank of `beta_E` be `r>0`. For an actual saturated
subbundle `F` of the constant ambient, define `F^-` to be its sheaf
derivative kernel and `F^+` its saturated forward transform. If the
generic derivative rank is `s`, both `F/F^-` and `F^+/F` have rank `s`.
Differentiation gives regular adjacent maps, including across ramified
parameters after the stated sheaf-kernel and saturation construction.

Outward increments cannot increase. On the forward side the derivative
of the new stage vanishes on the preceding stage modulo the next one,
and hence factors through the preceding increment. On the backward side
the derivative takes values in the preceding quotient. Continue on each
side of `E` while the increment equals `r`. Finite ambient rank ensures a
unique maximal consecutive plateau

    F0 < F1 < ... < Fm,    E=Fk,    m=k+l,
    rank Fi = 17+r(i-k),    k,l>=1.                       (8)

At interior indices `0<i<m`, the derivative kernel is `F(i-1)` and the
forward transform is `F(i+1)`: the natural inclusions have equal generic
ranks, and saturation in the same ambient identifies the bundles.
At the endpoints, the derivative ranks are strictly smaller than `r`.
They must not be assumed equal to `r` or equal to one.

Writing

    p=rank F0=17-rk,    q=codim Fm=13-rl,

nonnegative ranks give `rk<=17` and `rl<=13`. Every stage `Fi` for
`i<m` has no constant subbundle. Below `E`, this follows by inclusion;
above `E`, a constant subbundle lies in the interior derivative kernel
and propagates backwards into `E`. Dually every `Fi` with `i>0` spans
the full constant ambient. A proper constant span below `E` would
propagate forwards and contain `E`, contradicting its full span.

There is no missing endpoint case in (1). For all its bins, `p>0`.
If the endpoint derivative of `F0` were zero, `F0` would be a nonzero
constant subbundle of `E`, impossible. Thus

    1 <= rank beta_F0 <= min(r-1,p).                      (9)

If `q>0` and the derivative of `Fm` were zero, `Fm` would be a proper
constant subspace containing `E`, also impossible. Thus

    1 <= rank beta_Fm <= min(r-1,q)       if q>0.           (10)

The sole `q=0` bin is `r=13,k=l=1`; here `Fm=H tensor O` and its
derivative has rank zero. This successful endpoint must be retained.

Equation (4) does not forbid a nonconstant rank-one endpoint. It forbids
an invariant constant line, a different object. Removing a rank-one
endpoint solely because `H` has no trivial constituent would be invalid.

## 4. Cubic persistence and quadratic visibility

We give the arbitrary-rank persistence proof rather than extrapolate a
rank-three result by its title. Suppose `H0(E(d))` is nonzero. Saturate
the image of a nonzero section to a line `L=O(-e)` in `E`. Then `e<=d`.
Its inclusion in `H tensor O` is saturated as well, since both successive
quotients are locally free. We have `e>=1`: a line of nonnegative degree
inside a trivial bundle must have degree zero and be constant, excluded
by `H0(E)=0`.

On an affine chart this inclusion is represented by a polynomial vector
`f(z)=v0+v1 z+...+ve z^e`. The vectors `f,...,f^(e)` span the same
constant coefficient space as `v0,...,ve`, by the triangular derivative
identity with nonzero factorial diagonal in characteristic zero. This
is a universal proof for arbitrary sections; no actual coefficients or
jets are evaluated. Therefore the `e`-th saturated forward transform
of `L` has reached its constant span, possibly earlier.

Differentiation and saturation preserve inclusion, so the `j`-th
transform of `L` lies in `F(k+j)` whenever that stage exists. If `l>d`,
then `k+e<m`, placing a nonzero constant subbundle in an interior stage.
Section 3 excludes that. Consequently

    H0(E(d)) nonzero implies l<=d.                        (11)

Apply precisely this argument to the dual reversed plateau with central
bundle `Q*`. Its forward length is `k`, so

    H0(Q*(d)) nonzero implies k<=d.                       (12)

The cubic nonvanishings (6) yield `k,l<=3`. Combined with the rank
budgets, they prove (1). The equalities in (7) give, as representations,

    H0(E(2)) = D, P, V, 0 for sources D, P, V, Z.

Equation (11) proves (2). The absence of quadratic sections for `Z`
does not force a length-three plateau. Nor does this argument provide
`H0(Q*(2))` for any source, so it gives no corresponding global `k<=2`
improvement. In particular, primal and dual directions cannot be swapped.

Only ordinary bundle cohomology uses equivariant Birkhoff splitting.
The persistence proof takes one actual saturated line inside the actual
filtered inclusion; it never refines the rank-r plateau into horizontal
line curves or assumes a split connection.

## 5. The auxiliary-map success stratum

The actual gate theorem identifies `SF` with the middle arrow in

    0 -> ker(B_l A_l) -> ker B_l -> coker A_l
      -> coker(B_l A_l) -> 0,

where actual multiplication by `l` gives injective
`A_l:M2,+ -> M3,-` and surjective `B_l:M3,- -> M4,+`, of dimensions
`41 -> 54 -> 37`. Its local Koszul comparison is what identifies the
middle map with the derivative; the assertion is not inferred from
dimensions alone. On the nonempty open subset where generic rank is `r`,

    rank(l^2)=24+r,
    dim ker(l^2)=17-r,
    dim coker(l^2)=13-r.                                  (13)

Hence `r=13` is exactly the generic-surjectivity stratum for this
positive square map, and its maximal plateau necessarily has `(k,l)=(1,1)`.
The current bounds do not prove the actual map attains that stratum.
The nine smaller ranks are failures of this sufficient square-endpoint
criterion, not proofs that a different smoothing pencil fails.

The gate source explains a further conditional implication for its
positive pencil once square surjectivity is proved. This note proves no
full-adjoint invertibility, no actual source coefficient or residual
identity, no Bockstein order, and no original proof repair. Its word
“successful” refers only to the specified auxiliary-map criterion.

## 6. Optional determinant-degree consistency check

This check prevents treating elementary endpoint degree bounds as an
unproved additional exclusion. Let `L_i=F_i/F(i-1)`, `c_i=deg L_i`,
`a=deg F0`, `b=deg Fm`. The actual regular derivative induces a generically
injective map `L_i -> L_(i+1) tensor Omega`. Its determinant gives

    c_(i+1)-c_i=2r+delta_i,    delta_i>=0.                  (14)

All stages and quotients are center-even in the actual equivariant
ambient. Since `G` is perfect, their determinant degrees are even;
therefore `a,b,c_i,delta_i` are even. The negative top slope of `E`
gives `a<=-2p`, or `a<=-ceil_even(3p)` for source `Z`. The annihilator
of `Fm` is a subbundle of `Q*`, which has strictly negative summands;
hence `b<=-ceil_even(q)` when `q>0`. When `q=0`, exactly `b=0`.

Eliminating `c_1` from (14) gives the universal identity

    (k+l)(-54) = l a+k b-rkl(k+l)
       -l sum_(j<k) j delta_j
       -k sum_(j>=k) (k+l-j) delta_j.                     (15)

No linewise connection splitting is used to obtain (14) or (15).
Every coarse bin, and every source-refined bin allowed by (2), has
abstract even integers satisfying these limited conditions. The
certificate constructs them with every `delta_i=0`: choose an even
`c` so that

    c_i=c+2r(i-1),
    a=-54-kc-rk(k-1),
    b=-54+lc+rl(2k+l-1),                                 (16)

and check the displayed endpoint inequalities. For the full endpoint
`r=13,k=l=1`, take `c=28`, giving `a=-82,b=0`.

These integer witnesses establish consistency only of the displayed
degree/parity constraints. They are not bundles with the required
representation characters, actual filtered inclusions, or realizations
of the bins. Stronger endpoint, image, character, or saturation arguments
may still exclude them. The character of `H` does not itself justify
dropping any bin on constant-endpoint grounds.

## 7. Reproduction and certificate boundary

Run `python3 verify.py` and `python3 -O verify.py`; their JSON outputs
must match `RESULT.json` byte for byte. No dependencies are required.
Run from any working directory. All checks use explicit exceptions,
not assertions disabled by optimization.

The verifier authenticates all four retained complete sources by byte
length, SHA256, Git blob identity, and immutable public URL. Universal
integer McKay-character arithmetic checks (4)-(7), all four rank/degrees,
their Euler characters and quadratic visibility. It solves only the
four-variable equation `b+c+e+f=3` after the imported primary inclusion,
not a historical 28-, 37-, or 159-record enumeration. It then derives
the full bounded list in (1)-(2), the endpoint ranges (9)-(10), all exact
square dimensions (13), and the limited degree witnesses (16).

No actual HM/source coefficients, parameter choices, jets, multiplication
or Gauss matrices, actual ranks, or historical enumeration are computed.
The written geometric proof, not integer acceptance alone, supplies
maximality, persistence, saturation, and actual-map identification.
The separate generic-rank-four lower bound remains an explicit imported
premise. This is not proof-assistant verification of the original theorem.
