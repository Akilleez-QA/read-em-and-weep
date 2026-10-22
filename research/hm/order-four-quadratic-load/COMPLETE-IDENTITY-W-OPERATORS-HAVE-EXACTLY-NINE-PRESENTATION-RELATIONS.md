# Complete identity-W operators have exactly nine presentation relations

## 1. Statement and dependencies

The complete marked coefficient family has54 Rq and10 Rh channels. Its map to the actual **supported identity-W middle operators** has kernel dimension9 and image dimension55. These are universal exterior-presentation relations, not source equations and not an actual-instance rank test. The result does not exclude an operator or solve the source completion.

Use `COMPLETE-IDENTITY-W-COEFFICIENTS-HAVE-AN-EXPLICIT-MARKED-GENERATING-SET.md` for the complete coefficient space and `IDENTITY-W-ADDITIONS-LEAVE-THE-PRINCIPAL-U-RECONSTRUCTION-UNCHANGED.md` for the full arbitrary-input factorization. The proof below contains no source coefficients; its verifier imports only SymPy.

Pinned public prerequisites: [complete coefficient construction, PR730](https://github.com/Akilleez-QA/read-em-and-weep/blob/a79c896439bc141dcb07a8891ba391ee8b38fcc9/research/hm/order-four-quadratic-load/COMPLETE-IDENTITY-W-COEFFICIENTS-HAVE-AN-EXPLICIT-MARKED-GENERATING-SET.md) and [full operator factorization, PR734](https://github.com/Akilleez-QA/read-em-and-weep/blob/6a16340165751d4f4265106c6dee39dede7b6afe/research/hm/order-four-quadratic-load/IDENTITY-W-ADDITIONS-LEAVE-THE-PRINCIPAL-U-RECONSTRUCTION-UNCHANGED.md).

The latter factorization says an identity-W operator with polar symbol r is determined by

    R = K E_r - E_r up adj_6(K) low.

It vanishes as a full exterior operator iff R=0: apply it to an arbitrary mixed input supported in either negative coordinate and read its VV component. Multiplication by that negative coordinate is injective in the polynomial coefficient ring. Thus no presentation relation is lost by passing to R.

## 2. Universal orthogonal calculation

Write the six-space as V tensor U, where V is orthogonal of dimension3 and U is symplectic of dimension2. After a constant orthogonal-frame identification, E_r up is a common nonzero scalar times

    B(r)_ij = sum_k epsilon_ijk r_k.

The same identification sends the physical trace-free positive H to an arbitrary symmetric trace-free3-by3 matrix H, and its other polar symbol to Hr. This is only a change of basis for fixed tensors, not a choice of monad coefficients. Explicitly, if S^t G S=I, then r'=S^t r, H'=S^t H S^-t is symmetric because HG=GH^t; the cross matrix acquires only the common factor det(S)^-1.

For the full coefficient pair write Q(H) for Rq and K for Rh. Q is linear in H; K is independent of H. Multiplication of R by the invertible `up` gives the kernel equation

    Q(H) B(r) - B(r) Q(H)^dagger
      + K B(Hr) - B(Hr) K^dagger = 0.                    (1)

End(U)=scalar plus sl(U), with symplectic adjoint respectively +1 and -1. Therefore (1) separates into the following two exhaustive cases.

### Scalar U sector

Here the dagger is ordinary transpose on the3-by3 coefficient. For a symmetric matrix-valued linear form X(r), define

    Rec(X)_il = (1/3) sum_jk (partial X_ij/partial r_k) epsilon_ljk.

Direct epsilon contraction gives

    Rec(Q B-B Q^t) = Q-(tr Q/3)I.                       (2)

Set X=-(K B(Hr)-B(Hr)K^t). Thus the only possible trace-free part of Q is Rec(X). Substitution into (1) has eight independent unit coefficient consequences: all six off-diagonal entries of K vanish and K00=K22, K11=K22. The verifier records the literal coefficients, not a matrix-rank calculation. For example with

    H = [[a,b,c],[b,d,e],[c,e,-a-d]],

coefficients of the residual `Rec(X)B-B Rec(X)^t-X` include

    [r0 c] residual00 = -2 K01,
    [r0 b] residual00 =  2 K02,
    [r1 c] residual01 = (2/3) K10,
    [r1 b] residual00 = (2/3) K12,
    [r2 b] residual02 = -(2/3) K20,
    [r2 c] residual00 = -(2/3) K21,
    [r2 b] residual00 = -(2/3)(K00-K22),
    [r2 b] residual11 =  (2/3)(K11-K22).

Conversely K=sI gives X=0, and (2) then says Q=lambda(H)I. Hence this sector's kernel is precisely D5 plus1, of dimension6.

### Traceless U sector

For each of the three traceless U factors, the transpose terms have the opposite sign. The universal cross-product identity is

    Q B(r)+B(r) Q^t = B((tr Q I-Q^t)r).

The map L(Q)=tr(Q)I-Q^t is invertible, with

    L_inverse(Z)=(tr Z/2)I-Z^t.

Consequently the kernel is exactly

    Q(H)=-L_inverse(L(K)H),                              (3)

with K an arbitrary3-by3 matrix. There are9 parameters for each of the three U factors, hence27 in this sector. Formula (3) supplies the relations explicitly.

Combining the sectors, the universal216-dimensional coefficient-pair space has a33-dimensional presentation kernel and183-dimensional image. This conclusion follows from explicit inverses and unit coefficients only.

## 3. The marked equivariant family

As G-modules, the universal kernel is

    D5 + 1 + End(V) tensor sl(U)
      = 2·1 + A + 3V + P4 + 3D5.                        (4)

Indeed End(V)=1+V+D5 and sl(U)=V. The marked negative coefficient input is N=2A+V+P4+D5. Exactness of taking G-equivariant Hom in characteristic zero therefore gives

    dim Hom_G(N,kernel) = 2+3+1+3 = 9.

The complete coefficient theorem supplies dimension64 before the exterior map, so its image has dimension55. The verifier independently checks the full character arithmetic, including dimensions216,33,183 and64,9,55, distinguishing A from V.

The87 Rq generators in that theorem are deliberately redundant already at the coefficient level. The additional nine relations here are intrinsic to the64-dimensional coefficient space, not a claim that an87-element list has only nine dependencies. No smaller source-family screen is inherited; all remaining coupled U and c equations must still be solved.
