# Thirty canonical primary rank-eight points

Work over C. Let H be the order-125 Heisenberg group, with center Z of order five and projective quotient H/Z=(F5)^2. Use the actual pinned equivariant exterior model

    phi: exterior^2 A -> V tensor W,
    dim A=dim V=5, dim W=2,

where A and V are irreducible Heisenberg representations with nontrivial central characters, V has the square of the central character of A, and H acts trivially on W. The actual primary evaluation image at [x] is

    Y_x=sl(W) phi(x wedge A).

The support map sigma:Q(-1) tensor W* -> V tensor O on P(A) and its rank-at-most-four degeneracy scheme D4(sigma) are those of PR552.

## 1. The canonical thirty-point set

There are six one-dimensional subgroups of H/Z. For each, choose any noncentral order-five lift g. On A, g has five distinct eigencharacters, each with a one-dimensional eigenspace. This follows directly from the Schrödinger representation, or from its character: the trace of every nonidentity power of g is zero. Changing the lift by a central element or replacing its generator does not change the set of five eigenlines.

The five eigenlines arising from two distinct directions are disjoint. Indeed lifts of independent directions have nontrivial central commutator. If their operators had a common eigenline, their commutator would act trivially on it; the nontrivial central character of A makes this impossible.

Thus these six sets form a reduced set Omega of thirty distinct points in P(A). The normalizer permutes the directions and eigenlines, so Omega is normalizer invariant. In fact it is one orbit: SL2(F5) acts transitively on the six directions, and the projective Heisenberg group acts transitively on the five eigenlines of each direction by conjugation. This orbit assertion is not needed for the rank calculation.

## 2. Exact support and primary rank at every point of Omega

Fix a direction and label the five eigencharacters of its lift on A by the residues b in F5. Let x span the eigenspace with label a. The four-dimensional star x wedge A is the direct sum of four one-dimensional eigenspaces, with distinct characters a+b for b not equal to a. It therefore omits precisely character 2a.

The same lift has each character exactly once on V; since W is H-trivial, each character space of V tensor W is V_j tensor W, where dim V_j=1. Equivariance and injectivity of phi imply that each of the four nonzero star-character lines maps to a nonzero line

    V_(a+b) tensor w_b,  w_b in W nonzero.

Consequently the V-support of the star is exactly the direct sum of the four V-character lines other than V_(2a). In particular sigma has rank exactly four at [x]. No transitivity argument and no choice or evaluation of the vectors w_b is required.

For each nonzero w in W, sl(W)w=W: in a basis beginning with w, a diagonal traceless operator and a suitable off-diagonal operator send w to two independent vectors. Applying this separately to the four star-character lines gives

    Y_x = direct sum over b not equal to a of (V_(a+b) tensor W),
    dim Y_x=8.

Thus the actual primary evaluation has rank exactly eight at every point of Omega. This is an unconditional structural rank theorem on the whole canonical orbit, not a selected-instance coefficient or matrix evaluation.

## 3. Consequences for the support-drop scheme

The reduced thirty-point scheme Omega is contained in D4(sigma). Indeed every maximal minor vanishes at each point, and its ideal is consequently contained in the radical ideal of Omega. PR552 proved that D4(sigma) is proper and has no divisorial component, but did not prove it finite.

If D4(sigma) is zero-dimensional, it has the expected codimension four, so the dual maximal-minor Porteous formula gives length c4((Q(-1) tensor W*)*)=30. The closed subscheme Omega already has length thirty. Therefore in this conditional case

    D4(sigma)=Omega

as schemes: the support drop is exactly the thirty reduced eigenlines. This argument neither assumes nor proves finiteness. Additional positive-dimensional components are not excluded here.

## Exact dependencies and limits

- PR552, commit e037e0a3686ecaae2d4691435c54db338e2b1798, constructs sigma and proves its Chern class and conditional length:
https://github.com/Akilleez-QA/read-em-and-weep/blob/e037e0a3686ecaae2d4691435c54db338e2b1798/research/hm/primary-support-strata/PROOF.md
- The actual exterior model and its evaluation formula are pinned in PR543, commit 7bf725bcd857a2deb975f9ecb80fca32e7833ae0:
https://github.com/Akilleez-QA/read-em-and-weep/blob/7bf725bcd857a2deb975f9ecb80fca32e7833ae0/research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md
- Horrocks-Mumford (1973), Sections 1–2, constructs the Heisenberg representations, the normalizer quotient SL2(F5), and the exterior multiplicity representation W:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

The new unconditional result is the canonical thirty-point inclusion and exact primary rank eight on that entire orbit. The equality of schemes is conditional on finiteness. Neither support-three exclusion, full adjoint invertibility, prescribed source membership, Q4, higher lifting, nor algebraicity is established. No selected HM/source coefficients, matrices, numerical ranks, or large computations are used. This is a mathematical derivation, not formal verification.
