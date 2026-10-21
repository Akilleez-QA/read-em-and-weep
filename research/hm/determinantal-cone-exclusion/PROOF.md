# Excluding the zero determinantal comparison by pure-diagram positivity

Work over the complex numbers. Let S be the polynomial ring in five variables, D=Fitt_0(H), Q=S/D and R=S/Ann(H). Assume the pinned results of PR503 at c56c902d227f6205cf132897dd66cf2070f05b4a and its dependencies, notably PR502 at f8c9b1fb8b03a5721e4eca97cac4137f7ba955d0. These give a finite-length quotient with the following minimal free modules:

F0=S;
F1=35S(-4);
F2=52S(-5)+(55+k)S(-6);
F3=kS(-6)+160S(-7);
F4=110S(-8);
F5=20S(-9)+3S(-10).

The comparison rho:Tor_3(R)_6 -> Tor_2(Ann(H)/D)_6 has rank 45-k. Equivariance already restricts k to {15,25,35,45}, with the 15-dimensional U source summand killed and the other irreducible source summands having dimensions 10 and 20.

## 1. A positivity inequality

The Eisenbud–Schreyer theorem on Cohen–Macaulay Betti tables decomposes beta(Q) as a positive rational combination of pure diagrams of codimension five. It applies because Q is nonzero and finite length over S, hence Cohen–Macaulay of codimension five.

There is no cancellation in a positive decomposition. Consequently every contributing degree sequence must have the form

(0,4,a,b,8,c), where a is 5 or 6, b is 6 or 7, a<b, and c is 9 or 10.

Only sequences (0,4,5,6,8,c) contribute to beta_(3,6). For a pure diagram pi(d), the Herzog–Kühl formula, with arbitrary positive normalization, is

pi_(i,d_i)=C / product_(j!=i) |d_i-d_j|.

Therefore for d=(0,4,5,6,8,c),

pi_(3,6)/pi_(2,5)
 = [5*1*1*3*(c-5)]/[6*2*1*2*(c-6)]
 = 5(c-5)/[8(c-6)].

This equals 5/6 for c=9 and 25/32 for c=10. Every other permitted pure diagram has zero entry at (3,6) and nonnegative entry at (2,5). Adding the inequalities for all summands proves

beta_(3,6)(Q) <= (5/6) beta_(2,5)(Q) = 130/3.

Since k is integral, k<=43. In particular k=45 is impossible.

## 2. Consequence for the actual comparison

Combining the new inequality with the pinned equivariant restriction gives

k in {15,25,35}, and rank(rho) in {30,20,10}.

Thus rho is nonzero. At least one of its 10-dimensional W' and 20-dimensional Qspin source channels injects. This does not decide which one, and it does not assert that both inject. It is a structural nonvanishing proof, not evaluation of a selected source matrix or its coefficients.

The nonzero linear lift from PR506 is not used: that lift has positive-degree entries and does not by itself imply Tor nonvanishing.

## 3. Sharpness of this numerical method and the next boundary

Normalize pure diagrams by their entry at (0,0) being one. Write pi_1, pi_2, pi_3, pi_4 for the respective degree sequences

(0,4,5,6,8,9),
(0,4,5,7,8,9),
(0,4,6,7,8,9),
(0,4,6,7,8,10).

They form a totally ordered chain. Their nonzero homological entries, from homological degree zero to five, are respectively

pi_1: (1,54,144,120,45,16),
pi_2: (1,42,84,120,105,28),
pi_3: (1,126/5,168,288,189,224/5),
pi_4: (1,70/3,140,640/3,105,28/3).

Direct substitution into the displayed Betti family gives the identity

beta(k) = (k/120) pi_1
        + (13/21-k/70) pi_2
        + ((k+10)/168) pi_3
        + (9/28) pi_4.

Every coefficient is nonnegative for 0<=k<=130/3. This independently certifies that all three surviving k values lie in the Cohen–Macaulay rational Betti cone with precisely the required support. Thus positivity of this cone alone cannot exclude k=15,25,35; actual channel structure or an additional invariant is required. Cone membership does not assert realization by this particular quotient or even by a cyclic quotient with these exact integral Betti numbers.

## Sources, dependencies, and status

- Eisenbud–Schreyer, Betti Numbers of Graded Modules and Cohomology of Vector Bundles: https://arxiv.org/html/0712.1843v3 (Theorem 0.2, positive pure decomposition); the Herzog–Kühl formula is displayed immediately before Theorem 0.1 in the same introduction.
- PR503: https://github.com/Akilleez-QA/read-em-and-weep/blob/c56c902d227f6205cf132897dd66cf2070f05b4a/research/hm/determinantal-resolution-constraints/PROOF.md
- PR502: https://github.com/Akilleez-QA/read-em-and-weep/blob/f8c9b1fb8b03a5721e4eca97cac4137f7ba955d0/research/hm/excess-contraction-invertibility/PROOF.md

Authored structural proof, pending independent review; not formally checked. The pure-diagram arithmetic concerns a universal rational cone and the already-published Betti family, not selected actual HM/source matrices, source ranks or coefficients. No source-instance evaluation, coefficient search or large computation is used. No first-order source value, higher-order lifting, or algebraicity conclusion is claimed.
