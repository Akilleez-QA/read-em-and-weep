# Independent review

## Verdict: PASS

Reviewed the complete `PROOF.md`, including Section 4a, against the supplied reduced-channel and involution-exclusion proofs. All mathematical claims follow from the stated structural inputs. No selected actual HM/source-instance evaluation, parameter scan, numerical rank calculation, or large computation was used. This review checks the mathematics conditional on the pinned inputs; it is an independent mathematical review, not proof-assistant certification.

## Checks performed

1. **Joint dual image.** The local proof establishes equality with the direct sum of ideals, not merely separate projection surjectivity. The unit complementary column gives `(a,1)` with `a` in the maximal ideal; the reduced maximal-minor ideal supplies every `(m,0)`, permitting subtraction of `(a,0)`. Thus the intrinsic two-channel decomposition is respected.

2. **Normal form and torsion-freeness.** Two entries independent modulo the square of the maximal ideal form a regular parameter system and generate that ideal by Nakayama. All other entries can be eliminated by invertible target operations. The displayed normal form has dual kernel free of rank six and cokernel `R^5` direct sum the maximal ideal. The syzygy and cokernel maps have the stated signs up to harmless scalar choices.

3. **Dualization and canonical completion.** The skyscraper sheaves have vanishing sheaf Ext in degrees zero and one against the structure sheaf, with degree-two Ext the tangent-determinant line. Hence `J*=Q O`, and dualizing the first sequence gives precisely the displayed four-term exact sequence. Its first map is the original E under canonical bidual identifications. The resulting locally free extension of T across codimension two is canonically its double dual. No unjustified splitting or reconstruction of extension data is claimed.

4. **Equivariant characters.** The axis-line character is the dihedral reflection sign. The tangent determinant is its inverse cube, hence that same sign. Frobenius reciprocity gives six-point defect module `A+A'` and ten-point defect module `A+A'+P`. The degree-n twist changes the character to sign raised to `n+1`, exactly as Section 4a states. The two odd-degree invariant residue coordinates are independent in the claimed range because residue evaluation is surjective there.

5. **Global lifting and cohomology.** Vanishing of `H^1(O(n))` for every integer n proves the quotient and kernel identifications in (11), including necessity and sufficiency and the stated ambiguity in lifts. The resolution of F gives dimensions 84, 82, and 98 in degree zero. It also gives `H^1(T(n))=0` for n at least -2. The stated 0-regularity and its consequences hold. The character identities used to identify `H^0(F)^G` with Q are correct; exactness of invariants then gives both asserted invariant vanishings.

6. **Wedge reconstruction.** On the rank-two open set, wedge vanishing is exactly membership in the two-dimensional subbundle and determines unique regular coefficients. Hartogs extension for the coefficient bundle across finitely many points proves the sheaf kernel statement, and the same argument after twisting proves (16). It does not confuse fiberwise rank degeneration with sheaf-theoretic kernel enlargement. The negative-degree conclusion is correct.

7. **Scope.** The proof distinguishes reflexive-quotient lifting from channel membership and explicitly leaves actual-channel identification and higher/source lifting unresolved. Its conclusion does not exceed the supplied assumptions.

No corrections are required. The stronger regularity statement is explicitly verified below.

## Stronger regularity: PASS

Independently verified the stronger regularity paragraph in Section 4. From the displayed resolution of F*, `H^1(F*)=0`; each nonempty orbit has `H^0(I_i)=0`, so `H^0(J)=0`, and (2) implies `H^1(H)=0`. Serre duality, using `S*=H`, gives `H^1(S(-3))=H^1(H)*=0` and `H^2(S(-4))=H^0(H(1))*=0`. The latter follows from the stated inclusion into a direct sum of `O(-1)`. These are precisely the vanishings making S (-2)-regular, so S(-2) is 0-regular and globally generated. The resolution twisted by -2 gives `h^0(F(-2))=20`; the channel sequence gives `h^0(T(-2))=20` and `H^1(T(-2))=0`; the length-sixteen defect sequence then gives `h^0(S(-2))=36`. The paragraph is correct as written and the final artifact remains PASS.
