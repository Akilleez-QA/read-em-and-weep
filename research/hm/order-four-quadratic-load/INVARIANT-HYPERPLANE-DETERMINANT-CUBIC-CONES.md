# Determinant cubic cones on every inversion-invariant hyperplane through the positive plane

## Theorem

Let F be normalized Horrocks–Mumford on P(V directsum W*), where V is the positive three-space and W* the negative two-space of inversion. Put R=P(V), and for lambda in P(W*) let

    H_lambda=P(V directsum lambda).

Then:

1. h0(F_Hlambda(2))=2 for every lambda.
2. Their actual section bundle over P(W*) is O(-3) tensor W, as an equivariant subbundle of H0(F_R(2)) tensor O.
3. The wedge of the two sections is a nonzero cubic on H_lambda. Its equation depends only on the positive coordinates. Therefore its zero scheme is the cubic cone, with vertex lambda, over a nonzero plane cubic in R.

The base cubic is not asserted smooth, irreducible, reduced, or a product. No generation statement follows from this theorem. In particular, the dimensions h0(F_H(1))=0 and h0(F_H(2))=2 are not a classification of the zero curves of these sections.

## 1. Actual plane and normal-class inputs

Use the genuine binary normalizer group G=SL2(F5). Its center acts positively on V and negatively on W. The actual fixed-plane theorem gives

    0 -> A O_R(-3) -> D O_R(-2) -> F_R -> 0,
    A=Sym^2 W,  D=Sym^4 W,
    H0(F_R(1))=0,  H0(F_R(2))=D,  H1(F_R)=A.

The identifications of D and A are equivariant: D is the unique irreducible five-space, and A is the three-space different from V. The bundle F_R(1) is acyclic.

Every hyperplane restriction F_H is stable. Restricting further from H_lambda to R gives

    0 -> F_Hlambda -> F_Hlambda(1) -> F_R(1) -> 0.

Thus H0(F_Hlambda(1))=0 for every lambda. The next restriction sequence makes

    H0(F_Hlambda(2)) -> H0(F_R(2))=D                  (1)

injective.

The actual ambient second-normal projective comparison class zeta is nonzero and belongs to

    (Sym^2 W tensor H1(End_0(F_R)(-2)))^G.

Its coefficient map is the unique nonzero A-channel. The dual Steiner sequence tensored by F_R(-2) gives

    0 -> End(F_R)(-2) -> D* tensor F_R
      -> A* tensor F_R(1) -> 0.

Consequently the canonical cohomology identification is

    H1(End(F_R)(-2)) = D* tensor A.                    (2)

Under (2), a deformation class acts on D=H0(F_R(2)) by its corresponding map D->A. This is naturality of evaluation: the first sheaf map is composition with the actual presentation D O_R(-2)->F_R. Removing the trace does not change H1, since H1(O_R(-2))=0.

## 2. Exact dimension two on every hyperplane

Restricting the second-normal comparison to the direction lambda in W* evaluates its quadratic coefficient. Every section in (1) must satisfy the resulting necessary lifting equation

    y_lambda(s)=0,
    y_lambda:D=Sym^4 W -> A=Sym^2 W.                  (3)

This is the vector-bundle lifting equation as well as the projective one: scalar first and second comparison classes have zero H1 on the plane. Inversion-equivariant local frames eliminate the first normal term.

The relevant G-equivariant map Sym^2 W* tensor Sym^4 W -> Sym^2 W is unique up to scalar. Its standard nonzero representative is second contraction. By (2) and zeta!=0, its actual scalar is nonzero. Therefore (3) is proportional to contraction twice by lambda.

Let ell_lambda=ker(lambda:W->C), a line in W. In characteristic zero, second contraction is onto and has kernel

    ker y_lambda = ell_lambda^3 W.                    (4)

This is a universal symmetric-power identity: it kills precisely the quartics containing at least three factors from ell_lambda. The quotient has dimension three and contracts isomorphically onto Sym^2 W. No actual HM coefficients are evaluated. Equation (4) bounds h0(F_Hlambda(2)) by two.

For the reverse inequality, actual ambient cohomology gives

    h1(F(1))=h1(F(2))=10,
    trace(inversion|H1(F(1)))
      =trace(inversion|H1(F(2)))=-2.

The odd linear equation of H_lambda therefore induces a map from the negative six-space in H1(F(1)) to the positive four-space in H1(F(2)). Its kernel has dimension at least two. Since H0(F(1))=H0(F(2))=0, the hyperplane restriction sequence identifies this kernel with a subspace of H0(F_Hlambda(2)), including the sign of the odd equation in the first term. Hence

    h0(F_Hlambda(2))=2,
    im(1)=ell_lambda^3 W                              (5)

for every lambda. The sections are inversion-even, also clear from their injective restriction into D on R.

## 3. The section bundle and all tautological twists

Set T=P(W*) and let L=O_T(-1) be its tautological line. The universal hyperplane is the projective bundle of lines

    pi:H=P_T((V tensor O_T) directsum L) -> T.

Its relative O_H(1) is the pullback of ambient O_P4(1). In particular

    pi_*O_H(1)=(V* tensor O_T) directsum O_T(1).

The constant value in (5), properness, and cohomology and base change make

    Y=pi_*(F|H(2))

a rank-two vector bundle. Restriction to R identifies it with the kernel of the surjective bundle map

    D tensor O_T -> A tensor O_T(2).

The annihilator lines ell_lambda form O_T(-1): this follows either from the tautological sequence or from the invariant symplectic identification W* with W. Formula (4) therefore gives an actual equivariant bundle isomorphism

    Y=O_T(-3) tensor W,
    det Y=O_T(-6).                                    (6)

The determinant of W is the trivial representation. Thus (6) includes the equivariant determinant, not only its ordinary degree.

## 4. The determinant wedge is nonzero in every fiber

The two sections in (5) are generically independent on H_lambda. Otherwise the saturation of their image in F_Hlambda(2) is a rank-one reflexive subsheaf O_Hlambda(d). Saturation is reflexive because the ambient bundle is locally free and the quotient is torsion-free. Since two independent sections factor through it, d>=1.

The resulting injection O(d)->F_Hlambda(2) gives a nonzero section in twist 2-d. Multiplying by a nonzero form of degree d-1 produces a section of F_Hlambda(1), contradicting Section 1. Thus the wedge is nonzero.

As det F=O_P4(-1), its determinant lies in H0(O_Hlambda(3)). This determinant identification is equivariant: any discrepancy is a character of the perfect group G, hence trivial. The relative evaluation map therefore gives the actual equivariant morphism

    det Y -> pi_*O_H(3).                              (7)

It is nonzero on every fiber. The phrase "the determinant cubic" means the nonzero one-dimensional wedge of the two-dimensional section space, not uniqueness among all cubics in H_lambda.

## 5. Equivariance removes the negative-coordinate term

The projective-bundle formula, with the convention fixed in Section 3, gives

    pi_*O_H(3)
      = Sym^3 V* tensor O_T
        directsum Sym^2 V* tensor O_T(1)
        directsum V* tensor O_T(2)
        directsum O_T(3).

The summand with negative-coordinate degree j has central inversion character (-1)^j. Since det Y is even, only j=0 and j=2 can occur in (7). The possible degree-two negative-coordinate coefficient would therefore be an invariant element of

    Hom_G(O_T(-6),V* tensor O_T(2))
      = (V* tensor H0(O_T(8)))^G
      = (V* tensor Sym^8 W)^G.                         (8)

There is no omitted base twist: the O_T(2) in (8) is the square of the dual tautological negative line, and the additional O_T(6) is the dual of det Y.

The universal binary character calculation gives

    Sym^8 W = 4 directsum 5.

For example its characters on the A5 classes of orders 1,2,3,5,5 are (9,1,0,-1,-1), which are those of 4+5. This calculation is unchanged by interchanging the two binary two-spaces. Since V is irreducible of dimension three, (8) is zero.

Thus (7) factors through Sym^3 V* tensor O_T. Every determinant cubic depends only on the positive coordinates, proving the cone assertion.

The remaining morphism is O_T(-6)->Sym^3 V* tensor O_T and is nowhere zero. Hence the base cubics form an everywhere-defined equivariant map

    T -> P(Sym^3 V*)

whose pulled-back hyperplane bundle is O_T(6). This does not assert that the map is an embedding or that its image has degree six.

## Sources and limits

- INVARIANT-CONIC-SECOND-NORMAL-COLLAPSE.md supplies the actual opposite-three identification and linearizations.
- ACTUAL-AMBIENT-SECOND-NORMAL-NONVANISHING.md supplies the actual zeta!=0. Its coefficient map and the dual Steiner action are used explicitly in Sections 1–2.
- INVERSION-EVEN-TWIST-THREE-VANISHING.md supplies H0(F_H(1))=0 for the hyperplanes through R, using stability of every hyperplane restriction and the actual Steiner plane.
- LOWER-TWIST-EVEN-QUADRIC-PARITY.md and FULL-ADJOINT-PENCIL-INVOLUTION-BLOCKS.md supply the two actual primary cohomology traces used for the lower bound.

The theorem concerns the determinant of the actual two sections on each actual hyperplane. It makes no assertion about smoothness, factorization, products generating further sections, generic rank of any adjoint multiplication, or completion of the full proof repair. No selected HM/source coefficients, evaluated actual matrices or ranks, scans, or experiments are used.
