# Independent audit: exceptional-channel axis exhaustion

## Verdict and scope

The proof is correct conditional on the explicitly stated canonical endpoint interface of PR661–663. I independently read the three supplied proof artifacts and checked their precise uses. No actual HM endpoint coefficients, source-instance matrices, or ranks were evaluated. The final bound of 21 is correct, including the liaison argument. The original bounds of 25 and 24 are retained below as independently checked intermediate steps; Section 6 records the final strengthened result.

## 1. Scheme-theoretic fixed-channel bound

A row of the quadratic map together with the three linear rows of L has five maximal minors, all of degree five. Across four rows this gives twenty quintics. Because L is surjective at every point, locally a pivot minor is a unit and Gaussian elimination changes L into [I_3 0]. For each appended row its last two entries are exactly its restriction to the local kernel frame. Two maximal minors recover those entries up to units, and all other maximal minors lie in their ideal. Row and column operations used here preserve the relevant ideals, so the twenty global quintics generate the ideal sheaf of the zero scheme Z_q, not only its radical.

The local row normalizations are legitimate despite the different global degrees: all bundles have first been trivialized locally. The global determinants still have degree 1+1+1+2=5.

Every zero of a nonzero fixed channel lies in the finite rank-drop support of E. Consequently the generated linear series has no fixed curve. Pick a nonzero member F, then choose H outside the finitely many proper subspaces defined by divisibility by an irreducible factor of F. The complete intersection V(F,H) has length 25 and contains Z_q scheme-theoretically. This proves length(Z_q) ≤ 25, including nonreduced structure.

## 2. Strict improvement to 24

Suppose equality holds. The closed inclusion Z_q ⊂ V(F,H) between schemes of equal finite length is equality. Hence Z_q is a (5,5) complete intersection. Its Koszul resolution is

0 → O(-10) → O(-5)^2 → I_Z → 0.

Twisting by five and taking global sections gives dim H^0(I_Z(5))=2, since H^0(O(-5))=H^1(O(-5))=0 on P². Equivariance of the fixed channel makes its zero scheme A5-invariant, so this is an A5-stable two-dimensional subspace of H^0(O(5)).

Every complex two-dimensional representation of A5 is trivial. For an elementary argument, a nontrivial representation would be faithful by simplicity. Its determinant is trivial because A5 has no nontrivial abelian quotient. A nonidentity involution in SL2(C) must be -I, which contradicts faithfulness because A5 has fifteen distinct involutions. Complete reducibility, or the same argument applied to the whole representation, excludes any nontrivial two-dimensional action.

There are no A5-invariant quintics on A. Here is a proof avoiding the invariant-ring classification. The invariant square conic C has an invariant equation c of degree two and is equivariantly P(W). Every A5 orbit on C has at least twelve points by PR661's cyclic-stabilizer argument. A nonzero invariant degree-five homogeneous polynomial with nonzero restriction to C would define an invariant effective divisor of degree ten there, impossible. Therefore it is divisible by c. Its quotient is an invariant cubic, by invariance of c and the integral-domain property. Repeating the restriction argument at degrees three and one forces another division by c and then the vanishing of the remaining invariant linear form. Thus the original quintic is zero.

The required invariant two-plane is therefore impossible. The rigorous improved bound is length(Z_q) ≤ 24.

## 3. Exhaustion of off-conic orbits

An off-conic point is an unordered pair of distinct points of P(W). Its pointwise stabilizer H_0 is cyclic because a finite subgroup fixing 0 and infinity lies in C*. Its full pair stabilizer H has [H:H_0] ≤ 2.

If H_0 is nontrivial its order is 2, 3, or 5. Its two fixed points determine the pair uniquely. Both inclusions H=N_A5(H_0) hold: a normalizer preserves the fixed set; a pair-preserving element normalizes the pointwise stabilizer. These normalizers have orders 4, 6, and 10, hence the associated orbits have sizes 15, 10, and 6. The usual involution/C3/C5 counts in A5, together with conjugacy of subgroups of the same order, give these normalizer orders. For order two the normalizer equals the centralizer V4.

The axis pair attached to distinct subgroups of the same order cannot coincide, since otherwise the pointwise stabilizer would contain distinct subgroups of that order while remaining cyclic. Pairs for different orders also cannot coincide, since A5 has no cyclic subgroup containing either combined order. This confirms uniqueness and disjointness of the three axis orbits.

When H_0 is trivial, |H| is one or two; orbit size is 60 or 30. This exhausts the complex projective possibilities without any reality assumption.

## 4. Passage to the degeneracy support

At every degeneracy point E has exact rank one, by PR663. Its kernel is therefore a unique projective line in Q. Q consists of invariant intertwiners, so the A5 action on Q is trivial; the same kernel line occurs at every point of the orbit. That orbit is contained in one fixed-channel zero scheme and thus has at most 24 points. PR661 excludes the conic. The classification above now leaves only the 6-, 10-, and 15-point axis orbits.

PR663 already forces the first two. Therefore the support has exactly 16 or 31 points, with the single unresolved alternative being occurrence of the C2 axis orbit. There are at most three exceptional projective channels, all mixed with respect to parity. No scheme-length assertion about the entire degeneracy scheme follows from this argument.

## 5. Multiplicity audit and strengthened corollaries

Equivariance gives isomorphisms of the local zero schemes along each orbit. Writing their common local lengths as m_5, m_3, m_2, with zero for an absent orbit, gives

6m_5 + 10m_3 + 15m_2 ≤ 24.

Thus m_2 is at most one; whenever present, that orbit is reduced in Z_q. A common C3/C5 channel has (m_5,m_3)=(1,1) or (2,1), and no C2 support, hence length 16 or 22. A common C2/C5 channel has multiplicities (1,0,1), hence length 21 and is reduced everywhere. A common C2/C3 channel is impossible, since its support alone would have length 25.

Under the original weaker bound 25, the statement that a common C2/C3 channel would have reduced length 25 was a correct conditional arithmetic consequence. After the sharpening, that case must instead be explicitly excluded. The statement that all three channels cannot coincide remains correct, but the C2/C3 separation is strictly stronger.

All reducedness statements here apply to the fixed-channel zero scheme Z_q. They do not establish reducedness, local length, or transverse determinantal structure for the universal rank-drop scheme Δ.

## Inputs independently read

- https://github.com/Akilleez-QA/read-em-and-weep/blob/1325647fd916bf2daa71b11efeae6d52cfefa2cd/research/hm/endpoint-square-reconstruction/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/f75a18fd411350adda35dedf18751eee002a39bc/research/hm/endpoint-base-locus-exclusion/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/ad3ab59f6fbbbb3e5bde1da58b3b92a1f49c6889/research/hm/secant-detection-exceptions/PROOF.md
- PROOF.md

This is a mathematical audit, not a proof-assistant certification. The canonical HM-to-representation interface is an explicit hypothesis rather than independently reconstructed here.

## 6. Final strengthening: liaison gives the bound 21

The subsequently proposed sharper bound is also correct. This section supersedes the numeric bound 24 and the possible length-22 case above, while retaining those arguments as independently checked intermediate steps.

Let T be the (5,5) complete intersection containing Z=Z_q. Suppose length Z ≥ 22 and let R be its residual scheme inside T, defined by I_R=I_T:I_Z. Standard zero-dimensional complete-intersection linkage gives length R=25−length Z=r≤3 and

0 → I_T(5) → I_Z(5) → ω_R(-2) → 0.

The twist is correct: ω_T=O_T(5+5−3)=O_T(7), and I_Z/I_T=Hom_T(O_R,O_T)=ω_R(-7). These statements apply to arbitrary finite Z here, including nonreduced schemes; zero-dimensional local rings are Cohen–Macaulay, and T is Gorenstein.

From the Koszul resolution, H^0(I_T(5)) has dimension two and H^1(I_T(5)) is naturally dual to H^0(O(2)), of dimension six. Finite-scheme duality identifies H^0(ω_R(-2)) with the dual of H^0(O_R(2)). Under these identifications the connecting homomorphism is dual to the ordinary restriction H^0(O(2)) → H^0(O_R(2)). Consequently

h^0(I_Z(5)) = 2 + h^1(I_R(2)).

Every finite plane scheme of length at most three imposes independent conditions on quadrics. To see this without a reducedness assumption, choose an affine chart containing its support and let B be its length-r coordinate algebra. Filter B by images F_d of polynomials in the two affine coordinates of total degree at most d. If F_d=F_(d−1) before reaching B, multiplication by either coordinate preserves F_d, forcing F_d=B because it contains 1. Thus the dimensions increase strictly from dim F_0=1 until reaching r, and F_(r−1)=B. For r≤3 quadrics therefore suffice. The empty residual case is immediate.

It follows that h^1(I_R(2))=0 and h^0(I_Z(5))=2, contradicting the A5 argument of Section 2. Therefore

length(Z_q) ≤ 21.

The corrected multiplicity inequality is

6m_5 + 10m_3 + 15m_2 ≤ 21.

All support-exhaustion conclusions remain unchanged. A common C3/C5 channel now necessarily has reduced zero scheme of length 16: the former (2,1) alternative had length 22 and is excluded. A common C2/C5 channel, if it exists, has reduced length 21. A common C2/C3 channel is impossible. These conclusions do not assert existence of either permitted equality of channel lines.

The liaison step uses standard exact duality, not any actual endpoint evaluation or numerical rank calculation.

## Final artifact verification

I reread the final PROOF.md containing the bound 21 and confirm its claims and derivations as written. SHA-256 of the audited proof: 9eefd2c23f477c1180411adce6d69de273b2b03b80c19bc232fee9f8325b78df.
