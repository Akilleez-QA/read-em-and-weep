# Independent whole-proof geometry review: conditional profile (1,1) closure

## Reviewed version and verdict

- Reviewed file: `PROOF.md` in this packet.
- Exact SHA256: `126fc2e7cbf54ae91f8e2eba3c0e809f70cf49c0f0aef28b574c5be3762ca6d2`.
- File size: 13,550 bytes.
- Review date: 2026-10-23 UTC.
- Verdict: **PASS, with the stated conditional scope. No blocking mathematical issue or correction was found.**

The proof establishes that the actual saturated inclusion cannot have generic Gauss rank three with maximal profile (1,1), assuming the pinned actual-input and original profile-specific necessity theorems. This is a genuine closure of that entire profile-specific branch, not merely a rejection of a later surviving ledger. It does not establish maximal-profile exhaustiveness or a global rank-three exclusion. The scope restrictions in Sections 1 and 6 are necessary and are respected throughout.

I read the complete main proof and all fourteen retained input files, including the original profile-specific theorem, its ordered JSON, and the original verifier as source code. I did not execute the original verifier or rerun its historical enumeration. I also read the production checker and character implementation, but did not use them or `RESULT.json` to derive the independent arithmetic checks described below.

The review covers the entire geometric chain, including the imported shape exclusions, rather than treating a checker count as a proof. The original necessity theorem and the deeper actual HM results invoked by the pinned inputs remain explicit theorem imports. This review does not claim to reconstruct every earlier HM/module theorem from first principles, nor does fourteen-file authentication by itself prove those foundational inputs.

## 1. Input identity and proof boundary

All fourteen retained files have the byte counts, SHA256 hashes, and Git blob SHA1 identifiers recorded in `INPUTS.json`. I checked these identities directly from the local bytes. Their manifest gives immutable full commit URLs. This review verifies those local identities; it does not claim a separate fresh network refetch.

The imported roles are correctly separated:

1. The ambient-Gauss and actual-splitting originals give the actual inclusion in the constant thirty-space, not merely the unrelated coefficient presentation. They supply ranks 17 and 13, both negative degrees -54, the group marking, and the plateau conventions.
2. The strict-top theorem concerns kernels of the actual constant-ambient second fundamental form. It requires no continued rank-three plateau assumption.
3. The original profile11 written theorem supplies necessity of the entire ordered 159-record overlist. The JSON alone would not supply that geometric implication.
4. PR1123 supplies four necessary actual E types independently of the later rank-three source ledger. PR1140 supplies coefficient-space cubic visibility for each of them.
5. PR1135, PR1142 and PR1145 are actual quotient-shape exclusions. Their complete proofs are present and their hypotheses match the current application.
6. PR1134 is not used to transport a profile21 assertion. The only needed iterated-section argument is rederived in Section 5 of the main proof and is independent of that profile.

The primal lower bound a >= -4 is properly identified as an imported all-profile theorem from PR674. That input itself uses an earlier all-profile a >= -8 result. This is a transparent transitive theorem dependency, not something certified by the present arithmetic checker. It does not invalidate the explicitly conditional closure.

## 2. Actual endpoint geometry, saturation, and termination

### Saturation

For a saturated subbundle F of the constant ambient, its second fundamental form is an O-linear map from F to a vector bundle. Its image is torsion-free and hence locally free on the smooth curve. Thus the kernel F-minus has locally free quotient in F. The exact sequence of ambient quotients then shows that F-minus is saturated in the original constant ambient as well.

This argument applies at every iteration, on either side. It does not require the image of a Gauss quotient in a later target bundle to be saturated. The main proof keeps those notions separate.

### Derivative injections

If F_j is the derivative kernel of F_(j-1), then differentiation of its local sections remains in F_(j-1) tensor Omega. Modulo F_j the derivative is O-linear: the extra term in differentiating a scalar multiple lies in F_j. Its kernel is exactly F_(j+1), because the inclusion of F_(j-1)/F_j into the original ambient quotient is injective. Therefore

    F_j/F_(j+1) -> (F_(j-1)/F_j)(-2)

is a genuine sheaf injection. Iteration yields the stated injection into C(-2j). It follows that the quotient ranks q_j are nonincreasing.

### Both endpoint ranks

The ranks of E and S are 17 and 13. Their original derivative ranks agree and equal three by negative transpose. Hence K and L have ranks 14 and 10 respectively.

At profile (1,1), K is the backward endpoint of the maximal primal rank-three plateau. Its derivative has rank at most three by the injection just proved. If it had rank three, its forward transform would have the rank of E and be saturated inside E, so the plateau would extend backward. Maximality excludes that. Thus rank beta_K <= 2.

The dual reversed plateau gives the same argument at L: a rank-three derivative there would extend the original forward plateau. Thus rank beta_L <= 2 as well. There is no assumption that an endpoint derivative still has rank three. Conversely, negativity ensures that a nonzero endpoint cannot have derivative rank zero.

### Termination

Every later F_j is a subbundle of the negative bundle E or S. It therefore has only negative splitting degrees. If a nonzero F_j were horizontal, its Grassmannian classifying map would have zero differential. Over C it would be constant, and saturation would make the subbundle a constant vector subbundle of degree zero. This contradicts negativity.

Every nonzero stage consequently loses positive rank. The chain ends at zero after finitely many stages, proving both the rank telescoping sum and the degree telescoping sum. No unproved infinite-descent or eventual-rank assertion is involved.

## 3. Capacity inequality and its orientation

For any rank-q sheaf injection G_j -> C(-2j), taking the top exterior power gives a nonzero map from the determinant line of G_j to a direct sum of line bundles. Its degree is at most the largest degree of a target summand. Therefore

    deg G_j <= lambda_1 + ... + lambda_q - 2j q.

This argument remains valid with torsion in the cokernel. It requires neither equality classification nor saturation of the image.

Since q_j is nonincreasing and takes values at most two, the heights h_1 and h_2 describe every possible rank pattern, including h_2 = 0. Summing the bound gives the capacity formula in the main proof. The two independent orientations are:

- primal: n = rank K = 14, C = A, deg K = -54-a;
- dual: n = rank L = 10, C = B, deg L = -54-b.

These have not been exchanged. The rank-14 side has heights 7 through 14, and the rank-10 side has heights 5 through 10. Both inequalities hold for the same actual pair A,B. They do not select different source witnesses. The universal capacity is a necessary upper bound even if a maximizing height is not geometrically realized; overestimating it only weakens the exclusion.

No argument in this section requires top(S) <= -2. The actual top(S) <= -1 is enough for negativity and termination. Equal degrees and tied optimizing heights cause no problem because this part of the proof only uses inequalities.

The primal-only exclusions deserve explicit mention. Original rows 32, 50 and 52 all have deg K = -52 but primal capacity -70. They are therefore excluded even though their dual capacities do not exclude them. This is precisely the contribution of retaining both endpoint orientations.

## 4. Actual source and cubic visibility conditions

The four source types each have rank 17 and degree -54. Every summand degree is at least -8. Global generation of E(8) passes to its actual quotient A(8), so every ordinary degree of A is at least -8.

Only E_D has a summand of degree at most -8, and it has exactly one such ordinary line. All higher summands have zero Hom to O(-8). Thus an O(-8) quotient forces E_D, and a quotient onto 2O(-8) is impossible: its only possible source has rank one. This is a simultaneous quotient-rank obstruction, not two unrelated tests for nonzero maps.

I checked PR1140's stronger cubic visibility argument. Its two important safeguards are correct:

- The actual top-row kernel has top at most -3 and rank at most dim(R)-1. Its cubic section dimension is therefore too small to kill the six-dimensional T6 constituent.
- If the displayed cubic T6 channel coincided with the top-row T6 channel, a bundle map from the cubic summand to the top block would cancel it. Its graph is a saturated direct summand with negative degree and complementary top at most -2. A killed graph would have internal derivative landing in degrees at most -4, so it would be horizontal, a contradiction.

This forces independent T6 channels, while the cubic W-prime channel survives by the same negative-graph argument. The conclusion is an injection of W-prime + 2T6 into H0(A(3)). It is not a fiberwise injection of a rank-fourteen bundle into a rank-three quotient. The main proof uses only the legitimate coefficient-space consequence.

## 5. Audit of the original 159-record necessity import

The original written theorem has the correct profile11 orientation and explicitly avoids the stronger profile12 dual-interior hypothesis. Its source cohomology and strict-top vanishings justify the endpoint envelopes for K and L without assuming either endpoint derivative has rank three.

The remaining necessary conditions have the indicated direction:

- Quotients E -> A and S -> B imply the stated H1 upper bounds.
- Negative transpose gives A -> B-star(-2) and B -> A-star(-2), together with their injections into Q(-2) and E-star(-2).
- The determinant length is t = -6-a-b, not a defect of a different later derivative.
- The invariant divisor possibilities up to degree 28 include 24 as twice the twelve-point orbit.
- Serre duality turns B(u) -> E-star(u-2) into the necessary inequality H0(B(u)) <= H1(E(-u)). The actual irreducibles are self-dual.
- The historical requirement that one actual E type satisfy the primal and dual finite cohomology tests is necessary. It is not a realization theorem, and the present proof does not use its compatible_E_types witnesses.

The center-even rank-three splitting classification is exhaustive: three even trivial lines, an odd W or W-prime block plus an even trivial line, or one even A_std or V block. The original degree and cohomology arguments supply finite bounds. Reading `original-verifier.py` confirms that its loops and filters implement those stated necessary conditions and preserve ordered A/B orientation. Its finite twist interval is correctly described as a necessary filter, not an all-twist sufficiency claim.

The original written necessity theorem is therefore being imported in the right direction: any actual profile11 configuration supplies one of the listed records. Rejection of every record then excludes that configuration. The proof never reverses necessity into occurrence.

## 6. Independent bounded arithmetic and exact residual coverage

I independently recomputed the required fixed-record character and capacity decisions. This was not a rerun of the historical enumeration: the input was exactly the 159 authenticated existing records, and no new hypothetical list was generated.

The character computation used the nine fixed conjugacy classes and exact arithmetic in Q(sqrt(5)). Symmetric characters were calculated from the closed polynomial

    chi(Sym^n)(x) = sum_k (-1)^k binomial(n-k,k) x^(n-2k),

rather than the production representation recurrence. I verified orthonormality of the nine physical irreducible characters. Only fixed symmetric degrees through 31 and the finite endpoint height values were used. Neither `characters.py` nor `RESULT.json` was imported or trusted.

The disjoint decision order independently returns:

- 56 source degree/multiplicity exclusions;
- 32 further cubic-visibility exclusions;
- 62 further dual-capacity exclusions;
- three further primal-capacity exclusions, exactly 32, 50, 52;
- six residual original indices, exactly 94, 95, 100, 106, 109, 127.

Their exact shapes and checks are:

| Original index | A | B | (a,b,t) | Cap_14(A) | Cap_10(B) |
|---|---|---|---|---:|---:|
| 94 | O(-8)+O(4)+O(6) | O(-8)+O(-6)+O(6) | (2,-8,0) | -42 | -42 |
| 95 | W O(5)+O(-8) | W O(-7)+O(6) | (2,-8,0) | -42 | -44 |
| 100 | O(-8)+O(4)+O(8) | O(-10)+O(-6)+O(6) | (4,-10,0) | -26 | -42 |
| 106 | O(-8)+O(4)+O(10) | O(-12)+O(-6)+O(6) | (6,-12,0) | -10 | -42 |
| 109 | W-prime O(-5)+O(16) | W-prime O(3)+O(-18) | (6,-12,0) | 20 | -30 |
| 127 | O(-8)+O(2)+O(16) | O(-18)+O(-4)+O(6) | (10,-16,0) | 38 | -38 |

All t values here are the original transpose defects. Their becoming zero after the necessary filters does not set any other map's determinant torsion to zero.

## 7. Review of all five imported residual shape exclusions

### Rows 94 and 95: PR1135

Projection to the negative O(-8) target is an isomorphism on the sole possible source O(-8). Its kernel therefore lies in E-hat, and E-hat maps onto the positive rank-two quotient. This cancellation does not assume a horizontal Birkhoff splitting.

For O(4)+O(6), the D row to O(4) vanishes by character, and the nonzero row to O(6) is basepoint-free: an invariant common-zero divisor has degree at most eight, below the minimum nonempty invariant orbit degree twelve. Its kernel rank and degree force both the cubic S4 and T6 channels to survive.

For W O(5), a rank-one D image would have to be O(2), but its equivariant Hom into W O(5) vanishes. The actual rank-two image is globally generated after twisting by two and has at least five sections. Its invariant torsion defect is at most eleven and hence zero. Kernel rank then forces both cubic constituents to survive.

In both cases, graph cancellation makes the displayed cubic T6 channel independent and retains W-prime. The resulting cubic section isomorphism forces K to be entirely of degree -4. Euler characters identify its coefficient representation as 2V+2P. Strict-top injects this into H0(A(2)) = V+2P+D, contradicting the V multiplicity. The actual V(-4) source rows are retained; there is no discarded negative tail or fiber-rank inference from section injectivity.

### Rows 100 and 106: PR1142

The complete cubic-kernel alternative is either zero or S4. In the latter case the actual D-row kernel has rank four and four sections after twisting by three. Its nonpositive splitting forces S4 O(-3), so its coherent image is the genuine line O(2), even if this image is not saturated in A.

Both residual A shapes have zero equivariant Hom from O(2). Thus their cubic kernel vanishes, K has top at most -4, and strict-top gives the sharper injection H0(K(4)) -> H0(A(2)). The resulting fourth-twist Euler envelope has V coefficient -1 in each case. The O(-8) tail is correctly retained through H1 in the Euler character. This proof needs no hypothesis on the derivative rank of K.

### Row 127: PR1145

I checked the entire equality-case geometry, including its positive-defect companion row 119. The latter has deg L = -26 while its capacity is -50, so it is excluded independently. For row 127, deg L = -38 equals the dual capacity, and the only heights are (7,3) and (8,2).

Because the degrees 6,-4,-18 are distinct, equality of each determinant bound identifies the actual composite image with the top one or two summands. Lower wedge components vanish by degree, the top determinant has no zeros, and generic image containment extends across the curve. This justifies the nonzero leading derivative channels; it is not an arbitrary splitting of the connection.

At height eight, the final O(-10) line has at least nine independent osculating directions. Every proper equivariant quotient of Sym10 W = A_std+V+D has dimension at most eight, so its coefficient system is full. Its rank-nine osculating subbundle has apolar annihilator W O(-9). E has no maps to this bundle by degree. A nonzero constant subspace would then lie in S, contradicting H0(S)=0. Only top(S) <= -1 is used.

At height seven, the final O(-8) line has full Sym8 W = P+D coefficient system. The projection of E into the resulting constant nine-space factors through its apolar O(-8) line, and only the actual source O(-8) can supply it. The scalar is nonzero. The coefficient image of that source line then gives a genuine constant complement, proving the constant splitting H = N + C_9 and E = F + J. This is stronger than, and not inferred from, an ordinary Birkhoff splitting.

The residual inclusion has rank F=16 in dim N=21, and its dual bundle has rank five and degree -46. Block-diagonal differentiation gives the residual endpoint rank bound one. Its three successive line quotient degree bounds sum to exactly -24, forcing a final O(-10) line and four independent derivative directions.

The proof correctly allows its degree-ten coefficient quotient to be partial. Dualizing that quotient embeds its dual into the full Sym10 space, where apolarity forces the projection of F to factor through (V+P)O(-4). Degree kills all source blocks except V(-4), and the remaining scalar cannot vanish because S has no constants.

The sextic-net lemma then forces fullness: the three-dimensional V in Sym6 W has no common divisor by the minimum invariant orbit size; its rank-two syzygy splitting has positive indices summing to six and hence each at most five. After twisting by four, H1 vanishes, so V tensor Sym4 W surjects onto Sym10 W. Consequently the residual coefficient space has dimension eleven. The rank-thirteen high-degree source block would inject into the constant kernel of dimension ten, which is impossible.

This closes the difficult height-seven case without assuming completeness prematurely, importing the stronger profile21 dual bound, or assigning a horizontal connection to a Birkhoff complement.

## 8. Row 109: forced source and twist-ten deficit

The quotient W-prime O(-5) rules out E_V and E_Z by degree. In E_D only O(-8) could contribute, but Hom_G(O(-8),W-prime O(-5)) is zero because Sym3 W = S4 does not contain W-prime. Thus E_P is the actual source. No existential source witness is chosen from the historical JSON.

For its successive actual kernels, strict-top gives top(F_i) <= -2-i. Therefore H0(F_9(10)) = 0. Telescoping the nine short exact sequences, followed by the actual quotient injections J_i -> A(-2i), proves

    H0(E(10)) <= sum_(i=0)^8 H0(A(10-2i))

coefficientwise. This remains true if the chain reaches zero earlier. It is a representation inequality obtained from exact sequences and semisimplicity, not an asserted map of the original bundles into a rank-incompatible target.

The source has exactly four trivial constituents: one each from P tensor Sym8, W-prime tensor Sym7, T6 tensor Sym7, and V tensor Sym6. The additional W-prime tensor Sym5 contributes none.

The W-prime target part has symmetric indices 5,3,1, with W-prime multiplicities 0,0,0. The scalar part has indices 26,24,22,20,18,16,14,12,10, with trivial multiplicities 0,1,0,1,0,0,0,1,0. I independently checked these fixed values. Thus the target has three invariants, contradicting the four in the source. No profile21 premise enters this argument.

## 9. Final issues and authorized scope

No blocking issue was found. No correction to the reviewed proof is required for its conditional profile11 theorem.

The claim must remain conditional on the actual-input and original necessity theorems. In particular the original maximal-profile exhaustiveness question is not resolved by this packet. Separate exclusions of profiles (1,2) and (2,1) do not make the three labels exhaustive. No global COV, rank-four theorem, maximal rank, smoothing, algebraicity, or original-theorem repair follows from this review.

No selected actual HM/source coefficient, parameter, point, jet, matrix, tensor, source-instance rank, scan, or large computation was evaluated. No public files were written or modified. The only write from this review is this local review document.
