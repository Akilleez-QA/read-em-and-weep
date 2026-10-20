# Lower Rao multiplication and quadratic sections of the HM lines

Work over C. Let S=Sym(V*), dim V=5, and let C be the twenty-five disjoint transverse HM evaluation-degeneracy lines in P(V). Write I=I_C and M_d=H^1(I_C(d)). A hyperplane is called proper here if it contains no component line of C.

## 1. Pinned structural input

PR471 identifies M_5=R_6 direct-sum End_0(V), M_6=V*, with dim R_6=6. Under the actual adjoint identification, multiplication by ell in V* is (r,A) |-> ell composed with A. The Rao module is generated in degree zero, so S_1 M_4=M_5. The Hilbert function gives dim M_4=25(5)-70=55 and dim M_5=30; I_4=0 and dim I_5=6. PR472 proves that every nonzero linear form maps M_5 onto M_6 and that every proper hyperplane section D consists of twenty-five reduced points with h_D(6)=25. Here h_D denotes the Hilbert function of its saturated coordinate ring, not the dimension of all sections of O_D.

## 2. A uniform lower bound in the preceding degree

Fix a proper H=(ell=0) and put r=rank(ell:M_4 -> M_5). The ideal restriction sequence in degree five and H^2(I_C(4))=H^1(O_C(4))=0 identify

H^1(I_(D,H)(5))=coker(ell:M_4 -> M_5).

Consequently h_D(5)=25-(30-r)=r-5. Macaulay's Hilbert-function growth theorem gives h_D(6)<=h_D(5)^{<5>}. The fifth binomial expansion of nineteen is

19=binom(6,5)+binom(5,4)+binom(4,3)+binom(3,2)+binom(1,1),

whose Macaulay successor is 7+6+5+4+1=23. The successor operation is increasing. Thus h_D(5)<=19 would contradict h_D(6)=25. Hence

rank(ell:M_4 -> M_5)>=25,
dim coker(ell:M_4 -> M_5)<=5,
dim ker(ell:M_4 -> M_5)<=30.

This holds for every proper hyperplane, including special ones. It does not assert surjectivity or an exact rank in this degree. The bound allows h_D(5)=20: its fifth Macaulay successor is twenty-five.

## 3. A projected rank-one lemma

For a five-dimensional vector space V, let pi:End(V) -> End(V)/(C Id). The induced projective map from the rank-one Segre variety P(V) times P(V*) is everywhere defined and injective. Indeed a nonzero scalar multiple of Id has rank five, whereas the difference of two rank-one matrices has rank at most two. Its image X is closed because the Segre variety is projective. Projection to the second Segre factor is therefore well-defined on the unique rank-one representatives of points of X.

We need the following elementary property. If a projective linear space W of dimension four lies in X, then its rank-one representatives all share a common first factor or all share a common second factor. To prove it, take two independent representatives A and B. Any point of their projected line has a rank-one representative T with

T=alpha A+beta B+gamma Id.

If gamma were nonzero, this would express an invertible rank-five matrix as a sum of three rank-at-most-one matrices. Hence gamma=0. The line spanned by A and B is consequently a line of rank-one matrices. Two independent rank-one matrices have this property only when they share a first or a second factor: otherwise their sum has rank two. Finally, pairwise sharing forces one common factor throughout the family. If two members have independent first factors, they have the same second factor, and every other member must have that second factor; the opposite case is symmetric. This proves the stated ruling property without invoking a classification theorem.

For dimension and closed-image arguments below, one may work on the Segre variety itself and the closed inverse image of W; injectivity of pi makes all fibers zero-dimensional. No scheme-theoretic assertion about this projection is needed.

## 4. One proper linear factor admits a general second factor

Fix a proper ell_1 and put U=ell_1 M_4 inside M_5. Section 2 gives codim U<=5. Commutativity, degree-zero generation, and PR472 give

S_1 U=ell_1(S_1 M_4)=ell_1 M_5=M_6.

For a second nonzero linear form ell, the map ell:U -> M_6 fails to be surjective exactly when there is a nonzero y in M_6*=V such that the functional (r,A) |-> ell(Ay) annihilates U. Under the trace pairing, this functional is the class pi(y tensor ell) in End(V)/(C Id)=End_0(V)*, with zero R_6* component. Put

W=P(U^perp intersection End_0(V)*).

Its dimension is at most four. The bad second factors form the projection to P(V*) of the closed incidence of rank-one classes lying in W. This projection is closed because the incidence is projective.

Suppose the bad set were all P(V*). Its incidence would have dimension at least four. Since its image in X lies in W and pi has zero-dimensional fibers, W would have dimension four and would be contained in X: a closed subset of a projective four-space with dimension four is the whole space. Section 3's ruling property then applies. Since the second-factor projection covers P(V*), the first factor must be a fixed nonzero y. It follows that ell(Ay)=0 for every ell in V* and every (r,A) in U. Equivalently every vector in S_1 U annihilates y, contradicting S_1 U=V*.

Thus the bad second-factor set is a proper closed subset of P(V*), of dimension at most three. For every proper ell_1, a general ell_2 therefore makes

ell_1 ell_2:M_4 -> M_6

surjective. The proof concerns actual multiplication, not a generic replacement map.

## 5. A nonempty quadratic open and sextic interpolation

Multiplication S_2 -> Hom(M_4,M_6) depends linearly on the quadric. Its rank-five locus is Zariski open, and section 4 proves it is nonempty. Since the space of quadrics is irreducible, it meets the nonempty open of smooth quadrics transverse to all twenty-five lines. Therefore a general smooth quadric q has q:M_4 -> M_6 surjective, and Q=(q=0) meets C in fifty distinct reduced points D_q.

For such q, restriction gives

0 -> I_C(4) --q--> I_C(6) -> I_(D_q,Q)(6) -> 0.

The surjection on Rao groups and H^2(I_C(4))=0 imply H^1(I_(D_q,Q)(6))=0. Thus D_q imposes fifty independent sextic conditions on Q. Since h^0(O_Q(6))=binom(10,4)-binom(8,4)=210-70=140,

h^0(I_(D_q,Q)(6))=90.

The nonempty open, rather than all smooth quadrics, is the conclusion. No membership in this open is asserted for the original fixed quadratic invariant or for any selected HM/source-instance pair.

## Public dependencies and scope

- PR471, a38c45f91c3f29134c6c8d0a2c51d5e8d1e002d9: actual top Rao adjoint, degree-zero generation and Hilbert data. https://github.com/Akilleez-QA/read-em-and-weep/blob/a38c45f91c3f29134c6c8d0a2c51d5e8d1e002d9/research/hm/rao-socle/PROOF.md
- PR472, 306cd02e623881f3caeddaf17a286c33d3bec63f: uniform top multiplication and sextic interpolation for proper hyperplane sections. https://github.com/Akilleez-QA/read-em-and-weep/blob/306cd02e623881f3caeddaf17a286c33d3bec63f/research/hm/universal-tail/PROOF.md
- Juan C. Migliore, The Geometry of Hilbert Functions, Definitions 2.3–2.5 and Theorem 2.6, p4, for the standard Macaulay growth theorem used in section 2: https://academicweb.nd.edu/~jmiglior/Hilb.pdf

This is an authored structural argument requiring mathematical review, not proof-assistant verification. No selected actual HM/source-instance evaluation, numerical multiplication matrix/rank calculation, coefficient search, generator/checker or large computation is used. The original fixed-pair values, actual-source membership, pure conditions, higher-order lifting and algebraicity remain unresolved. No exact lower linear rank, whole-module Lefschetz theorem, or all-smooth-quadrics assertion is made.
