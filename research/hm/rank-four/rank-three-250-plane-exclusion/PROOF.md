# The 250-point orbit has residual rank at least four

## Statement and dependencies

Under the representation and repeated-input-injectivity hypotheses of `../rank-two-250-plane-exclusion/PROOF.md`, every point of the normalizer orbit of size 250 has rank b at least eight, hence residual rank Q at least four.

We use from that proof: the normalized binary-icosahedral action V=T⊕W; the ten-point orbit O⊂P(T); the absence of any plane cubic through O; and the universal lower bound four for the even block. We use the character identities in `../canonical-line-parity-exclusion/PROOF.md`. No evaluation of the actual source operation is made. This proof is conditional on the correctness of those stated inputs; it does not replace their independent audits.

Write T'=Sym²W, and P4,P5 for the irreducible A5 modules of dimensions four and five. The modules T and T' are the two inequivalent three-dimensional irreducibles. In particular

    Sym²T=1⊕P5,    T'⊗T=P4⊕P5.

The invariant quadratic form on T is denoted q. Use it to identify T with its dual and P5 with symmetric traceless endomorphisms of T.

## 1. The odd block has rank at least three on O

For completeness, this follows from Section 3 of the preceding plane proof without any upper bound on the total rank. If the odd block had rank at most two at one point of O, equivariance would make all its three-minors vanish on O. They are cubics, hence identically zero. Repeated-input injectivity gives rank at least two everywhere on P(T), so its image bundle I has constant rank two. The repeated-input map O(-2)⊗W→I is a fiberwise isomorphism, whereas the linear block gives a surjection O(-1)^6→I. This contradicts Hom(O(-1),O(-2))=0. Thus the odd rank on O is at least three.

## 2. What even rank four would force

Suppose the even block has rank four at p∈O. It then has rank four at every point of O.

The universal outer-symmetric cyclic-zero module on T is

    S_(2,1)T=sl(T)=T⊕P5.

As proved previously, the P5 constituent survives injectively under f. Let H⊂J+ be its specific five-dimensional image. The universal map is

    f0(a,b,d)=a⊗(b×d)+d⊗(b×a).

For fixed u, its projection onto P5 is, up to nonzero scalar, S↦[C_u,S], where C_u(x)=u×x and S is a symmetric tensor. It has rank four for every nonzero u.

The T constituent cannot also survive. Indeed apply b_u to the invariant metric tensor ∑e_i² in orthonormal coordinates. Its universal value is

    2∑e_i⊗(u×e_i),

a nonzero skew-symmetric matrix for every u≠0. Its P5 projection is zero. If T survives, its image is disjoint from H by inequivalence of the irreducibles; the metric value therefore supplies a nonzero vector in the kernel of projection to H, while that projection already has rank four. Rank-nullity supplies a fifth image dimension, contradicting rank four at p. Consequently f|T³ has image precisely H and no T constituent.

The even block's remaining source is Sym²W=T'. Its coefficient map is the equivariant linear map

    g:T'⊗T→J+,    g(w²,u)=f(w,u,w),

extended by polarization. At every u representing a point of O, the pure-T source already has four-dimensional image inside H. Since the entire even block has rank four there, g(T',u) lies in that pure-T image, and in particular in H.

Project to J+/H. For each s∈T', the linear map u↦g(s,u) mod H vanishes on the representatives of O. Those representatives span T by irreducibility, so this map is identically zero. Hence the entire mixed coefficient image lies in the one specific copy H of P5. This argument removes every other irreducible component and every additional copy of P5 without any assumption on target multiplicities.

Moreover g is nonzero: if it were zero, cyclic zero and outer symmetry would give

    2f(w,w,t)=-f(w,t,w)=0

for all w∈W and t∈T, contradicting repeated-input injectivity for nonzero w,t. Thus, after identifying H with P5, g is the nonzero (unique up to scalar) equivariant map T'⊗T→P5.

## 3. Its cubic annihilator cannot vanish identically

For u≠0 put

    K(u)=u⊗u-(q(u)/3)Id ∈ P5.

The trace pairing on P5 is nondegenerate. Since C_u commutes with K(u), the image of S↦[C_u,S] is orthogonal to K(u). Therefore, at each point u∈O, the containment proved above implies

    F_s(u):=tr(g(s,u)K(u))=0             for all s∈T'.

Each F_s is a homogeneous cubic on T. The no-cubic lemma forces every F_s to vanish identically. We now prove that this is impossible for nonzero g.

The invariant nondegenerate pairings identify the coefficient tensor of g with an equivariant map

    a:T'→P5⊗T.

It is nonzero, hence injective. Identify P5 with the traceless quadratic forms on T. Since g(s,u) is traceless, F_s(u)=tr(g(s,u)(u⊗u)). Thus the map s↦F_s is exactly the composition

    T' --a--> P5⊗T --m--> Sym³T,

under the invariant identifications, where m is multiplication of a traceless quadratic by a linear form.

The multiplication map m is surjective. In orthonormal coordinates x1,x2,x3, all off-diagonal quadratics xi xj are traceless, so their linear multiples give every cubic monomial involving two or more distinct variables. The remaining monomial xi³ is the sum

    (xi²-xj²)xi + (xi xj)xj,       j≠i,

also in the image. Hence every cubic is in the image.

The character identities are

    P5⊗T = T⊕T'⊕P4⊕P5,
    Sym³T = T⊕T'⊕P4.

They follow directly from the A5 character table already recorded in the canonical-line proof: the respective character vectors are (15,-1,0,0,0) and (10,-2,1,0,0), on classes of sizes 1,15,20,12,12. Since m is equivariant and surjective, its kernel is P5. This kernel cannot contain the image of the nonzero map a from the inequivalent irreducible T'. Therefore m∘a is nonzero, contradicting the identically vanishing cubics F_s.

## 4. Conclusion and scope

The even block has rank at least five at every point of O; the odd block has rank at least three there. Their target parity spaces are complementary, so rank b≥8 and rank Q≥4 on O. Normalizer equivariance propagates the bound to the entire 250-point orbit.

Thus that orbit is disjoint from Z3. This does not exclude other isolated Z3 points and does not by itself classify the remaining finite rank-three locus. Only universal tensor identities, small finite-group characters, and bundle geometry were used.
