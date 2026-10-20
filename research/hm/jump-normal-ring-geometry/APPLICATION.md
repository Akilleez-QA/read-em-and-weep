# Application to ordinary HM deformation hulls

## Dependency status

The all-orders dependency has passed its independent audit (verified 2026-10-20). The historical source files and SHA-256 hashes are listed below. These identify the original audit receipt, not editorially normalized publication bytes; the final-publication check records the latter.

- `../formal-jump-normal-forms/PROOF.md`: `dff5923dffd3f5657c3be3cd3979ed5ac456aed00d0765243ce379bf181c70a3`.
- `../formal-jump-normal-forms/AUDIT.md`: `aab68d6940045552342bc3fb3cb7f9de33ff88813722c305d823f51da7c47c7e`.
- The universal algebra `PROOF.md` here: `93dd3734adf259c434375937bd1bb3cf186ebaa9a657ea2e8102e40b30674884`.

The following is therefore a corollary to that accepted all-orders theorem and the universal algebra. It does not independently repeat the imported HM cohomology, pairing, cyclic-model, or genericity proofs. This file leaves the separately audited universal proof unchanged.

## Corollary

Let X_p be a smooth quintic, E=F|X_p the restricted normalized HM bundle, and R its complete minimal ordinary bundle-deformation hull on fixed X_p. Let A be the 24-dimensional orbit tangent space, K_p=ker Φ(p), and L_p:A→Sym²K_p* the orbit derivative pairing established in the imported obstruction theorem.

Assume either:

1. rank Φ(p)=1 and L_p≠0; or
2. Φ(p)=0 and L_p is surjective.

Then the entire reduced formal hull is exactly the embedded smooth 24-dimensional orbit germ. There are no additional reduced branches. Its nilradical N is nonzero, square zero, and supported on a divisor D of that orbit germ. The total hull is generically reduced of Hilbert–Samuel multiplicity one, but is not Cohen–Macaulay: its depth at the given point is 23. Its unique embedded associated prime is the generic prime of D, and there is no embedded prime supported just at the vertex described below.

In case 1, in suitable noncanonical formal orbit coordinates, D=(t1=0) is smooth and N≅O_D as an O_D-module. The embedding dimension is 25, and the Hilbert series is (1+q−q²)/(1−q)^24.

In case 2, D=(t1t3−t2²=0) is the rank-three quadric cone times a 21-dimensional smooth formal germ. Its singular locus is (t1,t2,t3)=0. The module N is isomorphic to the ideal (t1,t2) in O_D: it is rank-one reflexive and maximal Cohen–Macaulay, locally free away from the vertex, but requires two generators along the vertex. Its multiplication in R is identically zero; the ideal model describes its module structure, not its algebra multiplication. The embedding dimension is 26, and the Hilbert series is (1+2q−2q²)/(1−q)^24.

In both cases the nonregular and non-Cohen–Macaulay loci of the formal spectrum are exactly D. Over a generic point of D, the finite-map fiber to the reduced germ consists of dual numbers. This fiber description is distinct from the localization of the hull at that prime, which is a one-dimensional DVR extended by a square-zero copy of its residue field. The quadric-vertex fiber instead has length three and a two-dimensional square-zero maximal ideal. Away from D the hull is reduced and regular.

The vertex normal form, localized along the smooth part of D, has the rank-one pattern: after eliminating one normal variable it is T_p[ε]/(ε²,dε), with d=t1t3−t2² a regular parameter. This is compatibility of local algebra, not a claim of a globally identified family of HM hulls as p varies.

## Proof and scope

The all-orders theorem identifies R, preserving the orbit ideal, with R1 or R2 of the universal proof. Every assertion is then proved in Sections 1–5 of that proof, including explicit primary decompositions. The earlier genericity results make these consequences valid on nonempty open dense subsets of the smooth-quintic rank-one and vertex strata, respectively.

The noncanonical formal coordinates do not identify D with any independently defined geometric subvariety without further argument. No claim is made at nontransverse rank-one points or nonsurjective vertices, nor of analytic/algebraic coordinate equivalence, DGLA formality, a global moduli description, source-restricted deformation behavior, or ordered higher products. Primary quadratic equations alone would not suffice: the full-normal-form theorem is indispensable for this corollary.
