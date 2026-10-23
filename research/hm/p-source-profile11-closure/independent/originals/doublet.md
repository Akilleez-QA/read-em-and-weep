# A terminal doublet forces scalar degree at least fourteen

## Theorem and scope

Work over C on the physical binary-icosahedral parameter line P(W*), with G=SL2(F5), determinant convention and the ACTUAL saturated rank17 degree−54 bundle E inside the constant thirty-dimensional plane-section bundle H O. Write K=E^- for its actual Gauss kernel and A=E/K for the locally free quotient, not the saturation of its image in the ambient derivative target.

Assume generic derivative rank three and maximal rank-three profile (k,l)=(1,1). Then neither of the following equivariant quotient shapes is possible:

    A = W' O(-1) + O(4),
    A = W' O(-1) + O(10).

This holds for every actual primary source type, independently of the dual quotient B and determinant defect. It does not exclude the entire profile, prove an exhaustive global frontier, or complete the original proof repair.

More generally, suppose rank A=3, rank(beta_K)<=2, A=W'O(-1)+O(e), H0(K(3))=W', and W' is absent from Sym^(e+1)W (a negative symmetric exponent means zero). Then e>=14. The proof needs no scalar-row evaluation and no connection-compatible splitting.

## 1. Pinned geometric inputs

INPUTS.json contains ten complete immutable public originals, authenticated by URL, byte count, SHA256 and Git blob ID. The actual embedding, plateau convention and strict-top lemma are pinned at db51525015bb7c5e825833d550d08dedf6f6ea96. The primary four-type theorem is PR1123 at 504b7eb800407dfc7e6340c98c72cdd553939f54; the cubic alternatives are PR1140 at 7a2488bcd36d95f79b5198001111b1a31fe5c3ba; the D-type image criterion is PR1142 at df2fd3d35dac577d7f1e1c4d51fe68b1fcc824ad. PR1153 at 4b97c71dace666dd5bf39e0128abbe7b01a2f056 supplies the P-type localization and Euler factorization, though the simpler endpoint argument below needs only its cubic-kernel character and general cubic-vanishing envelope.

The actual-splitting original Section4 writes F_k=E and ker(beta_Fi)=F_(i−1) at interior plateau stages. Section5 says maximal plateau endpoints have derivative rank one or two. Therefore when k=1, K=F_0 is precisely the lower endpoint and rank(beta_K)<=2. This is not an assumed rank bound on every iterated derivative. The argument actually requires only k=1, not the forward-length condition l=1.

Strict-top says: if F is saturated in the constant ambient and all its ordinary degrees are <=−d with d>0, then H0(F^-(d))=0. Every successive Gauss kernel is saturated in that same constant ambient. For K inside E, its actual derivative lands in (E/K)(−2)=A(−2); for K^- inside K, its derivative lands in (K/K^-)(−2). These factorizations follow because each preceding second fundamental form vanishes on its kernel. No abstract projection is regarded as horizontal.

## 2. Cubic vanishing is impossible for either target

The four necessary actual source types are

    D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8),
    P O(-2)+(W'+T)O(-3)+V O(-4)+W' O(-5),
    V O(-2)+(W'+T)O(-3)+2V O(-4),
    (W'+2T)O(-3)+V O(-4).

All have chi_G(E(4))=3V+3P+2D. Their possible H0(K(3)) characters are respectively 0 or S, 0 or W', 0, 0.

Whenever H0(K(3))=0, all K degrees are <=−4 and strict-top gives H0(K^-(4))=0. Thus the actual derivative injects H0(K(4)) into H0(A(2)). Euler additivity makes

    C(A)=H0(A(2))+chi_G(A(4))−(3V+3P+2D)

an actual cokernel character plus H1(K(4)), hence genuine. Exact characters for the two targets are

    C(W'O(-1)+O(4))  = −V,
    C(W'O(-1)+O(10)) = 1+2 A_std+D−V.

Both have V multiplicity −1, so cubic vanishing is impossible.

This already rules out the V and Z sources. For the D source a nonzero cubic kernel forces a nonzero actual map O(2)->A by PR1142. Maps to W'O(-1) vanish by degree. Maps to O(e) require invariants in Sym^(e−2)W. For e=4 this is A_std; for e=10 it is P+D. Both have no invariants. Thus D is impossible too. Only P could remain, and PR1140 forces H0(K(3))=W'.

For clarity, PR1153 additionally locates this W' in the unique top Euler inclusion W'O(-3)->P O(-2), and forces its actual quotient row to factor through W'O(-1). That stronger information is consistent with what follows but is not needed to identify any connection splitting or full scalar row.

## 3. The doublet endpoint image is forced, not guessed

Strict-top for E gives all K degrees <=−3. Equivariant Birkhoff splitting is legitimate in characteristic zero. Since H0(K(3))=W', the complete top-degree block is exactly

    C = W' O(-3),   K is abstractly C + N,

where all degrees of N are <=−4. Indeed only degree−3 summands contribute sections at twist3. Rank K=14, and C has rank2.

The actual derivative of K takes values in

    A(-2)=W'O(-3)+O(e−2).

Its restriction from C to the scalar summand has Hom space Hom_G(W',Sym^(e+1)W), which is zero by hypothesis. Its restriction to the doublet is a scalar endomorphism by Schur's lemma. That scalar cannot be zero: otherwise C would be killed by beta_K and H0(K^-(3)) would contain W', contrary to strict-top for K. Consequently beta_K restricts to an isomorphism C->W'O(-3).

Since beta_K has generic rank at most2, its projection onto the remaining scalar target vanishes generically: the full first summand is already in its image. A morphism of bundles vanishing generically on the integral line vanishes everywhere. Thus the coherent image is EXACTLY the displayed W'O(-3), with a split surjection

    0 -> K^- -> K -> W'O(-3) -> 0.

This image is saturated in this particular target because it is a displayed direct summand and the restriction on C is an isomorphism. No general saturation of a derivative image is assumed. The right inverse is a bundle right inverse, not a horizontal map. In particular K^-=ker(beta_K) is abstractly isomorphic to N and has all degrees <=−4.

## 4. The next derivative yields the degree contradiction

The actual derivative of K^- lands in

    (K/K^-)(-2) = W'O(-5).

If K^- had any degree−4 summand, the whole degree−4 coefficient block would map to zero in W'O(-5), since the ordinary Hom degree is −1. Thus H0((K^-)^-(4)) would be nonzero. Strict-top applied to the saturated negative bundle K^- forbids this. Therefore every degree of K^- is <=−5. This argument does not constrain the rank of this next derivative.

Now deg A=e−2, so deg K=−52−e. The displayed rank2 derivative image has degree−6. Hence

    rank K^- = 12,   deg K^- = −46−e.

Twelve degrees at most−5 have sum at most−60. Therefore −46−e<=−60, or e>=14. This proves the general conditional bound.

For e=4 and10 the required Hom vanishings hold because

    Sym5 W=T,   Sym11 W=W+S+T,

and neither contains W'. Their residual degrees would be respectively −50 and−56, both exceeding −60. These contradictions finish the two all-source exclusions.

## 5. Fixed historical labels and limits

Read only the frozen original profile11 JSON, without regenerating its enumeration. The first shape occurs at zero-based indices86,87,88,89,96; the second occurs at116. These identify historical records to which the theorem applies, independently of their B or defect. They are not a current-live case count, a claimed incremental count against every later result, or a completeness assertion about present branches.

The proof uses only actual-map geometric implications and universal representation identities. The checker verifies every imported byte identity, source ranks/degrees/Euler characters, signed envelopes, all relevant Hom vanishings, the endpoint degree arithmetic and those fixed labels. It does not itself prove the geometric imported results. No actual coefficients, selected parameters, points, jets, instance tensors, matrices or rank experiments are evaluated. No stopped spike or consumed experiment is restarted.
