# A necessary degree bound for a rank-two Gauss plateau

## Result and scope

Let E be the actual rank-seventeen, degree-minus-fifty-four subbundle of the constant thirty-space H = H0(B_R(4))_+. Retain the established facts

    H0(E(1)) = 0,
    Q = (H tensor O_T)/E = D_lin(1) is ample,
    H0(E) = 0,     H0(Q*) = 0,
    T = P^1.

Suppose, only for the purposes of deriving necessary conditions, that the actual second fundamental form of E has generic rank two.

Iterate saturated backward and forward Gauss transforms from E. The maximal consecutive plateau of rank-two graded blocks containing the two blocks on either side of E has k blocks below E and l blocks above E, where

    1 <= k <= 8,     1 <= l <= 6.

Its lower endpoint has rank p = 17-2k, and its upper endpoint has codimension q = 13-2l. Both p and q are positive odd integers. Then necessarily

    kl(k+l-3) <= 20k+10l.                         (1)

In particular,

    k+l <= 10,     p+q >= 10.                     (2)

A stronger integer formulation says

    20k+10l-kl(k+l-3) = l A + k B

for some nonnegative integers A,B. In the bounded ranges above this integrality condition eliminates no additional pair beyond (1), but it records the exact form of the remaining degree defects.

The allowed numerical upper bounds on l are:

    k = 1,2,3: l <= 6;
    k = 4:     l <= 5;
    k = 5:     l <= 4;
    k = 6,7:   l <= 3;
    k = 8:     l <= 2.

These are necessary conditions for an actual rank-two SF. They neither assert realization of any allowed profile nor exclude rank two. In particular, the fully persistent rank-two profile k=8,l=6 is impossible, but many shorter profiles remain numerically possible.

No decomposition into two rank-one osculating curves is assumed or derived. No actual HM coefficients or actual map ranks are evaluated.

## 1. The actual constant ambient representation

Use A = Sym^2 W, V for the other genuine three-space, P4 for the genuine four-space, and D5 = Sym^4 W. The actual negative-coordinate Koszul description of H has middle term W tensor M3,-, left term M2,+, and right term M4,+. The left map is injective because multiplication by each nonzero negative linear form on M2,+ is injective; the right map is surjective because multiplication by each such form from M3,- to M4,+ is surjective. Therefore its actual middle cohomology has representation class

    H = W tensor (3W' + 3S4 + 6T6)
        -(A+2V+3P4+4D5)
        -(2V+4P4+3D5).

The universal binary-icosahedral identities

    W tensor W' = P4,
    W tensor S4 = A+D5,
    W tensor T6 = D5+V+P4

give

    W tensor (3W' + 3S4 + 6T6) = 3A+6V+9P4+9D5,

and hence the actual decomposition is

    H = 2A+2V+2P4+2D5.                            (3)

Its dimension is 30, and its center acts trivially. In particular it has no trivial, one-dimensional, or two-dimensional constituent. Any subsequently constructed constant G-invariant subspace must be a genuine submodule of (3); arbitrary constant subspaces cannot be silently substituted for such submodules.

## 2. Gauss transforms with changing rank

All the saturation and constant-subbundle facts in RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md apply without a rank-one assumption. For a saturated subbundle F of the trivial ambient bundle, let

    F^- = ker(beta_F)

and let F^+ be the saturated forward transform defined by the image of beta_F. If beta_F has generic rank s, then

    rank(F/F^-) = rank(F^+/F) = s,
    dF^- subset F tensor Omega,
    dF subset F^+ tensor Omega.

The induced map

    F/F^- -> (F^+/F) tensor Omega

has generic rank s, although it may have a torsion cokernel.

Backward from E, the next SF has generic rank at most the previous one, since its image lies in the preceding graded quotient. Forward from E, the next SF likewise has rank at most the previous one, since it vanishes on the preceding subbundle. Thus all successive rank increments are at most two and are nonincreasing when moving outwards from E.

A positive-rank backward stage cannot have zero SF: it lies in E and would then be a nonzero constant subbundle, contradicting H0(E)=0. A proper forward stage cannot have zero SF: it contains E and would then be a proper constant subbundle containing E, contradicting H0(Q*)=0. Consequently outward increments are two until they become one, after which they remain one until the appropriate endpoint is reached.

Since rank E=17 and codimension E=13 are both odd, neither direction can reach its terminal endpoint using only increments of two. There are uniquely determined positive integers k<=8 and l<=6 such that the maximal consecutive rank-two plateau is a saturated chain

    F_0 subset F_1 subset ... subset F_m,
    m = k+l,     F_k = E,
    rank F_i = p+2i,
    p = 17-2k,     rank F_m = 30-q,     q = 13-2l.

Here F_0 and F_m themselves have generic SF rank one. The displayed plateau is only a partial flag: its graded bundles L_i=F_i/F_(i-1), 1<=i<=m, all have rank two.

For each 1<=i<m the regular derivative descends to

    L_i -> L_(i+1) tensor Omega.

This map has generic rank two. For backward stages this follows from the defining sheaf kernel; for forward stages the preceding rank-two block lies in the kernel and accounts for its entire generic rank. The same assertion holds at E. Saturation handles all exceptional parameters and introduces no poles.

## 3. Determinant degrees and equivariant parity

Write

    c_i = deg L_i,
    a = deg F_0,     b = deg F_m.

Taking determinants of the preceding rank-two derivative maps gives nonzero regular line-bundle maps

    det L_i -> det L_(i+1) tensor Omega^2.

Since deg Omega^2=-4,

    c_(i+1)-c_i = 4+delta_i,     delta_i>=0.        (4)

The nonnegative integer delta_i is the degree of an effective zero divisor, so special or ramified parameters strengthen rather than reverse the inequality.

Every saturated Gauss stage is naturally G-equivariant, because the trivial connection, sheaf kernels, and saturation commute with the G action. Its determinant inherits trivial action of the central involution from the center-even ambient representation (3).

A G-linearization of O_T(n) differs from the standard one by a character of G. The binary icosahedral group is perfect and has no nontrivial characters. In the standard linearization its central involution acts by (-1)^n. Thus a determinant carrying trivial central action must have even degree. In particular,

    a, b, and every c_i are even; every delta_i is even.  (5)

The vanishing H0(E(1))=0 implies H0(F_0(1))=0. Splitting on P^1 therefore gives

    a <= -2p.

The quotient (H tensor O_T)/F_m is a rank-q quotient of the ample bundle Q. On P^1 it splits into positive-degree line bundles, so -b>=q. Since b is even and q is odd, this improves to

    b <= -(q+1).                                  (6)

Write the nonnegative even degree defects as

    a = -2p-2alpha,
    b = -(q+1)-2beta,
    delta_i = 2epsilon_i,

where alpha,beta,epsilon_i are nonnegative integers.

## 4. Exact plateau identity

Since sum c_i=b-a and sum_(i<=k)c_i=deg E-a, elimination of c_1 from (4) gives

    m deg E = l a + k b - 2klm
              -l sum_(j<k) j delta_j
              -k sum_(j>=k) (m-j) delta_j.         (7)

This is a universal identity for a rank-two plateau, not an inequality inferred from a splitting of rank-two blocks.

Substitute deg E=-54, p=17-2k, q=13-2l, and the nonnegative defects from Section 3. Dividing by two gives

    20k+10l-kl(k+l-3)
      = l [alpha + sum_(j<k) j epsilon_j]
        +k [beta + sum_(j>=k)(m-j) epsilon_j].      (8)

Its right-hand side is a nonnegative integer in the semigroup generated by k and l. This proves (1) and the stronger integer formulation.

Without the equivariant parity input, the same proof still gives the weaker valid inequality

    2kl(k+l-3) <= 41k+20l.

Thus parity is a genuine strengthening, not an assumption hidden in the ordinary degree calculation.

## 5. Why rank one does not automatically generalize to rank two

For rank one, no common constant vector and full constant span force a complete flag of line bundles. Each adjacent derivative then gives a scalar degree inequality, and the sum of all line degrees is zero.

For rank two, the canonical construction gives rank-two blocks in a central plateau and rank-one blocks in the outer tails. At a change of block rank, the derivative is an injection of a line into a rank-two bundle or a surjection of a rank-two bundle onto a line, only generically after saturation. Such a map does not compare their determinant degrees in the manner used in (4). It controls an image line, not the degree of an unchosen complementary line.

Refining the rank-two blocks by line subbundles is possible abstractly on P^1, but does not ensure that derivatives preserve the refinement or give nonzero adjacent line maps. Neither a splitting of each bundle nor a decomposition of the constant G-module supplies a horizontal splitting into two rank-one osculating curves. Treating it as one would add an unproved geometric hypothesis.

The proven necessary conditions therefore stop at (8). Remaining allowed profiles show that the present plateau degree constraints alone do not contradict generic SF rank two. Further exclusion would need additional actual geometry controlling the unequal-rank transitions, image lines, their degrees, or their equivariant positions.

## Reproduction and dependencies

Run `python verify_rank_two_gauss_plateau.py`. It verifies the universal coefficient identity symbolically, the actual ambient representation class by exact abstract character arithmetic, and the finite arithmetic of hypothetical integer profiles. That last calculation is not an evaluation of any actual Gauss or multiplication rank.

Dependencies:

- RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md: saturation, regular derivative descent, and the derivative-invariant constant-subbundle lemma. This frozen artifact is unchanged.
- TWIST-ONE-ACTUAL-SECTION-KERNEL-VANISHING.md: H0(E(1))=0, with physical parity checked independently.
- POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md: actual Koszul middle cohomology and constant ambient bundle.
- UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md: uniform injectivity/surjectivity, Q=D_lin(1), and its globally generated untwisting.
- POSITIVE-GAMMA-TWO-LINEAR-STEP-CRITERION.md and the existing character verifiers: the exact ambient characters and binary-icosahedral tensor identities.
