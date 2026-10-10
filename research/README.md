# Read em and weep

Research notes and reproducible experiments toward repairing withdrawn OpenAI mathematics manuscripts.

## Scope and status

This repository tracks work in progress. No complete repair of any withdrawn manuscript is claimed.

Primary target: algebraicity of Weil classes on split abelian eightfolds, with potential implications for the withdrawn Kuga–Satake and products-of-K3 manuscripts. A result about one special field or one special abelian variety is not a proof of the original theorem.

Reference source: [openai/math at adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a).

## Focused contributions

1. Explicit normalized Horrocks–Mumford pullback on a fixed abelian fourfold, with an algebraic atlas and exact matrix checks.
2. A finite line-complex model for derived endomorphisms, with executable integer certificates for selected deck-character sectors.
3. A smooth 87-parameter family and an injective Kodaira–Spencer map.
4. Reduction of a second-order quantization test to an obstruction class, including a lift-independent full-sign component.

Each contribution should have its own small PR, stating assumptions, reproducible checks, limitations, and remaining tasks.

## Current boundaries

- The candidate has discriminant square class 15. Other imaginary quadratic fields are not covered.
- The isolated second-order obstruction has not yet been evaluated.
- The total Ext¹ calculation reports dimension 87; independent reconstruction and the resulting smooth-family comparison are under review.
- Passing finite computations does not establish all-order quantization or a global algebraic-cycle construction.
- The original theorem requires every specified field, polarization, and member of the family.

## Evidence conventions

Distinguish a proved implication, an exact computation in a specified model, an independently reviewed argument, and a conjectural next step. Rerunning the same code demonstrates reproducibility; it does not independently validate the model.

Every experiment records its input, expected signal, exact output, interpretation, and failure boundary. Failed and superseded routes remain in the record with their corrections.

## Publication gate

Tracking PRs belong to this fork. An upstream solution submission requires a complete checked proof of the stated theorem.
