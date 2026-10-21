# Two-pentad transversality from exceptional edge support

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected HM/source coefficient, coordinate, derivative, matrix, rank evaluation, numerical scan, or computer algebra is used. The only symbolic arithmetic is universal order-five character geometry.

## 1. Inputs and proposed conclusion

In this note C denotes H1(D), not the length540 operator quotient called C in PR616.

Pinned inputs in Akilleez-QA/read-em-and-weep:

- PR617, 7f240b04bc4f03cfe73ffd64cae17c453dd895e6, research/hm/cubic-scalar-constraints/PROOF.md, especially Sections 2 and 5: for distinct pentads G,H, the twenty-dimensional first-jet images W_G,W_H in N=Hom(S,C), where C=H1(D), have intersection dimension either 0 or 16. Dimension zero is equivalent to both normalization scalar gates being nonzero.
- PR616, cf7a16cff86cf6cd7ee982b5fa6c309835d25eac, research/hm/cubic-residual-channels/PROOF.md, Sections 2, 6, 8, 9: C is the irreducible five-dimensional Heisenberg module with faithful central character c^(-3); S has dimension10; each inclusion F_G=H0(O_ZG(3))->C is an isomorphism; the individual center first-jet maps are injective; W_G is their sum in Hom(S,C).
- PR610, e4898406ed2552dd40e9695f9fda3d9f1d270301, research/hm/cubic-joint-characters/PROOF.md, Sections 4–5: for any direction, the twenty nonzero repeated-index exceptional tensors give ten distinct one-dimensional joint-weight spaces of S*. The two representatives of each weight are (i,j) and (2i-j,3i-2j).

We prove the new geometric restriction dim(W_G intersect W_H)<=8. Together with the pinned 0-or-16 dichotomy this proves W_G intersect W_H=0, both normalization gates nonzero, rank(b_N)=48, and the embedded tangent upper bound147. Neither descent gate is determined. The original-source/full-adjoint/algebraicity boundary of PR1 at 2531056eae05fdf31e8fb4ca3affc5907073ad73 is unchanged.

## 2. Five cohomology fiber lines and Fourier uncertainty

For a direction G, denote by c_(G,i) the image in C of the one-dimensional fiber at its i-th center under F_G->C. These five lines form a direct-sum decomposition of C. They are precisely its five G-eigenlines: the chosen order-five lift acts on the fiber at L_i by zeta^(-3i), and these characters are distinct.

For any distinct G,H, the two decompositions are Fourier-related up to nonzero rescalings and permutations. This assertion concerns an arbitrary irreducible Heisenberg representation, not coefficients of the cubic map. Indeed choose order-five lifts g,h of independent directions in the representation C. Their commutator is a primitive fifth root lambda because the central character is faithful. Starting with a g-eigenvector e_0, the vectors e_j=h^j e_0 are a g-eigenbasis. The h-eigenvectors are the five sums sum_j lambda^(aj)e_j, up to reindexing. Any other choice of generators or eigenvectors only rescales or permutes these bases.

Consequently, if I is a set of at most three G-fiber lines and J a set of at most two H-fiber lines, then

    span(c_(G,i):i in I) intersect span(c_(H,j):j in J) = 0.   (1)

For a direct universal proof, a vector in the second span vanishing in the G-coordinates outside I gives at least two equations in at most two coefficients. Any one-by-one or two-by-two Fourier minor is nonzero: the latter is a root-of-unity factor times 1-lambda^((a-b)(c-d)), with both differences nonzero modulo5. Thus all those coefficients vanish. This is a special case of the universal uncertainty inequality |support_G(v)|+|support_H(v)|>=6. Only the two-column case is needed here.

## 3. The geometric edge-support lemma

Fix H and label its five centers by i in F5. Let E_(H,i) subset S* be the four-dimensional image of the first-jet map at center i, after trivializing that center's O(3) fiber. Its projectivization is the exceptional P3 image. The subspace itself and all ensuing support statements do not depend on this trivialization.

By PR610 the four tangent directions from i to j, j != i, have nonzero image lines q(L_i^2 L_j) in S*. They belong to four distinct joint weights. Their span is E_(H,i), since the four source tangent lines span the tangent space and the first-jet map is injective.

The only other repeated-index representative sharing the line q(L_i^2 L_j) is based at k=2i-j. For i != j, this k differs from i. Conversely for every unordered pair {i,k} of distinct centers, choosing j=2i-k gives exactly that shared line. Hence the ten joint-weight lines form a basis decomposition

    S* = direct-sum_(unordered {i,k}) ell_(i,k),
    E_(H,i) = direct-sum_(k != i) ell_(i,k).                  (2)

This is the complete graph on five vertices: each exceptional tangent image is the span of its four incident edge lines. This geometric first-jet incidence is the new input not encoded by abstract normalizer equivariance of b.

Let s_(i,k) in S denote any vector dual to a nonzero generator of ell_(i,k), with respect to the direct-sum decomposition (2). Every f in W_H has its i-th cohomology row in E_(H,i), by the definition of the postulation derivative. Thus (2) gives the support restriction

    f(s_(i,k)) belongs to c_(H,i) + c_(H,k).                  (3)

Here a sum of lines means their two-dimensional span. The coefficients of these vectors are neither computed nor constrained; either can be zero. Equation (3) is simply the tensor support identity W_H=direct-sum_i c_(H,i) tensor E_(H,i), interpreted in C tensor S*=Hom(S,C).

## 4. Mixed fiber-plane exclusion

Let I be any at-most-three centers of G, and put C_(G,I)=span(c_(G,i):i in I). We claim

    W_H intersect Hom(S,C_(G,I)) = 0.                        (4)

For f in that intersection, each edge-basis input s_(i,k) has output simultaneously in C_(G,I) and in c_(H,i)+c_(H,k), by (3). Equation (1) forces every such output to vanish. The ten s_(i,k) form a basis of S, hence f=0.

This is a new geometric support exclusion: a nonzero motion of one pentad cannot have its entire postulation image supported on any three cohomology fibers from another pentad. It does not use the unknown scalar gates.

## 5. Intersection bound and resolution

Take any three-element I among the G centers. In the decomposition

    W_G = direct-sum_(i in Z_G) c_(G,i) tensor E_(G,i),

project onto the two summands indexed by the complementary centers. The target has dimension8. Its restriction to W_G intersect W_H is injective: its kernel lies in W_H intersect Hom(S,C_(G,I)), which is zero by (4). Therefore

    dim(W_G intersect W_H) <= 8.                             (5)

The pinned dichotomy says the same dimension is either0 or16. Thus it is0 for every pair of distinct pentads. PR617 Section5 now implies both beta_1 and beta_4 are nonzero and q=2. PR616 gives rank(b_N)=24q=48 and full rank parameter r in {2,3,4}. Accordingly

    dim ker b in {0,24,48},
    dim T_embedded in {99,123,147},
    dim T_embedded <=147.

This conclusion is a geometric proof of nonvanishing, not an evaluation of either scalar. It does not determine the descent scalars beta_2,beta_3, smoothness, higher-order integrability, original-source algebraicity, or a full-adjoint assertion.

## 6. Immediate next reduction

The normalization image is exactly N_nt: it is contained there by equivariance and absence of source invariants, and both spaces now have dimension48. Thus coker(b_N) is canonically N^U, of dimension2, using the canonical averaging decomposition N=N^U direct-sum N_nt. The kernel is the direct sum of the two twenty-four-dimensional normalizer irreducibles characterized at a fixed nontrivial U-character by shear weights2 and3.

The canonical residual descent map b_J:ker b_N->J now has source dimension48. On each nontrivial U-character its source has exactly shear weights2 and3 and its target J has exactly the matching weights, once each. Its image has zero component in the canonical invariant twelve-dimensional subspace J^U; the remaining target J_nt is precisely the sum of the matching two twenty-four-dimensional irreducibles. Therefore the only remaining possible embedded tangent dimensions correspond to zero, one, or two nonzero descent scalar channels. All normalization ambiguities have been removed. Further improvement requires new geometry of the simultaneous singular-section lines K_sigma and their gluing discrepancies, not another normalization-postulation rank test.
