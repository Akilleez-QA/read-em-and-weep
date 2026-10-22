# A finite degree envelope for a negative Gauss flag

A checked necessary degree bound. No claim of realization or completion.

Let F be a nonzero saturated subbundle of a constant bundle on P1 in characteristic zero, with every splitting degree strictly negative. Every Gauss derivative below uses the same constant connection. Suppose a locally free sheaf J has a sheaf injection (not necessarily with saturated image) into (H tensor O)/F and the actual second fundamental form of F factors through J(-2), where J has splitting degrees lambda_1 >= ... >= lambda_b. Thus the factored map has exactly the Gauss kernel; an arbitrary lift through a noninjective map is not allowed. Set F_0=F, F_j=F_{j-1}^- and Q_j=F_{j-1}/F_j.

Every F_j is saturated in the same constant bundle. The strict-top-slope lemma therefore applies at every nonzero stage. A nonzero stage cannot have derivative zero: its kernel would equal itself, contradicting strict decrease of its highest splitting degree. Thus ranks strictly decrease until F_m=0, with m at most rank(F).

The first image Q_1 injects into J(-2). Because F_{j-1} is the Gauss kernel of F_{j-2}, its derivative lands in (F_{j-2}/F_{j-1})(-2)=Q_{j-1}(-2). Consequently Q_j injects into Q_{j-1}(-2), and hence into J(-2j).

The positive integers q_j=rank(Q_j) form a nonincreasing partition of n=rank(F), with q_1<=b. Degree additivity gives deg(F)=sum_j deg(Q_j). Taking determinants of Q_j -> J(-2j) gives

    deg(Q_j) <= lambda_1+...+lambda_{q_j} - 2j q_j.

This uses only a sheaf injection, not fiberwise saturation of its image in J(-2j). Therefore

    deg(F) <= max_q sum_j (lambda_1+...+lambda_{q_j} - 2j q_j),

where q ranges over the finite partitions of n with largest part at most b. The maximum is a necessary upper envelope, not an assertion that a corresponding Gauss flag exists. No ranks of later derivatives are prescribed: all permitted decreasing-rank patterns are retained.

For n=11 and b=3 there are sixteen partitions. The independent checker enumerates all and confirms the maximum using a separate memoized recurrence. For J degrees (-10,-10,4), (-10,-6,4), (-10,0,2), and (-10,2,2), the upper envelopes are respectively -78,-70,-60,-50. Any application must separately establish the actual J and deg(F). For example, deg(F)=-52 cannot coexist with the first J under these hypotheses.

The iteration premise is the [published strict-top-slope lemma](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md). This is an abstract integer and bundle argument, not an evaluation of actual source coefficients or an actual-instance rank calculation.

## Equivalent column formula

Write h_i for the number of parts q_j at least i. Then h_1>=...>=h_b>=0 and sum h_i=n. Conversely every such height vector gives exactly one allowed partition. The objective is

    sum_i [h_i lambda_i - h_i(h_i+1)].

Indeed each lambda_i occurs h_i times, and sum of the corresponding step indices is 1+...+h_i. This gives a second finite description of the same necessary envelope. The checker independently enumerates height vectors as well as partitions and a memoized recurrence.

## Reproduction and scope

Run `python verify_gauss_degree_capacity_independent.py` with standard Python. The three finite integer methods agree. The geometric proof was independently checked, including saturation, termination and derivative factorization. Applying the numerical examples to a particular proof-repair branch requires its actual J and F hypotheses to be supplied separately; this note does not declare those branches excluded. No actual source coefficients, points, matrices or numerical ranks are evaluated.
