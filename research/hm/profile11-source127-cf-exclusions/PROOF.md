# The double twelve-orbit obstruction excludes both cf-family source127 edges

## Statement and boundary

For the original zero-defect label

    G3.11.cce6e3ba4eeb, source_index127,
    A_q=O(-8)+O(2)+O(16), B_q=O(-18)+O(-4)+O(6),

the following two entire source edges are impossible:

    (0,0,1,0,0,1,0,1):
      E=(V+P+D) O(-2)+V O(-4)+O(-8)+O(-10);
    (0,0,1,0,0,0,1,0):
      E=(V+P+D) O(-2)+V O(-4)+W O(-9).

The proof checks the exact transfer of the high-line reduction from PR861 and then retains the projected image's torsion: the modification has exactly twice the reduced twelve-point orbit, not zero. Dual cohomology forces a rank-eleven subbundle with two Wp top copies, but the actual dual quotient admits only one. Both scalar and Euler ways of supplying the negative endpoint are covered without assuming any individual endpoint component nonzero.

This is two source-edge exclusions, not a whole-label exclusion or a global rank result. No compatible-pair count or frontier decrement is claimed. No selected actual HM/source coefficients, parameters, points, derivatives, matrices, source-instance ranks, selected models, scans, or large computation are used. The stabilizer argument is uniform over an orbit, not evaluation at a selected actual parameter.

## 1. Immutable actual input and the transferred interfaces

The original actual source, strict-top, quotient and stable-label inputs are at commit db51525015bb7c5e825833d550d08dedf6f6ea96:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, one-one-endpoint-necessary-pairs.json, and rank-three-quotient-frontier-144.json. Their Git blobs and immutable paths are in the accompanying manifest. The source decoder and original entry127 give exactly the two displayed bundles, each rank17 and degree-54.

PR861, commit 7b5b3371a82cb92f46ea60895e45617d0891a5b0, proves the high-line subsystem, basepoint-free polar contradiction, and exact intersections for the cf source at index113:

https://github.com/Akilleez-QA/read-em-and-weep/blob/7b5b3371a82cb92f46ea60895e45617d0891a5b0/research/hm/profile11-source113-cf-reduction/PROOF.md

We do not assume that its source113 statement automatically applies here. Sections2-3 below recheck every interface affected by replacing the negative quotient and either tail, and restate the proof used. The subsequent double-divisor and dual arguments are proved here for source127. No unpublished source113 completion is a dependency.

The other interfaces are PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac, Section3 (actual saturated internal/external derivative images), and PR802, commit e484640a6565c278321bf6557860262c1ac1b7df, Sections3 and5 (exact small kernels and first-polar generation):

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

Work over C with the binary icosahedral group G and irreducibles W,Wp,A,V,P,S,D,T as in those sources. In particular A=Sym2 W, S=Sym3 W, D=Sym4 W and T=Sym5 W. There are no nontrivial one-dimensional characters. Every nonempty invariant effective divisor has degree at least12; an invariant divisor of degree12 is the reduced exceptional orbit D12.

The actual E is saturated in H O, dim H=30, spans H, and has all degrees at most-2. Strict-top gives H0(E^-(2))=0. Original determinant defect zero gives the actual saturated quotient

    E^+/E=A2=O(-6)+O(4)+O(18) subset Q=H O/E.    (1)

Write the lower source tail as

    N=O(-8)+O(-10) or W O(-9).

Thus N has rank2 and degree-18, and every degree of N(-2) is at most-10. Every derivative and constant projection below uses the original trivial connection.

## 2. The basepoint-free high-line branch is excluded for both tails

The D O(-2) component to O(2) cannot be zero. Otherwise the entire top (V+P+D) O(-2) maps only to O(16). Strict-top and its twelve independent sections make this map onto, because a nonempty common invariant divisor would leave at most seven sections. Its complete kernels, as in PR802, are

    T O(-3)+P O(-4)+O(-6),
    (Wp+T) O(-3)+Wp O(-5)+O(-6).

The internal target is V O(-6)+N(-2). Every component vanishes, including O(-6)->V O(-6). Thus the raw derivative is saturated rank one and the first-span quotient is O(18). The quadratic Gauss gap at rank12 would require18=24 or18<=11, impossible. The D-to-O(2) row is therefore nonzero and onto.

Set F=(V+P) O(-2). It maps only to O(16), since neither V nor P occurs in Sym4 W=D. Its seven sections are independent. Their common divisor has degree0 or12, and a degree12 divisor leaves the complete Sym6 W=V+P system.

If it is basepoint-free, the exact four possible kernels from PR861 Section3 are

    P O(-4)+W O(-7);
    Wp O(-3)+Wp O(-5)+W O(-7);
    P O(-4)+O(-6)+O(-8);
    Wp O(-3)+Wp O(-5)+O(-6)+O(-8).                (2)

This list uses only F and its onto degree-eighteen system, not the lower endpoint. For our two sources the actual internal target is

    D O(-4)+V O(-6)+N(-2).

The complete internal possibilities are still precisely 0, W O(-7), O(-8), with the two nonzero images entering D O(-4) by the saturated universal multiplication W tensor l^3 and tautological fourth-power line. Every new tail component is zero by degree. The V target exceptions are the same zero Hom spaces as in PR861.

The actual-image lemma and first polars now give exactly its three cases: zero internal image has positive first-span degree4; O(-8) has constant character A+P and nongenuine linear character T-S. The only remaining possibility is

    M=F^+=P O+T O(-1), J=W O(-7).               (3)

Here is the rest of the transferred contradiction, with the changed negative quotient retained. Project by the actual constant P in (3). The map F->T O(-1) has channels from V and P. The P channel is nonzero, because otherwise P O(-2) would inject into constant P of equal rank with an invariant degree-eight determinant, which does not exist. Both channels cannot be nonzero, since then their map is the onto complete Euler contraction Sym6 W O(-2)->Sym5 W O(-1), making the negative target horizontal. Thus the V channel is zero.

For an actual saturated linear R O(-1) with constant coefficient kernel Kc in R W, its derivative kernel is Kc O(-2), by the Euler sequence and fiberwise injectivity. Applying this to T O(-1), its coefficient kernel contains P. The multiplicity-free T W=V+P+D and its constant span of dimension at least7 force Kc=P. Consequently the full actual constant span Ctot of M has

    Ctot=P+V+D, dim Ctot=12,
    Ctot O/M=Wp O(3), M/M^-=Wp O(1), rank M^-=8.

The intersection E intersect M has quotient W O(-5) by F and rank9. Its induced map W O(-5)->Wp O(1) is nonzero, because rank9 cannot lie in M^- of rank8. It has generic rank2: a rank-one saturated image would be O(d), d<=1; the first map requires -5<=d and W in Sym(d+5), forcing d=-4, whereas O(-4)->Wp O(1) is zero because Wp is absent from Sym5 W.

The actual derivative of M identifies the two rank-two quotients above after twisting by-2. Therefore derivatives of E intersect M force Ctot O into E^+; saturation upgrades generic containment. Its map to the lower summands of (1) is zero on M and factors through Wp O(3). Both Hom spaces to O(4) and O(-6) vanish, respectively because Wp is not W and by degree. Thus its image in E^+/E lies only in O(18), giving a rank-eleven kernel in E of degree at least-18. Every subbundle of E has all degrees at most-2, so this kernel must have degree at most-22. Contradiction.

This rechecks the entire basepoint-free exclusion for both tails and for the new O(-6) quotient in (1); it imports no source113 whole-edge conclusion.

## 3. The remaining branch has exact actual intersections

The high line therefore has divisor D12, with residual complete degree-six system. Its kernel is T O(-3), whose actual internal derivative into D O(-4)+V O(-6)+N(-2) is zero by degree. The raw first span has rank8 and degree-8. Its invariant saturation defect is at most8, but a nonzero defect would have length at least12. It is consequently already saturated and

    M=F^+=(Wp+T) O(-1)=Sym7 W O(-1).

Its derivative kills F and has rank at most one. It is nonzero because M is negative and saturated. A linear bundle reaches its full constant span after one derivative, so that span C has dimension9. The complete degree-eight Euler sequence identifies

    C=Sym8 W=P+D,
    C O/M=O(8), M/F=O(6), C O/F=W O(7), M^-=F.  (4)

We need the actual intersections, not a presumed saturated projection. If C O lay in E^+, its quotient W O(7) by F would map to (1), with both lower components zero by degree. Its high component is nonzero and onto: two independent degree-eleven sections have no nonempty invariant common divisor. Its kernel is O(-4), which would inject into

    E/F=D O(-2)+V O(-4)+N.

Every equivariant Hom from O(-4) to this bundle is zero. For D the coefficient would have to occur in Sym2 W=A; for V it would be an invariant vector; the tails are too negative. Hence C is not contained in E^+. Since M lies in the intersection and is saturated, C O intersect E^+=M. If E intersect C O is denoted N0, derivatives of N0 lie in C O intersect E^+=M. Because N0 lies in M, it lies in M^-=F. Therefore

    E intersect C O=F, E^+ intersect C O=M.       (5)

The projected image Z0=E/F in (H/C) O is thus an injective image sheaf, with rank10 and degree-40, spanning the constant twenty-one-space. It is not asserted saturated.

## 4. Derivative compatibility and stabilizer characters force two copies of D12

Set Qplus=H O/E^+ and L=O(18) subset A2. Equation(5) gives an injective sheaf map

    j:C O/M=O(8)->Qplus.

The derivative of E^+ kills E, so its restriction to the highest line of A2 is a map phi:O(18)->Qplus(-2). The derivative of M induces the isomorphism M/F=O(6)->(C O/M)(-2)=O(6). Its comparison with the map M/F->L, which is multiplication by f12, yields

    j(-2)=f12 phi                                (6)

up to a nonzero scalar. Thus j vanishes on D12. No saturation of j or phi is assumed.

Because L is saturated in Q, take Q/L. The inclusion B=C O/F=W O(7)->Q induces

    k:B/(M/F)=O(8)->Q/L.

Its projection to Qplus is j. At every point of D12, its fiber image therefore lies in A2/L=O(-6)+O(4). For an arbitrary binary stabilizer with tautological eigenvalue zeta of order10, the fiber of O(a) has character zeta^(-a). Thus

    domain O(8): zeta^2;
    targets O(-6), O(4): zeta^6, zeta^6.

These differ, so equivariance forces k to vanish at every point of D12. Since that orbit is reduced, k factors through f12:O(8)->O(20). This is a fiberwise divisibility argument in Q/L; it does not assume a global projection from Q to its lower quotient summands.

Locally split the saturated line L in Q and choose a frame of B extending M/F. Its first column is f12 times a generator of L. The second column modulo L is also divisible by f12. Therefore every rank-two minor of B->Q is divisible by f12 squared. The saturation defect divisor of B in Q is at least2D12.

The inclusions B->Q and Z0->(H/C) O have the same cokernel H O/(E+C O); its torsion is their respective saturation quotient. Their complete defect divisors therefore coincide, including multiplicities. If the total length is delta, the saturation Z of Z0 has

    delta>=24, rank Z=10, deg Z=-40+delta.       (7)

## 5. Full span makes the double divisor exact

Z spans the constant twenty-one-space H/C. Its splitting degrees are nonpositive, so h0(Z*)=rank Z-deg Z=50-delta. Full span makes (H/C)*->H0(Z*) injective. Thus delta<=29.

The invariant effective divisor obtained by subtracting2D12 from the defect divisor has degree between0 and5. The invariant-divisor lower bound12 forces it empty. Hence

    defect divisor=2D12, delta=24, deg Z=-16.    (8)

Let Sigma be the saturation of B in Q. Then rank Sigma=2 and deg Sigma=14+24=38. It contains the whole saturated L, since B contains f12 O(6) with generic span L. Consequently

    0 -> O(18) -> Sigma -> O(20) ->0.            (9)

The equivariant extension space is H1(O(-2)), a one-dimensional trivial representation. Thus the only bundle types are

    Sigma=O(18)+O(20), or Sigma=W O(19).         (10)

This is not a horizontal splitting or an assertion that either extension occurs.

## 6. Dual cohomology forces too many Wp top sections

Set R=(Q/Sigma)*. There is an exact sequence

    0 -> R -> Q* -> Sigma* ->0.                  (11)

Here rank R=11 and deg R=-16. The pinned actual-bundle presentation gives

    0 -> Q* -> M3* O(-1) -> M2* O ->0,
    M3=3Wp+3S+6T, M2=A+2V+3P+4D.

Therefore

    H1(Q*)=M2,
    chi_G(Q*(3))=T-2W-S.                        (12)

Q* has no constant sections, so every splitting degree of Q*, and of R, is at most-1. We do not assume H0(Q*(1))=0.

Both types in (10) have the same equivariant K-class. Their negative duals satisfy

    H1(Sigma*)=Sym16 W+Sym18 W=A+2V+3P+3D,
    chi_G(Sigma*(3))=-Sym13 W-Sym15 W.

Negativity makes all relevant H0 groups at twist0 vanish. The cohomology of (11) thus gives

    H1(R)=D,
    chi_G(R(3))=-W+Wp+S+4T.                     (13)

For these identities Sym13 W=W+Wp+S+T and Sym15 W=S+2T.

There are exactly two possible negative-block supports for H1(R)=D. An atom U O(-j), j>=2, contributes U Sym(j-2) W, with (j-1)dim U<=5. At j2 only D fits; at j3 the four odd irreducibles tensored by W give1+A, P, A+D, V+P+D, none a subcharacter of D; at j4 the only dimension-eligible scalar gives A; at j5 no odd irreducible fits; at j6 the scalar gives D. All later atoms exceed the dimension bound. Thus

    R=L6 O(-1)+D O(-2), or R=L10 O(-1)+O(-6).   (14)

The first option and (13) would require L6 A=-W+Wp+3T, not a genuine character. In the second, (13) gives L10 A=Wp+S+4T. The identities

    W A=W+S, Wp A=T,
    S A=W+S+T, T A=Wp+S+2T

then force L10=2Wp+T: absence of W eliminates W and S coefficients, the Wp and S terms require one T, and the remaining T multiplicity requires two Wp. Hence

    R=(2Wp+T) O(-1)+O(-6).                     (15)

Apply strict-top to the actual Q*, whose degrees are at most-1. Its actual Gauss quotient is the original B_q=O(-18)+O(-4)+O(6), so strict-top supplies an injection

    H0(Q*(1)) -> H0(B_q(1))=Sym7 W=Wp+T.       (16)

But the subbundle R supplies H0(R(1))=2Wp+T inside H0(Q*(1)). The two Wp copies cannot inject into the single Wp copy of (16). This contradiction excludes the divisor-twelve branch for both tails.

## Conclusion and verification boundary

Section2 excludes the basepoint-free branch and Sections3-6 exclude the only nonempty common-divisor branch. Both entire source edges in the statement are therefore impossible. The proof retains the exact length24 modification and does not assume a saturated projected residual prematurely.

The bounded verifier checks both original source identities, all changed Hom channels and quotient rows, stabilizer exponents, character budgets, dual support and multiplicities, and degree arithmetic. The actual connection, double-divisor, saturation and span arguments are mathematical proofs above, not consequences of executing the verifier. This is not Lean certification, a whole-label exclusion, or a global conclusion.
