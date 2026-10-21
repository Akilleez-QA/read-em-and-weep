# Global equality of the primary degeneracy scheme and the modular surface

Status: authored structural proof, independently mathematically reviewed in REVIEW.md; not formally checked. Work over C. All coordinate identities below are universal representation identities in indeterminate coordinates, not evaluations at selected HM/source instances.

## 1. Inputs and conclusion

Let D=D9(e) be the actual primary evaluation degeneracy scheme on P(A), for e:3Q(-1)→10O. Let S be its unique normalizer-invariant integral component containing the twenty-five distinguished lines, and let C be their reduced union.

The exact pinned inputs are:

- PR566, commit 11642c25ba1b3046e8bc97e3f0e95f077e010375: D is a smooth surface in an open neighborhood of C, and the component there is S.
- PR567, commit e0f15a5c6a49d2101dae450dae4d26171a259331: S is invariant under the projective Heisenberg normalizer N.
- PR569, commit 3c79994aac419f7c963b06df52e0e330929318a2: the five distinguished lines in each affine block span a unique hyperplane, and a cyclic eigenbasis identifies its five parallel-block hyperplanes with the five eigen-coordinate hyperplanes.
- PR570, commit e5e55594ef2b99cefb81c4c02b22cb45e1ff0025: S is exactly the coordinate-copy BHM surface S15, its torsion sections are exactly C, and D=S scheme-theoretically on the coordinate torus U={x0 x1 x2 x3 x4≠0}.
- PR571, commit 25afc8bfce079492b6b06bb6f52489f8d481c2aa: the primitive Galois/dual conventions give the same projective translation subgroup and the same affine-block directions in this exact coordinate copy.

The new conclusion is the global equality of closed subschemes

D=S.

In particular there are no additional components, embedded components or nilpotent structure hidden on the coordinate boundary. This is equality of ideal sheaves, hence of saturated homogeneous ideals; it is not a claim that an unsaturated list of maximal minors is itself saturated.

## 2. The exact public base-locus dictionary

Write the standard coordinate generators as the cyclic shift σ(e_i)=e_(i-1) and diagonal τ(e_i)=ζ^i e_i, for indices in F5. The reversal ι(e_i)=e_(-i) has negative eigenspace

P1−: x0=0, x1+x4=0, x2+x3=0.

Replacing ζ by a primitive power replaces τ by a primitive power and leaves the generated subgroup unchanged. The dual conventions invert generators and again give the same subgroup. Reversal is unchanged. Thus this assertion concerns the actual projective subgroup in the primary coordinate space, and does not identify two inequivalent linear central characters.

BHM, Section 5.2, Proposition 13, printed page 69, identifies the images of all twenty-five torsion sections of its S15 as the translates of precisely this P1−. Its displayed equation (24) is x0=x2+x3=x1+x4=0. By PR570 these are exactly the distinguished lines C in the primary space.

Aure–Decker–Hulek–Popescu–Ranestad, “Syzygies of abelian and bielliptic surfaces in P4,” Section 1, uses the same cyclic shift, diagonal and reversal. Section 3, printed page 9, states that the union of the twenty-five translates of P1− is cut out by the Heisenberg-invariant quintics. In particular, their common zero set is C. Only this set-theoretic consequence is needed; no stronger base-ideal multiplicity is imported.

Consequently, in the exact primary coordinate space,

V(H0(O_P4(5))^H5)=C as sets.                       (1)

This transfer is justified by equality of the displayed coordinate group and the displayed starting line, not by matching degrees or using the separate fixed-beta surfaces.

Public sources:

- BHM: https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf , Section 5.2 Proposition 13, together with Section 4.5 Propositions 9–11.
- ADHPR: https://arxiv.org/pdf/alg-geom/9606013 , Sections 1 and 3, especially the invariant-quintic base-locus statement on printed page 9.

## 3. Six boundary products span all invariant quintics

For each of the six cyclic directions U in G=F5², let q_U be the product of the equations of its five eigen-coordinate hyperplanes. By PR569 these are also the five affine-block hyperplanes in that direction. Each q_U is Heisenberg invariant: the chosen cyclic generator acts diagonally with eigenvalue product one, a complementary generator cycles the five factors with product one, and the center acts trivially on degree-five polynomials.

The normalizer acts transitively on the six cyclic directions. Therefore the six divisors V(q_U) belong to the normalizer orbit of the coordinate-boundary divisor V(x0 x1 x2 x3 x4).

For completeness, the following universal calculation proves that their span is the entire invariant space. Choose Schrödinger coordinates and a primitive fifth root ζ. Up to scalar and relabeling the six products are

q_infinity=product_i x_i,
q_a=product_(b in F5)(sum_(i in F5) ζ^(a i²+b i)x_i), a in F5.

Indeed quadratic-phase changes applied to the Fourier eigenbasis give the eigenbases of the five nonvertical cyclic directions; a change a↦a/2 merely relabels them.

Collect the terms of q_a by the quadratic weight w=sum_i i² times the exponent of x_i. Then q_a=sum_w ζ^(aw)Q_w. Every Q_w is nonzero. In q_0 the coefficients of x0^5, x0³ x_i x_(-i), and x0 x_i² x_(-i)² are respectively 1, -5, and 5. For i=1,2 their weights exhibit all residues: 0; 2,3; 4,1. To check these coefficients universally, put λ_b=yζ^(bi)+zζ^(-bi). Character orthogonality gives p1=p3=0, p2=10yz, p4=30y²z². Newton identities give e2=-5yz and e4=p2²/8-p4/4=5y²z².

Fourier inversion proves the five q_a independent. Their span has weight-zero subspace C Q_0. The remaining q_infinity has weight zero but is not proportional to Q_0, because only Q_0 has a nonzero x0^5 coefficient. Hence the six products are independent.

Finally the diagonal-weight-zero degree-five monomials number (126+4)/5=26, by the root-of-unity filter. Under the cyclic shift exactly one such monomial, product_i x_i, is fixed; the other twenty-five form five orbits of length five. Thus the whole Heisenberg-invariant quintic space has dimension six. We have proved

span{q_U}=H0(O_P4(5))^H5,
intersection_U V(q_U)=C as sets,                   (2)

where the second equality follows from (1). The polynomial calculation is a universal representation calculation, not an actual-source point or rank evaluation.

## 4. Eliminate the global scheme discrepancy

Since the reduced component S is a closed subscheme of D, there is an inclusion of coherent ideal sheaves I_D⊂I_S. Put

K=I_S/I_D.

The two schemes are N-invariant: D is defined by the actual equivariant evaluation map and S is invariant by PR567. Hence the closed support Supp(K) is N-invariant. PR570 gives K|U=0, so

Supp(K)⊂V(x0 x1 x2 x3 x4).

Applying every normalizer translate and using invariance gives

Supp(K)⊂intersection_(n in N) n V(x0 x1 x2 x3 x4)
       ⊂intersection_U V(q_U)=C.

But PR566 says D is already a smooth surface around every point of C and its component there is S. Consequently I_D=I_S in a neighborhood of C, and K has zero stalk at every point of C. A coherent sheaf whose support is contained in C but has no support point on C is zero. Thus K=0 globally, proving D=S.

This argument controls all coherent scheme discrepancies simultaneously, including embedded or nilpotent structure. It does not merely exclude extra top-dimensional components.

## 5. Exact depth defect at the thirty double points

There is also a local structural consequence. At each of the thirty double points, BHM Proposition 10 gives precisely two smooth surface branches with complementary tangent planes in the smooth four-dimensional ambient space. In the completed ambient local ring their branch ideals have sum equal to the maximal ideal: their linear parts already span the cotangent space, and Nakayama applies. Since the reduced analytic germ is the union of those two branches, its completed local ring is the fiber product

C[[u1,u2]] ×_C C[[v1,v2]]
≅ C[[u1,u2,v1,v2]]/(u_i v_j : 1≤i,j≤2).

The exact sequence from this fiber product into the direct sum of the two regular two-dimensional branch rings, with cokernel C, gives depth one by the depth lemma. Thus D is not locally Cohen–Macaulay at exactly these thirty points; it is regular elsewhere. This does not contradict the Cohen–Macaulayness of the distinct primary-bad quadratic-parameter scheme. In particular, applying an expected-codimension-three determinantal Cohen–Macaulay conclusion to this actual codimension-two surface would be incorrect.

## 6. Geometric scope

The actual full primary degeneracy scheme is therefore the reduced integral degree-fifteen modular image identified in PR570. Its normalization is S(5); it is smooth except at the thirty transverse double points described by BHM Proposition 10. Those singularities and the smooth neighborhood of the twenty-five distinguished lines now describe D itself, rather than only its reduced line-bearing component.

This does not turn D into the separate primary-bad quadratic-parameter eightfold, nor identify it with a fixed-beta degeneracy surface. It does not imply generic square primary injection, invertibility of the remaining full-adjoint boundary, prescribed-source membership, higher lifting, or algebraicity. No selected source instance, coefficient matrix or numerical rank has been evaluated.
