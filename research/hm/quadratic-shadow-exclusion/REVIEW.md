# Independent mathematical review

Reviewed PROOF.md with SHA-256 f8214c36c5ba583e2138d910736495a366ff9f22aab7a0e54d1b3954b7a83040.

Verdict: the exclusion of the twenty-five-dimensional cubic ghost is valid, conditional on the pinned earlier structural results. The remaining alternatives are zero and fifteen; equivalently the actual J_5 Tor-channel scalar is nonzero. No value or nonvanishing of the U' scalar is inferred.

## Checks performed

1. Actual generation of H_j=H^2(B(j-5)) through degree three uses three separately established multiplication maps. The bottom map is the transpose, with multiplication curried, of PR476's actual endpoint evaluation and is an isomorphism. PR467 supplies nonvanishing and irreducibility for the next surjection. PR469 supplies the middle surjection. Thus there are exactly ten quadratic relations and fifty cubic relations before quotienting by linear products.

2. In the coordinate Koszul hypercohomology spectral sequence for B(2), the relevant E_2 positions are (-4,2) and (-2,1). The former has no possible incoming higher differential. Its only possible outgoing differential other than d_2 has target H^0(B(1))=0. The latter has no other incoming differential because H^3(B(-3))=0 and the complex ends at -5; its outgoing d_2 has target H^0(B(2))=0. The explicit Riemann–Roch audit in the proof establishes both positive-twist H^0 vanishings without incorrectly appealing to stability alone. The zero abutment therefore makes d_2 an isomorphism.

3. The Serre pairing H_j tensor H_(5-j) -> C and complementary exterior pairing give the total Koszul degree shift ten. Hence Tor_4(H,C)_7 is dual to Tor_1(H,C)_3, up to the harmless determinant line. This yields r=50-dim(T R_2).

4. The ten lex quadrics in one free component have cubic shadow 28. Independently, the same bound follows by taking initial monomials, splitting their counts between the two free components, and applying ordinary Macaulay shadow bounds to each. For a quadratic count a from zero through ten the minimum shadows are 0,5,9,12,14,15,19,22,24,25,28; the sum for a and 10-a is at least 28. This checks the module comparison without any generic-rank assumption or rank-adjusted persistence argument. Consequently r<=22, excluding 25 from PR478's alternatives.

5. The added character-theoretic proof also checks. The actual quadratic relation space is A* tensor W', and its linear products lie in A tensor (R_6 direct-sum 1 direct-sum U'), with no J_5 channel. At the adjacent spectral positions (-3,2) and (-1,1), the only other possible differentials are killed respectively by H^3(B(-3)), H^0(B(2)), H^3(B(-2)), and H^4(B(-3)), all zero by the stated inputs. Thus Tor_1(K,C)_3 is dual to Tor_2(H,C)_3. The latter is a subspace of the linear products of quadratic relations, so its missing J_5 channel independently excludes the twenty-five-dimensional ghost. No scalar is assumed nonzero merely because a Hom space exists.

This review checks the new derivation and its use of the cited dependencies; it is not a fresh proof of every earlier HM input and is not formal proof-assistant verification. No selected HM/source coefficients, numerical matrices, fixed-form ranks, generator searches or large computations were used. The original fixed-pair quotients, selected-source membership, first-order sufficiency, higher-order lifting and algebraicity remain unresolved as stated.
