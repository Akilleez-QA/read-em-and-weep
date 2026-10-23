# The nine-dimensional branch gives an actual terminal negative module

## Conditional result

Retain the actual source2 nonzero pure-V Q-compatible radical hypotheses,
and assume the nine-dimensional endpoint branch of PR1059/PR1066. Let
R=Sym W be the polynomial ring of the SAME two actual negative coordinates.
Define the full actual negative submodule

    F_infty = R · im h

inside the actual cohomology module, with its original cohomological
integer grading. Then it is concentrated in degrees two, three and four:

    (F_infty)_2=P+D,  (F_infty)_3=W'+2T,  (F_infty)_4=NC4=P+D,
    (F_infty)_d=0 for d>=5.

Its actual minimal G-equivariant R-free resolution is

    0 -> (P+D) tensor R(-6)
      -> S tensor R(-3) plus (2V+P) tensor R(-4)
                         plus S tensor R(-5)
      -> (P+D) tensor R(-2) -> F_infty -> 0.             (1)

Its negative-coordinate socle is precisely the embedded NC4, its length
is32, and its exact annihilator in R is (W)^3. Thus it is a faithful
module over R/(W)^3. No claim is made that it is free over that quotient.

This promotes PR1066's previously artificial truncation to the actual
negative submodule, using the new actual degree-five annihilation theorem.
It does not describe the full Rao module, impose positive-coordinate
stability, identify any repeated D copies, or select the nine-dimensional
branch. No actual coefficient, point, parameter, jet or source rank is
computed.

## 1. Exact inputs and retained embeddings

INPUTS.json pins and authenticates five complete public proofs:

- PR1068 at05e8b33eb87e9f36aa30500145cc42bc0ea00df8,
  pure-v-terminal-nonvanishing/PROOF.md: NC4 is the actual joint-negative
  kernel in degree four. Only Sections1–3, not its canonical terminal
  sextet or radical-extension conclusions, are used here.
- PR1066 at638efef0469b7230f04560d0a02f3cf4d4116c0c,
  source2-pure-v-small-relations/PROOF.md: the actual first three spaces,
  forced nonzero P graph, absence of lower socle and minimal resolution
  of their explicitly artificial truncation.
- PR795 at3f811311d76914a555c7e7d0c5b887b41805aa6c,
  source2-radical-filtration/PROOF.md: the actual evaluation diagram and
  inclusion NC into the same fixed-variable source2 pencils.
- PR1052 at64e4fdd771a14a764c6e119d2eb25b0237d83622,
  negative-string-terminal-gate/PROOF.md: actual Koszul exactness

      0 -> M3 --delta--> W tensor M4 --mu--> M5 -> 0.       (2)

- PR1056 at875e86e2eec36a050e9a626735199681762e43ec,
  restriction-socle-kernel/PROOF.md: actual connecting-map identification
  of the next multiplications and the maximal-slope kernel subspace.

All paths above have prefix research/hm/. No numerical catalogue table
from PR1056 is used. The relevant statements were read as full proofs,
not inferred from their titles or representation counts.

PR795 supplies the exact actual kernel inclusion

    0 -> E_C=(P+D)O(-2) -> E_R -> T O(-3) -> 0,
    E= W O(-9) direct-sum E_R.                            (3)

Its evaluation diagram identifies NC4 with the IMAGE of H1(E_C) in
H1(E)=M4. Its first two spaces and second arrows are literally

    NC2=Sym16 W, NC3=Sym17 W,
    NC4=Sym18 W/H_t,   s -> [ell s].                     (4)

In particular NC3 has dimension18 and NC4 dimension9. These are actual
subspaces of the original pencils, not newly chosen equal-character
summands. PR1066's endpoint equality F4=NC4 refers to these inclusions.

## 2. Why the next actual negative arrows kill this endpoint

Here is the direct arrow argument, retaining the full exact sequence (2).
With formal coordinate notation x,y, its injection is

    delta(s)=x tensor (ys)-y tensor (xs)

up to the fixed invertible determinant convention. Because (4) is a
subpencil for BOTH actual negative arrows, it restricts to an injection

    NC3 -> W tensor NC4.

The two spaces have dimension18, so this actual restriction is onto.
Exactness of (2) therefore gives mu(W tensor NC4)=0. In other words
both actual maps NC4->M5 vanish. This argument uses actual containment
and injectivity before the dimension comparison, not character matching.

The bundle argument in PR1068 independently authenticates the same
embedding. In (3), the quotient E/E_C is W O(-9) plus T O(-3).
After twisting by2 it has no sections. Thus H0(E_C(2))->H0(E(2)) is
an isomorphism, and evaluation identifies E_C with the canonical
maximal slope-minus-two subbundle E_{-2}. PR1056 identifies the actual
joint-negative kernel with the image of H1(E_{-2}) in H1(E), with the
same determinant convention. PR795's diagram identifies that image
with NC4. Hence the equality used here is indeed

    NC4=ker[M4 -> W tensor M5]

as embedded subspaces. No splitting of E_R or comparison of abstract
D representations enters this identification.

## 3. Promotion from artificial truncation to actual submodule

By definition, the degree-two, degree-three and degree-four pieces of
R·im h are the actual F2,F3,F4 used in PR1066. In the branch under
consideration F4=NC4. Section2 gives W F4=0 in actual degree five.
Associativity then gives R_d F4=0 for every d>0, so every higher
negative descendant of the generators vanishes as well.

Consequently the identity on the first three actual spaces identifies
F_infty, after shifting its generators from degree two to degree zero,
with the entire truncated R-module of PR1066. This is an isomorphism of
modules with all negative multiplication maps, not merely equality of
Hilbert functions. It transports that theorem's socle calculation and
minimal resolution. Shifting each degree there by two gives exactly(1).
The socle is the same embedded NC4, and length is9+14+9=32.

The forced nonzero graph and its Q-preserving normalization boundary
remain as in PR1066; promoting the module does not assign a value to
that graph scalar or construct new positive-coordinate actions.

## 4. Exact negative annihilator

Write m=(W) in R. Section3 gives m³ F_infty=0. The homogeneous degree-zero
annihilator is zero because F_infty is nonzero. The degree-one
annihilator is the kernel of the G-map

    W -> Hom((F_infty)_2,(F_infty)_3).

It is zero: W is irreducible and the action is nonzero, indeed its
images generate the nonzero degree-three piece. Similarly the
quadratic annihilator is the kernel of

    Sym²W -> Hom((F_infty)_2,(F_infty)_4).

Sym²W=A is irreducible and this action is nonzero because it generates
NC4. Its kernel is zero. Since F_infty is graded, its annihilator is
a homogeneous ideal: apply a putative inhomogeneous annihilator to
homogeneous generators and separate output degrees. Thus there are
no lower-degree annihilators and

    Ann_R(F_infty)=m³.

This is an exact universal structural conclusion for the conditional
actual submodule, not a rank computation for a selected quadratic.
It asserts nothing about annihilators involving positive variables.

## Verification and scope

verify.py authenticates all five immutable inputs and checks the bounded
cohomology dimensions, determinant-convention Koszul cancellation,
restricted dimensions, degree shifts, Hilbert numerator and annihilator
irreducibility counts. Its structural checks do not replace the actual-map
proof in Sections1–3. Run python verify.py and python -O verify.py; both
produce RESULT.json identically. No external files are modified.
