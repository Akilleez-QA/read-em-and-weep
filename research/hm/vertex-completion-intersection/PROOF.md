# Exact vertex image of the whole-quadric completion kernel

## Result and scope

Use the marked monad, notation, and physical center grading of PR682 and
PR683. Let Z=P(W*) be the reduced negative vertex line of Q, and let
K be the global twist-four middle operators admitting a homogeneous whole-Q
completion dC=-qV. Write Ncal for the rank50 kernel of the rank53 parabolic
Pcal -> B_Q, not for the canonical rank-one nilpotent N. Set
P2=Sym^2 A tensor D=1+A+V+2P+3D. All family dimensions below mean
Hom_Gamma(P2,-) dimensions, not ordinary section dimensions.

The exact image of K_+ at Z is H0(Z,Ncal_Z(4))_+. Its character is

    2*1+6*A+5*V+7*P+9*D,

with dimension108 and family dimension54. Thus restriction of the
738-dimensional homogeneous middle family has kernel684. This is exactly
its intersection with the1095-dimensional joint vertex/ramification kernel
of PR681, not a subtraction of dimensions of unrelated spaces.

Furthermore the vertex-zero homogeneous kernel still maps onto the entire
four-dimensional divided-class variation space of PR683. Fixing both a
reachable vertex value and a reachable divided cohomology class leaves
middle-family dimension680 and full-completion-family dimension775. Fixing
only a reachable vertex value leaves684 middle and779 full parameters.
No selected actual coefficient, point, matrix, or rank is evaluated.

## 1. The actual canonical nilpotent vanishes on the reduced vertex

The published spinor-filtration proof constructs N by symmetrically squaring
the saturated injection O_wt(1) -> F_Q(2), where Q=P(1,1,2,2) has weighted
coordinates (a,b,u,v). The reduced vertex ideal is (a^2,ab,b^2) in the even
Veronese ring. This construction, not merely the word nilpotent, implies
N|Z=0.

Indeed work on either vertex chart u!=0 or v!=0. Its index-two cover has
coordinates a,b and one coordinate along Z; the deck involution negates
a,b and fixes the last coordinate. The spinor is the odd module, while
F_Q(2), being locally free on the coarse scheme, admits locally a descended
free frame. The even weighted twists trivialize using the chart's nonzero
degree-two coordinate, so they contribute only invertible factors. A homomorphism from the odd module to that free module is
represented on the cover by a vector of odd regular functions h_i. To see
regularity directly, if the images of a,b in a free component are p,q,
the genuine R-linear relation (ab)p=a^2 q, pulled to the cover and
cancelled by a, gives bp=aq. Coprimality of a,b then gives p=ah, q=bh
in the regular cover ring. Invariance of p,q forces h odd. Every such h lies
in (a,b).

On the complement of the vertex, the normalized symmetric square defining
N has entries h_i h_j, up to the invertible determinant trivializations.
Both it and this expression extend regularly, so they agree everywhere.
These products belong to the invariant ideal (a^2,ab,b^2). Consequently
N vanishes scheme-theoretically on the reduced Z. This argument does not
identify its full, possibly nonreduced zero scheme.

PR683 combines the preserving-cone and moving-line exclusion theorems to
prove the actual identity H0(B_Q(4))_+=N(A+D). Every one of these sections
therefore restricts to zero on Z. This actual identity is essential: a
claim about arbitrary adjoints would not follow just from N|Z=0.

## 2. Surjectivity of the rank50 restriction

The canonical rank50 resolution restricts to Q and Z as

    0 -> Lambda^2 S O(3) -> S E(4) -> Ncal(4) -> 0.

The constant determinant line Delta^-1 is understood; it is Gamma-trivial.
These are sequences of vector bundles. Let I=I_(Z/Q). Tensoring with I
remains exact, since the last term is locally free.

We first prove H0(E_Q(4)) -> H0(E_Z(4)) onto. On Z the Euler kernel is
V O plus det(W) O(-1), so

    E_Z=U Lambda^2 V O plus U V det(W) O(-1).

The Koszul generators H0(E(1))=U Lambda^3 H restrict onto H0(E_Z(1)):
the Lambda^2 V tensor W component maps isomorphically to the first summand's
linear sections, and V tensor Lambda^2 W maps isomorphically to the second
summand's constant sections, by contraction with the universal W coordinate.
Multiplying these sections by ordinary cubics in W fills both summands of
H0(E_Z(4)), since multiplication Sym^1 W tensor Sym^3 W -> Sym^4 W is
onto, as is multiplication of constants by Sym^3 W. The ambient products
restrict through Q. This proves the claimed surjectivity, rather than
inferring it from global generation alone.

PR682 gives H^i(E_Q(4))=H^i(O_Q(3))=0 for i>0. The displayed split on P1
also makes E_Z(4) and O_Z(3) higher-acyclic. Thus

    H1(E_Q(4) tensor I)=0,       H2(I(3))=0.

The tensor-I rank50 resolution gives H1(Ncal(4) tensor I)=0. Therefore

    H0(Q,Ncal(4)) -> H0(Z,Ncal_Z(4))

is onto. All maps are equivariant; center projection and Hom_Gamma(P2,-)
preserve this surjectivity in characteristic zero.

## 3. The image and exact intersection

PR683 proves both surjections

    K -> H0(Q,Pcal(4)) -> H0(Q,B_Q(4)),

with kernels qH0(sp(E)(2)) and H0(Ncal(4)), respectively. For an even
section of Pcal(4), its induced adjoint restricts to zero on Z by Section1.
The locally split exact sequence Ncal_Z -> Pcal_Z -> B_Z then places its
vertex restriction in Ncal_Z. Conversely every section of Ncal_Z(4)
extends to Ncal_Q(4) by Section2, then to a member of K by PR683.
Hence the vertex image is exactly the asserted section space.

To compare with PR681, denote by J the joint map consisting of vertex
restriction and the three-coefficient mixed functional on the twelve
ramification joining lines. Its kernel has family dimension1095. The
mixed functional vanishes on every member of K: subtract two source
completion equations, or apply the source-annihilating functional used in
PR678 to the homogeneous equation T alpha=alpha R on Q. The source term
is annihilated by that same marked functional: the projected A and C
images lie in ker(lambda), while B has no VV output. The forcing is zero.
This is an identity along each joining line, so all three coefficients
vanish, not just a value at one physical orbit. Consequently

    K intersect ker J = ker(K -> H0(Ncal_Z(4))).

This identifies the maps whose kernels are being intersected.

## 4. Characters and dimensions

Ordinarily h0(E_Z(4))=6*5+6*4=54 and h0(O_Z(3))=4, so
h0(Ncal_Z(4))=5*54-10*4=230. In the Gamma representation ring,

    [H0 E_Z(4)]=U Lambda^2 V Sym^4 W + U V det(W) Sym^3 W,
    [H0 Ncal_Z(4)]=S[H0 E_Z(4)]-Lambda^2 S Sym^3 W.

With the physical center signs, E_Z(4) has even dimension24 and odd
 dimension30, while Lambda^2 S has even dimension4 and odd dimension6.
Thus the even dimension is3*24+2*30-6*4=108. The character calculation
in verify.py gives2*1+6*A+5*V+7*P+9*D, hence family dimension
2+6+5+2*7+3*9=54. Its involution character is zero, an independent check.
Subtracting this actual image from the PR683 kernel character gives

    K_vertexzero,+ =21*1+72*A+65*V+92*P+114*D,
    dimension1370, family dimension684.

The verifier checks exact abstract finite-group characters and the resulting
arithmetic. Surjectivity and the kernel intersection are proved above, not
certified by a numerical rank computation.

## 5. Vertex and divided class can be matched independently within their images

Let rho:K_+ -> H0(B_Q(4))_+ be the induced adjoint map of PR683. Given b
in its target, lift b to p in H0(Pcal(4))_+. Its vertex value n lies in
H0(Ncal_Z(4))_+. Choose a lift ntilde in H0(Ncal_Q(4))_+ by Section2.
Then p-ntilde has zero vertex value and the same induced adjoint b. Lift
it to K. This proves rho remains onto on K_vertexzero,+. Equivalently,

    K_+ -> H0(Ncal_Z(4))_+ directsum H0(B_Q(4))_+

is onto. The second component controls the divided class by
[V]= -delta_q rho(T); PR683 proves delta_q injective using H0(B(4))=0.
Thus imposing zero vertex and zero divided-class variation subtracts
A+D, giving dimension1362 and family dimension680, not merely an upper
or lower bound.

For any nonempty affine forcing solution set, choose one solution T0.
Its possible vertex values form exactly the affine translate
T0|Z + Hom_Gamma(P2,H0(Ncal_Z(4))_+), of dimension54 inside the90-dimensional
ambient vertex family space. The divided classes form the PR683 translate
of the four-dimensional boundary image. Every pair within these two
translates is attained, by the proved joint surjectivity. Each nonempty
joint fiber has middle dimension680. Source lifts add the same95 parameters
as PR682, without changing the vertex or divided class, giving full
 dimensions775, or779 if only vertex is fixed. These are unquotiented affine
fibers, not gauge quotients. Fixing the divided cochain itself is a different
condition, not counted here. Prescribed class assignments must themselves
be P2-equivariant families for these family statements to apply.

This resolves the structural intersection and vertex/class compatibility
of homogeneous whole-Q completion. It does not construct the chosen actual
primitive, claim arbitrary vertex data are completable, determine the
fourth Bockstein, or establish algebraicity.

## Immutable dependencies

- PR683: https://github.com/Akilleez-QA/read-em-and-weep/blob/d4008b924e9ddff9726f86ccccc1574677da9218/research/hm/completion-kernel-dimensions/PROOF.md
- PR682: https://github.com/Akilleez-QA/read-em-and-weep/blob/5a8249656bfb406d4a0a89994b0de6293e5acd8f/research/hm/source-completion-criterion/PROOF.md
- PR681: https://github.com/Akilleez-QA/read-em-and-weep/blob/a930f9cc295d79c2342b4eebe6f34efc04ccf05d/research/hm/degree-one-restriction/PROOF.md
- PR678: https://github.com/Akilleez-QA/read-em-and-weep/blob/f47c81086e5bd17be4ba714e43fa7f6226d41beb/research/hm/ramification-family-target/PROOF.md
- Actual mixed source elimination, Section3: https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-RAMIFICATION-DETECTS-A-NONZERO-MIXED-FORM-MIDDLE-VALUE.md
- Actual spinor construction, Sections1 and5: https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md

Authored mathematical proof with independent review recorded in REVIEW.md;
not proof-assistant formalization or selected actual-instance computation.
