# Reversal-fixed marked classes

## Result

For the invariant marked ambient continuation categories of PR436 and PR438, the image of the parity forgetful map is exactly the fixed locus of reversal combined with the opposite product, at every finite order and at the coefficientwise formal limit:

\[
\operatorname{im}(J_n)=\operatorname{Fix}(\mathcal I:U_n\to U_n),
\qquad
\operatorname{im}(J_\infty)=
\operatorname{Fix}(\mathcal I:U_\infty\to U_\infty).
\]

Consequently an unrestricted marked formal presentation has a parity normal form if and only if it is marked-equivalent to its reversed opposite. Equivalently, every finite truncation is equivalent to its reversed opposite.

Whenever the lower class has a parity normal form, the next failure is measured by the canonical anti-fixed fiber difference

\[
q_n(u)=\tfrac12(u-\mathcal Iu)\in Q_n.
\]

It vanishes exactly when parity normalization extends to that next degree. On the inversion-equivariant fourfold, \(Q_n\) has dimension 12 for even new degree and 16 for odd new degree.

## New proof step

The proof checks the full noncommutative pentagon, gauge transport, gauge composition, and inner 2-unit orientations. The unit map \(a\mapsto\tau(a^{-1})\) is covariant, and Čech indices are not reversed.

It then identifies the involution on the unrestricted one-step \(HH^2\)-torsor. Full lower-automorphism 2-triviality from PR438 makes this an equivariant calculation on the genuine finite class fiber, not only on lifts of a literal presentation. Induction and the established inverse-limit comparisons give the formal criterion. No coherent square-one condition on the chosen comparison \(x\to\mathcal I x\) is assumed.

## Exact dependencies

- [PR438](https://github.com/Akilleez-QA/read-em-and-weep/pull/438), commit `971c16a67b1e7d12fce0a8e2d2165ca4839911de`: unrestricted lower-automorphism removal, forgetful injectivity, unrestricted inverse-limit comparison, and finite detection of the parity image. This is the natural stack base.
- [PR436](https://github.com/Akilleez-QA/read-em-and-weep/pull/436), commit `502c978a17cd7037d740d4d08d373c1cb8bd5829`: marked parity tower and its inverse-limit comparison.
- [PR425](https://github.com/Akilleez-QA/read-em-and-weep/pull/425), commit `df433cdd359fa9c7750bf9c8b9765229eac534f6`: exact top difference and gauge calculations and the one-step parity image.
- [PR416 literal parity continuation](https://github.com/Akilleez-QA/read-em-and-weep/blob/c71356722bc7bd1a426d26ea0ca6d050f4c3ed81/research/hm/parity-separated-ambient-lifting/REVERSAL-COMPATIBLE-CONTINUATION.md), commit `c71356722bc7bd1a426d26ea0ca6d050f4c3ed81`, retaining the [invariant literal small-extension premise](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725).

The regular normalized differential, arity-zero, individually invariant acyclic-cover, characteristic-zero, abelian inversion, fixed initial marking, and literal lifting hypotheses remain explicit. The general abelian formulation is conditional on the same literal lifting premise; the cited source application is the stipulated elliptic fourfold.

## Files and integrity

- `PROOF.md`: complete argument and source pins.
- `INDEPENDENT-REVIEW.md`: independent mathematical review of the exact proof.
- `ROOT-REVIEW.md`: separate root mathematical review of the exact proof.

The proof SHA-256 is:

`148dd88be35ab5bce6b95005ebef8a9425dbe92bfa8a457dc05f9ce635dfb34f`

This is mathematical text review, not formal machine verification. No mathematical or selected-source computation was run.

## Boundaries

This is a statement about marked object classes, not classification of coherent involutive 2-actions or unmarked objects. It does not identify the unitary and ordinary 2-unit categories, whose scalar 2-automorphisms differ.

The first-order data and all coefficients below the fixed initial order remain literal inputs. The new result concerns higher-order ambient normalization. It gives no uniform bound for the first failing order and no arbitrary fixed-product continuation, module lift, period interpretation, analytic convergence, algebraicity, or six-pure-condition vanishing. No actual HM/source obstruction or detector value is evaluated.
