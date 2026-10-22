# Independent audit of the actual semisimple scalar, primitive, and detecting fiber

## Result and scope

This note independently identifies the ACTUAL scalar inverse and Gram primitive used in ACTUAL-SEMISIMPLE-C5-AXIS-VECTOR-CUP-VANISHES.md. It also identifies its detecting target character and checks exactness in vector cohomology, before either the connecting D5 quotient or the second-symbol quotient.

All identities are uniform for an arbitrary order-five stabilizer and its two abstract eigenspace lines. The symbols A,B,c,lambda,k and the socle scale e remain arbitrary nonzero symbols. No actual HM coefficient is assigned, no actual-instance matrix or rank is evaluated, and no local model replaces the actual cubic or quintic extension.

Use the conventions of ACTUAL-C5-SQUARE-CORRECTION-HAS-A-SIMPLE-ROOT.md. Thus s,t have weights -1,+1, X,Y have weights +3,-3, and z=t/s, w=-s/t=-1/z are volume-compatible charts. Put

    a=st,       h=XY^3.

The two inputs have characters0 and4, respectively.

## 1. The actual global inverse, from two socle pairings

Let e be defined by the actual socle value lambda_socle(X^3Y^3)=e st. Its cubic annihilation identities, together with the abstract symplectic relation C=Ac,D=-Bc, give

    lambda_socle(XY^5)=-(A/B)e s^2,
    lambda_socle(X^5Y)=(B/A)e t^2.

For the unnormalized positive quadratic transvectant, the actual quotient Q is characterized by

    tau(Q(H),q)=lambda_socle(H q),      q in Sym^2 Wprime.

Consequently

    Q(XY^3)=(e/4)[-(A/B)X^2 s^2+Y^2 st],
    Q(X^3Y)=(e/4)[X^2 st+(B/A)Y^2 t^2].                (1)

These are two tensor identities from the actual socle pairing, not selected entries of an evaluated source matrix.

For a=st, D_a=t partial_t-s partial_s. Equation(1) gives

    k a Lie_(D_a)(Qh)=(k e A/(2B))X^2 s^3t.

The global quartic-valued section

    u=(kA/B)X^3Y s^2-kXY^3 st                           (2)

maps to this same expression by(1). Since H0(Q(2)) is an isomorphism, (2) is THE actual scalar correction. In the x-chart and the oriented y-chart,

    Gamma_x=(kA/B)X^3Y+kXY^3z,
    Gamma_y=(kA/B)X^3Y w^2+3kXY^3w.                    (3)

In particular Gamma_y is not obtained by forgetting its inhomogeneous line-frame term.

## 2. The actual n and unique Gram primitive

Use the global meromorphic quintic g0 and transitions p_x,p_y of the divisor-defined two-chart calculation. The exact quotient identity h f_z=m f+n g0 gives

    n=A/(B lambda)[A XY+Ac X^2z^2+3Bc Y^2z^3+Bc^2 XYz^5],
    m=XY^2(A X+5Bc Yz^3)/(2Bc z^4).                    (4)

The restriction isomorphism for O_D(2,6) makes this n the actual h*kappa, not an independently chosen lift. The companion verifier here checks the exact polynomial identity in(4) with all parameters unassigned.

The source Gram primitive is

    eta0_x=A/(Bc)z^(-4),       eta0_y=A/(Bc)w^2.        (5)

Indeed, with the actual transition conventions g_i=g0+p_i f, direct universal transvection gives

    eta0_x+tau(p_x,n_x)=-3c z,
    eta0_y+tau(p_y,n_y)=-13A/(Bc)w^2.                  (6)

Both regular target primitives are regular on their entire affine charts. Their differences give the actual Gram cocycle. Any difference from the pinned actual Gram lift would therefore be a global section of O(-2), which is zero. Thus (5) is the actual primitive. It cannot be replaced by zero even though its y expression happens to be regular.

## 3. The actual detecting annihilator

The C5 characters of P4 are2,4,6,8; those of A are8,0,2. The second symbol at a=st is weight preserving, since it is quadratic in the weight-zero a. Its image has only characters2 and8. The established rank-two axis theorem says these are exactly its two image lines, so the cokernel fiber has characters4 and6.

The h=XY^3 input has character4. Its dual detecting annihilator therefore has character6. Under the actual inclusion i^t:P4-dual->V tensor H0(O_L(2)), that line is

    i^t c proportional to Y^2t^2-(2A/B)X^2st.          (7)

To check the ratio without any target matrix, pair(7) with Q(XY^3) from(1) in the PRODUCT positive/negative quadratic apolar form. The pairing is zero. All other Q(D5) characters pair trivially with character6 by their weights. The orthogonal complement of the actual Q(D5) summand is exactly the unique P4 summand, so this is the actual i^t line, up to one common nonzero scalar.

The final dual test zeta=a i^t c consequently has expressions

    zeta_x=Y^2z^3-(2A/B)X^2z^2,
    zeta_y=-Y^2w-(2A/B)X^2w^2.                        (8)

These annihilate the ACTUAL second-symbol image in its cokernel fiber. This is not merely evaluation of a sextic minor at a point of its zero scheme.

## 4. Independent cohomology check after the full expansion

The full expansion in ACTUAL-SEMISIMPLE-C5-AXIS-VECTOR-CUP-VANISHES.md, verified there with every source and frame term retained, has principal parts

    R_x=C6 XYz^(-6)+C1 XYz^(-1),       R_y regular,
    C6=3k lambda/(10Bc^2),             C1=-k lambda/(2A). (9)

The global meromorphic source-comparison theorem identifies(9) with the actual vector class. The fixed physical normalization is the same nonzero scalar nu0 throughout.

First, remove the order-six part using the global V O(-6) meromorphic section with x coefficient C6 XYz^(-6). Its y coefficient is C6 XY, regular. The remaining lower class is

    C1 XYz^(-1)/nu0 != 0 in H1(V O_L(-6)).             (10)

Its character is4: the O(-6) fiber at x has character6, z^(-1) has character8, and XY has character0. The connecting A has characters8,0,2, so(10) is still nonzero modulo A.

Now cup by a. Its expressions are a_x=z and a_y=-w. The sole remaining polar part of aR is C6 XYz^(-5). This is globally removable in V O(-4): the global meromorphic section with that x coefficient has y coefficient -C6 XYw, which is regular. Therefore

    [aR/nu0]=0 in H1(V O_L(-4)).                       (11)

No choice of the final ratio(7) is needed for(11). As a compatible check, every polar coefficient in(9) is proportional to XY, which pairs identically to zero with both X^2 and Y^2 in(8).

The normalizer of the order-five subgroup interchanges its two fixed points and the positive eigenlines X,Y. It preserves the semisimple quadratic line and exchanges the h=XY^3 and h=X^3Y characters. Hence the other detecting input also satisfies(11), uniformly at every one of the six axes. The other three input characters cannot contribute to the rank-two cokernel by weights. This proves vanishing in the actual cokernel fibers, not just ordinary vanishing of a polynomial section on the support of the degeneracy scheme.

The further conclusion that these fiber vanishings exclude the remaining discriminant-divisible gate belongs to THIRD-GATE-VANISHING-AT-SIX-AXES-KILLS-RESIDUAL-CHANNEL.md. No replacement of the length-four local degeneracy schemes by reduced points is made here.

## Verification and references

Run python verify_semisimple_actual_scalar_primitive_audit.py. It checks(1)-(6), the product-apolar annihilator, the oriented Gamma law, and the lower/upper principal-parts arithmetic. The separate verify_semisimple_axis_vector_cup_cancellation.py checks the full Laurent expansion; that work is not replaced by a test of the scalar summand alone.

Other inputs: ACTUAL-MEROMORPHIC-QUINTIC-SOURCE-CHANGE-PRESERVES-VECTOR-CLASS.md; ACTUAL-C5-SQUARE-CORRECTION-HAS-A-SIMPLE-ROOT.md; ACTUAL-CONE-DIAGONAL-IS-CANONICAL-RESIDUE-INVERSE.md; SECOND-BOCKSTEIN-SYMBOL-SIX-AXIS-DEGENERACY.md, together with the already established nonzero actual second scalar.
