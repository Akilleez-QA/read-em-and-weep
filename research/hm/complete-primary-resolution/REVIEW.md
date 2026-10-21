# Independent review: complete primary and node resolutions

Verdict: **PASS** for the structural deduction from the four declared, reviewed inputs. No mathematical blocker was found. The initially pending quintic dependency has now been immutably pinned and independently fetched as part of this review.

Reviewed on 2026-10-21 UTC. This is an independent mathematical review, not formal verification or a fresh certification of all upstream geometry. I read the complete proof and the local normalization-resolution, conductor-canonical-module, low-equation-exclusion, and quintic-gap proofs, including the latter's independent review. No selected actual HM/source coefficients, matrices, point evaluations, rank tests, numerical search, or large computation was used.

## 1. Minimality and canonical shifts

The degree lower bounds on F1(R), F2(R), and F3(R) are valid. In a minimal exact free resolution, a basis vector cannot have zero differential: exactness would place it in the next differential's image, contained in the homogeneous maximal ideal times the free term. Every nonzero differential entry has positive degree. Starting from the absence of node equations below degree three therefore gives minima 3, 4, and 5.

Since R is Cohen–Macaulay of codimension four, dualizing its resolution has just the required Ext4 cohomology. Combining the ambient canonical twist (-5) with M=omega_R(-5) gives exactly

F_i(M)=Hom_P(F_(4-i)(R),P(-10)).

A degree-a basis vector becomes degree 10-a. Thus Tor1(M,k) has no degree above 5, Tor2(M,k) has no degree above 6, and the last M-term is P(-10). These bounds precede and do not assume A=B.

## 2. Closing the section gap

The Tor tail in Section 3 has the correct direction. The induced surjection N/mN→M/mM is an isomorphism in degree two because both pieces have dimension five; its remaining kernel is exactly the degree-zero unit. Consequently B/mB can be supported only in degree zero or in degrees at most five coming from Tor1(M,k).

The actual ambient agreement through degree five makes every positive-degree B-element in that range a positive-degree polynomial multiple of the unit, hence an element of mB. There are no negative-degree elements. Therefore B/mB=k·1, and graded Nakayama applies because B is finite. Its conclusion is P·1=B, exactly A=B. No higher-degree restriction-surjectivity assumption, normality assumption, or dimension-only substitution occurs.

## 3. Tor exactness forces the supports

The long exact sequence from 0→A→N→M→0 is correct throughout. Since pd(N)=2, it gives Tor3(A,k)=Tor4(M,k)=k(-10). Primary equation exclusion through degree five puts Tor1(A,k) in degrees at least six and Tor2(A,k) in degrees at least seven. The map Tor2(A,k)→Tor2(N,k)=k(-5)^4 is therefore zero, yielding Tor3(M,k)≅Tor2(A,k).

Duality now bounds the node generators above by degree three, while the earlier minimum was three. Thus all node generators are cubic; their number is 35-25=10. This forces Tor2(A,k)=k(-7)^10.

The map Tor1(A,k)→Tor1(N,k) is zero by degree. The injection of the unit Tor0(A,k)→Tor0(N,k) makes Tor1(N,k)→Tor1(M,k) surjective, so it is an isomorphism. The remaining exact segment is precisely

0→k(-5)^4→Tor2(M,k)→Tor1(A,k)→0.

The upper bound six on the middle term and lower bound six on the last force the primary generators into degree six alone. These arguments determine actual minimal-resolution supports before any unknown Betti multiplicity is extracted from a Hilbert series.

## 4. Numerator and the resulting resolutions

Direct polynomial multiplication gives

t²(5+10t+10t²+4t³+t⁴)(1-t)^4
=5t²-10t³+4t⁵+10t⁶-10t⁷+t¹⁰.

Subtracting this from the stated numerator of N gives 1-10t⁶+10t⁷-t¹⁰. Comparing only after the Tor supports are known forces ten sextic primary generators. Hence the claimed primary ring and ideal resolutions follow. The short exact sequence of graded Tor spaces then gives Tor2(M,k)=k(-5)^4⊕k(-6)^10; canonical reversal gives F2(R)=P(-5)^4⊕P(-4)^10. All other displayed node and M terms agree with that same duality.

The regularity and depth checks are consistent: A has projective dimension three, depth two, and regularity seven. It is not Cohen–Macaulay, and A=B does not imply normality or equality with N.

## 5. Dependency and scope qualification

The local quintic proof derives its conclusion from the actual normalization resolution, lower conductor representations, low-degree ambient agreement, invariant parity, and an integral-hyperplane Hilbert-function bound. It does not use A=B in all degrees or either complete resolution proved here. No circular use was found in the inspected local dependency chain.

I fetched research/hm/quintic-gap/PROOF.md and REVIEW.md from Akilleez-QA/read-em-and-weep at immutable commit 4392ed5dfce5f706ea80733b25f8c7fc507a4a58. Both fetched contents exactly match the local files inspected above, including the independent PASS review. Input 4 now cites that commit, so there is no remaining pending quintic dependency in this proof. The update changes only dependency/status text, not the mathematical deduction.

Verified source: https://github.com/Akilleez-QA/read-em-and-weep/blob/4392ed5dfce5f706ea80733b25f8c7fc507a4a58/research/hm/quintic-gap/PROOF.md

The conclusions determine the ranks and twists of existing actual minimal resolutions, not explicit differential matrices. They do not establish the separate full-adjoint, prescribed-source, lifting, or algebraicity assertions.
