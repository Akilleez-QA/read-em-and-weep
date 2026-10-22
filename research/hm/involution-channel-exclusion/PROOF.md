# Six polar lines and the Plücker quadric exclude the involution channel

## Statement and inputs

Work over C. Let G=A5, let A be either three-dimensional rotation representation, and let P be the irreducible four-dimensional representation. Set X=P(A), with invariant nonsingular quadratic form B and its square conic C. Use the canonical endpoint interface

0 → K → D⊗O_X → A⊗O_X(1) → 0,
F=K*⊗P⊗O_X(2),
E:Q⊗O_X → F,
Q=Q_+⊕Q_−,

where D has dimension five, K has rank two, both one-dimensional channel spaces are trivial G-modules, and t_q:K→P⊗O_X(2) is the section associated with q∈Q.

Pinned structural inputs are:

- PR661, commit 1325647fd916bf2daa71b11efeae6d52cfefa2cd: this canonical kernel and two-channel interface.
- PR663, commit ad3ab59f6fbbbb3e5bde1da58b3b92a1f49c6889: neither parity section vanishes; E has rank at least one everywhere; its rank is exactly one at the six C5 axes and ten C3 axes.
- PR664, commit 90d9aa88b3cea99e8dd1acea0acda9095021185e: the support of the rank-at-most-one scheme Δ of E is either these sixteen axes or all thirty-one C5/C3/C2 axes.
- PR667, commit 7d53ea234b99b75e89a29c4caba7ec564e134410, Sections 2–4 only: every q with nonzero symmetric component gives a fixed map t_q whose restriction to C has generic rank two. This is the universal osculating-bundle theorem, not the later actual-normal-variation specialization.

**Theorem.** The C2 axes do not belong to Δ. Consequently Supp(Δ) is exactly the six C5 and ten C3 axes.

Combining this with the separately proved reduced-channel theorem of PR668, commit ca3c34c40363bde6315a0797eb66a5d3ea68c104 (research/hm/reduced-channel-degeneracy/PROOF.md), gives the stronger scheme statement: Δ is exactly the reduced union of those sixteen axes; there are precisely two exceptional projective channels, one vanishing exactly at the six reduced C5 axes and one exactly at the ten reduced C3 axes. All other nonzero channels are nowhere zero as sections of F.

The exclusion below does not require that separate reduced-channel theorem or the fixed-channel length bound. It uses only structural symmetry and polynomial identities, without selected actual HM/source-instance evaluation, coefficient calculation, rank evaluation, parameter scans, or large computation.

## 1. The polar six-line arrangement

Let Σ5 be the set of six C5 axes in X. An axis is the positive eigenline of its cyclic rotation subgroup; its projective stabilizer is its dihedral normalizer D10. In particular there are five involutions stabilizing each C5 axis. There are fifteen involutions in G, all conjugate. Counting incidences (p,g) with p∈Σ5 and g an involution fixing p gives 6·5=30. Consequently every involution fixes exactly two distinct points of Σ5.

For an involution g the representation A has eigenvalues (1,−1,−1). Let a_g be its positive axis and N_g its negative eigenspace. Its positive eigenline is not a C5 axis: the C2 and C5 axis orbits are distinct. Thus its two fixed C5 axes lie in P(N_g). The invariant bilinear form makes the two eigenspaces orthogonal, so N_g=a_g^⊥.

For p∈Σ5 define its polar line L_p=P(p^⊥). If p and p′ are the two C5 axes fixed by g, the preceding orthogonality shows

                         L_p ∩ L_p′ = {a_g}.                 (1)

The lines L_p and L_p′ are distinct since polarity is an isomorphism from projective points to projective lines. Distinct involutions have distinct positive axes: an orthogonal determinant-one involution is determined by its nonisotropic positive eigenline, acting as −1 on its orthogonal complement. Hence the assignment g↦{p,p′} is injective by (1). Both the involution set and the set of unordered pairs of six points have size fifteen, so the assignment is bijective.

It follows that the fifteen pairwise intersections of the six polar lines are distinct and are exactly the fifteen C2 axes. In particular no three lines are concurrent, and each line contains exactly five of these axes. This proves every incidence needed below directly; no presumed general-position configuration or coordinate realization is being used.

Let F6 be the product of nonzero equations for the six lines. Its degree is six, and its divisor is G-invariant. Therefore its span is a one-dimensional G-representation. Since A5 has no nontrivial characters, F6 is G-invariant. Different choices of equations merely rescale F6.

## 2. Septics doubly vanishing at the intersections contain all six lines

Let Σ2 be the fifteen pairwise intersections above. If a homogeneous septic f belongs to m_p² locally at every p∈Σ2, then every L_p divides f.

Indeed, if f did not vanish identically on one of the lines, its restriction would be a nonzero section of O_{P1}(7). Each of the five distinct intersection points on that line contributes order at least two, since restriction sends the surface maximal ideal squared into the square of the curve maximal ideal. This would give at least ten zeros counted with multiplicity, exceeding seven. Thus the restriction is zero. The six distinct linear factors all divide f, proving

               H⁰(X,I_{Σ2}^{(2)}(7)) ⊂ F6·H⁰(X,O_X(1)).    (2)

Here I_{Σ2}^{(2)} denotes the ideal sheaf with stalk m_p² at each of the fifteen reduced points. In fact equality holds, since F6 itself has multiplicity two at each pairwise intersection. Only the displayed containment is needed.

## 3. A hypothetical C2 channel produces a linear exterior covariant

Suppose that E has rank one at a C2 axis. Its kernel is a line Cq⊂Q, and t_q vanishes there. Because Q is a trivial G-module and t_q is an equivariant section, t_q then vanishes at every point of the transitive C2 axis orbit Σ2. Neither parity section vanishes anywhere, so q has both parity components nonzero. In particular PR667's universal statement applies and gives Λ²(t_q)≠0.

The determinant of the kernel sequence is equivariantly

                         det K ≅ O_X(−3).

The possible constant determinant factors of D and A are trivial because they are characters of A5. Thus the exterior square is a nonzero equivariant section

             w_q=Λ²(t_q) ∈ H⁰(X,Λ²P⊗O_X(7)).             (3)

Every local matrix entry of t_q belongs to m_p at p∈Σ2. Each 2×2 minor consequently belongs to m_p². Applying (2) to every scalar component of (3) gives a unique factorization

                         w_q = F6·j,                      (4)

where j∈Λ²P⊗H⁰(X,O_X(1)) is nonzero. Since both w_q and F6 are invariant, so is j. Equivalently j is a nonzero G-equivariant linear map

                          j:A → Λ²P.                      (5)

All determinant and parameter twists have been included; the remaining covariant is genuinely linear, not a rational or twisted map.

## 4. The unique three-dimensional summand is not a plane of decomposable bivectors

For completeness, the four-dimensional character on the classes (1,2,3,5a,5b) is

                         χ_P=(4,0,1,−1,−1).

It is the permutation representation on five letters minus the trivial representation. The identity χ_{Λ²P}(g)=(χ_P(g)²−χ_P(g²))/2 gives

                         χ_{Λ²P}=(6,−2,0,1,1).

The two inequivalent three-dimensional characters are

                 (3,−1,0,φ,ψ),   (3,−1,0,ψ,φ),

where φ=(1+√5)/2 and ψ=1−φ. Hence

                         Λ²P ≅ A ⊕ A′,                   (6)

with A′ inequivalent to A and both summands occurring once. This is a universal representation identity, not an evaluation of an actual endpoint map. By (5), j identifies A with the unique A summand, up to nonzero scalar.

Exterior multiplication defines a symmetric nondegenerate pairing

              β:Λ²P×Λ²P → Λ⁴P ≅ C,
              β(u,v)=u∧v.                                (7)

Nondegeneracy is the usual complementary-basis pairing on bivectors in dimension four. The target is the trivial G-module because det P is a character of A5. Both A and A′ are self-dual, so Schur's lemma makes them orthogonal for β: an off-diagonal pairing would yield a nonzero map A→(A′)*, impossible. Consequently β restricts nondegenerately to each summand. Its restriction to j(A) is in particular not identically zero on the diagonal; in characteristic zero an identically zero diagonal of a symmetric form would imply that the entire form vanished by polarization. Thus

                        j(a)∧j(a)

is a nonzero homogeneous quadratic polynomial in a with values in Λ⁴P. More precisely it is a nonzero scalar multiple of the invariant quadratic B(a,a).

## 5. Plücker gives the contradiction

The exterior square of a rank-two source map is always decomposable fiberwise. Accordingly the section (3) satisfies the polynomial Plücker identity

                          w_q∧w_q=0.                      (8)

Substituting (4) gives F6²(j∧j)=0 as a polynomial with values in the one-dimensional space Λ⁴P. The homogeneous coordinate ring Sym(A*) is an integral domain and F6≠0, so j∧j=0. This contradicts Section 4.

Therefore no fixed channel can vanish on the C2 orbit. Since E has rank at least one everywhere, a point of its rank-at-most-one locus has a nonzero kernel channel; the contradiction excludes all C2 axes from Δ. The support alternative of PR664 now proves the theorem.

## Contribution and limits

The previously unresolved 16-versus-31 alternative for the family-detection support is resolved in favor of sixteen. With the independently established reduced-channel result, this also resolves the scheme and exceptional-channel alternatives: Δ has length sixteen and exactly two distinct reduced fixed-channel fibers, of lengths six and ten.

This does not identify the actual HM family with either exceptional channel, compute a numerical parity ratio, evaluate any selected actual endpoint or source instance, determine the next ambient division or fourth Bockstein, prove prescribed-source membership or higher lifting, settle the (1,3) Gauss/full affine R2/global monad-homotopy questions, or repair the original theorem. The rank of E, the zero scheme of t_q, and the rank of a fixed map K→P(2) remain distinct notions throughout.

Sources:

- https://github.com/Akilleez-QA/read-em-and-weep/pull/1
- https://github.com/Akilleez-QA/read-em-and-weep/pull/661
- https://github.com/Akilleez-QA/read-em-and-weep/pull/663
- https://github.com/Akilleez-QA/read-em-and-weep/pull/664
- https://github.com/Akilleez-QA/read-em-and-weep/pull/667
- https://github.com/Akilleez-QA/read-em-and-weep/blob/ca3c34c40363bde6315a0797eb66a5d3ea68c104/research/hm/reduced-channel-degeneracy/PROOF.md
