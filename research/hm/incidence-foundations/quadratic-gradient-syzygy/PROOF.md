# Quadratic gradient syzygies and low-rank target quadrics

Work over C (the arguments use characteristic different from 2). Let E have dimension four. Let q_1,...,q_5 be independent homogeneous quadrics on E, and suppose their 5 by 4 Jacobian has generic rank four. Assume its maximal-minor gcd is an integral homogeneous quadric g. Let Q=V(g) in P(E). In the incidence application, assume the generic vector kernel over Q is one-dimensional, and its projective kernel map has nonplanar surface image (indeed the established theorem gives image Q itself).

## 1. Universal polarization lemma

For any number of independent quadrics q_i on any vector space, every homogeneous quadratic gradient syzygy

    sum_i r_i dq_i = 0

has the form r=Cq for a constant symmetric matrix C. In particular q^t Cq=0.

Proof. Write R_i and Q_i for the symmetric polar forms of r_i and q_i, respectively, normalized by R_i(x,x)=r_i(x) and Q_i(x,x)=q_i(x). The hypothesis is

    sum_i r_i(x) Q_i(x,y) = 0   for all x,y.

Replace x by x+ty and use x as the final argument. The coefficient of t^2 is

    sum_i [r_i(y) q_i(x) + 2 R_i(x,y) Q_i(x,y)] = 0.

Replace x by x+ty instead and use y as the final argument. The coefficient of t is

    sum_i [r_i(x) q_i(y) + 2 R_i(x,y) Q_i(x,y)] = 0.

Subtracting proves that the biform F(x,y)=sum_i r_i(x)q_i(y) is symmetric in x,y.

Put W=span(q_i) inside S=Sym^2(E^*). The tensor F belongs to S tensor W. Its symmetry also puts it in W tensor S. These two spaces intersect in W tensor W: choose any complementary subspace to W in S and decompose the tensor product. Independence of the q_i therefore gives r_i in W. Writing r=Cq, symmetry of F implies C is symmetric. Finally evaluate the original differential identity at the radial vector x to obtain 2 sum_i r_i q_i=0, hence q^t Cq=0. This completes the proof.

Conversely, every constant symmetric C with q^t Cq=0 gives the gradient syzygy (Cq)^t dq=0 by differentiation.

## 2. Consequences for the maximal-minor syzygy

Divide the signed maximal-minor vector by g. The resulting nonzero primitive vector r has homogeneous quadratic entries and satisfies r^t dq=0. Section 1 gives r=Cq with C symmetric and nonzero.

The matrix C has rank at least three. Indeed, a nonzero quadratic form of rank one or two over C factors into linear forms. A relation of rank at most two among q_i would therefore force a nonzero constant linear combination of the independent q_i to vanish, because C[E] is an integral domain.

The rational map [q]:P^3 --> P^4 has three-dimensional image. One way to see this is that the affine differential has rank four; its radial direction maps to the radial direction by Euler's identity, so the projective differential has rank three generically. Its image closure is consequently the irreducible quadric hypersurface q^t Cq=0. The quadratic relation is unique up to scalar: any other relation differentiates to a left syzygy, and the image is a quadric hypersurface with principal ideal. This uniqueness assertion concerns quadratic relations, not arbitrary polynomial differential syzygies.

## 3. Rank three cannot have nonplanar kernel image

If rank C=3, change basis among the q_i to put the relation in the form

    q_0 q_2 = q_1^2.

The three displayed quadrics remain independent. Unique factorization gives

    (q_0,q_1,q_2) = h (a^2,ab,b^2)

up to nonzero constant rescalings, where a,b are relatively prime homogeneous polynomials. Here a and b have equal degree because q_0,q_1,q_2 have the same degree. Independence forces their degree to be positive. Since deg(h)+2deg(a)=2, it follows that h is constant and a,b are independent linear forms.

For a general x in the integral nonplanar quadric Q, a(x) and b(x) are both nonzero. A kernel vector y for the full Jacobian must in particular annihilate d(a^2)_x and d(b^2)_x. Thus a(y)=b(y)=0. The projective kernel image is contained in the fixed projective line P(ker(a) intersect ker(b)). This contradicts its being a nonplanar surface. Hence rank C is not three in the incidence setting.

## 4. Rank four forces an ambient projective-linear involution

If rank C=4, change basis so that

    q_0 q_3 = q_1 q_2.

Unique factorization of this rank-one polynomial matrix gives

    (q_0,q_1,q_2,q_3) = h (l_1 m_1,l_1 m_2,l_2 m_1,l_2 m_2),

with each pair (l_1,l_2) and (m_1,m_2) relatively prime. For completeness, take a gcd a of q_0,q_1 and write q_0=a m_1, q_1=a m_2 with gcd(m_1,m_2)=1. The relation forces q_2=b m_1 and q_3=b m_2. Removing gcd(a,b) gives the claimed expression. Equal degrees of the four entries make each pair homogeneous of a common degree. Independence of all four entries forces both pair degrees to be positive. Their sum plus deg(h) equals two, so h is constant and all l_i,m_j are linear. Each pair is linearly independent.

Let L=span(l_1,l_2) and H=span(m_1,m_2), subspaces of E^*. Their intersection cannot have dimension two, because then the four products would lie in Sym^2 L of dimension three.

For general x in Q, both vectors l(x) and m(x) are nonzero. The four derivative equations for a kernel vector y say

    l(y) tensor m(x) + l(x) tensor m(y) = 0.

For nonzero l(x),m(x), this elementary tensor equation is equivalent to

    l(y)=t l(x),    m(y)=-t m(x)

for a scalar t. To verify this, quotient the first tensor factor by the line spanned by l(x), and then quotient the second factor by the line spanned by m(x).

If dim(L intersect H)=1, choose nonzero z in their intersection. Since Q is nonplanar, z(x) is nonzero at general x in Q. The two equations give z(y)=t z(x)=-t z(x), hence t=0. Thus y annihilates L+H, which has dimension three. The projective kernel image is the fixed point P((L+H)^perp), again impossible.

Therefore E^*=L direct-sum H. Define the invertible linear involution T on E by

    l(Tx)=l(x),    m(Tx)=-m(x)

for every l in L, m in H. The first four Jacobian rows have kernel precisely C Tx on the open under consideration. Consequently the full kernel map on Q is [x] -> [Tx]. In particular the birational involution of the common factor quadric extends to an ambient projective-linear involution with two-dimensional +1 and -1 eigenspaces.

There is also an explicit equation for Q. Let q_4 be the fifth quadric with polar form Q_4. The last derivative equation on the candidate partner is Q_4(x,Tx)=0. This is a nonzero quadratic polynomial: if it vanished identically, the full Jacobian would have generic rank at most three, contrary to hypothesis. It vanishes on Q, so it is a scalar multiple of g. In coordinates E=E_+ direct-sum E_-, if q_4=A(u)+B(v)+D(u,v), the equation is A(u)-B(v)=0 (the mixed term cancels).

## 5. Exact scope

Without any extra compatibility map, the conclusions are: the primitive quadratic syzygy always has r=Cq with C constant symmetric; rank C is four or five in the nonplanar-incidence setting; rank four forces an ambient balanced linear involution.

With the additional linear map v:K -> E, dense compatibility v(xy) in span(x,y), and square avoidance v(e^2) not in Ce for every nonzero e^2 in K, the established fixed-linear-correspondence exclusion applies to Section 4. Thus only rank C=5 remains.

This note does not classify rank-five quadratic parameterizations of the smooth three-dimensional target quadric and does not exclude that last case. In particular, it does not assume that all such parameterizations are standard stereographic ones or that their Jacobian gcd must be a double plane.
