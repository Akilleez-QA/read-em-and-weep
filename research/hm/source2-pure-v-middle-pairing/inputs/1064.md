# The marked residual string and the homotopy kernel on NR

## Theorem and boundary

Retain the conditional actual source2 pure-V compatible radical and its
canonical homotopy h. Fix a genuine negative-pencil separation N=N0⊕NR
and the actual exact negative system 0→NC→NR --π→N8→0. Let
U=(U2,U3,U4)=(A_can,S_can,D_can) be the actual canonical string of PR1050.
Then U⊂NR, π|U is injective at all three vertices, and

    π4(D_can)=D8⊂N8,4=V8+P8+D8,
    D_can∩NC4=0.                                      (1)

In particular (1) holds in BOTH remaining generated-endpoint branches,
not merely the nine-dimensional one. Put U8=π(U). There is an actual
fixed-variable splitting on this restricted inverse image:

    π^(-1)(U8)=NC⊕U.                                  (2)

This does not split the full residual extension NR over N8.

Moreover put K_R=ker h∩NR4. Then

    h(NR4)=I2,   dim K_R=16,   NR4=K_R⊕D_can.          (3)

Here I2=im j2 is the degree-two D; it is not D_can or D8.

For the remaining assertions assume the ACTUAL N0 projection of P_h is
zero, where P_h is the canonical P in im h. There are two necessary cases:

- P_h⊂NC2: F4=NC4, h(NC4)=0, and
  K_R=π4^(-1)(V8+P8), with exact sequence
  0→NC4→K_R→V8+P8→0.
- π2(P_h)≠0: F4=K_R, h induces an isomorphism NC4/I4→I2, and
  0→I4→F4 --π4→N8,4→0.

Thus under zero N0 projection, h|NC4=0 if and only if dim F4=9;
otherwise dim F4=16 and that restriction has rank five. These are proved
actual-map ranks under explicitly retained hypotheses, not instance
computations. No branch, projection, scalar value, or source occurrence
is selected. The nonzero-N0 branch is not excluded or assigned a value
of h|NC4.

## 1. Immutable inputs and exact objects

INPUTS.json retains four exact public proofs:

- PR795 at 3f811311d76914a555c7e7d0c5b887b41805aa6c: the genuine residual
  extension and complete fixed-variable degree-eight evaluation model.
- PR1050 at ec18a0fd62c4a9495adf6aad9564d379afc42b62: the canonical actual
  A→S→D string, constructed using ring commutativity and joint-negative
  injectivity, with coherent ordinary symmetric multiplication.
- PR1059 at af2f163e4bcc593b6895ace840c139d2d4668cde: exact endpoint
  alternatives9/16, the actual quotient transport in the residual-large
  branch, h(NC4)=0 in the small branch, and the orientation of j4, which
  kills NR4. It also supplies the precise polarization quotient below.
- PR1061 at 90f33f808c2962cdd4c41d11ac32a10c30b0d353: h|D_can≅I2,
  ker h⊂im Q, and im Q=ker h⊕D_can, with all generated F4⊂ker h.

All actual-source transfer and geometric hypotheses of those proofs are
retained. The refinement does not identify any of PR1060's marked mixed
P+D blocks with im h and does not analyze its full V-channel multiplicity
kernel. The new information is the position of the canonical string in
the actual residual quotient and its consequences for h there.

The actual spaces needed are

    N0,2=P+D,          NC2=Sym16 W=V+P+2D,
    NC3=Sym17 W,       NC4=P+D,
    N8,2=A⊗Sym4 W,     N8,3=A⊗Sym5 W,
    N8,4=(A⊗Sym6 W)/Delta(Sym8 W)=V+P+D.             (4)

Here Delta is complete polarization into bidegree(2,6). The arrows keep
the first A coefficient factor fixed and multiply the SECOND polynomial
factor by the same negative linear form. All actual quotient maps commute
with these arrows. In particular NR4 has dimension9+12=21.

## 2. The marked string projects, rather than disappearing in NC

Since N0,2 has no A, the actual equivariant projector kills U2; hence
U2⊂NR2. Negative stability of NR then puts all U in NR. Since NC2 has
no A, π2|U2 is injective. Its image is the unique A in A⊗Sym4 W:
Clebsch decomposition gives Sym6 W+Sym4 W+Sym2 W, with only the last
summand containing A. This is an embedding conclusion using the actual
projector and exact quotient, not a character-only choice of source.

We calculate its descendants in the precise quotient (4). Use formal
variables X,Y for the first A factor, and x,y for the polynomial factor.
For f∈Sym2 W its unique A inclusion is, up to a nonzero scalar,

    e(f)=(Xy−Yx)^2 f(x,y).                            (5)

The alternating determinant is SL2-invariant, so (5) is equivariant and
nonzero. Its three coefficient polynomials in X²,XY,Y² are

    y²f, −2xyf, x²f.

The endpoint quotient is realized by the unnormalized transvectants

    C(a⊗g)=((a,g)_1,(a,g)_2)∈Sym6 W⊕Sym4 W,
    (a,g)_k=Σ_j (−1)^j binom(k,j)
        (∂x^(k−j)∂y^j a)(∂x^j∂y^(k−j) g).           (6)

As checked in PR1059 and again here, C has rank12 and its kernel is
exactly the nine-dimensional complete polarization Delta(Sym8 W).
This is a fixed-variable quotient identification, not a character match.

Let b and f be arbitrary formal binary quadratics, with all six
coefficients retained as indeterminates. Differentiate (5) after multiplying
its second factor by b. An exact polynomial identity is

    C(b e(f))=(0,84 b f).                             (7)

The checker proves (7) identically in those six coefficients. Since all
products bf span Sym4 W, the complete quadratic descendant image is
exactly the unique D8, and its map from Sym4 W is nonzero and injective.
The scalar84 belongs only to the universal normalization (5)-(6); it is
NOT an actual source coefficient. Actual identification of π2(U2) with
(5) has an unevaluated nonzero scalar.

By actual multiplication compatibility, the image π4(U4) is precisely
this D8. PR1050 already proves U4 irreducible and generated by these
quadratic descendants. Thus π4|U4 is an isomorphism onto D8. In the
middle, π3(U3) cannot vanish, since its negative descendants include D8.
Irreducibility of U3=S makes π3|U3 injective. This proves (1) and
injectivity at every vertex, without a splitting of NR.

Define U8 to be the actual image submodule π(U). At each vertex any
element of π^(-1)(U8) has a unique lift in U modulo NC, and NC∩U=0.
Since all maps are negative-module maps, this proves (2) as an actual
fixed-variable direct sum. Its dimension triple is (20,22,14). It is only
the inverse image of the (3,4,5) submodule U8 of N8=(15,18,12).
No Q-stability is asserted for (2).

## 3. Exact rank of h on the residual endpoint

The pure-V orientation in PR1059 says j4(NR4)=0. The identity
ker j4=im Q, imported in PR1061, therefore gives NR4⊂im Q. Since
h(im Q)=I2, one has h(NR4)⊂I2. But U4=D_can⊂NR4 and PR1061 proves
h|D_can is an isomorphism onto I2. Thus h(NR4)=I2 and the kernel has
dimension21−5=16. The same marked section r=(h|D_can)^(-1) gives the
actual splitting (3), with projector r h restricted to NR4.

Since I4⊂NC4 and h(I4)=0, the only possible nonzero channel of h|NC4
is the unique D constituent. Hence either it vanishes or it induces an
isomorphism NC4/I4→I2. This observation alone does not choose a value;
the next section identifies it only under the specified projection cases.

## 4. The two residual generated branches

Assume e2(P_h)=0, with e the actual N0 projector. Then all of F lies in
NR because im h=I2+P_h and I2⊂NC2.

In the small case P_h⊂NC2, PR1059 gives F4=NC4 and h NC4=0. Thus h|NR4
descends through π4 to a map N8,4→I2. Its restriction on D8 is an
isomorphism by (1) and h|D_can≅I2. Equivariance kills the V8 and P8
summands. Therefore the descended kernel is exactly V8+P8, proving the
first asserted inverse-image identity and exact sequence.

In the other residual case π2(P_h)≠0, PR1059 proves that the actual
map A⊗P_h→N8,4 is an isomorphism. It also proves dim F4=16 and that
F4→N8,4 is onto with kernel I4. But F4⊂NR4∩ker h=K_R and both spaces
have dimension16. Thus F4=K_R, and K_R∩NC4=I4. The restriction h|NC4
then has kernel I4 and rank9−4=5; since its image is contained in I2,
it induces the asserted isomorphism NC4/I4→I2.

These two cases exhaust zero N0 projection. They prove the stated
if-and-only-if without evaluating the homotopy's remaining scalar. They
do not apply the large residual conclusion when e2(P_h)≠0: in that
case F4 need not lie in NR4, so equality with K_R is not established.

## 5. Reproduction and limits

Run python verify.py and python -O verify.py. The verifier authenticates
four retained immutable inputs, reconstructs the exact quotient C and
polarization inclusion, proves the determinant-square inclusion and (7)
with symbolic coefficients, and checks the dimension and character
arithmetic. Actual inherited maps, their exactness and the subspace
arguments use the written proofs, not numerical experiments.

There is no actual HM coefficient, direction, jet, point or matrix
specialization. No branch or source pair is excluded or realized; no
original Bockstein is newly asserted zero. This result does not decide
D_can's degree-five descendants, does not extend h to a graded-module
homomorphism, and does not split the entire residual negative system.
