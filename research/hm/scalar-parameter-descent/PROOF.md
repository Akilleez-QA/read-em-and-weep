# Polynomial parameter descent of the intrinsic fourth-square scalar

## Result and fixed dependencies

Work over C with the actual marked bundle F on X=P4, B=End_0(F), and the integral rank-three quadric Q=(q=0). All spaces below retain the physical-center-even summand. Write W for the negative-coordinate binary representation, U for its Galois-conjugate positive-coordinate binary representation, A=Sym^2 W, D=D5=Sym^4 U, V=Sym^2 U, and P=P4. In particular A and V are different three-dimensional representations. The physical involution is not the extra Serre involution.

We prove that the intrinsic section rho4 of PR691 is a Gamma-equivariant polynomial function of (a,h), of bidegree (3,1), with values in the fixed 27-dimensional target of PR692:

    rho4 : A x D -> T = Sym^8 U tensor Sym^2 W.

Consequently its possible equivariant family space has dimension23. Restriction to all square directions a=ell^2 has kernel dimension7 and quotient dimension16. These are dimensions of spaces of possible families, not an evaluation, rank, nonvanishing or vanishing of the actual family.

The fixed dependencies are:

- [The actual fourth-neighborhood ladder](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md): actual global completions exist and dU_a=q^2 Z_a, with U_a and Z_a linear in a; b=L_can(a,h) is bilinear.
- [PR685](https://github.com/Akilleez-QA/read-em-and-weep/pull/685), commit [449a8df60662bd7a1d93e318ea4f7e6dab28e5ad](https://github.com/Akilleez-QA/read-em-and-weep/commit/449a8df60662bd7a1d93e318ea4f7e6dab28e5ad): every even completion gives square-zero J3; every such aJ3 extends to4Q, including after changing the divided class, by the explicit correction -q^2 U_a s.
- [PR687](https://github.com/Akilleez-QA/read-em-and-weep/pull/687), commit [2874402c884a6b426cfd521a674c962a738f84a6](https://github.com/Akilleez-QA/read-em-and-weep/commit/2874402c884a6b426cfd521a674c962a738f84a6): J4^2=q^3 S4 Id defines S4 intrinsically, independently of the even completion and fourth lift.
- [PR691](https://github.com/Akilleez-QA/read-em-and-weep/pull/691), commit [dac9a7eca25d112dff9702ec863d161709792326](https://github.com/Akilleez-QA/read-em-and-weep/commit/dac9a7eca25d112dff9702ec863d161709792326): for nonzero a,h, S4=a^3 h rho4 with unique rho4 in H0(O_Q(6))_+, and rho4 lies in I^2 on the smooth locus.
- [PR692](https://github.com/Akilleez-QA/read-em-and-weep/pull/692), commit [858f96ba1539afb1293f31239b8761af08e46f60](https://github.com/Akilleez-QA/read-em-and-weep/commit/858f96ba1539afb1293f31239b8761af08e46f60): each such rho4 lies in the single fixed polynomial block T.

The linear dependence of U_a is given explicitly by [the canonical multiplied-lift theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md). Since dU_a=q^2 Z_a and division by the fixed q^2 is injective on the relevant global cochain spaces, Z_a is linear as well.

The bilinear correction b=L_can(a,h) is the compatible fixed-probe correction of [the polynomial third-vanishing theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md), sections 2 and 3: its bundle map D tensor O(-3) -> A tensor O(-2) is linear in a and in h.

The new issue here is regularity in the source parameters. Pointwise division on Q alone does not establish that regularity.

## 1. Polynomial actual fourth lifts exist

We use one elementary finite-dimensional fact. If L:E->F is a fixed equivariant linear map and a homogeneous polynomial f on a vector space has values in im L, then it has a homogeneous polynomial lift through L of the same degree. Indeed choose a linear section of E->im L and average it over the finite group Gamma. Equivalently polarize f and use exactness of Hom_Gamma(-,-). If the image condition is known on a dense open set, projection to F/im L is a polynomial vanishing on that open set, hence identically zero. The same statement holds for multihomogeneous polynomials.

Apply this to the fixed finite-dimensional global monad-cochain map

    L(C,V)=dC+qV,

where C has degree zero and twist4 and V is a closed degree-one cochain of twist2. Work in the fixed trace-free duality and even summands. The right side f(a,h)=a h Z_a has bidegree(2,1), and belongs pointwise to im L by the actual ladder. Therefore choose equivariant polynomial (C(a,h),V(a,h)) of bidegree(2,1). Taking the induced actual section gives the polynomial family

    J3=(a h-q b)U_a-q^2 C in H0(B_(3Q)(8)),

also of bidegree(2,1). Inducing a bundle endomorphism from a closed restricted cochain is a fixed linear map, so it does not alter this parameter degree.

Now use a second FIXED finite-dimensional linear map, the restriction

    R:H0(B_(4Q)(10))_+ -> H0(B_(3Q)(10))_+.

The polynomial aJ3 has bidegree(3,1). PR685's explicit compatible correction proves that it lies pointwise in im R for every nonzero source pair, even for our chosen completion rather than only for the original ladder completion. The finite-dimensional lemma gives a Gamma-equivariant polynomial actual section J4 lifting aJ3, of bidegree(3,1).

This deliberately uses actual section spaces for the last lift. No family of arbitrarily chosen pointwise primitives E or W is assumed polynomial. All choices used are fixed linear splittings in finite representations, not parameter-dependent inverses. No actual splitting coefficients are evaluated. In particular no compatibility of an arbitrary cochain choice with an unevaluated higher primitive is presumed.

The square J4^2 has bidegree(6,2). It vanishes on3Q because J3^2=0; taking the unique last-layer scalar S4 is a fixed linear operation. Thus

    S4 in H0(O_Q(14))_+ tensor Sym^6(A*) tensor Sym^2(D*).

Choice independence from PR687 makes this polynomial family intrinsic. The polynomial extension also defines zero-source values without invoking division there.

## 2. No poles in source parameters

Put Y=P(A) x P(D), with projective spaces parametrizing lines. For m>=0 write H_m=H0(O_Q(m))_+. The universal multiplication by the source section a(x)^3 h(x) defines a bundle map on Y

    M:H_6 tensor O_Y(3,1) -> H_14 tensor O_Y(6,2).

Both a and h restrict nontrivially to Q for every projective parameter: their indicated summands inject into H0(O_Q(2)). Since Q is integral, their product is nonzero and multiplication by it is injective on every H_6 fiber. Hence M has constant rank dim H_6, its image is a vector subbundle, and its cokernel is locally free. This constant-rank statement concerns a universal multiplication map, not a selected actual HM matrix or rank calculation.

The polynomial S4 is a global section of the target bundle. PR691 says its value lies in im M in every fiber. Its projection to the locally free cokernel therefore vanishes at every closed point of the reduced variety Y; the section is zero. Thus S4 has a unique global preimage in H_6 tensor O_Y(3,1). Using

    H0(Y,O_Y(3,1))=Sym^3(A*) tensor D*,

we obtain a polynomial rho4 of bidegree(3,1), without any parameter denominators. Uniqueness and equivariance of M and S4 imply equivariance of rho4. Each value lies in T by PR692. The projection to H_6/T is a polynomial zero on all nonzero source pairs and therefore zero identically, so the whole family lands in T.

This is descent on the smooth parameter variety Y. It is not a Hartogs argument for the nonreflexive ideal I^2 on singular Q. No membership in I^2 at the vertex follows from this proof.

## 3. The exact equivariant family and discriminant sequence

Over Gamma the abstract decompositions are

    Sym^8 U = P + D,
    T = A + 2V + 2P + 2D,
    Sym^3 A tensor D = 3A + 3V + 3P + 4D.

Therefore

    dim Hom_Gamma(Sym^3 A tensor D,T)=3+6+6+8=23.

All displayed irreducibles are self-dual, but the polynomial family is naturally in T tensor Sym^3(A*) tensor D*, or equivalently the Hom space just written. Self-duality is not being used to identify parameter vectors with coordinate functions without qualification.

Let Delta be the discriminant quadratic on A=Sym^2 W. The Veronese conic of square binary quadratics is cut out by Delta. Restriction of cubic polynomial functions to this conic gives the exact equivariant sequence

    0 -> Delta A* -> Sym^3(A*) -> Sym^6(W*) -> 0.

Indeed the conic has principal homogeneous ideal (Delta), and O_P(A)(3) restricts to O_P(W)(6); dimensions are3,10,7. Tensor with T and D*, then take Gamma invariants. Exactness is preserved because Gamma is finite in characteristic zero. Hence restriction of possible rho4 families to all square directions is surjective, and its kernel consists EXACTLY of

    rho(a,h)=Delta(a) L(a,h),
    L in Hom_Gamma(A tensor D,T).

The decomposition A tensor D=A+V+P+D gives kernel dimension1+2+2+2=7. The square-direction family space has dimension23-7=16; equivalently

    dim Hom_Gamma(Sym^6 W tensor D,T)=16.

Thus vanishing on all square directions would only force the actual family to be Delta times an unknown bilinear family in a seven-dimensional possible space. It would not by itself prove rho4=0. Conversely any actual nonzero restriction would prove rho4 nonzero. Neither test has been evaluated here, and no square direction has been selected or evaluated.

## Scope and reproduction

Run python verify.py. It uses exact arithmetic in Q(sqrt5) on nine abstract binary-icosahedral conjugacy classes to check the representations and dimensions above. It checks no actual HM coefficient, point, derivative, source instance, or matrix. The geometric descent is a written proof, not a formal proof-assistant check.

The remaining mathematical question is the actual element of this 23-dimensional space, including its seven-dimensional discriminant-multiple ambiguity after square restriction. The vertex I^2 condition, scalar vanishing, the fourth Bockstein value, higher-order unobstructedness, and algebraicity remain unresolved. None is identified with the dimensions proved here.
