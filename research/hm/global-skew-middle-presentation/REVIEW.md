# Independent review of the global skew-operator presentation

## Scope and verdict

I read the complete local `PROOF.md`. The universal bundle argument, the global presentation, and the vertex restriction computation are correct over the stated characteristic-zero field. Sections 4 and 5 correctly distinguish pointwise nonvanishing from simultaneous interpolation and from satisfaction of the monad-source equations. Nonvanishing of the actual shared input Y follows directly from fiberwise injectivity of the actual left monad arrow.

This review uses structural linear algebra and bundle arguments only. It does not evaluate selected HM/source coefficients, physical points, actual matrices, or ranks, and does not independently inspect the cited public source documents.

## Bundle and presentation checks

Writing D = det(U) tensor det(H), the canonical alternating form takes values in D tensor O(-1). The determinant-aware identification is

    sp(E)(4) = Sym^2(E(1))(3) tensor D^(-1).

Thus the displayed identification in the proof is correct under its fixed determinant trivializations. The wedge form on Lambda^2 F is symmetric, and tensoring with the alternating form on U gives the required alternating form on E.

The plus sign in the transvection formula is correct. Sections p and q of E(1) yield a twist-one skew operator after the determinant identification; a cubic coefficient gives twist four.

The graded symmetric-square resolution has the stated terms: degree-one factors contribute Lambda^2 G_1, whereas degree-two factors contribute Sym^2 G_2. All line bundles after twisting by three have no higher cohomology, and O(-1) has no cohomology at all. Consequently the exact global presentation and dimensions are correct:

    0 -> C^20 -> C^425 -> C^3000 -> C^7350
      -> H^0(sp(E)(4)) -> 0,

    h^0(sp(E)(4)) = 4755.

The original parameter-space relation kernel has dimension 2595.

On the vertex, E(1) splits as six copies of O(1) and six copies of O. The map from G_0 to its vertex global sections is surjective, with kernel U tensor Lambda^3 V. Multiplication of binary forms proves surjectivity of the restriction on global skew operators. The restricted operator space has dimension 390, and the restriction kernel in the 4755-dimensional operator space has dimension 4365. These are not dimensions of the kernel in the original 7350-dimensional parameter space.

## Section 4: vertex-cubic family

The space H^0(I_Z^3(3)) consists precisely of cubics in the positive coordinates. Multiplying the globally defined transvections by these cubics produces operators vanishing to at least third order along the entire vertex.

At a point with nonzero positive component, one such cubic has nonzero value. The Koszul evaluation map onto E(1) is surjective, and symmetric transvections span the symplectic Lie algebra of the fiber. Therefore this finite-dimensional global family generates the full skew-operator fiber away from Z. No point selection or rank experiment is needed. The additional nonzero negative-component hypothesis is used in the subsequent VV projection argument, not in this fiber-generation assertion itself.

For nonzero Y and nonzero ell, the functional T -> ell(TY) is nonzero on the symplectic Lie algebra. Nondegeneracy makes p -> beta(p,Y) a nonzero linear functional. Over C the two proper hyperplanes defined by ell(p) = 0 and beta(p,Y) = 0 cannot cover the fiber. A p outside their union gives

    ell(T_(p,p)Y) = 2 ell(p) beta(p,Y) != 0.

The proposed lift of a VV two-form is also correct. If w(e) = 1, then contraction with x sends e wedge i_v alpha to i_v alpha, because i_v squared is zero. Hence alpha - e wedge i_v alpha is in K_x and projects to alpha. This proves that the VV projection is onto when w is nonzero. It proves the nonvanishing of the induced functional provided the stated Cartan quotient functional itself is nonzero.

## The nonzero shared input

The proof uses direct fiberwise injectivity, retaining the actual monad's sign and determinant conventions:

At the relevant physical input, let the actual left monad arrow act by

    (s,t) -> (a_m A + b_m B)s + c_m C t.

For a_m and c_m nonzero, its value on (-u/a_m, z/c_m) is

    Y = Cz - Au - (b_m/a_m)Bu.

Since z is nonzero, this source vector is nonzero. Fiberwise injectivity of the actual left monad arrow therefore implies Y is nonzero.

This is a structural argument. It neither computes the value of Y nor requires actual coefficient matrices. Its hypotheses must be stated at the relevant inputs: a_m and c_m are nonzero, z is nonzero, and the left monad arrow is fiberwise injective there. In particular, injectivity should mean injectivity on that fiber, rather than merely injectivity as a sheaf map.

## Finite sets and the ramification caveat

For each fixed physical point with the required nonzero input and functional, evaluation defines a nonzero linear functional on the same finite-dimensional global family. Its zero locus is a proper hyperplane. A finite union of these hyperplanes cannot cover the family, proving simultaneous nonvanishing at any fixed finite collection.

This is not an interpolation theorem. The ramification locus in P^1 times P^1 does not by itself specify twelve canonical points in P^4. Relative positive/negative scalings, or equivalently physical points on the associated joining lines, must first be fixed. The quantifier proved is: for each such finite choice there exists a suitable operator. It is not: there exists one operator working at every physical point of all joining lines. The caveat already present in Section 4 makes this distinction correctly.

## Section 5: exact remaining limitation

The results exclude a universal pointwise obstruction coming solely from K-preservation, determinant skewness, and third-order vertex vanishing. They do not establish the image after imposing equivariance, source-parameter weights, or the coupled monad-arrow/source equations. Section 5 correctly leaves those conditions unresolved and makes no claim about a full primitive, the fourth Bockstein, a higher-order lift, or algebraicity.

The proof explicitly restricts its conclusion to global K-preserving determinant-skew middle operators before imposing the coupled monad-source equations; it does not claim a cochain-compatible construction.

## Final assessment

The proof is sound under its stated nonzero-channel and fiberwise monad-injectivity hypotheses. The physical-point caveat is essential and is correctly retained. I inspected and reran verify.py: it passed the bounded universal dimension arithmetic, contraction-squared cancellation on the ten constant three-form basis elements with free coordinate symbols, and formal transvection skewness cancellation. These checks contain no selected actual HM coefficients, physical point evaluations, or actual matrix ranks. No further actual-instance evaluation is warranted by this review.
