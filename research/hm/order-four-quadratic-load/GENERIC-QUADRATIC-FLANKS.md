# Both actual quadratic flanks are generically good

## New consequence of the square-jet theorem

Let F be the normalized HM bundle, B=End_0(F), and let P=P(H0(O_P4(2))) be the projective fourteen-dimensional space of quadrics. Retain the actual multiplication-compatible primary/residual rows

0 -> P_2 -> H1(B(2)) -> N_2 -> 0,
0 -> P_4 -> H1(B(4)) -> N_4 -> 0,

of dimensions (20,85,65) and (40,85,45). These are the actual extension rows, not chosen split vector-space models. P_2=H0(F(3)) tensor H1(F), P_4=H0(F(3)) tensor H1(F(2)).

PRIMARY-INJECTION-AND-FAILURE.md proves a nonempty Zariski-open set of q where P_2 -> P_4 is injective. UNIQUE-CUBIC-SQUARE-JET-INJECTIVITY.md at af3cf8bf93c4274e7651ad3d85e310825febaeee now proves that a general square q=ell² makes the actual residual N_2 -> N_4 surjective, via its pinned Rao duality. Surjectivity is an open condition on the full space of quadrics. Thus the residual-good locus is a nonempty open in P, not merely a statement about an abstract matrix.

Since P is irreducible, these two nonempty opens intersect in a nonempty dense open U. Intersecting additionally with the smooth-quadric open remains nonempty. Consequently a general smooth quadric has BOTH actual primary injectivity and residual surjectivity. No assertion that the same square has primary injectivity is required, and no product-to-square inference is used.

## The remaining obstruction is exactly the actual rank-twenty boundary

Over U write the universal multiplication maps using O_P(-1):

P_2 tensor O(-1) -> P_4 tensor O,
N_2 tensor O(-1) -> N_4 tensor O.

Let C be the cokernel of the first and K the kernel of the second. Both are vector bundles of rank20 on U. The snake lemma for the actual rows supplies a canonical bundle map

delta:K -> C.

For every q in U its kernel and cokernel are respectively the kernel and cokernel of q:H1(B(2))->H1(B(4)). Hence the full quadratic map has corank at most20 on this dense open, and is invertible exactly where delta is invertible. In particular the new flank theorem does not prove that delta is nonzero, full-rank, or invertible anywhere.

## Chern and determinant bookkeeping on the good open

Let h be the restriction of c1(O_P(1)). In K-theory on U the exact sequences give

[C]=40[O]-20[O(-1)],
[K]=65[O(-1)]-45[O].

Therefore

c1(C)=20h, c2(C)=210h²,
c1(K)=-65h, c2(K)=2080h².

These identities are identities in the Chow/cohomology rings where the restricted classes are defined; they do not assume that restriction from P is injective in those degrees. In particular no contradiction is inferred from these Chern classes merely because U is open.

The determinant of the remaining actual boundary is a section of

det(C) tensor det(K)^(-1) = O_U(85),

up to the fixed determinant lines of the constant cohomology spaces. This agrees with the degree85 determinant of the full 85-by-85 universal quadratic multiplication. The agreement does not prove that either determinant is nonzero. It identifies exactly what a future nonvanishing argument must address, after the two flanks have now been established on a common open.

## Sources and limits

All source files are in Akilleez-QA/read-em-and-weep, draft PR543, research/hm/order-four-quadratic-load/:
- PRIMARY-INJECTION-AND-FAILURE.md: universal primary-open proof and actual snake boundary.
- UNIQUE-CUBIC-SQUARE-JET-INJECTIVITY.md, af3cf8bf93c4274e7651ad3d85e310825febaeee: actual generic square Rao injectivity and residual surjectivity, with the complete pinned section-case chain.
- DOUBLE-HYPERPLANE-JET-CRITERION.md, 18963f6d45068dd561c63420b9f0135103a9d09b: the actual Rao jet and residual identification.

The new conclusion is simultaneous generic goodness of the two actual flanks, including on smooth quadrics, and its exact twenty-dimensional remaining boundary. The selected original coefficients, full Q4, source membership and higher lifting are not settled. No selected source matrices, coefficient evaluations, numerical ranks, scans, local-model spike or consumed experiment were used.
