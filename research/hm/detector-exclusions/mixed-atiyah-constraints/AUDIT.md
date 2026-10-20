> Historical mathematical audit, preserved in full apart from nonmathematical process statements and source-link normalization. Original-source hashes identify the audited source text; publication-byte hashes are recorded separately. This is not a claim of a fresh or formal proof check.

# Independent audit of the universal mixed Atiyah argument

## Verdict

The revised proof passes this audit. Its algebra, signs, representation classification, geometric block parity, and Chern-class specialization are correct. The two initially requested precisions are now explicit and were rechecked: pointwise trace-free representatives in §1, and a retained projection factoring through the block-even projector in §3. The stated bounded exclusion and square-zero constraint follow. The one-dimensional classification concerns universal bilinear maps; it does not establish a nonzero realization on these specific Atiyah classes. Additional geometric relations could make C zero. Neither the classification nor the square-zero identity identifies C with the actual module obstruction.

## Checks

1. **Total-degree signs.** The projected Atiyah representatives remain End-valued forms of type (1,1), even though only their holomorphic index is projected. Their scalar entries have even total degree and commute. Ordinary rank-two Cayley–Hamilton and cyclic trace therefore apply. This differs from ordinary End-valued (0,1) Yoneda representatives. The holomorphic projections commute with the Dolbeault differential because the cotangent splitting is holomorphic.

   As now explicitly done in §1, take B_z=A_z−(tr A_z/2)Id and B_h=A_h−(tr A_h/2)Id at representative level. These are pointwise traceless and represent the classes written in the proof, since [tr A_z]=−x and [tr A_h]=−y. The cohomological trace identities alone do not imply that an arbitrary choice of harmonic x,y makes the original curvature expressions pointwise traceless.

2. **Complete bilinear classification.** The displayed decomposition V₂⊗V₂=V₄⊕V₂⊕V₀ is complete, with V₂ entirely alternating. The trace pairing identifies the scalar symmetric summand; the bracket identifies the alternating summand. Hence the equivariant bilinear Hom space to sl₂ has dimension one, and the symmetric Hom space is zero. Scalar-valued bilinear terms disappear after trace-free projection. This proves completeness within the expressly defined coefficient-free, derivative-free bilinear scope, including the corresponding homogeneous quadratic expressions in two labeled inputs.

3. **Intrinsic mixed bundle and block parity.** The mixed summand M=Ω¹_z⊗Ω¹_h is embedded by α⊗β↦α∧β. Under factor exchange this embedding equips M with the geometric action that includes the minus sign from reordering the two holomorphic factors. One must not append that sign again after pulling back differential-form products. Naturality gives τ*C=[B_h,B_z]=−C exactly as claimed. This is the geometric action inherited from Ω²_X, rather than a bare tensor-flip convention.

   An equivariant L consequently sends C to the odd sector. For the retained conclusion the revised §3 explicitly supplies P_ret=P_ret P_+, where P_+=(1+τ)/2; a block-equivariant projector with block-even image has this property. Even image by itself is insufficient for an arbitrary linear projector. With this verified projector convention, P_ret L(C)=0. Odd auxiliary data or the odd component of a coefficient transformation can evade this parity exclusion, but cannot guarantee a nonzero retained value.

4. **Discriminant identity.** With p=tr(U²), q=tr(UV), r=tr(V²), polarized Cayley–Hamilton gives U²=(p/2)Id, V²=(r/2)Id and UV+VU=qId. Thus UVUV=qUV−(pr/4)Id and [U,V]²=(q²−pr)Id. Cyclic trace also gives tr([U,V]U)=tr([U,V]V)=0. There is no missing factor of two or sign.

5. **Chern specialization.** The imported normalized HM classes c₁=−H and c₂=4H² give tr A²=−7(x+y)² and tr B²=−(15/2)(x+y)². The direct holomorphic-degree decomposition yields p=−(15/2)x² and r=−(15/2)y². Its mixed part is 2q, since tr(B_hB_z)=tr(B_zB_h), giving q=−(15/2)xy. Therefore q²=pr and C²=0 in H⁴(End(E)⊗ω_X). This is a cohomological equality, not a representative-level harmonic or matrix identity.

## Sources and scope

Checked the local PROOF.md and its three listed local references: the relative Chern constraints, target-relative Atiyah-square detectors, and ordered Yoneda-product addendum. The normalized Chern inputs and retained-sector identification are treated as imported premises; no claim is made here to have independently fetched or verified the public comments.
