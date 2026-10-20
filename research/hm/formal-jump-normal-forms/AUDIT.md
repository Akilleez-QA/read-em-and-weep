# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-formal-jump-rings-PUBLICATION-CHECK.md](../hm-formal-jump-rings-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit: full formal jump-hull normal forms

## Verdict and audited version

**Pass, with the explicitly imported audited HM inputs. No mathematical correction is required.** The cyclic minimal-model input applies without stability. The passage from the full endomorphism algebra to an ordinary deformation hull is valid. The orbit-straightening and coefficient-absorption arguments determine the entire completed local rings under the stated rank hypotheses, rather than only their quadratic initial ideals. The nonreducedness, reduction, and square-zero module descriptions follow.

Audited [PROOF.md](PROOF.md), SHA-256:

`dff5923dffd3f5657c3be3cd3979ed5ac456aed00d0765243ce379bf181c70a3`.

The following current dependency hashes were independently checked against their recorded audits:

- Generic restriction deformation proof: `261c57bde9ce8bad8b04e511a08dc3eae40d4746c34592e4195979f4d64ef21f`.
- Its embedded-orbit complement JUMP-STRATA.md: `dd698b95c1cdec3d1b01824785ce06beaac93c90667a2a03f34c852a3003cdca`.
- Mixed obstruction-pairing proof: `cf9fd13f7d68485652a490d011b05684e6715144e03f34ef3f6ce9c54a46e4c3`.
- Heisenberg vertex-obstruction proof: `6a2abcbae2506e47d5b28808449a9c3fb2a55de854ff8252e734e83b7b7d3d7d`.

I read these local arguments and the relevant audits, and separately checked the primary cyclic-model theorem. This audit does not repeat the original HM cohomology computations, the scalar nonvanishing theorem, or the genericity proofs. It checks that their stated conclusions are sufficient and used correctly.

## 1. Primary theorem hypotheses

The full text of [van Garderen, arXiv:2306.00771v2](https://arxiv.org/html/2306.00771v2) was checked, particularly Theorems 5.1, 5.2, 5.10, Corollary 4.24, and Remark 5.12. Theorem 5.10 applies to a perfect complex on a smooth projective variety with a volume germ along its support; it does not require stability or polystability. Theorem 5.2 and Remark 5.12 identify the projective Calabi–Yau pairing with Serre duality. Corollary 4.24 requires the unital minimal-model setup and H⁰ equal to the base algebra. Here that algebra is C, and simplicity supplies H⁰(End E)=C. The vector bundle E is perfect; adjunction gives a global nowhere-vanishing volume form on the smooth quintic. Thus all relevant hypotheses hold. References to polystable moduli elsewhere in the paper impose no extra hypothesis on the theorem used here.

Only the formal consequence is needed. There is no reliance on a stable-sheaf coarse moduli space, a global quotient presentation, or convergence of the subsequently chosen classifying map.

## 2. Why the full cyclic Maurer–Cartan ring is a hull

The Dolbeault endomorphism DGA has the correct bundle-deformation equation: perturbing the holomorphic structure by an endomorphism-valued degree-one form gives integrability precisely when its differential plus its square is zero. Change of trivialization is the associated gauge equivalence. Its commutator DGLA therefore controls the ordinary bundle deformation problem. On a projective complex variety, the corresponding Artinian holomorphic and algebraic bundle deformations agree by GAGA; passing to this Dolbeault model does not change the formal problem.

Antisymmetrizing an A∞ minimal model gives the appropriate L∞ minimal model. On repeated degree-one inputs its Maurer–Cartan expression is the displayed sum of higher products, with the convention chosen in the proof. Every term lies in Ext², since m_n has degree 2−n. All terms have order at least two because the model is minimal. Hence the solution functor is represented by the completed symmetric algebra on Ext¹ dual, modulo the components of this expression.

The distinction between this solution functor and its gauge quotient is handled correctly. Given a small extension and a deformation class lifting the class of a prescribed solution, first choose a Maurer–Cartan representative of the lifted class. Its reduction and the prescribed solution differ by gauge equivalence. Gauge parameters lift along the coefficient-algebra surjection. Applying lifted parameters, or lifted finite compositions of the corresponding flows, changes the representative so that its reduction is the prescribed solution. All flows are finite to each Artinian order. This proves formal smoothness of the solution functor onto the deformation functor. Over the dual numbers the gauge action is zero: the linear differential vanishes, and every remaining action term has at least two factors in the maximal ideal. The tangent map is therefore an isomorphism. These are exactly the hull conditions.

In particular, scalar automorphisms do not invalidate this argument. It proves the required hull statement without claiming that the solution functor universally represents the unrigidified stack or that all stabilizers vanish. General background is [Manetti, Deformation theory via differential graded Lie algebras](https://arxiv.org/abs/math/0507284); the lifting argument above checks the specific use here.

Cyclicity makes each of the n+1 derivatives of the degree-(n+1) potential term equal after the stated sign convention. Thus df is the Serre-dual image of the full Maurer–Cartan map. Since the pairing between Ext² and Ext¹ is perfect, this is equality of defining ideals, not merely equality of their zero sets. The cubic term is one third of the paired Yoneda square, equivalently one sixth of the paired symmetric bracket. It therefore agrees with the imported primary cubic. A common nonzero scalar normalization has no effect on the ideal or the rank hypotheses.

## 3. Full End and fixed determinant

The associative cyclic construction is correctly performed on End E. End₀E is closed under the graded commutator but not generally under associative composition, so applying the quoted associative theorem directly to it would not be justified. The proof expressly avoids that error.

In characteristic zero the scalar and trace-free summands split. The scalar H¹ and H² groups vanish on a smooth quintic, so the full tangent and obstruction spaces identify with the trace-free ones. Scalar and trace-free endomorphisms are orthogonal under trace. The trace pairing restricted to the trace-free summand is nondegenerate, which checks compatibility with the imported Serre pairing and primary cubic.

The determinant comparison also has the correct scope. Scalar H¹/H² vanishings leave no determinant deformation parameter or obstruction. A unit changing a determinant identification and reducing to one has a square root over an Artinian C-algebra, so it can be corrected by a scalar bundle automorphism. Thus the ordinary and fixed-determinant parameter functors have the same hull here. This does not identify their inertia groups or assert equality of the corresponding unrigidified moduli stacks.

## 4. The orbit is a genuine embedded critical subgerm

The imported orbit argument gives an actual formal family with injective 24-dimensional tangent map. The hull lifting property supplies compatible classifying maps over all powers of its parameter maximal ideal; their inverse limit gives the displayed homomorphism from the hull to a 24-variable power-series ring. This is stronger than the existence of 24 independent tangent vectors alone.

Surjectivity of the cotangent map allows 24 ambient coordinates whose images are formal coordinates on the target. After choosing those target coordinates, subtracting the image of each remaining coordinate makes that coordinate vanish. The substitution has invertible linear part and fixes the closed point. Its kernel is precisely the normal coordinate ideal (z). Since the map factors through the critical hull, the complete gradient ideal lies in (z).

Under each such formal coordinate change, the chain rule multiplies the vector of derivatives by an invertible Jacobian matrix. Therefore the defining ideal remains exactly the gradient ideal of the transformed potential. One does not lose the critical presentation by straightening the orbit.

The expansion of the potential into z-degree zero, one, and at least two is unique. Vanishing of the normal derivatives on z=0 kills all z-linear coefficients. Vanishing of its tangential derivatives makes the z-degree-zero term constant, because the coefficient field has characteristic zero. Removing that constant gives f in (z)². Since the original potential starts in total degree three and the substitution is local, f still lies in m³.

The cubic terms involving one orbit argument and two normal arguments are intrinsic to the tangent subspace A and quotient H/A: the terms with two orbit arguments vanish. Altering a complement can therefore change the pure normal cubic but does not change the coefficient map L_p after the corresponding tangent identifications. Thus the needed rank hypothesis survives the straightening.

## 5. Coefficient absorption removes every higher term

The lemma in Section 4 is valid for formal series. Every monomial of normal degree at least two is divisible by a quadratic normal monomial. Assigning each monomial to one such divisor groups the series into finitely many formal coefficient series. This assignment is well-defined in the maximal-ideal topology and involves no convergence assertion. Total degree at least three ensures that all coefficient series have zero constant term.

Although the representation is not unique when there is more than one normal variable, its orbit-linear coefficients are unique: they are exactly the coefficients of the distinct monomials t_i z_j z_k in the cubic term. Surjectivity of L_p therefore makes the selected coefficient functions independent in the orbit directions, regardless of the assignment used for higher normal monomials.

After choosing suitable linear orbit coordinates, replacing the first r(r+1)/2 orbit coordinates by those coefficient functions has invertible linear matrix. Its other orbit-coordinate block is the identity, and all normal coordinates remain unchanged. Linear normal terms in the new orbit coordinates merely form an off-diagonal block and do not affect invertibility. The formal inverse-function theorem applies. In the resulting coordinates the original entire series equals the universal normal quadratic form with the new orbit coordinates as coefficients.

This proves exact right-equivalence, with no omitted higher-order remainder. It preserves the orbit ideal and induces an invertible reparametrization on the orbit itself. By the chain rule it transports the entire gradient ideal. The proof correctly requires surjectivity; the weaker condition that a family of quadratics has no common projective zero cannot substitute for the independence of all coefficient functions.

For one normal coordinate the resulting potential is t₁z²/2, whose full gradient ideal is (z²,t₁z). For two normal coordinates the potential is (t₁z₁²+2t₂z₁z₂+t₃z₂²)/2. Its three orbit derivatives generate (z₁,z₂)², and its two normal derivatives are exactly the two displayed mixed relations. All remaining derivatives vanish. This independently verifies both exact rings.

## 6. Reduction and nilpotent modules

For both displayed ideals, containment of (z)² and containment in (z) imply that the radical is exactly (z), since the quotient by (z) is a power-series domain. Thus (z) is the unique minimal prime and gives the whole nilradical in the quotient; its square is zero. The reduction is the embedded smooth orbit germ, not merely a subscheme of an otherwise undetermined reduction.

The normal coordinate classes are nonzero: the ideals contain no linear terms, so these classes remain independent in the cotangent space. Hence both rings genuinely are nonreduced. Their reductions have dimension 24, while their embedding dimensions are 25 and 26.

Every element has a unique representative as a power series in the orbit coordinates plus a linear combination of the normal coordinates modulo the stated linear relations, because all normal quadratic terms vanish. The rank-one nilradical is consequently B/(t₁). At the vertex it is the cokernel of the stated symmetric two-by-two matrix over B. Multiplication within either nilradical is zero, giving the asserted square-zero B-algebra structures.

The module support claims are exact. For a square presentation matrix, its zeroth Fitting ideal is generated by its determinant, and the support of a finitely presented module is the vanishing set of that ideal. Here this is t₁t₃−t₂². Equivalently, away from the determinant the presentation matrix is invertible; at a local prime containing the determinant a surjective square matrix would have invertible determinant by Nakayama, a contradiction. The rank-one module has support t₁=0 directly. These are symbolic consequences of the universal normal forms and make no assertion about a separately selected physical or HM source matrix.

## 7. Scope of the conclusion and of this audit

The imported nonempty open dense rank loci make these exact descriptions generic on the respective smooth-quintic jump strata. The proof does not extend them to every rank-one point or every vertex, and does not use the weaker common-zero criterion to overstate the vertex conclusion.

The formal-only limitation is justified. Even though the initial cyclic potential may be analytic, the classifying map and orbit-straightening were constructed in formal power series. No convergence or algebraicity of those changes has been established. Removing the higher terms of this commutative potential also does not imply formality of the full controlling A∞ or dg Lie algebra, nor vanishing of ordered or constrained obstruction operations.

This audit used local proof and audit reads, primary-source browsing, file hashes, and abstract formal and module algebra. Only this local audit file was written. No selected quintic, HM/source/cofactor matrix, polynomial or numerical rank instance, external write, selected-instance computation, or large computation was used.
