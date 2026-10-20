# Line-projected full-support rank-five surfaces: a finite splitting reduction

All spaces are over C. Let E have dimension four, K subset Sym²E have dimension five and full support, and X subset E have dimension two. Assume an irreducible rank-two surface S has an ordered-factor component whose first image is P(X). Suppose v:K→E is linear, compatible on a dense rank-two open of S, and has no compatible square. In the universal trilinear application the last condition follows from repeated-input injection. No realization by an actual source operation is assumed.

## New structural lemma

Put M_l={m in E: lm in K}. Its generic dimension is exactly two. The saturated kernel bundle W on P(X) has one of the splittings

    O², O⊕O(-1), O⊕O(-2), O(-1)².

The degree-zero case gives complementary two-planes and an identically compatible Segre quadric. The degree-one case is precisely the full-support five-coefficient cubic-scroll family already classified in ../full-support-scroll-exclusion/PROOF.md; its types I and II are excluded, leaving III. There are no additional lower-span degree-one cases under square avoidance. The two degree-two cases cannot be discarded by a dimension-count shortcut: their six pre-symmetrization coefficients necessarily have one relation after multiplication, and a genuinely squarefree quartic example is given below.

This is conditional on the ordered-factor image being a line; it says nothing about arbitrary factor images.

## 1. Bundle and degree bounds

The multiplication pencil defines

    E⊗O → (Sym²E/K)⊗O(1),   m ↦ lm mod K.

Let I be its image sheaf and W its kernel. On the smooth curve P¹, I is locally free. The exact sequence 0→W→O⁴→I→0 shows that I is globally generated. Its sheaf injection into O(1)⁵ implies every splitting summand has degree at most one (otherwise its map into every O(1) is zero). Thus I splits into copies of O and O(1). W splits as a sum of O(-a_i), with a_i≥0, and sum a_i=deg I≤rank I.

The dominating surface implies dim M_l≥2 generically, so rank I≤2. Rank zero is impossible because then K contains XE, which has dimension seven.

Suppose rank I=1. If I=O, then W is a constant three-plane W0. K contains XW0, of dimension 6−binom(dim(X∩W0),2). Dimension five forces X⊂W0, and K=XW0 has support three, contradiction.

If I=O(1), write the surjection as sα+tβ with α,β independent. Set W0=ker α∩ker β, of dimension two. Besides W0, its kernel has a generator m(s,t) linear in s,t whose image in E/W0 is an isomorphism from the parameter space. K contains XW0 and all (sx+ty)m(s,t).

If X≠W0, dim XW0=4. Modulo W0-products, the latter tensors map to lbar mbar in Sym²(E/W0), whose span has dimension at least two: if dim Xbar=1 this is a nonzero scalar linear form times an invertible vector-valued linear form; if dim Xbar=2, a one-dimensional product span would force the infinitely many first factors lbar to divide one fixed nonzero quadratic, impossible. Thus dim K≥6. If X=W0, XW0=Sym²X has dimension three, while the cross terms of l m(s,t) give three independent coefficients in X⊗(E/X), because mbar is invertible. Again dim K≥6. This excludes rank one.

Consequently rank I=2 and W has rank two, yielding exactly the four listed splittings.

## 2. Coefficient-space control

For degree one write W=O z⊕O(-1)m with m=sp+tr. The vectors z,p,r are independent: otherwise the nonzero section m modulo z has values in a fixed line, and its linear scalar vanishes somewhere, contradicting that W is a subbundle of O⁴.

For degree two, the coefficient vectors of the two minimal generators total four (either 1+3 or 2+2), and they must span E. If they lay in H of dimension at most three, enlarge H to dimension three. Then I=(H⊗O/W)⊕O, and its rank-one first summand has degree two. This contradicts the proved restriction on splitting degrees of I. Hence these four coefficient vectors are independent.

Before symmetric multiplication, the coefficients of l times each generator span a subspace R of X⊗E of dimension d+4, where d=deg I. This follows directly in the displayed independent coefficient bases. The multiplication map X⊗E→Sym²E has kernel Λ²X, of dimension one. Therefore the tensor span has dimension at least d+3. For d=2, it must be exactly five, and Λ²X must lie in R. This is the genuine source of the compulsory quartic relation, not a reason to exclude quartics.

For generic l, P(M_l) is a line. Its incidence over an open subset of P(X) is irreducible of dimension two. Thus the given ordered-factor surface is dense in that incidence; compatibility on S supplies compatibility on this entire generic family.

## 3. Degrees zero and one

For d=0, W is a constant two-plane Z and S is the product surface of factors in X and Z. If X∩Z=Ce, two limiting support planes at e² are X and Z, forcing v(e²)∈Ce. If X=Z, S is the binary plane; compatibility forces v(Sym²X)⊂X, and the binary cubic e∧v(e²) has a projective zero. Both violate square avoidance. Hence X and Z are complementary. The usual bilinear compatibility calculation then gives the finite C_(2,2) annihilation incidence in the trilinear application.

For d=1, the coefficient tensors are

    xz, yz, xp, xr+yp, yr.

If dependent, a nonzero relation has the form

    x(az+cp+dr)+y(bz+dp+er)=0.

Because x,y are independent, its two parenthesized factors are h y and −h x for a scalar h. Independence of z,p,r shows h cannot vanish. Thus X lies in H=span(z,p,r). The tensor span has dimension exactly four by Section 2 and is a ternary web. The abstract theorem of ../rank-six-cubic-web/REDUCIBLE.md excludes a compatible surface for every square-avoiding map from such a four-dimensional ternary web into E. It does not require that web to equal the full residual kernel. Thus the dependent case is impossible.

If the five tensors are independent they span K. Full support then gives precisely the hypotheses of ../full-support-scroll-exclusion/PROOF.md. That theorem classifies I, II, III and excludes I and II under square avoidance. Hence III is the only degree-one survivor.

## 4. A genuinely distinct squarefree quartic

Take a basis p,q,r,w of E and set

    X=span(q,r),
    K=span(pq, pr−q², qr, r²−qw, rw).

The family

    (-s q+t r)[a(s p+t q)+b(s r+t w)]

lies in K. Its expansion has coefficients

    a[-s² pq+st(pr−q²)+t² qr]
      +b[-s² qr+st(r²−qw)+t² rw].

The five displayed tensors are independent and have full support. If h²∈K, absent p² and w² coefficients force h∈span(q,r). The ties of q² to pr and r² to qw then force h=0. Thus K has no nonzero square, and v=0 is compatible on the entire surface.

The map from P¹_(s:t)×P¹_(a:b) is basepoint free with line bundle O(2,1): the two vectors sp+tq and sr+tw are independent at every base point, and the first factor is nonzero. The multiplication map has finite fibers because a nonzero rank-two quadratic has only two factor lines, each of which determines the base point and then the fiber point. Generically the second factor is outside X, so the first factor is uniquely recognized and the map is birational. Therefore its image has degree (2h1+h2)²=4. It is an integral rank-two quartic surface, distinct from the cubic-scroll case.

This disproves any claim that line projection plus dimension five, full support, and square avoidance force the cubic-scroll normal form. It does not disprove a stronger statement using the global trilinear operation or additional finite incidences. In particular no conclusion that this quartic does or does not force a corrected rank-one (2,3) rectangle is asserted here.

## 5. Source checkpoint, audit, and next step

Direct connected-tool reads on 2026-10-19 at approximately 12:51 UTC verified PR1 head 2531056eae05fdf31e8fb4ca3affc5907073ad73 and PR79 head 4659e4425c6b5ab6b1899e6af93656ac03ff0862, both open drafts. PR79 discussion is empty. PR1 has a newer comment than the supplied checkpoint: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6267584308 at 12:48:36, distinguishing internal-overlap inertia cancellation from failure of the inter-ambient root equivalence to descend. It leaves effective global charts and full corrected comparison unfinished and does not change the tensor hypotheses used here.

Only read-only source checks, symbolic mathematics, and this local mathematical artifact were used. No actual source operation, physical rank, source input, numerical experiment, or external write was performed.

The remaining useful local step is to classify the compulsory degree-two relation and all compatible corrections. A separate quartic analysis is pursuing it. The surviving quartic must not be silently routed through the existing finite rank-one rectangular incidence without a proof of that implication. After removing a contraction correction, the immediate residual consequence K⊂XE supplies at most rank two on the (2,4) product XE, whose dimension is seven; that is a different incidence.
