# Selected full-owner E12 lowering: conditional exact representation

The new `lower_selected_kernel_denominators.py` lowers all four normal-ordered E12 terms for seed 4, row 2, staircase (3,11,15), at full labels

- a=(seed4, occurrence0, carrier1, legal12, standard3)
- b=(seed4, occurrence1, carrier2, legal13, standard11)
- c=(seed4, occurrence2, carrier4, legal15, standard15).

These labels form a structurally active candidate, not a proved nonzero weight or coefficient. They are source-first with positive sorting sign. The masks obey the finite-coordinate active-weight restrictions and retain nonzero logarithmic frame terms. This is one selected full-label sector, not an entire symbolic branch family. The prior carrier123 candidate is excluded: its endpoint partition weight is zero on standard15. A regression test requires this zero and distinguishes the carrier124 candidate without asserting any coefficient value is nonzero.

## Exact lowering and pinned certificate reliance

The current inverse is rewritten as C_ab^-1=C_ba, where C_ab=(P_a I_b)^t. The proof uses P_a I_a=Id, d I_a=0, P_a d=0 and I_b P_b=Id-dH_b-H_bd. Both multiplication orders are necessary before transposing. No determinant-one shortcut is used. The existing pinned homogeneous identity certificate and historical checker were inspected read-only. Their recorded four identities and canonical model hash match the authenticated model. The lowering binds both file hashes and the canonical model hash and relies on that existing certificate; it does not rerun physical polynomial checks.

Every I/P polynomial is read from the authenticated pinned metadata and converted to a factored add/multiply/power DAG after elementary-symmetric substitution. No physical polynomial is expanded or evaluated. The actual di/dp/dh coefficient metadata is checked to equal -h_carrier for each of these primary carriers. The minus sign is retained in each block numerator.

The selector uses the complete pinned entry -2*(I_a transpose(tf(R)) P_a)[12,6]. The tracefree projection tf(R)=R-tr(R)/2 Id is explicit for each current, so no unproved zero-trace assumption is necessary. The matching physical-frame conjugations cancel once before this normalized contraction. Both logarithmic Q terms remain in each tangent.

Each scalar carries a denominator dictionary keyed by the entire owner label and factor kind. Multiplication adds orders; addition lifts to the componentwise least common multiple; differentiation performs the exact quotient rule. The resulting per-owner orders are therefore derived from the rational arithmetic representation, not from declared bound flags. They are sufficient representation orders, not claims about minimal pole orders after numerator cancellation. In particular the deliberately unsimplified derivative ledger can retain zero-derivative factors.

The maximum derived orders across all eight multipliers are carrier20, legal3, standard5251. The local carrier54/legal29 partition cancels each matching owner's factors. Fixed local weights are pulled back to the common finite coordinates once; for an infinity coordinate their scalar clearing part contributes x_i^[-270-29*degree(legal)], with degree1 or3. Standard factors contribute x_i^-order. No section twist is attached to scalar rho.

The quotient AST includes exact binomial sums and a bounded-composition-sum operator whose body contains integer affine powers and chained binomial coefficients. Large composition domains are not enumerated. All ordinary negative powers in the output DAG apply only to coordinates; the bounded sum's polynomial powers are nonnegative on its explicitly recorded domain. No arbitrary polynomial inverse, unresolved partial node or current source leaf remains in this conditional representation.

## Validation and limits

Fifteen tests cover four E signs, complete owner retention, derived orders, coordinate-only inverses, exact denominator metadata mutation rejection, wrong-owner/excess-order rejection, active-mask filtering, carrier123 endpoint zero, finite sum domains, an abstract derivative control, an explicitly nonzero-trace projection control, and unchanged gates/resources. Abstract low-threshold composition sums are evaluated to verify their exact weighted partition identity, and an abstract rational quotient is differentiated against its explicit formula. No physical source is evaluated. Cross-PYTHONHASHSEED byte equality and exact saved-artifact regeneration are checked. The finite sum and full lowering passed the independent audit recorded in selected-full-owner-kernel-lowering-independent-audit.md.

The global kernel remains at 78 unresolved regularization families. No admission/execution flag changes. Private resource configuration is omitted; execution release remains false. Artifact size is metadata size, not an arithmetic memory certificate. No physical coefficient or obstruction value is computed, and nothing is posted externally.
