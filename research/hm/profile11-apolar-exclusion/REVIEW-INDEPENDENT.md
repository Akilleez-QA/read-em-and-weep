# Independent whole-proof review

## Verdict and binding

PASS for the stated exclusion: under the actual saturated inclusion, primary four-type theorem, and necessary maximal-profile-(1,1) classification imported in PROOF.md, the quotient A=O(-8)+O(2)+O(16) cannot occur. No mathematical blocker or missing actual-map compatibility step was found.

This is an independent review of all eight sections of the final PROOF.md, all seven retained inputs, the bounded verifier, characters.py, RESULT.json, and REPRODUCE.md. I did not rely on another reviewer’s conclusions or review file. This verdict binds exactly:

- PROOF.md SHA256: 47ce243076419081917682b9ab78990e7cf8066598d8eae1f4a175e80ab91b98.
- PROOF.md byte count: 16005.
- verify.py SHA256: 14534e059dd5052c3052be3a6102aa2e378d25612727ae45ae15762f883eaa2a.
- characters.py SHA256: 5b3b1d415f26ca467670afeb73357cbb0e9c125a6b1acd25155b6d85eef4e4f1.
- RESULT.json SHA256: ece3083613037b66e0a92250e67f9dea17bef255c82ea102695c155635e0b43f.

The conclusion is not a full profile-(1,1) exclusion, a global rank-three exclusion, or an original-theorem repair. Historical indices 119 and 127 are zero-based positions in the pinned complete 159-record file, not a live-frontier count.

## 1. Independent authentication and imported dependencies

I independently fetched every exact immutable public GitHub URL in INPUTS.json. All seven complete returned UTF-8 files agree byte-for-byte with their retained copies. I independently recomputed their byte counts, SHA256 hashes, and Git blob SHA1 identities; all agree with INPUTS.json. These fresh checks are retained in REVIEW-INDEPENDENT-AUTHENTICATION.json, separately from the author’s authentication file.

I read the imported actual-inclusion proof, equivariant-splitting proof, strict-top proof, primary terminal-slope proof, necessary profile-(1,1) theorem, and character source. The written profile theorem supplies geometric necessity; the JSON supplies the original ordered output. Parsing that fixed output confirms that exactly indices 119 and 127 have the specified A, with the two B shapes and defects stated in PROOF.md. I did not rerun the historical enumeration or independently reconstruct all the deeper theorems imported by those original proofs. In particular PR1123 and the necessary-list theorem remain identified theorem inputs, rather than conclusions inferred solely from their computer outputs.

The primary theorem’s four remaining necessary E types are used correctly: only the D type admits any map to O(-8). The onto composite E -> A -> O(-8) forces that type. The term “remaining types” must not be read as asserting that any of them is realized.

## 2. Endpoint capacity, equality, and actual leading derivatives

The successive backward Gauss kernels are saturated in the same constant bundle. The derivative on F_j lands in F_(j-1) modulo F_j, and its kernel is F_(j+1), giving the stated sheaf injections G_j -> G_(j-1)(-2). These need not initially have saturated image. Their ranks are nonincreasing.

Every F_j is negative because it is a subbundle of S. A nonzero saturated negative bundle cannot have identically zero derivative: its Grassmannian map would then be constant in characteristic zero, making the bundle trivial of degree zero. Thus rank decreases until the flag reaches zero, and sum q_j=rank L=10. Together with q_1<=2 this gives precisely the six heights h_1=5,...,10.

I independently recomputed the capacities. For B=(6,-16,-18), the maximum is -50, whereas deg L=-26. This excludes the defect-12 case without applying any equality argument to it. For B=(6,-4,-18), the maximum is -38, attained only at heights (7,3) and (8,2), and deg L=-38. Since every determinant inequality has a nonnegative deficit, equality of the sum forces equality separately.

The unique highest line in each exterior power of B makes the equality argument valid. The Plucker image generically equals the top q-plane; its projection to the complementary quotient vanishes generically and hence everywhere. Equal-degree determinant then has no zeros, so the actual composite map identifies G_j with the top q summands of B(-2j). This is stronger than a splitting-type coincidence and justifies the leading-channel argument.

Composing the actual intermediate derivative maps reproduces those exact top-line maps. Consequently the final line C=O(6-2h) has successive nonzero leading symbols and its first k derivatives span k+1 generic directions in F_(h-k). No derivative is being assigned to an arbitrary Birkhoff complement.

## 3. Representation dimensions and apolar signs

I independently checked the small character identities by exact Q(sqrt(5)) arithmetic using the nine universal class traces, including the distinction V != Sym2 W. The coefficient systems have decompositions Sym8 W=P+D and Sym10 W=A_std+V+D. Since the irreducibles are distinct, every proper quotient of Sym8 has dimension at most 5, and every proper quotient of Sym10 has dimension at most 8. Thus the eight generic directions in height 7 force all nine coefficients, while the nine directions in height 8 force all eleven coefficients. The height-7 lower bound is eight, not nine; the representation argument correctly supplies the final dimension.

The no-character-twist sentence in the final proof is valid for the perfect group SL2(F5). It ensures the rank-one equivariant bundles have precisely the stated standard O(e) linearizations. The fixed determinant identification is used consistently.

With invariant apolarity, the universal formula is

    Ann(l^(n-k) Sym^k W) = l^(k+1) Sym^(n-k-1) W.

Its bundle rank is n-k and its line twist is -(k+1). The three uses are therefore correct:

- n=10, k=8: W O(-9).
- n=8, k=7: O(-8).
- n=10, k=3: Sym6 W O(-4).

In height 8, all E degrees are at least -8, so every ordinary Hom to O(-9) vanishes. The projection to U_11* is zero, producing a prohibited constant U_11 subbundle of S. Only H0(S)=0 is used; no stronger profile-(2,1) bound has been imported.

## 4. Genuine constant splitting in height 7

The projection E -> U_9* factors through the complete degree-eight annihilator J_0. Higher-degree source summands have zero Hom to O(-8), while the sole O(-8) channel is scalar. That scalar must be nonzero, since a zero projection would place U_9 inside S.

After an equivariant Birkhoff splitting E=F+J, the embedded F lies in the constant kernel N. The decisive further argument is valid: the actual coefficient map of J, composed with H -> U_9*, is an isomorphism because J maps isomorphically onto the complete line J_0. Hence its image C_9 is a genuine nine-dimensional constant complement to N. This does not assume that the original Birkhoff splitting was horizontal.

Now H=N direct-sum C_9 and E=F direct-sum J as actual embedded bundles. The quotient splits as (N O/F) direct-sum (C_9 O/J); local freeness of the original quotient makes F saturated in N O. The constant ambient decomposition makes the two second fundamental forms genuinely block diagonal. The nonconstant line J has zero Gauss kernel, so cancellation gives the stated A_F. Rank F=16 and deg F=-46 agree independently.

## 5. Residual endpoint and the forced O(-10) line

Dualizing the constant decomposition gives S=S_F direct-sum S_J, with rank S_F=5 and degree -46. The universal degree-eight annihilator and its backward derivative kernel are Sym7 W O(-1) and Sym6 W O(-2), respectively. Their ranks and degrees are (8,-8) and (7,-14), giving B_J=O(6). Its derivative rank, and that of L_J, are one; negativity rules out rank zero.

Block diagonal differentiation then gives rank L_F=3, B_F=O(-4)+O(-18), and deg L_F=-24. The endpoint bound on beta_L leaves beta_(L_F) of rank at most one; negativity forces rank one. Monotonicity and negativity give ranks 5,3,2,1,0 for the successive actual chain.

Each of the three line quotients has degree at most -4-2j. Their total -24 equals (-6)+(-8)+(-10), so equality holds in every step. The same exact-image argument forces the terminal line M_3=O(-10) and its four independent generic osculating directions in S_F. The proof correctly does not infer completeness of the degree-ten coefficient quotient from only four directions.

## 6. Partial quotient, cubic-degree vanishings, and final contradiction

For any quotient q:Sym10 W -> R given by the actual line, duality gives an injection R* -> (Sym10 W)*. Pulling the actual projection of F through this injection is legitimate even if R is proper or the projected curve is ramified. Since F annihilates q(l^7 Sym3 W), the pulled-back map annihilates the full universal l^7 Sym3 W and factors through l^4 Sym6 W. Generic containment extends globally through the saturated annihilator bundle; no inverse of q or fictitious full curve in R is used.

The degree -2 and degree -3 source blocks have zero Hom to the degree -4 factor: their Hom line twists are -2 and -1. Only V O(-4) remains. Equivariance and the unique V in Sym6 W make this channel scalar, with zero channel to P. A zero scalar would make the nonzero constant R annihilate all of F, contradicting H0(S_F)=0. Thus R* contains l^4 V for every line l.

After the sextic-net span proved below, R* equals the full eleven-dimensional degree-ten space. The rank-13 subbundle D O(-2)+(W'+T)O(-3) is killed by the actual constant projection N O -> R* O and would inject into its constant rank-10 kernel. This is impossible. The final dimension count uses a real constant projection, not a non-horizontal bundle projector.

## 7. Universal sextic-net lemma

The common-zero divisor of the invariant sextic net has degree at most six and is G-invariant. For the faithful projective A5 action, a point stabilizer is cyclic: its tangent character is injective on a finite stabilizer. Its order is at most five, so each orbit has at least twelve points. Therefore the net is basepoint-free.

Its evaluation kernel has rank two and degree -6. Independence of the three sextics gives H0 of that kernel equal to zero, so its Birkhoff summands are O(-a), O(-b) with a,b>=1 and a+b=6. Hence a,b<=5, and twisting by four gives H1=0. The induced multiplication V tensor Sym4 W -> Sym10 W is surjective. Pure fourth powers span Sym4 W in characteristic zero, giving exactly the span of all l^4 V used in Section 6.

This argument is valid for any independent basepoint-free binary sextic net. It is not a special-coefficient rank computation. I independently checked all five possible positive ordered pairs (a,b), including the extreme (1,5) and (5,1), where the smallest twisted degree is -1 and still has vanishing H1.

## 8. Bounded verifier and restrictions

I read verify.py and characters.py in full. The character recurrence is checked against the exact nine-class physical character source. The Hom formula has the correct target-minus-source twist. The verifier checks all seven local immutable identities, the exact two fixed records, the twelve universal height capacities, both equality heights, coefficient quotient dimensions, residual degrees and ranks, the three apolar formulas, and all five sextic syzygy splittings. Its checks use explicit exceptions, not removable assertions.

I independently ran python3 verify.py and python3 -O verify.py. Both complete successfully and both check their generated result against retained RESULT.json. Each reports 194 bounded checks. The minor redirected-stdout trailing-newline issue found in review has been corrected. I reran both final versions and separately compared each redirected stdout with RESULT.json using cmp; both are now byte-identical to the retained result.

I also independently recomputed the relevant characters, capacities, residual rank/degree identities, and all five syzygy bounds outside the author’s verifier. No selected actual HM/source coefficient, point, parameter, jet, matrix, tensor, or instance rank was evaluated. No historical search or enumeration, large computation, or public write was performed.

There is no unresolved mathematical correction required for the stated narrow theorem. The imported theorem hypotheses and all explicitly excluded broader conclusions remain unchanged.
