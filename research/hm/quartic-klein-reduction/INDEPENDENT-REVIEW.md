# Independent review: quartic-generator orbit theorem

## Scope

Reviewed PROOF.md SHA256: e7114ca707190f306aa2acaecae7ad253e84dfb3e3201e1db703412ae266f4bd.

This review checks the structural derivation from the pinned actual-module inputs of PR489, PR494, PR516, PR519, PR520 and PR522. It does not independently reprove those inputs. No selected HM/source-instance matrix, rank, coefficient, or source value was evaluated. The binary calculation below is a universal two-dimensional tensor identity. This is mathematical review, not formal proof-assistant checking.

## Checks

1. **Equivariant splittings and multiplicities.** The ordinary splitting obstruction vanishes on P1, and averaging a splitting over the finite normalizer preserves its right-inverse property. Taking the multiplicity of the genuine normalizer representation V gives a genuine action of the quotient SL(2,F5), rather than an unsupported projective action. The source multiplicities are Qspin, W and T4; the upper target is U and the lower target is W with twist -1. The listed tensor rules kill the upper W and T4 blocks and the lower T4 block. Moreover an equivariant graph from W O(-1) to U O is zero, since U tensor W=R6 contains no W.

2. **Surjectivity of the upper block.** Nonzero follows from PR522: an identically zero upper block would leave rank at most two and at least fifteen quartic generators. The maximal-minor divisor has degree at most nine and is invariant, so the rank is constant. If its rank is one, its image O(-d) has 0<=d<=3, forcing U into Sym^d W, which is impossible. If its rank is two, its quotient from U O is O(d), with 0<=d<=6; the first occurrence of U forces d=6. The image twisted by three is then a globally generated rank-two degree-zero bundle, hence trivial. Its quotient map from Qspin would give a nonzero two-dimensional quotient representation of the irreducible four-dimensional Qspin, impossible. Thus the upper block is onto, with kernel O(-12). The standard line-bundle linearizations are justified because the quotient group has no nontrivial characters.

3. **Identification of the actual lower map.** Dualizing the lower multiplication map gives

   (J4/I4)* = T tensor W O(1) -> T* tensor E tensor W O(3) = T* tensor (J3/I3)*.

   It is induced by the actual multiplication T tensor T -> E tensor Sym^2 W together with the quotient maps D2 and D4. Currying that nonzero symmetric multiplication selects the U-prime channel in T* tensor E. Therefore the product-rule formula is an identification of the actual map, not merely an arbitrary nonzero map between equal representation types.

4. **Universal nonvanishing and rank of the lower W block.** For binary quadratics g,h, set v=Dh(lambda). Euler's identity gives h(lambda)=lambda(v)/2, hence

   D(gh)(lambda)=g(lambda)v+lambda(v)Dg(lambda)/2.

   At lambda=x*, the corresponding tensor for v=x is 2 y^2 tensor x - xy tensor y after the symplectic identification of the dual quadratic space. The invariant contraction gives -4y-y=-5y. For v=y it gives zero. This independently confirms a nonzero rank-one block. Binary covariance makes the calculation uniform in every nonzero lambda. Its kernel, image and cokernel are O(-4), O(-2) and O, respectively.

5. **Reduction to one section.** Since the upper block is surjective, its lower residual modulo the rank-one image is exactly a morphism O(-12)->O. Cokernels commute with taking fibers by right exactness; no unjustified kernel base-change assertion is needed at the eventual zero divisor.

6. **Structural nonvanishing of the residual section.** If the residual section were zero, the equivariant cokernel would be O. The quotient from U O plus W O(-1) to this O must vanish on U O, because U has no invariant functional. It would consequently factor through W O(-1). But the full lower map is surjective: PR516 proves T_w/I generated in degree three, giving fiberwise surjectivity onto J4/I4 and therefore a surjective bundle map. No nonzero quotient of this target can annihilate that map. This contradiction proves the residual section is nonzero. It is not a multiplicity-one inference and uses no selected evaluation.

7. **Orbit and multiplicity conclusion.** The section has degree twelve and is invariant. The unique possible nonzero invariant effective divisor of that degree is the reduced twelve-point orbit of order-five stabilizers. Hence the multiplicity cokernel is ordinarily isomorphic to O_Omega (without asserting an equivariant trivialization), the original cokernel has length sixty, and its fibers have dimension five precisely on Omega and zero elsewhere.

## Conclusion and boundaries

The proof determines the quartic-generator parameter: it is zero off the twelve-point orbit and five on that orbit. In particular neither a constant positive value nor the constant zero pattern survives. The conclusion is conditional on the pinned original-module identities, pairing, and degree-three generation. It does not determine the middle obstruction parameter b, settle the original fixed scalar-pair residual, or establish higher-order lifting or algebraicity for that separate problem.
