# Rank-one boundary support curves: irreducible quadrics and pencils

Work over C. This note uses only abstract linear algebra and projective geometry. 

## Statement

Let E have dimension four, let 0≠Q∈Sym²E* be a scalar quadratic functional, and put K=ker(Q:Sym²E→C), of dimension nine. Let v:K→E be linear and suppose there is **no compatible square**:

    e≠0, e²∈K  ⇒  v(e²)∉Ce.

Consider a complete integral curve T with a nonconstant morphism

    a:T→P(E*),    t↦[a_t],    A_t=ker a_t.

Suppose for every t there exists a five-dimensional subspace K_t satisfying

    K_t⊂K∩Sym²A_t,       v(K_t)⊂A_t.                 (1)

Then:

1. If rank(Q)≥3, such a curve does not exist.
2. For any nonzero Q, such a curve cannot have image a projective line in P(E*).

The first conclusion also holds whenever Q|A_t is nonzero at every t, regardless of rank(Q). No exclusion of every nonlinear curve for rank(Q)≤2 is asserted.

In the full-flag boundary setting, the closed limiting-kernel and correction incidences already proved in `/research/hm/middle-surface/flag-boundary-resolution/PROOF.md`, Sections 4A–4B, supply exactly (1). One need not choose K_t regularly. At a rank-one residual point Q denotes a chosen scalar representative of its one-dimensional residual image; rank(Q) in this note means the rank of that scalar quadratic form, **not** residual rank.

## 1. Normalization and the universal bundles

Replace T by its normalization. It remains a connected integral projective curve over C, the support map remains nonconstant, and (1) remains valid pointwise. Write L=a*O(1). The universal covector is a nowhere-zero bundle quotient

    a:E⊗O_T→L,

with rank-three kernel bundle A. Equivalently a is a section of E*⊗L. Choose once and for all an arbitrary linear extension V:Sym²E→E of v.

We identify a quadratic functional B on Sym²E with the polynomial e↦B(e²). Thus multiplication of covectors aℓ has polynomial value a(e)ℓ(e). Define the shear S_ℓ:Sym²E→E by

    S_ℓ(ef)=(ℓ(e)f+ℓ(f)e)/2.

Then S_ℓ(e²)=ℓ(e)e, and a∘S_ℓ corresponds exactly to the polynomial aℓ. The source convention q↦2q(d) agrees with S_ℓ when d=ℓ/2. These factors are important; this note uses S_ℓ(q)=q(ℓ).

## 2. Regularity of the proportionality scalar

Assume Q|A_t≠0 for every t. Set q=Q|Sym²A, a section of the rank-six bundle Sym²A*. It is nowhere zero, so it spans a line subbundle O_T·q with locally free quotient. This can be checked by choosing, near each point, a component of q which is a unit.

Each K∩Sym²A_t is five-dimensional, hence (1) forces

    K_t=ker(Q|Sym²A_t).

Consequently the restriction r=(a∘V)|Sym²A, a section of Sym²A*⊗L, vanishes on ker q fiberwise. It is therefore fiberwise proportional to q. Its image in the locally free quotient (Sym²A*/O_Tq)⊗L vanishes at all closed points and hence vanishes as a section, since T is reduced. There is a unique regular section

    λ∈H⁰(T,L),       r=λq.                           (2)

Explicitly, wherever the i-th component q_i is a unit, λ=r_i/q_i in a local frame of L. Fiberwise proportionality makes all these formulas agree. In particular λ is not merely a meromorphic section, and no pole-removal assumption is being made.

## 3. Bundle division by the universal covector

Multiplication by a gives an exact sequence of vector bundles

    0→E*⊗O_T --(ℓ↦aℓ)--> Sym²E*⊗L
      →Sym²A*⊗L→0.                                 (3)

For verification, trivialize L and choose a local frame of E⊗O_T whose first three vectors span A and whose fourth has a-value one. The kernel of restriction of quadratic polynomials to A consists uniquely of the four polynomials aℓ. This proves both exactness and local freeness. The construction is independent of the frame: multiplying the local representative of a by a transition unit multiplies the target representative by the same unit, leaving the quotient ℓ unchanged. This also explains why the left side is the trivial E* bundle, not E*⊗L or E*⊗L^{-1}.

By (2), the global section a∘V−λQ lies in the kernel in (3). It has a unique global preimage

    ℓ∈H⁰(T,E*⊗O_T)=E*,

where the last equality follows from projectivity and integrality of T. Therefore ℓ is a single constant covector and, as quadratic-polynomial bundle sections,

    a∘(V−S_ℓ)=λQ.                                  (4)

Restriction to the fixed vector space K gives a_t(v−S_ℓ)(K)=0 for every t. Hence

    (v−S_ℓ)(K)⊂W:=⋂_{t∈T} A_t.

Nonconstancy of a supplies two distinct hyperplanes, so dim W≤2.

## 4. A two-dimensional image forces a compatible square

The following elementary fact finishes the argument and is useful separately. Suppose a covector ℓ and a subspace W⊂E of dimension at most two satisfy

    (v−S_ℓ)(K)⊂W.

Extend v−S_ℓ linearly from K to a map F:Sym²E→W. Choose coordinates on W and let F₁,F₂ be the resulting homogeneous quadratic polynomials on E, padding with zero polynomials if necessary. The homogeneous ideal

    (Q,F₁,F₂)⊂C[E]

has height at most three. Its projective zero locus in P(E)=P³ is nonempty: otherwise its affine zero locus would be only the origin, its radical would be the homogeneous maximal ideal of height four, contradicting the height bound. Thus some e≠0 satisfies Q(e²)=F₁(e)=F₂(e)=0. It follows that

    e²∈K,       v(e²)=S_ℓ(e²)=ℓ(e)e,

contradicting square avoidance. This argument needs no smoothness or irreducibility of the quadric and does not assume the two quadratic equations meet properly.

Finally, if rank(Q)≥3, Q cannot be divisible by a linear form: a product of two linear forms has quadratic-form rank at most two. If Q vanished identically on A_t, its polynomial would be divisible by a_t. Thus Q|A_t is nonzero everywhere, and Sections 2–4 prove conclusion 1.

## 5. A separate exclusion for every pencil, including degenerate Q

Suppose the support image is a projective line. Its completeness and nonconstancy imply that it is the entire line. Choose independent covectors x,y spanning this line, and set W=ker x∩ker y, of dimension two. The condition Q|ker(x+ty)≠0 fails for at most two parameters, since failure means the corresponding linear form divides Q. At every other parameter,

    K_t=K∩Sym²ker(x+ty).                              (5)

### Case 1: Q|W=0

Then Sym²W⊂K, and (5) implies Sym²W⊂K_t for every nonexceptional parameter. Therefore v(Sym²W) is contained in the intersection of those infinitely many distinct hyperplanes, which is W. The expression

    e↦e∧v(e²),       e∈W,

is a homogeneous binary cubic with values in the one-dimensional space det W. It either vanishes identically or has a zero in P(W) over C. Either possibility gives a compatible square. Thus this case is impossible.

### Case 2: Q|W≠0

In this case no member of the pencil divides Q. Put P=x∘V and R=y∘V, homogeneous quadratic polynomials on E. Over the generic parameter field C(t), equation (5) and proportionality give

    P+tR=λ(t)Q+(x+ty)ℓ_t,

with λ(t)∈C(t) and ℓ_t∈E*⊗C(t). Clear all parameter denominators: for a nonzero D(t)∈C[t] and a polynomial N(t),

    D(t)(P+tR)=N(t)Q+(x+ty)B(t),                    (6)

where B(t) is polynomial in t with coefficients linear in the E coordinates. In the localization at y, substitute t=−x/y. After clearing powers of y, (6) says that Q divides a nonzero homogeneous binary polynomial in x,y times

    xR−yP.

Every nonzero homogeneous binary polynomial splits into pencil linear forms over C. None divides Q, since Q|W≠0. Cancellation in the polynomial UFD therefore proves, with multiplicities even when Q is a square,

    xR−yP=Q·M                                      (7)

for a linear polynomial M (possibly zero).

Restrict (7) to W. Since Q|W≠0 and C[W] is a domain, M|W=0, so M=αx+βy for scalars α,β. Rearrangement yields

    x(R−αQ)=y(P+βQ).

Because x and y are relatively prime, there is one linear polynomial ℓ such that

    P+βQ=xℓ,       R−αQ=yℓ.

On K, both identities state that x and y annihilate v−S_ℓ. Hence (v−S_ℓ)(K)⊂W, and Section 4 again gives a compatible square. This proves conclusion 2.

## 6. Exact scope for the finite-boundary alternative

At residual rank one, an actual complete nonconstant curve of limiting supports can occur under square avoidance only if the scalar annihilator quadric has rank at most two, its support image is nonlinear, and that curve meets at least one hyperplane on which Q vanishes identically. These are necessary conditions, not an existence claim.

For rank(Q)≤2 the regularity argument in Section 2 cannot be applied across such exceptional hyperplanes: Q|A vanishes there, and λ and the divided covector can acquire poles. No unjustified extension across those points is used here. The pencil proof handles them separately, but it does not handle every nonlinear support curve.

Any refinement also excluding residual-rank-two support curves must be established independently before combining it with this note. This note alone does not establish the final finite-boundary classification or exclude a boundary curve in the middle surface. Residual rank zero is excluded separately below.

## 7. Universal exclusion of residual rank zero

Suppose instead that the residual map is zero. Then K=Sym²E, and a correction v:Sym²E→E with no compatible square would exist. Its diagonal polynomial e↦v(e²) gives a section of E⊗O_{P(E)}(2). The twisted Euler sequence is

    0→O_{P³}(1)→E⊗O_{P³}(2)→T_{P³}(1)→0.

Let s be the image section of T_{P³}(1). At [e] the first map has image the line Ce in the E factor (with the appropriate line-bundle twists), so

    s([e])=0  ⇔  v(e²)∈Ce.

Writing h=c₁(O(1)), the Euler sequence gives

    c(T_{P³}(1))=(1+2h)^4/(1+h),
    c₃(T_{P³}(1))=(32−24+8−1)h³=15h³≠0.

If s were nowhere zero, it would define a line subbundle O⊂T_{P³}(1) with rank-two locally free quotient, forcing c₃(T_{P³}(1))=0 by Whitney's formula. Therefore s has a zero, which is a compatible square. This contradiction proves that residual rank zero is universally impossible under square avoidance. No restriction on the support family, and no actual source rank evaluation, is involved.
