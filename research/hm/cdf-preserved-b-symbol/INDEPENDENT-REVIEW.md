# Independent review: preserved c-d-f B-block symbol

## Verdict

PASS for the stated conditional theorem, against the exact bytes listed below. The hypothesis remains the one-sided inclusion Q(X_B) ⊂ Y_B for an actual source127 c-d-f occurrence. No proof of that inclusion, contradiction to it, actual realization, or source/pair exclusion is obtained. This review is verification, not an additional deduction.

The reviewer read the complete proof, verifier, and all four pinned proof inputs. The original first- and second-Bockstein notes named in PR935 were also read and their Git blob hashes checked independently against PR935. The square-filtration note was consulted as supplementary context for the D-source vanishing; that extra consultation is not needed to replace the explicitly pinned PR935 theorem.

## Mathematical checks

1. The fixed-variable reconstruction in PR924, particularly Sections 4 and 6, supports preservation of the indicated blocks by every negative multiplication T_a. This is not an assumption that Q preserves their complements. PR920 alone retains lifts; the argument correctly uses PR924's later simultaneous identification, rather than erasing those lifts directly from PR920.

2. The actual kernel is A+D, with multiplicity one for each irreducible. The unique A of X lies in X_B and is killed by Q. Consequently its intersection with X_B can only be A or the entire actual A+D. In the A-only case, equivariant character subtraction gives a surjection onto Y_B. A formal right inverse then solves the pencil equation recursively within X_B. In particular the original second obstruction on A vanishes, contradicting the imported geometric nonvanishing. The other case therefore holds, and its image character is V+2P+D, dimension 16. This identifies the actual embedded kernel, not merely its abstract character.

3. The induced map H¹(S)=D → C=P is zero by inequivalence of irreducibles, establishing Y_B ⊂ im Q. The long exact sequence then gives H⁰(U)=D, H¹(U)=P and the connecting isomorphism δ. Neither this exact sequence nor these cohomology identifications split Q. In particular the unprescribed X_F → Y_B component remains allowed and is precisely what the connecting map can detect.

4. For k in K and Qz=−T_a k, the quotient cycle represented by z has connecting class −α_a(k). Under the canonical C ≅ H¹(U), the second error T_a z becomes γ_a([z]). Hence β₂,a=−γ_a δ⁻¹α_a with the stated common sign convention. Corrections differ by actual Q-cycles; global first-Bockstein vanishing removes this ambiguity. This is the original second obstruction for q0+t a: the original first note gives the correction −hζ_a and second class −[a hζ_a], and PR935 explicitly compares arbitrary first corrections with it. No different normal-obstruction target is substituted.

5. Actual nonvanishing on A implies both α|A and γ are nonzero polynomial families. The three requisite equivariant Hom spaces have dimension one. Thus their representatives are multiplication A⊗A → D, projected multiplication A⊗D → P, and the first transvectant A⊗D → D. Identifying any actual D copy with Sym⁴W only changes nonzero scalar normalizations; no coefficient value is selected.

6. The crucial D argument is valid beyond a single monomial test. The polarized map with diagonal a τ(a,h) is SL₂-equivariant: the determinant derivative τ is invariant under determinant-one coordinate changes, and multiplication is natural. The identity at the synthetic monomials x² and x³y proves this universal map is nonzero. Its image therefore equals the irreducible Sym⁶W. Consequently composition with its nonzero G-equivariant P projection is nonzero, even though that projection is not SL₂-equivariant. Polarization in characteristic zero returns nonzero diagonal data as a polynomial family. Since γ's scalar is already nonzero and the actual second family vanishes identically on D, α|D must vanish. No sampled actual parameter or instance rank is involved.

7. Multiplication by a nonzero binary quadratic is injective in the polynomial domain. The projective family consequently has constant image dimension three, a locally free rank-two quotient, and Chern class (1−H)^−3 = 1+3H+6H² on P(A). This applies only to the stated internal first-symbol quotient. The zero D summand does not disappear from its domain.

## Novelty and limitations

The comparison with the supplied existing c-d-f results is substantive: PR924 gives the negative-pencil algebra and marks the full-module extension boundary; PR935 rules out a compatible projector by forcing a *surjective* B block with kernel A under two-sided preservation. The present hypothesis is weaker, and the forced non-surjective B block with kernel A+D is not that excluded projector branch. PR939 supplies the already-established quotient/pair condition, not a new cut here. The new conditional content is the embedded whole-kernel conclusion, quotient connecting isomorphism, and internal/quotient first-symbol determination. A separate review does not add to that content or to any progress count.

The result imports the established actual kernel/cokernel and Bockstein theorems; this review does not independently reconstruct all their geometric dependencies. No claim of exhaustive novelty against every remote publication is made beyond comparison with the supplied existing c-d-f results. The hypothesis (H) still needs actual geometry. Scalar commutant alone cannot settle it. No universal coefficient table, selected actual HM/source coefficients, points, parameters, jets, instance ranks, local-model spike, or public write was used.

## Executable verification

Both commands completed with status pass, 35 checks, and actual_instance_evaluations=0:

- python verify.py
- python -O verify.py

The checks use explicit exceptions, so optimization does not erase them. All four input SHA-256 values and Git blob hashes match INPUTS.json. The supplementary original first/second notes match the independently stated PR935 blob IDs fe4410bbba05060545b22ac6bc80aac8e7c62ce4 and 21c7af094d7088f38ab0ee8fc25b01952ea13d11. These are content authentication against pinned IDs, not a fresh remote attestation of commit membership.

The verifier's scalar transfer identity is only a toy consistency check; the mathematical comparison in item 4 above supplies the general proof. Likewise its raising-operator identity is not alone a full SL₂-equivariance proof; the determinant/transvectant argument in item 6 supplies that proof. Passing tests are not presented as a formal proof-assistant certification.

One editorial ambiguity was corrected before final freeze: the phrase following the cokernel statement now explicitly says that Q|X_B has rank 16.

## Final reviewed hashes

| File | Bytes | SHA-256 | Git blob SHA-1 |
|---|---:|---|---|
| PROOF.md | 7335 | e07a59e7b8e8d35b2f9a164515ff65eeddeca4baca4a0964c731b36b7713e38d | eebebae694f59e786aaebc64c3838d732b2a3832 |
| verify.py | 3960 | e88298d360e3e2ed9f548d99b6d1c13e6b8ff5aa660e94d13f4b504e5191d9d1 | dc31db0763b5b1174532764265fc6a1eaa6710f9 |
| INPUTS.json | 643 | 49550f71200949bf5596bac39ed15020e931fae58d269b7975aad8e810741a5f | db02a7bb3b8b196399716111e707f2c0af22f480 |
| inputs/920.md | 20293 | 5cc83c225a03ba670b7859d1a64aec161611ec9cc35fffe79479fdd5b7dadf62 | 718b5245560a84568492874bab8d8c34730e8319 |
| inputs/924.md | 18095 | 0d740d6f70de924b0442af71cb37e050165efbe9ab984a76f0e1e40b5d27a599 | 83f5aee293995257459229e6b323522224ce8f3d |
| inputs/935.md | 11636 | 06fe9d6bf5f51d1d38ff5f594f93703cf91b48d6cffcf7256c3e281de631365d | 187fe2a8c1499e11afdb5002091aa3c144e1b4a3 |
| inputs/939.md | 4455 | 8263fd71ba117d916411829cc2063c73ae70ca04433d2237b0c05600542301b0 | 00452eb96b90000d9f938a8d96c0ecb780d02160 |

Supplementary original notes, read from the existing source126-typeII-joint-annihilator input copies:

- POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md: SHA-256 1ca888691a900c6eb9de65a082130ae1b106ef6261e241c33ed91668693e34d8; Git blob fe4410bbba05060545b22ac6bc80aac8e7c62ce4.
- ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md: SHA-256 364648ec61bc5f71f5891353a65a148c3f05093872f85466118dc047d67f693c; Git blob 21c7af094d7088f38ab0ee8fc25b01952ea13d11.
