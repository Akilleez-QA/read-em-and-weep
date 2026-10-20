# Geometry of the two candidate jump normal rings

## Scope and result

This is universal commutative algebra over C. No assertion that an actual HM deformation hull is isomorphic to these rings is made here. The files `../jump-obstruction-pairing/PROOF.md` and `../heisenberg-vertex-obstructions/PROOF.md` establish their quadratic initial equations in the stated generic transverse/surjective cases, but quadratic initial equations alone do not identify a completed local ring. The geometric conclusions below apply to actual hulls only after a separate all-orders identification.

Put T=C[[t1,...,t24]], a=t1, b=t2, c=t3, d=ac-b². Define

    R1=T[[z]]/(z²,az),
    R2=T[[z1,z2]]/((z1,z2)²,az1+bz2,bz1+cz2).

Both rings have dimension 24, smooth reduced ring T, generic multiplicity one, depth 23, and one embedded associated prime. They are therefore non-Cohen–Macaulay despite having a smooth irreducible reduced germ and multiplicity one. Their nilradicals have square zero and live only on a divisor of the reduced germ. The first divisor is smooth; the second is the irreducible quadric d=0. In the second case the nilradical is rank-one maximal Cohen–Macaulay over that quadric, locally free away from its singular vertex, and needs two generators along the vertex.

## 1. Split square-zero descriptions

Every power series modulo the squares of the normal-variable ideal has a unique expression of degree at most one in normal variables before imposing the displayed linear relations. Hence

    R_i = T ⊕ J_i,
    (f,u)(g,v)=(fg,fv+gu),
    J1=T/(a),
    J2=coker(M:T²→T²),   M=[[a,b],[b,c]].

Here z, or z1,z2, give the generators of J. These are isomorphisms of augmented T-algebras, not merely vector-space splittings. T injects, and augmentation is the quotient by J. Because T is reduced and J²=0, J is exactly the nilradical; R_i,red=T. Prime ideals correspond bijectively to those of T, by p↦p⊕J.

Since det M=d≠0 in the domain T, M is injective (multiply by its adjugate). Thus J2 has the exact free resolution

    0→T² --M→ T²→J2→0.                          (1)

The adjugate identity also gives dJ2=0.

## 2. The quadric module is a divisor ideal

The power series d is irreducible and A=T/(d) is a domain: C[[a,b,c]]/(ac-b²) is the degree-two invariant subring C[[u,v]]^{±1}, via a=u²,b=uv,c=v²; adjoining the other 21 formal variables preserves this description and the domain property. The invariant description follows by grouping even-total-degree monomials, with the sole relation ac=b².

Define J2→A by z1↦b, z2↦−a. Its image is the ideal (a,b)⊂A. Both relations vanish. To check injectivity, suppose (x,y)∈T² maps to zero, so bx−ay=kd for some k∈T. Then

    b(x+kb)=a(y+kc).

The relatively prime prime elements a,b in the regular power series ring give x+kb=aℓ and y+kc=bℓ. Consequently

    (x,y)=(aℓ−kb,bℓ−kc)=M(ℓ,−k).

This is exactly the image in (1). Therefore

    J2 ≅ (a,b) as an A-module.                    (2)

In particular it is nonzero torsion-free of rank one over A, and Ann_T(J2)=(d). This statement also verifies that no hidden torsion supported at the vertex occurs.

The invariants of the nilradicals as T-modules are:

| Module | Annihilator | Support | Associated primes | Fitt_0 | Fitt_1 | Fitt_2 |
|---|---|---|---|---|---|---|
| J1 | (a) | V(a) | {(a)} | (a) | T | T |
| J2 | (d) | V(d) | {(d)} | (d) | (a,b,c) | T |

Fitting ideals follow directly from the presentations, and associated primes follow from torsion-freeness over the respective domain T/(a) or T/(d). Over A, Fitt_0(J2)=0 and Fitt_1(J2)=(a,b,c)A. Its nonfree locus is exactly V(a,b,c): if some matrix entry is a unit in T_p, elementary row/column operations reduce M to diag(1,unit·d), making J2,p free of rank one over A_p. If a,b,c all belong to p, the presentation modulo the residue field has zero matrix, so J2 needs two generators and is not rank-one free.

Auslander–Buchsbaum applied to (1) gives depth_T J2=23, since its projective dimension is one (it is nonzero torsion and hence not T-free). Depth as an A-module is also 23, so J2 is maximal Cohen–Macaulay. The same localized calculation proves the MCM property at every point of its support. A is normal: it is a hypersurface, hence S2, and its Jacobian ideal (a,b,c) has codimension two in A, hence A is regular in codimension one. A torsion-free MCM module on this normal ring satisfies S2 and is reflexive. Thus J2 is a rank-one reflexive module which is not a line bundle at the vertex. No choice of a global generator can trivialize this nilpotent thickening there.

## 3. Associated primes and explicit primary decompositions

Write S_i for the regular power series ring before quotient, I_i for the defining ideal, and Z_i for the ideal of its normal variables. Let f1=a and f2=d. Then

    I_i = Z_i ∩ (I_i+(f_i)).                       (3)

Indeed I_i⊂Z_i and f_i Z_i⊂I_i by the annihilator calculation. If an element of I_i+(f_i) lies in Z_i, write it as h+f_i g with h∈I_i. Its image in S_i/Z_i=T implies f_i gbar=0. As T is a domain and f_i≠0, g∈Z_i, proving (3).

Z_i is prime. The second component Q_i=I_i+(f_i) is P_i=(f_i,Z_i)-primary. Its quotient is

    S_i/Q_i = (T/(f_i)) ⊕ J_i.

The base is a domain and J_i is torsion-free over that base. Any element with nonzero base part is a nonzerodivisor: multiplying it by (g,v) to zero first forces g=0, then forces v=0. An element with zero base part is nilpotent. Thus every zerodivisor in this quotient is nilpotent, the criterion for Q_i to be primary. Neither component in (3) is redundant: f_i belongs to Q_i but not Z_i; the normal variables are not all in Q_i because J_i≠0. Therefore the associated primes of R_i are exactly

    minimal: J_i,
    embedded: (f_i)⊕J_i.

Alternatively these associated primes follow directly from the idealization module. An element (0,u) with u≠0 has annihilator (f_i)⊕J_i, since J_i is torsion-free over T/(f_i). The element (f_i,0) has annihilator J_i. The primary decomposition excludes any other associated prime, in particular any additional one at the quadric vertex.

## 4. Local nilpotent geometry and the multiplicity distinction

The support of J is exactly the nonreduced locus of R. Outside V(f_i), the ring is simply the smooth reduced ring T locally. Along V(f_i), its nilradical remains nonzero; the topological space still has only the single underlying smooth component Spec T.

For the finite morphism Spec R_i→Spec T, the fiber over p is the square-zero algebra

    κ(p) ⊕ (J_i⊗_T κ(p)).

For R1 its length is one off V(a), two on V(a). For R2 its length is one off V(d), two on V(d)\V(a,b,c), and three on V(a,b,c). This last fiber has square-zero two-dimensional maximal ideal. These fiber lengths must not be confused with the generic multiplicity of the entire 24-dimensional ring, which is one, or with the dimension of the local ring at the embedded prime, which is one.

At the embedded prime p=(f_i), T_p is a DVR, and J_i,p is one copy of its residue field. Thus

    R_i,p ≅ T_p ⊕ κ(p)

as a square-zero idealization; choosing a uniformizer π and nilpotent generator ε, this is T_p[ε]/(ε²,πε). It is a one-dimensional ring with an embedded closed-point nilpotent, not a doubled irreducible component. Its quotient by π has length two. Along the singular vertex of the quadric, R2 has two infinitesimal normal generators, but still no new irreducible or associated component there.

### Compatibility of vertex and rank-one normal rings

At any p in V(d) outside V(a,b,c), at least one of a,c is a unit: if b is a unit then ac=b² modulo p forces both to be units. Suppose a is a unit. Eliminate z1 using z1=−(b/a)z2. The second relation becomes (d/a)z2=0, and the square-zero relations reduce to z2²=0. Consequently

    R2,p ≅ T_p[ε]/(ε²,dε).

Since the divisor is smooth there, d is a member of a regular parameter system in T_p. This is the rank-one pattern over that localized regular base; after completion and a choice of coefficient field it is literally the analogous formal power-series normal form. This is a compatibility of the universal rings along the smooth divisor, not an additional assertion about actual deformation families.

## 5. Depth, Hilbert series, and multiplicity

Depth of these idealizations equals min(depth_T T,depth_T J_i). One way to justify comparing T-depth and R-depth is that the ideal generated by the maximal ideal of T in R is primary for the maximal ideal of R; local cohomology with these supports agrees, and the underlying T-module is T⊕J_i. Both J_i have depth 23. Consequently

    dim R_i=24,   depth R_i=23.

More generally, for any p in V(f_i), the localized nonzero torsion module J_i,p has projective dimension one over the regular ring T_p. Hence depth R_i,p = ht(p)−1 and dim R_i,p = ht(p). Off V(f_i), R_i,p=T_p is regular. Thus the non-Cohen–Macaulay locus and the nonregular locus are both exactly the nilpotent-support divisor, not merely its vertex.

Their embedding dimensions are respectively 25 and 26 because all defining relations are quadratic. Neither ring is Cohen–Macaulay or S1. The latter failure also follows from its embedded associated prime. Since a complete intersection local ring is Cohen–Macaulay, neither is a complete intersection.

All defining equations are homogeneous quadratics in standard degree one variables, so the maximal-ideal associated graded ring is the corresponding polynomial quotient. The graded presentations of the nilradicals are

    J1:  C[t](-1)/(a),
    J2:  0→C[t](-2)² --M→ C[t](-1)²→J2→0.

Thus, with q the Hilbert-series variable,

    H_R1(q) = (1+q−q²)/(1−q)^24,
    H_R2(q) = (1+2q−2q²)/(1−q)^24.

Both Hilbert–Samuel multiplicities are the numerator evaluated at q=1, namely one. The nilradicals have dimension 23; their module multiplicities at the origin are respectively one and two, consistent with the quadric's degree and the rank-one module (2). This gives an additional check on the full-ring multiplicity calculation. Multiplicity one does not force regularity here because the rings have embedded components.

## 6. Conditional consequence for the deformation problem

If a separate all-orders theorem identifies the ordinary fixed-quintic bundle hull at a transverse rank-one jump with R1, or at a surjective vertex with R2, then that hull has exactly the smooth 24-dimensional orbit germ as its reduced germ. Its entire extra deformation structure consists of a square-zero nilradical on an embedded codimension-one locus; there are no further reduced branches or higher nilpotence. At a surjective vertex the support is a rank-three quadratic cone times a 21-dimensional smooth factor, and the nilradical is its noninvertible rank-one reflexive module, with two generators precisely along the 21-dimensional vertex. This is strictly stronger than the known primary obstruction equations, dimension, and obstructedness.

These are conditional implications, not proofs of the all-orders premise. In particular a quotient or deformation with these quadratic initial equations need not inherit this nilradical, primary decomposition, reduced structure, Hilbert series, or multiplicity. No HM-specific matrix, selected polynomial, source/cofactor, or rank instance is evaluated here.
