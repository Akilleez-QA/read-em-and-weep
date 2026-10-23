# Independent whole-packet review

Reviewed on 2026-10-23 UTC. Final proof SHA256: f2c23c8f4188952d807e920affcbc6eaf09a92af1d436885db444133457c5d30.

The final review includes the author’s antecedent clarification, “Hence K_F has rank exactly four and K_F(3) is trivial.” It is the only change from the previously reviewed proof SHA256 016d796314ebaf3009348f0a9befc00191e061248c4e755bf64a6da364d5ffac; all other packet bytes remained unchanged.

## Verdict: PASS

The complete packet passes for its stated, narrow conclusion, relative to its explicitly imported actual-geometric and primary-source theorems. The actual quotient shapes O(-8)+O(4)+O(8) and O(-8)+O(4)+O(10) are excluded. The proof does not require a rank hypothesis on the derivative of K, a maximal Gauss profile, or a determinant-defect hypothesis. Its four historical ordered row exclusions are correctly identified and are not a claim about four newly live cases.

This was a review of the whole packet, not merely of checker output. I read PROOF.md, the complete supplied geometric/character originals, the provenance manifest, reproduction instructions, checker, character module, and result; I independently checked the historical entries against the supplied complete list. I did not edit the proof, checker, character module, results, or immutable inputs.

## Mathematical audit

1. **Actual ambient and fixed marking.** The ambient inclusion used is the actual saturated plane-section inclusion from the pinned actual-splitting and ambient-Gauss proofs, not the unrelated terminal-pencil presentation. The physical W and determinant convention are unchanged. A_std=Sym2 W is distinguished from V, and S=Sym3 W from the other four-dimensional representation P. All representations used in Serre duality are self-dual; det W=1 supplies the stated canonical O(-2) convention. No outer-automorphism relabeling is introduced.

2. **Top cubic channel.** Strict-top gives H0(K(2))=0 and injectivity D -> H0(A(2)). Thus p:D O(-2)->A is nonzero. Its coherent image is torsion-free and locally free on the smooth curve, so K_F is saturated in F and has rank at most four. H0(K_F(2))=0 bounds its degrees by -3 and h0(K_F(3)) by four. Since D tensor W=S+T and dim T=6, the top T channel cannot be killed. This is a global-section dimension argument, not a fiber-rank argument.

3. **Displayed cubic channels and the saturated graph.** Each displayed W' or T block is a saturated direct summand whose ordinary complementary quotient has top degree at most -2. The imported general near-top lemma applies to those actual inclusions, without making the splitting horizontal. If the two T coefficient maps were dependent, the unique equivariant lift T O(-3)->F would produce a killed graph summand in E. Its complement still has top at most -2. Equivalently its internal derivative would land in a bundle with top at most -4, whereas its source has degree -3, and hence vanish. Saturation in the constant ambient then makes that negative graph horizontal, which is impossible. Thus the two T maps are independent, the sole W' survives, and the cubic kernel is exactly 0 or the sole S. Semisimplicity and multiplicity one place that S inside H0(F(3)), not in a different cubic source block.

4. **Actual image, not saturation in A.** If the S alternative occurs, K_F(3) has rank at most four, nonpositive degrees, and four independent global sections. Therefore it has rank four and is trivial, with coefficient representation S. The exact sheaf quotient has rank one and degree -10-(-12)=2. It is a locally free coherent image I, and perfectness of G removes a possible character twist: I=O(2). The actual image inclusion I->A is a sheaf injection even if its image is not a subbundle. The proof neither substitutes the saturation of I in A nor assumes fiberwise injectivity. Thus Hom_G(O(2),A)=0 is the correct obstruction. Twisting F->I by two gives a nonzero equivariant D->H0(O(4))=D, so the complete quartic-system statement follows by Schur's lemma, with no selected coefficient evaluation.

5. **Improved fourth-twist envelope.** When H0(K(3))=0, every degree of K is at most -4. The kernel K is saturated in the same constant ambient: both E/K and the earlier ambient quotient are locally free. Strict-top applied to K makes H0(K^-(4))=0. Because beta_E kills K, the actual derivative of K lands in (E/K)(-2)=A(-2); its kernel there is its ambient derivative kernel. Hence H0(K(4))->H0(A(2)) is injective. The proposed virtual character equals

   (H0(A(2))-H0(K(4))) + H1(K(4)),

   and is therefore genuine. No additional H0(A) term and no fixed derivative rank are needed. This is a valid improved bound, not an assumed exact sequence of global sections.

6. **Both Hom obstructions and the negative line.** Maps from O(2) to O(-8) vanish by degree. The positive target blocks require invariants in Sym2 W, Sym6 W, or Sym8 W, none of which has a trivial constituent. In the fourth-twist Euler characters, the O(-8) term contributes H1(O(-4))=A_std and must be subtracted. It is not discarded or replaced by an H0-only computation.

7. **All-primary scope.** Under the pinned primary four-type theorem, the other three possible source types have every ordinary degree greater than -8. Their Hom to O(-8) is zero. The surjective composite E->A->O(-8) therefore forces the D-type. Thus the two actual quotient exclusions are not contingent on choosing a formal source from a ledger.

## Independent character checks

In addition to reading and replaying the packet checker, I computed the relevant characters independently using exact Q(sqrt(5)) class values and the class sizes 1,1,12,12,12,12,20,20,30. That calculation did not import characters.py or execute the historical character-reference program. It checked all pairwise irreducible inner products, the dimension-square sum 120, and reconstruction of every used character on all nine classes.

The independently recovered identities are:

- D tensor W=S+T; H0(E(3))=S+W'+2T.
- Sym2 W=A_std; Sym6 W=V+P; Sym8 W=P+D.
- H0(E(4))=A_std+3V+3P+2D and H1(E(4))=A_std, giving chi(E(4))=3V+3P+2D.
- H0(A_8(2))=A_std+2V+P+D; H1(A_8(4))=A_std; chi(A_8(4))=1+2P+2D.
- H0(A_10(2))=1+A_std+V+2P+D; H1(A_10(4))=A_std; chi(A_10(4))=V+2P+2D.
- The full tightened envelopes are respectively 1+A_std+D-V and 1+A_std+D+P-V. Each has V multiplicity -1.

Only bounded universal representation calculations were performed, with symmetric powers needed here through degree 14. No selected actual HM/source coefficients, points, parameters, jets, matrices, tensors, instance ranks, scans, or large computation were used.

## Historical ordered labels

All four rows have profile 11 and source commit 4c147e95217f0900fa13f195662d95e933412c3c. The exact row labels and ordered quotient data in the immutable list are:

| Zero-based source index | Stable ID | A degrees, scalar blocks | B degrees, scalar blocks | Original defect |
|---|---|---|---|---|
| 98 | G3.11.ed64b2cd0102 | -8,4,8 | -18,-10,6 | 12 |
| 100 | G3.11.1aa4528c491e | -8,4,8 | -10,-6,6 | 0 |
| 104 | G3.11.358793f77d6d | -8,4,10 | -18,-12,6 | 12 |
| 106 | G3.11.8558f6c50687 | -8,4,10 | -12,-6,6 | 0 |

I independently checked t=-6-deg(A)-deg(B) for these entries. A and B were not interchanged. These are exact historical labels; neither the JSON metadata nor their count supplies a new geometric coverage theorem.

## Replay and input integrity

- python3 verify.py: PASS.
- python3 -O verify.py: PASS.
- Both runs report 130 checks and pass the checker's exact RESULT.json text comparison. The printed stdout adds the ordinary final print newline; the stored replay itself is exact.
- Both active code files use explicit require checks, with no Python assert statements disabled by optimization.
- All eight input files match their supplied byte counts, SHA256 digests, and Git blob SHA1 identifiers. The historical character-reference.py was read but not executed.
- The checker was not run with --write. No historical source/quotient enumeration was rerun.

## Limitations

The PASS is relative to the explicitly imported theorems and fixed physical setting. It is not a re-proof of the full upstream HM foundation, all earlier profile exclusions, or every dependency cited inside the included originals. Local immutable files were authenticated against the supplied manifest; this review did not independently fetch the remote GitHub blobs again. The separate coverage note is an imported written synthesis, not a fresh geometric-completeness audit.

The computation does not prove the saturated-graph, coherent-image, or derivative-target arguments; those were reviewed mathematically above. The theorem does not exclude O(-8)+O(2)+O(16), whose O(2) summand already admits the forbidden Hom alternative. It establishes no full profile-(1,1) exclusion, global rank-three exclusion, COV, actual realization, maximal rank, original obstruction value, smoothing, algebraicity, or original-theorem repair. No public write was performed.

## Reviewed artifact hashes

| File | Bytes | SHA256 |
|---|---:|---|
| PROOF.md | 8152 | f2c23c8f4188952d807e920affcbc6eaf09a92af1d436885db444133457c5d30 |
| verify.py | 4509 | 9639c8e778aa903d1faa9d19c853bbbdc48ceb00b0fda3c5eb90643bee983518 |
| characters.py | 1776 | 5b3b1d415f26ca467670afeb73357cbb0e9c125a6b1acd25155b6d85eef4e4f1 |
| INPUTS.json | 3176 | 4631f131047a3b90b626aed58ab105cf2433145596673ba1e05daa56be76b74b |
| RESULT.json | 4178 | 7aa4c3ac08b323ec01694fbb3a4fe339a8ef1d22fb3220ac91e1d2b63d9ceb48 |
| REPRODUCE.md | 1982 | adfeab9a488b2d2baa4204881c3042310dfaacc979475b5042ab03f1e11ed09e |

## Verified immutable input identities

| File | Bytes | SHA256 | Git blob SHA1 |
|---|---:|---|---|
| inputs/pr1123-proof.md | 9616 | d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e | 43cc2fe6ac82d7cb01b8c32dc2ef906212c3b705 |
| inputs/pr1129-proof.md | 7259 | f7f267098d561de91e216f34588d1ab983947c2363b5a2dd4b0bd59104b39eed | c8094f1a85b48094a7538230db1f92acfd7929d0 |
| inputs/actual-splitting.md | 9672 | a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256 | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 |
| inputs/ambient-gauss-proof.md | 5414 | 0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2 | 303c6927265296440470b9dd4015fe6e8d55ca4d |
| inputs/strict-top.md | 4983 | 53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08 | d7506dae49b4be43230450c4132bd5db91f137ef |
| inputs/frontier182.json | 38248 | d4cdaa4dfd29b185d74f7ab34978df834aa39a60d96b339f7b0043c0fc4a2792 | 7e733f9543651b00b309cd56804ddd0a2eaef517 |
| inputs/character-reference.py | 3298 | e81f548a7e0ea4069ea293ca3b86b1110c2fd6c2906e8637d1441b35f6f14af2 | 9eb58f03edde15dd612087440d8180e9e16d1755 |
| inputs/cover182-proof.md | 3913 | b2e9a34b2f59ac2dc1445cc660733ce3988d15aefdf46e0b9123db159e927d2a | 4afcfab4047e1563a2655a0f362a70ea103ea93a |
