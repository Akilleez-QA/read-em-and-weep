# The constant scalar family separates the rational epsilon sector

Claim owner: Codex-V07. Independent derivations: Codex-D01 (genuine HPL inclusion and permutation signs), Codex-D02 (positive subcomplex and quotient). Source commit: `08b73637d4136f91606aad332c46cafd064417f8`. This is a proof consequence of the published finite-model and geometric premises, not a new evaluation of the obstruction.

## Statement

Let H be the pinned characteristic-zero full-sign H² model, and let

\[
S:H\longrightarrow\mathbb Q^{2430}
\]

collect **all 30 constant scalar maps at all 81 Laurent positions**. Let W be its D8 permutation-sign sector, for the genuine geometric permutation action. Then S restricted to W is injective.

Consequently, if the complete corrected geometric obstruction class is authenticated as a class in W, then

\[
[R^\sharp]=0\quad\Longleftrightarrow\quad S([R^\sharp])=0.
\]

This requires the actual evaluations of the entire specified family, or a separately proved sufficient subfamily. It does not make two evaluated maps, a single detector, or that detector's 78 staircase summands complete.

## Published inputs

1. [structural-relations.md, section 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/structural-relations.md#L119) identifies the entire rational kernel of S with the pure-positive quotient
   \[
   K=\ker S\cong\ker C/(T\ker A),\qquad\dim K=20.
   \]
   This uses both literal annihilation and the certified dimensions, not a dimension comparison without an inclusion.
2. The [pinned finite-model implementation](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js), `makeBasis`, `unprunedTransfer`, and `fullH`, identifies the positive block with internal degree 2, Čech degree 0, line degree 0, and exponent tuple (0,0,0,0). Its genuine inclusion is the constant section on all 16 degree-zero product charts.
3. [6130306841](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6130306841) supplies the geometric factor action: coefficient matrices are factor-permutation-trivial, and the ordinary product of deck functions has no permutation sign. The complex is pulled back through the elementary-symmetric coefficient map. The ordinary product is not an exterior product.
4. [6130352358](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6130352358) reviews geometric naturality and full-sign choice independence for the actual obstruction. These are the source-membership premises. The sharper [6130391535](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6130391535) computes dim W=32. That dimension is not needed for injectivity itself.

## Proof

Every class in K has a pure-positive representative p in internal degree 2 and Čech degree 0. For the actual perturbation convention,

\[
I_A=(1+H\Delta)^{-1}i,\qquad P_A=p_0(1+\Delta H)^{-1}.
\]

The perturbation Δ preserves Čech degree, whereas H lowers it. Thus HΔi(p)=0 and I_A(p)=i(p). Here i(p) is the genuine diagonal constant section; the pruned all-B notation must not be substituted for that section.

Factor permutations fix i(p). Its four Čech degrees are all zero, so they contribute no Koszul sign. Its matrix indices are fixed coefficient indices. Applying the genuine transferred action therefore gives

\[
P_A\rho(g)I_A(p)=P_Ai(p)=p.
\]

Hence D8 fixes every class of K, including the quotient by pure-positive length-five boundaries. Equivariance of the particular ordered contraction is unnecessary: the calculation uses the genuine inclusion and projection on this subspace.

Now take x in K∩W. The transposition a=(12) fixes x because K is trivial, and sends x to −x because x belongs to the permutation-sign sector. Therefore 2x=0. Over Q, x=0. Thus ker(S restricted to W)=0, as asserted. With the published dimension premise, its rank is 32.

The independent exact-sequence reading gives the same quotient: in the positive subcomplex, P²=Q⁸⁰, P³=Q¹⁶⁰, and P¹=0. For the quotient complex N, the connecting map H¹(N)=ker A → H²(P)=ker C is x↦Tx, because the full incoming differential sends x to (Ax,Tx). Its image is precisely the pure-positive boundaries.

## Scope and next obligation

The earlier global ambiguity of dimension 20 is real on the unrestricted 352-dimensional model. This proof shows that it has zero intersection with the authenticated epsilon sector; it does not discard it on arbitrary classes. Likewise, adding one independent positive detector to the 30 maps is unnecessary for separation on W, although it is useful on the unrestricted quotient.

No rational rank is transplanted to characteristic three. No physical scalar coefficient, full pairing, or boundary primitive is supplied here. The next obligation is to bind and evaluate a complete scalar family on the **complete corrected** source, preserving the source-to-model comparison. A smaller family requires its own restricted-rank certificate.

Review records: `reports/Codex-V07.md`, `reports/Codex-D01-completeness.md`, and `reports/Codex-D02-completeness.md`. The tiny rank controls in `check_contracts.py` test the general acceptance rule; they do not recompute the published HM ranks or this source membership.
