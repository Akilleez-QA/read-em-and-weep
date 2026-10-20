# Consequences of the structural nonzero-scalar theorem

## Dependency status

Verified dependency: the full [quintic scalar propagation proof](../quintic-scalar-propagation/PROOF.md), especially Sections 7–9, and its [final independent audit](../quintic-scalar-propagation/AUDIT.md) establish c≠0. The historical source proof SHA-256 was checked against that historical audit and matched (not a hash of the editorially normalized publication): `35a93234687c5d79533f8fc55a7589b3cae6546e683dd3e4c192adbbc3d89c4c`. This document applies the newly verified theorem without altering the earlier hash-audited conditional [PROOF.md](PROOF.md) or [RELATIVE.md](RELATIVE.md).

## Corollary from c≠0

By the cited structural theorem c≠0 for the actual HM bundle, the nonzero branches of the two preceding theorems now apply unconditionally:

1. For a smooth quintic Xₚ, the simple restriction F|Xₚ has self-Ext dimensions (1,26−r,26−r,1), where r=rank Ψ(p). The exact tangent-dimension strata are 26 on Ω∩P(ker Ψ), 25 on Ω∩(V(ad−b²)\P(ker Ψ)), and 24 on Ω\V(ad−b²). All three strata are nonempty; a general smooth quintic has dimension 24.

2. On the universal smooth-quintic family π:𝒳→Ω, the trace-free degree-one relative cohomology sheaf is the constant rank-24 bundle H¹B⊗O. Its fiber map to individual H¹ is injective, with cokernel of dimension 0, 1, or 2 at rank 2, 1, or 0. The cokernel is canonically Tor₁(𝒞,k([p])). Thus the individual tangent spaces do not form the fibers of this single rank-24 vector bundle at the jump locus.

3. The degree-two relative cohomology sheaf fits into the canonical sequence

       0→𝒞→R²π_*𝔅→H³B(−5)⊗O(−1)→0,

   where 𝒞 is the cokernel of the injective universal sheaf map U⊗O(−1)→U*⊗O. It is a rank-one maximal Cohen–Macaulay sheaf on the determinant quadric, locally free there away from its vertex. The degree-two base-change map is an isomorphism at every point of Ω.

4. The determinant quadric is an actual cohomology-jump hypersurface, not merely an auxiliary representation-theoretic possibility. Its equation is defined up to a nonzero factor, and it remains distinct from the hypersurface-singularity discriminant of quintic equations.

No numerical normalization of c is needed. None of these conclusions determines the actual obstruction maps, local moduli dimensions, conductor-cofactor ranks, or physical-source obstruction values. The new input excludes only the zero branch of the already established restriction and relative-cohomology dichotomies.
