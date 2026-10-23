# Independent review: corrected terminal factorization

Verdict: PASS for the stated conditional actual-map conclusions and the explicitly limited formal control.

## Frozen SHA256 hashes

- PROOF.md: 70f38fada0735ee5c7a5eef11ed316a02573f2ae09059101bae2bb3a83d3e516
- verify.py: 6b5157c79310568e5fe36e0ddeca2765b13b0b1376a31fa00e36c6057912ebad
- INPUTS.json: 31d1649c15a7ae49c359ab987643afdb4ed1ab0a21990c74cd09c3e492baa966
- RESULT.json: fc5ce2ea780bc942fa08d7f1dd20ebaa8a08179138565d1f1f6bc56776dd2291

## Authentication and replay

The four complete immutable proofs were freshly fetched. Their contents matched the retained files byte-for-byte and their returned Git blob hashes matched INPUTS.json:

- PR1096: 24df79d14846fd9d942eae8bb0772b3859f49849
- PR1094: dd21bc9302ea9ffcd84dddf72ce7a676c326600d
- PR1081: 3aa53fa809fa82cef18629cc040cf61fe4eb0a90
- PR1072: 65dda3e16ded2b79ad84c583f248b09c425e9881

Independent normal and optimized verifier executions passed all 40 checks, with byte-identical outputs equal to RESULT.json. Explicit exceptions retain the checks under optimization. The formal matrices and graph coordinates are universal multiplicity data, not actual source entries.

## Mathematical checks

1. The map a is defined on the actual quotient H/K by the two induced isomorphisms j3 and Theta. Equality of their kernels proves lift independence, and its target is the marked actual image L_Theta rather than an arbitrarily chosen complementary T.
2. The quotient identity q Theta=d j3 and q a=d put Theta-a j3 in I3. This difference kills H=ker Q3 and therefore descends through Q3 onto V5. Since Q3 restricted to J is onto and the old factorization holds there, the descended row is exactly ell. This proves the full-domain formula with its necessary correction. Alternatively, subtracting a lift in H with the same j3 image gives the same formula directly. No extension of h or a polynomial-module compatibility is introduced.
3. The canonical projections of the two marked image summands yield the two component identities. The domains are essential: Theta=ell Q3 alone is asserted only on J, not on all M3.
4. PR1081 supplies the actual isomorphism F5 to V0 under the genuine terminal projection. Its inverse defines g uniquely. Consequently restricting ell to F5 gives literally ell0+tau g. PR1094 supplies the exact equivalence between this row vanishing and R=0.
5. If tau=0, zero restriction would force both pieces of the onto row ell to vanish, a contradiction. If tau is nonzero, irreducibility of its actual T source and target makes it invertible; hence there is exactly one possible zero graph, -tau inverse ell0. This is a criterion for the retained actual graph, not existence of a source realizing that graph. The residual-large comparison is explicitly within each retained actual object, not an identification of coefficients across instances.
6. The cross-block consequence uses NR3 contained in J and Theta(NR3)=I3. When tau=0, the restricted formula becomes ell0 e0 Q3, proving surjectivity of the detected cross-block image. It does not give the rank of the entire off-diagonal block or select tau.
7. The formal operator family has the stated square-zero products, corrected formula, marked complement and fixed unit minors. Its free terminal coordinate demonstrates only that those abstract odd-operator identities do not determine that coordinate. It is explicitly not a realization of the negative module or source geometry; the proof makes no stronger non-implication claim.

No actual coefficient, direction, point, jet, source matrix or instance rank was evaluated. No public write was performed. The new contributions are the canonical corrected global factorization, the fixed-row graph criterion and conditional cross-block detection; imported incidence and odd-action results remain attributed.
