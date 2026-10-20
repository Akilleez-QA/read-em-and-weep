> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Full-support Heisenberg Chern congruences

## Result

Let E be an H5-equivariant coherent sheaf on P(V)=P4, of rank n, with uniform central weight zeta^w. Use the convention that O(m) has central weight zeta^(-m). In A*(P4) tensor F5 one has

    ch(E) = n exp(-w h),
    c(E) = (1-w h)^n,

where each expression is truncated after h^4. In particular

    c_i(E) = binom(n,i)(-w)^i modulo 5,  1 <= i <= 4.

These formulas apply to coherent sheaves, not only vector bundles. The congruence for a rational Chern-character coefficient is in Z_(5), where the denominators 2, 6, and 24 are invertible.

For the remaining rank-seven branch of the established global-image problem they force exactly

    c2(F)=5,  c2(R)=4.

For the historical rank-ten branch with (k,d)=(7,5), already excluded by historical source quintic-normalizer-exclusion/PROOF.md (ancillary to the present rank-eight assembly), they give the conditional formulas

    c2(F) in {4,9,14,19,24,29,34,39,44},
    c2(R)=49-c2(F),
    ch2(F/G) in {-45/2,-35/2,-25/2,-15/2,-5/2,5/2,15/2,25/2,35/2} h^2.

These congruences alone do not exclude rank seven or rank ten. The additional degree-four surface argument in ../rank-seven-degree-four-surface-exclusion/PROOF.md excludes rank seven. The rank-ten k=7 formulas are historical conditional formulas, not a currently surviving branch.

## 1. Euler-polynomial restriction

The representation lemma of ../heisenberg-defect-hilbert-congruence/PROOF.md implies

    P(m):=chi(E(m)) = 0 modulo 5 if m is not w modulo 5.

An integer-valued polynomial of degree at most four has its coefficients in Z_(5): its integral binomial expansion has denominators dividing 24. Its leading coefficient is n/24. Therefore the reduction of P is the unique degree-at-most-four polynomial with those four roots and that leading coefficient:

    P(m) = (n/24)((m-w)^4-1) modulo 5.             (1)

This includes ranks divisible by five: in that case its leading coefficient vanishes, its remaining degree is at most three, and the four roots force the zero polynomial.

## 2. Riemann--Roch

Write ch(E)=n+a1 h+a2 h^2+a3 h^3+a4 h^4. The Todd class of P4 is

    td(P4)=1+(5/2)h+(35/12)h^2+(25/12)h^3+h^4.

Modulo five this becomes 1+h^4. Riemann--Roch thus says

    P(m)= n + n m^4/24 + a1 m^3/6 + a2 m^2/2 + a3 m + a4 modulo 5.

Comparing with (1) gives

    a1=-nw,  a2=nw^2/2,  a3=-nw^3/6,  a4=nw^4/24.

For the constant comparison, use 24=-1 modulo five: the constant in (1) is n(w^4-1)/24=n+nw^4/24. This proves the Chern-character formula. Newton identities through degree four use only denominators prime to five, so convert it to the asserted total-Chern-class formula.

As a useful consistency check, if n=0 all four character coefficients vanish modulo five. This recovers the proper-support Hilbert congruence and extends it to all Chern-character components of a proper-support uniform-weight sheaf.

## 3. Application to saturated image and quotient

Use the established sequence

    0 -> F -> J tensor O -> R -> 0,
    rank F=n=r+4,  rank R=20-n,
    c1(F)=-k h,  c1(R)=k h.

Both sheaves have central weight three, inherited from J. Consequently

    c2(F)=9 binom(n,2) modulo 5,
    c2(R)=9 binom(20-n,2) modulo 5.               (2)

The established positivity and zero-c2 splitting arguments in ../rank-nine-defect-two-sided/PROOF.md, applied with the current ranks as in historical source rank-ten-pure-divisorial-defect/PROOF.md (ancillary to the present rank-eight assembly), give strict positivity of both numbers. Indeed F* is reflexive and generated outside codimension two, R is globally generated and torsion-free, and a zero second Chern class would produce a nonzero proper invariant subspace in J or J*. Since c(F)c(R)=1,

    c2(F)+c2(R)=k^2.                            (3)

The determinant branches considered below, including the rank-seven refinement in ../rank-seven-cubic-plucker-obstruction/PROOF.md and the rank-nine kernel refinement, have these necessary values. Rank seven is subsequently excluded by the degree-four surface argument, and rank-ten k=7 is already excluded by the normalizer-quintic argument:

- r=4, n=8, k=4: (c2(F),c2(R)) is (2,14), (7,9), or (12,4).
- r=6, n=10, k=5: the pair is (5,20), (10,15), (15,10), or (20,5).
- r=7, n=11, k=3 (subsequently excluded): the pair is exactly (5,4).
- r=8, n=12, k=6: the pair is (4,32), (9,27), (14,22), (19,17), (24,12), (29,7), or (34,2).
- r=9, n=13, k=4: the pair is (2,14), (7,9), or (12,4), agreeing with the independently derived saturation-defect degrees 35,30,25 respectively.
- r=10, n=14, k=7 (historical, already excluded): c2(F) is one of 4,9,14,19,24,29,34,39,44, and c2(R)=49-c2(F).
- r=10, n=14, k=12: the already proved zero-defect branch has (69,75), consistent with (2).

The obsolete rank-ten k=2 possibility is also excluded immediately by (2) and strict positivity: c2(F) is at least four and c2(R), being positive and divisible by five, is at least five, while (3) would give sum four.

In the rank-ten k=7 case the existing identity c2(F)=43/2-t, with ch2(F/G)=t h^2, yields the nine-value list in the result.

## 4. Higher Chern classes do not immediately exclude rank seven

For n=11 and w=3 the total Chern congruence reduces, through degree four, to

    c(F)=1+2h modulo 5,
    c(R)=1+3h+4h^2+2h^3+h^4 modulo 5.

Thus c3(F) and c4(F) are divisible by five, while c3(R)=2 and c4(R)=1 modulo five. These restrictions are fully compatible with the exact-sequence identities and c1(F)=-3, c2(F)=5. More explicitly, if c3(F)=x and c4(F)=y, inversion gives

    c3(R)=-3-x,
    c4(R)=-29-6x-y.

For x=y=0 modulo five these have exactly the required residues. Hence the congruences and established strict second-Chern positivity alone do not eliminate the remaining rank-seven branch. No unsupported positivity assertion for higher Chern classes of singular sheaves is used.

## Evidence boundary

Only existing local proof texts, universal finite-group representation theory, Riemann--Roch, and small integer arithmetic were used. No actual HM source, operation matrix, product, selected input, rank instance, polynomial instance, jet, or residue was evaluated. The only write is this local proof deliverable.
