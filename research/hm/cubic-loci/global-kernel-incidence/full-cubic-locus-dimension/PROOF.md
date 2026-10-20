# Exact dimension of the full cubic zero scheme

## Theorem

Work over C, with dim V=5, and let Z=Z(f)⊂V³ be the scheme-theoretic zero locus of the canonical trilinear operation. Import the structural hypotheses and conclusions of the three proof files named below. Then:

1. dim Z=10, its codimension in V³ is five, and its local dimension at the origin is ten.
2. Each of the three coordinate-zero affine ten-planes is an irreducible component of the underlying zero locus.
3. The independent-triple part has dimension at most ten. Its parts over kernel dimensions zero, one, two, three, four have respective upper bounds: empty, nine, nine, ten, ten.
4. Importing the twenty-independent-cubic conclusion of the extension-locus theorem, with its nonvanishing hypothesis discharged by the structural nonvanishing theorem, the ideal at the origin has height five and twenty minimal generators. The origin has embedding dimension fifteen, is singular, and is not a local complete intersection.

The dimension assertions concern the full scheme's Krull dimension, including all its underlying components; they do not assert reducedness, equidimensionality, a component count, or generic multiplicities. They do not determine whether the independent-triple part actually attains dimension ten.

## Imports and evidence boundary

The imports are:

- [the general three plane kernel manuscript](../general-three-plane-kernel/PROOF.md): the universal map T_W:Schur_(2,1)W→J3, its kernel K_W⊂sl(W) after trivializing det W, the absence of nonzero rank-one elements of K_W, dim K_W≤4, and the global spectral-incidence/eigenline description of independent zero triples.
- [the ap three plane cubic frames manuscript](../../two-and-three-plane-zeros/ap-three-plane-cubic-frames/PROOF.md): the existence of an arithmetic-progression three-plane for which dim K_W=1, established there by structural weight separation.
- [the two plane cubic zero scheme manuscript](../../two-and-three-plane-zeros/two-plane-cubic-zero-scheme/PROOF.md): zero triples of span at most two are exactly triples of span at most one or with a zero input.
- For statement 4, [the extension locus singularity manuscript](../../repeated-input-slice/extension-locus-singularity/PROOF.md): the independent twenty-cubic and local-generator conclusions. Its nonzero-scalar hypothesis is discharged by [the cubic structural nonvanishing manuscript](../../cubic-structural-nonvanishing/cubic-structural-nonvanishing/PROOF.md), Sections 5 and 7, which prove nonvanishing and surjectivity of the linearized image structurally.

All arguments here use abstract linear spaces, vector bundles, universal invariant polynomials, and dimension theory. No actual HM/source/model matrices, products, ranks, points, jets, residue values, or Massey evaluations are computed. The AP theorem is imported as a structural theorem, not reconstructed by evaluation. 

## 1. A four-dimensional constant-rank-two space is impossible

**Universal lemma.** A complex linear subspace L⊂Hom(C³,C³) in which every nonzero element has rank exactly two has dimension at most three.

Suppose otherwise and restrict to a four-dimensional subspace. On P(L)=P³ the tautological universal linear map is

    φ: O³ → O³(1).

At every geometric point it has rank two. The rank-at-most-one closed locus is empty, and all three-by-three minors vanish identically because they vanish at every point of the reduced base. On open charts where a two-by-two minor is invertible, elementary bundle operations split off an identity block, with the remaining block zero. Thus its kernel and cokernel are line bundles, not merely coherent sheaves. Since Pic(P³)=Z, they are O(a) and O(b) for integers a,b. Consequently

    0 → O(a) → O³ → O³(1) → O(b) → 0

is exact. Its K-theory relation, followed by the Chern character in CH*(P³)_Q=Q[H]/(H⁴), is

    exp(aH) − exp(bH) = 3 − 3 exp(H).

The coefficients of H, H², H³ give, respectively,

    a−b=−3,   a²−b²=−3,   a³−b³=−3.

The first two imply a+b=1, hence a=−1 and b=2. But then a³−b³=−9, contradicting the third equation. This proves the lemma.

**Corollary.** If dim K_W=4, the restricted determinant h_W=det|K_W is not the zero polynomial.

Indeed, if h_W were zero, every nonzero element would be singular. Its rank cannot be one by the imported rank-one exclusion and cannot be zero because it is nonzero. Every nonzero element would have rank exactly two, contradicting the lemma. Trivializing det W merely rescales the endomorphism and does not affect this conclusion.

## 2. Grassmannian kernel strata

Put G=Gr(3,V); it is irreducible of dimension 3(5−3)=6. On G let E=Schur_(2,1)S, a bundle of rank eight, and let

    T:E → J3⊗O_G

be the imported global bundle map. For 0≤k≤4 let G_k be its determinantal stratum with kernel dimension exactly k (rank exactly 8−k). These finitely many locally closed strata cover G by the imported uniform bound. Their underlying reduced schemes suffice for all dimension estimates; the determinantal scheme structures may also be retained.

The locus

    D={W:dim K_W≥2}={W:rank T_W≤6}

is closed by minors. It is proper because the AP theorem supplies a three-plane of rank seven. Therefore dim D≤5. In particular,

    dim G_0, dim G_1 ≤6,
    dim G_k ≤5 for k=2,3,4.

No generic kernel dimension is asserted: the nonempty rank-at-least-seven open can contain rank eight as well as rank seven.

## 3. Spectral fibers and independent triples

Let Z^(3) be the intersection of Z with the open locus of triples spanning a three-plane. The span morphism sends it to G; a frame of the tautological bundle gives precisely such a triple, so this is the zero-frame scheme in the imported theorem.

On G_k, the spectral incidence has geometric fiber

    X_W = { [A]∈P(K_W): h_W(A)=0, q_W(A)≠0 },
    q_W(A)=tr(A²).

For k=0 this is empty. For k=1 its dimension is at most zero. For k=2 or k=3, its dimension is at most k−1, using only its containment in P(K_W). For k=4, Section 1 says h_W is a nonzero homogeneous cubic on a four-dimensional space. Its projective zero scheme has dimension two: a nonzero positive-degree polynomial is a nonzerodivisor in the polynomial ring, and its projective hypersurface in P³ has dimension two. Removing q_W=0 cannot increase dimension, so dim X_W≤2 (and X_W may be empty).

The independent-zero-frame scheme over X has a finite étale degree-two oriented eigenline cover followed by a Zariski locally trivial (G_m)³-bundle, as proved in the imported incidence theorem. Consequently the fiber over a fixed W, when nonempty, has dimension dim X_W+3. Nilpotents do not affect this calculation. Thus the span fibers have upper bounds

    k=0: empty;
    k=1: 3;
    k=2: 4;
    k=3: 5;
    k=4: 5.

For a finite-type morphism, dimension is at most base dimension plus the largest geometric-fiber dimension. Applying this on each G_k gives

    dim(Z^(3)|G_1)≤6+3=9,
    dim(Z^(3)|G_2)≤5+4=9,
    dim(Z^(3)|G_3)≤5+5=10,
    dim(Z^(3)|G_4)≤5+5=10.

Empty strata are ignored. The finite stratification therefore gives dim Z^(3)≤10. These estimates do not require flatness or a global kernel bundle across rank jumps; the imported global incidence construction, or its restriction to the constant-rank strata, supplies the finite-type morphisms used here.

## 4. Dependent triples and the full dimension

Let R_≤2⊂V³ be the rank-at-most-two determinantal locus. By the imported two-plane theorem, the underlying support of Z∩R_≤2 is the union of the three coordinate-zero ten-planes and the rank-at-most-one locus D_1 for a 5-by-3 matrix. The latter is the affine cone over P⁴×P² and has dimension 4+2+1=7. Hence this closed dependent part has dimension ten. Alternatively, its exact-rank-two part consists of the three independent-pair opens of those ten-planes, while its remaining part has dimension seven.

The underlying space of Z is partitioned into its dependent closed part and the independent open part. A finite locally closed stratification of a noetherian finite-type scheme has dimension equal to the maximum of its strata dimensions. Section 3 and the preceding paragraph therefore imply dim Z≤10. Trilinearity gives scheme-theoretic inclusion of every coordinate-zero ten-plane, so dim Z≥10. Thus dim Z=10 and codim_(V³) Z=15−10=5.

Each coordinate-zero plane is a closed irreducible subset of dimension ten. It lies in an irreducible component of Z. Since every component has dimension at most ten, equality of dimensions forces that component's underlying space to be exactly the plane: a proper closed irreducible subset of an irreducible finite-type variety has strictly smaller dimension. This proves statement 2 without claiming that these are the only components.

At the origin, one coordinate plane supplies a quotient of the local ring of Z of dimension ten, so the local dimension is at least ten. Localization cannot increase the global dimension, so the local dimension is exactly ten as well.

## 5. The local ideal and complete-intersection obstruction

Using the extension-locus theorem together with the structural nonvanishing theorem, let S be the fifteen-variable coordinate polynomial ring, m its homogeneous maximal ideal, R=S_m, and I the cubic defining ideal. That theorem gives

    μ_R(IR)=20,     IR⊂(mR)³,

and embedding dimension fifteen for A=R/IR. Section 4 gives dim A=10. Since R is a regular local ring of dimension fifteen, its dimension formula gives height_R(IR)=15−10=5. Thus A is singular, and IR cannot be generated by a regular sequence: a complete-intersection ideal would have minimal number of generators equal to height, whereas 20>5. The imported theorem also explains why this excludes the intrinsic local-complete-intersection property, not only this presentation.

The original nonzero-scalar hypothesis of the extension-locus theorem has already been discharged by [the cubic structural nonvanishing manuscript](../../cubic-structural-nonvanishing/cubic-structural-nonvanishing/PROOF.md). Thus the twenty-generator conclusion applies to the actual canonical operation. No scalar value is computed here or needed for this deduction.

## 6. A necessary condition for additional top-dimensional components

One further exclusion follows without new input. Refine G_3 according to whether h_W is identically zero. This is a closed condition within G_3: on that stratum K is a rank-three bundle and the restriction of determinant is a section of an appropriate twisted Sym³ K* bundle, whose zero section imposes the condition.

Where k=3 and h_W is nonzero, its zero locus in P² has dimension one, so the independent-frame fiber has dimension at most four and that stratum contributes dimension at most 5+4=9. Together with the previous bounds for k≤2, this proves:

Any ten-dimensional irreducible component whose generic triple is independent must generically lie either over k=4, or over k=3 with h_W identically zero. In either case its span image has dimension five, and its generic spectral fiber has dimension two.

For precision, take the unique dense locally closed piece of the component arising after these finite refinements; its span-image closure and generic fiber obey the dimension formula. A ten-dimensional piece with fibers bounded by five must have image dimension at least five, while the proper degeneracy locus bounds it by five. Its generic frame fiber therefore has dimension five, equivalently spectral dimension two. This is a necessary condition only, not an existence statement or exclusion of smaller components.

In the k=3, h_W=0 alternative, K_W is itself a three-dimensional constant-rank-two linear space by the same rank-one exclusion. The universal P³ obstruction leaves this possibility open; the P² Chern-character calculation has no degree-three equation and hence does not contradict it.
