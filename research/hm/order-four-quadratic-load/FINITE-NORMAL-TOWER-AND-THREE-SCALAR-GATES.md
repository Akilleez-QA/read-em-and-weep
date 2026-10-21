# A finite normal tower with three scalar gates

Let Q=Q0 be the actual invariant quadric, B=End_0(F), and Q_n=(q0^n=0). Fix the determinant inherited from F and the identification on Q. All equivariance is for the binary icosahedral group G over C. No actual coefficient or multiplication matrix is evaluated below.

## Result

The equivariant first-normal extension torsor is an affine line. There are at most two marked isomorphism classes on Q_2 which extend to Q_3, including the actual ambient restriction. Each such class has a unique marked lift to Q_3. It has a unique formal continuation if and only if two further scalar obstructions, for Q_3 to Q_4 and Q_4 to Q_5, vanish. All steps from Q_5 onward are unobstructed and uniquely liftable.

Thus there are at most two fixed-determinant equivariant formal extensions with fixed reduction on Q. This is a theorem about a formal neighborhood, not algebraization, and it proves no positive cubic Bockstein nonvanishing.

The three potentially nonzero obstruction spaces are

    H2(B_Q(-4))^G = C,  H2(B_Q(-6))^G = C,
    H2(B_Q(-8))^G = C.

The last equality uses the NEW actual multiplication theorem

    q0:H1(B(3))^G -> H1(B(5))^G is zero.                 (1)

This zero is forced by the actual primary submodule, not by two one-dimensional vector spaces alone.

## 1. Uniform ambient vanishings, with pinned inputs

The following three uniform bounds hold:

    H3(B(t))=0 for t>=-1,
    H2(B(t))=0 for t>=1,
    H1(B(t))=0 for t>=6.                                (2)

For the second bound, [PR167, Section 2](https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md) proves t>=2 by the actual Decker section resolution. [PR455, Section 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md) proves the remaining t=1 endpoint.

For the first bound, PR167's tensor resolution has terms

    E0(t)=15F(t-3)+4F(t-2),  E1(t)=35F(t-4),
    E2(t)=20F(t-5),         E3(t)=2F(t-7).

At total cohomological degree3 and t>=0, the only controlling groups are

    H3(E0)=15H1(F(-t-1))*+4H1(F(-t-2))*=0,
    H4(E1)=35H0(F(-t))*=0.

The remaining degrees exceed4. Here H1(F(s))=0 for s<0 and H0(F(s))=0 for s<3 are the pinned primary inputs. Therefore H3(End(F)(t))=0, and trace splitting gives the same for B. PR455 Section2 separately proves the endpoint H3(B(-1))=0.

For the third bound use the stronger actual primary-image theorem, [Section 6](https://github.com/Akilleez-QA/read-em-and-weep/blob/d5d9bd997145b0ecf7d7bd659a19fb7845afb75f/research/hm/actual-primary-image-extension/PROOF.md). Its exact sequence injects the primary term and identifies the quotient inside the dual Rao module of the actual disjoint lines. At t>=6 the primary H1(F(t-2)) vanishes, and the Rao degree 5-t is negative, so its H0 on every line vanishes. Consequently H1(B(t))=0. This uses no Hilbert-table or rank assumption.

## 2. Uniqueness and termination of the obstruction tower

For n>=2 the square-zero ideal for Q_n inside Q_(n+1) is O_Q(-2n). Fixed-determinant lifts have obstruction in H2(B_Q(-2n)); if it vanishes, their marked isomorphism classes form a torsor under H1(B_Q(-2n)), with marked infinitesimal automorphisms H0(B_Q(-2n)). These groups depend on the fixed reduction E=F|Q, not on which earlier lift has been chosen.

Restricting B(-2n) gives

    H1(B(-2n)) -> H1(B_Q(-2n)) -> H2(B(-2n-2)).

By self-duality of B and omega_P4=O(-5), the outside groups are dual to H3(B(2n-5)) and H2(B(2n-3)). They vanish by (2), for all n>=2. Thus

    H1(B_Q(-2n))=0 for every n>=2.                       (3)

Also H0(B(-2n))=0 by stability, and H1(B(-2n-2)) is dual to H3(B(2n-3))=0. The restriction sequence therefore gives H0(B_Q(-2n))=0. Hence marked lifts, when they exist, are unique up to a unique isomorphism inducing identity on the preceding thickening and preserving determinant.

The rank-three quadric is a projective Gorenstein hypersurface even though singular, so its dualizing sheaf is O_Q(-3). Since B_Q is locally free and self-dual, Serre duality gives

    H2(B_Q(-2n)) = H1(B_Q(2n-3))*.

When n>=5, set m=2n-3>=7. The positive restriction sequence places H1(B_Q(m)) between H1(B(m)) and H2(B(m-2)), both zero by (2). Thus all obstruction groups vanish from n=5 onward, even before invariants. Only n=2,3,4, the transitions to 3Q,4Q,5Q, can obstruct. Finite-group invariants are exact and add no descent obstruction in characteristic zero.

## 3. Exact odd-twist characters

Use the actual equivariant monad K-class with ambient H=V+W, N=A+Wprime and K=Omega^2(2):

    [F]=[Wprime K]-[N O(-1)]-[N O],
    [K]=[Lambda^2 H O]-[H O(1)]+[O(2)],
    [B(t)]=[F]^2[O(t+1)]-[O(t)].

These are the same fixed linearizations as verify_negative_vertex_scalar.py and verify_exceptional_hyperplane_characters.py. Taking Euler characters in the universal representation ring gives

    H1(B(1)) = A+2V+2P4+2D5+W+2S4+3T6,
    H1(B(3)) = 1+4A+2V+3P4+3D5+3Wprime+3S4+6T6,
    H1(B(5)) = 1+A+V+D5+Wprime+3T6.                    (4)

The cohomology inputs that convert Euler characters to H1 are essential. Higher groups vanish by (2), with H4 vanishing by stability and duality. H0(B(1))=H0(B(3))=0 follows from the actual exterior-symmetric evaluation resolution: its line tail is negative, H0(F(t-2))=0, and the preceding image has H1=0. At t=5 that resolution gives H0(B(5))=Sym^2 P4=1+P4+D5, as in TWIST-FIVE-GLOBAL-COHOMOLOGY-AND-BOUNDARY-DEFECT.md. The resolution and its actual multiplication identification are pinned at d5d9bd99 above.

The standalone verifier verify_normal_tower_characters.py evaluates the universal character expressions at all nine abstract conjugacy classes and checks each full decomposition. It does not evaluate a map of the actual bundle.

## 4. The actual scalar in (1) vanishes

The same pinned primary-image theorem gives an injective graded multiplication map

    U tensor H1(F(t-2)) -> H1(B(t)),  U=H0(F(3))=P4.    (5)

The primary characters are

    H1(F(1))=P4+W+S4,  H1(F(3))=W.

The first is already checked in verify_negative_vertex_scalar.py. The second follows from the actual monad Euler class, H0(F(3))=P4 and the primary higher-cohomology support. Both are checked again by the companion verifier as applicable.

At t=3 the source of (5) has exactly one invariant, from P4 tensor P4. Its image must therefore be the unique invariant line of H1(B(3)) in (4). At t=5 the source is P4 tensor W=Wprime+T6, which has no invariant. Because (5) is a graded module map, q0 sends the entire primary submodule in twist3 into the primary submodule in twist5. Since q0 is invariant, it kills the invariant line. This proves (1) for the actual q0 multiplication.

## 5. Three scalar targets and the finite number of formal extensions

The normal-derivative note proves the invariant injection

    H2(B(-4))^G=C -> H2(B_Q(-4))^G.

Its cokernel lies in H3(B(-6))^G=H1(B(1))^{G,*}=0 by (4), so it is an isomorphism. By Q-duality, the other two obstruction dimensions are those of H1(B_Q(3))^G and H1(B_Q(5))^G. The restriction sequences and (2) identify these with

    coker[H1(B(1))^G -> H1(B(3))^G]=C,
    coker[q0:H1(B(3))^G -> H1(B(5))^G]=C,

respectively. The second equality uses the actual zero theorem (1).

Relative to the actual ambient first-normal point, ACTUAL-SECOND-NORMAL-OBSTRUCTION-DERIVATIVE-IS-INJECTIVE.md proves that the first obstruction is the scalar polynomial

    ob(s)=c s+d s^2,  c!=0.

Its zero scheme consists of exactly one reduced point if d=0, or exactly two distinct reduced points if d!=0. The actual point is s=0. The other point, if present, has a unique marked Q_3 lift by (3), and its further existence is decided by one scalar obstruction to Q_4 and then one to Q_5. All later lifts exist uniquely. Therefore at most two formal extensions exist, and their determination is a finite three-gate problem. The values d and the two later scalar obstructions have not been computed here.

Nothing in this theorem identifies these bundle-lifting obstructions with the positive cubic Bockstein gate. Nor does it imply algebraization or solve the original source-membership/Weil problem.
