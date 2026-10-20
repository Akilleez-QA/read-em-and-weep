# Independent mathematical review

Date: 2026-10-20.

Reviewed artifact: `PROOF.md`.

Verified SHA-256: `4bdf1d5b0a530b2d3a16f1a69065ad1c9d87cd9ce4d630e73cbe6cc56d7e953d`.

## Verdict: PASS

The structural argument establishes

    H^1(P^4, End_0(F)(6)) = 0

from the pinned section resolution and primary Horrocks–Mumford cohomology and representation inputs. The maps, twists, dual orientations, and constant-row descent have been independently checked as mathematical text. This is not formal proof verification.

### Multiplication contraction

The natural map is correctly written

    c: S_1 tensor M_3^vee -> M_2^vee,
    c(l tensor lambda)(m) = lambda(l m).

Its first factor is S_1, not S_1^vee. Naturality of multiplication gives N-equivariance with the usual contragredient actions. Generation of M in degree zero implies S_1 M_2=M_3, so c is nonzero. The extending irreducible H-module S_1 tensored with the irreducible N/H-module M_3^vee is N-irreducible. Consequently c is injective, and the dimensions 5 times 2 = 10 = dim M_2 make it an isomorphism.

### Constant-row descent

For d:35O(-5)->15O(-4), a constant row a annihilating d extends by zero to a morphism from 15O(-4) plus 4O(-3) to O(-4). It annihilates the entire image of the preceding resolution term, not merely its linear-block projection. Exactness therefore makes it descend to F. Since

    Hom(F,O(-4)) = H^0(F^vee(-4)) = H^0(F(-3)) = 0,

the extended morphism and hence a vanish. Thus rho is injective.

### Independent twist and cokernel check

Tensoring the section resolution by F(7) gives the complex resolving F tensor F(7) with terms, in degrees -3 through 0,

    2F(-1), 20F(1), 35F(2), 15F(3) plus 4F(4).

The primary cohomology table makes F(-1) acyclic and gives no positive cohomology beyond degree one in the other terms. In total cohomological degree one, the hypercohomology spectral sequence therefore has exactly the cokernel of

    35M_2 -> 15M_3 plus 4M_4 = 15M_3.

There are no possible higher incoming or outgoing differentials affecting that term. Because F^vee=F(1), the resolved bundle is End(F)(6). In characteristic zero the trace splitting End(F)=O plus End_0(F), together with H^1(O(6))=0, gives precisely the cokernel asserted in the proof.

### Dual factorization

The dual incoming map is

    U^vee tensor M_3^vee
      -> R^vee tensor S_1 tensor M_3^vee
      -> R^vee tensor M_2^vee,

with factors rho tensor id and id tensor c. For each relation, the resulting functional evaluates as the sum of lambda_j(d_jr m), which is exactly the dual of the original cohomology map. Hence the factorization is valid. The first factor is injective and the second an isomorphism. This proves surjectivity of the incoming map and the claimed vanishing.

## References and scope

Primary representation and cohomology checks used Horrocks–Mumford, *A rank 2 vector bundle on P^4 with 15,000 symmetries*, Topology 12 (1973), pp. 67, 72, 74, and the appendix:

https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

The section resolution is the pinned Decker input cited in the proof, *Monads and cohomology modules of rank 2 vector bundles*, Compositio Mathematica 76 (1990), Remark 2:

https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf

This review does not independently re-prove that published resolution. It independently checks its use in the tensor and cokernel argument.

The endpoint assertion also appears in arXiv:2207.08901v5, Lemma 2(2), but its displayed proof stops after the H^0 argument. The present proof does not rely on that assertion or its tensor-cohomology table:

https://arxiv.org/pdf/2207.08901v5

The fixed quotient consequence follows immediately from the zero target. The paired geometric conclusions remain conditional on the separately established identifications in PR439 and PR437; their geometry was not independently re-audited here. No claim of order-six optimality, actual-source membership, existence of a primitive, module lifting, or quantization algebraicity is certified.

No selected multiplication or section-resolution matrix was evaluated. No rank calculation, numerical experiment, computational algebra script, or mathematical checker was run. A file hash was checked solely to bind this review to the artifact above.
