# Independent review: separation of the two invisible quartic lines

## Verdict

**PASS, conditional on the stated pinned inputs.** The new argument establishes that every nonzero member of the factoring line is nonzero as a full D-family at every point of the discriminant conic. The separation from the PR658 line, injectivity of the combined test, and the one-dimensional square supplement at a C5 point follow correctly. No substantive correction is required.

Reviewed file: `SEPARATING-THE-TWO-INVISIBLE-QUARTIC-LINES.md`.

Frozen SHA-256: `e48523c2fea6173f1f69aa4d763ecae3e4029a89986999a447717dd9ea0ed989`.

This is a mathematical audit, not a formal verification. The fixed identification J, everywhere-surjectivity of L_can, the dimensions and exact kernel of restriction to K, the second-symbol resolution, disjointness of Sigma and Delta, and the defining properties of N are accepted as pinned inputs. In particular this review does not independently reproduce the actual-map identification from PR543. No actual HM coefficient, selected point, source vector, derivative, or matrix was evaluated.

## 1. Representations and the degree-seven obstruction

Twisting the supplied resolution by seven gives

    0 → A O(-1) → P4 O(1) → I_Sigma(7) → 0.

The stated H0 and H1 vanishings imply H0(I_Sigma(7)) ≅ P4 ⊗ H0(O(1)). With the convention X=P(A) of lines, H0(O(1))=A*, and the standard SL2 self-duality identifies A* with A. Thus the decomposition used in the proof has the correct variance.

The two representation assertions can be checked independently on the five projective A5 classes. Let phi=(1+sqrt(5))/2 and psi=(1-sqrt(5))/2; label the order-five classes so that A has the following character. The class sizes are 1, 15, 20, 12, 12:

| Representation | 1 | 2 | 3 | 5a | 5b |
| --- | ---: | ---: | ---: | ---: | ---: |
| A | 3 | -1 | 0 | phi | psi |
| V | 3 | -1 | 0 | psi | phi |
| P4 | 4 | 0 | 1 | -1 | -1 |
| D | 5 | 1 | -1 | 0 | 0 |
| Sym6 W | 7 | -1 | 1 | -phi | -psi |

These verify P4⊗A = V⊕P4⊕D and Sym6 W = V⊕P4. In particular, neither contains A. Independently, the A-multiplicity in either relevant representation is zero because phi²+psi²=3: the character inner-product numerator is 36−12(phi²+psi²)=0. Swapping the two order-five labels changes none of these conclusions.

Multiplication by delta gives the asserted short exact sequence because Sigma is disjoint from the Cartier divisor Delta. Locally along Delta the ideal is O_X; away from Delta, delta is a unit. Consequently a section of I_Sigma(9) with zero restriction to Delta has a unique preimage in H0(I_Sigma(7)). The multiplication map is equivariant, so this preimage construction is equivariant as well. No unproved surjectivity on global sections is needed. It follows that the nonzero equivariant M cannot restrict identically to zero.

Under the Veronese parametrization, O_X(9)|Delta pulls back to O_P(W)(18). Strictly its sections are Sym18 W*, which is equivariantly isomorphic to Sym18 W using the invariant alternating form on W. Irreducibility of A then makes the resulting nonzero section-space map injective. The image is indeed a three-dimensional degree-eighteen series.

## 2. The gcd argument rules out every base point

The common-zero divisor B means the greatest common divisor of the three sections, with multiplicities. A nonzero section exists, so deg B≤18. Since the section subspace is G-stable, B is invariant under the projective A5 action, including its multiplicities.

A finite point stabilizer in PGL2(C) is cyclic. Thus its possible orders here are 1, 2, 3, 5, giving orbit sizes 60, 30, 20, 12. There is exactly one twelve-point orbit: A5 has six order-five subgroups, each has two fixed points, and distinct such subgroups cannot share a fixed point because its stabilizer would be cyclic. This accounts for all twelve points in that orbit.

Therefore a nonempty invariant effective divisor of degree at most eighteen has degree twelve and is that orbit with multiplicity one. The line of its defining binary forms is G-stable, hence carries a character. Since SL2(F5) is perfect, that character is trivial. Division by the invariant degree-twelve form consequently preserves equivariance and produces a nonzero map A→Sym6 W*≅Sym6 W. The representation calculation above excludes this. B is empty.

This proves base-point freeness, not merely generic nonvanishing. It covers the exceptional 12-, 20-, and 30-point orbits as well as generic points, with no assumption about which orbit might contain a base point.

## 3. Bundle twists and fiberwise nonvanishing

The coefficients of M lie in H0(I_Sigma(9)), so the relevant bundle map is

    A O_X(1) → I_Sigma(10).

Its restriction to Delta is A O_Delta(1)→O_Delta(10). The coefficient line bundle is O_Delta(9), of binary degree eighteen; the source and target plane twists pull back to degrees two and twenty. The proof's twists are consistent throughout.

At each point of Delta, the absence of a common zero says exactly that this map is a nonzero functional from a three-dimensional fiber to a one-dimensional fiber. Composing it with the assumed surjective fiber map L_can remains nonzero. This proves the claimed nonvanishing at every square. No evaluation of an individual source vector is implied.

## 4. Separation and the single-scalar supplement

Since ker r=T and T is one-dimensional, nonvanishing of e_p on every nonzero element of T implies ker(r,e_p)=0 for every p in Delta. The PR658 input states N is one-dimensional and every element of N vanishes on Delta. Hence T∩N=0, and r|N is injective. These deductions use exactly the supplied properties of N and no additional actual-fiber calculation.

At a point whose projective stabilizer is C5, the stabilizer in G is its cyclic order-ten inverse image. Choose an order-ten lift with W-eigenvalues eta and eta^(-1), eta primitive of order ten. For p=[ell²], O_X(-1)|p has weight eta², so O_X(10)|p has weight eta^(-20)=1. As Sigma is disjoint from Delta, the identification of I_Sigma(10)|p with this line is equivariant.

The D=Sym4 W weights are eta^4, eta², 1, eta^(-2), eta^(-4). Exactly one is trivial. Thus Hom_Stab(p)(D,F|p) has dimension one, supported on the intrinsic stabilizer-fixed line represented in an eigenbasis by ell²m² and transported by J. The center acts trivially on both D and the target, so the same answer is obtained using the projective C5. No choice of a normalized numerical scalar is necessary.

The combined map lands in a target of dimension 3+1=4 and is injective. Equivalently, surjectivity of r gives a lift of any first component, and the nonzero map from T to the one-dimensional second target adjusts that lift to any desired second component. The asserted isomorphism follows.

## Precision and scope

Two optional expository clarifications would make conventions fully explicit but are not mathematical defects: mention the standard self-dual identifications when writing H0(O(1))=A and H0(O_P(W)(18))=Sym18 W, and call the full stabilizer in G the C10 lift of projective C5.

The result is a structural statement about the universal equivariant space Q. It does not establish actual fourth-gate vanishing or nonvanishing, nor does it resolve prescribed-source membership, additional specialized kernels, higher Smith exponents, full repair, or algebraicity. The manuscript preserves these limitations correctly.
