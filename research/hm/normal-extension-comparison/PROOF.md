# Comparing the first-normal torsor with the normalized vertex transition

Work over C with the actual marked cone bundle F_Q, B_Q=End0(F_Q), its invariant nilpotent N, and the physical quadric equation q. Write Γ for the binary icosahedral symmetry group. All deformations below preserve the determinant and the marking on Q. Let T be the affine line of Γ-equivariant first-normal extensions to 2Q; its translation space is D=H1(Q,B_Q(-2))^Γ.

The class κ of [PR778](https://github.com/Akilleez-QA/read-em-and-weep/blob/e527b939f9a8f5cf8967f32048a23a9d830d77c9/research/hm/normal-transition-channel/PROOF.md) extends to every member of T. There is a canonical linear isomorphism

    R:D → H1(L,J)^Γ,    J=P4⊗O_L(-8),
    κ(E+ξ)=κ(E)+R(ξ),

where the plus convention means multiplying source-to-target transition matrices on the right by I+q c_ij, with c representing ξ. The two sides use the same convention. The diagonal composite of R is the physical-even diagonal component of ordinary restriction to L.

The reference-origin comparison in Section 6 identifies the unique κ-zero extension with the midpoint. Consequently κ of the actual ambient endpoint is nonzero, because the actual endpoint extends to 3Q while the midpoint does not. No numerical normalization of κ or higher obstruction value is determined.

## 1. Pinned inputs

The following sources are all at commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, under research/hm/order-four-quadratic-load/:

- [MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md): D is a line; the block transformation φ=diag(1_V,μ1_W), μ²=−1, acts on T by reflection and hence on D by −1; H0(B_Q)^Γ=0. The midpoint need not extend to 3Q.
- [NEGATIVE-VERTEX-EVALUATION-SCALAR.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/NEGATIVE-VERTEX-EVALUATION-SCALAR.md): the actual physical inversion eigenlines are F_Q(2)|L=O(5)_−⊕O(-2)_+.
- [ACTUAL-CONIC-RESIDUE-FORCES-VERTEX-SERRE-COCYCLE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CONIC-RESIDUE-FORCES-VERTEX-SERRE-COCYCLE.md): the actual marked vertex-open bundle differs from its homogeneous vertex presentation by I+tN, of matrix weight eight.
- [ACTUAL-NORMAL-CLASS-HAS-A-NONZERO-LOWEST-VERTEX-DIAGONAL.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-NORMAL-CLASS-HAS-A-NONZERO-LOWEST-VERTEX-DIAGONAL.md): the extracted trace-degree-eight component of a nonzero global invariant normal class is nonzero in J_eta=P4 O(-8), with exact sequence 0→V O(-10)→J_eta→O(-2)→0 and triangular law r↦r+2pd. Its proof uses the actual square-shadow identity and the next input, not dimension equality.
- [ACTUAL-NORMAL-TRACE-HAS-NONZERO-NILPOTENT-COMPONENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-NORMAL-TRACE-HAS-NONZERO-NILPOTENT-COMPONENT.md): the actual square shadow δ(αe_v+βn8) has β≠0. This is proved through restriction of the dual class to the first conic neighborhood, including its H0 connecting map.

PR778 constructs J from the actual normalized homogeneous transitions and proves diagonal detection H1(J)^Γ≅H1(O(-2))=C. We use that construction, not a choice of an abstract isomorphism between rank-four bundles.

## 2. The global variation line is physically even

Let ι be the physical inversion on coordinates. In the block convention above ι=φ²=diag(1_V,−1_W). The derivative of the affine reflection action of φ on T is −1 on D, so the square of this derivative is +1.

One must check that squaring the chosen cone marking of φ gives the actual action of ι on D. The two markings differ by a Γ-equivariant automorphism of F_Q. Every such automorphism is scalar: its trace-free part belongs to H0(B_Q)^Γ=0, and H0(O_Q)=C. Scalar automorphisms act trivially on End0(F_Q) and on its deformation cohomology. The normal equation q is fixed by both block transformations, so there is no omitted normal-line character. Consequently the derivative square is exactly physical inversion on D, and

    D=D^+.

This argument does not replace physical inversion by stack stabilizer parity, or infer physical parity from the word invariant. Since the actual ambient extension is physically equivariant and the induced physical action on its translation space is identity, every point of T is fixed by physical inversion. More concretely, after refining to a physical-stable cover, an invariant deformation class admits an even representative by averaging its cocycle and cochains over this finite involution; adding that cocycle to the actual extension constructs the desired even transition matrices on 2Q. Averaging over Γ as well gives the same equivariant deformation class.

## 3. Construction of R as a coefficient quotient

Normalize N12 on the fixed cone once, using PR777 as in PR778. This normalization is independent of the extension to 2Q: N and the cone bundle are fixed. In these regular physical frames, cone transitions have homogeneous term

    T0=[[a,0],[c2,d]],

and all higher terms have nonnegative matrix weights, with the first possible positive weight four. Scalar weight-four terms have no effect in the adjoint. The homogeneous lift of T0 is exactly multiplicative, as proved in PR778.

Every regular even trace-free adjoint coefficient has matrix weight at least zero. Its weight-zero truncation is [[t,0],[ell2,−t]]. Changing frames transports that truncation by Ad(T0); positive-weight transition terms cannot feed into weight zero. Tensoring with the normal ideal O_Q(-2) gives precisely

    0 → V O_L(-10) → J → O_L(-2) → 0.

Thus restriction to the formal vertex neighborhood followed by this finite coefficient quotient is a morphism of Čech complexes. Define R by its induced cohomology map on D. Only a finite jet is used; no convergence claim or direct-sum/completion interchange is needed. A change c↦c+δb changes the coefficient by the J-coboundary of the weight-zero truncation of b. A refinement or change of regular normalized frame gives the canonical identification from PR778. The resulting map is independent of representatives and natural under Γ.

The diagonal of the weight-zero truncation is simply the diagonal value at the reduced line L. At L the lower degree-two term vanishes. The physical-even part of B_Q(-2)|L is exactly its diagonal O_L(-2), since the two eigenlines have opposite signs and both off-diagonal Hom lines are physical-odd, whereas the even twist −2 contributes no sign. Therefore the diagonal composite of R equals ordinary restriction to L followed by this intrinsic physical-even summand. This also provides a description without the lower-entry coefficient choices.

## 4. The map is the existing nonzero leading-component map

The source ACTUAL-NORMAL-CLASS-HAS-A-NONZERO-LOWEST-VERTEX-DIAGONAL.md uses “trace degree eight” for exactly the matrices [[t,0],[ell2,−t]] of physical twist −2: multiplication by the leading nilpotent n8 gives trace degree eight. Its diagonal, lower coefficient line, and actual triangular transport r↦r+2pd are exactly those just constructed. Twisting F_Q by the stack spinor line in that presentation does not change End0 or its conjugation transition law. Thus J_eta is identified with J by the actual coefficient construction, not by their abstract splitting types.

The possible actual conic correction has matrix weight eight and hence cannot change this coefficient quotient. The further weight-four cone gauges used to kill N12 likewise act identically on weight-zero adjoint coefficients. Weight-zero changes merely make the canonical simultaneous identification of J and J_eta. Consequently R is the same leading-component map as in that source on the physically even invariant line.

For completeness its nonvanishing mechanism is as follows. The actual global square shadow of a nonzero normal generator η is δ(αe_v+βn8), with β≠0 by the conic-neighborhood duality theorem. On the vertex open the constant e_v is already global, so the leading shadow is βδ(n8). The exact degree-eight square-ideal sequence has middle term Sym8(U) O_L(-4), whose H0 is zero. The nonzero nilpotent section n8 therefore has nonzero connecting image. The actual trace map identifies the rank-four coefficient J_eta with that degree-eight square-ideal coefficient, so the extracted class is nonzero. This proves R(η)≠0 through the actual maps. Since D and H1(J)^Γ are lines, R is now, and only now, an isomorphism.

## 5. Affine variation, and what it does not identify

Let P_ij represent E on 2Q and c_ij represent ξ with the source-frame convention. Since q²=0 there, the modified transitions

    P'_ij=P_ij(I+q c_ij)

represent E+ξ exactly. The normal-line transition factor is retained in c_ij∈B_Q(-2). Both extensions have the same cone transition and the same N12 normalization. As q has weight four, the trace-free weight-four transition coefficient changes by exactly q(c_ij)_0. Products with positive-weight corrections have weight at least eight; products of two normal corrections vanish on 2Q. Dividing out the same q ideal factor gives

    Z'_ij=Z_ij+(c_ij)_0,

and hence κ(E+ξ)=κ(E)+R(ξ). This proves the affine law without any lift to 3Q or to an ambient vector bundle.

Because R is an isomorphism, κ:T→H1(J)^Γ is an affine bijection. There is exactly one E_zero in T for which the normalized trace-free weight-four ambient defect is removable. If E_actual and m are the distinct actual endpoint and midpoint, then κ(E_actual)−κ(m)=R(E_actual−m) is nonzero. In particular those two κ values cannot both vanish.

The affine law alone makes no origin identification: E_zero is defined by the homogeneous transition reference near L, whereas m is defined by the global reflection and the boundary of N. Section 6 supplies the additional compatibility of these reference conditions. None of these assertions computes a fifth-section obstruction or removes the separate harmonic transport defects emphasized in PR778.

## 6. The block reflection fixes the homogeneous-reference origin

### Lemma: naturality under a marked block automorphism

Let φ be a block coordinate automorphism fixing the ambient equation q and acting on the fixed cone bundle through a marked isomorphism M:φ*F_Q→F_Q. Suppose its induced adjoint action sends the fixed N to a nonzero constant multiple of N. Suppose it commutes with physical inversion on the adjoint. Then the normalized coefficient construction satisfies

    κ(φ·E)=φ_J κ(E),

with no additive offset, where φ_J is the linear map on H1(J) induced by the leading homogeneous part of M, the coordinate map, and the normal ideal line.

#### Proof retaining the marking

Use normalized regular physical frames for F_Q and their pullbacks by φ. Both N12 terms are zero, including after rescaling N by the stated constant. Coordinate block scaling preserves the cover grading. The regular matrix of M therefore has nonnegative matrix weights, with homogeneous part M0 lower triangular of the form [[a,0],[c2,d]]. Its two diagonal entries are units since M is invertible on L. Write M=M0(I+Y4+weight≥8) on Q. The weight-eight intertwining identity identifies the leading nilpotents. The weight-twelve identity then gives [Y4,n8]=0, because both normalized weight-twelve coefficients are zero and the twisting scalar is constant. By the regular weight-four ad_n injection, Y4 is scalar modulo its trace.

The homogeneous lower-triangular matrix M0 has a canonical ambient lift. Products, inverses, and the coordinate substitution under φ commute exactly with this lift: the only nonconstant entry is ordinary transverse-linear, and products of lower entries never occur. Consequently the relation between the two leading transition cocycles, induced on Q by M0, is also an exact relation between their ambient homogeneous references. There is no reference defect here, even away from Q.

Choose arbitrary local lifts of the full marking M to 2Q, reducing to M on Q. Such lifts exist on a refined affine cover since the bundles are free there; they are only local changes of frames, not a claim that M extends to an isomorphism between any global first-normal bundles. Modulo weight eight and scalar corrections, each local lift has the form

    M0(I+q Z0).

Indeed its trace-free weight-four part restricts to zero on Q by the previous paragraph, and homogeneous divisibility by q gives Z0 in the local coefficient sheaf J. There may be a scalar weight-four part, but its adjoint effect is zero and its products with weight-four terms have weight eight.

Transporting the pulled-back transition cocycle by these local lifts is exactly how the marked action φ·E is represented. The exact relation of homogeneous references just proved shows that its qZ coefficient is φ_J applied to the old coefficient, plus the Čech coboundary of the local Z0. Therefore the cohomology class is φ_Jκ(E), with no surviving affine term. The conclusion is independent of which local lifts of M were chosen, because a different lift changes only that local cochain. This proves the lemma.

### Application to the Serre reflection

For φ=diag(1_V,μ1_W), μ²=−1, the pinned midpoint theorem supplies the Γ-equivariant cone marking and states that N has eigenvalue −1. The marking itself can be taken physically even, not merely commuting with inversion on the adjoint. The two orders of composing the marking with physical inversion are Γ-equivariant isomorphisms between the same cone bundles and differ by a scalar because H0(B_Q)^Γ=0. Since inversion squares to the identity, this scalar is ±1. If it were −1, the marking would exchange the physical eigenlines on L. But φ fixes L pointwise, and O(5) is the unique maximal-degree line subbundle of O(5)⊕O(-2); an isomorphism must preserve it and cannot map it into O(-2), since Hom(O(5),O(-2))=0. Thus the scalar is +1. The marking preserves the ordered physical eigenlines and has the nonnegative weighted triangular expansion used in the lemma. Hence the lemma applies. Changing a determinant marking by a scalar square root does not change this argument or the adjoint action.

The diagonal coefficient of J is O_L(-2). The map φ fixes L projectively, scales each negative homogeneous coordinate by μ, and acts on its natural O(-2) coefficient line with character μ^(-2)=−1. Conjugation by the lower-triangular M0 fixes the diagonal quotient. The base Čech coordinate v/u is unchanged. Thus φ_J is −1 on H1(O_L(-2)), and therefore on H1(J)^Γ by the diagonal detection isomorphism. It follows that

    κ(φ·E)=−κ(E).

The midpoint m is the unique fixed point of the affine reflection φ on T. Characteristic zero now gives κ(m)=−κ(m), hence κ(m)=0. As R is an isomorphism, this identifies the unique κ-zero first-normal extension with m.

The actual ambient endpoint E_actual extends to 3Q. The midpoint does not: the pinned midpoint theorem gives obstruction −c²/(4d)≠0. Therefore E_actual≠m, and the affine variation law yields

    κ(E_actual)=R(E_actual−m)≠0.

This proves only nonvanishing of the actual normalized first ambient transition class, not its scalar in an independently normalized Euler basis. It does not evaluate β4, a fifth-section obstruction, or an algebraicity obstruction. A nonzero ambient transition class is compatible with an actual ambient bundle; it obstructs only removal of this particular weighted transition layer relative to the homogeneous reference.

### Checks and potential failure points addressed

- The order-four coordinate map acts on N by a constant scalar, from the actual Serre marking theorem; an unspecified base-dependent rescaling would require extra terms and is not used.
- A global lift of the cone marking is neither assumed nor needed: arbitrary local lifts contribute only an explicitly identified J-coboundary.
- Exact ambient multiplicativity is used only for lower-triangular weight-zero matrices, not for arbitrary harmonic lifts.
- Physical parity is checked on the adjoint using scalar marking ambiguity, not inferred from stack parity.
- The coefficient μ^(-2) includes the normal ideal twist; forgetting it would incorrectly make the diagonal action positive.
- The affine offset is killed by the exact homogeneous-reference compatibility, not by the fact that the source and target are lines.


## Verification and scope

The new argument consists of the marking check for physical parity, the finite coefficient quotient on Čech complexes, its identification with the pinned actual leading map, the exact square-zero transition multiplication, and the exact marked-reference compatibility for the block reflection. Nonvanishing of the leading map is a cited earlier theorem, not a newly discovered scalar calculation. No actual coefficients, points, source derivatives or selected-instance ranks were evaluated, and no scan or large computation was performed. This is an authored structural proof, not a formal proof-assistant certificate.
