# A finite backward descent excludes the nonzero-J bf source branch

## Scope and proof status

This proposed exclusion concerns only G3.11.73682b4c817f and the nonzero internal-J branch of

    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10).

It uses the quartic subsystem published in PR819, immutable commit 03fee9278072f9ac00a5fcee5deb04b7fce61ae5:

https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BF-SUBSYSTEM.md

It additionally uses BF-THIRD-BACKWARD-QUOTIENT.md, frozen SHA256 16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0, which is awaiting its own fresh review. The present note also requires fresh independent review. No full-label exclusion is claimed.

Write U[-j] for U tensor O(-j), and 1[-j] for O(-j). Set K_i=E^{(-i)}. The input is

    K_2/K_3=W[1],   K_3/K_4=W[-1],
    rank K_3=10, degree K_3=-62,

and exactly four necessary K_3 types:

    I:   S[-5]+P[-6]+W[-9];
    II:  (P+D)[-6]+1[-8];
    III: S[-5]+P[-6]+1[-8]+1[-10];
    IV:  T[-5]+(V+1)[-8].                          (1)

All quotients are actual Gauss quotients, not merely saturated abstract target bundles. The original constant connection is used throughout. Every subsequent kernel is saturated in that same ambient constant bundle. A negative horizontal subbundle is impossible. Strict-top applies at each step: if maxdeg K<=-d, its kernel has degrees at most -d-1, and H0(K(d)) injects into the actual derivative target at twist d.

All calculations below are bounded representation identities, exact kernel sequences, and actual derivative-channel arguments. There are no selected coefficients, points, derivative values, matrices, source-instance ranks, or scans.

## 1. Three necessary types for K_4

The actual quotient K_3 -> W[-1] is onto. In types I and III its S[-5] block maps onto the Euler subline 1[-2], and its P[-6] block maps onto the Euler quotient 1. The kernels are

    ker(S[-5] -> 1[-2])=A[-6],
    ker(P[-6] -> 1)=V[-8].                          (2)

The first is the full cubic evaluation sequence. For the second, the P subsystem of Sym6 W is basepoint-free by the invariant-divisor bound. Its rank-three degree-minus-twenty-four kernel is V[-8]: after twist six its H1 budget is V and its rank and degree force that sole supported block. The extension of V[-8] by A[-6] splits, since its Ext1 vanishes by degrees.

The W[-9] block in I and the 1[-8],1[-10] blocks in III map identically to zero in W[-1]. Their Hom spaces are zero, using W not in W tensor Sym8 W, and 1 absent from W tensor Sym7 W and W tensor Sym9 W. Thus the corresponding K_4 types are

    A[-6]+V[-8]+W[-9],
    A[-6]+(V+1)[-8]+1[-10].                        (3)

For II the top kernel of (P+D)[-6] -> W[-1] is S[-7]+V[-8]. Indeed at twist six its H1 budget is V, and at twist seven its Euler character is S; the complete small budget supports V[-8] and the forced S[-7] top. The 1[-8] block maps to zero. This gives S[-7]+(V+1)[-8].

For IV the kernel of the onto top T[-5] -> W[-1] has H1 at twist five equal to S and Euler character at twist six zero. The complete small support gives the necessary alternatives

    S[-7],  or A[-6]+1[-10].

The latter is an overlist possibility; it need not be realizable by the unique top map. The 1[-8] block maps to zero. The extension by V[-8] splits in either alternative: the only potentially negative degree term is Ext1(V[-8],1[-10])=H1(V[-2]), whose invariant part is zero. Hence IV yields one of the types already listed.

Thus exactly the following necessary overlist suffices:

    a: S[-7]+(V+1)[-8];
    b: A[-6]+V[-8]+W[-9];
    c: A[-6]+(V+1)[-8]+1[-10].                     (4)

Every type has rank eight and degree minus sixty.

## 2. Force the actual quotient K_4/K_5=W[-3]

The derivative of K_4 lands in W[-3]. Its nonzero top S[-7] or A[-6] channel is the Euler subline 1[-4], with full cubic or quadratic section system. Thus its image contains this whole saturated line. The only possible component into the Euler quotient 1[-2] is V[-8]: all other lower blocks have zero Hom by the identities Sym3 W=S, Sym6 W=V+P, Sym7 W=Wp+T, Sym8 W=P+D. If the V component is nonzero, its degree-six irreducible section system is basepoint-free, so the full derivative image is W[-3].

Suppose instead that the image has rank one. It is then exactly 1[-4], because of the onto top channel.

For type a, its kernel K_5 contains A[-8]+V[-8]+1[-8]. The derivative of K_5 lands in 1[-6]. Strict-top at degree eight would inject a representation containing V+1 into H0(O(2))=A, impossible.

For types b and c, the top A[-6] has kernel W[-7]. Also V[-8] lies in K_5, since V does not occur in Sym4 W=D. The next derivative targets 1[-6]. Strict-top forces W[-7] onto that line through its full linear system. Therefore K_5/K_6=1[-6]. The V[-8] block maps trivially to 1[-6], since V is absent from Sym2 W=A; thus V[-8] lies in K_6. Now maxdeg K_6<=-8, while its derivative targets 1[-8]. Strict-top would inject V into H0(O)=1. This is impossible.

Hence the rank-one case is excluded in all three types, proving the exact saturated quotient

    K_4/K_5=W[-3].                                 (5)

## 3. Determine K_5 and eliminate one type

The kernels of the onto top-to-Euler-line maps are A[-8] in type a and W[-7] in b,c. The V[-8] map to the Euler quotient 1[-2] is onto, and its kernel is

    ker(V[-8] -> 1[-2])=Wp[-11].                   (6)

For completeness, after twisting by eight this is the kernel of V O -> O(6). It has rank two, degree minus six, and no constant sections. The only center-even rank-two negative splitting possibilities are two degree-minus-three lines with coefficient W or Wp, or 1[-2]+1[-4]. The latter would contribute a trivial section at twist two, absent from V tensor Sym2 W=P+D. At twist three the Euler character is V tensor Sym3 W-Sym9 W=Wp, identifying the coefficient as Wp.

All relevant extensions of (6) by A[-8] or W[-7] split by positive-degree Ext1 vanishing. The remaining lower blocks have zero maps to W[-3]. Therefore

    a gives (A+1)[-8]+Wp[-11];
    b gives W[-7]+W[-9]+Wp[-11];
    c gives W[-7]+1[-8]+1[-10]+Wp[-11].            (7)

All have rank six and degree minus fifty-four. The first is impossible immediately: its derivative lands in W[-5], and strict-top at degree eight would inject A+1 into W tensor Sym3 W=A+D, which contains no trivial representation.

Only the last two types in (7) remain.

## 4. Force K_5/K_6=W[-5]

The W[-7] top block maps onto the Euler 1[-6] subline of W[-5]. The only block capable of reaching the Euler quotient 1[-4] is Wp[-11]. Its nonzero degree-seven system is basepoint-free, so if nonzero the image is all W[-5].

Suppose the image has rank one. Then it is exactly 1[-6]. All lower blocks map to zero there: W is absent from Sym3 W, 1 is absent from Sym2 W and Sym4 W, and Wp is absent from Sym5 W. Thus the next kernel is respectively

    K_6=1[-8]+W[-9]+Wp[-11],
    or K_6=2 1[-8]+1[-10]+Wp[-11].

In the second case, the next derivative target is 1[-8], so strict-top cannot inject two trivial top coefficients into its single trivial section.

In the first case, strict-top forces the top 1[-8] isomorphically onto the derivative target 1[-8]. Its kernel K_7 is W[-9]+Wp[-11], after eliminating any lower graph into the isomorphic top line. The following derivative targets 1[-10], but strict-top at degree nine would inject W into H0(O(-1))=0. This is impossible.

Therefore the rank-one possibility is excluded, and

    K_5/K_6=W[-5]                                  (8)

is the full saturated image.

## 5. Determine K_6 and isolate the forced ramified quotient

The Euler-line kernel of W[-7] -> 1[-6] is 1[-8]. The Wp[-11] map to 1[-4] is onto; its line kernel has degree -22-(-4)=-18, hence is 1[-18]. The extension of 1[-18] by 1[-8] splits by Ext1 vanishing. The other blocks have zero maps into W[-5]. Thus

    K_6=1[-8]+W[-9]+1[-18],
    or K_6=2 1[-8]+1[-10]+1[-18].                 (9)

Both have rank four and degree minus forty-four. The second is impossible by strict-top: its derivative target is W[-7], whose twist-eight sections are W tensor W=1+A, with just one trivial coefficient.

For the first type, the top 1[-8] maps onto the standard Euler subline 1[-8] of W[-7]. Its quotient is 1[-6]. The W[-9] block has no component into 1[-6], since W does not occur in Sym3 W. The only possible quotient component is

    1[-18] -> 1[-6].                               (10)

If (10) were zero, the derivative image would be exactly 1[-8]. The next kernel would be W[-9]+1[-18], and its derivative would target 1[-10]. Strict-top at degree nine again gives the impossible injection W -> H0(O(-1)). Therefore (10) is nonzero.

The invariant section space of O(12) is one-dimensional. Its nonzero section f12 cuts out the twelve-point orbit. Thus (10) is a scalar multiple of f12 and has exactly that divisor. The resulting rank-two raw derivative image is

    I=1[-8]+1[-18] subset W[-7],                   (11)

not the saturated target W[-7]. To verify the asserted splitting as the actual image, the top 1[-8] and the 1[-18] source define an injective rank-two sheaf map into W[-7]; the quotient component of the latter is the nonzero f12, so the kernel is zero. The W[-9] image lies in the Euler line and adds nothing to this image sheaf. Thus the source quotient really is (11), with a degree-twelve determinant defect.

No saturation has been silently discarded. This is the precise stage where a divisor correction is forced.

## 6. The final negative kernel would be horizontal

From (11), the actual kernel of K_6 -> I is

    K_7=W[-9].                                    (12)

Indeed the 1[-18] coefficient of a kernel section must vanish after projecting through the nonzero f12. The remaining W[-9] component may map into the Euler line, but the top 1[-8] is an isomorphism onto that line, so its graph kernel is isomorphic to W[-9].

Because K_7 is the actual derivative kernel of K_6, its own derivative lands in

    (K_6/K_7)(-2)=1[-10]+1[-20].

Every map from W[-9] to this target vanishes by ordinary degrees. Hence K_7 is horizontal in the original constant ambient bundle. A saturated horizontal bundle in characteristic zero is constant and has degree zero. This contradicts degree K_7=-18.

The nonzero-J branch of the specified bf source is therefore impossible, subject to independent verification of this proof and its frozen third-backward dependency. This argument makes no claim about other compatible sources or the full stable label.
