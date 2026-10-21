# The invariant projected boundary is a single transvectant

## New exact reduction

Fix a nonzero equivariant quotient rho:C_lin->O_T(2). The actual plane boundary, followed by rho, is

    H0(B_R(5)) tensor O_T -> C_lin(2) -> O_T(4).

Equivalently it is a G-map b_rho:H0(B_R(5))->D, where D=H0(O_T(4))=Sym^4 W. The independently established surjectivity of the plane boundary makes b_rho nonzero.

Let q0 be the invariant positive quadratic. On the subspace q0 H0(B_R(3)), the map b_rho is necessarily an unknown scalar times the SL2 second-transvectant projection

    Sym^2(Sym^4 W) -> Sym^4 W.                       (1)

In particular the other G-equivariant D channel, coming from the D summand of Sym^8 W, is forced to vanish. This conclusion uses the actual moving-square annihilation, not just the dimensions of the Hom spaces.

The unknown scalar in (1) is a nonzero universal multiple of the scalar lambda_rho in PROJECTED-SMALL-CHANNEL-AND-DISCRIMINANT-FACTOR.md. Thus lambda_rho is zero if and only if b_rho annihilates q0 H0(B_R(3)). Every projected invariant-positive self-diagonal block is zero, whether this scalar is zero or not.

## 1. The actual annihilation identity

Let a(ell):A->S3:=H0(B_R(3))=Sym^2 D be the moving leading square inclusion. It comes from the actual hyperplane sections, and has image

    Sym^2(ell^3 W) subset Sym^2(Sym^4 W).

For every positive quadratic q_+ and every parameter ell, q_+ a(ell)c extends to the corresponding hyperplane. Hence the actual plane boundary, and therefore its projection b_rho evaluated at ell, gives

    evaluation_ell b_rho(q_+ a(ell)c)=0.             (2)

The identity is pointwise for the genuine bundle sections and holds for all c in A. In homogeneous parameter coordinates its left side has degree ten: six from a and four from evaluation of the O_T(4) output.

## 2. The two possible D channels on the invariant-positive subspace

The full SL2 decomposition is

    Sym^2(Sym^4 W)=Sym^8 W directsum Sym^4 W directsum 1.

For G=SL(2,5), Sym^8 W=P4+D and Sym^4 W=D. Thus there are exactly two G-equivariant maps S3->D. One is the projection (1), denoted p_low. The other factors through a fixed nonzero G-projection

    p_high:Sym^8 W -> D.

We show that p_low satisfies (2) with q_+=q0 and p_high does not.

Use the invariant apolar pairings to identify D and Sym^8 W with their duals. Evaluation at ell on D is pairing against ell^4. The top projection of a(ell)c is ell^6 c. If p_high satisfied (2), its transpose j:D->Sym^8 W would obey

    pairing(j(ell^4), ell^6 c)=0 for every c in Sym^2 W.

The apolar annihilator of ell^6 Sym^2 W in Sym^8 W is exactly ell^3 Sym^5 W. Therefore

    j(ell^4) belongs to ell^3 Sym^5 W for every ell.  (3)

The family ell^4 gives O_T(-4)->D tensor O_T, while ell^3 Sym^5 W is the subbundle Sym^5 W tensor O_T(-3) of Sym^8 W tensor O_T. Condition (3) consequently factors the equivariant map through

    O_T(-4) -> Sym^5 W tensor O_T(-3).

But its space of equivariant global maps is

    (Sym^5 W tensor H0(O_T(1)))^G
       = (Sym^6 W directsum Sym^4 W)^G=0,

because Sym^6 W=V+P4 and Sym^4 W=D have no invariant. The factored map would be zero. The pure fourth powers span D, so j would be zero, a contradiction. Thus the high-channel constraint is nonzero.

For the low channel, the second transvectant of ell^3 w1 and ell^3 w2 is a multiple of ell^4. Its pairing against ell^4 is zero. Hence p_low satisfies (2). Since its contribution is identically zero and the high-channel contribution is nonzero, (2) forces the high coefficient of b_rho(q0 times -) to be zero. This proves (1).

The apolar annihilator statement is uniform and elementary. After choosing a symplectic basis with ell equal to its first vector, the three monomials divisible by ell^6 pair only with the three complementary monomials; their annihilator consists precisely of forms divisible by ell^3. No actual HM coefficient is chosen by this basis calculation.

## 3. Identification with the discriminant-factor scalar

Normalize the second transvectant of binary quartics by

    (f,g)_2=f_xx g_yy-2 f_xy g_xy+f_yy g_xx.

The universal identity is

    (ell^3 w1,ell^3 w2)_2
       = -18 [ell,w1][ell,w2] ell^4.                 (4)

Normalize the apolar pairing so that pairing(ell^4,m^4)=[ell,m]^4. It follows that the projected plane boundary of q0 a(ell)c, evaluated at another parameter m, is a scalar multiple of

    [ell,m]^4 times evaluation_ell(c),               (5)

where evaluation_ell(c) denotes [ell,w1][ell,w2] on c=w1w2.

The actual cross-root restriction formula divides (5) by the bracket of the two parameter equations. Thus it yields the bracket-cubed biform

    [ell,m]^3 evaluation_ell(c).

This is precisely the nonzero universal coupling in the small-channel theorem. It follows that the coefficient in (1) and lambda_rho differ by a fixed nonzero normalization constant, including the stated sign conversion if the signed Bockstein is used.

Differentiating (5) in ell at ell=m gives zero, since it has a fourth-order diagonal zero. The actual diagonal Hermite identity therefore shows that each self-diagonal q0 block vanishes. Cross-root compatibility still retains the unknown scalar and the discriminant factor. This vanishing does not assert that the whole projected q0 map is zero.

## 4. The exact remaining test if the invariant channel vanishes

The actual nonzero map b_rho could still annihilate q0 S3. The conic sequence and H1(B_R(3))=0 give

    0 -> q0 H0(B_R(3)) -> H0(B_R(5))
      -> H0(B_C0(5)) -> 0.

Thus lambda_rho=0 is exactly the condition that b_rho factor through this conic section space. Its dimension is 48-15=33. The known characters give

    H0(B_R(5))=2*1+2A+V+3P4+5D,
    H0(B_R(3))=1+P4+2D,
    H0(B_C0(5))=1+2A+V+2P4+3D.

In particular the space of equivariant candidate factorizations to D has dimension three.

The remaining positive directions form D inside Sym^2 V*=1+D. For a candidate b in this three-space, define the intrinsic constraint

    T(b)(c,q)(ell)=evaluation_ell b(q a(ell)c),
    c in A, q in D.

The quotient by q0 S3 in the argument of b is understood. The result is homogeneous of degree ten in ell, so

    T:Hom_G(H0(B_C0(5)),D)
        -> Hom_G(A tensor D,Sym^10 W).              (6)

Both sides have dimension three: Sym^10 W=A+V+D and A tensor D=A+V+P4+D. The map (6) is defined by the actual plane multiplication and the actual universal moving square inclusion. It is not a freely chosen three-by-three map.

If (6) were proved injective by a compatible structural argument, the nonzero actual b_rho could not factor through the conic, and lambda_rho would be nonzero. No injectivity of (6) is proved here. In particular the dimension equality and zeta!=0 do not prove it.

The choice issue is real. If the actual quotient space L=Hom_G(C_lin,O_T(2)) has dimension two, lambda is a linear functional on L, and it must have a nonzero kernel. Thus a theorem that every nonzero rho has lambda_rho!=0 would also exclude those remaining splitting possibilities. At present it would be incorrect to infer that exclusion from target surjectivity alone.

## Source interfaces and scope

The moving leading square and its actual diagonal/cross-root boundary identities are established in TWO-ROOT-DIVIDED-DIFFERENCE-SMOOTHING-FORMULA.md. The quotient and the discriminant-factor scalar are treated in PROJECTED-SMALL-CHANNEL-AND-DISCRIMINANT-FACTOR.md. Uniform plane-boundary surjectivity is the independently checked SURJECTIVE-PLANE-BOUNDARY-BY-CONIC-RESIDUALS.md theorem. The plane Steiner presentation supplies the cohomology and characters used here.

The new deduction is the forced removal of the high D channel, its exact transvectant identification, and the resulting precise conic-factorization test. No actual source coefficient, chosen bundle matrix, or rank is evaluated.
