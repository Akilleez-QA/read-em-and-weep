# The corrected actual third-neighborhood lift is square-zero

## Statement and fixed inputs

Let J3=(a h-q b)U_a-q^2 C_h be the ACTUAL global section of
B_(3Q)(8) constructed in
ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md.
Retain its fixed duality, physical-positive parity, and actual ambient bundle.
For every nonzero negative quadratic a and positive source h in D5,

    J3^2=0 on 3Q.

This holds for every choice of the indicated actual global primitive C_h.
It neither computes that primitive nor the subsequent fourth Bockstein.
All local calculations below are universal regular-pair identities, not
actual-instance coefficient tests. The zero-source cases may be taken with
zero primitives; no assertion about arbitrary unrelated lifts is needed there.

## 1. The scalar obstruction and its exact ideal

Since J3 restricts on 2Q to (a h-q b)U_a and U_a^2=0, trace-free
Cayley-Hamilton gives

    J3^2=q^2 chi I,       chi in H0(O_Q(12))_+.

Put f0=a^2 h, so J3|Q=f0 N. Changing any local trace-free lift from
2Q to 3Q by q^2 K changes chi by f0 tr(NK). The regular Serre pair
sigma=(f,g) gives

    im[tr(N-):B_Q(4)->O_Q(6)]=I_Z^2(6).

Thus the obstruction to a local square-zero extension is precisely chi
modulo f0 I_Z^2(6), not modulo I_Z or the reduced support. We prove that
this obstruction vanishes at every point of Q.

## 2. Vertex charts: the socle bound kills this obstruction

On either negative chart, the exact actual coherence theorem factors
U_a as a scalar multiple of a local actual square-zero first-normal lift
N_s or N_t of N. Consequently (a h-q b)U_a equals F N_s on 2Q,
where F|Q=f0. Use the positive binary cover of the vertex chart and its
harmonic lifting convention. Write a trace-free local lift

    N_s=L(n)+q L(T),

with no additional q^2 coefficient. Here n is the actual regular-pair matrix, starting in weighted matrix
degree eight, with regular initial pair (f3,g5); n8 denotes its leading
term. A matrix's degree is its diagonal
cover degree, with upper/lower degrees two less/more. The entries of T
are regular, possibly completed power series. Its components of degree
less than four vanish. Indeed the first-normal square equation in those
degrees says tr(n8 T_d)=0. In a regular pair of degrees (3,5), writing
T_d=[[x,y],[z,-x]], reduction of
2fgx+g^2 y-f^2 z=0 modulo f and g gives

    y=f y1, z=g z1, x=(f z1-g y1)/2.

In the physical-positive sector d is even. Regular entries require d>=-2; for d=-2,0,2, the degrees of
y1 and z1 are negative, so all entries vanish.
(The first harmonic square term has degree twelve and cannot enter here.)

The q^2 scalar square coefficient of this chosen lift therefore starts
in cover degree eight: its terms are T^2, the first harmonic product of
n and T, and the second harmonic product of n with itself. The first
and second harmonic products lower cover degree by four and eight.
The source h has cover degree four. The ACTUAL uniform vertex square-ideal
quotient has no piece of degree at least twelve, by the (3,5) regular-pair
square resolution in POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md §1.
Thus h times this scalar coefficient belongs to I_Z^2. The square coefficient
of F N_s is f0^2 times that coefficient, which belongs to f0 I_Z^2.

This argument applies to the full regular actual local lift: completion is
faithfully flat and the square-ideal quotient has finite positive-degree
support, so higher terms cannot change the conclusion. The even containment
descends from the binary cover by the characteristic-zero invariant projection;
f^2,fg,g^2 are even. No homogeneous truncation is identified with the full
actual C_h.

## 3. Conic charts: coherence supplies the missing divisibility

Near the conic, Q is smooth and the actual Serre pair is regular with ideal
(s,t). After a local invertible frame write sigma=(s,t) and
N=u sigma sigma^t J, retaining the invertible local determinant factor u.
The physical s,t, equation q and multiplier kappa are not renormalized.
Choose ambient lifts of this frame and of s,t. Write

    U_a=a N+q T_a mod q^2.

Exact coherence gives

    a T_b-b T_a=-(kappa/2){a,b}N.

With tau(v)=sigma v^t J+v sigma^t J and
D_a sigma=(-a_t,a_s), the family (kappa u/2)tau(D_a sigma)
has exactly this alternating difference. Its difference R_a from T_a
satisfies a R_b=b R_a for all quadratics. Taking a=s^2,st,t^2
and using that s,t is a regular sequence shows R_a=a R with R regular.
Equivalently the common rational quotient has no height-one pole, hence
extends across (s,t) on this smooth chart.

The first-normal square-zero identity implies tr(NR)=0. Multiplication
by the unit u does not change this trace kernel. The regular-pair
tangent sequence therefore gives R=tau(v) for a regular local vector v.
Hence

    T_a=tau((kappa u/2)D_a sigma+a v),
    T_a^2=a^2(kappa u+sigma wedge v)^2 I.

Here sigma wedge D_a sigma=2a, and tau(w)^2=(sigma wedge w)^2 I.
For a local extension with no q^2 term the scalar square coefficient of
(a h-q b)U_a is therefore a^4 h^2(kappa u+sigma wedge v)^2.
The cross term containing b is zero since tr(NT_a)=0 and N^2=0.
After division by f0=a^2 h this lies in I_Z^2: a belongs to (s,t)^2.
This proves the required local obstruction vanishing across the conic,
including the locus a=0. It does not assert a globally flat kernel line.

## 4. Global vanishing

The two kinds of charts cover Z; away Z the vertex-chart factorization still
applies wherever s or t is nonzero. Thus chi lies locally in f0 I_Z^2(6)
everywhere. Since Q is integral and f0 is nonzero, its quotients glue to a
global section of I_Z^2(6) in positive parity.

The pinned square-filtration sequence and cone closure give

    H0(I_Z^2(6))_+=0.

For clarity this also follows directly by homogeneous blocks: in O_Q(6)_+
the vertex cover degrees are 0,4,8,12. The square ideal has no degree0 or4
piece; its degree8 coefficient bundle is P4 O_L(-2), with no global sections.
The remaining degree12 pure-positive block restricts injectively to O_C(12),
so cannot vanish on the conic. These are the actual associated filtered ideal blocks: starting with the
lowest nonzero block gives the same injectivity argument even when the
vertex ideal is presented in inhomogeneous generators. This is not an
assumption that an arbitrary adjoint lift is homogeneous.
Therefore chi/f0=0, proving J3^2=0.

The input about H0 and the square-ideal blocks is also recorded in
ACTUAL-VECTOR-SHADOW-LOSES-THIRTEEN-LOWER-LIFT-DIRECTIONS.md and
ACTUAL-NEGATIVE-INVOLUTION-SECTOR-AS-SQUARE-QUOTIENT.md. The actual coherence
and its physical root factors are fixed in
ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md.

## Reproduction and scope

The companion verifier checks the universal conic tangent square and the
coherence identity, the square expansion including b, and all filtered
inequalities. It does not evaluate any actual coefficients, actual matrix
ranks, or fourth value. The theorem supplies a further property of the
existing global J3, not an explicit next primitive or a solution of the repair.
