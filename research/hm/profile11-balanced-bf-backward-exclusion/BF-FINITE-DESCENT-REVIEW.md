# Independent review: finite backward descent for the bf source

## Verdict, exact bytes, and scope

**PASS.** The argument in `BF-FINITE-BACKWARD-DESCENT.md`, SHA256

`9558490385822a4d559d555c4f3372fd594e7ef0f504454da0707d962cf9fd49`,

correctly excludes the nonzero-internal-J branch of the source

    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10)

for stable label G3.11.73682b4c817f, subject to its explicitly pinned third-backward-quotient input. The two intermediate derivative images are genuinely the complete bundles W O(-3) and W O(-5). At the next stage the raw image is instead O(-8)+O(-18), with a compulsory determinant defect of degree 12 inside W O(-7). Retaining this raw image, rather than replacing it with its saturation, yields the final contradiction. No mathematical blocker was found.

This is not an exclusion of the entire stable label, and is not by itself an exclusion of the source's J=0 branch. Any combination with a separate J=0 result must retain that result's scope and pins.

The immediate dependency is `BF-THIRD-BACKWARD-QUOTIENT.md`, SHA256

`16475cd7d6012fff2efd8d3ec04bce884231ffbfe664914e948584c24afa69d0`.

The review here checks the finite continuation from its exact quotient and four-type conclusions. The dependency has its own independent review in `BF-BACKWARD-REVIEW.md`; its separate proof is not replaced by assuming the desired exclusion.

## Immutable sources

The quartic subsystem is [BF-SUBSYSTEM.md at the PR819 commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BF-SUBSYSTEM.md), commit `03fee9278072f9ac00a5fcee5deb04b7fce61ae5`, SHA256 `087d0b78196b7c0d5e773375e603359450e0e9fb0ebb3003734c44eea4e133b9`.

The original data and geometric lemmas are at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, under `research/hm/order-four-quadratic-load/`:

- [Actual equivariant splitting and Gauss persistence](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md), Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- [Negative Gauss kernels strictly lower the top slope](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md), Git blob `d7506dae49b4be43230450c4132bd5db91f137ef`.
- [The stable-label frontier](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json), Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`.
- [The necessary-pair list](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json), Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`.

The source is source_index72, tuple (0,1,0,0,0,1,0,1), in the zero-defect balanced label with A_q=O(-10)+W O(5). The subsystem's earlier principles are pinned at PR796 commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac` and PR799 commit `2172e4a7abbbe232f9f448bea6fa01dee7927460` in its dependency manifest.

## 1. Geometric rules used throughout

Write U[-j]=U tensor O(-j), K_i=E^(-i). Every K_i is an actual saturated subbundle of the original constant bundle. If K_(i+1) is the kernel of the second fundamental form of K_i, then derivatives of its sections lie in K_i. Its own second fundamental form therefore lands in

    (K_i/K_(i+1))(-2).

This statement uses the actual quotient, whether or not its identified image is saturated in an earlier derivative target. The quotient is locally free on P1 because it is isomorphic to a torsion-free image sheaf. Saturation of K_(i+1) in the constant ambient bundle follows from the two successive locally free quotients.

The pinned strict-top lemma applies whenever maxdeg K_i<=-d with d>0: its next kernel has maxdeg at most -d-1, and H0(K_i(d)) injects into the sections of any bundle through which its actual derivative factors. This is section injectivity, not fiberwise injectivity. All applications below have negative top degree and satisfy these hypotheses.

Over characteristic zero a saturated horizontal subbundle of a constant bundle is constant, hence has degree zero. Thus a nonzero negative such bundle cannot have zero derivative.

Equivariant Birkhoff–Grothendieck splitting is used for maps and cohomology, not as a splitting of the connection. Over the finite group in characteristic zero, an ordinary vanishing Ext1 also gives equivariant splitting. More generally

    Ext1_G(U[-a],R[-b])=(U* tensor R tensor H1(O(a-b)))^G.

All irreducibles used here are self-dual; the one-dimensional representation is trivial. Center parity requires the coefficient of O(-j) to have parity (-1)^j.

## 2. Independent character audit

The tensor-with-W identities used in the continuation are

    W^2=1+A,  WA=W+S,  WS=A+D,  WD=S+T,
    WT=V+P+D,  WV=T,  WP=Wp+T,  WWp=P.

The recurrence for symmetric powers gives

    Sym2 W=A,          Sym3 W=S,          Sym4 W=D,
    Sym5 W=T,          Sym6 W=V+P,        Sym7 W=Wp+T,
    Sym8 W=P+D,        Sym9 W=S+T,        Sym10 W=A+V+D,
    Sym11 W=W+S+T,     Sym12 W=1+A+P+D.

Also VA=P+D and VS=Wp+S+T. In particular the invariant section space in degree 12 has dimension one.

For checking full maps to W[-b], the relevant section representations are

    W Sym3 W=A+D,
    W Sym4 W=S+T,
    W Sym5 W=V+P+D,
    W Sym6 W=Wp+2T,
    W Sym7 W=V+2P+D,
    W Sym8 W=Wp+S+2T,
    W Sym9 W=A+V+P+2D.

These independently verify every asserted absent Hom channel. In each Euler-line top channel the relevant irreducible occurs exactly once, and its known complete evaluation followed by Euler inclusion is nonzero. Thus the unique channel is precisely that Euler-line channel.

Whenever a nonzero V, P, or Wp section system of degree 6 or 7 is used, irreducibility makes the coefficient map injective. Its common-zero divisor is invariant and has degree at most 6 or 7. The minimum degree 12 for a nonempty invariant divisor makes the system basepoint-free. No generic-rank argument is being substituted for this everywhere-surjectivity argument.

## 3. All K4 kernels and extensions

The pinned input is K3/K4=W[-1], with K3 of rank 10, degree -62, and the four listed types I–IV.

For I and III, the S[-5] top maps onto the Euler 1[-2] line. Its complete cubic evaluation kernel is A[-6]. The P[-6] map onto the Euler quotient 1 has kernel V[-8]. To check the latter identification independently, the kernel has no sections at twist 6, and its H1 there is Sym6 W-P=V. All its degrees are therefore at most -7. Among blocks of degree at most -8, the only contribution supported by this three-dimensional H1 budget is V[-8]: at degree -8 the coefficient must be V; odd degree -9 exceeds the dimension budget; at degree -10 the only possible coefficient 1 contributes A, not V; all further possibilities exceed the budget. Its rank 3 is already exhausted. Thus V[-8] is forced, without a realizability assumption.

The resulting extension of V[-8] by A[-6] splits because H1(O(2))=0. The remaining blocks map identically to zero in W[-1]: W is absent from W Sym8 W, while 1 is absent from W Sym7 W and W Sym9 W. Hence I and III give

    A[-6]+V[-8]+W[-9],
    A[-6]+(V+1)[-8]+1[-10].

For II, the onto (P+D)[-6] top map has kernel Q with no twist-six sections and H1(Q(6))=V. The same supported-block audit forces V[-8] below degree -7. At twist 7 its Euler character is S, so its remaining top is S[-7]. The zero-map 1[-8] block gives

    S[-7]+(V+1)[-8].

For IV, the onto T[-5] top map has kernel Q with maxdeg Q<=-6, H1(Q(5))=S, and chi_G(Q(6))=0. The complete small support is especially short. Below degree -6 only S[-7] and 1[-10] can contribute within the S budget. At degree -7 the coefficient must be S; at degree -8 only the trivial coefficient fits the dimension bound, and it contributes W, not S; odd degree -9 already exceeds that bound; degree -10 contributes Sym3 W=S; later degrees exceed it. Accordingly Q is either S[-7], or A[-6]+1[-10], the latter top being forced by the twist-six character. This is a necessary overlist, as claimed.

The extension by V[-8] splits in both alternatives. The only non-ordinary-positive case is

    Ext1_G(V[-8],1[-10])=(V tensor H1(O(-2)))^G=V^G=0.

The 1[-8] summand has zero map to W[-1] and remains a direct kernel summand. Consequently the exact necessary K4 overlist is

    a: S[-7]+(V+1)[-8],
    b: A[-6]+V[-8]+W[-9],
    c: A[-6]+(V+1)[-8]+1[-10].

Each has rank 8 and degree -60.

## 4. The first new exact image and its kernels

The derivative of K4 lands in W[-3]. Strict-top makes its top S[-7] or A[-6] channel nonzero. By uniqueness this channel is the full Euler 1[-4] line. On projecting to the Euler quotient 1[-2], only V[-8] can contribute: all other coefficients are absent from the appropriate symmetric powers listed above. A nonzero V channel is basepoint-free, and together with the full Euler line gives the whole W[-3], not merely its saturation.

If the V quotient channel were zero, the raw image would be exactly 1[-4]. For a, K5 then contains (A+V+1)[-8], while its derivative target is 1[-6]. Strict-top at twist 8 cannot inject V+1 into H0(O(2))=A.

For b,c, K5 contains W[-7] and V[-8]. The former is the complete quadratic-evaluation kernel; the latter is killed because V is absent from Sym4 W. Strict-top forces the W top to surject to the next target 1[-6] through its full linear system. The V[-8] summand is again killed because V is absent from Sym2 W. Therefore K6 contains V[-8] and has maxdeg at most -8, but its derivative targets 1[-8]. Strict-top would inject V into 1, a contradiction. All generic-rank-one cases, and automatically rank zero because of the nonzero top channel, are excluded. Hence

    K4/K5=W[-3].

The V[-8] quotient channel to 1[-2] has kernel Wp[-11]. After twisting by 8 its kernel has rank 2, degree -6, and no constant sections. Center parity leaves only W[-3], Wp[-3], or 1[-2]+1[-4]. The last is excluded by the absence of 1 in VA=P+D. At twist 3 the character VS-Sym9 W=Wp identifies the remaining coefficient. This checks the asserted kernel without selecting a map instance.

The top Euler-line kernels are A[-8] for a and W[-7] for b,c. Extensions by Wp[-11] split by H1(O(3))=H1(O(4))=0. All remaining lower blocks have zero full map to W[-3], as checked by W Sym5 W, W Sym6 W, and W Sym7 W. Thus K5 is respectively

    (A+1)[-8]+Wp[-11],
    W[-7]+W[-9]+Wp[-11],
    W[-7]+1[-8]+1[-10]+Wp[-11].

Each has rank 6 and degree -54. The first is impossible: strict-top at twist 8 would inject A+1 into W Sym3 W=A+D, which contains no 1.

## 5. The second new exact image and its kernels

For either remaining K5, the unique W[-7] top channel maps onto the Euler 1[-6] line in W[-5]. Only Wp[-11] can reach the Euler quotient 1[-4]. Its nonzero degree-seven system is basepoint-free, so a nonzero quotient channel again makes the full derivative image W[-5].

If that quotient channel is zero, the raw image is exactly 1[-6]. Every lower block maps trivially to this line, by the absences W from Sym3 W, 1 from Sym2 W and Sym4 W, and Wp from Sym5 W. The next kernel is therefore

    1[-8]+W[-9]+Wp[-11],
    or 2 1[-8]+1[-10]+Wp[-11].

The second type violates strict-top against the next target 1[-8], which has only one trivial twist-eight section. In the first type, strict-top forces the top 1[-8] isomorphically onto that target. Removing lower graph components gives kernel W[-9]+Wp[-11]. Its next derivative targets 1[-10], whose twist-nine sections vanish, contradicting the W top. Thus

    K5/K6=W[-5]

as an everywhere-surjective actual image.

The top kernel is 1[-8]. The basepoint-free Wp[-11] map to 1[-4] has line kernel of degree -18, necessarily 1[-18]. Its extension by 1[-8] splits since H1(O(10))=0. All remaining lower full maps to W[-5] vanish: W is absent from W Sym4 W and 1 is absent from W Sym3 W and W Sym5 W. Consequently

    K6=1[-8]+W[-9]+1[-18],
    or K6=2 1[-8]+1[-10]+1[-18].

Each has rank 4 and degree -44. The second violates strict-top at twist 8 because the derivative target W[-7] has sections W^2=1+A, with only one trivial copy. This checks every K6 alternative and does not impose a false saturation assumption at the subsequent step.

## 6. The compulsory defect and final contradiction

In the surviving K6, strict-top forces its top 1[-8] onto the unique Euler 1[-8] subline of W[-7]. The W[-9] block has zero component in the Euler quotient 1[-6], since W is absent from Sym3 W. Only 1[-18] can reach that quotient.

If its quotient component were zero, the derivative image would be exactly 1[-8]. Taking the graph kernel gives W[-9]+1[-18], whose next derivative targets 1[-10]. Strict-top at twist 9 is again impossible. Therefore the quotient component 1[-18]->1[-6] is nonzero.

It is a nonzero invariant section of O(12). The independent symmetric-power calculation above shows that this invariant space is one-dimensional. Its degree-12 zero divisor is invariant; the minimum orbit size 12 forces it to be precisely the reduced twelve-point orbit.

Let B=1[-8]+1[-18] be the sum of the top and lowest source summands. The restricted derivative B->W[-7] is injective as a sheaf: projecting a kernel section to the Euler quotient annihilates it by the nonzero O(12) section, so its 1[-18] component vanishes, after which the isomorphic Euler-line component also vanishes. The W[-9] source image is contained in the already-surjective Euler line and adds nothing. Thus the full raw image I is genuinely isomorphic to B:

    I=1[-8]+1[-18] subset W[-7].

Its determinant defect is deg W[-7]-deg I=-14-(-26)=12. Although I is not saturated in W[-7], it is the actual quotient K6/K7. The kernel is exactly the graph of the possible W[-9] map into the isomorphic top line, hence

    K7=W[-9],  rank K7=2,  deg K7=-18.

Because K7 is the actual derivative kernel of K6, its own derivative factors through

    (K6/K7)(-2)=I(-2)=1[-10]+1[-20].

There is no nonzero ordinary bundle map from W[-9] to either summand: the two relevant line degrees are -1 and -11. Its derivative therefore vanishes. K7 remains saturated in the original constant ambient bundle by the geometric rule in Section 1, so it must be constant of degree zero. This contradicts degree -18.

This final step depends on the raw quotient I, not its saturation W[-7]. The proof explicitly retains that distinction, which is essential to the contradiction.

## Audit boundary

The verification uses universal exact sequences, bounded representation identities and support classifications, ordinary and equivariant Ext1 vanishing, the strict-top lemma, and actual constant-connection derivative factorizations. It uses no selected source coefficients, selected points, evaluated derivatives, instance matrices or ranks, or source-model scans. The result is the specified nonzero-J source-branch exclusion only.
