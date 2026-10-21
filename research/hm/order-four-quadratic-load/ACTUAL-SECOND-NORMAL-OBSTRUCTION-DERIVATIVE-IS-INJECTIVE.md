# The actual second-normal obstruction has injective invariant derivative

## Theorem

Let Q=Q0, Q1=2Q=(q0^2=0), Q2=3Q=(q0^3=0), and E=F|Q. Fix determinants and the identification with E on Q. The equivariant first-normal extension torsor has tangent

    T=H1(Q,B_Q(-2))^G=C.

Use the ACTUAL first-normal extension F|Q1 as the origin of this torsor. It extends to Q2, supplied by the actual ambient F. Let

    ob:T -> H2(Q,B_Q(-4))^G

be the obstruction to extending the corresponding first-normal bundle to Q2. Then its derivative at the actual point is the canonical composite

    D:T --delta_amb--> H2(P4,B(-4))^G
          --restriction--> H2(Q,B_Q(-4))^G.                     (1)

The first arrow is the already proved isomorphism, and the second is injective. The target is in fact one-dimensional by the independent character calculation below. Therefore D is an isomorphism and NONZERO.

Consequently the actual first-normal extension is an isolated REDUCED point of the locus of those extending to Q2. More precisely, after choosing a generator eta of T and its affine coordinate s, the exact obstruction has the form

    ob(s)=s D(eta)+s^2 Q(eta),                                  (2)

for a fixed class Q(eta) in the same obstruction space. Thus at most one OTHER first-normal extension can extend to Q2. Its existence is not asserted. No third-Bockstein nonvanishing follows merely from this derivative.

## 1. Which derivative is the normal obstruction

The sheaf of first-order variations of E on Q1 which are zero on Q is B_Q(-2). A lift of such a variation to Q2 must take values in the sheaf

    q0 B|Q2 = B|Q1(-2).

The equality includes the natural parameter line: multiplication by q0 identifies O_Q1(-2) with its image ideal in O_Q2. Its restriction exact sequence is

    0 -> B_Q(-4) -> B|Q1(-2) -> B_Q(-2) -> 0.                  (3)

A representative eta of a first-normal variation can be lifted locally to the middle sheaf. Its coboundary takes values in the left sheaf. This is precisely the first-order failure of the varied transition functions to glue on Q2. Thus the connecting homomorphism of (3) is the derivative of the extension obstruction at the actual Q1 bundle.

This statement concerns the derivative at the actual extension, not a purported canonical origin for the full extension torsor. We deliberately use the existing ambient F to supply this origin and the actual middle sheaf in (3).

There is a commutative diagram of actual sheaf extensions

    0 -> B(-4)   -> B(-2)     -> B_Q(-2) -> 0
          |            |             ||
    0 -> B_Q(-4) -> B|Q1(-2)  -> B_Q(-2) -> 0.

The first two vertical arrows are restriction. Naturality of connecting homomorphisms proves (1). In particular the ambient connecting map alone has a different target and must NOT be identified with the normal obstruction derivative before this comparison.

## 2. The derivative survives restriction

NEGATIVE-MONAD-INVARIANT-SCALAR-IS-NONZERO.md proves

    H1(B(-2))^G=H2(B(-2))^G=0,
    T --delta_amb--> H2(B(-4))^G=C

is an isomorphism.

The other needed ambient input is the established structural twist-one vanishing H2(B(1))=0. Since B is self-dual and omega_P4=O(-5), Serre duality gives

    H2(B(-6))=H2(B(1))*=0.                                    (4)

The restriction sequence B(-6)->B(-4)->B_Q(-4) therefore makes

    H2(B(-4)) -> H2(B_Q(-4))                                  (5)

injective, even before taking G invariants. Combining (5) with the invariant isomorphism gives the claimed nonzero derivative. This proves nonvanishing without needing a target dimension calculation. The companion FINITE-NORMAL-TOWER-AND-THREE-SCALAR-GATES.md, Sections3 and5, now independently checks H1(B(1))^G=0 from the actual monad character. The cokernel of (5) on invariants lies in H3(B(-6))^G=H1(B(1))^{G,*}=0. Consequently H2(B_Q(-4))^G is exactly one-dimensional and D is an isomorphism.

Provenance of the twist-one input: LOWEST-COKERNEL-SUMMANDS-EXCEPTIONAL-BOUNDARY.md, final Sources section, and FIXED-CONIC-PARITY-JETS-AND-POSITIVE-GATE.md cite the structural proof at PR455, immutable commit 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4, research/hm/twist-one-structural-vanishing/PROOF.md. This is an established input, not a newly evaluated matrix.

## 3. Exact quadratic dependence and the finite ambiguity

Choose local frames of the actual F on Q2. On Q1 an arbitrary equivariant extension with fixed reduction is obtained by modifying its transitions by a normal factor whose coefficient is s eta. Because the normal ideal of Q in Q1 has square zero, these modifications define the whole affine torsor, with no quadratic gluing equation at that stage.

To test extension to Q2, lift eta locally one normal order farther, as a trace-free endomorphism in the indicated twisted frames. Modify the actual transitions using

    exp(s q0 eta_tilde)
      =1+s q0 eta_tilde+(s^2 q0^2/2) eta_tilde^2 modulo q0^3.

This determinant-one correction preserves the fixed ambient determinant line. On Q1 it is exactly the prescribed first-normal family. Triple transition products have a linear term from the lifted coboundary and a quadratic term from two first-normal coefficients, including the displayed determinant correction. Products of three first-normal factors vanish modulo q0^3. The defect therefore has the form 1+q0^2(s C+s^2 Q) with no higher power of s; because its determinant is one, its coefficient is trace-free. The constant term vanishes because the reference ambient bundle actually extends. Its linear class is D(eta) by Section1. This proves (2).

Here are the needed independence checks. Changing eta_tilde by a multiple q0 nu changes the linear defect by the coboundary of nu. Changing the Q2 transition corrections by arbitrary second-normal terms changes the defect by their coboundaries. Changing eta by a coboundary is implemented by the local gauge exp(s q0 lambda), with its own order-two correction retained. Since the obstruction lies in the q0^2 ideal and this gauge reduces to identity on Q, its action on the obstruction coefficient is trivial; any change of the chosen higher lift again contributes a coboundary. Thus the cohomology obstruction is independent of these choices, with its target canonically identified by the fixed reduction to E. A change of affine coordinate on the first-normal torsor does not increase the polynomial degree.

The quadratic class is the usual cup/bracket expression in compatible exponential/dg conventions, but its precise normalization is immaterial for the finite bound. Determinant corrections and local gauge terms have been included before imposing that bound, rather than discarded as if they vanished separately.

For s nonzero, ob(s)=0 requires

    D(eta)+s Q(eta)=0.

Since D(eta) is nonzero, there is at most one such s. There is no second solution if Q is zero or is not proportional to D. If Q is a nonzero multiple of D, there is exactly one possible nonzero s, and vanishing of this square-zero lifting obstruction is the standard sufficient gluing criterion for extension to Q2. Equivariance introduces no additional obstruction in characteristic zero, by exactness of finite-group averaging.

The actual point is reduced even scheme-theoretically: one component of ob(s) has nonzero linear coefficient, so in the local ring at s=0 its equation is s times a unit and generates the maximal ideal. The zero scheme of the vector-valued degree-two polynomial has length at most two, since at least one component is a nonzero polynomial of degree at most two. This claim concerns the first-normal lifting locus in its affine torsor, not a fine moduli scheme of all choices of second-normal extensions.

There is also uniqueness of the second-normal lift, in the correct marked sense. The same restriction long exact sequence gives

    H1(B(-4)) -> H1(B_Q(-4)) -> H2(B(-6)).

The right group vanishes by (4), and the left vanishes by Serre duality from H3(B(-1))=0, proved in PR455 and recorded in FIXED-CONIC-PARITY-JETS-AND-POSITIVE-GATE.md. Hence H1(B_Q(-4))=0, even before invariants. Once the obstruction vanishes, isomorphism classes of fixed-determinant lifts of a given first-normal bundle, with an identification of their restriction to that first-normal bundle, form a torsor under this zero group. Therefore every liftable first-normal point has exactly one marked second-normal isomorphism class. The companion finite-normal-tower theorem also proves H0(B_Q(-4))=0, so the marked isomorphism inducing identity on the first-normal restriction is itself unique. No existence of an additional global ambient bundle is asserted.

## 4. Precise mismatch with the positive cubic gate

The cubic gate has target P=H1(B_Q(4))_+, modulo the actual second-symbol image. The nonzero normal derivative has target H2(B_Q(-4))^G. These are different cohomological degrees as well as different twists.

The ordinary polynomial expression with the required degree in the direction and source, a^3 h, has ordinary degree8. Multiplying D(eta) by it gives

    a^3 h D(eta) in H2(B_Q(4))_+=0,                            (6)

where the vanishing is part of the proved invariant-cone rank33 theorem. Therefore PRIMARY polynomial multiplication of this nonzero derivative cannot be the cubic gate: it lands in zero and never lowers cohomological degree. Likewise a bare invocation of the connecting isomorphism (1) supplies no homotopy or contraction that lowers degree2 to degree1.

The affine secondary-variation map L:T->C^2 constructed in POSITIVE-SECONDARY-TENSOR-NORMAL-VARIATION.md instead uses the actual adjoint action and choices of primitives whose resulting ambiguity vanishes. Its formula involves the cochain tau satisfying d tau=-[eta,c]. The injectivity of D does not imply injectivity or nonvanishing of L, nor an equality between the actual absolute cubic value and either derivative.

A future comparison could relate these maps through a genuine secondary operation, but must construct that operation and verify its choice corrections. Mere one-dimensionality of T or availability of the nonzero class D(eta) is insufficient. Equation (6) explicitly rules out the naive ordinary-multiplication comparison.

## Evidence and scope

The derivative formula is proved by local transition variation and the displayed exact diagram. Its nonvanishing uses only already established monad cohomology, twist-one vanishing, and Serre duality. The quadratic bound uses the actual nilpotence order q0^3, not a local-model experiment. The companion verifier checks formal order bounds, the duality twist, and the elementary quadratic zero-set deduction. No actual coefficients, actual matrix evaluations, rank scans are used.
