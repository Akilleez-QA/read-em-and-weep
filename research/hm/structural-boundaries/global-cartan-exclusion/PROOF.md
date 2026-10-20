# No globally ordered algebraic diagonal carrier atlas downstairs

## Theorem and scope

Work over C. Let E be the rank-two degree-zero cohomology of the authenticated homogeneous four-term complex on P4, and B=rho*E on Y=(P1)^4. Neither E nor B has a globally covering regular algebraic atlas whose invertible overlap matrices are diagonal with a consistent ordering of the coordinate lines. This includes arbitrary open refinements and regular algebraic changes of frames.

This is a bounded exclusion of a downstairs/Y globalization of the accepted same-carrier Cartan shortcut. It does not exclude arbitrary gauges of the physical N-twisted bundle on X=C^4, unordered/Weyl-monomial atlases, rational or meromorphic frames, or source-specific mixed-carrier cancellation. No detector, deformation obstruction, or algebraicity conclusion is obtained.

## 1. Actual downstairs object

The accepted product-root proof (included in dependencies, sections 3,4,7) defines rho:Y→P4 by the coefficients of the product of four binary linear forms. Their lack of common zeros proves rho*O(1)=M=O_Y(1,1,1,1). For the product elliptic x-map q:X→Y and f=rho q, it identifies the specified root line N by N²=f*O(1), including legal/infinity frame conventions.

Its section 4 identifies the homogeneous complex L on P4 as

    L^(-1)=5O(-1), L^0=15O, L^1=10O(1), L^2=2O(2).

The accepted homogeneous contractions are regular on the six covering carrier opens D(h_j), D(a). They split this same complex into contractible pairs and a locally free rank-two cohomology object in degree zero. Consequently E=H^0(L) is an actual vector bundle with no other cohomology sheaves. Pullback preserves these explicit split identities, without an extra flatness assumption. The physical bundle is V=f*E tensor N. We do not infer the existence of E merely by attempting to descend V from X.

The original public source is ext-model.md, section 1, at add03476d9055aa00e1e00778eea6332cf8e01cc; it states exactly this complex and sole cohomology. The accepted source-bound regular contraction supplies the premise used here independently of that document's Ext calculations.

## 2. Chern conventions

Write H=c1(O_P4(1)). The cohomological signs in degrees (-1,0,1,2) give

    [E]=-5[O(-1)]+15[O]-10[O(1)]+2[O(2)],
    ch(E)=-5 exp(-H)+15-10 exp(H)+2 exp(2H).

Thus rank E=-5+15-10+2=2, and

    c1(E)=(5-10+4)H=-H,
    ch2(E)=(-5-10+8)H²/2=-7H²/2.

Using ch2=(c1²-2c2)/2 yields c2(E)=4H². These are normalized downstairs conventions, not the alternative unnormalized (5H,10H²) convention. No identification with a different classical presentation is needed.

For consistency, put n=c1(N), so f*H=2n. The rank-two twist formula gives

    c1(V)=-2n+2n=0,
    c2(V)=16n²+n(-2n)+n²=15n².

The actual X complex has character -5 exp(-n)+15 exp(n)-10 exp(3n)+2 exp(5n), with first two positive components 0 and -15n², agreeing with this. This does not classify line bundles on X or prove arbitrary-X nonsplitting.

## 3. All algebraic line splittings on Y are excluded

Let e_i=pr_i*c1(O_P1(1)), i=0,1,2,3. The Chow ring is

    CH*(Y)=Z[e_0,e_1,e_2,e_3]/(e_0²,e_1²,e_2²,e_3²).

The six e_i e_j for i<j form an independent degree-two basis. Every algebraic line bundle is O_Y(a_0,a_1,a_2,a_3), with integral a_i. For completeness, the Picard statement follows by induction under S×P1→S: subtract the constant degree on the connected P1 fibers; the resulting line is trivial on each fiber, its pushforward is a line bundle by cohomology and base change, and evaluation identifies it with a pullback. Start with S a point. Thus all line bundles on Y are included, not only symmetric multidegrees.

Set h=sum_i e_i=rho*H. Then c1(B)=-h and c2(B)=4h²=8 sum_(i<j)e_i e_j. A splitting would therefore have the form

    B=O_Y(a_0,...,a_3) direct-sum O_Y(-1-a_0,...,-1-a_3).

Its coefficient of e_i e_j in c2 is

    a_i(-1-a_j)+a_j(-1-a_i)=-a_i-a_j-2a_i a_j.

Equating with 8 gives

    (2a_i+1)(2a_j+1)=-15 for every i<j.

Already three indices contradict this: write b_i=2a_i+1. Since b_0b_1=b_0b_2=-15, b_0 is nonzero and b_1=b_2. The remaining equation requires b_1²=-15. Hence B cannot split.

On P4, Pic(P4)=Z and a splitting would be O(a) direct-sum O(-1-a), requiring -a(a+1)=4, or (2a+1)²=-15. Alternatively a splitting of E would pull back to the excluded splitting of B.

## 4. Atlas consequence and exact limitation

Regular ordered diagonal invertible transitions diag(u_ij,v_ij) glue the two coordinate lines separately to global line bundles. Their direct sum is the original bundle. Thus the nonsplitting excludes every such atlas, including refinements and regular algebraic regaugings. If local frames were initially described as local line-summand frames, refine again to trivialize the lines and apply the same argument.

The accepted same-carrier lemma uses P_c I_c=Id to give g_ij=D(nu_j/nu_i) when every vertex has the same carrier. It does not glue its two directions across different carriers. This theorem prevents replacing that restricted identity by a global ordered diagonal atlas downstairs/on Y. It does not prove that every possible all-carrier simplification entails such an atlas.

The existing six-carrier theorem computes locally diagonal reference connection forms P_c dI_c=diag(0,dlog s_c), and retains the overlap defect. Diagonal local connection forms are not diagonal transition matrices. The two results are therefore compatible; no assertion about impossibility of a global connection is made here.

An arbitrary gauge on X is outside the result, even though N²=f*O(1). Such a proposal is covered only if it demonstrably induces the forbidden regular ordered atlas downstairs or on Y. Likewise dense-open rational diagonalization, meromorphic gauges, a different base change, unordered/Weyl-monomial overlaps, local Cartan-valued currents, and source-specific jet/kernel cancellations are not excluded. The thirty detector values and the full obstruction remain unresolved.

## 5. Prior-result check and sources

Read on 2026-10-18: PR1 through comment 6250661140, PR79 at b80a710530a5d5d9b1844196bc446459daf0732f, accepted same-carrier and product-root proofs, and the existing six-carrier connection note. Searches of local mathematical notes and PR1 for Cartan/nonsplitting/diagonal-transition claims, plus an indexed repository Chern/diagonal search, located no existing copy of this particular all-line-bundle Y contradiction. This is not a mathematical-literature novelty claim. Its bounded added utility is the exclusion of the specific globalization shortcut.

- Exact complex/model: https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md (statement and section 1).
- Accepted product-root proof and independent review: dependencies/product-root-PROOF.md and dependencies/product-root-REVIEW.md (especially proof sections 3,4,7).
- Accepted same-carrier proof and review: dependencies/same-carrier-PROOF.md and dependencies/same-carrier-REVIEW.md (especially proof sections 1,4).
- Local diagonal connections and retained overlap defects: https://github.com/Akilleez-QA/read-em-and-weep/blob/b80a710530a5d5d9b1844196bc446459daf0732f/research/hm/null-source-integration/complete-raw-remainder/source_diagonal_connections.md
- Current frontier: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6250661140
- Projective-space Picard classification: https://stacks.math.columbia.edu/tag/0BXJ

Only symbolic Chern identities and line-gluing arguments were used. No actual source/model/matrix/polynomial/point/jet evaluation occurred. The included source-bound premises are accepted dependencies, not conclusions of a new source execution. The independent final-byte review is REVIEW.md; SHA256SUMS binds all packet files.
