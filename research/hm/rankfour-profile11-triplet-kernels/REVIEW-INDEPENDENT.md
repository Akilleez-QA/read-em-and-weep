# Independent whole-proof review: triplet kernels and two positive images

## Verdict

**ACCEPT, conditional on the actual geometric inputs explicitly imported in the statement.** I found no material mathematical gap in the five necessary kernel alternatives, the full coherent-image assertion for K1 and K2, or the ensuing actual equalities K^+=E0 and E0^-=K. The claims do not use a zero-original-defect assertion or a rank-seventeen rank-three classification. They do not establish existence or exclude any of the five displayed alternatives.

This review is bound to the following exact bytes:

| File under `rankfour-profile11-triplet-kernels/` | SHA-256 |
| --- | --- |
| `PROOF.md` | `4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a` |
| `inputs/low-top.md` | `c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af` |
| `inputs/top-four.md` | `56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0` |

I read both supplied input proofs in full. The input labels identify PR1185 and PR1194; this review verifies the retained mathematical texts and the hashes above, not a fresh remote Git-provenance lookup. Their own transitive actual-source and physical-line hypotheses remain imports, exactly as the proposed theorem says.

## Independent reproducible arithmetic

Run:

    python verify-independent.py

Result: **PASS, 1,291 exact assertions.** Normal Python and `python -O` produce byte-identical results. The saved results are `VERIFY-INDEPENDENT.json` and `VERIFY-INDEPENDENT-OPT.json` beside this review. The packaged checker locates the proof and inputs relative to its own resolved directory, so the packet is portable and independent of the current working directory. The script is independent of the author's `characters.py`: it imports none of that file, uses an explicit nine-row character table with class sizes, checks character orthogonality and the sum of squared dimensions, and decomposes products by exact class inner products over Q(sqrt(5)). Symmetric powers are evaluated using the determinant-one trace recurrence rather than the author's McKay adjacency implementation.

It inspects only individual fixed universal atoms R(-j), for the nine physical irreducibles and 5<=j<=14, with the relevant six- or ten-dimensional budget. It does not construct or enumerate kernel tuples, height configurations, actual coefficients, points, jets, tensors, matrices, or instance ranks. The endpoint inequality is checked symbolically via the parity of h1+h2=11.

## 1. Imported actual geometry and coefficient gates

The ambient is the original saturated inclusion E in a constant rank-thirty bundle over the physical P(W*) in characteristic zero, with the fixed SL2 determinant convention. This matters in four places: the actual derivative is the second fundamental form for the constant connection; Omega^1 is O(-2) with the intended equivariance; saturated derivative kernels remain saturated in the same constant ambient; and a saturated horizontal subbundle is constant.

The imported hypotheses provide rank(E)=17, degree(E)=-54, the four actual source types, the two section gates, the cubic alternatives, top(K)<=-3, and endpoint derivative rank at most three under the maximal ordered plateau (1,1). These are not inferred from an ordinary Birkhoff splitting alone.

For the particular quotient A_std(4)+O(-8), the first two section gates do hold: H0 is A_std+V+P+D and its twist-one H0 is W'+S4+2T6. The source-D conclusion is justified by the actual negative quotient projection: all source Hom spaces into O(-8) vanish except the unique source O(-8) row of E_D. The source, quotient, and kernel rank/degree arithmetic is (17,-54), (4,4), and (13,-58).

Nothing in these deductions uses saturation of the original transposed image A_q -> Q(-2), nor sets the determinant defect to zero. A coherent injection suffices for the section gates.

## 2. Near-top injection is an actual-map argument

For an equivariant ordinary splitting K=R3(-3)+R4(-4)+N, with top(N)<=-5, the second fundamental form of K lands in A_q(-2) because K=E^-.

If a coefficient of R4 is killed by the induced coefficient map, its associated direct line O(-4) is killed by the map to A_q(-2). Its own derivative modulo that line then factors through (K/O(-4))(-2), whose top degree is at most -5. There is no nonzero ordinary Hom from O(-4) to that target. The line is saturated in K, in E, and in the original constant ambient, so this would be a negative horizontal line, a contradiction.

The chosen coefficient line need not be G-invariant for the horizontal contradiction. The full coefficient map is equivariant, which subsequently permits the representation-multiplicity obstruction. This proves exactly the R4 injection used in the proof; it does not inject all H0(K(4)) and does not require a horizontal Birkhoff splitting.

## 3. Kernel cohomology and complete individual atoms

Equivariant Euler additivity gives chi(K(3))=-T6 and chi(K(4))=V+P. Consequently

    H1(N(3))=R3+T6,
    R4=V+P-R3 tensor W+H1(N(4)).

Serre duality introduces no missing determinant character: the determinant convention is trivial and the relevant SL2(F5) representations are self-dual. For R(-j), the two H1 terms are R tensor Sym^(j-5) W and R tensor Sym^(j-6) W, with a negative symmetric index giving zero. The first has dimension (j-4)dim(R). Positivity of every individual contribution justifies both the dimension bound and testing containment in the prescribed representation budget.

For budget T6, the exact complete atom list is the four stated atoms T6(-5), V(-6), W'(-7), O(-10). Irreducibility of the total budget forces one atom, not an unexamined sum. The V(-6) choice produces R4=2V+P, which cannot inject into V+2P+2D. The other three choices give exactly K1, K2, K3.

For budget S4+T6, the checker reproduces all ten stated atoms, with both H1 representations exactly as printed. The equation for R4 requires H1(N(4)) to supply A_std and D. Among all individual atoms, only O(-8) and W(-9) supply A_std. The W(-9) atom consumes the whole budget and gives K4. O(-8) consumes S4, leaving the irreducible T6 budget; its unique D-supplying atom is O(-10), giving K5. This is a structural budget argument, not a tuple search.

All five resulting splittings have rank thirteen, degree -58, cubic Euler character -T6, and quartic Euler character V+P. The wording “five necessary alternatives” is appropriately conditional and does not assert their realization.

## 4. Nonzero V row, rank one, and absence of base divisors

Each surviving splitting contains an actual chosen V(-4) summand in R4. The near-top coefficient injection makes its derivative row nonzero. Its component in O(-10) vanishes by ordinary degree, so it maps into A_std(2).

The determinant-compatible binary evaluation sequence

    0 -> W(1) -> A_std(2) -> O(4) -> 0

is exact as an equivariant sequence. The V-row composition with O(4) lies in Hom_G(V,Sym8 W), which vanishes because Sym8 W=P+D. Thus the actual row factors through this fixed W(1) subbundle.

If its generic rank were one, its saturation in W(1) would be a G-equivariant line. Since G is perfect, equivariant linearisations of an ordinary O(e) do not acquire a nontrivial character. The center-even target gives even e, and its ordinary top degree gives e<=1, hence e<=0. Every Hom_G(V,Sym^(e+4) W) vanishes for such e; negative symmetric indices give zero, and degrees zero through four contain no V. Factoring the row through its saturated line therefore contradicts nonzero rank one. The saturation is used only for this argument, not substituted for the actual image in the theorem.

At generic rank two, the maximal minors are sections of O(10): det(W(1)) has degree two and each pair of source lines contributes degree -8. Their common vanishing divisor is G-invariant because the map is equivariant and the determinantal ideal is invariant. At least one minor is nonzero, so the common divisor has degree at most ten.

A point stabilizer in a finite group of complex projective-line automorphisms is cyclic. The effective projective action is A5, whose cyclic subgroups have order at most five. Hence every orbit has size at least 60/5=12. Any nonzero effective invariant divisor has degree at least twelve. The common divisor is empty, so the V-row is everywhere surjective onto W(1), not merely generically rank two. This proves actual coherent-image containment of W(1) in beta_K.

Optional simplification, not a correction: even the degree-one possibility in the saturated-line argument would be excluded because Sym5 W=T6 also contains no V. The existing parity argument is valid.

## 5. Full coherent image for K1 and K2

Every summand of K1 and K2 has degree greater than -10, so the whole derivative has zero O(-10) component. Its image lies in A_std(2) and already contains the entire W(1) subbundle.

The remaining composition to O(4) has exactly the rows considered in the proof. Each P(-4) row has polynomial degree eight; the T6(-5) row has degree nine. Every nonzero such equivariant row is everywhere surjective onto O(4), because its common divisor is invariant and has degree less than twelve. The W'(-7) row has zero Hom into O(4), since Sym11 W=W+S4+T6 has no W'. The V row has already been shown zero in this quotient.

If any remaining scalar-quotient row is nonzero, the image contains ker(A_std(2)->O(4)) and surjects onto O(4). Stalkwise exactness then makes the coherent image all of A_std(2); this conclusion does not merely identify its saturation.

If the composition were identically zero, the coherent image would be exactly W(1), already obtained from the V row. Thus F=K^- would have actual rank eleven and degree -60, with the actual quotient K/F=W(1). K is negative and saturated in the original constant ambient, so the imported terminating derivative-kernel filtration applies to K itself. Its graded coherent-image injections land successively in W(1-2j), and its rank drops have at most two columns.

For their ordered heights h1>=h2>=0 with h1+h2=11, the capacity is

    deg(F) <= h1+h2-h1(h1+1)-h2(h2+1)
           = -h1^2-h2^2 <= -61.

Indeed (h1-h2)^2>=1 because the sum is odd, so h1^2+h2^2=(121+(h1-h2)^2)/2>=61. This is a uniform inequality for every allowed height, not a height scan. It contradicts degree(F)=-60. It uses the correct actual rank eleven; neither rank thirteen nor a substituted rank-three classification appears.

Consequently the full coherent image is A_std(2) for K1 and K2. Its rank is three and degree six, so K^- has rank ten and degree -64.

## 6. Actual endpoint equalities

The negative quotient component E -> O(-8) is the nonzero scalar on the unique source O(-8). Thus its kernel is precisely the displayed actual summand E0, and K is contained in E0. Surjectivity of the actual quotient gives E0/K=A_std(4).

For K1 and K2, the established derivative image A_std(2), after tensoring by T_P1, is the full positive quotient A_std(4). The derivative span of K therefore fills E0 modulo K and has no negative quotient component. Since E0 is saturated in E and the original ambient, the actual saturated derivative span is exactly K^+=E0.

Every section of K has derivative in E0 by this image calculation, giving K subset E0^-. Conversely, a section of E0 whose derivative remains in E0 also has derivative in E, and therefore lies in E^-=K. Hence E0^-=K as actual subbundles. Its rank and degree are sixteen and -46; its derivative rank is sixteen minus thirteen, namely three.

These are relations among actual maps and subbundles. No ordinary summand of E has been declared horizontal or connection-compatible.

## Boundary

The proof intentionally leaves K3, K4, K5 and the actual triplet quotient unresolved. The full-image argument is not extended to them: their deeper tails permit additional degree/Hom behavior not analyzed here. The five-alternative reduction and the K1/K2 full-image result are correct under the stated imports. No public write, merge, submission, or upstream operation was performed during this review.
