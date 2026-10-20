# Independent audit: rank-five curve support is empty or the canonical conic orbit

## Verdict

The transfer in ../rank-five-curve-classification/PROOF.md is valid under its explicitly stated hypotheses. The reduced curve support Γ5 is empty or equals the union of the twenty-five canonical conics, of reduced degree 50. No earlier rank-four-specific conic coefficient restriction is needed or transferred. This conclusion does not exclude isolated rank-five points, establish the conic alternative occurs, or identify determinantal multiplicities.

The proof was independently checked against the line, conic, cubic/quartic, degree-hundred, degree-sixty, small-component-orbit, and polarization proof files. The audit concerns their transfer and the relevant universal arguments; it retains the standing representation identities and previously established degree and pointwise-rank theorems as inputs.

## 1. Hypotheses and line avoidance

RANK_FIVE_DEGREE.md gives deg Γ5≤75 under the mixed-minor hypotheses. The curve classification separately retains dim Z5≤1 and N-invariance. The needed canonical negative-line avoidance is the pointwise rank Q≥6 theorem in ../rank-four-canonical-conic-exclusion/LINE_ADDENDUM.md. The older ../canonical-line-rank-five-strengthening/PROOF.md only gives rank Q≥5 and would not suffice to avoid Z5.

The cited new line addendum uses the actual twenty-dimensional target and its parity representation, so the transfer must not silently discard that assumption. Its proof excludes a P4 constituent of the eight-dimensional positive target and then uses the prior rank-four-even-block image classification, whose derivation is independent of the total rank. The rank Q≥6 conclusion is exactly the avoidance needed here.

Global emptiness of Z4 is not required for the geometric classification. It supplies the additional statement that all remaining Z5 points have rank exactly five.

## 2. Lines and conics

The line argument transfers Sections 1–5 of ../rank-four-line-component-exclusion/PROOF.md, an orbit lemma: any line with at most125 normalizer translates is canonical or meets a canonical negative line. Since each line translate in a one-dimensional invariant closed set is an irreducible component, the new bound75 is sufficient. Avoidance of the negative lines excludes both possibilities.

Sections 1–3 of ../rank-four-conic-component-classification/PROOF.md are also rank-independent. An integral conic has a proper three-dimensional vector span, so its A-stabilizer has order1 or5. In the trivial-stabilizer case the new degree bound gives 50[G:H]≤75, hence H=G. The central-involution cocycle argument conjugates the stabilizer to G; the unique three-dimensional invariant span is T and the unique invariant quadratic is q. In the axis case, the sixty distinct spans and five distinct conics over each give at least300 orbit members, impossible here. The canonical conics have exactly25 distinct translates, so the whole conic contribution is either absent or precisely degree50.

The coefficient restrictions in Section4 of that conic proof depend on total rank at most8, equivalently residual rank at most4. They cannot be imported for Z5. The proposed proof correctly excludes them.

## 3. Cubic and quartic orbit exhaustion

Sections 1–6 of ../rank-four-degree-three-four-exclusion/PROOF.md apply to every N-invariant reduced curve of total degree at most125. Their use of a rank-four no-conic theorem occurs only in the final combined conclusion and is not part of the cubic/quartic exclusion.

The exhaustive cases remain valid at degree75: an A-fixed component would span P4 and be a rational quartic, contradicting faithful C5² action; a free A-orbit has complement stabilizer G and is excluded by invariant plane equations or the faithful full-span G-action; an axis-stable plane has sixty translates; an axis-stable hyperplane has thirty translates and at least five curves over each; an axis-stable full-span quartic has at least150 translates after the order-five lift argument. The latter argument allows a translation part in the lift and does not assume the lift is the displayed diagonal shear. Thus no stabilizer or span case was lost in the transfer.

## 4. The residual union and degree lower bound

D is the reduced union of all nonconic irreducible components of Γ5. This is a closed reduced projective curve if nonempty, not the set-theoretic complement of the conics. It is N-invariant because degree is preserved by the action. Intersections with removed conics cause no difficulty. Degrees of distinct reduced components add, even when components intersect, so deg D≤75, and deg D≤25 if conics occur. All its integral components have degree at least5.

Here is the needed rank-free argument. An A-orbit of25 components costs at least125 degrees. An A-orbit of five has an order-five axis stabilizer, and its six conjugate axes give six disjoint A-orbits, costing at least150 degrees. Therefore every component of D is A-stable and spans P4.

The disjoint-normalization lemma of ../rank-four-degree-hundred-lower-bound/PROOF.md, Section2, then proves 50 divides deg D. Its full-span condition is essential and has just been established. On the disjoint union of component normalizations, each component stabilizer acts faithfully. Hilbert90 supplies an invariant rational section on a representative component, and equivariant transport produces a global invariant rational section on the disjoint normalization. There is no gluing requirement at original intersections. Point stabilizers are cyclic, with orders1,2,3,4,5,6,10. Canonical O(5) linearization and trivial order-five fibre characters force divisor coefficients to be divisible by5 at inertia orders divisible by5. The resulting orbit contributions are all divisible by250, proving 250 divides 5 deg D. This uses no rank assumption.

A positive degree≤75 must consequently equal50. The exclusion in ../rank-four-degree-sixty-lower-bound/PROOF.md, Section5, is likewise a general invariant-curve theorem without rank input. Its necessary imports are general: small-degree A-stable components have at least20 translates; integral N-stable curves have normalization genus at least326; Heisenberg divisibility and the irreducibility of quadratic forms give the refined genus upper bound306 through degree55. The rank-four line/conic exclusions in that file are used only when applying the general theorem to Γ4. Here absence of those components in D was established separately.

Therefore D is empty. This validates both the no-conic branch and the branch with the complete canonical conic orbit. The degree125 endpoint argument is unnecessary for this transfer.

## 5. Remaining exact-rank configuration

The cited POINTWISE_ADDENDUM.md gives even rank≥5 and odd rank≥4 on each canonical conic. Containment in Z5 gives rank b≤9, so both ranks must be exactly(5,4) everywhere. Conversely these ranks imply containment, and equivariance propagates it to all25 conics. The previous odd-rank-three contradiction and simultaneous(5,3) coefficient restrictions do not exclude this new configuration. The proposed final section correctly leaves that issue open.

## Scope

Only local mathematical proof files and universal group, curve, and divisor arguments were read or written. No actual source coefficient, source map, selected input, operation matrix, rank instance, jet, or residue was evaluated. No actual source-instance evaluation is claimed.
