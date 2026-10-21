# Independent review of the derived middle homology bounds

Reviewed proof SHA256: ec8cf20c4827542400324960517a17faf0900b143b8f0fabb64516ac43f51960.

Verdict: the module identifications, complete two-parameter intermediate Hilbert functions, and nonvanishing in every homological degree pass independent mathematical review, conditional on the pinned prior inputs. This is not formal proof-assistant verification.

## Resolution and grading audit

PR540 proves scheme-theoretically that the universal binary-block maximal-minor quotient over P is B. Its monomial straightening argument uses the exact minor moves, not merely a rank-one set-theoretic parametrization. The section-ring cohomology argument gives B Cohen--Macaulay of dimension six. Since P is regular of dimension fifteen, the maximal-minor ideal has grade nine, precisely the expected grade for a two-by-ten matrix. The ordinary Eagon--Northcott complex therefore resolves B over P.

Its base change to S is the actual C^0, because PR490 identifies the actual quadratic presentation with the universal binary relation inclusion and the source shifts change from P degree one to S degree two. The direct decomposition of S into even and odd polynomial degrees is preserved by the P action and by every differential. Projection onto either parity is exact. Thus Tor_i^P(A,B) is exactly the regraded even part of M_i^0; no flatness of this specialization is required.

Reversed duality of the universal length-nine complex gives the C^8 resolution with internal shift ten. Hence omega_B=N_8(-5), after the canonical P shift -15. Together with omega_A=O(-3), PR540's derived duality gives the claimed odd-part shift 15-5-3=7. Independently, the same shift follows from the original S reciprocity: (M_i^0)_(2d) is dual to (M_(4-i)^8)_(15-2d), and 15-2d=2(7-d)+1. This directly checks both the parity and the degree convention.

## Support and dimension audit

1. PR508 Section 1 proves M_3^8 has minimum S degree at least seven by initial-degree injectivity of the left strand. PR507 reciprocity therefore gives maximum degree eight for M_1^0. Its chain term has minimum degree four. PR508 Section 3 gives its degree-four dimension ten; PR509 Section 3 gives its degree-six dimension 225. Only degrees four, six and eight survive even projection.

2. PR509 Section 4 proves support of M_2^0 is contained in S degrees seven through ten and support of M_3^0 in nine through twelve. These are genuine vanishing statements, not inferences from a list of known components. PR508 Section 2 gives dim(M_3^0)_12=dim(M_1^8)_3=85.

3. PR494 gives Sym^8 H Hilbert function (9,45,55) in S degrees zero, one and two. PR507 therefore gives M_4^0 supported in degrees thirteen through fifteen. This justifies discarding M_4^0 in both Euler calculations; PR507 also eliminates all homology above index four.

4. In S degree eight the alternating free dimension is 495-45(70)+240(15)-630=315. Q vanishes, and homology indices three and four cannot contribute. Consequently dim(M_2^0)_8=315+dim(M_1^0)_8.

5. In S degree ten the alternating free dimension is 1001-45(210)+240(70)-630(15)+1008=-91. Homology indices zero, one and four vanish. Consequently dim(M_3^0)_10=91+dim(M_2^0)_10.

Writing x=dim(M_1^0)_8 and y=dim(M_2^0)_10, the entire intermediate Hilbert functions follow exactly as stated: T_1=(10,225,x) in P degrees (2,3,4), T_2=(315+x,y) in degrees (4,5), T_3=(91+y,85) in degrees (5,6). Their length lower bounds are respectively 235,315,176. Nonnegativity of x,y suffices; no ranks or values of these parameters are assumed.

As an independent endpoint check, the same parity identification and the known Sym^8 H Hilbert function also give T_4=45 k(-7): only S degree fourteen of M_4^0 survives, and positive-degree P action necessarily vanishes. This endpoint strengthens the prior top-Tor socle statement but is not needed for the candidate's intermediate bounds.

## Contribution and limits

The parity/duality bridge translates the earlier complexes and is not by itself a new numerical theorem. The quantitative nonvanishing of all three intermediate derived-intersection modules, with their complete two-parameter Hilbert functions, is the additional conclusion beyond PR540. The argument does not identify x or y, identify either with the separate determinantal parameter k, or settle the selected source problem, higher-order lifting, or algebraicity.

Review used the displayed structural proofs and small free-module dimension arithmetic only. No selected HM/source-instance evaluation, coefficient search, numerical matrix-rank computation, or large computation was performed. No external publication was performed in this review.
