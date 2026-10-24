# Independent whole-proof review: forward length three

## Verdict and reviewed object

**PASS, conditional on the explicitly imported foundational premises A1–A4.**
I find no gap in the exclusion of a maximal generic rank-three plateau with
forward length `l=3`, uniformly for every allowed `k>=1`. This is a review of
the geometry and the arithmetic together, not an arithmetic-only approval.

Reviewed on 2026-10-24 UTC:

- `PROOF.md`, SHA256
  `d16a3186e5d922fe55206c7f139e152fb9153614be71e2a172f47b801c44c40c`.
- The four foundational source copies identified by `INPUTS.json`, at
  repository commit `db51525015bb7c5e825833d550d08dedf6f6ea96`.
- `INPUTS.json`, SHA256
  `f365a59d991e90ebec228657929fc9a4c8d5d9faef4f9da03e6fa01a92a443df`;
  the independent checker freezes this manifest as well as the proof.
- The displayed claims were independently checked by
  `review/verify_independent_mckay.py`, which does not import or execute the
  author's character checker or any historical enumeration.

I first audited the underlying mathematical argument and its sources, then
reviewed the frozen final proof. I did not read the retained earlier reviewer
verdict. The independent calculation uses integer multiplicities in the
affine-E8 McKay graph, rather than the author's nine-class arithmetic.

The verdict does not independently reprove the actual geometric
presentations, their physical linearizations, or `H0(E(1))=0`. Those are
declared imports, not conclusions of the representation check. In particular,
the constant ambient space is the original thirty-dimensional `H`, not `M3`.
The actual inclusion and connection remain fixed throughout.

## 1. Persistence, including the lower endpoint

The section-persistence argument works at all indices used in the proof.
For a section of `Fi(d)`, saturate its line to `O(-e)` in `Fi`; then it is
saturated in `H O` because both successive quotients are locally free.
Here `e<=d`; negative `e` cannot occur for a line in a trivial bundle, and
`e=0` would already be a forbidden constant subbundle. A polynomial lift
of degree at most `e` and its first `e` derivatives span its constant
coefficient space: the change of generators is triangular with nonzero
factorial diagonal. Linear dependence among coefficient vectors does not
affect that span statement. Saturation extends it across the missing
affine parameter and across ramification.

The required inclusions are `dFi subset Fi+1 tensor Omega`, not an assertion
that the lower endpoint has derivative rank three. At index zero this
inclusion follows because `F0` is the derivative kernel of `F1`.
For `i<=k`, absence of constants follows from `Fi subset E`; for `k<i<m`,
a constant subbundle propagates backward through the exact interior
kernels to `E`. Thus the lower endpoint also has no constants, although
the proof initially states the interior version. This supplies precisely
the endpoint case needed for `K` when `k=1`.

Consequently `i+d<m` implies the asserted vanishing. The dual argument
uses the same facts for the reversed annihilator flag and `Q*`. Positive
Euler multiplicities imply actual sections because `H1` is genuine;
therefore the finite range follows without assuming any `H1` vanishing
at twist three.

## 2. Forced source splitting and the full image

Under `l=3`, `H0(E(2))=0`, so all degrees are at most `-3` and
`H1(E(2))=V`. The cohomology contribution of an irreducible block
`R O(-j)` is exactly `R Sym^(j-4) W` for `j>=4`.

- At `j=4`, irreducibility of the total budget forces precisely `V`.
- At `j=5`, central parity makes the cost at least four-dimensional.
- At `j=6`, only a scalar coefficient could fit dimension three, but it
  contributes `A`, not `V`.
- At `j>=7`, the cost already exceeds dimension three.

This is a dimension and irreducibility argument, not the historical
source-splitting enumeration. The remaining `-3` coefficient is
`Wp+2T`, using `W V=T`. Equivariant splitting is legitimate by the
invariant slope filtration and averaging, and is used only as a bundle
splitting, never as a horizontal decomposition.

For `K=E^-`, persistence gives `H0(K(3))=0`; rank fourteen then gives
`deg(K)<=-56` and `deg(I)>=11`. The section injection `U -> H0(I)` is
the one from the actual quotient sequence. Generic generation of
`Sbar(1)` follows from the full source `E(4)`, not from the cubic source
alone. Every degree of `Sbar` is therefore at least `-1`. A negative
irreducible block can receive a source projection only if it is
`V O(-1)`, which would consume rank three and contradict the section
injection. Thus the nonnegative-degree conclusion is valid without any
assumption about the rank of the cubic subimage.

## 3. Negative transpose and the uniform dual envelope

Differentiating the annihilator pairing proves the negative-transpose
identity for the two actual second fundamental forms. The annihilator
of the dual sheaf kernel is the **saturation** of the primal image.
This gives `Sbar=(Q*/Kd)^*(1)` and does not identify the unsaturated
image with its saturation prematurely.

Write the first four reversed-dual stages as
`G0=L0`, `G1=Kd2`, `G2=Kd`, `G3=Q*`. Their ranks are `4,7,10,13`.
With `B=G3/G2=Sbar*(1)`, the two actual interior derivatives give

    G2/G1 -> B(-2),
    G1/G0 -> (G2/G1)(-2) -> B(-4).

Each first arrow is generically injective between rank-three vector
bundles and therefore injective as a sheaf; its torsion cokernel is
allowed. There are no poles. Since `3<k+3` for every `k>=1`, persistence
gives `H0(G0(3))=0`. The two quotient sequences consequently imply

    H0(G2(3)) <= H0(B(1))+H0(B(-1)).

Substitution of `B=Sbar*(1)` gives the two terms stated in the proof.
Taking Euler characteristics in `0 -> G2(3) -> Q*(3) -> B(3) -> 0`
then gives exactly inequality (5), in coefficientwise representation
order. In particular, `k=1` is not exceptional: the argument neither
differentiates the lower endpoint as a rank-three stage nor uses a
condition beyond the upper endpoint.

## 4. Exhaustiveness of the four shapes

The formula for `Phi_e` has the correct twists and Serre-duality sign.
The central parity of a coefficient at degree `e` is `(-1)^(e+1)`.
Every irreducible direct summand of `Sbar` receives a nonzero projection
from the full source because that source is generically surjective.

The only rank partitions of three into irreducible coefficient ranks
are `1+1+1`, `3`, and `2+1`. Scalar degrees `1,3` are excluded by both
source Hom tests, so scalar degrees are odd and at least five. Three
scalars supply no positive `T` to the envelope. An irreducible triplet
has only six or twelve sections at degrees one or three, and a
nonpositive envelope at all higher eligible degrees. This leaves only
the doublet-plus-scalar case.

For a doublet of degree at least four, the envelope has no positive
`T`, again impossible. At degrees zero and two, both full-source Hom
tests exclude `W`, leaving `Wp`. The resulting complete signed budgets
are `2W+Wp+2S+T` and `2W+Wp+S`. The scalar degree-five case fails the
degree lower bound. The dimensions bound the remaining scalar degree
by 25 or 15; these are proved bounds, not empirical search limits.

The two finite lists of odd scalar degrees, together with the section
inclusion and coefficientwise budget, leave exactly
`(a,b)=(0,15),(0,17),(0,19),(2,7)`. The independent checker recomputes
the entire necessary test on both fixed lists. This does not enumerate
historical source, dual-source, quotient, or negative-tail records.

## 5. Invariant defect and the terminal contradiction

`I` and `Sbar` are rank-three locally free sheaves, so the determinant
of their inclusion defines an effective divisor whose degree is their
degree difference. Equivariance makes this divisor invariant. The four
shapes give defect bounds `4,6,8,0`; every positive invariant divisor
has degree at least twelve. The projective `A5` stabilizer argument
justifies that lower bound independently of any rank-two result.
Thus the actual full image equals its saturation in every case.

The full signed values of `chi_G(K(4))`, in the displayed quotient order,
are independently reproduced as

    2V+P;
    -A+2V+D;
    -1-A+2V+P;
    2V+2P.

The negative coefficients in the middle two cases cannot be discarded;
they are retained in both the check and its output. For the particular
`V` coefficient, genuineness of `H1` forces at least two copies in
`H0`. Since every degree of `K` is at most `-4`, `H0(K(4))` is exactly
its degree `-4` coefficient space. Hence a direct top summand
`2V O(-4)` exists without classifying any lower-degree tail.

The derivative of `K` lands in `(E/K)(-2)` because `K` is the actual
kernel of the derivative of `E`. In each of the four cases the entire
equivariant Hom from one `V O(-4)` to that target is one-dimensional:
the doublet term contributes zero and the scalar term contributes one.
Thus the two-dimensional multiplicity space has a nonzero constant
kernel vector, yielding a direct `C=V O(-4)` killed by `beta_K`.

This does not yet assume that a chosen splitting is horizontal. Rather,
the internal derivative of `C` now lands in `(K/C)(-2)`, whose every
degree is at most `-6`. Every underlying line-bundle Hom from `O(-4)`
to this target is zero. Therefore `C` really is horizontal. It is
saturated in the original ambient bundle, since both `K/C` and `H O/K`
are locally free. The characteristic-zero Grassmannian argument then
makes it a constant subbundle, contradicting `deg(C)=-12`.

## Independent reproduction and limits

From the packet directory:

    python3 review/verify_independent_mckay.py
    python3 -O review/verify_independent_mckay.py

Both give the single checked-in `RESULT-INDEPENDENT.json`, identically;
normal and optimized outputs were compared byte-for-byte before delivery.
The checker makes 223 fixed requirements, uses symmetric powers only
through degree 25, verifies the frozen proof hash, and authenticates
the four local source copies against their manifest byte lengths,
SHA256 hashes, and Git blob identities. It also runs from another
working directory because all paths are relative to its own location.
Those hash checks establish local source identity, not independent
online authentication of the repository commit.

No actual coefficients, selected parameters, points, jets, instance
matrices, ranks, or scans were constructed. No external state was
changed. No rank-four lane was used. This review supports only the
dependency-shortening alternative for the three `l=3` entries; it does
not add exclusions to the separately established nine-profile result
or establish any new rank bound or solution of the original repair.
