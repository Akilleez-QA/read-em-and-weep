# Independent scoped review

## Exact reviewed edition

Reviewed on 2026-10-20. This review binds exactly to:

- `PROOF.md`, SHA-256 `7b336def2d87813b493586dc9fe1627201414cf980223a86eac8113fe836038b`.
- `README.md`, SHA-256 `a274bc0342ffb42004c6a73cb89aebc7f8b7afa8e7c6c5e8947859a8a45104db`.

Verdict: **no blocking mathematical finding within the stated scope**.
The abstract generic-quadratic theorem, the induced generic multiplication
surjectivity for the fixed HM trace-free coefficient, and the generic
translated ordered-root order-six vanishing follow from the named inputs.
This is an independent mathematical review, not formal verification.

The final edition also incorporates harmless precision improvements:
the rank-one-space lemma assumes its operator space is nonzero, and the
abstract counterexample is finite length. The arbitrary-field lemma uses
the name `k` consistently for scalar spans. None changes the HM argument.

## 1. Independent algebra check

The key lemma was checked independently before reading the author's draft.
Let `L` be the linear space of maps `mu_q:M_1 -> M_3`. If no member is
surjective, every member has rank at most one.

The rank-one-space argument in Section 1 is valid. Two rank-one operators
whose image vectors and defining functionals are both independent have
a rank-two sum. Starting from one nonzero operator, either all images
lie in its image line or comparison with a second independent image
forces all functionals to be proportional. This proves the stated
dichotomy without invoking a classification result.

Generation in degree zero gives both necessary equalities:

    M_1 = S_1 M_0,        M_3 = S_2 M_1.

The second equality rules out the common-image alternative. In the
common-kernel alternative, choosing a nonzero functional `lambda` and an
element `a_0` with `lambda(a_0)=1` gives a *linear* map
`G(q)=q a_0` satisfying `q a=lambda(a)G(q)`. There is no unproved
factorization or compatibility assumption at this point.

The first equality permits a single choice `z,m` with
`c=lambda(zm) != 0`. The two displayed commutativity identities then give

    c G(xy) = lambda(xm) G(yz),
    c G(yz) = lambda(ym) G(z^2),

and therefore

    G(xy) = c^(-2) lambda(xm) lambda(ym) G(z^2).

Products of linear forms span `S_2`, so every multiplication image lies
in one fixed span of dimension at most one. This contradicts
`M_3=S_2M_1` and `dim M_3=2`, including the case `G(z^2)=0`.
The argument uses the same `m,z` throughout and does not require a
chosen HM element or a multiplication-table calculation.

The nonempty locus is Zariski open because the multiplication matrix
depends linearly on quadratic coefficients and surjectivity is detected
by its maximal minors. Scaling a quadratic does not change its image,
so the projective locus `U_M` is correctly defined. No maximal minor
is evaluated in this proof.

## 2. Primary generation and the trace-free coefficient

The independently fetched PR167 proof contains the exact tail

    15S(-1) -> 5S -> H^1_*(F) -> 0.

Thus degree-zero generation is an actual imported premise, not a
consequence guessed from dimensions. The same source supplies the
Hilbert function with `dim M_3=2` and `M_4=0`.

PR440 Section 3 supplies the two natural surjections at twists four
and six. Its proof explicitly states compatibility with multiplication
by every homogeneous polynomial. If `q:M_1 -> M_3` is onto, the map
from `15M_1 + 4M_2` to `15M_3` is onto; the four-copy part lands in
`M_4=0`. Lifting a target class through the two surjections proves
that `q:H^1(B(4)) -> H^1(B(6))` is onto. This correctly proves the
stronger statement independently of the cubic `r`.

The reduced presentation is also used correctly. The primary-module
portion of PR440 does not require `(q,r)` to be a regular sequence.
That requirement belongs to its separate surface-Koszul argument.
Here `bar M_3=0`, so the target of the retained reduced differential
vanishes. The proof does not incorrectly delete an incoming map or
infer vanishing merely from a bound on the dimension of its target.

## 3. Universal quadratic and the orbit argument

The independently fetched PR158 weight-geometry input gives exactly
the two weight differences and the full rank-six trace normalization
used in Section 4. The identities

    sigma_i = e_2 - 3p_i,
    p_1p_2 + p_1p_3 + p_2p_3 = e_1e_3 - 4e_4

give `sum sigma_i^2=6(e_2^2-3e_1e_3+12e_4)`, hence
`t_2=12(c^2-3bd+12ae)` in ordinary homogeneous coefficient coordinates.
This agrees separately with PR139's recorded rank-six trace identity.
Agreement on the dense monic chart extends to the global homogeneous
quadratic section. A harmless determinant-line normalization only
rescales it.

The quadratic is nondegenerate: its gradient vanishes only at the
zero coefficient vector. Equivalently it consists of two nondegenerate
paired coordinate blocks and a nonzero square. No HM map is evaluated
by this universal scalar statement.

The nondegenerate locus in projective quadratic space is nonempty
open and is a single `PGL_5` orbit over the complex numbers.
Its intersection with `U_M` is nonempty because projective quadratic
space is irreducible. The inverse image under the orbit map is
therefore nonempty open, and it is dense because `PGL_5` is
irreducible. Using projective quadrics, or equivalently GL lifts with
scalar-invariant conclusions, resolves the `O(1)` linearization issue.

## 4. Transport and the exact scope of order six

The orientation in Section 5 is correct:

    q_g = g o q_0,
    u_g = (g^(-1))^*u_0,       v_g = (g^(-1))^*v_0.

These are precisely the invariant sections on the target of `q_g`
whose pullbacks recover the original ordered-root weights. The
root variety, ordinary collision ideal and root permutation action
remain fixed. The fixed HM bundle is not acted on by an assumed
equivariant structure. Instead its pulled-back coefficient
`E_g=q_g^*B tensor A_g^(-2)` varies.

PR437's filtration theorem applies to any locally free coefficient.
Applying it to `g^*B`, then transporting by the target isomorphism
`g` and using the projection formula, yields the stated filtration
with the *fixed* target bundle `B` and the translated ideals
`K_n(u_g,v_g)`. Scheme-theoretic collision strata, including quadruple
collisions, are transported rather than removed.

The PR439 endpoint then gives

    H^2(Z,I_D^6 E_g)_chi^vee = Q(u_g,v_g) + Q(u_g,v_g).

The generic quadratic result kills each quotient, proving the entire
ideal-coefficient vanishing at order six for every `g` in the
specified nonempty open set. The ensuing restriction injectivity
and existence of ideal-valued primitives for closed ideal-valued
cochains follow from the coefficient exact sequence and ordinary
affine Cech cohomology, with exact characteristic-zero character
projection.

These statements concern the varying coefficient `E_g`. They do not
prove that the identity transformation lies in the good locus, that
every projective transformation preserves HM, or that the originally
fixed source has high-order membership.

## 5. Fixed-position limitation

The finite-length abstract example in Section 6 is valid:

    M = C[x_0,x_1,x_2,x_3,x_4] /
        (x_2,x_3,x_4,x_0x_1,x_0^4,x_1^4).

Its degree-three part has basis `x_0^3,x_1^3`. The displayed
nondegenerate quadratic annihilates the module, whereas
`x_0^2+x_1^2` sends the basis of `M_1` to that degree-three basis.
This is not an HM counterexample. It establishes only that smoothness
of a prescribed quadratic cannot replace the genericity condition
under the abstract hypotheses.

In particular the reviewed theorem does not evaluate
`Q(t_2,t_3)` at the original fixed relative position, prove the
order-six bound optimal, determine any actual obstruction or source
representative, solve the separate pure conditions, construct a
module lift, or establish algebraicity.

## 6. Independently inspected sources

The following exact public inputs were fetched read-only. For the
first five proof files below, local byte copies were checked against
the returned Git blob identifiers; this was file-integrity checking,
not execution of mathematical checkers.

- PR167, commit `063da90fc4543304e87e701cdefcc08225412f17`,
  `research/conductor-normalization/sharper-hm-regularity/PROOF.md`,
  blob `31c7475d89b6c833696b6e915724e5d6d4221e42`,
  SHA-256 `996e42cc441a21aef8636f1ff7e808a25c07baf504d4111b3810da1209d0262a`.
- PR440, commit `829e03411d04511f6cf04860bf18db4a70b12448`,
  `research/hm/degree-six-structural-reduction/PROOF.md`,
  blob `998dd6d488636565c6b32e8879383cce167f010f`,
  SHA-256 `3a1550676140a8558c417838a017488bf9d45c100e125f8b487ffadd533df3eb`.
- PR437, commit `50e82ed233cd7729c38608194f990376eb832418`,
  `research/hm/paired-collision-filtration/PROOF.md`,
  blob `9697423e880070cdf34cbc3548f5a2b32b2a40a0`,
  SHA-256 `41fd8967a1bd876c0375ab35c889d3eec431e5a72cd66ca2fa74937e503cbca1`.
- PR439, commit `bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b`,
  `research/hm/paired-collision-endpoint/PROOF.md`,
  blob `8b420be9fd49374981a7dfc59058483a4ae4dbfa`,
  SHA-256 `4ed13b7412e21665d2e102c9dbece152c47e962e3913596f5f0475e4187a7453`.
- PR139, commit `c5fb4a0bcc3c8e35093fcfcff9a73a79a45a18e5`,
  `research/hm/cubic-reconstruction/PROOF.md`,
  blob `daf01b27c34233f81aa2f2a2eae0f4f90827ef89`,
  SHA-256 `bc6b3fb7756cecba34a679ea603478021c0bbe89fff40d2e8a96a30e16278122`.
- PR158, commit `aab61d34a84c9b8b5a908606a7beb7212d45fe7c`,
  `research/conductor-normalization/ideal-power-contractions/WEIGHT-GEOMETRY-INPUTS.md`,
  returned blob `507b5281144debc5395f88ac605e5a89c4867b87`.

Current PR1 was fetched independently through comment
`6290422971` (2026-10-20 12:04:35 UTC; 453 returned discussion
entries). Its latest coefficient handoff leaves the fixed quotient
unevaluated. Targeted inspection of that discussion and the pinned
proofs did not locate the present generic-quadratic theorem. PR144's
metadata at `5d517ce3c7e528195c80541fd2d27e8037d315aa` identifies a
different generic restriction-deformation result. This review does
not certify the author's search queries as an exhaustive repository
or literature novelty search.

The primary published resolution and older geometric/cohomological
theorems are imported as stated in those pinned proof packages.
No fresh primary-PDF page audit, selected HM/source evaluation,
HM multiplication-matrix construction or rank calculation, random
sample, mathematical checker execution, or external write was
performed for this review.
