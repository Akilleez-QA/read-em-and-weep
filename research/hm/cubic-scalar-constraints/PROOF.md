# Pentad-supported deformation theorem and the exact symmetry-only frontier

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected HM/source coefficient, matrix, point evaluation, rank computation, scan, or computer algebra is used. The Fourier calculation below concerns the universal cyclic group of order five only.

## 1. Input and contribution

Input: PR616, commit cf7a16cff86cf6cd7ee982b5fa6c309835d25eac, research/hm/cubic-residual-channels/PROOF.md, especially Sections 5, 7–9. Its pinned inputs and the PR1 original-source/full-adjoint scope boundary at commit 2531056eae05fdf31e8fb4ca3affc5907073ad73 remain unchanged.

Let Dirs be the six directions of U=F5^2. Write Z_G for the eigenline pentad of G, T_G=direct-sum_(z in Z_G) T_z P(A), T=direct-sum_G T_G, and P=pgl(A) inside T via the injective evaluation map. Put H=T/P. The canonical residual obstruction is b:H->E, with quotient b_N:H->N. Its character blocks have four shear weights 1,2,3,4, each once, in both source and target. The normalization target has weights 1,4; the descent target has weights 2,3. Set

    r = number of nonzero full gates, 1 <= r <= 4,
    q = number of nonzero normalization gates, 1 <= q <= 2.

For I subset Dirs of size m, let T_I=direct-sum_(G in I) T_G and H_I=image(T_I->H). These are actual supported center-motion spaces, not abstractly chosen subspaces of H.

We prove an exact geometric support theorem, a two-pentad lifting criterion for simultaneous normalization nonvanishing, and a precise limitation on further symmetry-only arguments. We do not determine r or q for the actual geometric map.

## 2. A universal order-five Fourier lemma

Let zeta be any primitive fifth root, and let F be the character table with entries F_(a,j)=zeta^(aj), a,j in F5. Every square minor of F is nonzero.

For order one this is immediate. For two distinct row labels a,b and column labels c,d, the minor is a nonzero root of unity times

    1 - zeta^((a-b)(d-c)),

which is nonzero because F5 is a field. Orthogonality gives F^(-1)=(1/5) conjugate(F). The complementary-minor identity for an invertible matrix identifies each minor of order three or four, up to a nonzero factor and sign, with a complementary minor of order two or one of F^(-1). Those have just been proved nonzero. The order-five determinant is nonzero by orthogonality. Thus every rectangular subtable with a rows and k columns has rank min(a,k).

This is a uniform symbolic character proof, not a calculation on the geometric obstruction or on a selected source instance.

## 3. Source coordinates forced by the cyclic stabilizer

Fix a nontrivial character chi of U and let K=ker chi. By PR616, (T_G)_chi is a line if G differs from K and is zero if G=K. The intrinsic shear h fixing chi cyclically permutes the five contributing directions and has order five. Choose any nonzero vector e_0 in one contributing line and put e_j=h^j e_0. This gives an orbit basis; no tangent vector is evaluated at a selected point.

The line P_chi is h-fixed. Since evaluation is injective and the fixed space in the cyclic regular representation is one-dimensional,

    P_chi = span(e_0+e_1+e_2+e_3+e_4).

In particular its components in all five contributing direction lines are nonzero. Therefore

    dim(T_I intersect P) = 0 for 0 <= m <= 4,
                          4 for m=5,
                         24 for m=6.                         (1)

Indeed P_chi lies in T_I exactly when all five directions other than K belong to I. There are four nontrivial characters with any specified kernel K.

In the orbit basis the weight projections are the Fourier functionals, up to nonzero factors and the harmless choice of Fourier sign. The composite T_chi->H_chi->E_chi is zero on weight zero and on the vanishing scalar gates; on each remaining weight it is a nonzero map between lines. Consequently its restriction to any k direction lines has rank min(k,r), by Section 2. This remains true if the active weights are transported differently for different chi: only their cardinality matters. The same assertion holds for b_N with r replaced by q.

## 4. Exact supported-kernel formula

Let a=r for the full obstruction and a=q for normalization. Write B_a for the corresponding map on H, and let d_m be the right side of (1). Then

    dim ker(B_a restricted to H_I)
      = 4m max(m-1-a,0) + 4(6-m) max(m-a,0) - d_m.            (2)

Proof: for the 4m characters with kernel in I, the supported character space has dimension m-1. For the other 4(6-m) characters it has dimension m. Section 3 computes their kernel dimensions as max(m-1-a,0) and max(m-a,0), respectively. There is no trivial-character contribution. This computes the kernel on T_I. Its subspace T_I intersect P is contained in the kernel and is precisely the kernel of T_I->H_I, so subtracting d_m proves (2).

For the full obstruction, for m=1,2,3,4 respectively, the supported-kernel dimensions are:

    r=1: 0, 16, 36, 56;
    r=2: 0,  0, 12, 32;
    r=3: 0,  0,  0,  8;
    r=4: 0,  0,  0,  0.

These hold for every subset of the stated size, not merely one normalizer orbit of subsets. For m=5 or6 the answer is 24(4-r), the full kernel dimension. Indeed H_I=H whenever m=5: its dimension is 100-4=96. The analogous normalization formula gives 24(4-q) for m=5 or6.

Thus if the full kernel is nonzero, the smallest number of pentads that can support a nonzero genuine section-preserving deformation class is exactly r+1. In particular r=1,2,3 force such classes on every set of respectively two, three, or four pentads. This is a support-exclusion theorem: no nonzero class can be supported on at most r pentads. For r=4 no such class exists at all. These assertions concern first-order classes and do not assert higher-order integrability.

## 5. Concrete geometric next dependency: two-pentad postulation

Write delta:T->N for the intrinsic cubic-postulation derivative from PR616 Section 2. For any distinct directions G,H, the restriction

    delta_(G,H): T_G direct-sum T_H -> Hom(S,H1(D))

is either injective or has a kernel of dimension exactly sixteen. More precisely, the following are equivalent:

1. Both normalization scalar gates beta_1,beta_4 are nonzero.
2. delta_(G,H) is injective for one pair of distinct pentads.
3. delta_(G,H) is injective for every pair of distinct pentads.
4. No nonzero first-order motion supported on two pentads preserves all ten cubic sections to first order.

These follow from (2) with a=q,m=2 and q in {1,2}. No ambient-coordinate quotient is hidden: T_G direct-sum T_H intersects P trivially.

Equivalently let W_G=delta(T_G), a twenty-dimensional subspace of N by PR616 Section 9. Then

    dim(W_G intersect W_H) = 0 if q=2, and 16 if q=1.          (3)

The kernel of delta_(G,H) identifies with this intersection by (v,w)->delta(v)=-delta(w). This supplies a precise geometric transversality target: proving that two pentad first-jet images have trivial intersection would force BOTH normalization gates nonzero and improve the embedded tangent upper bound from171 to147. The proof above does not establish that transversality. Conversely, merely proving single-pentad injectivity cannot establish it.

For the full map, the same two-pentad test detects r=1 versus r>=2. Three-pentad injectivity detects r>=3, and four-pentad injectivity detects r=4. These are exact lifting criteria, not claims that the tests have been resolved.

## 6. Full-normalizer equivariance alone cannot decide another gate

This section concerns abstract equivariant maps with the already established representations; it does NOT assert that arbitrary such maps arise as geometric deformation obstructions.

Let Gamma be the projective group generated by U and all intrinsic shears used in PR616. Its action on U has image SL2(F5). Every projective normalizer of U preserves the Heisenberg commutator pairing, since conjugation by a linear lift fixes scalar matrices; its action therefore belongs to Sp2(F5)=SL2(F5). The kernel of this action is exactly U. To see this, any projective transformation centralizing U has a linear lift a satisfying a H(u) a^(-1)=c(u)H(u) for Heisenberg lifts H(u). Multiplication shows c is a character of U. The nondegenerate commutator pairing realizes this character as conjugation by a Heisenberg operator H(v). The quotient a H(v)^(-1) then commutes with the irreducible Heisenberg representation, hence is scalar. Thus the projective centralizer is U. It follows that Gamma is finite of order25*120=3000 and equals the full projective normalizer of U.

The stabilizer Gamma_chi of a fixed nontrivial character chi has order125 and equals U semidirect <h>. Indeed its quotient in SL2(F5) is the order-five unipotent stabilizer of a nonzero dual vector, and the specified order-five h lifts its generator, with trivial intersection with U.

For each t in {1,2,3,4}, the chosen chi,h=t source line extends to a Gamma-stable subspace by taking all its Gamma-translates. For each of the twenty-four nontrivial U-characters there is exactly one line in this subspace: independence of the transport choice follows because Gamma_chi preserves the chosen line. The resulting twenty-four-dimensional representation is irreducible: any invariant subspace decomposes into U-character spaces, and transitivity propagates any nonzero one-dimensional character space to all twenty-four. The four such representations are pairwise nonisomorphic, since any intertwiner would preserve chi and h-weights. Their direct sum is H. Exactly the same construction in E_nt gives four matching pairwise nonisomorphic irreducibles. The t=1,4 summands project isomorphically onto N_nt and the t=2,3 summands comprise J_nt.

Consequently

    Hom_Gamma(H,E_nt) is the direct sum of four lines.         (4)

Each scalar may independently be set to zero or chosen nonzero in an ABSTRACT equivariant map. Moreover, whenever at least one normalization scalar is nonzero, its restriction to every single pentad is injective: Section 3 with k<=1 proves this for every nontrivial character. Thus every one of the twelve patterns having (beta_1,beta_4) not both zero is compatible with full-normalizer equivariance, the target filtration, and the previously known single-pentad injectivity.

This is a rigorous exclusion of a proposed proof route: those representation-theoretic facts and one-pentad injectivity alone cannot force any further scalar relation or sharper tangent bound. Any improvement must use additional geometric content, for example the two-pentad transversality in Section 5, a genuinely new functorial pairing, or a stronger lifting argument. The present theorem supplies the exact next geometric dependency and all support bounds without evaluating it.

## 7. Boundary and next step

No individual beta_t has been computed, no actual residual rank has been determined, and no stronger unconditional bound than171 is asserted. In particular no naive conjugation argument exchanging t and -t is used. Original HM/source, full-adjoint, algebraicity and higher-order deformation claims remain open exactly as in the pinned input. A further allowed step would be a coordinate-free proof or obstruction to the intrinsic intersection (3); it cannot be replaced by a source matrix or point evaluation under the standing restrictions.
