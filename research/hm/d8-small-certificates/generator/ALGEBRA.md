# Algebraic audit of the corrected HM transposition

12 October 2026

The map implemented in `generator-action.js` is the transferred geometric action
of the transposition a=(12), namely T=Pρ(a)I, on the pinned full-sign HM finite
model over Q. Its nonzero off-diagonal blocks are genuine four-step corrections.
The B/C compression and the exponent pruning preserve this exact map. The
chain-map identity follows on every cochain from the perturbation identities,
independently of selected-column tests. This audit does not construct or identify
a geometric obstruction.

## Conventions and source model

Use the line complex and ordered tensor contraction specified by
`pinned-verify-hm-ext.js` and `full-sign-boundary-oracle.js`. Their SHA-256 pins are
checked by `generator-action.js`; the underlying line-complex source commit is
`add03476d9055aa00e1e00778eea6332cf8e01cc`.

Write d₀ for the tensor Čech differential, h for the ordered Čech homotopy, and
q=ip for the unperturbed harmonic projector. The side conditions are

    pi=1,  1−ip=d₀h+hd₀,  h²=0,  ph=0,  hi=0.

For internal endomorphism degree r and Čech degree p, use
Δ=(−1)^p[d_K,−]. Thus the right-composition coefficient in the commutator is
−(−1)^r. The line-complex polynomial identities d_K²=0 imply Δ²=0, and the
Čech totalization sign gives d₀Δ+Δd₀=0. Consequently D=d₀+Δ squares to zero.

The map ρ(a) swaps the first two exponents and chart labels. Its coefficient is
−1 precisely when both swapped chart factors have Čech degree one. The
coefficient multiplicity spaces are fixed. The ordinary product y₁y₂y₃y₄ gives
no additional sign. The elementary symmetric polynomials in d_K are unchanged
by this swap, so ρD=Dρ. The unperturbed i and p are equivariant because the four
line degrees and the four one-factor contractions agree.

## Exact transfer and the chain-map identity

For the sign convention above the perturbation formulas are

    I=(1+hΔ)⁻¹i,  P=p(1+Δh)⁻¹,
    d=pΔ(1+hΔ)⁻¹i.

These are finite sums: each h lowers Čech degree, which lies between zero and
four. The perturbation identities are DI=Id and PD=dP. Hence

    dT=dPρI=PDρI=PρDI=PρId=Td.

This proves the identity on the entire finite model over Q. It is not a claim
inferred from a sample of basis columns. Matching the implementation to the
displayed finite formula, as justified below, is the relevant implementation
obligation. Exhaustive exact matrix tests additionally certify the concrete
generated matrices against the existing differential.

The general transfer theorem does not require T²=1 on cochains. If H is the
perturbed homotopy, then

    T²−1=−d(PρHρI)−(PρHρI)d.

Thus it induces the actual involution on cohomology even if its cochain group
relation is only true up to homotopy. In this concrete computation,
`verify-generator.js` also certifies the stronger equality T_a²=1 on every
finite cochain. This verified property belongs to this particular adjacent
generator; no strict relations involving other generators are asserted.

## Why the compressed states are exact

In one Čech factor use labels A and B for degree-zero chart components and C
for degree one. Let J be the span of tensor monomial states containing at least
one A label. Then:

- Δ preserves chart labels, so ΔJ is contained in J.
- ρ permutes labels, so ρJ is contained in J.
- hJ is contained in J. In a summand of the ordered homotopy, an earlier A is
  killed by its factor q; h kills an A in its own factor; a later A persists.
- pJ=0, since the one-factor harmonic projection kills A.

Every word p(Δh)^uρ(hΔ)^vi can therefore be evaluated modulo J. Discarding A
branches at any intermediate stage is exact. On H⁰, the inclusion A+B becomes
B modulo J; on H¹ the inclusion is C. The surviving one-factor h branch is

    C(x^e) ↦ B(x^e)  if e<0 and e≤n,
    C(x^e) ↦ 0       otherwise,

where n=r−2 in the full-sign sector. Earlier B factors survive q exactly when
0≤e≤n; earlier C factors survive exactly when n<e<0. These are precisely the
tests in the pinned `homotopy` implementation. The tensor sign counts preceding
C labels. The `rho` implementation supplies the C,C swap sign.

This is a quotient argument for words in Δ, h, ρ and p. It is deliberately not
an assertion that the B/C states form a quotient Čech complex: d₀ can send an A
state to a C state, so J is not d₀-stable.

Each Δ monomial adds either zero or one to every exponent; h, ρ and p do not
change the multiset of exponents. For a permutation-invariant final window
[lo,hi], a state with t remaining Δ steps cannot contribute if one exponent is
outside [lo−t,hi]. The code uses this exact reachability bound. In degree two the
target window is [0,0], and in degree three it is [0,1].

## Why four steps and three candidate terms suffice

The relevant harmonic spaces are

    V²=N_(−2,4) ⊕ P_(2,0),  dimensions 6480+80,
    V³=N_(−1,4) ⊕ P_(3,0),  dimensions 3920+160.

In a term p(−Δh)^uρ(−hΔ)^vi, each Δ raises internal degree by one and each h
lowers Čech degree by one. Therefore an N→P correction requires u+v=4, and its
overall expansion sign is positive. The terms with u=0 or v=0 vanish by ph=0
or hi=0, using equivariance of p or i. Only (u,v)=(3,1),(2,2),(1,3) remain.

The diagonal blocks are the harmonic signed permutations. On N, the sign of a
is −1. On P it is +1. The degree-two P block is the identity, since all its
exponents are zero; the degree-three P block permutes its binary exponent
tuples. Degree one and degree four have no such off-diagonal blocks.

## Exact simplification for the first adjacent transposition

At a fixed internal degree, let h_j and q_j be the one-factor operators, extended
to the tensor product with their Koszul signs. The ordered homotopy and its
conjugate are

    h  =h₁+q₁h₂+q₁q₂h₃+q₁q₂q₃h₄,
    h′ =ρhρ⁻¹=h₂+q₂h₁+q₁q₂h₃+q₁q₂q₃h₄.

The relations h_j²=h_jq_j=q_jh_j=0 imply

    hh′=h₁h₂,  and therefore hρh=h₁h₂ρ.

For example, the product of the common tail with itself is zero by the tensor
contraction side conditions, and every mixed term other than h₁h₂ contains one
of the vanishing one-factor products. This identity includes all graded signs.

Every candidate correction contains exactly this central hρh. In compressed
states its replacement swaps the first two exponents and changes both labels
from C to B, with coefficient +1, provided both exponents are negative and at
most n. It is zero otherwise. The two minus signs are the C,C permutation sign
and the sign of applying h₂ while the first factor is C.

This also proves the observed vanishing of four of the six candidate blocks.
Before the central pair, factors 1 and 2 must both remain C; afterward they are
both B. Every other h must consequently act in factor 3 or 4.

- In degree two, for v=1 or v=2 the central line degree is n=v−4≤−2. Its new
  B exponents remain negative after the next Δ. A further ordered h in factor
  3 or 4 requires those earlier B factors to be harmonic H⁰, which is
  impossible. Thus only (u,v)=(1,3) survives. Its preceding two h operations
  must occur in factor 4 and then factor 3: the opposite order leaves a
  negative B in factor 3 blocking the operation in factor 4.
- In degree three, v=1 fails by the same argument, with central n=−2. If v=3,
  the second preceding h is applied at internal degree r=1, where n=−1. It
  would need the first two C factors to be harmonic H¹ of O(−1), but that space
  is zero. Thus only (u,v)=(2,2) survives.

These vanishings are algebraic and apply to every source column. They do not
depend on an empirical zero count. The implementation may retain all three
candidate terms as a transparent check of the formula.

## An exhaustive finite matrix certificate

Write the differential blocks as

    d¹=(A₁,B₁)ᵗ,
    d²=[[A₂,0],[B₂,C₂]],
    d³=(A₃,0),

where each A is a one-step N→N map, B₁ and B₂ are the five-step N→P maps, and
C₂ is the one-step P→P map. Write the action blocks as

    T¹=S₁,  T²=[[S₂,0],[K₂,R₂]],
    T³=[[S₃,0],[K₃,R₃]],  T⁴=S₄.

Here S denotes the negative harmonic permutation, R the positive permutation,
and K the computed correction. An exact sparse matrix certificate need only
check the following complete list of rectangular equalities:

    A₁S₁=S₂A₁,
    B₁S₁=K₂A₁+R₂B₁,
    A₂S₂=S₃A₂,
    B₂S₂+C₂K₂=K₃A₂+R₃B₂,
    C₂R₂=R₃C₂,
    A₃S₃=S₄A₃.

Checking every column with exact integer arithmetic is a rigorous certificate;
checking selected columns is only a debugging test. The matrices can be
generated once and multiplied sparsely, avoiding repeated five-step transfers
inside each matrix-product check. The HPL proof above explains why these
identities hold and covers every column without relying on numerical sampling.

The saved `certificate.json` reports a successful exhaustive run: all 2,560
degree-one columns, all 6,560 degree-two columns, and all 4,080 degree-three
columns satisfy dT=Td, with structurally zero source blocks handled explicitly.
It also checks d²=0 and T_a²=1. The degree-two correction has 568 nonzero entries
in 272 columns; the degree-three correction has 1,664 entries in 1,128 columns.
All nonzero correction coefficients have absolute value one. Runtime is recorded in `certificate.json`; it is descriptive, not part of
the proof.

## Scope over other fields

The operators used here and their matrix entries are integral, and the
chain-map identities can be reduced modulo a prime. This observation does not
transfer rational cohomology dimensions, detector completeness, or obstruction
nonvanishing to or from characteristic three. Those require separate
base-change or saturation information. No obstruction representative, geometric
choice-independence theorem, or evaluation of an obstruction is supplied by this
generator-action computation.
