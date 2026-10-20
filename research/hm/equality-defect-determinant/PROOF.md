# Determinant obstruction at equality in the isolated-defect rank bound

## Theorem

Let R be a regular local complex ring of dimension four, with residue field C, and let a finite group H act on R preserving its maximal ideal. Let M be an H-equivariant reflexive module of rank r, locally free on the punctured spectrum, with an equivariant isomorphism M≅M*. Write

    P=Ext^1_R(M,R), Q=Ext^2_R(M,R), D(-)=Ext^4_R(-,R),
    T=P/mP, s=dim T, V=Tor_1^R(P,C).

Suppose P is nonzero and beta1(P)=r+2s. Then

    det(V) = det(M*)|_closed_point

as H-characters. Here det(M*) means its reflexive determinant line, and the right side is the character on its fiber. In particular, when r=2 and the determinant is equivariantly trivial, V must have trivial determinant, not merely be self-dual.

This is an equality-case refinement of the representation-imbalance bound. It requires no symmetric or alternating normalization of a chosen isomorphism M→M*. It is derived by constructing a free equivariant monad, rather than guessing the symmetry of the Tor comparison map.

## 1. Isolated local duality

For every reflexive N free on the punctured spectrum, one has pd(N)≤2 and finite-length Ext^1(N,R),Ext^2(N,R). Dimension shifting in a minimal free resolution and grade four of finite-length modules give

    Ext^1(N*,R) ≅ D(Ext^2(N,R)).

Applying this to N* and using N**=N and finite biduality also gives

    Ext^2(N*,R) ≅ D(Ext^1(N,R)).

All maps are equivariant. The functor D already includes the canonical-character factor; no additional determinant twist is inserted. The proof of the first identity is recorded explicitly in the representation-defect bound: split the dual resolution into its image/kernel sequences, use Ext^j(L,R)=0 for j<4 for finite-length L, and dimension shift. Thus P≅D(Q) by the stipulated self-duality of M.

## 2. Two universal extensions give a free middle term

Choose the equivariant minimal free cover A=R⊗T→P. Such a cover exists by lifting the finite-dimensional generator space equivariantly and applying Nakayama. Its kernel I lies in mA.

The chosen surjection A→P corresponds to an extension class in

    Ext^1_R(M,A*) ≅ A*⊗Ext^1_R(M,R).

Choose the corresponding equivariant extension

    0→A*→E→M→0.                                      (1)

An invariant extension class admits an equivariant representative because finite-group invariants are exact in characteristic zero. The connecting map A→Ext^1(M,R) is the chosen surjection. Consequently

    Ext^1(E,R)=0, Ext^2(E,R)≅Q.

The module E is reflexive: it is free on the punctured spectrum; its depth at the closed point is at least two by (1), it is torsion-free, and hence it satisfies S2 over the regular normal ring.

Dualizing (1) gives

    0→M*→E*→A→P→0,

or 0→M*→E*→I→0. Since I is the first syzygy of finite-length P, Ext^1(I,R)=Ext^2(I,R)=0. Therefore

    Ext^1(E*,R) ≅ Ext^1(M*,R) ≅ P.

The second isolated-duality identity gives Ext^2(E*,R)=D(Ext^1(E,R))=0.

Choose a second equivariant extension

    0→A*→F→E*→0                                     (2)

whose connecting map A→Ext^1(E*,R)≅P is a minimal surjection. Then Ext^1(F,R)=Ext^2(F,R)=0. As for E, the module F is reflexive, hence has projective dimension at most two. A nonzero last free term in a minimal resolution of positive length would produce nonzero Ext in that length, by Nakayama. Thus F is free. Its rank is

    rank F = rank E* + s = r+2s.

Composing F→E* with E*→A gives L:F→A. Its cokernel is P and its image is I. The complex

    A*→F→A

has zero left cohomology, middle cohomology M*, and right cohomology P. This construction does not assert that its middle differential is literally the transpose of the other differential under an alternating form.

## 3. Equality identifies the middle representation

Because A→P is minimal, the Tor sequence gives the equivariant identification

    I/mI ≅ Tor_1(P,C)=V.

The free cover F→I has rank r+2s. Under the assumed equality beta1(P)=r+2s, it is minimal; reduction modulo m is therefore an isomorphism

    F/mF ≅ V.

An equivariant free module over the local ring has an equivariant basis lifted from its fiber: average a lift of the fiber representation, then use Nakayama and equality of ranks. Consequently the determinant character of F is det(V).

On the punctured spectrum the complex is a monad of vector bundles with exact ends. Taking determinants of its two short exact sequences yields

    det(M*) ≅ det(F)⊗det(A*)^(-1)⊗det(A)^(-1)
             ≅ det(F).

The cancellation of det(A*) and det(A) is canonical and equivariant. Both sides extend as invertible reflexive lines across the codimension-four closed point, so the equality is equivariant there as well. Taking fibers proves the theorem.

## 4. Complete sign choice for the length-sixteen residual family

Use the candidate family over C[[x1,x2,x3,x4]], with lambda≠0,lambda^4≠1 and epsilon=±1. Its generator count is s=4 and its ten minimal relation representation is

    V=O2 ⊕ O3 ⊕ C_epsilon.

The four-dimensional summands O2 and O3 are dual, so their determinant characters cancel. On the clock pair, B has opposite weights and the chosen C4 generator has matrix

    [[0,epsilon],[1,0]].

Its determinant is -epsilon. The central character on the relation space is trivial in the candidate conventions. Therefore det(V)(g)=-epsilon.

If the epsilon=+1 member were Ext^1(M,R)=D Ext^2(M,R) for an equivariantly determinant-trivial isolated rank-two reflexive M, then beta1(P)=10=r+2s and the theorem would force det(V)=1. But det(V)(g)=-1. This is impossible.

Thus epsilon=+1 is excluded for ALL such isolated equivariant realizations, not only the previously tested constant-coefficient symplectic ansatz. The separately constructed epsilon=-1 symplectic monad realizes every allowed lambda. Together these establish exactly which sign of this residual family is realizable in the stipulated local category.

The statement fixes the H-action and determinant linearization. Twisting M by a character changes its determinant by the square of that character and changes the induced defect character; dropping equivariant determinant triviality changes the problem. No assertion is made about a global HM kernel, prescribed Chern classes, or full projective-normalizer equivariance.

## Sources and verification boundary

The isolated-duality and minimal-generator setup are the existing representation-defect theorem (published in PR174). The candidate relation representation and the epsilon=-1 realization are the separate length-sixteen construction and symplectic-realization proofs. The present determinant refinement and epsilon=+1 exclusion are newly derived here.

For comparison only, the double-universal-extension method is the local counterpart of the projective monad construction discussed by W. Decker, *Monads and cohomology modules of rank 2 vector bundles*, Compositio Mathematica76 (1990),7–17, introduction and Proposition1: https://www.numdam.org/item/CM_1990__76_1-2_7_0.pdf . The proof above establishes the local equivariant statement directly; it does not apply a projective theorem without checking its hypotheses.

No selected HM/source instance, matrix rank, jet or obstruction value is evaluated. No formal proof execution is claimed. Independent review is required before publication.
