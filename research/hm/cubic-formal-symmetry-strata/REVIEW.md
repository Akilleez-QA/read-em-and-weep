# Independent mathematical review

Verdict: PASS, conditional on the pinned input theorems.

Reviewed artifact: PROOF.md, SHA256

    1aa09bf88477682ce3502485b1265d50379e05bfd1f3af85a888847fd529f06c

The review checked the complete argument, including the effective and finite-type consequences in Section 5, against the prorepresentability and automorphism statements of PR634, the representation and fixed-dimension statements of PR626/627, the effectivity and formal-faithfulness argument of PR628, and the arbitrary finite polarized jet realization theorem of PR630 Section 1. This is independent mathematical review, not proof-assistant verification or a new verification of every earlier dependency.

## Checks

1. **Action and linearization.** Changing a marking by left composition gives a genuine natural action. Taking inverse pullback on functions gives the dual left representation, so the averaged cotangent section has the stated equivariance. Its images lift a cotangent basis, and regularity of the complete local ring makes the resulting power-series substitution invertible. This proves all-Artin equivariance, rather than assuming that tangent linearization alone controls the formal functor. No algebraic equivariant slice follows or is claimed.

2. **Automorphisms and fixed functors.** The small-extension kernel is H0(Theta_V) tensor J and vanishes. Thus reduction is injective for every Artin base, and lifts of a specified special-fiber element are unique. A fixed re-marked class gives the lift, with the inverse marking convention handled explicitly. Uniqueness forces the group law, proving that fixed classes and specified H-equivariant deformations agree. Quotienting the power-series ring by the linear H-differences yields precisely the power-series ring on the dual of T^H. Intersections correspond to generated subgroups.

3. **Arrangement versus point functors.** The finite intersection of the linear prime ideals gives a reduced formal arrangement whose dimension is the maximum component dimension, namely 288 by PR627. The note correctly does not identify its Artin-valued points with the union of the component point sets, nor assert a nonempty open complement inside the one-point formal spectrum. These qualifications avoid two otherwise genuine errors.

4. **Delayed threshold.** For n<k, t^k v vanishes in A_n. For n>=k its fixed-element equation is t^k(gamma(v)-v)=0; since the coefficient vector is over C and t^k is nonzero in A_n, it forces gamma(v)=v. Choosing v in T_free therefore gives full Gamma below k and the trivial group at and above k. The k>=2 case genuinely has zero first-order class, while its kth-order class is nonconstant. This is a new higher-order construction, not a restatement of the earlier free first-order theorem.

5. **Realization and persistence.** PR628 applies to the compatible polarized system without requiring nonzero first-order variation. PR630 Section 1 realizes its jet modulo t^(k+1), again without that requirement. Identity at order k propagates to all later orders by the zero reduction kernels even when the approximating higher terms differ. Proper formal faithfulness over either complete or ordinary local DVR then eliminates global fixed-base automorphisms. Finally, flatness over integral B makes the generic fiber schematically dense, justifying the equalizer argument for Aut_B(Y). These claims do not require every generic-fiber automorphism to extend, and do not imply that it does. The note correctly refrains from importing the nonzero-first-order section-loss proposition.

6. **Unmarked groupoid.** For chosen representatives with markings alpha_x and alpha_y, an unmarked isomorphism f:X_x -> X_y corresponds to gamma=alpha_y f_C alpha_x inverse and y=gamma.x. Existence and uniqueness for a prescribed gamma give the action groupoid; compositions multiply these elements. Thus the orbit and stabilizer assertions are valid. The sign-action example correctly demonstrates both failure of surjectivity and failure of injectivity of orbit sets into invariant-ring Artin points.

## Scope

All arguments are structural and use no selected HM/source coefficients, points, matrices or rank evaluations, and no large computation. The proof distinguishes marked formal universality, effective schemes over C[[t]], finite-jet realization on finite-type curves, and geometric generic-fiber automorphisms. The latter remain undetermined. Scalar automorphisms of polarized pairs remain, and no original full-adjoint or Weil-class algebraicity conclusion is asserted.
