# Independent review: secondary quotient splitting

Verdict: PASS within the stated immutable-input scope. No proof revision required.

Reviewed exact artifacts:

- PROOF.md SHA256: f0eb53bd49cbbb8da9a030ec253e92304dfc3110b7a3b0ced577c460fcb9641f
- verify.py SHA256: b9c78503823b1c181fa99f0305b727bbcaabfc69e91b6fc699bf31ff81d647dd

The copied SQUARE and SECOND inputs were read directly. Their bytes, SHA256 values, and Git blob identities match INPUTS.json under both checker runs. This review verifies the local inputs and their mathematical interfaces; external repository provenance was supplied by the parent’s separate immutable-source authentication.

## Mathematical audit

1. SQUARE equations (6), (7), and (9) retain the actual maps, twists, surjectivity, and quotient identification. On T=P(W*), H0(O(2))=Sym2 W=A. Thus the coefficient representation for f is Hom_G(P+D,A tensor A), not Hom_G(P+D,A) or an untwisted fiberwise substitute.
2. Lambda2 A=A and A tensor V=P+D, whereas A tensor A=1+A+D. The P block therefore vanishes; the D coefficient space is one-dimensional. The actual surjectivity of f excludes scalar zero, so its D kernel equals that of y tensor O(2). The resulting actual quotient is P O(2) directsum W O(-1), with rank six and degree six.
3. Standard linearizations are consistent: the center acts trivially on the P O(2) summand and also on W O(-1). No hidden determinant character appears, since det W is trivial. The same fact removes a determinant correction from equivariant Serre duality.
4. The positive summand is exactly the maximal-slope Harder–Narasimhan subbundle. The equivariant space of differences of splittings vanishes by W tensor Sym3 W=A+D, which contains no P. The proof correctly distinguishes uniqueness of the equivariant complementary subbundle from uniqueness of a named direct-sum isomorphism. Ordinary complements have a 32-dimensional difference space.
5. SECOND theorem (2) supplies the actual injection K into H0(B_R(3)) O, not merely a numerical condition. A split pullback over P O(2) would inject a positive-degree bundle into this trivial bundle, contradicting H0(O(-2))=0. The P-extension is therefore genuinely nonzero even after forgetting equivariance, and the whole K extension is nonsplit.
6. In characteristic zero for the finite group G, equivariant Ext is the invariant part of ordinary Ext. Serre duality gives H1(O(-8))=Sym6 W dual and H1(O(-5))=Sym3 W dual. Self-duality of the named representations gives the displayed Hom formulas. A tensor P=V+P+D and Sym6 W=V+P give dimension two; A tensor W=W+Sym3 W gives dimension one. These computations do not determine either a projective direction in the first extension space or the actual second component.
7. The remaining-boundary section correctly disclaims any computation of the secondary map or its rank/kernel, any splitting of K, and any actual quadric section conclusion.

## Independent checks

- Ran python verify.py: PASS.
- Ran python -O verify.py: PASS.
- Independently checked the abstract-character identities in exact Q(sqrt(5)) arithmetic using a separate existing nine-class character implementation, including Lambda2 A=A, A tensor V=P+D, A tensor A=1+A+D, W tensor Sym3 W=A+D, A tensor P=V+P+D, A tensor W=W+Sym3 W, and both Ext dimensions.
- The verifier uses explicit require checks, so optimization does not disable its tests. It evaluates only fixed abstract character data and immutable-file identities, not actual HM/source coefficients, points, derivatives, selected matrices, or instance ranks.

The checker corroborates the bounded representation arithmetic and input integrity. Actual-map identification, canonical HN reasoning, and forced nonsplitting are supplied by the structural proof and the audited immutable-input interfaces, not inferred from the checker alone.
