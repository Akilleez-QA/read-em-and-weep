# Three V+P4 profiles excluded by backward Gauss persistence

## Result and scope

Each of the three remaining formal primal profiles with quadratic section module R=V+P4 is impossible in the hypothetical (k,l)=(3,2) plateau:

    X: (0,1,1,0,0,0,0,1),
       E=(V+P)O(-2)+T O(-3)+V O(-4)+O(-10);
    Y: (0,0,2,1,0,0,0,0),
       E=(V+P)O(-2)+(2V+P)O(-4);
    Z: (1,0,2,0,1,0,0,0),
       E=(V+P)O(-2)+Wp O(-3)+2V O(-4)+Wp O(-5).

Here P=P4, Wp=Wprime, T=T6, D=D5, and A=Sym^2 W is the other even three-dimensional irreducible. Starting with the verified five-type remainder in `FOUR-MIXED-P4-D5-TYPES-EXCLUDED-BY-OCTIC-EVALUATION.md`, these exclusions alone leave two of 28. The separate V+D5 and R=0 directions are not claimed here. No full plateau exclusion or smoothing closure is claimed; the established SF-rank bound three and square-rank bound 27 are unchanged.

The argument and verifier use only universal representation arithmetic, hypothetical equivariant splitting types, exact images, degrees and persistence. They use no actual HM coefficients, selected actual points, source-instance matrices or rank tests, scans, model spikes or consumed experiments. Frozen files are read and executed unchanged.

## 1. Frozen input and common backward estimate

Use the octic-evaluation note above, `THREE-P4-QUADRATIC-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md`, `P4-ZERO-PAIRING-EXCLUDED-BY-BACKWARD-PERSISTENCE.md`, and their frozen dependencies.

The saturated plateau F0<K2<K<E<F4<F5 has ranks 8,11,14,17,20,23. Its two interior backward derivatives have rank three, deg E=-54, and

    H0(K(2))=0, H0(K2(3))=0, H0(F0(4))=0.

Every positive invariant torsion length is at least twelve. Every possible Q has maximum degree at most eight and largest-two-degree sum at most fourteen. Define

    phi:R O -> Q, psi:T O -> E*(1), B:R O -> T O(3).

The first two maps are injective on sections. Their ranks a,b and the pairing rank t obey a+b-3<=t<=min(a,b). The frozen pairing theorem says B is zero or has saturated image Wp O(1), with section module P.

Put A0=E/K and C=K/K2. The actual image C embeds in A0(-2) with invariant torsion colength delta. Consequently

    deg K2=-54-2 deg A0+6+delta,
    chi(K2(4))=7-2 deg A0+delta,
    H0(K2(4)) -> H0(C(2)) -> H0(A0) is injective.       (1)

No saturation of C is assumed in this estimate.

## 2. Nonzero cubic pairing is impossible

Suppose B is nonzero. It kills the V section summand of R. If a=2, the rank-two image of phi projects onto the rank-two image of B with zero kernel (a rank-zero subsheaf of a bundle vanishes). Thus V also maps to zero under phi, contrary to injectivity on sections. Therefore a=3. Since t=2, the rank inequality forces b=2.

The projection of im psi onto the quadratic summand R O(3) is the saturated Wp O(2) supplied by dual complete evaluation of B. The projection from im psi onto this rank-two bundle is surjective and has rank-zero torsion-free kernel, hence is an isomorphism. In particular im psi is a graph over a subbundle and is saturated in E*(1).

Let I be the actual full derivative image in Q. Its projection onto T O(3) is Wp O(1), so

    0 -> O(n) -> I -> Wp O(1) -> 0.

The line kernel contains the nonzero V section image of phi. Its degree is even and at most eight. Among those degrees, Sym^n W contains V only for n=6. The extension splits because H1(O(5))=0. Hence

    A0=O(4)+Wp O(-1).                                  (2)

Now (1) gives 3+delta<=5. The invariant torsion gap forces delta=0. Exact equivariant K-theory, identically for X,Y,Z, gives

    chi_G(K2(4))=V,   H0(A0)=D.

Thus H0(K2(4)) contains V, while its injection target does not. This contradiction proves B=0.

## 3. Zero pairing with b=2 is impossible

Since a,b are positive and a+b<=3, b=2 forces a=1. The actual quadratic image is a globally generated even-degree line O(n), n<=8, whose sections contain R. The unique possibility is n=6, because Sym^6 W=V+P. Its section map is an isomorphism and its bundle map is complete evaluation. It is saturated in Q: its possible defect is at most two, smaller than twelve.

Let L=im psi, let Lbar be its saturation in E*(1), set m=deg Lbar, and let epsilon=deg Lbar-deg L. Every equivariant splitting block of L receives a nonzero map from T O. The exhaustive central-parity and character test says every ordinary degree is at least two; an eligible line has degree at least five. Thus deg L>=4. Also every ordinary degree of Lbar is at least two: otherwise every component map from L to a lower-degree summand of Lbar would vanish, contradicting generic rank two of the inclusion.

The actual projected dual image of the full derivative is Lbar*(3), not an unproved dual of L: factor psi through the subbundle Lbar, dualize its inclusion, and use that the generically surjective map T O->Lbar dualizes injectively. The rank-one kernel contains the saturated O(6) and therefore equals it. Twisting gives

    0 -> O(4) -> A0 -> Lbar*(1) -> 0.

The quotient has no sections, and H1(O(4))=0, so h0(A0)=5 and deg A0=6-m. Equation (1) gives

    2m-5+delta<=5, hence 4<=m<=5.

Since epsilon<=m-4<=1, the invariant torsion gap forces epsilon=0. Two eligible lines would have total degree at least ten, so L must be one irreducible rank-two block. Its degree is even, hence m=4, and the unique eligible block is Wp O(2). The extension splits, giving (2) again. Equation (1) forces delta<=2, hence delta=0, and the same V-versus-D contradiction excludes this branch.

Notice that this argument proves saturation from persistence. It does not use an invalid maximum-target-degree bound in the profile with a high O(11) line.

## 4. The only possible rank-one cubic image

It remains to consider b=1; a can be one or two. Exhaustive equivariant Hom tests for globally generated image lines receiving T show:

    X: only O(11); Y: none; Z: none.

Thus Y and Z are finished. For X, O(11) is its target's highest-degree line and is saturated. Duality produces the quotient O(-10) of A0. Only the displayed O(-10) summand of E can map to that line, and its scalar must be an isomorphism. Therefore

    K embeds in E'=(V+P)O(-2)+T O(-3)+V O(-4).           (3)

The rank-two kernel C0 of I->O(-8) embeds in Q. Write c=deg C0; the largest-two-degree bound gives c<=14. Therefore

    deg A0=c-14, deg K=-40-c>=-54.

Every ordinary degree of K is at most -3 by persistence. Its excess below fourteen degree-minus-three dimensions is

    q=-deg K-42<=12.                                   (4)

The next derivative K->A0(-2) has rank three. Since its target has quotient O(-12), its composite with that quotient is nonzero.

## 5. Exhaustive low-tail obstruction

A splitting block contributing to Hom(K,O(-12)) has degree at most -12. If its coefficient dimension were at least two, it would contribute at least eighteen to (4). Thus it is a line, with trivial coefficient because G has no nontrivial characters. Central parity and (4) leave only O(-12) or O(-14).

Remove O(-14). The remaining rank thirteen has excess at most one. Degree-minus-three blocks have odd central character and even dimension. Odd total rank therefore requires an even-degree block; the only available one within excess one is O(-4). But Hom_G(O(-4),E')=0, contradicting (3).

Remove O(-12). The remaining rank thirteen has excess at most three. A degree-minus-five block has dimension at least two and excess at least four, so cannot occur. Blocks of degree at most minus seven likewise exceed the budget. The possibilities with positive excess are lines O(-4), a line O(-6), or an even rank-three block at degree minus four. Both line Hom spaces into E' vanish. The even three-spaces are A and V; Hom_G(A O(-4),E')=0. Thus the only surviving necessary shape is

    O(-12)+V O(-4)+U O(-3), dim U=10.

Its injection into E' would inject U into

    H0(E'(3))=(V+P) tensor W + T = Wp+3T.

There is no ten-dimensional subrepresentation: the possible dimensions are 2a+6b for a=0,1 and b=0,1,2,3, never ten. This final contradiction exhausts b=1 and all three profiles.

## Reproduction

Run `python3 verify_three_v_p4_backward_gauss.py`. It executes the frozen five-remainder chain unchanged, verifies the three tuples, the complete eligible line lists, parity and degree bounds, the two Euler-character obstructions, all stated Hom vanishings, and an exhaustive nonnegative splitting recursion for the residual thirteen dimensions after each possible low tail. It independently leaves no residual shape. It records two surviving tuples after these three exclusions alone.
