# Quadratic-annihilated endpoint reduction for every non-V source2 radical line

## Result

Retain the pinned actual-source hypotheses. Suppose a nonzero radical
endomorphism j of the fixed source2 negative pencil commutes with the actual
invariant quadratic Q, and j is not pure V. The unique exceptional mixed
radical direction is now INCLUDED. Let I=im(j), barN=N/I, and barQ be induced
by Q. The genuinely embedded endpoint subpencil NC defines a subspace

    Z=NC2/I2 inside barN2,       character V+D, dimension8.

Every induced negative quadratic annihilates Z. This does not assert that
the first negative arrows kill Z, or that Z is their common kernel.

The restriction barQ|Z has exactly two possible ranks,8 or3:

- Rank8 gives a further24-to-20 linear obstruction pencil, preserving all
  formal cohomology and every t-adic Bockstein of the original41-to-37 family
  Q+tT_a. Its invariant kernel is A+D, cokernel P, rank16.
- Rank3 gives a permanent D kernel plus an active24-to-25 pencil with invariant
  kernel A, cokernel P, rank21. Every37-minor of the original41-to-37 matrix
  vanishes identically on the whole affine family Q+Sym²W of negative-
  quadratic perturbations. The original map is never onto on that family.

Thus all the two-term rank3/8 conclusions of PR957 extend from regular
non-V directions to EVERY non-V direction. Neither a compatible line nor
an actual rank alternative is asserted to exist. No source/pair exclusion,
full repair, or assertion about other quadratic directions follows.

## 1. Exact inputs

INPUTS.json records public immutable paths, Git blobs and SHA-256 hashes;
inputs/ contains exact originals from Akilleez-QA/read-em-and-weep:

- PR794 at7fd254100b83bb03f41b776ea3119690aa51f671,
  research/hm/source2-radical-rank-locus/PROOF.md.
- PR795 at3f811311d76914a555c7e7d0c5b887b41805aa6c,
  research/hm/source2-radical-filtration/PROOF.md.
- PR950 at54c7e78bd5351b3ecbdcc4b3b558a0012eb79566,
  research/hm/source2-radical-image-reduction/PROOF.md.
- PR957 at8175dc16dd729b9078281024a5915a66d15ccb2e,
  research/hm/source2-regular-zero-arrow-reduction/PROOF.md.

PR794 supplies containment of every radical image in the genuinely embedded
NC, not merely isomorphic representations. For every non-V direction,
I2=P+D, I4=NC4=P+D, of dimension9. Its middle image equals NC3 except at the
unique exceptional mixed direction, where NC3/I3 has character T, dimension6.
These assertions hold for every balanced endpoint and both coupling classes.

PR795 supplies the genuine exact sequence0->NC->NR->N8->0 of the original
fixed negative pencils, including its natural arrow maps. In particular
NC has characters(V+P+2D,W'+S+2T,P+D). The actual-map transfer hypotheses
in those sources remain in force.

PR950 proves for every non-V compatible j, including the exceptional one,
that Q:I2->I4 is an isomorphism. It gives the filtered two-term cancellation
from original41-to-37 to barN2->barN4 of dimensions32-to-28, with

    barN2=A+2V+2P+3D,  barN4=2V+3P+2D,
    ker barQ=A+D,      coker barQ=P.                         (1)

Its filtered equivalence extends over the multivariable formal power-series
ring, because its image block has invertible constant term and all negative
quadratics preserve I. No full three-vertex or full-module equivalence is
asserted. PR957 supplies the elementary constant-block reduction mechanism;
we repeat its algebra below with the weaker, newly proved hypothesis.

## 2. The crucial weaker condition: quadratic annihilation

Since I is a subpencil contained in NC, its quotient K=NC/I is genuinely
embedded as a subpencil of barN. At vertex two,

    K2=(V+P+2D)/(P+D) has character V+D;

at vertex four, K4=NC4/I4=0. Thus K has one of the two character triples

    regular non-V:        (V+D,0,0);
    exceptional mixed:    (V+D,T,0).                        (2)

These are character descriptions of the actual subpencil; no splitting
of the exceptional triple is asserted. Let barA_l and barB_m be the two
fixed families of negative linear arrows. Subpencil containment gives

    barA_l(Z) subset K3,          barB_m(K3) subset K4=0

for EVERY pair of linear forms l,m. Hence

    barB_m barA_l(Z)=0.                                      (3)

Every induced negative quadratic is a linear combination of these
composites, so barT_a(Z)=0 for all a in Sym²W. This proves the required
condition even if the exceptional first arrows on Z are nonzero. It uses
neither an exceptional extension splitting nor a common-first-kernel claim.
The space Z here is the embedded endpoint quotient, not a replacement by
an arbitrarily chosen isomorphic V+D.

## 3. Two restriction ranks and cancellation without a pencil splitting

Set F=barQ|Z. By(1), its restriction to V is injective since ker barQ has
no V. On the irreducible D it is either zero or injective. Inequivalent
V and D images cannot intersect. Therefore rank F is3 or8. Put

    L=ker F, Y=im F;
    rank8: L=0,Y=V+D;       rank3: L=D,Y=V.

Equation(3) says that the whole perturbed map restricted to Z is the
constant F, simultaneously for every negative quadratic. Define an active
linear pencil on the canonical quotient spaces

    C2=barN2/Z,  C4=barN4/Y,
    M_C(t)[x]=[(barQ+t barT_a)x].                             (4)

It is well defined without assuming that barQ preserves NC or any splitting
of barN. Choose complements only for an explicit chain calculation:
Z=L+Z', barN2=L+Z'+X, barN4=Y+W. The restriction F:Z'->Y is invertible.
The matrix of the actual two-term family then has shape

    [ 0  F  C(t) ]
    [ 0  0  D(t) ],         D(t)=M_C(t).

The domain shear(l,z,x)->(l,z-F^-1 C(t)x,x) is polynomial and invertible,
with inverse changing minus to plus. It preserves the t-adic filtration.
It removes C(t), after which the constant F block contracts. Thus the
original complex, after PR950's first cancellation, is filtered homotopy
equivalent to

    L[[t]][0] direct-sum [C2[[t]] --M_C(t)--> C4[[t]]].       (5)

The same identities hold modulo every t^m and over the multivariable formal
power-series ring. Therefore all t-adic Bockstein pages and differentials
are preserved by(5), retaining the permanent L summand when nonzero. None
of this needs the first arrows to kill Z: only the quadratic condition(3)
is used to obtain the constant F block.

Subtracting characters in(1) gives C2=A+V+2P+2D, dimension24. For rank8,
C4=V+3P+D has dimension20; acyclic cancellation retains kernel A+D and
cokernel P, giving invariant rank16. For rank3, C4=V+3P+2D has dimension25;
the removed Z->Y complex is onto with kernel D, so the active kernel is A,
cokernel P, and invariant rank21. The direct permanent D in(5) must NOT be
dropped in stating equivalence to the original obstruction problem.

## 4. Entire affine-family consequence and scope

In the rank3 case the quotient has the same five-dimensional D in its
kernel for every negative quadratic perturbation. Over C[[z1,z2,z3]],
where the z_i are formal coordinates on Sym²W, the original nine-dimensional
image block remains invertible because its constant term is invertible.
Over the fraction field, restoring that block gives original rank at most
9+(32-5)=36. All37-minors are polynomials in z1,z2,z3. Since the polynomial
ring injects into the formal power-series ring and its fraction field,
these minors are identically zero. Hence the original41-to-37 map has rank
at most36 at EVERY point of the affine family Q+Sym²W, including points
where the nine-dimensional image block is no longer invertible. We do
not extend formal invertibility to those points; polynomial identities
supply the rank conclusion there.

No coefficient or point in this family is selected or evaluated. Surjectivity
somewhere in this affine family would force rank8, but is not supplied here.
Nothing is asserted about quadratic directions outside this affine family.
The pure V direction remains outside the theorem: there NC4/I4 has
character D rather than zero, so the key implication(3) is not available
from endpoint equality. The no-compatible-line alternative remains open.
The source/pair ledger and original proof repair remain unchanged.

## Reproducible support

verify.py checks exact source bytes, both endpoint-quotient character
patterns, the restriction-rank dichotomy, and bounded synthetic subpencils
with NONZERO first arrows into the exceptional six-dimensional middle space
but zero second composites. It then verifies constant-block cancellation
coefficientwise in multiple formal variables. These tests support the new
weaker-hypothesis deduction, not an actual-source numerical experiment or
a replacement for its universal proof. No proof-assistant certification is
claimed.
