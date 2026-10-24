# Independent whole-proof review and separate nine-class calculation

## Verdict and exact reviewed object

**PASS, conditional on the explicitly imported actual-input and original profile-specific necessity theorems.** I found no blocking mathematical defect in the full closure argument or in the use of its six residual-shape exclusions. The independent calculation reproduces every complete certificate for all 159 original ordered records, not merely the totals. This review supports exclusion of maximal rank-three profile **(1,1)** and nothing globally stronger.

The reviewed `PROOF.md` has SHA256:

`126fc2e7cbf54ae91f8e2eba3c0e809f70cf49c0f0aef28b574c5be3762ca6d2`

The reviewed `INPUTS.json` has SHA256:

`d9a88cacfb0752c78f1caf00dd35fbe1c8c6a08b12a0c3b9e0f8939698abab08`

I read the entire new proof and all retained complete written proofs: actual splitting, actual ambient Gauss comparison, strict top, the original profile11 necessity theorem, the primal degree bound, the primary four-type theorem, cubic visibility, the two-shape theorem, the cubic-kernel theorem, the profile11 apolar exclusion, and the prior profile-reduction theorem. I also read the entire original verifier and original physical character reference. The ordered JSON was parsed in full and every record independently processed. Neither the historical verifier nor the production verifier/character module was executed or imported.

The original enumeration remains an **imported necessity theorem**, not a theorem newly inferred from this review's row arithmetic. The retained proofs have their own explicitly named upstream actual-module and geometric hypotheses. This review checks the complete retained arguments and their application here; it does not purport to re-establish or fetch every transitive ancestor of those hypotheses.

## 1. Authentication and independent method

All 14 manifest entries pass independent byte-count, SHA256 and Git-blob-SHA1 calculations. Every URL is checked against its exact full 40-character commit and repository path. Additionally, I independently re-fetched each complete file through the read-only GitHub connector at that pinned commit. The returned complete content, Git blob identifier and canonical URL matched the retained input and manifest. This is recorded in `independent/REMOTE-AUTHENTICATION.json`; it is not merely trust in the existing `FETCH.json`.

`independent/recompute.py` parses only the physical nine-class trace, class-size and positive-four-space table assignments from `inputs/character-reference.py`, using a restricted AST evaluator. It reconstructs the nine irreducible class characters with the reference's fixed labeling. It does not import that module, its symmetric-power routine, `characters.py`, any McKay multiplication matrix, or any production functions.

For a determinant-one two-dimensional class of trace x, the calculation uses the closed polynomial

    chi(Sym^n W)(x) = sum_(k=0)^floor(n/2) (-1)^k binom(n-k,k) x^(n-2k).

The arithmetic is exact in Q(sqrt(5)), implemented with rational pairs. This polynomial remains valid on the central classes x=2 and x=-2, so no division or limiting convention occurs. Tensor products are pointwise products on all nine conjugacy classes. Decomposition uses the class-size-weighted inner product divided by 120. The code checks all 81 irreducible orthogonality relations, physical dimensions, completeness by sum of squared dimensions, integrality, and reconstruction on every conjugacy class for every decomposed character.

For each endpoint height it independently constructs the entire derivative-rank partition and sums the stagewise exterior-degree bounds. It then verifies equality to the proof's closed height formula. Thus the independent capacity calculation is not just a copied closed-form maximum routine.

The file `independent/CERTIFICATES.json` is completely generated before the program opens `RESULT.json`. It contains the original ordered A and B blocks, original zero-based index, a, b, original defect, complete cubic character, expanded ordinary degrees, every height value, every maximizing height, first obstruction, and residual closing theorem. Auxiliary whole characters for the four sources and residual shape arguments are also retained. The historical `compatible_E_types` field is not used to make any decision.

Normal Python and `python -O` both pass **8,670 explicit checks** and produce identical certificate and summary bytes. There are no correctness-critical Python assertions to disappear under optimization. The script is relocatable and requires only the standard library, the retained inputs, `PROOF.md`, `INPUTS.json`, and `RESULT.json`. In particular it does not require the duplicate scratch file `RESULT.optimized.json`.

## 2. Actual objects, necessity and same-source discipline

The proof consistently uses the actual rank17 degree-minus54 bundle E in the constant 30-space, not its unrelated 54-dimensional coefficient presentation. Its annihilator S=Q* has rank13 and degree-minus54. A and B are the actual locally free derivative quotients. Their induced derivative images can be nonsaturated, and no argument here silently replaces such an image by its saturation.

For maximal profile (1,1), K and L have ranks14 and10, and both are genuine endpoints whose next derivative ranks are at most two. E has top degree at most -2; S has only the required top bound -1. The written original profile11 proof explicitly distinguishes this from stronger dual-interior hypotheses. Its degree windows, determinant-defect possibilities, parity, incidence and cohomology tests are logically necessary conditions on the same actual inclusion. Its read-only verifier agrees with those tests and retains all original ordered pairs and defects. I did not rerun its historical search or claim to derive its geometric coverage from its output size.

The imported a>=-4 theorem has the correct all-profile scope. Its exclusion of a=-6 uses the original transpose incidence and invariant multiplication, not the profile12 interior estimate. The profile12-specific statements later in that imported proof are not used here. Likewise PR1134's section-envelope argument is genuinely independent of a later plateau rank and is fully rederived in Section5 of the new proof.

The four-type reduction is an actual-source result, rather than a source-ledger filter. Its proof uses both arrows of the terminal pencil, the common fixed determinant rotation, the canonical slope quotient, and functorial terminal reconstruction. In the lower-slope quotient, the kernel map vanishes by degree; the first coefficient arrow then factors through a trivial bundle into O(-1) and vanishes; the second arrow also vanishes by surjectivity. The genuine primary terminal coefficient space consequently lies in the canonical degree-minus-three coefficient space. Intersecting this inclusion with the old splitting equations gives exactly the four displayed sources. No horizontal splitting of the Gauss connection is obtained or needed from a Birkhoff decomposition.

All four sources satisfy the uniform minimum-degree and cubic-visibility constraints. Thus the finite argument does not select an E witness for one test and a different E witness for another. Whenever a residual quotient contains O(-8), its onto projection forces the same actual D-source. In row109 the separate onto projection forces the actual P-source. The historical existential compatibility lists play no role.

## 3. Two-endpoint capacity lemma

The capacity proof is valid in both orientations.

1. A derivative kernel has torsion-free quotient in its source. On the smooth curve that quotient is locally free; combined with the previous ambient quotient this makes each subsequent kernel saturated in the original constant bundle.
2. For successive actual kernels F_j, differentiation of F_j lies in F_(j-1), and its projection modulo F_j has kernel exactly F_(j+1). This gives an injection of locally free sheaves G_j into G_(j-1)(-2), and hence into C(-2j). It is an injection of the coherent image, not a saturated-image assertion.
3. These injections make the positive ranks q_j nonincreasing. The endpoint hypothesis gives q_1<=2. Every nonzero F_j is negative as a subbundle of E or S. If its derivative were zero, its Grassmannian map would be constant in characteristic zero, and saturation would make it a degree-zero constant bundle. Therefore its derivative rank is positive and the rank strictly decreases until zero. This justifies summing all quotient ranks and degrees.
4. A nonzero top exterior-power morphism gives deg G_j no larger than the sum of the q_j largest ordinary degrees of C, minus 2j q_j. Expanding representation dimensions into ordinary line degrees is essential and is done in the calculation.
5. Nonincreasing ranks in {1,2} correspond exactly to heights h_1>=h_2>=0 with sum n. Summing the bounds produces the stated two-column capacity. The cases h_2=0 include rank-one endpoints. Repeated top degrees and tied maximizing heights cause no loss of necessity.

The resulting inequalities concern the same actual pair: deg K=-54-a <= Cap14(A) and deg L=-54-b <= Cap10(B). Only eight primal and six dual heights are used. The proof needs neither an equality classification nor top(S)<=-2 to obtain this necessary bound.

## 4. Uniform source and cubic obstructions

All ordinary degrees of the four sources are at least -8, so E(8) and its quotient A(8) are globally generated. This rules out any degree below -8 in A. For a two-dimensional O(-8) target, only the single scalar O(-8) of the D-source could contribute. Its simultaneous image has rank at most one. This is the correct joint quotient-rank obstruction, not two separate nonzero-Hom tests.

The cubic visibility theorem is also used in its correct coefficient-space sense. A killed saturated cubic graph has internal derivative target of top degree at most -4, hence is horizontal by Hom vanishing, contrary to negativity. For each nonzero quadratic top block, its actual coherent-image kernel has cubic section dimension at most dim R-1, less than six. Therefore the top T channel cannot vanish. If that channel coincided with the cubic T channel, the unique relevant equivariant bundle map would cancel it by a saturated graph, giving the same impossible negative horizontal block. The W' constituent is distinct. Thus W'+2T injects into H0(A(3)) for every actual source type. No fiber-rank14 claim follows, and none is made.

The independent calculation recomputes each entire H0(A(3)), not merely its W' and T entries. It uses negative symmetric indices as zero, with all representation and repeated-block multiplicities preserved.

## 5. All159 certificates and exact residuals

The exact first-obstruction partition is:

- Source degree or simultaneous quotient-rank obstruction: 56 original records.
- Cubic visibility, among those left: 32.
- Dual endpoint capacity, among those left: 62.
- Primal endpoint capacity, among those left: original indices 32,50,52.
- Residual shape arguments: original indices 94,95,100,106,109,127.

For each of the three primal-only first exclusions, deg K=-52 while Cap14(A)=-70. All 159 row certificates and all **2,226** endpoint-height values agree exactly with the production result, including optimizing-height ties. The complete index sets are in the independent certificate file. The partition is certified by per-record tests, not by the identity 56+32+62+3+6=159 alone.

Here are the exact retained block orders from the original JSON, without renumbering. `one` denotes the trivial coefficient representation.

    94:  A=[(-8,one),(4,one),(6,one)]
         B=[(-8,one),(-6,one),(6,one)]
         (a,b,t)=(2,-8,0); capacities=(-42,-42).
    95:  A=[(5,W),(-8,one)]
         B=[(-7,W),(6,one)]
         (a,b,t)=(2,-8,0); capacities=(-42,-44).
    100: A=[(-8,one),(4,one),(8,one)]
         B=[(-10,one),(-6,one),(6,one)]
         (a,b,t)=(4,-10,0); capacities=(-26,-42).
    106: A=[(-8,one),(4,one),(10,one)]
         B=[(-12,one),(-6,one),(6,one)]
         (a,b,t)=(6,-12,0); capacities=(-10,-42).
    109: A=[(-5,Wp),(16,one)]
         B=[(3,Wp),(-18,one)]
         (a,b,t)=(6,-12,0); capacities=(20,-30).
    127: A=[(-8,one),(2,one),(16,one)]
         B=[(-18,one),(-4,one),(6,one)]
         (a,b,t)=(10,-16,0); capacities=(38,-38).

The proof's reordered displays denote the same splittings; the independent data preserve the original list order exactly. Each t is the original transpose defect. No defect of a different Gauss derivative is set to zero.

## 6. Complete residual-shape dependency review

### PR1135: rows94 and95

The forced D-source matches the imported theorem exactly. The scalar O(-8) quotient cancels by the actual onto row; possible positive components of its source do not alter the actual kernel. In the split case, the D row cannot land in O(4); its nonzero five-section system to O(6) has invariant common-zero divisor of degree at most eight, so it is onto by the minimum orbit size twelve. The cubic S channel cannot be killed: that would trivialize a rank-four nonpositive kernel whose degree is negative. The T channel cannot fit in its kernel dimension either.

In the balanced case, a rank-one coherent image would have the only possible equivariant degree n=2, but Hom_G(O(2),W O(5))=0. Rank two follows. Global generation after twist two bounds the torsion defect by eleven, and invariance then forces zero defect. Its cubic kernel has rank at most three, so neither S nor T is lost. The saturated-graph argument supplies the independent second T channel in both cases.

Thus H0(K(3))=0 and deg K=-56 with rank14 forces K=(2V+2P)O(-4). Strict-top injects its quartic coefficients into H0(A(2)), which has only one V copy. The independent calculation verifies both Euler identities, keeps the negative scalar tail, and obtains exactly this multiplicity contradiction. No derivative-rank assumption on K is imported.

### PR1142: rows100 and106

For the D-source, H0(K(3)) is either zero or S. If S survives, the actual top-row kernel must be S O(-3): its rank is at most four, it is nonpositive after twist three, and it has four independent sections. Its actual coherent image is consequently the line O(2), giving an equivariant sheaf injection into A, without requiring saturation in A.

For both residual shapes Hom_G(O(2),A)=0, by absence of invariants in the relevant symmetric degrees. Therefore K has top at most -4. The strict-top quartic injection and Euler additivity give the improved envelope with exactly H0(A(2))+chi(A(4))-chi(E(4)), not an extra H0(A) term. The independent calculation verifies that its V coefficient is -1 in both cases. The negative O(-8) contribution is retained in chi(A(4)).

### PR1145: row127, with its positive-defect alternative retained

I checked the full proof, including both equality heights and the partial-polynomial-system issue.

The other original row for this A is119, with original defect12. Its dual degree is -26 but its largest capacity is -50, so it is excluded directly. Row127 has degree -38 and maximizing height pairs (7,3) and (8,2). Equality in the sum forces equality in every exterior-degree bound. Since the three B degrees are distinct, the highest exterior summand is unique. A nonzero determinant map of equal degree has no zero; all lower components vanish by degree. Thus each actual composite image is the appropriate top subbundle, and the leading derivative channels are nonzero.

For height8, nine independent osculating directions in a degree-ten coefficient quotient force that quotient to be full: Sym10 W=A_std+V+D has no proper quotient of dimension nine or more. The apolar annihilator of the resulting rank-nine osculating subbundle is W O(-9). Every E summand has degree at least -8, so its projection into that annihilator is zero. This would put a nonzero constant space in S, impossible. Only negativity of S is used.

For height7, the degree-eight coefficient system is full because Sym8 W=P+D has no proper quotient of dimension eight or more. The projection of E to its constant nine-space factors through O(-8) and is nonzero on the unique source O(-8). The actual coefficient map of that source is consequently a constant-space isomorphism onto the projection. Its image provides a genuine constant complement to the 21-dimensional kernel. This proves the claimed block decomposition of the actual embedded inclusion; it does not assume a Birkhoff complement is horizontal.

The residual rank16 bundle F in that constant 21-space has dual rank5 and quotient B_F=O(-4)+O(-18). The other constant block contributes rank-one endpoint derivative. Therefore the residual endpoint derivative has rank at most one and, by negativity, exactly one until zero. Its three line-quotient bounds sum exactly to deg L_F=-24, forcing the last line O(-10) and four actual osculating directions.

Crucially, the residual degree-ten coefficient quotient R is allowed to be proper. The proof dualizes its quotient map and embeds R* in the full Sym10 dual before taking the universal apolar annihilator. This legitimately factors F through (V+P)O(-4). All higher-degree source blocks have zero Hom there; only the unique V(-4) scalar channel remains. Its scalar cannot vanish, because then a nonzero constant R would annihilate F. Hence R* contains every l^4 V.

The sextic-net lemma proves these spaces span the full Sym10: the invariant V-net has no common zero, since its divisor degree is at most six and every projective orbit has size at least twelve. Its evaluation kernel is O(-a)+O(-b), a,b>=1, a+b=6. After twist four both H1 groups vanish, proving surjectivity V tensor Sym4 W -> Sym10 W. Pure fourth powers span Sym4 W in characteristic zero. Thus R is full only at this justified final stage. Its dimension eleven leaves constant kernel dimension ten, which cannot contain the rank13 sum D(-2)+(W'+T)(-3). This closes the difficult height7 branch without stronger dual top or an unsupported full-coefficient-system assumption.

## 7. Row109: independently checked P-source and invariant deficit

The quotient projection to W'(-5) is onto. For E_V and E_Z all source degrees are greater than -5. For E_D only O(-8) could contribute by degree, but its equivariant Hom has trivial multiplicity zero in W' tensor Sym3 W. The independent code computes the entire Hom contribution from each source block: the total dimensions for D,P,V,Z are respectively 0,1,0,0. Hence the same actual source is E_P.

For F_i=E^(-i), strict-top gives top F_9<=-11, so H0(F_9(10))=0. The exact kernel-quotient sequences give the section inequality after telescoping; the actual injections J_i->A(-2i) then give the nine-term upper envelope. Semisimplicity legitimizes coefficientwise addition. No later rank-three hypothesis, endpoint top bound on S, or profile21-specific fact enters this deduction.

The independent complete source character at twist ten is

    4*one + 8*A_std + 6*V + 8*P + 11*D.

The complete nine-term target character is

    3*one + 10*A_std + 10*V + 13*P + 16*D.

Each of P tensor Sym8, W' tensor Sym7, T tensor Sym7 and V tensor Sym6 contributes one source invariant; W' tensor Sym5 contributes zero. The W' part of the target at degrees5,3,1 contributes zero each. Its scalar degrees26,24,22,20,18,16,14,12,10 have invariant multiplicities

    0,1,0,1,0,0,0,1,0.

Thus the necessary inequality fails on invariants as **4>3**. This excludes the actual shape in any profile in which it arose; no stronger dual bound is being transferred.

## 8. Reproduction evidence and boundary

See `independent/README.md` for relocatable normal and optimized replay instructions. Exact SHA256 identities:

- Independent code `independent/recompute.py`: `238b6dd7cca4931db8ec8080aab92bad7293e10ee5cb684d09b74e81d350e917`.
- Complete independent certificates: `5f644b133cb56fcf0ef38e0443b8eefee93661e2d8bdf956c1ff08cfde8eb6b5`.
- Independent summary: `10a8e0fba99688eddb5c1192d185693a2c41070179720909426d7f6227b0756c`.
- Independent remote authentication: `27869b659b9dbf05e21cf74e360c7e58fc9fb5a0e92a8b82bd5c334e088e01ec`.
- Compared production `RESULT.json`: `eca3f6e448fad6830b63ba7e4f7566a95adbb1a3da6c6f511c7e1b99873e48bb`.

The proof resolves the stated original maximal-profile(1,1) coverage dependency, relative to its pinned actual and necessity inputs. It neither proves nor assumes that all hypothetical generic-rank-three configurations have profiles (1,1),(1,2),(2,1). The earlier maximal-profile exhaustiveness remains a separate unresolved dependency here. Consequently there is **no global rank-three exclusion, global COV, rank-four theorem, maximal-rank result, full-adjoint invertibility, smoothing, algebraicity, or original-theorem repair** in this verdict.

All work was limited to retained proofs, read-only immutable-source authentication, and fixed-record universal arithmetic. No actual HM/source-instance coefficient, selected parameter or point, actual jet, tensor, matrix, instance-rank evaluation, scan, historical re-enumeration, large computation, or public write was performed.
