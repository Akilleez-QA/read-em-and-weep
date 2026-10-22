# Positive Serre residue and its canonical cone scalar correction

## Result and boundary

Use the actual regular spinor section on X=P_stack(1,1,2,2):

    0 -> O_X --sigma--> G -> I_Z(2) -> 0.

The actual homogeneous vertex scheme, not just its support, is the one established in NORMAL-QUADRATIC-NONZERO-BY-SERRE-RESIDUE-DOUBLE-COVER.md. Write L=P(W), and V=Sym^2(Wprime), A=Sym^2(W), D5=Sym^4(W). All twists below are physical hyperplane twists.

The positive Serre-residue quotient is canonically represented by the pure vertex cover-degree-four component:

    H0(V O_L(2)) = P4+D5  -> H1(I_Z(2))_+                 (1)

and this arrow is an isomorphism. In particular one cannot discard the D5 summand by an ambient quadratic adjustment without also creating a conic residue.

For a negative quadratic a, every residue r in the space on the left of (1) has a unique lift of a r in the polynomial subspace

    D5 tensor H0(O_L(2)) = D5 tensor A

of positive-quadratic times negative-quadratic quartics. These polynomials vanish on the conic. This gives a canonical scalar correction for the Serre operator with symbol a h D_a, once its actual residue r is known. It does not calculate that residue, lift the operator to 2Q, or evaluate the third Bockstein.

## 1. The full positive residue quotient

The actual vertex even quotient is graded for the negative block torus. Its positive pieces at physical twist2 are the cover-degree-zero piece O_L(2) and cover-degree-four piece V O_L(2). The cover-degree-two and cover-degree-six pieces have negative physical parity and do not enter this assertion. The cubic even quotient identification is supplied by UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md together with the actual cubic identification used in the Serre double-cover proof.

The reduced conic contributes H0(O_C(2))=D5. Hence

    H0(O_Z(2))_+ = A + (P4+D5) + D5.

This is a graded support decomposition, not an assumed splitting of an arbitrary filtered sheaf. Ambient positive quadratics are A+D5. Their A component restricts isomorphically to the degree-zero vertex component and vanishes on C. Their D5 component restricts isomorphically to C; it can also have a degree-four vertex component. Consequently the image has zero intersection with the pure degree-four vertex space, and its quotient is exactly that space. The vanishing H1(O_X(2))=0 gives (1) through the ideal sequence.

Equivalently, the conic restriction kills any putative D5 quadratic in H0(I_Z(2))_+, and the reduced vertex restriction then kills A. Thus H0(I_Z(2))_+=0. Nothing here chooses actual coefficients or evaluates a map matrix.

## 2. A canonical inverse after multiplying by a

The actual cubic relation gives the exact sequence

    0 -> Wprime O_L(-5) -> D5 O_L(-2) -> V O_L -> 0.

Twisting by4 yields

    0 -> Wprime O_L(-1) -> D5 O_L(2) -> V O_L(4) -> 0.

Both H0 and H1 of its left term vanish. Therefore the induced map

    H0(D5 O_L(2)) -> H0(V O_L(4))                         (2)

is an isomorphism. This is a geometric isomorphism for the actual nonzero complete cubic relation, not an assertion that nonzero representation-theoretic legs have nonzero composite.

Define u(a,r) as its unique inverse image of a r. As an ambient polynomial, u has positive cover-degree4 and negative ordinary degree2, hence physical degree4. It vanishes on the conic and restricts to a r on the vertex. It is equivariant and bilinear in a,r. The choice of the identification of the cubic quotient with V cancels between (2) and a r.

## 3. The residue nine-space embeds in the adjoint obstruction space

The regular-section square sequence, before the twist used in the third obstruction, is

    0 -> G -> B_Q(2) -> I_Z^2(4) -> 0.                    (3)

Its positive square-ideal global sections vanish. Indeed ambient homogeneous quartics have positive cover degrees0,4,8. The first two inject into the square quotient, because the square ideal has minimum cover degree6. The degree8 kernel is H0(P4 O_L(-4))=0 from the actual square relation sequence. Restricting to the vertex already proves the required injection, without any selected coefficient calculation.

The section sequence and H1(O_X)=H2(O_X)=0 identify H1(G)_+ with H1(I_Z(2))_+. Thus (3) injects the nine-dimensional residue space into C=H1(B_Q(2))_+. Multiplication by every negative quadratic a kills this image: the diagram obtained by multiplying (3) by a factors its cohomology map through H1(G(2))=0. This is a sheaf-level explanation, not just a character obstruction.

For the Serre involution marking with subline1 and quotient-1, H1(G)_+ has eigenvalue-1: its identification with H1(I_Z(2)) includes the quotient marking. The G term in (3) carries a second minus sign from the determinant identification B_Q(2)=Sym^2G tensor (det G)^(-1)(2). Hence the embedded residue nine-space has eigenvalue+1 in C. This keeps the two signs separate; omitting the determinant sign would put the residue space in the wrong eigenspace.

## 4. Application to the actual tangent operator

Let h belong to the positive D5 quadratics and D_a be the actual negative sl(W) vector field. Locally at the vertex h has cover-degree4; D_a preserves cover-degree. The actual homogeneous (3,5) complete intersection has socle degree6. Therefore h D_a sends both generators into the ideal, in degrees7 and9. Near the reduced conic it also preserves the ideal. Thus theta=h D_a preserves the entire Z scheme.

Use the natural D_a action on det G=O_X(2), multiplied by h. This specifies the determinant-line component of the derivation. The induced action on the Serre dualizing residue line then gives an intrinsic residue derivative

    r_theta = epsilon^{-1} L_theta(epsilon) in H0(O_Z(2)).

The conic component is zero: D_a acts on the negative normal W-plane with trace zero, and in a positive-coordinate determinant frame its determinant-line action is zero. At the vertex the relation matrix coefficients for theta have diagonal cover-degree4, as does the determinant-line term. Thus r_theta belongs to the pure cover-degree4 space in (1). This definition retains the determinant-line contribution; a bare trace of a generator relation matrix without that contribution is not invariant under frame changes.

For the symbol a theta the residue is a r_theta, since derivations on the ideal and on the determinant line are multiplied together by a. Formula (2) supplies a global scalar u(a,r_theta). The usual Serre-extension compatibility equation can therefore be solved: choose scalar actions on the subline and quotient whose difference cancels that residue. If the fixed determinant requires opposite scalar actions, take the appropriate signed half of u on the subline. The sign depends on whether the residue action is defined on the extension line or its dual; existence and uniqueness within the polynomial subspace (2) are unchanged. Once compatible end actions are fixed, their difference is an extension obstruction in Ext^1(I_Z(2),O_X(4)). The local-to-global Ext sequence identifies this obstruction with its residue, because Hom(I_Z(2),O_X(4))=O_X(2) and H1(O_X(2))=H2(O_X(2))=0. Thus vanishing of the corrected residue kills the global obstruction, not just its localization. Functoriality of Ext then supplies an operator on the middle bundle G with the required symbol. This is a cone statement only.

One useful necessity check is available at twist2. The proved primary square calculation gives

    H0(G(2))_+ = A+D5 = sigma H0(O_X(2))_+.

Hence any positive global operator on G of twist2 sends sigma to a multiple of sigma. Such an operator necessarily preserves the section line. This explains why the residue of h D_a cannot be ignored merely because h D_a is tangent to Z. At twist4 we assert existence of the explicitly corrected section-preserving operator, not that every operator preserves sigma.

## Dependencies and reproducibility

This deduction uses the actual scheme homogeneity from the Serre double-cover proof; the actual cubic identification plus its universal quotient theorem; and H0(G(2))_+=A+D5 from WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md. It does not replace these with a generic model.

Run verify_positive_serre_residue_correction.py for the character and degree checks. The remaining normal problem is extending this cone operator across 2Q with the actual first-normal bundle, or the equivalent constant secondary operation. No third-value vanishing or nonvanishing is asserted.
