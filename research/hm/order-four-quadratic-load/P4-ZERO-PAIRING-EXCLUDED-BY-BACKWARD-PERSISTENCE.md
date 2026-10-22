# All three single-P4 types have nonzero cubic pairing

## Result and scope

In the hypothetical generic-SF-rank-three plateau `(k,l)=(3,2)`, the branch `B=0` is impossible for each of the three formal primal types

    X: (0,2,0,0,0,0,0,1), E=P O(-2)+2T O(-3)+O(-10);
    Y: (0,1,1,1,0,0,0,0), E=P O(-2)+T O(-3)+(V+P) O(-4);
    Z: (1,1,1,0,1,0,0,0), E=P O(-2)+(Wp+T) O(-3)+V O(-4)+Wp O(-5).

Here `P=P4`, `Wp=Wprime`, `S=S4`, `D=D5`, and `T=T6`. This note treats only zero pairing. By itself it does not exclude these types' nonzero-pairing branches, the whole adjacent profile, or generic SF rank three. The established lower bounds SF rank 3 and square rank 27 are unchanged.

The proof uses only universal representations, hypothetical bundle splittings and degrees, saturation, complete evaluation, and backward persistence. It selects no actual HM/source coefficients and uses no actual maps, matrices, rank tests, scans, local models, or positive operators.

## 1. Frozen inputs

Use `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, `ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md`, `RANK-THREE-CUBIC-PAIRING-EXCLUDED-IN-ADJACENT-GAUSS-PROFILE.md`, and `SIX-LARGE-QUADRATIC-MODULES-EXCLUDED-BY-BACKWARD-GAUSS.md`.

The saturated plateau is

    F0 < K2 < K < E < F4 < F5,

with ranks `8,11,14,17,20,23`, `deg E=-54`, and

    H0(K(2))=0, H0(K2(3))=0, H0(F0(4))=0.                 (1)

Both backward derivatives in the interior have rank three. Every positive invariant torsion length is at least 12. In each of the five possible Q types, the maximum ordinary degree is at most eight, and the largest two degrees sum to at most fourteen. The canonical cubic evaluation in Q* is `T O(-3)`.

Put

    phi:P O -> Q, psi:T O -> E*(1), B:P O -> T O(3).

Both restricted derivatives are injective on sections. If their ranks are a,b and `B=0`, then `a+b<=3`. Both a,b are positive. All equivariant splittings below are bundle splittings, never horizontal splittings.

## 2. The rank-two cubic-image branch

First assume b=2. Then a=1, and the image J of phi is a globally generated equivariant line whose sections contain P. Testing the even degrees through eight gives exactly

    J=O(n), n=6 or 8.                                    (2)

J is saturated in Q: a possible defect is at most `8-n<12`.

The necessary rank-two image blocks of psi are

    X: Wp O(2), Wp O(4), W O(10);
    Y: Wp O(2), Wp O(4);
    Z: Wp O(2), Wp O(4), Wp O(6).

There are no rank-one blocks in Y or Z. In X the only eligible line is O(11), so two line summands cannot form a rank-two image. The block `W O(10)` has degree 20, whereas the maximum rank-two degree in E*(1) for X is 15; hence it cannot inject. Consequently

    L=im psi=Wp O(e),
    e in {2,4} for X,Y, and e in {2,4,6} for Z.           (3)

Every L is saturated. The maximum rank-two degrees of E*(1) for X,Y,Z are respectively 15,10,12, so their possible defects are at most `15-2e`, `10-2e`, `12-2e`, all nonnegative cases being less than twelve.

Let I be the actual full image of `beta_E(2):E(2)->Q`. Dualizing the saturated L identifies the projected image in `T O(3)` with `Wp O(3-e)`. Its rank-one kernel contains saturated J and therefore equals J. The extension splits because `H1(O(n+e-3))=0`. Thus

    A:=E/K=O(n-2)+Wp O(1-e).                             (4)

This argument identifies actual image sheaves, not merely their saturations.

## 3. A uniform second-image saturation bound

Let C be the actual rank-three image of `beta_K:K->A(-2)`. Its cokernel is torsion of invariant length delta, so

    K/K2=C, deg C=deg A-6-delta, delta>=0.

Since `deg A=n-2e`, Riemann--Roch gives

    chi(K2(4))=7-2n+4e+delta.                            (5)

The next derivative has target C(2), which injects into A. Persistence (1) therefore gives

    chi(K2(4)) <= h0(K2(4)) <= h0(C(2)) <= h0(A)=n-1.

Consequently

    delta <= 3n-4e-8.                                   (6)

For e=2, the upper bounds are two and eight, so delta=0. For e=4,n=6 the upper bound is negative, so that case is impossible. For e=4,n=8 the upper bound is zero, so delta=0. Both e=6 cases have negative upper bound and are impossible.

Whenever delta=0, `C=A(-2)`, so equivariant K-theory fixes the next Euler character. All three E types give the same characters:

    (n,e)=(6,2): chi_G(K2(4))=V;
    (n,e)=(8,4): chi_G(K2(4))=-A3+2V+P;
    (n,e)=(8,2): chi_G(K2(4))=-A3+V+P-D.                 (7)

Here A3 denotes the three-dimensional irreducible called A in the frozen notes, not the quotient bundle (4).

The next target is `C(2)=A`. Its section module is D when n=6 and V+P when n=8. In the first case (7) forces a V absent from the target. In the second case it forces two V copies while the target has one. Both contradict (1), irrespective of any H1. Only `(n,e)=(8,2)` remains.

## 4. The remaining kernel has exactly two formal shapes

For `(n,e)=(8,2)` the two exact quotients are

    E/K=O(6)+Wp O(-1), K/K2=O(4)+Wp O(-3).

In addition to the final line of (7), exact character arithmetic gives

    chi_G(K2(3))=-(Wp+S+T).                              (8)

Write `K2=U O(-4)+sum_{j>=5} R_j O(-j)`. This exhausts its splitting by (1). The degree-four coefficient U is center-even, with no positivity assumption beyond being a representation. Since H0(K2(3))=0, (8) gives the positive identity

    sum_{j>=5} R_j Sym^(j-5) W = Wp+S+T.                (9)

Its dimension bounds each block by `(j-4) dim R_j<=12`, hence j<=16. Checking all nine irreducibles and central parity leaves the following eligible individual blocks `(j,R_j)`:

    (5,Wp),(5,S),(5,T),(6,V),(6,P),(6,D),(7,Wp),
    (8,1),(8,V),(9,W),(9,Wp),(10,1),(12,1),(14,1).

An exhaustive nonnegative-character recursion for (9), followed by

    U=-A3+V+P-D+sum_{j>=6} R_j Sym^(j-6) W,

and the rank condition `dim U+sum dim R_j=11`, leaves exactly

    K2=(V+P) O(-4)+Wp O(-5)+Htail,
    Htail=O(-8)+O(-10) or W O(-9).                       (10)

This is finite universal representation arithmetic, not a map or model experiment. The companion verifier reproduces the complete recursion and checks both shapes, rather than assuming realizability.

## 5. The rank-one endpoint obstruction

For (10), the next derivative twisted by four has the form

    (V+P) O + Wp O(-1)+Htail(4) -> O(6)+Wp O(-1).

Its section map is injective by (1); both section modules equal V+P. It is thus complete evaluation onto O(6). The only possible map to the Wp O(-1) target comes from the displayed Wp O(-1) summand: all tail Hom spaces vanish. Generic rank three forces its scalar to be an isomorphism. Therefore

    F0=T O(-5)+Htail, K2/F0=O(2)+Wp O(-5).              (11)

Every Hom from F0 to Wp O(-7) vanishes. Its derivative therefore has rank at most one. Rank zero would make F0 constant, impossible because F0 lies in E and E contains no nonzero constant subbundle. Thus F0 has rank-one derivative, rank eight, and degree -48.

Apply the frozen rank-one flag theorem inside F0's own smallest constant span, of dimension 8+s. Its forward transforms lie in the original F_j, so s>=5. The rank-one degree bound gives s<=6. Since H0(F0(5)) contains T, section persistence inside this rank-one flag gives s<=5, hence s=5. The invariant ramification identity then requires

    104=(8+5)(48-8*5)
       in <96,160,240,60,100,150>.

This is impossible. This is precisely the endpoint argument proved in Section 2.2 of `SIX-LARGE-QUADRATIC-MODULES-EXCLUDED-BY-BACKWARD-GAUSS.md`. It excludes the final b=2 branch.

## 6. The rank-one cubic-image branch for X

Only X admits b=1. The line image is necessarily O(11); it is the highest ordinary-degree summand in E*(1), hence saturated. Duality gives a quotient of I onto O(-8). Let C0 be its rank-two kernel. Since C0 injects into Q, `c:=deg C0<=14`. Consequently

    deg(E/K)=c-14, deg K=-40-c>=-54.                     (12)

The corresponding quotient of E is O(-10). Only E's O(-10) summand can map to it; its scalar must be an isomorphism. Hence

    K embeds in E'=P O(-2)+2T O(-3).                     (13)

The next derivative has target `(E/K)(-2)`, which has a line quotient O(-12). Its rank three forces a nonzero composite `K->O(-12)`.

We show that this is impossible using only (12), (13), and (1). Every ordinary degree of K is at most -3. Define its degree excess over `14 O(-3)` as

    q=-deg K-42<=12.

Any summand contributing to `Hom(K,O(-12))` has degree at most -12. A coefficient block of dimension at least two would alone contribute at least 18 to q. Thus it must be an equivariant line. Central parity and q<=12 leave only O(-12) or O(-14).

After removing O(-14), the remaining rank thirteen has excess at most one. Parity forces a degree-even block, hence a line O(-4). But `Hom_G(O(-4),E')=0`.

After removing O(-12), the remaining rank thirteen has excess at most three. A degree -5 odd-coefficient block has dimension at least two and excess at least four, so cannot occur. The possibilities are:

- a line O(-6), forbidden by `Hom_G(O(-6),E')=0`;
- a line O(-4), likewise forbidden;
- a rank-three coefficient block at degree -4, with all remaining ten dimensions at degree -3.

The final possibility would give a ten-dimensional subrepresentation of

    H0(E'(3))=Wp+3T.

There is none: a subrepresentation has dimension `2a+6b` with a=0 or1 and b=0,1,2,3, never ten. This exhausts all possibilities, so `Hom(K,O(-12))=0`, the required contradiction. It does not depend on whether a=1 or2.

Every zero-pairing branch for X,Y,Z has now been excluded.

## Verification

Run `python3 verify_p4_zero_pairing.py`. It checks the three type tuples, every small-image and saturation list, the uniform torsion bounds, all Euler characters, the exhaustive two-shape K2 recursion, the endpoint Hom vanishings and semigroup obstruction, and the final rank-one-image degree argument. It reads and runs earlier verifiers unchanged. All arithmetic is universal; the geometric steps are proved above.
