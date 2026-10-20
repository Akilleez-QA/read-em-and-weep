# Actual cubic application of constant rank kernel nets

The preceding universal arguments are not duplicated. Sections1–4 are proved in unit01; its P³ obstruction is also proved there. The actual spectral/eigenline construction is proved in unit09.

## Imported fixed-kernel hypotheses

For Sections5–6, let K=K_W⊂sl(W), dim W=3, be three-dimensional and rank-one-free with det|K=0. Put q(A)=tr(A²) and X=P(K)\{q=0}. Unit01 proves its skew-symmetric normal form and nondegenerate q. Section7 separately considers four-dimensional rank-one-free K with q nonzero, as expressly stated there.

## 5. Oriented cover and the fixed-plane frame scheme

Now import the spectral/eigenline theorem of [the general three plane kernel theorem](../../../global-kernel-incidence/general-three-plane-kernel/PROOF.md) for a fixed W whose structural kernel satisfies the hypotheses. Trivialize det(W); on X the universal endomorphism is valued in L*, where L=O(−1). Its oriented cover chooses a nowhere-zero λ∈L* with λ²=Q/2, where Q is the universal trace-square section. Normalizing the universal endomorphism by λ identifies this cover with

    X~ ≅ { N∈K : q(N)=2 }.

Explicitly, at a point represented by a nonzero A∈K, write λ(A) for the evaluation of λ on its tautological generator. The normalized endomorphism N=A/λ(A) is independent of the choice of A and satisfies q(N)=2. Conversely such an N determines [N] and the functional λ on CN with λ(N)=1. These constructions are regular and inverse. The deck involution is N↦−N, and the projection is N↦[N]. The finite étale degree-two property also follows directly from the imported construction.

The affine quadric q=2 is smooth because q is nondegenerate and its gradient cannot vanish on a nonzero level. It is irreducible: a reducible polynomial q−2 of degree two would be a product of affine linear polynomials, whose degree-two homogeneous part has quadratic rank at most two, contradicting rank q=3. Thus X~ is a smooth irreducible surface.

The imported scheme identification expresses the independent zero-frame scheme over this fixed W as

    S_+^× ×_(X~) S_0^× ×_(X~) S_-^×,

where the three eigenline bundles correspond to eigenvalues +1, 0, −1 of N. It is a Zariski locally trivial principal (G_m)³-bundle. Local triviality proves smoothness and dimension 2+3=5, and also irreducibility: the inverse image of each nonempty trivializing open is irreducible, and any two such inverse images intersect because X~ is irreducible. The bundle is nonempty and exhausts the fixed-W independent zero scheme scheme-theoretically.

This does not assert that the relative frame space over a varying stratum is smooth, reduced, or globally trivial. Those properties can still depend on the geometry and scheme structure of the unknown base.

## 6. Consequence for the full dimension theorem

The full-cubic-dimension proof leaves two possible sources for a ten-dimensional component with generically independent triples: k=4, or k=3 with restricted determinant identically zero. In the second alternative, the present theorem removes any remaining uncertainty about the individual geometric frame fibers: each is smooth irreducible of dimension five, and its spectral incidence is a projective plane minus a smooth conic. The dimension and nonemptiness of the actual locus of such W remain unproved. Accordingly this classification alone neither proves nor excludes an additional ten-dimensional component of the full cubic zero scheme.

## 7. Existence for four-dimensional kernels when q is nonzero

**Corollary.** Let K⊂sl(W) be four-dimensional and contain no nonzero rank-one endomorphism. If q=tr(A²)|K is not identically zero, then there exists [A]∈P(K) with det A=0 and q(A)≠0. Thus an actual structural kernel of dimension four with nonzero restricted q admits independent zero frames.

Write h=det|K. The constant-rank P³ obstruction in [the full cubic locus dimension theorem](../../../global-kernel-incidence/full-cubic-locus-dimension/PROOF.md) shows h≠0: otherwise every nonzero element of K would have rank two. If q has rank at least three, the polynomial criterion in [the general three plane kernel theorem](../../../global-kernel-incidence/general-three-plane-kernel/PROOF.md) already gives existence.

Suppose instead that q has rank one or two, and assume for contradiction that no such [A] exists. The same polynomial criterion says that every irreducible factor of h divides q. Since q has rank at most two over C, its irreducible factors are linear. Hence h has a linear factor ℓ. The hyperplane L=ker(ℓ)⊂K is three-dimensional, has det|L=0, and contains no nonzero rank-one endomorphism. The classification above forces q|L to have rank three. Restriction cannot increase the rank of a quadratic form, contradicting rank(q|K)≤2. This proves the corollary.

More generally, if any rank-one-free subspace K⊂sl(W) contains a three-dimensional subspace L on which determinant vanishes identically, then q|L has rank three, so rank(q|K)≥3 and the spectral incidence of K is nonempty. Indeed the nonempty incidence already occurs inside P(L).

The four-dimensional case q≡0 is expressly outside this corollary. No assertion here excludes that possibility or claims existence of independent zero frames in it.
