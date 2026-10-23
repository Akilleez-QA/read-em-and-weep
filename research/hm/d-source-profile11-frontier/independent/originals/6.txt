# Cubic-section rigidity excludes both low degree-two quotient shapes

## 1. The exact actual-source theorem

Work over C on the original fixed parameter line P(W*) with the physical binary-icosahedral action, all linearizations and determinant conventions unchanged. Let E be the actual saturated HM subbundle of the constant plane-section bundle H O, beta_E its second fundamental form, K=E^- its saturated kernel, and A_q=E/K its actual locally free derivative quotient.

Assume the exact D-type from the primary-terminal four-type theorem:

    E=D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8).           (1)

Neither of these actual quotient splittings is possible:

    A_split=O(-8)+O(4)+O(6),
    A_bal=O(-8)+W O(5).                            (2)

The theorem makes no assumption on the generic rank of beta_K and thus applies to every maximal-profile placement of these E/A pairs. It also makes no assumption on the determinant defect of A_q -> B_q^*(-2), its saturation, or the ordinary Birkhoff splitting being horizontal.

The mechanism is stronger than a rank bound: either quotient in (2) would force the actual derivative kernel

    K=(2V+2P)O(-4),                               (3)

whose top coefficient cannot inject into its actual derivative target. All rows from V O(-4) are retained throughout.

Seven complete immutable public inputs, authenticated in INPUTS.json, fix the actual ambient inclusion, strict-top lemma, character convention, primary four-type result and original row identities. PR1123 at 504b7eb800407dfc7e6340c98c72cdd553939f54 gives (1) as one of four necessary source types; PR1129 at d1238732f42df5c70ba4430e230428d2cf699bbe gives the general near-top coefficient visibility lemma. We use that lemma for explicitly saturated graph subbundles, not a canonical-pencil Gauss derivative. Their full URLs and paths are in the manifest.

Write A_std=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and W',V,P for the remaining 2,3,4 dimensional irreducibles. In particular

    W D=S+T; Sym6 W=V+P; Sym7 W=W'+T;
    Sym8 W=P+D; Sym9 W=S+T;
    Sym10 W=A_std+V+D.                            (4)

Every nonempty invariant effective divisor on P(W*) has degree at least 12: its projective A5 orbits have sizes 12,20,30 or60. This fact is used to prove saturation, never to presume it.

## 2. Cancel the negative scalar quotient, retaining the actual map

Choose an equivariant Birkhoff splitting of (1); no summand is assumed horizontal. Write

    E_hat=D O(-2)+(W'+T)O(-3)+V O(-4).

In the actual quotient map E -> A_q, projection onto O(-8) can receive a map only from the displayed O(-8) source, by degree. Surjectivity makes that scalar an isomorphism. Consequently K lies in E_hat and is exactly the kernel of an everywhere-surjective actual bundle map

    p:E_hat -> C,
    C=O(4)+O(6) or C=W O(5).                       (5)

The O(-8) source may also have positive rows; they do not alter this exact kernel statement. We have not discarded them to assert a horizontal decomposition.

The canonical top block F=D O(-2) has a nonzero p-row. Indeed strict-top on E gives an injection H0(E(2))=D -> H0(A_q(2)); the negative quotient has no sections. By irreducibility its induced five-dimensional section system is independent.

## 3. The D row and its cubic sections: split case

For C=O(4)+O(6), the D row into O(4) vanishes because D is absent from Sym6 W=V+P. Its O(6) row is nonzero. It is given by five independent sections of O(8). Their common zero divisor is invariant and has degree at most8, so the minimum 12 rules out any common zero. Hence

    D O(-2) -> O(6) is onto.

Let K_D be its kernel. Then rank K_D=4, deg K_D=-16, and H0(K_D(2))=0. Thus every degree of K_D is at most-3, so K_D(3) has nonpositive degrees and h0<=4.

The induced cubic-section map is

    D tensor W=S+T -> H0(O(9))=S+T.                (6)

Its T channel cannot vanish, since a six-dimensional kernel does not fit in H0(K_D(3)). Its S channel cannot vanish either: four independent kernel sections would force the rank-four nonpositive bundle K_D(3) to be trivial, contradicting deg K_D(3)=-4. Therefore (6) is an isomorphism. In particular, viewed inside H0(C(3)), the D row has section image S plus one T multiplicity line.

This argument does not evaluate either scalar channel. It proves each nonzero from the actual surjection and kernel degree.

## 4. The D row and its cubic sections: balanced case

Now let C=W O(5). First its nonzero D row has generic rank two.

If its image had rank one, it would be an equivariant line O(n). Since it injects into 2O(5), n<=5; since it is center-even and G has no nontrivial characters, n is even. The quotient D O(-2) -> O(n) makes O(n+2) globally generated and places D in Sym^(n+2) W. The only n in this range is n=2. But

    Hom_G(O(2),W O(5))=Hom_G(W,Sym3 W)=0,

so that line cannot inject into the target. Rank one is impossible.

Let I be the actual rank-two image. Then I(2) is globally generated and has at least five independent sections, supplied by D. Since H1(I(2))=0, Riemann–Roch gives

    deg I+6=h0(I(2))>=5.

The invariant torsion defect inside W O(5) is therefore

    0<=delta=10-deg I<=11.

The invariant minimum 12 forces delta=0, so the actual D row is onto W O(5). Its kernel K_D has rank3, degree-20, and H0(K_D(2))=0. Therefore K_D(3) is nonpositive of rank 3, and h0<=3.

The induced map on cubic sections is

    S+T -> H0(W O(8))=W'+S+2T.                    (7)

Neither S nor T can lie in the kernel, since their dimensions 4 and6 exceed3. Thus (7) is injective, with image S plus one T multiplicity line. Once again, this derives nonzero channels without choosing actual coefficients.

## 5. A graph argument forces the other cubic channels

For either C, its cubic sections are exactly

    H0(C(3))=W'+S+2T.                             (8)

The displayed W'(-3) block has nonzero derivative. If it were killed, its internal derivative would land in the complementary degrees at most-2, twisted by-2, so it would be a forbidden horizontal negative block, exactly the near-top lemma. Since (8) has a single W', its image fills that constituent.

The D cubic image already fills S and one T line. The displayed T(-3) source must give an independent T multiplicity line. Suppose otherwise. There is a one-dimensional space Hom_G(T(-3),D(-2)), because WD=S+T. Its composition into C is nonzero: this is exactly the nonzero T channel in (6) or (7). Thus any T-row lying in the D image factors through a unique morphism g:T(-3) -> D(-2).

Replace the displayed T(-3) by its graph under minus g. This is an actual equivariant triangular bundle change, giving a saturated direct graph subbundle T(-3) in E; no scalar is selected numerically. Its full derivative would now be zero, since the O(-8) quotient row is zero by degree and its C row has been canceled. The complementary quotient still has all degrees at most-2. Its internal derivative therefore vanishes by Hom(O(-3),O(-4))=0, making it horizontal and negative, impossible.

The two T multiplicity lines are consequently independent. Together with S and W', the map on cubic sections of (5) is an isomorphism:

    H0(E_hat(3))=S+W'+2T -> H0(C(3))=S+W'+2T.     (9)

The V(-4) source has no cubic sections, but its actual rows in (5) have not been set to zero. They have no effect on the exact H0 kernel in (9).

## 6. The exact kernel contradicts strict-top

Exactness of (5) and (9) gives H0(K(3))=0. The actual quotient A_q in either case has rank3, degree2, so rank K=14 and deg K=-56. Every degree of K is at most-4. Their sum forces every one of its fourteen ordinary degrees to be exactly-4.

The actual source Euler identity and (4) give

    chi_G(E(4))=3V+3P+2D,
    chi_G(A_q(4))=V+P+2D.

Thus the coefficient representation is 2V+2P, proving (3).

The derivative of K factors through the ACTUAL internal quotient A_q(-2); its kernel is the next Gauss kernel whether or not its rank is three. Strict-top applied to K at its top degree-4 therefore injects

    H0(K(4))=2V+2P -> H0(A_q(2))=V+2P+D.

There are two V copies in the source and only one in the target. This is impossible. It proves both exclusions in (2) with no condition on beta_K's rank, no torsion-defect choice and no horizontal splitting.

## 7. Direct coverage consequence and remaining obligation

Under the actual four-type conclusion of PR1123, any quotient with an O(-8) summand already forces the D-type: the other three sources have no maps to O(-8). Consequently this theorem excludes every original182 row with either A_q in (2): ten original profile(1,1) rows and four original profile(2,1) rows. Their stable IDs, full ordered quotients and original defects are in RESULT.json.

This is a cut of the fixed historical necessary list, not fourteen previously live frontier exclusions. It is not to be added to later campaign totals. In particular the original profile21 rows3/4 and6/7 are removed, covering both original defects12 and0 for each shape.

The profile(1,1) and profile(2,1) coverage obligations are not closed here. No COV theorem, global rank-three exclusion, maximal rank, obstruction value, full-adjoint invertibility, smoothing, algebraicity or original theorem repair is claimed. No actual coefficient, parameter, point, tensor, jet, matrix, source-instance rank, scan or historical enumeration was evaluated.
