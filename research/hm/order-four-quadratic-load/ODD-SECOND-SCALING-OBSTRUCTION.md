# The actual second odd scaling obstruction is an eighteen-to-thirty root gate

## Theorem and exact scope

Retain the actual smooth even quadric Q=(q_++q_-=0), fixed conic C, ideal I, negative two-space W, and normalized HM adjoint B. For the finite odd scaling family

    M_epsilon=((I/I^9) tensor g_epsilon*B tensor O_Q(4))_-,
    g_epsilon(x,u,v)=(x,epsilon u,epsilon v),

the established first obstruction is a surjective thirty-to-twelve map delta_q at order epsilon squared. Its kernel has dimension eighteen.

The NEXT actual obstruction, at order epsilon to the fourth power, is canonically an operator

    Delta_q:ker(delta_q)
          -> H1(B_R(-1)) tensor (Sym^5 W/q_- Sym^3 W),   (1)

of dimensions eighteen to thirty. This is the entire secondary obstruction, not merely a necessary component of a larger obstruction. Its target injects canonically into the full secondary obstruction quotient, and its vanishing is equivalent to the existence of a lift through order epsilon to the fourth power.

More intrinsically, on the negative direction line P(W*) there is an actual bundle map

    beta:K -> H1(B_R(-1)) tensor O(4),                  (2)
    0 -> K -> H0(B_R(3)) tensor O
      -> H1(B_R(1)) tensor O(2) -> 0,

where K has rank nine and degree minus twelve. If Z(q_-) is the reduced divisor of the two roots of q_-, then (1) is exactly

    H0(Z(q_-),K(1))
      --beta(1)--> H1(B_R(-1)) tensor H0(O_(Z(q_-))(5)). (3)

Thus it is the direct sum of two actual nine-to-fifteen secondary root maps. These maps depend on the actual fourth normal neighborhood of F. They do not discard its nonlinear quartic transition term. The resulting root operator is independent of the positive equation q_+: that equation affects only lower harmonic corrections, which disappear in the correct quotient.

No rank of beta is asserted. If its generic rank on P(W*) is r, the actual generic odd-section bound improves to 18-2r; proving r=9 would prove generic odd vanishing in the even quadric family. This note constructs the exact test but does not establish that additional assertion.

## 1. The full secondary quotient and even parameter

The finite scaling family is flat and properly supported, as proved in the first-odd-obstruction note. Its special fiber has

    h0(M_0)=30,   h1(M_0)=90.

The latter follows from its exact harmonic decomposition:

    2 B_R(3)|4C,  2 B_R(1)|3C,
    2 B_R(-1)|2C,  2 B_C(-3),

whose H1 dimensions are respectively 6,18,36,30. The first boundary has rank twelve. Without further structure, the intrinsic next differential would therefore have target

    H1(M_0)/im(delta_q),  of dimension 78.             (4)

The parameter involution epsilon -> -epsilon is compatible with the actual inversion linearization of End(F). Its action on the special-fiber adjoint is trivial. Locally, averaging a basis and applying Nakayama gives an equivariant basis with invariant reduction; in these bases the adjoint family descends formally to t=epsilon^2. Equivalently, its projective transitions can be chosen to have only even powers of epsilon. Thus there is no intervening odd-parameter obstruction.

The general secondary differential is the t-squared lifting obstruction on ker(delta_q), modulo the first-boundary image. It can be defined directly by the two successive short exact sequences of parameter truncations, or by the associated cohomological spectral sequence. The construction does not require a matrix presentation.

## 2. The actual quartic term and first correction must both remain

In local projective frames over the positive plane, write actual transitions relative to the reference pullback through fourth normal order as

    exp(t ad(z_ij)+t^2 ad(r_ij)) modulo t^3,

with z_ij homogeneous of normal degree two and r_ij homogeneous of normal degree four. Here z represents the actual zeta. The logarithmic quartic term r satisfies the Baker–Campbell–Hausdorff gluing equation; in a consistent Čech convention its coboundary is minus one half of the bracket of the quadratic terms on triple overlaps. It is NOT generally a cocycle and is NOT set to zero.

For a leading section s_0 and a chosen first correction s_1 satisfying the first gluing equation, the second gluing defect is represented, with compatible transport, by

    [r_ij,s_0] + [z_ij,s_1,j]
      + (1/2)[z_ij,[z_ij,s_0]].                       (5)

Changing s_1 by a global special-fiber section changes this class by delta_q of that section. Changes of projective frames or logarithmic representatives give the same secondary class in (4), because it is the obstruction of the actual parameter-truncated family. Formula (5) is a display of that intrinsic class, not its definition.

The absence of a free invariant fourth-order comparison class only gives uniqueness up equivariant comparison once the preceding data are fixed. It does not remove r or the quadratic term in (5).

## 3. First corrections can be chosen on the whole plane, but not in a single normal degree

A special-fiber section is represented by an actual linear normal polynomial

    s_0 in H0(B_R(3)) tensor W.

Its first gluing defect is the cubic [z,s_0]. Harmonic reduction under q_-=-q_+ produces:

- a degree-three harmonic cocycle with coefficient in B_R(1);
- a degree-one harmonic cocycle with coefficient in B_R(3), obtained by multiplying the q_-W part by -q_+.

Membership in ker(delta_q) says the first cocycle vanishes already in H1(B_R(1)), since restriction to B_R(1)|3C is injective on H1. The second cocycle is always exact on the whole plane because H1(B_R(3))=0. Hence one can choose a first correction s_1 on a cover of R with harmonic degrees one and three only, and plane coefficients B_R(3) and B_R(1), respectively.

The degree-one correction must not be omitted. It is precisely the compensation for the q_-W component discarded in the first obstruction. Restricting an assumed pure degree-three primitive would miss it.

The degree-three primitive is unique modulo changes of reference frame, since H0(B_R(1))=0. The remaining degree-one freedom is exactly the original thirty-dimensional space of global special-fiber sections.

## 4. Exact reduction from seventy-eight to thirty dimensions

Using the first corrections just constructed, every term in (5) has normal polynomial degree at most five. After harmonic reduction it has only degrees one, three, and five, with coefficient bundles

    B_R(3),  B_R(1),  B_R(-1),

respectively. The resulting components are cocycles on the whole plane. The degree-one cohomology is zero. The degree-three cohomology is the twelve-dimensional space

    H1(B_R(1)) tensor (Sym^3 W/q_-W),

which is exactly the entire first-boundary image because delta_q is surjective.

Only the degree-five class remains in the secondary quotient. Its target is the one in (1). This identification is independent of a choice of harmonic complement: changing a quintic representative by q_- times a cubic sends it, using q_-=-q_+, into the degree-three image, with a possible degree-one component whose H1 is zero.

The resulting thirty-dimensional target injects into (4). On the highest harmonic summand, this follows from the restriction sequence

    0 -> B_R(-5) -> B_R(-1) -> B_R(-1)|2C -> 0

and H1(B_R(-5))=0. The analogous degree-three injection was proved in the first-obstruction note. Therefore no part of the secondary obstruction is lost in replacing (4) by (1).

Conversely, if the class in (1) is zero, the only remaining secondary cohomology is in the first-boundary image. Changing the degree-one first correction by a global special-fiber section cancels it because delta_q is onto that image. The remaining defect is a coboundary and can be removed by a second correction. This proves the claimed equivalence with lifting through t squared, or epsilon to the fourth power.

## 5. Intrinsic construction of the root maps from actual normal neighborhoods

Let lambda be a point of P(W*), regarded as a negative direction. The actual linear three-space

    P3_lambda=P(V_+ directsum lambda)

contains R as a hyperplane. Its formal normal line has conormal O_R(-1) tensor lambda*. Projection onto R is defined on all the finite neighborhoods under consideration.

Restrict B(3) to the third normal neighborhood of R inside this P3, push forward to R, and take inversion invariants. Call the result E_lambda^1. Likewise let E_lambda^2 be obtained from the fifth normal neighborhood. Their invariant even graded pieces give exact sequences

    0 -> B_R(1) tensor (lambda*)^2
      -> E_lambda^1 -> B_R(3) -> 0,                   (6)

    0 -> B_R(-1) tensor (lambda*)^4
      -> E_lambda^2 -> E_lambda^1 -> 0.               (7)

No splitting is asserted for either sequence. Their transition functions contain precisely the actual quadratic and quartic normal information of F.

The boundary in (6) is the actual first cup map mu_(zeta(lambda)), proved surjective in the first-obstruction note. Since H0(B_R(1))=0, each element of its kernel has a UNIQUE lift to H0(E_lambda^1). Thus

    H0(E_lambda^1)=ker(mu_(zeta(lambda))),  dimension 9,
    H1(E_lambda^1)=H2(E_lambda^1)=0.                   (8)

The boundary of (7) consequently defines the canonical secondary root map

    beta_lambda:ker(mu_(zeta(lambda)))
        -> H1(B_R(-1)) tensor (lambda*)^4.            (9)

It has no quotient ambiguity from a first correction, because H0(B_R(1))=0. The exact section sequence is

    0 -> H0(E_lambda^2) -> ker(mu_lambda)
      --beta_lambda--> H1(B_R(-1)) tensor (lambda*)^4
      -> H1(E_lambda^2) -> 0,                         (10)

with H2(E_lambda^2)=0. In particular injectivity of beta_lambda is exactly absence of an inversion-even B(3) section on this actual fifth normal neighborhood. It is not an assertion about the full formal neighborhood or global P4.

This construction proves choice independence without making a convention for the signs in (5).

## 6. Algebraic family of root maps and exact evaluation on the two roots

Over P(W*), the tautological negative direction has dual O(1). The sequences (6)-(7) therefore form algebraic families with kernel twists O(2) and O(4). Since the first cup is onto at every direction, cohomology and base change give the actual vector bundle sequence

    0 -> K -> H0(B_R(3)) tensor O
      -> H1(B_R(1)) tensor O(2) -> 0.

Its ranks are 9,15,6 and deg K=-12. The next relative boundary is exactly the bundle map beta in (2). The source is not replaced by a trivial rank-nine bundle. Equivalently, the relative derived cohomology of E^2 is represented by the two-term complex

    [K --beta--> H1(B_R(-1)) tensor O(4)].             (11)

Let lambda_1,lambda_2 be the two roots of q_-. Evaluation of linear and quintic normal forms gives

    W=H0(O_(Z(q_-))(1)),
    Sym^5 W/q_-Sym^3 W=H0(O_(Z(q_-))(5)).              (12)

The first kernel therefore identifies with H0(Z(q_-),K(1)). In the highest degree-five component of (5), evaluation at a root eliminates every q_-multiple. The degree-three primitive is exactly the unique first lift in (8), while the degree-one compensation contributes only to lower normal degree and disappears from this component. The remaining class is beta_lambda applied to the corresponding root section, with its degree-one evaluation-line factor.

This proves (3). In particular the positive equation q_+ has disappeared for a justified reason: it occurs in the lower harmonic compensation, not in the highest degree-five root obstruction. This is not permission to omit it before taking the correct quotient.

## 7. What remains open

Let r be the generic rank of the actual algebraic map beta on P(W*). Its rank-drop set away from the generic rank is finite. A general nondegenerate q_- has both roots in the rank-r open, so

    rank(Delta_q)=2r,
    dim ker(Delta_q)=18-2r.                            (13)

The torsion-free pushforward lattice of the finite scaling family maps into both successive obstruction kernels. Together with uniform H0(I^9 B_Q(4))=0, this proves

    h0(B_Q(4))_- <= 18-2r

on the corresponding generic even-quadric open. No value of r, and no nonzero minor of beta, is proved here. If r=9, odd vanishing would follow; if r<9, further actual normal and parameter obstructions may still kill survivors.

The new result is an exact quartic-neighborhood operator and its two-root reduction. It preserves the nonlinear fourth normal term, its interaction with the first correction, all evaluation-line twists, and the finite-neighborhood versus global distinction.

## 8. A finite hyperplane endpoint after one further boundary

The root construction also has a precise global endpoint on H_lambda=P3_lambda, separate from global sections on Q. Let E_lambda^3 be the inversion-even pushforward of B(3) on the seventh normal neighborhood of R in H_lambda. Its additional even layer gives

    0 -> B_R(-3) tensor (lambda*)^6
      -> E_lambda^3 -> E_lambda^2 -> 0.

Since H0(B_R(-3))=0, the resulting next boundary is

    gamma_lambda:ker(beta_lambda)
        -> H1(B_R(-3)) tensor (lambda*)^6,
    dim H1(B_R(-3))=h1(B_R)=12.                       (14)

Its source is the actual section space of E_lambda^2 from (10), not the whole original nine-space. A section in this source has a unique preceding lift because all intervening negative H0 groups vanish. No value of the boundary (14) is asserted.

For every even normal degree m>=8, self-duality and Serre duality give

    H1(B_R(3-m))=H1(B_R(m-6))*=0,

since m-6>=2. The corresponding H0 groups are also zero. Thus inversion-even sections extend uniquely at every later normal step. Odd normal layers have negative inversion character and add no invariant layer.

Finally, global sections on the formal neighborhood of the hyperplane R in P3 agree with global sections on P3. Indeed, for E=B|H_lambda(3), the divisor-power sequence

    0 -> E(-m) -> E -> E|_(mR) -> 0

has H0(E(-m))=H1(E(-m))=0 for m sufficiently large, by negative absence of sections and Serre duality followed by positive Serre vanishing on P3. This comparison is inversion-equivariant. Therefore

    H0(H_lambda,B|H_lambda(3))_+ = ker(gamma_lambda).   (15)

This proves that beta and the one subsequent normal-degree-six boundary form a finite exact section test for the actual hyperplane restriction. It does not assert hyperplane vanishing and does not identify it with the global odd quadric problem.

There is also an independent ambient description of the same endpoint. If ell is the odd linear equation of H_lambda, the actual sequence

    0 -> B(2) tensor <ell> -> B(3) -> B|H_lambda(3) -> 0

and H0(B(2))=H0(B(3))=0 identify (15) with the kernel of the actual odd-linear multiplication map

    H1(B(2))_- tensor <ell> -> H1(B(3))_+,
    dimensions 44 -> 46.                              (16)

The defining-line character is retained in (16); it is what turns the negative source parity into positive parity. No injectivity of this actual pencil is assumed.

## Dependencies

ODD-FIRST-SCALING-OBSTRUCTION.md proves the actual first cup formula, surjectivity of every nonzero coefficient cup, the thirty-to-twelve first gate, and the finite-family section-lattice bound. ACTUAL-AMBIENT-SECOND-NORMAL-NONVANISHING.md, published at b3fc992ebba27fc28967f934bf9966148eb86961, supplies zeta!=0. The established actual plane lemma gives H0(B_R(1))=0 and H1(B_R(1))=V directsum A; the symmetric-square Steiner resolution gives H1(B_R(t))=0 for t>=2 and all negative-twist consequences used here. The uniform conic splitting bound a<=1 and uniform I^7 detection justify the finite-family statements without a balanced-conic assumption.

No selected HM coefficients, actual matrix evaluation, rank scan, public write, or vanishing inferred merely from a missing invariant parameter is used.
