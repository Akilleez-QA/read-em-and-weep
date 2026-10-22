# The projected two-dimensional channel and its exact discriminant factor

## Results

The actual linear cokernel C_lin admits a G=SL(2,5)-equivariant quotient rho:C_lin->O_T(2). Fix one such quotient, without declaring it canonical when the quotient space has dimension two. The actual root-transform target then has a quotient

    C_quad -> S3,       Sn:=nu_*eta*O_T(n),

where S3 is a rank-two Steiner bundle on the negative-quadratic plane P. Project the actual positive multiplication map to this quotient:

    m_rho:(A tensor K) tensor Sym^2 V* tensor O_P(1) -> S3,
    A=Sym^2 W,       K=S(-5).

The space of all equivariant maps of this type has dimension seven. Its invariant-positive-quadratic part has dimension one; its other positive directions have six independent representation-theoretic couplings. These dimensions constrain the actual map but do not assign its coefficients.

More sharply, let q0 be the invariant positive quadratic and let Disc be the discriminant section of O_P(2). There is a canonical surjection, up to the usual fixed one-dimensional volume normalization,

    psi:A tensor K(3) -> S3.                         (1)

For an unknown scalar lambda_rho, the projected actual invariant-positive map is

    m_rho(q0) = lambda_rho Disc times psi(-2),
    A tensor K(1) -> S3.                             (2)

Here psi(-2) has target S3(-2), and multiplication by Disc supplies S3. Thus the projected q0 channel vanishes identically on the discriminant. If lambda_rho is nonzero, it has rank two away from the discriminant, vanishes to exactly first order along it, and its map after dividing by Disc is surjective everywhere. No nonvanishing of lambda_rho is claimed.

The signed deformation Bockstein for q_-+s q_+=0 is the negative of positive multiplication in the convention already fixed. Changing to that convention changes lambda_rho by a minus sign and none of these assertions.

## 1. The quotient is actual, but its choice can matter

The equivariant splitting-constraint theorem for C_lin proves that every surviving splitting has a nonzero equivariant map to O_T(2). Every such nonzero map is fiberwise surjective. The argument is exact: among positive-degree blocks R tensor O_T(d), the only contributions to Hom_G(C_lin,O_T(2)) are

    1 tensor O_T(2), through the identity,
    W tensor O_T(1), through evaluation W tensor O_T(1)->O_T(2).

Each nonzero contribution is already surjective. Any nonzero combination across these summands remains surjective by restriction to one contributing summand. No choice of an actual splitting or coefficient is used here.

Write L=Hom_G(C_lin,O_T(2)). The remaining possibilities have dim L equal to one or two. If dim L=1, the quotient is unique projectively, and its kernel is canonical. If dim L=2, individual quotients form P(L); the present data do not choose one. The complete evaluation gives the canonical quotient

    C_lin -> L* tensor O_T(2).

This is fiberwise surjective because every nonzero element of L remains nonzero in each fiber dual. The proof of the splitting constraint and this quotient assertion is the companion equivariant C_lin splitting theorem; no new enumeration is being performed here.

The root correspondence has eta flat and nu finite. Applying the exact functor nu_*eta*(- tensor O_T(1)) to a chosen rho gives the actual surjection

    C_quad=nu_*eta*(C_lin(1)) -> S3.                 (3)

In particular (3) is not merely a quotient of the generic target vector space. It includes every doubled and previously exceptional root. The complete choice-free quotient is C_quad->L* tensor S3.

## 2. Finite-flat duality and the precise Hom space

The universal root divisor Z in T x P has bidegree (2,1). Relative adjunction over P gives

    omega_(Z/P)=O_Z(0,1)=nu*O_P(1),

because omega_T=O_T(-2). The standard determinant of W is trivial for G; no character factor is omitted. The degree-two finite flat map is Gorenstein, so duality applies also at a doubled root. It gives

    K* = (nu_*O_Z(-5))*
       = nu_*(O_Z(5) tensor omega_(Z/P))
       = S5 tensor O_P(1).                          (4)

Consequently

    Hom(A tensor K(1),S3)
       = A* tensor H0(P,S5 tensor S3).              (5)

For n>=1, the root-divisor sequence gives the actual Steiner presentation

    0 -> Sym^(n-2) W tensor O_P(-1)
      -> Sym^n W tensor O_P -> Sn -> 0,             (6)

with the left term zero when n=1. In particular S3 has presentation

    0 -> W tensor O_P(-1) -> Sym^3 W tensor O_P
      -> S3 -> 0.

Tensoring the S5 and S3 presentations gives a length-two locally free resolution. Its negative terms are sums of O_P(-1) and O_P(-2), both acyclic on P2. Thus the natural map on sections is an isomorphism

    H0(S5 tensor S3)=Sym^5 W tensor Sym^3 W.          (7)

This is an actual Hom identification, not a dimension substitution.

## 3. The seven equivariant couplings

Clebsch--Gordan for the defining two-space gives

    Sym^5 W tensor Sym^3 W
       = Sym^8 W + Sym^6 W + Sym^4 W + Sym^2 W.

Restricting to G, with P4 the four-dimensional center-even irreducible and D5 the five-dimensional irreducible, this is

    A + V + 2P4 + 2D5.                              (8)

The positive quadratic representation is Sym^2 V*=1+D5. The invariant-positive part of (5) has dimension one, since A occurs once in (8). Moreover

    A tensor D5=A+V+P4+D5,

so the D5-positive part has dimension 1+1+2+2=6. Hence the total invariant Hom dimension is seven.

For a chosen rho, the actual projected map is one point of this seven-dimensional space. The assertion does not prove any of its components nonzero. Changing rho changes this point linearly. For the canonical full quotient L* tensor S3, the coefficient is an element of L* tensor this seven-dimensional space; it is not a choice of one privileged quotient.

## 4. The invariant coupling is a discriminant multiple

The single A in (8) is already the unique Sym^2 W summand for full SL2. In the biform description of (7), its inclusion is

    a |-> [x,y]^3 a(x),

where a is a binary quadratic, the biform has degrees (5,3), and [x,y] is the invariant bracket. Choosing the opposite bracket or its volume normalization only rescales the unique coupling.

For a double root t, the two root variables are independently dual numbers x=t+h and y=t+k, with h^2=k^2=0. The bracket is a unit multiple of h-k, and (h-k)^3=0. Hence the entire coupling vanishes on the discriminant as a section of its actual Hom bundle.

The exact multiplicity can be seen without evaluating any actual coefficient. On a monic root chart let both z,w satisfy

    X^2-sigma1 X+sigma2=0.

In that universal quotient algebra,

    (z-w)^3=(sigma1^2-4 sigma2)(z-w).               (9)

Thus the bracket-cubed coupling is one discriminant factor times the bracket coupling, with the precise homogeneous line factors supplied by (4)-(5).

There is also a coordinate-free construction of the factor, which proves its surjectivity everywhere. The residual-root involution iota:Z->Z interchanges the two roots; it is defined even over the discriminant. The universal product of root lines gives

    iota*eta*O_T(1)
       = nu*O_P(1) tensor eta*O_T(-1).              (10)

Evaluation A=H0(T,O_T(2)) gives a surjection on Z

    A tensor O_Z(-5) -> O_Z(-3).

Twist by nu*O_P(3), use (10), and take the finite pushforward. The result is

    A tensor K(3)
       -> nu_*(O_Z(-3) tensor nu*O_P(3))
        = nu_*iota*O_Z(3)
        = S3.

This is psi in (1), and it is surjective at every point because the original evaluation is surjective and finite pushforward is exact. It is SL2-equivariant and nonzero. Multiplication by Disc gives the unique nonzero SL2, hence unique G, invariant-positive coupling, up to scalar. This proves (2), including its behavior at the discriminant.

For completeness the evaluation kernel on T is W tensor O_T(-1). Hence

    0 -> W tensor S(-6)(3) -> A tensor K(3)
      --psi--> S3 -> 0.                             (11)

By (4) with 5 replaced by 6, S(-6)(3)=S6*(2). Thus the rank-four kernel in (11) is W tensor S6*(2). This describes the universal factor's kernel, not the kernel of the full actual six-to-ten map.

## 5. Exactly two of the seven couplings have the discriminant factor

There is an exact universal characterization of sections in (7) vanishing on the discriminant. A biform of bidegree (5,3) has that property if and only if it is divisible by [x,y]^3.

Indeed, at every point of the diagonal in T x T, its restriction to two independent first-order root jets must vanish. A diagonal vanishing order zero or one is detected by its value or first derivative. At order two the coefficient of hk in (h-k)^2 is -2 and detects the leading term. In characteristic zero, vanishing on all these root jets therefore forces diagonal order at least three. Conversely order at least three plainly suffices. Dividing by the diagonal cubic leaves bidegree (2,0), so the space is exactly

    [x,y]^3 Sym^2 W = A.                            (12)

Equivalently H0(S5 tensor S3(-2)) is A, with multiplication by Disc identifying it with the section subspace in (12).

It follows that the equivariant positive couplings which vanish along the discriminant form a two-dimensional subspace of the seven-dimensional space:

    dim Hom_G(A tensor (1+D5), A)=1+1=2.

One is the invariant-positive channel in (2); the other is the unique A channel inside A tensor D5. The quotient has dimension five and is detected by restriction to the discriminant. This is a decomposition of the available operator space. It neither states which of the five surviving restriction coefficients are actually nonzero nor assigns either discriminant-factor coefficient.

If dim L=2, the canonical full quotient has invariant-positive coefficient lambda in L*. If lambda is nonzero, its image lies in the rank-two subbundle C lambda tensor S3 off the discriminant, not in two independently variable copies of S3. If lambda=0, the entire invariant-positive projection vanishes. Again the present proof does not choose between these possibilities.

## 6. The precise remaining scalar question

The nonzero ambient second-normal class zeta establishes certain earlier cup maps. It does not, by representation theory alone, assign lambda_rho in (2). This scalar additionally involves the actual quotient rho of C_lin and the actual plane-restriction boundary appearing in the Hermite formula. The identity that the invariant positive conic has vanishing restricted second-normal classes does not identify that quotient or its global boundary.

Thus a proof that lambda_rho is nonzero, or a proof that it vanishes, needs a further compatible geometric identification of this projected boundary. Neither the seven-dimensional Hom count, the existence of psi, nor zeta!=0 alone supplies it. Equations (2), (11), and (12) retain an exact, much smaller target for such an argument without replacing the actual operator by a generic one.

## Source interfaces

The exact root transform and the absence of cokernel torsion are established in QUADRATIC-TARGET-FROM-HYPERPLANE-TORSION.md and DISCRIMINANT-PRINCIPAL-PARTS-AND-SMOOTHING-FILTRATION.md, using the checked all-hyperplane square theorem. The actual Hermite operator, including its sign conversion and line twists, is TWO-ROOT-DIVIDED-DIFFERENCE-SMOOTHING-FORMULA.md. The equivariant splitting and O_T(2) quotient are the independently checked C_lin splitting-constraint theorem. The proof here does not repeat that enumeration or infer a particular actual splitting.

All polynomial identities and character decompositions are universal. No actual HM/source coefficients, selected evaluation, or actual rank computation occurs.
