# A four-dimensional rank-one-free subspace of sl(3) is not totally isotropic

## Statement and scope

Work over C. Let U be a three-dimensional vector space, and let K⊂sl(U) be a four-dimensional linear subspace containing no nonzero rank-one endomorphism. Then the quadratic polynomial

    q|K : A ↦ tr(A²)

is not identically zero.

More generally, no projective integral surface contained in P(sl(U)) can consist entirely of regular nilpotent endomorphisms. Here “regular nilpotent” means a nilpotent endomorphism of rank two, with its scalar multiple regarded as the same projective point.

This is a universal vector-bundle argument. It computes no actual HM/source/model matrices, products, ranks, points, jets, residues, or Massey values.  We use standard resolution of singularities for complex projective surfaces and elementary Chern-class identities.

## 1. A twisted regular-nilpotent endomorphism on a surface

Let X be a smooth integral projective surface and let M be a line bundle on X. Put E=U⊗O_X. Suppose a bundle map

    N:E → E⊗M

satisfies N³=0, where powers are twisted compositions (thus N²:E→E⊗M² and N³:E→E⊗M³). Suppose every geometric fiber of N has rank two and every geometric fiber of N² has rank one.

Set

    F1=ker N,     F2=ker N².

These are vector subbundles of E of ranks one and two. Indeed, on the reduced scheme X constant geometric rank implies that the larger minors vanish identically; around an invertible maximal minor, elementary bundle operations put the map into a split constant-rank form. Its kernel and image are locally direct summands. In particular all relevant kernel formations commute with taking fibers.

One has F1⊂F2. Twisted composition shows that N(F2)⊂F1⊗M and N(E)⊂F2⊗M. Therefore N induces maps

    F2/F1 → F1⊗M,
    E/F2 → (F2/F1)⊗M.

Both are isomorphisms of line bundles. To verify this, trivialize M at a geometric point. The fiber is a three-dimensional regular nilpotent operator. Its kernel flag has dimensions one and two; the operator induces nonzero maps on successive graded pieces. Thus the displayed line-bundle maps are nowhere zero, hence invertible locally. This argument also explicitly fixes the twist signs.

Writing L=F1, the filtration of the trivial rank-three bundle E has graded pieces

    L,   L⊗M,   L⊗M².

No splitting of the filtration is claimed or needed.

## 2. Chern-class contradiction when M has positive square

Let l=c1(L) and H=c1(M). By the Whitney product formula for the two short exact sequences in the filtration,

    c(E)=(1+l)(1+l+H)(1+l+2H).

Since E is trivial, its first two Chern classes vanish. Hence in the rational Chow ring of X,

    0=3l+3H,
    0=3l²+6lH+2H².

The first identity gives l=−H in CH¹(X)_Q, and substitution in the second gives

    H²=0 in CH²(X)_Q.

In particular its degree is zero. Consequently such a twisted regular-nilpotent map cannot exist when deg_X c1(M)²>0. Torsion in Pic(X) causes no difficulty because only rational Chern classes and the numerical degree are used.

## 3. No projective surface of regular nilpotents

Suppose S⊂P(sl(U)) is an integral projective surface, with every closed point represented by a regular nilpotent endomorphism. On projective space the tautological inclusion O(−1)→sl(U)⊗O yields the universal twisted endomorphism

    N:U⊗O_S → U⊗O_S(1).

The identity N³=0 holds on S: it holds at every closed point, so all local coefficients vanish on the reduced complex variety S. Equivalently it follows from twisted Cayley–Hamilton and the vanishing of the trace-square and determinant sections. At every point N has rank two and N² has rank one, by the elementary Jordan-type characterization of regular nilpotents in dimension three.

Choose a smooth projective resolution π:X→S. Pull back the universal map and put M=π*O_S(1). Its fiber ranks remain two and one, and its cube is zero. Section 2 therefore gives deg_X c1(M)²=0.

On the other hand, the projection formula and π_*[X]=[S] give

    deg_X c1(π*O_S(1))² = deg_S c1(O_S(1))² = deg(S)>0.

This is a contradiction. Although the pullback M need not be ample on the resolution, its self-intersection is strictly positive, which is exactly what the argument requires.

## 4. Application to K

Assume for contradiction q|K=0. Write h=det|K. First suppose h is nonzero. Its projective zero scheme in P(K)=P³ is a cubic hypersurface. Choose any irreducible component of its support and give it the reduced structure; denote it S. Then S is an integral projective surface of positive degree. This construction does not assume that the cubic is irreducible or reduced.

At every closed point [A] of S, the representative A is nonzero, traceless, satisfies tr(A²)=0, and has det(A)=0. Its characteristic polynomial is

    t³ − (tr(A²)/2)t − det(A) = t³.

Cayley–Hamilton gives A³=0. The rank-one exclusion and A≠0 force rank A=2. A nilpotent endomorphism in dimension three with rank two has a single Jordan block, so rank A²=1. Thus S consists entirely of regular nilpotents, contradicting Section 3.

The preceding unit proves a constant-rank-two P³ obstruction, but this argument does not need it: if h=0 identically, every point of P(K) is regular nilpotent by the same reasoning, and any projective plane S⊂P(K) contradicts Section 3 directly.

Therefore q|K is nonzero.

