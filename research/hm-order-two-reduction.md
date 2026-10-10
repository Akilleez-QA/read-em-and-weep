# A lift-independent component of the second-order test

Status: a reduction to a specified obstruction component. Its value has not yet been computed. No solution of the eightfold theorem is claimed.

## Fixed data

Let C:y²=x³−x and X=C⁴. Let E be the rank-two determinant-trivial Horrocks–Mumford pullback described in [the carrier and atlas note](https://github.com/Akilleez-QA/read-em-and-weep/pull/2), with c₂(E)=15θ².

Write V_i=y_i∂/∂x_i+(3x_i²−1)∂/(2∂y_i). These are commuting global holomorphic vector fields. Fix
π=V₁∧V₂+V₃∧V₄,
Π=ι_π(θ²)/2,
ξ=π+15Π ∈ HH²(X),
using the HKR action convention ι_π exp(λθ)=λ²Π exp(λθ).

The rank-two trace-free curvature identity makes the contracted Atiyah square scalar. Its value is −15Π·id_E; the gerbe summand contributes +15Π·id_E. Thus ev_E(ξ)=0. This is a first-order statement.

## General second-order equation

For any fixed second-order ambient extension of ξ, choose a first-order lift a of E. Its second-order obstruction O₂(a) lies in Ext²(E,E). Replacing a by a+u, with u∈Ext¹(E,E), changes this obstruction by
O₂(a+u)=O₂(a)+L_ξ(u)+u∪u,
where L_ξ is linear in u and linear in the chosen first-order ambient data. Changing the second-order ambient extension by η∈HH²(X) adds ev_E(η), up to the sign convention used for the obstruction.

These are cohomology statements. A nonzero cocycle before passing to Ext², or a nonzero obstruction for one arbitrarily chosen lift, is not by itself a no-lift theorem.

## Deck-character reduction

The group G=(Z/2)⁴ acts by y_i↦−y_i. Label a character by a subset S⊂{1,2,3,4}; multiplication of characters is symmetric difference.

The explicit finite-RHom calculation gives
Ext¹(E,E)_S=0 for |S|=2,3,4.
The checked rank data are:
- |S|=2: source640; successive ranks450,100,90.
- |S|=3: source1280; successive ranks1250,30.
- |S|=4: source2560; successive ranks2550,10.

The finite model and executable certificate supply the precise matrices and Čech contraction. In particular, this conclusion uses the higher transferred differentials, not only the first matrix rank.

Consequently every u has only characters of weight0 or1. The two summands of ξ have characters {1,2} and {3,4}. A character-compatible baseline first-order lift can be chosen by projecting a solution of the linear lift equation onto these two characters.

Its quadratic obstruction can have only trivial and full-sign {1,2,3,4} characters. The full-sign projection is unchanged by every first-order choice:
- u∪u has weights0,1,2;
- L_ξ(u) has weights1,2,3.

It is also unchanged by every second-order ambient acceleration. Indeed HH²(X)=H⁰(Λ²T_X)⊕H¹(T_X)⊕H²(O_X) has only weights0 and2, and evaluation respects characters.

Thus the class
O_full = pr_{ {1,2,3,4} } O₂(a)
is well-defined independently of these choices. A nonzero value would obstruct every second-order lift with the prescribed first-order direction. A zero value would only pass this one necessary test.

This argument does not require the stronger assertion that the entire linear term L_ξ vanishes.

## Required chain-level calculation

To calculate O_full one still needs:
1. A specified second-order star-algebroid extending ξ.
2. Its action on the explicit bundle transitions, including overlap algebra automorphisms.
3. An actual first-order null-homotopy.
4. The resulting second-order cocycle.
5. Its image in the checked finite-RHom model, followed by the full-sign projection and a cohomology test.

The algebraic representative q=y/x of H¹(O_C) is useful, but products of such functions representing Π are not central under Moyal multiplication. Treating exp(hb) as a central gerbe cocycle without correcting overlap automorphisms gives an invalid calculation.

There is an explicit starting identity:
V(q)=(x+x⁻¹)/2=δ(a), with a₀=−x/2 and a_∞=x⁻¹/2.
It can be used to construct rational overlap derivations for a chosen second-order algebroid. Its cup-product signs, compatibility equations and module equations must be included in the calculation.

No value of O_full is asserted here.
