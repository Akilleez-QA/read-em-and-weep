# Read em and weep

Research notes and reproducible experiments toward repairing withdrawn OpenAI mathematics manuscripts.

## Scope and status

This repository tracks work in progress. No complete repair of any withdrawn manuscript is claimed.

Primary target: algebraicity of Weil classes on split abelian eightfolds, with potential implications for the withdrawn Kuga–Satake and products-of-K3 manuscripts. A result about one special field or one special abelian variety is not a proof of the original theorem.

Reference source: [openai/math at adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a).

## Focused contributions

1. Explicit normalized Horrocks–Mumford pullback on a fixed abelian fourfold, with an algebraic atlas and exact matrix checks.
2. A finite line-complex model for derived endomorphisms, with executable integer certificates for all deck-character sectors.
3. A smooth 87-parameter family and an injective Kodaira–Spencer map.
4. Reduction of a second-order quantization test to an obstruction class, including a lift-independent full-sign component.

Each contribution should have its own small PR, stating assumptions, reproducible checks, limitations, and remaining tasks.

## Current boundaries

- The candidate has discriminant square class 15. Other imaginary quadratic fields are not covered.
- The isolated second-order obstruction has not yet been evaluated.
- The exact Ext¹ dimension is 87. Combined with the smooth-family injection, this gives vanishing of all ordinary fixed-base Yoneda squares; the ambient obstruction remains a separate question.
- Passing finite computations does not establish all-order quantization or a global algebraic-cycle construction.
- The original theorem requires every specified field, polarization, and member of the family.

## Evidence conventions

Distinguish a proved implication, an exact computation in a specified model, an independently reviewed argument, and a conjectural next step. Rerunning the same code demonstrates reproducibility; it does not independently validate the model.

Every experiment records its input, expected signal, exact output, interpretation, and failure boundary. Failed and superseded routes remain in the record with their corrections.

## Publication gate

Tracking PRs belong to this fork. An upstream solution submission requires a complete checked proof of the stated theorem.

## Tracking PRs

- [#2: carrier and atlas](https://github.com/Akilleez-QA/read-em-and-weep/pull/2)
- [#3: smooth-family proof](https://github.com/Akilleez-QA/read-em-and-weep/pull/3)
- [#4: order-two obstruction reduction](https://github.com/Akilleez-QA/read-em-and-weep/pull/4)
- [#5: exact Ext certificates](https://github.com/Akilleez-QA/read-em-and-weep/pull/5)
- [#6: geometry/sign history](https://github.com/Akilleez-QA/read-em-and-weep/pull/6)
- [#7: carrier experiment history](https://github.com/Akilleez-QA/read-em-and-weep/pull/7)
- [#8: HM computation history](https://github.com/Akilleez-QA/read-em-and-weep/pull/8)
- [#9: route register and provenance](https://github.com/Akilleez-QA/read-em-and-weep/pull/9)

[Coordination between null and mr. slop](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6093415611).

## Further focused results

- [#10: exact local contractions and SL₂ frames](https://github.com/Akilleez-QA/read-em-and-weep/pull/10)
- [#11: surface-ideal character obstructions](https://github.com/Akilleez-QA/read-em-and-weep/pull/11)
- [#12: local normalized-crossing obstruction](https://github.com/Akilleez-QA/read-em-and-weep/pull/12)
- [#13: three-term line-power exclusion](https://github.com/Akilleez-QA/read-em-and-weep/pull/13)
- [#14: six-chart transitions and 216 exact cocycles](https://github.com/Akilleez-QA/read-em-and-weep/pull/14)
- [#15: exact line-calibration target](https://github.com/Akilleez-QA/read-em-and-weep/pull/15)
- [#16: calibrated algebroid derivation and unfinished comparison](https://github.com/Akilleez-QA/read-em-and-weep/pull/16)

An explicit first-order cochain primitive is now derived coefficientwise in #19, with 6,864 exact point-regression equations including mixed line charts. The complete global comparison and projected ambient second-order obstruction remain unfinished. The whole-obstruction reduction also requires its stated additional hypotheses; the full-sign independence is the narrower checked statement.

- [#17: ordinary formal deformation bases](https://github.com/Akilleez-QA/read-em-and-weep/pull/17)
- [#18: executed scalar refinement comparison](https://github.com/Akilleez-QA/read-em-and-weep/pull/18)
- [#19: explicit first-order lift and exact regressions](https://github.com/Akilleez-QA/read-em-and-weep/pull/19)
