> Historical mathematical review retained with the source. This is not a new independent review or a formal verification certificate.

# Independent audit: sharp ribbon connecting ranks and line lifting

## Verdict

The proof passes independent review under its stated ribbon-local hypotheses. For every even d≥4 it establishes all attainable connecting ranks

    0,…,min(7,d−3),

and, for d≥8, identifies the entire effective family of connecting maps with the specified binary Hankel/catalecticant family. The square-zero construction takes place on the actual fixed nonsplit E=2C. It neither substitutes a split ribbon nor assumes that a ribbon-local bundle extends to an ambient HM bundle.

The equivalences between e=0, lifting the maximal line of F_C, splitting F on E, and lifting the positive-root line of End₀(F_C) are correct for d≥4. The different zero-boundary conditions for d≥8 and d=4,6 are also correct. No substantive correction to these assertions is needed.

Three useful precisions are checked below: the positive-root lift, when it exists, is unique as an embedded line lift; the d=6 full rank is determined by a row-space test; and catalecticant rank is not a claimed classification of evaluation length, symmetric tensor rank, or unframed bundle isomorphism classes. The revised proof, reread during this audit, explicitly includes the first two points and the generic maximal-rank assertion.

Read directly: this directory's PROOF.md and ../ribbon-duality-constraints/PROOF.md and AUDIT.md. The review consists only of formal square-zero algebra, exact sequences, line-bundle cohomology, Serre duality, and symbolic polynomial identities. No selected HM map, splitting, source, retained class, polynomial instance, or actual rank was evaluated.

## 1. The reference exists on the specified nonsplit ribbon

Here J=O_C(−4), with J²=0, and a plane twist restricts to twice its degree on C. The units sequence identifies 1+J with J additively. Every global unit on C is constant and lifts to E, and H²(C,J)=0. Consequently the exact sequence used in the proof is indeed

    0 → H¹(J) → Pic(E) → Pic(C) → 0.

There is no additional quotient of H¹(J) by nonlifting constants. Multiplication by two is an automorphism of its complex-vector-space kernel. To obtain a square root of a line bundle whose restriction degree is even, lift the half-degree line from C, compare its square to the desired line, and correct that comparison by half its kernel class. This works on E without an algebra retraction to C.

For L=O_E(d/2 plane) and D=O_E(−2 plane), the restriction degree of LD is d−4. Thus A₀²≅LD exists, and Q₀=DA₀⁻¹ gives

    det(A₀⊕Q₀)=D,
    Hom(Q₀,A₀)=L.

Their restriction degrees are exactly a=(d−4)/2 and b=(−d−4)/2. This also handles the cases in which these integers are odd; it does not require A₀ or Q₀ to be plane restrictions.

The resulting End₀ reference decomposes as L⊕O_E⊕L⁻¹ with the indicated root and Cartan generators. After twisting by −2 plane, the sole section contribution on C for d≥4 is the positive root O_C(d−4). Its reference line on E is O_E(d/2−2 plane). Conic restriction from the plane is surjective because H¹(P²,O(m))=0 for every integer m. Hence every such section lifts on E and ε⁰=0. This is the necessary justification for using a pure deformation cup product rather than a formula with an unaccounted reference boundary.

## 2. Determinant-fixed lifts form the asserted framed torsor

Fix the reduction identification with F⁰_C and a compatible identification of the determinant with D. On a sufficiently fine affine cover, the reduction isomorphism lifts to bundle isomorphisms on E. A determinant discrepancy reducing to one lies in 1+J and can be removed locally. Their overlap differences therefore have the form 1+u with

    u ∈ J⊗End₀(F_C).

Indeed det(1+u)=1+tr(u) exactly, since every quadratic term has coefficients in J². Products and gauge transformations in this kernel are additive. The cocycle equation is the usual one in the sheaf J⊗End₀(F_C), with its gluing supplied by the reference bundle. It is not an equation requiring a split structure sheaf.

Conversely, multiplication of the reference transitions by any such cocycle gives invertible transition maps satisfying the cocycle condition and preserving the determinant identification. Equivalence through maps reducing to the identity amounts precisely to a coboundary. Thus the reference makes the set of framed isomorphism classes a torsor with coordinates

    H¹(O_C(d−4)) ⊕ H¹(O_C(−4)) ⊕ H¹(O_C(−d−4)).

The first group vanishes for d≥4. It is legitimate to kill the entire p component by a reduction-trivial gauge change and retain the classes h and e. No condition couples h and e: products that could impose such a condition vanish in J².

The framing qualification is essential. Reduction automorphisms are not being quotiented out here. The proof consistently states a classification of effective boundaries and framed deformation parameters, not a classification of unframed bundles.

## 3. The full boundary formula and its twists

Conjugation by 1+u acts on the tracefree endomorphism bundle as 1+ad(u). In the stated conventions,

    [H,E₊]=2E₊,       [E₋,E₊]=−H,       [E₊,E₊]=0.

Transporting a global reference lift of a quotient section through the local comparisons therefore produces the overlap cocycle

    ε(s)=(2h cup s, −e cup s, 0),

up to the common Čech sign. Its three targets are respectively

    H¹(O_C(d−8)), H¹(O_C(−8)), H¹(O_C(−d−8)).

All degrees agree: h has coefficient degree −4, e has coefficient degree −d−4, and s has degree d−4. The first-order part of a chosen reference section cannot add another term, since multiplication by u kills it through J²=0. The fixed nonsplit base has already been incorporated by comparing genuine bundles and sections on E.

For d≥8, H¹(O_C(d−8))=0. Thus every possible boundary is its Cartan block, with no lower-root contribution and no residual diagonal contribution. Conversely, every e occurs in the determinant-fixed torsor, so this description covers the entire effective family, not only a constructed subset.

## 4. Catalecticant identification and exact rank strata

Set n=d−4. Serre duality gives

    H¹(O_C(−d−4))=H⁰(O_C(n+6))* ,
    H¹(O_C(−8))=H⁰(O_C(6))* .

Compatibility with cup product identifies the Cartan map by

    ⟨C_e(s),t⟩=⟨e,st⟩,

where s and t have degrees n and 6. In the explicitly chosen unnormalized monomial bases, multiplication produces the matrix

    (C_e)_(i,j)=μ_(i+j),    0≤i≤6, 0≤j≤n.

There are no omitted binomial factors: such factors arise only after changing to another convention for identifying functionals with binary forms.

Every monomial of degree n+6 is a product of a degree-n and a degree-6 monomial. Therefore the multiplication map spans H⁰(O_C(n+6)), and C_e=0 implies e=0 for all n≥0. This proves injectivity of the parameterization, including the two small cases.

For d≥8 the stated Hankel determinantal conditions consequently give an exact classification of the rank loci in the effective parameter space. Rank at most r is equivalent to vanishing of all (r+1)-minors; exact positive rank r adds the nonvanishing of at least one r-minor. Rank zero is simply e=0. In the full framed bundle parameter space, h remains an unrestricted factor in these loci.

This is a complete matrix-rank description, not a normal-form theorem expressing each e as a short sum of point evaluations. In particular, the evaluation construction below supplies witnesses for the permitted ranks; it does not exhaust each rank stratum. Neither symmetric tensor rank nor minimal evaluation or confluent-evaluation length is asserted to equal the rank of this one, potentially unbalanced, catalecticant. The proof's warning about evaluation decompositions should be read with this full qualification.

## 5. The symbolic family attains every allowed rank

For a formal r with 1≤r≤min(7,n+1), work over the ring generated by the z_k and w_k with all w_k and z_i−z_j inverted. The functional

    e(f)=Σ_k w_k f(1,z_k)

has moments μ_l=Σ_k w_k z_k^l. Formal multiplication gives

    C_e=V_6 diag(w_k) V_n^T.

The first r rows of each Vandermonde matrix form an invertible square matrix: their determinant is the formal product of all z_j−z_i. Hence V_6 is a split injection, V_n^T is a split surjection, and the diagonal matrix is invertible. The composite has a locally free image of rank r on this parameter scheme. Equivalently, its leading r×r determinant is

    (∏_k w_k)(∏_(i<j)(z_j−z_i))²,

which is a unit, while every (r+1)-minor vanishes by the factorization. This proves exact rank r on every fiber without choosing or evaluating parameter values.

The parameter scheme is a nonempty open subset over C. The H¹ class can be represented universally on a fixed affine cover of C and used to modify the reference transitions on E after base change. Cohomology here is compatible with this flat scalar extension. Taking h=0 and the pure lower-root cocycle therefore yields determinant-correct rank-two bundles on the same E with precisely these connecting ranks. The rank-zero member is the reference.

There is no inference that all points of a determinantal stratum arise from this distinct-point family. That is unnecessary for sharpness: the universal upper bound together with one symbolic family for each integer proves the exact attainable interval.

The added genericity assertion is correct. The e-parameter space is an irreducible affine space; the maximal-rank locus is nonempty by the universal construction and open by its minor conditions, hence dense. For d≥8, adjoining the unrestricted h-coordinate preserves this statement. This is a statement about the framed ribbon-local parameter family. It makes no density claim about an HM family or about an unframed moduli space.

## 6. The small cases and their complete rank tests

### d=4

Here n=0. The domain is one-dimensional, e is identified with the Cartan column in H¹(O_C(−8)), and the positive-root component is 2h in H¹(O_C(−4)). Since these are separate direct summands, they cannot cancel each other. Thus

    rank ε=0 iff e=h=0;
    rank ε=1 otherwise.

This proves the complete classification of pairs (e,h) in this case, not just existence of the two ranks.

### d=6

Here n=2. The Cartan block is C_e of size 7×3. The positive-root target is H¹(O_C(−2)), which is one-dimensional. Serre duality identifies the corresponding row H_h with h as a functional on H⁰(O_C(2)). The full boundary is the stack of −C_e and 2H_h.

The revised proof's explicit rank description is correct: if k=rank C_e, then

    rank ε=k     when H_h belongs to row(C_e),
    rank ε=k+1   when H_h does not belong to row(C_e).

When k=3 the second case is impossible because the row space is already the whole three-dimensional dual domain. Equivalently, the second case means that h is nonzero on ker C_e. This rule also includes k=0: then e=0, and a nonzero h gives rank one. Consequently rank zero is exactly e=h=0, and all ranks 0,1,2,3 occur with h=0 by the symbolic construction.

The statements concerning d=0,2 are appropriately limited. Their section domain is zero, so the boundary supplies no splitting criterion. In particular the vanishing of H¹(O_C(d−4)) used to deduce splitting fails at those smaller d, and the proof does not silently extend that deduction to them.

## 7. Maximal-line obstruction and splitting of F

For d≥4, a−b=d>0. The maximal line A_C in F_C is unique, since there are no maps from O_C(a) to the lower-degree quotient. The standard square-zero graph-lifting obstruction lies in

    H¹(J⊗Hom(A_C,F_C/A_C))=H¹(O_C(−d−4)).

The reference supplies a global initial line lift. In graph coordinates the lower-left overlap discrepancy is exactly e; changing local graphs changes it by a coboundary. Hence the maximal line lifts precisely when e=0. Local primitive generators show that a successful lift is a line subbundle with locally free quotient.

If e=0, a reduction-trivial gauge change kills its representative. The upper component can then be killed as well because H¹(O_C(d−4))=0. The remaining diagonal transition changes exhibit

    F=A⊕Q,       AQ=D.

The operations are independent because the kernel group is additive. Conversely, any direct-sum decomposition of F restricts to one with degrees a,b, by uniqueness of the splitting type on P¹. Its degree-a factor restricts to the unique A_C, so it forces e=0. This proves both directions of the asserted splitting equivalence.

For completeness, a successful embedded lift of A_C is itself unique: differences of two such line lifts form

    H⁰(J⊗Hom(A_C,F_C/A_C))=H⁰(O_C(−d−4))=0.

This concerns the maximal embedded line, not the choice of a complementary summand or its presentation.

## 8. Positive-root lifts in B and the reference-line qualification

Let P=Hom(Q_C,A_C)⊂B_C. The obstruction to lifting it as an embedded line subbundle of B is the class of ad(u)|P modulo P in

    H¹(J⊗Hom(P,B_C/P)).

Relative to the chosen splitting, this group has Cartan and opposite-root components with coefficient line bundles O_C(−d−4) and O_C(−2d−4). The obstruction is (−e,0). Thus an arbitrary line-subbundle lift of P exists iff e=0; no isotropy assumption on a proposed lift is needed for necessity. When e=0, the splitting of F supplies the lift Hom(Q,A), which is isotropic.

One can sharpen the wording to remove any ambiguity about which line lift is being compared to the reference. Differences between embedded lifts of P form

    H⁰(O_C(−d−4)) ⊕ H⁰(O_C(−2d−4))=0.

Therefore the embedded lift, when it exists, is unique. In particular an arbitrary lift cannot have a different underlying line-bundle class from the positive-root line supplied by the split F.

With e=0, the diagonal transitions deform A₀ by h and Q₀ by −h. Their ratio therefore deforms L=Hom(Q₀,A₀) by 2h in the injected group H¹(J)⊂Pic(E). Since multiplication by two is injective,

    Hom(Q,A)≅L iff h=0.

Thus “P lifts as some line bundle” requires only e=0, whereas “P lifts as the fixed reference line L” requires e=h=0. The latter comparison retains its specified reference. Likewise the framed determinant-fixed bundle equals the reference framed class iff e=h=0. Merely knowing that F is split does not identify its factors with A₀,Q₀.

Combining these observations with injectivity of e↦C_e proves the exact zero-boundary statements:

    d≥8: ε=0 iff e=0 iff F splits iff the stated lines lift;
    d=4,6: ε=0 iff e=h=0.

In the small cases e=0 with h≠0 gives a split F with nonzero boundary. For d≥8 the same diagonal direction is invisible to the boundary.

## 9. Scope of sharpness and final qualifications

The constructed models preserve the fixed E, J, D, restricted rank-two splitting, and genuine tracefree endomorphism structure. Therefore these data alone cannot exclude any integer in the proved interval or impose a positive lower bound. This is a sharpness statement about exactly that ribbon-local package.

It gives no realization by an actual HM restriction, no ambient extension theorem, and no assertion about a component-image quotient or retained source. Additional global or HM-specific requirements can restrict which ribbon-local parameters occur. The proof properly keeps those issues separate.

No correction of a theorem or formula is required. The final review confirms the following qualifications:

1. The revised proof states the vanishing of H⁰(J⊗Hom(P,B_C/P)), making uniqueness of the embedded P lift explicit. Its analogous statement for A_C is also correct.
2. The revised proof includes the d=6 row-space criterion and therefore describes the rank of every pair (e,h), not merely the attainable integers.
3. The determinantal classification must remain distinct from evaluation decomposition length and tensor rank; the Vandermonde family proves attainability only. The proof does not assert otherwise, and this audit spells out the distinction to avoid overreading the reference to confluent evaluations.

These qualifications and the valid genericity addition do not change the claimed sharp rank interval or any of the lifting equivalences. All requested checks are complete.
