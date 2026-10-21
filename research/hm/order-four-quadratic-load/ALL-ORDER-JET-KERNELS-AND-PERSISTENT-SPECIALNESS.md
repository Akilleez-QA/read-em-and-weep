# All-order jet kernels and a finite test for persistent fiber specialness

## Actual geometric setup

Let X=P_Q(E), with quotient tautological class L and source hyperplane H. Its fifty simple evaluation base points form Z. Write b:Xhat->X for their blowup, E_exc for the exceptional divisor, A=L-E_exc=f*O_P3(1), and M=2L-H. The globally checked derived comparison gives

    Rf_*M=[V tensor O -> P tensor O(1)]

in degrees zero and one, with dim V=20, dim P=5 and actual differential theta. Define the coherent sheaf

    N=ker[theta*:P* tensor O(-1) -> V* tensor O].

No generic or chosen matrix replaces theta.

## 1. Every auxiliary jet kernel is a twist of one sheaf

For every integer t>=1 there is a natural identification, with fixed scalar volume lines understood,

    H0(X,I_Z^(t+1) tensor O_X(tL+3H)) = H0(P3,N(t)).        (1)

Proof. The canonical classes are K_X=-2L+2H and K_Xhat=b*K_X+3E_exc. Thus

    K_Xhat - (M-(t+4)A) = tL+3H-(t+1)E_exc.

The standard blowup pushforward b_*O(-(t+1)E_exc)=I_Z^(t+1), together with Serre duality on the smooth fourfold Xhat, identifies the left side of (1) with H4(Xhat,M-(t+4)A)*. In the theta model the only terms contributing to this fourth cohomology are

    V tensor H3(O(-t-4)) -> P tensor H3(O(-t-3)).

Its cokernel is H4. Serre duality on P3 identifies the dual kernel with

    ker[P* tensor H0(O(t-1)) -> V* tensor H0(O(t))],

which is H0(N(t)). This proves (1). In particular t=1 and t=2 recover the previously named J5 and J6 kernels.

These are kernels of actual evaluations of O_X(tL+3H) to the order-(t+1) fat points at Z. Equation (1) asserts nothing about maximal rank of those evaluations.

## 2. One nonspecial fiber eliminates all these kernels

By derived base change, H1(Xhat_beta,M|Xhat_beta)=coker(theta_beta). If one beta has H1=0, theta is generically surjective. Its dual then has zero generic kernel. Since N is a subsheaf of a vector bundle and hence torsion-free, this implies N=0. Formula (1) then kills every jet kernel for every t>=1. No bound on dim ker[H0(theta)] is needed.

Conversely, if every fiber has H1>0, theta has generic rank at most four. N has positive rank, and N(t) has nonzero global sections for all sufficiently large t. Thus some higher auxiliary jet kernel is nonzero. This distinguishes persistent specialness from isolated or lower-dimensional fiber failures, which can occur even when N=0.

It also distinguishes this issue from the constant global kernel of theta: a pointwise-surjective theta can still have a nonzero kernel on global sections, as the abstract rank-two-annihilator example in THETA-REFLEXIVE-EXTENSION-AND-SEGRE-DEGENERACY.md proves. Eliminating every jet kernel is not itself a proof of primitive-four vanishing.

## 3. Only the first five jet kernels are needed for this test

There is a finite universal bound. If theta has generic rank s<=4, then

    H0(N(s+1)) is nonzero.                              (2)

Choose s columns of its dual linear matrix that are independent over the function field, and one further column. Choose s rows for which the first s columns have nonzero determinant. The signed s-by-s cofactors of this s-by-(s+1) submatrix give a nonzero column relation, with homogeneous polynomial coefficients of degree s. It annihilates every row, not just the chosen rows: all rows are linear combinations of the selected independent rows over the function field, and the resulting polynomial identity holds on a dense open and hence everywhere. Extending by zeros to the five columns gives a nonzero element of H0(N(s+1)). For s=0 any constant column vector gives the assertion.

Consequently the following are equivalent:

1. Some beta fiber is nonspecial for M, meaning H1=0.
2. N=0, equivalently theta has generic rank five.
3. All auxiliary jet kernels in (1) vanish.
4. The five auxiliary jet kernels with t=1,2,3,4,5 vanish.
5. The single auxiliary jet kernel H0(X,I_Z^6 tensor O_X(5L+3H)) vanishes.

For (5), multiply the nonzero cofactor section of N(s+1) by a nonzero homogeneous polynomial of degree 4-s. This remains nonzero because N is a subsheaf of a vector bundle on integral P3, and gives a section of N(5).

If the persistent generic fiber corank is c=5-s>0, a nonzero kernel already occurs for some t<=6-c. This bound uses only a universal cofactor identity; it is not an evaluation of any selected HM minor.

## 4. Asymptotic size in the persistent case

If the persistent generic corank is c>0, N has rank c. Its Hilbert polynomial and Serre vanishing imply

    dim H0(X,I_Z^(t+1)(tL+3H)) = (c/6)t^3 + O(t^2)

for sufficiently large t. Thus the leading growth of the actual higher jet kernels measures the persistent generic fiber corank. This gives no value for the actual corank.

## Scope

The theorem supplies an exact finite criterion for generic fiber nonspecialness and links all higher auxiliary jet kernels to it. It does not prove that any of its equivalent conditions holds for the actual HM map, does not eliminate its constant global kernel, and does not solve original-source membership or higher deformation lifting.

Dependencies: FINITE-EXCEPTION-DERIVED-COMPARISON.md, the established fifty-point blowup geometry, and THETA-REFLEXIVE-EXTENSION-AND-SEGRE-DEGENERACY.md. All arguments are symbolic and retain the actual map.
