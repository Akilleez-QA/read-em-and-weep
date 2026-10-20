> Publication scope: Rank352 obstruction bundle and relative zero scheme; P and S remain imported. The original D table is now independently supplied by cubic P01, not newly recalculated here. Source-stage audit/checker references describe historical evidence, not fresh execution or bundled executable artifacts. Named source identities are hypotheses unless separately proved below.

# A relative rank-352 obstruction bundle and its algebraic zero scheme

## 1. Statement with separate premises

Work over a characteristic-zero field k. Let C be the smooth projective elliptic curve y²=z³−z, X=C⁴, Y=(P¹)⁴, q:X→Y the product double cover, N=⊠O_C(O), and G=(Z/2)⁴ its deck group. Write χ for the full-sign character. Let u denote the original five elementary-symmetric coefficient sections, modulo common scalar.

The following inputs must not be conflated.

**P (geometric presentation).** The specified homogeneous four-term locally free presentation of H on P⁴ is exact except for its locally free degree-zero cohomology, and its first arrow is the literal sparse arrow in [the full-coefficient theorem](../../cubic-loci/foundation-p01/COEFFICIENT-FAMILY.md). This includes its imported historical exactness premise; no new certification is supplied here.

**D (historical dimensions).** At u, for the induced conjugation action of G on End E, the invariant Ext dimensions in degrees 0 through 4 are (1,79,352,0,0). These are imported from [the historical Ext-model snapshot](../../cubic-loci/foundation-p01/INVARIANT-COHOMOLOGY.md), not recomputed. No other character-dimension table is necessary for this proof.

**S (actual source identification).** Admit the inherited homogeneous source identities, determinant normalization, raw recipe, and rational-denotation conventions specified in [the source-family proof, §§1–4 and 8](../relative-mixed-character-purity/dependencies/SOURCE-FAMILY.md). Its chart-weight argument then proves a regular family of the SAME actual closed mixed residual, on its actual root/carrier cover. S is additional to P and D. It is not implied merely by an abstract bundle family or by exactness of the presentation.

Under P and D there is a smooth affine open neighborhood B of u in the 79-dimensional projectivized coefficient parameter space and vector bundles

    A = (R²π_* End 𝓔)^G,       V = (R²π_* End 𝓔)_χ,
    rank A = rank V = 352,      V ≅ A∨,

where π:X×B→B and the duality uses a chosen nonzero volume form on X. Both bundles and the cohomology interpretation commute with arbitrary base change, including nonreduced Artinian bases.

Under S as well, the actual residual has a regular full-sign class section rχ∈Γ(B,V). Its zero scheme Zχ⊂B is closed algebraic and represents vanishing of that projected class under base change. At every point b where rχ(b)=0 its tangent space is the kernel of the corrected variation formula in §7.

**Purity boundary.** This construction always concerns the full-sign projection of the actual residual. To call Zχ the vanishing locus of the entire mixed obstruction requires the further conclusion or premise that the entire mixed class is full-sign throughout this neighborhood. The cited source-family theorem proves actual regularity and closure, but does not itself state this character-purity result. Without independently checking it, no equality between full-sign vanishing and total vanishing is claimed.

In particular this theorem proves neither that u belongs to Zχ nor that any point does, and proves neither nonvanishing nor identically zero behavior of rχ.

## 2. Extending the sparse Kodaira–Spencer proof to every independent tuple

Put W=H⁰(Y,O(1,1,1,1)); dim W=16, and q* identifies it with H⁰(X,N²). Let U⊂P(W⁵) be the generating locus constructed in the full-coefficient theorem. Intersect it with the open locus Uind where the five sections are linearly independent. This contains u: the five elementary-symmetric sections have disjoint nonempty supports in the squarefree-monomial basis.

For any geometric point s∈Uind, repeat that theorem with s in place of u. The complex terms are still 5N⁻¹,15N,10N³,2N⁵. Their line-bundle cohomology and the strict-chain-map lifting argument are unchanged. A zero KS class therefore forces

    δγ = Pγ − γQ

with P,Q constant. Each singleton row forces δs_i to belong to span(s₀,…,s₄), so δs=Ms for a constant matrix M. The literal support argument uses only independence of the five labels and the fixed sparse pattern. Its cyclic coefficient identity forces M to be scalar. Thus δs is zero as a projective tangent. This is a new uniform use of the bundled proof, not an assertion that its original statement already claimed uniform injectivity.

Every geometric fiber has an injective KS map from a 79-dimensional tangent space. The universal map factors through q, and N has its fixed natural deck linearization. Hence the entire bundle family is G-equivariant with trivial G-action on the parameter space. Its KS classes lie in invariant Ext¹, not merely in total Ext¹. Consequently

    dim Ext¹(E_s,E_s)^G ≥ 79

at every geometric point of Uind. No rank computation or specialization is involved.

Choose an affine projective chart containing u and normalize the tuples by ℓ(s)=1, with ℓ(u)=1. On this chart the presentation terms and the identification F*O(1)=N² are fixed, and the source theorem §8 applies literally. We shall shrink inside this chart.

## 3. Perfect pushforward, semicontinuity, and the dimension sandwich

End 𝓔 is a vector bundle on the smooth proper product X×Uind. Its derived pushforward is perfect and commutes with arbitrary derived base change, by [Stacks Project, Lemma 36.30.4](https://stacks.math.columbia.edu/tag/0A1G). Averaging gives idempotents

    e_α = (1/16) Σ_(g∈G) α(g)⁻¹ g.

Their summands K_α of Rπ_*End 𝓔 are perfect and commute with base change. Equivalently, finite projection q gives coefficient bundles End(F_Y*H)⊗L_α on Y, where L_α is the corresponding summand of q_*O_X. Their pushforwards give the same K_α.

Fiber cohomology dimensions of K_1 are upper semicontinuous and its Euler characteristic is locally constant; these are the finite-complex statements underlying [Stacks Project, Lemmas 36.32.1–2](https://stacks.math.columbia.edu/tag/0BDM). At u, D supplies the five dimensions. Shrink around u so that

    h⁰_inv ≤ 1,   h¹_inv ≤ 79,   h³_inv = h⁴_inv = 0.

The identity endomorphism gives h⁰_inv≥1 in every fiber. Section 2 gives h¹_inv≥79 in every fiber. Thus h⁰_inv=1 and h¹_inv=79 everywhere on this open. The invariant Euler characteristic on its component is its value at u,

    χ_inv = 1 − 79 + 352 = 274.

Therefore h²_inv=352 throughout. All other degrees vanish since the fibers are four-dimensional and E_s is locally free. This obtains the needed Euler value directly from the separated historical premise D and local constancy. No separate Riemann–Roch or historical rank certificate is being silently authenticated.

## 4. Why this really gives bundles and arbitrary base change

Shrink to a smooth affine neighborhood B of u in the preceding open. It is reduced. On an affine refinement a perfect complex is represented by a bounded complex of finite free modules. Constant dimensions of all its fiber cohomology determine, recursively from the ends, constant ranks for all differentials.

A constant-rank map of finite free modules on a reduced scheme locally splits: invert a maximal nonvanishing minor; all larger minors vanish in every residue field and hence vanish in the reduced ring. Row and column operations then exhibit an identity block and a zero complementary block. Applied successively to the finite complex, this splits off contractible pairs and leaves its cohomology as finite locally free modules with zero differentials. This is an abstract local argument, not an evaluated matrix calculation.

It follows that all invariant cohomology sheaves are locally free and that their formation commutes with arbitrary base change. The reducedness of B is used here: a complex with a nilpotent differential on an initially nonreduced base can have constant pointwise dimensions without this conclusion. After the splitting on B is established, pulling it back to a nonreduced base is legitimate and preserves the base-change statement. In particular A is locally free of rank 352.

## 5. Full-sign duality

The volume form Ω=∧_(i=1)^4(dz_i/y_i), up to a nonzero scalar, trivializes ω_X and transforms by χ under G. Trace identifies End 𝓔 with its dual. [Serre duality on a smooth proper variety](https://stacks.math.columbia.edu/tag/0FVU) on every geometric fiber therefore pairs invariant Ext^j perfectly with full-sign Ext^(4−j). The full-sign fiber dimensions are consequently

    (h⁰_χ,h¹_χ,h²_χ,h³_χ,h⁴_χ) = (0,0,352,79,1).

The same perfect-complex splitting argument gives the full-sign relative cohomology bundles and arbitrary base change. Cup product followed by matrix trace and Serre trace gives an algebraic relative pairing A⊗V→O_B after choosing Ω. It is perfect on every geometric fiber; hence V→A∨ is an isomorphism of vector bundles. Intrinsically the target before choosing Ω is the fixed one-dimensional top-cohomology line H⁴(X,O_X), carrying character χ. Thus an invariant/full-sign pairing is the appropriate one, rather than invariant/invariant duality.

In particular R¹π_*End(𝓔)_χ=0 on B and after every base change. This will ensure the explicit primitive-independence in §7.

## 6. From the actual regular cocycle to an algebraic section and zero scheme

The source-family theorem §8 applies to the normalized universal tuples on B. Under S its root/carrier construction supplies a regular End(𝓔)-valued Čech 2-cocycle R_B on an actual open cover of X×B. Its line-frame compatibility is proved there by homogeneous weight cancellation, while carrier changes are genuine transition maps; it is not enough to have unrelated closed classes on separate fibers.

Refine by finitely many affine opens. Since X×B is separated, finite intersections of affine opens are affine, so this Čech complex computes coherent cohomology. The regular cochain and its actual cocycle identity define a class

    [R_B] ∈ H²(X×B,End 𝓔).

Because B is affine, the Leray spectral sequence gives H²(X×B,End 𝓔)=Γ(B,R²π_*End 𝓔). Projecting its class by e_χ gives rχ∈Γ(B,V). A deck-stable affine refinement permits projection at the cochain level as well; equivalently project the derived class, which is cover-independent. The quotient rule for physical derivations commutes with parameter base change, because the physical fields kill parameter functions. Thus this section specializes to the actual projected source class, rather than merely to some section with the same central value.

Let Iχ be the image of V∨→O_B, λ↦λ(rχ). Define

    Zχ = Spec_B(O_B/Iχ).

In any local trivialization of V it is cut out by the 352 regular coordinate functions of rχ. This does not assert their independence, their nonvanishing, a codimension, or reducedness of Zχ. Changing a bundle trivialization changes the generators, not the ideal.

For every T→B, the map factors through Zχ exactly when its pulled-back section is zero. Via arbitrary base change this says the projected relative class vanishes. For affine T, including any local Artinian T, it is also equivalent to vanishing in H²(X×T,End 𝓔_T)_χ. For nonaffine T one should retain the relative-section formulation; a zero relative section need not automatically make an arbitrary absolute cohomology class zero without examining Leray terms.

For a point b∈Zχ, the completed local zero scheme is cut out in Ō_(B,b) by the completed ideal Iχ. Its Artinian points are exactly coefficient-family deformations through b on which this second-order mixed projected obstruction vanishes. If b is not in Zχ there is no such pointed formal locus. At u no membership assertion has been established. One can always define the formal inverse image inside Spf(Ō_(B,u)); if rχ(u) is nonzero, its defining ideal becomes the unit ideal and this formal zero scheme is empty. Completion introduces no claim about higher star orders, existence of a full star module, convergence, or algebraization of arbitrary formal solutions.

## 7. Corrected derivative and the exact tangent criterion at a zero

Let b be a k-point with rχ(b)=0; the same assertion applies after extending the residue field for a geometric point. Use a finite deck-stable affine refinement of the source cover. Write R for a projected full-sign representative at b. Choose a regular full-sign Čech 1-cochain Q such that δQ=R. Such a primitive exists because the projected cohomology class is zero; averaging makes it full-sign.

Take a coefficient tangent τ:Spec k[ε]/(ε²)→B at b. Work in first-vertex row-End conventions, with transitions g_ij(ε), G_ij=g_ij(0),

    T_ij(M)=G_ij⁻¹ M G_ij,     a_ij=G_ij⁻¹ dot g_ij.

On 1-cochains, δQ on the triple ijk is T_ij Q_jk−Q_ik+Q_ij. Holding the matrix coefficients of Q fixed while differentiating gives

    (dot δ Q)_ijk = [T_ij Q_jk,a_ij].

Extend Q arbitrarily to a regular first-order cochain Q(ε). Local frames on the fixed affine refinement allow such lifts. The cochain

    D_τ = dot R − dot δ Q − δ dot Q

is closed: differentiate δ_ε(R_ε−δ_ε Q_ε)=0 and use R−δQ=0. In a choice with dot Q=0, its class is represented by

    dot R_ijk − [T_ij Q_jk,a_ij].

If the character projectors vary in the chosen matrix coordinates, R_ε here means the actual projected cochain e_χ(ε)R_ε; differentiating that projection is included in dot R. One must not replace it by projection in frozen non-equivariant coordinates without justification.

This class is precisely the intrinsic derivative drχ_b(τ)∈V_b: subtracting the lifted coboundary makes the family cocycle zero at the special fiber, and its ε coefficient is its first-order relative cohomology class. The arbitrary lift changes D_τ by a coboundary. If the lift is not equivariant, D_τ itself need not be a full-sign cochain, but its class is full-sign; alternatively average the lift using the actual family action. If a different full-sign primitive Q′ is chosen, Q′−Q is a full-sign 1-cocycle. Since H¹(X,End E_b)_χ=0, write Q′−Q=δP. Differentiating δ_ε²=0 gives dot δ·δP=−δ·dot δ P, so the change in the displayed derivative is again exact. Coordinate, frame, and cover independence also follows from its intrinsic section-jet description.

The exact tangent criterion is therefore

    T_b Zχ = {τ∈T_bB : [D_τ]=0 in Ext²(E_b,E_b)_χ}.

This is not the uncorrected derivative dot R, and it is not a freely chosen direction in a fixed H². It requires a zero b and a primitive there. It supplies no primitive at u unless rχ(u)=0 has first been established.

## 8. Scope and evidence boundary

The vector bundle is proved under P and D. The actual section additionally needs S. Identification of its zero scheme with total mixed-obstruction vanishing additionally needs full-sign purity. These hypotheses are independent in purpose and evidence.

The theorem gives no evaluated equations, no nonzero obstruction witness, no zero point, no higher star-order lifting theorem. The use of rank in the geometric vector-bundle proof is abstract algebra, not a computation of any model matrix.

