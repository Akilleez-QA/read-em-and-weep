# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-jump-obstructions-PUBLICATION-CHECK.md](../hm-jump-obstructions-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit: Heisenberg stabilizers and generic vertex obstructions

## Verdict and audited version

**Pass, with the explicitly imported audited HM inputs. No mathematical correction is required.** The universal stabilizer argument proves the claimed orbit-rank bound. Character separation preserves this rank after restriction to K. The two incidence arguments give the stated codimension bounds, and the imported deformation arguments then prove actual generic obstructedness, hull dimension 24, and embedding dimension 26. Section 6 correctly gives the entire five-dimensional quadratic initial space at every surjective vertex.

Audited [PROOF.md](PROOF.md), SHA-256:

`6a2abcbae2506e47d5b28808449a9c3fb2a55de854ff8252e734e83b7b7d3d7d`.

This audit checks the new argument independently and reviews its local dependency chain. It does not re-prove the original HM cohomology computations or the previously audited scalar-propagation theorem. The following on-disk dependency hashes match their recorded audits:

- Apolar middle-module proof: `20e7bb1e00504f29736a716cc603234e2b53993e9c53a6728bd833f117308ab4`.
- Restriction jump-locus proof: `5009e39fe76a0971e96ef1473946187525283e0c5cbb1312b2c52b0f1b08f39a`.
- Nonzero-scalar corollary: `038c429400ac00da021177fc123150e3e4ae6dc6056daa7475b2dd6162c35a2a`.
- Mixed obstruction-pairing proof: `cf9fd13f7d68485652a490d011b05684e6715144e03f34ef3f6ce9c54a46e4c3`.
- Generic restriction/orbit proof: `261c57bde9ce8bad8b04e511a08dc3eae40d4746c34592e4195979f4d64ef21f`.
- Its embedded-orbit complement JUMP-STRATA.md: `dd698b95c1cdec3d1b01824785ce06beaac93c90667a2a03f34c852a3003cdca` (also recorded in the obstruction-pairing audit).
- Scalar-propagation proof: `35a93234687c5d79533f8fc55a7589b3cae6546e683dd3e4c192adbbc3d89c4c`.

The imported facts used here are surjectivity and H₅-equivariance of Ψ, H₅-triviality of its target, Φ=cΨ with c nonzero, the smooth-member theorem for K, the ambient orbit Kodaira–Spencer isomorphism, the tangent-space restriction sequence, the exact mixed cyclic cubic, and the embedded 24-dimensional formal orbit germ. The restriction proof's original conditional treatment of c is legitimately resolved by the later nonzero corollary.

## 1. Weight decomposition and bracket closure

From ZX=ζXZ, conjugation by X and Z on X^rZ^s has eigenvalues ζ^(−s) and ζ^r. Distinct pairs (r,s) give distinct characters of the abelian conjugation quotient. All 25 matrices are nonzero, so their distinct eigenspaces make them linearly independent and hence a basis of End(V). The trace checks give the asserted 24 nontrivial weight lines in sl(V), with no trivial summand.

The multiplication scalar ζ^(sr') and commutator coefficient ζ^(sr')−ζ^(s'r) are correct. Their difference is nonzero exactly when the determinant is nonzero modulo five. In that case a+b cannot be zero. In characteristic zero every stable subspace is the direct sum of its character components; because those components are one-dimensional, an H₅-stable Lie subalgebra is specified by a subset of the nonzero weights. Closure under the nonzero brackets gives precisely the addition rule used in Section 2.

No classification of Lie subalgebras is assumed, and no normalizer irreducibility is needed for this new result.

## 2. Finite-field support argument

For independent a,b, repeated additions of a to b are allowed because det(a,b+ka) is always det(a,b), which is nonzero. These give the entire affine line b+F₅a.

At the induction step, the determinant of b+ia and (m−1)b+ja equals ((m−1)i−j)det(a,b). With j=k−i, this is (mi−k)det(a,b). Since m is one of 2,3,4, only one value of i is forbidden; a permitted i always exists. Both summands are nonzero and already supported. Their sum is mb+ka, producing all four affine lines with nonzero b coefficient.

For the final step, det(b+ia,4b+ja)=(4i−j)det(a,b)=−k det(a,b) when i+j=k. For k nonzero this gives all nonzero multiples of a. The resulting twenty plus four vectors exhaust the 24 nonzero weights.

Consequently a proper supported subalgebra contains no independent pair. Its support lies in one F₅-line, which has only four nonzero vectors, so its complex dimension is at most four. The empty support causes no exception. All brackets among weights in the same line vanish, so the additional abelian assertion is also correct. This is a universal finite-field argument, not an enumeration or a selected instance calculation.

## 3. Invariant-functional stabilizers and character separation

The stabilizer h_q is a Lie subalgebra by the representation identity. Because q is H₅-fixed, the map v↦v·q intertwines conjugation on sl(V) with the action on S₅*, proving H₅-stability of both its kernel and image.

If its kernel were all of sl(V), q would be fixed by connected SL(V). The representation S₅*=Sym⁵V is irreducible and nontrivial, so it has no nonzero fixed vector. Thus the stabilizer is proper and the preceding support argument gives dim h_q≤4. Rank-nullity yields dim D_q≥20. This concerns the actual vector stabilizer and tangent orbit image, exactly as required by the incidence construction.

Every character in the source sl(V) is nontrivial. Its equivariant image D_q therefore has no trivial character. The central μ₅ acts trivially on Sym⁵V, consistent with treating these as characters of the abelian quotient. Since the three-dimensional net T is entirely fixed by H₅, D_q∩T=0. In particular one does not lose up to three dimensions when restricting these orbit functionals to K: one loses none. This stronger observation is justified and is essential to the numerical bounds claimed.

## 4. Transpose, restriction rank, and the two incidences

The infinitesimal contragredient identity gives A_q transpose equal to v↦−(v·q)|_K. The kernel of the restriction map S₅*→K* is exactly T=K-perpendicular. Its restriction to D_q is injective by the character argument. Therefore rank A_q=dim D_q≥20 and dim ker A_q≤123−20=103.

The projective incidence equations are bilinear and homogeneous in both variables. Every fiber over P(T) is the projectivization of that kernel and has dimension at most 102. Since P(T) has dimension two, the total incidence has dimension at most 104. Projection to P(K) is proper, so its image is closed, and its dimension is no larger than 104. The ambient projective dimension is 122, giving codimension at least 18.

The image equals the nonsurjectivity locus: a map into the three-dimensional space Sym²U* fails to be surjective exactly when a nonzero dual functional annihilates its image. Via Ψ*, that dual functional is the nonzero q used in the incidence. The equation α(L_p(v))=c q(v·p), with c nonzero, proves the equivalence. Full SL(V)-equivariance of Ψ is neither asserted nor used.

For the second incidence, u² is nonzero and Ψ* is injective, so the image of P(U) is a genuine Veronese conic in P(T), of dimension one. The same fiber bound now gives dimension at most 103 and codimension at least 19 for the closed projected image. Pairing a quadratic form with u² is its evaluation at (u,u), so this image is exactly the common-projective-zero locus. Such an evaluation is a nonzero functional on Sym²U*, proving that this locus is contained in the nonsurjectivity locus.

The proof correctly claims lower bounds on codimension, without asserting sharpness or nonemptiness of either exceptional locus.

## 5. Actual hull dimension and obstructedness

The incidence bound makes the surjectivity locus a nonempty open subset of the irreducible P(K). The imported basepoint-free Bertini argument supplies another nonempty open subset consisting of smooth quintics. Their intersection is nonempty and dense in the smooth-quintic vertex.

At such a smooth vertex, the imported restriction sequence gives tangent dimension 26 and an inclusion of the 24-dimensional ambient deformation space A. The orbit Kodaira–Spencer isomorphism identifies A with sl(V). The mixed-pairing proof gives the displayed cubic W₃ with no missing term involving two orbit arguments, and its gradient is the primary quadratic obstruction map. In particular its orbit derivatives supply exactly im L_p as binary quadratics, up to the harmless scalar 1/2, regardless of G.

If these quadratics have no common projective zero, their affine common zero set is the origin. The Nullstellensatz gives radical (z₁,z₂). After adjoining 24 orbit variables, the ring cut out by these quadratics has dimension 24. The associated graded minimal hull is a quotient of this ring, so has dimension at most 24. A complete Noetherian local hull and its maximal-ideal associated graded ring have the same Krull dimension.

The reverse inequality comes from the imported actual embedded smooth formal orbit germ. This is stronger than having 24 independent tangent vectors: the classifying homomorphism from the hull to a 24-variable power-series ring is surjective by the formal inverse-function argument in JUMP-STRATA.md. It therefore supplies a genuine dimension lower bound. The hull has dimension exactly 24.

Its embedding dimension remains 26, so it is nonregular and cannot be formally smooth. This establishes actual obstructedness for ordinary deformations on the fixed smooth quintic, not merely nonvanishing of an obstruction-space dimension. The same reasoning works on the larger complement of the common-zero locus. No conclusions about reducedness, multiplicity, the complete ideal, or all components are inferred.

## 6. Exact primary normal form

Surjectivity of L_p allows its three coefficient functionals to be chosen as three independent orbit coordinates. This gives W₃=1/2(t₁z₁²+2t₂z₁z₂+t₃z₂²)+G/6, with the remaining 21 orbit coordinates absent.

Multiplication U*⊗Sym²U*→Sym³U* is surjective for binary forms, so linear forms ℓ_i with ℓ₁z₁²+2ℓ₂z₁z₂+ℓ₃z₂²=G/3 exist. Substituting t_i=t_i'−ℓ_i(z) subtracts G/6 from the displayed mixed part, exactly cancelling the original G/6. The factor 1/3 and the sign of the shear are correct. The shear is an invertible linear change, fixes the orbit subspace z=0 pointwise, and corresponds to changing the tangent splitting. It is not an assertion that the original G vanishes.

The transformed cubic has partial derivatives z₁²/2, z₁z₂, z₂²/2, t₁z₁+t₂z₂, and t₂z₁+t₃z₂, with all other orbit derivatives zero. The three pure normal quadratics are independent. The two mixed quadratics are independent, for example by their respective t₁z₁ and t₃z₂ terms, and cannot combine to a pure normal quadratic. Thus the gradient spans precisely the five-dimensional space stated in (5).

Under the linear coordinate change, the chain rule changes gradient components by an invertible dual linear transformation, as required for the identification of obstruction space with tangent dual. The imported minimal Kuranishi construction gives generators with quadratic parts equal to these gradient components. Since every generator starts in degree at least two, every degree-two term in the defining ideal is a constant linear combination of those parts; higher terms or cancellations cannot create additional degree-two equations. This proves exactness of the five-dimensional quadratic initial space, rather than a mere lower bound.

The ideal generated by these quadratic forms contains (z₁,z₂)² and is contained in (z₁,z₂), so its radical is exactly (z₁,z₂). This confirms the normal form and its dimension consequence while leaving higher-degree initial equations and the full formal hull undetermined.

## Scope of the audit

Only local proof/audit reads, universal symbolic reasoning, file hashes, and this local audit-file write were used. No selected polynomial, HM/source/cofactor matrix, numerical rank instance, or large computation was evaluated. No external application or previously audited proof was modified.
