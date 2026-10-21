# Exact elliptic pushforward constraints for the fifty-point interpolation kernel

Work over C with the modular normalization X, elliptic fibration pi:X->P1, divisor classes I,F and H=I+2F, as pinned in PRIMARY-NORMALIZATION-QUADRIC-INTERPOLATION.md. Set Y in |2H| general, Z=C intersect Y, L=O_Y(3H-Z), and pi_Y=pi|Y. These are symbolic deductions, without selected coordinates or rank evaluations.

## 1. Positive fiber degrees and equivariant splitting

For p>0, O_X(pI) has degree 5p on every smooth elliptic fiber, and degree p on each component of an I5 fiber. The fiber dualizing bundle is trivial. The inverse line bundle has negative degree on every component, hence no global section; duality gives fiber H1=0. Cohomology and base change therefore give

 R1 pi_* O_X(pI)=0,
 E_p=pi_*O_X(pI) locally free of rank5p.

By surface Riemann-Roch,

 chi(O_X(pI))=5-5p(p+3)/2,
 deg E_p=5-5p(p+5)/2.

The Heisenberg action linearizes O_X(I) and acts trivially on the elliptic base. For p not divisible by five the center acts with nontrivial character. The unique irreducible representation of that central character has dimension five, so E_p=V_p tensor W_p, with W_p of rank p. Consequently every splitting multiplicity of E_p on P1 is divisible by five.

For 1<=p<=4 and q<p, an effective pI+qF would have negative intersection q-p with every torsion section. Thus it would contain their sum C=5I. The residual class (p-5)I+qF has negative intersection with the nef fiber, impossible. Hence

 H0(X,pI+qF)=0 for q<p.                     (1)

## 2. Two explicit splitting conclusions

For p=4, E_4 has rank20 and degree -85. Write E_4=V_4 tensor direct_sum_(j=1)^4 O(a_j). Equation (1) at q=3 gives a_j<=-4, while sum a_j=-17. The only possibility is

 E_4 = O(-5)^5 direct_sum O(-4)^15.         (2)

For p=2, rank10 and degree -30 similarly give a_1,a_2<=-2 and a_1+a_2=-6. Thus

 E_2 = O(-2)^5 direct_sum O(-4)^5,
 or E_2 = O(-3)^10.                        (3)

No claim is made here selecting one of these two possibilities.

As a consistency check, p=1 gives E_1=O(-2)^5. This independently recovers h0(I+2F)=5, agreeing with BHM Section4.4 Lemma11 (printed page62), which explicitly computes the cohomology of I+qF. It does not rely on inferring completeness merely from a map to P4.

## 3. The interpolation kernel as a kernel bundle on P1

Since omega_(X/P1)=O_X(5F), relative duality gives

 R1 pi_*O_X(-pI+qF)=E_p^* tensor O(q-5).

The negative-fiber-degree bundles O_X(H-C)=O_X(-4I+2F) and O_X(3H-C)=O_X(-2I+6F) have zero direct images. Push forward their exact restriction sequence along pi. Since pi_Y is finite, its higher direct image is zero. We obtain an actual exact sequence of vector bundles

 0 -> pi_Y*L -> O(2)^5 direct_sum O(1)^15 --q--> T -> 0,  (4)

where, according to the two alternatives in (3),

 T=O(3)^5 direct_sum O(5)^5,
 or T=O(4)^10.

In particular pi_Y*L has rank10 and degree25-40=-15. Taking cohomology of (4) is precisely the 45-to-50 multiplication and interpolation sequence previously derived:

 0 -> H0(Y,L) -> C45 --q--> C50 -> H1(Y,L) -> 0.

Although the sheaf map in (4) is surjective, its global-section map need not be. The calculation does not substitute sheaf surjectivity for the missing interpolation injectivity or for the adjoint twenty-boundary. If pi_Y*L=direct_sum O(b_i), then sum b_i=-15, b_i<=2 by its injection into the displayed source, and h0(L)=sum max(b_i+1,0). On the known cubic-injective open, the fifteen-dimensional normalized-cubic argument also bounds that sum by15.

## Sources and scope

BHM, Shioda's Modular Surface S(5) and the Horrocks-Mumford Bundle, Section4.3 supplies the Heisenberg linearization on O_X(I) and the fiber geometry, and Section4.4 Lemma11 supplies the independent degree-one cohomology check:
https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

The pinned primary identification is PR570 at e5e55594ef2b99cefb81c4c02b22cb45e1ff0025. The exact splitting classification, relative-dual kernel presentation and resulting restrictions above are new deductions. No full Q4 or boundary determinant value is asserted.
