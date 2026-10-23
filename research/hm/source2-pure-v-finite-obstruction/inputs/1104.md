# The actual zero-fourth branch has a two-dimensional original-fifth gate

## Theorem and boundary

Retain the actual source2 nonzero pure-V compatible-radical hypotheses,
and assume that the unique quadratic fourth lift R of PR1025 is zero.
This includes the zero-alpha residual-large branch of PR1097. Then the
actual quotient fourth symbol is a canonical global sheaf map

    s4:P O_X(-4) -> J=I_Z(6),       X=P(A).                  (1)

It admits a homogeneous cubic lift C:P O(-4)->D O(-1), but this lift
is NOT unique. Its equivariant ambiguity is exactly one-dimensional.
The original fifth symbol on the surviving D sheaf satisfies

    iota beta5,M = -s4 L.                                  (2)

Consequently the original fifth vanishes identically if and only if s4
vanishes. The exact space containing this gate has dimension two.
In the fixed PR1031 conventions, a basis of its lift CLASSES is

    C1(a)=rho_D(a) R1(a),
    C2(a)=rho_D(a) R2(a).                                  (3)

Thus the first possible subsequent original obstruction really has a
nonzero two-dimensional equivariant naturality target. This theorem
does NOT prove its actual value nonzero or zero, nor that arbitrary
classes are realizable by an HM source. In particular symmetry and the
displayed equivariant target and naturality comparison do not force
fifth vanishing. Further actual identities could constrain this gate;
this result does not claim to exhaust them.

If this actual two-component fifth class is nonzero, the generic Smith
profile of the ORIGINAL 37-by41 block (not the full adjoint) is 33 unit factors, three t^2 factors and one t^5 factor, with
maximal-minor ideal (t^11). If it is zero, the final pivot is absent or
has exponent at least six. No upper-bound improvement is claimed here.
All assertions concern original sheaf pages and the generic direction;
additional specialized A kernels at second-rank-drop points are NOT
claimed exhausted by (2).

## 1. Actual pages and immutable inputs

INPUTS.json records six exact originals: PR1019, PR1025, the original
third-vanishing proof, PR1031 proof and universal model, and PR1097.
The essential new continuation uses PR1025 at
09f1377f83b027ca27eea0b3a9f40a1b92c6c466 and its exact endpoint maps,
not a replacement by an abstract equal-character complex. PR1031 is at
7150cf97eeebe473bcd7c61c1f968c73625d92ef; PR1097 is at
2ddc4b01fa96e7ce7830b093f4df5a29dafd2187.

Write M for the original two-term pencil q+tT_a, I=im j its actual
image subcomplex, and U=M/I. The actual image pencil is

    I=[D --t L_a--> P],        L_a(d)=[a d].

The quotient H0 at t=0 is A+P, its H1 is P, its first symbol is zero,
and its second symbol is [B,0], with B=-mu Lm, mu nonzero, and
m_a:A->D ordinary multiplication by a. B is injective as a SHEAF,
although its fibers drop rank at six axes. Hence after the second page
the quotient source SHEAF is P and the original source SHEAF is D.
The target is coker B. Original third vanishing and R=0 ensure that
these same original sheaves survive to the fifth page. Quotient third
vanishes because its unique quadratic lift is R=0.

The radical induces actual maps f0,f1 on U with

    f1 qbar=0,       f1 Tbar_a=L_a f0,
    ker f1=im qbar.                                        (4)

The last equality follows from the induced isomorphism H1(U)->P.
The target subquotient and its resolution are the exact ones of PR1025:

    J=im L/im B subset coker B,
    0 -> A O(-2) plus O(-5) --(m,kappa)--> D O(-1)
      --[L]--> J -> 0.                                    (5)

J is torsion-free. No split of the residual module is introduced.

## 2. The extra global correction actually exists

Fix the canonical quotient degree-zero P inclusion x0, identified with
I4 through the connecting map. Choose fixed equivariant linear inverses
on im qbar, so that polynomial corrections x1(a),x2(a) satisfy

    qbar x1=-Tbar_a x0,     qbar x2=-Tbar_a x1.             (6)

Their degrees are one and two. These corrections exist globally by the
quotient first and second vanishings on P. PR1025 identifies f0 x2 as
an equivariant quadratic lift of its quotient-third symbol and proves
that this quadratic lift is UNIQUE. Since R=0, it follows that

    f0 x2=0, hence f1 Tbar_a x2=0.                         (7)

This is stronger than only saying the class is zero modulo im B.
Equations (4) and (7) put Tbar_a x2 in im qbar for every direction,
as a polynomial family. A fixed equivariant inverse now gives a global
homogeneous cubic correction

    qbar x3=-Tbar_a x2.                                   (8)

Its next obstruction represents the quotient fourth. Applying (4) gives

    f1 Tbar_a x3=L_a f0 x3.

Thus its class lands in J and (1) is a global map, with cubic lift
C=f0 x3. No division by a direction-dependent minor is used.

The symbol, not this lift, is independent of correction choices.
One can subtract correction strings for the earliest difference between
two lift strings successively. A degree-one P difference contributes
the now-zero quotient third, later P differences contribute earlier zero
symbols, and a degree-two A difference contributes B times that
quadratic correction. These are exactly the lower-page target images.
Equivalently these are the ordinary page identifications of the actual
t-adic two-term complex. Since B is sheaf-injective, no extra A source
sheaf occurs. The inclusion J into coker B makes its resulting class
canonical in J as well. This argument does not claim that formation of
the page source commutes with specialization at the six axes.

## 3. Extending the original corrected-lift comparison

Use the actual inverse s:I4->P_h of q|P_h and fix p in I4. Choose actual
original corrections x=s(p), y,z with

    qx=p,       qy=-T_a x,       qz=-T_a y.

These are the corrections used in PR1025, globally equivariant in p
and polynomial in a. Their quotient classes are x0,x1,x2. The raw
identity (7) applies to this choice as well. The endpoint identification
iota:H1(M)->I4 therefore gives iota([T_a z])=0, so T_a z lies in im q.
Choose the additional actual correction w with

    qw=-T_a z.

Its quotient class is an x3 as in (8). For an original source d in D,
put p=L_a d, so qx=T_a d. The original successive lift string is

    d, -x, -y, -z, -w.

Every consecutive q/T term cancels. Its fifth representative is
-T_a w, while the quotient fourth at p is represented by Tbar_a bar w.
The two endpoint identifications give (2), including its minus sign.
All correction ambiguities are lower-page images; only im B remains
in the target. This proves a homogeneous sheaf identity of degree5,
not an uncorrected fifth coefficient of a chosen Schur block.

L is generically onto by the pinned universal rank theorem used in
PR1025. If beta5|D is identically zero, (2) forces s4 zero generically,
and then globally because J is torsion-free. Conversely s4=0 immediately
kills (2). This establishes the asserted equivalence without any actual
coefficient evaluation.

## 4. The cubic lift quotient and its exact basis

Twist (5) by four. Since H1(P2,O(k))=0 for every integer k and
H0(O(-1))=0, the equivariant global-section sequence is

    0 -> Hom_G(P,A tensor Sym2 A)
      -> Hom_G(P,D tensor Sym3 A)
      -> Hom_G(P,H0(J(4))) -> 0.                         (9)

These are plane-coordinate symmetric powers, not binary Sym powers of W.
The exact character multiplicities are respectively1,3,2. Thus the
cubic lift has a one-dimensional m-valued ambiguity; there is no kappa
ambiguity at this degree. This contrasts with the unique quadratic lift.

For an explicit whole-representation certificate retain PR1031's apolar
matrices Pi,E,G4 and the action rho. Define four cubic lifts

    C1=rho_D R1,   C2=rho_D R2,
    C3=R1 rho_P,   C4=R2 rho_P.

The coefficient matrices give C3=C2 literally and span a space of
dimension3. Hence they span the full middle term of (9). Set f_p=Ep in
Sym6 W and use unnormalized binary transvectants. The exact identity is

    C4(a)p-(1/4)C1(a)p=-(1/720) a (a^2,f_p)_4.           (10)

The right-hand side is m_a times a homogeneous quadratic A-valued
family. It is nonzero and spans the entire one-dimensional ambiguity
in (9). Consequently the classes of C1,C2 form a basis of (1).
The checker verifies (10) on all formal quadratic and P coefficients.

There is also a direct nonzero certificate for the ORIGINAL fifth
classes, retaining all quotient indeterminacy. Let N be the signed
maximal-minor row of the universal second symbol B=Pi(a^2 A), so NB=0.
The determinant-embedded original fifth rows are, up to the common
endpoint sign,

    H1=N L C1 L,       H2=N L C2 L.                       (11)

Each is a D-valued row of degree11 on P(A). They are independent. In
coefficient ordering by row entry and then p^i q^j t^(11-i-j), increasing
i and j, the two-row coefficient minor at indices1 and3 is

    20480 sqrt5 /27 !=0.                                 (12)

This is a minor of the complete coefficient vectors, NOT evaluation at
chosen directions or an actual source-instance rank. The checker also
verifies N L C4 L=H1/4 and N Lm=0, so the certificate explicitly kills
the cubic gauge. Nonzero formal representatives do not select the actual
fifth class. Its two coefficients remain entirely unselected.

## 5. Consequences and exact missing interface

Over the generic direction field the known original elimination gives
33 unit pivots and three pivots t^2. R=0 leaves a 1-by5 row of order at
least5. Its coefficient at order5 is the genuine beta5 just constructed.
Thus nonzero s4 is equivalent to the final exponent5 and maximal-minor
valuation6+5=11. If s4=0 the row has order at least6 or vanishes entirely.

The missing actual interface is a determination of the class of f0 x3
in the TWO-dimensional quotient (9), not a proof that a cubic correction
exists and not a choice of its one-dimensional gauge. The pinned earlier
identities determine neither coefficient. Equation (10) and the full
coefficient minor (12) demonstrate that representation theory, the
canonical J target and the original-fifth comparison do not annihilate
that quotient by themselves. No actual source occurrence, fifth value,
finite last exponent, global surjectivity, or full repair is concluded.

Run python verify.py and python -O verify.py to reproduce RESULT.json.
The six input digests, exact character multiplicities, cubic gauge,
whole original-row independence and generic valuation arithmetic are
checked without actual HM coefficients, parameters, points, jets or
source-instance matrices. The corrected-lift and sheaf-page arguments
above, rather than symbolic rank counts alone, supply the actual-map
transport. No public files are modified.
