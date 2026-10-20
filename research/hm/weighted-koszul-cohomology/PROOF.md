# Weighted Koszul cohomology and the failure of diagonal restriction to detect the obstruction

## Scope convention

The assertions below concern coefficient geometry, finite-group actions and the stated coherent cohomology. References to unevaluated coordinates mean that this argument does not evaluate them; they are not a claim about the latest status of every other argument. The raw-source regularity, coefficient/character identification and raw-to-canonical class comparison are separate hypotheses wherever a source application is discussed. No first-order lifting theorem, higher-order obstruction vanishing, formal integrability or algebraicity follows merely from these coefficient statements.

## Result

At the admitted algebraic sheaf, character and HM-cohomology scope of the cited sources, the reduced triple-diagonal ideal gives an exact sequence

    0 → H²(Y,B0(-3)) → (U⊗H²(Z,E))_sign
      → H²(Y,B0(-4)) → 0,

of dimensions 20 → 30 → 10. Here Y=P4, Z=(P1)^4, q is the symmetric quotient, A=O(1,1,1,1)=q*O_Y(1), U is the two-dimensional Specht (2,2) weight space, and E=q*B0⊗A^(-2), B0=End0(HM), with the natural ungraded permutation linearization.

This is a Koszul realization of the retained weighted quotient. More decisively, inclusion I_D EA → EA induces an isomorphism on sign cohomology in EVERY degree, where D is the reduced union of the four triple diagonals. Consequently vanishing on these diagonals imposes no additional condition whatsoever on the ten-dimensional sign target. Every class in that target has a regular diagonal-vanishing representative. The result does not assert nonvanishing or vanishing of the actual physical source, and does not evaluate it.

## 1. The actual coefficient and its linearization

All displayed line identifications in this proof concern the S4 action after fixing the harmless one-dimensional binary determinant/volume lines. They are not assertions of canonical GL2 identifications. If those lines are retained, the Koszul left term has the factor det(U_weight), and the canonical-line and Vandermonde formulas carry their usual binary determinant factors. No GL2 action on HM or B0 is assumed. Exactness, dimensions and the vanishing criterion do not depend on these one-dimensional normalization choices.

Let rho:C^4→Z be the product of the four root double covers. In the natural deck linearization the all-four-odd summand of rho_*O is O(-2,-2,-2,-2)=A^(-2). This is stated explicitly in §4 of closure-and-characters.md: character S twists by -2 precisely in factors belonging to S.

The normalized End bundle has no surviving scalar root-line twist: End(N⊗pi*HM)=pi*End(HM). Section 2 of that source checks that root-frame signs cancel in transported normalized End cochains, split-column powers are even, and the old connection is invariant. Thus the all-four-odd tracefree coefficient after finite pushforward is precisely E=q*B0 A^(-2). Permuting the four odd scalar factors is ordinary multiplication, not a permutation of differential forms. It adds no Koszul sign. A has its natural ungraded action and is equivariantly q*O_Y(1).

There is a different sign on canonical forms: omega_Z is equivariantly A^(-2)⊗sign, since a permutation of four one-forms has its permutation sign. Hence

    E = q*B0⊗omega_Z⊗sign.

These conventions agree with the source's statement that ordinary full-deck-sign functions differ from the canonical-line convention by S4 sign. The full-deck character of (Z/2)^4 and the permutation sign of S4 are distinct and are not interchanged silently here.

For an application to the raw source, assume the transferred raw mixed class and canonical corrected class agree under the stated hypotheses of [comment 6274541018](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6274541018). [Comment 6271101716](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716) supplies the normalized full-source formula and gauge-boundary rule in its admitted domain. The geometric split coefficient maps proved in [PR387](https://github.com/Akilleez-QA/read-em-and-weep/blob/e276e0e181e62a60c3ae24759b8bfed746f2492b/research/regular-trace-transport/PROOF.md) do not themselves establish this actual-class comparison.

## 2. Restriction to D has no sign summand

The independent coefficient-geometry proof establishes that D is reduced and that the weight sections form a regular sequence with ideal I_D. Each irreducible component is one triple diagonal. A transposition among its three equal coordinates fixes that component pointwise. Its action on A, all powers of A, and q*B0 over that component is the identity: A is a pullback from Y with descent linearization, and so is q*B0.

Let s be a sign-equivariant section of EA|D over q^(-1)(V)∩D for an open V⊂Y. Restrict to any one component. A transposition fixing that component gives simultaneously s↦s from the geometric coefficient action and s↦-s from sign equivariance. Therefore its restriction is zero. Because D is reduced, a section of its locally free coefficient bundle which restricts to zero on every irreducible component is zero. This applies also across the quadruple diagonal; no generic extension across a nonreduced scheme is being assumed.

It follows as a sheaf identity that

    (q_*(EA|D))_sign = 0.

Finite pushforward and the finite-group sign projector are exact. Applying them to 0→I_D EA→EA→EA|D→0 therefore proves an isomorphism

    (q_*I_D EA)_sign ≅ (q_*EA)_sign,

and consequently the asserted isomorphism on cohomology in all degrees. This is stronger than the observation that the particular weighted remainder vanishes on D: all sign-valued cochains already have this restriction property on a quotient-adapted affine cover.

## 3. Pushforward of the equivariant Koszul sequence

The coefficient result gives

    0 → sign⊗EA^(-1) --alpha→ U⊗E --mu→ I_D EA → 0,

where mu is multiplication by the two weight generators and alpha is the Koszul syzygy. Taking finite pushforward and the sign summand gives an exact sequence on Y

    0 → B0(-3) → M → B0(-4) → 0,                 (K)
    M := (U⊗q_*E)_sign.

For the first term, (q_*EA^(-1))^S4=B0(-3), because EA^(-1)=q*B0(-3) has descent linearization and (q_*O_Z)^S4=O_Y. For the last term, Section 2 removes I_D, while finite duality and the canonical-line sign yield

    (q_*EA)_sign = B0⊗(q_*omega_Z)^S4⊗O_Y(1)
                    = B0⊗omega_Y(1) = B0(-4).

The identity (q_*omega_Z)^S4=omega_Y is global: finite duality identifies it with the invariant part of Hom(q_*O_Z,omega_Y), and normalized trace splits the invariant O_Y summand. There is no inversion of a discriminant or use of the degenerate algebra-trace pairing.

## 4. A stronger split-bundle proof of exactness

Apply the same Koszul argument with B0 omitted. It gives a coefficient sequence

    0 → O_Y(-3) → M0 → O_Y(-4) → 0,
    M0=(U⊗q_*A^(-2))_sign.

Both ends are line bundles, so M0 is a rank-two bundle. This extension splits because Ext¹(O(-4),O(-3))=H¹(O(1))=0. Tensoring this split sequence by B0 gives (K). Therefore every connecting cohomology homomorphism is zero, and the stated H² short exact sequence follows without any HM Ext¹ vanishing or dimension-forced injection. The splitting used to prove exactness need not be chosen canonically. This strengthens the independent long-exact-sequence verification below.

The same coefficient middle bundle is G*⊗omega_Y, up to the fixed one-dimensional weight normalization, with G the tracefree block-even paired function bundle. Indeed Ind_H^S4 1=1⊕U identifies G with the U multiplicity bundle of q_*O_Z; finite duality and E's canonical-line sign give its dual times omega_Y. This relates the Koszul realization to the earlier retained filtration. The point of the present result is its actual Koszul maps and the complete invisibility of diagonal restriction, not a new numerical decomposition.

### Optional independent Ext-based check and dimensions

The admitted all-four-root Ext¹ vanishing is H¹(Z,E)=0 for the tracefree summand. Its invariant summand is H¹(Y,B0(-2)), so the latter vanishes. The perfect trace pairing identifies B0*=B0. Serre duality on P4 therefore gives

    H³(Y,B0(-3)) = H¹(Y,B0(-2))* = 0.

Thus the H² map from M to B0(-4) in (K) is surjective.

To identify its middle dimension without assuming an S4 action on the fixed paired ambient, let H be the order-eight stabilizer of partition 12|34 and chi=sign|H. For the actual geometric S4-module V=H²(Z,E), the paired block-even source space is its H-character slice and has admitted dimension 32. Its full S4-sign summand has dimension 2. Frobenius reciprocity and

    Ind_H^S4 chi = sign ⊕ U

show that the multiplicity of U in V is 32-2=30. Since U*=U and U⊗sign≅U,

    dim (U⊗V)_sign = 30.

This is the multiplicity space, not the whole 60-dimensional U-isotypic component. The domain and target H² dimensions in (K) are respectively 20 and 10 by the admitted HM twist dimensions. Exactness and surjectivity make the image of the first map 30-10=20 dimensional. Its domain also has dimension 20, hence it is injective. This proves the displayed short exact sequence without requiring an unproved H¹(B0(-4)) vanishing.

The unweighted sign space is H²(B0(-5)), dimension 2; its known primitive is separate. A fixed nonzero pairing weight identifies the retained H-character slice, after removing its full-sign component, with this multiplicity-space presentation up to the already specified projector normalization. The map mu is actual multiplication followed by sign projection. Its kernel is the Koszul twenty-space, rather than a vanishing forced by diagonal support.

## 5. Regular cochain criterion

Choose an affine cover of Y and pull it back under finite q. All opens and intersections are affine and group-stable, and all coefficient sequences above are exact on their sections. Let t be a closed sign two-cochain in I_D EA representing the weighted remainder. A global algebraic splitting of (K), proved in Section 4, directly supplies a regular closed lift r in its middle term: apply the splitting to t degree by degree. For the actual closed weighted source, the transported projected source already provides such a closed multiplication lift.

The exact sequence says precisely

    [t]=0 iff [r] belongs to alpha(H²(Y,B0(-3))).

Concretely, in that case r=alpha(a)+delta b for a closed first-term two-cochain a and a middle-term one-cochain b. Then t=delta(mu b), giving a regular primitive. Conversely, if t=delta h, lift h on affine intersections to a middle-term one-cochain b. The difference r-delta b lies uniquely in the image of alpha; its preimage is closed because alpha is injective. This proves the criterion without assuming the two generator coefficients of an arbitrary factorization are individually closed.

The source-to-canonical comparison boundary from comment 6274541018 must still be included when transferring such a primitive to the canonical source. No primitive or kernel membership for that particular source is supplied here.

## 6. Published alternant and ideal-power theorem

The complete argument formerly occupying this section is already committed in [WEIGHT-GEOMETRY-INPUTS.md, “Regular alternant division and cubic ideal order”](https://github.com/Akilleez-QA/read-em-and-weep/blob/aab61d34a84c9b8b5a908606a7beb7212d45fe7c/research/conductor-normalization/ideal-power-contractions/WEIGHT-GEOMETRY-INPUTS.md). It proves, without discriminant inversion, that sign cochains in EA are divisible by the six-bracket Vandermonde v. It follows that they lie in J⁶EA at the small diagonal and in I_D³EA. For k=1,2,3 the sign pushforward of I_D^kEA equals that of EA, hence all its cohomology groups agree. The exponent three is sharp for universal local coefficient membership, not a statement about the global H² map at k=4 or the actual source's order.

That complete published proof is a dependency, not a new result here. Its numerical exponent is unrelated to deformation order and does not furnish an I_D⁷E or I_D¹²E representative of an unweighted actual class.

## 7. Consequence and scope

The existing coefficient restriction theorem excludes an automatic-vanishing route: triple-diagonal ideal membership cannot shrink the weighted sign target at all. The additional presentation here supplies the full Koszul maps, the split coefficient extension, and the regular kernel/primitive criterion; it does not claim a new diagonal-restriction theorem. The full ten-dimensional obstruction is the quotient of the thirty-dimensional weight-multiplicity space by its twenty-dimensional Koszul syzygy image. The known weight factorization locates a representative in a coefficient ideal that is already cohomologically invisible to the sign target.

This does not exclude a source-specific cancellation, a corrected weighted transgression, or an independently constructed regular primitive. No actual retained coordinate is evaluated by this argument. The proof uses sheaf geometry, finite-group representation theory and the explicitly admitted twist dimensions. The split coefficient proof does not need the optional Ext¹-vanishing check.

## Primary provenance

- https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276688181 (weighted remainder)
- https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716 (complete normalized source)
- https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6274541018 (class transfer and sign/constant identification)
- https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260407782 (finite quotient, line characters, 32=2+10+20 dimensions)
- https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md (§§2 and 4, actual root characters and admitted Ext¹ inputs)

The source-character file is identified by its public commit. This proof does not elevate imported source hypotheses to independently verified conclusions. See DEPENDENCIES.md for the coefficient transport and the sharper existing conditional collision criterion.
