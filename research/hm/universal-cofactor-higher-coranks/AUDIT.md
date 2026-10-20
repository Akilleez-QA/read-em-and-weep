# Audit checks for higher coranks and incidence resolutions

The four component audits below retain the mathematical checks for PROOF.md and INCIDENCES.md Parts A–C. Application-specific identification assumptions have been replaced by the abstract definition of E. Historical file hashes have been replaced by SHA256SUMS for this exact publication payload. Limitations recorded in a component concern that derivation alone; later components establish the indicated extensions.

## All-corank theorem

# Independent audit: all cofactor coranks and the small crepant resolution

## Verdict and audited version

**Pass for the abstract model, using the preceding divisor/resolution theorem.** The arbitrary-cokernel restriction rank, all incidence dimensions, nonemptiness and irreducibility of the six reduced rank loci, all-corank transversality and the local determinantal models, the absolute rank-four bound, smallness and crepancy, and terminal and rational singularities are correct.


I read the full proof and the proof/audit pair in `../universal-cofactor-normal-form`, together with `INCIDENCES.md`. The operator space E₀=V⊗sl(U) is defined abstractly. Normality and reducedness of D₁ and the cokernel-line resolution come from the preceding packet.

## 1. Constraint rank and fixed-intersection base

The natural trace pairing identifies the annihilator of E₀ inside Hom(U,V⊗U)* with V*⊗C·Id_U. For a c-plane C⊂V*⊗U*, its intersection with C⊗U consists exactly of tensors ℓ⊗Id_U with ℓ⊗U*⊂C. Taking coefficients in the final U factor proves both directions without any noncanonical identification U≅U*. Consequently the dual restriction map has kernel L(C), of dimension k, and the formulas

    rank(r_C)=2c−k,     dim K_C=15−2c+k

are exact for every C.

For fixed k, first choosing L∈Gr(k,V*) and then a (c−2k)-plane in (V*/L)⊗U* gives the correct relative Grassmannian. The condition that the quotient plane contains no full ℓ'⊗U* is open by properness of the incidence with P(V*/L). It is equivalent to L(C)=L, because C contains L⊗U*, so lifting quotient vectors changes nothing about full-factor containment. The kernel-bundle description in the proof supplies a regular inverse. Thus the asserted base is genuinely an open subvariety of that relative Grassmannian, not merely a set-theoretic parameterization.

Its dimension is k(5−k)+(c−2k)(10−c). The constant-rank kernel bundle has rank 15−2c+k, so adding the Gr(5,K_C) fiber gives precisely

    dim I_(c,k)=50−c²+k(2c−10−k).

The formula is only used for nonempty bases and fibers, as required.

## 2. Feasibility, maxima, and exact witnesses

A five-plane J⊂K_C forces k≥2c−10, whereas the full-factor subspace L(C)⊗U*⊂C forces k≤floor(c/2). These inequalities are incompatible for c≥7. It is enough to apply this at c=7 to exclude every larger corank as well.

For c≤5 the correction k(2c−10−k) is strictly negative whenever k>0. Thus k=0 is the unique maximizing stratum. For c=6 feasibility forces k=2 or 3; their corrections are respectively 0 and −3. Hence the only possible maximal contribution has k=2, with dimension14, and the other contribution has dimension11.

The H/E examples for c≤5 have independent generators and direct-sum evaluation rank 10−c. Their dual cokernels lie in V*⊗span(e₂*) and therefore contain no nonzero full ℓ⊗U*. The c=6 example also has five independent generators: one in each of the first two V slots and three in the third. Its evaluation image is exactly the stated four-dimensional direct sum. Its six-dimensional dual cokernel has full-factor space precisely span(v₄*,v₅*), so k=2.

In each maximizing incidence, exact corank c is a nonempty open condition. Its c-plane is then the whole dual cokernel and hence unique; the constant-rank kernel bundle makes the inverse regular. This proves the matching dimension lower bound, rather than merely nonemptiness. The exact dimensions are 49,46,41,34,25,14.

## 3. Irreducibility and component exclusion

The component lower bound used in Section4 is valid. On a smooth 50-dimensional chart, the graph has dimension50, the product with the standard rank variety has dimension150−c², and the ambient product has dimension150. The diagonal/regular-embedding argument gives dimension at least50−c² for every component of their intersection, not only for a distinguished component.

There are finitely many possible k. Every incidence image closure is irreducible and remains inside the closed reduced locus D_c. Exactly one possible k has maximal dimension; its image has that dimension by the explicit exact-corank witness. Every other image closure is strictly smaller and therefore cannot contain an irreducible component of D_c. The unique maximal closure consequently equals all of D_c. The nonempty open S_c is then irreducible too.

The proof correctly confines this argument to reduced supports. Expected dimension and an incidence parameterization alone would not justify reducedness or Cohen–Macaulayness of the pulled-back ideal of minors.

## 4. Smallness and canonical bundle

Over S_c, the dual cokernels form a rank-c bundle, so the inverse image in the cokernel-line resolution is a projective bundle with fiber P^(c−1). Its dimension is therefore exactly

    49−c(c−1),

not merely bounded by this number. For c≥2 the maximum is47 at c=2. The inverse image of the singular locus is a finite union of such strata and has no divisorial component in the smooth49-fold Z. The resolution is small. The additional strict small-map inequality c²−1>2(c−1) is also correct for every c≥2.

Adjunction gives ω_D₁=O_D₁(−13). Over the isomorphism locus S₁, the canonical sheaves have their natural birational identification. Its complement in Z has codimension at least two, so the rational identification has no zero or pole divisor and extends. This proves crepancy as an equality of compatible canonical divisors, beyond abstract line-bundle equivalence.

The independent bundle check is correct: det K=O_P⁹(−2), rank K=13, and the relative canonical bundle of Gr(5,K) is (det S)^13⊗q*(det K)^(-5). The base canonical line O_P⁹(−10) cancels q*O(10), leaving (det S)^13=π*O_D₁(−13). Constant one-dimensional factors cause no geometric issue.

## 5. All-corank transversality and analytic determinantal schemes

The normal-map surjectivity argument from the corank-two packet extends to every exact corank, exactly as the final proof now states. The following argument was independently derived during this audit and then independently confirmed by two further readers before incorporation.

To avoid overloading the letter C, let Q=coker β_J, let p:V⊗U→Q be the quotient, and put W=Q*⊂V*⊗U*. Set R=ker β_J and L={ℓ:ℓ⊗U*⊂W}. The normal derivative is

    ν:Hom(J,E₀/J)→Hom(R,Q).

The map F:E₀/J→Hom(U,Q) induced by p has trace-annihilator consisting exactly of maps A:Q→U such that A p=ℓ⊗Id_U for ℓ∈L. This is the general restriction-rank calculation already proved.

Suppose q:Q→R annihilates im ν under the perfect trace pairing. In a basis a₁,…,a₅ of J, write q(z)=Σ a_j⊗Q_j(z), with Q_j:Q→U. Independent variations of the five basis vectors force each Q_j to annihilate im F. Thus Q_j p=ℓ_j⊗Id_U for some ℓ_j∈L. Because q lands in R, composing β_J q=0 with p yields

    Σ a_j∘(ℓ_j⊗Id_U)=0.

Under the natural injective inclusion E₀⊗V*⊂End(V⊗U), this is exactly Σ a_j⊗ℓ_j=0. Linear independence of the a_j forces every ℓ_j=0. Surjectivity of p then gives every Q_j=0 and q=0. Thus ν is onto.

The Schur-complement and holomorphic submersion argument in the proof consequently gives, at every exact-corank-c point, the germ

    (D₁,J) ≅ ({det X=0}⊂Mat_c,0) × (C^(50−c²),0).

The minor-ideal identity also holds scheme-theoretically in these analytic coordinates. After replacing the invertible block by an identity block of size r=10−c, any (r+s)-minor of diag(I_r,F) is a combination of minors of F of size at least s, hence belongs to I_s(F). Conversely every s-minor of F occurs by adjoining the complete identity block. Thus the full ideal equals I_s(F), with s=c−d+1 for corank at least d. The actual ideals of minors therefore have the claimed generic determinantal analytic models, not just the same set of zeros. In particular every S_c is smooth of its expected dimension, and D₆=S₆ is smooth because D₇ is empty. The proof correctly makes no unsupported claim of a Zariski-local product.

## 6. Terminal and rational singularities: independently checked references

I independently opened the cited author-hosted references and checked the relevant statements and hypotheses.

Kollár’s [Chapter2](https://web.math.princeton.edu/~kollar/book/chap2.pdf#page=5) proves in Proposition3, printedpage5, that exceptional divisors over a smooth variety have positive discrepancy. Lemma12, printedpage8, gives discrepancy invariance under crepant pullback; Corollary16, printedpage10, supplies the terminal criterion. For the proof here, every exceptional divisorial valuation over D₁ is exceptional over Z: a divisor already on Z cannot be contracted by the small morphism. Crepancy identifies its discrepancy over D₁ with its positive discrepancy over smooth Z. Hence the terminal conclusion, and therefore the canonical conclusion, is valid. No Q-factoriality hypothesis or conclusion is needed.

Popa’s [notes, Exercise1.2.5(ii), printedpage7, PDFpage11](https://people.math.harvard.edu/~mpopa/265/Math265-notes.pdf#page=11) state the Grauert–Riemenschneider vanishing used here. Our morphism is projective and birational with smooth source, so the required properness hypotheses hold. The canonical line on D₁ is invertible. Consequently crepancy and the projection formula convert vanishing of Rⁱπ_*ω_Z into vanishing of Rⁱπ_*O_Z for i>0. Proper birationality and normality give π_*O_Z=O_D₁. This establishes rational singularities; the distinction from rationality of D₁ itself is properly preserved. The existence-of-one-resolution formulation is also explicitly justified in Corollary1.2.7 of those notes, printedpage8.

The Popa page fragment and pushforward notation in the proof match the cited source.

## Scope boundary



## Corank-two derivation

# Independent audit: universal corank-two geometry

## Verdict

**Pass for the abstract operator model.** The reduced corank-at-least-two locus is irreducible of dimension 46. At every point of exact corank two, including the special two-plane cokernel type, the normal map is surjective and the analytic germ of the divisor is the three-dimensional ordinary quadratic node times a smooth 46-dimensional germ.


I read the complete proof and the preceding proof/audit pair in `../universal-cofactor-normal-form`. I independently checked the two-plane rank classification, both incidence dimensions, the lower bound on every irreducible component, special-cokernel transversality, and the analytic local and local scheme conclusions. No geometric-module identification is used.

## 1. Starting point and notation

The abstract model defines E=V tensor sl(U), where dim V=5 and dim U=2, embedded faithfully in Hom(U,V tensor U). Thus dim E=15 and dim Gr(5,E)=5(15-5)=50. The inherited divisor D is reduced, with smooth locus precisely the exact-corank-one locus. Consequently its reduced singular locus is the support S of the rank-at-most-eight condition. No scheme-theoretic identification between the global Jacobian ideal and the global size-nine-minor ideal is being assumed.

For a five-plane J the evaluation map has ten-dimensional domain and target. At exact corank two, both its kernel R and cokernel C have dimension two, and the annihilator C* is a genuine two-plane in the fixed ten-dimensional dual output space.

## 2. The exceptional two-planes are classified exactly

The trace pairing identifies the annihilator of sl(U) inside End(U) with the scalar line. Therefore the annihilator of E in the full operator dual is V* tensor C Id. Restriction to W tensor U gives exactly the kernel formula in Section 2; the dimensions of the dual source and the original target are both four.

If a nonzero tensor ell tensor Id lies in W tensor U, its contractions on the U factor span ell tensor U*. That is a two-dimensional space contained in the two-dimensional W, so equality is forced. Conversely this equality supplies the scalar tensor in the kernel. For such W, a second linearly independent covector ell' in the intersection would force W to contain both ell tensor U* and ell' tensor U*, a four-dimensional space. Hence the kernel is exactly one-dimensional in the exceptional case and zero otherwise. The ranks 3 and 4, and kernel dimensions 12 and 11, follow.

The exceptional planes form a closed copy of P(V*) of dimension four. One concrete verification of the stated embedding is its Plucker map: the wedge of ell tensor u1* with ell tensor u2* depends quadratically on ell and realizes the degree-two Veronese embedding in the corresponding Sym^2(V*) summand of the Plucker space. This also verifies regularity of the inverse onto the image; a merely set-theoretic parametrization is not needed.

## 3. Both incidence dimensions and the exact-rank witness

The condition J contained in K_W is closed in the product of the two Grassmannians, so the complete incidence and its special restriction are projective. The fiber over a fixed J is Gr(2,C_J*): choosing W is precisely choosing a two-dimensional subspace of the annihilator of the evaluation image.

Over the nonspecial base, the map defining K has constant rank four. Its rank-eleven kernel is a vector bundle, making the relative Grassmannian smooth and irreducible of dimension

    dim Gr(2,10) + dim Gr(5,11) = 16 + 30 = 46.

The nonspecial base is a nonempty open subset of the irreducible Grassmannian. Over the special P^4, the constant rank is three and the kernel rank is twelve, giving the smooth irreducible special incidence dimension

    4 + dim Gr(5,12) = 4 + 35 = 39.

These two locally closed strata exhaust the incidence, so the incidence and its image have dimension at most 46. This conclusion does not require irreducibility of the complete incidence.

The displayed five independent abstract operators split by the five V coordinates. Three H0 blocks have rank two each, and two E0 blocks rank one each, giving rank eight. The two missing output directions yield exactly the listed cokernel plane. That plane has two-dimensional support in V*, so cannot be ell tensor U*. Thus the witness belongs to the nonspecial incidence.

Exact corank two is open within S. Over this locus the annihilator of the rank-eight image varies regularly as a rank-two subbundle. Accordingly the cokernel plane is unique and provides a regular inverse to the incidence projection there. In particular the nonempty open exact-corank-two part of the 46-dimensional nonspecial incidence has image dimension 46. Its image closure S0 is irreducible of that dimension.

## 4. The component lower bound and irreducibility

The affine chart X of G has dimension 50. The ordinary rank-at-most-eight variety in Mat10 is irreducible of dimension 100-4=96. Hence in the smooth product X times Mat10, of dimension 150, the graph has dimension 50 and X times the rank variety has dimension 146.

The intersection-dimension inequality in a smooth ambient variety applies to every irreducible component, even when the intersection is not transverse or has nonreduced scheme structure. It gives the lower bound 50+146-150=46. Equivalently, one can work in the product of the graph and X times the rank variety, of dimension 196, and impose the 150 local diagonal equations; every component has dimension at least 46. The set-theoretic intersection is exactly S intersect X. Covering G by these charts proves that every irreducible component of S has dimension at least 46.

The image of the special incidence is closed by projectivity and has dimension at most 39. The image of the entire incidence is S, while the closure of the nonspecial image is the irreducible S0, so S=S0 union S_sp. Every irreducible component of this union is contained in one of its two closed members. A component not contained in S0 would therefore be contained in the at-most-39-dimensional special image, contradicting the component lower bound. This proves S=S0 and exact dimension 46. Its codimensions are four in G and three in the 49-dimensional D.

The proof correctly separates this reduced-locus conclusion from global claims about the scheme defined by minors or the complete incidence.

## 5. Transversality, including special cokernels

The tangent space of G at J is Hom(J,E/J). Evaluation followed by projection to C vanishes on J, so F:E/J to Hom(U,C) is well-defined. Restricting the induced map J tensor U to C to R gives exactly the normal map displayed in the proof. Changing lifts by elements of J contributes only to the old evaluation image and hence zero in C.

For nonspecial W=C*, the rank classification makes F surjective. A linear map from J to Hom(U,C) can be lifted independently on each basis element of J, and any map R to C extends to J tensor U. Their composition proves the asserted surjectivity of the normal map.

For special W=ell tensor U*, the evaluation image is contained in ker(ell) tensor U. Both spaces have dimension eight at exact corank two, so they are equal. Therefore C is identified with U by ell tensor Id, as used in the proof. The resulting map E to End(U) has image exactly sl(U); choosing v with ell(v)=1 proves surjectivity onto that image. Because J lies in its kernel, the descended map on E/J has the same image.

Under the perfect trace pairing, a functional on Hom(R,C) is represented by q:C to R. Composing with R contained in J tensor U and expanding in a basis of J gives coefficient maps Q_j:C to U. Independent variations of each basis vector make the annihilator condition precisely trace(A Q_j)=0 for all A in sl(U). After C=U, each Q_j must be scalar. Thus q(c)=a tensor c for a single a in J. The requirement that the image lie in R says a(c)=0 for every c. Faithfulness of E as an operator space forces a=0 and q=0. This establishes injectivity of the dual normal map, hence surjectivity of the normal map, at every special exact-corank-two point as well.

The faithfulness step is essential: E is an actual operator subspace of Hom(U,V⊗U).

## 6. Analytic product and local schemes

An invertible size-eight minor remains invertible in a neighborhood. Holomorphic invertible row and column operations there give an invertible eight-by-eight block and a two-by-two Schur complement A, with A=0 at the point. The derivative of A is the kernel-to-cokernel normal map up to invertible changes of bases. Its surjectivity makes the four entries of A independent local holomorphic coordinates; they extend to a coordinate system of the smooth 50-dimensional ambient Grassmannian.

The determinant is a unit times det(A). Its zero germ is therefore precisely the product stated in the proof. The Hessian of x11 x22-x12 x21 has full rank four over C, so this is the three-dimensional ordinary quadratic node times a 46-dimensional smooth germ, not merely a tangent-cone description. The proof correctly claims an analytic product rather than an unsupported Zariski-local product.

The local size-nine-minor ideal becomes the ideal of the four entries of A: adjoining an invertible rank-eight block makes rank at most eight equivalent scheme-theoretically to A=0. This ideal defines a smooth reduced 46-dimensional locus. The Jacobian singular ideal of the hypersurface has the same form: the derivatives of det(A) are, up to signs, the four entries of A, and multiplying the hypersurface equation by a unit does not change its singular ideal modulo that equation. Both local scheme equalities in Section 6 are valid.

Exact corank two is a nonempty open subset of the now-proven irreducible S and hence dense. The higher-corank locus is a proper closed subset, so the stated upper bound 45 follows. No sharper estimate is needed for the conclusions.

## Scope

All new arguments are universal finite-dimensional linear algebra and algebraic geometry. The abstract H0/E0 witness is a point of the full universal Grassmannian, not a computation for an actual conductor family. This audit establishes no actual HM/cofactor rank, source nonvanishing, Massey value, or obstruction value. It makes no additional global reducedness, Cohen-Macaulay, higher-corank, complete-incidence, or rational-singularity claim.



## Two-plane incidence

# Independent audit: smooth two-plane incidence

## Verdict

**Pass. No mathematical correction is required.** The full two-plane incidence is smooth and irreducible of dimension 46. Its projective morphism to the reduced corank-at-least-two locus is proper and birational, is an isomorphism over exact corank two, and has the stated Grassmannian scheme-theoretic fibers. It is therefore a resolution in the usual sense of a proper birational morphism from a smooth variety.



## 1. Scheme and dimensions

The ambient product has dimension 50+16=66. The bundle Hom(T tensor U,W*) has rank (5 times 2) times 2=20. Its evaluation section vanishes exactly when all operators in J have output annihilated by W. Thus its scheme-theoretic zero locus is the full incidence, not merely its support.

At a zero, variation of J contributes f_W composed with h for an arbitrary h:J to E/J. This is well-defined because f_W vanishes on J. At a nonspecial W, the induced map E/J to Hom(U,W*) is onto. Consequently the J variations already cover every one of the twenty section coordinates. The zero locus is smooth of dimension 66-20=46 at those points.

## 2. The special differential

For W=ell tensor U*, the chosen splitting V=V0 plus C v0 gives K_W=V0 tensor sl(U), and the quotient output W* identifies with U. The induced map E/J to End(U) has image exactly sl(U). Its five independent J coefficients therefore produce Hom(J,sl(U)), a fifteen-dimensional subspace of the twenty-dimensional target Hom(J,End(U)). The quotient is canonically J* after taking trace, up to an irrelevant nonzero scalar normalization.

The displayed tangent parametrization is exact. The space Hom(U*,V0* tensor U*) has dimension 2 times 8=16, and every such tangent map has the form

    delta w(v tensor u) = w(T(v)u)

for a unique linear map T:V0 to End(U). Applying this to a(u)=sum v_i tensor A_i u yields precisely

    delta f_W(a) = sum T(v_i) A_i.

There is no missing transpose or sign: both sides, paired with w, are sum w(T(v_i)A_i u). Passing to the quotient by sl(U) consequently gives the trace pairing in equation (1).

The trace pairing End(U) times sl(U) to C is nondegenerate on the sl(U) factor, and its kernel on End(U) is the scalar line. Tensoring with V0* shows that the sixteen-dimensional space of T maps onto the twelve-dimensional K_W*, with four-dimensional kernel V0* tensor C Id. A tangent motion ell to ell+t m in the special P(V*) locus has exactly T(v)=m(v)Id, verifying the stated identification of this kernel.

Finally, restriction K_W* to J* is surjective because J is a five-dimensional linear subspace of K_W. Thus W variation covers all five quotient directions missing from J variation. This proves that the full section differential has rank fifteen plus five, or twenty, at every special point. Together with the nonspecial calculation, the section is transverse to zero everywhere. The incidence scheme is therefore smooth, reduced, and purely 46-dimensional.

## 3. Irreducibility

The nonspecial incidence is an irreducible open subset of dimension 46. Its closed special complement has dimension 39 by the core proof. Every irreducible component of the smooth full incidence has dimension 46 and hence cannot be contained in this complement. Thus the nonspecial open is dense in the full incidence. The closure of an irreducible set is irreducible, proving the asserted irreducibility.

This argument avoids an unsupported assumption that all special points deform to nonspecial points; smoothness and the strict dimension inequality establish that conclusion.

## 4. Projection and resolution

The projection is projective because the incidence is closed in a product of projective Grassmannians. Its set-theoretic image is the corank-at-least-two locus. It factors scheme-theoretically through reduced S: any function vanishing on S pulls back to a function vanishing at all points of the reduced incidence and hence is zero.

For fixed J, the equation on W is that it lie inside the kernel of the dual evaluation map, namely C_J*. The representing closed Grassmannian is Gr(2,C_J*), so this is the scheme-theoretic fiber. At corank c its dimension is 2(c-2), including the reduced single point at c=2.

On the exact-corank-two locus the rank-eight image is locally a vector subbundle, so its annihilator is a regular rank-two subbundle. This supplies the stated regular inverse, not merely a pointwise inverse. The locus is nonempty and dense in the irreducible reduced S by the core proof. Therefore the projective morphism is birational and is an isomorphism over that open locus. Its smooth source makes it a resolution.

The addendum appropriately makes no claim that this morphism is an isomorphism over every smooth point of S, or that it is small. Those would require further information. Normality, Gorensteinness, canonical classes, and crepancy are not needed for the stated resolution conclusion and are not inferred here.

## Scope



## All-corank incidence

# Independent audit of all-corank incidence resolutions

## Review status

**Pass.** The local geometry, smallness and canonical calculations are checked below.


## 1. Local geometry of the incidence scheme

The zero-locus bundle is correctly Hom(T⊗U,W*), of rank 10c. At a base point of corank d the Schur complement is a submersion to Mat_d by the imported all-corank transversality theorem. Output-coordinate changes identify the incidence scheme, not merely its points, with the ordinary left-kernel incidence for that matrix. The latter is the vector bundle Hom(C^d,ann(W)) over Gr(c,d), with dimension d(d−c)+c(d−c)=d²−c². The remaining smooth factor has dimension 50−d². Thus Z_c is everywhere smooth of dimension 50−c². Ambient codimension is 10c, so the evaluation section is regular and adjunction applies.

## 2. Irreducibility and smallness

The fibers are scheme-theoretic Grassmannians Gr(c,d). Over the smooth irreducible exact-corank-c stratum the projection is an isomorphism, because the entire dual kernel varies as a bundle. Above a higher stratum S_d the dimension is 50−d²+c(d−c), and its codimension in Z_c is d(d−c). Every component of the smooth source has dimension 50−c²; therefore every component meets the single irreducible dense open over S_c. This proves irreducibility and birationality without ignoring possible incidence components.

For d>c, d(d−c)≥c+1≥2, excluding divisorial exceptional components. Moreover the codimension of S_d in D_c minus twice its fiber dimension is (d−c)²>0. A finite union of the rank strata gives the required strict inequality for every fiber-dimension threshold. Both uses of the word small are justified. For c=6 the map is an isomorphism and D_6 is smooth of dimension fourteen.

## 3. Canonical determinant calculation

The ambient canonical line is (det T)^15⊗(det W)^10. The equation bundle determinant is (det T*)^(2c)⊗(det W*)^10: the T⊗U factor has rank ten, and its determinant is (det T)^2 up to a fixed line. Their product leaves (det T)^(15−2c). Hence ω_(Z_c)=π_c*O_(D_c)(2c−15). The signs and exponents are correct, including the cases c=1,2,6.

## 4. Primary-source check and target singularities

I independently opened Bruns and Vetter's author-hosted, publisher-authorized book [Determinantal Rings](https://www.home.uni-osnabrueck.de/wbruns/brunsw/detrings.pdf). Corollary 5.17 (printed page 60, PDF page 68) gives the Cohen–Macaulay property, and Theorem 6.3 (printed page 65, PDF page 73) gives normal integral domains. The ordinary rank-r determinantal ring is the special case R(X;[1,…,r|1,…,r]), also explicitly identified on printed page 70. Corollary 8.9 (printed page 98, PDF page 106) independently gives Gorenstein for square generic matrices when 0<r<min(m,n). Rank zero is a point and needs no theorem.

These results apply to every matrix-rank local model used here. I also checked the added algebraic étale upgrade: the regular Schur-complement entries have independent differentials, and adding regular functions completing their cotangent basis makes a map to affine 50-space that is étale near the given point. Invertible block operations identify the actual minor ideals and incidence equations with exact pullbacks. Normality, reducedness, and Cohen–Macaulayness therefore transfer from the generic models under étale maps, without needing an analytic-algebraization claim. Consequently the minors define reduced, normal, Cohen–Macaulay schemes, agreeing with the previously used reduced loci.

On a normal Cohen–Macaulay D_c the dualizing sheaf is reflexive of rank one. Its equality with O_(D_c)(2c−15) over S_c extends across a complement of codimension at least 2c+1 by reflexivity. It is thus invertible, proving Gorenstein without needing Corollary 8.9. Over the smooth source, the natural canonical comparison extends across the codimension-at-least-two exceptional set. This proves genuine crepancy, rather than merely an accidental equality of line-bundle classes.

## 5. Scope

The conclusions apply only to the universal family of independent effective five-planes. The proof makes no evaluation or placement claim about the actual conductor family and no selected actual HM, cofactor, source, or obstruction computation. The corresponding derivations are retained in INCIDENCES.md.
