# The actual determinant factors are residual chords of the canonical incidence

## Theorem

Let R be the positive fixed plane, C0 its invariant smooth conic, and T=P(W*) the negative hyperplane pencil. Let B be the actual determinant line-factor cover, with its established canonical realization

    B subset T x P(W'^*),         bidegree (3,3),
    M=pi*O_T(1),   N=the other ruling,   tau=M-N,
    K_B=M+N,       tau has exact order five.

Identify P(W'^*) with C0. The actual polarization of the six-nodal sextic factor map is L=K_B+2tau=3M-N.

There is a canonical, up to a common nonzero scalar, invariant bidegree-(3,3) form Phi(ell,x). Its zero curve is exactly B, not a second curve with the same numerical class. It arises directly from restriction of the actual plane bundle to C0. The following statements hold.

1. The actual determinant cubic, restricted to C0, is a nonzero scalar times Phi(ell,-)^2.
2. The actual line factor indexed by (ell,x) in B is the residual chord defined by the binary quadratic Phi(ell,-)/linear_x. Thus a general determinant is the triangle joining the three distinct conic points in the fiber. It is not the three tangents at those points.
3. At a branch fiber 2x+y, the determinant is the double chord through x,y together with the tangent at x. This is the established double-polar-plus-tangent special member.
4. On T x C0 the actual two-section evaluation Y->F_R(2)|C0 has rank two off B, rank one on B away from R_N, and rank zero exactly on the reduced twelve-point divisor R_N, the ramification of the other ruling B->C0. Its determinant divisor is 2B. The rank-zero assertion is scheme-theoretic.

A square restriction of a product of three distinct lines does not imply that each line is tangent: the sides of an inscribed triangle give the same square restriction. This distinction is essential here.

## 1. The actual fiber representation on the invariant conic

Put E=F_R(2). The established balanced invariant-conic theorem gives E|C0=R2 tensor O_P1(3) for a two-dimensional G=SL(2,5) representation R2. The center acts trivially on E over the fixed plane, and by minus one on O_P1(3). Thus R2 has odd center and is W or W'. It cannot be a sum of one-dimensional representations, since G is perfect.

The conic exact sequence and H1(B_R(3))=0 give

    H0(B_C0(5)) = H0(B_R(5)) / q0 H0(B_R(3))
       = 1+2A+V+2P4+3D5.                            (1)

The parameter conic uses W', with Sym^2 W'=V. Its degree-ten binary sections have representation

    Sym^10 W'=A+V+D5.

If R2=W, the constant tracefree endomorphism representation is A and its tensor product with this binary section space is exactly (1). If R2=W', that representation would be V and the result would instead be

    1+A+2V+2P4+3D5,

which differs. Hence the actual representation is

    E|C0=W tensor O_P1(3),
    B|C0=A tensor O_P1.                             (2)

Thus (2) is not inferred merely from the balanced splitting type.

## 2. Cartan restriction and the determinant-square identity

The plane restriction H0(E)=D5=Sym^4 W injects into H0(E|C0), since H0(E(-2))=H0(F_R)=0. The latter section space is

    W tensor Sym^3 W'.

The two binary cubic representations Sym^3 W and Sym^3 W' are isomorphic irreducible four-spaces. Choose an intertwiner between them; its scalar is immaterial. Under this identification, W tensor Sym^3 W decomposes as Sym^4 W plus Sym^2 W. The D5 inclusion is unique, so actual restriction is, up to scalar, the Cartan inclusion

    Sym^4 W -> W tensor Sym^3 W.

At a conic point x, let theta_x be the resulting evaluation functional on Sym^3 W. The actual hyperplane two-space is Y_ell=ell^3 W. On this space the evaluation map, with the standard symmetric normalization, is

    M_(ell,x)(w)
       = [w theta_x(ell^3)+3 ell theta_x(ell^2 w)]/4. (3)

Define

    Phi(ell,x)=theta_x(ell^3),
    r_(ell,x)(w)=theta_x(ell^2 w).

Then r(ell)=Phi, and (3) is (Phi Id+3 ell tensor r)/4. The rank-one determinant formula gives

    det M = Phi^2/4.                                (4)

The omitted common scalar is nonzero because the actual restriction D5->H0(E|C0) is nonzero. All degree factors agree: Phi has bidegree (3,3); the determinant of Y->E|C0 has bidegree (6,6), the restriction of the cubic family to C0. Equation (4) proves assertion 1.

This is a universal polarization identity, not an evaluation of selected HM coefficients or of an actual matrix at a chosen point.

## 3. Phi defines the existing canonical cover

The section Phi is invariant and nonzero. Indeed theta_x ranges over the evaluation functionals of an invertible intertwiner, and pure binary cubes span Sym^3 W. Hence Phi cannot vanish identically. It also has no identically zero fiber over T, since the intertwiner sends each nonzero pure cube to a nonzero binary cubic.

The canonical realization of the actual factor cover has a unique invariant equation in bidegree (3,3):

    (Sym^3 W tensor Sym^3 W')^G has dimension one.

The established curve B and Phi therefore define the same divisor after the actual equivariant ruling identifications. In particular Phi=0 is smooth of genus four, its first projection is the existing factor-cover map pi, and its two ramification divisors are the already established R_M,R_N. Smoothness is imported from that identified actual cover, not guessed from an arbitrary invariant equation.

## 4. Residual division gives the actual factor map

For b=(ell,x) on B, let linear_x be the binary linear form vanishing at x on C0. Define

    r_b = Phi(ell,-)/linear_x.                       (5)

This is always a nonzero binary quadratic, including at ramification. The conic restriction isomorphism H0(R,O_R(1))=H0(C0,O_P1(2)) identifies it with a unique positive-plane line.

The division is global and equivariant. The cubic evaluation sequence on C0 is

    0 -> H0(O_P1(2)) tensor O_P1(-1)
      -> H0(O_P1(3)) tensor O -> O_P1(3) -> 0,

where the first map multiplies by the tautological vanishing linear form. Restricted to B, inserting the parameter line M^3 shows that (5) is a basepoint-free three-dimensional system of the line bundle

    L_res=3M-N.                                     (6)

No fiber Phi(ell,-) is zero, so the residual system has no common zero.

The actual factor map f has the established actual polarization

    L=K_B+2tau=3M-N=L_res.

Since K_B-L=-2tau is nontrivial of degree zero, Riemann--Roch gives h0(L)=3. Thus both the residual system and the actual line-factor system are the full H0(L). Their equivariant line-bundle identifications differ only by a character, and G has no nontrivial characters. Both target coordinate spaces are the same irreducible three-space V. Schur's lemma identifies the two systems up to a common nonzero scalar. Therefore the two projective morphisms agree everywhere:

    f(b)=the line defined by r_b.                    (7)

This proves the actual map identity, not merely equality of degrees or line-bundle classes. It incorporates the residual-division argument independently supplied in the companion chord note.

## 5. Ordinary and branch fibers

At a reduced fiber write Phi(ell,-)=l1 l2 l3 up to scalar. Formula (5) gives

    l2 l3,       l1 l3,       l1 l2.

These are exactly the three chords through pairs of the three conic points. Their product restricts to (l1 l2 l3)^2, in accordance with (4). This is why a square conic restriction is compatible with the actual sextic chord image.

At a simple branch fiber 2x+y, write Phi=linear_x^2 linear_y. Its residual quadratics are linear_x linear_y with multiplicity two, and linear_x^2 with multiplicity one. The actual determinant is therefore the double chord through x,y plus the tangent at x. At the order-five parameters, x,y are the two invariant conic points, so their chord is the polar line of the corresponding nonisotropic axis. This recovers the actual double-polar-plus-tangent geometry and the sign L=K_B+2tau.

## 6. The exact evaluation rank strata

Formula (3) also gives an intrinsic description of where the two actual sections evaluate independently on C0.

If Phi!=0, (4) makes M invertible. On Phi=0, equation (3) becomes (3/4) ell tensor r. It has rank one exactly when r!=0, and rank zero exactly when r=0.

The differential of Phi in the negative parameter direction is three times r, with Euler's relation r(ell)=Phi. Thus on B, r=0 is precisely the ramification condition for the projection to C0, namely R_N. Since B is smooth and that ramification is simple, these are twelve reduced points.

The scheme structure is also exact. Locally ell has a nonzero coordinate. The entries of M generate Phi and the two components of r: Phi is recovered from trace(M)=5Phi/4, and then ell tensor r is recovered from M. Therefore the ideal of its rank-zero locus is

    (Phi, partial_ell Phi),

the ordinary ramification ideal of B->C0. There is no additional embedded rank-zero scheme. The determinant ideal itself is (Phi^2), so the rank-at-most-one divisor is the doubled curve 2B, as distinct from its reduced support B.

On B away from R_N, the kernel line of M is precisely C ell, because r(ell)=0 and r!=0. Consequently the distinguished square-power section ell^4 is the unique line in Y_ell whose restriction vanishes at each such conic incidence point. This is an evaluation statement on C0, not a claim that its entire zero curve in the hyperplane is reduced or smooth.

## Dependencies and boundaries

THREE-LINE-FACTOR-COVER-GEOMETRY.md proves the actual smooth canonical cover, its rulings, exact five-torsion, and h0(L)=3. The actual sextic alternative and sign are proved in ACTUAL-SEXTIC-FACTOR-IMAGE-BY-CHERN-LENGTH.md and THREE-LINE-POLARIZATION-SIGN-AND-SPECIAL-FIBERS.md. The invariant-conic balance and plane Steiner representation are established inputs. The residual-chord construction above incorporates the independently checked companion argument rather than defining a competing factor cover.

The conclusion resolves the apparent tension between a square conic restriction and the actual sextic image: triangles, not three tangents, provide that restriction. It does not determine the remaining projected smoothing scalar or prove injectivity of its three-dimensional constraint. No actual coefficients or selected ranks are evaluated.
