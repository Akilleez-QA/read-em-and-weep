# Preserved supporting-theorem audit

This is the original mathematical review, not an independent certification of publication edits. Its primary-source assumptions remain explicit.

# Independent audit: normalized HM regularity and collision bounds

## Verdict

The normalized Horrocks–Mumford bundle F is exactly 5-regular. Consequently B0=End₀(F) is 9-regular. The resulting purely regularity-based common sufficient order is 10 for an **unweighted** source in I^10 E; an already first-weighted source in I^k EA instead requires k≥11 by that particular argument.

The tensor-monad improvement is valid: H²(B0(t))=0 for every t≥3. Together with the 9-regularity H¹ threshold, it lowers the common unweighted order to 8.

There is a still stronger map-free consequence of the section-module resolution printed across Decker pp.14–16:

    H¹(B0(t))=0 for every t≥7,
    H²(B0(t))=0 for every t≥2.

These give the common sufficient unweighted order **7**, retaining all existing global regular transport, sign/constant comparison, and injectivity premises. They also permit the common downstairs thickening N6, of transverse length 5 and degree 30. None of these numbers is asserted minimal, and none proves the actual source has the required ideal order.

## 1. Primary-source verification

I visually inspected the supplied primary PDF, Wolfram Decker, “Monads and cohomology modules of rank 2 vector bundles,” Compositio Mathematica 76 (1990), 7–17; item https://www.numdam.org/item/CM_1990__76_1-2_7_0/ . The relevant pages are printed 13–16, PDF pages 8–11. The printed page 13 explicitly identifies the normalization c1(F)=−1 and states that H²F(*) is a vector space W situated only in degree −2. The printed page 16 gives the minimal free resolution

    0→2S(−8)→20S(−6)→35S(−5)⊕2S(−3)
      →15S(−4)⊕4S(−3)⊕10S(−2)→15S(−1)→5S→H¹F(*)→0,

where S=C[z0,…,z4]. This matches the proposed transcription. Its alternating Hilbert numerator is

    5−15z+10z²+2z³+15z⁴−35z⁵+20z⁶−2z⁸
      =(1−z)^5(5+10z+10z²+2z³).

Thus

    h¹F(t)=5,10,10,2 for t=0,1,2,3 respectively,
    h¹F(t)=0 for every other integer t.

This uses exactness and degrees of a published universal resolution, not an evaluation or rank computation of its displayed matrix.

Since F has rank two and determinant O(−1), F∨=F(1). Serre duality on P⁴ consequently reads

    H^i(F(t))^*=H^(4−i)(F(−t−4)).

## 2. Exactly 5-regular

The four required groups vanish:

    H¹F(4)=0,
    H²F(3)=0,
    H³F(2)^*=H¹F(−6)=0,
    H⁴F(1)^*=H⁰F(−5)=0.

For the last group no stability assertion or evaluated map is needed. Write the normalized monad as

    5O(−1)→M=2Ω²(2)→5O,

with kernel K of the second arrow. The exact sequences are

    0→K→M→5O→0,
    0→5O(−1)→K→F→0.

The exterior Euler sequence embeds Ω²(2) into 10O. Therefore, for every t<0, H⁰(M(t))=0, whence H⁰(K(t))=0. Since H¹(O(t−1))=0 on P⁴, the second sequence gives H⁰(F(t))=0 for t<0. This applies to t=−5.

On the other hand h¹F(3)=2, so F is not 4-regular. Persistence of regularity rules out every smaller regularity integer. Therefore reg(F)=5 exactly.

Tensor-regularity subadditivity gives F∨ 4-regular and End(F)=F⊗F∨ 9-regular. Over C, the trace splitting End(F)=O⊕B0 makes B0 9-regular. In particular

    H¹(B0(t))=0 for t≥8,
    H²(B0(t))=0 for t≥7.

This establishes an upper bound for the regularity of B0, not its exact regularity.

## 3. The proposed tensor-monad improvement is sound

The bundle Ω²(2), hence M, is 1-regular. For example the exact linear resolution

    0→O(−3)→5O(−2)→10O(−1)→Ω²(2)→0

has the required shifts. Since F∨ is 4-regular, N=F∨⊗M is 5-regular, so H²(N(t))=0 for t≥3.

Tensor the first monad short sequence by F∨. Its cohomology contains

    H¹(5F∨(t))→H²(F∨⊗K(t))→H²(N(t)).

For t≥3 the left group is 5H¹F(t+1)=0, and the right group is zero by the preceding regularity statement. Thus H²(F∨⊗K(t))=0.

Tensor the second short sequence by F∨ and twist by t. It becomes

    0→5F(t)→F∨⊗K(t)→End(F)(t)→0.

The group following H²End(F)(t) is H³(5F(t)), whose dual is 5H¹F(−t−4)=0 for t≥3. Hence H²End(F)(t), and therefore H²B0(t), vanish for t≥3. Every arrow used is a formal bundle map from the monad; none is evaluated.

## 4. Stronger thresholds from the section-module resolution

This improvement is separately checkable directly from the same primary paper. On printed page 14 Decker writes the exact minimal free resolution

    0→F3→F2→F1→F0→H⁰F(*)→0.

On printed page 15 its relation to the H¹-resolution is displayed: the latter has successive terms F3, F2, F1⊕(S(−3)⊗W), F0⊕(S(−2)⊗V⊗W), S(−1)⊗V1⊗U, S⊗V3. Comparing with the concrete shifts on page 16 identifies

    F3=2S(−8), F2=20S(−6), F1=35S(−5),
    F0=15S(−4)⊕4S(−3).

Thus sheafification gives the exact locally free resolution

    0→2O(−8)→20O(−6)→35O(−5)
      →15O(−4)⊕4O(−3)→F→0.

Tensor by F∨(t)=F(t+1). Let the resulting terms, indexed from the term surjecting onto End(F)(t), be

    E0=15F(t−3)⊕4F(t−2),
    E1=35F(t−4),
    E2=20F(t−5),
    E3=2F(t−7).

For an exact resolution E3→E2→E1→E0→G, vanishing of H^(p+j)(Ej) for all j implies H^p(G)=0. This follows by splitting into kernel sequences, or by the usual resolution-cohomology spectral sequence. The criterion requires no H⁰ surjectivity or evaluation of any differential.

For p=1 and t≥7:

- H¹(E0)=0 because t−3≥4 and t−2≥5.
- H²(E1)=0 because H²F is supported only at −2, while t−4≥3.
- H³(E2)^*=20H¹F(1−t)=0.
- H⁴(E3)^*=2H⁰F(3−t)=0, since 3−t<0.

Therefore H¹End(F)(t)=0 for t≥7.

For p=2 and t≥2:

- H²(E0)=0 because t−3,t−2≥−1, while H²F is supported only at −2.
- H³(E1)^*=35H¹F(−t)=0.
- H⁴(E2)^*=20H⁰F(1−t)=0, since 1−t<0.
- H⁵(E3)=0 by dimension.

Therefore H²End(F)(t)=0 for t≥2. Trace splitting passes both conclusions to B0. This argument has no matrix-rank or maximal-rank assumption.

## 5. Collision consequences and the order distinction

Retain the audited ordinary ideal I of the reduced union of all triple diagonals, its S4 stability, the actual globally linearized coefficient E=q*B0⊗A^(−2), and the weighted invariant ideals

    K_n=(t₂^a t₃^b : 2a+3b≥n).

For r=0,1,2 and k≥3 the imported actual-subsheaf formula is

    (q_*(I^k EA^r))_sign=B0(r−5)K_(k−3).

Set n=k−3. The adjacent-generator resolution of K_n has generator degrees d_i≥n and adjacent-syzygy degrees

    e_i=2a_i+3b_(i+1)=d_i+3(b_(i+1)−b_i)≥n+3.

After tensoring, the controlling outer groups dualize to

    H²(B0(d_i−r)), H¹(B0(e_i−r)).

The different certified threshold pairs give the following sufficient conclusions:

- From 9-regularity alone: d_i−r≥7 and e_i−r≥8 are assured by n≥r+7, hence k≥r+10.
- From Section 3 plus 9-regularity: d_i−r≥3 and e_i−r≥8 are assured by n≥r+5, hence k≥r+8.
- From Section 4: d_i−r≥2 and e_i−r≥7 are assured by n≥r+4, hence k≥r+7.

Thus the strongest bound established here gives coefficient vanishings at orders 7,8,9 for r=0,1,2. The global sections σ∈IA and τ=σ²−q*t₂/6∈I²A² turn an unweighted closed R∈I^7E into closed σR∈I^8EA and τR∈I^9EA². Full sign projection preserves these ideal orders because I is S4-stable.

With all three regular transport maps and the injective constant inclusions assumed in the existing full-target theorem, these vanishings kill the constant coordinate and both retained coordinates. The weaker formulation using only the H-sign projection R_H=e_HS remains valid, with I^7 replacing I^12. Closure, regularity and [R_H]=j0([C]) are separate premises. None follows merely from group characters or ideal algebra. The already established source-comparison and ramification/canonical-form conventions must be retained unchanged.

The apparent order10/order11 discrepancy in the original regularity-only question is therefore resolved: order10 refers to the common **unweighted** source; order11 refers to the first-weighted coefficient. For example K7 contains the genuine minimal monomial t₂²t₃ of degree7. Its first-weight dual group is H²B0(6), so the 9-regularity threshold alone cannot justify first-weight order10. Sections 3–4 subsequently supply stronger vanishings, but that is a new argument, not a parity exception to the original degree bound.

## 6. Common downstairs detectors

The same exact-sequence argument makes restriction

    H²(Y,B0(r−5))→H²(N_n,B0(r−5)|N_n)

injective whenever H²(B0(r−5)K_n)=0. Under Section 4, a common n=6 works for r=0,1,2. Put u=t₂,v=t₃. Then

    K6=(u³,u²v,v²).

Its generator degrees are (6,7,6) and adjacent-syzygy degrees are (9,10). The exact global resolution is

    0→O(−9)⊕O(−10)→2O(−6)⊕O(−7)→O→O_N6→0.

The five monomials of weight less than6 are 1,u,u²,v,uv. Hence N6 has transverse length5. Since N is the degree6 complete-intersection surface, degree(N6)=30. These are surface multiplicities, not counts of points. The previously audited flat-base-change argument supplies exactness even over the singular base surface. The resolution and codimension two give Cohen–Macaulayness; Gorensteinness is not required or asserted.

Dualizing by O(−5) gives

    0→O(−5)→2O(1)⊕O(2)→O(4)⊕O(5)→ω_N6→0.

For r=0,1,2, Serre duality therefore turns the injective restrictions into the surjective detector maps

    H⁰(N6,B0(5−r)|N6⊗ω_N6)↠H²(Y,B0(−r)).

This is not surjectivity of obstruction restriction, and the dualizing sheaf is not claimed invertible.

For the weaker intermediate bounds, the proposed numerical checks are also correct:

- K7=(u⁴,u²v,uv²,v³), transverse length7, degree42; it works commonly using Section 3 and H¹ threshold8.
- K9=(u⁵,u³v,u²v²,v³), transverse length10=5+3+2, degree60; it works commonly from 9-regularity alone.

The natural quotient maps from Q7=E/I^7E land respectively in coefficient quotients by K4,K5,K6. The common N6 theorem instead restricts already defined global coordinate classes. One cannot replace the smaller ideals by K6 in the natural quotient construction for r<2. Similarly the intermediate Q8 maps naturally to K5,K6,K7, and Q10 maps naturally to K7,K8,K9. These distinctions preserve the previously audited finite-neighborhood diagrams.

## Scope

I checked the primary pages and the local all-powers, effective-bound, full-target and finite-detector proofs.  The current older downstream files still contain their prior numeric bounds; this audit records replacements without silently changing those premises or claiming the source satisfies them.

## 7. Final audit of SHARPEST-BOUND.md, including poles and endpoints

I independently reviewed the complete SHARPEST-BOUND.md after its preparation. Its section-module reconstruction, diagonal-vanishing argument, coefficient orders 7/8/9, common unweighted order7, N6 multiplicity and resolutions, and quotient-versus-common-support distinction all agree with the calculations above. No correction is needed.

The pole consequence is correct under the imported Cartier-divisor and compatible regular Čech-complex premises. A single degree-six discriminant twist sends the two target coefficients B0(−4), B0(−3) to B0(2), B0(3); both resulting H² groups vanish. In the exact sequence

    0→F_i→F_i(D)→F_i(D)/F_i→0,

the boundary H¹(F_i(D)/F_i)→H²(F_i) is consequently surjective. Equivalently every regular 2-cocycle has a compatible meromorphic primitive with at most a simple pole. This does not imply that the primitive is regular, that the retained class is zero, or that the simple-pole presentation is unique. Its closed-meromorphic ambiguity remains im H¹(F_i(D)), which is not shown to vanish by the positive thresholds.

The two proposed endpoint bounds are also sound:

    h²B0(1)≤30,
    h¹B0(6)≤30.

For t=1, H²(E0)=15H²F(−2) has dimension30, while H³(E1)=35H³F(−3)=0, H⁴(E2)=20H⁴F(−4)=0 and H⁵(E3)=0. Here H⁴F(−4)^*=H⁰F(0)=0 follows from the primary section module generated in degrees3 and4. Splitting the resolution into kernels shows that H²(E0) surjects onto H²End(F)(1), proving the first bound.

For t=6, H¹(E0)=15H¹F(3) has dimension30, while H²(E1)=35H²F(2)=0, H³(E2)=20H³F(1)=0 and H⁴(E3)=2H⁴F(−1)=0. Therefore H¹(E0) surjects onto H¹End(F)(6), proving the second bound. Intermediate cohomology of the scalar summand O vanishes, so these are the stated B0 bounds. The unevaluated maps may have nontrivial images; neither equality nor vanishing of either endpoint group follows.

Final verdict: the strongest stated proof and these endpoint upper bounds pass this independent audit. All actual source-membership, transport and obstruction-value limitations remain in force.
