# Independent review: PASS after one corrected support omission

Reviewed proof: `PROOF.md`.

Final reviewed SHA256:

`f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc`

Review date: 2026-10-23 UTC.

## Verdict and scope

PASS for the five stated conclusions, restricted to

- `G3.11.863639aa192e`, source index 69;
- `G3.11.73682b4c817f`, source index 72.

The proof excludes the ef and be strata for both labels, ce for the balanced label, and the generic-rank-two top-image branch of bc for both labels. It forces the stated actual constant and standard linear subsystems in cf and split-ce, and forces the nonzero saturated internal image O(-10) in the generic-rank-two bf branch. It does not exclude either full label, all of bf or bc, or the bb source. I found no remaining mathematical blocker in the final reviewed version.

The independent review used the copied public source documents, their two designated catalog records, bounded abstract representation identities, and exact-sequence arguments. It did not evaluate selected actual HM/source coefficients, parameters, points, derivatives, matrices, ranks, selected models, or scans. No external write was made.

## Exact public input pins

The following five files are in `Akilleez-QA/read-em-and-weep` at commit
`db51525015bb7c5e825833d550d08dedf6f6ea96`, under
`research/hm/order-four-quadratic-load/`:

1. `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`
   Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
2. `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`
   Git blob `d7506dae49b4be43230450c4132bd5db91f137ef`.
3. `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`
   Git blob `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
4. `one-one-endpoint-necessary-pairs.json`
   Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`.
5. `rank-three-quotient-frontier-144.json`
   Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`.

Public directory:
https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The other three dependencies are:

- PR796, commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, path `research/hm/profile12-quadratic-block-exclusion/PROOF.md`, Git blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md
- PR799, commit `2172e4a7abbbe232f9f448bea6fa01dee7927460`, path `research/hm/profile11-quadratic-polar-obstruction/PROOF.md`, Git blob `a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1`.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md
- PR802, commit `e484640a6565c278321bf6557860262c1ac1b7df`, path `research/hm/profile11-o16-constant-span-exclusion/PROOF.md`, Git blob `98a1bd6123e148476da0b997d879aecbf885ec97`.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

I independently fetched the commit-pinned file metadata for all eight files and verified the returned Git blob IDs. The copies initially had one extra terminal LF; this was identified during review and removed. The final local copies have exactly the Git blob hashes above. That byte-level correction changed no mathematical content.

## Correction found and resolved

The initial proof hash was
`12348d96208c3d1c6583889831ddcbcd41bcf1250b2cc24c907e84f59bf7a847`.

Its claimed complete support list for the H1 budget P+D omitted

`V O(-6)`.

Indeed V tensor Sym^2 W = P+D, and (6-3) dim V = 9 fits that budget exactly. The initial assertion that only the trivial coefficient could fit at degree -6 was therefore false.

The final version correctly includes this block, its twist-three Euler contribution -T, and its rejection in bc: the required degree-minus-three coefficient would be T-S, which is not genuine. The other degree-six coefficient A is rejected because A tensor A = 1+A+D. Thus the final kernel list (4) and every stated conclusion remain unchanged. This was a correction to completeness of the intermediate support proof, not a new source-stratum exclusion.

## Verification details

### 1. Source decoding and exact catalog scope

The frontier records identify precisely the two labels, their zero original defects, and source indices 69 and 72. The catalog records at those zero-based indices each contain exactly the ten tuples a=d=g=0, h=1, b+c+e+f=2.

Substitution in the original source formula gives

E = (cV+(e+1)P+fD) O(-2) + bT O(-3) + cV O(-4) + eWp O(-5) + f O(-8) + O(-10).

The additional P in e+1 is required. The baseline P O(-2)+O(-10) has rank 5 and degree -18. Each unit of b,c,e,f contributes rank 6 and degree -18. Since their sum is two, rank E=17 and degree E=-54. The seven displayed source rows follow exactly after the three already-known multiplicity exclusions. No missing source is silently dropped.

### 2. Generic rank versus saturated image

The strict-top result gives an injection of the entire top coefficient representation R into H0(U(2)); it does not by itself assert fiberwise rank two. The proof correctly supplies that extra argument only where needed.

For the split target, the two P source copies fill the two P multiplicities in Sym^6 W+Sym^8 W. A constant invertible change in this multiplicity space separates the two rows. For cf, V and D separate the rows directly. Every nonzero such row is basepoint-free: its invariant common divisor has degree at most eight, below the minimum invariant orbit degree twelve.

For the balanced target, an invariant saturated line has trivial coefficient character and even degree t<=4. Its twist-two section space therefore has dimension at most seven. This rules out generic rank one for the five stated top spaces of dimensions 13,12,11,9,8.

For any generic-rank-two image S0, S0(2) is globally generated and hence H1 vanishes. Since deg U=10, its section dimension is exactly 16-d, where d is the torsion length of U/S0. A nonzero invariant torsion divisor has d>=12. The independent r-dimensional section space then contradicts r>4. This proves actual surjectivity and removes every divisor correction in the applications. The argument is correctly not applied to bb.

### 3. Exhaustive small kernels and internal channels

The identities in (3) follow from the surjective exact sequence and H0(K0(2))=0. For a block Z O(-j), j>=4, its H1 contribution is Z Sym^(j-4) W, and the dimension bound is (j-3) dim Z. Central parity and this bound leave exactly the supports in the corrected Section 3. In particular the only additional degree-six candidate is the corrected V O(-6).

Matching the twist-three Euler character eliminates the D O(-4) alternative for ce, the Wp O(-7) alternative for be, and both the V O(-6) and O(-12) alternatives for bc. The surviving choices are exactly (4), including all three bf possibilities. Their ranks and degrees agree with rank K0=r-2 and deg K0=-2r-10.

For ef and cf every internal channel vanishes by degree. For ce, be, and bc, the possible O(-8) channels vanish by the stated absent constituents of Sym^2 W, W, and Sym^3 W. The possible Wp O(-5) to T O(-5) channel in bc also vanishes by inequivalent irreducibles. For bf, the first two kernels have zero internal map; in the third, only O(-10) contributes. Its quintic channel and its scalar channel are each saturated when nonzero, and their combined graph remains saturated.

The derivative-image lemma uses the actual nested subbundles F subset E subset H O. With zero internal image and saturated external image U it gives precisely F^+/F=U(2), not merely a generic identification. No interior-profile assertion H0(E^+)=0 is imported from PR796.

### 4. Actual constant projection and the rank-two polar lemma

First-polars generate the raw quadratic first span. Raw-image saturation is established before this is used to identify it with F^+. Consequently every degree of F^+ is either zero or minus one. Its degree-zero space C=H0(F^+) consists of actual constant ambient vectors.

After quotienting by this actual C, M=J O(-1) is saturated in the constant quotient. The projected F lies in the derivative kernel of M. Its rank is at least s-1: rank(F intersect C)=c would force C into saturated F and contradict H0(F)=0. Thus the derivative rank of M is at most one, and it is nonzero because a nonzero saturated negative bundle cannot be horizontal.

For an embedded pure-linear bundle, values and first derivatives span exactly its full constant coefficient space at every point. It follows that M^+ is constant of rank s+1, with quotient line O(s). Since G is perfect the coefficient character is trivial. Cohomology identifies the complete evaluation sequence, giving C1=Sym^s W and J=Sym^(s-1) W. The derivative kernel is the standard Sym^(s-2) W O(-2), equivalently the forms with a double zero at the tautological line.

The map from R O(-2) to that pure quadratic kernel is constant in coefficient spaces. Its full generic rank therefore makes it onto everywhere. Its kernel is the actual intersection R0 O(-2)=F intersect C, of rank c-1. This intersection is saturated in C because its quotient injects into H O/F. Thus the quotient is O(2c-2), and the resulting sequence

0 -> O(2c-2) -> U(2) -> O(s-2) -> 0

is exact with locally free quotient. This verifies the core new polar obstruction, including the saturation steps needed to avoid replacing actual connection data by a formal splitting.

### 5. Applications and the final bc projection

The characters C and J in (12)-(13) follow from the two twists of the actual exact sequence. The ef injection is ruled out equivariantly for both targets. The be injection is ruled out by degree. Balanced-ce is ruled out by degree. In split-ce and cf, the stated surviving inclusions are the unique equivariant channels, and the standard projected subsystems and intersection representations follow from the polar lemma. The bf zero-internal possibility is ruled out by degree, leaving only its nonzero saturated O(-10) channel.

In the generic-rank-two bc branch, F^+ is the actual constant space (P+D) O. The zero internal image gives F^+ intersect E=F and identifies (E+F^+)/E with the saturated U(2). Hence E+F^+ is saturated in H O, and its constant projection is the actual saturated Z=E/F. Projecting the already-saturated raw derivative of E gives the saturated raw derivative of Z. Its forward quotient is O(-8), equivalently its exact Gauss quotient is O(-10), with no hidden torsion correction.

The T O(-3) top block maps trivially to that Gauss quotient, so its derivative lands in Z. Its internal derivative to V O(-6)+O(-12) is zero by ordinary degrees. It is therefore a negative-degree saturated horizontal subbundle of a constant bundle, impossible in characteristic zero. This proves exactly the claimed rank-two-branch exclusion, without excluding a possible rank-one top image.

## Remaining limits

This review does not establish realization of the forced subsystems, remove either full frontier label, or resolve bb, the nonzero bf internal channel, the rank-one bc branch, or the subsequent analysis of cf and split-ce. The proof explicitly preserves those limits. No additional correction or missing dependency was found for its stated conclusions.
