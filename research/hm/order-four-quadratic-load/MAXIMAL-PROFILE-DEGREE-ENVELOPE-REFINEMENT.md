# Maximal-profile degree capacities exclude two further quotient labels

## Result

Starting from the39 labels retained by the unrestricted primal and dual degree envelopes, maximality of the stated profiles excludes

- G3.11.cb21c818278d;
- G3.21.7d21add56d56.

The frontier becomes **37**, with profile counts **29/4/4**. Both exclusions use the dual endpoint with l=1. No profile is closed, and no endpoint derivative rank is assumed to be exactly one or two.

This application is stacked on dual PR720, commit1869b195a6c474b973497814b8e04075cba062b4. It uses the finite degree-envelope theorem of PR715, commit8ddbcedc7e01f33ae9aacff56df8da0a33503b57, but restricts its derivative partitions using the separately justified maximal-profile condition.

## Why the endpoint rank is at most two

Use the published convention in Section4 of `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: a maximal consecutive plateau is

    F0 < F1 < ... < Fm,  Fk=E,  m=k+l,

with rank-three successive blocks, and at each interior stage Fi its Gauss kernel is F(i-1) and its forward transform is F(i+1).

For k=1, K=E^- is F0. Its derivative factors through A(-2), where A=E/K has rank3, so its rank is at most3. If that rank were3, its derivative would generically fill A(-2); saturation would give K^+=E. Its kernel K^- would then extend the rank-three plateau one block farther left, contradicting maximality. Thus the derivative rank of K is at most2.

For k=2, K=F1 is an interior rank-three stage, so its derivative rank is3. Its kernel M=F0 is the endpoint, whose derivative rank is at most2 by the same maximality argument. The reversed dual plateau has central bundle Q* at index l, so the identical statements hold for L=(Q*)^- with l replacing k. These deductions use only saturation and generic rank to identify the forward transform, not a fiberwise full-rank assertion.

All nonzero backward stages are negative saturated subbundles. By the strict-slope theorem a nonzero such stage cannot have identically zero derivative. Hence the positive derivative ranks q_j are the same terminating nonincreasing partitions used by the general degree-envelope theorem. Zero stages after termination add no parts.

## Exact restricted partition family

For the primal F=K use rank n=14 and J=A; for the dual F=L use rank n=10 and J=B. Their orientations and actual degrees -54-deg J are those already established in the unrestricted applications.

If the corresponding plateau length is1, retain every partition with q1<=2. If it is2, retain every partition with q1=3 and q2<=2. No other part is fixed. In the conjugate-height notation h1>=h2>=h3>=0 with sum n, these conditions are exactly

    h3=0 for length1,   h3=1 for length2.

Thus the necessary capacity is the maximum of

    sum_i [h_i lambda_i-h_i(h_i+1)]

on that restricted, exhaustive height set, where lambda are the three ordinary degrees of J in decreasing order. The checker also constructs q_j from each height vector and verifies directly that the partition conditions and the h3 rule agree.

## The two numerical contradictions

For both excluded labels, l=1 and the dual bundle has ordinary degrees

    B: (6,-8,-8),  rank L=10,  deg L=-54-deg B=-44.

The unrestricted capacity was not sufficient to exclude them. Put t=h2, so h1=10-t and 0<=t<=5. The objective is exactly

    -50+6t-2t^2 = -46-2(t-1)(t-2).

For integer t the product (t-1)(t-2) is nonnegative, so the maximum is -46, attained exactly at t=1,2, equivalently (h1,h2,h3)=(9,1,0),(8,2,0). Therefore the actual degree -44 exceeds the necessary bound -46 by two. Exhausting both orientations on all39 starting labels produces no other exclusion.

## Reproduction and limits

Run `python3 verify_maximal_profile_degree_envelope_refinement.py` to produce `maximal-profile-degree-envelope-refinement.json`. The standalone checker pins the baseline144, public720 certificate, general theorem and plateau-convention note. It checks78 orientation/label pairs and preserves all182 original IDs as143 previously excluded, two newly excluded and37 remaining. It imports no other verifier or unpublished audit/witness files.

All calculations involve bounded abstract integer degrees and partitions. No actual coefficients, points, source matrices, actual-instance rank calculations, scans, spikes or consumed experiments enter. This is a necessary-condition refinement, not a realization, profile-closure, smoothing or SF claim.
