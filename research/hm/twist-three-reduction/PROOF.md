# Twist three: one irreducible fifteen-dimensional obstruction

## New result and precise boundary

Let F be the normalized Horrocks–Mumford bundle on complex P4, and B=End_0(F). Then

    H^0 B(3) = 0 or V_1 ⊗ χ_3,
    h^0 B(3) ∈ {0,15},
    (h^0 B(3),h^1 B(3)) ∈ {(0,100),(15,115)},
    H^i B(3)=0 for i≥2.

Here N, V_1, W=χ_2, W′=χ_2′ and χ_3=Sym²W use the explicit conventions and primary-source derivation in [INPUTS.md](INPUTS.md). The vanishing prerequisite is [twist two](../twist-two-vanishing/PROOF.md). In particular V_1 has dimension five and central character ζ². The fifteen-dimensional alternative is irreducible for N. Its fate is decided by a single d_2 differential restricted to that irreducible block: the map is either zero or injective. No selected matrix, source, polynomial, cofactor or pairing instance is evaluated. The theorem does not decide between these alternatives.

## 1. Imported inputs and source check

The primary section resolution, equivariantly refined, is

    0 → A O(-8) → D O(-6) → G O(-5)
      → P O(-4) ⊕ C O(-3) → F → 0,

with dimensions (A,D,G,P,C)=(2,20,35,15,4). [INPUTS.md](INPUTS.md) derives A=W′ and C=χ_4 directly from the primary cohomology calculation and the resolution twisted by three. The cohomology inputs are H¹F=V_3, H¹F(1)=V_1⊗W′, H²F(-2)=W, H⁰F(t)=0 for t<3, and H¹F(t) supported at t=0,1,2,3 with dimensions 5,10,10,2. Also F*=F(1), H³F(t)=H¹F(-t-4)*, and H⁴F(t)=H⁰F(-t-4)*.

Sources freshly reopened 2026-10-20:

- Decker, Monads and cohomology modules of rank 2 vector bundles, Compositio 76 (1990), printed pp.14–16: https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf
- Horrocks–Mumford, A rank 2 vector bundle on P4 with 15,000 symmetries, Topology 12 (1973), Lemma3.3, §4, and Appendix printed p.81: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

The latter Appendix gives the finite character table. Its character rows give directly

    W′⊗χ_3′ = W′ ⊕ χ_4#,
    W⊗χ_4# = χ_3 ⊕ χ_5.

For example at the two order-five unipotent classes, W has values η,η′; W′ has η′,η; χ_4# has -1,-1; χ_3 has -η,-η′; χ_5 has 0,0. The remaining seven columns also agree. χ_4# is the spinorial four-space, distinct from C=χ_4. Lemma3.3(v),(vi), dualizing (vi), gives

    Sym²V=V_1⊗χ_3′,
    S_3=Sym³V*=V_1⊗(χ_5⊕W′).

All coefficient spaces can be chosen equivariantly because N is finite over C. Finite-dimensional N-modules are semisimple. The H5-isotypic equivalence (HM §2) proves that V_1⊗χ_3 is irreducible, not merely dimension fifteen.

## 2. Identify the twenty-dimensional coefficient, not just its dimension

Twist the section resolution by one. Only the following line-bundle cohomology entries survive:

    A⊗H⁴O(-7)=W′⊗Sym²V in column -3,
    D⊗H⁴O(-5)=D in column -2.

The equality H⁴O(-7)=Sym²V is equivariant Serre duality, since N⊂SL(V). The other twists are -4,-3,-2 and are acyclic. The cohomology of this two-term vector-space complex is H¹F(1) in its kernel and H²F(1)=0 in its cokernel. Therefore

    0 → V_1⊗W′ → W′⊗Sym²V → D → 0.

Substitute Sym²V=V_1⊗χ_3′ and the first character identity above. Semisimplicity gives

    D = V_1⊗χ_4#.

This identification follows from a cohomology exact sequence, not from an arbitrary labeling of a twenty-space.

## 3. Twist-three spectral sequence

Tensor the section resolution by F*(3)=F(4). Its terms in columns -3,-2,-1,0 are

    W′⊗F(-4), D⊗F(-2), G⊗F(-1),
    P⊗F ⊕ χ_4⊗F(1).

Exactly three E_1 entries are nonzero:

    U=E_1^(-3,3)=W′⊗V_3*=V_1⊗W′, dimension10;
    T=E_1^(-2,2)=D⊗W=V_1⊗(χ_3⊕χ_5), dimension40;
    Q=E_1^(0,1)=P⊗V_3 ⊕ χ_4⊗(V_1⊗W′), dimension115.

All H⁰ entries vanish; all omitted H²,H³,H⁴ entries vanish by the imported table and duality. Every d_1 vanishes. The only possibly nonzero differentials are

    d_2:T→Q,
    d_3:U→coker(d_2).

The first two entries have total degree zero, the last total degree one. Hence H⁰End(F)(3) has associated graded subrepresentations of U and T; no assertion of an unjustified canonical embedding into their direct sum is needed. Semisimplicity identifies its representation class with the sum of its graded pieces.

## 4. Scalars force the two permanent pieces

Trace splits H⁰End(F)(3)=S_3 ⊕ H⁰B(3), equivariantly. Since S_3=V_1⊗(χ_5⊕W′), its thirty-five dimensions must survive in the associated graded. U contains exactly its ten-dimensional V_1⊗W′ type; T contains exactly its twenty-five-dimensional V_1⊗χ_5 type. These two irreducible types have no other occurrence in U⊕T.

Consequently all of U survives: d_3=0. The restriction of d_2 to V_1⊗χ_5 is zero. Write

    δ_3 : V_1⊗χ_3 → Q

for the remaining restriction. Then

    H⁰B(3) ≅ ker δ_3.

No higher differential exists in this column range. By irreducibility the kernel is zero or the entire fifteen-space. Thus δ_3 is either injective or zero, proving the theorem's dichotomy. This reasoning does not require identifying P or the multiplicity of the domain type in Q, and does not assert that δ_3 is a scalar.

## 5. Exact companion cohomology

The E_1 page has only total degrees zero and one. Therefore H^iEnd(F)(3)=0 for i≥2. Its Euler characteristic is 10+40-115=-65. Subtract χO(3)=35 to obtain χB(3)=-100. Hence h¹B(3)=100+h⁰B(3), with the claimed two possibilities.

## 6. New geometric restriction under the nonzero alternative

This section uses the proved input H⁰B(2)=0. Let e:H⁰B(3)⊗O→B(3) and let I be the saturated image of generic rank r. If r<3, write det I=O(a). Wedges of generating sections imply a≥0. Equivariance and central character ζ² of B(3) imply a≡3r mod5. The determinant inclusion extends over codimension two into Λ^rB(3).

For r=1 this gives H⁰B(3-a)≠0, hence a≤0, contradicting a≡3 mod5. Thus r≠1.

For r=2, Λ²B(3)=B(6), so H⁰B(6-a)≠0 forces a≤3. The congruence a≡1 mod5 forces exactly a=1. We now exclude this last rank-two case, using a linear Plücker argument rather than treating the congruence as sufficient.

Dualizing evaluation on the dense locally free, full-rank locus gives a family of two-planes J_x⊂T_0*, where T_0=H⁰B(3) has dimension15. Its Plücker coordinates are the global sections of det I=O(1) induced by Λ²T_0→det I. Thus the rational Plücker map is given by linear forms. Its image closure is a projective linear space P^s, with 0≤s≤4, wholly contained in Gr(2,T_0*) by closedness.

For completeness, a projective linear P^s of decomposable two-vectors represents two-planes whose total span has dimension at most2+s when s≥1, and dimension2 when s=0. Indeed any two represented planes meet in a line, since the sum of their bivectors is decomposable only then. Fix two distinct planes A,B with common line L and three-dimensional span H. Any third plane either contains L or lies in H. If a plane containing L leaves H, every other plane must contain L, since otherwise its intersection with that plane would be zero. The family is therefore a star of planes containing L, or lies entirely in H. In the star case the residual lines span dimension s+1, so total span is s+2; in the second case total span is at most3. This proves the bound.

It follows that all J_x span at most six dimensions. But an element of T_0 annihilating all J_x is a global section whose evaluation vanishes on a dense open subset. A section of the vector bundle B(3) vanishing densely is identically zero. Thus the J_x span all fifteen dimensions of T_0*, a contradiction. Generic evaluation therefore has rank THREE. No assertion about local freeness of I everywhere or absence of base points of the rational map was needed.

Since r=3, the divisorial evaluation defect is N-invariant and has degree at most9, from the maximal minors in O(9). Characters of N are trivial, so the center forces its degree to be a multiple of5. The only positive possibility is5, excluded by S_5^N=0 (HM Theorem3.5). Thus the cokernel T_e has codimension≥2 support, and the kernel K is reflexive of rank12 with

    c1(K)=-9H,  ch2(K)=(3/2+t)H²,
    Δ(K)=45-24t,

where ch2(T_e)=tH² and t is a nonnegative integer. There is an additional unconditional arithmetic restriction: 5 divides t. Indeed T_e is N-equivariant with scalar center ζ², so H^i(T_e(m)) has central character ζ^(2-m). For m not congruent to2 modulo5, every H5-irreducible constituent has dimension5; therefore χ(T_e(m)) is divisible by5. Since T_e has dimension at most2, its integer-valued Hilbert polynomial has the form

    P(m)=t binom(m,2)+a m+b,  a,b∈Z.

This follows from the integer finite-difference basis, with leading coefficient t/2. Reduction modulo5 is a polynomial of degree at most2, because2 is invertible modulo5. It vanishes at four residue classes, hence is identically zero. Its quadratic coefficient yields t≡0 modulo5. Consequently

    t∈{0,5,10,15,...}.

The discriminant identity does NOT prove semistability. Conditional on semistability of K, Bogomolov gives 45-24t≥0 and hence t≤1; the new divisibility then forces t=0. Equivalently any nonzero codimension-two defect forces K to be unstable. This conditional implication is a precise next target, not a proof of K's semistability or twist-three vanishing.

## Scope

This is new progress beyond the twist-two vanishing and prior general singular-spectral constraints: it reduces twist three to a single irreducible d_2 block and proves generic full-rank evaluation without divisorial defect in the nonzero alternative. It neither proves twist-three vanishing nor determines actual source membership, pairing values, cofactor rank, collision order, or any physical obstruction. No selected instance was evaluated and no external service was changed.
