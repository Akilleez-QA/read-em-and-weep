# Invariant ordered Yoneda products vanish

Let E=N⊗(σq)*H on the product elliptic carrier described in COEFFICIENT-FAMILY.md. The smooth coefficient family has tangent image the full 79-dimensional invariant Ext¹, by COEFFICIENT-FAMILY.md and INVARIANT-COHOMOLOGY.md. Every ordered product of two invariant Ext¹ classes is zero. Only this invariant statement is included; no non-invariant-character classification is needed.

## 1. Rank-two identity with signs and normalization

Let E be any rank-two holomorphic vector bundle on a complex manifold. Use the Dolbeault differential graded algebra

    A^{0,*}(End E),   differential ∂̄,

whose product is exterior product of forms together with composition of endomorphisms. This algebra computes Ext^*(E,E) and its ordinary Yoneda multiplication.

For trace-free endomorphisms A and B of a two-dimensional vector space, the formal Cayley–Hamilton identity and its polarization give

    AB + BA = tr(AB)·Id.                              (1)

For example, polarize A²=(tr(A²)/2)·Id. The trace of AB+BA is 2tr(AB), so the scalar on the right side of (1) is tr(AB), not tr(AB)/2.

Now take trace-free End E-valued (0,1)-forms α and β. Locally write

    α = Σ_i A_i θ_i,    β = Σ_j B_j θ_j,

where the θ_i are scalar (0,1)-forms. Reindexing the second product and using θ_j∧θ_i=−θ_i∧θ_j yields

    α∧β − β∧α
      = Σ_{i,j} (A_i B_j + B_j A_i) θ_i∧θ_j
      = Σ_{i,j} tr(A_i B_j) θ_i∧θ_j ·Id
      = tr(α∧β)·Id.                                  (2)

This equality is pointwise and is independent of the frame of E. There is no factor 1/2 in (2). It is the ordinary difference of the two products, not the graded commutator: for degree-one inputs, the graded commutator is α∧β+β∧α.

If α and β are ∂̄-closed, all terms in (2) are closed. Passing to cohomology gives

    a∪b − b∪a = tr(a∪b)·Id                          (3)

for classes represented by trace-free forms. The scalar-to-endomorphism map on the right is induced by O→End E, f↦f·Id.

## 2. Trace-free representatives of invariant classes

In characteristic zero there is a canonical splitting

    End E = O·Id ⊕ End₀ E,

with projection onto the first factor given by A↦(tr(A)/2)·Id. It commutes with the Dolbeault differential and with the geometric symmetry action.

Consequently any class a∈H¹(End E) whose trace vanishes in H¹(O) has a closed trace-free Dolbeault representative. Explicitly, if α is a closed representative, put

    α₀ = α − (tr(α)/2)·Id.

Then α₀ is closed and trace-free. Since tr(α) represents zero cohomology, the subtracted scalar-valued form is exact, and α₀ represents the same class a. No pointwise trace condition on an initially chosen representative is being assumed.

For the product elliptic double cover q:X=C⁴→Y=(P¹)⁴, the invariants of q_*O_X are O_Y. Finiteness and exactness of deck invariants in characteristic zero imply

    H^i(X,O_X)^G = H^i(Y,O_Y) = 0,    i>0.

In particular H¹(O_X)^G=H²(O_X)^G=0. These vanishings follow equally from Künneth: positive-degree O_X cohomology has only nontrivial deck characters.

The trace map is G-equivariant. Thus every invariant a∈Ext¹(E,E)^G has zero trace and admits the trace-free representative required in (3). The argument does not require the chosen representative itself to be deck-invariant, although averaging would also supply that property.

For invariant a,b, their product and its trace are invariant. Since H²(O_X)^G=0, equation (3) therefore implies

    a∪b = b∪a.                                      (4)

This is an equality of Ext² classes. The corresponding scalar Dolbeault form need not vanish identically; it is exact, which is precisely what is required.

## 3. The smooth invariant family kills the remaining symmetric part

The established smooth 79-dimensional coefficient family exhausts V₀=Ext¹(E,E)^G. Every v∈V₀ therefore extends to second order in an actual family, so its primary obstruction vanishes:

    v∪v = 0.

Applying this to v=a+b and subtracting the two diagonal equalities gives

    a∪b + b∪a = 0.                                  (5)

Combining (4) with (5) and using characteristic zero proves

    a∪b = 0    for all a,b∈V₀.                      (6)

Thus the whole ordered invariant-invariant multiplication is zero, including its previously unaddressed alternating part. Both inputs are necessary for this conclusion: the rank-two argument kills the ordinary difference in invariant Ext², while the actual smooth family kills the ordinary sum.

