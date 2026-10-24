# Independent whole-proof review

## Verdict and reviewed object

PASS relative to the stated actual-geometric inputs. No substantive gap found in the symbolic fourteen-shape derivation, three capacity exclusions, uniform quartic V-visibility lemma, four subsequent exclusions, the two dual-sign cuts, both actual-kernel exclusions, or the final three-shape necessary conclusion.

Reviewed final `PROOF.md` SHA256:

    56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0

## Source authentication and actual premises

I read all four complete source texts in `inputs/`, the classification notes, and the complete final proof. I independently fetched all four files through the GitHub connector at their full immutable commits. The fresh content equals each retained local file byte-for-byte, and all four commit/path URLs, Git blob identities, byte lengths, and SHA256 values agree with `INPUTS.json`. Details are in `REVIEW-AUTHENTICITY.json`.

The proof imports rather than purports to reconstruct the following actual prerequisites: the original saturated inclusion in the 30-dimensional constant ambient, the exact dual presentation, the four necessary sources, the actual two-cubic-channel theorem, and the maximal-(1,1) endpoint rank/capacity construction. The final prose makes these imports explicit. The negative-minimum conclusion is used from the general portion of low-top Section 2, not its later contradictory low-top hypothesis. The -8 lower bound follows independently from global generation of E(8) and its actual quotient.

This authentication is not an independent re-proof of every transitive HM premise. Neither my arithmetic verifier nor the author's verifier is a proof-assistant certificate of those premises.

## Section-by-section logical review

1. **Section gates.** Dualizing the exact locally free S presentation, and then twisting, gives the displayed exact Q(-2) presentation. Its cohomology really yields H0(Q(-2))=M2 and H0(Q(-1))=M3. The actual coherent injection of A_q into Q(-2) is enough to inject these section spaces. No saturated image or determinant-defect equality is needed.

2. **Rank and parity exhaustion.** An even top degree permits only even irreducible coefficient representations. A rank-four top irreducible fills the quotient and contradicts the negative minimum. A rank-three top leaves one scalar; V(4), unlike A_std(4), is removed by the forbidden W at twist one. In the scalar-top case, the remaining rank three has exactly the stated irreducible dimension partitions. The scalar 0 and repeated scalar 2 exclusions, the W(1) and W(-1) exclusions, the fixed negative-source Hom tests, and the two cubic T copies give precisely T and C1 through C13. This is a symbolic exhaustion, not a reconstruction from a candidate search. Merely nonzero source Hom is never promoted to simultaneous surjectivity.

3. **Negative source projections.** A quotient onto any direct target summand must be surjective onto that summand. The only source of O(-8) is the single scalar row in E_D. Its rank-one supply rules out two such target scalars, and also rules out the W(-7) projection. The remaining vanishing/forcing assertions in Section 2 hold with the specified physical marking.

4. **Capacity.** The imported capacity applies to actual saturated successive derivative kernels and coherent-image injections. The displayed square completion is an identity on sum h_i=13. Its center lies on that plane and is the continuous maximum there. Taking the floor gives a valid integer upper bound even before ordering or nonnegativity restrictions are imposed. Each printed height triple is ordered, nonnegative, sums to thirteen, and attains that floor. Thus every capacity stated is exact, and C1, C4, C12 are precisely the exclusions under this test. The contradiction needs only the upper bound, not the equality witnesses.

5. **Quartic visibility, especially source V.** Let C be the full displayed quartic V block. If H0(A_q(4)) has no V, equivariance kills the actual quotient row on C. Only then does beta_E kill C and force C's own second fundamental form into (E/C)(-2). In sources D and P, the sole degree-accessible target coefficients are D and P, neither V; in source Z there is no degree-accessible target. Consequently C is horizontal in those three cases.

   In source V, the only accessible internal target is V(-4), so the internal derivative is a constant equivariant map 2V to V. Its coefficient kernel contains V (or is all 2V). A coefficient kernel subbundle U(-4) is saturated in C, E, and the constant ambient. Its derivative modulo C vanishes. Its remaining second fundamental form lands in (C/U(-4))(-2), of degree -6 when nonzero, and hence vanishes by degree. This is the indispensable second step: zero derivative modulo C is not silently equated with horizontality. The resulting saturated negative horizontal subbundle contradicts constancy of its Grassmannian map over C. Thus V occurs in H0(A_q(4)). Semisimplicity turns occurrence into a coefficient-representation injection.

6. **Four cuts and seven intermediate survivors.** The four listed quartic characters have zero V; all seven final characters have positive V. The source restrictions on scalar and doublet tails remain intact. This intermediate list is explicitly necessary only, not a realization theorem, assertion of compatibility for every source, or profile closure.

7. **Two all-defect dual cuts.** The actual coherent transpose injection bounds top B by -2-v. Rank-nine endpoint capacity then gives b>=9v; with a+b=-8-t this is a+9v<=-8-t. C8 and C9 have left sides -5 and -3, respectively, and hence fail for every t>=0. This uses no equality-case or saturation assumption.

8. **The derivative coefficient facts for K.** K is saturated in E and the constant ambient, and top K<=-3 by strict top. For a chosen splitting K=R3(-3)+R4(-4)+N, a killed coefficient line in either displayed block is saturated in K. Its own derivative lands in (K/line)(-2), of top at most -5, so it vanishes by degree. The resulting negative horizontal line is impossible. This proves the coefficient injections R3 into H0(A_q(1)) and R4 into H0(A_q(2)); it does not assert that all H0(K(4)) injects.

9. **C10: O(4)+O(2)+W'(-3).** The actual Euler characters are chi K(3)=-W' and chi K(4)=2V+D for every source. The derivative target S4+T6 excludes the cubic W' kernel alternative, leaving R3=0 or S4. If R3=0, H1(N(3))=W' forces N=W'(-5), so R4=2V+D. If R3=S4, the only allowed tail atoms under the six-dimensional genuine budget are W'(-5), S4(-5), and O(-8). Their two possible complete tails give R4=2V-A_std or 2V. The first is nongenuine. The other two genuine cases each require two V copies in a target V+P+D with only one. This excludes C10.

10. **C7: O(4)+W'(3)+O(-8).** The source is D. A cubic S4 kernel can map into the source only through D(-2), with a one-dimensional equivariant Hom space. The canonical evaluation sequence identifies that image with the kernel of D(-2) onto O(2). Consequently the actual D-row would factor through O(2); all three quotient component Hom spaces from O(2) vanish, contradicting strict top. Thus R3=0. Here the O(-8) tail is correctly accounted for in Euler characteristic, not discarded by substituting H0: chi K(3)=-W-W' and chi K(4)=2V+P-1. The only tails with H1(N(3))=W+W' are W(-5)+W'(-5) or O(-6)+W'(-5). They give nongenuine R4=2V+P-1 or genuine R4=2V+P. The latter cannot inject into A_std+D+V+2P, which has only one V.

11. **Atom exhaustion and final scope.** For an atom R(-j), j>=5, the twist-three H1 contribution has dimension (j-4)dim R. Dimension and central parity alone restrict a six-dimensional budget to j=5 with W,W',S4,T6; j=6 with 1,A_std,V; j=7 with W,W'; j=8 with 1; or j=10 with 1. The forbidden constituent test leaves exactly the three stated atoms. For a four-dimensional budget, the only candidates are W,W',S4 at j=5, or 1 at j=6,8; the target excludes S4. These are fixed individual-atom tests, not a kernel-bundle search. The final forms T,C2,C6 all contain O(-8), so each forces source D. Their quotient degrees 4,2,2 and kernel degrees -58,-56,-56 agree. The three forms are left open, not asserted realized or excluded.

## Hidden-assumption audit

- The source splitting is used only as an ordinary equivariant bundle splitting. No summand is assumed horizontal.
- A vanishing quotient row is distinguished from a vanishing actual derivative. The proof calculates the possible internal derivative and, in source V, its residual derivative.
- Saturation is used only where proved: a direct summand of E is saturated in E and hence in the original constant ambient; coefficient subspaces of an equal-degree block are likewise saturated. The derivative image in Q(-2) is not made saturated.
- No connection or flat quotient on E/K is introduced. No splitting of the ambient connection is assumed.
- The argument does not replace A_q by a cohomological presentation, and does not interchange the actual 30-dimensional Gauss ambient with the 54-dimensional coefficient presentation.
- No zero-defect, equality-of-degrees, unproved exactness of a projected source row, or surjectivity inferred from nonzero Hom appears.
- The local quartic consequence extends the established negative-horizontal/near-top mechanism by examining the possible degree-minus-two top target. The final prose appropriately attributes the underlying mechanism and does not establish or claim historical priority for that method.

## Independent arithmetic verification

`review_verify.py` is independent of `characters.py` and `verify.py`. It uses the nine conjugacy classes, exact Q(sqrt(5)) arithmetic, and the closed Chebyshev polynomial formula

    Sym_n(x) = sum_{k=0}^{floor(n/2)} (-1)^k binomial(n-k,k) x^(n-2k).

It does not use the author's McKay recurrence. It checks orthonormality and physical representation dimensions/marking, the fixed small tensor products, fixed source-Hom calculations, the fourteen already symbolically derived shapes, all initial coefficient gates, the square-completion certificates, the sole possible internal-derivative target, all quartic characters, the two dual-sign cuts, the fixed dimension-at-most-six H1 atoms, exact kernel Euler calculations, and both actual-kernel exclusions. It also pins the exact reviewed final proof SHA256 and refuses to certify changed prose. It contains no global bundle generator, height scan, historical record enumeration, or actual HM map/coefficient/parameter/point/jet/tensor/matrix/rank evaluation.

Both normal and optimized runs pass 3,591 explicit checks, with byte-identical output. No `assert` statement is used, so optimization does not discard checks. Files:

- `REVIEW-RESULT.json`
- `REVIEW-RESULT-OPTIMIZED.json`

Their common SHA256 is:

    e8247acea866affc4d8afac3acf3f19f71f47e1d11d7d928054e2f7efe738a45

The independent verifier SHA256 is:

    23cdee0bc8880698aaebf16264e1ea0cbd51603e0d9748e73a3316a50b873626

I also ran the author's 281-check verifier normally and optimized, obtaining identical output, then compared every normalized arithmetic record with the independent output. All fourteen block lists, quotient degrees, kernel degrees, capacities, and quartic characters agree. The two sign-cut labels, two kernel-cut labels, and final three labels also agree.

Reproduce from this directory:

    python review_verify.py > REVIEW-RESULT.json
    python -O review_verify.py > REVIEW-RESULT-OPTIMIZED.json
    cmp REVIEW-RESULT.json REVIEW-RESULT-OPTIMIZED.json

## Contribution and remaining scope

The reviewed result establishes the uniform actual-source coefficient requirement V in H0(A_q(4)) and, on the maximal-(1,1), rank-four, top-degree-four locus, reduces fourteen symbolically necessary shapes to three source-D forms after three capacity, four quartic, two dual-sign, and two actual-kernel exclusions. This leaves three open necessary configurations. The final result needs no additional source theorem beyond the four authenticated originals; the relevant near-top coefficient injection is reproved in the final text. It does not eliminate the whole locus, change a global rank bound, prove realization, settle higher top degrees, or repair the original theorem.

All work for this review was read-only on GitHub and local to the shared cloud workspace. No public write, PR, merge, or upstream submission was made.
