# Generic beta surfaces and the actual abelian interpolation form of the full boundary

## Scope and checked inputs

This note gives a geometric realization of the remaining twist-four boundary through the actual universal beta family. It does not prove invertibility of that boundary. Generic smoothness, the abelian blowdown, and the family determinant twists are established separately, so none is inferred from numerical agreement.

Work over C. Let F be normalized HM, c1(F)=-1, c2(F)=4, E=F(3), U=H0(E), dim U=4. Let T=Gr(3,U)=P(U*) and let

    0 -> Bcal -> U tensor O_T -> O_T(1) -> 0

be the universal hyperplane sequence. Write d=det U, so det Bcal=d tensor O_T(-1). The actual evaluation minors cut out C, the disjoint union of 25 HM lines. Its rank-zero hyperplane parameters form Gamma. For B in T, X_B is the rank-at-most-one surface of B tensor O -> E.

Repository inputs:

- BETA-DEGENERACY-SURFACE.md, 26240e70230aef0de1f1b8714a06bd644adeec69: all X_B are pure locally CM degree15 surfaces, with the actual Hilbert–Burch resolution and chi(O_X(n))=(15n^2-25n)/2.
- BETA-QUOTIENT-POSITIVITY.md, 098a2769986103880e9c8aec437c7ea06b9388b1: off Gamma the B-evaluation has constant rank one, C is the regular zero divisor of the residual quotient section, and X_B is smooth along C.
- UNIFORM-FLAT-EVALUATION-FIBRATION.md, 1c8166298f30f30a8ab30cde5c27467f9bef8e22: choose a common-good smooth quadric Q, transverse to C and containing no component of any X_B. The resolved evaluation map f:Xhat -> T is flat; Xhat is the blowup of P_Q(E|Q) at the fifty simple evaluation base points.
- QUADRIC-FIFTY-POINT-BOUNDARY.md, 22bdcb7e9c833e7a1819d0ec28e5e615be9c7a4f: H0(I_C(1))=H0(I_C(3))=0, the compatible determinant conventions, and the actual fifty-point boundary. In particular the low-degree equation vanishings below are pinned inputs, not inferred merely from scheme-theoretic generation of I_C by quintics.
- Both actual quadratic flanks are good on the established common open: primary q:H1(F)->H1(F(2)) is injective, and Rao q:H1(I_C(1))->H1(I_C(3)) is injective. These are distinct maps.

Primary literature used: Aure–Decker–Hulek–Popescu–Ranestad, Syzygies of Abelian and Bielliptic Surfaces in P4, arXiv:alg-geom/9606013v2, https://arxiv.org/pdf/alg-geom/9606013 . Section3 fixes the normalized HM conventions and its cohomology module; Section7 describes the smooth linked degree15 family; Proposition8.4(ii) supplies its (2,10) polarization type. The degree15 (1,20) family in Section8 is different and is not substituted here.

## 1. General actual X_B is smooth

Consider the universal rank-drop family Scal in P4 times T. Over P4 minus C, evaluation U -> E is surjective. If K_x is its rank-two kernel, rank(B -> E_x)<=1 is equivalent to K_x subset B. Thus Scal over P4 minus C is the projective-line bundle parametrizing hyperplanes containing K_x, and is smooth and irreducible.

Over T minus Gamma, the evaluation B -> E has rank exactly one on X_B, including along C. Locally, after invertible row/column operations, it is

    [1 0 0; 0 a b].

The surface is the regular embedding (a,b). The full residual section cuts C as a Cartier divisor. Its local quotient ring is regular of dimension one, so the two-dimensional local ring of X_B is regular. Hence X_B is smooth at every point of C. The same local derivatives show the universal family is smooth along C times (T minus Gamma).

Consequently Scal over T minus Gamma is smooth everywhere. The projection is proper and has constant pure fiber dimension two. In characteristic zero, generic smoothness, together with properness to remove the closed image of the nonsmooth locus, gives a nonempty open T_sm whose entire fibers X_B are smooth.

These smooth fibers are connected. The Hilbert–Burch resolution gives H1(I_X)=H2(F(-7)) tensor det B=0. For the last equality, Serre duality reduces to H2(F(3))=0; this follows directly from the normalized HM monad 5O(-1) -> 2 Omega^2(2) -> 5O after twisting by3. Thus H0(O_X)=C. Smooth connected fibers are integral. This proves generic smoothness/integrality without assuming that every off-Gamma fiber is integral.

## 2. Exact identification with the linked abelian family

Take a general ordered basis s1,s2,s3 of B. The zero surface A0=Z(s1) is a smooth HM abelian surface. The Serre sequence for s1 identifies H0(I_A0(5)) with U/<s1>, by s |-> s1 wedge s. Therefore the two quintics

    f12=s1 wedge s2,   f13=s1 wedge s3

are a general pair of quintics through A0. They have no common divisor and define a (5,5) complete intersection.

The residual scheme to A0 is exactly X_B, not just a surface with the same numerical invariants. Locally write s1=(a,b), s2=(c,e), s3=(g,h), and put f23=ch-eg. The identities

    a f23 = c f13 - g f12,
    b f23 = e f13 - h f12

give I_X=(f12,f13,f23) subset (f12,f13):(a,b). The residual is locally CM of degree25-10=15. The actual X_B is also pure locally CM degree15. The inclusion and equality of degrees give equality at every generic point. A nonzero subsheaf of O_X cannot be supported only in smaller dimension because O_X has no embedded associated primes. Thus the two ideals agree scheme-theoretically.

ADHPR Section7 therefore applies to this actual B-family, not merely to an analogous construction. It identifies the general linked surface as a non-minimal abelian surface with the 25 HM lines exceptional. Proposition8.4(ii) gives the descended polarization type (2,10).

There is also an intrinsic check of the minimal type. For fixed B off Gamma, let A_B be the image line of B -> E and Q_B the quotient. The residual one-dimensional space U/B gives a section of Q_B with scheme zero divisor C. Hence, up to its fixed one-dimensional factor U/B,

    Q_B = O_X(C),   A_B = O_X(5H-C).

Adjunction gives omega_X=O_X(C), up to a fixed determinant line. On a smooth X, each component C_i is a rational line and the C_i are disjoint, so

    -2=(K_X+C_i).C_i=2 C_i^2,
    C_i^2=-1.

Contracting all25 gives pi:X -> A. Since K_X=C, the canonical blowup formula gives K_A=0. Moreover O_X(C)|C_i=O_P1(-1), so H0(O_X(C))=H0(O_X)=C. Thus p_g=1, and chi(O_X)=0 gives q=2. These are actual canonical/cohomological identities, not a guess from degree. They agree with the abelian classification and exclude the ruled/bielliptic alternatives in ADHPR Proposition2.7.

Set P to be the descended line bundle satisfying

    pi*P = H+C.

It exists because (H+C).C_i=0 for every exceptional curve. Its square is40. It is ample: every curve on A has strict transform T not contained in C, and (H+C).T>0, while P^2>0. Thus (A,P) is the actual polarized abelian surface of type (2,10), with X=Bl_Sigma A for the25 distinct contraction points Sigma.

## 3. A general quadric fiber is the normalization of a 25-nodal divisor

Choose B in T_sm and Q general on the common-good open. D=X_B intersect Q is a smooth integral curve of class2H. It meets each exceptional line twice in distinct points, because ambient quadrics restrict to the complete quadratic system on that line. Under pi, its image Dbar lies in |2P| and has an ordinary node at each point of Sigma. There are no other singularities because pi is an isomorphism away from C and D is smooth there.

The exact numerical checks are

    H^2=15,  H.C=25,  C^2=-25,
    D^2=60,  D.C=50,  deg K_D=110,  g(D)=56.

Equivalently, p_a(Dbar)=1+(2P)^2/2=81 and its25 ordinary nodes lower the normalization genus to56.

Let L be the original tautological quotient class on P_Q(E), pulled back to Xhat. The quotient graph over this B gives

    L|D = Q_B|D = O_D(C)

up to a constant line. This is an identity of quotient line bundles, not an inference from degree. Consequently the twist-four eigenline M=O_Xhat(2L-H) restricts as

    M|D = O_D(2C-H),
    omega_D tensor (M|D)^(-1) = O_D(3H-C).

In particular deg(M|D)=70 and chi(M|D)=15. Every smooth fixed-beta fiber has at least15 sections of M. Fiberwise vanishing is impossible and is not the global full-adjoint criterion.

## 4. Exact 25-point interpolation, with proved dimensions

On A, define the actual fat-point cohomology spaces

    V1(B)=H1(A,P tensor I_Sigma^2),
    V3(B)=H1(A,P^3 tensor I_Sigma^4).

The blowup formula R pi_* O_X(-mC)=I_Sigma^m identifies these with H1(X,H-C) and H1(X,3H-C), respectively. The quadric section corresponds to the actual section

    q_B in H0(A,P^2 tensor I_Sigma^2).

Multiplication by this section, not a generic matrix, gives

    mu_B: V1(B) -> V3(B).

Its dimensions are exactly55 -> 70. Here is a proof rather than an expected fat-point count. The Hilbert–Burch resolution and normalized HM cohomology give, for n=1,3,

    H0(X,nH)=H0(P4,O(n)),
    H1(X,nH)=det B tensor H1(F(3-n))*,
    H2(X,nH)=0.

Thus h0(X,H)=5, h0(X,3H)=35, h1(X,H)=10, and h1(X,3H)=5. The needed H2(F(0))=H2(F(2))=0 follow from the normalized monad; H1(F) and H1(F(2)) have dimensions5 and10 by ADHPR Proposition3.2.

There are no ambient equations of C in degrees1 or3, and the displayed restriction isomorphisms show H0(X,H-C)=H0(X,3H-C)=0. Also H2 of these two line bundles vanishes: Serre duality reduces to negative P powers with effective exceptional summands, whose pushforwards have no sections. Therefore the restriction sequence to the actual25 lines gives exact extensions

    0 -> H1(I_C(1)) -> V1(B)
      -> det B tensor H1(F(2))* -> 0,
    0 -> H1(I_C(3)) -> V3(B)
      -> det B tensor H1(F)* -> 0.

The left dimensions are50-5=45 and100-35=65. This proves55 and70.

Equivalently, on the abelian surface, h0(P)=20, h0(P^3)=180 and positive-degree higher cohomology vanishes. The actual evaluation maps to the25 double and quadruple points are injective, because their section kernels were just proved zero. Their target lengths are75 and250, giving defect dimensions55 and70. This is a proved injectivity statement for these particular evaluations, not an assumption of general-position fat points.

The curve sequence

    0 -> O_X(H-C) --q--> O_X(3H-C)
      -> O_D(3H-C) -> 0

and Serre duality yield natural identifications

    H1(D,M|D)* = ker mu_B,
    H0(D,M|D)* = coker mu_B,
    h0(D,M|D) = 15 + dim ker mu_B.

The rank of mu_B is not asserted.

## 5. The actual five-to-twenty fiber boundary

Write M_n=H1(I_C(n)), and set

    R=coker[q:M1 -> M3],                 dim R=20,
    P0=H1(Q,F_Q(2)),                     dim P0=5.

The established primary injection identifies P0* with ker[H1(F(2))* -> H1(F)*]. The two exact extensions in Section4 form a commutative multiplication-by-q diagram. Its upper map q:M1 -> M3 is injective. Its lower map is the actual dual primary map and is surjective. The snake lemma therefore gives the actual boundary

    delta_B: det B tensor P0* -> R,

with

    ker mu_B = ker delta_B,
    coker mu_B = coker delta_B.

This is an actual5 -> 20 map. It is not the full20 -> 20 boundary evaluated at a randomly chosen matrix, and its injectivity at one or all B would not by itself prove the global conclusion.

## 6. Universalization and the essential parameter-line factors

The universal Hilbert–Burch resolution on P4 times T is

    0 -> det Bcal tensor F(-7)
      -> wedge^2 Bcal tensor O_P4(-5)
      -> I_Scal -> 0.

The middle term must not be replaced by Bcal: a basis makes both three-dimensional on a fixed fiber, but they are different bundles on T.

The resolution remains exact after every specialization B, since each determinantal ideal has height two. The relative local flatness criterion therefore gives the flat universal family; all cohomology computations below commute with base change. For n=1,3 the same calculation makes the Vn into vector bundles on all of T, with exact sequences

    0 -> M_n tensor O_T -> Vn
      -> det Bcal tensor H1(F(3-n))* -> 0.

They are derived from the actual sheaf I_(C times T)/Scal(n), so they continue over Gamma without requiring its quotient line to be invertible there. Multiplication by the fixed q supplies the actual universal V1 -> V3. Taking the preceding snake boundary produces the globally defined bundle map

    delta: det Bcal tensor P0* -> R tensor O_T.

On T minus Gamma, the quotient line is NOT simply O(C) in families. Its canonical residual section belongs to

    Hom(U/Bcal,Q_univ)=Q_univ tensor O_T(-1)

and has divisor C. Hence the exact family identity is

    Q_univ = O(C) tensor O_T(1).

Relative adjunction gives

    omega_Scal/T = det Bcal^(-1) tensor Q_univ,
    omega_Dcal/T = det Bcal^(-1) tensor Q_univ tensor O(2H).

With M=Q_univ^2 tensor O(-H), the parameter twists cancel exactly:

    omega_Dcal/T tensor M^(-1)
      = d^(-1) tensor O_Dcal(3H-C).

The surviving d=det U is constant, whereas O_T(1) is not; dropping the latter prematurely gives a wrong universal boundary.

## 7. Exact global full-adjoint realization

Over T minus Gamma, Dcal=(Scal intersect (Q times T)) is scheme-isomorphic to f^(-1)(T minus Gamma). Indeed the quotient E -> Q_univ defines the graph into P_Q(E); its evaluation-base ideal pulls back to the Cartier divisor Z=(C intersect Q) times T, so the graph lifts uniquely to the evaluation blowup. Conversely (source projection,f) lands in Dcal. Both compositions are the identity off Z and hence everywhere. Locally the universal family is smooth: away from Z it is a projective-line bundle over Q minus Z, and at Z the rank-one normal form and transversality give independent local equations.

The curve sequence of Section4 globalizes over T. Its derived direct image is represented by [V1 -> V3] in degrees0,1. The extensions defining Vn split because Ext^1(O_T(-1),O_T)=H1(O_T(1))=0. After any such splittings, eliminating the acyclic constant upper and lower blocks reduces the complex to

    [det Bcal tensor P0* --delta--> R tensor O_T]

in degrees0,1. The remaining differential is precisely the intrinsic snake boundary, independent of those splitting choices; it is not replaced by a generic map. Relative duality and Section6 therefore identify f_*M on T minus Gamma with the kernel of the dual actual map

    theta: d tensor R* tensor O_T -> P0 tensor O_T(1).

This is a20-by5 bundle presentation, not a numerical dimension analogy. Taking global sections gives

    Theta: d tensor R* -> P0 tensor U,

an actual20 -> 20 map.

There is no missing extension condition at Gamma. Flatness of f makes f^(-1)(Gamma) codimension two in the smooth fourfold Xhat. Hartogs for the invertible M gives

    H0(Xhat,M)=H0(f^(-1)(T minus Gamma),M).

Likewise sections of the constant source of theta over T minus Gamma extend uniquely to T, and the equation theta(s)=0 persists on the closure. Consequently

    H0(Q,End_0(F_Q)(4))
      = H0(Xhat,M)
      = ker[Theta:d tensor R* -> P0 tensor U].

The first equality is the actual quotient-projective-bundle identification pi_*O(2L-H)=Sym^2(E)(-1)=End_0(F_Q)(4), together with blowup invariance of the pulled-back line bundle.

Thus the full-adjoint boundary has a checked realization by the universal25-point abelian interpolation problem. Its residual source is exactly det(U) tensor R*, matching the prescribed source convention, and its target is exactly H1(F_Q(2)) tensor U. The construction comes from actual sheaf sequences and relative duality, not matching two20-dimensional spaces. This supplies its own necessary-and-sufficient map criterion. Literal equality with a differently presented named boundary should be asserted only after fixing the corresponding comparison identifications; the equality of kernels alone would not establish such an equality of maps.

## Boundary

No rank of Theta is proved, and no vanishing of its kernel follows from the55/70 or20/20 counts. Even maximal-rank interpolation on individual smooth fibers would only reduce h0(M|D) to15; a global section can still be a compatible member of those unavoidable fiber spaces. The actual universal boundary/gluing is indispensable.

This result concerns the remaining generic primitive twist-four gate. It does not settle fixed original-source membership, higher lifting, the full repair, or a permission to merge or submit anything. The companion verify_intersection_identities.py checks only the universal integer intersection and jet-length identities; it is not an HM rank certificate.
