# Exact square-conic rank stratification and the actual sextic factorization

## 1. Pinned interface and statement

Work over C with G=SL2(F5), its fixed binary representation W, A=Sym²W, D=Sym⁴W, and the LOWER endpoint irreducible four-dimensional A5-module P. Let X=P(W), with its tautological bundle O_X(−1), and identify X with the square conic in P(A) by [u]↦[u²]. Thus O_P(A)(1)|X=O_X(2). All twists below, unless explicitly described otherwise, are on X.

We use PR661–665's canonical source identification and two-channel interface, not a new selected actual HM evaluation. In particular

Q=Q_+⊕Q_−,
B_+(b,h)=π8(bh),   B_−(b,h)=π6((b,h)_1),
Sym⁸W=D⊕P,   Sym⁶W=V⊕P,
K_(u²)=u³W.

Here π8 and π6 are the projections to P followed by fixed nonzero identifications with the endpoint P. Choosing these representatives merely introduces coefficients α,β in q=αB_++βB_−; no numerical values of actual coefficients will be used.

The actual additional hypothesis is exactly PR665's established normal-variation datum at 1cc13d0bf21abc6553c51a48c72896758cbc333a: a nonzero actual family q_eta has nonzero symmetric and alternating components; at one C5 square, with eigenlines Cu,Cv, it kills u³v and is nonzero on u⁴. Let C_act⊂Q be its projective family line, intrinsically ker(q↦q(u²,u³v)). PR665 proves this line independent of the chosen square in the twelve-point orbit and identifies it with the image of the one-dimensional actual normal space.

**Theorem.** On the square conic:

1. The pure alternating family has restricted rank one everywhere.
2. Every family with nonzero symmetric component has generic restricted rank two.
3. For q on C_act, the rank-one degeneracy scheme is exactly the twelve C5 square points, each reduced. Rank is two everywhere else. For every other projective family with nonzero symmetric component, rank is two everywhere.
4. For q on C_act, after twisting the restricted map by O(−4), its saturated image E in P⊗O has E≅O(−1)², and its quotient is O(1)². Equivariantly E=W′⊗O(−1) and the quotient is W′⊗O(1), where W′ is the other binary two-dimensional representation characterized by P≅W′⊗W. The map factors uniquely through E:

W⊗O(−7) → W′⊗O(−1) → P⊗O.

The first arrow is a 2×2 matrix of binary sextics. Its determinant is, up to nonzero scalar, the degree-twelve form with simple zeros precisely at the C5 orbit. Untwisted the factorization is

K|X=W⊗O(−3) → W′⊗O(3) → P⊗O(4).

These are structural consequences of the pinned interface and actual two-input datum. They do not evaluate any additional actual coefficient, rank, or source instance.

## 2. The relevant bundles and universal formula

Multiplication gives a fiberwise injective map W⊗O(−3)→D⊗O, sending w⊗u³ to u³w. Its image is K|X by the established transvectant-kernel identification. The endpoint's quadratic parameter twist pulls back to O(4); hence the restricted family is a map W⊗O(−3)→P⊗O(4). Twist by O(−4) to obtain

φ_q:W⊗O(−7)→P⊗O.

For a symplectic pairing [ , ] on W and the unnormalized first transvectant, its fiber formula is

φ_q(u,w)=απ8(u⁷w)+4β[u,w]π6(u⁶).                 (1)

Indeed (u⁴,u³w)_1=4[u,w]u⁶. Both terms in (1) are homogeneous of degree seven in u and linear in w. This explicitly verifies that the alternating term has the SAME bundle degree as the symmetric term. Set C8(u)=π8(u⁸), C6(u)=π6(u⁶). Then

φ_q(u,u)=αC8(u).                               (2)

Both C8 and C6 are nowhere zero on X: every projective A5 orbit has at least twelve points, whose nth powers span SymⁿW for n=6,8. A vanished projection at one point would put this whole spanning orbit into a proper complementary submodule. Equivalently Cn defines a line subbundle O(−n)→P⊗O.

If α=0 and β≠0, formula (1) has rank exactly one everywhere. Its kernel is the tautological w=u line, namely O(−8) in W⊗O(−7), and its saturated image is C6(O(−6)). This also handles the pure alternating case without a genericity argument.

## 3. An everywhere embedded symmetric osculating bundle

Recall the invariant Wronskian bound from PR663. If U⊂SymⁿW is a G-stable k-dimensional subspace containing a form with a root of multiplicity m whose orbit has size N, then

N max(0,m−k+1) ≤ k(n−k+1).                     (3)

For completeness, the Wronskian of k linearly independent degree-n binary sections is nonzero in characteristic zero and has total degree k(n−k+1). Its local order is Σ_i(a_i−i) for the vanishing sequence a_0<…<a_(k−1). A section of order m forces local weight at least max(0,m−k+1); equivariance gives the same lower bound at all N orbit points. This proof includes base points.

Apply (3) to the complementary D⊂Sym⁸W, with k=5,n=8. No nonzero element of D can have a root of multiplicity seven, since N≥12 would imply 36≤20. For every nonzero u,w, the form u⁷w has such a root. Therefore

π8(u⁷w)≠0 for all u≠0,w≠0.                   (4)

Consequently the map

S:W⊗O(−7)→P⊗O,   S(u,w)=π8(u⁷w)

is fiberwise injective everywhere. Its image F is a rank-two subbundle, not merely a generic subsheaf, and S identifies F≅W⊗O(−7). Fiberwise F is the first osculating plane spanned by C8(u) and its derivative in a complementary direction. No argument about the actual map's minors or rank has been used to obtain F.

## 4. Generic rank two without coefficients

Suppose α≠0. Equation (2) ensures φ_q has rank at least one everywhere. If β=0 it is αS, already everywhere rank two.

Assume β≠0 and, for contradiction, that φ_q has generic rank one. Its generic image is then the line spanned by C8(u), by (2). At a general u choose any w with [u,w]≠0. Formula (1) implies

C6(u)∈span(C8(u),S(u,w))=F_u.

Consider the global bundle map C6:O(−6)→P⊗O and its composite into the locally free quotient (P⊗O)/F. This composite vanishes generically, hence everywhere on the integral curve X. Thus C6 factors through F. But

Hom(O(−6),F)=W⊗H⁰(O(−1))=0,

contradicting the nonzero map C6. This proves generic rank two for EVERY α≠0, without choosing or calculating α/β. The argument is not circular: F is the symmetric osculating subbundle independently constructed in Section 3, not the actual image saturation to be calculated later.

## 5. Exact degeneracy scheme and complete classification

For α≠0, the 2×2 minors of φ_q are sections of O(14), not all zero by Section 4. On the smooth curve X their common ideal defines an effective divisor D_q: locally a discrete valuation ring makes this ideal principal, with order the minimum of the minor orders. Thus deg D_q≤14. Equivariance makes D_q A5-invariant, including its multiplicities.

Point stabilizers in the projective A5 action are cyclic of orders 1,2,3,5. Hence possible orbit sizes on X are 60,30,20,12. There is a unique orbit of size twelve: the two fixed points of each of the six C5 subgroups. It follows immediately that D_q is either empty or exactly that orbit with multiplicity one. In particular neither extra points nor higher multiplicity can be hidden in the degeneracy scheme.

At a C5 square choose a binary generator with weights η,η⁻¹ on u,v, η primitive tenth root. Formula (2) lies in P-weight η⁸. The mixed value φ_q(u,v) lies in P-weight η⁶. These distinct weight spaces are one-dimensional. The pure value is nonzero for α≠0, so rank drops precisely when the mixed value is zero. Each channel has nonzero mixed value: the symmetric one by (4), and the alternating one by C6≠0. Therefore mixed evaluation Q→P[η⁶] has a unique kernel line meeting neither parity axis. This is exactly C_act by the supplied actual datum and PR665's reconstruction.

It follows that D_q is the twelve-point reduced divisor exactly for q∈C_act, and is empty for all other α≠0. Combined with the pure alternating case, this proves the complete stated square-conic classification. It concerns the rank of a FIXED map K_(u²)→P, not the different rank of the family-detection map Q→Hom(K_a,P) studied in PR663–664.

## 6. Saturation and exact splitting

Fix nonzero q∈C_act. Since φ_q has generic rank two, it is an injection of sheaves, with image I≅W⊗O(−7), of degree −14. Let E be its saturation in P⊗O. On a smooth curve E and (P⊗O)/E are locally free. At each point the local Smith normal form for I→P⊗O has elementary divisors t^a,t^b; the order of the minors is a+b and equals length(E/I). Therefore

length(E/I)=deg D_q=12,   deg E=−14+12=−2.

Moreover rank is at least one at every point, and D_q is reduced, so the local elementary divisors at each of its twelve points are (1,t). Thus E/I has length one there and zero elsewhere.

Every summand of E has degree ≤0 because E embeds into O⁴. The subspace H⁰(E)⊂H⁰(P⊗O)=P is G-stable. Irreducibility of P makes it zero or all of P. The latter is impossible: it would place all four constant sections in a rank-two subbundle. Hence H⁰(E)=0, all its summands have degree ≤−1, and degree −2 gives

E≅O(−1)⊕O(−1).

Write H=(P⊗O)/E. This rank-two bundle is globally generated, has degree two, and H* embeds into P*⊗O. The identical irreducibility argument gives H⁰(H*)=0. Its splitting therefore has both degrees positive, and H≅O(1)². These statements use the actual simple divisor, not merely a negative-degree heuristic.

## 7. Equivariant identification and sextic matrix

Set R=H⁰(E(1)), a two-dimensional G-module. Evaluation gives an equivariant isomorphism R⊗O(−1)≅E. The center acts trivially on E⊂P⊗O, and as −1 on O(1), so it acts as −1 on R. The inclusion E→P⊗O corresponds, by adjunction and H⁰(O(1))=W*, to a nonzero G-map

R⊗W→P.

Since P is irreducible and both sides have dimension four, this is an isomorphism. In particular R is irreducible. Also R is not W: W⊗W=1⊕Sym²W has no P constituent. Thus R is the other binary two-dimensional module W′, or equivalently it is intrinsically characterized here by the tensor isomorphism P≅W′⊗W. The invariant symplectic form identifies W* with W when needed; no parameter twist is discarded.

After fixing this tensor isomorphism, the inclusion E→P⊗O is the tautological inclusion

W′⊗O(−1)→W′⊗W⊗O.

It is unique up to scalar: its equivariant Hom space is Hom_G(W′⊗W,P)=End_G(P)=C. Consequently the actual map factors through this canonical rank-two subbundle. Its first arrow is W⊗O(−7)→W′⊗O(−1), with entries in H⁰(O(6)); its determinant is a nonzero degree-twelve section. Both binary representations have determinant one, so it may be regarded as an invariant degree-twelve binary form, up to scalar. Its divisor is exactly D_q by the saturated inclusion, hence the twelve simple C5 points.

The sextic arrow itself is also unique up to scalar. Indeed the invariant symplectic form gives W*≅W, and hence

Hom_G(W⊗O(−7),W′⊗O(−1))
 ≅ (W*⊗W′⊗Sym⁶W*)^G
 ≅ Hom_G(Sym⁶W,P)
 ≅ C,

using P≅W′⊗W and Sym⁶W=V⊕P. Thus the unique nonzero equivariant sextic arrow, composed with the tautological inclusion, recovers the restricted actual map up to overall scale. This fixes its projective reconstruction, not the numerical normalization of the actual normal coordinate or the chosen parity representatives.

The tautological sequence 0→O(−1)→W⊗O→O(1)→0 is G-equivariant because det W=1. Tensoring it with W′ identifies the quotient equivariantly as H≅W′⊗O(1). The complete exact quotient package is therefore

0→W⊗O(−7)→W′⊗O(−1)→T→0,
0→W′⊗O(−1)→P⊗O→W′⊗O(1)→0,

where T has one-dimensional length-one stalk at each of the twelve C5 points. Untwisting the second sequence gives 0→W′⊗O(3)→P⊗O(4)→W′⊗O(5)→0. No scalar normalization of T, the determinant, or the actual normal coordinate is claimed.

## 8. Scope and sources

The theorem classifies the restriction to the square conic, identifies the actual image saturation, and fixes the determinant divisor of a sextic factorization. It does not determine the rank of the full D→P map, identify the actual family with any nonsquare axis-annihilating channel, compute an actual numerical parity ratio, evaluate a next ambient division, establish a fourth Bockstein, or solve source membership, higher lifting, or complete repair. The lower P is not the third-Bockstein P.

- https://github.com/Akilleez-QA/read-em-and-weep/pull/1
- https://github.com/Akilleez-QA/read-em-and-weep/pull/543
- https://github.com/Akilleez-QA/read-em-and-weep/blob/1325647fd916bf2daa71b11efeae6d52cfefa2cd/research/hm/endpoint-square-reconstruction/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/f75a18fd411350adda35dedf18751eee002a39bc/research/hm/endpoint-base-locus-exclusion/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/ad3ab59f6fbbbb3e5bde1da58b3b92a1f49c6889/research/hm/secant-detection-exceptions/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/pull/664
- https://github.com/Akilleez-QA/read-em-and-weep/blob/1cc13d0bf21abc6553c51a48c72896758cbc333a/research/hm/actual-endpoint-parity-consequences/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/fb574c01207099eeb63960da5cb23ad2f2498a84/research/hm/order-four-quadratic-load/ACTUAL-ENDPOINT-NORMAL-VARIATION-IS-NONZERO.md
