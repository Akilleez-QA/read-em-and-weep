# Weighted alternation: the (2,2) selection theorem

## Scope convention

The assertions below concern coefficient geometry, finite-group actions and the stated coherent cohomology. References to unevaluated coordinates mean that this argument does not evaluate them; they are not a claim about the latest status of every other argument. The raw-source regularity, coefficient/character identification and raw-to-canonical class comparison are separate hypotheses wherever a source application is discussed. No first-order lifting theorem, higher-order obstruction vanishing, formal integrability or algebraicity follows merely from these coefficient statements.

## Result and boundary

Over C, the pullback of the binary-quadratic discriminant polarization to the ordered-root space has S4 orbit of type Specht (2,2). Consequently the weighted sign projection receives only the (2,2)-isotypic component of an actual upstairs geometric End cohomology class. This yields an exact regular cochain target and a commutator formula. It proves no new obstruction vanishing and evaluates no source, detector, or pairing.

There is an important limitation: the block-even paired sector already has only sign and (2,2) constituents under the genuine upstairs S4 action. After the certified constant/sign vanishing, its retained image is entirely (2,2). Thus this selection theorem does not discard a further portion of the retained thirty conditions. The ten-dimensional weighted trace is a contraction of that isotypic sector, not the selection of a different S4 irreducible type.

## 1. Geometry and conventions

Let Z=(P(V))^4, dim V=2, A=O_Z(1,1,1,1), and q:Z→Y=P(Sym^4 V) the multiplication quotient. Give A its natural ungraded permutation linearization. It is equivariantly q*O_Y(1), since multiplication of the four linear factors is commutative, with no permutation sign. Let p:Z→X=P(Sym^2 V)×P(Sym^2 V) pair factors 12 and 34. Then p*O_X(1,1)=A.

The same weight pulls back to the actual root cover T=C^4 used for the raw End class. Everything below works on T with this pulled-back line, or directly on Z for any genuinely linearized coefficient sheaf. The pullback on weight sections is injective because the root cover is surjective.

Use the actual geometric action on the upstairs End bundle, not an asserted S4 action on a fixed paired deformation ambient. For the imported carrier F=N⊗π*E, End(F)=End(π*E) canonically: scalar root-line factors cancel. Since π is invariant under permutations, this gives the geometric End action used by the source theorem. Tensoring by A retains that genuine action. The underlying bundle E need not have an SL2 action.

One may compute regular cochains on inverse images of an affine cover of the finite quotient Y. These opens and their finite intersections are affine and S4-stable. Geometric pullback and its bundle linearizations then define actual chain actions commuting with the Čech differential δ. Alternatively use an equivariant refinement of any regular source cover. A matrix formula in frames must include the induced frame transports; it is not merely a permutation of derivative labels.

## 2. Explicit polarization and its orbit

For q=ax²+2bxy+cy² and q'=a'x²+2b'xy+c'y², fix σ(q,q')=bb'−(ac'+ca')/2. This fixes one nonzero scale; all conclusions survive rescaling. On the dense affine root chart q12=(x−x1y)(x−x2y), q34=(x−x3y)(x−x4y), its pullback is

  σ12|34 = (x1+x2)(x3+x4)/4 − (x1x2+x3x4)/2.

Define σ13|24 and σ14|23 by relabeling. Direct expansion gives the global section relation

  σ12|34 + σ13|24 + σ14|23 = 0.

This is a homogeneous polynomial identity after restoring the root coordinates; agreement on the dense affine chart also proves equality of global sections. The three sections are not proportional: their coefficients of x1x2, x1x3, x1x4 distinguish them. Thus their span U has dimension two and the displayed relation is its only linear relation.

S4 permutes these three sections through its action on unordered pair partitions. The kernel is the Klein four group. Therefore U is the quotient of the three-dimensional permutation representation on pair partitions by its invariant line. Equivalently it is the zero-sum standard representation of S3 inflated to S4. It is irreducible: a hypothetical invariant line would be stable under the two transpositions of S3, whose eigenlines in the zero-sum plane do not coincide. Its S4 character on cycle types 1, (12), (12)(34), (123), (1234) is

  χU = (2, 0, 2, −1, 0).

This identifies U with Specht (2,2). In particular U*=U and U⊗sign≅U. The latter follows immediately from this character, whose nonzero values occur only on even conjugacy classes.

The determinant-character line of the polarization under GL(V) does not alter this permutation representation. The commuting GL(V) and S4 actions must not be conflated. In particular SL2 invariance of σ does not mean S4 invariance.

## 3. Exact selection theorem

Let K be the regular cochain complex of the actual upstairs geometric End sheaf (or any genuinely S4-linearized sheaf), and K_A its tensor by A. Multiplication is an equivariant chain map

  μ: U⊗K → K_A,   u⊗R ↦ uR,

with trivial differential on U. For e_sign=(1/24)Σg sign(g)g and the central (2,2) projector e22, define

  Tσ(R)=e_sign(σR).

Then the following is an exact cochain identity, not just equality modulo boundaries:

  Tσ(R)=Tσ(e22R).

Proof: the composed equivariant map U⊗K→(K_A)_sign kills U⊗K_λ unless sign occurs in U⊗λ. By tensor-Hom adjunction this occurrence is equivalent to λ≅U*⊗sign≅U. Complete reducibility for the finite group in characteristic zero proves the assertion degree by degree. Cochain spaces need not be finite-dimensional: the finite group algebra is semisimple, so the same central-idempotent decomposition and argument apply to all modules.

Explicitly, with sums over the three double transpositions and eight 3-cycles,

  e22 = (1/12)(2 id + 2Σ_double-transpositions g − Σ_3-cycles g).

The projector uses the actual geometric action. It is regular and commutes with δ. Thus for a closed R the canonical candidate is the closed projected source e22R, followed by weighted alternation. No evaluation is involved in writing this formula.

Equivalently the bilinear operation factors canonically through

  U⊗H²(K)_22 → H²(K_A)_sign.

For fixed σ this is a linear map on the (2,2)-isotypic source. It need not be injective or zero. Its actual values, kernel on the specified source, and any primitive remain uncomputed.

## 4. The exact regular commutator

The action respects multiplication: g(σR)=(gσ)(gR). Therefore

  e_sign(σR) − σ e_sign(R)
    = (1/24)Σg sign(g)(gσ−σ)gR
    =: Kσ(R).

Every summand is a regular A-valued cochain. No division by σ, a branch equation, or a discriminant is used; 24 is invertible over C. The formula is independent of local trivializations when interpreted as multiplication of sections of the linearized line A.

If δR=0 and the established unweighted identity is e_sign R=δP, then

  e_sign(σR)=δ(σP)+Kσ(R),
  δKσ(R)=0.

Hence the weighted class is exactly [Kσ(R)]. A regular weighted primitive exists if and only if Kσ(R) has a regular primitive; the formula does not furnish that primitive. Multiplication by a global section commutes with the Čech differential, although it need not commute with other differential operators in a source expression.

One can normalize P to e_signP without changing δP. Then its (2,2) projection is zero. Removing the known sign boundary from R leaves its (2,2) projection unchanged. Thus the old primitive has no direct control over the canonical surviving source e22R. Also e_sign(σ e_signR)=0 identically by the selection theorem, which makes especially clear that weighting an already sign-projected source cannot recover the desired weighted sign projection.

## 5. Canonical forms, signs, and ramification

The preceding theorem uses the natural ungraded action on A and the actual action on End. It does not put a sign into A by analogy with a top form. On a product of four curves, the canonical top form acquires sign(g) under permutation of the four one-form factors. Thus the natural action on ω_Z differs by sign from the ungraded external tensor-product linearization of its four canonical-line factors. On C^4 the same sign appears in the ordered volume Ω1∧Ω2∧Ω3∧Ω4. Converting End-valued functions to top forms by this volume exchanges sign and invariant sectors. One must perform that conversion on both source and target, including the action, rather than identify the plain line-bundle type with its canonical linearization.

An overall consistent sign twist of the cochain action changes which projector represents the geometric trace, but the selected source type remains (2,2), since it is self-conjugate. The commutator formula with e_sign refers specifically to the geometric End convention of the cited alternating theorem and transfer comment.

All section identities and multiplication/projector maps are global regular maps. Their validity includes coincident roots and ramification. The action is on the whole cover and sheaves, not a claim that S4 acts on an individual moving-point stalk. No algebra-trace pairing is inverted. The finite-duality trace, not an étale-only averaging formula, justifies descent across the branch locus.

## 6. Relation to the ten-condition target

For the specified finite-flat quotient tower, the regular normalized trace theorem [PR387](https://github.com/Akilleez-QA/read-em-and-weep/blob/e276e0e181e62a60c3ae24759b8bfed746f2492b/research/regular-trace-transport/PROOF.md) establishes the coefficient-level identification: on the paired sector, the upstairs full sign projector corresponds to the finite-duality constant projector. Identifying an actual raw source with this recipient remains the separate comparison hypothesis of [comment 6274541018](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6274541018). Tensoring this identification by O_Y(1) preserves it because A=q*O_Y(1) with its natural descent linearization. Multiplication by σ is compatible with the actual upstairs coefficient inclusion. Consequently the weighted sign class is the injective upstairs image of the constant coefficient inclusion applied to

  C10(σ)=Tr_m^ω(σ C).

The constant inclusion on the finite-duality coefficient bundle is

  i_const(η): f ↦ η Tr(f)/6.

Therefore the precise comparison is Tσ(j(C))=j_1(i_const(C10(σ))) with the understood twisted coefficient inclusion j_1. In particular its vanishing is equivalent to C10(σ)=0. This does not insert a factor 1/6 into C10 itself: the divisor six belongs only to i_const and to the constant projector. The weighted trace remains λ↦λ(σ).

Equality of the imported raw class and j(C) suffices: multiplication and projection take any regular boundary in that comparison to a boundary. No S4 action on the fixed paired ambient is needed. The full normalized mixed source must still be used. The class comparison and source regularity are imported, not independently revalidated here.

## 7. What the pair character already forces

Let H=<(12),(34),(13)(24)> be the order-eight stabilizer of partition 12|34. The canonical block-even paired End class has H character χ=sign|H: each inner pair swap acts by −1, while exchanging the two two-dimensional blocks acts by +1. This is exactly the sign conversion between paired canonical forms and the actual upstairs End convention described above; it uses the source's admitted character and transfer identifications.

For any S4-module M and v∈M with hv=χ(h)v, there is a surjective map from Ind_H^S4 χ to the orbit span of v. But

  Ind_H^S4 χ = sign ⊗ Ind_H^S4 1
             = sign ⊗ (1 ⊕ U)
             = sign ⊕ U.

Indeed S4/H is the three-element set of pair partitions. Hence an H-sign vector has only sign and (2,2) isotypic components. Applying the already certified e_sign[j(C)]=0 gives

  [j(C)] = e22[j(C)].

This is a cohomological statement about the actual block-even class; an unaveraged representative need not satisfy the H character pointwise. A regular representative with that character may be obtained by the finite H character projector whenever needed. The sign primitive may then be subtracted regularly. No additional source value is obtained.

This explains the limitation sharply: the representation selection can discard irrelevant types from an arbitrary raw cochain before weighting, but on the retained paired class every remaining condition was already carried by (2,2). More precisely, the retained paired space maps into an H-sign slice of the full upstairs (2,2)-isotypic cohomology; that slice need not itself be S4-stable. No S4 representation on the fixed thirty-dimensional paired target is asserted. The upstairs multiplicity space can still support both the ten- and twenty-dimensional coefficient pieces. S4 type alone does not distinguish those pieces or show either is zero.

In the full natural canonical-sheaf convention, the paired source is H-invariant and the relevant full-group projector is invariant rather than sign. Tensoring by the ordered top-form character exchanges these conventions. The decomposition Ind_H^S4(1)=1⊕(2,2) gives exactly the same retained conclusion.


## Public dependencies

See DEPENDENCIES.md for commit-pinned source closure, coefficient geometry and transport. The comparison [R]=j(C) is assumed only in its admitted source-specific scope. Neither that equality nor high-order ideal membership is proved here.
