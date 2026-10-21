# Six projected lines from the six cyclic Heisenberg directions

Work over C. This concerns the actual primary degeneracy surface, not the fixed-three-section surface or the quadratic-parameter eightfold.

## Immutable inputs and statement

Use PR562 at 86b643fe2adecbd321d1c8f98be84fe2082bcd10 for the twenty-five pairwise disjoint distinguished lines, labeled by the torsor G=F5^2 of projective Heisenberg translations. Use PR563 at 56c3c4c37bd51fc710eec4b80662c5506f357f8f for the stabilizer representation: in the five-dimensional ambient Schrödinger representation V, the chosen center line is L_0=P(V_-), the negative two-dimensional eigenspace of the central reversal z of SL2(F5); its positive eigenspace V_+ is an irreducible three-dimensional A5 representation. The reversal acts on G by inversion.

Use PR567 at e0f15a5c6a49d2101dae450dae4d26171a259331 for the unique invariant integral reduced surface S containing all twenty-five lines. Its degree d satisfies 10<=d<=95 and 5|d. Projection from L_0 extends to a morphism f:S->P(V/V_-), generically finite of degree n=d-7. Every L_v with v nonzero maps isomorphically onto a target line. S is smooth near all the distinguished lines, and each has self-intersection -5. No global normality is assumed.

**Theorem.** The images of the twenty-four noncentral distinguished lines are exactly six distinct lines. They are indexed by the one-dimensional F5 subspaces U of G, and

f(L_v)=f(L_w) if and only if F5 v=F5 w.

Each image line is therefore covered isomorphically by the four distinguished lines with labels in U minus {0}. Consequently n>=4, and the divisibility 5|d improves the degree range to

15<=d<=95, 5|d.

This excludes degree ten for S. It does not determine d, the complete inverse images of these six lines, or the remaining surface components of the primary degeneracy scheme.

## 1. A universal cyclic-reversal identity

Fix any nonzero v in G. Choose an order-five Heisenberg lift g of v. We can normalize its central scalar so that z g z^{-1}=g^{-1}. Indeed, initially z g z^{-1}=omega^a g^{-1}; replacing g by omega^b g changes the discrepancy to a+2b modulo five, which can be made zero. All such lifts have order five.

The spectrum of g consists of all five fifth roots of unity with multiplicity one. One way to see this without computing any source-instance matrix is to choose a Heisenberg element whose commutator with g is a primitive central element. Conjugation by that element cyclically permutes the five eigenspaces of g. Their dimensions are equal and sum to five.

Let zeta be a primitive fifth root. The identity z g z^{-1}=g^{-1} pairs the zeta^j and zeta^{-j} eigenspaces. Choose eigenvectors e_j, j in F5, so that z(e_j)=e_{-j} for j nonzero. On the eigenvalue-one line z acts by +1: the two paired blocks each contribute one positive and one negative eigenvector, whereas the total eigenspace dimensions of z are three positive and two negative. Scale e_0 arbitrarily.

It follows that

V_- = span(e_1-e_{-1}, e_2-e_{-2}),
V_+ = span(e_0, e_1+e_{-1}, e_2+e_{-2}).

Identify the quotient V/V_- with V_+ using p_+=(1+z)/2. For every k in {1,2,3,4} and j in {1,2},

p_+(g^k(e_j-e_{-j})) = (zeta^{jk}-zeta^{-jk})/2 * (e_j+e_{-j}).

Both displayed coefficients are nonzero, since 2jk is not zero modulo five. Thus the image vector plane

p_+(g^k V_-)=span(e_1+e_{-1},e_2+e_{-2})

is independent of k. The four source lines g^k L_0=L_{kv} therefore have the same projected line. This holds for every cyclic direction F5 v, not for one evaluated HM instance.

There are six such cyclic directions, partitioning the twenty-four nonzero labels into sets of four. Hence there are at most six distinct target image lines.

## 2. The six images are distinct

The chosen SL2(F5) stabilizer acts transitively on the twenty-four nonzero labels. Its center acts trivially on the target plane, so the distinct image lines form a single orbit of A5 in the dual projective plane. The dual of V_+ is again an irreducible three-dimensional A5 representation.

There is no orbit of size one: such an orbit would give an invariant vector line, contradicting irreducibility. An orbit of size two, three, or four gives a nontrivial permutation representation of the simple group A5 into S_m. Simplicity makes it injective, impossible since m!<60.

An orbit of size five would have a stabilizer of order twelve, an A4 subgroup. Its normal Klein four subgroup K acts with zero fixed-vector space in the three-dimensional representation. To check this directly, each nonidentity involution has determinant one and, by faithfulness, is not the identity; hence its eigenvalues are 1,-1,-1 and its trace is -1. The character average gives dim(V_+^K)=(3-3)/4=0, and the same holds in the dual. But every one-dimensional character of A4 is trivial on K. Therefore A4 cannot preserve a vector line in either representation, excluding an orbit of size five.

The nonempty image-line orbit has size at most six and not less than six, so it has exactly six. As each cyclic direction already gives only one image, distinct cyclic directions give distinct images. Each image contains exactly four distinguished source lines above it.

## 3. Four lines in a fiber over a divisor bound the generic degree

Fix one image line ell and its generic point eta. The fiber of f over eta is zero-dimensional. Otherwise its closure would have dimension at least two inside the integral surface S and map into ell, contradicting dominance of f. Since f is proper, it is finite over a neighborhood of eta.

Set A=O_{P2,eta}, a discrete valuation ring. The finite base change of S to Spec A has a finite A-algebra B that is torsion-free over A: it is obtained from the integral dominating surface S. Thus B is a free A-module of rank n=[C(S):C(P2)]. Its closed fiber has length n over C(ell).

The four distinguished source lines mapping isomorphically to ell give four distinct points of this closed fiber, each with residue field C(ell). They are distinct because the source lines are pairwise disjoint. Each point contributes length at least one. Therefore n>=4. This argument does not require global normality of S, or unproved flatness on all of P2.

Substituting n=d-7 gives d>=11. Since 5 divides d, necessarily d>=15. Combined with PR567 this gives the asserted range.

## 4. A further effective-divisor consequence

For any cyclic direction U, put C_U=sum_{v in U} L_v, the five-line divisor including L_0. All five lines are globally Cartier on S: S is smooth near them and their ideals are the unit ideal away from them. The inverse-image Cartier divisor f^*(ell_U) contains each of the four noncentral lines at least once. Subtracting those lines leaves an effective Cartier divisor R_U with class

R_U ~ H-C_U.

For clarity, effectivity after subtraction can be checked locally: away from the four lines there is nothing to check, and near each line the surface is regular and its local defining equation divides the equation of the pullback divisor. The four lines are disjoint.

The established intersection numbers give

H.R_U=d-5,    R_U^2=d-35,
R_U.L_v=6 for v in U,    R_U.L_w=1 for w not in U.

In particular R_U is nonzero, since d>=15. These identities constrain the residual inverse-image divisors. They do not imply d>=35: an effective divisor can have negative self-intersection, and no moving-pencil assertion is made for the six R_U.

## 5. Six lines each tangent at two ordinary flexes of the center sextic

For this additional corollary use PR568 at ca47572a64b9a0110848ba6c8c33ce23209c068a: the restriction nu=f|L_0:P1->P2 is the normalization of an irreducible rational sextic C with exactly ten ordinary nodes, forming one A5 orbit, and no other singularities. The source action is faithful A5. Its pulled-back hyperplane bundle has degree six.

Let E be the union of the six projected target lines. None is a component of the irreducible sextic. Thus nu^*E is an invariant effective divisor on P1 of degree 36.

Every point stabilizer for a finite subgroup of PGL2(C) is cyclic: its derivative at the fixed point is faithful, since a finite-order projective transformation fixing a point and having derivative one is the identity. The cyclic subgroup orders in A5 are 1,2,3,5, so source orbit sizes are 60,30,20,12. An invariant effective divisor of degree 36 must therefore be three times an orbit of length twelve; no other nonnegative combination of these sizes has total 36. There is exactly one orbit of length twelve: the six subgroups of order five each fix two points, and different such subgroups cannot share a fixed point because point stabilizers are cyclic. Denote this orbit by T. We obtain

nu^*E=3 sum_{p in T} p.

We next exclude coincidences among target line intersections. If at least three of the six target lines passed through a point, its A5 orbit would have at least six points by the target-plane small-orbit exclusion in Section 2. Each such point accounts for at least three distinct unordered pairs of lines, and any line-pair meets at only one point. This would require at least eighteen of the available fifteen line-pairs, a contradiction. Hence the six lines have no triple concurrence, and their pairwise intersections form a fifteen-element invariant set J.

The image of T cannot lie in the ten-node orbit: an equivariant surjection from a transitive twelve-element set to a transitive ten-element set is impossible, because its fibers would have equal cardinality. Therefore nu(T) consists of smooth points of C, where normalization is an isomorphism. In particular nu(T) is a twelve-element orbit. It is disjoint from J. Indeed, if the two invariant sets met, transitivity would put all twelve points of nu(T) in J, leaving an invariant three-element set, contrary to the absence of target point orbits of size at most five.

Consequently each point of nu(T) belongs to exactly one of the six target lines. At such a smooth point the pullback multiplicity of that line is exactly three, by the displayed divisor identity. Every target line has total intersection degree six with C. It therefore meets C at exactly two distinct smooth points, each of intersection multiplicity three, and has no further intersections with C. Equivalently, the six lines are tangent at pairs of ordinary flexes of the center sextic. The twelve flexes constitute precisely the exceptional twelve-point A5 orbit on its normalization.

This is a statement about the six distinguished projected lines. It does not assert that these are all flexes or all bitangent lines of the sextic.

## Verification and scope

The argument consists of a universal representation identity, the small-orbit exclusion, a finite-module degree estimate, and Cartier intersection calculations. No selected actual HM coefficients, source point, numerical rank, or large computation are evaluated. It is a mathematical derivation, not a formal proof-assistant certificate. It uses the already established identification of the center line with the negative reversal eigenspace; it does not independently re-prove that input.
