# Nonvanishing of the trivial-character middle obstruction

Work over C, with the actual module H, its symmetric balanced trace pairing of degree five, the Heisenberg group Gamma and normalizer quotient G=SL2(F5). Write W=W', Q=Sym3(W), and retain T,E,A_rep,W0,U,U',T4,J5 from the pinned representation conventions. Parameter twists are on P(W). No selected parameter is evaluated.

## Pinned inputs

- [PR528, commit bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa](https://github.com/Akilleez-QA/read-em-and-weep/blob/bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa/research/hm/middle-family-parity/PROOF.md): the relative obstruction is symmetric, its trivial block is W0 O(-3) -> W0* O(3), and its nonzero alternative has simple determinant divisor Omega. The nontrivial characters contribute either zero or 24 generically.
- [PR518, commit b17c7cac111568f9b45876a2ad8fae4e46578841](https://github.com/Akilleez-QA/read-em-and-weep/blob/b17c7cac111568f9b45876a2ad8fae4e46578841/research/hm/middle-obstruction-symmetry/PROOF.md): chain-level lift formula q(v,v')=<d^{-1}v,v'> and its sign.
- [PR499, commit 1112189481554b0353c64178e3adc0dede2c3fbe](https://github.com/Akilleez-QA/read-em-and-weep/blob/1112189481554b0353c64178e3adc0dede2c3fbe/research/hm/middle-euler-ghost-exclusion/PROOF.md): K(H)_5 is acyclic.
- [PR490, commit 1c5ad353bb5f1808150f64cde3c29b92c6e13d91](https://github.com/Akilleez-QA/read-em-and-weep/blob/1c5ad353bb5f1808150f64cde3c29b92c6e13d91/research/hm/dual-tensor-bridge/VERIFICATION.md): H has no linear relations; its degree-two quadratic relation is E times the lower W summand in Sym2(W) tensor W. Thus H2=E tensor Q, and passage to a column is binary evaluation.
- [PR512, commit 26811b53c198879d0c55a2fb9ba75187bee38d9c](https://github.com/Akilleez-QA/read-em-and-weep/blob/26811b53c198879d0c55a2fb9ba75187bee38d9c/research/hm/column-family-intersections/PROOF.md), and PR528: the actual quotient C=H/M has C2=E O(3), and B=M-perp=D5(C).

Representation identities are from [Horrocks--Mumford (1973), Section 3.3 and appendix](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf), with the same actual linearizations as PR528:

Lambda3(T)=A_rep tensor W0, E=A_rep*, Sym2(E)=T* tensor U, Lambda2(E)=T* tensor W',
Sym2(Q)=U + T4 + U', Lambda2(Q)=1 + J5,
Sym2(W0)=U, Lambda2(W0)=1.

The last two identities also follow from binary Clebsch--Gordan: Sym2(Sym3 W)=Sym6 W + Sym2 W, Lambda2(Sym3 W)=Sym4 W + 1; Sym6 W=U+T4, Sym4 W=J5. All summands here are pairwise nonisomorphic where indicated. Q and W0 have nondegenerate invariant alternating forms.

## 1. A constant eight-dimensional inverse controls the block

Take Gamma invariants of the degree-five Koszul complex of H. Its vector-space dimensions, from left Koszul degree5 to right degree0, are

2 -> 2 -> 8 -> 8 -> 2 -> 2.

The first arrow is an isomorphism: it is the scalar identity in T tensor Lambda4(T), tensored with W, using H1=T tensor W and det(T)=1. The last arrow is an isomorphism by pairing duality. Exactness follows from acyclicity and exactness of invariants for a finite group in characteristic zero. Therefore the central differential is an isomorphism

d: X -> X*,  X=(H2 tensor Lambda3(T))^Gamma=Q tensor W0.

The identification of its target with X* is the perfect Koszul pairing. Formula (2) of PR518 shows that d is symmetric. Let D denote its symmetric bilinear form on X. Its inverse is a symmetric bilinear form D^{-1} on X*.

The quotient H2=E tensor Sym3(W) -> C2=E O(3) is ordinary cubic evaluation, since the lower binary summand is precisely the quadratic relation. Dualizing and taking Gamma invariants after exterior pairing identifies

(B3 tensor Lambda2(T))^Gamma -> (H3 tensor Lambda2(T))^Gamma=X* tensor O

with the cubic Veronese inclusion

W0* tensor O(-3) -> W0* tensor Q* tensor O.

There are no boundaries in this B term because B2=0. Its outgoing invariant differential is zero because the subsequent invariant differential of K(H)_5 is zero. Consequently it is exactly the trivial summand of Tor2(B)_5. The lift formula of PR518 now identifies Q_1 with the restriction of D^{-1} to this Veronese family of two-planes.

## 2. The restriction kernel among invariant forms

Invariant symmetric forms on X* form a two-dimensional space. Under the natural decomposition

Sym2(Q tensor W0) = (Sym2 Q tensor Sym2 W0) + (Lambda2 Q tensor Lambda2 W0),

each summand contributes exactly one invariant. The latter invariant is the product of the two alternating forms; call this line L_alt. It vanishes on every plane W0* tensor k lambda^3, since an alternating form vanishes on (lambda^3,lambda^3).

The first invariant does not vanish identically on this family. Restriction on the Q factor is the multiplication map Sym2(Sym3 W) -> Sym6 W. Its kernel is the U'=Sym2 W summand, whereas the invariant in Sym2 Q tensor Sym2 W0 uses the U summand. Multiplication is therefore nonzero on that invariant. Thus the kernel of restriction is exactly L_alt.

In particular, if Q_1 were identically zero, D^{-1} would be a nonzero product of alternating forms. Its inverse D would also be a product of alternating forms, since the inverse of a tensor product is the tensor product of the inverses. It would lie in the alternating-alternating summand of Sym2(X*).

## 3. Actual multiplication excludes that line

Consider the actual invariant trilinear form

m(t,h,k)=b_H(th,k),  t in T, h,k in H2.

Balance and symmetry imply m(t,h,k)=m(t,k,h). The decomposition H2=E tensor Q gives

Sym2(H2)=(Sym2 E tensor Sym2 Q) + (Lambda2 E tensor Lambda2 Q).

The second part cannot contribute an invariant pairing with T: Lambda2(E)=T* tensor W', whereas Lambda2(Q)=1+J5 contains no W'. Thus the actual trilinear form belongs entirely to the first part. In particular it is symmetric separately in the two Q arguments.

The Koszul form D is obtained from m by contraction in T and wedge pairing on Lambda3(T). These operations do not act on the Q factors. Hence D remains symmetric in its two Q arguments. Being a symmetric form on Q tensor W0, it belongs to Sym2(Q*) tensor Sym2(W0*), and has no component in Lambda2(Q*) tensor Lambda2(W0*).

But D is invertible, hence nonzero. It therefore cannot be the nonzero alternating-product form forced by Q_1=0 in Section2. This contradiction proves Q_1 is not identically zero.

## 4. Two-eigenvalue normal form

Choose nonzero invariant alternating forms on Q and W0 and let J:X -> X* be their tensor product. It is an invertible symmetric form. Define A=J^{-1}d, an equivariant endomorphism of X=U direct_sum J5. By multiplicity-free decomposition, A acts by scalars a on U and c on J5. Both are nonzero because d and J are invertible.

The trace of A is the contraction of the tensor d against J^{-1}. This contraction is zero: d is separately symmetric in its Q indices, while the corresponding factor of J^{-1} is alternating. Thus

3a+5c=0.

Consequently there is a nonzero scalar t such that A acts by 5t on U and by -3t on J5. Equivalently,

d=J composed with t(5 Id_U direct_sum -3 Id_J5).

This is a relative normalization after the choice of the two alternating forms; it does not assign a numerical value to the actual scalar t. The inverse has the corresponding reciprocal factors (5t)^{-1} and (-3t)^{-1}. Thus the actual central differential has a fixed eigenvalue ratio 5:-3, not two independent unknown eigenvalues.

## 5. Consequences

PR528 now applies in its nonzero alternative: Q_1 is invertible away from Omega, has corank one at each point of Omega, and its determinant has the reduced divisor Omega. Consequently b(w) is even off Omega and odd on Omega. The generic middle Betti number is restricted to {0,24}, rather than {0,2,24,26}. No assertion is made that the nontrivial-character pair scalars are nonzero, or that b equals one on Omega.

This is a structural derivation conditional on the pinned inputs, awaiting independent review. No numerical rank, selected HM instance, coefficient search or large computation occurs. It is not a formal proof-assistant check and does not settle the original fixed-pair residual, higher-order lifting or algebraicity.
