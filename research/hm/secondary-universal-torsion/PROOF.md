# Universal simple secondary torsion and completion of the coefficient branches

Work over C on T=P(W*) with G=SL2(F5). Write A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, P=W tensor W', and V=Sym2 W'. Every representation and line-bundle twist is equivariant.

## 1. Actual input and theorem

The immutable originals, with exact byte identities, are in INPUTS.json. FIBER is PR1004, COMPLEMENTARY is PR1014, VONLY is PR1021, FORCEDW is PR971 and BALANCED is PR976. These prove the actual setup

    L=A O(-6) -> K=T6 O(-1) plus A O(-2) -> Q=P O(2) plus W O(-1),

with the first sequence short exact, and the actual secondary boundary

    b:Q -> (V+P+D) O(4).

Its row J is (a_J i_J,b_J j_J), for J=V,P,D, in the unique nonzero channels. The original map beta on K is b composed with the quotient, with an additional identically zero A O(4) target row. Actual quartic transition corrections remain in the six coefficients. No coefficient condition is asserted to hold for the actual object.

Let r be the generic rank of beta. For r>0 let I_r(beta) be the sheaf of ideals generated locally by its r-by-r minors. For r=0 put I_0=O_T. Then, without any hypothesis on the six actual coefficients,

    I_r(beta) is either O_T or I_Omega,

where Omega is the reduced invariant twelve-point orbit. The torsion subsheaf of coker beta is correspondingly zero or has length12, with one copy of the residue field as its local module at each point of Omega. In particular it has no higher-order local elementary divisors and no support on another orbit.

Here I_r is indexed by matrix size, not by a fixed Fitting index across branches. Since the original target has rank15, it equals Fitt_(15-r)(coker beta). For the reduced rank12 target the same ideal is Fitt_(12-r)(coker b). This distinction matters when r changes.

The new proof fills three missing coefficient strata at once. The P-only stratum supplies the final possible simple rank-drop mechanism. The other two strata have constant rank. Prior strata then yield the unconditional theorem, not merely a list of conditional calculations.

## 2. Channel geometry used

FIBER proves unconditionally:

* i_D:P O(2)->D O(4) is a subbundle inclusion with quotient O(12).
* i_V:P O(2)->V O(4) is onto with kernel O(-4).
* i_P:P O(2)->P O(4) has kernel W' O(1), image W' O(3), and quotient W' O(5).
* j_V and j_P are everywhere injective; j_D=v epsilon, with epsilon:W O(-1)->O onto and v:O->D O(4) a subbundle inclusion. Its kernel is O(-2).

The assertion about the quotient of i_P also follows directly from its Euler-square construction: tensor the Euler sequence by W' O(4). Thus no splitting of a positive-degree quotient is assumed.

COMPLEMENTARY proves the unique nonzero channel

    m:W O(-1)->W' O(5)

has determinant a nonzero invariant twelve-form f12 with reduced divisor Omega. It has rank2 off Omega and rank1 on Omega. At the abstract C10 stabilizer, with O(1) character lambda and zeta=lambda^2, W O(-1) has characters0,4, whereas W' O(5) has characters1,4. Consequently the kernel of m on Omega has character0. The Euler kernel has character4. These are statements over the homogeneous orbit, not evaluations at a selected actual point.

## 3. New P-only stratum

Assume a_D=a_V=0 and a_P!=0. Quotient the P target by the subbundle image(i_P)=W' O(3). The induced W-source map is

    h:W O(-1) -> V O(4) plus W' O(5) plus D O(4),
    h=(b_V j_V, c b_P m, b_D j_D),                 (1)

where c is a fixed nonzero scalar depending only on channel normalizations. Indeed the projection of j_P cannot vanish: otherwise it would factor through W' O(3), but

    Hom_G(W O(-1),W' O(3))=Hom_G(P,Sym4 W)=0.

The quotient channel has dimension1 since P occurs once in Sym6 W=V+P. Thus b_P vanishes if and only if its residual coefficient vanishes. No unknown linear recombination or selected coefficient is introduced.

There are canonical exact identifications

    coker b = coker h,
    0 -> W' O(1) -> ker b -> ker h -> 0.          (2)

The right map in (2) retains the actual P-component lift. Surjectivity follows locally by lifting into P O(2) through its onto map to image(i_P); it is a sheaf statement, not an assertion of a global splitting. Locally split source kernel and target image of i_P. Elementary row operations then express b as an identity block of size2, the residual map h, and two zero source columns. Hence every fiber rank is 2+rank h, and its generic-rank minor ideal is that of h at its generic rank.

The complete residual alternatives are:

    b_V != 0:                         rank h=2 everywhere;
    b_V=0, b_P b_D != 0:              rank h=2 everywhere;
    b_V=b_D=0, b_P != 0:              rank h=2 off Omega, 1 on Omega;
    b_V=b_P=0, b_D != 0:              rank h=1 everywhere;
    b_V=b_P=b_D=0:                    rank h=0 everywhere.

The first line uses injectivity of j_V. The second uses m off Omega and the distinct kernel characters of m and epsilon on Omega. In the third, h is m with zero other rows, so its two-by-two minor ideal is exactly (f12). At each zero a rank-one unit minor and a determinant vanishing to order1 give local Smith form diag(1,t), plus zero rows. This proves exactly one simple torsion factor, not just a fiber-rank drop. The last two lines use the Euler factorization. Thus all P-only cases have zero torsion except precisely the third line, which has length12.

As an additional kernel constraint, whenever h is sheaf-injective the original kernel is the actual preimage E of W' O(1) in K:

    0 -> A O(-6) -> E -> W' O(1) -> 0.           (3)

This extension is nonzero, because a splitting would inject the positive bundle W' O(1) into the negative balanced K. Its invariant Ext space has dimension1:

    Ext1_G(W' O(1),A O(-6))=Hom_G(A tensor W',Sym5 W)=C,

using A tensor W'=T6. In fact the new kernel is determined:

    E = V O(-2) plus W O(-5).                       (4)

Here is a coefficient-free derivation. Set F=ker(q_W:K->W O(-1)). As proved in Section5, F=T6 O(-1) plus O(-4). The kernel E fits 0->E->F->W' O(3)->0, since the map F->P O(2) is onto and i_P has image W' O(3). From (3) twisted by2, the V summand of H0(W' O(3))=W' tensor S=V+D maps to zero in H1(A O(-4))=A tensor A=1+A+D. It therefore supplies a nonzero V subspace of H0(E(2)). Its map V O(-2)->F lands in T6 O(-1), because Hom(O(-2),O(-4))=0. The channel has multiplicity1, and T6=V tensor W identifies it with V tensored with the Euler inclusion O(-2)->W O(-1). Thus it is a subbundle and

    F / V O(-2) = V O plus O(-4).

The induced onto map V O plus O(-4)->W' O(3) is nonzero on V O, since the line O(-4) alone cannot surject onto a rank-two bundle. This V-to-W' channel has rank2 everywhere. A generic rank-one factorization would use an equivariant line O(d), with 0<=d<=3, forcing V to occur in Sym^d W, which is impossible. Its minors have degree6, so any nonempty common zero divisor would be invariant of degree at most6, impossible since every projective orbit has size at least12. Its kernel is consequently O(-6).

It follows that C=E/V O(-2) fits 0->O(-6)->C->O(-4)->0. If this split, Ext1(C,V O(-2))=0 would give an O(-4) summand of E. But H0(E(4))^G=0: sequence (3) injects it into (W' tensor Sym5 W)^G=0. Thus C is the nonzero Euler extension W O(-5). Finally Ext1(W O(-5),V O(-2))=0, proving (4) equivariantly after averaging. The splitting is unique equivariantly since Hom_G(W O(-5),V O(-2))=Hom_G(W,V tensor S)=0 and the reverse Hom has negative degree. In the remaining two residual cases (2) and the actual preimage sequence retain the kernel without discarding graph lifts.

## 4. New D-source-without-D-W stratum

Assume a_D!=0 and b_D=0, with no restrictions on a_V,a_P. The full P-source map is an everywhere-injective graph over its D projection i_D. If at least one of b_V,b_P is nonzero, a kernel vector (p,w) first satisfies i_D(p)=0, hence p=0, and then an injective j_V or j_P forces w=0. This works on every fiber. Therefore b has constant rank6, ker beta=L, and its cokernel is locally free.

If b_V=b_P=0, all W-source rows vanish. The full P block still has constant rank4. The reduced kernel is exactly W O(-1), not a nontrivial graph, and FORCEDW identifies its actual preimage as D O(-4). Again the cokernel is locally free. This treats arbitrary other P coefficients simultaneously, without selecting or normalizing them.

## 5. New zero-P-source stratum

Assume a_V=a_P=a_D=0. The map factors through W O(-1). If (b_V,b_P)!=0, its rank is constantly2; if b_V=b_P=0 and b_D!=0, its rank is constantly1; if all b vanish, its rank is0. No torsion occurs.

The original kernels can also be identified without any coefficient selection. The canonical projection q_W:K->W O(-1) kills T6 O(-1), since Hom_G(T6,W)=0. Its restriction to A O(-2) is onto and is the unique nonzero quadratic-evaluation channel, whose kernel is O(-4). Accordingly the rank2 case has original kernel

    T6 O(-1) plus O(-4).

In the rank1 case the Euler composite on A O(-2) is the nonzero degree-two evaluation onto O, with kernel W O(-3). The kernel is therefore

    T6 O(-1) plus W O(-3).

For rank0 it is K itself. The uniqueness and nonvanishing of these evaluation maps follow either from the standard quadratic Euler sequence or from the actual onto q_W and epsilon. These direct-sum statements are on the canonical balanced decomposition of K, not on an arbitrarily split quotient extension.

## 6. Exhaustive partition and global theorem

Every six-channel coefficient tuple lies in exactly one of these disjoint strata:

1. a_D!=0, b_D!=0: FIBER, PR1004.
2. a_D!=0, b_D=0: Section4 above.
3. a_D=0, a_V!=0, a_P!=0: COMPLEMENTARY, PR1014.
4. a_D=0, a_V!=0, a_P=0: VONLY, PR1021.
5. a_D=a_V=0, a_P!=0: Section3 above.
6. a_D=a_V=a_P=0: Section5 above.

FIBER proves its generic-rank minor ideal is O_T or I_Omega, with exactly one simple torsion factor at each orbit point in the latter case. COMPLEMENTARY proves the same by its residual two-column determinant and stabilizer analysis. VONLY has constant rank. The new strata have just been proved to have these same alternatives, and the displayed partition is exhaustive independently of all W-source zero patterns. This proves the theorem for b.

Finally K->Q is an onto bundle map, hence locally splits. Adding its three kernel columns to b adds only zero columns after local invertible operations. Adding the identically zero A target row block changes no nonzero minor ideals or torsion. Thus the same theorem holds for the original beta. At a point of Omega in a jumping case the fiber kernel is one dimension larger than the kernel sheaf's fiber; the local torsion term accounts for that difference.

## 7. Scope

This completes the rank-drop support and multiplicity problem for the actual secondary map, conditional on no selected branch at all. It does not select whether its actual torsion is zero or length12, identify its full torsion-free quotient, or resolve the later obstruction, top sigma, vertex extension, global odd-quadric question, or source/catalogue alternatives. All actual quartic corrections remain present. No actual HM/source coefficient, parameter, point, derivative, jet, matrix or instance rank was evaluated.
