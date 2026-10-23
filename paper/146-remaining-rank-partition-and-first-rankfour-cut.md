# 146. A finite remaining-rank partition and the first rank-four exclusion

**Craig Ward · 23 October 2026 · One coarse rank-four stratum removed**

## The new reduction, in a fixed counting domain

The [remaining-rank partition, PR1171](https://github.com/Akilleez-QA/read-em-and-weep/blob/8497b6e793f36c14448fecdf88d209971273e069/research/hm/remaining-rank-strata/PROOF.md), combined with [chapter 145](145-nine-profile-coverage-and-square-rank.md), supplies a finite necessary list for the actual generic Gauss rank r≥4. The [new rank-four theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/ba6b3ef9f1a2ca79f9491025560e2a074a42dbbd/research/hm/rankfour-extremal-plateau/PROOF.md) excludes the ordered maximal plateau (r,k,l)=(4,3,3).

Thus the fixed coarse list of **27 bad-rank bins is reduced to 26**. The rank-four group decreases from nine to eight. This is an exclusion of one entire necessary stratum, not merely another test or a relabeling of previous rank-three work.

Here “bad” means r<13, failure to attain the sufficient positive-square-surjectivity criterion. It does not mean that the original repair is impossible in that bin or that another smoothing pencil fails. The remaining bins are necessary containers, not realized examples or a classification of the geometry inside them. Their number is not a completion percentage or an estimate of remaining difficulty.

## The finite partition and its unchanged boundary

Rank budgets and actual cubic persistence give

    1≤k≤min(3, floor(17/r)),
    1≤l≤min(3, floor(13/r)).

The lengths are ordered. D/P/V sources have quadratic sections, improving only the forward bound to l≤2. Z has no such quadratic visibility; that absence does not force l=3. In particular l=3 requires r=4 and source Z. There is no corresponding unproved global k≤2 improvement.

| Generic SF rank r | Baseline bad bins | Bins not excluded by this new theorem | Generic positive-square rank | Generic positive-square cokernel |
| ---: | ---: | ---: | ---: | ---: |
| 4 | 9 | 8 | 28 | 9 |
| 5 | 6 | 6 | 29 | 8 |
| 6 | 4 | 4 | 30 | 7 |
| 7 | 2 | 2 | 31 | 6 |
| 8 | 2 | 2 | 32 | 5 |
| 9 | 1 | 1 | 33 | 4 |
| 10 | 1 | 1 | 34 | 3 |
| 11 | 1 | 1 | 35 | 2 |
| 12 | 1 | 1 | 36 | 1 |
| **Total** | **27** | **26** | | |

Rank thirteen is separate: its unique coarse label is (13,1,1), and if attained it gives generic surjectivity of the positive square map, of rank37 with kernel4 and cokernel0. It has not been proved attained. The upper endpoint is the full constant ambient in that case, with derivative rank zero; omitting it would incorrectly remove the auxiliary success stratum.

The optional source-labeled refinement has 99 bad labels before this theorem and 98 afterward: only Z could occupy the removed l=3 bin. This refines the same containers, not an additional total to add to 26. The rank bounds of chapter145 remain SF≥4 and square rank≥28. Removing (4,3,3) does not prove SF≥5, surjectivity, full-adjoint invertibility or the original repair, and does not improve the separate cone rank36 result.

## Persistence forces exact endpoint degrees

For the hypothetical rank-four (3,3) plateau, write the actual saturated stages

    F₀ ⊂ F₁ ⊂ ⋯ ⊂ F₆,     E=F₃,     rank F_i=5+4i.

Interior derivative kernels and saturated transforms are the adjacent stages. A polynomial-section persistence argument works at both endpoints as well as inside: if i+d<6 then H⁰(F_i(d))=0, and the same holds for the reversed annihilator stages. This uses actual lines and characteristic-zero Taylor inversion, not a horizontal splitting of equivariant summands. The endpoint derivative ranks are not assumed four.

At i=3,d=2 it gives top degree E≤-3. The rank17, degree-54 budget leaves a total deficit of three below O(-3). The actual identity H¹(E(1))=W′+3T₆ then forces

    E=(W′+2T₆) O(-3)+V O(-4).

The short deficit argument proves this without regenerating the historical source enumeration. In particular V is the other three-space, distinct from the physical A₃=Sym²W.

Endpoint persistence gives all five degrees of F₀ at most -6, and F₆⊥=O(-e) with e≥6. If a=deg F₀ and b=deg F₆, then a≤-30 and b≤-6.

Set L_i=F_i/F_(i-1), c_i=deg L_i. The regular generically invertible derivative maps L_i→L_(i+1)(-2) give

    c_(i+1)=c_i+8+δ_i,     δ_i≥0.

Using deg F₃=-54 yields the exact identity

    a+b = -36+δ₁+2δ₂+3δ₃+2δ₄+δ₅.

The left side is at most -36 and the right side at least -36. Hence a=-30, b=-6, every δ_i=0, and

    (c₁,c₂,c₃,c₄,c₅,c₆)=(-16,-8,0,8,16,24).

All adjacent graded derivative maps are now genuine bundle isomorphisms. With B=L₃, rank B=4, degree B=0 and L_i=B(2i-6). This splits neither the filtered bundle nor its ambient connection. No invariant-divisor gap was needed to make the defects vanish.

## Twenty abstract quotients reduce to one

F₁ has rank9, degree-46 and top degree at most -5. Parity forces F₁=R₈ O(-5)+O(-6), while F₀=R₅ O(-6). The exact sequence at twist5 gives H¹(B(1))=0. Thus every ordinary degree of B is at least -2; rank4 and total degree0 bound the top degree by6.

F₂ has rank13, degree-54 and top degree at most -4. Its deficit of two allows only

    R₁₁ O(-4)+X O(-5),     X=W or W′,
    or R₁₂ O(-4)+O(-6).

Consequently H¹(F₂(3)) is W or W′, and H¹(F₂(4)) is either zero or the trivial representation. The actual long exact sequence at twist3 forces

    H⁰(B(3)) = W′+2T₆+X,     X∈{W,W′}.

There are exactly twenty unordered irreducible-block multisets of rank4, degree0, slopes -2 through6 and correct central parity. This is a newly derived finite abstract quotient problem, not a rerun of the old 28/37/159-record lists and not a realization theorem. Exact character calculation leaves only

    B=O(-2)+W′ O(-1)+O(4),

whose cubic character is W+W′+2T₆. There is no survivor with the extra W′ instead of W.

## The physical three-space gives the contradiction

At twist4, exact equivariant Euler additivity for 0→F₂→E→B→0 gives

    χ_G(F₂(4)) = 2V+2P-A₃,     A₃=Sym²W.

The ordinary dimension is eleven, consistent with rank and degree, so dimension counting does not exclude it. But the only possible H¹ correction is zero or the trivial representation. Hence H⁰(F₂(4)) would be either 2V+2P-A₃ or 2V+2P+1-A₃. Both retain coefficient -1 at the physical A₃ and cannot be genuine section representations. The sole abstract quotient is impossible, excluding the entire actual (4,3,3) stratum.

This does not import the old rank-three cubic pairing inequality at rank four. It uses the actual degree, persistence, determinant and cohomology identities for the rank-four plateau itself.

## Evidence and preservation

The partition proof has SHA256 `4e3444e45d39cab9f45d31b8c204fa8749b076e33a5ccc55a6fe2e06d20038ed`. Its four complete direct sources were freshly authenticated and independently read. Author and independent controls reproduce under ordinary and optimized Python, also from an unrelated working directory. The independent suite checks exact label sets, the full-ambient endpoint, source visibility, formal determinant identities and eleven negative/scope controls.

The rank-four proof has SHA256 `7fac6f279bc25dcc0561743dfae189dd70f2cf98e81ad11371745f1c954d4e6a`. Its final hash-bound independent whole-proof review accepts the conditional exclusion, including endpoint persistence, the L₁=B(-4) index, the direct source-deficit argument and both possible H¹ tails. The reviewer also derives the unique quotient by a separate positive-character argument, not merely by rerunning the author's enumeration. Its author certificate reports 768 checks under ordinary and optimized Python, with independent enumeration and character methods for the new twenty-shape problem. The written geometric proof, not a count of accepted controls, justifies persistence, saturation and actual cohomology prerequisites.

No actual HM coefficient, parameter, jet, matrix or instance rank is evaluated. The stopped experiments are not rerun. Chapter145 and all prior chapter files retain their original cutoffs; the delivered v0.3 PDF is unchanged.
