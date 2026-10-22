# Independent deductive review

Status: PASS.

Reviewed artifact: `PROOF.md`, SHA-256 `a06e4e12e6981dc328e51a393b8946bce122384085d3c4975381579c81b9e32c`.

## Sources checked directly

- [PR747, immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a0ee30a5142477e54245b7c6f22d561abb4f5f1/research/hm/source-family-fourth-square-exclusion/PROOF.md): the fixed-frame identity, C-linearity of h to K_h, nonzero d, and the distinction between immutable class and fourth-square scalar.
- [PR752, immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/e0d0cb31fbef5c7d6f1148e2278fbce115239dcf/research/hm/exceptional-direction-bounds/PROOF.md): rational-pencil rigidity and the exact two-dimensional eigenspace plus scalar-compatibility criterion.

## Independent checks

1. For every nonzero v, Q(v) is nonzero, self-adjoint and trace-free. Its repeated eigenspace is v-perp with eigenvalue -B(v,v)/3, including the isotropic rank-one square-zero case. Conversely both eigenspace types of PR752 have this form up to scalar.
2. The rank-three identity center misses every secant and tangent line of the quadratic Veronese. Point and length-two separation therefore give a closed immersion, not merely a set-theoretic parametrization. Pullback O(1)=O(2) gives smooth degree-four image. The transported Sym4 W marking and its fourth-power boundary are distinguished from an unspecified physical positive marking.
3. The compatibility equation is exactly Psi(v)=K_{S^{-1}Q(v)}+(gamma/3)B(v,v)d. Its finitely many coefficient vectors span a finite-dimensional C-space, so the equations define an ordinary closed C-locus despite the ambient k-vector space V.
4. Symmetric polarization and inverse-B contraction give ctr(Q)=0 and ctr(B(v,v))=3, with no missing factor of two. Hence ctr(Psi)=gamma d is nonzero. The scalar quadratic system is therefore nonzero, its P2 zero locus has dimension at most one, and its image has codimension at least three in P(H).
5. Fourth powers span the transported five-dimensional source module. Thus the whole isotropic boundary is exceptional exactly when K is the zero linear map. In that case the defining ideal is (q), giving the reduced conic. Otherwise a nonzero restricted quartic bounds the boundary intersection by length four, without determining any actual coefficient or source point.

A minor notation correction replaced Z by X=j(Z) when discussing a subset of the source surface. No mathematical repair was required.

This is an independent deductive review, not a proof-assistant check. No selected actual HM/source instance, coefficient, point, derivative, matrix rank, model substitution or scan was evaluated. The result neither proves that the exceptional source locus is nonempty nor decides beta4 or algebraicity. Vanishing of the immutable class remains only a necessary scalar-square gate.
