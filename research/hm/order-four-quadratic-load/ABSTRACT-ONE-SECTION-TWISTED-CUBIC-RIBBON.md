# An abstract stable one-section bundle from a twisted-cubic ribbon

## Scope

This is a symbolic construction of stable rank-two bundles on P3 with c1=−1, c2=4, h0(G(1))=0 and h0(G(2))=1. It shows that the nonreduced minimal-sextic alternative in MINIMAL-HYPERPLANE-SECTION-CURVE-DICHOTOMY.md cannot be excluded using only those numerical, stability, and regular-section properties. No claim that the constructed bundles are HM hyperplane restrictions is made.

## 1. The lci ribbon

Let R⊂P3 be a smooth twisted cubic, with R≅P1 and O_R(1)=O_P1(3). Its conormal bundle is N*_(R/P3)=O_P1(−5)^2. Choose any two coprime binary sextics p,q. They define a surjection

I_R/I_R² = O(−5)^2 --(p,q)--> L=O(1).

Define I_C to be the kernel of I_R→L. Then I_R²⊂I_C⊂I_R, and

0→L→O_C→O_R→0,

with square-zero kernel. This is a ribbon of degree six. It is a locally complete intersection: at any point of R, surjectivity allows a local basis of the conormal in which the quotient is one coordinate. Lifting that basis to regular generators y,z of I_R gives I_C=(y,z²), up to interchange of y and z. Thus C is Gorenstein and has no embedded points.

Euler characteristics give χ(O_C)=χ(O_P1)+χ(O_P1(1))=1+2=3, so p_a(C)=−2.

## 2. Exact subcanonical identity, not just a degree comparison

Duality for the ribbon gives

ω_C|R = ω_R⊗L^−1 = O_P1(−3).

This can also be checked from the local complete-intersection presentation: the determinant of its conormal restricted to R is det(N*_(R/P3))⊗L, because one normal generator is replaced by its square. Adjunction then gives ω_R⊗L^−1.

The square-zero units sequence is

1→1+L→O_C*→O_R*→1,

where 1+L is additively L. Since H1(R,L)=0 and H2(R,L)=0, restriction Pic(C)→Pic(R) is an isomorphism. Both ω_C and O_C(−1) restrict to O_P1(−3). Therefore

ω_C≅O_C(−1)

as line bundles on the entire nonreduced curve, not merely after restriction or numerical equivalence.

## 3. No containing quadrics or cubics

A degree-d equation vanishing on C first vanishes on R. Its conormal class lies in

H0(N*_(R/P3)(d)) = H0(O_P1(3d−5))^2.

To vanish on C this pair (a,b) must satisfy pa+qb=0. Since p,q are coprime of degree six, every polynomial syzygy is a multiple of (q,−p). For d=2 or3 the degree of a,b is respectively one or four, less than six; hence a=b=0. The equation must therefore lie in the sheaf square I_R².

There are no nonzero degree-two or degree-three equations in H0(I_R²(d)). Indeed their restriction to every secant line through two distinct points of R vanishes to order at least two at each endpoint, hence identically because d<4. Secant lines of a twisted cubic fill P3, so the equation is zero. This handles the sheaf square, not just the unsaturated polynomial ideal square.

Thus H0(I_C(2))=H0(I_C(3))=0. Also H0(I_C(1))=0 because R is nondegenerate.

## 4. The associated stable bundle

The Hartshorne–Serre correspondence applies: C is codimension-two lci, ω_C=O_C(−1)=ω_P3⊗O_P3(3)|C, and H2(O_P3(−3))=0. It produces a rank-two vector bundle E with a regular section cutting C and

0→O_P3→E→I_C(3)→0,

det E=O(3), c2(E)=6.

For a primary account of this existence theorem, see Arrondo, A home-made Hartshorne–Serre correspondence, arXiv:math/0610015:
https://arxiv.org/pdf/math/0610015 .

Set G=E(−2). Then c1(G)=−1 and c2(G)=6−2·3+4=4. Intermediate line-bundle cohomology on P3 and the preceding ideal vanishings give

h0(G)=h0(I_C(1))=0,
h0(G(1))=h0(I_C(2))=0,
h0(G(2))=1+h0(I_C(3))=1.

For a normalized rank-two bundle with c1=−1 on P3, H0(G)=0 implies slope stability: any destabilizing saturated rank-one subsheaf has reflexive hull O(a) with a≥0, and its inclusion extends across codimension two to a nonzero section of G(−a), which would give a section of G. Thus G is stable.

Its unique projective minimal section cuts the nonreduced lci ribbon C. This is an actual abstract example family, not a proposal awaiting a numerical rank computation.

## Boundary

The generic HM alternative b=1 remains unresolved. Its exclusion needs additional HM geometry or multiplication structure; stability, Chern classes, absence of twist-one sections, regularity and subcanonical genus alone are insufficient. The construction uses arbitrary coprime sextics in a universal auxiliary ribbon problem, not selected HM coefficients or an experiment on the original source.
