# Exact Smith profile of the positive component in endpoint nine

**Craig Ward · 23 October 2026 · PR1077**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/3100c7c401e3f68eaeb08ea6088a128d612d5390/research/hm/source2-pure-v-small-positive-smith/PROOF.md).

## Conditional maximal row rank, not invertibility

Retain actual compatible pure-V radical and endpoint nine. The nonzero transfer scalar is proved by PR1075, not added as an unevaluated nonvanishing premise. For the actual positive component M_a(t)=Q+tT_a, of dimensions 41→37, every nonzero direction outside the support of E=Z⊔E12 has Smith form over C[[t]]

    [diag(1 repeated 33 times, t²,t²,t²,t⁴) | 0_(37×4)].

E has length 46 and support of 28 points: six C₅ axes carrying length-four ideals, ten reduced C₃ axes and twelve reduced ambient conic points. No Smith profile is asserted at any of those support points. The same profile holds over K[[t]] for the symbolic generic direction K=C(P(A)), with a local trivialization of the direction line.

Consequently this positive component has maximal generic row rank 37, free formal kernel of rank four and formal cokernel (K[[t]]/(t²))³⊕K[[t]]/(t⁴), of length ten. The maximal-minor ideal is exactly (t¹⁰). This rectangular component is not invertible, and nothing here proves full adjoint invertibility, controls the other parity component or completes the original repair.

## Why the open set is precise

The determinant-embedded original fourth D row has component ideal sheaf exactly I_E. Away from the six C₅ axes the second A symbol has rank three, its cokernel is a line bundle and the surviving fourth source is exactly D. The determinant embedding is a fiber isomorphism there, not at singular target points. Outside all of supp(E), the fourth row is nonzero and its actual fourth Bockstein therefore has rank one.

The ten C₃ axes and twelve conic points are excluded as well: the fourth D row vanishes there. At C₅ the second rank also drops. Thus the uniform profile is not inferred across a singular ideal-sheaf fiber or additional specialized A-kernel inputs. The scheme I_E is not the quadratic-lift degeneracy scheme.

## Formal elimination retains the correction term

The original invariant Q rank 33 splits off 33 unit pivots. Original first-symbol vanishing makes the remaining 4×8 matrix divisible by t². Rank-three second symbol yields three t² factors, leaving a 1×5 row divisible by t³. Original third-symbol vanishing raises that divisibility to t⁴; the nonzero fourth gives common valuation exactly four and one t⁴ pivot.

After division by t², the relevant block expansion is

    [ I3+tA+O(t²)    tB+O(t²) ]
    [ tC+O(t²)       tD+t²E+O(t³) ].

The Schur residual is tD+t²(E−CB)+O(t³), so the fourth coefficient is the corrected E−CB, not the raw lower-right E. This retains the effect of the second-order pivots rather than skipping a page correction.

## Determinantal orders and limits

Determinantal valuations are zero for sizes 1 through 33, then 2,4,6,10 for sizes 34,35,36,37. All maximal minors have order at least ten and at least one has order exactly ten; not every maximal minor need be nonzero or have that order.

For each allowed fixed direction the polynomial pencil has row rank 37 on a nonempty Zariski-open set of t, not at t=0 or necessarily every nonzero t. The four-dimensional Laurent-series kernel is compatible with full row rank and is not a target obstruction. Source occurrence, endpoint selection, opposite-bundle type and the full adjoint problem remain open. Exact formal algebra checks support the imported actual Bockstein and ideal-sheaf arguments, not an actual-instance evaluation.
