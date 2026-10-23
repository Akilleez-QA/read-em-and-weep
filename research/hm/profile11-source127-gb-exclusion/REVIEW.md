# Independent review: source127 g-b nested-annihilator exclusion

## Verdict

**PASS, within the exact frozen actual/profile hypotheses stated below.** I found no mathematical correction required in the frozen proof. The claimed contradiction is a whole exclusion of the single original tuple `(0,1,0,0,0,0,1,0)` at source_index127, stable label `G3.11.cce6e3ba4eeb`, with its original zero defect and maximal profile-(1,1). It is not an exclusion of the other tuples at source_index127, the entire stable label, all profiles, or all abstract bundles with the displayed splitting.

The decisive new argument is valid: actual constant restriction maps, applied twice, give a second dual osculating rank at least `11+5+3=19`, whereas this original maximal profile permits at most `13+3+2=18`. No horizontal splitting, additive rank assertion for a nonconstant extension, or selected source-instance evaluation is needed. The compatible twist-one character in the remaining branch does not produce a contradiction and is correctly not used as one.

The review below supplies independent explanations of the actual images, coherent-lattice equality, saturation, and connection compatibility on which the rank inequality depends. It also checks the earlier kernel reductions and endpoint interfaces rather than importing the scalar-tail conclusion of PR885.

## Scope, sources, and restrictions

I read in full the frozen PROOF.md and verify.py and all of ACTUAL.md, STRICT-TOP.md, PR859.md, PR867.md, and PR885.md. I read the relevant exact catalog row and stable-label record and verified the Git blob identities of all seven manifest inputs. I ran the frozen verifier successfully. Separately, I reproduced the fixed kernel, channel, and polar-character calculations using the affine-E8 McKay recurrence, rather than the verifier's conjugacy-class arithmetic.

No selected actual HM/source coefficients, parameters, points, derivative values, matrices, instance ranks, models, scans, or large computation were used. Formal Euler maps and generic rational-section arguments below apply universally. The abandoned open-family work was not read or used. The frozen proof and verifier were not edited. This review does not claim formal proof-assistant certification or independently re-prove the original actual HM presentations upstream of the pinned inputs.

The hypotheses retained from those inputs are:

- Characteristic zero, the binary icosahedral group G, the defining two-space W, standard line-bundle linearizations, and the stated irreducible representations. G has no nontrivial line characters, and a nonempty invariant effective divisor on P1 has degree at least twelve.
- The actual saturated full-span inclusion E in H O, with H=2A+2V+2P+2D, rank E=17, degree E=-54, and the actual Q* presentation and its cohomological consequences.
- The exact g-b splitting E=(P+D)O(-2)+T O(-3)+W O(-9).
- Original zero defect: the raw derivative quotient A_q is saturated, and E^+/E=A_q(2)=O(-6)+O(4)+O(18).
- The original actual dual endpoint B_q=O(-18)+O(-4)+O(6), and the **maximal** profile-(1,1), not merely the first Gauss rank being three.
- Forward transforms and backward kernels are actual saturated transforms for the ambient trivial connection. Equivariant bundle splittings are not assumed horizontal.

### Frozen byte identities

SHA256 values:

| File | SHA256 |
|---|---|
| PROOF.md | 43572f7008c0216bfbb4ba82095ee3a85f90e8184436b7ecbffd94552c7035bc |
| verify.py | f5559f0daa8d4d197913f1be3cdeea829449cf0b09fb47e7b30136e37695b608 |
| audit-inputs/manifest.json | 6277c34072f2f3a2cb284d9c2055475a90c31043608a3dd50be56ff53cda47a8 |
| ACTUAL.md | a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256 |
| STRICT-TOP.md | 53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08 |
| pairs.json | 6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb |
| frontier.json | a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad |
| PR859.md | 0477e228a7253400fc80c58e484157a23cbadce559dcf252758155191f490f5f |
| PR867.md | 10030e0f7acc9ac4bb35efb29356c2a85132b88876983d58b8a359d2c660e07f |
| PR885.md | 3e3a994defbeea2cefff4b0a64a93f70e0059417f8850a79d85069c1d45ab169 |

Immutable Git identities, checked by hashing `blob <length>\0<bytes>`:

| Input | Commit | Git blob |
|---|---|---|
| ACTUAL.md | db51525015bb7c5e825833d550d08dedf6f6ea96 | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 |
| STRICT-TOP.md | db51525015bb7c5e825833d550d08dedf6f6ea96 | d7506dae49b4be43230450c4132bd5db91f137ef |
| pairs.json | db51525015bb7c5e825833d550d08dedf6f6ea96 | fe0afa410d89340d3082dc814277f89fbb582c19 |
| frontier.json | db51525015bb7c5e825833d550d08dedf6f6ea96 | 8b5971092f9ef762584912609fd5e9301c4e271d |
| PR859.md | 6129e92a26572779003f3295227f688b77ed881c | 79ec9cd555997cb9e3b8dc76f3b64fa3f836ad2e |
| PR867.md | b2a12c98bc162062a938b7a7a6a90ab45786e340 | 76a6bd75b77232af222ccb91555499b4a4437311 |
| PR885.md | 53939364de5459822be1a32be08f2b12dbbb4280 | 3d473e81c158e45c923a1177e71701c40ac477c5 |

The manifest supplies their exact repository paths and immutable URLs. The original row has thirteen compatible E tuples; this review concerns only its g-b tuple. The original stable-label record has profile `11`, source_index127, original_defect=0, and the displayed A and B.

## 1. Original actual conventions and the upper rank bound

ACTUAL explicitly distinguishes equivariant splitting from horizontal splitting. Its Sections 4–5 define a maximal consecutive rank-three plateau, with the dual reversed plateau having forward length k. With k=1, Q* has first forward increment three, but its next increment is strictly less than three. Thus

    rank(Q*)=13,
    rank(Q*)^+=16,
    rank(Q*)^(++) <=18.

This bound does not follow from the splitting of E or Q* alone. It uses the maximality of the original profile. The frozen proof states that dependence correctly.

STRICT-TOP applies to the actual E because its splitting degrees are at most -2 and gives H0(E^-(2))=0. It also applies to Q*, whose degrees are at most -1 because it is a subbundle of a constant bundle with H0(Q*)=0. Consequently the map on twist-one sections induced by the actual dual derivative is injective into H0(B_q(1)). This is the strict-top interface used in the degree-38 obstruction; it is not fiberwise injectivity of the whole derivative map.

## 2. High-P surjectivity, exhaustive kernels, and changed internal channels

Set F=P O(-2). Its negative derivative row is zero by degree, and its O(2) row is zero because P is absent from Sym4 W. PR859 explicitly includes the g-b tuple. Its divisor-twelve exclusion therefore proves that the remaining map F->O(16) is onto. In particular, this use of PR859 does not silently saturate an external map with a common divisor.

The exact kernel K has rank three, degree -24, and the two characters stated in the proof. PR867 Section 2 uses only these characters, rank, degree, and central parity, so its complete classification is transferable here. In particular its c-d-f-specific *later* channel exclusions are not transferable, and the frozen proof appropriately recomputes those channels.

For clarity, the thirteen abstract candidates are two three-dimensional blocks A(-8), V(-8); eight two-space/scalar pairs with (j,k)=(3,18),(5,14),(7,10),(9,6) and coefficient W or Wp; and three scalar triples (6,6,12), (6,8,10), (8,8,8). A scalar degree-four block is excluded by the invariant-free H1 budget. Both character constraints leave exactly the five stated kernels I–V.

I independently recomputed this using multiplication by W on the irreducible basis:

    W*1=W, W*W=1+A, W*A=W+S, W*S=A+D,
    W*D=S+T, W*T=D+V+P, W*V=T,
    W*P=Wp+T, W*Wp=P,
    Sym(n+1)=W*Sym(n)-Sym(n-1).

The resulting five candidates and every nonzero Hom into D(-4)+T(-5)+W(-11) agree with the proof. Every listed channel has multiplicity one. No channel into W(-11) remains. In the only degree-eligible case O(-18)->W(-11), the required W in Sym7=Wp+T is absent.

The actual saturated images are also correctly identified, not merely their generic ranks:

- I: the D map is the Euler quotient A(-8)->W(-7) followed by the everywhere-injective l^3 map; a nonzero T map is an everywhere-injective l^3 map from A(-8). Thus J is 0, W(-7), or A(-8).
- II: the W(-7) map into D(-4) is an injection by l^3; the O(-10) map into T(-5) is the complete quintic line. They occupy separate rows and yield precisely the four stated sums.
- III: the D map factors through the Euler quotient O(-8); the T map is the injective l^4 map from W(-9). The scalar O(-6) has no channel.
- IV: the Wp(-3) part has no channel. Each nonzero scalar covariant into D(-4) or T(-5) is saturated, and so is a nonzero pair. One can also see this without enumerating possible divisor degrees: after a common divisor, the irreducible coefficient system still has respectively five or six independent sections, so the possible divisor length is at most ten or eight, below twelve.
- V: only O(-8)->D(-4) and O(-10)->T(-5) occur, in distinct rows; they are saturated complete-power lines.

Here saturation of both internal and external images really implies saturation of the full raw derivative image I_F. Indeed, in the inverse image of the saturated external line, quotienting by I_F identifies the remaining quotient with (E/F)(-2)/J, which is locally free. The further ambient quotient is locally free as well. This justifies the exact sequences in (6) *before* using first-polar generation.

The quadratic polar map P W O(-1)->F^+ is onto that raw, now saturated, first span. Thus its only splitting degrees are 0 and -1. Independent Euler-character calculations give:

| J | Constant coefficient of M | Linear coefficient of M |
|---|---|---|
| W(-7) | V+P | 0 |
| A(-8) | 0 | Wp+T |
| W(-7)+O(-10) | 0 | Wp+T |
| O(-18) | 0 | T |
| W(-9) | A | Wp+T-S |
| O(-8)+O(-10) | A | Wp+T-S |

The last two are impossible genuine representations. The zero and isolated scalar-image alternatives give positive degree in a constant bundle. This verifies the complete reduction to (7), with no dropped tail channel.

## 3. The nonconstant first spans and the negative endpoint

### Rank-eight first span

For M=P W O(-1), the quadratic coefficient map has source P Sym2=V+P+D. Since a negative rank-eight bundle spans at least nine constants, the only possible full coefficient spaces are P+D and V+P+D.

For the nine-space, the linear Euler calculation gives C/M=O(8) and M^-=(V+P)O(-2). N=E intersect M is saturated in M and has rank seven. If it were contained in M^-, equality would force the absent V(-2) coefficient into E. Otherwise differentiating N supplies C/M; since N^+ already contains F^+=M, saturation puts all C in E^+. The lower rows vanish first on M/F=P O and then on C/M=O(8). Consequently E intersect C has rank eight and degree -18. Its ordinary degrees are at most -2, so its degree-minus-two coefficient has dimension six or seven. No such subrepresentation exists in the multiplicity-free P+D top block. This exclusion is sound.

For the twelve-space, the actual quadratic Euler model yields

    M/F=P O,
    C/M=P O(2),
    beta_M: M/F -> (C/M)(-2) an isomorphism.

N/F is saturated in M/F because M/N is the actual saturated high line O(18). Therefore its image under this isomorphism is saturated, and Y=N^+ has precisely the displayed quotients A(-4) or W(-3)+O(-6). In both cases C/Y=O(20). The proof that C is not in E^+ is valid: its lower rows would vanish on P O(2), leaving a rank-eleven degree-minus-eighteen subbundle of E, inconsistent with all degrees at most -2. As Y and E^+ intersect C are saturated, this proves E^+ intersect C=Y.

The case-I lower rows vanish by the stated Hom spaces. In case II, the positive row vanishes as stated, but the negative scalar row cannot be dismissed by its splitting type alone. The proof correctly uses the actual induced derivative instead.

Here is the connection diagram in words. Let q_- be the projection E^+/E->O(-6). It vanishes on M, so its restriction to Y factors through Y/M. The isomorphism

    N/F -> (Y/M)(-2)

is induced by the actual derivative modulo M. Composing it with q_-(-2) equals the negative component of beta_E on N/F. The scalar O(-8) in N/F maps into E/F only through T(-3): its D(-2) component would require D in Sym6, which is absent, and the W(-9) target is too low. The negative component of beta_E on T(-3) is zero by degree. Lifts differing by F cause no ambiguity because beta_E on F has only the high row. Thus the induced negative O(-6) row of Y/M is zero. This is an actual connection argument, not a horizontal-splitting assertion and not a transfer of the surviving scalar-tail row of PR885.

Both twelve-space cases therefore give rank-ten, degree-minus-thirty-eight E intersect C with the required high-line extension.

### Rank-six first span

For M=T(-1), its linear coefficient map T W=V+P+D has P in its kernel because beta_M kills F. Its constant span has dimension at least seven, so it is exactly V+D, of dimension eight. The complete cubic Euler model tensored by Wp supplies the stated actual quotients and derivative isomorphism. It gives Y/M=O(-14) and C/Y=O(20).

If C were in E^+, the lower rows would vanish on Wp O(3). The resulting rank-three degree-minus-ten bundle (E intersect C)/F cannot have degree-minus-two coefficients, since no coefficient of dimension at most three maps to D. It cannot have degree-minus-three coefficients either: the only eligible two-dimensional odd coefficients are W and Wp, neither of which maps to T at equal degree or to D(-2), since D W=S+T. The new W(-9) target is again too low. All degrees would therefore be at most -4, a contradiction. Thus E^+ intersect C=Y. The lower rows of Y require scalar invariants in degrees eighteen and eight, both absent, giving the rank-six degree-minus-thirty-eight intersection.

### Degree-38 obstruction checked independently

For either c=12 or c=8, let X=E intersect C have rank c-2 and degree -38 and let U0=C/X be the stated extension of O(20) by O(18). The projected E/X has rank 19-c, degree -16, and full span in H/C. Its saturation defect delta is the same as that of U0 in Q, by their common cokernel. Nonpositive degrees and full span give

    30-c <= h0((E/X)^*_sat)=35-c-delta.

Thus delta<=5. Invariance forces delta=0. This is the needed saturation step before dualizing.

The two equivariant extension types of U0 are O(18)+O(20) and W O(19). In either case R=(Q/U0)* has rank eleven, degree -16, H1(R)=D, and chi_G(R(3))=-W+Wp+S+4T, using the pinned Q* presentation. Its degrees are at most -1. The entire H1 budget permits only D(-2) or O(-6) as a more-negative block. The first would force a genuine linear coefficient times A to contain a negative W multiplicity. In the second case, the exact equation for the linear coefficient is L A=Wp+S+4T, uniquely giving L=2Wp+T. Thus H0(R(1))=2Wp+T injects into H0(Q*(1)), while strict-top injects the latter into H0(B_q(1))=Wp+T. This is impossible. The obstruction uses the shared actual Q presentation and B endpoint, not the scalar-tail splitting of PR885.

This completes, rather than assumes, the exclusion of every nonconstant M left in (7).

## 4. The constant seven-space produces the actual constant ten-space

For M=(V+P)O, its actual image in Q is the high line L=O(18). Thus N=E intersect M has N/F=W(-5), and the quotient inclusion into E/F can have only its D(-2) component. The T component would require W in T Sym2=Wp+S+2T; the W(-9) component vanishes by degree. The nonzero D map is l^3 with quotient A O.

Because M/N=L is saturated in Q, projecting E along the constant M is a saturated inclusion. Its quotient is genuinely

    E/N=A O+T(-3)+W(-9),

not merely a character identity. The A O subbundle in a trivial bundle is constant because its global sections are constant. Its inverse image in H defines C0=A+V+P. The inverse image in E is exactly the entire top block F0=(P+D)(-2), since A O is the quotient of D(-2) by the displayed W(-5) and the two lower direct summands survive untouched. Consequently

    E intersect C0=F0,
    C0/F0=L=O(18) saturated in Q.

This proves (11) through actual projections without identifying any abstract summand of E with a constant horizontal summand.

Projecting by C0 gives a saturated full-span Z=T(-3)+W(-9) in Hbar=A+V+P+2D. Its quotient is Qbar=Q/L. Since C0 lies in E^+ and removes exactly L, the raw derivative image of Z is the quotient A_q/O(16)=O(2)+O(-8), still saturated. Constancy of the projection is essential here and is available.

## 5. The complete T-chain identifies its actual constant span

Write R=T(-3). If its positive external row were zero, both external rows would vanish, and its only possible internal derivative toward W(-11) is zero by degree. Then R would be a negative horizontal subbundle, impossible. The nonzero row is the complete quintic map, so its exact derivative kernel is D(-4); the latter has no internal derivative toward W(-11).

At each subsequent step, the current kernel differentiates into the preceding bundle modulo itself. A zero map would make it horizontal. The nonzero equivariant map is the complete symmetric-power evaluation, hence is onto its line target with the standard next kernel. More explicitly, writing R_j=Sym^j W O(j-8), the quotient R_j/R_(j-1) is O(2j-8), and the induced derivative of R_(j-1) has degree-(j-1) complete evaluation into O(2j-10). Its kernel is R_(j-2). These are saturated exact Euler sequences.

This establishes the whole actual chain

    O(-8), W(-7), A(-6), S(-5), D(-4), T(-3),

with each term the saturated first span of its predecessor. The line's coefficient map is a quotient of Sym8=P+D. Its span contains a rank-six term, but every proper subrepresentation of P+D has dimension at most five. Thus its coefficient map is a constant isomorphism onto C=Sym8 W, and its actual later terms are U_j^8 under that isomorphism. In particular R=U5^8 and C/R=A O(6). This is stronger than merely matching the splitting of R or C/R.

## 6. Projected W(-9): rank, coherent lattice, and saturation in the correct order

Let pi be the constant projection by C, and D0=Hbar/C=A+V+D.

1. **Generic rank is two.** Rank zero contradicts full span. If the coherent image of W(-9) had rank one, it would be a line O(e), with -9<=e<=0, and the map onto it would require W in Sym(e+9). The only possibility is e=-8, giving the Euler kernel O(-10). That kernel maps into C, but its induced map to C/R=A O(6) is zero because A is absent from Sym16. Hence it would lie in R, contradicting the direct-sum injection R+W(-9)=Z. No saturation of the rank-one image was assumed in this argument.

2. **Keep the original coherent lattice.** The rank-two sheaf injection has coherent image N isomorphic to the original W(-9). This alone does not say N is saturated, and the proof does not yet claim that. The negative external row is necessarily the nonzero complete Euler map W(-9)->O(-8), with kernel K0=O(-10). Its projection K is a nonzero line of degree -10 in D0 O. Any zero divisor would have length at most ten and be invariant, so it has none. K is saturated. It is nonconstant: a constant projective image would give an invariant one-dimensional coefficient subspace of D0, which has no trivial constituent and no other one-dimensional G constituent.

3. **Derivative containment is an equality-of-lattices argument, not a generic assertion.** The external negative derivative of K0 is zero. The entire positive quotient is supplied inside C by R^+/R. More precisely, the inverse image of the positive O(4) inside Z^+ is Z+R^+. Therefore derivatives of K0 lie in Z+C as sheaves. Applying the constant projection gives derivatives of K in the coherent image N, not just in its saturation. Since K0 is the Euler kernel, N/K=O(-8). The resulting second fundamental map

       K=O(-10) -> (N/K)(-2)=O(-10)

   is nonzero; otherwise K is horizontal. It is therefore an isomorphism. Locally K together with its derivatives contains K and surjects everywhere onto N/K, so its raw first-polar sheaf equals N. This justifies the decisive coherent-lattice equality.

4. **Only now identify and saturate N.** Full span of Z implies that N spans all D0. A line and its raw first polar have the same constant coefficient span, so K also spans D0. Its degree-ten coefficient map Sym10 W->D0 is onto; both sides have dimension eleven. Transporting by this constant isomorphism identifies K with the complete degree-ten line U0^10 and N with its first polar U1^10. The standard Euler quotient then proves N is saturated. No presumption of saturation or equality from generic rank has entered this deduction.

The quotient sequence is now an exact sequence of bundles:

    0 -> C/R -> Qbar -> D0/N ->0.

Indeed Z intersect C=R because pi on W(-9) is injective, and N is now known saturated. Thus C/R is saturated in Qbar. This is exactly the needed order of reasoning before dualizing.

## 7. Actual dual images and ambient connections

Let rho:Hbar* O->C* O be the constant restriction map. Its constant kernel is D0* O. Since all quotients just established are locally free, dualizing gives

    0 -> R1=(D0/N)* -> R0=Qbar* -> (C/R)* ->0.

These maps are the actual restriction maps induced by the inclusions, not maps chosen after splitting the sequence. Consequently:

- R1 is the actual annihilator of N in D0*, hence U8^10 under the dual of the constant coefficient identification already proved.
- rho(R0) is the actual annihilator of R in C*, hence U2^8.
- R1 lies in the fixed constant kernel of rho.

For a universal flag U_k^n=l^(n-k)Sym^k W, the actual second fundamental maps are obtained by differentiating the formal power. In characteristic zero the coefficient n-k is nonzero, and each forward transform is U_(k+1)^n. The invariant symmetric-power duality identifies its annihilator with U_(n-k-1)^n. These statements concern the actual embeddings transported by constant isomorphisms, not merely their splitting types.

One need not, and should not, claim that R0 or the extension has a flat splitting. The sufficient connection compatibility is the elementary identity

    rho(Ds)=D(rho(s))

for ambient rational sections, because rho is constant. Rational sections of rho(R0) have rational lifts in R0. Therefore projection of the j-th generic osculating span of R0 is *exactly* the j-th osculating span of its image U2^8. Independently, the j-th span of R1 remains in the constant kernel. Rank-nullity then gives

    rank Osc_2(R0)
      >= rank Osc_2(U8^10) + rank Osc_2(U2^8)
      = 11+5=16.

Possible extension couplings affect lifts, but cannot identify a direction in a fixed constant kernel with a nonzero direction measured in its quotient. This is the correct replacement for invalid rank additivity through a moving extension.

For the outer restriction sigma:H* O->C0* O, saturation of L in Q gives the exact sequence

    0 -> R0=Qbar* -> Q* -> L* ->0.

Again these are actual maps: R0 lies in the fixed constant annihilator of C0, and sigma(Q*) is the actual line L* in C0*. The exact sequence 0->F0->C0 O->O(18)->0 and H0(F0)=0 show that the ten coefficient sections are linearly independent, so this line has full coefficient span C0*.

Its generic second osculating dimension is three. An independent proof is to normalize one nonzero rational coordinate to 1. If the value, first derivative, and second derivative had rank at most two, then the second derivative vector would be a rational scalar times the first derivative vector. Choosing a nonconstant coordinate u, every other coordinate v would satisfy (v'/u')'=0 and hence v=a u+b with a,b constant. All coordinates would then span at most two dimensions over C, contrary to their ten-dimensional coefficient span. This argument selects no actual point, coefficient value, or source-instance derivative.

Applying the same constant-kernel rank-nullity inequality gives

    rank Osc_2(Q*) >=16+3=19.

Generic osculating spans are the generic fibers of iterated saturated forward transforms; saturation does not change these ranks. Therefore this contradicts the original maximal-profile bound 18. Both independent second directions in the residual extension, and the additional outer line direction, are accounted for by fixed constant projections.

## 8. Twist-one test and obstruction boundary

The ordinary equivariant bundle extensions split because the relevant H1 groups vanish; averaging is legitimate in characteristic zero. Thus the final hypothetical branch has the bundle type

    Q*=(P+D)O(-2)+A O(-6)+O(-18).

This is not claimed to be a horizontal decomposition. Independent fixed-character computation gives exactly

    H1(Q*)=A+2V+3P+4D,
    chi_G(Q*(1))=-W-2S-3T.

These match the pinned actual character data. In particular the early twist-one test does not eliminate this branch. The actual nested constant-annihilator flag and the maximal plateau, not those characters, provide the exclusion. A block-diagonal abstract construction matching the splitting but having second dual gain three would not realize the specified source profile. No conclusion about the separate c-d-f abstract family follows here.

## 9. Verification result and corrections

The frozen verify.py completed successfully with its two PASS/scope lines. The independent affine-E8 recurrence reproduced all thirteen kernel candidates and the five survivors, all nonzero changed-tail Hom channels, all surviving and impossible polar characters, Sym16=V+P+2D, and the final compatible Q* characters. The exact manifest blob identities and the proof/verifier SHA256 identities were checked.

**Required corrections: none.** The expanded arguments in Sections 3, 6, and 7 of this review explain the potentially easy-to-misread interfaces: the endpoint-specific induced negative derivative, equality of the projected first-polar coherent lattice before saturation, and the actual dual restriction images with their constant ambient connections. They validate the frozen text rather than repair a false statement. Any future abbreviated presentation should preserve these points and the explicit dependence on maximal profile-(1,1).

This verdict is about the exact frozen proof and inputs identified above. It does not establish a new aggregate frontier count, extend the result to neighboring source tuples, or replace any required publication/repository review process.
