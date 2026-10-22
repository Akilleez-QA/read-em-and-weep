# Actual ramification forces a nontrivial principal U-source correction

## Result and exact scope

Keep the actual Cartan identification f:Sym^3 W -> P=Sym^3 Wprime and the
full channel markings of UNIVERSAL-CARTAN-KOSZUL-MULTIPLIER-HOMOTOPY.md.
Write Abar(v)=Pi(A(v)):U->P for the Cartan a-channel.
For nonzero a in Sym^2 W* and positive trace-free h in D5, the next-division
principal c-column equation CANNOT be solved by a middle principal symbol S
which satisfies

    S(v,w) Abar(v)=0 on q0(v)=0,                       (1)

if the only source blocks retained are source-AA and source-A-to-U.
This holds for arbitrary polynomial S satisfying (1), not only the
Clifford-right-factor family. In particular adding the off-diagonal A-to-U
source block alone does not repair the preceding right-factor obstruction.

This is a restriction on an ansatz, not an obstruction to the actual next
division, whose existence is already proved. A successful construction must
allow a nonzero principal U-column balance (through other source/middle
terms), or use a middle realization outside the specified Cartan principal
comparison. No fourth value is inferred.

## 1. The actual bicubic as incidence of the two cubic curves

The Cartan four-space P has its fixed nondegenerate alternating apolar form.
It contains two rational normal cubic curves: the positive cubic
[r^3], r in Wprime, and the image under the actual conformally symplectic f
of the negative cubic [ell^3], ell in W. Denote their tangent two-planes by

    Lplus(r)=r^2 Wprime,       Lminus(ell)=f(ell^2 W).

Both are Lagrangian. The osculating hyperplane of the negative curve is

    Hminus(ell)=f(ell Sym^2 W)=(f(ell^3))^perp.

Use transported f coordinates when writing the last two spaces. The equation

    <r^3,f(ell^3)>=0                                  (2)

is a nonzero invariant bicubic. It is nonzero because both pure-cube curves
span P and f is invertible. The invariant bicubic line is one-dimensional,
so (2) cuts out exactly the ACTUAL divisor D of
ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md.
No normalization of that equation is needed for this identification of zero
schemes. The actual identification f, rather than an arbitrary isomorphism,
is essential here.

The same universal Clebsch map identifies im Abar(r^2) with Lplus(r).
Equivalently this is the Cartan projection of v tensor U at the null vector
v=r^2, retaining its nonzero marked common scalar.

## 2. Twelve simultaneous test fibers, used uniformly

The smooth genus-four curve D has two degree-three projections. Riemann--Hurwitz
gives degree twelve for each ramification divisor. Each is invariant. Every
point orbit in the product projects to an orbit of at least twelve points
on either icosahedral line. It follows that each ramification divisor is one
reduced twelve-point orbit, projecting bijectively to twelve distinct points
on BOTH lines.

The two ramification divisors are disjoint: if both differentials vanished
at a point, both partial derivatives of the smooth bicubic equation would
vanish there. This is also immediate from the tangent-plane description.
At ramification of D over the negative line, differentiating (2) in the
positive variable gives

    Lplus(r) subset Hminus(ell).                     (3)

At such a point Lplus(r) is NOT Lminus(ell). Otherwise r^3 belongs to the
Lagrangian plane Lminus(ell), making the negative partial derivative of (2)
zero too, contrary to smoothness. Therefore

    Lplus(r) contains a vector outside Lminus(ell).  (4)

For each fixed nonzero a,h, at least six of these twelve pairs have both
 a(w) and h(r^2) nonzero. Indeed a has degree two on the negative line, while
h(r^2) has degree four on the positive line and is not identically zero:
a trace-free quadratic vanishing on the null conic would be a multiple of q0.
The two projections are bijective on the orbit, so at most two plus four
pairs are excluded. This is a uniform orbit argument, not selection or
evaluation of any actual point or coefficient.

## 3. The principal c-column contradiction

Use any ramification pair in the nonempty locus just established, only as a
variable point of that orbit-level argument. In the compatible negative
binary notation put ell=i_w omega. The actual Clebsch c-channel is

    p_C(w,z)=-f(ell z),             z in Sym^2 W.

Its image is Hminus(ell), and the inverse image of Lminus(ell) is ell W.
The quotient P/Hminus(ell) is evaluation at w in f coordinates; denote this
functional by lambda_w. With the fixed Hamiltonian convention,

    lambda_w((delta_(D_a) C)_(VV))=2a(w) z(w).        (5)

This is the natural coefficient derivative identity used in
CLIFFORD-FACTORED-CARTAN-LIFTS-CANNOT-SOLVE-THE-PURE-C-COLUMN.md, not a
replacement of natural K pullback by a fixed-coordinate derivative.

With source-AA=Psrc and source-A-to-U=Qsrc, the necessary principal equation
for the ansatz is, modulo q0,

    S p_C-p_C Psrc-(a_m/c_m)Abar Qsrc
          -a h (delta_(D_a) C)_(VV)=0.              (6)

Apply lambda_w at the variable ramification pair. The Psrc term is killed
because its image is Hminus. The Qsrc term is killed by (3). By (4), choose
an abstract input z for which p_C(w,z) lies in Lplus but not in Lminus.
Then (1) kills the first term, whereas z(w) is nonzero. Equation (5) makes
the remaining term

    -2a(w)^2 h(r^2) z(w),

which is nonzero. This contradiction proves the theorem. No value or rank
of an actual HM matrix has been calculated. All scalar channel factors in
(6) are retained; the vanished Qsrc term is zero independently of its factor.
The proof does not need a classification or divisibility assertion for S.

## 4. What must be retained next

A source-A-to-U block also contributes a B Qsrc term in the full c-column,
which must be handled at its own bidegree. Even solving that additional term
would not remove the principal contradiction above under assumption (1).
Thus the appropriate next ansatz must retain the coupled U-source equations,
not impose that the middle Cartan symbol annihilates Abar on the cone.
Neither existence of an abstract division nor nonzero off-diagonal tensors
supplies the missing actual cochain. The complete divided class and fourth
Bockstein remain unresolved.

## Reproduction

The verifier checks the universal cubic apolar tangent-plane identities,
the Clebsch evaluation and Hamiltonian factor two, and the exact orbit/degree
arithmetic. Actual geometry is supplied by the pinned smooth bicubic theorem
and actual Cartan identification; it is not inferred from those symbolic tests.
