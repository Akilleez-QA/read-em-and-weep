# Degree 70: smooth étale candidates, two genera, and quadratic multiplicity exclusion

## Result

Work over C with the standard projective Schrödinger normalizer N=A⋊G, A=F₅², G=SL₂(F₅), |N|=3000. Import the established exclusions of invariant integral curves through degree55 and invariant integral quintic surfaces, and the point-orbit and sectional geometry results cited below.

Every N-invariant reduced curve C⊂P⁴ of total degree70 without line or conic components is integral and smooth. The action of A on C is free. Its genus and quotient genus satisfy

    (g(C),g(C/A)) ∈ {(326,14),(351,15)}.

Put M_n=H¹(P⁴,I_C(n)). Then

    h⁰(C,O_C(1))=5,   M₁=0,   I_C(2)=I_C(3)=0;
    dim M₂∈{0,5,10},   dim M₃∈{0,5,10,15}.

For a general hyperplane section Γ, let k=dim ker(M₂ --ℓ--> M₃). Necessarily k≤4, and hΓ(3)=20−k. More precisely:

- If dim M₂≤5, then k=0, hΓ(3)=20 and g(C)≤369.
- If dim M₂=10, write M₂=U₂⊗E under the Heisenberg isotypic equivalence, with dim U₂=5 and dim E=2. Then E is nontrivial irreducible; E=1⊕1 is impossible. The generic Rao slice has rank≥6, so dim M₃≥10 and hΓ(3)≥16.

These are necessary conditions, not an exclusion or existence theorem for degree70. The theorem addresses total reduced degree70 before proving integrality. It does not classify degree70 components of a larger reducible curve. It does not depend on the degree65 exclusion.

## 1. Explicit dependencies

1. The component-orbit and degree-divisibility facts, and the integral exclusion through degree55: ../rank-four-degree-sixty-lower-bound/PROOF.md and its stated dependencies. An A-stable component has degree divisible by5. An A-stable integral component of degree5 or10 has N-orbit size≥20. The faithful N-action on normalization forces genus≥326.
2. Cubic exclusion and uniform-position genus method: ../degree-sixty-curve-frontier/PROOF.md, §§1–3. The cubic argument applies whenever degree>27; it is reproduced in abbreviated form below.
3. Point-orbit gap: ../normalizer-refined-point-gap/PROOF.md. The unique30-point orbit E₃₀ consists of Heisenberg eigenpoints; every other point orbit has size≥250. ../normalizer-minimal-point-orbit/PROOF.md also proves that E₃₀ is exactly the locus of nontrivial projective A-stabilizers.
4. The audited extraction and lifting of an integral quintic from five sectional cubics: ../quadratic-deficiency-exclusion/PROOF.md and INDEPENDENT_GEOMETRY_AUDIT.md. The argument depends on degree inequalities d>27, d>22 and d>25, not on d=60 or the dimension of M₂ as such.
5. The HM identity and the odd multiplicity injectivity lemma: ../cubic-massey-module-reduction/PROOF.md, §3; ../degree-sixty-five-pencil-exclusion/PROOF.md, §4. Only that abstract lemma is imported, not its degree65 exclusion. Below, the elementary even counterpart is also proved.

## 2. Integrality, initial section bounds, and p_a≤507

A component A-orbit of size25 would cost at least75 degrees. An orbit of size5 has an axis stabilizer whose six conjugates force at least30 components, costing at least90. Thus all components are A-stable and have degrees divisible by5. A nonsingleton G-orbit has size≥5, hence its common degree is≤14 and therefore5 or10. Its N-orbit must instead have size≥20 by dependency1, costing≥100. Every component is consequently N-stable. Each has degree≥60, so total degree70 forces exactly one component.

The integral curve spans P⁴ and N acts faithfully on its smooth normalization ν:X→C. Hence g(X)≥326. Set L=ν*O_C(1). If h⁰(X,L)≥10, ten sections containing the ambient five give a basepoint-free birational degree70 series in P⁹. Castelnuovo gives π(70,9)=264<326 (69=8·8+5). Heisenberg central-character divisibility makes h⁰(X,L) a multiple of5, so h⁰(X,L)=5. It follows that h⁰(C,O_C(1))=5 and M₁=0.

A nonzero invariant cubic system has gcd1: a positive-degree gcd of degree≤3 would span an H-character line, impossible since its central character is nontrivial. Two cubics then cut a degree9 complete-intersection surface. If its cubic base locus had no surface, a third cubic would cut a degree27 curve containing C. Otherwise the reduced invariant surface union has total degree≤9. The A-component orbit argument and Heisenberg degree divisibility leave exactly one integral quintic surface, necessarily invariant, contrary to dependency1. Thus I_C(3)=I_C(2)=0.

For a general hyperplane section Γ, the restriction sequences give hΓ(1)=4 and hΓ(2)=10. Uniform position gives

    hΓ(a+b) ≥ min(70,hΓ(a)+hΓ(b)−1).

Successive lower bounds through saturation are

    4,10,13,19,22,28,31,37,40,46,49,55,58,64,67,70.

The general, non-ACM genus inequality yields

    p_a(C) ≤ Σ_{n≥1}(70−hΓ(n))
           ≤66+60+57+51+48+42+39+33+30+24+21+15+12+6+3
           =507.

Therefore the normalization defect δ=p_a(C)−g(X) satisfies 0≤δ≤181.

## 3. Smoothness without a rank-four-specific hypothesis

The singular locus of an integral curve is finite and N-invariant. Any singular orbit outside E₃₀ would contain≥250 points, each with δ_p≥1, contradicting δ≤181. We now rule out E₃₀ as well.

Every cyclic subgroup of N has order≤10. To check this directly, write an affine element as (a,s), with a∈F₅² and s∈SL₂(F₅). If s has no eigenvalue1, conjugation by a translation removes a, so the element has the order of s, at most10. If s has eigenvalue1, it is identity or unipotent. For s=I+J with J²=0,

    (a,s)^5 = ((I+s+s²+s³+s⁴)a,I) = (0,I),

because Σ_{i=0}⁴(I+iJ)=5I+10J=0 in F₅. The identity case is included. This exhausts the possibilities. The possible nontrivial orders in G are2,3,4,5,6,10, as proved in ../binary-group-genus-thirteen/PROOF.md, §1.

The faithful finite N-action on the smooth normalization has cyclic point stabilizers, by its faithful tangent representation. For p∈E₃₀, |N_p|=100. Every x∈ν⁻¹(p) has stabilizer N_x⊂N_p of order≤10. Its N_p-orbit inside ν⁻¹(p) therefore has at least10 elements. Thus C has at least10 branches at p and δ_p≥9. The last inequality follows from the residue map from the normalization local algebra to C^r modulo the diagonal constants, of dimension r−1.

If any point of E₃₀ were singular, the whole orbit would be, and δ≥30·9=270, again impossible. Thus C is smooth.

Moreover C cannot contain any point of E₃₀, since a smooth curve point has cyclic stabilizer of order≤10, whereas N_p there has order100. Since precisely E₃₀ has nontrivial A-stabilizers, A acts freely on C. Riemann–Hurwitz gives

    g(C)=25q−24,   q=g(C/A)≥14.

The initial upper bound507 therefore gives q∈{14,…,21}.

## 4. Five sectional cubics are impossible

For general Γ, we claim dim IΓ(3)≤4. Suppose instead there are at least five independent cubics through Γ. Their common gcd is1: a common quadratic or cubic leaves at most four or one independent cubics; a common linear factor leaves quadrics through at least67 of the points, impossible by uniform position and hΓ(2)=10.

Two general cubics cut a degree9 complete-intersection curve. The curve components of the full cubic base locus have total degree≤9, and its isolated reduced points number≤27. Full S₇₀ sectional monodromy, acting also on the at most9 base-curve components, forces the component-fixing kernel to act transitively on Γ. Since70>27, a reduced integral component D contains all70 points. This is exactly the component-labeling argument of dependency4, unchanged when the cubic system has more than five members.

D has no quadric and lies on at least five cubics. Laudal's lemma and restriction to a general plane section, as in dependency4, imply deg D≤5; degree≤4 would force a quadric by h⁰(O_D(2))≤2deg D+1. Hence D is quintic. It is unique because total base-curve degree≤9. Its canonical family lifts to an integral quintic surface by the cited Chiantini–Ciliberto theorem, since70>22. Uniqueness follows from70>25, so the surface is invariant, a contradiction.

The hyperplane restriction sequence, since I_C(2)=I_C(3)=0, identifies

    IΓ(3) = ker(M₂ --ℓ--> M₃).

Thus k≤4 and hΓ(3)=20−k≥16. This already improves the arithmetic genus bound to456 via the sequence

    4,10,16,19,25,31,34,40,46,49,55,61,64,70.

## 5. Two genera and the enlarged Rao spaces

The section series remain birational because they contain ambient Veronese sections. Castelnuovo and central-character divisibility give

    h⁰(C,O_C(2))≤25,   since π(140,29)=276<326;
    h⁰(C,O_C(3))≤50,   since π(210,54)=309<326.

Thus dim M₂ is0,5 or10, and dim M₃ is0,5,10 or15.

Suppose g(C)≥376, the next allowed free-A genus after351. Then

    π(140,24)=351<376,   π(210,49)=356<376

force h⁰(O_C(2))≤20 and h⁰(O_C(3))≤45, hence dim M₂≤5 and dim M₃≤10. If M₂=0, then k=0. If dim M₂=5, write M₂=U₂ (the unique five-dimensional normalizer extension of the relevant Heisenberg module). The HM identity is

    S₁⊗U₂ = U₃⊗(T*⊕W′*),

where dim T=3, dim W′=2, and these are irreducible. Since dim M₃≤10, a nonzero multiplication has image U₃⊗W′*. The odd-multiplicity lemma in dependency5 says its general slice is injective. Zero multiplication would give k=5, excluded by §4. Therefore k=0 in all cases.

If hΓ(3)=20, uniform-position growth gives

    4,10,20,23,29,39,42,48,58,61,67,70,

and p_a(C)≤66+60+50+47+41+31+28+22+12+9+3=369. This contradicts g(C)≥376. We conclude g(C) is326 or351, and q is14 or15.

## 6. More precise quadratic Rao alternatives

The H-isotypic equivalence gives M₂=U₂⊗E and M₃=U₃⊗F, where dim E≤2 and dim F≤3; multiplication corresponds to a G-map

    (T*⊕W′*)⊗E → F.

If dim E=1, perfection gives E=1. Zero multiplication is excluded by §4. A nonzero map can have only the T* image or only the W′* image, since dim F≤3 cannot contain both. The odd image has generically injective slices by dependency5. The even image also has generically injective slices: in the abstract weight coordinates of that lemma the T* projection is the even part under t↦−t. If an elementary tensor x⊗y projects to zero, its t=0 coefficients give x_k y_k=0 for each k. Over C(x₀,…,x₄), all x_k are units, so y=0. Thus k=0 whenever dim M₂=5, proving the sharper assertion in the Result.

If dim E=2 and E is reducible, perfection and semisimplicity imply E=1⊕1. The source multiplicity is then T*⊕T*⊕W′*⊕W′*. As dim F≤3, the image can contain at most one copy of T* or at most one copy of W′*, and cannot contain both. In either nonzero case the G-map factors as the selected projection on T*⊕W′* tensored with one linear functional on E. Consequently each Rao slice M₂→M₃ factors through a five-dimensional space and has rank≤5, so k≥5. The zero map is worse. This contradicts §4. Hence E is irreducible nontrivial. Generic rank≥6 forces dim M₃≥10. No stronger assertion about which irreducible E occurs, actual multiplication nonvanishing in a designated channel, or actual curve existence is made.

## 7. Verification boundary

Only proof files were read and written. The elementary sums and Castelnuovo divisions are numerical checks of universal bounds; no actual source tensor, source coefficient, selected point, problem-specific matrix, operation value or rank instance was evaluated. No actual source-instance evaluation is claimed. The new smoothness argument and the use of at least five rather than exactly five sectional cubics are especially suitable for independent checking.
