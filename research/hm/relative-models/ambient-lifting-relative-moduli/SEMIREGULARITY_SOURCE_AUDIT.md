# Independent source audit: standard semiregularity on the retained sector

PASS, reviewed 2026-10-19.

Source: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259931094 (04:51:33 UTC). Verified the definition and normalization against Buchweitz–Flenner, Introduction pp. 2–3, https://arxiv.org/pdf/math/9912245 . The classical equivariant bundle and supplied Ext representation remain explicit premises.

On the fourfold, only q=0,1,2 can contribute to H^(q+2)(Omega^q). The factor one-form and H1(O) generators both have singleton deck weight. Their two subsets have full sign precisely when disjoint and complementary. Thus 2q+2=4, leaving only q=1. The full-sign target is four-dimensional H3(Omega1).

With the alternating omitted-factor basis in the comment, permutation acts by sign times permutation of four entries. Its character is (4,-2,0,1,0), and its decomposition is sign plus Vsign. In particular there is no U22 constituent. Naturality of the Atiyah class and trace gives equivariance under the stated linearization, so Schur's lemma kills the entire supplied U22 isotype, and therefore each retained line in it.

This is a statement about the natural linear semiregularity map. It does not require, and does not establish, an extension of ordinary sheaf-obstruction vanishing theorems to varying algebroid modules. The comment correctly declines to credit semiregularity with removal of both sign-source copies. It also correctly concludes that a test factoring through this map supplies no condition on the retained U22 sector.

No actual obstruction value, source operation, or detector was evaluated. The prior ambient torsor and local-defect conclusions remain unchanged. No outstanding correction.
