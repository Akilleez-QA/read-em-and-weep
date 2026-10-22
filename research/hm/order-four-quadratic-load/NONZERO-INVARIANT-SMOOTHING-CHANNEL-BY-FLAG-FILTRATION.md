# The invariant projected smoothing channel is nonzero

## Theorem

The actual conic-factorization constraint T from INVARIANT-BOUNDARY-TRANSVECTANT-AND-REMAINING-TEST.md is injective, hence an isomorphism between its three-dimensional spaces. Its proof is a filtration argument on the actual canonical (3,3) curve, not a matrix evaluation or a generic-rank assertion.

Consequently:

1. For every nonzero equivariant quotient rho:C_lin->O_T(2), the invariant-positive coefficient lambda_rho is nonzero.
2. The quotient space Hom_G(C_lin,O_T(2)) has dimension exactly one. Thus the quotient and its kernel are canonical up to scalar; the remaining splitting candidates with two independent such quotients are excluded.
3. The actual invariant-positive projected multiplication is a nonzero scalar times

       Disc times psi(-2): A tensor K(1) -> S3,

   with psi:A tensor K(3)->S3 the canonical everywhere-surjective map. Therefore its rank is two off the discriminant, it vanishes to exactly first order on the discriminant, and after removing that factor it is surjective everywhere.
4. On a general smooth inversion-even quadric, h0(B_Q(4))_-<=4. This improves the previous upper bound six. It does not prove odd vanishing or complete the full-adjoint maximal-rank question.

The signed deformation Bockstein differs from positive multiplication by the previously fixed overall minus sign. The nonvanishing and rank conclusions are unchanged.

## 1. Actual inputs and notation

Let X=T x C0=P(W*) x P(W'^*). Write O_X(a,b) for degree a on T and degree b on C0. The established actual evaluation is

    e:W tensor O_X(-3,0) -> W tensor O_X(0,3).

The invariant equation Phi of the actual smooth canonical curve B has bidegree (3,3). The Cartan formula is

    e=(Phi Id+3 ell tensor r)/4,       r(ell)=Phi.     (1)

Thus e preserves the tautological ell-line, with diagonal factors Phi and Phi/4. Its determinant is Phi^2/4.

On B let M=O_X(1,0)|B, N=O_X(0,1)|B. The actual factor-cover theorem gives

    deg M=deg N=3,      K_B=M+N,
    tau=M-N has exact order five,
    B/A5 has signature (2,5,5).

In particular the two ramification orbits R_M,R_N have degree twelve, and the only other nontrivial stabilizer orbit has degree thirty. The corresponding classes are

    R_M=K_B+2M=4M-tau,
    R_N=K_B+2N=4M-3tau=4M+2tau.                     (2)

The actual plane boundary H0(B_R(5)) O_T->C_lin(2) is everywhere surjective. The earlier transvectant theorem says that for a nonzero quotient rho, its projected map b_rho is nonzero, and lambda_rho=0 exactly when b_rho factors through H0(B_C0(5)). The remaining annihilation constraints are the actual map T studied next.

## 2. Realize the remaining constraint as a cokernel cohomology group

Multiplying the symmetric square of e by the conic degree-four line gives the actual family of restricted moving square products

    A tensor O_X(-6,4)
       --Sym^2 e--> A tensor O_X(0,10),
    A=Sym^2 W.

At a fixed ell, this sends a square of the actual two hyperplane sections times a positive quadratic restricted to C0 to its section in B_C0(5).

Dualize this map and tensor by O_X(4,-2), where O_C0(-2) is the canonical bundle of the conic parameter P1. Define F by the exact sequence

    0 -> A tensor O_X(4,-12)
      --(Sym^2 e)^vee--> A tensor O_X(10,-6)
      -> F -> 0.                                    (3)

The left map is injective because its determinant is nonzero. The invariant pairings identify A* with A; this changes no line factor.

Both vector-bundle terms in (3) have no H0, because their C0 degrees are negative. Kunneth and Serre duality on C0 identify the invariant part of their H1 map with

    T:Hom_G(H0(B_C0(5)),D)
       -> Hom_G(A tensor D,Sym^10 W),
    D=Sym^4 W=H0(O_T(4)).                            (4)

Indeed the first H1 has conic factor H1(O(-12))=H0(O(10))* and parameter factor H0(O(4)); the second has H1(O(-6))=H0(O(4))* and parameter factor H0(O(10)). The arrow is dual to the actual symmetric-square evaluation and conic multiplication, exactly the map defining the moving-square constraint. It is not a newly assigned arrow between those representations.

The long exact sequence of (3), followed by exact finite-group invariants, consequently gives

    ker T = H0(X,F)^G.                              (5)

It remains to prove that the right side is zero.

## 3. A strict tautological filtration of F

The constant two-space W over T has its tautological filtration with graded line bundles O_T(-1),O_T(1). Its symmetric square A has the induced three-step flag with graded line bundles

    O_T(-2),       O_T,       O_T(2).                (6)

Under the symplectic identification W*=W, the transpose of e is its symplectic adjoint. In a local basis beginning with ell, e is upper triangular with diagonal Phi,Phi/4; its symplectic adjoint is still upper triangular, now with diagonal Phi/4,Phi. Hence the apolar transpose of Sym^2 e preserves (6), with graded maps nonzero constant multiples of

    Phi^2,       Phi^2,       Phi^2.

The scalar factors can be taken as 1/16,1/4,1; only their nonvanishing matters.

Apply this flag to both terms of (3). Every associated graded map is injective as a sheaf map on the smooth integral surface X, since it is multiplication by the nonzero section Phi^2. Therefore the induced cokernel filtration is strict, and its three graded pieces are

    O_(2B)(8,-6),       O_(2B)(10,-6),
    O_(2B)(12,-6).                                  (7)

For example, the first is the cokernel of O_X(2,-12)->O_X(8,-6); their difference is (6,6), the divisor 2B. This explains all twists in (7). The special rank-zero points of e do not invalidate the filtration: multiplication by Phi^2 remains an injective sheaf map at those points.

Since G is finite over C, taking invariant sections is exact on representations. It is enough to prove that each graded sheaf in (7) has no invariant global section.

## 4. Both layers of every doubled-curve graded piece have no invariants

For t=8,10,12 the square-zero sequence of B inside 2B is

    0 -> O_B((t-3)M-9N)
      -> O_(2B)(t,-6)
      -> O_B(tM-6N) -> 0.                           (8)

### The nilpotent layers

Their degrees are -12,-6,0, respectively. The first two have no sections at all. The last is

    O_B(9M-9N)=O_B(9tau),

a nontrivial degree-zero line bundle because tau has exact order five. It too has no sections.

### The reduced layers of degree six and eighteen

For t=8 and t=12, the reduced layers have degrees six and eighteen. A nonzero invariant section would have an invariant effective divisor of that degree. By the actual signature (2,5,5), the possible point-orbit degrees are 12,12,30,60. Neither six nor eighteen is a nonnegative sum of these orbit degrees. Thus neither line bundle has an invariant section.

### The reduced layer of degree twelve

For t=10 its class is

    10M-6N=4M+6tau=4M+tau.                          (9)

An invariant effective divisor of degree twelve must be exactly R_M or R_N. Their classes in (2) are 4M-tau and 4M+2tau. Both differ from (9) by a nontrivial multiple of the exact order-five class tau. Hence (9) cannot have an invariant section either.

These arguments use the actual line-bundle classes, not merely their degrees. G-linearizations cannot remove the discrepancy: G is perfect, and the bundles in (8) have trivial central action, so an invariant section gives precisely such an A5-invariant divisor.

It follows from (8) that every graded sheaf in (7) has zero invariant H0. The strict filtration then gives H0(F)^G=0. By (5), T is injective. Its two spaces were independently identified as dimension three, so it is an isomorphism.

## 5. Nonzero scalar and uniqueness of the quotient

Suppose rho is a nonzero equivariant quotient and lambda_rho=0. The transvectant theorem then makes the nonzero actual projected plane boundary b_rho factor through H0(B_C0(5)). Its actual moving-square annihilation puts that nonzero factorization in ker T, contradicting the injectivity just proved. Hence

    lambda_rho != 0 for every nonzero rho.           (10)

The assignment rho |-> lambda_rho is linear after fixing the harmless common normalizations. It is therefore an injective map

    Hom_G(C_lin,O_T(2)) -> C.

The source is nonzero by the checked splitting-constraint theorem, so it has dimension exactly one. This removes the two-quotient alternatives without selecting an actual splitting.

The small-channel theorem already identified the actual invariant-positive map as lambda_rho Disc psi(-2), with psi everywhere surjective. Combining it with (10) proves the asserted exact rank and discriminant multiplicity. This is an actual nonvanishing result obtained from the flag and divisor argument, not from the existence of a possible nonzero Hom component.

## 6. Consequence for smooth even quadrics

Fix any nondegenerate negative quadratic q_-. Its reducible quadric D has the established six-dimensional odd section space, and its actual first smoothing obstruction has target dimension ten. For the positive invariant quadratic q0, the rank-two quotient just proved shows that the full first obstruction has rank at least two. Thus its kernel has dimension at most four.

Consider the actual family

    D_s=(q_-+s q0=0).

For s!=0 it is a smooth inversion-even quadric. Proper cohomology and the first-order lifting condition imply that a general nearby fiber has odd section dimension at most the dimension of the kernel of the first obstruction, hence at most four. More concretely, the two independent first-order obstructions give a nonzero rank-two minor in the reduced deformation presentation; they cannot disappear on every nonzero parameter.

No chosen parameter or actual coefficient is evaluated in this argument. Since the smooth-even parameter space is irreducible and odd cohomology is upper semicontinuous, this proves

    h0(B_Q(4))_- <= 4

for a general smooth even quadric. The remaining four source directions, and the remaining positive excess question, are not settled here. In particular this is not a proof of odd vanishing or of exact full corank four.

## 7. The exact remaining four-to-eight bundle map

Let K8 be the kernel of the now unique projective quotient C_quad->S3. It is a vector bundle of rank eight. The canonical factor sequence, twisted by O_P(-2), is

    0 -> W tensor S6* -> A tensor K(1)
      --psi(-2)--> S3(-2) -> 0.                     (11)

The projected actual multiplication is lambda Disc psi(-2). Since lambda is nonzero and multiplication by Disc is injective as a sheaf map into the locally free S3, the full actual map restricts to

    m_res: W tensor S6* -> K8.                       (12)

Indeed (12) is obtained simply by restricting the original map to the kernel in (11); its image is in K8. As sheaves on all of P, the kernel of the original invariant-positive map equals ker(m_res). At every point off the discriminant, the full fiber map is injective if and only if the residual four-to-eight fiber map is injective. Along the discriminant the rank-two projected map vanishes, so this fiberwise equivalence must not be asserted there.

The exact Chern data are

    rank(W tensor S6*)=4,   c1=-10h,   c2=55h^2,
    rank(K8)=8,            c1=24h,    c2=300h^2.      (13)

For the source, S6 has Steiner presentation 5 O(-1)->7 O and therefore c1=5h,c2=15h^2; two copies of its dual give (13). For the target, c1(C_quad)=26h,c2(C_quad)=351h^2 and c1(S3)=2h,c2(S3)=3h^2 give c1(K8)=24h and c2(K8)=351-3-48=300.

There is a precise geometric interpretation over two distinct roots. The residual-root involution in psi exchanges target branches, but its kernel is simply the evaluation kernel at each source root. Under the invariant apolar identification, at ell this is

    ker[A=Sym^2 W -> O_T(2)|ell]=ell W.

The square map from Y_ell=ell^3 W sends this two-space to

    (ell^4) times Y_ell subset Sym^2 Y_ell.

Thus the remaining two directions at each root are exactly the square products containing the actual distinguished vertex-vanishing section ell^4. The normal-coordinate and complementary-root factors in the root source are invertible for distinct roots and do not alter this kernel identification. No assertion is made that these four surviving directions lift, or that the residual map is injective.

## Dependencies and scope

The actual Cartan evaluation, smooth canonical incidence, ramification classes and residual-chord identification are recorded in [ACTUAL-CHORD-INCIDENCE-AND-CONIC-EVALUATION.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/06ed0e4402d4bc4c408e7709b6396dabe0da67aa/research/hm/order-four-quadratic-load/ACTUAL-CHORD-INCIDENCE-AND-CONIC-EVALUATION.md) and its factor-cover sources. The exact projected transvectant and T are in INVARIANT-BOUNDARY-TRANSVECTANT-AND-REMAINING-TEST.md. The quotient, finite-duality twists and canonical surjection psi are in PROJECTED-SMALL-CHANNEL-AND-DISCRIMINANT-FACTOR.md. Uniform plane-boundary surjectivity is the checked SURJECTIVE-PLANE-BOUNDARY-BY-CONIC-RESIDUALS.md theorem.

The proof uses the exact order-five class and the two actual degree-twelve orbits. It retains the nilpotent layer of 2B and the apolar-transpose flag; dropping either would leave a gap. No selected HM coefficients, actual matrix evaluation, numerical rank test, or generic-map assumption occurs.
