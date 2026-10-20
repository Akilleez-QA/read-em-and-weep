# Full middle-surviving two-zero scheme: exact quadrics and center-supported embedded structure

## Theorem

Work over C with dim V=5 and target J of dimension 20. Use the stipulated trilinear map f, outer symmetry f(x,y,z)=f(z,y,x), the cyclic-zero identity, and the split injection A_u:H→J, A_u(v)=f(u,u,v), for a complement H to Cu. Assume the residual quadratic map Q_u on V/Cu has rank ten at the common line under consideration.

Consider the two-zero stratum with precisely the middle input nonzero. After shrinking its smooth five-dimensional u-base S, write

    (x,y,z)=(a u+p,u,c u+q),     p,q∈H,   dim H=4.

Let R=O(S), T=R[a,c,p_1,…,p_4,q_1,…,q_4], and set

    L_i=c p_i+a q_i,
    E_ij=p_i q_j+p_j q_i    (1≤i≤j≤4),
    I=(L_i,E_ij),
    P_x=(a,p),    P_z=(c,q),    P=(p,q),    m=(a,c,p,q),
    Q=(P²,L_i),
    K=I+(p_i q_j : all i,j).

The exact full zero scheme of f on this chart, including all its components and embedded structure, is Spec(T/I). In particular the coefficients of the resulting equations do not depend on u. This is an exact relative product, not merely a normal cone or a model for the isolated primary component.

The following statements hold:

1. K=P_x∩P_z∩Q. Here P_x and P_z are prime, and Q is P-primary.
2. K/I is a free R-module of rank six, with basis the classes of p_i q_j for i<j. Its annihilator is exactly m. It is the entire submodule of T/I supported on the two-zero center, equivalently H⁰_m(T/I).
3. There is an irredundant primary decomposition

       I=P_x∩P_z∩Q∩(I+m³).

   The last ideal is m-primary. Thus the associated primes are precisely P_x, P_z, P, and m. The first three are minimal; m is the sole embedded prime.
4. The embedded primary quotient T/(I+m³) is free of rank 52 over R, with graded ranks 1,10,41. This length is a feature of this chosen primary component, whereas the intrinsic center-supported torsion has rank six.
5. The reduction has ideal (c p_i,a q_i,p_i q_j). Its nilradical has square zero. As a module over the reduced rank-one component D=Spec R[a,c], it is

       R[a,c]^4 ⊕ R^6,

   with the first summand represented by c p_i=−a q_i and the second by the six antisymmetric cross classes. The second summand is supported on a=c=0.
6. At a closed point of the two-zero center, X has local dimension 10, embedding dimension 15, and depth 5. Its three minimal components have dimensions 10,10,7 and generic multiplicities 1,1,5. The defining ideal has exactly fourteen minimal quadratic generators in the ten transverse variables.
7. The chart is flat over S; every graded piece is locally free over S. Its full closed-point tangent cone is T_uS times the fixed transverse quadratic cone Spec C[a,c,p,q]/I. Thus the relative-cone description now determines the entire tangent cone in this middle-surviving case.

All assertions are conditional only on the stated symbolic identities, the repeated-input split injection, and the rank-ten hypothesis. No actual input, matrix, operation, rank instance, or source evaluation is used.

## 1. Algebraic target splitting gives the full ideal

Choose a fixed linear functional ell nonzero at u, and put H=ker ell. Then p,q,a,c,u are exact independent coordinates on the open chart ell(y)≠0. The stipulated identities give

    f(a u+p,u,c u+q)=c A_u(p)+a A_u(q)+B_u(p,q),
    B_u(p,q)=f(p,u,q).

Outer symmetry says B_u(p,q)=B_u(q,p). Thus B_u is a linear map out of Sym²H. In a basis of H,

    B_u(p,q)=Σ_i p_iq_i B_u(e_i,e_i)
             +Σ_{i<j}(p_iq_j+p_jq_i) B_u(e_i,e_j).

Every coordinate of B_u(p,q) therefore belongs to the ideal E=(E_ij); the diagonal factor two is invertible.

Split the bundle injection A_u:H→J algebraically, writing J=A_u(H)⊕J' after shrinking S. Let π be projection to J'. The rank-ten hypothesis for Q_u says precisely that the induced map

    Sym²H → J',    vw ↦ π B_u(v,w),

is injective of rank ten. Its source has rank ten, so after further shrinking it has an algebraic left inverse. This is a vector-bundle splitting on the given rank open; it requires no chosen numerical rank evaluation.

Applying this left inverse to the residual equations π B_u(p,q)=0 recovers all ten generators E_ij. Conversely those residual equations belong to E, so their ideal is exactly E. The H-projection of the full equation is

    c p+a q + A_u^{-1}(the A_u(H)-projection of B_u(p,q)).

Its second summand is already in E. Consequently the full component ideal is exactly (E,cp+aq)=I. No division by a or c is involved, and the argument holds at a=c=p=q=0 itself.

This argument is specific to a nonzero middle input. The mixed term in a nonzero-outer-input chart is f(p,q,u); its antisymmetric part is not disposed of by this proof.

## 2. Elementary consequences of the quadrics

Write w_ij for the class of p_iq_j in T/I. The equations give

    w_ij=−w_ji,     w_ii=0.

Every mixed monomial of degree at least three in p,q vanishes. For example, modulo E,

    p_i p_j q_k=−p_i p_k q_j
               = p_k p_j q_i
               =−p_j p_i q_k,

so it is zero because 2 is invertible. The same argument handles one p and two q, including repeated indices.

Multiplying L_i by p_j and L_j by p_i, then adding and subtracting, gives

    c p_i p_j=0,     a w_ij=0.

Multiplying L_i by q_j and L_j by q_i gives

    a q_i q_j=0,     c w_ij=0.

It follows that m annihilates every w_ij, and K/I is generated over R by the six classes w_ij, i<j.

These six classes are R-linearly independent. Give all ten variables a,c,p,q total degree one and R degree zero. The degree-two part I_2 is the direct R-span of the four L_i and ten E_ij. The L_i use monomials involving a or c, whereas the E_ij span the symmetric cross tensors. They have zero intersection with the six-dimensional alternating cross-tensor subspace. Since I is generated in degree two, no higher-degree relation can create a relation in that subspace. Hence

    K/I ≅ (T/m)^6=R^6,

with all six generators in total degree two. Its annihilator is exactly m since R is an integral domain.

## 3. The three-component intersection

Put D=R[a,c]. The ring T/Q is the split square-zero algebra

    D ⊕ (a,c)D^4.

To see this, map p_i↦a t_i and q_i↦−c t_i into D[t_1,…,t_4]/(t)^2. The module of relations on (a,−c) is generated by (c,a), because a,c is a regular sequence. Thus its kernel is exactly (P²,L_i)=Q. Since D is a domain and (a,c)D^4 is torsion-free over D, every element with nonzero D-part is a nonzerodivisor. All elements with zero D-part are square-zero. This proves that Q is P-primary.

There is evident containment K⊂P_x∩P_z∩Q. For the reverse containment use the grading by degree in p,q, with a,c in degree zero. The quotient T/K has the following direct decomposition as a D-module:

    degree 0: D;
    degree 1: M=D^8/(c p_i+a q_i), isomorphic to (a,c)D^4;
    degree d≥2: (D/(c))⊗_R Sym^d(R^4_p)
                 ⊕ (D/(a))⊗_R Sym^d(R^4_q).

Indeed K kills all mixed products. Multiplying L_i by positive-degree pure p monomials imposes exactly c times every pure p monomial of degree at least two; multiplying by pure q monomials imposes exactly a times every pure q monomial of degree at least two. There are no relations between the displayed homogeneous summands.

The map T/K→T/Q is the identity on degree zero and degree one, and kills the higher-degree summands. Therefore an element in its kernel consists of pure p and pure q tails. The map to T/P_z=R[a,p] is injective on the p tail; the map to T/P_x=R[c,q] is injective on the q tail. Hence

    T/K → T/P_x ⊕ T/P_z ⊕ T/Q

is injective. Its kernel calculation proves K=P_x∩P_z∩Q.

The three radicals P_x,P_z,P are pairwise incomparable. This is an irredundant primary decomposition of K, with precisely these three associated primes. In particular H⁰_m(T/K)=0: for each displayed primary ideal its radical omits an element of m, whose powers remain nonzerodivisors in the corresponding primary quotient.

Combining this with 0→K/I→T/I→T/K→0 and m(K/I)=0 proves

    H⁰_m(T/I)=K/I.

## 4. The embedded primary component and exhaustive associated primes

Let U=I+m³. The quotient T/U has no terms of total degree at least three. Its graded pieces have ranks

    degree 0: 1;
    degree 1: 10;
    degree 2: binomial(11,2)−4−10=41.

The direct coefficient description in degree two proves that all three pieces are free over R. Thus T/U is free of rank 52 over R, with nilpotent ideal m/U and reduced quotient R.

If s∉m, its constant term is a nonzero element r of R. Multiplication by s has multiplication by r as its map on each associated graded piece for the finite m-filtration. Since these pieces are R-free, that map is injective. The filtered map itself is therefore injective. Thus every zero divisor of T/U lies in its nilradical, and U is m-primary.

Modulo I, the ideal K/I is concentrated in total degree two, whereas (I+m³)/I is concentrated in degrees at least three. Their intersection is zero. Hence

    I=K∩U=P_x∩P_z∩Q∩U.

The component U is necessary because K/I has rank six. The other three components are necessary because their incomparable radicals are the three minimal primes, and localization at any one of them removes the other components. This decomposition is irredundant.

For completeness, the exact sequence above gives

    Ass(T/I) ⊂ Ass(K/I) ∪ Ass(T/K)
             ={m,P_x,P_z,P}.

The submodule K/I supplies m as an associated prime, and the three minimal primes are associated to T/I. Thus the displayed list is exhaustive: there are no further embedded primes, including ones imposing additional conditions on u within this rank-ten open.

The rank 52 of T/U is not the intrinsic embedded-torsion length. The intrinsic module H⁰_m(T/I) has rank six. Embedded primary components are not generally unique; the exhibited U is a convenient explicit choice.

## 5. Reduction and square-zero nilradical

The two coordinate ideals use disjoint groups of variables, so

    P_x∩P_z=(ac,a q_i,c p_i,p_iq_j).

Intersecting with P=(p,q) removes only the base term ac and yields

    sqrt(I)=P_x∩P_z∩P=(a q_i,c p_i,p_iq_j).

One may verify the latter intersection by p,q-degree: any positive-degree multiple of ac is already in (cp,aq), and degree zero has zero intersection with P.

Modulo I, write h_i=c p_i=−a q_i. The nilradical N is generated by h_i and w_ij, i<j. Section 2 shows that p and q kill these generators and that a,c kill the w_ij. It also gives N²=0: all products involving a w_ij, c w_ij, p w_ij or q w_ij vanish, and h_i h_j=c²p_i p_j=0.

There are no D-linear relations among the h_i. In T/Q they map to ac t_i, which are D-linearly independent. Nor can a nonzero combination of h_i equal an alternating cross class: applying T/I→T/Q forces its coefficients to vanish, after which the independence from Section 2 applies. Consequently

    N ≅ D^4 ⊕ (D/(a,c))^6.

The representatives h_i and w_ij all have total degree two. This decomposition is a module statement, with the D-action obtained by restricting to the reduced rank-one component. It does not assert that the whole reducible scheme is a split square-zero algebra over its reduction.

## 6. Flatness, dimensions, depth, and tangent cone

The target-splitting argument identifies the chart exactly with R⊗_C A_*, where

    A_*=C[a,c,p,q]/(cp+aq, p_iq_j+p_jq_i).

Thus the chart is a product over its u-base and is R-flat. Each total graded piece is finite free over R. This also follows directly from the module description in Section 3 and the six extra free classes in Section 2.

At a closed point of the center the base has regular local dimension five. Its regular parameters remain a regular sequence on the product ring. After quotienting by them, the transverse local ring has a nonzero socle: the six w_ij are killed by its whole maximal ideal. Its depth is therefore zero, and the depth of the full local ring is exactly five.

The coordinate components have fiber dimension five and are generically reduced. The rank-one component has fiber dimension two; its primary quotient becomes D⊕D^4 after passing to the fraction field of D, so its generic multiplicity is five. Adding the five-dimensional base gives component dimensions 10,10,7 and local dimension 10 at their common center. The center itself has dimension five.

All equations have order two at the center. Their fourteen quadratic forms are independent, as shown in Section 2. There are ten independent transverse tangent directions and five base tangent directions, so the embedding dimension is 15. The fourteen quadrics minimally generate the ideal there.

Because the relative equations are coefficient-free and homogeneous, the maximal-ideal associated graded ring at a closed center point is

    gr(O_{S,u}) ⊗_C A_*.

Therefore the full tangent cone equals T_uS times the transverse quadratic cone, with its six center-supported embedded classes retained. This is stronger than the relative normal-cone assertion available before the exact full ideal was identified.

An optional check is the transverse Hilbert series, obtained from the D-module decomposition and the six extra degree-two classes:

    H_{A_*}(t)=2/(1−t)^5+5/(1−t)^2−10/(1−t)+4+6t².

Its initial graded dimensions are 1,10,41,80. In particular its fourteen quadratic relations agree with 55−41=14.

## 7. Relation to the earlier boundary and primary-closure results

This theorem upgrades the middle-surviving portion of /research/hm/middle-surface/two-zero-boundary/PROOF.md from a relative quadratic-cone description to a complete original germ. In this case the projective quadratic scheme has only the three listed components. The extra embedded module is supported on the center and disappears when the cone is blown up; this explains why the previously established projective and endpoint charts did not detect it.

The ideal Q coincides with the local isolated rank-one primary component in /research/hm/middle-surface/global-rank-one-primary-closure/PROOF.md. Its square-zero module is (a,c)D^4, and its own full local depth is six at the center. The full X has the additional coordinate components and the rank-six center-supported torsion, so its depth is instead five. These different depth claims concern different schemes.

The proof makes no claim about a two-zero stratum with nonzero first or third input, about rank-drop common lines, or about the all-zero vertex. In those cases the same elimination need not apply. All calculations here are symbolic identities in formal coordinates, not evaluated source instances.
