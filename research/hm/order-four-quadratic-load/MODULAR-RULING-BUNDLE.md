# The modular ruling determinant and the fixed-coordinate polarization correction

## Source and conventions

Primary source: Aure, Decker, Hulek, Popescu, Ranestad, Syzygies of Abelian and Bielliptic Surfaces in P4, arXiv:alg-geom/9606013v2, https://arxiv.org/pdf/alg-geom/9606013 . Read Sections4.4–4.5 and4.14–4.16, together with the definition of the bilinear matrix T immediately preceding Lemma4.14. Repository dictionary: 38c517ed358c08d776b59ab5def5856106dcdeb5.

Let S=S(5) be the smooth modular elliptic surface, with maps to the x-projective space and modular parameter P1_(λ:μ). Write H for the pulled-back x-hyperplane and F for a modular fiber; H=I+2F. All indices below are modulo5. The actual universal elliptic curve equations pulled back to S are

q_i=−λμ x_i²−μ² x_(i+1)x_(i+4)+λ² x_(i+2)x_(i+3)=0.

The following are universal identities in the coordinates and parameters, not selected coefficient or rank tests.

## 1. A canonical rank-two ruling bundle across the cusps

Set p=(0,λ,μ,−μ,−λ). Define the alternating matrix

N_ij=x_(3i+3j) p_(3i−3j).

It is the column-reversed Moore matrix of the source. Its entries are sections of D=O_S(H+F). Its four-by-four Pfaffians vanish on S by the displayed elliptic equations. Thus it has rank at most two everywhere, including points over modular cusps.

It is nowhere zero. If λ≠0, choose a fixed difference i−j with p_(3i−3j)=λ. As j runs through F5, the sum3i+3j runs through every index, so those five entries include λ times every x-coordinate. They cannot all vanish. If μ≠0 the identical argument uses a difference giving μ. At least one of λ,μ is nonzero.

Consequently N has rank exactly two at every point of S. Its image defines a rank-two subbundle K⊂O_S^5. The nonzero decomposable alternating tensor gives

O_S(−H−F) ≅ det K ⊂ Λ²O_S^5.

Put V=K*. In the quotient convention the ruling family is P_S(V), with tautological z-hyperplane ξ, and

**det V=O_S(H+F)=O_S(I+3F).**

There is no uncomputed cusp divisor in this determinant: the alternating tensor was proved nowhere zero on all of S.

## 2. Identification with the z-ruling, rather than an unrelated Moore plane

The source incidence equations, linear in z, are

A_i(z)=λx_i z_i+μ(x_(i+2)z_(i+1)+x_(i+3)z_(i+4)),
B_i(z)=μx_i z_i−λ(x_(i+1)z_(i+3)+x_(i+4)z_(i+2)).

The zeroth column of N is

(0,−μx3,λx1,−λx4,μx2)^t.

Substitution yields

(A_0,A_1,A_2,A_3,A_4)=(0,0,q4,−q1,0),
(B_0,B_1,B_2,B_3,B_4)=(0,q2,0,0,−q3).

The other columns follow by simultaneous cyclic shifts: N_(i+j),j is the zeroth-column expression with x_r replaced by x_(r+j). Hence every image vector of N satisfies all ten incidence equations.

Over the smooth modular locus those equations define a projective line by Lemma4.14. The two-dimensional image K is therefore exactly that ruling plane. P_S(V) is the canonical extension/closure of the smooth ruling incidence across the cusps. This does not assert that the entire unsaturated incidence scheme defined by ten equations has no extra cusp components.

## 3. The fixed w-coordinate map loses two fiber classes

On P_S(V), the three rows t0,t1,t2 of the source matrix T(x,z) are sections of O(ξ+H), component by component. The incidence equations impose

λ t0+μ t2=0,      μ t0−λ t1=0.

The kernel of the resulting rank-two matrix O_S^3→O_S(F)^2 is the line subbundle O_S(−2F), injected by the nowhere-zero column

(λμ, μ², −λ²)^t.

There is therefore a unique global five-component section ŵ with

T(x,z)=(λμ, μ², −λ²)^t ⊗ ŵ,

and each component of ŵ has line-bundle class

**ξ+H−2F=ξ+I.**

Over λμ≠0, the first row t0 differs from ŵ by the common nonzero scalar λμ, so both define the same fixed-coordinate projective w-map. Globally, however, the first-row formulas have fixed divisors over λ=0 and μ=0. One must divide out those two fibers before assigning its polarization. Treating the fixed-w map as having class ξ+H on the compact modular surface is incorrect.

This factorization is global and uses a nowhere-zero Veronese column; it does not arise from a numerical comparison of degrees. If the source morphism Φ_T to P14 is basepoint free on the canonical incidence, then the five components of ŵ are likewise basepoint free, since their simultaneous vanishing is equivalent to simultaneous vanishing of all fifteen components of T. Independently of that basepoint-freeness assertion, the fixed-w formulas are sections of precisely the corrected line bundle ξ+I.

## 4. Fiberwise generation determines the second Chern class

Let f:S→P1 be the modular fibration. The subbundle K⊂O_S^5 is equivariant for the actual Heisenberg action in the z-coordinate representation. Every fiber E, including an I5 cusp fiber, is connected and reduced, with H0(O_E)=C and trivial dualizing sheaf.

Therefore H0(K|E) is an invariant subspace of the five-dimensional irreducible ambient Schrödinger representation. It cannot be the whole space, since K has rank two at every point. Hence H0(K|E)=0. Serre duality on the Gorenstein genus-one fiber gives H1(V|E)=0. Since deg(det V|E)=5, Riemann–Roch gives h0(V|E)=5.

Dualizing the inclusion K⊂O_S^5 gives a surjection O_S^5*→V. On each fiber, its map from the five-dimensional constant representation into H0(V|E) is nonzero and equivariant. Irreducibility of the source makes this map injective, and equality of dimensions makes it an isomorphism. Cohomology and base change therefore give

f_*V=O_P1^5,      R¹f_*V=0,      χ(S,V)=5.

Using χ(O_S)=5, K_S=3F and c1(V)=I+3F, surface Riemann–Roch yields

5=2·5 + [(I+3F)²−(I+3F)·3F]/2 − c2(V)
 =10+(25−15)/2−c2(V).

Thus **c2(V)=10**.

Consequently

ξ³=c1(V)²−c2(V)=15,
(ξ+I)³=25−10+3(I+3F)I+3I²=30.

The corrected fixed-w cube is therefore30. The uncorrected ξ+H cube would instead be120, explaining the apparent degree contradiction. A generic degree or birationality assertion for the map is not inferred merely from this cube.

## 5. Scope

The checked results are the rank-two bundle extension, its determinant and second Chern class, its modular direct images, and the corrected fixed-coordinate polarization. Identifying a general pulled-back quadric with the actual resolved evaluation surface requires a separate proof, including fifty exceptional corrections. No global norm obstruction or primitive twist-three/four exclusion is asserted here.
