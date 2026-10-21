# Hyperplane sections obstruct middle-primary invertibility

## Verified literature premise

The companion MIDDLE-LINEAR-DETERMINANT-ZERO.md records the checked primary sources: Banica–Manolache, INCREST preprint 104 (1981), section 1, Lemma 1, printed pp.3–4, and Boralevi, arXiv:math/0602002, printed p.6. Together they imply that every HM hyperplane restriction G has H^0(G(2)) nonzero. The authored lemma and its proof were checked against the scan; its Gruson–Peskine curve-theorem dependency is identified but not independently reproved here.

Sources:
https://imar.ro/~increst/1981/104_1981.pdf
https://arxiv.org/pdf/math/0602002

The product exact sequence below is derived directly from restriction sequences. It needs no additional genericity premise.

## 1. The exact consequence for the actual primary arrow

Let F be the normalized HM bundle on P4 and A_d=H^1(F(d)). The actual dimensions are dim A_0=5 and dim A_1=dim A_2=10. The global section vanishings H^0(F(j))=0 for j=0,1,2 are part of the established HM cohomology.

For H=V(ell), write G=F|H. The exact sequence

    0 -> F(1) --ell--> F(2) -> G(2) -> 0

identifies

    ker(ell:A_1 -> A_2)=H^0(G(2)).

Therefore this middle linear map is singular. Every HM hyperplane restriction is stable, so every nonzero ell gives a singular middle map. Equivalently the determinant of the universal 10-by-10 middle-primary linear map is identically zero.

This is not the different top arrow ell:A_2->A_3, whose target has dimension two. Its established surjectivity is unaffected. No exact value of the middle corank is inferred.

## 2. A nontrivial boundary remains for product quadratics

Take q=ell1 ell2 and G_i=F|H_i. Put

    K1=H^0(G_1(1)),  B2=H^0(G_2(2)).

The degree-one restriction sequence identifies K1 with ker(ell1:A_0->A_1). The degree-two sequence gives the connecting injection kappa_2:B2->A_1 with image ker(ell2:A_1->A_2). Define

    t_(1,2):B2 -> A_1/(ell1 A_0)

as kappa_2 followed by the quotient map. Then there is an exact sequence

    0 -> K1 -> ker(q:A_0->A_2) -> B2 --t_(1,2)--> A_1/(ell1 A_0).

The middle map sends x in ker(q) to the unique section corresponding to ell1 x under kappa_2. Its image is exactly ker t_(1,2). Thus

    q is primary-injective
      iff K1=0 and t_(1,2) is injective.

Writing a=dim K1 and b=dim B2 gives

    dim ker(q)=a+b-rank(t_(1,2)),
    dim[A_1/(ell1 A_0)]=5+a,
    dim ker(q)>=max(a,b-5).

The verified literature premise gives b>=1, so this boundary is always a nontrivial condition. One cannot replace it by invertibility of the middle factor, or by vanishing of its section space. Reversing ell1 and ell2 gives the equivalent symmetric criterion, because graded multiplication commutes.

For q=ell^2, use the same formulas with H1=H2=H. No assertion that t_(ell,ell) vanishes or fails injectivity is justified by the singularity of ell:A_1->A_2 alone.

## 3. Why generic quadratic injection is not contradicted

The already proved generic quadratic statement concerns q:A_0->A_2, a 5-to-10 map, not the middle linear 10-to-10 map. Even for a product, a singular map from A_1 to A_2 can be injective on the at-most-five-dimensional subspace ell1 A_0. The exact obstruction is the intersection of this subspace with kappa_2(B2), precisely measured by t_(1,2).

Moreover product quadratics form a proper subvariety of all quadratics. Thus generic primary injection in the full quadratic parameter space does not itself prove that a good product or good square exists. Conversely, failure of every product, if it were established by another argument, would not contradict the generic full-space result.

Throughout this document A_d means primary cohomology H^1(F(d)). The Rao residual square map R_1->R_3, with R_d=H^1(I_C(d)), studied in DOUBLE-HYPERPLANE-JET-CRITERION.md uses different modules. The present primary section obstruction neither evaluates that residual jet map nor resolves the full adjoint 20-dimensional lift boundary. No conclusion about the original selected quadratic, full Q4, or exact generic middle corank is drawn.
