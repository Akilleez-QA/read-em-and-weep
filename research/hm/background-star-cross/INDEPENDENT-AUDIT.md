# Independent structural audit

## Verdict

Accepted, conditional on the explicitly inherited universal contraction, determinant normalization, genuine covering and raw-transgression premises. No blocking mathematical error or missing cross term was found.

Reviewed proof: `PROOF.md`, SHA-256 `4c3b7c2de2be7b25e164b9387a91b91bf22174ccffaa00b43b572efd9134c191`. The final revision with relative bundled dependency references was reread; its mathematics agrees with the audited version.

This audit read the proof and its listed proof-text dependencies only. It performed structural differentiation and sign/order checks; it did not authenticate source bytes, execute source/checkers, evaluate model matrices or polynomials, or evaluate points, jets, residuals or detectors.

## Checks

1. **Inherited actual first lift.** Structural closure §§5–6 state precisely the ordered scalar recipe, the commutator first lift, and equation (1), including `U_ik` and the positive `b_ijk g_ik` term. The ranks, internal signs, weights, endpoint-linear terms, coefficient `1/4`, and terminal correction `−15 q_a q_b/8` agree. The compatible-family common split construction supplies a family identity rather than merely a central-fiber equality. Determinant one and the rank-two polarized characteristic identity are genuinely needed in this inheritance and are not silently reproved here.

2. **Full derivative.** Equation (2) includes both derivatives in each ordered product, both bidifferential input derivatives, `dot U_ik`, and both derivatives of `b g_ik`. Fixed z,y coordinates and commuting horizontal/physical derivations justify omission of `dot μ`; the proof also states the additional term for variable μ. The statement concerns one background tangent times one star parameter, so no second-star-order scalar-product anomaly has been discarded at the order under discussion.

3. **Normalization and transports.** Left multiplication by `g_ik^−1` yields `T_ij u_jk−u_ik+u_ij+m=b I`. For `a=g^−1 dot g`, differentiating conjugation gives `T dot M−a T M+T M a`, hence the stated positive `[T M,a]`. Differentiating the left output inverse gives `−a_ik m`, in the displayed order. Thus `C=[T_ij u_jk,a_ij]+dot m` is the complete differentiated normalized cross term. Neither of these two normalization contributions may be dropped.

4. **Gerbe constancy.** With masks fixed and q expressed by the invariant z-root formula, every `dot q` vanishes. The ordered gerbe itself, not just its class, therefore has `dot b=0`. The warning about the moving inverse-x odd basis is warranted by the compatible-family chart formulas. Source physical labels and geometric coordinate labels are explicitly distinguished in the reviewed revision.

5. **Scalar and ancestor differentiation.** Equation (8) differentiates both endpoints of each wedge trace and both endpoints in each linear trace. The final quadratic-q derivative vanishes for the proved fixed-coordinate reason. The displayed ancestor derivative follows by differentiating `−(V F)F^−1−A_old` in a fixed reference, with its positive inverse-variation contribution. The caveat about moving frames prevents misuse of `dot A_old=0` after a parameter-dependent target frame change.

6. **Primitive and trace.** Differentiating `L=g^−1 Vg` gives `dot L=Va+[L,a]`, and the commutator product rule gives (9). Trace of every k and dot k is zero. Since scalar inclusion and trace commute with Čech transport, (5) gives precisely `C=−δ(dot S I+dot k)` and `tf(C)=−δ dot k`. Taking half the trace gives `δ dot S=−tr(dot m)/2`. Constancy of the scalar gerbe does not justify deleting the scalar edge derivative.

7. **Genuine cover and regularity.** The cited compatible-family and source-domain proofs use actual pulled-back carrier denominators and actual legal opens, with fixed roots and moving primitive arguments. After restriction to dual numbers, an affine central refinement maps into these genuine opens because the thickening has the same underlying topological space. Denominators invertible centrally remain units on this thickening. Taylor coefficients and physical derivatives of the regular localized formulas are regular on the corresponding central overlaps. The parameter derivative here is taken from the genuine family, or equivalently extracted as a Taylor coefficient; it need not be a derivation of the dual-number quotient itself. Separatedness of X makes affine intersections acyclic for End(E), so this is a genuine sheaf-cohomological boundary, not a merely rational primitive.

8. **Four directions and limitations.** The fixed-variety four-parameter family permits each substitution `x_i=z_i+t c_i`; the same root and split-complex argument applies without requiring new scalar identities. Injectivity of the KS map is used only to name four independent background directions. The proof correctly keeps ordinary background Yoneda products and two-star-parameter obstructions separate.

## General-family qualification

For varying scalar b the identity is `C−dot b I=−δ dot u`. Tracefree exactness survives automatically. Full exactness is equivalent to vanishing of the scalar class when dot b is a scalar cocycle: sufficiency follows from the proposed primitive `h I−dot u` if `dot b=δh`, and necessity follows by half-trace. Characteristic zero is inherited from the family dependencies, so division by the rank two is legitimate and scalar inclusion has the cochain retraction `tr/2`. The proof states the necessary cocycle proviso and specializes to the stronger pointwise-zero derivative in this family.

No new pole bound, production admission, higher-star-order lift, detector conclusion, or reauthentication of the inherited geometric hypotheses is supplied by this audit.
