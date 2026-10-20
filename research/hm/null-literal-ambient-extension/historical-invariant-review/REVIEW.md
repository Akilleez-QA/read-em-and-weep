# Independent review: invariant ambient formal extension

## Verdict

The proposed unobstructedness mechanism is mathematically sound for the **full ambient deformation problem**, and there is no parity-based counterexample here. But the sentence “HH³-invariants vanish, therefore this literal algebroid two-jet extends” omits a real presentation/comparison argument. The cited algebraic results identify geometric and Lie descent up to gauge; they do not, merely by their stated conclusions, supply a strictly invariant Maurer–Cartan representative with the specified literal truncation.

Safe current conclusion: a conditional ambient-extension theorem, with one explicit standard descent-lifting lemma to supply. This is substantially stronger evidence than an arbitrary abstract Hochschild deformation claim, but should not be presented as a completed literal-presentation theorem until that lemma or an equivalent equivariant relative comparison is included.

Higher local star products, overlap maps, and triple units must all be permitted to change starting at h³. Nothing here proves an extension with the exact all-order Moyal product held fixed. Nothing here quantizes E or computes any of its second-order obstruction coordinates.

## Inputs read

1. [PR16 note at c8aec970fd65a105f39f4e8aeb8a17f0f0053f89](https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md), especially §§1–3; the rest was also available locally in the sibling review input.
2. [PR4 reduction at fa9be3c2d90ffce8d864bf927ecf3d7cd8dd5de5](https://github.com/Akilleez-QA/read-em-and-weep/blob/fa9be3c2d90ffce8d864bf927ecf3d7cd8dd5de5/research/hm-order-two-reduction.md), read in full.

No source/owner/jet evaluations, production imports, matrix products, or experiment were performed. No external post was made.

## Correct deformation complex

Take the finite product affine cover U of X=C⁴ used for the q and a cochains. Its members and intersections are preserved individually by diagonal inversion ι. Let D be the sheaf of normalized algebraic polydifferential Hochschild cochains, shifted so that an r-argument operation has degree r−1. In particular:

- D^(−1)=O_X, representing the inner gauge/triple-unit part;
- D^0 consists of normalized differential operators;
- D^1 consists of normalized bidifferential operators;
- the differential is the Hochschild differential of ordinary multiplication.

The correct nonlinear object is the cosimplicial DGLA C(U,D), with its Deligne crossed-groupoid descent; alternatively use a suitable Thom–Whitney/Thom–Sullivan DGLA totalization. The ordinary additive Čech total complex computes its tangent/obstruction cohomology. One must **not** declare the ordinary Alexander–Whitney Čech complex with a naively extended Gerstenhaber bracket to be a DGLA without checking the construction.

Do not remove D^(−1). Truncating to positive-arity cochains changes the deformation problem and loses the H²(O_X) direction used by b. Also distinguish this from Hochschild cohomology of the quotient stack [X/ι], which can have additional fixed-locus sectors: only invariant ambient cochains on X are intended here.

## Primary sources checked

[Yekutieli, Twisted Deformation Quantization of Algebraic Varieties, arXiv:0905.0488v5](https://arxiv.org/html/0905.0488): Theorem 3.6 gives affine geometrization using normalized polydifferential cochains. Theorem 9.5 identifies Lie and geometric descent classes for a finite affine cover, compatibly with parameter changes and refinements. Theorem 6.22 and Corollary 7.4 relate geometric descent to twisted deformations. These apply algebraically over C; the formality/quantization theorem is not needed for the obstruction-vanishing argument. These stated comparison results are on gauge classes, so literal and equivariant lifting requires additional justification.

[BGNT, Deformations of algebroid stacks, arXiv:0810.0030](https://arxiv.org/html/0810.0030): Theorem 5.22 gives a Deligne 2-groupoid description through the cosimplicial matrix-algebra model; Theorem 5.25 uses the differential jet model and contractible bases. These are useful supporting framework, but their manifold/groupoid setup must not silently replace the algebraic comparison above.

For a totalization route, [Hinich, Descent of Deligne groupoids](https://arxiv.org/abs/alg-geom/9606010), Theorem 4.1, is relevant, with its finite-cosimplicial-dimension hypothesis requiring attention. [BGNT, Deligne groupoid revisited](https://tac.mta.ca/tac/volumes/30/29/30-29abs.html), Theorem 4.2, compares the higher nerve with the simplicial MC construction. A general citation to these is not a substitute for checking the relative, equivariant statement being used here.

## Cohomology and involution: no remaining uncertainty

The algebraic HKR map is natural for automorphisms and is a quasi-isomorphism of complexes from polyvectors to polydifferential cochains; no Lie-formality assertion is needed. Affine Čech computation gives

H²(Tot C(U,D)) = ⨁_(p+q=3) H^q(X,Λ^p T_X) = HH³(X).

For diagonal inversion on an abelian fourfold, T_X is trivial with inversion acting as −1 on invariant vector fields. Inversion acts by (−1)^q on H^q(O_X). Hence its action on the displayed summand is (−1)^(p+q)=−1. Thus HH³(X)^ι=0. Likewise all of HH²(X) is invariant. Dimensions are respectively 56 and 28, though dimensions are unnecessary.

The Reynolds projector (1+ι)/2 commutes with the differential. Therefore H²(L^ι)=H²(L)^ι=0 for a strict equivariant model L computing this complex. This uses characteristic zero and assumes h is fixed by ι.

The literal two-jet is strictly invariant on the stated cover: q_i and V_i are odd; a_i is even; b is a sum of products of two odd q's; every term of T has one odd q and one odd V. The Moyal bidifferential coefficients are invariant. Thus μ through h², F=id+h²T, and A=1+hb+h²b²/2 are invariant as cochains, not just as cohomology classes.

## Fully proved conditional MC statement

Let L be a C-DGLA with a strict involution, H²(L)^ι=0, and a supplied invariant element α_(2) in MC(hL[h]/h³). Then α_(2) admits an invariant lift α in MC(hL[[h]]) with exactly the same coefficients through h².

Proof: suppose α is solved modulo h^(n+1). Choose an invariant coefficientwise lift modulo h^(n+2). Its curvature is h^(n+1)c. The Bianchi identity makes dc=0. The bracket with α contributes a further h and therefore vanishes on this small-extension kernel; the relevant differential is the original d, not a twisted differential. Since c is invariant and H²(L)^ι=0, choose dv=−c and replace v by its Reynolds average. Adding h^(n+1)v kills the curvature and changes no earlier coefficient. Induct, then take the h-adic inverse limit.

The same argument works in an equivariant filtered L∞ model, with the corresponding MC/Bianchi identities. It is not legitimate simply to average a nonlinear MC solution; the averaging is applied to each **linear correction equation**.

## Precise missing bridge and recommended repair

### Route A: literal descent lifting (preferred)

State and prove this lemma for the above affine cover and normalized differential descent data:

**Small-extension descent lemma.** Given a differential algebroid descent triple (μ_i,F_ij,A_ijk) modulo h^(n+1), its arbitrary coefficientwise lift modulo h^(n+2) has an obstruction cocycle in total degree 2 of C(U,D). The components are the local associativity, overlap-homomorphism, triple-inner-gluing, and quadruple/pentagon defects. Changing the new coefficients changes this cocycle by the total differential of a total-degree-1 correction. All operations are natural under cover-preserving automorphisms.

The four obstruction component bidegrees (Čech degree, D degree) are (0,2), (1,1), (2,0), (3,−1). The correction bidegrees are (0,1), (1,0), (2,−1), corresponding exactly to μ,F,A. At a small-extension kernel all products with lower-order deformation terms disappear, so the linearized differential is the ordinary Čech–Hochschild total differential. The cocycle identity follows from coherence identities among the four defects; it must be written with a consistent orientation matching PR16, or cited from a result that states precisely this relative lifting property.

Once that lemma is supplied, averaging a primitive of each defect gives invariant corrections starting at h³. This proves existence on the same cover with the literal two-jet preserved, and avoids the need to choose an invariant MC representative via an abstract equivalence. Differential operators remain differential and all coefficients remain regular on their designated intersections. Taking inverse limits of these coefficientwise-compatible triples gives formal algebroid descent; the inverses and units exist h-adically.

**Review status:** the linearized complex and induction are identified above; I have not expanded and verified all four nonlinear coherence-to-cocycle sign identities. Thus the lemma is an explicit remaining proof obligation, not an executed certificate in this review.

### Route B: relative equivariant comparison

Alternatively establish that an equivariant totalization/descent comparison admits a strictly invariant MC representative for the supplied strict descent two-jet, and that its extension can be transported back with the prescribed reduction. An equivalence on ordinary gauge classes does not alone establish this. Functoriality and finite-group averaging suggest the bridge is available, but averaging an arbitrary L∞ quasi-isomorphism is not generally an L∞ morphism.

For nonequivariant literal matching, differential gauge transformations congruent to identity and overlap inner units can be lifted coefficientwise (using logarithms/exponentials or h-adic inverses), then used to transport the extended presentation. That establishes why literal equality is more than a class statement but is usually repairable. Strict invariant matching additionally requires an invariant comparison/gauge or a finite-group strictification argument; it must not be assumed from invariance of a gauge class.

## Suggested final theorem wording

“For the full differential algebroid descent problem on X=C⁴, diagonal inversion has no invariant ambient obstruction classes: HH³(X)^ι=0. Consequently every strictly invariant finite-order descent deformation extends formally, provided the standard equivariant small-extension descent lemma is used. In particular the invariant PR16 two-jet has an ambient formal extension preserving its coefficients through h². Higher local products and gluing coefficients are allowed to vary.”

Until the lemma is included, prefix the second sentence by “Under the explicit descent-lifting comparison stated below”. Do not describe this as completion of the bundle quantization, the full-sign test, or any of the unresolved second-order coordinates.
