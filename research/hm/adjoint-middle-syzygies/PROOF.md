# The degree-five gap and degree-six adjoint syzygies

Work over C on P(V)=P^4. Put T=V*, S=Sym(T), B=End_0(F), K_j=H^1(B(j-1)), and H_j=H^2(B(j-5)), with their actual multiplication maps. We prove

Tor_i^S(K,C)_5=0 for every i,

and, in internal degree six,

Tor_2^S(K,C)_6=H^0(B(5))=Sym^2 H^0(F(3)),
Tor_3^S(K,C)_6=H_0* tensor det T=W',
Tor_i^S(K,C)_6=0 for i other than 2 and 3.

Thus there are exactly ten minimal second syzygies and two minimal third syzygies in internal degree six, while internal degree five has no minimal syzygies at all. These conclusions are independent of the unresolved cubic ghost and the pending middle parameter in the full Betti family of H.

## 1. The required section vanishing

The pinned Chern character is ch(B)=3-15h^2+(75/4)h^4. Riemann–Roch on P^4 gives

chi(B(t))=3 binom(t+4,4)-(15/2)t^2-(75/2)t-25.

At t=4 this is -85. PR463 proves h^1(B(4))=85 by the symmetric evaluation sequence: its primary contribution has dimension forty and its residue contribution is 50-5=45. H^2(B(4))=0 by the structural bound PR167; H^3(B(4))=0 by PR476; H^4(B(4))=H^0(B(-9))*=0 by stability. Consequently H^0(B(4))=0.

We also use H^0(B(t))=0 for t<=3. For t<0 this follows from stability, and t=0 from simplicity. PR479 audits t=1,2 by Riemann–Roch and the established cohomology dimensions. For t=3, the same formula gives chi(B(3))=-100. PR477 records h^1(B(3))=100 from the symmetric evaluation sequence; its primary term has dimension forty and its residue term has dimension 75-15=60. The same structural higher-cohomology vanishings apply, giving H^0(B(3))=0. Thus every section group in twists at most four vanishes. No positive-twist section vanishing is inferred merely from stability.

PR456 proves the actual isomorphism Sym^2 H^0(F(3)) -> H^0(B(5)). Its dimension is ten.

## 2. High internal degrees of the H Koszul complex

PR482 proves that H is generated in degree zero and has no linear relations. Its actual Serre-compatible pairing has complementary H degree five. Pairing the five-variable Koszul complexes gives

Tor_i(H,C)_d=Tor_(5-i)(H,C)_(10-d)* tensor det T.

The determinant character is trivial for the normalizer, although the vanishings below do not require that trivialization.

Every Tor group of H in internal degree one vanishes: Tor_0(H,C)_1=0 by generation, Tor_1(H,C)_1=0 by the actual isomorphism T tensor H_0 -> H_1, and Tor_i(H,C)_1=0 for i>=2 by degree. Duality therefore gives

Tor_i(H,C)_9=0 for all i.

In internal degree zero the only nonzero group is Tor_0(H,C)_0=H_0=W'. Hence in internal degree ten the only nonzero H Tor group is

Tor_5(H,C)_10=H_0* tensor det T=W'.

No assertion about the remaining cubic scalar or the full higher resolution of H is needed.

## 3. The degree-five gap

Tensor the exact coordinate Koszul sheaf complex on P^4 by B(4). Its hypercohomology spectral sequence has

E_1^(-i,q)=Lambda^i T tensor H^q(B(4-i)),

with differential d_a of bidegree (a,1-a). The q=1 row is the internal-degree-five Koszul complex of K. The q=2 row is the internal-degree-nine Koszul complex of H, whose E_2 terms all vanish by section 2.

The q=0 row is zero already on E_1, because its twists range from -1 to four and section 1 proves all corresponding H^0 groups vanish. The q=3 row is zero because all its twists are at least -1, in the H^3 vanishing range of PR476. The q=4 row is zero by Serre duality and negative-twist H^0 stability, since its twists are also at least -1.

Therefore E_2 has only its q=1 row, consisting of Tor_i(K,C)_5. No differential of order at least two can enter or leave a nonzero row. All these terms survive to E_infinity, but the sheaf Koszul complex is exact and its hypercohomology is zero. Every Tor_i(K,C)_5 is consequently zero.

## 4. The two degree-six groups

Now tensor the coordinate Koszul complex by B(5). The q=1 row is internal K degree six and the q=2 row is internal H degree ten. The q=3 and q=4 rows vanish by the same structural bounds. The q=0 row has only one nonzero term, at position (0,0), equal to H^0(B(5)); every earlier term has twist at most four.

By section 2 the q=2 row has only one nonzero E_2 term, at (-5,2), equal to H_0* tensor det T. Thus the only possible nonzero higher differentials are the following two d_2 maps:

H_0* tensor det T at (-5,2) -> Tor_3(K,C)_6 at (-3,1),
Tor_2(K,C)_6 at (-2,1) -> H^0(B(5)) at (0,0).

For the first map, the source has no incoming differential and its possible outgoing d_3 target (-2,0) is zero. Its target has no other incoming differential and its outgoing d_2 target (-1,0) is zero. Therefore both terms can disappear from the zero abutment only if this d_2 is an isomorphism.

For the second map, its source has no nonzero incoming differential: the d_2 source (-4,2) is zero, and the q=3 and q=4 rows are zero. It has no outgoing differential after d_2. The target has no other nonzero incoming differential: the d_3 source (-3,2) is zero, as are the higher-row sources. Thus this d_2 is also an isomorphism.

Every other q=1 term has no nonzero incoming or outgoing differential and must vanish. This proves all the stated internal-degree-six assertions. The isomorphisms arise from actual hypercohomology differentials, not from matching dimensions or an arbitrary equivariant map.

## Contribution and boundary

The result gives a genuine gap in the minimal resolution of K, followed by exactly specified degree-six second and third syzygy spaces. It complements the complete relation-degree bound without deciding the remaining cubic relation channel. It does not calculate selected polynomial multiplication, a fixed-pair quotient, source membership, higher-order lifting, or algebraicity. It also does not replace the fixed-pair Tor boundary of PR477 with zero.

## Pinned dependencies

- PR482, H generation and self-duality: https://github.com/Akilleez-QA/read-em-and-weep/blob/30c2f32418bbe68ad5b2635ee424d698f329fe8d/research/hm/dual-cohomology-presentation/PROOF.md
- PR479, positive-twist section vanishings and Chern character: https://github.com/Akilleez-QA/read-em-and-weep/blob/b57cf851bb244706acfe6c6485d4dfa54ceb6519/research/hm/quadratic-shadow-exclusion/PROOF.md
- PR477, h^1(B(3))=100: https://github.com/Akilleez-QA/read-em-and-weep/blob/ff87076794e97238150485b12183c3cd0f4711e4/research/hm/adjoint-primary-extension/PROOF.md
- PR476, H^3 vanishing: https://github.com/Akilleez-QA/read-em-and-weep/blob/3aa461bc3581fb72fbf923fbe869ddee023b435a/research/hm/five-generator-module/PROOF.md
- PR463, h^1(B(4))=85: https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md
- PR456, symmetric evaluation sections: https://github.com/Akilleez-QA/read-em-and-weep/blob/07c11a096970a58f5f275b1438d4df3a27a1c6dd/research/hm/symmetric-evaluation/PROOF.md
- PR167, structural H^2 vanishing: https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md

This is an authored structural proof with mathematical reviews accompanying this proof, not formal proof-assistant verification. No selected actual HM/source-instance evaluation, numerical multiplication matrix or rank, coefficient search, generator/checker, or large computation was performed.
