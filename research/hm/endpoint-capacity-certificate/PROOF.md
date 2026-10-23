# Exact certificates for two-height endpoint degree capacity

## Contribution and scope

This is a reusable integer optimization theorem and independently checkable certificate implementation. It generalizes the six-height capacity calculation in [PR1138](https://github.com/Akilleez-QA/read-em-and-weep/pull/1138), pinned at `c69f97aaf00e116e3a8abebf19a8e02868c4f7c4`, to arbitrary positive rank. It is not a claim of literature novelty, a new actual-source exclusion, or a completed proof repair. The four PR1138 degree triples are labelled already-known regressions, not new progress. No actual coefficients, points, jets, matrices, or rank computations occur.

## Hypotheses of the geometric application

Suppose a terminating endpoint filtration has graded pieces G_j of nonincreasing positive ranks q_j <= 2, with sum q_j=N. Suppose it has injections G_j into B(-2j), where the ordered largest ordinary splitting degrees of B are lambda1 >= lambda2. Determinants then give deg(G_j) <= sum_{i<=q_j} lambda_i - 2j q_j. Define h_i as the number of j with q_j >= i. Thus h1 >= h2 >= 0, h1+h2=N, and degree additivity gives

    deg(endpoint) <= F(h1,h2)
    F(h1,h2) = sum_{i=1,2} [h_i lambda_i - h_i(h_i+1)].

The termination, injections, splitting degrees, and determinant inequalities are geometric hypotheses, not verified by this arithmetic code. If B has rank larger than two its lower degrees are irrelevant to this bound only because q_j <= 2. The application must establish that endpoint-rank hypothesis independently.

## Exact maximum and complete optimizer set

Let N>=1 and lambda1>=lambda2 be integers. Set

    L=ceil(N/2), U=N, B=lambda1-lambda2+2N,
    C=N lambda2-N^2-N.

Putting h=h1 and h2=N-h gives, by expansion,

    F(h)=-2h^2+B h+C,  L<=h<=U, h integral.
    8F(h)=B^2+8C-(4h-B)^2.                         (1)
    F(h+1)-F(h)=B-4h-2.                           (2)

Equation (1) proves that maximizing F is exactly minimizing distance to B/4 on the integer interval. Clip floor(B/4) and floor(B/4)+1 to [L,U], deduplicate, and evaluate F at these at most two candidates. This gives the complete optimizer set and its exact value using only integer arithmetic. Equivalently they are the nearest integers to the vertex clamped to the real interval. There is no loop whose length depends on N. Arithmetic bit complexity is not constant, since integers can grow.

Equation (2) decreases strictly by four per step. Consequently there are at most two maximizers, and if there are two they are consecutive. A tie exists exactly when B=4h+2 for an integer h with L<=h<h+1<=U. The congruence B=2 modulo 4 alone is insufficient at a clipped boundary. For example odd N with lambda1=lambda2 has one feasible maximizing height despite the two unrestricted integer nearest points. The gap lambda1-lambda2=2N-2 gives the endpoint tie (N-1,N) whenever both heights are feasible.

## Independently checked certificate

A certificate records N, lambda1, lambda2, the maximum M, the complete ordered height list, and the squared distance in (1). The verifier does not call the optimizer and never enumerates the interval. It checks admissibility, all listed values, (1), distinctness, and adjacency. If a feasible integer lies to the left of the list, the last forward difference into the first listed height must be strictly positive. If one lies to the right, the first forward difference beyond the last listed height must be strictly negative. Because the differences decrease strictly, all earlier values are smaller and all later values are smaller. These strict outside checks also reject either omitted member of a tie. Internal equal values and adjacency establish the whole listed plateau. This proves both optimality and completeness, not just that one submitted point is a local maximum.

## Degree consequences and equality-only strict-top filter

Under the geometric hypotheses, a proposed degree d>M is impossible. For d<M the capacity supplies no exclusion. If d=M, only maximizing heights can occur, and every summed determinant inequality must be equality, since their nonnegative deficits sum to zero.

For a further conclusion one must SEPARATELY prove equality of the actual top-image flags and that the final nonzero stage at height h has top degree lambda1-2h. Unique top determinant summands are one route, but arithmetic equality alone does not prove these actual-image facts. Also assume initial top<=t0 and strict-top decrease by at least one at every stage. Then

    lambda1-2h = top(F_h) <= t0-h,
    hence h >= lambda1-t0.                         (3)

Thus (3) filters the maximizing heights only when d=M and the actual-image hypotheses hold. If none survive, that equality configuration is excluded. If one or more survive, this argument alone does not realize them or exclude them. Equation (3) is NOT an unconditional restriction on all rank partitions and does NOT lower the universal maximum. In particular it cannot be used when d<M. The implementation enforces this separation by rejecting below/above-capacity calls and requiring an explicit caller attestation for the geometric top-flag proof. This attestation is an API guard, not authentication or formal verification of geometry. For equal heights, the caller must still establish top(F_h)=lambda1-2h; the API does not assume that the final stage is a line.

## Validation

`verify.py` compares the closed form with direct evaluation of the original two-summand expression on 7,800 synthetic parameter triples (1<=N<=24, -12<=lambda2<=lambda1<=12). It tests integer translation covariance, 39,000 conditional equality filters against the direct top inequality, malformed input rejection, omitted and forged ties, parity, clipping, singleton domains, and strict-inequality classification. Four huge integer certificates have ranks of roughly 100 decimal digits; these use no interval enumeration. The four PR1138 examples are separate, explicitly already-known regression controls. The full 62,442 checks have identical JSON output in normal and optimized Python.

These tests check implementation of the proved arithmetic. They are neither a proof-assistant verification nor evidence of any additional actual-source exclusion.
