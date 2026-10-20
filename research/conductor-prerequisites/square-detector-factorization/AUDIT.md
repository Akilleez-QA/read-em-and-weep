> Current actual-bundle specialization: the degree-one-kernel exclusion rules out a=1. The a=1 formulas below are historical conditional algebraic derivations, not current actual alternatives.

> Historical mathematical review retained with the source. This is not a new independent review or a formal verification certificate.

# Independent audit of the line-and-ideal-square factorization

## Verdict

The statements in `PROOF.md` are correct under its stated inputs: the saturated-line bound, a locally free rank-two E, a smooth conic C, and characteristic zero. In particular, no error was found in the nonreduced zero-scheme calculation, the rank-two kernel, the ambient Ext factorization, or the exact 2C line-membership criterion. The distinction between all sections on 2C and globally extendable sections is essential and is handled correctly.

The following checks supply details and a stronger criterion: in the nonzero-detector branch, **all** sections on 2C extend if and only if Z is disjoint from C. The actual extension and ambient map are still needed to evaluate the detector.

## 1. Negative endomorphisms and restriction kernels

For k>0, the trace and determinant of f:E→E(-k) vanish. Twisted Cayley–Hamilton gives f(-k)f=0. Its saturated kernel is a line bundle L=O(b), and the induced nonzero map from I_Z'(-2-b) to O(b-k) gives

    0 ≠ H⁰(O(2b+2-k)).

Thus b≥0, including k=1. The uniqueness argument applies: a second nonnegative saturated line has zero composite to I_Z(-2-a), so is contained in K; saturation forces equality. Therefore every negative-twist endomorphism is j times a section of N(-k). This proves the stated dimensions and the uniform vanishing at twists at most −5. The compositions vanish as claimed because the quotient followed by the line inclusion is zero.

The entries of j locally generate I_Z²=(x²,xy,y²). This ideal has no codimension-one support. Over every height-one local ring, j is a primitive vector, and B_W/jN is torsion-free. Equivalently, if a rational multiple of j has regular entries, its coefficient has no divisorial poles and hence is regular on the smooth surface. Since any local equation q^m of mC acts injectively on a torsion-free sheaf, Tor₁(B_W/jN,O_mC)=0. Thus j remains injective after restriction to every mC, even when Z meets C nontransversely.

The restriction kernel in (5) follows from the usual divisor sequence and the negative-twist formula. Its dimensions are exactly as stated: 0 for a=0 on C, 3 for a=1 on C, and 0 for either a on 2C. No surjectivity onto the full restricted section space follows from this step alone.

## 2. The ideal square and its kernel

In a local frame, write the line inclusion as (x,y), and put

    j = [−xy, x²; −y², xy].

For A=[u,v;w,−u], trace(jA)=x²w−2xyu−y²v. Therefore the image of trace contraction is exactly (x²,xy,y²), not I_Z, its radical, or a symbolic approximation. At points of Z, x,y are a regular sequence. The Hilbert–Burch relations of their ordinary ideal square have a free rank-two syzygy module, identified with symmetric multiplication by (x,y). This proves

    0→K⊗E⊗det(E)⁻¹→B_W→I_Z²⊗N⁻¹→0.

The trace/Sym² convention can change the displayed maps by a nonzero scalar, but the maps may and must be normalized together so that contraction is literally the trace dual of j. All images, kernels, and vanishing criteria are independent of that scalar.

The length calculation is valid for nonreduced Z: I_Z/I_Z² is locally free of rank two over O_Z, so length(O/I_Z²)=3 length(Z). A Chern-class check gives

    c₂(E(a+2)) = length(Z),
    c₂(B_W) = 4 length(Z) − (2a+2)² = 60.

After twisting by −2 the kernel is E(a). The defining extension twisted by −a−1 has outer terms O(−1) and I_Z(−3−2a), proving H⁰(E(−a−1))=0. Rank-two duality and Serre duality then give H²(E(a))=0. The long exact sequence proves the H² isomorphism in (3); the zero-dimensional quotient proves the second H² isomorphism there. No vanishing of H¹(J) is needed.

## 3. Ambient duality with a non-locally-free ideal sheaf

Although J is not locally free at Z, the asserted Ext² identification is valid. Derived adjunction for the codimension-two regular embedding gives

    RHom_Y(i_*J,ω_Y) ≅ RHom_W(J,ω_W)[−2]

at the global derived-Hom level. Hence Ext²_Y(i_*J,ω_Y)=Hom_W(J,ω_W). The identity Hom(I_Z²,O_W)=O_W holds because a zero-dimensional ideal on a smooth surface agrees with O in codimension one and has reflexive hull O.

Pullback along c' is the trace-dual map j on H⁰(N(−1)); pullback along actual ambient restriction is the original Gysin transpose. Thus the map v_e in (4), its scalar-ideal vanishing test, and the warning that its rank is not determined by Z or the parameter count are all correct.

## 4. Exact line-membership on 2C

The divisor sequence for N(−1)=O(2a+1) has left term O(2a−3). Its H⁰ vanishes for a=0,1, and its H¹ vanishes on P². Therefore restriction of coefficient sections to 2C is an isomorphism. Since j_2C is an injection of sheaves, left-exactness of H⁰ proves (6) and the quotient-membership criterion exactly as written.

The saturation formula on C is also exact. If I_Z O_C=(t^r), the restricted inclusion K|C→E|C loses order r and the restricted nilpotent line loses order 2r. Thus the saturated nilpotent line is N(−1)|C(2R), with quotient length 2 length(R). This does not create any additional globally extendable sections.

## 5. Additional full-section criterion

The independently proved `SUPPLEMENT.md` strengthens the result: in the nonzero-detector branch, the full restriction map to 2C is an isomorphism if and only if Z is disjoint from C. If d=length(Z∩C)>0 and ℓ=length O_W/(I_Z²,q²), then ℓ≥2d and there are at least ℓ−1 extra sections for a=0, or ℓ extra sections for a=1. No exact extra dimension is asserted. The proof retains nonreduced intersections and uses the torsion of (B_W/jN)|2C.

## Scope of this audit

No actual HM matrices, selected component ranks, ambient source classes, or zero schemes were computed. This audit verifies the structural statements and the separate supplement; it does not remove the need for the actual extension and ambient map when evaluating the detector.
