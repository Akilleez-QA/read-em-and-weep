# Independent review: full-positive triplet span

Verdict: ACCEPT as a conditional necessary-constraint theorem, with the stated actual-geometric premises. No mathematical correction is required.

Reviewed proof: `PROOF.md`, SHA256 `145a8b2607ac5d888de52aa75ce4271fb8426a63f5123841f356a4025354fc6b`.

This review covers the entire proof, including the actual geometry and all imported facts it uses. It does not merely rerun the author's verifier. The independent `review_verify.py` uses a separately implemented exact character inner product on the nine conjugacy classes, fixed degree identities, and hardcoded immutable-source byte checks. It imports no author module and uses explicit exceptions rather than optimizable assertions. It passes 209 checks with identical output in ordinary and optimized Python. These arithmetic checks are not a formal verification of the sheaf-geometric arguments reviewed below.

## 1. Source authenticity and import boundary

I independently fetched all seven complete source files using the GitHub read connector at the exact commits and paths in `INPUTS.json`. Every returned full UTF-8 body equals the retained input bytes, every returned Git blob SHA equals the locally recomputed Git blob hash, and every byte length and SHA256 equals the immutable record. `REVIEW-AUTHENTICITY.json` records this separate source check. The larger raw fetch-response retention is local provenance only and is not required for replay.

The imports used are exactly these:

- PR1194, `top-four.md`: the actual source-D restriction and the two section gates for the triplet quotient. The proof states these gates before kernel analysis. The source-D claim follows already from the unique possible negative O(-8) quotient row and is explicitly retained in that source's final statement.
- PR1198, `five-kernels.md`, especially Section 5: when the actual coherent image is A(2), the negative quotient row gives K inside E0 and E0/K=A(4); the image identifies K^+=E0, and kernel comparison gives E0^-=K. Those arguments do not use the particular K1/K2 splitting after the full-image hypothesis has been established, so their application to the same full-image branch of K3/K4/K5 is valid.
- PR1199, `deep-images.md`: the explicit full-positive alternative exists in the necessary image list for each remaining K. Its universal principal-parts identity is applicable to arbitrary actual coefficient systems; it does not require a complete actual linear system. Its separate negative-image flag and invariant-divisor branch are not imported into this branch.
- PR1196, `zero-defect.md`: original triplet determinant defect t=0, proved without the present full-positive assumption. The source's coherent-image capacity and determinant-equality argument preserve torsion until it is excluded. This is a fact about the original rank-four transpose, not a prematurely assumed small-ambient equality.
- PR1185, `low-top.md`, Section 2: the actual negative kernel filtration and coherent graded injections are stated and proved before the low-top assumption. The reviewed proof reuses that geometric mechanism at the actual changed ranks, not a rank-seventeen numerical classification.
- ACTUAL, `actual.md`: physical representation conventions, center-even bundles, equivariant splitting, full constant span, and H1(S)=M2. The original actual presentations and their transitive geometric foundations remain assumptions, as the theorem explicitly says.
- PR1197, `pair-defect.md`: methodological context only. Its decomposable quotient and t=12 conclusion are not used as a theorem for the triplet. The small-ambient argument is supplied again with the triplet degrees and independently checks.

No source is replaced by an unpinned branch reference. No implication is claimed to re-prove the transitive actual-geometric hypotheses behind the frozen presentations.

## 2. Minimal span, actual complement, and original defect

The span C is G-stable because E0 is equivariant. E0 is saturated in the constant ambient: E/E0 is a line bundle and E itself is saturated. It is therefore also saturated in C tensor O. The actual coefficient map of E/E0 surjects onto H/C because E spans H; its domain is Sym8 W=P+D, giving m>=21 without any completeness assumption about the octic yet.

Since C is constant, the derivative of E0 has the same rank there as in H. The actual annihilator duality gives B0 into A(-6), retaining any torsion cokernel. Thus deg L0>=-28. Minimality gives H0(S0)=0 and hence strict negativity. The repeated coherent graded injections into A(-6-2j) and termination by the negative-horizontal argument give, for n>=4, deg L0<=-8q1-10(n-q1)<=-10n+6<=-34. This contradiction is valid for every admissible filtration; it does not scan possible heights or replace images by saturations. Thus m<=22. The only quotient dimensions of P+D are 0,4,5,9, so the required dimension eight or nine must be nine, giving m=21.

The octic coefficient map becomes an isomorphism after projection to H/C and is consequently injective itself. Its image J is a genuine constant complement of C. This is the key geometric distinction: the proof obtains a connection-preserved ambient splitting from actual coefficient spans, rather than assuming an ordinary source splitting is horizontal. The actual E inclusion then does split into E0 in C and the octic in J.

Only at this point is the octic known complete. Its annihilator Sym7 W(-1), derivative kernel Sym6 W(-2), and everywhere quotient O(6) are the canonical Veronese statements. The first-jet assertion is justified uniformly by H1(O(8)(-Z))=H1(O(6))=0 for every length-two subscheme Z. The resulting original transpose is actually block diagonal, with zero-defect octic block. Hence its original t=0 is exactly the small transpose defect, not merely a comparison of abstract splitting types. The actual injection B0 into A(-6) is an everywhere isomorphism. The resulting ranks 5,2 and endpoint degree -28 are correct.

## 3. Cohomology and exhaustive rank-two splitting

The octic annihilator is acyclic, so H1(S0)=M2. Both S0 and B0 are negative; the cohomology exact sequence therefore determines H1(L0)=M2-H1(B0)=V+2P+3D. Serre duality with the fixed determinant convention identifies H1(B0) with H0(A(4)). This does not presume an unproved vanishing for L0.

Finite-group equivariant splitting and center parity are used correctly. A rank-two irreducible coefficient block would have odd coefficient parity but average line degree -14, so it cannot occur. The remaining possibilities are the seven unordered even scalar partitions of 28. The stated forbidden trivial or A constituents are correct for j=2,4,6,8,12,14; j=10 gives exactly Sym8+Sym16=V+2P+3D. Therefore L0=O(-10)+O(-18). This is a fixed rank-two partition argument, not a large bundle search.

## 4. Actual derivative and saturation

The U=O(-10) and T=O(-18) summands are saturated lines in the constant ambient, since both successive bundle quotients are locally free. If the actual U row vanished modulo L0, its own derivative would factor through O(-20), which is impossible by degree. For T, the corresponding internal target is O(-12), and the equivariant Hom is the invariant space in Sym6 W, which is zero. Thus the two rows are nonzero without assuming that either splitting summand is horizontal.

The U row is a scalar multiple of the canonical dual quadratic evaluation and is a saturated line in A(-8). Generic dependence would force the T row to factor regularly through that saturated line: the quotient is torsion-free, so generic vanishing is global vanishing. But Hom_G(T,U) is the invariant space in Sym8 W, also zero. Thus the combined actual map has rank two generically and is a sheaf injection.

For its saturation Ibar, det Ibar has degree -28+d. The nonzero determinant map into wedge2 A(-8)=A(-16) gives d<=12. The defect is an actual effective G-invariant divisor, so d>0 requires d>=12. At d=12 the unique linearization of O(-16), using perfectness of G, would give an invariant vector in A. There is none. Hence d=0, and the actual map has rank two at every point. The cokernel is an equivariant O(4), not a line plus hidden torsion. This disposes of both generic-rank and saturation gaps.

## 5. Intrinsic jets and the actual forward transform

Twisting the saturated derivative image by O(2) gives an actual saturated rank-two N in B0 with quotient O(6). Its preimage M in S0 is the saturated first forward transform; saturation also holds in the constant ambient because S0 itself is saturated. Rank M=4 and deg M=-52 follow directly.

The dual differential-evaluation map P1(L0*)* into the constant C* bundle is intrinsic: it is obtained by taking jets of the coefficient sections coming from constant covectors. It does not presume that these sections form a complete linear system. Its generic image is precisely the first derivative span. The universal identity gives source W(-9)+W(-17), rank four and degree -52. Since M is saturated, the map factors regularly through M. A generically invertible map of equal-rank bundles of equal degree has no determinant zeros, so it is an everywhere isomorphism. This validates the actual forward-transform splitting rather than merely an abstract candidate with the same invariants.

## 6. Joint coefficient span and individual alternatives

Let C' be the constant span of L0. It contains M because it is constant and therefore contains derivatives of L0. The composite S0 into the trivial quotient C*/C' factors through the actual positive line S0/M=O(6). That composite is zero because Hom(O(6),O)=0. Thus C' contains the span of S0.

The latter span is all C*: a nonzero constant vector annihilating every S0 fiber would lie in every E0 fiber, giving a nonzero section of E0, contrary to its negative splitting. This is the needed actual coefficient-span argument; it is stronger than comparing dimensions. It proves surjectivity of Sym10 W plus Sym18 W onto C*.

The original dual exact sequence gives H*=2A+2V+2P+2D. Removing the proven J gives C*=2A+2V+P+D. The two coefficient domains are A+V+D and A+V+2P+D, so semisimplicity identifies the kernel representation as P+D. The final proof correctly clarifies that this is an equivariant isomorphism type, not a selected or canonical embedded kernel.

Surjectivity makes the full two-copy A and V multiplicity maps invertible, so each scalar curve retains its own A and V and the respective copies are independent. Only the degree-eighteen curve contributes P and it retains one of its two domain copies. Exactly one D copy survives in the joint image; either or both curve maps may be nonzero on D. If both are, their image intersection is precisely the unique constant D; if not, the images are disjoint. These are all and only the stated individual span alternatives. Neither curve is silently promoted to a complete coefficient system.

## 7. Scope and verification limits

The accepted conclusion concerns only the actual full-positive coherent-image branch. It excludes or realizes no whole K splitting, triplet quotient, maximal profile, or coarse bin. It supplies no higher-order realization, algebraicity, generic rank-five bound, or original-repair claim. The decomposable W-positive branch and the other triplet coherent-image branches are unaffected. No selected actual HM/source-instance coefficient, point, jet, tensor, matrix, or rank was evaluated; only fixed representation characters and symbolic degree arguments were used.

The separate original-endpoint corollary requested during review is also valid, without changing the frozen proof: L=L0+Sym6 W(-2), beta_L has rank three everywhere, and L^-=Sym5 W(-3)=T6(-3). The octic statement uses universal second-jet separation of its already-proven complete system; the L0 component has zero derivative kernel by Section 4 above. This corollary is not needed for acceptance of the main theorem.

The portable checker is deliberately limited to `PROOF.md`, `INPUTS.json`, the seven retained inputs, and its own explicit small arithmetic data. Freshness of the original connector reads is a provenance record, not something an offline hash checker can recreate. Fail-closed mutation tests confirm that changed proof bytes, changed input bytes, and changed input-manifest data are rejected in both ordinary and optimized Python. No GitHub write was performed by this reviewer.
