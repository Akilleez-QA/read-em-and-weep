# Simplicity of the canonical ruling bundle on an I5 fiber

## Precisely required inputs

Let E be a reduced cycle of five projective lines with ordinary nodes, and let V be the actual canonical ruling bundle restricted to E. Use the checked properties:

- V has rank two and is globally generated;
- h0(E,V)=5;
- on each component C_j≅P1, V|C_j≅O⊕O(1);
- the actual Heisenberg group H5 acts equivariantly, transitively on the five nodes;
- its action on H0(E,V) is the irreducible five-dimensional Schrödinger representation.

These are the canonical bundle and action, not a substituted model. The splitting input is recorded in CANONICAL-CUSP-COMPONENTS.md; global generation, fiberwise h0, and the action are recorded in MODULAR-RULING-BUNDLE.md at commit 5967472ac1a9afe35628dac672fc88321b429110. The argument below uses no chosen gluing coefficients.

## 1. Positive sublines cannot match at all nodes

On each component C_j, the O(1) subline P_j⊂V|C_j is intrinsic: Hom(O(1),O)=0, so it is the unique maximal-degree subline. At a node, the two branches supply two lines inside the same two-dimensional fiber of V. Call the node matching if those lines agree.

The matching condition is invariant under any equivariant bundle automorphism. Transitivity on nodes therefore makes either every node matching or every node nonmatching.

Suppose all nodes match. Then the P_j glue to a line subbundle P⊂V. This can be checked in the standard description of vector bundles on a nodal curve as component bundles with fiber identifications at the nodes: the identifications preserve the selected lines, and their quotients glue to a line bundle R. Thus P has multidegree (1,1,1,1,1), and R has multidegree (0,0,0,0).

The dualizing bundle of the cycle E is trivial. Since P^{-1} has degree −1 on every component, it has no global section. Serre duality and Riemann–Roch on the nodal genus-one curve give h1(P)=0 and h0(P)=5.

The quotient R of a globally generated bundle is globally generated. A globally generated multidegree-zero line bundle on this connected cycle is trivial. Indeed, a global section nonzero at one smooth point is a nonzero constant on that component after trivialization, hence nonzero at both adjacent nodes. Gluing propagates nonvanishing around the entire cycle. It is consequently a nowhere-vanishing section of R.

Now the exact sequence 0→P→V→O_E→0 and h1(P)=0 give h0(V)=h0(P)+h0(O_E)=6, contradicting h0(V)=5.

Therefore every node is nonmatching.

## 2. There are no nonzero square-zero endomorphisms

Let α be an endomorphism of V with trace and determinant identically zero. On each component, relative to O⊕O(1), its matrix has the form

    [ a   0 ]
    [ ℓ   d ]

with a,d constants and ℓ a section of O(1). The conditions a+d=0 and ad=0 force a=d=0. Thus the fiber image of α on either branch lies in its positive line P_j.

At each node the two fiber endomorphisms must agree. Their common image lies in the intersection of the two nonmatching positive lines, which is zero. Hence α vanishes at the node. Its component coefficient ℓ therefore vanishes at both distinct endpoints of C_j. A section of O(1) vanishing at two points is zero. This holds on every component, so α=0 globally.

Equivalently, every square-zero endomorphism vanishes. The direct trace-and-determinant argument avoids any assumption on diagonalizability at the nodes.

## 3. Heisenberg characters force simplicity

Global generation makes the natural map

End_E(V) → End_C(H0(E,V))

injective: an endomorphism vanishing on all generating sections vanishes as a bundle map. The invariant subspace End_E(V)^{H5} is consequently scalar by Schur's lemma.

The center of H5 acts by a scalar on H0(E,V). Equivariance and surjectivity of the evaluation map imply that it acts by that same scalar on every fiber of V. Its conjugation action on End_E(V) is therefore trivial. The action on End_E(V) factors through H5/Z≅(Z/5)^2 and decomposes into character eigenspaces.

Take an endomorphism α in a nontrivial character χ eigenspace. Since H0(O_E)=C carries the trivial action, equivariance of trace gives tr α=0. Determinant transforms by χ²; since χ has order five, χ² is also nontrivial, so det α=0. Section 2 then gives α=0.

All nontrivial eigenspaces vanish, while the invariant eigenspace is precisely C·Id. Therefore

H0(E,End(V))=C,       H0(E,End_0(V))=0.

Since End_0(V) is self-dual by the trace pairing and ω_E=O_E, Serre duality also gives

H1(E,End_0(V))=0.

Thus the trace-free endomorphism bundle is acyclic on every I5 cusp fiber. This is fiberwise simplicity and acyclicity; by itself it does not assert surjectivity of an unrelated global evaluation map without the corresponding base-change argument.

No selected coefficients, numerical ranks, experiments, or external writes are used.


## 4. Global relative acyclicity, including the cusps

For a smooth modular fiber E, ADHPR Section5 following Proposition5.5 (PDF p.35) identifies the normalized ruling scroll with the projectivization of the unique nonsplit extension

0→O_E(−o)→E0→O_E→0.

Source: https://arxiv.org/pdf/alg-geom/9606013 . This rank-two degree-minus-one bundle is stable. Indeed, a hypothetical subline A of degree at least zero has zero map to O_E(−o), hence maps nontrivially to O_E. This forces deg A=0 and A≅O_E, and the induced isomorphism to the quotient splits the extension, a contradiction. The actual ruling bundle V differs by a line twist, which preserves stability and its endomorphism bundle. Stability implies H0(End0 V|E)=0, and Serre duality with ω_E=O_E gives H1=0.

Together with Sections1–3 this proves trace-free endomorphism acyclicity on every fiber of the modular elliptic fibration f:S→P1, smooth or I5. Since End0(V) is a vector bundle and f is a flat proper family of curves, cohomology and base change gives

Rf_*End0(V)=0.

The derived projection formula consequently yields, for every integer a,

H^i(S,End0(V)⊗f*O_P1(a))=0 for every i.

This conclusion includes the cusp fibers: there is no residual torsion direct image supported at the modular cusps. When a candidate dual value-map obstruction injects into this trace-free endomorphism cohomology or its relative direct image, that injection kills the obstruction. The injection itself belongs to the separate value-map proof and is not silently assumed here.
