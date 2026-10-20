# Full Sylow-five symmetry cuts the exceptional kernel Grassmannian to (P1)^4

## Result and boundary

Let V have basis e_j, j in F5, and X e_j=e_(j+1), Z e_j=zeta^j e_j, D e_j=zeta^(j²)e_j. Let T=Schur_(2,1)V=ker(V tensor exterior²V -> exterior³V). Use the actual target representation J=A* tensor Sym³W and the established nonzero equivariant surjection q:T -> J. No value of q is used below.

Set g=X Z³ D³ and H′=<g,Z>. The full linear Sylow-five group P=<X,Z,D> has order 625, and H′ is normal of index five. Full P-equivariance forces a new necessary configuration on the four-dimensional exceptional-clock kernel L: it must be the direct sum of four lines, one in each of four canonically specified two-dimensional spaces. Thus its parameter locus is (P1)^4 inside Gr(4,8), before imposing the incidence requirements for residual rank five and repeated-input injectivity.

This is a necessary configuration, not exclusion of rank five, not existence of a globally cyclic realization, and not a new rank computation. In particular the local C5 countermodel does not establish realization of this configuration.

## 1. Group verification

The 625 matrices zeta^c X^a Z^b D^d, with a,b,c,d in F5, form a group. The relations Z X=zeta X Z and D X D^-1=zeta X Z² put any product in this normal form. They are distinct: permutation parts determine a, and equality of the remaining diagonal entries says that the degree-at-most-two polynomial c+bj+dj² is zero for all five j, forcing b=c=d=0. Each generator has order five, so this is a five-group. Since the linear normalizer has order 5 times 3000, it is Sylow.

The elements zeta^c g^a Z^b are 125 distinct matrices by the same permutation argument, and Zg=zeta gZ. Also g^5=1, since the exponents accumulated around its permutation cycle sum to 3 sum j+3 sum j²=0 in F5. Thus H′ is Heisenberg of order125.

Conjugation by D sends g to zeta g Z² and fixes Z. Thus D normalizes H′. Moreover H′ and D generate P because X=g D^-3 Z^-3. Hence H′ is normal in P with quotient C5. This verification does not incorrectly identify P with the point stabilizer: the exceptional point stabilizer remains C5 projectively.

## 2. Corrected quotient action

For any P-module M with central character zeta³, define Q(Z_M) to be the spectral operator acting by zeta^(2j²) on the Z_M-eigenspace of eigenvalue zeta^j. This is an unambiguous polynomial in Z_M; 2 is the inverse of 3 in F5. Define

    B_M = D_M Q(Z_M)^-1.

The group relation on M is D_M X_M D_M^-1=zeta³ X_M Z_M². Since X_M increases Z-weight by 3, the ratio of Q-eigenvalues is

    zeta^[2((j+3)²-j²)] = zeta^(2j+3).

It follows that Q(Z_M) has the same conjugation effect on X_M as D_M. Therefore B_M commutes with X_M and Z_M, and also D_M. In particular it commutes with all of P and with g_M. Both factors commute and have fifth power one, so B_M^5=1. Its formation is natural in P-equivariant maps.

On a degree-three tensor with original indices a,b,c, B_T is multiplication by

    zeta^[a²+b²+c²-2(a+b+c)²].

This formula respects the Schur subspace, uses no operation coefficients, and gives an explicit universal description of the extra constraint. Although D itself does not preserve a chosen g-eigenspace, B_T does. Confusing these two operators would invalidate the argument.

## 3. Source multiplicities

On the original Z-weight-zero space T[Z=1], Q is identity and B_T=D_T. The four repeated-index vectors e_a tensor (e_a wedge e_(-2a)), a≠0, have D-weights 6a²=a². The remaining two distinct-index blocks, indexed by {0,1,4} and {0,2,3}, each have dimension two and weights 2 and 3 respectively. Consequently the B-eigenvalue multiplicities on this eight-dimensional space are

    weight 0: 0; weights 1,2,3,4: 2 each.

Each B-eigenspace in all of T is H′-stable. The central character is primitive, so each is a sum of five-dimensional irreducible H′ modules. In such a module either noncentral clock, Z or g, has five simple eigenvalues. Therefore on any fixed g-eigenspace U of T the B-eigenspaces E_1,E_2,E_3,E_4 all have dimension two, and U is their direct sum.

A scalar normalization of g to fix the chosen point line merely relabels its eigenvalues and leaves this statement unchanged.

## 4. Actual target multiplicities, including scalar normalization

We spell out the normalization because mere knowledge that J restricts to four copies of each g-character is insufficient here.

Use the established normalizer identities exterior²V=A tensor W and J=A* tensor Sym³W, with A the five-dimensional irreducible module of Heisenberg central character zeta² and W Heisenberg-trivial. On A, each Z-weight j occurs once. The relation D X D^-1=zeta² X Z² implies that D acts on its Z-weight j line as

    delta zeta^(3j²),

where delta^5=1. Here X changes weight by 2 and 3=1/2 modulo5. The normalizer contains the torus element inducing index scaling by 2, which conjugates D to D^4 and conjugates their actions on A. Thus their traces agree. The nonzero quadratic Gauss sums sum_j zeta^(3j²) and sum_j zeta^(12j²) agree by reindexing j -> 2j. Hence delta=delta^4; together with delta^5=1 this gives delta=1.

On exterior²V, the Z-weight-zero lines indexed by the pairs {1,4} and {2,3} have D-weights 2 and 3. Since A has D-eigenvalue one on its Z-weight-zero line, W restricted to D has weights 2 and 3. Consequently Sym³W has weights

    6, 7, 8, 9 modulo5 = 1,2,3,4,

each once. On A*, the weight-j line has D-eigenvalue zeta^(-3j²)=zeta^(2j²), precisely the Q-factor. Thus B_J acts as identity on A* times the action of D on Sym³W. Its four nontrivial eigenvalues occur once each on every Z-clock or g-clock eigenspace of J.

The trace argument uses only the already established extension A to the normalizer. It makes no choice or evaluation of the cubic-operation map.

## 5. The new kernel constraint

The kernel K of q has dimension20. Naturality gives B_J q=q B_T, so each B-eigensummand maps surjectively onto the corresponding target eigensummand. Equivariance and semisimplicity then give, for any g-clock eigenspace U,

    L=K intersect U = ell_1 direct sum ell_2 direct sum ell_3 direct sum ell_4,
    ell_a is a one-dimensional subspace of E_a, dim E_a=2.

Equivalently, if p_a=(1/5) sum_(n=0)^4 zeta^(-an) B_T^n, then p_a L is a line for each a=1,2,3,4, and L=sum_a p_a L. Thus the allowed kernels form the explicitly specified product of projective lines inside the full four-plane Grassmannian.

## 6. Rank-five incidence formulation

Choose the standard H′ eigenbasis at an exceptional g-eigenpoint, normalize its eigenvalue to one, and use exactly the universal spaces H_0,...,H_4 in Sections3–4 of ../heisenberg-universal-rank-four/PROOF.md. That proof gives

    rank Q_u = 10 - sum_(j=0)^4 dim(L intersect H_j).

A residual-rank-five point therefore requires a quadruple (ell_1,...,ell_4) in the product above satisfying

    sum_(j=0)^4 dim((ell_1+ell_2+ell_3+ell_4) intersect H_j)=5.

Repeated-input injectivity additionally forbids all repeated-input tensors in K; in particular L contains none of the four lines C r_i of the cited proof. These are necessary conditions only. The condition involving all repeated tensors is stronger than those four exclusions and must not be silently replaced by them in a proposed construction.

The old H′ argument allowed an arbitrary four-plane in an eight-space, subject to repeated-vector exclusions. Full P reduces that family from Gr(4,8), dimension16, to the above dimension-four product. This is genuine extra global symmetry information, but does not by itself assert that the displayed incidence locus is empty. Nor does a point of the incidence locus alone supply full-normalizer equivariance or the remaining global injectivity conditions.

## Evidence boundary and audit

Only finite-group normal forms, quadratic-character algebra, Schur-tensor decompositions, and universal subspace incidence were used. There was no evaluation of the actual operation, source coefficients, selected source input, rank instance, derivative, or residue. The only writes are this local artifact and its audit. An independent line-by-line audit passed without correction; see AUDIT.md.
