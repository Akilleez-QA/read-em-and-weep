# Degree 65 is excluded by the abstract odd-multiplicity Rao pencil

## Result

In the complex projective Schrödinger-normalizer setting of the cited proof packets, there is no invariant reduced curve of degree 65 without line or conic components. Together with the already audited degree-60 exclusion and the exclusion through degree 55, this raises the reduced rank-four support alternative to

    Γ₄ is empty, or 70 ≤ deg Γ₄ ≤ 125, with 5 | deg Γ₄.

The new ingredient is a structural injectivity lemma for the unique eligible ten-dimensional target of quadratic-to-cubic Rao multiplication. The proof uses formal indeterminates, not an evaluated polynomial, point, matrix, rank instance, or actual source datum. It does not assume normality or arithmetic Cohen–Macaulayness.

## 1. Conventions and imported results

Write H for the order-125 Heisenberg group, Z(H)=μ₅, and G=SL₂(F₅). The linear normalizer is Ñ=H⋊G. The projective normalizer is N̄=Ñ/μ₅; its normal abelian subgroup is Aproj=H/μ₅≅F₅². All vector-space representation statements below concern Ñ, while invariance of projective varieties concerns N̄. The five-dimensional HM representation called A in the literature will be denoted AHM here, avoiding confusion with Aproj.

Import the following established results, exactly as used in the supplied packets:

1. Faithful N̄-actions on the normalization of a nondegenerate invariant integral curve have genus at least 326.
2. There is no N̄-stable integral curve of degree at most 55; Aproj-stable components have degrees divisible by five. Aproj-stable integral components of degrees 5 or 10 have N̄-orbits of size at least 20.
3. There is no N̄-invariant integral quintic surface, including nonnormal surfaces.
4. For S₁=V*, the HM tensor identity is

       V*⊗AHM* ≅ AHM⊗(T*⊕W′*),

   where T has dimension three and central G-involution +1, and W′ is an irreducible two-dimensional representation with central G-involution −1. Neither has a trivial constituent.
5. The audited sectional extraction/lifting argument: if an integral curve C⊂P⁴ has degree d>27, I_C(2)=I_C(3)=0, M₁=0, dim M₂=5, and multiplication S₁⊗M₂→M₃ is zero, then its general hyperplane sections lie on a canonically determined integral quintic. If d>22, the family lifts to an integral quintic surface; if d>25, that surface is unique and hence invariant whenever C is invariant.

Mathematical dependencies:

- ../rank-four-degree-sixty-lower-bound/PROOF.md
- ../degree-sixty-curve-frontier/PROOF.md
- ../quadratic-deficiency-exclusion/PROOF.md
- ../quadratic-deficiency-exclusion/INDEPENDENT_GEOMETRY_AUDIT.md
- ../cubic-massey-module-reduction/PROOF.md, §3, for the audited HM identity.

For clarity, item 5 is not importing a theorem special to degree 60. The audited proof uses that degree only in the comparisons d>27, d>22, d>25, the full symmetric sectional monodromy S_d, and the common-factor argument requiring d−3≥10. All these hold for d=65. Section 6 below records this specialization explicitly.

## 2. Integrality, linear normality, and absence of cubics

Let C be a putative invariant reduced degree-65 curve with no line or conic components. An Aproj-component orbit of size 25 costs at least 75 degrees. An orbit of size five, after conjugating its stabilizer through the six axes, forces at least thirty components and costs at least 90 degrees. Hence every component is Aproj-stable and has degree divisible by five.

The component action factors through the perfect group G. Any nonsingleton orbit has size at least five, so its common component degree is at most thirteen, hence 5 or 10. The imported small-component theorem then forces orbit degree at least 100. Thus every component is N̄-stable. Each has degree at least 60 by item 2 and divisibility, so degree 65 permits only one component. Thus C is integral.

Its span is all P⁴ by irreducibility of the Schrödinger representation. The action on its normalization ν:X→C is faithful: a finite-order projective transformation fixing the nondegenerate integral curve pointwise must have its span in one eigenspace, hence is projectively trivial. Therefore g(X)≥326.

Put L=ν*O_C(1). The nontrivial Heisenberg central character forces h⁰(X,Lⁿ) and h⁰(C,O_C(n)) to be multiples of five whenever 5∤n. If h⁰(X,L)≥10, choose ten sections containing the five ambient ones; this gives a basepoint-free birational degree-65 map to P⁹. Castelnuovo gives

    g(X) ≤ π(65,9)=224,

a contradiction. Therefore h⁰(X,L)=h⁰(C,O_C(1))=5 and M₁=H¹(I_C(1))=0.

The cubic exclusion in the degree-sixty frontier applies verbatim, since 65>27. In detail, a nonzero invariant cubic system has gcd one: a positive-degree gcd of degree at most three would give an H-character with nontrivial central character, impossible. Two general members cut a degree-nine surface complete intersection. If the cubic base locus has no surface component, a third member cuts a degree-27 complete-intersection curve containing C, impossible. The reduced union of base surfaces is invariant and of total degree at most nine. The component-orbit argument makes each surface Aproj-stable, and Heisenberg Hilbert-polynomial divisibility makes each surface degree divisible by five. There is exactly one, of degree five, and it is N̄-stable, contradicting item 3. Consequently

    I_C(2)=I_C(3)=0.

For a general hyperplane section Γ, uniform position and the hyperplane ideal sequences give hΓ(1)=4 and hΓ(2)=10.

## 3. Section counts and the genus obstruction to injective Rao multiplication

Twenty-five sections of L², including the fifteen ambient quadrics, would give a basepoint-free birational degree-130 image in P²⁴, with

    g(X) ≤ π(130,24)=300 <326.

Thus h⁰(X,L²)≤20. Since no ambient quadric vanishes, the intermediate space H⁰(C,O_C(2)) has dimension 15 or 20. Accordingly M₂ has dimension zero or five.

Likewise, fifty sections of L³, including the thirty-five ambient cubics, would give a birational degree-195 image in P⁴⁹, with

    g(X) ≤ π(195,49)=296 <326.

Consequently h⁰(X,L³)≤45, and dim M₃∈{0,5,10}.

If M₂=0, or if multiplication by a general linear form ℓ gives an injective map M₂→M₃, the hyperplane ideal sequence, using I_C(2)=I_C(3)=0, gives IΓ(3)=0 and hΓ(3)=20. Uniform-position growth

    hΓ(a+b) ≥ min(65,hΓ(a)+hΓ(b)−1)

then gives, from degrees one through eleven,

    4, 10, 20, 23, 29, 39, 42, 48, 58, 61, 65.

The general non-ACM genus bound gives

    g(X) ≤ p_a(C) ≤ Σ_(n≥1)(65−hΓ(n))
         ≤ 61+55+45+42+36+26+23+17+7+4
         =316,

a contradiction. This bound follows by comparing R_C/ℓR_C with the saturated coordinate ring of Γ and telescoping its Hilbert function; it requires no ACM hypothesis.

It follows that dim M₂=5 and multiplication M₂→M₃ cannot be injective on any nonempty open set of linear forms.

## 4. Abstract odd-multiplicity injectivity lemma

**Lemma.** Every nonzero Ñ-equivariant map

    μ: V*⊗AHM* → AHM⊗W′*

restricts to an injective map μ_x:AHM*→AHM⊗W′* for general x∈V*.

**Proof.** For a nonzero central weight a∈F₅, let U_a denote the five-dimensional H-module with basis e_i, i∈F₅, in which clock and shift act by

    clock(e_i)=ζ^(a i)e_i,      shift(e_i)=e_(i+1).

Its extension to Ñ is unique up to isomorphism: two extensions differ by a character of the perfect group G. In the extension, the central involution ι=−I∈G acts by e_i↦e_−i. Indeed it must be a scalar multiple λ of this inversion because it inverts clock and shift. Its square is one, so λ=±1; its determinant is one because G is perfect. Inversion on five letters has determinant +1, whereas minus inversion has determinant −1. Thus λ=+1.

Take a to be the central weight of V*, so V*=U_a, AHM*=U_(2a), and AHM=U_(3a), since 3a=−2a. Identify the tensor basis e_i⊗f_j with u_k⊗v_t, where

    k=(i+2j)/3,       t=i−j,
    i=k+4t,          j=k+3t                    in F₅.

Clock and shift act only on u_k. The involution acts by (k,t)↦(−k,−t). Therefore its action on the five-dimensional multiplicity space is v_t↦v_−t. Its even and odd parts have dimensions three and two, respectively. By the imported HM identity, these are precisely T* and W′*: the G-central involution acts on those constituents by +1 and −1.

Every nonzero equivariant map in the lemma annihilates the even constituent and is an isomorphism on the odd constituent, by irreducibility and Schur's lemma. Its kernel is therefore exactly the even multiplicity summand. Consequently, writing x=Σ x_i e_i and y=Σ y_j f_j, the equation μ(x⊗y)=0 is equivalent to

    x_(k+4t)y_(k+3t) = x_(k−4t)y_(k−3t)

for k∈F₅ and t=1,2. Equivalently, for every unordered distinct pair {j,l}⊂F₅,

    x_(2j−l)y_j = x_(2l−j)y_l.                 (∗)

Now work over the rational function field F=C(x₀,x₁,x₂,x₃,x₄), with five algebraically independent indeterminates. The equations for pairs {0,1}, {1,2}, and {0,2} say

    x₄y₀=x₂y₁,     x₀y₁=x₃y₂,     x₃y₀=x₄y₂.

Elimination gives

    (x₄²x₀−x₂x₃²)y₀=0.

The coefficient is a nonzero polynomial (its two monomials are distinct), hence a nonzero element of F. Thus y₀=0. Equations (∗) for {0,l} then give y_l=0 for every l≠0, since their coefficients are nonzero indeterminates. The kernel over F is zero. Generic injectivity follows, and its open locus meets the open set of transverse general hyperplanes. This is a formal identity argument; no specialization or rank-instance evaluation has been made. ∎

## 5. Applying the lemma to the actual Rao module

The five-dimensional M₂ has the same H-central character as AHM* and thus is AHM* as an Ñ-module, by the extension uniqueness above. The H-isotypic form of M₃ is AHM⊗E, where E is a G-representation of dimension at most two. Its dimension bound is essential.

The actual graded Rao multiplication is Ñ-equivariant. By

    V*⊗M₂ ≅ AHM⊗(T*⊕W′*),

any nonzero map into M₃ must have image AHM⊗W′*: the irreducible T* has dimension three and cannot map into E. If such a nonzero map exists, E≅W′*, the target has dimension ten, and the map is the unique eligible map up to scalar. Section 4 proves that it is generically injective on the five-dimensional slices. Section 3 excludes this.

Therefore the actual Rao multiplication vanishes identically:

    S₁⊗M₂ → M₃ is zero.

This conclusion does not infer nonvanishing of a particular operation from representation multiplicity. It treats both the zero map and every possible nonzero map, and rules out the latter by a geometric genus bound.

## 6. Quintic extraction and contradiction

For general H, the hyperplane sequence gives

    H⁰(IΓ(3)) = ker(M₂ --ℓ--> M₃) = M₂,

so there are exactly five independent sectional cubics. Apply the audited geometry with d=65:

- Their common gcd is one. A common quadratic or cubic is impossible by dimension. A common linear factor leaves five quadrics through at least 62 points; uniform position with hΓ(2)=10 prohibits even a nonzero quadric through ten of these points.
- Two general cubics form a degree-nine complete-intersection curve. The reduced curve components of the full cubic base locus have total degree at most nine, and its isolated reduced points number at most 27.
- Full S₆₅ sectional monodromy, combined with the action on at most nine base-curve components, has a component-fixing kernel acting transitively on the 65 section points. Since 65>27, some base-curve component contains a section point and therefore contains all 65.
- This reduced integral component D is nondegenerate, quadric-free, and lies on five independent cubics. Laudal's lemma and restriction to a general plane section give deg D≤5; the normalization section count forces deg D≥5. Thus D is quintic. It is unique since total base-curve degree is at most nine.
- As detailed in the independent audit, uniqueness descends the geometric generic component, and the Hilbert scheme supplies a flat family of geometrically integral quintics over an open set of the hyperplane space.
- Chiantini–Ciliberto Theorem 0.2 with (s,h,r,n)=(5,3,4,1) has threshold D=22. Since 65>22, the family lifts to an integral quintic surface containing C. Two such surfaces would have distinct general quintic sections with at least 65 common points, contrary to the intersection bound 25. Hence this surface is unique and N̄-invariant.

This contradicts the imported quintic-surface exclusion. The putative degree-65 curve does not exist.

## 7. Next frontier and stopping boundary

The concrete next step is degree 70. The same section-count strategy changes there: π(140,24)=351, so genus ≥326 no longer forces h⁰(X,L²)≤20. Quadratic Rao dimension ten can enter, and π(210,49)=356 allows h⁰(X,L³)=50 and hence cubic Rao dimension fifteen. On the other hand, π(140,29)=276 and π(210,54)=309 bound the quadratic and cubic section dimensions by 25 and 50, respectively. The degree-65 proof must not be silently extended across those changed bounds. A useful next task is to classify the eligible quadratic and cubic multiplicity modules at degree 70, then analyze their linear multiplication pencils before invoking the same sectional geometry.

An independent audit should particularly check the weight-index transformation and involution sign in Section 4, the passage from generic-field injectivity to general hyperplanes, and the target dimension argument in Section 5.

Only cloud proof files were read or written. No source app, GitHub state, actual source tensor, coefficient instance, selected point, operation matrix, or rank instance was evaluated or changed. All small arithmetic above is displayed explicitly; no large computation was used.
