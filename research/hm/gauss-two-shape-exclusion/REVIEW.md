# Independent review: two low degree-two Gauss quotients

## Verdict and exact binding

PASS for the standalone theorem and its stated fourteen-row historical consequence, relative to the seven pinned actual inputs. Both quotient shapes force the impossible strict-top inclusion 2V+2P into V+2P+D. The argument needs neither a profile assumption nor a rank-three assumption on the next Gauss derivative.

This review binds the final frozen SHA256 hashes:

- PROOF.md: a3c6a5ca199edd50e09268a605cee536e43a2233571e14e43e18e7c031aacdb0
- verify.py: cb9946f549b2db8c832f4ce9406dfb4a290646c3d579015a69a45e030fd5bbba
- characters.py: 5b3b1d415f26ca467670afeb73357cbb0e9c125a6b1acd25155b6d85eef4e4f1
- RESULT.json: e23d6a797de50fefe04ad3cfe6b55a0d0ed79c23988182be3a19ca1ea75da96b
- INPUTS.json: f951277dfa33a7a6fa0e707dae42af18f5711da7a9efcac4c2d66f4a7eabf196
- REPRODUCE.md: 4fe32adf79723cd690a4c4231c8bd9f180dfdd955a285e24f4fb31f22f16fe44

I reviewed the complete proof, checker, character module, result, reproduction note and source scope. I ran the checker in normal and optimized modes, independently recalculated the required characters by conjugacy-class averages, independently matched the fourteen full historical records, and recomputed the byte length, SHA256 and Git blob SHA1 of each included original against the manifest.

The earlier draft had an optional combination with a separate profile21 reduction. That paragraph was removed before this binding, and the final reproduction note no longer relies on it. This review does not certify a four-row residual profile21 claim. The core theorem, checker and machine result were unaffected by that scope correction.

## 1. Actual bundle and source scope

The theorem starts with the exact actual splitting

    E=D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8)

and the actual constant plane-section embedding. It does not replace that embedding by a terminal-pencil embedding or assume the Birkhoff splitting is horizontal. The local quotient A_q=E/ker(beta_E) is the actual locally free derivative quotient, not a prescribed abstract target with an arbitrary arrow.

PR1123 is used only where its four-type theorem is needed: the other three possible source types have all degrees greater than -8 and therefore admit no nonzero map to O(-8). Thus either displayed quotient forces the exact D-type among those four sources. The core two-shape theorem already assumes the D-type and is independent of that coverage reduction.

PR1129 supplies the correctly stated near-top coefficient lemma, previously independently reviewed. Its use here is on saturated ordinary graph subbundles with explicitly controlled quotient degrees. The proof also spells out the relevant horizontal-negative-subbundle contradiction rather than silently treating bundle summands as horizontal.

The historical JSON fixes row identities and ordered quotient data. Its labels and flags are not used to prove geometric completeness. The fourteen-row application is valid as a cut of those fixed records and is explicitly not a claim of fourteen newly live exclusions.

## 2. Cancellation of the negative scalar factor

Only the displayed scalar O(-8) source can map to the O(-8) target factor. Surjectivity of E -> A_q forces this scalar map to be an isomorphism. Hence a kernel vector has zero scalar coordinate, and the actual kernel is exactly

    K=ker(E_hat -> C),
    E_hat=D O(-2)+(W'+T)O(-3)+V O(-4).

The induced map to C is onto: a target section (0,c) lifts through E, and its lift must have zero scalar coordinate. Possible positive-target rows from the scalar source are not incorrectly erased; they simply do not affect this kernel statement.

Strict-top for the actual E gives H0(K(2))=0. Since H0(E(2))=D, its D row is nonzero and gives five independent coefficient sections. This uses actual derivative geometry, not a dimension-only inference about an arbitrary map.

## 3. Split target: all nonzero channels are justified

For C=O(4)+O(6), the D-to-O(4) row vanishes since D is absent from Sym6 W. The nonzero O(6) row is a degree-eight section system. Its common-zero divisor is invariant and has degree at most eight, so it is empty. Thus this row is onto.

The invariant-divisor bound is legitimate. The projective action is A5, and the stabilizer of a point in a finite subgroup of PGL2(C) is cyclic. Its order here can only be 1,2,3 or5; hence nonempty orbits have sizes 60,30,20 or12. A nonempty invariant effective divisor has degree at least twelve.

The kernel K_D has rank four and degree -16. Injectivity of the D coefficient at twist two gives maxdeg K_D<=-3. Thus K_D(3) is nonpositive with at most four independent sections. In the cubic map S+T -> S+T, the T channel cannot vanish because dim T=6; the S channel cannot vanish because four sections would force all four nonpositive summands to be degree zero, contrary to deg K_D(3)=-4. Therefore the cubic map is an isomorphism. This proves, rather than assumes, the nonzero scalar channels.

## 4. Balanced target: rank and saturation are established separately

For C=W O(5), use the actual coherent image I of the D row. It is torsion-free as a subsheaf of C and hence locally free on the smooth line P1. It is not presumed saturated in C. The map D O(-2) -> I is onto by the definition of the image, so I(2) is globally generated. If I had rank one, it would be an equivariant line O(n). Its injection into 2O(5), without any saturation assumption, forces n<=5; its even central action forces n even. The quotient from D O(-2) makes O(n+2) globally generated, so n>=-2. Within n=-2,0,2,4, only n=2 permits D inside Sym^(n+2) W. Yet Hom_G(O(2),W O(5))=0 because W is absent from Sym3 W. Thus the coherent image has rank two. This argument never replaces the image by its saturation without justification.

For the rank-two image I, I(2) is a quotient of a constant bundle, hence globally generated. Its five independent D sections imply

    deg I+6=h0(I(2))>=5.

The torsion length in W O(5) is delta=10-deg I, so 0<=delta<=11. The determinant defect divisor is invariant; the same minimum twelve forces delta=0. Only at this rank-two defect step is saturation proved. Therefore the actual D row is everywhere onto.

Its kernel has rank three, degree -20 and maximum degree at most -3. The cubic kernel has dimension at most three. Every nonzero G-subrepresentation of S+T has dimension at least four, so the cubic D map is injective. Its image is S plus one T multiplicity line. All rank, degree, parity, generation and twist claims in this argument check out.

## 5. The graph construction and the retained V rows

For both targets, H0(C(3))=W'+S+2T. Near-top visibility makes the W' cubic source nonzero, filling the unique W' constituent.

The space Hom_G(T(-3),D(-2)) has dimension one. Its composition into C is nonzero because it is precisely the nonzero T channel already proved for the D row. If the separate T row belonged to that same target multiplicity line, its bundle map would factor through a unique graph lift into D(-2). Subtracting the lift is an equivariant triangular bundle change. The resulting graph is a saturated T O(-3) subbundle of E, with complementary degrees at most -2.

Its full external beta_E row would vanish, including the negative quotient row by degree. The internal derivative then lies in a quotient with maximum degree -2 twisted by -2, and has no Hom from O(-3). It would make the negative graph horizontal, contradicting saturation in the constant ambient bundle. Thus the two T lines are independent.

This proves the cubic-section isomorphism, not just generic fiber surjectivity. The V O(-4) source contributes no cubic sections, but its actual bundle rows remain untouched. There is no tacit elimination of those rows and no need for a connection-compatible complement.

## 6. Pure kernel and the final representation obstruction

The cubic-section isomorphism gives H0(K(3))=0. The exact source and quotient give rank K=14 and deg K=-56. Hence every summand has degree at most -4 and all fourteen degrees must equal -4.

The Euler character calculation correctly includes the negative O(-8) tail: at twist four it contributes minus A_std through H1, not zero. For either quotient its corresponding O(-8) tail gives the same subtraction. The resulting exact identities are

    chi_G(E(4))=3V+3P+2D,
    chi_G(A_q(4))=V+P+2D,
    K=(2V+2P)O(-4).

K is saturated in E and in the constant ambient bundle. Because K=ker(beta_E), its actual second fundamental form factors through A_q(-2). Strict-top on K therefore forces an injection

    2V+2P=H0(K(4)) -> H0(A_q(2))=V+2P+D.

The V multiplicity mismatch is decisive. No assumption on the next derivative rank is needed, so the theorem genuinely applies to every profile containing the exact E/A_q pairs.

## 7. Independent character computation and reproducibility

Both python verify.py and python -O verify.py succeeded after the final scope revision. Each internally reproduces RESULT.json byte-for-byte and records 144 checks. Their emitted JSON also agrees with RESULT.json. No --write execution was used.

My independent computation did not import verify.py or characters.py. It used exact arithmetic in Q(sqrt(5)) on the nine classes with sizes

    1,1,12,12,12,12,20,20,30

and W traces

    2,-2,phi,-phi,phi',-phi',1,-1,0,
    phi=(1+sqrt(5))/2, phi'=(1-sqrt(5))/2.

I evaluated symmetric-power characters by s0=1, s1=t, s(n)=t s(n-1)-s(n-2), formed tensor products pointwise, and took class-weighted inner products divided by 120. The nine irreducible characters were checked pairwise orthonormal. This independently verified Sym6 through Sym10, D tensor W, D tensor Sym2 W, W tensor Sym7 through Sym9 W, the rank-one Hom obstruction, both cubic target characters, both Euler differences, and both strict-top target characters.

The independent output gives the same forced kernel coefficient 2V+2P and target V+2P+D for each shape. The abstract character calculation verifies numerical ingredients; the geometry is supplied by the reviewed proof.

All seven source byte lengths, SHA256 hashes and Git blob SHA1 identities match INPUTS.json. The manifest supplies immutable public commit URLs. The copied PR1129 proof also matches the exact previously reviewed visibility proof hash f7f267098d561de91e216f34588d1ab983947c2363b5a2dd4b0bd59104b39eed.

## 8. Independent fourteen-row identity check

I filtered the fixed authenticated historical list by the two exact A shapes, without rerunning any quotient or source enumeration. The fourteen resulting full dictionaries agree with RESULT.json, including stable ID, profile, source index and commit, complete ordered A and B blocks, and original defect. I separately recomputed rank A=rank B=3 and original defect -6-deg A-deg B for every matched record.

The exact records are:

- Profile11 index77, G3.11.bda60479b90e, defect20.
- Profile11 index78, G3.11.d410285c831a, defect20.
- Profile11 index80, G3.11.379add3f34d0, defect12.
- Profile11 index81, G3.11.84bacc79212b, defect12.
- Profile11 index82, G3.11.ce461c0a9a5e, defect12.
- Profile11 index83, G3.11.9ee2ea50aa76, defect12.
- Profile11 index84, G3.11.142416330965, defect12.
- Profile11 index85, G3.11.9e100b5437dd, defect12.
- Profile11 index94, G3.11.32f5d3efc97b, defect0.
- Profile11 index95, G3.11.966331d6ffc3, defect0.
- Profile21 index3, G3.21.ae29bef8b31e, defect12.
- Profile21 index4, G3.21.3bc00aa2165a, defect0.
- Profile21 index6, G3.21.94406336f081, defect12.
- Profile21 index7, G3.21.8de61cbbef4b, defect0.

The independent count is ten profile11 plus four profile21, with no profile12 matches. This authenticates the historical cut, not coverage beyond the imported geometric inputs and not a live-frontier count.

## Final scope

The frozen packet proves two genuine exact-source quotient exclusions and correctly transfers them to the fourteen matching historical records using the separately pinned four-type theorem. It does not establish COV, a global rank-three exclusion, a current residual frontier, or any repair of the original theorem. These limitations are stated consistently in the revised proof and reproduction note.

No selected actual coefficient, point, parameter, tensor, jet, matrix, derivative evaluation, instance rank, instance scan, or historical enumeration was used. I found no remaining mathematical gap in the standalone theorem at its stated scope.
