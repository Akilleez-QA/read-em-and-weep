# A universal stationary section space fixes the conditional degree-eighteen coefficient kernel

## Statement and exact scope

The unpublished stationary-subspace audit was preparation, not a direct
dependency or independent review of this packet. This complete new proof and
its complete immutable direct originals require a new independent review
before publication.

The universal theorem below concerns only the fixed complex binary-icosahedral
section representation. Its application retains the full-positive triplet
branch, original t=0, original local delta=12, residual simultaneous rank-seven
k=2 geometry, and remaining original kernel K1, together with every complete
transitive actual-geometric assumption of the direct originals in Section 1.
Nothing here realizes or excludes K1 or any whole profile.

Put X=P(W*), parametrizing lines in W*, for the fixed faithful complex
determinant-one binary-icosahedral representation W of G=SL2(F5). This is not
the defining-characteristic representation over F5. Write

    H_n=H0(X,O(n))=Sym^n W,
    A=Sym^2 W, D=Sym^4 W,

and let V_alt and P denote the alternate three-dimensional and the
four-dimensional even irreducibles. Let Z12=D12 be the unique reduced invariant
orbit of length twelve. The notation Z12 avoids confusion with the actual
eleven-dimensional constant coefficient space called Z in the direct original.

The universal conclusions are a canonical torsion sheaf T of length twelve,
a canonical surjective map tau, and a canonical copy P0 of P such that

    H0(T)=V_alt+D+P,
    0 -> A18 direct-sum P0 -> H18 --tau--> H0(T) -> 0,
    A18=H18[A], P0=ker(tau|H18[P]).                    (U)

Here brackets mean entire isotypic subspaces. The unique invariant section
space of type A+P that is projectively stationary to first order along all of
Z12 is exactly ker tau. All such spaces are automatically basepoint-free.

In the retained actual K1 case, let V18 subset C* be the original dual
degree-eighteen curve's fifteen-dimensional coefficient span, and let

    j18:V18* -> H18

be its actual scalar-section injection. Let Lambda15=im j18, and let Lambda7
be the section image of its canonical constant seven-space projection. Then

    Lambda7=ker tau=A18 direct-sum P0,
    Lambda15=ker(pi_P tau)
            =A18 direct-sum H18[V_alt] direct-sum D18 direct-sum P0.       (A)

Here D18=H18[D], T_P=H0(T)[P], and pi_P:H0(T)->T_P is the canonical isotypic
projection. Define the original coefficient map by the transpose, using only
the canonical double-dual identification:

    b18=j18*:H18* -> V18**=V18.

Its exact kernel is therefore

    ker b18=im((pi_P tau)*:T_P* -> H18*) isomorphic to P*.                 (K)

This fixes the kernel as a subspace of the fixed coefficient domain H18*, not
merely its representation type. It does not identify V18 with V18*, determine
the whole coefficient map, select any coefficient tensor, or identify any
moving quotient with a constant space.

## 1. Two complete direct originals and assertion provenance

The complete direct originals are:

- PR1238 at d259230fbf7259e52db267c56203a29f221da5f0,
  research/hm/rankfour-profile11-triplet-seven-space-ramification/PROOF.md,
  retained in inputs/seven-space-ramification.md. Its complete bytes
  have SHA256 25388c411411f7304afc2dc7ad6695af5a931e852ba138c45cfb7a6f708d84e3.
- PR1206 at 252b967ebbfbea6fc0c6451a835ab2daff92d73b,
  research/hm/rankfour-profile11-triplet-shared-d/PROOF.md,
  retained in inputs/shared-d.md.

Both entire originals were freshly fetched through read-only connector calls
at these immutable commits, without line-range limits. Their complete UTF8
bytes equal the complete originals read for this proof. INPUTS.json records
exact lengths, SHA256 hashes, Git blobs, and immutable URLs. Full connector
responses are retained only in LOCAL-SOURCE-FETCHES.json, excluded from
publication and selected-only replay. No excerpt replaces an original, and
all complete transitive actual-geometric hypotheses remain assumptions.

The complete seven-space theorem supplies the actual constant inclusion C7
subset C, the representation C7=A+P, and the original dual curve
Y0=O(-18) subset C* O. Its projection by the genuine constant restriction
C*->C7* is an everywhere saturated line y7 with coefficient span all of C7*.
The projected scalar system has vanishing sequence (0,2,3,4,5,6,8) along the
entire reduced D12. In particular its projective differential vanishes there.
Its construction of C7 through the earlier perfect-pairing theorem is retained
as part of its complete transitive hypotheses, not reproved or replaced here.

The complete PR1206 theorem supplies the actual coefficient span

    V18=A+V_alt+D+P, dim V18=15,

of this same original Y0 in the genuine constant C* of dimension twenty-one.
Its T and C18 are our Y0 and V18; its V is our V_alt. Its section and source
gates remain assumptions. The alternate auxiliary primal degree-eighteen
curve is not Y0 and is not used here.

Every actual-geometric fact used in Sections 8-9 is expressly stated in these
two complete direct originals. The complete PR1237 splitting proof was read
to check directions during preparation, but supplies no additional premise
needed beyond the stated seven-space theorem. It is not an additional direct
dependency. Sections 2-7 below are proved independently in the fixed universal
section spaces.

## 2. Fixed characters, invariant orbits, and basepoint-free subsystems

The even representations factor through the fixed projective A5. Its five
conjugacy classes have sizes 1,15,20,12,12 and orders 1,2,3,5,5. Set
phi=(1+sqrt(5))/2 and phi_bar=1-phi. The fixed character table is

    class         1   2   3   5a       5b
    1             1   1   1    1        1
    A             3  -1   0   phi      phi_bar
    V_alt         3  -1   0   phi_bar  phi
    P             4   0   1   -1       -1
    D             5   1  -1    0        0.

The labels 5a and 5b order the fixed conjugacy classes by the trace of A; they
do not select a projective point, eigenline, stabilizer generator, or source
instance. The A row is the symmetric square of the physical doublet: on a
projective rotation through angle theta it is 1+2cos(theta). The V_alt row is
obtained by the outer automorphism of A5 interchanging its two classes of
five-cycles. The P row is the five-letter permutation representation minus
the trivial line. The D row follows from Sym^4 W. Weighted character inner
products give norm one and pairwise orthogonality for these five rows, and
1^2+3^2+3^2+4^2+5^2=60 shows they exhaust the irreducibles. They are self-dual
as representation types because these characters are real-valued. No actual
space is identified with its dual by this observation.

For a fixed conjugacy class, the even symmetric-power characters h_m=chi(H_2m)
satisfy

    h_0=1, h_1=chi(A),
    h_(m+1)=(chi(A)-1)h_m-h_(m-1), m>=1.             (1)

Indeed h_m is the geometric sum of the formal rotation weights with exponents
-m through m. Applying (1) through degree eighteen and taking the displayed
character inner products gives, in particular,

    H4=D, H6=V_alt+P, H12=1+A+D+P,
    H18=A+V_alt+D+2P.                                (2)

This is a bounded fixed-character calculation, not a section or source
evaluation. Section 10 records a second recurrence check through degree
eighteen from the physical W-tensor ring.

Each stabilizer of a finite subgroup of PGL2(C) acting on P1 is cyclic. Its
action on the tangent line is faithful: a finite-order transformation fixing
a point with derivative one is the identity in characteristic zero. A finite
subgroup of C* is cyclic. The even cycle types on five letters give element
orders 1,2,3,5 in A5. Therefore orbit lengths on X are among

    60,30,20,12.                                      (3)

There is exactly one length-twelve orbit. A5 has twenty-four elements of
order five, hence six distinct cyclic order-five subgroups. Each has two
fixed points on P1. The fixed loci of distinct such subgroups are disjoint
because a projective point stabilizer is cyclic and cannot contain two of
them. Their union has twelve points and is A5-stable. Each orbit in it has
length twelve, so the union is one reduced orbit Z12.

The one-dimensional invariant subspace H12^G in (2) is its equation line.
Every nonzero member f12 of that line has invariant degree-twelve zero
divisor, necessarily exactly Z12. Only the equation line and its product
subspaces are used; no scalar normalization is chosen.

The fixed divisor B_F of a nonzero invariant subsystem F subset H_n is an
effective invariant divisor of degree at most n, intrinsically defined by
the evaluation image F tensor O_X -> O_X(n). For n<=18, a nonempty fixed
divisor must be Z12, by (3). If either A18=H18[A] or D18=H18[D] had this fixed
divisor, it would lie in

    H0(O(18)(-Z12))=f12 H6=V_alt+P,

contradicting (2). Thus A18 and D18 are basepoint-free. Multiplicity one in
(2) makes A18, D18, and H18[V_alt] unique subspaces, while H18[P] has two
copies of P and no copy has yet been selected.

## 3. Whole-orbit inertia and the canonical first-jet quotient

Put L=O_X(18). The first-principal-parts exact sequence is

    0 -> Omega_X tensor L -> P_X^1(L) --q--> L -> 0.  (4)

Its construction from the first infinitesimal neighborhood of the diagonal
is functorial and equivariant. It requires no connection or trivialization.
Let J=P_X^1(L)|Z12 and K=(Omega_X tensor L)|Z12.

All following inertia statements are uniform over the full reduced orbit.
The inverse image of an order-five projective stabilizer in G is cyclic of
order ten. Let alpha denote its character on the tautological line
O_X(-1)|Z12, as a conjugation-compatible character family over the orbit.
It is faithful: if an element acts trivially there, determinant one makes
its other eigenvalue one, and finite order implies that element is identity.
Write mu=alpha^2, the primitive order-five projective inertia character.
These are symbolic characters, not a selected generator or root of unity.

Our convention P(W*) parametrizes lines, so the value and derivative weights
are different and have the following directions:

    L|Z12: alpha^(-18)=alpha^2=mu,
    K: alpha^(2-18)=alpha^4=mu^2.                    (5)

Here Omega_X=O_X(-2) equivariantly because det W=1. In particular pure
derivatives carry the cotangent weight, not the tangent weight. The fixed
inertia restrictions are

    A:     mu^(-1),1,mu,
    V_alt: mu^(-2),1,mu^2,
    D:     mu^(-2),mu^(-1),1,mu,mu^2,
    P:     mu,mu^2,mu^3,mu^4.                       (6)

The A and D rows follow directly from the symmetric powers of W, the P row
from the reduced five-letter permutation representation, and the V_alt row
by subtracting P from H6 in (2). Thus (6) is determined by fixed universal
representations and no actual geometric section data.

The global first-jet map gives an equivariant O_Z12-linear map

    j_A:A18 tensor O_Z12 -> J.

This is the O_Z12-linear extension of the complex-linear jet operation on
global sections; the jet operation itself is not asserted to be O_X-linear.
The two inertia characters of J in (4) are the distinct characters mu and
mu^2. Semisimplicity of finite-group representations in characteristic zero
and (6) force im j_A into the unique mu-isotypic line of J. Basepoint-freeness
of A18 makes its value map onto. Consequently

    L_A=im j_A is a line bundle on Z12,
    q|L_A:L_A -> L|Z12 is an isomorphism,
    K -> J/L_A is a canonical equivariant isomorphism.                  (7)

These statements concern line bundles on the reduced finite scheme Z12.
With i:Z12->X define

    T=i_*(J/L_A),
    tau:H18 --j^1|Z12--> H0(J) -> H0(T).               (8)

Then T has length twelve and tau(A18)=0. The decomposition J=L_A direct-sum K
holds only along this reduced orbit. Neither a global splitting of (4) nor
a quotient connection or horizontal nonconstant splitting is claimed.

## 4. The target and the universal product subspace

An equivariant line bundle on a transitive finite orbit gives the induced
representation of its inertia character on global sections. By (5)-(7),

    H0(T) isomorphic to Ind_(C5)^(A5)(mu^2).           (9)

This notation is understood up to conjugacy of inertia data and makes no
additional geometric choice. Frobenius reciprocity and (6) give multiplicity
one for V_alt,D,P and zero for 1,A. Their dimensions sum to twelve. Hence

    H0(T)=V_alt+D+P                                   (10)

as representation type, with canonical isotypic subspaces.

For a second derivation and the required nonvanishing, use any nonzero member
f12 of the invariant equation line, without normalization. Its conormal
differential along its reduced zero divisor is a nowhere-zero equivariant
section of (Omega_X tensor O_X(12))|Z12. Multiplication by this differential
identifies O_X(6)|Z12 with K and then with J/L_A. The restriction sequence

    0 -> O_X(-6) --f12--> O_X(6) -> O_X(6)|Z12 -> 0

gives, using H0(O(-6))=0 and H1(O(6))=0,

    0 -> H6 -> H0(T) -> H1(O_X(-6)) -> 0.             (11)

Equivariant Serre duality identifies the last representation with H4*=D*;
as a representation type it is D. Thus (11) independently gives (10).

The first-jet Leibniz identity along the full zero scheme is the factorization

    tau(f12 ·):H6 -> H0(O(6)|Z12)
                   --d(f12)--> H0(K) -> H0(T).        (12)

The first arrow is injective since its kernel is H0(O(-6))=0; the last two
arrows are isomorphisms. Thus tau is injective on the entire fixed universal
product subspace f12 H6. In particular its image there is the unique target
V_alt+P, and

    tau|H18[P]:2P -> H0(T)[P]=P

is onto. Define

    P0=ker(tau|H18[P]) isomorphic to P.                (13)

This definition uses only fixed universal spaces and canonical maps. Also
H18[P]=P0 direct-sum f12 H6[P]. Scaling f12 changes neither product subspace,
tau, T, nor P0. No pointwise section evaluation, coefficient choice, or search
in the multiplicity space occurs.

## 5. Intrinsic first-order stationarity and uniqueness

For a basepoint-free subsystem F subset H18, let phi_F:X->P(F*) be its
projective map. In the evaluation sequence

    0 -> M_F -> F tensor O_X -> L -> 0,

the restriction of the first-principal-parts evaluation to M_F lands in
Omega_X tensor L. It is the differential of phi_F, after the usual Euler
sequence identification and twist by L. Equivalently, in any formal local
trivialization it takes a value-zero section to the derivative of its ratio
to a nonzero value section. This is a general intrinsic criterion, not an
evaluation of a selected actual section or point. Therefore

    d phi_F|Z12=0
      iff the first-jet image of F on Z12 is a line mapping
          isomorphically under q to L|Z12.            (14)

Any invariant Lambda subset H18 of type A+P has the form A18 direct-sum Q
with Q a single irreducible subspace of type P in H18[P]. It is basepoint-free
because A18 is. Its first-jet image contains L_A, so (14) gives

    d phi_Lambda|Z12=0 iff tau(Lambda)=0
                       iff Q=P0.                     (15)

Thus A18 direct-sum P0 is the unique invariant stationary seven-space of this
type. The converse is included: it is itself basepoint-free and stationary
along the full reduced orbit. This is a statement within H18, not a
realization of any actual HM branch.

## 6. A self-contained universal Wronskian bound

Let F be an m-dimensional independent section subsystem of O_X(n), and put
r=m-1. Its full Wronskian is the determinant of

    F tensor O_X -> P_X^r(O_X(n)).

The principal-parts filtration has graded lines O_X(n) tensor Omega_X^j for
0<=j<=r. Thus the Wronskian is a section of

    det(F)* tensor O_X(m(n-r)).                        (16)

It is nonzero in characteristic zero. For completeness, at an arbitrary
formal local parameter the vanishing filtration of the independent system
admits an adapted basis with distinct orders a0<...<ar. In the determinant
of the derivatives, the coefficient of order sum(a_i-i) is a nonzero product
of leading coefficients and the Vandermonde product of the distinct integers
a_i. The derivative coefficient array consists of falling factorials, whose
determinant is that Vandermonde product. This proves both nonvanishing and
the local multiplicity formula

    w_F=sum_(i=0)^r(a_i-i).                            (17)

This local formal proof is uniform in the point and system; no actual
parameter, section, coefficient, matrix, rank, or jet is selected or evaluated.

If F is basepoint-free and its projective differential vanishes, then a0=0
and a1>=2. Strict increase gives a_i>=i+1 for i>=1. Hence w_F>=r there.
If F is invariant, the Wronskian zero divisor is invariant because the
principal-parts evaluation is equivariant. Its determinant representation
does not affect its zero divisor; here it is in fact trivial since the even
representations factor through the perfect group A5.

## 7. Surjectivity and the exact universal seven-dimensional kernel

By (12), tau is already nonzero on the source V_alt and on one source P.
Assume tau(D18)=0. The basepoint-free D18 then has first-jet image contained
in L_A, with its value map onto L|Z12. The image is therefore exactly L_A,
and (14) makes its five-section system stationary along all of Z12.

Apply Section 6 with m=5, n=18. Its nonzero Wronskian has degree

    5(18-4)=70

and at least four units of multiplicity along every point of Z12. Its
residual effective invariant divisor after subtracting 4Z12 would have
degree 70-48=22. This is impossible by (3): degrees below thirty can only
be nonnegative sums of 12 and 20, and none is 22. Thus tau(D18) is nonzero.
The unique D in source and target makes its image the entire target D.
Together with (12), this proves the exact sequence (U).

An independent degree contradiction reaches the same conclusion without the
residual-divisor step. If tau(D18)=0, the twelve-dimensional system
A18 direct-sum D18 direct-sum P0 is basepoint-free, contains L_A in its
first-jet image, and is stationary along Z12. Its Wronskian degree is
12(18-11)=84, whereas stationarity forces degree at least 11*12=132.

These Wronskian arguments use higher principal parts only to obstruct
excessive first-order stationarity. They assert no new higher-order branch
matching, no actual higher-jet identification, and no algebraicity.

## 8. The actual seven-space section image is the universal kernel

Fix map directions before using representation self-duality. The original
dual curve is the actual equivariant map

    i18:O_X(-18) -> C* tensor O_X.

By tensor-Hom adjunction it determines an actual scalar-section map

    sigma18:C -> H18.

Its transpose H18*->C* has image exactly the coefficient span V18. Equivalently
ker sigma18=ann_C(V18), so sigma18 descends to the injection

    j18:V18* -> H18,
    V18*=C/ann_C(V18), Lambda15=im j18.               (18)

These quotient and double-dual identifications are canonical for constant
vector spaces. If a scalar presentation of O(-18) is changed, the maps scale
but their images and kernels do not. No such scalar is fixed or evaluated.
The coefficient map associated with the original curve is exactly

    b18=j18*:H18* -> V18**=V18.                       (19)

Thus (19) is the actual coefficient map, not a map manufactured by an
unverified self-duality. Its composite with V18 subset C* is the transpose
of sigma18.

The constant inclusion k7:C7->C has transpose

    r7=k7*:C* -> C7*.

The projected curve y7 is (r7 tensor O_X)i18. Its coefficient map is therefore
r7 b18, and its scalar-section map is

    j7=sigma18 k7=j18 (r7|V18)*:C7 -> H18,            (20)

where C7**=C7 is the canonical double dual. The seven-space theorem says its
coefficient span is all of C7*, so r7|V18 is onto and j7 is injective.
Consequently

    Lambda7=im j7 subset im j18=Lambda15.             (21)

This is the required section-space containment, derived from a genuine
constant projection of the original curve. No moving quotient is projected,
and no connection is invoked. As a representation Lambda7 is C7=A+P, not an
unverified identification of a coefficient space with its dual.

The complete seven-space theorem also makes y7 basepoint-free with vanishing
sequence (0,2,3,4,5,6,8) all along Z12. The missing order-one entry means its
projective differential is zero there, by the intrinsic criterion (14).
Applying (15) and (U) gives the actual embedded equality

    Lambda7=A18 direct-sum P0=ker tau.                (22)

Only first-order stationarity is used from the stronger vanishing-sequence
input. The fact that the prior theorem proved saturation, rather than
silently replacing a coherent image by its saturation, is part of that
complete dependency and is not bypassed here.

## 9. The original fifteen-space and its coefficient kernel

By PR1206 and representation self-duality, V18* has type A+V_alt+D+P. Since
j18 is equivariant and injective, the same is true of Lambda15. Multiplicity
one in (2) forces its A,V_alt,D pieces to be the full subspaces A18,
H18[V_alt],D18. Its sole P piece contains the P0 already present in Lambda7
by (21)-(22); since both have dimension four it equals P0. Thus

    Lambda15=A18 direct-sum H18[V_alt] direct-sum D18 direct-sum P0.       (23)

Let T_P=H0(T)[P]. Isotypic decomposition of a finite-dimensional G-module
is canonical, so its projection pi_P:H0(T)->T_P needs no chosen decomposition
within any repeated source isotypic space. Put gamma=pi_P tau. Equation (13)
makes gamma onto T_P, while equivariance makes it zero on A18,H18[V_alt],D18.
Hence (23) is exactly

    Lambda15=ker gamma.                               (24)

Dualizing the finite-dimensional exact sequence for gamma shows

    Lambda15^perp=im(gamma*:T_P* -> H18*).             (25)

On the other hand (18)-(19) give ker b18=Lambda15^perp. Combining them gives
the fully directed actual coefficient statement

    0 -> T_P* --gamma*--> H18* --b18--> V18 -> 0.      (26)

This identifies the entire four-dimensional coefficient kernel in its fixed
domain, not just an abstract representation isomorphic to P. No V18=V18*
identification is used or needed; self-duality entered only when listing
representation types in (23). The isotypic projection acts on the fixed
target H0(T), never on a moving quotient.

## 10. Fresh bounded verification and contribution

The checker computes the physical symmetric-power characters only through
degree eighteen, using the fixed recurrence

    Sym^(n+1) W=W tensor Sym^n W-Sym^(n-1) W

and the universal adjacency data

    W tensor 1=W, W tensor W=1+A, W tensor A=W+S4,
    W tensor S4=A+D, W tensor D=S4+T6,
    W tensor T6=D+V_alt+P, W tensor V_alt=T6,
    W tensor P=T6+W', W tensor W'=P.

It independently verifies every even-degree decomposition through eighteen
using the A5 character table and recurrence (1), with exact arithmetic in
Z[phi]. The W-tensor recurrence is a check of fixed representation data,
not a selected actual tensor. It also checks the symbolic inertia-weight
multiplicities, the target dimension, the Wronskian degrees and impossible
residual degree, and the exact dimensions in (U) and (26). No broad scan,
numerical roots, source parameters, actual coefficient systems, selected
points, eigenlines, jets, tensors, matrices, or instance ranks are evaluated.

The new universal theorem isolates a canonical stationary P0 in the repeated
P component of H18. Applying the proved constant seven-space theorem turns
this universal uniqueness into the actual section identities (22)-(24),
and then into the precise original coefficient-kernel identity (26). The
original fifteen-dimensional system is not assumed complete; its missing
P is now fixed canonically by the universal first-jet quotient.

The result remains a necessary condition in the residual simultaneous K1
case. It neither realizes nor excludes that case, changes original t or
delta, settles another branch, determines the actual original coefficient
tensor, nor proves higher-order matching or algebraicity. There is no
quotient connection, differentiated nonconstant inverse, horizontal Birkhoff
splitting, or silent saturation replacement.

The checker cannot certify the whole-orbit linearization argument, the
intrinsic stationarity criterion, the Wronskian proof, actual source
sufficiency, or the section/coefficient-space directions. Those require
independent review of this entire frozen proof and both complete freshly
authenticated immutable direct originals. The prior universal audit does
not substitute for that new review.
