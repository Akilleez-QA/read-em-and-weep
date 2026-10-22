# Further endpoint descent excludes index9 cyclic second defect24

## Claim and actual stages

For stable ID **G3.21.1c43993b4f83**, source index9,

    A=O(-8)+O6+O16,  B=O(-18)+O(-8)+O6,

the cyclic alternative T_def=O4|2D12 is impossible. Together with the separately proved semisimple exclusion and the published local module restrictions, this removes the whole second-defect24 branch. It does not exclude the quotient label; frontier143 is unchanged.

Write K=E^-, M=K^-, J=K/M and C=A(-2)=O(-10)+O4+O14. The actual image sequence is

    0 -> J -> C -> O4|2D12 -> 0.

The published endpoint theorem leaves precisely

    M1=Wp O(-5)+W O(-7)+(V+P) O(-4),
    M2=Wp O(-5)+O(-6)+O(-8)+(V+P) O(-4).

Strict Gauss-kernel slope decrease gives top K<=-3, top M<=-4, top M^-<=-5, and top M^{--}<=-6. The last statement is the published arbitrary-rank iteration lemma, not a rank-three assertion about either endpoint.

## 1. A complete rank-two overlist forces J

At C10 the cyclic target has generator weight4 and socle weight4-12=2, while the low O(-10) has weight0. Its whole component is therefore zero, not just its top component. Thus J=O(-10)+J', where J' is a rank-two degree -6 locally free subsheaf of O4+O14.

Its maximum degree is at most14. The effective central character permits only even-degree trivial lines or odd-degree W/Wp blocks. Consequently the complete overlist is

    O(e)+O(-6-e), e=-20,-18,...,-4,
    W O(-3), Wp O(-3).

There are exactly eleven candidates. The line-pair lower bound -20 follows from the sum -6 and upper bound14, not an arbitrary cutoff. The cyclic divisor exact sequence gives

    chi(J')=Sym14 W-Sym18 W=-P.

Only four candidates match: O(-20)+O14, O(-16)+O10, O(-10)+O4, and Wp O(-3).

The O10 summand of the second candidate cannot embed into O4+O14: ordinary degree rules out its O4 component and (Sym4 W)^G=0 rules out its O14 component. The Wp O(-3) candidate gives H0(J(2))=0, contradicting the required injection H0(M(4))->H0(J(2)), since both endpoints have seven sections at twist4.

For J'=O(-20)+O14, the actual-source Euler identity and top K<=-3 give

    H1(K(2))=chi(A(2))-chi(E(2))=A_std+2V+3P+D,
    H1(J(2))=Sym6 W+Sym16 W=2V+2P+2D.

Here chi(E(2)) comes from the actual presentation M3 O(-1)->M4 O, with M3=3Wp+3S+6T and M4=2V+4P+3D. The surjection H1(K(2))->H1(J(2)) cannot increase the D multiplicity from one to two. Therefore only

    J=2O(-10)+O4                                      (1)

survives. In fact its O4 summand can map only into the middle O4 of C, since (Sym10 W)^G=0. Thus the quotient C->T_def annihilates both low and middle summands and is supplied by O14. No lift from O14 to O4 has been assumed or used.

## 2. The endpoint derivative has a forced rank-one image

The actual derivative of M factors through J(-2)=2O(-12)+O2 and has kernel N=M^-. Every summand of either listed M has degree greater than -12. Both O(-12) components of the derivative are therefore zero.

The slope bound on N makes the induced map H0(M(4))->H0(J(2)) injective. Both sides are V+P=Sym6 W, of dimension7, so the map is an isomorphism onto all H0(O6). These sections generate O6 everywhere. Thus the bundle map M(4)->O6, and equivalently M->O2, is globally surjective. This derives, rather than assumes, the rank-one image and the exact sequence

    0 -> N -> M -> O2 -> 0.                           (2)

There are no torsion zeros left in this image.

## 3. One more endpoint derivative is impossible

Both listed endpoints have h0(M(5))=16: the degree -4 block contributes14, the Wp degree -5 block contributes2, and the remaining summands contribute zero. Twisting (2) by five yields

    h0(N(5)) >= 16-h0(O7)=16-8=8.                    (3)

Because N=M^- kills M's second fundamental form, its own derivative factors through (M/N)(-2)=O0. Its kernel is N^-=M^{--}. The published iterative strict-slope lemma gives H0(N^-(5))=0. Hence this further derivative injects

    H0(N(5)) -> H0(O5),

whose target has dimension6, contradicting (3). No prescribed rank of N or N^- is needed. This proves the cyclic alternative impossible.

## Reproduction and limits

Run `python3 verify_two_one_index_nine_cyclic_twenty_four_descent_exclusion.py`. It writes `two-one-index-nine-cyclic-twenty-four-descent-exclusion.json`. The standalone checker pins the published frontier144, endpoint alternatives, primal-interior proof and arbitrary-rank strict-slope lemma. It derives the eleven-item overlist, reproduces exact Q(sqrt(5)) character tests, checks both endpoint section counts and degree support, and verifies8>6.

This uses no unpublished E/Q/K witness datasets, selected actual coefficients or points, matrices or actual rank tests, scans, spikes or consumed experiments. The computation checks abstract characters and integers; the global-evaluation and further-derivative arguments above supply the geometric implications. No global realization, whole quotient-case exclusion, smoothing or SF claim is made.
