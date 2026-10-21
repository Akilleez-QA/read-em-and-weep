# The residual canonical decic and its six nodes

Status: authored structural proof, independently mathematically reviewed in REVIEW.md; not formally checked. Work over C. All representation calculations below are universal for a faithful A5 action on P1. No selected HM/source point, coefficient matrix, rank, or numerical fixture is evaluated.

## 1. Pinned input and conclusions

Use PR571 at 25afc8bfce079492b6b06bb6f52489f8d481c2aa. On the actual primary surface S, its six residual product sections s_U globally generate M=5H-C. Its normalization is ν:X=S(5)→S, with elliptic fibration π:X→P1 and ν*M=π*O(10). The pulled-back sections come from binary decics with divisors 5(p_U^++p_U^-). The twelve distinct cusps form six pairs indexed by the six directions U in F5². The compatible faithful A5 action on the base permutes these pairs by its action on the six directions. The resulting map f:P1→Γ⊂P5 is finite birational and Γ has degree ten. At this stage independence of the six sections was not assumed.

We prove:

1. The six sections are linearly independent, so Γ spans P5.
2. Γ has exactly six ordinary nodes. The normalization preimage of each node is precisely one cusp pair {p_U^+,p_U^-}; there are no other identifications or singularities.
3. Γ has arithmetic genus six and O_Γ(1)=ω_Γ. The displayed six-dimensional system is its complete canonical series.
4. The elliptic fibration π does not descend to a morphism S→P1. This last statement also uses the normalization gluing in PR570 and its precise BHM source.

## 2. Cusp pairs are the six rotation axes

The stabilizer of a direction in A5 is a dihedral subgroup D5 of order ten. Its normal subgroup C5 acts trivially on the corresponding set of two cusps, since an order-five group cannot act nontrivially on two points. A nonidentity order-five projective transformation has exactly two fixed points. Thus this cusp pair is exactly that C5's fixed pair.

Conjugate the finite projective action into PSU2: its finite inverse image in SL2(C) preserves a positive definite Hermitian form obtained by averaging. On the round sphere P1, PSU2 is the rotation group SO3. The six Sylow-five subgroups therefore determine six unoriented real axes. Choose a unit orientation n_U on each. Let G be their 6-by-6 real Gram matrix, G_UV=n_U·n_V.

For fixed U, its cyclic group C5 acts transitively on the other five axes. Indeed, if it fixed another axis, it would normalize the corresponding distinct Sylow-five subgroup. That normalizer is D5, whose unique Sylow-five subgroup would then be both groups, a contradiction. Thus |n_U·n_V| is constant for V≠U.

The symmetric operator T=Σ_U n_U n_U^t commutes with the rotation action of A5. The real three-dimensional representation is irreducible: an invariant proper real subspace would give an invariant line, and hence a map A5→O2; its image cannot be a faithful nonabelian simple rotation group, whereas the kernel must be trivial or all of A5. Consequently T is scalar, and its trace six gives T=2I. Taking its quadratic form on n_U yields

  2=Σ_V(n_U·n_V)^2=1+5c².

Hence c²=1/5, and for distinct axes G_UV=±1/√5. This derives the needed geometry from the group action, without choosing coordinates for any HM instance.

## 3. A universal Gram identity for fifth powers

For an oriented axis n choose the real spin-one binary quadratic q_n whose roots are its antipodal fixed pair, normalized by q_(north)=XY and equivariance under SU2. Its stabilizer acts trivially on XY, so this is well-defined; reversing the axis changes its sign. The six actual decics are nonzero scalar multiples of q_n^5 because their divisors agree.

Equip Sym^10(C²) with its SU2-invariant positive definite Hermitian form, scaled so ||X^5Y^5||=1. Distinct monomials are orthogonal. For axes n,m with dot product t, rotate n to north and m into a meridian making angle θ, with t=cos θ. After this rotation the quadratic q_m has coefficients

  q_m=-(1/2)sin(θ) X²+cos(θ) XY+(1/2)sin(θ) Y².

The pairing of X^5Y^5 with q_m^5 is therefore its X^5Y^5 coefficient. Direct expansion gives

  t^5-5t^3(1-t²)+(15/8)t(1-t²)²
  =(63t^5-70t^3+15t)/8=:P5(t).

Both vectors have norm one by SU2 invariance. Thus their Gram entries are P5(n·m), an identity for arbitrary axes. At t²=1/5 it simplifies to P5(t)=11t/25. On the diagonal P5(1)=1. The Gram matrix K of the six decics is consequently

  K=(14/25)I_6+(11/25)G.

Since G is positive semidefinite, K is positive definite: for any nonzero complex column a, a*Ka≥(14/25)||a||²>0. Hence the six decics are linearly independent. Their scalar multiples arising from the residual sections are independent too. Pullback by the surjective maps X→S and X→P1 detects linear relations, proving independence on S as well.

This is a universal inner-product calculation, not an evaluation of the actual HM map or a deduction from independence of unrelated ambient quintics.

## 4. Each cusp pair has one image

Let W be the now six-dimensional span of the decics. With the oriented-axis generators above, it is the signed permutation representation on the six axes: an element preserving an axis acts on q_n^5 by +1 or -1 according as it preserves or reverses its orientation. Equivalently W=Ind_D5^A5(sign), where sign is trivial on C5 and negative on the normalizer's involutions.

We need only three character values, which can be proved directly. The identity has trace six. An order-five element fixes exactly its own axis, positively, and permutes the other five, so its trace is one. An involution normalizes exactly two of the six Sylow-five subgroups: double-counting incidences gives 6·5/15=2, since all fifteen involutions are conjugate. On each of these two fixed axes it reverses orientation, because it conjugates the associated order-five rotation to its inverse. Thus its trace is -2.

Fix a C5 and an involution h in its D5 normalizer. Averaging the C5 action gives dim W^C5=(6+4)/5=2. Because every hc with c∈C5 is an involution, the trace of h on W^C5 is

  (1/5)Σ_(c∈C5)χ(hc)=-2.

The involution h has eigenvalues ±1, so it acts as -I on this two-dimensional subspace. The same is true on (W*)^C5.

The nonzero evaluation vector at either fixed point of C5 belongs to (W*)^C5, not merely to an unspecified eigenline. To check its character, lift a generator to diag(λ,λ^-1) in SU2, with λ^10=1. On the fiber of the degree-ten binary series at either fixed point its character is λ^10 or λ^-10, hence one. The involution h interchanges the two fixed points and acts scalarly on the relevant fixed subspace. Equivariance therefore identifies their projective evaluation vectors. This proves f(p_U^+)=f(p_U^-).

There are six distinct images. Each is fixed by its D5. There is no proper subgroup strictly between D5 and A5: a larger subgroup would have order20 or30, giving an action on three or two cosets, impossible for the simple group A5. Thus an image has orbit six or one. Orbit one would give an A5-invariant line in W*. Since A5 has no nontrivial one-dimensional characters, that would be a fixed vector. But W has no fixed vector: in a transitive signed permutation representation, a fixed vector's coordinate at one axis must be negated by a stabilizing reflection, hence zero, and transitivity forces all coordinates zero. The same holds for W*, which is self-dual via its invariant real positive form. Orbit one is therefore impossible.

## 5. The genus budget proves exactly six nodes

The curve Γ is integral, nondegenerate of degree ten in P5, and its normalization is P1 by PR571. Castelnuovo's arithmetic genus bound gives

  p_a(Γ)≤binom(2,2)·4+2·1=6,

because 10-1=2(5-1)+1. This is the ordinary bound for an integral curve; no smoothness of Γ is required. A public reference stating this form for integral curves is V. Di Gennaro, “The genus of curves in P4 and P5 not contained in quadrics,” §2(v):
https://link.springer.com/article/10.1007/s12215-022-00788-x
Only the classical bound recalled there is used, not that article's additional hypotheses for its new bounds.

The normalization formula p_a(Γ)=Σ_x δ_x applies since the normalization has genus zero. The six distinct images just found each have at least two branches, hence δ_x≥1. Thus equality holds in the bound: p_a(Γ)=6, these six points each have δ=1, and every other point has δ=0.

At a reduced curve singularity with two normalization branches, δ=1 forces an ordinary node. Explicitly, its completed local ring embeds in C[[u]]⊕C[[v]] and is contained in the subring of pairs with equal constant term. This latter subring already has colength one. Equality of colengths forces equality with that subring, which is C[[u,v]]/(uv). The six singularities are therefore ordinary nodes, with exactly two smooth transverse branches each. Their normalization preimages are precisely the six specified cusp pairs. Every other point is smooth and has one preimage.

## 6. The decic embedding is canonical

A nodal integral curve is Gorenstein. Thus ω_Γ is invertible of degree 2p_a-2=10. Write L=O_Γ(1), also of degree ten. Nondegeneracy gives h0(L)≥6, while Riemann–Roch yields h0(L)-h1(L)=10+1-6=5. Therefore h1(L)≥1. Serre duality supplies a nonzero section of the degree-zero invertible sheaf ω_Γ⊗L^-1.

On an integral projective curve such a section has an effective Cartier zero divisor of degree zero, hence no zeros, and trivializes its line bundle. Consequently L≅ω_Γ. Then h1(L)=h0(O_Γ)=1, so h0(L)=6. The six residual coordinates give the complete canonical embedding of this six-nodal rational curve of arithmetic genus six.

## 7. The smooth elliptic base does not descend to S

For this additional assertion use PR570 at e5e55594ef2b99cefb81c4c02b22cb45e1ff0025 and the precise normalization gluing established by Barth–Hulek–Moore, “Shioda's Modular Surface S(5) and the Horrocks–Mumford Bundle,” Proposition 9 and Proposition 10, printed pp.63–64:
https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

The source proves that different fibers have disjoint image curves except for pairs of singular pentagons sharing their five vertices. At each of the thirty resulting double points the normalization has two preimages on two distinct singular fibers. This property transfers to the actual primary surface through the exact coordinate-copy identification of PR570.

Suppose there were a morphism ψ:S→P1 with ψ∘ν=π. At any such double point x choose its two preimages y,z. Since they lie on distinct fibers, π(y)≠π(z). But ψ(ν(y))=ψ(x)=ψ(ν(z)), a contradiction. Thus π does not descend. The same contradiction applies after any automorphism of P1.

This proves non-descent of the particular elliptic fibration, not nonexistence of every morphism from S to P1. It does not assert a Stein-factorization statement for S→Γ, nor identify the whole primary degeneracy scheme with S at its boundary.

## Scope and verification

The new deductions are the universal Gram identity, actual restricted-section independence, the six cusp-pair identifications with exact nodal genus budget, canonical polarization, and the explicit non-descent consequence of the cited normalization gluing. They concern the primary surface and residual curve, not the separate fixed-beta surfaces. They do not prove full Q4, source-instance membership, higher target lifting, or algebraicity. No formal proof assistant or actual-source computation is claimed.
