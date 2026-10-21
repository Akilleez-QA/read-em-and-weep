# Closing the ambient section gap and determining the actual primary and node resolutions

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected actual HM/source coefficients, evaluation matrices, rank tests, numerical search, or large computation are used.

## 1. Inputs, notation, and scope

Let P=C[x0,...,x4], m=P_+, k=P/m, and write P(-a) for a free module whose basis has degree a. Let S be the actual primary surface, X its finite normalization, Z its thirty reduced nodes, and put

A=P/I_S, B=Gamma_*O_S, N=Gamma_*O_X, R=P/I_Z, M=im(N→Gamma_*(nu_*O_X/O_S)).

All modules and maps are the actual ones, not replacements specified by Hilbert functions. The following established inputs are used:

1. Normalization resolution, PR592, commit 1a2822304e0e76d985f8a083fb36548127b881a1, research/hm/normalization-resolution/PROOF.md:
   0→P(-5)^4→P(-3)^10→P⊕P(-2)^5→N→0.
   The P summand maps by the unit. In particular N is CM of dimension 3.
2. Conductor canonical module, PR596, commit c54a80181e0e63a9f6a7404c07c525db131e3590, research/hm/conductor-canonical-module/PROOF.md:
   0→B→N→M→0, M≅omega_R(-5), omega_R=Ext^4_P(R,P(-5)).
   R is CM of dimension 1, with h-vector (1,4,10,10,5), no quadrics, and minimal last free term F4(R)=P(-8)^5. M has five generators, all in degree 2, and F4(M)=P(-10). Also B is finite, depth B=2, reg B=7, and A⊂B is the actual unit image with finite-length quotient.
3. Low-equation exclusion, PR595, commit 1107ece91d6ef00a097bfc35cb32c463ee82bc87, research/hm/low-equation-exclusion/PROOF.md: I_S,d=0 and A_d=B_d for 0≤d≤4.
4. Quintic exclusion, commit 4392ed5dfce5f706ea80733b25f8c7fc507a4a58, research/hm/quintic-gap/PROOF.md and REVIEW.md: I_S,5=0 and A_5=B_5. This independently reviewed structural proof does not use any conclusion here.

Exact dependency links:

- Normalization resolution: https://github.com/Akilleez-QA/read-em-and-weep/blob/1a2822304e0e76d985f8a083fb36548127b881a1/research/hm/normalization-resolution/PROOF.md
- Conductor canonical module: https://github.com/Akilleez-QA/read-em-and-weep/blob/c54a80181e0e63a9f6a7404c07c525db131e3590/research/hm/conductor-canonical-module/PROOF.md
- Low-equation exclusion: https://github.com/Akilleez-QA/read-em-and-weep/blob/1107ece91d6ef00a097bfc35cb32c463ee82bc87/research/hm/low-equation-exclusion/PROOF.md
- Quintic exclusion: https://github.com/Akilleez-QA/read-em-and-weep/blob/4392ed5dfce5f706ea80733b25f8c7fc507a4a58/research/hm/quintic-gap/PROOF.md
- Quintic review: https://github.com/Akilleez-QA/read-em-and-weep/blob/4392ed5dfce5f706ea80733b25f8c7fc507a4a58/research/hm/quintic-gap/REVIEW.md

The theorem proved here is A=B, followed by the actual minimal resolutions

0→P(-10)→P(-7)^10→P(-6)^10→I_S→0,

0→P(-8)^5→P(-7)^10→P(-4)^10⊕P(-5)^4→P(-3)^10→P→R→0.

The first assertion means every ambient restriction P_d→H0(S,O_S(d)) is surjective. It does NOT mean that S or A is normal/integrally closed: S has nonnormal nodes, and B⊊N. No conclusion about full-adjoint lifting, prescribed sources, or algebraicity is claimed.

## 2. Degree bounds from an actual minimal resolution

Write F_i=F_i(R) for the actual minimal free resolution of R. Since R is CM of dimension 1 over P, its projective dimension is 4. There are no linear or quadratic equations, so every summand of F1 has basis degree at least 3. Minimality then implies that every summand of F2 has degree at least 4 and every summand of F3 has degree at least 5.

Here is the elementary justification for this use of minimality. Every basis vector of a nonzero free term has a nonzero image under its differential: if it mapped to zero, exactness would put that basis vector in the image of the next differential, which lies in m times the free term, an impossibility. Each nonzero matrix entry of a minimal differential has positive degree. A basis degree in F_i therefore exceeds at least one degree occurring in F_(i-1), and hence exceeds its minimum degree.

Canonical duality, with the additional (-5) twist defining M, identifies its minimal resolution term by term as

F_i(M)=Hom_P(F_(4-i)(R),P(-10)),  0≤i≤4.                 (1)

This is exact because R is CM of codimension 4: its dual complex has cohomology only at Ext^4. Dualization preserves minimality since all entries remain in m. Thus a summand P(-a) of F_(4-i)(R) contributes P(-(10-a)) to F_i(M). In particular

Tor_1^P(M,k) is supported in degrees at most 5,             (2)
Tor_2^P(M,k) is supported in degrees at most 6.             (3)

These upper bounds are established before identifying A with B or computing any unknown middle Betti number.

## 3. The finite-degree test closes the entire ambient gap

Apply Tor^P(-,k) to the actual exact sequence 0→B→N→M→0. Its end is

Tor_1(M,k)→B/mB→N/mN→M/mM→0.                              (4)

The map N/mN→M/mM is an isomorphism on the five degree-two generators and kills exactly the degree-zero unit. Indeed the surjection N→M induces a surjection on minimal-generator quotients, N/mN=k⊕k(-2)^5, and M/mM=k(-2)^5. Degree preservation and equal dimensions prove the stated isomorphism without selecting a matrix. Therefore the kernel in (4) is precisely k in degree zero. Combining this with (2), B/mB has no nonzero graded piece above degree 5.

Inputs 3–4 say that every B_d for 0≤d≤5 is the image of the unit map P_d→B_d. For 1≤d≤5 this image lies in (mB)_d. There are no negative sections, since B⊂N and N has none. Also B_0=k. Consequently B/mB=k, concentrated in degree zero and generated by the unit. Graded Nakayama, for the finite graded P-module B, implies P·1=B. Its image is A by definition, so

A=B.                                                       (5)

In particular depth A=2, reg A=7, and pd_P A=3. The argument uses only the low-degree agreement through 5 and the upper bound (2); it does not assume that higher restriction maps are surjective. The absence of primary equations through degree 5 is not needed for this generation argument but is needed in the following Tor computation.

## 4. The top two primary syzygies and the cubic node generators

Use T_i(V)=Tor_i^P(V,k). We now have the actual exact sequence

0→A→N→M→0.                                                (6)

Since pd N=2 and T4(M)=k(-10), the long exact sequence gives

T3(A)≅T4(M)=k(-10).                                       (7)

There is no missing term: T4(N)=T3(N)=0. Next the exact segment is

0→T3(M)→T2(A)→T2(N)→T2(M)→T1(A)→T1(N)→T1(M)
 →T0(A)→T0(N)→T0(M)→0.                                   (8)

Because I_S has no equations through degree 5, all degrees of T1(A) are at least 6, and minimality gives all degrees of T2(A) at least 7. On the other hand T2(N)=k(-5)^4. Thus the degree-zero map T2(A)→T2(N) vanishes, and (8) yields

T3(M)≅T2(A), supported in degrees at least 7.              (9)

By (1), the degrees of T3(M) are 10 minus the generator degrees of I_Z, namely the degrees of F1(R). Equation (9) therefore bounds those generator degrees above by 3. The lower bound from Section 2 was 3. Hence I_Z is generated entirely in degree 3. Its number of generators is

dim(I_Z)_3=dim P_3−dim R_3=35−25=10.

It follows that

T1(R)=k(-3)^10, T3(M)=k(-7)^10, T2(A)=k(-7)^10.            (10)

In particular the cubic generation of the actual node ideal is derived from the actual extension, not assumed from its Hilbert function.

## 5. The remaining primary and node terms

The map T1(A)→T1(N) vanishes, since the source is supported in degrees at least 6 while T1(N)=k(-3)^10. Moreover T0(A)→T0(N) sends its degree-zero unit injectively to the unit of N. Exactness of (8) consequently gives an isomorphism

T1(N)≅T1(M)=k(-3)^10.                                    (11)

By (1), this determines F3(R)=P(-7)^10. The same exact sequence, with the zero maps just proved, gives

0→k(-5)^4→T2(M)→T1(A)→0.                                 (12)

By (3), the middle term has no degree above 6; the last term has no degree below 6. Thus T1(A) is supported only in degree 6. Let its dimension be b. No cancellation hypothesis has been used.

The Hilbert series now fixes b. Inputs 1–2 and (5) give

Hilb_A=Hilb_N−Hilb_M,
Hilb_N=(1+5t²−10t³+4t⁵)/(1−t)^5,
Hilb_M=t²(5+10t+10t²+4t³+t⁴)/(1−t).

Multiplying by (1−t)^5 and subtracting gives

(1−t)^5 Hilb_A=1−10t⁶+10t⁷−t¹⁰.                          (13)

The Tor degree supports have already been proved: T0(A)=k, T1(A)=k(-6)^b, T2(A)=k(-7)^10, T3(A)=k(-10), and no higher Tor. Their alternating numerator is 1−bt⁶+10t⁷−t¹⁰, so (13) forces b=10. Therefore the actual minimal resolution of A is

0→P(-10)→P(-7)^10→P(-6)^10→P→A→0.                        (14)

Removing its final P→A gives the claimed ideal resolution. This use of Hilbert series determines only a multiplicity after degree supports and exactness have already been forced; it does not guess a resolution from a numerator.

Equation (12), degree by degree, now determines

T2(M)=k(-5)^4⊕k(-6)^10.

Duality (1) gives F2(R)=P(-5)^4⊕P(-4)^10. Combining this with F1(R), F3(R), and Input 2's F4(R) proves the claimed node-ring resolution. For completeness, the actual minimal M-resolution is

0→P(-10)→P(-7)^10→P(-6)^10⊕P(-5)^4→P(-3)^10→P(-2)^5→M→0.

Every differential is a differential of an existing minimal resolution of the specified actual module, or its canonical dual. The proof determines the ranks and twists; it does not claim to produce explicit matrices. Positive shifts on each permissible nonzero differential are consistent with, and already guaranteed by, minimality.

## 6. Dependency and conclusion audit

The logical order is: known canonical duality and no node quadrics → upper bound on T1(M) → generation of B in degrees at most 5 → low-degree ambient agreement forces A=B → primary generator lower bound → T3(M) and T2(A) comparison → cubic generation of I_Z → remaining Tor supports → Hilbert multiplicity. None of the output resolutions is used as an input, and no full-adjoint statement enters.

The result resolves both the entire finite-length ambient gap and the middle Betti ambiguity for the actual primary/node modules, using the independently reviewed and immutably pinned quintic input. The primary coordinate ring has depth 2 and regularity 7, not Cohen–Macaulay; its complete section property is not integral closedness. The full-adjoint and prescribed-source dependencies remain separate.
