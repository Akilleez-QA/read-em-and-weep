# Degree 100 for the resolved Plücker map and the exceptional-beta budget

## Inputs

Over C, let C be the reduced disjoint union of the 25 HM lines in P4, and let the six quintic evaluation minors identify Λ²U with H0(I_C(5)) and generate I_C. Let Y=Bl_C(P4), with exceptional divisor E_exc and H the pullback hyperplane class. The kernel Plücker map has target G=Gr(2,U), the smooth Plücker quadric in P5.

Use the established fixed-beta surface degree dichotomy and the proof KAPPA-RATIONAL-SEXTIC.md: the rank-zero parameter image Γ⊂P(U*) is a smooth rational sextic, and C→Γ is the disjoint union of 25 isomorphisms. This note does not reproduce that separate equivariance/genus-bound proof.

## 1. The resolved Plücker map has generic degree 100

Since the minors generate I_C, their pullbacks generate the line bundle L=O_Y(5H−E_exc). They define a morphism F:Y→P5 extending the kernel Plücker map. Its image lies in G because the Plücker quadratic relation holds on the dense complement of E_exc and Y is integral. Thus F:Y→G and F*O_G(1)=L.

For the blowup of the smooth codimension-three center C, the exceptional pushforwards are

π_*(E_exc)=π_*(E_exc²)=0,
π_*(E_exc³)=[C],
π_*(E_exc⁴)=i_*c1(N_{C/P4}).

Here each component line has N=O(1)^3, so deg C=25 and deg c1(N)=75. The last sign can also be checked on E_exc=P(N) with the lines convention: O_Y(E_exc)|E_exc=O_P(N)(−1), and pushforward of ξ³ is −c1(N), where ξ=c1(O_P(N)(1)). Therefore

L⁴=625−20·25+75=200.

A globally generated line bundle with nonzero fourth self-intersection has four-dimensional image. Since G is integral of dimension four, F is surjective and generically finite. The Plücker degree of G is two, so

deg(F)·2=L⁴=200,
**deg(F)=100.**

An independent sign check works directly on each exceptional divisor: E_i=P(N_L)=P1×P2, O_Y(E_i)|E_i=O_P1(1)⊠O_P2(−1), and H|E_i=h. With ξ the P2 hyperplane class, H E_i³=∫h(h−ξ)²=1 and E_i⁴=∫(h−ξ)³=3. The lower mixed terms vanish. Summing over 25 disjoint components recovers 25 and 75, and hence 200.

This argument uses intersection numbers, not numerical evaluations of HM matrices.

## 2. Exceptional projective planes over a parameter B in Γ

Fix B∈Γ and let β_B={K∈G:K⊂B}, a projective plane. At a point p∈C, locally a unit entry reduces the full evaluation matrix to

[1 0 0 0; 0 x y z],

where (x,y,z) generates I_C. On the exceptional fiber P(N_p)=P², a normal direction [x:y:z] determines the corresponding two-dimensional kernel in the three-space κ(p). Hence F maps this exceptional fiber isomorphically onto β_κ(p). The row/column trivializations are used locally to prove this intrinsic statement, not to identify varying target bases globally.

Exactly 25 points p∈C satisfy κ(p)=B, one on each component. They give 25 projective-plane surface components in F^−1(β_B), each mapping isomorphically onto β_B. For every other p, β_B∩β_κ(p) is the single point K=B∩κ(p). These remaining exceptional intersections vary over C and contribute only curves, not additional surface components.

Outside E_exc, the scheme F^−1(β_B) is exactly X_B minus C, because K_x⊂B is equivalent to rank(B→E_x)≤1. It has dimension two. Thus F^−1(β_B) has dimension two everywhere as a closed set: its surface components are the strict transforms of components of X_B, together with the 25 exceptional planes.

Since β_B is a regular codimension-two embedding in the smooth fourfold G, its pullback is locally cut by two equations. In the regular fourfold Y these equations have height two and form a regular sequence. Therefore the scheme-theoretic inverse image is the expected intersection cycle, without an excess component of larger dimension.

## 3. The exact degree budget, with multiplicities retained

Write m for the generic scheme multiplicity along one exceptional plane. All 25 multiplicities agree by the Heisenberg action: the group acts transitively on the component lines, acts trivially on U, fixes B, and acts equivariantly on the blowup and F.

Let Z_j be the nonexceptional surface components of F^−1(β_B), let n_j be their scheme multiplicities, and let δ_j be the generic degree of Z_j→β_B when dominant; put δ_j=0 when its image has dimension less than two.

Proper pushforward and compatibility of refined pullback with proper pushforward give

F_*[F^−1(β_B)] = 100[β_B].

Equivalently, intersecting over a general point of β_B with multiplicities retained gives the exact identity

**25m + Σ_j n_j δ_j = 100.**

In particular

1≤m≤4,
Σ_j n_j δ_j = 100−25m ∈ {75,50,25,0}.

For the established residual-beta component alternatives, all generic component multiplicities of X_B are one, so n_j=1 for their strict transforms. Retaining n_j in the formula avoids needing that extra input in the general statement.

If even one nonexceptional component dominates β_B, then m≤3. Conversely, m=4 forces every nonexceptional component to have image of dimension at most one. If m≤3, at least one nonexceptional component dominates, but this alone does not identify it with the sextic-containing component when X_B is reducible.

## 4. Exact first-jet criterion for m=1

For precision, return to a fixed original basis of U in which B is the kernel at p. Local row operations can put evaluation into the form [1,b;0,a], with a=(a1,a2,a3) defining C and b vanishing at p. Let t be a parameter on C at p. On a blowup chart put a=s n, where n is the generic exceptional direction. To first order in the normal coordinates (t,s) to the exceptional plane, write

b=t v+s M n+O((t,s)²).

Here v is nonzero because κ restricts to an immersion on C. The condition K⊂B becomes b proportional to n, or equivalently pr_n(b)=0 in C³/<n>. Its normal linearization has columns pr_n(v) and pr_n(Mn). Thus

m=1 if and only if det[n,v,Mn] is not identically zero as a function of n.

Indeed the local ring of Y at the generic point of the exceptional plane is regular of dimension two. The two pulled-back beta equations define a finite-length quotient there. Its length is one exactly when their linear terms generate the maximal ideal, equivalently the displayed two columns are independent. This provides the equivalence, not merely a sufficient test.

If det[n,v,Mn] vanishes identically, then m≥2 and the nonexceptional degree budget is at most 50. Nothing here evaluates that determinant for the actual HM bundle or assumes its nonvanishing.

## Boundary and next dependency

The universally checked new result is the degree-100 resolved Plücker map and, over Γ, the four-valued budget 75/50/25/0 after accounting for the exceptional planes with their true multiplicities. The count 25 of exceptional planes does not justify subtracting exactly 25: their scheme multiplicity must first be established.

In particular this argument does not yet prove that the sextic-containing S maps dominantly to β_B. Such dominance would allow the plane-quotient normal-defect upper-bound argument on its general moving sextics; absent dominance, that extension is not claimed. The precise remaining dependency is the actual exceptional multiplicity and, in the reducible case, which nonexceptional component carries the remaining degree.

No source-coefficient evaluation, selected matrix rank, scan, restarted local-model spike, or consumed one-shot experiment was used. No external writes were made.

Intersection-theory reference: the proper projection formula for Gysin/intersection products used in Section 3 is Stacks Project, Lemma 42.62.4 (tag 0FFC), https://stacks.math.columbia.edu/tag/0FFC . Both Y and G are smooth proper varieties, as required there. The expected-codimension regular-sequence check identifies the pullback class with the actual inverse-image fundamental cycle in this application.
