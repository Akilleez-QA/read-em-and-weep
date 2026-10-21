# The twist-four common-value space has dimension exactly forty-five

## Statement and scope

For a general ambient quadric, let Y in |2H| be the smooth genus-46 curve on the modular surface S=S(5). With H=I+2F, define A4=O_Y(12F-H). Then

    h0(Y,A4)=45,    h1(Y,A4)=0.

This is a geometric open-condition argument, not a selected-coefficient or numerical rank test. It supplies the exact source dimension for the still unresolved actual twist-four connecting map.

## Primary geometric input

Aure–Decker–Hulek–Popescu–Ranestad, Syzygies of Abelian and Bielliptic Surfaces in P4, Proposition 4.2(iv)–(v), states that the degree-fifteen image S15 is smooth away from thirty points, its normalization is S(5), and each of the twenty-five five-torsion sections maps one-to-one to its corresponding HM line. Section 4.7 identifies the hyperplane class H=I+2F. Source: https://arxiv.org/pdf/alg-geom/9606013 .

Consequently the normalization morphism is finite and birational. Over the general point of a fixed HM line its inverse image is precisely the corresponding section C. No other curve maps to that line, and no curve is contracted; possible additional inverse images over exceptional points are finite. We use C²=-5, H.C=1, F.C=1, H²=15, H.F=5, and K_S=3F.

## A reducible divisor that detects nontriviality

Set N=O_S(3H-9F). It has degree zero on every divisor of class 2H. Consider the linear system of ambient quadrics containing the fixed HM line. Its pullback to S has fixed divisor exactly C, with multiplicity one:

- The ambient base scheme is the line, so finiteness of normalization gives no other fixed curve.
- Near the general point of C, the normalization is an isomorphism onto the smooth surface S15. The linear forms vanishing on the line generate the ideal of C there. Their products with linear forms nonzero at that point show that the generic vanishing order is one.

After removing C, the residual system has no fixed divisor, although isolated basepoints are allowed. Its rational map is birational onto a surface: away from the line, choose a linear form ell vanishing on the line but nonzero at the point. The five quadrics ell*x_i recover the original ambient coordinates by their ratios. Since the normalization is birational, these ratios recover the general point of S. Resolve the isolated base ideal, then apply Bertini irreducibility and generic reducedness in characteristic zero. A general residual divisor R is therefore reduced and integral. In particular a general quadric through the line pulls back to the Cartier divisor

    Y0=C+R,    R in |2H-C|,

with no common component between C and R.

The relevant degrees are

    deg N|C = 3-9 = -6,
    C.R = 2H.C-C² = 7,
    deg N|R = 6,
    deg O_R(N-C) = -1.

The divisor sequence on the smooth surface gives

    0 -> O_R(N-C) -> O_{Y0}(N) -> O_C(N) -> 0.

Both outer sheaves have no global sections: C is integral and the indicated degrees are negative, and R is reduced integral. Hence H0(Y0,N)=0.

The universal nonzero quadric divisor on S is a flat Cartier family. Upper semicontinuity now gives H0(Y,N)=0 on a nonempty open set of ambient quadrics, intersecting the existing common open conditions. Adjunction gives omega_Y=O_Y(2H+3F), so omega_Y tensor A4^{-1}=N|Y. Thus h1(A4)=0. Since deg A4=90 and g(Y)=46, Riemann–Roch gives h0(A4)=45.

The proof does not infer anything about injectivity of the actual forty-five-to-eighty-five connecting map.
