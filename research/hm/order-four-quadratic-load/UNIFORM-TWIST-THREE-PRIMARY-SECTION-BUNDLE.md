# The uniform twist-three primary section bundle

## Theorem

Let pi:Hcal -> T=P(W*) be the universal pencil of hyperplanes containing the positive fixed plane R, and let F be the normalized actual HM bundle. With the established linearizations, every fiber satisfies

    h0(F_H(3))=12, H^i(F_H(3))=0 for all i>0.

The equivariant section bundle splits as

    pi_* F_Hcal(3) = P4 O_T plus T6 O_T(-1) plus W O_T(-2).

The first two summands have physical inversion parity even and the final summand odd. The splitting exists equivariantly; no assertion of a preferred splitting of the even extension is needed.

This is a uniform argument, including the twelve order-five parameters. It strengthens the special-fiber primary vanishing independently proved from the ribbon curve.

## 1. Inputs and higher ambient vanishing

The established ambient primary groups are

    H0(F(2))=0,
    H0(F(3))=P4 (even),
    H1(F(2))=(1 plus A) (even) plus T6 (odd),
    H1(F(3))=W (odd).

The actual hyperplane two-section bundle is

    Y2=pi_*F_Hcal(2)=W O_T(-3),

and its sections are physical inversion-even. In particular h0(F_H(2))=2 for every parameter. The actual fixed-plane restriction F_R(3) has inversion-even fibers, hence all its sections are even.

For clarity, H2(F(2))=0 is not an inference from an Euler characteristic. The normalized monad has terms

    5 O(-1), 2 Omega²(2), 5 O.

After twist 2 or 3, each term has no positive cohomology: the middle terms are Omega²(4) or Omega²(5), with the same vanishing by the exterior Euler sequence (equivalently the elementary Bott calculation). Let K be the kernel of the monad's right surjection. The two short exact sequences

    0 -> K -> middle -> right -> 0,
    0 -> left -> K -> F(t) -> 0

then show H^i(F(t))=0 for i>=2, t=2,3. The possibly nonzero H1 is deliberately retained.

The monad and its normalization are explicitly recorded in RANK-ONE-VERTEX-SECTION-CURVE.md, section 5. GENERIC-BETA-ABELIAN-INTERPOLATION.md, section 4, separately records H2(F(2))=0; FULL-ADJOINT-PENCIL-INVOLUTION-BLOCKS.md, section 1, records concentration in H1 at F(2). These are precise source-file dependencies, not assertions that every file occurs at a single immutable commit.

## 2. Exactly two odd fiber sections

Fix H and let u_H be its remaining negative linear coordinate, so R is the Cartier divisor (u_H=0) in H. Restriction gives

    0 -> F_H(2) --u_H--> F_H(3) -> F_R(3) -> 0.

Since the last term has no odd sections, every odd section of F_H(3) is divisible by u_H. The quotient section is even, and conversely multiplication by u_H sends each of the two even sections of F_H(2) to an odd section of F_H(3). Therefore

    H0(F_H(3))_- = u_H H0(F_H(2)), dimension 2.     (1)

This uses the actual restriction sequence and parity, not a generic-rank expectation.

## 3. Ambient multiplication is uniformly surjective

The ambient hyperplane equation ell is odd. The sequence

    0 -> F(2) --ell--> F(3) -> F_H(3) -> 0

yields

    0 -> P4 -> H0(F_H(3)) -> H1(F(2)) tensor <ell>
      -> W -> H1(F_H(3)) -> 0.

The last zero is justified by H2(F(2))=0. Accounting for the odd factor ell, the only nonzero target block is

    (1 plus A) tensor <ell> -> W,

of dimensions four to two and physical odd parity. Since P4 is even, equation (1) identifies its kernel with the two-dimensional odd section space. Thus this map is surjective on every fiber. The other target parity is zero. Consequently

    H1(F_H(3))=0,
    h0(F_H(3))=4+(10-2)=12.

The same restriction sequence and the higher ambient vanishings prove H2(F_H(3))=H3(F_H(3))=0. Cohomology and base change therefore applies in every degree: the section bundle is locally free of rank twelve, and the higher direct images vanish.

## 4. Bundle splitting with the correct normal-coordinate twist

The negative coordinate line remaining on H is the tautological quotient

    W* O_T / O_T(-1) = O_T(1).

Thus the fiberwise multiplication in (1) globalizes without zeros and identifies the odd section bundle as

    (pi_*F_Hcal(3))_- = Y2 tensor O_T(1)
                      = W O_T(-2).               (2)

This sign of the twist is essential; it is the quotient of linear coordinate functions, not its dual.

For the even bundle, the ambient exact sequence gives

    0 -> P4 O_T -> (pi_*F_Hcal(3))_+
      -> T6 O_T(-1) -> 0.                         (3)

The extension group is a tensor factor times H1(O_T(1))=0. Hence (3) splits. Since G is finite in characteristic zero, averaging a splitting makes it equivariant. Combining (2) and (3) proves the stated bundle decomposition.

The center signs agree with physical parity: T6 and O(-1) each have negative center, so their tensor product is even; W O(-2) is odd. No character is silently discarded in the normal-coordinate multiplication.

## Limits

This uniform primary result removes the primary correction in all twist-three symmetric-square obstruction comparisons where the same regular-section diagram applies. It does not on its own assert that a given adjoint polynomial shadow fails to extend. The separate special-octic nonextension argument supplies that additional actual geometry for the a=18 exclusion. No actual coefficients, selected ranks, scans, or experiments occur here.
