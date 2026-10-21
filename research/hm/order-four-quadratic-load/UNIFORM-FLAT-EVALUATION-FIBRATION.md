# Uniform flatness and the integral Gamma inverse image

## 1. Uniform avoidance of surface components

For every three-space B in U, the maximal-minor degeneracy scheme X_B in P4 is pure locally Cohen–Macaulay of dimension two and degree fifteen. This is the all-B statement proved in BETA-DEGENERACY-SURFACE.md Section1, immutable source 26240e70230aef0de1f1b8714a06bd644adeec69. It follows from absence of a common divisorial factor and the local Hilbert–Burch resolution; it does not require X_B to be integral.

The integral components of all these fibers have a constructible parameter space of dimension at most three. Here is the required justification rather than an assumption of a global component labeling. Start over the generic point of an irreducible parameter stratum. Its finitely many geometric integral components are defined over a finite extension of the function field. Spread their closures after the corresponding generically finite base change; after shrinking, their fibers are geometrically integral and give precisely the fiber components. Apply the same procedure to the closed complement. Noetherian induction gives finitely many strata and finite-type generically finite covers of them, each of dimension at most three. This suffices for the incidence dimension estimate, irrespective of monodromy or collisions of components.

Every integral surface T in P4 imposes at least six independent conditions on quadrics. Choose a general linear projection T -> P2 that is dominant. The pullbacks of the six quadratic monomials on P2 are linearly independent on T. Thus the projective space of quadrics containing T has dimension at most 14-6=8.

The incidence of a component T of some X_B and a quadric containing T consequently has dimension at most 3+8=11. Its image closure in the fourteen-dimensional space of quadrics is proper. Choose a smooth quadric Q outside this closure and transverse to the evaluation lines. Then no component of any X_B is contained in Q. Since each X_B is pure locally CM, X_B intersect Q is a pure curve, for every B.

## 2. Every evaluation fiber is one-dimensional

Let X=P_Q(E), let Xhat be the blowup at the fifty simple evaluation base points, and let f:Xhat -> P(U*) be the resolved evaluation map. Off the marked points of Q, evaluation has rank two, and each point of X_B intersect Q determines exactly one quotient in the fiber over B.

At a marked point z, choose a constant basis and frame giving the local evaluation coordinates

    [u : u h_1+a_1 : u h_2+a_2 : u h_3+a_3],

near the quotient base point, with h_i(0)=0 and a_1,a_2,a_3 regular coordinates on Q. The four displayed functions form regular coordinates to first order. On the exceptional P3 the resolved map is therefore a projective linear isomorphism onto P(U*). The strict transform of the original quotient P1 over z maps constantly to κ(z). No other positive-dimensional fiber piece lies over a marked point.

It follows that every f-fiber has dimension exactly one. There are no isolated irreducible fiber components: locally a fiber is cut out by three parameters in the smooth fourfold Xhat, so each component has dimension at least one. Since the target P3 is regular and the source is Cohen–Macaulay, the dimension equality gives flatness by miracle flatness. Its fibers are local complete intersections, hence Gorenstein curves.

## 3. The entire Gamma inverse image is integral

Put S_Gamma=f^{-1}(Gamma). Since Gamma is a smooth curve regularly embedded in P3 in codimension two, flat pullback gives a regular sequence on Xhat. Thus S_Gamma is a locally complete-intersection Cohen–Macaulay surface, flat over Gamma.

For a general modular parameter B, X_B is the integral degree-fifteen scroll. A general quadric cuts an integral curve by Bertini; the incidence and quotient description identifies the generic fiber of the restriction over Gamma with this curve away from finitely many marked parameters. This generic-integrality condition holds on a nonempty open set of choices of Q, so may be imposed along with Section1's uniform avoidance condition.

A finite-type flat scheme over an integral smooth curve with integral generic fiber is integral here. Explicitly flatness makes every nonzero base parameter a non-zero-divisor; hence all associated primes dominate the base. Generic reducedness and absence of embedded primes imply reducedness, and distinct irreducible components would give distinct components in the generic fiber. Therefore S_Gamma is integral. In particular there are no additional raw components supported over cusp parameters.

The compact normalization established in COMPACT-DOMINATING-NORMALIZATION.md is consequently the normalization of the entire S_Gamma, not merely one component:

    S_Gamma^normal = Bl_{50}(W).

This does not say S_Gamma itself is normal or smooth.

## 4. Arithmetic genus and normalization defect

The flat fibration has arithmetic-genus-fifty-six fibers. Write L for the original tautological class, H for the pulled-back quadric hyperplane and A=L-sum E_i. The canonical class of the smooth fourfold is

    K_Xhat=-2L+2H+3 sum E_i.

For a fiber cut out by three target hyperplanes, adjunction gives

    K_fiber=(K_Xhat+3A)|fiber=(L+2H)|fiber.

The projective-bundle relation and c1(E)=5H,c2(E)=10H² give L⁴=50 and HL³=30. Exceptional mixed products with these pulled-back classes vanish. Hence

    deg K_fiber=A³(L+2H)=50+60=110,
    p_a(fiber)=56.

Independently, X_B has Hilbert polynomial (15n²-25n)/2, so its proper quadric section has polynomial 30n-55, giving the same arithmetic genus.

Over a general point of Gamma, the normalized fiber is the genus-sixteen quadric section of the normalized elliptic scroll. Therefore its normalization quotient has length

    delta=56-16=40.

This is a new conductor-size constraint. Flatness does not remove this nonnormality; rather, it makes the genus discrepancy precise. No conclusion about the final eigenquotient obstruction or a complete proof repair is asserted.

## 5. Global Euler characteristic and conductor class

For n nonnegative, the blowup pushforward formula and the length of a four-dimensional point jet give

    χ(O_Xhat(nA))=χ_Q(Sym^n E)-50 binom(n+3,4).

Riemann–Roch on Q, with td(Q)=1+(3/2)H+(13/12)H²+(1/2)H³ and H³=2, yields

    χ_Q(Sym^n E)=(n+1)(5n+3)(5n²+4)/12,
    χ(O_Xhat(nA))=−55n³/6−20n²−59n/6+1.

In particular A² td_2(Xhat)=−40 and A³ td_1(Xhat)=−55. The smooth rational sextic has Chern character 6a²−11a³ in P3, since its degree is six and its Euler characteristic is one. Flat pullback and Riemann–Roch therefore give

    χ(O_S_Gamma)=6(−40)−11(−55)=365.

The normalization Bl50(W) has χ(O)=55. Its normalization quotient N=ν_*O_normal/O_S_Gamma consequently satisfies

    χ(N)=−310.

Its generic fiber length is forty by Section4. No claim that N is flat or finite over Gamma at every cusp is needed for this Euler-characteristic identity.

Finally det N_Gamma/P3=O_P1(22), by the tangent-normal sequence. Adjunction on S_Gamma and the established tautological formulas imply

    ν^*K_S_Gamma=π^*(5I+10F)+2h−sum F_i.

Since the target is Gorenstein and the normalization is smooth, its conductor divisor has class ν^*K_S_Gamma−K_normal, namely

    Δ=2G,     G=π^*H+h−sum F_i.

Here equality denotes divisor class; identification with a particular graph divisor requires a separate argument. The intersection numbers are G²=160, G.K_normal=320 and p_a(G)=241. These follow from (π^*H)²=30, (π^*H).h=60, h²=60 before the fifty blowups. This conductor class is compatible with, but does not by itself prove, a doubled graph description.
