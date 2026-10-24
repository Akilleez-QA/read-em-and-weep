# The rank-four reverse-adjacent plateau (3,2) is impossible

## 1. Result and precise scope

Retain the actual geometric hypotheses, fixed physical representation marking,
and original parameter line in the four complete immutable originals pinned
in `INPUTS.json`. The actual second fundamental form cannot have generic rank
four and ordered maximal consecutive rank-four plateau lengths `(k,l)=(3,2)`.

The order matters: the central bundle is the actual rank-seventeen E, and its
annihilator is the different rank-thirteen Q*. This proof does not exchange
their presentations and does not assume the source-Z splitting of E. In
particular l=2 does not force that splitting. The result excludes exactly
this ordered rank-four stratum. It does not exclude the other rank-four
profiles, prove generic rank at least five, prove square-map surjectivity or
full-adjoint invertibility, or repair the original theorem.

There are no actual coefficients, parameters, jets, matrices, actual-instance
rank calculations, or local-model experiments. No historical candidate
enumeration is imported or rerun. The only finite search is a new, forced
401-pair domain of abstract rank-five endpoint splitting data. No rank-four
quotient splitting is enumerated or assigned.

## 2. Actual inputs and geometric assumption ledger

Work over C with G=SL2(F5), the binary icosahedral group, on the original
physical parameter line T=P(W*). Give O(1) its standard determinant-one
linearization. Fix the genuine irreducibles

    1, W, A=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W,
    P, W', V,
    dimensions 1,2,3,4,5,6,4,2,3.

The center-odd irreducibles are W,S4,T6,W'; the remaining five are even.
All nine are self-dual. In particular A and V are distinct physically
marked three-spaces. G is perfect, so its only one-dimensional
representation is trivial.

The actual geometric inputs are the saturated, locally free inclusion and
its two actual equivariant presentations:

    0 -> E -> H tensor O -> Q -> 0,
    rank E=17, degree E=-54, dim H=30,
    rank Q*=13, degree Q*=-54,

    0 -> E  -> M3  tensor O(-1) -> M4  tensor O -> 0,
    0 -> Q* -> M3* tensor O(-1) -> M2* tensor O -> 0,

    M2=A+2V+3P+4D,
    M3=3W'+3S4+6T6,
    M4=2V+4P+3D,
    H=2A+2V+2P+2D.

The last equality is the actual Koszul middle-cohomology character
H=W M3-M2-M4, not identification with the coefficient space M3.
The source assumptions include that E and Q* have no nonzero constant
subbundle and span their constant ambient spaces. All actual Gauss stages
are saturated and equivariant, with the regular derivative/kernel properties
used below. These actual-geometric statements are retained premises, not
facts established by the arithmetic checker.

Write chi_G for equivariant Euler characteristic. The actual presentations
and the physical McKay identities give, in particular,

    chi_G(E(2))   = -V,
    chi_G(Q*(2)) = -1-2A-D-V,
    chi_G(Q*(3)) = -2W-S4+T6.                         (1)

At every integer twist, the checker uses the presentations themselves,
not only these three special values. For a representation R, put

    e(R,t)= R Sym^t W                  if t>=0,
            0                         if t=-1,
           -R Sym^(-t-2) W             if t<=-2.

Then

    chi_G(E(t))=e(M3,t-1)-e(M4,t),
    chi_G(Q*(t))=e(M3,t-1)-e(M2,t),
    chi_G(Q(t))=e(H,t)-chi_G(E(t)).                  (2)

The last formula uses the actual ambient exact sequence. These formulas
also verify chi_G(Q*(t))=-chi_G(Q(-t-2)), as expected from Serre duality.
There is no determinant-character correction because det W=1, and the
representation dual can be omitted because every irreducible is self-dual.

## 3. The hypothetical plateau and endpoint persistence

Suppose the excluded ordered plateau exists. Its actual saturated chain is

    F0 < F1 < F2 < F3 < F4 < F5,
    F3=E,     rank Fi=5+4i.                         (3)

Write Li=Fi/F(i-1), 1<=i<=5. At each interior stage, the derivative kernel
is F(i-1), the saturated forward transform is F(i+1), and the derivative
induces a regular, generically invertible map

    Li -> L(i+1)(-2),     1<=i<=4.                 (4)

No equality of the two endpoint derivative ranks is assumed. In particular,
the endpoints' derivative ranks need not be four, nor one.

Every Fi with i<5 has no nonzero constant subbundle. Below E this follows
by inclusion. Above E, any such subbundle lies in each derivative kernel
and propagates backwards to E. Every Fi with i>0 spans H: a proper constant
span below E contains each forward transform and hence E. Therefore the
reversed annihilator flag

    Di=F(5-i)^perp,     0<=i<=5,
    D2=Q*,             rank Di=5+4i,

has the same interior properties. Here D0=F5^perp is the upper endpoint
annihilator, not an assumed copy of the lower endpoint F0.

Universal section persistence, including at each endpoint, gives

    H0(Fi(d))=H0(Di(d))=0    for d>=0 and i+d<5.    (5)

For completeness, saturate a nonzero section into a line O(-s) in Fi,
where 1<=s<=d. This line remains saturated in the constant ambient because
both successive quotients are locally free. A degree-s polynomial vector
reaches its constant coefficient span after at most s derivatives: the
change from derivatives to coefficients is triangular with nonzero
factorial diagonal. Its successive saturated transforms are contained in
F(i+1),...,F(i+s). At i=0, the first inclusion follows from

dF0 subset F1 tensor Omega,

since F0 is the derivative kernel at F1. All later inclusions follow from
the interior transform identities. When i+s<5 the resulting nonzero
constant span contradicts the preceding no-constant-subbundle property.
The same argument applies to Di. No actual section or jet is chosen or
evaluated in this universal proof.

Consequently every ordinary degree of F0 and D0 is at most -5. Write

    a=degree F0,     b=degree F5=degree D0.

Both endpoints have rank five, so a,b<=-25. All stages are center-even,
and an equivariant line bundle has its standard linearization up to a
one-dimensional character. Since G is perfect, all stage determinant
degrees are even. Thus

    a<=-26,     b<=-26.                            (6)

Two further consequences of (5) that will be decisive are

    H0(F2(2))=0,     H0(D1(3))=0.                 (7)

## 4. Exactly two endpoint degree alternatives, with no ramification

Put ci=degree Li. Taking determinants of (4) gives

    c(i+1)=ci+8+delta_i,    delta_i>=0.             (8)

Each delta_i is the degree of an effective G-invariant divisor. The
projective group is A5. Finite point stabilizers on P1 are cyclic, so the
possible orbit sizes are 12,20,30,60. Hence every nonzero delta_i is at
least 12. Zeros at special parameters have not been discarded.

The central and total degree equations are

    -54=a+3c1+24+2delta1+delta2,
    b=a+5c1+80+4delta1+3delta2+2delta3+delta4.

Eliminating c1 yields the exact identity

    2a+3b=-150+2delta1+4delta2+6delta3+3delta4.      (9)

Set a=-26-2u and b=-26-2v, with u,v>=0. Then (9) becomes

    4u+6v+2delta1+4delta2+6delta3+3delta4=20.       (10)

The smallest possible nonzero defect contribution is 2*12=24, larger
than 20. Thus all four defects vanish. The remaining equation is
2u+3v=10, whose only nonnegative integer solutions are (5,0) and (2,2).
The full degree alternatives are therefore

| Case | (a,b) | (c1,c2,c3,c4,c5) | (degree F0,...,degree F5) |
|---|---|---|---|
| I | (-36,-26) | (-14,-6,2,10,18) | (-36,-50,-56,-54,-44,-26) |
| II | (-30,-30) | (-16,-8,0,8,16) | (-30,-46,-54,-54,-46,-30) |

Every map (4) is now an isomorphism. Set B=L3, a genuine rank-four
bundle of degree 2 in case I and degree 0 in case II. Then

    (L1,L2,L3,L4,L5)=(B(-4),B(-2),B,B(2),B(4)).    (11)

These are derivative-induced associated-graded identifications. They do
not split the filtered flag, its connection, or its embedding in H tensor O.

## 5. Eliminate the quotient without enumerating it

Exact-sequence additivity in equivariant K-theory gives

    [E]-[F0]=[B(-4)]+[B(-2)]+[B],
    [Q]-[D0*]=[B(2)]+[B(4)].                      (12)

The second equality uses the actual quotient of F5 in H tensor O, which
is D0*, and the two graded blocks above E. Twist it by -6. Its right
side is exactly the first two summands in the first equality. Subtraction
therefore gives the exact class identity

    [B]=[E]-[F0]-[Q(-6)]+[D0*(-6)].                (13)

For any proposed pair of endpoint splittings, define its forced Euler
function

    C(t)=chi_G(E(t))-chi_G(F0(t))
         -chi_G(Q(t-6))+chi_G(D0*(t-6)).           (14)

An actual pair must satisfy C(t)=chi_G(B(t)). Substitution back into the
second equality of (12) gives the necessary identities

    C(t+2)+C(t+4)+chi_G(D0*(t))-chi_G(Q(t))=0.      (15)

We use (15) only at t=0 and t=1. No claim that these necessary conditions
alone construct B or a flag is required.

The two exact sequences relevant to (7) are

    0 -> F2 -> E  -> B      -> 0,
    0 -> D1 -> Q* -> B*(-2) -> 0.                 (16)

For the second sequence, D2/D1=(F4/F3)*=L4*=B*(-2).
This is where the ordering and the distinct Q* presentation are essential.
By (7), Euler additivity, and Serre duality, the following two virtual
characters must both be genuine:

    C_pr=C(2)-chi_G(E(2))
      =-chi_G(F2(2))=H1(F2(2)),

    C_du=-C(-3)-chi_G(Q*(3))
      =-chi_G(D1(3))=H1(D1(3)).                  (17)

In the second line chi_G(B*(1))=-chi_G(B(-3)) was used. There is no
assumption of surjectivity on sections, no omission of an H1 term, and
no identification of Q* with E.

## 6. A forced finite endpoint domain

Equivariant Birkhoff splitting may be used for bundle cohomology. Its
existence follows by splitting the canonical slope filtration and
averaging over the finite group. It need not be horizontal. Write an
endpoint as a sum of irreducible blocks R O(e).

Every endpoint here has rank five, total degree d, and every ordinary
line degree at most -5. If one ordinary line has degree e, the other
four sum to at most -20. Therefore

    d+20 <= e <= -5.                              (18)

Every coefficient R has dimension at most five, and its central parity
must equal e modulo 2. Consequently the full domain consists of the
nonnegative block multiplicities n(e,R) satisfying

    sum n(e,R) dim R = 5,
    sum e n(e,R) dim R = d,
    d+20<=e<=-5,    parity R=e modulo 2.            (19)

There are no additional cutoff parameters. Equation (19) is a complete
necessary domain, not a list taken from the earlier source enumeration.
The number of splittings for each d is

| Endpoint degree d | Forced window | Number |
|---|---|---:|
| -36 | [-16,-5] | 44 |
| -30 | [-10,-5] | 15 |
| -26 | [-6,-5] | 4 |

The program reproduces each list in two independent ways: choosing
irreducible blocks by rank and degree, and choosing five ordinary line
degrees first before decomposing the coefficient space of each degree.
The complete lists, not just their counts, are in `RESULT.json`.

Thus case I has 44*4=176 pairs; case II has 15*15=225 pairs. For every
pair, (14)-(15) are evaluated both by the physical McKay recurrence and
independently by exact conjugacy-class characters in Q(sqrt5). In the
first domain exactly four pairs pass (15); in the second exactly ten do.
Their complete explicit list follows. They are only formal survivors
of necessary equalities, not actual bundles or maps asserted to occur.

## 7. All fourteen exact-Euler survivors fail persistence positivity

The following tables use direct-sum notation. Each row permits both
listed F0 alternatives, accounting for two endpoint pairs per row.

### Case I: four survivors

The lower endpoint is one of exactly

    F0=O(-10)+O(-8)+V O(-6),
    F0=W O(-9)+V O(-6).

For either lower alternative the two upper alternatives give

| D0 | C_pr from (17) | C_du from (17) |
|---|---|---|
| O(-6)+(W+W') O(-5) | D+3P | 2W+T6-W' |
| O(-6)+S4 O(-5) | -1+2D+2P | 2W+T6-W' |

The first row has negative W' multiplicity in C_du. The second has both a
negative trivial multiplicity in C_pr and a negative W' multiplicity in C_du.
Thus none of the four pairs can occur.

### Case II: ten survivors

The lower endpoint is one of exactly

    F0=O(-10)+S4 O(-5),
    F0=D O(-6).

For either lower alternative the five upper alternatives give

| D0 | C_pr from (17) | C_du from (17) |
|---|---|---|
| O(-10)+(W+W') O(-5) | 3P+V | W+S4+T6-W' |
| O(-10)+S4 O(-5) | -1+D+2P+V | W+S4+T6-W' |
| W' O(-7)+O(-6)+W' O(-5) | -1+D+2P+V | 2W+T6 |
| (1+P) O(-6) | -1+D+2P+V | 2W+T6 |
| D O(-6) | -1+D+2P+V | W+S4+T6-W' |

The first row has negative W' multiplicity in C_du. Every other row has a
negative trivial multiplicity in C_pr. This excludes all ten pairs.

The two columns are the forced characters of H1(F2(2)) and H1(D1(3))
from (17); P remains the fixed four-dimensional irreducible throughout. Their ordinary dimensions
are respectively 17 and 8 in case I, and 15 and 10 in case II. They
are positive dimensions, so mere numerical cohomology would not detect
the negative irreducible multiplicities.

Every actual endpoint pair would belong to the complete domain (19),
satisfy (15), and have genuine characters (17). The 401-pair test and
the explicit fourteen survivors show these requirements are incompatible.
This proves the stated ordered (3,2) exclusion.

## 8. Reproduction, audit boundary, and retained dependencies

Run `python3 verify.py` and `python3 -O verify.py` from any directory.
Both outputs must agree byte for byte with `RESULT.json`. The program
uses only the Python standard library and contains no Python assertion
whose removal under optimization could disable a check.

The checker authenticates all four retained originals, independently
checks exact physical characters, derives (9) symbolically, derives the
two endpoint alternatives and finite windows, reproduces both endpoint
enumerations, checks all 401 endpoint pairs and all fourteen final
character contradictions, and rejects mutations of the recorded
numerical/character contract. The latter are contract controls, not a
claim of proof-assistant verification or a substitute for the written
geometric argument.

The four sources are used as follows:

1. ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: actual E and Q*
   presentations, physical marking, legitimate equivariant splitting,
   and the arbitrary-rank section-persistence argument. Its historical
   28-type enumeration and source-Z conclusion are not used.
2. RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md: the actual ambient
   representation, generic-rank-independent regular derivative,
   saturation and kernel properties, and determinant parity. Its
   rank-two numerical conclusion is not used.
3. GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md: only the invariant-divisor
   orbit-size gap and regular graded-isomorphism consequence. Its
   rank-one-endpoint arguments and rank-two exclusions are not used.
4. POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md: the original actual ambient
   inclusion and geometric identification. No maximal-rank conclusion
   is imported.

Source hashes authenticate bytes, not all transitive geometric
prerequisites. The theorem is conditional on the actual-geometric ledger
in Section 2. The related (2,3) and (3,3) exclusions are not logical
inputs, and the unequal primal and dual roles remain intact throughout.
