# Actual polarization roots after pointed etale localization

Work over C. This concerns the integral projective cubic-image fourfold V=V51 and L0=O_V(1), not a selected original HM/source instance. Fix m>=1.

## Pinned dependencies

All PRs are in https://github.com/Akilleez-QA/read-em-and-weep.

- PR611 at 12b28d33627cc0e8b283d142dc16439a51bb5e00: V is integral projective, H0(O_V)=C, and L0 is ample.
- PR629 at 3ad872801158107d8fa71fa578f2ea948efd9f25: a single high-power Hilbert approximation realizes any prescribed finite formal jet on a smooth pointed curve, retaining the powered line bundle; symmetry-breaking first-order classes give trivial fixed-base automorphism groups.
- PR630 at 8024882d2129142fece5dbaf83b49e5f8e3817ca: a consecutive-power construction realizes original-polarized jets; nonzero abstract first-order motion forces generic h0(L)<=9.
- PR631 at 4954b42e25592cf4b66a28d6a232fbe6b528f72e: high-power embedded lifting is formally smooth over polarized deformations.
- PR632 at fcb0300e36bd3b023e00a872c78207901392e7c8: on every proper flat Artin deformation of V, a prescribed m-th power lift has a unique root class with fixed central root L0. Compatible central markings and power isomorphisms yield unique root triples up to unique isomorphism. The proof uses invertibility of m, not H2(O_V)=0, for this prescribed-power assertion.

## Theorem

Let f:Y->B be projective, flat and of finite presentation, where B is a smooth finite-type complex curve with a marked C-point b and Y_b identified with V. Let M be an invertible sheaf on Y, and fix an isomorphism theta0:L0^m->M_b.

There is a pointed etale neighborhood (B',b')->(B,b), with B' a smooth integral finite-type complex curve after shrinking, and an invertible sheaf L on Y'=Y x_B B', together with

    alpha:L|_(Y'_(b'))->L0,
    beta:L^m->M|_(Y'),

such that beta_b'=theta0 composed with alpha^m. Moreover L is relatively ample after shrinking B' around b'. All formal reductions of this triple are the unique fixed-central-root reductions supplied by PR632 for the pulled-back powered family.

This asserts an actual power relation on an actual curve neighborhood, not just on its completion. It does not assert a root on the original whole curve B or global uniqueness of roots.

## 1. Functions and a section near the marked fiber

First shrink B around b. The geometrically reduced locus of fibers is open for proper flat finitely presented morphisms [Stacks 0C0E](https://stacks.math.columbia.edu/tag/0C0E). It contains b because V is integral over C. Upper semicontinuity of h0(O), with residue-field base change [Stacks 0BDN](https://stacks.math.columbia.edu/tag/0BDN), gives h0(Y_s,O)<=1 near b, whereas every fiber is nonempty near b (the proper image is closed and the flat finitely presented image is open), so h0>=1. Thus h0=1 there. The same holds after residue-field extension by field base change for coherent cohomology. Consequently these geometrically reduced fibers are geometrically connected: a disconnected proper geometric fiber would have at least two independent constant functions. We need reduced connected fibers, not an unsupported assumption that all neighboring fibers are integral.

It follows that O_T -> f_(T,*) O_(Y_T) is an isomorphism for every base change T->B by [Stacks 0E0L](https://stacks.math.columbia.edu/tag/0E0L).

Choose a smooth C-point y in V, possible because an integral variety over a characteristic-zero field has a nonempty smooth locus. Flatness and the fiberwise criterion show f is smooth at y. The local normal form of a smooth morphism [Stacks 039P](https://stacks.math.columbia.edu/tag/039P) gives an etale map U->A^d_B near y. Pull back along the constant section with coordinates equal to those of y. Its inverse image is an etale neighborhood B1->B with a point b1 mapping to y and residue C, and supplies a section sigma:B1->Y_(B1). Shrink and retain the component through b1. Rename this pointed base B. All previous properties persist under this base change.

## 2. A finite-presentation parameter space for root classes

Let P=Pic_(Y/B), the relative fppf Picard sheaf. By [Stacks 0D2C](https://stacks.math.columbia.edu/tag/0D2C) and [Stacks 0DNI](https://stacks.math.columbia.edu/tag/0DNI), it is an algebraic space locally of finite presentation over B. These hypotheses hold by Section 1.

The section sigma removes the line-bundle representation obstruction: [Stacks 99.11.4, 0D24](https://stacks.math.columbia.edu/tag/0D24) identifies P(T) with the isomorphism classes of line bundles on Y_T trivialized along sigma_T. Such rigidified bundles have no nontrivial automorphisms, since every global unit comes from T and restriction along sigma is its inverse identification. In particular, a T-valued Picard class is represented by an actual line bundle, not only an fppf-local one.

Form the algebraic-space fiber product

    R = B x_( [M], P, [m] ) P,

where [m] sends a line-bundle class to its m-th tensor power. The point r0 in R_b is the class [L0], using theta0. Both P and R are locally of finite presentation over B. For R this also follows by expressing the fiber product as the equalizer of the two maps P->P over B: the diagonal of a locally finitely presented algebraic space is locally of finite presentation.

We claim R->B is etale at r0. Take a small extension A'->A of local Artin C-algebras, a pointed map Spec A'->B, and a map Spec A->R reducing to r0. By the rigidified description (or Pic(A)=0), this is a root class on the specified family Y_A whose m-th power equals M_A. Choose a central marking and compatible power isomorphism. PR632 gives a lift on the specified Y_(A'), and exactly one root class. Forgetting the chosen isomorphisms gives exactly one lift Spec A'->R. This also shows the relative tangent space at r0 is zero.

For completeness the passage from this infinitesimal statement to etaleness is legitimate for algebraic spaces: choose an etale scheme chart U->R and a C-point u over r0. The infinitesimal unique lifting property of this chart transfers the preceding existence statement to U->B. The local Artin smoothness criterion [Stacks 02HX](https://stacks.math.columbia.edu/tag/02HX) makes U->B smooth at u, and its relative tangent dimension is zero. Hence it is etale there. Etaleness descends along the etale chart. Shrink R to its etale locus around r0 and choose such a chart there. An affine open neighborhood B2 of u is a finite-type pointed etale neighborhood of B carrying the tautological root class.

## 3. Recovering an actual power isomorphism

Pull everything to B2 and denote its root class by ell. The section sigma and the Picard splitting give a representing line bundle L with sigma^*L trivial. Since m ell=[M], the same exact sequence gives

    L^m tensor M^(-1) = f^*N

for a line bundle N on B2. Trivialize N after Zariski shrinking around b2. This gives an actual isomorphism beta:L^m->M. No division of a base line bundle is needed. This step explicitly removes the residual base twist; equality in a relative Picard functor alone would not have been enough.

The central class of L is [L0], so choose alpha:L_b2->L0. The two central power isomorphisms beta_b2 and theta0 composed with alpha^m differ by a scalar in C*, since H0(O_V)=C. Multiply beta by the inverse discrepancy, a constant unit on B2, to impose the required central compatibility. Thus there is no unaddressed unit obstruction. No global choice of m-th roots of varying units on B2 has been used.

Finally, L_b2 is ample. Openness of relative ampleness for a line bundle in a proper family [Stacks 0D2S](https://stacks.math.columbia.edu/tag/0D2S) allows one more shrinking so L is relatively ample. Take the connected component through b2; a smooth connected complex curve is integral. Compose the pointed etale maps to obtain B'->the original B. This proves the theorem.

By PR632 the reductions of (L,alpha,beta) at b' agree uniquely, as root triples on the same marked infinitesimal families, with the formal root system for M. The unique comparison isomorphisms commute with reduction. This is a statement about formal reductions, not uniqueness on all of B'.

## 4. Next consequence: the single-power approximation already suffices

Start with a formal polarized pair (X_hat,L_hat), and apply PR629 using a sufficiently high single power L_hat^m. For any N>=2 it produces (Y,M)/B and an identification of its powered N-jet with (X_hat,L_hat^m) modulo t^N. Apply the theorem to this already constructed family, using the central root L0.

Pointed etale localization with residue field C preserves the completed local base ring and all its finite quotients. Transport the recovered L modulo t^N across the given powered-jet identification. It and L_hat modulo t^N are roots of the same power bundle with the same central root and central power identification. PR632 therefore identifies these polarized jets, including their power data. Thus PR629's single-power approximation can be upgraded to an original-polarized finite-jet realization on an etale neighborhood of its original curve. One does not need to rebuild the family in a product of two projective spaces. PR630 remains a separate direct construction that avoids this Picard-space step.

If the prescribed first-order class is in T_free, it remains so after the pointed etale change, with the pulled-back parameter t. Applying PR629's formal-faithfulness argument anew gives trivial fixed-base automorphism groups over each positive Artin quotient, the local DVR, and the new integral curve B'. This is not inferred merely from Aut_B(Y)=1, since automorphism groups can grow after base change. PR630's section-loss argument applies to this actual relatively ample root: any nonzero abstract first-order class forces generic h0(L)<=9.

## 5. An actual root on an etale high-power Hilbert chart

The argument also proves the following extension. Replace the smooth curve B by any finite-type complex scheme S with a C-point s, retain projective flat finite presentation and the central marked fiber V with theta0:L0^m->M_s. There is a pointed finite-type etale neighborhood S'->S carrying an actual relatively ample root L and power isomorphism as above. Indeed, the reduced-fiber openness, h0 semicontinuity, universal functions, smooth-point section construction, relative Picard space, small-extension criterion, base-twist trivialization and relative ampleness argument all hold over this Noetherian base without assuming it smooth or one-dimensional. Only the final assertion that the new base is a smooth integral curve is omitted. In particular this extension does not demand geometric integrality of every fiber: shrinking to geometrically reduced connected fibers suffices.

Apply it to the universal family near the point h of H=Hilb^(Q_m)(P^(n-1)) representing V in its complete high-power embedding, with M=O(1) restricted to that family. Here m is sufficiently large that L0^m is very ample with H1(L0^m)=0, n=h0(L0^m), and Q_m is its Hilbert polynomial. There is a pointed etale neighborhood (H',h')->(H,h) on whose universal-family pullback an actual relatively ample L satisfies L^m=O(1) and L_h'=L0 with the prescribed central power identification. Shrink H around h to the smooth locus supplied by PR631 and to the reduced-connected-fiber locus proved above; shrink H' correspondingly. Then H' is smooth at h', of dimension n^2+635. The actual pair family on H' induces the formal original-polarized lifting interface of PR632.

Thus the formal high-power parameter germ has an algebraic etale chart carrying the original polarization and its exact power relation. This is a parameter family, not a claim that H' represents polarized moduli, is a quotient by PGL_n, or gives a universal abstract pair deformation. It does not assert uniqueness of L across the chart.

## Boundaries and status

The added result is etale-local algebraicity of the fixed polarization root with an actual power relation on the family, plus the upgrade of single-power approximation. A different original formal arc may require a different curve for each N. No entire arc descent, global root on the original B, global uniqueness of roots, persistence of the ten original sections, generic-fiber automorphism theorem, original full-adjoint repair or Weil-class algebraicity conclusion is asserted. No selected actual HM/source evaluation or large computation is used. This is a mathematical proof conditional on the pinned inputs, not proof-assistant verification.
