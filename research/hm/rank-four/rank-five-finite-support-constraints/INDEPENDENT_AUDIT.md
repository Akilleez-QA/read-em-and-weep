# Independent audit: finite rank-five support and the binary-line refinement

## Verdict

PASS, conditional on the explicitly imported actual-target, equivariance, repeated-input-injectivity, pointwise exclusion, and determinantal base-locus hypotheses.

The finite support bound 784, the exclusion of the 300- and 500-point orbits, uniqueness of the 375-point orbit, and the support-cardinality list

    0, 250, 375, 600, 625, 750

are valid. The stronger binary-line quotient argument also passes: the 600-point possibility is the single distinguished nonzero-cocycle orbit M, not an unspecified orbit with standard C5 stabilizer. None of these arguments proves that any surviving possibility occurs or excludes isolated rank-five points altogether.

The initial version of Section 5 had an insufficient explanation for identifying one shear lift: determinant one on V and order five do not alone select a scalar representative. The final version repairs this using determinant one on the invariant three-dimensional summand T. I checked that revision and the completed Section 7.1. No remaining mathematical gap was found.

## 1. Finiteness and dependence on earlier exclusions

The audited curve classification asserts that the reduced curve part of Z5 is empty or the canonical union of twenty-five conics. The independent audit in ../rank-five-canonical-conic-exclusion/INDEPENDENT_AUDIT.md establishes pointwise residual rank at least six on those conics under the actual-target hypotheses. Together with dim Z5<=1, these inputs make Z5 finite. Merely knowing the classification without the new pointwise conic theorem would not suffice.

Avoidance of negative lines requires ../rank-four-canonical-conic-exclusion/LINE_ADDENDUM.md, not the older canonical-line rank-five theorem, which gives only rank at least five. Avoidance of E uses ../heisenberg-eigenpoint-rank-six/PROOF.md and its image-generation hypothesis. The proposed proof imports the correct stronger results.

## 2. Proper complete intersection and local contribution

Because L10 has finite base support, its first member can avoid all positive-dimensional components of Z9. This cuts the at-most-two-dimensional Z9 to dimension at most one. A second member can simultaneously avoid all three-dimensional components of the first hypersurface and every curve component of its intersection with Z9. These are finitely many proper linear conditions over an infinite field. The resulting complete-intersection surface Y meets Z9 in only finitely many points.

Consequently a member of L14 avoids every surface component of Y, and a further member avoids every curve component of the preceding intersection. At each stage Cohen–Macaulayness and unmixedness exclude embedded associated primes. The four sections form a regular sequence with finite projective zero scheme W and length 10*10*14*14=19600. Every point of Z5 lies in W.

At a point with matrix rank at most nine, invertible-block elimination gives I10 contained in m and I14 contained in m^5. Thus the local parameter ideal has generator orders at least (1,1,5,5). Raising the two degree-ten generators to fifth powers produces a parameter ideal contained in m^5. Its colength is at least 5^4=625 by the Hilbert–Samuel leading-coefficient comparison. The regular-sequence power filtration multiplies the original colength by 25, so the original local contribution is at least 25. Summing yields 25 times the reduced support cardinality at most 19600, hence at most 784.

No transversality, tangent-cone regularity, or determinantal-scheme reducedness is assumed. This is a reduced-support estimate through an auxiliary complete intersection; it is not a claim about the length of the determinantal scheme itself.

## 3. Exhaustion and exclusions of small orbits

Outside E, the stabilizer intersects A trivially and injects into K=SL2(F5). Orbit size is 25 times an index dividing 120. Between the established lower bound 250 and 784, the only possibilities are 250, 300, 375, 500, 600, 750. There are no omitted intermediate divisors.

Every even-order projected stabilizer contains the unique involution c=-I. The cocycle identity 2t(g)=t(c)-g t(c) conjugates the stabilizer into the standard complement. Thus the positive T and negative W eigenspaces may legitimately be used for the order-six, order-ten, order-eight, and order-four cases.

For C6, the W eigenlines are on an excluded negative line. The two nonunit T eigenlines are isotropic for the invariant quadratic form, since their eigenvalues have squares different from one. The remaining T axis is stabilized by the order-twelve normalizer and belongs to the unique 250-point orbit. It therefore cannot be a genuine 500-point point.

For C10, simultaneous shear/reflection eigenlines consist of e0, the two positive pair sums, and the two negative pair differences. The first belongs to E; the negative lines are excluded. The positive pair sums are isotropic. A precise scalar-independent verification is useful: the displayed shear has T-spectrum {1,zeta,zeta^-1}; an honest lift differs by a fifth-root scalar. Invariance of a nondegenerate quadratic form forces the shifted spectrum to be invariant under inversion, and its determinant on T is one. The latter also follows because K is perfect. Of the five scalar shifts, only the unshifted spectrum satisfies these conditions. Thus e0 is the unit eigenaxis and the other two lines are isotropic. One cannot instead infer uniqueness merely from determinant one on V and order five. The desired C10 exclusion is valid.

## 4. The unique quaternion orbit and the support arithmetic

An order-eight projected stabilizer is Sylow-two Q8. On T its quotient V4 acts through the three distinct nontrivial characters; on W it has no invariant line because its commutator c acts negatively. There are exactly three projectively fixed lines. They are outside E, since eight does not divide its point-stabilizer order 100. The noncanonical orbit lower bound forces each full stabilizer to have order at most twelve; divisibility by eight then forces order exactly eight. Their orbit size is 375.

The order-24 normalizer cyclically permutes these three character lines, and all Sylow-two subgroups are conjugate. Central-involution conjugation accounts for possible translation cocycles. This proves uniqueness of O375, rather than merely existence of some orbit of that size.

The character lines are mutually orthogonal and nonisotropic. A point outside E cannot be fixed by two distinct projective involutions: every involution has the form (a,c), and the product of two distinct ones is a nonzero translation. Thus these points also avoid every translated canonical conic and negative line. This geometric statement does not assert rank five there.

Uniqueness of O250 and O375 is essential in the support arithmetic: one cannot take two distinct 250-point orbits or two distinct 375-point orbits. The bound then leaves only the empty set, O250, O375, one 600-point orbit, O250 union O375, or one 750-point orbit. The 625 case is exactly that union.

## 5. Binary-line quotient refinement

This section independently checks the strengthening now included in Section 7.1 of the final proof.

Let U be any two-dimensional vector subspace of V. Outer symmetry and the cyclic identity make the restriction f|U^3 factor through S_(2,1)U, a two-dimensional space isomorphic to U tensor det U. For a basis u,v, the universal value F(u,u,v) is a nonzero scalar multiple of u tensor (u wedge v). Varying u and an independent v represents every nonzero line of this Schur module. Repeated-input injectivity therefore makes the induced linear map S_(2,1)U -> J injective. Denote its fixed two-dimensional image by H.

For every nonzero u in U, the universal values on uv and v^2 span this Schur module. Hence b_u(Sym^2 U)=H at every point of P(U). Projecting the entire matrix b to J/H gives an ordinary linear matrix pencil bar b on that line with

    rank bar b_u = rank b_u - 2.

Its eight-minors are degree-eight sections, and their common zero support is exactly Z5 intersect P(U). This equality uses the constant inclusion H in every image, not a moving quotient or a division by a coordinate.

For U=span(e_i,e_-i), the clock and reflection act effectively as D10. The coordinate endpoints lie in E. Every other point with a nontrivial D10 stabilizer is reflection-fixed. Such a point is also fixed by the standard shear D, which acts by a scalar on U and commutes with the relevant clock-reflection involution; hence its stabilizer contains C10. The previous C10 analysis excludes it. Every remaining point has a ten-point D10 orbit.

If one of these remaining points lay in Z5, all ten points would be zeros of every eight-minor of bar b. Each minor would vanish identically, forcing the entire line into Z5, contradicting finiteness. The final proof gives an even more direct nonvanishing check: at a coordinate endpoint in E, rank b is at least ten, so the quotient rank is at least eight and some eight-minor is nonzero. Thus the intersection has at most eight distinct points even without invoking finiteness for this step. This check is valid. Equivariance excludes every translate of both pair lines. This is the valid degree-eight argument; using the original degree-ten minors directly would not be sufficient.

## 6. Identification of the surviving 600-point orbit

Sections 1, 3, and 4 of ../order-five-rank-three-classification/PROOF.md are rank-independent. Their subgroup calculation has five cocycle classes over each unipotent C5, with the torus acting transitively on the four nonzero classes by s^3. Thus all 120 nonzero-class subgroups are conjugate. Each has five simple eigenlines; its order-25 normalizer cycles them through the nontrivial Weyl commutator. None is in E. No involution can stabilize such an eigenline, because it would normalize the C5 subgroup whereas that normalizer has odd order 25. An odd stabilizer containing C5 has order five or fifteen, and order fifteen is impossible in K. The stabilizer is therefore exactly C5, proving a single orbit M of size 600.

Zero-class C5 subgroups fix e0 and the two pair lines just excluded. Consequently the only possible 600-point contribution to Z5 is M. This imports no rank-three-specific conclusion and evaluates no representative of the actual operation.

## 7. Remaining order-four case and limits

For order-four stabilizer, the generator has T-spectrum {1,-1,-1} and W-spectrum {i,-i}. The W eigenlines are excluded. Its T eigenvalue-one axis is Q8-fixed and belongs to O375. A genuine 750-point candidate must therefore be on the projective line of the negative two-dimensional eigenspace in T, away from already excluded points. This is only a location constraint; no uniqueness of a 750-point orbit is established or required.

The remaining alternatives are necessary possibilities, not realizations. Finiteness and a support bound do not prove Z5 empty. No scheme multiplicity or actual rank on O250, O375, M, or the remaining 750-point candidates is calculated.

## Evidence boundary

Only local proof files, universal group/representation arguments, and regular-local-ring reasoning were used. No actual source coefficient, source tensor, selected input, operation matrix, rank instance, jet, or residue was evaluated.
