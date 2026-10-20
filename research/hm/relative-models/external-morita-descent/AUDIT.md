# Bounded independent audit

Audited `PROOF.md` and the revised `MIXED_OBSTRUCTION.md` on 2026-10-19. This is a mathematical audit of the displayed conditional statements. It does not independently verify the linked source comments, construct the supplied Morita data, or identify a physical ambient.

## Verdict

**Pass under the stated hypotheses.** No unresolved mathematical error was found in the algebraic coefficient-square theorem, its framed-module version, the specified completion theorem, or the ordinary sheaf-of-algebras obstruction calculation. The revised addendum correctly separates its explicit ordinary matrix formulas from the conditional comparison of a separately supplied algebroid defect complex.

## Checks performed

1. **Independent-group invariants.** Equations (1)–(2) follow from the tensor product of Reynolds idempotents, including for infinite-dimensional vector spaces. The proof correctly excludes both diagonal-group substitutions and arbitrary balanced invariant tensor comparisons.

2. **External overlaps and frames.** The balanced interchange map (5) and its reverse are well-defined. Product overlap invertibility, associative composition, and factorized module frames follow from the stipulated factor data. The nonfactorized module assertion (7) uses the supplied invariant basis and does not assert a general equivariant-module descent theorem.

3. **Strictification comparisons.** The double average factors exactly in (10). Its invertibility follows from the explicit factor unit hypotheses and the displayed tensor inverse. The separate unit qualification for nonfactorized comparisons is necessary. The example (13) correctly shows why algebraically tensoring complete factor rings does not supply the missing ambient unit hypothesis. The comparisons involving the prior strictification and root-transport theorems remain conditional on their supplied conventions and hypotheses.

4. **Pure and mixed ideals.** Unitality gives both product orders in (15). Tensor exactness over the field gives the intersection and quotient in (16). Reynolds gives the exact sum and reduction assertions. In particular (19) is an actual equality of ideals, and (21)–(22) identify precisely the quotient that removes the mixed ideal. These are stronger, properly justified assertions than a general unsupported claim that invariants commute with ideal multiplication.

5. **Modules and square-zero structure.** Equations (23)–(24) are coefficientwise in the invariant basis. Direct calculation verifies the double-sign boundary example (25). From the two actual square-zero factor ideals, all products in (27) vanish in the asserted order; no invariant-square substitution is used.

6. **Specified completion.** The countable towers of pure, mixed, and sum ideals have surjective transition maps. In particular the kernel tower for the pure-sum map is the mixed ideal tower, which proves exactness at the inverse limit and the closedness assertion (39). The same argument justifies the stated quotient comparisons. Surjective projections of the pure inverse-limit ideals yield the density argument for (40). The proof correctly claims the closed product, rather than silently equating it to the possibly smaller ordinary product. Fixed points commute with the inverse limit, and finite-level Reynolds identifies the induced invariant filtrations. The completed module and balanced-composition assertions retain their necessary fixed-frame and levelwise-definition hypotheses.

7. **Ordinary matrix obstruction.** In the revised addendum, the quotient fiber product assembles the compatible pure transition matrices. The square-zero kernel permits local invertible lifts on the stipulated cover/refinement. Expanding associativity gives exactly (31), and changing lifts by `(1+b_ij)T_ij` gives exactly (32). Thus the stated fixed-cover Čech class and vanishing criterion are correct. The coefficient conjugations depend only on the common classical transitions because the pure augmentation ideal annihilates the mixed ideal on both sides. The supplied equivariant/invariant frames identify the actual coefficient complex, and (34) is the correct ordinary matrix change-of-frame formula.

## Boundaries that must remain in the final claim

- The algebras are unital, the group orders are invertible, and the actions and external presentations are actually supplied.
- The completion uses the explicitly defined countable quotient tower, not an unspecified tensor topology.
- The obstruction calculation presupposes compatible frames and actual local lifts on the chosen cover or a supplied refinement; it makes no unconditional Čech-to-derived-cohomology assertion.
- Equations (29)–(32) are ordinary sheaf-of-algebras formulas. They are not formulas for a general algebroid with its overlap maps and coherence units suppressed. For an algebroid, only the comparison of a separately supplied actual equivariant defect complex is certified here.
- No physical factorization, existence of invariant module frames, particular obstruction value, or retained-value computation is established.

The revised files respect all of these boundaries. No additional correction is required by this audit.
