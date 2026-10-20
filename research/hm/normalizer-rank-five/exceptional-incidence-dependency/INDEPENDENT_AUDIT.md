# Independent audit of the exceptional incidence classification

## Verdict

PASS for the stated abstract incidence theorem and its conditional full-normalizer interpretation. This is a genuine refinement of the previous universal bound I(L) <= 6: it identifies its unique equality case and separates two necessary mechanisms for I(L)=5. It neither excludes actual residual rank five nor establishes a new numerical rank for the exceptional orbit.

Critical scope: I(L)=5 does **not** unconditionally force dim(L intersect R)=3 or projector collinearity. Those conclusions hold in the rho=1 cycle branch. The proof states the qualification correctly. Its paired example has I=5 and dim(L intersect R)=2.

## Dimension and case checks

1. Each repeated-edge intersection has dimension at most one, since a two-plane would contain its endpoint coordinate lines. Its nonzero generator has both endpoint coefficients nonzero. Each projected intersection has dimension at most one because H_j projects to Ct_j.
2. Every proper set of edges of the four-cycle forms a forest. Leaf elimination proves independence of its edge generators. Hence the edge relation space has dimension zero or one; a nonzero relation requires all four edges and their span then has dimension three.
3. Put r=dim(L intersect R), d=dim(proj_D L), so r+d=4. The edge span gives r >= e-rho. The k independent selected t_j belong to proj_D L, as does S_0. Their span W_A meets H_0 in exactly p dimensions. Therefore d >= k+h-p, and I=e+k+h <= 4+rho+p. The exact definition of p uses projections of the individual intersections L intersect H_j, not merely arbitrary coordinate directions in proj_D L.
4. If rho=1, then e=4, r>=3, and r cannot equal four because L would equal R and contain all forbidden lines. Thus r=3,d=1,k<=1,p=0 and k+h<=1. This proves I<=5 and, at equality, precisely (k,h)=(0,1) or (1,0).
5. If I=6, the cycle branch is impossible. Then p=2, k=4, d=4, r=e=0 and h=2. Thus L is the graph of a map A:D->R with A(t_j) in P_j. Containment of both H_0 generators gives A(t_1)=-A(t_4) and A(t_2)=-A(t_3). Opposite edge planes have zero intersection, forcing A=0. Conversely D has intersection dimensions (2,1,1,1,1), so equality is attained uniquely.
6. If I=5, the inequality forces rho+p>=1. The two listed abstract examples have exactly the claimed intersections and avoid all coordinate lines. They prove the necessary mechanisms are nonvacuous for the abstract arrangement, without proving realizability by the actual kernel or global repeated-input injectivity.

## Projector and representation scope

The imported class-sum result identifies the actual twenty-dimensional global kernel with the +5 eigenspace of C on the universal Schur module. Since C commutes with the full normalizer, it preserves the exceptional-clock space U. Its restriction has positive eigenspace L, so ker((I-C/5)|U)=L. Thus rank-nullity on R gives rank((I-C/5)|R)=4-dim(L intersect R).

In the cycle branch this rank is one. No r_i maps to zero by the coordinate-line exclusion, proving nonzero collinearity. Conversely, nonzero collinearity makes L intersect R a hyperplane with every coordinate coefficient nonzero; its four edge intersections span that hyperplane and have a single dependency. Thus the displayed condition exactly detects rho=1 under these hypotheses. It is necessary for rank five in that branch but insufficient for rank five overall: for example, abstractly L=R_0 plus C(t_1+t_2), where R_0 is the coordinate-sum-zero hyperplane, has rho=1 and I=4. This example concerns abstract incidence only and is not claimed to realize C.

C commutes with B because B is formed from normalizer operators and a polynomial in Z. The prior Sylow result supplies four two-dimensional B eigenspaces and one kernel line in each. The proof properly uses this only for the actual, already fixed L; it does not treat arbitrary product-of-lines points as full-normalizer kernels. No new compatibility constraint on C and B is proved here.

## Novelty and boundary

The equality classification I=6 iff L=D and the refined rho/p bound add genuine information beyond the old I<=6 proof. The projector statement itself is a useful rank-nullity reformulation of the cycle stratum, not a new representation-theoretic exclusion. The paired fixed-vector equations are likewise a translation of membership and require further substantive identities to rule them out. The proof explicitly acknowledges these limitations.

Reviewed sources: this directory's PROOF.md; ../heisenberg-universal-rank-four/PROOF.md; ../exceptional-sylow-kernel-constraint/PROOF.md; ../../rank-four/full-normalizer-pure-t-nonvanishing/PROOF.md. The imported target identification and global class-sum theorem are used as established inputs. Audit involved static reads and formal finite-dimensional reasoning only. No actual source, selected kernel projector, operation value, or rank instance was evaluated; no external writes or large computations were performed.

## Addendum: Section 4A seven-stratum classification

PASS. The exhaustive list of (r,e,k,h) at I=5 is

    (0,0,3,2), (0,0,4,1), (1,1,2,2), (1,1,3,1),
    (2,2,2,1), (3,4,0,1), (3,4,1,0).

For r<=2 one has rho=0, e<=r, k<=4-r, h<=2, e+k+h=5 and k+h-p<=4-r with p<=floor(k/2). Enumerating these small inequalities gives exactly the first five rows: for r=1, e=0 would require k=3,h=2 and violate the projection inequality; for r=2, e<=1 is impossible by the same inequality, and e=2 leaves only k=2,h=1. For r=0 the sum condition alone gives the two stated rows.

For completeness, the converse needed in the r=3 case is elementary: L intersect R is a hyperplane avoiding every coordinate line, so its defining functional has all four coefficients nonzero. It meets every P_j in a line; hence e=4, and those four lines span a three-space, giving rho=1. Section 2 then gives exactly the last two rows. The author added this converse explicitly in Section 4A after the audit request; it is also established later in Section 5.

All seven displayed representatives have dimension four and satisfy the line exclusions. Their individual nonzero-H_j intersection dimensions (j=1,2,3,4), followed by h, are respectively:

    (1,1,1,0); h=2
    (1,1,1,1); h=1
    (2,0,0,1); h=2
    (1,1,1,1); h=1
    (1,1,1,1); h=1
    (1,1,1,1); h=1
    (2,1,1,1); h=0.

For the fourth row the r_3+r_4 direction supplies the H_3 intersection while the other three are distinct-index axes. For the fifth row H_2 and H_3 supply the repeated-edge directions. Thus the equal intersection-dimension tuples in several rows do not conflate their r/e/k data.

The word 'complete' is justified for numerical incidence strata under the abstract arrangement hypotheses, not for four-plane equivalence classes, global repeated-input injectivity, or compatibility with the actual C/B operators. No such additional realization has been asserted or checked. The addendum uses only formal coordinate inspection of the supplied abstract examples, not an actual source or selected rank-instance evaluation.
