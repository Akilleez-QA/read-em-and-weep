# All ordinary background orders, one star order

## Precise conditional conclusion

Fix the marked, deck-linearized ordinary bundle E on the fixed X and the coefficient-family base point of [ordinary miniversality](../invariant-formal-hull/PROOF.md). Assume separately:

1. P: the exact presentation and literal first differential used for the full coefficient-family theorem and its audited Kodaira–Spencer injection.
2. D: the historical assertion dim Ext¹(E,E)^G = 79 for this same deck action. This is an imported numerical premise, not a recomputed rank certificate.
3. Q: the inherited homogeneous contraction, regular carrier cover, literal determinant normalization, and complete raw first-order transgression identifications in [the arbitrary-tuple source theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/92ccceb1a023dd86bf4d17f4b86b779cc1b7c44f/research/hm/relative-models/relative-mixed-character-purity/dependencies/SOURCE-FAMILY.md), especially §§2–4,8. Its imported exact A-receipt premise remains imported. P or D alone does not authenticate Q.

Then every marked G-equivariant ordinary deformation E_A on X over a local Artinian k-algebra A is induced by the completed coefficient family. For each of the two inherited branches r=(0,1),(2,3), separately, E_A admits a regular first-star-order lift with the same fixed ordered scalar gerbe as the source family. Here “lift” means a locally free gerbe-twisted right module for the first-order star algebra, described explicitly below. It does not mean an untwisted module over that global algebra.

The lifts can be chosen compatibly with coefficient classifying maps and their ordinary identifications across Artinian extensions. The established consequence is essential surjectivity onto ordinary deformations and a compatible lift construction over a smooth miniversal atlas. It is not a proof that the forgetful functor from *all* first-star structures is formally smooth.

Deck equivariance is asserted for the ordinary deformation and its classifying isomorphism only. No equivariant star structure with a trivially acted-on star parameter is asserted.

## 1. Pullback from the actual coefficient family

Put S = k[[t₁,…,t₇₉]]. Under P and D, ordinary miniversality gives a formally smooth map from h_S to the groupoid of marked G-equivariant ordinary bundles. Thus there are a continuous local map f:S→A and a marked G-equivariant isomorphism

    h: f*Ē → E_A.

Choose once an affine projective-coordinate chart about the pinned coefficient point and normalize its common scalar. This gives an actual generating five-tuple, rather than a merely projective tuple. The distinction matters: the projective universal map globally has an extra parameter-line twist, while the normalized chart trivializes that line. By [the full coefficient-family theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/COEFFICIENT-FAMILY.md), its sections are sections of the fixed N² and all are pulled back from the fixed quotient Y. The resulting ordinary family has the required deck linearization.

Apply Q to this normalized tuple family. The arbitrary-tuple theorem §8 extends the same source recipe to it, including its regular first lifts from §4. Restrict to the completion and pull back along f. This is not an inference from tangent vectors, a translated four-dimensional subfamily, or an equality only on the special fiber.

All these pullbacks are valid for nonreduced A. On a fixed affine refinement of the central root/carrier cover, denominators with invertible central reduction stay invertible on every Artinian thickening. Derivations extend to these localizations by the quotient rule. The relative physical derivations kill A and commute with coefficient-base change. The homogeneous identities and their derivatives therefore remain identities after arbitrary Artinian pullback. No smoothness or reducedness of Spec A is needed.

## 2. Exactly which first-star object is supplied

For one fixed branch r=(a,b), define the sheaf of associative A[ε]/(ε²)-algebras

    𝒜_(r,A) = O_(X_A) ⊕ ε O_(X_A),
    F ⋆ G = FG + ε μ_r(F,G),
    μ_r(F,G) = ((V_a F)(V_b G) − (V_b F)(V_a G))/2.

The product is extended bilinearly, so terms already containing ε contribute only their ordinary product. The bidifferential operator is a Hochschild cocycle because the V's are derivations; hence the product is associative modulo ε². Matrix products use this entrywise star product with matrix summation.

On the refined cover the pulled-back source gives regular matrices g_ij and U_(r,ij) satisfying

    g_jk g_ij = g_ik,
    U_jk g_ij + g_jk U_ij + μ_r(g_jk,g_ij)
      = U_ik + b_(r,ijk) g_ik,
    b_(r,ijk) = (15/4) q_(a,ij) q_(b,jk).

The q's use the fixed legal root frames and fixed old connections. Thus b is the same ordered scalar Čech cochain over every coefficient base: it is literally pulled back from X, not just constant in cohomology. The scalar edge correction in U is generally coefficient-dependent and must not be frozen; [background-star compatibility](../background-star-cross/PROOF.md), §§3–4, makes this distinction explicit.

Set T_ij = g_ij + ε U_ij and c_ijk = 1 + ε b_ijk. Then

    T_jk ⋆ T_ij = c_ijk ⋆ T_ik.

Each T is star-invertible, since its reduction g is invertible. Each c is central in the first-order algebra: any star commutator involving its ε b term is of order ε². Associativity on quadruple overlaps and cancellation of the invertible T imply

    c_jkl c_ijl = c_ijk c_ikl,

equivalently the usual scalar Čech cocycle equation for b. This also verifies the coherence needed below directly from the actual first-lift identity.

Take free right 𝒜_(r,A)-modules of rank two on the cover, written as columns, with transition maps given by left star multiplication by T_ij. These maps are right-linear. Their triple composition is c_ijk times the direct transition. This is precisely c-twisted descent data, or a locally free right module on the scalar gerbe with this specified twist convention. Its ε=0 reduction is the ordinary bundle f*Ē.

Without a chosen trivialization of c, the T's are not ordinary descent data for a module over the global sheaf 𝒜_(r,A). If the gerbe can be trivialized, extra scalar choices can convert them to such data, but no such trivialization or vanishing of [b] is proved here. The conclusion retains the actual ordered b, not a silently modified representative.

## 3. Transport to the given ordinary deformation

The ordinary isomorphism h must be used with star gauge corrections. Choose local frames so its matrices H_i satisfy

    g'_ij H_i = H_j g_ij,

where g' are the transitions of E_A. Regard H_i as matrices with zero ε coefficient; they have regular star inverses. Define

    T'_ij = H_j ⋆ T_ij ⋆ H_i^(⋆−1).

Then T' reduces to g', and centrality of c gives exactly

    T'_jk ⋆ T'_ij = c_ijk ⋆ T'_ik.

In particular, the same scalar cochain b is retained. If T'_ij=g'_ij+ε U'_ij, the explicit and convention-independent intertwining calculation gives

    U'_ij = [H_j U_ij + μ_r(H_j,g_ij)
                        − μ_r(g'_ij,H_i)] H_i^−1.

This follows by expanding T'_ij ⋆ H_i = H_j ⋆ T_ij. Simply replacing U by H_j U H_i^−1 would omit the two necessary μ terms. More general lifts H_i+εK_i provide additional gauge freedom; they are not required for existence.

With compatible marked central frames H_i reduces to identity at the coefficient base point. Its physical derivatives then reduce to zero there. Consequently the transported object reduces to the inherited central first-star object, if that star marking is desired. Arbitrary local choices change the presentation; existence does not claim canonical transport or uniqueness. Transported frames need not preserve the literal determinant-normalized source formula, which was used to establish existence before transport.

## 4. What compatibility across extensions means

Let A'→A be an Artinian surjection, let E_A be classified by f:S→A and h, and let E_A' be an ordinary deformation equipped with an identification of its reduction with E_A. Ordinary formal versality supplies f':S→A' lifting f and a classifying isomorphism h' lifting h. The source formulas pulled back along f' reduce to those pulled back along f. Choose compatible local ordinary frames and matrices for h', and perform the star-gauge transport of §3. Its reduction is exactly the previously chosen transported family lift.

This proves the relative lifting assertion for a first-star object already presented as a transported coefficient-family lift, with that presentation retained. Iterating produces compatible chosen objects over a tower of Artinian quotients. It remains a first-star-order assertion at every stage; the background nilpotence order is unrestricted.

For a completely arbitrary first-star object over E_A, no classification or reduction to this distinguished construction has been established. For fixed ordinary transitions and fixed b, the difference between two first lifts satisfies the homogeneous End(E_A)-valued Čech 1-cocycle equation after normalization. Gauge transformations reducing to identity modulo ε change that difference by a Čech coboundary. Hence additional first-star classes, and their ability to lift over ordinary extensions, must be controlled to prove formal smoothness of the entire forgetful functor. Ordinary versality and the existence of one formula-defined lift do not supply that control. This argument neither proves nor disproves such larger formal smoothness.

Equivalently, we have a compatible lift of the coefficient atlas into the first-star twisted-object problem, whose composite with forgetting star structure is the ordinary miniversal atlas. Essential surjectivity and lifting from this atlas must not be conflated with the lifting property for every object in the source groupoid.

## 5. Audit and excluded claims

- The numerical 79 uses P plus the independent historical D; it is not extracted from the source formulas.
- The first-star admission uses Q in addition; neither ordinary unobstructedness nor the ordinary 79-dimensional tangent computation implies it alone.
- Actual coefficient-family identities, not first-background derivatives, prove all background orders. The background-star calculation is a consistency check on the resulting first derivative and its varying scalar edge term.
- Only one ε with ε²=0 is used at a time. The two branches are two separate lifts. No ε² coefficient, two-star mixed term, mixed residual vanishing, or full star formal algebraization is concluded.
- Ordinary deck equivariance does not automatically lift with trivial star-parameter action. No such claim is needed here.
- The supplied object is gerbe-twisted. No untwisted global module, gerbe trivialization, universal moduli representation, or uniqueness of classifying maps is claimed.
- Closed mixed residual statements in the arbitrary-tuple reference are not used to resolve a mixed lifting problem.
