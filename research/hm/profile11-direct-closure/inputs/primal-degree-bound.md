# The primal quotient has degree at least minus four

## Result

Assume that the actual positive double-hyperplane second fundamental form has generic rank three. Write K=E^-, A=E/K and a=deg A. Then

    a >= -4.

This strengthens the previous a>=-8 bound. It applies to any maximal rank-three profile, not only (1,2).

For the (1,2) profile, the proved bound b=deg B>=-12 now implies that the original transpose injection A -> B*(-2) has no determinant torsion. Therefore

    A = B*(-2),   -4<=a<=6,   b=-6-a.

In particular the entire original twelve-defect branch is excluded. The second dual derivative is a different map; its torsion is not automatically zero. The (1,2) profile itself and the original research goal remain open.

## 1. Exact geometric inputs and two character envelopes

Use these results at the immutable commit bcb820f06b0d3df35c96f928360f1e973e552c65:

- [Asymmetric degree bounds](https://github.com/Akilleez-QA/read-em-and-weep/blob/bcb820f06b0d3df35c96f928360f1e973e552c65/research/hm/order-four-quadratic-load/ONE-TWO-ASYMMETRIC-QUOTIENT-DEGREE-AND-DEFECT-BOUNDS.md), especially Section 2, whose primal a>=-8 argument does not require the (1,2) profile.
- [Actual equivariant presentations](https://github.com/Akilleez-QA/read-em-and-weep/blob/bcb820f06b0d3df35c96f928360f1e973e552c65/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md).
- [Strict top-slope decrease](https://github.com/Akilleez-QA/read-em-and-weep/blob/bcb820f06b0d3df35c96f928360f1e973e552c65/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md).

The actual bundle E has rank 17, degree -54 and all summand degrees between -10 and -2. Thus K has rank 14, degree -54-a and top degree at most -3. The rank-three quotient A is center-even, every ordinary summand has degree at least -10, and a is even. The actual characters are

    chi(E(2))=-V,   chi(E(3))=W'+2T.

Here G is the binary icosahedral group, W is its standard two-space, W' the other two-space, A_std=Sym²W and V the inequivalent three-space, P the even four-space, S=Sym³W, D=Sym⁴W, T=Sym⁵W.

Since H0(K(2))=0, the exact quotient sequence implies that

    C2(A) := chi(A(2))+V = H1(K(2))

is genuine. Also K^- has top degree at most -4, independently of the rank of its derivative. The derivative of K factors through A(-2), so

    H0(K(3)) -> H0(A(1))

is injective. Hence

    C3(A) := H0(A(1))+chi(A(3))-(W'+2T)

is genuine: it is the sum of the cokernel character of that injection and H1(K(3)).
The dimensions also give

    h0(A(1)) >= chi(K(3)) = 2-a.

All these constraints hold for the actual derivative, without extending a plateau rank assertion to an endpoint.

## 2. Exclude degree minus eight by six explicit possibilities

A rank-three center-even equivariant splitting consists of three even-degree trivial lines, one odd-degree W or W' block plus an even-degree line, or a single even-degree A_std or V block. This is exhaustive because G has no other irreducibles of dimension at most three and no nontrivial one-dimensional characters.

At a=-8, each ordinary degree is at least -10 and h0(A(1))>=10. These facts leave exactly:

    O(-10)+O(-6)+O(8),
    2O(-8)+O(8),
    O(-10)+O(-8)+O(10),
    2O(-10)+O(12),
    W O(-9)+O(10),
    W' O(-9)+O(10).

For example, with three even line degrees x<=y<=z, two nonnegative entries would give h0(A(1))<=6. Thus only z contributes, z>=8, and x+y>=-20 gives z<=12. The four line triples above follow. The two-space cases give exactly the last two entries; the three-space case cannot have total degree -8.

Their C3 characters, in the same order, are

    -W'+2S-T,
    W-W',
    2W+S-T,
    W+2S-T,
    2W+S-T,
    2W+S-T.

Every one has a negative irreducible multiplicity. Thus a=-8 is impossible.

## 3. At degree minus six, a positive degree-twelve line is forced

Now a=-6 and h0(A(1))>=8. The same elementary degree/parity analysis leaves fifteen possibilities.
For three lines, their even degrees lie in [-10,14], sum to -6 and satisfy the dimension bound; this gives eleven triples.
For a two-space plus a line, the only possibilities are R O(-9)+O(12) and R O(-7)+O(8), for R=W,W'. A single three-space O(-2) has no sections at twist one and is impossible.

The two character envelopes above eliminate twelve entries. The table lists one negative multiplicity certificate for each excluded case; “C2:P” means that the P coefficient of C2 is negative.

    (-10,-10,14): C2:P
    (-10,-6,10): C3:T
    (-10,-4,8): C2:1
    (-10,-2,6): C3:T
    (-10,0,4): C3:T
    (-10,2,2): C2:P
    (-8,-8,10): C2:D
    (-8,-6,8): C3:W'
    (-8,-4,6): C2:1
    (-6,-6,6): C2:A_std
    W O(-7)+O(8): C3:W'
    W' O(-7)+O(8): C3:W'.

The remaining necessary types are exactly

    O(-10)+O(-8)+O(12),
    W O(-9)+O(12),
    W' O(-9)+O(12).

In particular each contains an equivariant O(12) summand. We do not assert that any of these quotient bundles is realizable.

## 4. Invariant multiplication forbids the required positive line

The actual presentation yields

    H1(Q*) = M2 = A_std+2V+3P+4D,

which has no trivial summand. Equivariant Serre duality on P(W) gives

    H0(Q(-2))^G = 0.

There is a nonzero invariant binary form f12 of degree twelve, since

    Sym^12 W = 1+A_std+P+D.

Equivalently, the twelve-point icosahedral orbit defines a degree-twelve invariant divisor. Its one-dimensional space of defining sections is stable under G, and perfectness of G makes its character trivial, supplying f12 without a coordinate choice.

Multiplication by f12 is injective on the locally free sheaf Q(-14), even though f12 has zeros. It therefore induces an injection

    H0(Q(-14))^G -> H0(Q(-2))^G = 0.

Consequently

    Hom_G(Q*,O(-14)) = H0(Q(-14))^G = 0.

This proof uses no proposed splitting of Q*. More generally, if a locally free G-bundle F satisfies H0(F(-2))^G=0, every positive degree d admitting a nonzero invariant binary form has H0(F(-d-2))^G=0. The invariant multiplier is a non-zero-divisor on a vector bundle; no nowhere-vanishing assertion is needed.

As an independent arithmetic cross-check only, the verifier also uses H1(Q*)=M2 to bound a hypothetical block R O(-j) mapping to O(-14). It must have j>=14, central parity (-1)^j and (j-1)dim R<=41. The complete conservative single-block list is O(-16), W O(-17), O(-18), W O(-19), O(-20), O(-28), O(-30); all seven have zero G-Hom to O(-14). This list does not assert realizability and is not needed for the invariant-multiplier proof.

## 5. Transpose incidence excludes degree minus six

For the actual derivative, let L=(Q*)^- and B=Q*/L. Negative transpose gives the injective rank-three map A -> B*(-2); dualizing the quotient Q* -> B embeds B* into Q. Thus there is a sheaf injection

    A -> B*(-2) -> Q(-2).

If a=-6, the O(12) summand forced in Section 3 gives a nonzero equivariant map O(12)->Q(-2), equivalently a nonzero map Q*->O(-14). This contradicts Section 4. Hence a=-6 is impossible.

Together with a>=-8 and even parity this proves a>=-4.

## 6. Eliminate the asymmetric twelve-defect branch

In profile (1,2), the established second-dual-interior argument gives b>=-12. The original transpose determinant has length

    t=-6-a-b >=0.

The new bound gives t<=10. Its divisor is invariant under the projective icosahedral action, whose smallest nonempty orbit has twelve points. Therefore t=0. The equal-rank sheaf injection is an isomorphism, A=B*(-2). The remaining degree interval follows immediately.

This does not erase the separate determinant defect of L/L^- -> B(-2). Its previous bound s<=2b+26 remains a bound on a different map.

## 7. The remaining second-dual defect is sharply bounded

Let s be the determinant length of J=L/L^- -> B(-2), and M=L^- as above. Substituting b=-6-a into the established bound gives

    0<=s<=14-2a,   deg M=-36+2a+s.

An invariant effective divisor of degree at most 22 has degree 0, 12 or 20: the projective icosahedral orbit lengths are 12,20,30,60, and two copies of the smallest orbit already have degree 24. Thus the full necessary degree table is

    a=-4, b=-2: s=0,12,20; deg M=-44,-32,-24.
    a=-2, b=-4: s=0,12;    deg M=-40,-28.
    a= 0, b=-6: s=0,12;    deg M=-36,-24.
    a= 2, b=-8: s=0;       deg M=-32.
    a= 4, b=-10: s=0;      deg M=-28.
    a= 6, b=-12: s=0;      deg M=-24.

In particular J=B(-2) at a=2,4,6. At a=-4 the twenty-point divisor must not be discarded. This is only a necessary list, not a realizability claim.

## Reproduction and status

Run python3 verify.py. The self-contained test uses exact binary-icosahedral character arithmetic in Q(sqrt(5)). It checks the six and fifteen elementary quotient candidates, every stated certificate, the complete conservative dual-block envelope (j<=42), the invariant degree-twelve multiplicity, and all seven optional Hom vanishings. It performs no actual-instance coefficient, point, matrix or rank evaluation and no rank scan. The injection, saturation, parity and invariant-divisor arguments are supplied above; a character test alone would not prove them.

