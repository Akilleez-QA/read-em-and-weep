# Independent audit of the factor-reversal symbol argument

## Verdict and scope

The claimed local sign obstruction is correct for algebra comparisons and ordinary sheaf-local Morita comparisons of the stipulated differential square-zero pair charts, including comparisons over a geometric factor automorphism. For the external product, a full opposite comparison reverses both pure coefficient identifications and therefore preserves the mixed coefficient identification, relative to canonical geometric pullback. This excludes a negative mixed-coefficient shortcut of that form. It does not exclude every categorical symmetry, every derived equivalence, or every possible negative action on the obstruction group.

This initial audit independently checks the claim from the explicit chart in null-actual-pair-comparison/RESULT.md and the duality interpretation in null-mixed-duality-reversal/DUALITY-RESULT.md. The author's factor-reversal REVERSAL-RESULT.md was not yet present at the time of this initial audit; a final comparison can be added when it arrives.

## 1. Exact symbol calculation

On a smooth surface in characteristic zero, the chart is A=O⊕ω with product

    (f,η)*(g,θ)=(fg,fθ+gη+(1/2)df∧dg).

The ideal ω is central and square-zero. Its commutator is exactly

    [(f,0),(g,0)]=(0,df∧dg).

Let a filtered comparison induce φ on O and ψ on ω. Since adding a coefficient-ideal element to a lift does not change a commutator, any algebra comparison satisfies

    ψ(df∧dg)=dφ(f)∧dφ(g).

An anti-algebra comparison satisfies the negative of that identity. Exact wedges locally generate the canonical line: choose local smooth/étale coordinates x,y, whose dx∧dy is a frame. Consequently ψ is respectively plus or minus the canonical pullback of top forms. No choice of scalar trivialization of ω or orientation-reversing coordinate map evades this conclusion. A geometric determinant already occurs in canonical pullback; it is not an additional freely selectable relative sign.

An arbitrary change of additive splitting may modify the displayed bidifferential representative, but its Hochschild coboundary has zero antisymmetrization because both the reduction and the coefficient bimodule are commutative/symmetric. Thus the commutator argument survives such changes without requiring a differential gauge assumption.

## 2. Why the ordinary Morita reduction is rank one

This step requires a sheaf-local ordinary Morita equivalence, represented locally by a finite projective progenerator. It does not hold merely because an unspecified abstract triangulated equivalence exists.

At a point, A is a noncommutative local ring: an element is invertible exactly when its image in the local commutative reduction O is invertible. Its maximal ideal is the inverse image of the maximal ideal of O, and its residue division ring is the residue field k. A finite projective module over a local ring is free. If the Morita progenerator P has rank n, its endomorphism ring is a matrix algebra of size n over A (up to the usual left/right opposite convention), with semisimple residue Mat_n(k). A target pair chart B also has residue division ring k, so n=1. A local frame of P therefore turns the equivalence into an algebra comparison with the appropriate left/right convention.

On overlaps these frames need not glue to a trivial line. Their reduction is a line bundle on the graph of the stipulated base automorphism. This permits genuine line twists and changes of unary/scalar descent data. It does not change the local symbol: frame changes are inner and their action on the central coefficient ideal is trivial. In particular one must not infer that all line twists disappear from the full ordinary-HKR triple; only its local bracket is unchanged.

The same argument applies after passing to the opposite target. An opposite comparison means a covariant Morita equivalence to the opposite algebra, or the corresponding contravariant module comparison; its symbol has the negative sign. The proof does not classify arbitrary Fourier–Mukai transforms or establish that an arbitrary derived equivalence has graph-line reduction. A derived comparison whose reduction is separately known to be a graph line with a shift has a comparable local end-algebra argument, but that is an extra hypothesis.

## 3. Two factors and the mixed line

For the stipulated factorized algebra on P²×P², let K_z and K_h be the two pure coefficient lines and J=K_z K_h≅K_z⊗K_h. The pure squares vanish and the mixed product is the specified canonical multiplication isomorphism. Taking the quotient by the other pure direction recovers each pair bracket. A factor-preserving covariant selfcomparison therefore has relative signs (+,+); a comparison to the full opposite has relative signs (−,−). Multiplicativity forces the action on J to be the product of the two signs, hence + in both cases.

Adding mixed-ideal terms to images of pure elements does not change this calculation: J annihilates both pure coefficient ideals. Factor exchange also adds no negative sign to J, since these are ordinary ungraded coefficient sheaves (and, in forms, swapping two degree-two top forms has positive Koszul sign).

This conclusion assumes a comparison preserving the specified pure directions, possibly permuting them by a geometric factor map. A claim about all maps that might mix the filtrations requires a separate argument. It also presupposes the actual external-product ambient; it does not control an independently specified mixed deformation with additional data.

## 4. What remains unproved

A negative sign on one factor produces a partial opposite, not an algebra or ordinary Morita selfcomparison of that fixed factor with canonical positive bracket. The local obstruction therefore blocks using one-factor reversal as the missing symmetry in the earlier self-duality argument.

It does not prove that a partial dualization functor cannot exist in a richer categorical setting, nor that such a functor preserves the specified boundary, carrier, or mixed extension. Those constructions would require their own proof. Nor does positive action on J imply identity on H²(End₀(E)⊗J): geometric pullback and the chosen bundle comparison can act nontrivially on End₀(E) and cohomology. The audit only excludes the proposed negative coefficient-line mechanism in the stated comparison class.

Finally, satisfying the symbol condition is necessary, not sufficient. Unary maps, scalar triple units, and coherent determinant-line twists may still obstruct the full comparison. The earlier mixed-duality report correctly did not assert a full simultaneous-reversal equivalence. This audit supplies no such existence theorem and evaluates none of the thirty retained obstruction coordinates.

The review is formal and conditional on the cited inputs. 

## Final cross-check of REVERSAL-RESULT.md, including its new opposite-return construction

The completed REVERSAL-RESULT.md has now been read together with null-root-morita-inertia/root-morita-0719/RESULT.md. It passes the audit with the scope qualifications above. Its Section 6 also supplies the extra argument against linear mixing for identity-base comparisons: functions drawn from each individual factor produce bracket values spanning the corresponding pure summand modulo J, so bracket compatibility fixes the summands separately. The broad derived-categorical exclusions remain unclaimed. The introductory phrase “derived obstruction” should be read as “proved symbol obstruction,” not as an assertion about all derived equivalences.

The completed report adds a genuine positive construction beyond the initial symbol obstruction. This construction checks exactly, as follows.

1. Taking the opposite preserves overlap maps and inverts central triple units, giving (−μ,v,−b). Coefficient negation gives a presentation B with (μ,−v,b).
2. The exact line-transport formula with L=O(1), q_ij=t_ij, adds df∧β_ij to the unary correction. Thus −v becomes v.
3. Its scalar formula is b^L=b−(−v_ij)(t_jk)/t_jk−μ(t_jk,t_ij)/t_ik. Since (−v_ij)(t_jk)/t_jk=+(1/2)β_ij∧β_jk and μ(t_jk,t_ij)/t_ik=−(1/2)β_ij∧β_jk, the corrections cancel. Hence b^L=b as an actual cocycle, not merely a cohomology class. No total-Čech sign reinterpretation is needed for this cancellation, which is expressed in ordinary pointwise wedge order.
4. The genuine line-transition cocycle and the previously proved exact Morita formula supply the full triple/pentagon coherence. Consequently B^L is literally the stipulated corrected pair presentation. This constructs an opposite-to-original Morita return with coefficient action −Id.
5. The external tensor of the pair returns is valid for the actual factorized ambient, retaining its mixed terms. Untwisting by O(1,1) acts on the classical dual bundle as E*↦E*⊗O(−1,−1)=E*⊗det E≅E. The sign of this line twist is consistent with the row-module formula H_ij=q_ij⁻¹G_ij.
6. Both pure coefficient actions are negative, so the mixed action is positive. The defect transformation under contragredient duality is −†, which equals +Id on rank-two tracefree endomorphisms. Thus the constructed return upgrades the earlier hypothetical ambient comparison but still imposes no additional tracefree vanishing equation.

Accordingly the earlier paragraph stating that this audit supplies no existence theorem describes its initial symbol-only stage and is superseded by this final cross-check: the explicit corrected external-product opposite return is now verified. No arbitrary full ambient, frozen physical jet, partial-dual categorical functor, or value of any retained detector is thereby established.
