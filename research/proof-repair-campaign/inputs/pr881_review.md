# Independent review of the complete source113 bf exclusion

## Verdict and exact reviewed object

**PASS. No outstanding mathematical blocker or required correction remains.** The proof excludes the entire original source edge

- stable label G3.11.ad509d55173f;
- source_index 113;
- tuple (0,1,0,0,0,1,0,1);
- E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10);
- A_q=O(-10)+O(2)+O(16), B_q=O(-18)+O(-4)+O(8);
- original determinant defect zero.

The reviewed file is `PROOF.md`, exact SHA256:

`f900fa54aa5ad18adc94bd7552b94891d77ccf1c5797af05414dbd8b851b4f63`.

Review date: 2026-10-23 UTC. This review applies to that final version, not the initial hash 12ae59cd698f740b7fa40c524c9a0b58c6f727d8a8f4648ba05c38814c3b18ba. The final version corrects both occurrences of the degree-ten symmetric-power decomposition to Sym10 W=A+V+D. The invariant-vanishing conclusions used there remain valid.

The scope is this entire source edge only. This review does not independently certify other sources, full-label coverage, a frontier decrement, or the original global goal. No publication was performed. The frozen proof was not edited during this review.

The proof's geometric reasoning was audited independently, including the actual connection, image saturation, coefficient maps and intersections. The supplied verifier passed. A second small audit, `review_independent.py`, uses the fixed binary-icosahedral McKay recurrence rather than the supplied character-table implementation; it also passed. Neither check evaluates selected actual coefficients, parameters, points, derivative values, matrices, instance ranks, models, scans or large computations. The universal geometric arguments, not either arithmetic script, establish the exclusion.

## 1. Original inputs and decoder

The four audit-input Git blob hashes match the original hashes stated in the proof. The original catalog entry has the exact endpoints, zero defect, and ten compatible source tuples including bf. The original frontier maps the asserted stable label to source_index 113.

The original decoder gives

R_2=(c+g+h-1)V+(d+e+g+h)P+(f+g)D=P+D,

and the tuple adds precisely T(-3), O(-8), and O(-10). Thus rank E=17 and degree E=-54 are correct. The pinned original presentation, not merely the splitting character, provides the constant ambient dimension 30, full span of E, negativity and the strict-top hypothesis. Zero defect identifies the actual saturated first quotient with A_q(2).

The local universal dependencies inspected have these SHA256 hashes:

- high-P kernel classification: 10030e0f7acc9ac4bb35efb29356c2a85132b88876983d58b8a359d2c660e07f;
- divisor-twelve argument: 0477e228a7253400fc80c58e484157a23cbadce559dcf252758155191f490f5f;
- related bb proof: 33e9195434e1c57b8d33fcec2bd6e80f76daf4cf4cd77092c93dfff4f1b42e3e.

The bf proof does not transfer an exclusion merely from sharing O(16) with another source. It rechecks the changed D row, both actual endpoint rows, the exceptional constant span, and every needed saturation. The degree-38 dual argument is restated and checked directly here.

## 2. Divisor branch and complete kernel classification

For F=P(-2), the lower external channels vanish: the degree to O(-10) is negative, and P is absent from Sym4 W for the O(2) channel. Strict-top injects P into Sym18 W. A common divisor therefore has degree at most 15. Its invariance, central parity, minimum orbit degree 12, and absence of an invariant in Sym14 W leave only degree 12.

After removing that entire divisor, the residual degree-six system is onto and has kernel V(-4). The cohomology budget is V, and rank, degree and parity force this exact kernel. For bf the actual internal target is D(-4)+T(-5)+O(-10)+O(-12). The equal-degree D channel vanishes by irreducibility; all other channels vanish by degree.

The full raw derivative image is therefore the unsaturated external image O(4), not O(16). Its raw first span has rank 5, degree -2 and quotient O(6) by F. A saturation defect has invariant length at most 2, so must be zero. The polar characters consequently give V O+Wp(-1).

The V summand is the actual constant subspace H0(M). Projection by it commutes with the connection. The projected P(-2) -> Wp(-1) is nonzero by rank and is the unique tensor-Wp Euler surjection. Local lifting makes the entire projected Wp(-1) horizontal, contradicting its negative degree. This excludes the divisor branch without silently saturating its external image.

For the basepoint-free high map, the five kernels in (3) are exhaustive. Rank three permits only a three-dimensional even irreducible, an odd two-space plus a scalar, or three scalar lines. H0(K(2))=0, central parity and the invariant-free H1 budget give exactly the thirteen stated candidates. Their two characters retain precisely I-V. The independent McKay audit reproduces the retained kernel characters; the supplied verifier checks all thirteen candidates.

## 3. Every internal channel and its actual saturated image

The full internal Hom support in section 3 is correct, including all scalar target rows. Both arithmetic audits reproduce it. Each listed individual channel has multiplicity one.

The rank-dropping D maps require more than that multiplicity statement. Their universal formulas are valid:

- A(-8) -> D(-4) is the first transvectant with the tautological fourth power. It factors through the Euler surjection A(-8) -> W(-7), with kernel O(-10), followed by multiplication by the tautological third power. Its image is the saturated W(-7).
- W(-9) -> D(-4) factors through the Euler surjection W(-9) -> O(-8), followed by the tautological fourth-power inclusion. Its image is the saturated O(-8).

The corresponding T multiplication maps in I and III are everywhere injective. Thus a nonzero T row gives the full A(-8) or W(-9) image, even when a D row is also present. If that T row is zero, the stated smaller D image is exact.

For II and V the D image and the possible O(-10) image lie in separate target summands. The latter is saturated whenever its tautological T component or equal-degree scalar component is nonzero. Their direct sum is therefore saturated as well.

In IV, a nonzero degree-14 D covariant or degree-13 T covariant has no common divisor. A degree-12 divisor would leave D in Sym2 W or T in Sym1 W, respectively. Both are impossible, and no other eligible invariant divisor occurs in those degrees. A combination of the two rows retains saturation because each nonzero component is already fiberwise injective. Therefore the complete image list (4), including the zero alternatives, is correct.

The actual-image lemma then applies, because the external O(16) and every possible internal image are saturated. All first spans have only degrees 0 and -1 by first-polar generation. Zero J, a sole O(-8), and a sole O(-10) give positive degree. J=W(-9) and J=O(-8)+O(-10) give the impossible linear coefficient Wp+T-S. The four surviving forms in (5) have exactly the asserted polar characters, ranks and degrees.

## 4. Constant seven-space branch

For M=(V+P) O, the image in Q is the saturated L=O(18). Consequently N=E intersect M has N/F=W(-5), rank 6 and degree -18. Its inclusion into E/F has only the D(-2) channel. The claimed absence of its T(-3) channel follows from T A=Wp+S+2T; scalar channels vanish by degree.

The unique D map is the universal multiplication inclusion W(-5) -> D(-2). Its complete quartic sequence has quotient A O. Hence the quotient E/N is exactly A O+T(-3)+O(-8)+O(-10).

Projection by the actual constant seven-space is saturated: its image L is saturated in Q, so the projected ambient quotient modulo E/N remains locally free. The derivative image is the original image modulo L, namely the saturated O(-10)+O(2). The A O in E/N is itself an actual constant subspace of that projected ambient space, since its degree-zero global sections embed as constant sections. Projecting by this A therefore also preserves the connection and leaves the same external derivative image.

For the resulting Z, the canonical O(-8) has no external component: one degree is negative and the other requires an invariant in Sym10 W=A+V+D. Its internal components to T(-5) and O(-12) vanish as well, because T is absent from Sym3 W and the other degree is negative. This is an actual saturated negative horizontal line, a contradiction. No arbitrary abstract splitting is treated as horizontal. The exact original O(-10) endpoint is genuinely used.

## 5. Both rank-eight linear branches

The polar isomorphism identifies M with P W(-1). Its actual constant coefficient span is a quotient of the multiplicity-free P Sym2 W=V+P+D. A saturated negative rank-eight subbundle needs span dimension at least 9. Hence only C=P+D or C=V+P+D can occur. The two actual intersections N/F are exactly A(-6) and W(-5)+O(-8), both rank three and degree -18.

### Dimension nine

The complete-evaluation assertion can be justified without any choice of coefficients: C/M is a line of degree 8, while H0(M)=H1(M)=0. Thus C -> H0(C/M) is an isomorphism, so C/M=O(8) has its complete evaluation kernel M. This identifies the actual derivative kernel as Sym6 W(-2)=(V+P)(-2), not merely an abstract bundle with that character.

N is saturated in M, as the intersection with the saturated E. If N lies in M^-, equal rank and saturation force equality. The resulting V(-2) has no map into any row of E. Otherwise derivatives of N have nonzero image in the line C/M. Since N lies in E and M lies in E^+, saturation of E^+ forces the entire C O into E^+.

The lower-row map then factors through O(8) and vanishes by degree, while M already maps onto L. Thus X=E intersect C has rank 8 and degree -18. Its degrees are at most -2 with total excess 2. The only possible ordinary patterns have a degree-minus-two coefficient of dimension 6 or 7. This coefficient must inject into the actual top P+D of E, whose possible subrepresentation dimensions are only 0,4,5,9. The contradiction is valid even though the ordinary slope bound alone would not suffice in bf.

### Dimension twelve

Here the actual coefficient map P Sym2 W -> C is an isomorphism. Constant identification of the coefficient space therefore gives the complete quadratic sequences and the actual derivative isomorphism in section 5b. In particular M/F=P O and C/M=P O(2).

N/F is the saturated kernel of the onto map M/F -> L. Its image under that derivative isomorphism gives the saturated Y/M=A(-4) or W(-3)+O(-6). The raw first span of N contains M because the raw first span of F is already M. Taking the inverse image of this saturated derivative image yields exactly Y=N^+, of rank 11 and degree -20, with C/Y=O(20).

If C lay in E^+, the lower rows would vanish after factoring through P O(2). The resulting rank-eleven, degree-minus-18 kernel in E contradicts the correct bf bound -24. Thus E^+ intersect C=Y: this intersection is saturated, contains the corank-one saturated Y, and cannot have full rank.

All lower-row maps of Y vanish as claimed. The needed nonnegative degrees are 8,7,10, with A absent from Sym8 W, W absent from Sym7 W, and no invariant in Sym10 W. The other degrees are negative. Therefore X=E intersect C has rank 10, degree -38, and the exact quotient sequence is 0 -> O(18) -> C/X -> O(20) -> 0.

## 6. Rank-six linear branch

For M=T(-1), the linear-bundle formula gives M^-=K1(-2), where K1 is the kernel of the actual coefficient map T W -> C. Since beta_M kills F, P is contained in K1. The multiplicity-free T W=V+P+D and the required span dimension at least 7 force C=V+D and K1=P.

The cubic identification is an identification of actual coefficient maps. The multiplication map Wp Sym2 W tensor W -> Wp Sym3 W is onto and has precisely kernel Wp W=P. The actual coefficient map has the same kernel, so these maps differ only by a constant equivariant isomorphism of their target. Such an isomorphism preserves the constant connection. This justifies every complete cubic sequence in (11), including the actual derivative isomorphism and M/F=Wp O(1).

N/F=O(-16) is saturated in M/F as the high-line kernel. Its derivative gives a saturated O(-14) in C/M, yielding Y of rank 7 and degree -20 with C/Y=O(20).

If C lay in E^+, its lower-row map would vanish and X/F would have rank 3, degree -10 inside the exact bf residual D(-2)+T(-3)+O(-8)+O(-10). No degree-minus-two coefficient in rank three can map to the irreducible D. After excluding that degree, a degree-minus-three coefficient can only be W or Wp; neither has a channel to D(-2) or T(-3). All degrees are thus at most -4, contradicting -10. This correctly accounts for the extra D row that was absent in bb.

As before, saturation gives E^+ intersect C=Y. Its lower-row maps factor through O(-14) and require invariants in degrees 18 or 6, both absent. Hence X has rank 6, degree -38, and the same exact extension of O(20) by O(18).

## 7. Uniform full-span saturation

For both c=12 and c=8, U0=C/X injects into Q, and Z0=E/X injects into (H/C) O. Their cokernel is the same sheaf H O/(E+C O). Its torsion subsheaf is the saturation defect of either injection, so the two defect lengths agree.

The residual rank 19-c, degree -16, and ambient dimension 30-c are correct. Saturating increases the degree to -16+delta. The resulting Z still spans H/C because E spans H. Dualizing its embedding consequently injects the constant linear forms of H/C into H0(Z*). Since Z has nonpositive splitting degrees,

30-c <= h0(Z*) = (19-c)-(-16+delta)=35-c-delta.

Thus 0<=delta<=5. The defect is equivariant, so its determinant divisor is invariant; a nonzero divisor has degree at least 12. Therefore delta=0 in both cases. This proves saturation of the actual U0 in Q rather than assuming it from an abstract extension. The cancellation of c in the bound is legitimate and is the key uniform step.

## 8. Exact dual obstruction

The extension space Ext1_G(O(20),O(18)) is the trivial one-dimensional H1(O(-2)). Its zero and nonzero classes give O(18)+O(20) and W O(19). Both have the stated equivariant K-class.

The saturated quotient makes R=(Q/U)* an actual rank-eleven degree-minus-16 subbundle of Q*. The original presentation bounds all its degrees by -1. All H0 groups in the relevant untwisted exact sequence vanish; thus the cohomology subtraction H1(R)=D is exact, not only an Euler-character statement. The twist-three Euler character is also correct.

The H1 budget D permits only D(-2) or O(-6) among degrees at most -2. This follows from parity, (j-1)dim coefficient<=5, and the actual product with Sym(j-2) W. The independent recurrence audit checks these finitely many abstract possibilities. Remaining terms have degree -1.

The D(-2) option forces a negative W multiplicity in L6 A. The O(-6) option uniquely gives L10=2Wp+T from the four stated products with A. Hence H0(R(1))=2Wp+T. Strict-top for the original Q* injects H0(Q*(1)) into the exact original H0(B_q(1))=Sym9 W=S+T. The Wp constituent makes this impossible. No stronger vanishing of H0(Q*(1)) has been assumed.

## Reproduction and boundaries

Both commands passed:

- python3 verify.py
- python3 review_independent.py

The reproduction instructions were read and both commands were rerun against the final package. Reviewed auxiliary SHA256 values:

- REPRODUCE.md: cc0200fc2952b29e4608a66a98404e1f621fafbf3fbb1298814a19d73a3f0054;

- verify.py: e4f075009d2d86bae357919552c164f01f5ec322844405573abaa411d59ca101;
- characters.py: 25d2c28c294298624ee50ce73b2a55422913f7e78b4817c7cb6e813e5004f1fc;
- review_independent.py: 08aa7885f081907a7f7cd5b831fd595d52c8cc9cf1f49984bc0a88b8f812d43b.

The complete source-edge exclusion is established under the pinned actual-bundle inputs. The coefficient-map clarifications above expand valid inferences in the proof; they are not missing hypotheses or unresolved dependencies. This is an independent mathematical and finite arithmetic review, not formal proof-assistant certification or a global coverage audit.
