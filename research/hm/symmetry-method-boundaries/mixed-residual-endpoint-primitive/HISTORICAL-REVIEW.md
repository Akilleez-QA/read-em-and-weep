Historical mathematical review of the source edition. Its displayed SHA-256 binds the original proof, not the normalized publication bytes. The mathematical closure, endpoint and Serre calculations are retained. See DEPENDENCIES.json for current immutable public source editions.

# Independent review: mixed obstruction and background KS classes

## Decision

Accepted, conditional on exactly the inherited universal identities, source-denotation, normalization and covering premises stated in PROOF.md. No additional mathematical gap was found in the parameterwise closure, regular fixed-cover construction, corrected cup-commutator primitive, or Serre-pairing consequence.

Reviewed PROOF.md SHA-256:

    587b02bcd991a5549f53356465513e84b4ba6317a8d6b7f9c1422275929015a6

## Checks performed

1. **Actual family closure.** I read COMPATIBLE-FAMILY §§1–4 and 7, FIRST-LIFT-STRUCTURAL §§6–8, the composite-edge erratum review, and the translated source-domain proof. The compatible family pulls back the same homogeneous primitive identities at the moving coefficient map while keeping the root data and physical derivations fixed in z,y. Its common split arrows and raw transgression therefore supply the actual first lifts over the parameter. The displayed first-lift equation correctly retains U_r,ik. The scalar-elimination identity and noncentral-gerbe anomaly of FIRST-LIFT-STRUCTURAL §7 apply algebraically to these parameterwise data. Each anomaly summand differentiates a scalar gerbe in its complementary physical pair; the fixed-root factor support kills these derivatives throughout the family. Thus closure over the parameter follows, rather than merely closure of the central fiber. Both raw scalars, both Fk corrections, the E terms and the composite-edge contributions remain present.

2. **Four directions and regularity.** Repeating the factorwise construction, or substituting x_d=z_d+t c_d, preserves the generating binary factors, matching line bundles, universal pullback identities and commuting physical derivations. Local regularity on the actual carrier/legal opens follows from the regular local ingredients and derivatives. This extension does not require, and the proof does not assert, a new four-parameter numerical pole certificate. The source edition used the background-family and diagonal arguments for rank four. The normalized edition replaces those already superseded direction-count proofs with the injective translation subfamily of PR179. The endpoint identity does not require this rank.

3. **Fixed cover over dual numbers.** For each affine refinement open U contained in a central owner open, U times Spec k[t]/(t^2) lies in that owner's restricted family open: the nilpotent thickening has the same underlying topology. An element invertible modulo t is invertible over the thickening. Thus the actual family frames, transitions and residual are regular on this fixed cover. Their t coefficients are regular central local coefficients. No product neighborhood over a reduced parameter interval is asserted. Since X is separated, finite affine intersections are affine, so this cover computes cohomology of End(E); local freeness identifies it with Ext. A finite refinement is available because X is projective and hence quasi-compact.

4. **Independent sign and transport derivation.** Set X_ijkl=T_ij R_jkl. Differentiating transport gives d(T_ij M)/dt=T_ij dot M+[T_ij M,a_ij], hence delta(dot R)=[a_ij,X_ijkl]. For h_ijk=R_ijk a_ik, the identities delta R=0 and a_il=a_ij+T_ij a_jl=a_ik+T_ik a_kl give

       (delta h)_ijkl=R_ijk T_ik a_kl-X_ijkl a_ij.

   Therefore delta(dot R-h)=a cup R-R cup a, with the stated transported Alexander–Whitney product and matrix order. Degrees one and two give exactly the graded commutator shown. The primitive is allowed to have scalar part. A regular cocycle extension R(t) is essential input; no connection on cohomology or extension of arbitrary Ext^2 classes is assumed.

5. **Row versus column conventions.** The explicit calculation is in the stated row-End algebra. A transpose reverses matrix composition, so comparison with a chosen column/Yoneda convention must carry the opposite multiplication and any associated degree or KS sign consistently. These changes preserve the vanishing commutator assertion. The review does not identify the unmodified row cochain formula with a column formula by entrywise transposition alone.

6. **Serre consequence.** Here C means the smooth projective elliptic curve, not the affine line, so X=C^4 is smooth proper of dimension four with trivial canonical bundle. A chosen nonzero volume form gives the stated perfect Ext^2 pairing. Graded cyclicity yields tr(aRb)=-tr(Rba), because moving a of degree one past Rb of degree three contributes a minus sign. Thus tr((aR-Ra)b)=-tr(R(ba+ab)), proving the stated annihilator inclusion. The same inclusion is invariant under consistent opposite-product and uniform KS-sign conventions. No dimension, nontriviality, or identification with a concrete retained test follows without further input.

## Scope

This review is static proof reading and abstract Čech/Ext algebra. It does not re-prove the inherited universal primitive identities or authenticate new source bytes. No actual source, matrix, polynomial instance, point, jet, residual, or detector was evaluated.
