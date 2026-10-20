# Independent audit: rank-one metric radical identity

## Verdict

The proof in PROOF.md is correct as stated, conditional on the actual regular supported correction and square avoidance established there. The new integral Picard relation and all displayed numerical consequences pass independent checking. The metric-fiber corollary is valid but is superseded by the stronger intrinsic metric-extension lemma once U⊂H is regular.

## Checks

1. A nowhere-zero projective metric generically of rank one on an integral complete curve has rank one everywhere: rank≤1 is closed and rank zero is excluded. Consequently its radical is a rank-two subbundle after normalization.

2. For S=P_T(R) parameterizing lines and L=O_S(−1), a square L² lies in the metric kernel. Projecting the actual correction to E/L eliminates its splitting shear. Thus it defines a global section of F=(π*E/L)⊗π*U⊗L^(−2). Square avoidance makes this section nowhere zero, giving c₂(F)=0 integrally in CH²(S).

3. With ξ=c₁(L*), the line convention gives ξ²+rξ=0 on this ruled surface. For G=π*E/L, c₁(G)=e+ξ and c₂(G)=eξ+ξ². The rank-two twist formula yields

    c₂(F)=(eξ+ξ²)+(e+ξ)(u+2ξ)+(u+2ξ)²
          =(3e+5u)ξ+7ξ².

All products of two classes pulled from T vanish. Pushforward gives 3e+5u−7r=0 in CH¹(T), including its Picard information, not only numerical degree.

4. Substituting e=−n−u and r=−p−u gives 7p+9u−3n=0. Therefore

    (det P*)^7≅(U*)^9⊗N³,
    7 deg(det P*)=9 deg(U*)+3 deg N.

There is no sign error. If Q=(U*)³⊗N and T₀=Q⊗(det P*)^(−2), then T₀³≅det P* and T₀^7≅Q follow algebraically from (det P*)^7≅Q³; this remains valid in the presence of Picard torsion.

5. At rank one h descends to a nondegenerate pairing (E/R)⊗(E/R)→M, hence M≅(E/R)² with the stated value-line convention. Thus m=2(p−n), 7m=18a−8n, and 7 deg((det E*)²⊗M³)=40a−10n. All signs agree.

6. N, U*, and det P* are pullbacks of the appropriate hyperplane/Plücker bundles, hence have nonnegative degrees. The divisibility and constant-radical exclusions follow. The finite metric-fiber argument correctly uses a curve inside the metric graph, rather than an arbitrary resolving exceptional curve.

## Limits

The relation does not itself exclude a rank-one boundary curve with nonconstant radical. It does not imply nonnegative discriminant degree on a curve contained in the discriminant. It requires actual-family regular support-valued correction; arbitrary independent choices of pointwise tensors do not supply the gluing used on S. The normalized complete curve is smooth over C, so the Chow/projective-bundle computations are legitimate without assuming the ambient metric model smooth.
