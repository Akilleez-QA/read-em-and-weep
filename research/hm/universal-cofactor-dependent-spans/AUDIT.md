# Independent audit: dependent operator spans

## Status

**Pass.** I read the complete companion `PROOF.md` after independently deriving the arguments below. Its universal trace-kernel identity, all sharp rank ranges, rectangular transversality, local minor-ideal models, support-incidence dimensions, irreducibility, minimum-rank classifications, and original-five-tuple exact sequence are sound. Here E = V ⊗ sl(U) is the definition of the abstract model. No module identification or multiplication-adjointness statement is used; the five-tuple calculation concerns ordinary kernels and cokernels.

Throughout, the ground field is C, dim U = 2, dim V = 5, and an element of E is viewed as a map U → V ⊗ U. Let J ⊂ E have dimension d, let W = J(U), and write r = dim W. The support P is the smallest subspace of V with W ⊂ P ⊗ U; write s = dim P. Equivalently, P is the smallest support of J inside V ⊗ sl(U).

## 1. Exact trace-kernel dimension

For any subspace W ⊂ V ⊗ U, define

    E(W) = E ∩ Hom(U,W).

The vector-valued trace map

    tr_V : V ⊗ End(U) → V

has kernel E. Its restriction to Hom(U,W) = W ⊗ U* sends a pure tensor w ⊗ λ to (id_V ⊗ λ)(w). Its image is therefore exactly the coefficient support P of W. Rank-nullity gives, without genericity assumptions,

    dim E(W) = 2r − s.

The support of J equals the support of W: inclusion of J in P ⊗ sl(U) implies inclusion of every evaluation in P ⊗ U; conversely, all values lying in P ⊗ U forces every matrix coefficient of every member of J to lie in P.

Since J ⊂ E(W) and W ⊂ P ⊗ U,

    d ≤ 2r − s,     r ≤ 2s.

Thus

    d ≤ floor(3r/2),     r ≥ ceil(2d/3).

No extra inequality such as s ≤ r is needed or generally implicit in the argument.

## 2. Exhaustive minimum-rank classification

The minima for d = 1,2,3,4,5 are respectively r = 1,2,2,3,4. In the following descriptions P is an arbitrary subspace of V of the specified dimension. “Full support” means that W is contained in no P' ⊗ U for a proper P' ⊂ P. All J and W mentioned are vector subspaces, not projective subspaces.

### d = 1, r = 1

Necessarily s = 1. Write P = Cv. Then J = C(v ⊗ N), where N is a nonzero rank-one traceless endomorphism of U. Equivalently N is nonzero nilpotent, with im N = ker N. Conversely every such J has evaluation rank one.

### d = 2, r = 2

There are precisely two support cases:

- s = 1: W = P ⊗ U and J is any two-dimensional subspace of P ⊗ sl(U).
- s = 2: choose any two-dimensional W ⊂ P ⊗ U of full support and set J = E(W). The trace formula gives dim J = 2.

In the first case the lower bound prohibits rank one. In the second case, the lower bound forces J(U) to have dimension at least two, so J(U) = W. Therefore there are no unstated evaluation-generation conditions on the parameter W.

### d = 3, r = 2

The inequalities force s = 1 and dim E(W) = 3. Hence

    W = P ⊗ U,     J = P ⊗ sl(U).

Conversely this gives rank two. In particular rank two holds exactly for J = v ⊗ sl(U) with nonzero v, interpreted using the line Cv.

### d = 4, r = 3

The inequalities force s = 2 and dim E(W) = 4. Choose any support plane P and any hyperplane W ⊂ P ⊗ U; set J = E(W). Every such hyperplane has full support, since a proper support line could accommodate dimension at most two. The lower bound forces evaluation rank at least three, hence J(U) = W. These are all possibilities.

### d = 5, r = 4

The inequalities give 2 ≤ s ≤ 3. Both cases occur:

- s = 2: W = P ⊗ U and J is any hyperplane in the six-dimensional P ⊗ sl(U).
- s = 3: choose any four-dimensional W ⊂ P ⊗ U of full support and set J = E(W). The trace formula gives dim J = 5.

In both cases the lower bound forces evaluation rank four. In the first case support cannot drop to a line, because a line supports an E-space of dimension only three. In the second case evaluation equals the prescribed W, hence has exactly its prescribed support.

All these parametrizations are injective at the level of the stated data: P is recovered as the support of J and, wherever W is an independent parameter, it is recovered as J(U).

## 3. Optional orbit refinements

Under abstract changes of V coordinates and conjugation on U, the d = 2, r = 2 cases have five types. For s = 1, a two-plane in sl(U) is classified by whether its trace-pairing orthogonal line is semisimple or nilpotent. For s = 2, a two-plane W in P ⊗ U has three types: a ruling P ⊗ u; a secant spanned by p₁ ⊗ u₁ and p₂ ⊗ u₂ with both pairs independent; or a tangent spanned by p₁ ⊗ u₁ and p₁ ⊗ u₂ + p₂ ⊗ u₁. This follows from the restriction of the determinant quadric to the projective line P(W): identically zero, two distinct zeros, or one double zero. Full P-support excludes the other ruling type.

For d = 4, r = 3 there are two types, according to whether the nonzero tensor defining the hyperplane W ⊂ P ⊗ U has rank one or two.

These abstract coordinate changes are not assertions of geometric symmetries of any separate geometric construction.

## 4. Audit of the stronger all-rank geometry

Let G_d = Gr(d,E), and let S_(d,r) be the exact evaluation-rank-r stratum. The following stronger statements also check out independently.

### Transversality at every exact rank

Put R = ker β_J and Q = coker β_J, with dimensions 2d − r and 10 − r. Let p : V ⊗ U → Q be the quotient. The normal derivative is

    Hom(J,E/J) → Hom(R,Q).

For completeness, its surjectivity can be checked by duality. The annihilator of the image of E/J → Hom(U,Q) consists of maps A : Q → U such that A p = ℓ ⊗ Id_U for some ℓ ∈ V*. This follows because the annihilator of V ⊗ sl(U) is V* ⊗ C·Id_U. For q : Q → R annihilating the normal derivative, write q(z) = Σ a_j ⊗ Q_j(z) in a basis of J. Independent variations of the a_j imply

    Q_j p = ℓ_j ⊗ Id_U.

Since q lands in R, β_J q = 0. Composing with p gives Σ a_j ⊗ ℓ_j = 0 in the naturally embedded E ⊗ V* ⊂ End(V ⊗ U). Independence of the a_j gives all ℓ_j = 0, and surjectivity of p gives Q_j = 0. Thus q = 0 and the normal derivative is onto.

Consequently every nonempty S_(d,r) is smooth and pure dimensional of dimension

    D(d,r) = d(15−d) − (2d−r)(10−r).

A Schur complement gives the usual rectangular determinantal analytic local model, so this assertion includes transversality to the standard rank stratification.

### Support incidence and unique maximal support

For fixed s, choose P ∈ Gr(s,V), choose W ∈ Gr(r,P ⊗ U) with full P-support, and then choose J ∈ Gr(d,E(W)) whose evaluation image is W. Both full-support and evaluation-generation are open conditions. The trace-kernel formula makes E(W) a vector bundle of constant rank 2r − s on the base. Thus each nonempty incidence is irreducible, of dimension

    I(d,r,s) = s(5−s) + r(2s−r) + d(2r−s−d).

The same dimension holds for its image, because P and W are uniquely recovered from J on the exact-rank locus. Feasibility requires s ≤ min(5,2r−d). Direct expansion gives

    I(d,r,s) − D(d,r) = (5−s)(s+d−2r) ≤ 0.

Equality occurs for exactly one feasible value of s, namely s₀ = min(5,2r−d). All smaller s give strict inequality. Given nonemptiness of S_(d,r), its pure dimension D and the finite support stratification force the s₀-incidence to be nonempty. Every component of S_(d,r) has dimension D, and only the unique irreducible s₀-image can have that dimension. Therefore S_(d,r) is irreducible and has generic support s₀.

### Nonemptiness and closed rank loci

All integers ceil(2d/3) ≤ r ≤ 2d occur for 1 ≤ d ≤ 5. For d ≤ r ≤ 2d, use d independent V-slots, putting a nonzero nilpotent E in 2d−r slots and an invertible traceless H in r−d slots. Their evaluation images lie in distinct V-slots and have total dimension r. The only remaining pairs are (d,r) = (3,2), (4,3), (5,4), witnessed by a full sl(U) in one V-slot and respectively zero, one, or two extra E generators in independent slots.

To infer irreducibility of the CLOSED locus rank β_J ≤ r, an additional argument beyond smoothness of the exact stratum is essential. Either of the following completes it:

1. The standard graph-intersection bound for a pulled-back determinantal variety says every component has dimension at least D(d,r). Lower exact-rank strata have strictly smaller dimension, because D(d,r) − D(d,r−1) = 2d + 11 − 2r > 0 for the relevant range. Hence no extra component can be supported entirely in lower rank.
2. At any lower exact rank t, the transverse Schur-complement model permits arbitrarily small residual matrices of rank r−t. Thus every rank-t point lies in the closure of the rank-r stratum.

Either proves that the closed rank≤r locus is the closure of its unique irreducible rank-r stratum and has dimension D(d,r). These arguments concern the underlying closed locus; scheme-theoretic statements require the local determinantal model, rather than incidence dimensions alone.

## 5. Final companion-proof review


The final text includes the necessary determinantal component-dimension argument for passing from exact rank to the closed rank locus. Its consecutive-rank dimension difference is correct. The generic maximal-support condition is open: support is the rank of the coefficient-contraction map for J, and all lower evaluation ranks have support bounded above by the same maximum.

The two d = 4 compression types are correct. For rank-one defining covector, write W = Cp ⊗ U + Cq ⊗ L; then E(W) = Cp ⊗ sl(U) + Cq ⊗ n_L. For rank-two defining covector, its map P → U* is injective, so no full p ⊗ U lies in W. The corresponding rank-one and rank-two hyperplane families have the stated dimensions eight and nine.

For the original five-tuple, tensoring the surjection A → J with U and taking the inverse image of ker β_J proves the canonical short exact sequence in Section 6. Its dimension decomposition does not assert a canonical splitting. Subtracting the complete rank intervals from ten gives exactly 8–9, 6–8, 4–8, 2–7, and 0–6; d = 0 gives ten. The additional support bound r ≥ ceil((d+s)/2) follows directly from d ≤ 2r−s. No correction to the final companion proof is required.

The final additions were also checked: the five abstract d = 2 orbit types agree with Section 3 of this audit, and the singular-locus formula for every proper rank locus is correct. At lower exact rank t < r < 2d, the residual bound k = r−t satisfies 0 < k < min(10−t,2d−t), so the defining minors have no linear terms at zero while the residual variety has positive codimension. At exact rank r the residual bound is zero, giving a smooth coordinate subspace. Thus Sing R_(d,r) = R_(d,r−1), with empty lower locus below the minimum, and every minimum-rank locus is smooth. The whole-Grassmannian case r = 2d is correctly excluded.
