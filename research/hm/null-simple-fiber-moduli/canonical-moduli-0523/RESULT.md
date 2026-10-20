# Canonical square-zero extensions, cotangent torsors, and the precise missing comparisons

## Result

There is a serious theorem-based route through **Hochschild characteristic classes and Atiyah classes**, and a more conditional route through **deformed 2-Calabi–Yau completions**. Neither currently identifies the actual source deformation, the lift torsor, or the mixed obstruction. The canonical bracket determines only one of three Hochschild components. The root-line correction can change the other two, including the crucial middle component.

A particularly relevant published-looking shortcut does **not** apply as stated: Han–Liu–Wang's exact-Hochschild-extension/Koszul-duality theorem has a degree-vanishing hypothesis excluding the desired n=2 case for nonzero unital algebras. This was checked in the rendered original PDF, not inferred from its abstract.

All statements below concern the stipulated static geometry. No physical source or jet values are evaluated in this argument. No global module or any of the thirty obstruction values is asserted.

## 1. The correct parameter space has three pieces

For S=P², define coefficient Hochschild cohomology by

    HH²(S,ω_S) := Ext²_{S×S}(O_Δ,Δ_*ω_S).

Coefficient HKR gives

    HH²(S,ω_S)
      ≅ H⁰(Λ²T_S⊗ω_S) ⊕ H¹(T_S⊗ω_S) ⊕ H²(ω_S)
      ≅ H⁰(O_S) ⊕ H¹(Ω¹_S) ⊕ H²(ω_S)
      ≅ C³.

The second isomorphism uses contraction with top forms, not a choice of a volume on P². Write the components as (a,b,c). Their meanings are respectively the biderivation, locally trivial/gluing deformation, and scalar gerby deformation. A globally split sheaf algebra with product (fg,fv+gu+B(f,g)/2) specifies a particular representative with no extra prescribed gluing or gerby component; an actual descended, Morita-modified, or algebroid deformation need not be that representative.

Therefore the identity Λ²Ω→ω fixes a, but it does not fix b or c. Scalar compensation alone changes c. It does not determine or remove b.

This is our coefficient-HKR calculation. Its formal input is the diagonal HKR/Atiyah construction described by Toda, §5, especially Proposition 5.3 and Lemma 5.8. Toda's Proposition 6.1 proves a lifting criterion for the usual untwisted HT² deformation using its action through the exponential Atiyah class. It is not itself a printed theorem for arbitrary ω-valued algebroids: extension to the present coefficients and the chosen module category still has to be established. [Toda, *Deformations and Fourier–Mukai transforms*](https://arxiv.org/pdf/math/0502571).

## 2. The strongest direct obstruction mechanism

Lowen's Theorem 4.8 and Corollary 4.9 identify the characteristic action of a Hochschild deformation class on an object with its first-order lifting obstruction. The setting is a linear category, respectively an abelian category with enough injectives, and a first-order deformation over dual numbers. This is an actual obstruction theorem, not just the observation that two vector spaces have equal dimensions. [Lowen, *Hochschild cohomology, the characteristic morphism and derived deformations*](https://preprints.ihes.fr/storage/Charfin.pdf).

For the present problem, the coefficient version has a concrete candidate map, without pretending ω is a scalar parameter:

    κ: O_Δ → Δ_*ω[2]
       ↦ κ_E: E → E⊗ω[2]

by the Fourier–Mukai action of this diagonal morphism. To prove it is the obstruction of the stipulated module problem, compare this action with the Čech lifting cocycle of that particular algebra/algebroid and its Morita data. This is the missing comparison to do first.

With a fixed normalization of HKR and the Atiyah exponential, its expected formula is

    o_κ(E) = (a/2) At(E)∧At(E) + b⌟At(E) + c·id_E.

Here b is equivalently a class in H¹(Hom(Ω¹,ω)); the notation b⌟At denotes evaluation, not an untyped wedge. If one instead identifies b with a one-form using contraction, the wedge sign must be fixed consistently. Factorials differ between published HKR conventions. The displayed normalization uses exp(At), so its degree-two term is At²/2; transport the algebra's B/2 convention before extracting a numerical scalar.

Taking trace connects this formula to ch₂(E), c₁(E), and rank(E). It explains exactly why stable-fiber compensation is scalar, but does not turn fiberwise compensation into familywise gluing.

Huybrechts–Thomas give a related precise theorem: for perfect complexes on commutative square-zero thickenings in their smooth-projective setup, the obstruction is the product of Atiyah and Kodaira–Spencer classes. Their commutative cotangent-complex theorem must not be directly applied to a noncommutative biderivation. [Huybrechts–Thomas](https://arxiv.org/abs/0805.3527).

## 3. Root-line / half-determinant correction is structurally essential

The following is a direct tensor identity, conditional on matching the preceding characteristic-class convention to the actual lifting problem. Tensoring E by a genuine line L with ℓ=At(L)=c₁(L) gives

    At(E⊗L) = At(E) + ℓ·id.

In the polynomial normalization above, evaluating κ on E⊗L instead of E has the effect

    a' = a,
    b' = b + aℓ,
    c' = c + bℓ + (a/2)ℓ².

This formula denotes the induced pairing in the middle term consistently with §2. Transport in the inverse direction substitutes −ℓ. Thus retaining End(E) and its Ext recipients while forgetting the tensor/Morita datum loses precisely information needed to identify κ.

For the supplied root relation N²=p*O(1), the formal Hodge correction is ℓ=H/2. Since rank(E)=2 and c₁(E)=−H, this is the determinant-centering shift. There is no O(1/2) line on P²; making this transport downstairs requires the actual root-gerbe or Morita descent, not a fictional line bundle. It is therefore legitimate to identify this as a possible missing middle term, but illegitimate to declare the actual class (a,0,c) from the bracket computation alone. No Cayley–Hamilton cancellation is promoted here to an established source-lifting theorem.

## 4. The Calabi–Yau completion route: exact theorems and exact gaps

For a finite-type dg category A, Bozec–Calaque–Scherotzke prove

    Perf_{G_n(A)} ≃ T*[2−n] Perf_A

(Corollary 6.12), with equality of the natural exact shifted-symplectic structures (Theorem 6.17). Section 6.2, equation (6.14) and the following pushout construction, sends a deformation parameter to the derived zero locus of its transgressed section. A negative-cyclic lift supplies the closed-form structure; §6.3 discusses this compatibility. For n=2 this is the ordinary-cotangent degree. Their Example 6.20 is not a general theorem; it is a quiver specialization. [Bozec–Calaque–Scherotzke, *Relative critical loci and quiver moduli*](https://arxiv.org/pdf/2006.01069).

Keller defines the deformed n-CY completion using a class in HH_{n−2}(A). His erratum expressly requires a negative-cyclic lift to assert the CY property. Merely having a Hochschild class is insufficient. [Keller, original](https://arxiv.org/abs/0908.3499); [Keller, erratum](https://arxiv.org/abs/1809.01126).

### Why n=2 is the right candidate, and n=3 is not

Our own degree check: for a smooth proper surface the Serre functor is tensor ω[2]. Therefore a categorical model of tensor ω is its Serre bimodule shifted by −2. A canonical square-zero extension has the formal shape A⊕DA[−2], where DA is the proper dual/Serre bimodule. Correspondingly coefficient HH² is naturally dual to HH₀; the Hodge decomposition also identifies its three summands with the three diagonal Hodge summands of HH₀(P²). The passage from a functional on HH₀ to an element of HH₀ needs an appropriate pairing/Koszul-duality comparison. It is not automatic identification of parameters, and Todd/Mukai normalizations can mix the displayed components.

The local canonical threefold Tot(ω_S) is instead associated with a 3-CY completion and −1-shifted cotangent/critical-locus geometry. It does not by itself explain the unshifted V-torsor in this task.

### The strongest directly relevant Koszul-duality theorem fails an essential hypothesis here

Han–Liu–Wang's Theorem 7 treats a finite-dimensional complete typical augmented dg K-algebra, K=k^t, an integer n satisfying A_{2−n}=0, and an exact class α∈H²(A,A∨[−n]). It identifies the Koszul dual of the associated Hochschild extension with Π_n(A†,α†). Exactness means arising from dual cyclic homology; the dual class has a negative-cyclic lift. At n=2 the printed condition is A₀=0, not merely vanishing of an augmentation-ideal piece. This excludes nonzero unital examples. Their Remark 2 explains that dropping the corresponding vanishing can give a curved A∞ algebra. [Han–Liu–Wang, Theorem 7 and Remark 2](https://arxiv.org/pdf/1909.02200).

Consequently this source provides an extremely relevant template, but not a theorem applicable to our n=2 extension as stated. A curved/relative version, or an independent comparison of the actual lift moduli with a deformed completion, is needed. Even such a comparison must identify the relevant subcategory of modules and the family E; a Koszul-dual algebra identity alone does not identify its entire module moduli with the stipulated locally free lift problem.

## 5. Determinant-line torsors: a valid diagnostic, not an identification

For a line D on a smooth moduli space M, the torsor of splittings of its Atiyah sequence is an Ω¹_M-torsor with class ±At(D)=±c₁(D), depending on the splitting convention. This follows directly by choosing local frames: differences of local connections are dlog of transition functions.

An explicit theorem identifying a bundle-connection moduli torsor with a determinant-line connection torsor is available for stable bundles on a **compact Riemann surface** in Biswas–Hurtubise; the degree-nonzero case includes a fixed logarithmic pole and scalar residue. Its dimension-one hypotheses are substantive. It is not a theorem for canonical square-zero quantizations on a surface. [Biswas–Hurtubise, *Meromorphic connections, determinant line bundles and the Tyurin parametrization*](https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806251612396032002-1806251612396032002-30feef7ae18aeccb46ec7620e260d8d5.pdf).

For our explicit E on S×U, determinants det Rs_*(E⊗q*Q), when defined for a chosen perfect Q, are legitimate candidate test lines. Their Atiyah classes can be compared to an independently derived transgression. However, choosing Q, the scalar coefficient, the Todd correction, and the equality to the lift torsor are additional work. An arbitrary complex cotangent-torsor class need not be the integral c₁ of a line.

Two especially important type checks follow from the supplied geometry:

1. V has rank 12, whereas Ω¹_U has rank 2. The Kodaira–Spencer dual gives V→Ω¹_U. Identifying the image of a class in H¹(U,V) with a determinant c₁ does not identify that class unless the kernel is controlled. On a suitable full smooth stable moduli locus one could use its own cotangent bundle, then pull the torsor back to U, but this moduli-level construction and its descent have to be supplied.
2. A lift torsor has class τ∈H¹(U,V). The stipulated mixed recipient is H¹(U,V⊗ω_U). There is no canonical operation that sends an individual τ to this latter group simply by saying “tensor the torsor by ω_U.” A second deformation and its compatibility must produce the coefficient. Even a full determination of τ is not, without that comparison, a computation of the mixed obstruction.

## 6. Holomorphic Chern–Simons and the practical next step

PTVV's orientation/transgression theorem produces (2−d)-shifted symplectic geometry from a d-dimensional Calabi–Yau source. For a genuine CY3 this is −1-shifted, consistent with critical loci; P² has no volume trivializing ω. Thus an appeal to holomorphic Chern–Simons or the local canonical threefold does not supply the missing ordinary cotangent torsor or the ω_U-valued mixed operation. [Pantev–Toën–Vaquié–Vezzosi, *Shifted Symplectic Structures*](https://arxiv.org/abs/1111.3209).

The shortest justified next step is:

- Define the actual coefficient-Hochschild/algebroid class after root-line transport, including all (a,b,c).
- Prove its characteristic action agrees with the chosen module lifting obstruction.
- Identify the familywise null-homotopy/lift torsor after scalar compensation; compare on overlaps to obtain its actual H¹(U,V) class.
- Only then compare with determinant/negative-cyclic transgression, or apply the second canonical deformation to reach H¹(U,V⊗ω_U).

The principal repair is therefore to retain the missing H¹(Ω¹_P²) datum and the exact module comparison. Existing CY and determinant theorems do not erase either requirement.
