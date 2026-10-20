# Integral quadric polar rank-drop surfaces: exact classification and exclusion

Work over C. Let dim E=4, let W be a three-dimensional space of symmetric bilinear forms, and set K=W-perp in Sym²E. Write M(a)b=(B_i(a,b)) for a basis of W. Assume M has generic rank three and W has no common radical. If the rank-drop locus D={rank M≤2} contains an integral quadric surface, then, after changing coordinates,

    E=P⊕Q, dim P=dim Q=2,
    W=span{p1 q1−p2 q2, p1 q2, p2 q1}.

Here harmless scalar conventions identify quadratic forms with their symmetric bilinear forms. In particular D is exactly the smooth quadric p1 q1+p2 q2=0, and M has rank two everywhere on D.

For every square-avoiding linear v:K→E, the compatible rank-two tensor locus has dimension at most two. Square avoidance means v(e²) is not in Ce whenever 0≠e² belongs to K.

## 1. The linear kernel vector

The four signed maximal minors of M form a nonzero cubic vector c with M(a)c(a)=0. An irreducible quadratic equation f of a surface in D divides all four entries. Let g be their homogeneous gcd. If deg g=3, c=g c0 with constant nonzero vector c0, and M(a)c0=0 identically. Symmetry makes c0 a common radical vector, contrary to hypothesis. Thus deg g=2 and c=g T a for a linear map T. Its entries have no common polynomial factor. In particular rank T≥2.

The identity M(a)Ta=0 says, for every B in W,

    B(a,Ta)=0, equivalently T^t B+B T=0.

Let I_T denote the vector space of symmetric forms satisfying this equation. Thus W⊂I_T and dim I_T≥3. Since deg g=2 and f divides it, g is a scalar multiple of the irreducible quadric f.

## 2. Classification of T sufficient for the integral-quadric hypothesis

The standard generalized-eigenspace decomposition gives a direct elementary calculation of I_T. A form in I_T pairs generalized eigenspaces with eigenvalues α and β only when α+β=0. On such a pair its nilpotent parts satisfy the corresponding intertwining equation. We give all cases needed here, including singular and nonsemisimple T.

### Rank three

The rank-three symmetrizer lemma in /research/hm/middle-surface/symmetrizer-prerequisite/rank_three_symmetrizer_kernel.md gives dim I_T≤3, with equality only for a semisimple map with eigenvalues (0,λ,λ,−λ), λ≠0. Hence W=I_T. In coordinates (z,u1,u2,w),

    W=span{z²,u1w,u2w}.

The maximal-minor vector has gcd zw. This contradicts irreducibility of g.

### Rank two: nonnilpotent cases

If the nonzero generalized eigenspaces have total dimension one, the remaining zero Jordan type must be J2⊕J1. All invariant forms annihilate the nonzero eigenspace, giving a common radical. Explicitly the invariant forms on J2⊕J1 are binary quadrics in the terminal J2 coordinate and the J1 coordinate, so generic polar rank is at most two as well. If their total dimension two, the zero generalized eigenspace is a semisimple two-plane U, because the nonzero part already contributes rank two. Unless the two nonzero eigenvalues are λ and −λ, the whole nonzero part is in the common radical. This includes an invertible nonsemisimple 2×2 Jordan block: its eigenvalue λ is nonzero, so the scalar 2λ plus the nilpotent action on its symmetric square is invertible, and I_T=Sym²U*, of generic polar rank at most two. The only remaining case is therefore

    T=0_U⊕λ⊕(−λ),
    I_T=Sym²U* ⊕ C(yz).

The net W must map nontrivially to the last summand, or it has a common radical. It consequently has a basis h1,h2,yz+h0, where h0,h1,h2 are binary quadrics on U. The signed-minor vector is, up to a nonzero constant and signs,

    Δ(u) (0,0,y,−z),

where Δ is the determinant of the two binary polar rows dh1,dh2 (constant factors in differentials do not matter). Generic rank three forces Δ≠0. Its degree is two and it is binary, so it factors over C. Again g is not irreducible.

### Rank two: nilpotent cases

There are exactly two Jordan types, J3⊕J1 and J2⊕J2. Solving T^tB+BT=0 gives respectively

    I_T=span{x1²−2x0x2, x2²,x2x3,x3²},
    I_T=span{−x0x3+x1x2, x1²,x1x3,x3²}.

These formulas can also be checked by applying the derivations x1∂x0+x2∂x1 and x1∂x0+x3∂x2 to the displayed quadrics; solving coefficientwise shows exhaustiveness. In each case write I_T=Cq0⊕Sym²U*, where U* is spanned by (x2,x3) or (x1,x3). Generic rank three requires W to project nontrivially onto Cq0. Thus W has a basis q0+h0,h1,h2 with binary hi. Cofactor expansion along the two columns on which h1,h2 vanish gives

    c(a)=constant · Δ(a) Ta,

where Δ is again the binary determinant of the two polar rows of h1,h2. It is nonzero by generic rank three and reducible over C. No nilpotent case survives.

These exhaust rank two: a nonzero eigenvalue together with a nontrivial zero Jordan block is the already excluded case of a one-dimensional nonzero generalized eigenspace.

### Rank four

For invertible T, only pairs of opposite eigenvalues contribute to I_T. The dimension is bounded by the sum of the products of opposite multiplicities. To reach dimension at least three in dimension four, there must be one opposite pair with multiplicities either (3,1) or (2,2). In the (3,1) case the kernel dimension equals the kernel dimension of the nilpotent part on the three-space, so dimension at least three forces semisimplicity. In the (2,2) case any nonzero nilpotent part reduces the four-dimensional cross-pair kernel to dimension at most two: a single J2 contributes rank two; two J2 blocks have a two-dimensional kernel for N⊗I+I⊗N. Thus this case is also semisimple.

For multiplicities (3,1), W=I_T is the complete cross space span{u1w,u2w,u3w}. The cofactor gcd is w², a double plane, so this is excluded.

The sole remaining possibility is the balanced involution, after rescaling:

    T=I_P⊕(−I_Q), dim P=dim Q=2,
    I_T=P*Q*.

The three-space W is a hyperplane in this four-dimensional cross space. Its annihilator there is a nonzero tensor C∈P Q, and

    K=Sym²P ⊕ Sym²Q ⊕ CC.

Changes of bases in P,Q reduce C to matrix rank one or two. For rank one, take C with only its (1,1) entry nonzero; then W is spanned by p1q2,p2q1,p2q2 and the cofactor gcd is p2q2. This is reducible. Thus C has rank two, and can be taken to be the identity. This gives exactly the asserted normal form of W.

## 3. Explicit polar geometry in the surviving form

For W=span{p1q1−p2q2,p1q2,p2q1}, omit a common nonzero normalization factor and write

    M(p,q) = [ q1 −q2  p1 −p2
               q2   0   0   p1
                0  q1  p2    0 ].

Its signed maximal-minor vector is

    (p1q1+p2q2)(p1,p2,−q1,−q2).

Thus D is exactly the smooth quadric p1q1+p2q2=0. Moreover rank M is at least two at every projective point. For example, if p1≠0 the last two coordinates of the first two rows are independent; if p2≠0 use the first and third rows. If p=0 and q≠0, the analogous first-two-coordinate check works. Hence rank M=2 everywhere on D.

In particular, at every [e]∈P(P), ker M(e)=P, and similarly at every point of P(Q) its kernel is Q. The full partner incidence over D is therefore a projective-line bundle over D, irreducible of dimension three.

## 4. Excluding a threefold lying over D

Suppose an integral ordered compatible threefold Z has a surface as its first factor image A. Its general fiber has dimension one, so A⊂D. Since D is integral, A=D. Every fiber of the full partner incidence over D is P(ker M(a))≅P¹. Consequently Z equals this full irreducible three-dimensional incidence: it is a closed subvariety of it of the same dimension. Equivalently, the generic fiber is the entire line and taking closure gives equality.

It follows that the compatibility polynomial identity holds on P(P)×P(P), since this entire product lies in that incidence. For independent e,b in P, compatibility gives v(eb)∈P. Such products span Sym²P, so

    v(Sym²P)⊂P.

The homogeneous binary cubic e↦e∧v(e²) takes values in the one-dimensional space Λ²P. It has a nonzero projective zero over C, whether it is the zero polynomial or a nonzero cubic. At such e, e²∈Sym²P⊂K and v(e²)∈Ce. This contradicts square avoidance.

This argument treats the full threefold over the quadric rank-drop surface, not just the ambient graph of T.

## 5. Excluding all other threefolds

The universal finite-compatible-partner-plane lemma in /research/hm/universal-polar/rank-three-compatible-fiber-structure/PROOF.md, Sections 1–2, excludes a point or curve as the factor image of any compatible threefold.

If its first image is P(E), the generic partner is uniquely [Ta], so dense compatibility holds on the graph of T and extends as a polynomial identity over all E. Choose nonzero e∈P and differentiate

    v(aTa)∧a∧Ta=0

at a=e in each direction q∈Q. Since Te=e and Tq=−q, this yields

    v(e²)∧e∧q=0 for every q∈Q.

Two independent q directions force v(e²)∈Ce, again a forbidden square. A surface image was excluded in Section 4. Thus no ordered compatible threefold exists. Any component of larger dimension contains an integral threefold; multiplication of independent ordered factors is finite, so the projective compatible rank-two tensor locus has dimension at most two as asserted.

## Scope and audit

This proves the entire no-common-radical, generic-polar-rank-three branch in which D contains an integral quadric surface. It does not classify nets with only planar rank-drop surface components, or with no rank-drop surfaces and all base points degenerate. The proof uses only small symbolic identities, Jordan decomposition, and projective dimension arguments.
