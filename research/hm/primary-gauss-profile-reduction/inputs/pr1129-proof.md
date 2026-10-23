# The canonical primary cubic block is visible in the actual Gauss quotient

## 1. Exact setting and immutable inputs

Work over C on the original negative parameter line T=P(W*), with the fixed physical G=SL2(F5) marking and determinant convention. Let E be the ACTUAL saturated subbundle of the constant thirty-space H O, Q=(H O)/E, and beta_E:E -> Q(-2) its second fundamental form for the constant connection. Put K=ker(beta_E) and A_q=E/K. The latter is the locally free actual image quotient: A_q injects as a sheaf into Q(-2), but its image need not be saturated there.

All seven full public originals are included unchanged and authenticated in INPUTS.json. The substantive inputs are:

- ACTUAL and POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE at db51525015bb7c5e825833d550d08dedf6f6ea96: this precise E is saturated in the constant plane-section bundle, and the original multiplication construction identifies its actual second fundamental form. We do not replace this inclusion by the canonical terminal-pencil inclusion.
- PR1124, 48396766d4e61a9de2455b1d068ba8abe09e05f3, research/hm/primary-negative-summand/PROOF.md, Sections 2–4: the actual primary maps construct a canonical saturated subbundle C=U O(-3) in this same E, U=W'+T6; its ACTUAL quotient E/C has H0((E/C)(1))=0, hence all its splitting degrees are at most -2. This quotient bound is not inferred from negativity of E: quotients need not preserve that bound.
- The strict-top source at db51525015bb7c5e825833d550d08dedf6f6ea96 supplies the familiar horizontal-negative-subbundle contradiction. We give the required stronger coefficient-wise argument independently below.
- The 182-cover note and its fixed original quotient list at that same commit provide the original stable row identities and ordered quotient splittings. Their geometric necessity is an imported earlier theorem; the finite JSON is not itself a proof of coverage.
- The elementary binary-icosahedral character source at the same commit supplies the physical irreducible convention and exact character table. The new checker independently verifies the tensor-by-W table from those character values rather than executing its other calculations.

The construction of C and its actual quotient is independent of the rank-three ledger. We do not use an ordinary complement, a horizontal projector, positive-coordinate compatibility, or a Q-compatible split.

## 2. General near-top coefficient visibility lemma

Let F be a saturated subbundle of a constant bundle H O on P1. Let C=U O(-d-1) be a saturated subbundle of F, where d>=0, and assume every splitting degree of F/C is at most -d. Then the coefficient map induced by the actual derivative is injective:

    U=H0(C(d+1)) -> H0((H O/F)(d-1)).                 (1)

Proof. Suppose a nonzero vector u of U is killed by (1). It defines the line L=Cu O(-d-1) inside C. The quotient C/L=(U/Cu)O(-d-1) is locally free. Since F/C and H O/F are locally free, successive extension sequences show that L is saturated in F and in H O. Moreover

    0 -> (U/Cu)O(-d-1) -> F/L -> F/C -> 0.

Twisting by d-1, both outer terms have zero H0. Thus H0((F/L)(d-1))=0. Equivalently every degree of F/L is at most -d. No choice of splitting of this sequence is needed.

The equation beta_F|L=0 says that the second fundamental form of L lands in the internal subbundle (F/L)(-2) of (H O/L)(-2). But

    Hom(L,(F/L)(-2))=H0((F/L)(d-1))=0.

Hence beta_L=0. Its Grassmannian classifying map has zero differential, so is constant over characteristic zero. Since L is saturated, it is the constant line subbundle, and has degree zero. This contradicts deg L=-d-1<0. Thus no nonzero u is killed, proving (1).

This is an injection of coefficient/global-section spaces. It is NOT fiberwise injectivity of C -> (H O/F)(-2), and gives no lower bound dim(U) on its generic fiber rank. The argument is related to the previously used near-top W' argument, not a claim that the horizontal-negative-subbundle method is new.

## 3. The actual primary block is visible in A_q

Use F=E, d=2 and the canonical C from Section 1. The derivative factors through the actual quotient A_q, so its restriction gives

    U O(-3) -> A_q -> Q(-2).

After twisting by three, the composite on H0 is injective by (1). The first map must therefore be injective as well. Equivariance yields the necessary representation inclusion

    W'+T6 embeds in H0(A_q(3)).                      (2)

The result holds for the actual derivative regardless of its generic rank. If the generic rank is three, it restricts the actual rank-three quotient splitting A_q. It does not use COV or a rank-three source specialization.

For example, A_q=W' O(-1)+O(2) is impossible: its cubic section space is

    W' tensor Sym2 W + Sym5 W = 2T6,

which contains no W'. Likewise O(-8)+O(2)+O(6) has cubic sections S4+2T6, also missing W'. These are exact equivariant quotient exclusions, not claims about arbitrary bundles lacking the actual connection and canonical primary input.

## 4. Exact bounded consequence for the original 182 rows

Each fixed row supplies the full ordered splitting of A_q. Formula (2) can therefore be checked by

    H0(A_q(3)) = sum_(e,R in A_q) R tensor Sym^(e+3) W,

where a negative symmetric-power index contributes zero. Multiplicities, including repeated line blocks, are retained. The proof of necessity is (2), not the row arithmetic.

Of the original 159/10/13 rows in profiles 11/12/21, respectively, precisely 25/1/4 fail (2). Thus 30 original labels are impossible by this one direct actual-primary criterion, while 134/9/9=152 original rows pass it. The exact cut, full cubic characters, and missing constituents are in RESULT.json. Every rejected row lacks W'; none merely lacks the T6 multiplicity.

These are cuts of a fixed HISTORICAL necessary list. They are not 30 newly live frontier exclusions and cannot be added to subsequent ledger counts. Passing (2) is only a necessary condition, never realization. The surviving152 are not a claimed new complete frontier independently of the imported182-cover theorem and its profile-exhaustion hypotheses.

The checker does not rerun the historical source or quotient enumeration. It evaluates one new necessary character condition on the fixed182 ordered splittings. Its tensor recurrences use only the9-dimensional representation ring and degrees at most31, not selected HM/source coefficients, points, parameters, tensors, jets, matrices, actual-instance ranks, or scans.

## 5. Contribution and unresolved coverage

This provides a direct geometric bridge from the canonical ACTUAL primary subbundle to the ACTUAL Gauss quotient, without confusing the two distinct ambient pencil inclusions. It supplies a rigorously derived necessary quotient condition and concrete exclusions that can shorten a fresh coverage audit.

It does NOT establish rank(beta_E)=3 implies E is E10/E13/E14. The rest of the original182 coverage reductions and actual-source transfer still require proof or separately authenticated imported theorems. No global rank-three exclusion, rank-four lower bound, maximal rank, original fourth/fifth obstruction value, full-adjoint invertibility, smoothing, algebraicity, or original theorem repair follows from this packet.
