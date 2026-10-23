# Independent integration review: all nine maximal rank-three profiles

## Verdict and exact review target

**PASS for the stated conditional theorem.** At the frozen bytes below, Sections 3–6 correctly combine the actual maximal-plateau exhaustion, separate exclusions of generic ranks 0, 1 and 2, and all nine ordered rank-three profile exclusions. They prove generic SF rank at least 4 and, through the actual square-map comparison, generic positive-square rank at least 28, kernel/positive double-hyperplane section dimension at most 13, and cokernel dimension at most 9.

No mathematical change to the candidate proof is required. This acceptance is conditional on its explicitly retained actual geometric theorems and inherited necessity/transfer prerequisites. It is not a fresh proof of every transitive HM input or historical enumeration, proof-assistant verification, surjectivity, SF rank 13, full-adjoint invertibility, a Bockstein-order theorem, smoothing completion, algebraicity, or original proof repair.

Reviewed candidate directory: `nine-profile-rank-bound`.

- `PROOF.md`: `1f2ec9df105df1d3b3e1b78a1822970c577b6daaa02a15b4d5c56bf076e81532`.
- `verify.py`: `49663da8305265f33656e2ac9d78ed3817cf0198fa05b664143d3d170a38c2b0`.
- `RESULT.json`: `29d503df461baad8c0c8a7595f6ecfae9aff244ea6439fc9b0055990f1163dc8`.
- `INPUTS.json`: `b1f376130b3f6fe84e6d8e723b99751b90823c14604de4063e94b7b27b6c2cbc`.
- `REGISTRY.json`: `6aed378989ec3a929feb8b0d798c047111a9ac0c2e0d3a1087ad83dc565107c6`.
- `COVERAGE.json`: `2931c7469389e8d5355bef19f7ea3f714d1aa437b1f8cc64db3109d2779a872c`.
- `REPRODUCE.md`: `077c5b3240351153aa34997d0f8eb3576be561efd20a5e11b19445c7d950e3e8`.

`TARGET-SHA256SUMS` records those seven exact files. `REVIEWED-INPUTS.json` is the identical frozen 52-source immutable URL/commit/byte/SHA-256/Git-blob manifest. Review performed 2026-10-23.

## 1. What was independently checked

I read the full candidate proof and all 52 retained direct mathematical source texts, including the original six-note (2,2) chain, all fourteen (3,1) notes, both P-source pairing branches for (3,2), the full-saturation (1,3) proof, the lower-rank flag arguments, and the actual hyperplane/Koszul foundations. This was not a review of the candidate's profile labels or of other reviewers' verdicts alone.

I separately read the completed cubic/lower-rank report, the full profile31 report, the original22/32 report, and the earlier accepted profile11 integration review. They corroborate the direct scope checks but are not mathematical premises in place of the original sources. The review conclusions were checked against the actual source texts; their verdicts do not replace those mathematical sources.

All 52 retained sources have independently recomputed byte counts, SHA-256, Git-blob identities and exact immutable URL structure agreeing with the frozen manifest. Forty-eight were also byte-compared to independently fetched immutable copies retained by the component reviewers; that comparison found no differing bytes. This integration review did not itself repeat their remote fetches. The four files not cross-compared by that procedure are the unused historical total-length note and the three imported profile11/12/21 combination theorems. Their manifest byte and Git identities were checked, and profile11 additionally matches the previously accepted exact proof hash `a53c95281f491f09fffc3a3f8fcd542c2b2038d8306367f9c42c183b9e6e8c03`.

The review's independently authored `independent_controls.py` imports no author verifier or historical enumerator. It implements a separate scoped implication checker and exact abstract arithmetic. It passes **26,968 explicit checks and rejects 128 harmful mutations**, identically under ordinary Python and `python -O`. Its only representation input is the defining-doublet McKay graph with the physical W marking. The program reconstructs symmetric-power actions, rather than importing the candidate's arithmetic or another proof enumerator.

No actual HM coefficient, parameter value, point, jet, tensor, instance matrix or actual-instance rank was selected, constructed or evaluated. No historical source-pair experiment or old 2947-record enumeration was regenerated. No external write was made.

## 2. Actual maximal-plateau exhaustion

The candidate's existence argument is valid for the actual saturated subbundle, not merely for its equivariant splitting class.

For any saturated F in the trivial ambient H O, the derivative kernel F-minus is saturated: F/F-minus is an image in a vector bundle and therefore torsion-free on the smooth curve, and the ambient quotient is an extension of torsion-free sheaves. The saturated forward transform F-plus is likewise a subbundle and contains the derivative regularly. Thus the differentiation inclusions used throughout remain valid at ramification points.

At the central E, generic SF rank three gives ranks 14 and 20 for the first backward and forward stages. Moving backward, the next derivative takes values in the preceding quotient twisted by O(-2); moving forward, it kills the preceding stage and factors through the last increment. Therefore each outward increment is at most its predecessor. Continuing exactly while it equals three gives a finite maximal consecutive plateau. It cannot skip a larger increment later and return to three, since the increments are nonincreasing.

The rank bounds alone give k from 1 through 5 and l from 1 through 4, with

    rank F_i = 17 + 3(i-k).

This is a genuine 20-pair a priori domain, not a nine-label assumption. Its endpoints are proper positive-rank bundles: 17 and 13 are not multiples of three. Maximality bounds their next derivatives by two. The candidate never assumes they are rank three or rank one. Indeed the no-constant/full-span hypotheses rule out zero at such endpoints, but the weaker bound “at most two” suffices for every imported theorem here.

At an interior stage, the preceding saturated subbundle is contained in the derivative kernel and has the same generic rank. Equality follows because both are saturated in the same ambient. The analogous argument gives equality with the next forward transform. These are sheaf equalities, not equality with enlarged pointwise kernels at exceptional parameters.

Interior constant subbundles above E propagate backward through these derivative kernels into E and are impossible. Below E their impossibility follows directly by inclusion. The dual constant-span argument is valid as well: a proper constant span of an earlier stage contains its forward transform and therefore eventually E, contradicting full span.

### Cubic sections really bound both ordered lengths

A nonzero section of E(d) supplies a line O(-e), with 1 <= e <= d, saturated in E and in H O. Its inclusion is a polynomial coefficient vector of degree e in an affine trivialization. In characteristic zero the vector and its first e formal derivatives span its constant coefficient space: the coefficient transformation is triangular with nonzero factorial diagonal. This is a universal algebraic identity for arbitrary coefficients, not an experiment at a selected parameter.

Differentiation and saturation preserve its containment in the corresponding successive plateau stages. If l>d, the constant coefficient span is reached in an interior stage, contradicting the preceding nondegeneracy. Hence H0(E(d)) nonzero implies l<=d. Applying this argument to the reversed annihilator plateau centered at Q* gives k<=d from H0(Q*(d)) nonzero. The reversal exchanges lengths but does not identify E and Q*.

The actual Euler characters are

    chi(E(3)) = W' + 2T6,
    chi(Q*(3)) = T6 - 2W - S4.

The positive coefficients imply nonzero sections because the H1 multiplicities are nonnegative. Neither argument assumes H1 vanishes. Therefore k,l are both in {1,2,3}. The independent controls derive these characters from the actual M2/M3/M4 characters and independently obtain the nine ordered pairs. They also check the reversed plateau's central rank13, so replacing12 with21 cannot pass.

This proves exhaustive coverage of all possible maximal rank-three plateaux. The separately retained historical “length at most four” theorem is unnecessary for this deduction and is not used as an implicit shortcut.

## 3. Compatibility of the imported hypotheses

All branches concern the same actual sequence

    0 -> E -> H O -> Q -> 0,
    dim H=30, rank E=17, degree E=-54,
    rank Q*=13, degree Q*=-54.

The actual coefficient presentation in the 54-dimensional M3 space is distinct. The Koszul middle cohomology supplies H with character 2A+2V+2P4+2D5. The independent controls reproduce dimension30 and the separate coefficient dimensions41,54,37.

The physical parameter line P(W*) and single determinant identification are preserved. W is the defining doublet, W' the other doublet, and V the nonstandard three-space. Renaming a local quotient A or a local representation T does not replace these identifications. The actual annihilator has the negative-transpose derivative, with the correct cotangent twist O(-2). None of the imported proofs makes an independent source/transpose rotation.

The global vanishing H0(E(1))=0 is an actual input proved using the physical odd twist-five section part and independently by the common-annihilator Koszul sequence. It is not inferred from l=1. In contrast, the top bound for Q* used in profile21 and22 follows from k>=2 via dual persistence; it is not promoted to a universal bound for profile11. The five dual cubic types used when k=3 follow from H0(Q*(2))=0, while the 37-type list for k=2 has the weaker twist-one hypothesis. These domains are used in the appropriate directions.

The primary-terminal theorem at commit504b7eb800407dfc7e6340c98c72cdd553939f54 supplies an actual embedded W'+T6 in R3 for this same E. Its proof uses both arrows of the actual terminal subpencil and functoriality under the canonical low-slope quotient. The zero map to the lower-slope kernel alone is not taken as enough: factorization of the first coefficient arrow through a constant quotient makes it zero, and commutativity/surjectivity then kills the second arrow. This is exactly what permits subtraction of the primary character from R3.

Intersecting that actual inclusion with the source equations gives exactly D,P,V,Z. The independent code exhausts the original bounded nonnegative equations, obtains all28 formal types and exactly these four primary types, and checks rank17 and degree-54 for each. They are necessary alternatives, not four realized bundles. The stronger reduction is compatible with all earlier exclusions on the larger28-type overlist.

Equivariant Birkhoff splitting and every graph/extension calculation remain bundle statements, never horizontal decompositions. Subsequent Hom obstructions are applied to every map out of the resulting bundle isomorphism type. Horizontal contradictions first prove that an actual derivative kills the subbundle and then prove its remaining internal derivative vanishes by negative-degree Hom; a mere killed external component is not mistaken for horizontality.

The original159, ten-shape, thirteen-pair, and22/31 necessary classifications remain imported mathematical premises, with their original hypotheses. No JSON size is used to establish their actual-source transfer. The new conclusion is not used by any imported exclusion; historical comments that other profiles remain open do not invalidate later combinations of their individually proved exclusions.

## 4. Profile-by-profile audit of the cover

### (1,1)

The exact accepted full theorem at commit707e597b176f9ac88c87a6a58aecf4cada88537c is imported, not merely the final D-pair proof. Under its retained original159 necessity, P and V/Z closures apply to the actual maximal11 geometry. D then reduces to ordered pairs32,50,52. Pairs32 and50 share the same A but have different B and determinant defects; the former's defect12 is retained. The two-endpoint exclusion covers32 and52; the accepted scalar-pair theorem covers50. The combination does not borrow the profile21 top bound or assume rank three at either endpoint.

### (1,2)

The direct primary-profile theorem at commit7cb2e260b2bcbac15df89612b6a2096263a9c89c imports the complete original ten necessary shapes. Five have an unreachable degree-minus-ten or degree-minus-nine quotient, one asks a single O(-8) source line to supply two such quotient lines, one lacks the actual primary W' cubic visibility, and the remaining three fail the iterated twist-four V section envelope. This proof covers all ten original shapes including their independent second-dual defects. Its partial21 restriction is not used as a complete21 theorem.

### (1,3)

The full-saturation theorem is essential. It starts with the full image I=(E/K)(3) of rank3, not with an assumed rank3 cubic subimage. Quartic generation allows degrees>=-1 in its saturation; the sole possible negative block V O(-1) would exhaust the rank and have no sections, contradicting the embedded cubic U. The dual envelope uses the rank-ten kernel and numerical Euler degree D-17, not the opposite-direction D-1. The four saturation candidates reduce to three after the actual target Hom test. Degree I>=11 and saturation degree<=19 give defect<=8, so the invariant divisor gap proves exactness. The resulting kernels all have a two-copy top-V bottleneck against a one-dimensional Hom target. The internal negative-degree argument then proves a negative V subbundle horizontal. This applies to every cubic-image rank and does not require an endpoint-rank assertion.

### (2,1)

The full closure at commitc69f97aaf00e116e3a8abebf19a8e02868c4f7c4 retains the original thirteen-pair necessity and its two direct predecessor reductions. The first excludes {0,1,8,11,12}, cubic rigidity excludes {3,4,6,7}, and the displayed closure treats {2,5,9,10}. These are disjoint and cover thirteen, including both defect12 rows in the rigidity part.

For the last four D-source rows, the rank10 endpoint has nonincreasing positive derivative ranks at most2. Their height partition has six possibilities. Independently recomputed degree capacities are -38,-42,-46,-49; the last three are strict contradictions. The equality case has heights (7,3) or(8,2), with the former removed by strict top decrease. The latter forces a degree10 line and at least9 independent derivative directions. Sym10=A+V+D has no proper equivariant quotient of dimension9 or more, so the entire polynomial system is forced. Its eighth osculating subbundle lies in Q*, and apolar annihilation makes the actual projection of E land in W O(-9), impossible for the exact D source whose least degree is-8. This is an actual inclusion/annihilator argument, not a matching-dimension claim.

### (2,2)

All six original notes are retained and applicable. The base exhausts every center-even rank3 quotient shape in the derived finite windows, with the actual28 primal and37 dual necessary sources. Exact-kernel and cohomology filters preserve necessity. The chain35→34→24→7→3 is not itself the proof: each removal is justified by the written necessary constraints and terminal arguments.

The second-interior degree proof gives a>=-2,b>=-10, so the ORIGINAL defect t=-6-a-b lies between0 and6 and vanishes. The distinct second defects are not thereby erased. For the seven surviving A shapes, the bounds are s<=2a+4 and s'<=8-2a. At a=-2, s' can equal12; the candidate explicitly retains it. The primal endpoint -V obstruction then excludes both a=-2 pairs. Only afterward are both second quotients exact for the three terminal pairs.

The dual rank7 endpoints are classified by two Euler twists and bounded degree excess. The degree-32 cases can reach only a line and the backward flag equation forces7d7=10, impossible. In degree-36, rank-one branches force7d7=6; the remaining rank-two branch has defect<=5 and hence zero, and its rank5 kernel reaches only O. Its last quotient degree-2 gives an impossible invariant divisor of degree2. Endpoints are never presumed rank3.

The new separate direct22 proof is NOT used in this candidate or as a replacement for the original chain. The supporting reviewer explicitly audited the original enumeration domain/filter logic and compact certificate partitions without regenerating all2947 historical records; this review does not elevate that to an independent complete enumeration replay.

### (2,3)

Only Sections2–4 of the adjacent-profile note are needed. Forward length3 forces the unique Z source. The FULL derivative image has degree>=13: degree11 would inject14 sections into at most13, and determinant parity excludes12. All37 dual types divide into nonzero and zero quadratic sections. The nonzero branch treats both saturated rank2 images and all eight P4 quadratic types, including the two high-line types; the latter give6 sections into2. In the zero-quadratic branch, irreducibility rather than a false cubic-persistence assertion controls a nonzero restricted derivative. If it vanishes, the next dual derivative still injects T6 into the actual full envelope and forces an impossible high line. The note's later partial32 result is not substituted for complete32 closure.

### (3,1)

The rank3 plateau is F0<K2<K<E<F4 of ranks8,11,14,17,20. Dual cubic section injectivity makes the restricted cubic derivative nonzero, so ranks1,2,3 exhaust its possibilities. The rank3 branch keeps the full saturation distinct until its small defect is proved zero, forces actual generated quotients, and ends with a negative horizontal endpoint.

The rank2 branch has exactly five necessary (n,e) shapes: (4,2),(6,2),(8,2),(6,4),(8,4). The small, middle and last-low exclusions treat the first, fourth and fifth. The(6,2) reduction plus exclusion treats all eight kernel types, the three explicit next kernels and all four residual high-map kernels, including nonsplit extensions. The(8,2) reduction has20 types, partitioned into9 doubled and11 single W' cases. The two separate exclusion papers cover both sectors; the single sector explicitly treats a zero low scalar and verifies the high-core/low-zero condition where required.

The rank1 branch has seven e9 and three e11 shapes. The degree-eleven paper removes all e11 and four e9; the final paper treats exactly the remaining three e9 shapes. It retains both first-image defect0/12 possibilities, includes the empty negative tail, distinguishes upper quintic first-jet evaluation from lower Clebsch evaluation, and checks every endpoint descent.

In every terminal descent, the next target uses the ACTUAL quotient by the sheaf kernel. A nonzero map supported on a line has that line as its abstract image sheaf even when it has invariant zeros; replacing it by its saturation would change subsequent twists and is not done. After F0, only negativity/nonhorizontality and derived Hom bounds are used, not rank3. This closes all three nonzero cubic-image ranks under the same actual input, without needing a global rank4 premise.

### (3,2)

The primary four-source reduction gives a short complete cover, independent of the historical28-source closure bookkeeping:

- D is exactly the tuple in SINGLE-D5-TYPE-EXCLUDED-BY-BACKWARD-GAUSS.md. Pairing vanishes, and both restricted dual cubic-image ranks1 and2 are covered. The rank1 residual C0 is not presumed globally generated; its full ten-pair K/C0 overlist is constrained by source Hom and Euler identities before the next two derivative contradictions.
- P is the THIRD tuple called Z within each historical three-P4 paper, not the zero-quadratic source called Z in the new four-source notation. Both the zero-pairing and nonzero-pairing papers are required and retained. Together they cover every pairing branch for exactly that source.
- V is the exact single-V tuple. Both e2 and e4 branches are covered, with all four e2 extension/kernel alternatives and actual next-map surjectivity proved by complete evaluation or the invariant defect gap.
- Z is the zero-quadratic tuple under l2. The proof does not infer l3 from zero quadratic sections. Its cubic rank3 branch is contradicted without assuming the restricted image saturated. Rank2 leaves exactly(6,2),(8,2),(8,4), all treated.

The common endpoint proof transferred from the P paper depends only on the exact two quotients, the two Euler classes, plateau ranks and persistence, not on an actual P summand or nonzero pairing in E. Thus its D and Z uses are justified. It forces the rank8 degree-48 endpoint's smallest constant span to have dimension13 and requires104 in <96,160,240,60,100,150>, which is impossible. The independent controls also verify this last obstruction.

### (3,3)

The two cubic restrictions are section-injective. The pairing inequalities and full small-image list force ranks(a,b,t)=(3,2,2), then the actual cubic image O(7)+W' O(2). The potentially positive saturation defect12 in the last two dual types is retained: equality in the top-three degree bound would force the canonical top subbundle, whose projection to T6 O(4) vanishes. This contradicts the nonzero pairing and proves defect0. The exact full image then fixes K=(2V+2P4)O(-4); its next derivative would inject14 sections into11. Persistence gives the contradiction. No cubic/full-image identification was made before saturation was proved.

Every one of the nine ordered alternatives from Section2 is therefore covered by a theorem with matching actual premises.

## 5. Lower ranks are excluded independently

Generic rank0 makes the algebraic Grassmannian differential zero. In characteristic zero the classifying map is constant, forcing the saturated tautological E to have degree0, contrary to-54.

For generic rank1, no common constant subbundle and full constant span force the complete saturated flag in the actual N=30 ambient. The regular derivative line maps have effective ramification; eliminating the first line degree gives the universal bound degree E<=-r(N-r). At r=17 this is-221, incompatible with-54. The independent code checks every coefficient of the universal flag identity over all2<=N<=40 and all ranks, and verifies that every ramification coefficient has the correct nonpositive sign. It does not choose a ramification vector for an actual bundle.

For generic rank2, the complete endpoint-flag exclusion applies with the actual twist-one vanishing, even physical determinant degrees and orbit semigroup. The prior plateau/orbit theorem reduces to profiles11,12,21 in the RANK-TWO problem. These labels must not be confused with the rank-three profiles above. The endpoint proof treats nonorthogonal and orthogonal constant spans, retains projection torsion until the invariant degree gap removes it, and uses the actual twist-one cohomology character for the final contradictions. Nothing in the new theorem relies on rank-three profile coverage to eliminate ranks0,1,2.

Consequently all generic ranks0 through3 are impossible, leaving the integer interval4 through13. The controls reject omission of any lower-rank theorem even if all nine rank-three profiles remain present.

## 6. Actual bridge and generic-versus-special distinction

The relevant maps are the ACTUAL multiplication arrows

    A_l: M2,+ -> M3,-, injective, dimensions41 ->54,
    B_l: M3,- -> M4,+, surjective, dimensions54 ->37.

Thus ker B_l has dimension17 and coker A_l dimension13. The natural map ker B_l -> coker A_l is identified with the second fundamental form of E in H O, not merely with an abstract map having the same dimensions. In the local Koszul presentation the plane section class(k,zk) differentiates to(k',zk'+k), and the actual quotient sends[(x,y)] to[y-zx], yielding[k] modulo l M2,+. The cotangent and parameter-line factors are retained; their one-dimensional fibers do not affect ranks.

The exact comparison sequence then gives, for every parameter where those already-proved uniform linear maps are taken,

    dim ker(l^2) = 17 - rank SF_l,
    dim coker(l^2) = 13 - rank SF_l,
    rank(l^2) = 24 + rank SF_l.

The positive double-hyperplane section formula identifies its even section dimension with that kernel. The independent controls verify all these identities for every abstract possible SF rank0 through13 from both source and target dimensions.

The new exclusion theorem concerns the GENERIC rank r. A nonzero generic r-minor stays nonzero on a nonempty Zariski-open set; every(r+1)-minor is identically zero. Hence SF has rank exactly r there, and multiplication has rank24+r there. Since r>=4, the stated generic inequalities follow. They are NOT asserted at every special parameter. In particular r>=4 leaves a nine-rank gap to the sufficient r=13 surjectivity criterion.

The separate rank36 invariant-cone specialization is neither improved nor contradicted: this rank28 lower bound is on the different square specialization. No statement about a generic smooth quadric section count or a q0-centered obstruction coefficient follows merely from these inequalities.

## 7. Verifier audit and independent executable evidence

The candidate's verifier has explicit fail-closed exceptions, not Python assertions. The manifest and theorem-scope registry are hash-locked. It authenticates all52 direct inputs, requires the scope-matched proof lists, checks both ordered directions, lower0/1/2 prerequisites, both P pairing branches and the22/31 defect/branch conditions, and derives the numerical conclusions. Its typed comparison distinguishes booleans from integers. The 626 rejected mutations and2 order controls are finite contract regression tests, not geometric proof or historical enumeration.

I found no route by which ordinary acceptance silently upgrades a partial profile theorem to full coverage under the frozen registry. The registry itself contains mathematical scope judgments, which were independently checked in the preceding sections. Hash binding prevents an edited source or edited scope registry being accepted merely because its filename is unchanged. Authenticating supporting sources outside the42 explicit profile/lower entries is still required by the main52-entry manifest.

The separate independent control suite checks:

1. All seven target artifact hashes and all52 source identities.
2. Common actual ambient/degree/marking/image conventions and conditionality.
3. The20 rank-feasible plateaux and nine cubic-bounded ordered alternatives, with correct reversed dual orientation.
4. Actual cubic Euler characters derived from the W fusion graph and separate coefficient/ambient dimensions.
5. Exhaustion of the original28 source equations and their exact four primary refinements.
6. Universal complete-flag degree coefficients and the rank-one contradiction.
7. The distinct22 determinant caps, common32 semigroup obstruction, and profile21 endpoint capacities/full degree10 character.
8. Every required profile source chain, all lower ranks, and every exact square consequence.
9. Rejection of128 changes, including every removed profile or required proof source, dropped lower rank, lost P pairing branch, rank3 endpoint, erased second-dual defect12, missing single31 sector, swapped12/21, coefficient-space substitution, independent parameter rotation, horizontal splitting, dimension-only bridge, and generic-to-special/surjectivity/full-repair promotion.

Reproduce from the published candidate packet root, with this review subset stored in `independent/`:

    python3 independent/independent_controls.py .
    python3 -O independent/independent_controls.py .

Both standard outputs must match `independent/RESULT.json` byte-for-byte. The explicit first argument supplies the location of the unchanged candidate packet. The executable does not treat review verdict strings as mathematical proof.

## Final boundary

The conditional integration is accepted at the exact frozen target hashes. Its mathematical advance is the written combination of separately scoped actual exclusions into generic SF>=4 and the exact square-map consequences. Component audits and this review are supporting verification, not additional progress counted as new theorems. Any edit to the proof, source manifest or imported theorem bytes requires review of the change; these hashes do not certify later revisions.
