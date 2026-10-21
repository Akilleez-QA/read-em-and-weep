# The pure standard Cauchy channel: classification and degree restrictions

## Universal linear-algebra theorem

Let T be a vector space and W a two-dimensional vector space over C. Suppose K is a three-dimensional subspace of T tensor W and its decomposable Plucker vector has zero projection to

    Lambda^3(T) tensor Sym^3(W)

in the Cauchy decomposition of Lambda^3(T tensor W). Then at least one of the following holds:

(A) The T-support of K has dimension two. Thus K is a hyperplane in E tensor W for a unique two-dimensional subspace E of T.

(B) K contains L tensor W for a unique line L in T, and its T-support has dimension at most three.

Conversely, each of these conditions makes the stated Cauchy projection zero. The alternatives need not be disjoint.

## Proof without selected values

Choose a basis of W, and write the inclusion K -> T tensor W as a pair of maps A,B:K -> T. Their joint map is injective. The Cauchy projection in the statement records the cubic polynomial Lambda^3(A+sB). Its vanishing is therefore equivalent to rank(A+sB)<=2 over C(s), or equivalently for every pencil parameter.

The generic rank is exactly two. To see why it cannot be one, write two nonzero rank-one maps as A=t tensor alpha and B=u tensor gamma. If every linear combination has rank at most one, either t,u are dependent or alpha,gamma are dependent. In the first case the joint image has dimension at most two and cannot receive K injectively; in the second case the joint kernel is nonzero. The cases with one zero map are even more immediate.

Take two rows of the pencil that are independent over C(s). Their cross product produces a nonzero polynomial kernel vector of degree at most two. Divide its components by their gcd, obtaining a primitive vector of least possible degree d. There is no constant kernel vector, by joint injectivity, so d is one or two.

If d=1, write the vector as u+s v. The coefficients u,v are independent, and

    Au=0,  Av=-Bu=t,  Bv=0.

The vector t is nonzero by joint injectivity. Thus the images of u,v span t tensor W. A third basis vector z contributes only Az and Bz to the T-support. This proves (B).

If d=2, write the vector as u+s v+s^2 z. These three coefficients are independent. Indeed, if their span had dimension two, the pencil restricted to that span would have generic rank at most one. A nonzero row of this restricted two-column pencil yields a polynomial kernel vector of degree at most one, contradicting minimality; a one-dimensional span would yield a constant kernel. The coefficient equations now read

    Au=0,  Av=-Bu=t,  Az=-Bv=t',  Bz=0.

All images lie in span(t,t'), so the T-support has dimension at most two. It cannot have dimension one, because K has dimension three and W dimension two. This proves (A).

In (A), every projection K -> T lands in E. In (B), every projection maps L tensor W into L, and the remaining one-dimensional quotient of K contributes at most one further image direction. Both therefore have projection rank at most two, proving the converse. Uniqueness of E follows from its definition as support. Two distinct full fibers L tensor W would have direct sum of dimension four, proving uniqueness of L.

## Application to the actual rank-seven kernel

Use the established actual beta map

    M2* tensor O_X -> sl(W')* tensor Omega_X^1(2),

where X=P(A0), A0=V3, M2*=V* tensor W', and dim V=5. If its generic rank is seven and its determinant covariant is the pure U' channel, its saturated kernel K has rank three, det K=O_X(-4), and its generic Plucker vector lies in S21(V*) tensor W'. The universal theorem applies over the function field of X.

## Stability forces full support for every actual rank-seven kernel

The already proved stability theorem gives that K is slope-stable of slope -4/3. Let E_s be the saturation of the image of contraction

    K tensor W'^* -> V* tensor O_X,

and let s be its rank. It is intrinsically N-invariant. Write det E_s=O_X(-a). The determinant inclusion implies a>=0. As an ordinary sheaf, K tensor W'^* is a direct sum of two copies of K, hence slope-semistable of slope -4/3. Its torsion-free image has slope at least -4/3, by the quotient characterization of semistability. Saturation can only increase first Chern degree. Consequently

    0 <= a <= floor(4s/3).

Central weight comparison gives a=3s modulo 5: the determinant of a rank-s subsheaf of V* has weight 4s, while O_X(-a) has weight 3a. Perfectness of N rules out a character adjustment.

These constraints exclude every s<5:

- s=1: a<=1, incompatible with a=3 modulo 5.
- s=2: the only possibility is a=1. But Lambda^2(V*)=V3 tensor W, and pairing with H0(O(1))=V1 leaves H-invariant multiplicity W, with no N/H-invariant vector. Hence the required equivariant determinant inclusion does not exist.
- s=3: the only possibility is a=4. Here Lambda^3(V*)=V1 tensor W, and Sym^4(A0*)=V3 tensor (J4_even direct-sum J4_odd direct-sum U direct-sum U'). None of the listed multiplicities is W, so the required equivariant determinant inclusion again does not exist.
- s=4: the only possibility is a=2. Here Lambda^4(V*)=V and Sym^2(A0*)=V2 tensor U. Their H-invariant multiplicity is U, with no N/H-invariant vector. This determinant inclusion is also impossible.

Thus s=5. Since E_s is saturated in V* tensor O_X and has the same rank, it is all of V* tensor O_X. Every hypothetical actual rank-seven kernel therefore has full V*-support.

This argument applies to the actual kernel regardless of its determinant-channel ratio. It uses its proved stability, rather than assuming that a freely chosen rank-three subspace or covariant is stable.

## Exclusion of the pure U' candidate

The universal pencil theorem says that a decomposable three-plane in the pure standard Cauchy channel has T-support of dimension at most three. Applied to the generic fiber of an actual kernel whose determinant lies in the pure U' channel, it contradicts the full-support result just proved. Therefore the pure U' candidate cannot be the determinant of the actual rank-seven kernel.

In the exact contraction criterion, this says D_beta(sigma_U') is nonzero. It does not exclude sigma_U' from the abstract Plucker candidate set: a decomposable covariant unrelated to the actual kernel need not define a stable sheaf.

Together with the earlier pure U-channel exclusion in TWO-CHANNEL-CRITERION.md, any surviving actual rank-seven determinant ratio must have both channel coefficients nonzero. This does not prove that a mixed candidate exists, that either of the at-most-two Plucker candidates is annihilated by beta, or that the generic evaluation rank is ten.

## The remaining full-support contraction has a fixed surface-cycle degree

There is a further necessary consequence if the actual rank-seven case occurs. Write J for the unsaturated image of the now generically surjective contraction K tensor W'^* -> V* tensor O_X, and write det J=O_X(-d). As a quotient of the semistable sheaf K direct-sum K, J has slope at least -4/3. Its inclusion in the trivial bundle also implies d>=0. Thus 0<=d<=6.

The determinant inclusion O_X(-d) -> det(V*) tensor O_X is an equivariant nonzero section of O_X(d). Since N is perfect, det(V*) is trivial as a character. Central weights force d=0 modulo 5, leaving d=0 or 5. The degree-five possibility is excluded by the absence of N-invariant quintics, as proved from HM Theorem 3.5 in PRIMARY-BAD-CODIMENSION-THREE.md. Hence d=0, and the quotient

    T_def = (V* tensor O_X)/J

is supported in codimension at least two: the determinant has no divisorial zeros.

The kernel of contraction has rank one and is reflexive. Indeed it is the kernel of a map from the reflexive sheaf K direct-sum K to the torsion-free sheaf J; the depth lemma gives the S2 condition, and torsion-freeness is automatic. On smooth projective space a rank-one reflexive sheaf is a line bundle. Determinants now identify this kernel as O_X(-8). Thus there is an exact sequence

    0 -> O_X(-8) -> K tensor W'^* -> J -> 0.

Since c1(J)=0, its second Chern class is

    c2(J)=c2(K direct-sum K)=2c2(K)+16.

The established Chern restriction c2(K) in {7,12} therefore yields c2(J) in {30,40}. Additivity of the Chern character in 0 -> J -> 5O_X -> T_def -> 0 identifies the codimension-two cycle of T_def with c2(J). Consequently its degree is either 30 or 40.

This is a necessary effective codimension-two defect cycle of the hypothetical rank-seven case. It does not assert that T_def is pure, reduced, or classified; components of higher codimension are allowed. In particular the positive cycle degree proves that this contraction cannot be surjective as a sheaf everywhere, even though it is generically surjective.

## Scope and dependencies

The full-support theorem is new structural information about any hypothetical actual rank-seven kernel. Its essential additional premise is the established stability of that kernel in RANK-SEVEN-STABILITY.md. The pure-standard exclusion combines this premise with the universal pencil classification, not with a selected rank or covariant evaluation.

The representation inputs are the primary HM identities already pinned in EVALUATION-RANK-EXCLUSIONS.md and TWO-CHANNEL-CRITERION.md: the exterior powers of V*, the Galois-conjugated quadratic and quartic identities, and the nonisomorphism of the displayed irreducible multiplicities. No selected pencil, HM coordinates, covariant values, minors, or ranks are evaluated. No conclusion about full Q4 or the original selected quadratic follows here.
