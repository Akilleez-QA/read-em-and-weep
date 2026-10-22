# Three P4 quadratic types are excluded by backward Gauss persistence

## Result and scope

For the hypothetical generic-SF-rank-three plateau `(k,l)=(3,2)`, all three remaining formal primal types with quadratic section module `R=P4` are impossible:

    X = P O(-2) + 2T O(-3) + O(-10),
    Y = P O(-2) + T O(-3) + (V+P) O(-4),
    Z = P O(-2) + (Wp+T) O(-3) + V O(-4) + Wp O(-5).

Their eight-variable tuples are, respectively,

    X: (0,2,0,0,0,0,0,1),
    Y: (0,1,1,1,0,0,0,0),
    Z: (1,1,1,0,1,0,0,0).

They are disjoint from all twelve frozen exclusions, so at most 13 of the original 28 formal primal types remain. This note proves the nonzero-cubic-pairing branch. The independent companion `P4-ZERO-PAIRING-EXCLUDED-BY-BACKWARD-PERSISTENCE.md` proves the zero-pairing branch for the same three types. Both branches are required for the stated theorem.

Only universal equivariant representations, bundle splittings, images and saturation, complete evaluation, degree bounds, and backward persistence are used. No actual HM/source coefficients, actual matrices or map/rank evaluations, parameter scans, model experiments, or positive-operator computations are used. The established bounds remain generic SF rank at least three and square rank at least 27; the entire adjacent profile and smoothing closure are not proved.

## 1. Frozen input

Use `SINGLE-V-QUADRATIC-TYPE-EXCLUDED-BY-BACKWARD-EVALUATION.md`, `SIX-LARGE-QUADRATIC-MODULES-EXCLUDED-BY-BACKWARD-GAUSS.md`, and their cited frozen inputs. Write `P=P4`, `Wp=Wprime`, `S=S4`, `D=D5`, and `T=T6`; let `A=Sym^2 W` denote the standard even three-space, distinct from V.

The saturated plateau is

    F0 < K2 < K < E < F4 < F5,

of ranks `8,11,14,17,20,23`, with

    H0(K(2))=0, H0(K2(3))=0, H0(F0(4))=0.                 (1)

The derivatives of K and K2 have rank three. The five possible Q bundles have maximum ordinary degree at most eight, and the canonical cubic evaluation in Q* is `T O(-3)`. Every positive invariant torsion/divisor length is at least 12; more precisely it lies in `<12,20,30>`.

The restricted derivatives and their cubic pairing are

    phi: P O -> Q,    psi: T O -> E*(1),
    B: P O -> T O(3).

Both restricted derivatives are injective on sections. Put `a=rank(phi)`, `b=rank(psi)`, and `t=rank(B)`. Then `a+b-3<=t<=min(a,b)`. The frozen cubic-pairing theorem says that B is zero or has saturated image `Wp O(1)`.

Assume from now through Section 6 that B is nonzero. Its image has section module P, so the surjection `P O -> Wp O(1)` is complete evaluation, with kernel `Wp O(-1)`. Its dual projection, twisted by three, has saturated image `Wp O(2)` in `P O(3)`. In particular a and b are at least two, and only `(a,b)=(2,2),(2,3),(3,2)` are possible.

## 2. The rank-three cubic derivative is impossible

Suppose b=3. Let `L=im psi`, a globally generated equivariant rank-three bundle inside E*(1). Its projection to the quadratic summand `P O(3)` is exactly the rank-two bundle `Wp O(2)`.

The complete necessary list of individual globally generated image blocks of rank at most three, using both the source T and the target E*(1), is:

    X: V O(1), Wp O(2), V O(3), Wp O(4), V O(5),
       A O(9), W O(10), O(11);
    Y: V O(1), Wp O(2), V O(3), Wp O(4), V O(5);
    Z: V O(1), Wp O(2), V O(3), Wp O(4), V O(5), Wp O(6).

This is an overlist, not an assertion that its blocks occur. There are no one-dimensional coefficient representations besides the trivial one. A rank-three irreducible block in this list has no map to `Wp O(2)`: for `V O(1)` the Hom space is `Hom(V,Wp tensor W)=Hom(V,P)=0`, and the others fail by degree. The only remaining rank-three direct sum with a rank-two projection is

    L=O(11)+Wp O(2),                                    (2)

and only X admits it. Its projection identifies the Wp block with the saturated `Wp O(2)` in `P O(3)`; its kernel O(11) is the unique highest line of E*(1). Thus L is saturated in E*(1). Since it has full derivative rank three, it equals `(E/K)*(1)`, and

    E/K=O(-10)+Wp O(-1).

The O(-10) quotient cancels X's unique O(-10) summand. The P block maps to `Wp O(-1)` by complete evaluation, with kernel `Wp O(-3)`; extending by the remaining `2T O(-3)` splits. Hence

    K=(Wp+2T) O(-3).

The next derivative twisted by three has target `O(-9)+Wp O`, whose sections are only Wp. Its section source is Wp+2T. This contradicts `H0(K2(3))=0`, proving b=2.

## 3. Determine the first quotient by one line degree

Because b=2 and B is nonzero, the same image-block list and the rank-two projection show that

    im psi=Wp O(2).

The projection onto its saturated copy in `P O(3)` is an isomorphism, so this image is saturated in E*(1), regardless of X's high O(11) summand.

Let `I=im[beta_E(2):E(2)->Q]`. Its projection to `T O(3)` is `Wp O(1)`, and its kernel is an equivariant line N. Write `N=O(n)`; n is even and n<=8 because N embeds in Q. Thus

    0 -> O(n) -> I -> Wp O(1) -> 0.                     (3)

If a=2, the image of phi projects isomorphically onto `Wp O(1)`, so it supplies a section of (3). Relative to that splitting, the quadratic P block maps entirely onto `Wp O(1)`. Writing `E=P O(-2)+H`, the high part H must therefore surject onto `O(n-2)`. Global generation after the largest negative twist of H gives the finite lower bound on n, and the exact Hom calculation gives

    X: n=-8,4,6,8;
    Y: n=4,6,8;
    Z: n=4,6,8.                                        (4)

If a=3, the evaluation kernel `Wp O(-1)` of B has a nonzero map to N. Among even n<=8, the first and only possible value is n=6, since `Wp` occurs in `Sym^(n+1) W` precisely at n=6 in that range. Then (3) splits by `H1(O(n-1))=0`.

In every case we have the exact quotient

    A_n:=E/K=O(n-2)+Wp O(-1),                           (5)

with n among the values in (4). No saturation of I in Q has been presumed.

## 4. A uniform backward degree argument removes all but n=8

The next derivative has generic rank three and image

    C=K/K2 subset A_n(-2).

Let delta be the length of its torsion cokernel. Its determinant is equivariant, so delta is either zero or at least 12. Exact degree arithmetic gives

    deg K2 = -54-deg A_n-deg C = -40-2n+delta,
    chi(K2(4)) = 15-2n+delta.                            (6)

The derivative of K2 twisted by four maps to `C(2) subset A_n`, and its kernel F0(4) has no sections. Therefore

    15-2n+delta <= h0(K2(4)) <= h0(A_n).                 (7)

For n=-8 the right side is zero and the left side is at least 31; for n=4 the right side is three and the left side is at least seven. Both are impossible.

For n=6 and n=8, the right sides are five and seven. Inequality (7) bounds delta by two and eight, respectively. The invariant-divisor gap forces delta=0 in both cases, so the second quotient is exactly `A_n(-2)`.

For n=6, equivariant K-theory now gives

    chi_G(K2(4))=V,
    H0(A_6)=D.

Thus H0(K2(4)) contains V but its derivative target does not, again contradicting `H0(F0(4))=0`.

Only n=8 remains, with both exact quotients fixed:

    E/K=O(6)+Wp O(-1),
    K/K2=O(4)+Wp O(-3).                                 (8)

## 5. Exact characters force just two second-kernel shapes

Subtracting (8) from any of X,Y,Z gives

    chi_G(K2(3))=-(Wp+S+T),
    chi_G(K2(4))=-A+V+P-D.                              (9)

By (1), every ordinary summand of K2 has degree at most -4. Write

    K2=U O(-4)+sum_(j>=5) R_j O(-j).

Its first character identity and equivariant Serre duality imply

    sum_(j>=5) R_j tensor Sym^(j-5) W = Wp+S+T.          (10)

Each nonzero block satisfies `(j-4) dim R_j<=12`, making the following complete list finite. The eligible individual blocks `(j,R)` and their contribution to (10) are:

    (5,Wp): Wp;          (5,S): S;         (5,T): T;
    (6,V): T;           (6,P): Wp+T;      (6,D): S+T;
    (7,Wp): T;          (8,1): S;         (8,V): Wp+S+T;
    (9,W): S+T;         (9,Wp): S+T;      (10,1): T;
    (12,1): Wp+T;       (14,1): S+T.

For any nonnegative combination matching (10), the second identity in (9) determines

    U=-A+V+P-D+sum_(j>=6) R_j tensor Sym^(j-6) W.        (11)

U must be a genuine representation. Exhaustively matching the three nonnegative multiplicities in (10) and retaining only genuine U in (11) gives precisely

    K2=(V+P) O(-4)+Wp O(-5)+W O(-9),                    (12a)
    K2=(V+P) O(-4)+Wp O(-5)+O(-8)+O(-10).               (12b)

The companion verifier checks every parity-compatible irreducible through the dimension bound, rather than just testing a proposed list, and then performs the full positive multiplicity recursion. Thus (12) is a complete formal-splitting consequence of the exact characters; no geometric realizability or untested map rank is inferred from the enumeration.

## 6. The common rank-one endpoint obstruction

For completeness, the frozen endpoint argument applies verbatim to both (12). Put `Htail=W O(-9)` or `O(-8)+O(-10)`. The next derivative is

    (V+P) O+Wp O(-1)+Htail(4) -> O(6)+Wp O(-1).         (13)

Persistence makes the map on sections injective. Both section modules are V+P, so its constant block is complete evaluation of O(6), hence surjective. Only the displayed Wp O(-1) block can map to the Wp O(-1) target: the constant block fails by degree, and the tail Hom spaces vanish. Rank three forces the scalar map on that block to be an isomorphism. Consequently

    F0=T O(-5)+Htail,
    K2/F0=O(2)+Wp O(-5),
    rank F0=8, deg F0=-48.                              (14)

All Hom spaces `F0 -> Wp O(-7)` vanish, so the derivative of F0, with target `O+Wp O(-7)`, has rank at most one. It cannot have rank zero, since F0 is a positive-rank subbundle of E and no nonzero constant subbundle lies there. Hence its rank is exactly one.

Let its smallest constant span have dimension `8+s`. Its rank-one forward transforms lie in the successive F_i, so s>=5: otherwise that constant span would occur in an interior plateau stage. The rank-one degree theorem gives `48>=8s`, hence s<=6. Since H0(F0(5)) contains T, section persistence in the rank-one flag inside its own constant span gives s<=5. Thus s=5.

The exact rank-one degree formula with invariant ramification now requires

    (8+5)(48-8*5)=104
      in <12*8,20*8,30*8,12*5,20*5,30*5>
       = <96,160,240,60,100,150>.

It is not: the only positive generators at most 104 are 60,96,100, and no nonnegative combination equals 104. This excludes (12), closes n=8, and finishes the nonzero-pairing branch for all three P types.

## 7. Reproduction and limits

Run `python3 verify_three_p4_backward_gauss.py`; it also runs `verify_p4_zero_pairing.py`. The combined verifier runs all preceding frozen exclusions, verifies the nonzero-pairing Hom lists, first-quotient degrees, uniform second-image colength bound, exact second-kernel classification, endpoint evaluation identities and semigroup obstruction, and the new remaining count. The zero-pairing companion may also be run separately.

The resulting count is at most 13 of 28 formal primal types, not a realization count. Neither a full `(3,2)` exclusion nor an improvement of SF rank three, square rank 27, or the smoothing endpoint has been proved.
