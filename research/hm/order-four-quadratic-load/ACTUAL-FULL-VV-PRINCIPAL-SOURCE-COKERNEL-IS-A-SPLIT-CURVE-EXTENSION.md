# The actual full VV principal source cokernel is a split curve extension

## Scope

This is an exact source-division theorem, not an evaluation of the actual
next-division residual. Unlike the Cartan-only twelve-point criterion, it
retains the spin component of the positive VV arrow. It still omits the
mixed-form companion of the full U-source arrow. All channel scalars are
nonzero and may be absorbed into the source identifications in this theorem.

Let S=P(U) times P(W), D the actual smooth integral bicubic, and P the
actual four-dimensional Cartan space. Use the fixed decomposition
U tensor wedge^2 V = Spin(U) plus P. The principal VV source map is

    Phi_full: U O(-2,0) plus A O(0,-1)
           --> (Spin(U) plus P) O,
    (u,z) |--> (M(r^2)u, Abar(r^2,u)+p_C(w,z)).          (1)

Here Spin(U) is identified with U by the fixed nonzero Clifford marking;
any fixed nonzero normalization of its M term gives the same statements.
The actual c-column p_C=-f(ell z) is retained. No source coefficient or
actual point has been assigned a numerical value.

## 1. Exact cokernel

Eliminate the fiberwise injective c-column using its marked sequence

    0 --> A O(0,-1) --> P O --> O(0,3) --> 0.

The remaining map is

    U O(-2,0) --> U O plus O(0,3),
    u |--> (M(r^2)u, ell_F(u)),                        (2)

where ell_F is the positive polar of the actual bicubic F, with its fixed
nonzero constant retained. In particular ell_F(r) is a nonzero constant
multiple of F by Euler's identity.

The null Clifford endomorphism M(r^2) has image the tautological line
O(-1,0) inside U O, and fits into the everywhere-exact sequence

    0 --> O(-3,0) --> U O(-2,0) --> O(-1,0) --> 0.      (3)

Its first arrow is multiplication by r, up to the fixed scalar. On this
kernel, the second component in (2) is exactly multiplication by a
nonzero constant times F:

    O(-3,0) --F--> O(0,3).

It is injective as a sheaf since F is a nonzero divisor on S. Consequently
(1) is sheaf-injective, even though its fiber rank drops along D. Its
cokernel C fits into

    0 --> O_D(0,3) --> C --> O(1,0) --> 0.              (4)

This follows by quotienting (2) first by the image line in (3), whose
quotient in U O is O(1,0). Thus the torsion in C is supported on the whole
actual cubic, not merely on its twelve ramification points.

## 2. Unique equivariant splitting

Since the last term in (4) is locally free, its extension class lies in

    Ext^1(O(1,0), O_D(0,3)) = H^1(O_D(-1,3)).

Use the divisor sequence

    0 --> O(-4,0) --> O(-1,3) --> O_D(-1,3) --> 0.

Product-line cohomology gives H^i(O(-1,3))=0 for all i,
H^2(O(-4,0))=0, and H^1(O(-4,0))=Sym^2 U^*=V. Hence

    H^1(O_D(-1,3))=0,
    H^0(O_D(-1,3))=V.

The extension splits. Its splittings form a torsor for V. Averaging a
splitting over the finite group gives an equivariant splitting, and V has
no invariant vector, so that splitting is unique equivariantly:

    C = O(1,0) plus O_D(0,3).                           (5)

This uniqueness uses the fixed equivariant endpoint identifications of
(4); it is not a chosen nonequivariant projection in an arbitrary frame.

## 3. Global division at the actual residual degree

Twist the exact sequence defining C by O(4,3). Its source is

    U O(2,3) plus A O(4,2),

which has no H^1. Therefore the global full-VV source image is precisely
the kernel of the quotient map

    H^0((Spin(U) plus P) O(4,3))
       --> H^0(O(5,3)) plus H^0(O_D(4,6)).              (6)

This map is surjective. The two obstruction spaces have dimensions 24 and
27: the latter follows from

    0 --> O(1,3) --> O(4,6) --> O_D(4,6) --> 0.

The complete dimension check is 69 -> 120 -> 51 -> 0, with injective
first arrow. Thus a principal VV residual can be removed by source terms
if and only if its two classes in (6) vanish. This is a stronger condition
than the Cartan-only twelve evaluations. It does not assert that an actual
candidate residual satisfies it. Uniqueness of source corrections here is on the positive cone; ambient polynomial representatives still have q0-multiple ambiguity.

Restoring the entire monad source also adds the b-channel mixed companion
B Q, and the other form-sector equations remain. No fourth Bockstein value
or global primitive follows from (6).

## Dependencies and verification

The marked cubic quotient and polar identification are those of
ACTUAL-RAMIFICATION-TESTS-CONTROL-GLOBAL-PRINCIPAL-CARTAN-SOURCE-DIVISION.md.
The full A=spin+Cartan decomposition is fixed in
ACTUAL-POSITIVE-ATIYAH-DERIVATIVE-HAS-A-SURJECTIVE-P4-TENSOR.md.
Actual smoothness and integrality are proved in
ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md.
The companion verifier checks the universal null-Clifford/Euler identities
with all bicubic coefficients free, and all line-bundle cohomology and
exact global dimensions. It performs no actual-instance evaluation.

Immutable dependencies: [principal Cartan criterion, PR688](https://github.com/Akilleez-QA/read-em-and-weep/blob/f8c2b20faa6ffef757791c98e281541a7b208397/research/hm/order-four-quadratic-load/ACTUAL-RAMIFICATION-TESTS-CONTROL-GLOBAL-PRINCIPAL-CARTAN-SOURCE-DIVISION.md), [marked full source decomposition](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-POSITIVE-ATIYAH-DERIVATIVE-HAS-A-SURJECTIVE-P4-TENSOR.md), and [actual bicubic](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md).
