# The rank-five synthetic fiber is an open K3 surface

## Statement and scope

Work over C with the conventions and synthetic construction of `PROOF.md`.
Write U=E0, let h be the nondegenerate symmetric bilinear form defining
ell:Sym²U→C, and let K=ker ell. Thus dim U=3 and dim K=5. Products in
Sym²U use ab=(a⊗b+b⊗a)/2; equivalently the coefficient of e1e2 in the
symmetric-algebra expression a e1²+b e1e2+c e2² is b, whereas the
off-diagonal entries of its contraction matrix are b/2.

There is a nonempty Zariski-open subset of Hom(K,U) such that, for v in
that subset, the separately projectivized independent-zero fiber of
the synthetic operation over its distinguished middle line is

    Y \ R,

where Y is a smooth projective K3 surface and R is one smooth rational
curve of self-intersection −2. In particular this fiber is a smooth
irreducible nonrational surface.

The quotient of Y by factor exchange is a smooth rational surface T
obtained by blowing up P² at ten distinct points. The cover Y→T is
branched along one smooth rational curve B of self-intersection −4,
with B∈|−2K_T|. The points of this blow-up are special; they are not
claimed to be ten general points of P².

This is a compactification of the abstract synthetic fixed-middle
fiber. It neither identifies the actual physical operation with this
model nor supplies a two-dimensional middle family or a
seven-dimensional affine zero component. The corrected outer-input
map contracts R and identifies its image with the full reduced
synthetic projective zero fiber over the distinguished middle line;
Y itself is its smooth birational resolution. No normality assertion
for that image is needed or made.

## 1. The projective-bundle resolution and its Chern classes

Let P=P(U*) parametrize covector lines, let H=c1(O_P(1)), and use the
tautological exact sequence

    0 → S → U⊗O_P → O_P(1) → 0.

Thus S has rank two, c1(S)=−H, and c2(S)=H². Restriction of ell gives
a surjective map Sym²S→O_P: otherwise a two-plane in U would be totally
isotropic for h, impossible for a nondegenerate ternary form. Set

    F=ker(Sym²S→O_P).

Then F is a rank-two subbundle of K⊗O_P. If x,y are formal Chern roots
of S, the Chern roots of Sym²S are 2x,x+y,2y. Consequently

    c1(F)=3c1(S)=−3H,
    c2(F)=2c1(S)²+4c2(S)=6H².

Put X=P_P(F), using the convention that projective bundles parametrize
lines, and let pi:X→P and Q=O_X(−1)⊂pi*F be the tautological line.
Write xi=c1(O_X(1)); all base bundles and H are pulled back when needed.
The variety X is smooth, irreducible, projective, and three-dimensional.
Its points are pairs ([k],[q]) with q∈K∩Sym²ker(k), q nonzero.

For this convention the projective-bundle formulas are

    K_X = −2xi + pi*(K_P−c1(F)) = −2xi,
    xi² − 3Hxi + 6H² = 0,
    ∫_X H²xi=1,    ∫_X Hxi²=3,    ∫_X xi³=3.

Forgetting [k] maps X onto the determinant cubic
{[q]∈P(K):rank q≤2}. Over rank exactly two this map is an isomorphism:
the support im(q) is a two-plane and its annihilator [k] is unique,
varying algebraically on the constant-rank locus.

## 2. Generic compatibility is the blow-up at ten points

A linear map v:K→U induces a section

    s_v ∈ H0(P,F*⊗O_P(1))

by the composite F⊂K⊗O_P→U⊗O_P→O_P(1). On X its evaluation on Q
is a section of O_X(1)⊗pi*O_P(1). Define its zero scheme

    T = {([k],[q])∈X : k(v(q))=0}.

Its divisor class, when v is generic, is xi+H.

The linear parameter space A=Hom(K,U) generates F*⊗O_P(1) at every
point. Indeed any linear map F_[k]→(U/ker k) extends first to K and
then lifts to U. The incidence of zero evaluations in P×A is therefore
the total space of a vector bundle of rank dim A−2 on P. It is smooth.
Generic smoothness in characteristic zero shows that the zero scheme
Z_v=Z(s_v) of a generic section from A is either empty or a reduced
zero-dimensional scheme.

It cannot be empty: a nowhere-zero section of a rank-two bundle on P²
would imply vanishing top Chern class, whereas

    c2(F*⊗O_P(1))
      = c2(F*) + Hc1(F*) + H²
      = (6+3+1)H² = 10H².

Equivalently the universal incidence is proper and surjective over A;
its generic fibers are smooth of dimension zero and have length ten.
Thus on a nonempty open subset A_reg, Z_v consists of ten distinct
points, and the section is regular at all of them.

For such v, T is isomorphic over P to Bl_(Z_v)P. To check this directly,
trivialize F and O_P(1), write s_v=(a,b), and write [x:y] for the line
in F. The equation of T is

    ax+by=0.

Away from (a,b)=0 there is the unique line [x:y]=[−b:a]. At a zero of
s_v, a,b form a regular system of parameters, and this same incidence
is the usual blow-up of the ideal (a,b), after the projective coordinate
change [x:y]=[−Y:X]. These local identifications glue to the canonical
graph closure of the kernel line of s_v.

In particular T is smooth, connected, rational, and projective, with

    h1(T,O_T)=h2(T,O_T)=0,
    K_T=(K_X+T)|_T=(−xi+H)|_T,
    K_T²=−1.

The last equality follows either from blowing up ten points of P² or
from (−xi+H)²(xi+H)=xi³−Hxi²−H²xi=3−3−1=−1.

## 3. The rank-one divisor and the branch curve

For a rank-two bundle S and a line Q⊂Sym²S, the binary discriminant is
a canonical morphism

    delta: Q² → (det S)².

In a local basis e1,e2 of S and with local generator
q=a e1²+b e1e2+c e2² of Q, it is

    delta(q²)=(b²−4ac)(e1∧e2)².

This formula is compatible with change of basis and rescaling q. Its
zero divisor D⊂X is the rank-one locus, with class

    [D]=2xi+2c1(S)=2xi−2H.

There is an isomorphism of schemes

    D ≅ {([e],[k])∈C0×P(U*): k(e)=0},

where C0={ [e]∈P(U):h(e,e)=0 } is a smooth plane conic. Indeed the
binary rank-one locus in P(Sym²S) is the relative Veronese image of
P(S); restriction to X imposes exactly h(e,e)=0. This also verifies
the scheme structure, rather than merely the rank-one points.
The displayed incidence is a P¹-bundle over C0, so D is smooth.

There is a nonempty open A_square⊂A on which

    v(e²)∉Ce   for every [e]∈C0.

For fixed [e] this failure condition has codimension two in A. The
incidence of failures over the projective curve C0 is closed of
dimension dim A−1; its proper projection is a proper closed subset of
A. Thus the asserted open is nonempty. This is the same square
avoidance condition used in `PROOF.md`.

Fix v∈A_reg∩A_square. On D the additional equation defining T is
k(v(e²))=0. For every [e]∈C0, the vectors e and v(e²) are independent.
There is therefore exactly one covector line [k] annihilating both.
This line varies regularly: it is the annihilator of the rank-two
subbundle generated by e and v(e²). Accordingly

    B=T∩D ≅ C0 ≅ P¹.

This intersection is scheme-theoretically a smooth reduced curve.
In each P¹ fiber of D→C0, k(v(e²)) is a nonzero linear equation. Its
zero is simple, so it defines a smooth section and T meets D
transversely. Hence on T

    B∈|2xi−2H|_T=|−2K_T|,
    B²=4K_T²=−4.

All required genericity conditions are simultaneous nonempty opens
of the irreducible affine space A. If the additional open
A_surface of `PROOF.md` is retained, it can be intersected too;
the present construction already proves its needed nonempty smooth
two-dimensional rank-two compatibility locus T\B.

## 4. The global double-cover algebra and its factor interpretation

On T set

    L = Q*⊗det S = O_T(xi−H) = O_T(−K_T).

The discriminant is a section delta∈H0(T,L²), vanishing simply along
B. Define the finite flat double cover

    rho:Y=Spec_T(O_T⊕L^(−1)) → T,

where multiplication L^(−2)→O_T is contraction with delta. This is
the correct cover algebra: the trace-zero summand is

    L^(−1)=Q⊗(det S)^(−1)=O_T(K_T),

not its dual. Changing the overall discriminant convention by a
nonzero square changes only the corresponding choice of local
square-root coordinate and gives an isomorphic cover over C.

For completeness, this cover is intrinsically the binary factor
scheme, including the doubled-root fibers. On p:P_T(S)→T let
M=O(−1) be the tautological factor line. The zero scheme of

    p*Q → Sym²(p*S/M)

parametrizes lines dividing q. Since q is nonzero at every base
point, its fibers are degree-two subschemes of P¹; this scheme is
finite flat of degree two over T. In the chart with a invertible,
writing a factor line as e1+z e2 gives

    az²−bz+c=0.

The coordinate w=2az−b satisfies w²=b²−4ac. Such charts cover
locally after changing the basis of S. Their transition functions
give precisely the trace-zero line Q⊗(det S)^(−1), so the factor
scheme is Y with the cover algebra displayed above.

One may also recover the line without coordinate transformations:
the factor divisor on P_T(S) has line bundle

    O(2)⊗p*(Q*⊗(det S)²).

Its defining exact sequence and
R¹p*O(−2)=det S identify the quotient of p*O_Y by O_T with
Q⊗(det S)^(−1). The trace map, divided by two, canonically splits
off O_T, and the local quadratic equation identifies multiplication
with the discriminant.

Over T\B the tensor has rank two and two distinct factor lines.
Choosing the first determines the second, so Y\rho^(−1)(B) is the
ordered-factor cover. If q=ab, then

    delta(q²)=(a∧b)²;

interchanging a and b negates its square root. Thus the involution
of Y is exactly factor exchange. Over B its fiber is the double
point corresponding to the repeated factor, while its total space
will be smooth. In particular Y is the normalization of T in the
function field of its ordered-factor cover.

## 5. Smoothness, connectedness, and the K3 invariants

Locally the cover is w²=d, where d is a local defining function for
the smooth reduced branch curve B. It is étale away from B and
smooth along B because dd does not vanish there. Thus Y is smooth.
It is projective because it is finite over the projective surface T.

The standard canonical formula for a smooth double cover is also
immediate by adjunction in the total space of L:

    K_Y ≅ rho*(K_T⊗L) ≅ O_Y.

Indeed that total space has canonical line bundle the pullback of
K_T⊗L^(−1), and the equation w²=delta is a section of the pullback
of L².

Because rho is finite,

    H^i(Y,O_Y)=H^i(T,O_T) ⊕ H^i(T,L^(−1))
              =H^i(T,O_T) ⊕ H^i(T,K_T).

Rationality of T and Serre duality give

    h0(Y,O_Y)=1+0=1,
    h1(Y,O_Y)=0+0=0,
    h2(Y,O_Y)=0+1=1.

Thus Y is connected. A connected smooth surface is irreducible,
since distinct irreducible components of a smooth scheme are
disjoint. Consequently Y is a smooth projective K3 surface (the
usual algebraic definition is K_Y trivial and h1(O_Y)=0). In
particular it is nonrational, also directly witnessed by h2(O_Y)=1,
which is a birational invariant of smooth projective surfaces.

The ramification divisor R maps isomorphically to B. Since
rho*B=2R and deg rho=2,

    4R²=2B²=−8,    hence R²=−2.

So R is one smooth rational (−2)-curve. Removing it leaves a smooth
irreducible nonrational surface with the same function field as Y.

## 6. Identification with the synthetic independent-zero fiber

On T\B every q has rank two, its support is S_[k], and k is the
unique annihilator of that support. The equation k(v(q))=0 is
therefore exactly

    v(q)∈im(q).

The isomorphism X^(2)→{[q]∈P(K):rank q=2} consequently identifies
T\B with the rank-two compatibility locus of `PROOF.md`, and the
preceding double cover is its ordered-factor cover.

To check the input reconstruction with the symmetric convention,
write q=ab with independent a,b∈U and write uniquely
v(q)=nu a+mu b. In the synthetic quotient, the graph relation says
B_u(q)=A_u(v(q)). Hence the unique corrected outer directions are

    x=a−mu u,    z=b−nu u,

and trilinearity gives f(x,u,z)=0. Independence of a,b makes x,u,z
linearly independent. This construction is independent of the
factor frames and has the inverse obtained by projecting x,z
modulo Cu. All these operations use vector bundles and invertible
rank-two decompositions; they therefore give a scheme isomorphism,
not just a pointwise bijection.

It follows that the separately projectivized independent-zero fiber
over [u] is exactly Y\R. At rank one the equation on T says only
v(e²) lies in the chosen two-plane S_[k]; square avoidance explicitly
forbids v(e²)∈Ce. Thus the boundary curve is part of this
compactification, not an additional locus of independent zeros.

Finally, imposing the stronger generic choice of v causes no change
to the subsequent synthetic quotient construction in `PROOF.md`:
its repeated-input avoidance and isolated rank-five middle point
use square avoidance, which still holds. The model's projective
independent-zero locus remains two-dimensional and its
all-inputs-nonzero affine locus remains five-dimensional.

## 7. A second model: a (1,1),(2,2) complete intersection

The K3 surface also has an intrinsic ordered-factor realization in
P(U)×P(U). Extend v arbitrarily to a linear map
v_tilde:Sym²U→U. Define Z by

    h(a,b)=0,
    a∧b∧v_tilde(ab)=0.

These are equations of bidegrees (1,1) and (2,2), respectively. The
second equation on the first hypersurface is independent of the
extension: changing v_tilde by ell(−)c changes that equation by
h(a,b)(a∧b∧c), a multiple of the first equation.

At a point with a,b independent, these equations say ab∈K and
v(ab)∈span(a,b). At a point on the diagonal, they say a=b=e with
h(e,e)=0. Square avoidance then ensures e and v(e²) are independent.
Thus everywhere on Z the matrix with columns a,b,v(ab) has constant
rank exactly two: its determinant vanishes scheme-theoretically and
at least one two-by-two minor is invertible locally. Its image is a
rank-two subbundle S_Z⊂U⊗O_Z, supplying a regular annihilator map
Z→P(U*). Together with q=ab, it gives a morphism Z→T and a chosen
factor line of q, hence a morphism Z→Y.

Conversely Y carries its first factor line and the second factor
line obtained by division of q by the first. This division is
regular even at the double root: the map A⊗S→Sym²S for a factor
line A is an injective bundle map, and q determines the line
Q⊗A^(−1)⊂S. These two lines give a morphism Y→Z. The constructions
are inverse on all test schemes, including on the diagonal, where
the plane is recovered as span(e,v(e²)). Hence

    Y ≅ Z ⊂ P²×P².

In this model R is the diagonal isotropic conic. The two equations
give a smooth complete intersection, and adjunction provides a
second check:

    K_Y=O_Y(−3,−3)⊗O_Y(1,1)⊗O_Y(2,2)=O_Y.

This realization also excludes any additional diagonal component:
the diagonal contribution is precisely the single curve R.

## 8. The corrected outer map and the full reduced projective fiber

Let A,B⊂U⊗O_Y denote the two factor line bundles. Locally choose
nonzero frames a,b and put q=ab and w=a∧b∈det S. The expressions

    X = (a∧b)a − (a∧v(ab))u,
    Z = (a∧b)b − (v(ab)∧b)u

take values in V⊗det S. Rescaling a by lambda and b by eta rescales
X by lambda²eta and Z by lambda eta². Equivalently these are global
bundle maps

    A²⊗B → V⊗det S,
    A⊗B² → V⊗det S.

Neither map vanishes anywhere. Off R, w is nonzero and the U-component
of X or Z is respectively wa or wb. On R, a and b are proportional
to e, and the terms e∧v(e²) are nonzero by square avoidance. Thus
the two expressions define an everywhere regular morphism

    Phi:Y→P(V)×P(V),    y↦([X],[Z]).

On Y\R, write v(ab)=nu a+mu b. Then

    X=w(a−mu u),    Z=w(b−nu u),

so Phi is exactly the independent-zero isomorphism of Section 6.
On R its two coordinates both equal [u]. Consequently Phi contracts
precisely R to o=([u],[u]) and is an isomorphism away from that point.
The trilinear zero equations hold on the dense open Y\R and hence
on all Y. Its projective image is the reduced closure of the
independent-zero fiber.

In fact this is the entire reduced projective zero fiber over [u].
Here is the needed general dependent-zero argument, using only the
outer symmetry, cyclic-zero identity, and repeated-input injectivity
already proved for the synthetic operation. Write

    A_x(z)=f(x,x,z).

For independent x,z, the vectors A_x(z) and A_z(x) in the target
are linearly independent. Indeed for
w=alpha x+beta z and t=gamma x+delta z, polarization of the two
symmetries gives

    A_w(t)=(alpha delta−beta gamma)
                 (alpha A_x(z)−beta A_z(x)).

Any dependence between the two displayed target vectors would give
a nonzero pair (alpha,beta) annihilating the second factor; choose
(gamma,delta) so the determinant is nonzero. Then w,t are
independent but A_w(t)=0, contradicting repeated-input injectivity.

Now suppose x,u,z are nonzero, dependent, and f(x,u,z)=0. If x,z
are independent, write u=a x+b z. Outer symmetry gives

    f(x,u,z)=a A_x(z)+b A_z(x),

forcing a=b=0, a contradiction. If x,z are proportional, the cyclic
identity instead gives f(x,u,x)=−2A_x(u), so vanishing forces u
proportional to x. Thus every dependent zero triple has all three
lines equal. For the fixed middle line [u], the only such point is o.

The complete reduced projective zero fiber is therefore

    (Y\R) ∪ {o},

and Phi is a proper birational resolution, with a single exceptional
curve R. If desired, its Stein factorization gives a factorization
through the normalization of that reduced image. This proof does
not assert that the image itself is normal, that its scheme
structure is reduced before taking the reduction, or that its
singularity is of a specified analytic type.

## Verification boundary

This proof uses only finite-dimensional linear algebra, projective
bundles, generic smoothness, blow-ups, and double-cover geometry.
It performs no evaluation of the actual source operation, no
numerical rank probe, no actual input computation, and no external
source write. The only output is this local proof artifact.
