# Twenty positive splittings and four actual kernels in the last rank-two quotient

## Result and limits

For the last first-quotient case (n,e)=(8,2), the full positive-tail and twist-four coefficient test leaves exactly twenty possible splittings of K. For the nine cases with two copies of Wprime in H0(K(3)), the actual next kernel Q has one of four explicitly determined shapes below. This is a checked reduction, not an exclusion of (8,2). The rank-one branch and the bounds SF>=3 and positive-square rank>=27 remain unchanged.

Inputs are EXTREMAL-31-FIVE-QUOTIENT-SECTION-ENVELOPES.md, EXTREMAL-31-LAST-LOW-QUOTIENT-EXCLUSION.md, and EXTREMAL-31-FIRST-REMAINING-QUOTIENT-EXCLUSION.md. Write P=P4, T=T6, and Wp=Wprime. Coefficients denote equivariant bundles. The derivative is the actual map

    delta: K -> O(4)+Wp(-3),

of generic rank three; K has rank 14 and degree -58. Its kernel Q has rank 11. Persistence gives H0(Q(2))=0 and H0(Q(3))<=T, as in the earlier low-quotient proof. No horizontal splitting is assumed.

## 1. Exhaustion

The exact Euler identities are

    chi(K(3))=Wp-S4,
    chi(K(4))=-A+V+3P.

The section bounds give

    R2=H0(K(2))=vV+sP,  v,s in {0,1},
    X=H0(K(3))=aWp+tT,  a in {1,2}, t in {0,1,2},
    R3=X-R2 W >= 0,
    H1(K(3))=(a-1)Wp+tT+S4.

Here Euler positivity forces a>=1. Every degree of K is at most -2. Rank and degree give a maximum negative degree of 32: a line of degree -j leaves thirteen dimensions of degree at most -2, hence j<=58-26. Each deeper irreducible block C(-j), j>=5, contributes C Sym^(j-5)W positively to H1(K(3)). Central parity and the largest possible H1 character leave precisely these 21 individual blocks:

    Wp(-5), S4(-5), T(-5), V(-6), P(-6), D5(-6),
    Wp(-7), T(-7), O(-8), V(-8), P(-8),
    W(-9), Wp(-9), O(-10), A(-10), W(-11),
    O(-12), W(-13), O(-14), O(-20), O(-22).

Enumerate all multisets with the required positive H1 character. For each, force

    R4=chi(K(4))-R2 Sym^2 W-R3 W
                        -sum_tail C chi(O(4-j)).

Requiring R3,R4 genuine yields the following complete list. Let L be independently either O(-8)+O(-10) or W(-9). Each line containing L represents two splittings; lines without L represent one.

    a=1:
    Wp(-3)+(V+2P)(-4)+O(-8);
    (Wp+T)(-3)+P(-4)+L;
    P(-2)+2P(-4)+L;
    V(-2)+Wp(-3)+(V+P)(-4)+L;
    V(-2)+(Wp+T)(-3)+L+O(-10);
    (V+P)(-2)+P(-4)+L+O(-10).

    a=2:
    2Wp(-3)+(V+P)(-4)+Wp(-5)+O(-8);
    (2Wp+T)(-3)+Wp(-5)+L;
    P(-2)+Wp(-3)+P(-4)+Wp(-5)+L;
    V(-2)+2Wp(-3)+V(-4)+Wp(-5)+L;
    (V+P)(-2)+Wp(-3)+Wp(-5)+L+O(-10).

Thus there are eleven a=1 and nine a=2 candidates. The verifier independently checks both Euler identities against all 28 primal profiles and verifies rank and degree for every candidate. This is an overlist of necessary bundle shapes, not a claim of realizability.

## 2. Actual low elimination when a=2

At twist three, the target has Wp multiplicity two: one in Sym^7 W and one from its constant Wp low block. Since H0(Q(3)) has no Wp and X has two copies, the induced map on these multiplicity spaces is injective. In particular its low component is nonzero on the Wp(-3) coefficient of K; degree excludes all degree -2 blocks from this low component, and deeper blocks have no twist-three sections.

A multiplicity-space change makes this a scalar isomorphism on one Wp(-3). All other low components lift through that isomorphism and are subtracted by triangular source automorphisms. A triangular target automorphism then clears its high component. These operations compute the actual kernel; they are not asserted horizontal. After removing the isomorphism the remaining high map to O(4) has the following source, in the order of the five a=2 lines:

    Wp(-3)+(V+P)(-4)+Wp(-5)+O(-8);
    (Wp+T)(-3)+Wp(-5)+L;
    P(-2)+P(-4)+Wp(-5)+L;
    V(-2)+Wp(-3)+V(-4)+Wp(-5)+L;
    (V+P)(-2)+Wp(-5)+L+O(-10).

In the first, second, and fourth lines, the residual Wp(-3) high map is nonzero: otherwise a Wp survives in H0(Q(3)). In the third and fifth lines, every degree -2 irreducible high map is nonzero because H0(Q(2))=0. The same forces the V component in the fourth line. Every such high map is surjective, since its degree-six or degree-seven irreducible polynomial series is basepoint-free by the invariant-divisor argument in the earlier low-quotient proof.

## 3. Actual high kernels, including all extension issues

The universal evaluations used here are

    ker(Wp(-3)->O(4))=O(-10),
    ker(P(-2)->O(4))=V(-4),
    ker((V+P)(-2)->O(4))=T(-3),
    ker((Wp+T)(-3)->O(4))=(V+P)(-4)

in the last two cases when both irreducible components are nonzero. The first follows from surjectivity of a rank-two septic pair and its determinant; the other identities were established in the cited proofs.

First line: V(-4) has no high map. Every P(-4) high map lifts through Wp(-3), because the obstruction is

    Ext^1_G(P(-4),O(-10))=(P Sym^4 W)^G=0.

Wp(-5) has no high map, since Wp is absent from Sym^9 W. The remaining O(-8) can give the one-dimensional extension of O(-8) by O(-10). Its zero and nonzero classes have middle bundles O(-8)+O(-10) and W(-9). Therefore Q=(V+P)(-4)+Wp(-5)+L.

Second line: if the T high component is nonzero, complete septic evaluation gives (V+P)(-4), and all deeper maps lift because their obstruction line degrees are at least one. This gives the same Q. If the T component is zero, it is an inactive T(-3); the septic-pair kernel is O(-10). For L=O(-8)+O(-10), only the O(-8) extension can be nontrivial, giving either O(-8)+2O(-10) or W(-9)+O(-10). For L=W(-9), Ext^1(W(-9),O(-10))=0 since H1(O(-1))=0, giving W(-9)+O(-10). The Wp(-5) high map is zero throughout.

Third line: start with the P sextic kernel V(-4). All other high maps lift, because their obstruction line degrees are nonnegative. Hence Q=(V+P)(-4)+Wp(-5)+L.

Fourth line: combine the nonzero V sextic and Wp septic. The kernel sits in an extension of Wp(-3) by Wp(-5). It is nonsplit, because Hom_G(Wp(-3),V(-2))=0 would prohibit a lift of the nonzero septic map. The invariant extension space is one-dimensional and its nonzero middle bundle is P(-4), by tensor Euler. The remaining maps lift with nonnegative obstruction line degrees, giving the same Q.

Fifth line: complete sextic evaluation gives T(-3), and all remaining maps lift, giving T(-3)+Wp(-5)+L+O(-10).

Every invoked lift may be averaged to be equivariant. No potentially nonzero Ext group is silently discarded. We have therefore proved the four-shape actual-kernel conclusion

    Q=(V+P)(-4)+Wp(-5)+L,
    or Q=T(-3)+Wp(-5)+L+O(-10),
    L=O(-8)+O(-10) or W(-9).

In all nine cases delta is surjective and K/Q=O(4)+Wp(-3). Each displayed Q has rank 11 and degree -56. The next actual derivative has target O(2)+Wp(-5). In each shape the only block admitting a low map is Wp(-5), so the required rank three forces that scalar block to be an isomorphism. The remaining high maps are not resolved here. A count of their dimensions is not an actual-kernel classification.

## Reproduction and boundary

Run python3 verify_extremal_31_last_remaining_quotient_reduction.py. It checks the complete exact-character enumeration, all twenty expected rows, the evaluation and extension characters, the stated lifting ranges, and the unique low-map support in all four actual Q shapes. Geometric basepoint-freeness, persistence, and the kernel arguments are supplied above, not inferred from arithmetic. No selected HM coefficients, points, matrices, rank experiments, or scans occur. Only this new proof and its new verifier were written; no frozen file was changed.
