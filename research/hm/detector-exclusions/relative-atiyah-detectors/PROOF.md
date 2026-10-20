# Target-relative Atiyah-square detectors

## Result

For the established rank-two carrier E=N⊗f*H on X=C⁴, with f=σq, define A=f*At(H) with values in f*Ω¹_P⁴, and

τrel(z)=tr(z∪A²) ∈ H⁴(X,f*Ω²_P⁴).

Unlike the ordinary Ω²_X target, this target is not excluded merely by full deck character. Nevertheless, τrel vanishes on the ENTIRE full-deck sector, hence on its retained [22] sector. In fact both proposed dual maps

H⁰(P⁴,Λ²T(-a)) → H²(P⁴,End H(-a)),   b ↦ b⌟At(H)²,   a=1,2,

are identically zero. This is a rank-two Atiyah identity plus the Euler sequence, not an obstruction computation. The provisional equivariant rank bound of eight is correct but strictly weaker than the resulting rank-zero bound. No conclusion about the obstruction itself follows.

## 1. A rank-two identity

Use exterior multiplication of holomorphic forms and the ordinary cohomological cup product throughout. Write α=At(H), c=tr α=c₁(H), and α₀=α−(c/2)Id. Then

 tf(α²)=c∪α₀.                                                (1)

Here is a bundle-valued proof, which does not require a global frame. The trace-free endomorphism bundle of a rank-two bundle satisfies the fiberwise identity uv+vu=tr(uv)Id. The cup square of a degree-one class in End₀(H)⊗Ω¹ is antisymmetric under simultaneous interchange of its two coefficient factors; projecting the Ω¹ factors to Ω² supplies another minus sign. Thus only the symmetric product of the two End₀ factors remains. Its matrix product is scalar by the displayed identity. Hence tf(α₀²)=0. Since c is scalar and its two signs cancel upon exchanging it with α₀, the cross terms in (α₀+(c/2)Id)² sum to cα₀, proving (1).

Equivalently, take a smooth connection compatible with the holomorphic structure and represent α by its End-valued (1,1) curvature. Its scalar entries are differential forms of even total degree, so the usual 2×2 Cayley–Hamilton identity applies. Taking trace-free parts gives (1), independently of the choice of connection. Either proof is an identity of global cohomology classes; it is not an assertion about entries of a source matrix.

## 2. Contraction factors through an acyclic Euler group

Let b be any section of Λ²T⊗O(-a). Contracting one Ω¹ factor defines b#:Ω¹→T(-a). The contraction of c∧α₀ is, up to a fixed nonzero scalar or sign depending on the normalization of bivector contraction, the evaluation cup product

 [b#c] ∪ α₀ ∈ H²(End₀H(-a)).                                (2)

This follows directly by antisymmetrizing the two holomorphic-form indices; the cohomological signs agree with (1). The value of that convention scalar is irrelevant for the vanishing claim. More concretely the expression is a sum b^{ij}(c_i∪(α₀)_j−c_j∪(α₀)_i), exactly the evaluation of the contracted vector-valued cocycle with α₀.

Twisting the Euler sequence gives

0→O(-a)→V⊗O(1-a)→T(-a)→0.

On P⁴, line bundles have no cohomology in degrees 1,2,3. Consequently H¹(T(-a))=0, in particular for a=1,2. Therefore [b#c]=0, and (2) vanishes. The scalar part of b⌟α² lies in H²(O(-a)), also zero. This proves that the two displayed dual maps vanish, without any HM-specific multiplication calculation. Indeed the same argument works for every integer a on P⁴ and every rank-two bundle.

## 3. Why these are exactly the relevant relative detectors

The trace pairing identifies End E with its dual. Serre duality on X identifies the dual of the full-deck part of H⁴(f*Ω²_P⁴) with the deck-invariant part of H⁰(f*Λ²T_P⁴), after choosing a nonzero holomorphic volume form. The volume has full deck character, geometric S4 character sgn, and simultaneous-inversion eigenvalue +1. The dual of τrel is contraction with A² followed by this Serre identification. Tensoring by N causes no End character and does not change this definition, which uses the target Atiyah class of H, not At(E).

The invariant global sections identify by finite pushforward with H⁰(P⁴,Λ²T⊗B), where B=σ_*O_Y. An S4-equivariant bundle splitting is

 B ≅ O⊗1 ⊕ O(-1)⊗(3[31]⊕[22])
             ⊕ O(-2)⊗(3[211]⊕[22]) ⊕ O(-3)⊗sgn.

The [22] part is therefore one copy of O(-1) and one of O(-2), tensored with the two-dimensional irreducible [22]. Multiplication by the pulled-back α² is O_P⁴-linear; hence in any such splitting it acts componentwise by precisely the two maps in §2. No compatibility of the splitting with multiplication in B is required. Since [22]⊗sgn≅[22], the Serre sign preserves this isotypic sector. The retained D8-epsilon sign-kernel selects one epsilon line of [22], so its dual map is also zero. This proves the stated relative-detector exclusion on the retained 30-dimensional sector and hence on its 12-dimensional inversion-positive part.

This argument is stronger than character counting: it establishes the actual cohomology maps are zero, not merely that the available domain is too small to span the desired dual space. It does not identify any historical detector with this relative trace construction.

## 3A. Stronger exclusion on the entire full-deck sector

Define τrel₁(z)=tr(z∪f*α) ∈ H³(X,f*Ω¹_P⁴). The full-deck component of this target equals H³(Y,σ*Ω¹_P⁴⊗L^(-2)). Pulling back and twisting the cotangent Euler sequence gives

0→σ*Ω¹_P⁴⊗L^(-2)→(L^(-3))⁵→L^(-2)→0.

For both displayed line bundles on Y=(P¹)⁴, Künneth places all cohomology in degree four. The long exact sequence therefore gives H³(σ*Ω¹⊗L^(-2))=0. Thus τrel₁ is zero on every full-deck class.

The rank-two Cayley–Hamilton identity can be written more fully as

 α²−c₁(H)α+c₂(H)Id=0

in H²(P⁴,End H⊗Ω²), with c₂ defined in the same Atiyah normalization. This follows from the curvature proof in §1, or by taking traces in (1) and using 2c₂=c₁²−tr(α²). In particular, multiplying by z and taking trace yields

 τrel(z)=f*c₁(H)∪τrel₁(z)−f*c₂(H)∪tr(z).

For a full-deck z, tr(z)=0 as a cohomology class even without an additional trace-free assumption: H²(O_X) has deck characters supported on exactly two factors, so its full-deck summand vanishes. Both terms on the right therefore vanish. This proves τrel=0 on the entire 352-dimensional full-deck Ext² sector, including its 176-dimensional inversion-positive part. No permutation, inversion, actual-source, or HM-specific cohomology input is needed for this stronger exclusion beyond the rank-two carrier and stated product-cover geometry.

The Atiyah identities here are cohomological identities. They are not claimed to hold for arbitrary uncorrected Čech representatives. The pullback target f*Ω¹ is retained throughout; replacing it prematurely with Ω¹_X would lose the point of this argument.

## 4. Independent check of the proposed inversion bound

The preceding zero theorem does not depend on this check. It is included to fix the linearizations and verify the suggested weaker bound.

Let R act on the five-dimensional coordinate section space with eigenvalue multiplicities (3,2). Its trace is 1 and determinant is +1. The binary-quartic convention identifies σ*O(1) with L using ordinary reversal on each P¹. On the [22] generator W₁, reversal acts as Schur_(2,2)(J)=det(J)²=+1. Finite duality B∨≅B(3)⊗sgn has no additional reversal character: the four P¹ determinant factors multiply to +1, as does det R on P⁴. Thus reversal also acts as +1 on W₂,[22]. Averaging graded generator lifts over S4×⟨j⟩ gives a simultaneous equivariant splitting. These two generator lines introduce no extra inversion sign.

Equivariantly Λ²T≅Ω²(5), since the determinant character of R is +1. The exterior Euler resolution gives

 tr H⁰(Ω²(k)) = tr(Λ²R) tr(Sym^{k-2}R)
                −tr(R) tr(Sym^{k-1}R)+tr(Sym^kR), k=3,4.

Here tr(Λ²R)=−2 and the symmetric-power traces for powers 1,2,3,4 are 1,3,3,6, obtained from (1-t)^(-3)(1+t)^(-2). Hence

- H⁰(Λ²T(-1))=H⁰(Ω²(4)): dimension 45, trace −3, positive dimension 21;
- H⁰(Λ²T(-2))=H⁰(Ω²(3)): dimension 10, trace −2, positive dimension 4.

For the HM Hom presentation, the internal degree-r coefficient traces for r=0,1,2,3 are 18,1,−8,−2, and the negative-degree traces agree. On P⁴, O(n) is acyclic for −4≤n≤−1; H⁴(O(-5)) has trace +1 under this R. Abstract equivariant Euler additivity then gives

 χ_R(End H(-1))=−1−8+6=−3,
 χ_R(End H(-2))=−8+2+2=−4.

The established cohomology rows are (0,5,10,0,0) and (0,0,20,0,0). To recover the missing H¹(-1) trace without assuming a lift on that group, use the already proved equivariant KS79 isomorphism. Its [31] multiplicity representation is Schur_(3,1)(C²)⊗R, of reversal trace (−1)·1=−1. On the pushforward decomposition the same multiplicity representation is Schur_(3,1)(C²)⊗H¹(End H(-1)), since other twists with [31] have no H¹. Therefore −tr H¹(End H(-1))=−1, so that trace is +1. Consequently

- H²(End H(-1)): dimension 10, trace −2, positive dimension 4;
- H²(End H(-2)): dimension 20, trace −4, positive dimension 8.

The volume contributes no inversion sign, and the self-duality of [22] with its sign twist does not change inversion. Thus an equivariant map of the indicated componentwise form would have positive-image dimension at most min(21,4)+min(4,8)=8 inside the 12-dimensional retained positive dual. Sections 1–2 show its actual image is zero.

## 5. Mathematical inputs and scope

Mathematical inputs: inversion-eigenspaces/PROOF.md and AUDIT.md; retained-sector-structural/PROOF.md; hm-presentation-independent/PROOF.md; characteristic-trace-route/PROOF.md; projective-target-directions/INVARIANT-EXT-STRUCTURAL-REDUCTION.md. The classical HM cohomology and KS79 theorem are imported exactly as in those audited documents. Actual source membership and inversion invariance retain their separately stated premises, but are unnecessary for the vanishing of the relative trace map on the abstract retained sector.
