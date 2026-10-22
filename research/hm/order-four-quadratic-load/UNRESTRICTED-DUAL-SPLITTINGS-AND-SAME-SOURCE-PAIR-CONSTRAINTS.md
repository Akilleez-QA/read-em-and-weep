# Unrestricted dual splittings and same-source pair constraints

## Result

Without H0(Q*(1))=0, the two adjacent cohomology identities give exactly **260 necessary equivariant splitting types** for Q*, with ordinary degrees in [-28,-1]. Exactly 37 lack degree -1 blocks; the other 223 cannot be discarded.

Requiring a common dual source type for the quotient Q* -> B and transpose injection A -> Q(-2), and endpoint section conditions, reduces the published 159 necessary (1,1) pairs to **126**, with defect counts {0:60,12:51,20:2,24:13}. There are 22 degree triples rather than 25. The removed triples (a,b,t) are (6,-24,12), (18,-24,0), and (-2,-24,20). The extreme total-degree intervals remain -4<=a<=24 and -30<=b<=-2. All ten published (1,2) pairs survive. No profile or positive-defect branch is excluded.

New verifier: `verify_unrestricted_dual_splittings.py`. Full data: `unrestricted-dual-splittings-and-pairs.json`. Run log: `unrestricted-dual-splittings-verification.log`. Pair IDs are zero-based indices in the original JSON files. These are necessary lists, not realization assertions.

## Adjacent identities and finite bounds

Use the actual center-even presentation from ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md:

    0 -> Q* -> M3 O(-1) -> M2 O -> 0,
    M2=A_std+2V+3P+4D, M3=3W'+3S+6T.

At twists zero and -1 the long exact cohomology sequences give H1(Q*)=M2 and H1(Q*(-1))=M3. No positive-twist vanishing is used. The presentation implies all splitting degrees are <=-1.

Equivariant splitting writes Q* as irreducible blocks R O(-j), j>=1, with central sign (-1)^j. All irreducibles are self-dual and det W=1. A block contributes C3=R Sym^(j-1)W to H1(Q*(-1)); it contributes C2=R Sym^(j-2)W to H1(Q*) for j>=2 and zero for j=1. Both are genuine subcharacters of their respective targets. Since dim C3=j dim R, j dim R<=54, proving the finite bound j<=54 including the degree -1 case.

The complete individual-block list is:

    (1,W'),(1,S),(1,T), (2,V),(2,P),(2,D),
    (3,W'),(3,T), (4,1),(4,V),(4,P), (5,W),(5,W'),
    (6,1),(6,A_std), (7,W),(7,S), (8,1),(8,A_std),
    (9,W),(10,1),(11,W'),(16,1),(17,W),(18,1),(28,1).

Thus Q*(28) is globally generated, and every ordinary degree of a locally free quotient B is >=-28. Its rank-three total degree can still be -30.

## Complete integer enumeration and conservative runtime bound

Each eligible block gives a nonnegative vector of W',S,T multiplicities in C3 followed by A_std,V,P,D multiplicities in C2. All other constituents have already been excluded by the individual-block tests. The target vector is (3,3,6;1,2,3,4).

For ordered blocks v_i, let N(i,r) be the number of nonnegative multiplicity solutions using blocks i onward with remaining target r. Set N(26,r)=1 for r=0 and zero otherwise, and use

    N(i,r)=sum_c N(i+1,r-c v_i),
    0<=c<=min_{v_ik>0} floor(r_k/v_ik).

Every block vector has a positive coordinate. Thus the recurrence is finite and counts each multiset exactly once. There are at most 27*(4*4*7*2*3*4*5)=362880 memoized states, with at most seven transitions each, hence at most 2540160 transitions. The verifier counts first, asserts N(0,target)=260, then enumerates only positive-count branches. That enumeration has at most 260*27 prefix visits and seven branch checks each. The observed state count is 98681.

The rank and degree constraints follow automatically: dim M3=54 is sum j dim R; dim M3-dim M2=13 is sum dim R. Both are redundantly checked on every output type, together with the exact adjacent characters.

The H0(Q*(1)) possibilities, with numbers of full types, are:

    0:37; T:8; S:15; W':87; W'+T:17; W'+S:32;
    2W':51; 2W'+T:3; 2W'+S:7; 3W':3.

The old 37 types are recovered only as a consistency check. The verifier does not import their list: it imports only the elementary exact character-ring implementation from verify_negative_vertex_scalar.py and independently derives all blocks and full types.

## Same-source tests

For each input pair (A,B), one and the same Q* type must satisfy all tests below. Different tests cannot use different witnesses.

1. Each irreducible block of B receives a nonzero equivariant Hom from Q*, necessary for surjectivity. Each irreducible block of A admits a nonzero Hom to Q(-2), necessary for injectivity. Hom(R O(e),S O(f)) has multiplicity of R in S Sym^(f-e)W for f>=e, and is zero otherwise. These tests are only necessary Hom tests, not map-rank calculations.
2. For every integer u in [-30,30], require H1(B(u))<=H1(Q*(u)) and H0(A(u))<=H1(Q*(-u)), coordinatewise in irreducible multiplicities. The first follows from the quotient sequence on P1; the second from transpose injection and equivariant Serre duality. This is a declared finite necessary filter, not a claim to characterize every twist.
3. Let L=ker(Q* -> B). Strict top-slope decrease gives maxdeg L<=-2 in both profiles, hence H0(L(1))=0 and H0(Q*(1))<=H0(B(1)). The next kernel L^- has top degree <=-3, so the derivative induces H0(L(2)) -> H0(B) injectively. Exactness of the quotient section sequence consequently gives H0(Q*(2))<=H0(B(2))+H0(B). No rank-three assumption on the endpoint derivative is used.

The published input pairs already have compatible primal E types. We do not impose an unproved relationship between the existential primal witness and existential dual witness. We impose only that the dual witness itself support all its tests simultaneously.

There are at most 169*260*61=2680340 pair/type/twist iterations, using cached universal character products. The final (1,1) list has 2140 compatible pair/Q records involving 189 Q types; the (1,2) list has 594 records involving 184 Q types. Its unchanged pair IDs are 0,2,4,6,7,8,12,14,20,21. Exact counts are asserted and input SHA-256 hashes recorded.

No frozen predecessor is edited or executed to regenerate its published pair files. No actual source coefficients, selected points, instance matrices, rank tests, model spikes or consumed experiments occur. The rank-three problem, source realization, positive-square rank28 and smoothing remain open.
