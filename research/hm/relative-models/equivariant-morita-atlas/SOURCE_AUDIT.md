# Independent source audit: PASS under the stated hypotheses

Source: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6263380151
Created and last updated: 2026-10-19 08:50:01 UTC.
PR1 head: 2531056eae05fdf31e8fb4ca3affc5907073ad73.
PR79 head: 4659e4425c6b5ab6b1899e6af93656ac03ff0862.

## Verified argument

For an actual equivariant Morita-invertible (D_i,D_j)-bimodule P that is free of rank one on the left, choose an invariant left generator e using the stipulated local trivial-residue hypothesis. The right action defines e b=phi(b)e. Morita invertibility identifies the right algebra with the opposite of the left-module endomorphism algebra, so phi is an algebra isomorphism. Invariance of e makes phi equivariant. Consequently P^G is the rank-one bimodule defined by the restricted isomorphism between invariant rings and is Morita-invertible there.

For two such bimodules, e_ij tensor e_jk is an invariant left generator of their balanced tensor. In these frames both sides of the claimed invariant tensor comparison are the rank-one bimodule for the composed algebra isomorphism; the natural map identifies their generators. This verifies precisely the comparison needed for supplied composition maps. It does not invoke a general tensor-commutation theorem for invariants. Naturality then preserves the actual associativity coherence.

For a weak overlap action, replacing sigma_g(p) by c_i(g) sigma_g(p) c_j(g)^(-1) produces the left coherence unit c_i(g)F_i(g)(c_i(h))A_i(g,h)c_i(gh)^(-1) and the corresponding right inverse coherence unit. Both become identity after strictification. In a balanced tensor, the adjacent c_j(g)^(-1) and c_j(g) cancel, so the original composition remains equivariant. Equality of separately chosen chart gauges is unnecessary.

With restriction-compatible sheaf data, quotient charts and locally available invariant generators supplied as stated, these constructions descend an algebroid and its locally free, inertia-trivial module problem. The previously audited invariant-frame descent supplies the local module equivalence; its naturality makes the gluing compatible. Compatible coefficient ideals can be handled by their actual invariant intersections in these frames.

## Scope

The statement assumes actual coherent bimodules, actual associative composition, and sheaf/atlas effectiveness; it does not construct them from completed stalk data. It does not assert a single global algebra, arbitrary two-sided base change, or a fully faithful functor on all bimodules. The warning concerning the ramified sign-cover tensor map is correct.

This closes the abstract chart-gauge compatibility criterion. It supplies no actual physical mixed atlas, ambient comparison, module existence, or retained obstruction value. No source operation was evaluated. No outstanding mathematical correction identified.
