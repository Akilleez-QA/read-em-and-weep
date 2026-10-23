# Formal classification of the actual plane-normal bundle up to dilation

Work over C with G=SL2(F5), the actual normalized HM bundle F on P4, its positive fixed plane R, and B=End0(F). All neighborhoods mR below are defined by ordinary ideal powers I_R^m. This is a structural proof: no selected actual coefficient, point, matrix, derivative, jet value, or instance rank is evaluated.

## 1. Exact premises and result

The immediate immutable inputs in Akilleez-QA/read-em-and-weep are:

- PR952, commit 13d0e53e0a64ec6935a2ca83af776942e201c4e9, research/hm/exceptional-polar-obstruction/PROOF.md. Its Section 2 proves the cohomology of the stable plane bundle F_R from the equivariant Steiner resolution. Its exact original geometric inputs are retained.
- PR955, commit bd92a1ad858323966b0596f7b92474ca1766f1a2, research/hm/finite-plane-neighborhood/PROOF.md. Its unique invariant section of B(4) on 3R is supported in I_R^2/I_R^3 and cannot extend to 7R.

Write A=Sym2 W, D=Sym4 W, and V=Sym2 W'. The positive coordinate space is V and the negative space is W; dual conventions give N_(R/P4)=W* tensor O_R(1), and N*=W tensor O_R(-1). These representations have trivial determinants.

Fix the actual marking on R and the determinant identification. The formal restriction of F has a canonical second-normal deformation class

    kappa in L := (Sym2 W tensor H1(R,B_R(-2)))^G,    dim L=1.

Here "second-normal" means the layer I_R^2/I_R^3, not the second thickening 2R. We prove:

1. The actual kappa is NONZERO. This is already known as zeta in HYPERPLANE-SQUARE-SURVIVORS.md, Section 4, at commit db51525015bb7c5e825833d550d08dedf6f6ea96 under research/hm/order-four-quadratic-load/. We give an independent deduction from PR955, but do not count nonvanishing itself as new.
2. Any two existing marked, determinant-fixed G-equivariant formal bundles with reduced restriction F_R are uniquely isomorphic if their kappa classes agree.
3. Every value of L is realized: zero by the pullback of F_R, and every nonzero value by a normal dilation of the actual formal restriction. Thus there is precisely one nontrivial formal type up to normal dilation. No assertion of a global P4-bundle isomorphism or algebraization follows.
4. Every nonzero formal type has the same first failing order for the invariant section in PR955. In particular the order-four versus order-six alternative cannot be changed by an independent higher normal choice after fixing the second-normal class. This does not select that first order.

The genuinely new conclusion is the marked formal classification and its no-higher-choice consequence, not the previously proved nonvanishing of zeta.

## 2. A genuine split ambient neighborhood and the deformation spaces

The complement of the negative projective line L_neg=P(W) admits the canonical projection to R=P(V). In a point of R represented by a line ell in V, its fiber is Hom(ell,W), so this complement is the total space of the normal bundle W* tensor O_R(1), using the fixed self-duality of W. Its zero section is R. This identifies the actual ambient formal neighborhood with the completion of that total space; it does NOT identify F with a pulled-back bundle. The tautological O_P4(1) restricts to the pullback of O_R(1) on this complement. We write rho for the projection.

For a square-zero step (n+1)R -> nR, the difference space for determinant-fixed lifts of a fixed rank-two bundle, and the obstruction to lifting a fixed isomorphism between two existing lifts, use

    T_n = (H1(R,B_R(-n)) tensor Sym^n W)^G.         (2)

Automorphisms inducing the identity at the previous step use the corresponding H0. Obstructions to existence can lie in H2; we do not discard them or assume unobstructedness. Formula (2) follows directly by comparing local transition maps: the ratio of two lifts is 1+c with c a trace-free matrix in the square-zero ideal, and the cocycle condition becomes additive. A change of local identifications changes c by a coboundary. Equivariantly one takes invariants, since averaging over the finite group is exact in characteristic zero. The same argument applies to isomorphism lifting and works with an equivariant affine cover and its refinements.

Stability of F_R implies H0(B_R(-n))=0 for n>0. Indeed a nonzero homomorphism F_R -> F_R(-n) contradicts the slope inequality for stable bundles. Also H0(O_R(-n))=0 and H1(O_R(-n))=0. Thus forgetting determinant introduces no extra difference or identity automorphism space; we nevertheless keep determinant fixed throughout.

The cohomology and Serre duality in PR952 give

    H1(B_R(-2)) = A+V+P+D,
    H1(B_R(-4)) = A+V,
    H1(B_R(-n)) = H1(B_R(n-3))* = 0  for n>=5.

For the last assertion, H1(B_R(t))=0 for every t>=2 follows from the displayed length-two Steiner square resolution: t=2 is its stated cohomology, and for t>=3 all relevant H2 of its line-bundle terms vanish. The center acts positively on B_R and on O_R(1), and by (-1)^n on Sym^n W. Therefore odd n have no invariant cohomology, without any claim that their underlying H1 vanishes. At n=2, A occurs once; at n=4, D is absent from A+V. Hence

    T_2 = L is one-dimensional;    T_n=0 for all n>=1, n!=2.   (3)

The identity-automorphism spaces vanish at every positive step, even before taking invariants.

## 3. Canonical class and compatible uniqueness, not an unobstructedness assumption

The split reference bundle is rho*F_R, with its pulled-back determinant and marking. On 2R every existing marked equivariant bundle is uniquely isomorphic to this reference: the sole difference group T_1 is zero, and the identity-automorphism group is zero. For the actual restriction, use this unique identification to compare its 3R restriction with the reference. The square-zero difference defines kappa in T_2 canonically.

Now let E and E' be two existing formal bundles with the same kappa. Their markings determine a unique isomorphism on R. The preceding argument uniquely extends it to 2R; equality of kappa extends it to 3R. At each subsequent step, the obstruction to extending this already fixed isomorphism is the difference class in T_n, which vanishes by (3). A lift exists and is unique because its ambiguity is H0(B_R tensor I^n/I^(n+1))^G=0 (the scalar part vanishes too). The unique lifts are compatible by construction. Taking their inverse limit gives the unique marked formal isomorphism.

This proves uniqueness for existing lifts. It never deduces existence of a bundle from vanishing H1, nor ignores an H2 obstruction. In particular, comparison with the split reference is valid whenever kappa=0 because both reference and actual bundles already exist at every finite order.

## 4. Nonvanishing forced by finite nonextension

Suppose the actual kappa were zero. Section 3 identifies F with rho*F_R through 7R, compatibly with the marking. On the total normal bundle, the decomposition into homogeneous fiber degrees gives a global section of rho*B_R tensor rho*O_R(4) from every element of

    H0(R,B_R(2)) tensor Sym2 W.

The unique invariant element is nonzero, and its restriction to 3R is exactly the candidate of PR955, because it lies in the degree-two layer and has the prescribed reduced coefficient. Restrict this polynomial section to 7R and transport it through the formal bundle isomorphism. It provides a nonzero invariant extension of the actual 3R candidate, contrary to PR955.

Therefore kappa is nonzero. Only a finite comparison through 7R is needed for this contradiction; no formal existence, convergence, or algebraization theorem is invoked.

## 5. Classification up to normal dilation

For c in C*, let d_c multiply the fibers of the normal bundle by c, fixing R. This is an actual G-equivariant automorphism of the ambient complement (and of its formal completion), and preserves the pulled-back determinant and marking. It acts on degree n normal functions by c^n. Consequently

    kappa(d_c*E)=c^2 kappa(E).                    (4)

Every nonzero vector in the line L equals c^2 kappa(F) for some c because C is algebraically closed. The pullbacks d_c*F supply existing formal bundles with all these classes, while rho*F_R supplies zero. Section 3 proves that these exhaust the marked formal isomorphism classes. The two choices c and -c yield the same marked class and hence the unique marked isomorphism. No identification of different nonzero classes without dilation is asserted.

Existence for all classes here is a consequence of the actual bundle and the geometric dilation, NOT an assertion that an abstract H2 obstruction group vanishes.

As a further consequence, the stabilizer of the actual formal isomorphism class under normal dilations is exactly {1,-1}: equality with its c-dilate forces c^2 kappa=kappa, hence c^2=1, and the converse follows from uniqueness. This remains true for unmarked G-equivariant bundle isomorphisms. Their restrictions to R are scalar by stability of F_R, so rescaling the isomorphism makes it marked; scalar conjugation does not change kappa. Thus the actual formal bundle cannot acquire a full normal C* dilation symmetry. This is a statement about the fixed normal-dilation subgroup, not a classification of all formal base automorphisms.

## 6. The first failing order is constant on the nonzero formal locus

An isomorphism of marked formal bundles induces an isomorphism of their adjoint bundles on every ordinary thickening, compatible with restriction and with the O(4) twist. A normal dilation preserves all ideal powers, and acts on the leading degree-two invariant section by the nonzero scalar c^2. Thus existence or nonexistence of an invariant extension of that section to mR is preserved both by marked formal isomorphism and by dilation. Sections 3 and 5 show that the first failing order in PR955 is the same for every nonzero class in L. If one nonzero formal deformation fails at order four, all do; if one reaches 5R, all do and all fail at order six.

This statement removes an apparent freedom: higher equivariant formal correction terms cannot be varied independently to change that alternative. Their representatives may change under gauge, but any two existing completions with the same second-normal class are uniquely isomorphic. The proof does not evaluate the plane cup-commutator that would distinguish the two alternatives.

## 7. Contribution and remaining gate

The new information is the uniqueness of the entire marked equivariant formal normal type once its second-normal class is fixed, existence of every class by actual dilation and the split reference, and the resulting two dilation orbits. Nonvanishing of the actual class is recovered independently from finite nonextension but was already known. We have not selected the first failing order, determined the opposite-pencil splitting or vertex-extension scalar, asserted a global isomorphism or algebraization, or changed a source/frontier label.
