# Independent whole-proof review

## Verdict

**PASS for the theorem exactly as scoped.** No substantive mathematical gap was found in the new argument. The actual-map conclusions follow from the pinned inputs and the universal representation calculation. The two remaining incidences are genuinely undecided by this argument, not defects hidden by the verification script.

Reviewed files:

- `PROOF.md`, SHA-256 `4ecb2dfce5a532932e29063a4ee79c2431ab1c74b00c8a3eee16d6b9ddbf2e87`.
- `verify.py`, SHA-256 `8d10e4caca62bc5f6e3ac8c9fc57372041b1b496c7f93514673f1122ed55d2b6`.
- All four complete originals in `inputs/`, together with `INPUTS.json`, `REPRODUCE.md`, and `RESULT.json`.

This is an independent reading of the entire proof, including its constructions and the relevant source arguments, not a verdict inferred solely from replay. The review treats the pinned originals' earlier established geometric and source-theoretic dependencies as inputs; it does not claim a recursive reproof of their entire preceding research history.

## 1. Source authentication and actual spaces

The four complete local originals match both their manifest SHA-256 digests and their Git blob hashes. A read-only GitHub retrieval at each exact repository path and commit independently returned the same blob:

- PR1108: `90fb985d182de8be9160c0b215a03fdac3695e13`.
- PR1111: `c06c24db089d3f7b7d11437e8688abc5f6c59186`.
- PR931: `060ad3bacb45086349e911265d6c0d6157bef4a0`.
- PR933: `a428ac4b4b8cb6b67b7b8e3b1625352468adeb05`.

PR931 supplies the actual source character, invariant-product kernel, and actual reachable-middle image containing the unique trivial constituent. PR933 supplies the actual target character and ordinary commuting positive multiplication. PR1111 supplies the three-channel tensor calculation. PR1108 supplies the actual homotopy kernel and its conditional alignment with the genuine negative projector.

In particular, E and F in the new proof are the full actual V-isotypical spaces, each of multiplicity two. They are not the single marked source copy or the single projected target copy. Since invariant multiplication is equivariant, Q2(E) lies in F; since ker Q2 contains no V, Q2|E is injective. Equal dimensions make it an actual isomorphism. Passage to Hom_G(V,-) expresses that same map on multiplicity spaces and does not replace the actual embeddings.

## 2. Scalar bottleneck and channel normalization

The scalar first arrow is onto. The full actual image of a contains the sole scalar H in P3, while the listed tensor decompositions show that only V tensor E can contribute a scalar. Thus the scalar restriction on E cannot vanish. This is stronger than an unjustified appeal to multiplicity one.

Using the invariant metric whose inverse quadratic is the fixed q is legitimate over C. It fixes the displayed tensor normalization without evaluating any actual multiplication coefficient. With that convention, the independent channels are precisely F0, F1, F2 through 1, V, D. Their completeness follows from V tensor V = 1+V+D and Schur's lemma, including the finite-group setting.

The identities C0 = C1 + (5/3)C2 and Q = -C1 + 5C2 are correct. The latter has the exact displayed normalization, not merely the same zero locus: the chosen inverse metric makes q equal to the orthonormal-basis sum used for the contraction.

The actual scalar composite is d s. Consequently K = Q^{-1}d s has rank at most one, and K squared = (tr K)K. Solving the two channel equations gives all three formulas in (1). The coefficient S = (9K-Id)/10 and both polynomial identities in (2) follow with the stated constants. The nilpotent trace-zero possibility is not silently excluded.

Crucially, scalar first-arrow surjectivity does not imply d is nonzero. Rank K = 0, with s nonzero and the scalar second arrow zero, remains permitted throughout. No converse from a nonzero first-arrow channel to a nonzero effective channel is used.

## 3. First-arrow dimensions and the canonical kernel

Each effective coefficient factors through its actual first-arrow restriction. Thus its rank only gives a lower bound on the relevant first-arrow multiplicity rank. Both shifted operators 3K-Id and K+Id have rank at least one, and their determinant zero conditions are respectively tr K = 1/3 and tr K = -1. They cannot both be singular. This proves precisely the allowed pairs (2,1), (1,2), (2,2), hence dimensions 12, 14, 17.

The implications from dimension 12 to trace -1 and from dimension 14 to trace 1/3 are correct and deliberately not reversed. The first arrow can have a larger image than its composite with b. If K = 0, both shifted coefficients are invertible, forcing dimension 17 despite the killed scalar second arrow.

The kernel of the onto scalar functional is a well-defined multiplicity line. Its embedded copy V_s is canonical even though a formula for s uses a tensor normalization. On that line the scalar channel vanishes and the V and D effective coefficients are nonzero multiples of the injective Q. The actual first-arrow restrictions are therefore injective on those two irreducibles, with disjoint images. The image is exactly V+D, of dimension eight. The statement that its F-projected two-step output lies in Q(V_s) is also correct; it makes no unsupported claim about other target irreducibles.

## 4. Conditional negative-row comparison

The source2 assumptions, residual-large condition, and R = 0 remain indispensable. Under them, PR1108 identifies the actual V_h with the kernel of e0 Q2 on the full E. In particular lambda = rho Q is a nonzero row and V_h corresponds to its kernel line. The marked V_C is transverse to that line, rather than identified with an arbitrary complement by character.

The final proof explicitly justifies p_V e0 = rho r on N4 by equivariance. Therefore applying rho to the full target calculation is exactly applying the specified genuine projector after the actual b. No projector is moved to the middle P3 and no second arrow is discarded.

Restriction of the three projected coefficients to ker lambda leaves the common factor lambda K in the ratio 1 : 3/4 : 3/20. Independence of the three channels proves vanishing exactly when that factor vanishes. Factoring K = u s reduces this to the product of maps between one-dimensional spaces, so vanishing is equivalent to lambda u = 0 or s|ker lambda = 0. These are exactly B0 contained in NR4 and V_h = V_s, respectively. This includes B0 = 0.

When neither incidence holds, all three coefficients survive, invariant contraction is zero, and each of the three actual first-arrow irreducible restrictions is injective. This establishes the stated dimension-nine injectivity on V tensor V_h. It does not identify or evaluate a higher correction.

Finally, tensoring over C is exact. Killing Sym2 V tensor ker Gamma is precisely the criterion for descent through the actual quotient E/ker Gamma, canonically identified with im Gamma. This proves the stated factorization criterion for the projected map on Sym2 V tensor E. It is not a factorization assertion for unrelated source constituents.

## 5. Universal constructions and limits of sharpness

The intermediate U in Section 5 is a valid construction, not merely a list of desired coefficient ranks. Projecting y tensor z onto 1, V, D, applying s on the scalar part, and applying the quotient maps on the other two parts defines a first arrow onto U. Each Cj descends to its indicated quotient, so the second arrow is well-defined and its composite is exactly the displayed three-channel tensor.

The commutativity equation establishes commuting positive actions at the source degree. Zero outgoing action from the final degree makes every remaining positive commutator zero. The chosen traces -1, 1/3, 1 give dimensions 12, 14, 17, and trace zero with u = 0 gives the separate dimension-17 killed-second-arrow control. Their middle characters fit inside the actual P3 character; padding changes no stated local calculation.

The three incidence controls also work: one has only kernel equality, one only residual scalar output, and one neither, with nonzero trace-free projected output. Taking Gamma = lambda supplies the stated row-kernel interface. These controls do not satisfy, or claim to satisfy, every full negative-module, global reachable-middle, geometric, or source-occurrence condition. Accordingly they justify sharpness only for the expressly stated local positive/multiplicity interface. They cannot establish actual HM realizability, nor settle either incidence in the actual source2 case.

## 6. Bounded verifier audit and final boundary

The verifier uses exact rational arithmetic and a four-variable formal polynomial ring. Its only finite tensor enumeration consists of the 27 basis triples of the universal orthogonal three-space. The small rational models and interface rows are abstract controls, not selected actual HM/source parameters. Explicit RuntimeError checks remain active under optimized Python.

Independent execution of python verify.py and python -O verify.py produced identical PASS outputs, each with 82 checks, byte-for-byte equal to RESULT.json. The checker's algebra and bookkeeping were read, not just executed. Actual scalar surjectivity, actual Q transport, the projector identity, the source hypotheses, and the universal module construction are justified in the written proof rather than outsourced to replay.

No blocking correction remains. In particular, the theorem does not decide whether R = 0 occurs, whether B0 is residual, or whether V_h equals V_s. It makes no actual HM/source coefficient, matrix, rank, point, jet, or derivative evaluation; no source exclusion, fifth-class computation, higher-order lifting conclusion, or algebraicity claim follows. Those boundaries are accurately retained.
