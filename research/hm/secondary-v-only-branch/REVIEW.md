# Independent structural review of the V-only P-source branch

The complete final PROOF.md, all three exact input originals, INPUTS.json, REPRODUCE.md and verify.py were reviewed. This approval binds PROOF.md SHA256:

    6c30cf1567e938ef280d823803c461b49bb81ec4bc0972b215860c5d86015330

The local input copies match the prior source proofs byte for byte; their byte counts, SHA256 hashes and Git blob identities pass the checker. Both `python verify.py` and `python -O verify.py` pass. The checker performs exact nine-class character arithmetic and source authentication, not actual instance evaluation; its scope is correctly distinguished from the bundle arguments in the proof and reproduction instructions. No selected actual HM coefficient, parameter, point, matrix, rank, derivative or jet was evaluated.

## Verdict

Approved without required mathematical changes. The conditional classification is valid. Under a_D=a_P=0 and a_V nonzero, the full actual map has constant fiber rank 5 if b_P is nonzero, rank 4 if b_P=0 and b_D is nonzero, and rank 3 if b_P=b_D=0. Its cokernel is torsion-free in every case. The proposed original-kernel alternatives and their common cancellation ratio are justified below. No assertion that the actual coefficients select any particular case follows.

## 1. Reduced V-row kernel and constant rank

Write t=b_V/a_V. The established exact P-source channel

    0 -> O(-4) -> P O(2) -> V O(4) -> 0

makes the V row surjective for every t. Its actual kernel E fits into

    0 -> O(-4) -> E -> W O(-1) -> 0.

For t=0 this splits. For t nonzero the class cannot vanish: a splitting would give a lift of the nonzero W-source V channel through P O(2), while Hom_G(W O(-1),P O(2))=0. The relevant equivariant Ext space is one-dimensional. The universal quadratic sequence

    0 -> O(-4) -> A O(-2) -> W O(-1) -> 0

is nonsplit, because a reverse lift would have the forbidden negative twist. Hence E is A O(-2) for t nonzero.

The remaining rows on E are exactly b_P j_P and b_D j_D after the onto projection E -> W O(-1). The established j_P is everywhere injective, and j_D is quartic Veronese after Euler evaluation, of rank one everywhere. Thus the residual ranks are respectively 2, 1 and 0. Adding the V-row rank three gives the asserted constant full ranks. The surjection K -> Q preserves them, and constant rank gives a locally free cokernel, including the additional zero A target row. The canonical cokernel identification in Section 3, equation (5), is also valid: inclusion of the remaining target rows is onto on the quotient after eliminating the onto V row, and its kernel is exactly the image of E, equal to the image of the W-source map because E -> W O(-1) is onto. No splitting of the V row is required. The generic-rank minor ideal is the unit ideal locally everywhere, so the no-degeneracy assertion is scheme-theoretic.

## 2. The actual canonical summand and cancellation ratio

The balanced splitting K=T6 O(-1) plus A O(-2) is canonical equivariantly: the higher-slope part is intrinsic, and Hom_G(A O(-2),T6 O(-1))=0. Let K_A be its A summand. The actual quotient projection q_W kills T6 O(-1) by inequivalence, so its restriction to K_A is onto.

The actual restriction q_P|K_A is nonzero, because otherwise K_A would map into the actual preimage K_W=D O(-4), which is impossible by negative degree. Its composite h0=i_V q_P|K_A is nonzero as well: if zero, q_P|K_A would factor through O(-4), again impossible by negative degree. The composite h1=j_V q_W|K_A is nonzero because q_W|K_A is onto and j_V is injective.

The space Hom_G(A O(-2),V O(4)) is one-dimensional, using A tensor V=P+D and Sym6 W=V+P. Therefore there is exactly one nonzero scalar eta with h0+eta h1=0. The numerical eta depends on the fixed actual quotient and the chosen channel generators. Its cancellation locus is intrinsic; the proof neither computes eta nor proves that the actual t equals it.

The subbundle B=ker(K_A -> W O(-1) -> O) is W O(-3), by the quadratic evaluation sequence. Moreover Hom_G(W O(-3),K) is one-dimensional: the T6 block contributes zero and the A block contributes one copy of W in A tensor W=W+S. Its unique nonzero map is the inclusion of B, up to scalar. Since q_W(B) is the Euler line O(-2), h1|B is nonzero. Thus precisely the same eta detects whether B lies in the V-row kernel.

## 3. Original-kernel extension classes

Set L=A O(-6). If b_P is nonzero, the reduced kernel is the actual P-source line O(-4), independently of t and b_D. Its original preimage is L plus O(-4), because Ext1_G(O(-4),L)=0.

Suppose b_P=0 and b_D is nonzero. For t nonzero the reduced kernel is W O(-3), the kernel of the composite A O(-2) -> W O(-1) -> O. Its original preimage is an extension of W O(-3) by L in a one-dimensional Ext space. It splits exactly at t=eta. Indeed a splitting must be the unique nonzero W O(-3) map into K, whose image is B; conversely at eta the map B to the reduced kernel is nonzero and hence an isomorphism of equivariant W O(-3) bundles.

A nonzero model is obtained by pulling back cubic evaluation

    0 -> A O(-6) -> S O(-5) -> O(-2) -> 0

along W O(-3) -> O(-2). Its middle bundle is O(-4) plus S O(-5): the resulting extension of S O(-5) by O(-4) has zero ordinary Ext. The extension over W O(-3) is nonsplit, since Hom(W O(-3),O(-4) plus S O(-5))=0. This proves the claimed generic original-kernel type.

Suppose b_P=b_D=0. For t nonzero the reduced kernel is A O(-2). Its original preimage is an extension of A O(-2) by L in a one-dimensional Ext space. It splits exactly at t=eta, because Hom_G(A O(-2),K) is one-dimensional and generated by K_A. A nonzero model follows by taking the symmetric square of

    0 -> O(-2) -> A O -> W O(1) -> 0

and twisting by O(-4):

    0 -> A O(-6) -> (1+D) O(-4) -> A O(-2) -> 0.

The kernel in this symmetric-square sequence is the image of O(-2) tensor A O, and Sym2 A=1+D. Negative degree rules out a splitting, so this is the required unique nonzero extension type.

## 4. The t=0 endpoint is retained

When t=0, the reduced V-row kernel is O(-4) plus W O(-1), and Ext1_G(O(-4),L)=0 separates the first summand. The actual preimage of W O(-1) is D O(-4), not an arbitrarily chosen extension model. Thus with b_P=b_D=0 the original kernel is O(-4) plus D O(-4), as claimed away from eta.

If b_D is nonzero, taking the kernel of D O(-4) -> W O(-1) -> O gives S O(-5), by quartic evaluation; hence the original kernel is O(-4) plus S O(-5). The final proof's independent argument also checks: an equivariant splitting of the O(-2) extension would give O(-2) -> K, whereas H0(K(2))^G=(T6 tensor W+A)^G=0. The one-dimensional Ext space and cubic-evaluation model then give the same middle bundle. This agrees with the stated nonexceptional alternative. The endpoint t=0 is distinct from eta because eta is nonzero.

All ranks and degrees agree with the actual source and target exact sequences. The named middle-bundle identifications away from the split locus are equivariant isomorphisms, not claims of canonical summands inside K. The argument preserves the fixed actual quotient, canonical source projections and original kernel pullbacks throughout.

## 5. Bound companion-file identities

    INPUTS.json: 2fff5a307127e342c824d8e008d5406cfdcb94a6f59049ad18b40dc5df6f99ef
    REPRODUCE.md: 10b9ff6a8ad42e85caa02201592d16fa0db382d0f2688b1527f102d23e0e76dc
    verify.py: 7388977a4b9da8504549a7745727f29a73425cb5c4e8c06757bad61264c83da1

The inherited source hypotheses remain in force. FIBER's separate two-nonzero-D-channel assumption is not imported into this new branch; only its unconditional channel constructions are used. Nothing selects the actual secondary coefficients, proves this branch occurs, or closes any global source/catalogue or odd-quadric question.
