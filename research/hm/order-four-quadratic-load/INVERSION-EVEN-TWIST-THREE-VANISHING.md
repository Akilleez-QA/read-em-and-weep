# Twist-three adjoint vanishing on general inversion-even quadrics

## Theorem

Let F be the normalized Horrocks–Mumford bundle on P4, B=End_0(F), and let iota be the normalizer inversion with ambient eigenspaces V_+ and V_- of dimensions three and two. Put R=P(V_+) and L=P(V_-), the fixed HM line. Then:

1. The actual restriction F_R has the Steiner resolution

       0 -> 3O_R(-3) -> 5O_R(-2) -> F_R -> 0.

2. Every hyperplane containing R satisfies H0(F_H(1))=0. A general product of two distinct equations of such hyperplanes is primary-good: H0(F_Q(2))=0. These products are inversion-even.
3. A general smooth inversion-even quadric satisfies

       H0(Q,B_Q(3))=0.

Consequently H0(B_Q(2))=0 on this same open. The theorem does not establish exact twist-four corank four. It also does not assert H0(B_H(2))=0 for invariant hyperplanes; the proof avoids that unresolved hyperplane-adjoint input. Boralevi's stability theorem for all hyperplanes supplies H0(F_H)=0, not either positive-twist vanishing. The previous general-hyperplane H0(F_H(1)) vanishing alone does not establish the new fixed-pencil statement. No universal assertion for H0(F_H(1)) on all hyperplanes is needed here.

## 1. The actual three-dimensional representation

Use the actual normalizer splitting N=H_5 semidirect SL2(F5), proved in Horrocks–Mumford, Section 1. The canonical Heisenberg operators indexed by z in F5^2 form a basis of End(V). Conjugation by the complementary SL2 permutes this basis through its natural action on z. There are exactly two orbits: zero and the nonzero vectors. Thus

       dim End_SL2(F5)(V)=2.

The central involution splits V into the nonzero summands V_+ and V_-. Complete reducibility and the commutant dimension force both summands to be irreducible and inequivalent. In particular V_+ is the actual irreducible three-dimensional representation of A5=SL2(F5)/{+1,-1}. This does not identify an abstract three-dimensional representation with the ambient one by dimension alone.

There is no A5 orbit of size at most four in R. An action on such an orbit gives A5 -> S_d for d<=4 and must be trivial, since A5 is simple and |S_d|<60. Every orbit point would therefore be a fixed projective point. Such a point is an invariant line, impossible in the irreducible representation V_+.

The plane R is disjoint from the 25 HM lines. It is disjoint from L. If a fixed point of iota belonged to another HM line, it would also belong to its distinct exchanged partner, contradicting disjointness of the lines. Thus evaluation U tensor O_R -> F_R(3), where U=H0(F(3)), is everywhere onto.

## 2. The positive fixed plane is Steiner

We use only the six possible plane resolutions in Boralevi, Corollary 2.2. They imply H0(F_P(-1))=0 for every plane P. They also give the following alternatives: an unstable restriction has h0(F_P)=1 and h0(F_P(1))=3; a stable non-Steiner restriction has h0(F_P(1)) equal to one or two; and the Steiner restriction has h0(F_P(1))=0.

If F_R were unstable, its unique section, up to scalar, would be preserved by the normalizer subgroup. It has no divisorial zero because H0(F_R(-1))=0. Its zero scheme has length c2(F_R)=4, is invariant, and is nonempty. Its support would contain an orbit of size at most four, contradicting Section 1. Hence F_R is stable.

Suppose h0(F_R(1))=1. The same argument applies: the unique section has no divisorial zero by stability, and its zero scheme has length c2(F_R(1))=4. This is again impossible.

Suppose h0(F_R(1))=2. The two sections are generically independent. Otherwise they lie in a saturated line subbundle O_R(a) of F_R(1). Stability of F_R forces a<=0, allowing at most one independent global section. Their nonzero determinant therefore spans an invariant line in H0(det F_R(1))=H0(O_R(1)). This is impossible because V_+^* is irreducible of dimension three. Equivariance of the determinant uses the actual bundle action; any difference between its linearization and the standard O_R(1) action is a character of the perfect group SL2(F5), hence trivial.

All non-Steiner alternatives are excluded. In particular F_R(1) is acyclic, not merely section-free.

## 3. Primary-good products inside the even subsystem

Let W=H0(I_R(1))=V_-^*. Every equation in W is odd, so every element of Sym^2 W is an even quadric. The degree-one Koszul calculation for the Steiner plane gives

       W tensor H1(F) -> H1(F(1))

as an isomorphism. Thus multiplication by every nonzero ell in W is injective on H1(F); the hyperplane restriction sequence proves H0(F_H(1))=0 for every H containing R.

The published generic-product theorem applies to this particular plane, not just to an unspecified generic plane. Its additional hypothesis is H0(I_R F(3))=0. This follows from the actual irreducibility of U: restriction U -> H0(F_R(3)) is equivariant, its kernel is a subrepresentation, and it is not the zero map because evaluation is onto along R. The actual U is the irreducible four-dimensional A5 representation, as checked in ACTUAL-GAMMA-CLEBSCH-CUBIC.md from Horrocks–Mumford (4.12).

Here is the exact module hypothesis and binary lemma, retaining the stronger condition that is essential to this application. Put A_j=H1(F(j)), choose a basis x,y of W, and let

       N=ker[Sym^2 W tensor A_0 -> A_2],  dim N=5.

The degree-one Koszul isomorphism identifies A_1 with W tensor A_0, and the degree-two Koszul calculation proves that the displayed map onto A_2 is surjective. The degree-three sequence is

       0 -> F(1) --(-y,x)--> F(2)^2 -> I_R F(3) -> 0.

Since H0(F(1))=H0(F(2))=0, it identifies H0(I_R F(3)) with the simultaneous kernel of x,y:A_1->A_2. Consequently the actual N satisfies

       z in W tensor A_0,  xz in N and yz in N  => z=0.       (*)

Condition (*) is strictly stronger than saying that N contains no space Sym^2 W tensor a for a fixed nonzero coefficient a.

To prove the needed binary lemma, evaluate N on P(W^*) and write B_p for the kernel of evaluation at p, with generic dimension b. Saturate the image in A_0 tensor O(2), obtaining a rank-(5-b) bundle E. The five independent polynomials give h0(E)>=5, and every splitting summand of E has degree at most two. If b>=3, rank E is at most two. Rank one is impossible. For rank two its splitting is necessarily (2,1) or (2,2). In the first case N=H0(E) contains Sym^2 W tensor a, violating (*). In the second, E=E_0 tensor O(2) for a fixed two-dimensional E_0 subset A_0, and N is a hyperplane in Sym^2 W tensor E_0. The conditions xz,yz in N impose at most two equations on the four-dimensional W tensor E_0, again violating (*). Thus b<=2.

Suppose every two general B_p meet nontrivially. For b=1 all are a fixed line, impossible because a polynomial vanishing at every p is zero. For b=2, the case where all B_p coincide is impossible by the same polynomial-vanishing argument. Otherwise choose two distinct B_p,B_q with intersection line L and three-dimensional span S. Every two-plane meeting both either contains L or lies in S. The irreducible curve of evaluation kernels must belong wholly to one of these two closed families. The common-L case is again impossible by polynomial vanishing. Hence all B_p lie in S. Evaluation of the three-dimensional polynomial space S then has generic rank at most one. Its saturated image O(d) satisfies d<=2 and h0(O(d))>=3, so d=2. Its inclusion in A_0 tensor O(2) is a constant coefficient a, forcing S=Sym^2 W tensor a subset N, contrary to (*). The b=0 case is immediate.

There are therefore distinct p,q with B_p intersect B_q=0. If ell_p,ell_q are their vanishing linear forms, the intersection is

       N intersect (ell_p ell_q tensor A_0),

which is exactly ker(ell_p ell_q:A_0->A_2), after dividing by the nonzero product. Thus some, and hence general, distinct products in Sym^2 W are primary-good.

For comparison, a five-dimensional relation space contained in Sym^2 W tensor span(a_0,a_1) can indeed dominate the entire quadratic plane while containing no fixed-coefficient three-space. It is nevertheless a hyperplane in that six-dimensional space, so the two-equation argument above produces a nonzero z violating (*). This potential counterexample is excluded by the actual degree-three Koszul kernel, not by a dimension-only general-position assertion.

The immutable proof is GENERIC-PRODUCT-PRIMARY-INJECTION.md at 7cd679d396232daaaf63e59ac2353613f66ececd; its content was checked against the current version. The degree-one and degree-two Koszul companion is GOOD-PLANE-PRIMARY-TRACE.md at 65c2bc0ffadd5abbaacf89695cce5ca465e43ce1. Both paths are under research/hm/order-four-quadratic-load/ in Akilleez-QA/read-em-and-weep. The new input here is that this particular invariant plane satisfies (*), proved by the actual irreducible U restriction, rather than by a generic-plane incidence argument.

## 4. The lower plane strata in the inversion-fixed family

Let Z be the closed union of Boralevi's four lower plane strata, excluding the Steiner open and the divisor stratum. It has dimension at most four in Gr(3,V). Let

       T={P(A directsum b): A subset V_+, dim A=2;
                              b subset V_-, dim b=1}.

This is the three-dimensional mixed inversion-fixed plane family Gr(2,V_+) times P(V_-). We claim dim(Z intersect T)<=2.

The unstable-plane locus has dimension two, so it cannot fill T. The stable lower stratum containing a 3-jumping HM line contributes nothing: no plane in T contains an HM line. Indeed every HM line is disjoint from R, so its vector space projects injectively, hence isomorphically, to V_-. A plane in T projects to a one-dimensional subspace of V_-.

The remaining stable lower stratum is (3,4)(1,2,2,3). Each such plane contains a unique 2-jumping line. This is Boralevi Proposition 4.5; the following argument also verifies uniqueness without a genericity assumption. The unique section of F_P(1) has a length-four zero scheme Z_P and no divisorial zero. Along any 2-jumping line its nonzero restriction is a section of O(3), with three zeros. Two distinct such lines would yield two length-three subschemes of Z_P whose scheme intersection has length at most one, since it lies in the intersection of the two lines. Their union would have length at least five, impossible. Existence follows from the nonzero linear entry O(-4)->O(-3) in the stated minimal resolution: it cannot vanish identically, since then O(-3) would split off F_P. On its zero line there is a quotient F_P|line -> O(-3), forcing splitting O(2) directsum O(-3).

For a plane in T that unique line must be fixed by iota. The irreducible jumping-line surface J2 is not fixed pointwise: it contains the 25 HM lines as points, and iota exchanges 24 of them in pairs. Hence its fixed locus has dimension at most one. A fixed line contained in a mixed plane is either contained in R or is itself mixed; L cannot be contained in a mixed plane. The first possibility cannot be 2-jumping: F_R(2) is globally generated by its Steiner resolution, whereas on a 2-jumping line its splitting would contain O(-1). A mixed fixed line is contained in a one-dimensional family of planes in T, obtained by extending its positive one-dimensional vector subspace to A. Thus the incidence of fixed 2-jumping lines with planes in T has dimension at most two. This proves the claim.

## 5. An invariant rank-four cone with an entirely good ruling

Consider the irreducible family D of nonzero even quadrics with rank of the positive block at most two. Its dense open consists of rank-four cones with positive vertex: the positive block has rank two and the negative block rank two. The primary-good products from Section 3 have positive block zero and negative block rank two, and belong to D. Primary goodness is open, so D has a nonempty primary-good rank-four open.

The connected centralizer G=(GL(V_+) times GL(V_-))/C* acts transitively on the rank-four positive-vertex cones. Fix one such cone and one ruling of its planes, parametrized by P1. Inversion preserves the ruling, acts nontrivially, and fixes precisely two ruling planes. These two planes are in T. Every other ruling plane belongs to the open G-orbit O in Gr(3,V), characterized by

       dim(P_vector intersect V_+)=1,
       P_vector intersect V_-=0.

These statements can be seen on the four-dimensional nondegenerate quotient by the positive vertex: its positive and negative eigenspaces both have dimension two. A fixed maximal isotropic plane is a sum of one isotropic line from each eigenspace; each ruling contains two of the four such choices. The other planes are graphs of isomorphisms between the two eigenspaces.

For each nonfixed ruling parameter, G maps onto the six-dimensional orbit O. Since dim Z<=4, the bad incidence in G times (P1 minus the two fixed points) has dimension at most dim G-1. For each fixed parameter the orbit is T, and Section 4 gives bad preimage dimension at most dim G-1. The union of these incidences is closed in G times P1, because Z is closed. Its projection is therefore a proper closed subset of G. A general G-translate has every ruling plane outside Z.

The primary-good open also pulls back to a nonempty open of G by transitivity. Since G is irreducible, these opens intersect. We obtain an actual inversion-even rank-four cone Q that is primary-good and whose chosen ruling has only Steiner or divisor-stratum planes.

## 6. Ruling pushforward and smoothing within the even system

Apply the already proved rank-four-cone argument to this Q. On the small resolution

       pi:Y=P_P1(O directsum O(1)^2) -> Q,

let p:Y->P1 and J=p_*pi^*F_Q(2). For each of the two allowed plane types, F_P(2) is globally generated with h0=5, higher cohomology zero, and its actual symmetric-product map is an isomorphism

       Sym^2 H0(F_P(2)) -> H0(B_P(3)).

Consequently J is locally free and the actual relative product is an isomorphism

       Sym^2 J -> p_*pi^*B_Q(3).

Primary goodness says H0(J)=H0(F_Q(2))=0. Every summand of J on P1 has negative degree, and so does every summand of Sym^2 J. Thus H0(B_Q(3))=0.

The universal hypersurface family over the even projective space P8 is flat, and restriction of B(3) is flat over that base. Vanishing is open by upper semicontinuity. The cone just constructed makes this open nonempty. Smooth even quadrics form a dense open, so the intersection is nonempty and dense. This proves the theorem entirely within the even subsystem.

## Dependencies and remaining gate

Primary sources:
- Horrocks–Mumford, A rank 2 vector bundle on P4 with 15,000 symmetries, Section 1 and (4.12): https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
- Boralevi, The Horrocks–Mumford bundle restricted to planes, Main Theorem, Corollary 2.2, Proposition 3.3 and Proposition 4.5: https://arxiv.org/pdf/math/0602002

Existing actual-map inputs are GOOD-PLANE-PRIMARY-TRACE.md, GENERIC-PRODUCT-PRIMARY-INJECTION.md, ACTUAL-GAMMA-CLEBSCH-CUBIC.md, and GENERIC-TWIST-THREE-ADJOINT-VANISHING.md. The last theorem is used only for its ruling pushforward proof, not by intersecting its generic open with the even subsystem.

The known parity calculation now yields the actual exact sequence on a nonempty open of smooth even quadrics

       0 -> H0(B_Q(4))_- -> C^34 -> C^38
         -> H1(B_Q(4))_- -> 0.

Injectivity of that specific Koszul multiplication, and vanishing of H1(B_Q(4))_+, remain separate. Neither is inferred from these dimensions. No selected coefficient, actual matrix rank, scan, or experiment is used.
