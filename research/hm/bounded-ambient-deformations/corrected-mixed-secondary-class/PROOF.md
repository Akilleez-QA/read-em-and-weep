# The surviving mixed datum is a joint secondary bracket

## Result and scope

There are three new, bounded conclusions.

1. In a compatible joint algebra–module deformation model, the mixed obstruction has the explicit secondary formula

       S(a,b;c) = [d y + [x,z]] in H²(k_J).

   Here x,z are closed joint lifts of the two pure ambient cocycles a,b, c is the actual mixed ambient correction satisfying dc+[a,b]=0, and y is any lift of c. The formula specifies all nullhomotopy dependence. Pure H¹(k_L)=H¹(k_M)=0 removes pure-lift indeterminacy. Mixed HH²(J)=0 removes allowed ambient-correction indeterminacy. Neither vanishing removes this secondary class.

2. A fully explicit universal joint-DGLA countermodel has unique marked pure lifts, zero pure characteristic classes, zero mixed ambient deformation and obstruction groups, and block-even symmetry, but has a nonzero mixed obstruction. A second model with exactly the same complexes and first-order maps has zero obstruction. Thus these linear and symmetry data cannot determine mixed vanishing. This is not a geometric realization of the HM carrier.

3. For the corrected geometric directions, the external Hochschild cup class η_z⊠η_h is nonzero in HH⁴(Y,ω_Y), and its ordinary characteristic image is zero. Its degree is four, whereas the desired mixed module obstruction has degree two. It is therefore not the missing mixed class. In particular ordinary multiplicativity of the characteristic action cannot turn first-order annihilation into mixed vanishing.

The secondary-model theorem below is explicit about its model hypothesis. We do not silently identify an abstract DGLA expression with the actual prescribed transition defect. A concrete joint-model comparison must preserve the complete descent equations, coefficient actions, and the left-minus-right sign of the already established gerbe class. The geometric conclusions in Section 6 do not depend on such a comparison. The counterexample in Section 5 is unconditional formal algebra.

## 1. Established geometric inputs

Use Y=P²_z×P²_h, L=O(-3,0), M=O(0,-3), J=L⊗M=ω_Y, and the corrected bundle E=m*HM. Read:

- antecedent mixed-obstruction-transport / PROOF.md;
- antecedent retained-obstruction-comparison / PROOF.md and INTEGRATION-COROLLARY.md;
- antecedent pure-downstairs-identification / PROOF.md;
- antecedent pure-deck-structure / INTEGRATION.md;
- antecedent mixed-ambient-rigidity / PROOF.md;
- antecedent mixed-atiyah-constraints / PROOF.md;
- antecedent characteristic-trace-route / PROOF.md.

Under their accepted same-source hypotheses, the actual full mixed obstruction and corrected full mixed obstruction are one class after the marked normalized transport. The corrected class lies in the retained block-even thirty-space. No nonzero coordinate or vanishing is known from those statements.

The corrected pure direction on either plane is

    η=(P,D_P(H/2),−2H²) in HH²(P²,ω_P²).

Its first component is the nonzero canonical identity Ω²→ω; its local multiplication correction is P/2. The third entry is the source triple-unit coordinate b, whose characteristic contribution is −b Id. We retain this convention and do not change scalar signs when writing a characteristic map.

The unique marked pure lifts give χ_E(η_z)=χ_E(η_h)=0. Their rigidity imports Ext¹(E,E⊗L)=Ext¹(E,E⊗M)=0 and the corresponding Ext⁰ vanishings from the established corrected pure statements. These are assertions about the specified coefficient and marked categories.

The ambient calculation gives HH²(Y,J)=HH³(Y,J)=0 and HH⁴(Y,J) of dimension nine. Its deformation interpretation is only for the coefficient-action-marked mixed category. In particular it does not permit arbitrary changes to operations with pure-coefficient inputs. Literal external products provide the full ambient under consideration.

## 2. Exact joint-model hypothesis

The following algebraic statement applies to a short exact sequence of cochain DGLAs (or coefficientwise complexes with all brackets below defined)

    0 → k → d → h → 0.

Use d for the middle DGLA in this display only; below the differential is denoted ∂ to avoid ambiguity. The projection is p:d→h. All degrees are cohomological. The complexes have coefficient labels L,M,J, with a bracket from L and M to J. Pure squares and any products with J vanish in the bounded coefficient quotient. Positive coefficients have even parameter degree: their labels introduce no extra Koszul sign.

The intended identifications are

    Hⁱ(k_Q)=Extⁱ(E,E⊗Q),
    Hⁱ(h_Q)=HH^(i+1)(Y,Q),       Q=L,M,J.

The connecting map H¹(h_Q)→H²(k_Q) is the characteristic obstruction map χ_Q, with the convention fixed by the module descent equation. For the geometric application, a model must encode the *marked* simultaneous algebra–module problem and the frozen coefficient-input operations. This hypothesis is stronger than naming the three vector spaces or importing HKR as a complex isomorphism. No global formality or strict compatibility of an HKR splitting with brackets is assumed.

Suppose a∈Z¹(h_L), b∈Z¹(h_M) are the pure ambient directions, and χ_L[a]=χ_M[b]=0. Choose preliminary lifts X,Z in d¹, and pure module nullhomotopies u∈k¹_L,v∈k¹_M such that

    ∂X=∂u,   ∂Z=∂v.

Then

    x=X−u,   z=Z−v

are closed joint pure lifts. An actual mixed ambient is represented by c∈h¹_J with

    ∂c+[a,b]=0.

Choose y∈d¹_J with p(y)=c. In a genuine model the unknown mixed module correction is an element t∈k¹_J. The mixed coefficient of the Maurer–Cartan equation is

    ∂(y+t)+[x,z]=0.

The coefficient is exactly [x,z], with no factor 1/2: the two cross terms in (1/2)[x+z,x+z] are equal because x,z have degree one.

## 3. Secondary formula, dependencies, and proof

Put R=∂y+[x,z]. Its projection is ∂c+[a,b]=0, so R lies in k²_J. It is closed because ∂x=∂z=0. Consequently

    S(a,b;c)=[R]∈H²(k_J)

is defined. A mixed module correction exists exactly when S=0. The equation to solve is ∂t=−R, matching the positive-defect convention. This is a statement about the specified joint model; identification with a separately presented gerbe cocycle must use that same sign.

### 3.1 What the Atiyah nullhomotopies contribute

Expanding the formula yields

    R = ∂y+[X,Z]−[u,Z]−[X,v]+[u,v].                 (1)

The first-order characteristic equations provide ∂u=∂X and ∂v=∂Z. They do not specify the brackets in (1), nor a primitive for their sum. The individual terms need not be closed, so interpreting any of them alone as an ordinary Yoneda class is generally invalid.

The choices X,Z merely split the joint complex. Keeping x,z fixed while replacing X,u by X+r,u+r, or Z,v by Z+s,v+s, leaves (1) literally unchanged. Thus the formula does not depend on a preferred chain-level representative of the characteristic map.

### 3.2 Changing the mixed lift

Replacing y by y+t with t∈k¹_J changes R by ∂t. Hence S is independent of y.

### 3.3 Changing pure module nullhomotopies

Any other closed joint lifts over the *same* a,b have the form x+q,z+r with q∈Z¹(k_L), r∈Z¹(k_M). Their obstruction changes by the class of

    [q,z]+[x,r]+[q,r].                             (2)

This is the full dependence, including the cross term when both choices change. These brackets are closed because all four arguments are closed. If q=∂U and r=∂V with U,V in k⁰, the change is the coboundary

    ∂( [U,z]−[x,V]+[U,∂V] ).                     (3)

Indeed ∂[x,V]=−[x,∂V] since |x|=1, while ∂[U,z]=[∂U,z]. Thus H¹(k_L)=H¹(k_M)=0 kills every ambiguity (2). H⁰(k_L)=H⁰(k_M)=0 gives uniqueness of marked comparisons in a nonnegative model; it is stronger than needed for independence of the class S.

### 3.4 Changing the allowed ambient correction

If c is replaced by c+e with ∂e=0 in h¹_J, choose a lift E of e. The difference of the two obstruction classes is

    [∂E]=χ_J([e]).                                (4)

This is the connecting-map definition, not an assumed equality of zero sets. In particular H¹(h_J)=HH²(Y,J)=0 removes this allowed ambiguity. H²(h_J)=HH³(Y,J)=0 ensures that a closed cross bracket [a,b] admits an ambient primitive c within this model. The two facts leave R in k²_J untouched.

Equation (4) only compares extensions in the fixed coefficient-action-marked model. It does not compare presentations with different operations on positive coefficient inputs.

### 3.5 Ambient representatives and the bounded pairing statement

For example, replace a by a+∂α, choose A∈d⁰_L lifting α, and set

    x′=x+∂A,   c′=c−[α,b],   y′=y−[A,z].

Then ∂c′+[a+∂α,b]=0 and R′=R literally. There is an analogous formula in the other direction; applying the two in succession includes their cross correction. Hence compatible representative changes preserve S.

If a single compatible bigraded model and coefficient-action family exist over linear spaces of pure directions, and every cross bracket admits a mixed ambient primitive (for example because H²(h_J)=0), the preceding identities, together with pure H¹ vanishing and mixed H¹ vanishing, give a well-defined bilinear secondary map on the relevant kernels of χ_L,χ_M. One may choose linear sections and primitives to see bilinearity, and independence then removes these choices. Existence of those primitives is an additional hypothesis, not a consequence of either H¹ vanishing.

This is a **conditional** pairing theorem. The geometric rigidity note by itself does not supply such a family over arbitrary pure characteristic kernels. For the already fixed external product and its scalar rescalings the bounded expression is compatible with (a,b,c)↦(λa,μb,λμc), and R↦λμR. No unrestricted pairing on all geometric kernel directions is claimed here.

## 4. The root-cause distinction: joint lifts versus Ext¹ classes

Even when H¹(k_L)=0, the closed joint lift x need not be exact in d_L. In fact if [a]≠0 in H¹(h_L), exactness x=∂A would imply a=∂p(A), a contradiction. The same holds for z.

Thus pure rigidity does not make x or z vanish in joint cohomology. It only makes the choice of lift over a or b unique. The coefficients u,v in (1) are generally *not closed*: their differentials are representatives of the first-order characteristic cochains. Those representatives can be exact without being literally zero.

It is therefore wrong to place x,z in the ordinary pure Ext¹ groups and infer [x,z]=0 because those groups vanish. This rules out a specific mistaken Yoneda-product route. It also explains why setting the cohomological characteristic images to zero is not a valid operation on every term of (1): the chosen nullhomotopies and mixed bracket compatibility still matter.

Exchange of the two pure factors gives [z,x]=[x,z], again because both joint lifts have degree one. The secondary curvature is therefore compatible with block-even symmetry. This differs from the block-odd commutator of projected Atiyah forms in antecedent mixed-atiyah-constraints / PROOF.md, whose scalar entries have even total form degree. Transferring the latter parity rule to the joint deformation lifts would use the wrong grading.

## 5. An exact countermodel, including ambient rigidity

Work over a characteristic-zero field. Construct a nonnegative bigraded DGLA k with

    k⁰=0,
    k¹=〈u,v〉,
    k²=〈a₀,b₀,w〉,
    ∂u=a₀,   ∂v=b₀,   ∂k²=0.

Assign bidegrees (1,0) to u,a₀; (0,1) to v,b₀; and (1,1) to w. Its only nonzero bracket of generators is

    [u,v]=[v,u]=w.

The squares [u,u],[v,v] are zero by definition. Degree-two generators are central. The differential is a derivation: for instance ∂[u,v]=0=[a₀,v]−[u,b₀]. Every Jacobi expression is zero because inner brackets are central. Hence this is a genuine DGLA, not merely a proposed curvature table.

Adjoin degree-one generators A,B of bidegrees (1,0),(0,1), with

    ∂A=a₀,   ∂B=b₀,

and all brackets involving A or B zero. This gives a DGLA d containing k as an ideal. Its quotient h is abelian with degree-one basis ā,b̄ and zero differential; it has no mixed component in any degree. Consequently

    H¹(k_L)=H¹(k_M)=0,   H⁰(k_L)=H⁰(k_M)=0,
    H¹(h_J)=H²(h_J)=0,
    H²(k_J)=〈[w]〉.

The connecting characteristic classes of ā,b̄ are [a₀]=[b₀]=0. The unique closed joint lifts over ā,b̄ are

    x=A−u,   z=B−v.

There are no degree-zero gauge parameters and no alternative pure closed kernel additions. The ambient mixed correction is c=0, uniquely, and choose y=0. Nevertheless

    R=[A−u,B−v]=[u,v]=w.

It is nonzero in H²(k_J), since k¹_J=0. In the bounded coefficient quotient the ambient direction exists, the two pure marked modules exist uniquely, but no joint mixed module solves the equation.

The exchange u↔v, a₀↔b₀, A↔B fixes w and preserves the differential and bracket. Thus this obstruction is block-even.

Finally define a second model by changing only [u,v] to zero. All complexes, cohomology groups, characteristic maps, pure lifts, mixed ambient rigidity, and block exchange remain the same. Its mixed obstruction is zero. Thus the listed first-order linear data, even supplemented by mixed ambient rigidity and block symmetry, cannot distinguish the two outcomes.

This example does **not** assert that either model is the corrected geometric deformation complex, that it has the HM Atiyah class or a rank-two bundle realization, or that arbitrary characteristic-trace information agrees. It proves exactly that the indicated linear/rigidity/symmetry premises do not entail mixed vanishing. Any geometric vanishing proof must use additional bracket/homotopy data or an identity with equivalent force.

## 6. A geometric wrong-degree exclusion requiring no joint-model comparison

Let χ_E denote the ordinary coefficient-valued Hochschild characteristic action, defined by applying diagonal kernels to E. Composition of kernels makes it compatible with cup products, including the natural twists by L and M. Therefore

    χ_E(η_z∪η_h)
      = χ_(E⊗M)(η_z)[2] composed with χ_E(η_h)
      = 0 in Ext⁴(E,E⊗J).                         (5)

Here χ_E(η_h):E→E⊗M[2], and the shifted next arrow goes from E⊗M[2] to E⊗J[4]. This avoids identifying the characteristic action on E⊗M with the action on E tensored by M, an identification that would need justification. Equation (5) needs only the first arrow to vanish. It uses the vanishing of an actual pure characteristic class established by its lift, not equality of its raw representative to zero.

On a plane, coefficient HKR and Λ^pT⊗ω≅Ω^(2−p) show that HH^n(P²,ω) is concentrated in n=2 and is three-dimensional. Every one of the three diagonal HKR summands contributes one dimension. For the product, external Künneth consequently gives

    HH⁴(Y,J) ≅ HH²(P²,ω)⊗HH²(P²,ω).

Under this identification η_z∪η_h is exactly η⊗η. The nonzero canonical bivector component of η ensures η≠0; a pure tensor of two nonzero vectors over a field is nonzero. Hence

    0≠η_z∪η_h∈ker(χ_E:HH⁴(Y,J)→Ext⁴(E,E⊗J)).    (6)

There is no need to calculate a physical source or a matrix instance to prove (6). No claim that this kernel is one-dimensional is made.

The desired mixed class is instead in Ext²(E,E⊗J). Thus (5) and (6) give no value for it. An ordinary degree-preserving characteristic action on the external cup product lands two degrees too high. A proposed formula using that product would require additional, specified degree-lowering secondary data; it cannot follow just from multiplicativity. Nor can it be an ordinary characteristic image of a mixed HH² class, since HH²(Y,J)=0 in the fixed ambient coefficient complex.

This last fact does not make the module class zero: its pure boundary is already deformed, and the mixed lifting problem is relative to that boundary. The secondary term measures this relative compatibility. It is not the primary characteristic class of a freely adjustable classical mixed ambient deformation.

## 7. Independent checks and remaining task

The signs in (2)–(3) were checked directly using the graded Leibniz rule rather than by analogy with an ungraded commutator. The symmetry check uses graded antisymmetry for two degree-one elements. The countermodel independently checks every differential, Jacobi, cohomology, pure-lift, and mixed-solvability claim directly. The degree-four calculation is independently forced by plane HKR concentration and external Künneth; it is not inferred from the secondary model.

The most concrete next mathematical input would be a compatible chain-level description of the joint bracket/nullhomotopies, or a geometric identity forcing their mixed curvature to be exact. Merely knowing the cohomological Atiyah annihilation, pure uniqueness, external ambient rigidity, or block-even membership cannot supply that identity. Ordinary Atiyah-trace maps were already shown blind to the retained class in the characteristic-trace proof, so their vanishing adds no detector here.
