# Independent structural review

The proposed proof is valid. In fact its length bounds can immediately be strengthened from 41 and 71 to **40 and 70**. No coefficients or instance computations are needed.

## 1. The degree-seven generator has no fixed curve

Let tau be a nonzero equivariant map D -> H^0(I_Z(7)). Its restriction to C is nonzero: a vanishing restriction would make every section divisible by delta and produce a map to H^0(I_Z(5))=0. Here division preserves vanishing on Z because Z is disjoint from C, so delta is a unit on Z.

View the restricted sections as binary forms of degree 14. Their common zero divisor is A5-invariant. Nontrivial orbit sizes on P^1 are 12, 20, 30, and 60, so a nonempty invariant effective divisor of degree at most 14 must have degree 12. Dividing by its binary equation gives an equivariant injection D -> Sym^2(W), which is impossible by dimension (or irreducibility). The equation can be chosen invariant: binary icosahedral relative characters are trivial; alternatively, the one-dimensional line of equations is invariant and this character is trivial. Thus tau restricts basepoint-freely to C.

Any fixed plane curve other than C meets C and would give a common zero there. C itself is excluded by the nonzero restriction. Hence tau has no fixed divisor.

## 2. Classification of fixed divisors in degree nine

By hypothesis, every nonzero degree-nine restriction in the relevant D-isotypic pencil is basepoint-free on C. Therefore a symbol with nonzero restriction has no fixed curve, by the preceding intersection argument.

The restriction kernel is precisely the line spanned by delta*tau. Since tau has no fixed divisor, every nonzero symbol on this line has gcd exactly delta, up to a nonzero scalar. This includes the assertion that the multiplicity of delta in the gcd is exactly one.

For either primitive system (degree d=7 or d=9), its base scheme B is finite, contains Z scheme-theoretically, and is disjoint from C. The five sections remain linearly independent because a nonzero map from irreducible D is injective.

## 3. Kernel bundle

The evaluation map gives an exact sequence

0 -> E -> D tensor O_P2 -> I_B(d) -> 0.

The sheaf E is locally free of rank four. At a base point, an ideal of finite colength in a regular local ring of dimension two has projective dimension one; hence the kernel of a surjection from a free module is free. Away from B the assertion is immediate.

Writing b=length(B), the Chern classes are

c1(E)=-d H,   c2(E)=(d^2-b) H^2.

## 4. Liaison bound, including a strict improvement

Choose general independent f,g from the five-dimensional primitive system. They have no common curve: after choosing a nonzero f, avoid the proper linear subspace of sections vanishing along each of its finitely many irreducible components. Their intersection T is a complete intersection of type (d,d), of length d^2, and contains B. Define the residual scheme R by I_R=(I_T:I_B). Zero-dimensional schemes on the smooth surface are locally Cohen–Macaulay, so ordinary complete-intersection linkage applies, with

length(R)=d^2-b.

The plane-point liaison identity is

h^0(I_B(d)) = 2 + h^1(I_R(d-3)).

One way to obtain it is the residual exact sequence

0 -> I_T(d) -> I_B(d) -> omega_R(3-d) -> 0.

Here h^0(I_T(d))=2. Under finite-scheme duality and Serre duality, the connecting map is dual to the restriction H^0(O_P2(d-3)) -> H^0(O_R(d-3)); its kernel therefore has dimension h^1(I_R(d-3)). In particular the identity does not assume reducedness or saturation properties beyond the scheme-theoretic ideals already specified.

Put n=length(R) and t=d-3. Since h^0(I_B(d))>=5, one has

n-h_R(t)=h^1(I_R(t))>=3.

For any nonempty finite plane scheme, h_R(t)>=min(n,t+1). To see this, choose a line avoiding its support, so its defining linear form is a nonzerodivisor on the homogeneous coordinate ring. The first differences of h_R are the Hilbert function of a standard graded Artinian quotient of a polynomial ring in two variables. This sequence starts at 1 and cannot have an internal zero. Thus the Hilbert function grows by at least one until it reaches n.

Consequently n>=d+1, which proves the originally claimed b<=d^2-d-1.

But equality is impossible. If n=d+1, the preceding inequalities force h_R(t)=t+1<n. Since t>=1 here, the Artinian first differences from degrees zero through t must all equal one. In particular h_R(1)=2, so R is scheme-theoretically contained in a line L. Because n=d+1>d, the restriction to L of either degree-d form f or g must be zero: a nonzero section of O_L(d) has zero scheme of length exactly d and cannot vanish on R. Thus L divides both f and g, a contradiction.

It follows that

length(B) <= d^2-d-2,

hence length(B)<=40 for d=7 and length(B)<=70 for d=9. Equivalently c2(E)>=d+2 (9 and 11, respectively).

These are clean valid improvements, not a claim of optimality. The given inclusion Z subset B also supplies length(B)>=24.

## Final artifact verification

I independently read the complete final `PROOF.md`, including its strict bound and all downstream numerical substitutions. It is mathematically sound conditional on its explicitly pinned structural inputs. In particular the noncollinear Hilbert-function argument used there is valid for nonreduced schemes: its Artinian first differences begin 1,2 and stay positive until their final nonzero degree, giving h_R(t)>=min(length(R),t+2) for t>=1.

Reviewed file: `PROOF.md`

SHA-256: `657affc9ba8cf78d3d5e5b4a6bcc33a06cc833444b3f9f7d9434d330f5119e3d`

Verdict: **PASS, conditional on the stated pinned inputs.** No correction required. This is an independent mathematical review, not proof-assistant certification and not a reconstruction of the pinned source interfaces or any actual HM coefficient computation.
