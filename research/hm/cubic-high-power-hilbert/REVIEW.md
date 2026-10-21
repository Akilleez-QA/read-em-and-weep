# Independent mathematical review

Verdict: **PASS, conditional on the pinned inputs.** The high-power Hilbert germ is smooth, the dimension is exactly `n^2+635`, and the two forgetful maps have the claimed Artin lifting properties and relative tangent dimensions. No substantive correction is required. This is an independent mathematical review, not proof-assistant verification.

Reviewed file: `PROOF.md` in this directory.

Exact reviewed SHA-256:

    33b5f65e825d1105190b3471bbb435c325f1f9bef7f7fb61cad9bb475f799b99

## 1. Inputs and scope

The argument uses only the following substantive interfaces: projectivity and integrality of V; h0(O_V)=1, h1(O_V)=60, H2(O_V)=0; local triviality and formal unobstructedness of its abstract Artin deformations; H0(Theta_V)=0 and h1(Theta_V)=576; and the ordinary symbol sequence for the line-bundle operator sheaf. These assertions agree with the pinned PR611, PR614 and PR615 texts checked through the repository connector. I additionally read the local PR614 and PR615 proofs, including the explicit affine-gluing argument, rather than interpreting their unobstructedness conclusion as a vanishing assertion for global cotangent Ext2.

PR622 and PR630 provide comparisons, not indispensable steps in the new smoothness argument. The result concerns a sufficiently high complete-power embedding of the same abstract V. It does not concern a new selected HM/source instance or a repair of the original full-adjoint claim.

Serre vanishing applies to the ample L0 on the projective scheme V without a smoothness or Cohen–Macaulay hypothesis. The proof of the lifting theorem needs only that M0=L0^m is very ample and H1(M0)=0. The equality n=P_V(m) is understood in the eventual range in which all higher cohomology vanishes. No effective threshold is claimed.

## 2. Prescribed abstract lifts and the Picard obstruction

For a small extension A' -> A with kernel J, flatness identifies the ideal of X in a given abstract lift X' with O_V tensor_C J. The units sequence is exact as a sequence of sheaves, even though a surjection on global units is not assumed. Its Picard obstruction consequently lies in H2(O_V) tensor_C J and vanishes.

This extends the given line bundle on the specified X', not merely on some abstract lift. It is therefore the required relative formal-smoothness statement. A chosen isomorphism with the line bundle on the reduction supplies any needed marking. Ampleness survives the nilpotent thickening. This step does not assert uniqueness of a line-bundle lift, or existence of a prescribed tensor root.

For first-order pairs, local triviality of the underlying schemes and local frames of the line bundle give the usual Cech classification by H1(A_M0). The symbol sequence, H0(Theta_V)=0 and H2(O_V)=0 yield the exact sequence

    0 -> H1(O_V) -> T_pair,m -> H1(Theta_V) -> 0.

Thus the pair tangent dimension is 636 and the relative tangent dimension over abstract deformations is 60. Scalar automorphisms of the line bundle are present in the category; their presence does not subtract a further dimension from this H1 classification. Combining the prescribed-lift result with PR614 really proves pair unobstructedness.

## 3. Sections, freeness and compatibility of embedding lifts

The section argument is valid for every Artin pair deformation, including a nontrivial deformation of the polarization. At a small extension the exact sequence

    0 -> M0 tensor_C J -> M_A' -> M_A -> 0

makes global-section restriction surjective because H1(M0)=0. The same long exact sequence proves H1(M_A')=0 from the induction hypothesis. Its H0 portion also gives

    length_C H0(M_A') = n dim_C J + n length_C A
                      = n length_C A'.

Lifted sections spanning on the central fiber generate the finite module H0(M_A') by nilpotent Nakayama. The resulting surjection from (A')^n is an isomorphism by the displayed equality of lengths. This avoids assuming cohomology and base change before proving the needed conclusion.

For the relative lifting diagram, the coordinate sections of the already specified embedded A-deformation reduce to the fixed complete central basis. Since H0(M_A) is free of rank n, they are a basis. They can therefore be lifted as that actual basis, rather than replaced by unrelated coordinates. Evaluation is surjective after reduction to V and hence surjective on the Artin thickening. The resulting map to the same fixed projective space restricts to the given embedded family over A.

## 4. Closed immersion and Hilbert functor

The proof's properness argument is legitimate: a flat finite-type Artin deformation is a finite-order thickening of its proper special fiber, and properness is invariant in this base-thickening situation. The morphism to projective space is proper because the target is separated over the base. Its underlying fibers are finite, since the special-fiber map is a closed immersion. Proper quasi-finite therefore makes it finite.

For this finite map, pushforward commutes with the special-fiber base change. The cokernel of the structure-sheaf map consequently has zero reduction to the special fiber and is annihilated by nilpotent Nakayama. This proves the map is a closed immersion; relative generation alone was not mistaken for an embedding criterion.

The source is flat over A', so its image is a flat embedded deformation. More precisely, the fixed-polynomial Hilbert scheme relevant here is

    Hilb^(Q_m)(P^(n-1)),   Q_m(t)=P_V(mt).

This is the finite-type Hilbert scheme to which the local smoothness criterion is applied. If “the Hilbert scheme” denotes the union over all polynomials, local finite type near h_m already suffices. No global finiteness assertion about that entire union is necessary.

## 5. Automorphisms and the exact tangent count

Over the dual numbers, lifts of the fixed central ordered basis form an affine torsor under End_C(H0(M0)), of dimension n^2. Two choices give the same marked embedded deformation exactly when a pair automorphism, inducing the identity on the central fiber, carries one to the other.

The infinitesimal underlying-scheme part of such an automorphism lies in H0(Theta_V), hence vanishes. The remaining part is multiplication by 1+epsilon c with c in H0(O_V)=C. This removes exactly the common-scalar line, not n scalar lines and not the 60 Picard directions. The resulting relative tangent space is pgl_n, of dimension n^2-1.

The independent stabilizer check is also correct. A projective infinitesimal transformation restricting to zero on V has each point of V as an eigenline of a representing matrix. The eigenline locus is a finite union of projectivized eigenspaces, also for a nonsemisimple matrix. Integrality forces V into one of them, and nondegeneracy of the complete-system embedding forces that eigenspace to be the whole ambient vector space. The matrix is therefore scalar. Thus the projective-coordinate arrow is injective, and

    0 -> pgl_n -> T_h_m Hilb -> T_pair,m -> 0

is exact. The dimension is (n^2-1)+636=n^2+635. This argument respects the central markings and does not quotient by all abstract automorphisms of the unmarked variety.

## 6. Actual smoothness and consequences

Starting with any embedded Artin deformation, PR614 supplies an abstract lift; the Picard step extends its line bundle on that chosen lift; and the section step extends the chosen embedding. Thus every required small-extension lifting problem is solved. This is stronger than a tangent-space computation.

The pointwise small-extension criterion in Stacks Lemma 37.12.1, tag 02HX, applies to the finite-type Hilbert scheme over C. It proves smoothness at h_m. At a smooth C-point, the local dimension equals the tangent dimension and the completion is a noncanonical power-series ring in that many variables.

Composition of the two smooth functor maps gives the claimed surjection onto all 576 abstract tangent directions. Its relative kernel is an extension of H1(O_V) by pgl_n, so has dimension n^2+59. The tangent quotient by the projective-coordinate orbit has dimension 636. Because the projective stabilizer has zero Lie algebra in characteristic zero, the orbit has dimension n^2-1 and is not open in this larger smooth germ. No canonical splitting, geometric quotient, coarse-moduli dimension, or representability of either abstract deformation functor is inferred.

The degree-one comparison is consistent: its nonzero H1(L0) obstructs lifting the original ten-section system, whereas H1(M0)=0 removes this obstacle for the high-power problem. Abstract, pair and embedded deformation spaces are kept distinct throughout.

## 7. Sources checked

- PR611 at commit `12b28d33627cc0e8b283d142dc16439a51bb5e00`: https://github.com/Akilleez-QA/read-em-and-weep/blob/12b28d33627cc0e8b283d142dc16439a51bb5e00/research/hm/cubic-branch-transversality/PROOF.md
- PR614 at commit `73fbf75838c91804ca637b5916d6aac217240958`: https://github.com/Akilleez-QA/read-em-and-weep/blob/73fbf75838c91804ca637b5916d6aac217240958/research/hm/cubic-global-deformations/PROOF.md
- PR615 at commit `24bc9b741c287f8ac207bd9df4de4c07c50bea2f`: https://github.com/Akilleez-QA/read-em-and-weep/blob/24bc9b741c287f8ac207bd9df4de4c07c50bea2f/research/hm/cubic-polarized-deformations/PROOF.md
- Picard groups of thickenings: https://stacks.math.columbia.edu/tag/0C6Q
- Serre vanishing: https://stacks.math.columbia.edu/tag/0B5T
- Properness under finite-order base thickenings: https://stacks.math.columbia.edu/tag/09ZW
- Proper morphisms with finite fibers: https://stacks.math.columbia.edu/tag/02OF
- Pointwise infinitesimal smoothness criterion: https://stacks.math.columbia.edu/tag/02HX

No selected HM/source coefficients, points, matrices, derivatives or numerical ranks were evaluated. No large computation, external write, upstream submission or modification of PROOF.md was performed. The review is limited to the stated proof and its declared interfaces, not an independent reconstruction of the entire upstream HM dependency chain.
