# Independent whole-proof review: constant octic complement and defect twelve

## Scope and evidence

This audit checks the complete final proof for exactly the two decomposable positive quotients F=O(2)+2O(4) and F=W O(3)+O(4). It does not treat A_std O(4)+O(-8), assert realization, or assume a connection-compatible Birkhoff splitting.

The prior image proof was read in full and its SHA256 independently checked as db1e23909dbabd423cbeb855f0f376e7e0fac53d557fdd8aef7685b5449edfdb. The pinned actual source and capacity proofs were also read. Their SHA256 values are a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256 and c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af. These input proofs remain imported geometric premises, not machine-certified facts.

## 1. Minimal constant span and actual complement: PASS

Let C be the actual minimal constant span of E0, and m=dim C. C is G-invariant. E/E0=O(-8), so the original span hypothesis on E gives a surjective coefficient map Sym8 W -> H/C. In particular m>=21.

The bundle S0=(C O/E0)* is saturated in C* O, has rank m-16 and degree -46, and is strictly negative: a constant subbundle of S0 would be a nonzero constant functional annihilating E0, contrary to minimality of C. Transposition preserves the generic rank three of beta_E0. Let L0=S0^- and B0=S0/L0. Then rank L0=m-19, rank B0=3, and the actual transpose induces a coherent injection B0 -> F*(-2). It follows that degree B0<=-16, degree L0>=-30, and top B0<=-4.

The successive actual saturated derivative kernels of L0 have coherent quotient injections into B0(-2j); their ranks are at most three. Their chain terminates because a nonzero saturated horizontal subbundle of the negative S0 would be constant. If rank L0=n>=5, the capacity is at most -4n-sum_i h_i(h_i+1), with three nonincreasing nonnegative heights summing to n. At n=5 this is at most -20-14=-34, and adding boxes only decreases it. This contradicts degree L0>=-30. Thus m<=23.

The semisimple quotient H/C of Sym8 W=P+D has dimension 7, 8, or 9. Its only possible dimension in this range is 9, hence m=21. The coefficient map of the actual chosen O(-8) source summand has nine-dimensional image J and projects isomorphically to H/C. Therefore J intersects C trivially, H=C direct sum J, and the actual source inclusion is E=E0 direct sum O(-8) inside the corresponding constant direct sum. The complement is derived from the actual source map; it is not merely an abstract bundle splitting.

## 2. Tail derivative, original defect, and cohomology: PASS

The coefficient identification J=Sym8 W makes the tail the complete degree-eight Veronese line. Its annihilator S_tail is Sym7 W tensor O(-1), so it is acyclic. The derivative of this complete linear system is nowhere zero, equivalently first-jet evaluation is surjective: H1(O(6))=0 ensures separation of every length-two subscheme. Consequently the dual derivative is onto O(6), its kernel is Sym6 W tensor O(-2), and its rank-one determinant defect is zero.

The decomposition of the constant ambient is preserved by the constant connection. Hence S=S0 direct sum S_tail, S^-=L0 direct sum S_tail^-, and S/S^-=B0 direct sum O(6). The original transposed rank-four derivative splits as the rank-three E0 transpose plus the defect-free rank-one tail map. Thus the original determinant defect is exactly the length t of Z in

    0 -> B0 -> F*(-2) -> Z -> 0.

This proves degree L0=-30+t. No defect has been discarded by saturating an image. The exact top triples for F*(-2) are (-4,-6,-6) and (-5,-5,-6). The only rank-two height patterns are (2,0,0) and (1,1,0); their maximum capacity is -14 in both cases. Therefore t<=16. The determinant divisor is A5-invariant. A projective A5 point stabilizer is cyclic, and its possible orders are 1,2,3,5; thus positive orbit sizes are 60,30,20,12. It follows that t is 0 or 12.

The original acyclicity identity gives H1(S0)=H1(S)=M2. Since B0 injects into the negative F*(-2), H0(B0)=0. From 0 -> L0 -> S0 -> B0 -> 0 one gets an exact sequence 0 -> H1(L0) -> M2 -> H1(B0) -> 0. From the displayed torsion sequence one gets 0 -> H0(Z) -> H1(B0) -> H1(F*(-2)) -> 0. Serre duality and self-duality of the representations identify the last term with H0(F)=A+2D. Therefore

    H1(L0)=2V+3P+2D-H0(Z)

as an equality in the representation ring with genuine left side. This is not a presumed exact sequence between H0(F) and M2. Negativity gives H0(L0)=0, and strict top for the actual kernel also gives top L0<=-2.

## 3. Closed character checks and all five torsion weights: PASS

The companion script uses the closed symmetric-power character polynomial sum_j (-1)^j binom(n-j,j) x^(n-2j), exact arithmetic in Q(sqrt5), and the nine binary-icosahedral conjugacy classes. It does not use the parent's symmetric-power recurrence or inspect any actual coefficient, parameter, point, jet, tensor, matrix, or instance rank.

At t=0, rank L0=2 and degree L0=-30. Center-even equivariant splitting permits only W(-15), W'(-15), or the seven unordered even scalar pairs with positive degrees (2,28), (4,26), (6,24), (8,22), (10,20), (12,18), (14,16). Both doublets have a trivial H1 constituent; every scalar pair has an A constituent. These are absent from 2V+3P+2D. The potentially misleading individual Sym16 has no A, but in the (12,18) pair its companion Sym10 does have A. Thus t=0 is impossible.

At t=12, Z is supported on a single reduced twelve-point orbit, with one-dimensional fibers. The central involution acts trivially, so all five fiber characters are those of a C5 stabilizer in A5. Choose its generator so physical A=Sym2 W has weights 0,1,4. The other restrictions have residues V:0,2,3; P:1,2,3,4; D:0,1,2,3,4. Frobenius reciprocity gives the following complete list:

- weight 0: 1+A+V+D;
- weight 1: A+P+D;
- weight 2: V+P+D;
- weight 3: V+P+D;
- weight 4: A+P+D.

Only weights 2 and 3 leave a genuine H1(L0). They have the same induced representation but must not be identified as equivariant torsion sheaves. Necessarily H1(L0)=V+2P+D and degree L0=-18.

There are exactly four unordered even scalar pairs, (2,16), (4,14), (6,12), (8,10), together with W(-9) and W'(-9). The first three scalar pairs and W'(-9) contribute 1 or A. Exactly W(-9) and O(-8)+O(-10) have H1=V+2P+D. This establishes necessary bundle types, not existence or exclusion of either.

## 4. Original dual endpoint and exact-text audit: PASS

The complete eight-section PROOF.md was read after publication of its local draft. Its SHA256 is 95cc7824898dd0bffe13f86ab1ede2947451eb3d4632e189baa608ad0de3fdec. The preceding proof audit applies to this exact text, including the complete first-jet separation proof, all five stabilizer weights, and the distinction between the two surviving torsion sheaves.

The actual text uses an even simpler valid capacity bound for rank n>=5: the first graded piece has degree <=-6q1 and each later piece has degree <=-8qj, hence total degree <=-8n+2q1<=-8n+6<=-34. This accounts for all ranks by termination of the actual negative-kernel chain. It has no extra saturation assumption.

The original dual endpoint conclusion also follows: Sym6 W=V+P, so L=S^- is (V+P)(-2)+W(-9) or (V+P)(-2)+O(-8)+O(-10). Both have rank nine and degree -32. The actual original quotient has b=-22, consistent with -54-b=-32, and t=-8-a-b=-8-2+22=12. The proof's repeated conditional/necessary language correctly prevents these conclusions being read as realization or exclusion results.

All three inputs have now been freshly fetched through the GitHub read-only file tool at their exact immutable commit/path identities. Complete decoded remote bytes equal the retained inputs, with byte lengths, SHA256 values, and recomputed Git blob SHA1 values all matching. The pair-image input is authenticated at commit 972993db6a0ab4f2a65f4f8da39cd3862923238d and Git blob 12cbf71fd50a623cc5e7daa4fcc3835bd016d460. See REVIEW-AUTHENTICITY.json for the complete records. This is full-byte authentication, not a check of metadata or selected excerpts.

## Status and reproduction

Whole-proof review: PASS. No mathematical correction or unresolved blocker was found. No public write, merge, upstream submission, selected actual instance, or broad candidate scan was performed.

Run python review_verify.py from any directory, or run python -O review_verify.py. The independent checker uses no author character module, performs 528 checked assertions with optimization-safe explicit conditions, and emits the full arithmetic/source-authentication JSON. The retained ordinary and optimized results are identical. The geometry is independently reviewed mathematical prose, not a machine proof-assistant certification; the original actual-geometric premises remain imported.
