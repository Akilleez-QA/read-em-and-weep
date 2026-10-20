# Independent audit: degree-one-hundred components and elliptic quintics

## Verdict

The proposed classification and exclusion are valid under the imported exact-degree and canonical-odd-line theorems. A nonempty reduced rank-four curve of degree 100 is either integral of degree 100 or consists of one orbit of five integral degree-20 components. The provisional third possibility, one orbit of twenty degree-five components, is impossible because one of its smooth elliptic components meets a canonical odd line.

This audit independently checks the argument, including its linearization and fixed-point signs. It relies only on local proof dependencies and abstract complex-curve/group arguments. No actual source tensor, selected input, operation matrix, rank instance, jet or residue is evaluated; 

## 1. Component orbit exhaustion

Import the results in ../rank-four-degree-hundred-lower-bound/PROOF.md: the total degree is 100; component degrees are at least five; A=F5^2 is normal in N=A semidirect SL2(F5); every A-stable integral component spans P4 and has degree divisible by five; an A-stable component of degree five or ten has N-orbit size at least twenty; there is no nonempty N-invariant reduced curve of degree at most 55 whose component degrees are at least five.

A free A-orbit would cost at least 125. An A-orbit of size five generates six disjoint A-orbits under N, indexed by its six distinct stabilizer axes, costing at least 150. Thus all components are A-stable.

Each N-orbit of components is itself an invariant reduced curve to which the audited degree-at-least-100 result applies. Consequently there is exactly one such orbit. If its size is m and its common component degree is e, then me=100. The component action factors through the perfect group SL2(F5), so m=1 or m>=5. Moreover 5 divides e. If e=5, m=20; if e=10, m=10 violates the orbit lower bound twenty. For e>=15 and m>=5, one has e<=20, so e=15 or20; e=15 cannot divide100 and e=20 gives m=5. Finally m=1 gives e=100.

This gives exactly (m,e)=(1,100),(5,20),(20,5), without an unproved classification of subgroups of SL2(F5). The same conclusion can alternatively be obtained using the audited degree-50 divisibility of each component orbit and exclusion of degree50.

## 2. A-stable quintics are smooth elliptic normal curves

Let D be a degree-five A-stable integral component, and X its normalization. Nondegeneracy and Castelnuovo give g(X)<=1. The A-action on X is faithful, because a finite-order projective transformation fixing the full-span integral curve pointwise is scalar.

For completeness, genus zero is impossible without invoking a classification of finite PGL2 subgroups. In a faithful action on a smooth curve, point stabilizers are cyclic. Nontrivial A-inertia has order five, so Riemann-Hurwitz gives

    g(X)=25g(X/A)-24+10t,

where t is the number of branch points downstairs. The right side is 1 modulo5, whereas genus zero is0. Hence g(X)=1. In fact g(X/A)=1 and t=0.

Put L=nu*O_D(1). It has degree five, H1(X,L)=0 and h0(X,L)=5 by Riemann-Roch. The restriction map V* -> H0(X,L) is injective because D spans P4; equality of dimensions makes it an isomorphism. Thus the original map is the complete degree-five linear series on the smooth elliptic X, which is very ample. It follows that D=X is smooth and linearly normal. This verifies both the absence of singularity and the completeness needed for the trace calculation.

## 3. The relevant reflection actually preserves D

In the twenty-component case, K=N_D has quotient H=K/A of order six. Since K contains all of A, it is precisely the full inverse image of H in N. Cauchy's theorem gives an involution in H; the unique involution of SL2(F5) is z=-I. Hence z lies in H and the standard complementary element (0,z) belongs to K.

There is therefore no need to guess a reflection lift, infer one from a merely projective elliptic action, or choose a complement to K. The canonical normalized honest involution R on V representing this (0,z) has R^2=I and eigenspaces T,W of dimensions three and two, respectively. Its negative projective eigenspace P(W) is one of the canonical odd lines. These facts are supplied by ../canonical-line-parity-exclusion/PROOF.md, Section1, and its cited canonical-line identification.

## 4. Fixed-point and character audit

The restriction r=R|D is a nontrivial involution of the elliptic curve. It acts by inversion on A under conjugation. Since A acts by translations and a translation commutes with A, r cannot be a translation. Consequently, after choosing an origin, it has the form x -> a-x. The equation 2x=a has four distinct solutions over C, and at each the tangent eigenvalue is -1.

Use the O(1)-linearization induced by the specific honest operator R, not an arbitrary scalar multiple of a projective lift. Under V* = H0(D,L), its trace is 3-2=1. Dualization does not change the signs of an involution. At a projective fixed point p=[v], the fibre action on O(-1)_p is the eigenvalue of R on v; the dual O(1) fibre has its inverse, which is the same sign. In particular, fibre sign -1 is equivalent to p lying on P(W).

Holomorphic Lefschetz applies to this smooth projective curve and this finite-order linearized line bundle. H1(D,L)=0, so its formula reads

    1 = sum over p in Fix(r) of epsilon_p/(1-(-1))
      = (epsilon_1+epsilon_2+epsilon_3+epsilon_4)/2.

Each epsilon_p is +1 or -1 because the lift squares to identity. Therefore their sum is2: exactly three are positive and exactly one is negative. Thus D meets the canonical odd line in a point. This is a set-theoretic assertion sufficient for the contradiction; no intersection-multiplicity claim is required.

Changing R to -R would interchange all signs and section trace but would not change the geometric conclusion when eigenspaces are tracked consistently. The normalized R fixes the preferred labels unambiguously.

## 5. Rank-four contradiction and scope

The independent established theorem ../canonical-line-rank-five-strengthening/PROOF.md gives residual rank at least five everywhere on every canonical odd line. This weaker already-audited bound is sufficient: these lines are disjoint from Z4. Any stronger rank-at-least-six theorem is unnecessary for this exclusion.

Since D is a component of the reduced rank-four curve, D is contained in Z4. Section4 produces a point of D on a canonical odd line, a contradiction. Thus (20,5) is excluded.

The two remaining cases are necessary possibilities, not constructions or existence statements. The argument alone does not exclude an integral degree-100 component or the orbit of five degree-20 components, establish nonemptiness, constrain isolated rank-four points, or determine scheme multiplicities.

## 6. Direct review of the final developing proof

The draft at ../rank-four-degree-hundred-components/PROOF.md was read in full after the independent derivation above. Its alternative orbit-by-orbit exhaustion is sound: for degree15 the only possible nonsingleton indices are5 and6, and the already-audited component divisibilities exclude both. Every remaining candidate orbit consumes the entire degree100 budget, so no mixed orbit configuration is omitted.

The additional description of the five-component stabilizer is also correct. The permutation image of perfect G on five letters lies in A5 and is nontrivial; every proper subgroup of A5 is solvable, so the image is A5. Its kernel has order two and is the unique central involution subgroup. The component stabilizer is therefore the inverse image of an A4 point stabilizer, an order24 binary tetrahedral subgroup, and K has order600.

The draft's rational-case centralizer argument is valid: in PGL2(C), an element of order five has centralizer a torus, and finite subgroups of that torus are cyclic. Its optional assertion H=C6 and j(E)=0 is also valid: conjugation on the translation subgroup A factors through the cyclic origin-preserving automorphism group, and its prescribed H-action on A is faithful. Thus an order-six H injects into that group, forcing its order to be six. No use of this extra assertion is needed for the exclusion.

No mathematical correction to the draft is required. The only scope clarification is that disjointness follows already from rank>=5 on canonical odd lines; the parent task's stronger rank>=6 phrasing need not be imported or re-proved.
