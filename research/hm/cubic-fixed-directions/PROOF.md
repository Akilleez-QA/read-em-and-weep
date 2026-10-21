# Order-five fixed directions exclude line-valued ambient nonnormality

Status: structural derivation over C; independent review requested. No selected actual HM/source coefficients, vectors, matrices, point evaluations, rank tests, scans or computer algebra. The ambient intersection dimension r is proved to lie in {0,1}, without choosing between these two values.

## 1. Exact inputs and conclusion

Use the actual-primary/modular dictionary and equivariance assumptions of these immutable predecessors:

- PR603, c9d38741e6a4c4eb714f61abe62aafdd9bb9ba81, research/hm/no-node-trisecants/PROOF.md, Sections 1–3: the ambient five-dimensional module A is an irreducible representation of the order-125 Heisenberg group with faithful central character; the projective translation quotient is U=(F5)^2. The noncentral-character/simple-eigenline lemma there is used below.
- PR604, a4a0b5ed6e9dd0c18e3a263d1b3f8d9a49f2bf8d, research/hm/cubic-embedding-locus/PROOF.md, Sections 1, 2, 5 and 8: the sixty pentagon component lines, the equivariant cubic map Phi:M=Bl_Z(P4)->V, and the common r in {0,1,2}. The translations U preserve each pentagon fiber and act transitively on its five components. Each exceptional E_z=P3 is linearly embedded. The bad loci Sigma_ell=Phi(E_z) intersect Phi(E_w) are mutually disjoint.
- PR605, 9df4c45d0c76ded1075a0652707bdbcd1f424189, research/hm/cubic-exceptional-fibers/PROOF.md, Sections 1–3: if r=1, Sigma_ell is a point outside Phi(C_ell), with exactly one exceptional preimage in E_z and one in E_w.
- PR607, e5f805f23537bd757791b01692afb3a2c4351fa3, research/hm/cubic-surface-immersion/PROOF.md: g:Y->T is a finite normalization, everywhere unramified, with Y smooth. For r=2 its only possible multiple fibers come from optional reduced intersections q_z=A_z intersect R_z^- and q_w=A_w intersect R_w^-. Here Y intersect E_z=R_z^+ disjoint-union R_z^-; A_z is the exceptional lift of Sigma_ell and passes through the marked point of R_z^+ associated to ell. An optional q_z is different from all four marked component-side directions in Y intersect E_z. The corresponding statements hold at w. Singleton fibers imply smoothness and an isomorphism neighborhood.

In particular, all use of the normalization geometry concerns the actual coordinate-copy surface, not another representation with matching dimensions. The two branches at a node are transverse, and each is incident with two distinct pentagon component directions. The sixty branch vertices are paired into thirty nodes.

The geometric source for the translation action and pentagons is Barth–Hulek–Moore, *Shioda's Modular Surface S(5) and the Horrocks–Mumford Bundle*, Section 4.2 and Section 4.5, Proposition 9, printed pp.57, 63–64. Proposition 10 on p.64 proves transverse branches. Public source:

https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

**Theorem.**

1. The alternative r=2 is impossible. In particular the ambient cubic normalization Phi is everywhere unramified and has only reduced fibers of length at most two.
2. If r=1, both exceptional preimages of every one of the sixty bad ambient values lie on Y. Therefore T has exactly sixty singular/nonnormal points; each has exactly two reduced normalization preimages. Both preimages are marked pentagon-side points on exceptional curves.
3. If r=0, both Phi and g are closed immersions. Thus the restricted cubic surface is smooth if and only if the ambient cubic image is smooth, if and only if r=0. Otherwise both have exactly the same sixty-point singular/nonnormal locus, each bad fiber of either normalization consisting of the same two reduced points on Y. No analytic transverse-double-point assertion is made for r=1.

## 2. An order-five stabilizer for every component

Fix any pentagon component ell with endpoint nodes z,w. The projective translation group U preserves its pentagon and acts on its five-cycle dual graph. The automorphism group of a five-cycle is dihedral of order ten. Since U has exponent five, its image lies in the cyclic rotation subgroup. Its transitivity on the five components, established in PR604, makes that image have order five. The kernel G therefore has order five and fixes every component of the pentagon.

In particular G preserves ell and its two endpoints individually: an order-five group cannot act nontrivially on a set of two points. This is a subgroup of the projective Heisenberg translations, not an arbitrary cyclic subgroup of the full normalizer.

At either endpoint, say z, G preserves the two-point normalization fiber over z, so fixes both branch vertices individually. It preserves the set of four component lines through z. Indeed the complete list of lines on S is given by PR604; only its four incident pentagon sides pass through z, since the distinguished section lines avoid all nodes. These four are distinct: the two sides on each branch have different tangent directions and the two branch tangent planes are transverse. An order-five permutation of a four-element set must be trivial. Thus all four side directions at z are individually fixed by G. Equivalently their four marked points in E_z are fixed.

This reasoning also handles the opposite normalization branch, even if it lies on the other member of a paired fiber. No assumed formula for the action on that second fiber, and no assumed coincidence of chosen local multipliers, is needed.

## 3. These are all fixed points on the exceptional P3

Let a be a lift to the Heisenberg group of a generator of G. Its action on A has five distinct eigenvalues, each with multiplicity one. Here is a basis-free verification. Nondegeneracy of the Heisenberg commutator gives h with hah^(-1)=za for a nontrivial central z. The central character sends z to a primitive fifth root eta. Hence conjugation identifies the spectrum of a with its eta-multiple, preserving multiplicities. As a finite-order operator a is diagonalizable. Its eigenvalues consequently form full eta-orbits, of size five. Since dim A=5, there is exactly one such orbit and every multiplicity is one.

The fixed projective point z is one eigenline L_z. The tangent representation is

    T_z P(A) = Hom(L_z,A/L_z).

Its four eigenvalues are the four ratios of the other eigenvalues to the eigenvalue of L_z. They are distinct. On E_z=P(T_z P(A)) the action therefore has exactly four fixed projective points, namely its four eigenlines. Section 2 has exhibited four distinct marked component directions as fixed points. It follows that

    (E_z)^G = {the four marked pentagon-side directions at z}
             subset Y intersect E_z.

The equality is an equality of sets of complex points, which is all that the subsequent argument needs. In particular it does not assert a scheme structure for a fixed locus or a selected differential computation. The argument applies identically at w.

## 4. Exclusion of the optional intersections when r=2

Because G preserves ell, z and w, equivariance makes it preserve Sigma_ell and its exceptional lift A_z. It also preserves R_z^+ and R_z^- individually: these correspond to the two fixed normalization vertices over z. If the optional point q_z=A_z intersect R_z^- existed, its uniqueness would make it G-fixed. Section 3 would force q_z to be one of the four marked side directions.

But PR607 excludes every such direction. To recall the short reason, q_z lies on R_z^-, which is disjoint from R_z^+, so it is not either marked point on R_z^+. Either marked point on R_z^- belongs to the strict transform of another component ell'. For r=2 its image lies on Sigma_ell'=Phi(C_ell'). If it also belonged to A_z, that image would lie on Sigma_ell as well, contradicting the disjointness of distinct bad lines. Thus no q_z exists. The same argument excludes q_w.

Applying this uniformly to every component removes all possible multiple fibers listed by PR607. Its unramified finite-normalization criterion makes g an isomorphism. Composing with the image embedding T subset P9 gives a closed immersion of Y. Smoothness and degree 75 follow from the source and the already established degree.

## 5. The same fixed directions contradict r=2 at an endpoint

The preceding conditional smoothness result can be strengthened to a contradiction. Suppose r=2 and retain ell,z,w,G. The marked point p_z on C_ell is fixed by G, hence alpha=Phi(p_z) is fixed too. By PR605, alpha belongs to Sigma_ell, which lies in Phi(E_w). Let e_w be its unique preimage in E_w. Equivariance and the embedding Phi|E_w make e_w G-fixed. Section 3 therefore makes e_w one of the four marked side directions at w.

It cannot be the direction p_w of ell itself, since Phi(p_w)=beta differs from alpha. Thus e_w is the marked direction of a different component ell'. Its image lies on Phi(C_ell')=Sigma_ell' in the r=2 case. This puts alpha in two distinct bad lines Sigma_ell and Sigma_ell', contradicting PR604.

Consequently r=2 cannot occur. This argument also shows directly why merely retaining the smooth-surface conditional alternative of Section 4 would miss a stronger conclusion: the opposite exceptional preimage at an endpoint is forced to be one of the prohibited optional marked points. PR605 now supplies everywhere unramifiedness of Phi and reduced fibers of length one or two in the only remaining cases r=0,1.

## 6. Forced marked double fibers when r=1

Now Sigma_ell is a single point y. Since G preserves ell and its endpoints, equivariance fixes y. The restriction Phi|E_z is an embedding, so the unique preimage e_z of y in E_z is fixed by G. Section 3 places it among the four marked directions, all belonging to Y. The same holds for e_w in E_w. Distinct ambient exceptional divisors are disjoint, so these are distinct points.

PR605 gives exactly these two ambient preimages and reduced fibers; restriction to Y therefore has the same two reduced points. PR607 already proves that every multiple surface fiber is singular/nonnormal and that no other surface singularities occur. The sixty distinct points Sigma_ell consequently give exactly sixty such points.

The endpoint marked points belonging to ell itself cannot be e_z or e_w, since PR605 proves y is not in Phi(C_ell) when r=1. Thus each forced preimage is a marked direction of a different incident component. We do not identify which one and do not infer tangent transversality between the two image surface branches.

## 7. Contribution and remaining boundary

The finite choices left in PR607 are now sharply reduced: r=2 is excluded altogether, while r=1 has all sixty double fibers. Both normalizations are everywhere unramified, and smoothness/embedding of the ambient and surface cubic images are equivalent. The new ingredient is the exhaustive fixed-point set of an order-five translation on each ambient exceptional P3, not an actual coefficient or kernel test.

The argument does not choose between r=0 and r=1. In particular it does not prove that the ambient normalization is an embedding, or that the surface is unconditionally smooth. It does not compute the r=1 conductor length, tangent intersection, completed local algebra or Hilbert polynomial of T. The separate full-adjoint, higher-lifting and algebraicity gates are unchanged.
