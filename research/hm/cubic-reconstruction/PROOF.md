# Canonical cubic splitting and regular reconstruction

This records the October 19, 2026 algebraic results in chronological order. The cubic result itself proves no obstruction vanishing. At this historical stage all thirty retained conditions were unknown; later symmetry reductions are separate results and are not imported into this proof.

## Public source order

1. [Filtration-only statement](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276362114): the abstract bundle alone does not choose a complement.
2. [Weighted remainder, October 19 20:32 UTC](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276688181): weighting the known alternating primitive gives zero, not a new primitive.
3. [Canonical cubic splitting, October 19 21:27 UTC](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6277692474): multiplication and normalized algebra trace correct the stronger no-canonical-complement claim.
4. [Regular reconstruction, October 19 22:53 UTC](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6279132359): a denominator-free inverse to evaluation, conditional on supplying the component primitives.

The underlying source release is [PR79](https://github.com/Akilleez-QA/read-em-and-weep/pull/79). The [complete mixed source](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716) and [raw-to-canonical comparison](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6274541018) remain dependencies. The [pinned raw closure proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-second-order-raw-closure/PROOF.md) is not duplicated here.

## Part I: Canonical cubic splitting

### Result and scope

The multiplication and trace of the binary-quartic factorization algebra supply a canonical complement that the abstract vector-bundle isomorphism alone does not supply. Work over characteristic zero, with the previously established finite locally free setup. Put

- B = m_*O_X, of rank six;
- A = B^+, the block-even algebra, of rank three;
- G = ker(Tr_6:A→O_Y), of rank two;
- W = H^0(Y,G(1)), a one-dimensional constant vector space;
- L = W⊗O_Y(−1), its canonical evaluation subbundle.

Here Tr_6 means the algebra trace on B, restricted to A. It equals twice the rank-three algebra trace Tr_3. Define the intrinsic multiplication-and-centering map

    b: W^{⊗2}⊗O_Y(−2) → G,
    b(w_1w_2) = w_1w_2 − Tr_6(w_1w_2)·1/6.

Its composite with G→Q=G/L is an isomorphism. Consequently b itself gives a canonical splitting

    G = L ⊕ K,       K = im(b) ≅ W^{⊗2}⊗O_Y(−2),
    A = O_Y·1 ⊕ L ⊕ K.

For any chosen nonzero generator σ of W, K is generated, with its twist, by

    τ = σ² − Tr_6(σ²)/6.

This is valid on every chart and at every branch fiber. There is no division by a quartic coefficient, a root difference, or a discriminant.

This supplies an unconditional canonical twenty-dimensional projection of the retained obstruction **using this additional algebra structure**. It corrects the blanket assertion in the earlier retained-filtration report that no such projection is available. Its narrower assertion remains correct: an abstract isomorphism G≅O(−1)⊕O(−2), or the canonical filtration alone, does not select a splitting.

Nothing here proves any actual mixed obstruction vanishes. At this October 19 stage, all thirty retained values remained unknown. Only universal exact scalar polynomial calculations and algebraic-sheaf arguments were used. 

### 1. Inputs and trace normalization

Public dependencies:

- [filtration-only statement](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276362114)
- [weighted remainder](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276688181)

Their imported bundle types are A≅O⊕O(−1)⊕O(−2) and G≅O(−1)⊕O(−2), with L canonical and Q of type O(−2). Their imported detector dimensions are ten and twenty. This report does not recalculate HM cohomology.

On the dense squarefree locus, A has three partition values, each repeated twice in the six ordered factorizations defining B. Therefore Tr_6|_A=2Tr_3 there. Both are regular sheaf maps on a locally free algebra over an integral base, so the equality holds globally. In particular, Tr_6(1)=6, Tr_3(1)=3, and the two correctly normalized centering operators agree:

    a − Tr_6(a)/6 = a − Tr_3(a)/3.

Using Tr_3(a)/6 instead would be incorrect.

### 2. Global proof that the square gives a complement

Define

    Φ: O_Y ⊕ W⊗O_Y(−1) ⊕ W^{⊗2}⊗O_Y(−2) → A

by the unit, the canonical evaluation, and b. This is defined intrinsically from multiplication, trace, and the already canonical W. Its source determinant has type O(−3), as does det A. Thus det Φ is a global section of a line bundle of type O_Y. Such a section is either identically zero or nowhere zero: after any identification of the constant line, it is a constant function on P⁴.

It remains to prove generic nonvanishing, without making a physical or numerical specialization. On the generic monic binary-root chart, let

    σ_1=(x1+x2)(x3+x4)−2(x1x2+x3x4),
    σ_2=(x1+x3)(x2+x4)−2(x1x3+x2x4),
    σ_3=(x1+x4)(x2+x3)−2(x1x4+x2x3).

These satisfy Σσ_i=0 and

    ∏_{i<j}(σ_i−σ_j)² = 3^6 ∏_{a<b}(x_a−x_b)².

This is a nonzero polynomial identity in independent indeterminates. Thus the generic σ_i are distinct. The three columns 1, σ_i, σ_i²−(Σσ_j²)/3 have nonzero Vandermonde determinant: subtracting a multiple of the unit column does not alter it. Hence Φ is generically invertible. Its constant determinant is nonzero, and Φ is a global isomorphism.

Equivalently, b followed by G→Q is a map between line bundles of the same type O(−2), so is a constant-line-valued scalar. Generic independence proves that this scalar is nonzero, giving the same everywhere-isomorphism conclusion. The constant scalar is not intrinsically a number until a separate trivialization of Q is chosen; the intrinsic assertion is the displayed isomorphism itself.

This proof uses the known splitting types only to identify the determinant type. It does not choose or use an arbitrary splitting to define Φ.

### 3. Constant lines and canonicity

W is the discriminant-polarization line. In the binary-vector-space convention of the earlier report it has the representation type (det V*)². The intrinsic square map takes W^{⊗2}, not an unlabelled scalar copy of O(−2). The construction proves

    Q ≅ W^{⊗2}⊗O_Y(−2),
    det G ≅ W^{⊗3}⊗O_Y(−3).

If σ is replaced by uσ for a nonzero constant u, then τ is replaced by u²τ. Thus L and K are unchanged. No choice of a volume form is needed for the subbundles, splitting, or projections; a volume choice merely writes their one-dimensional factors as numerical coordinates.

The canonical splitting Q→G is b composed with the inverse of its map to Q. The formerly available arbitrary splittings form a torsor under Hom(Q,L), of dimension five. Multiplication and normalized algebra trace select one point of this torsor, functorially for automorphisms of the binary-form algebra setup. Canonicity here refers to that structured setup, not to the bare underlying vector bundle.

### 4. Cubic resolvent with precise invariant convention

Write the quartic and a factorization with ordinary, unweighted coefficients:

    F(x,y)=a x⁴+b x³y+c x²y²+d xy³+e y⁴,
    q=u x²+v xy+w y²,       r=U x²+V xy+W y²,
    a=uU, b=uV+vU, c=uW+vV+wU, d=vW+wV, e=wW.

The normalization from the earlier reports is

    σ=vV−2(uW+wU).

Define the usual binary-quartic invariants

    I=c²−3bd+12ae,
    J=72ace+9bcd−27ad²−27b²e−2c³.

Then the following is an exact polynomial identity in the six independent quadratic coefficients:

    σ³−3Iσ−J=0.

It requires no monicity hypothesis. Under the chosen generator σ, the characteristic polynomial on A is therefore

    T³−3I T−J.

Indeed, it has the three generic partition values as roots, and equality extends regularly. Newton identities give

    Tr_3(σ)=0,       Tr_3(σ²)=6I,       Tr_3(σ³)=3J.

Consequently

    Tr_6(σ²)=12I,    τ=σ²−2I.

The multiplication table, interpreted in the appropriate twists, is

    σ² = τ+2I,
    στ = Iσ+J,
    τ² = 2I²+Jσ−Iτ.

These formulas present the algebra locally by the cubic resolvent, with basis 1,σ,τ (equivalently 1,σ,σ²).

**Sign-convention warning.** For a monic root polynomial

    z⁴−e1 z³+e2 z²−e3 z+e4,

one sometimes writes

    J_alt=2e2³−9e1e2e3+27e3²+27e1²e4−72e2e4.

Then J_alt=−J, the relation is σ³−3Iσ+J_alt=0, and the off-diagonal trace entry below is −6J_alt. There is no mathematical discrepancy.

Invariant line factors are understood as follows: fixing σ chooses scalar-coordinate expressions I and J; replacing σ by uσ replaces them by u²I and u³J. Intrinsically these are the corresponding maps from W² and W³ to H⁰(O(2)) and H⁰(O(3)).

### 5. Trace pairing and branch degeneracy

The rank-six algebra-trace pairing on the basis (1,σ,τ) is

    [ 6     0       0   ]
    [ 0    12I     6J   ]
    [ 0     6J    12I²  ].

In particular the two trace-zero generators are generally not orthogonal. The determinant of the G block is

    36(4I³−J²),

and the full determinant is

    216(4I³−J²).

For rank-three trace the entire array is halved, so the G-block determinant is 9(4I³−J²), and the full determinant is 27(4I³−J²).

With the ordinary quartic discriminant convention,

    4I³−J²=27 Disc(F).

Thus the rank-three full determinant is 729 Disc(F), agreeing exactly with the squared Vandermonde in §2. The rank-six full determinant is 5832 Disc(F).

The trace pairing degenerates along the quartic discriminant. This does not mean that 1,σ,τ cease to be a basis: it means that the algebra itself ceases to be étale and its trace pairing ceases to be perfect. At a repeated eigenvalue, evaluation at distinct reduced points no longer detects all directions of the nonreduced fiber. The determinant-line proof establishes the basis before specializing and remains valid in those fibers.

In particular, do not try to construct the splitting by inverting this Gram matrix. Such an inverse would introduce discriminant denominators and fail exactly where the actual global splitting remains regular. The construction in §2 involves no trace-pairing inversion.

### 6. The unconditional ten-plus-twenty detector

The new splitting canonically refines the earlier exact sequences to direct sums:

    D_30 = H²(B₀⊗L) ⊕ H²(B₀⊗K) = D_10 ⊕ D_20,
    T_30 = H²(B₀⊗L*⊗ω_Y) ⊕ H²(B₀⊗K*⊗ω_Y)
         = T_10 ⊕ T_20.

Here K≅Q via the original quotient map. The twenty-part projection exists whether or not the first ten-part projection vanishes. It agrees with the earlier canonical staged class when the first ten-part does vanish. This is a genuine additional algebraic splitting, not a proof that the first stage passes.

For the actual retained mixed class represented in finite duality by c_X, the two components, after choosing σ to display scalar coordinates, are

    C_10(σ) = Tr_m^ω(σ·c_X) ∈ H²(Y,B₀⊗ω_Y(1)),
    C_20(σ²) = Tr_m^ω(τ·c_X) ∈ H²(Y,B₀⊗ω_Y(2)).

Their intrinsic constant factors are W* and (W^{⊗2})*, respectively. In particular ω_Y(2) has the usual twist O(−3), not O(−2).

Finite-duality trace here is evaluation at the unit. No factor 1/6 multiplies these formulas. The fraction 1/6 occurs only in centering τ with the rank-six algebra trace. Explicitly, for λ∈Hom(B,ω_Y),

    Tr_m^ω(τλ)=λ(τ).

If the unweighted constant component already vanishes in cohomology, then the twenty-part weighted trace also equals Tr_m^ω(σ²c_X) in cohomology, since the difference is 2I·Tr_m^ω(c_X). At the cochain level this difference need not be zero; a known primitive for the constant part supplies its boundary correction.

The complete retained obstruction vanishes if and only if both displayed component classes vanish. No evaluation or primitive for either class has been obtained here.

### 7. Optional second-weight partition identity

With the signed transported source cochains r_i from the weighted-transgression report, put τ_i=σ_i²−2I. Then

    Στ_i=0,
    τ_i−τ_j=(σ_i+σ_j)(σ_i−σ_j)=−σ_k(σ_i−σ_j)

for the remaining index k. The same purely scalar coset-sum argument gives

    e(τR) = (1/9) Σ_{i<j}(τ_i−τ_j)(r_i−r_j).

Also e(τP)=0 for a sign-projected known primitive P. Thus the new canonical second weight supplies a precise second detector but does not rescue the failed strategy of multiplying the already solved common alternating primitive. All regularity and comparison-boundary qualifications in the prior weighted-transgression report remain in force.

### 8. Exact verification artifact

The accompanying check_splitting.py uses SymPy only for exact formal scalar polynomial identities. It checks:

1. The cubic relation after substituting the product of two fully generic quadratics, in six independent indeterminates.
2. The sum of the three generic root partition weights.
3. The squared Vandermonde identity with factor 729.
4. The invariant/discriminant identity 4I³−J²=27 Disc(F).
5. The nonzero coefficient 6912 of a³e³ in 4I³−J², without any numerical specialization.
6. Both nontrivial reduced multiplication relations involving τ.

Execution passed all explicit checks in both ordinary and python -O modes (no assert statements are used). No arbitrary parameter samples or physical data were used. The conclusions are algebraic structure and detector identification only; all thirty actual retained conditions were still open at this stage.


## Part II: Regular reconstruction

### Result and limits

Let A=O⊕L⊕L² with L=W⊗O_Y(−1), in the canonical centered cubic presentation of Part I of this proof. In a local frame write its basis as (1,σ,τ), with σ³=3Iσ+J and τ=σ²−2I. Let ε extract the coefficient of σ², equivalently of τ. The ε-dual basis is

    (τ+I, σ, 1).

For every actual A-dual-valued cochain λ, not only for its class,

    λ = ε( [λ(1)(τ+I)+λ(σ)σ+λ(τ)] · ).                 (1)

All maps in (1) are regular on the entire base, including every branch fiber. This is a coefficient-extraction Frobenius pairing, not an inverse of the algebra-trace pairing. Its determinant is −1.

This gives an exact reconstruction and an exact *conditional* primitive formula. It does not compute the weighted primitives or any physical value. The constant component is already exact by the imported comparison theorem; the first and second weighted components remain unsolved. At this October 19 stage, all thirty actual retained conditions remained unknown.

Dependencies: Part I of PROOF.md and AUDIT.md; [complete mixed source and correction equation](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716); [weighted remainder](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276688181); [filtration-only statement](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276362114). The latter's no-canonical-complement statement is superseded exactly as explained in the cubic report. No new claim is made about the explicitness of the comparison edge cochains in those inputs.

### 1. Frobenius calculation without localization

Work first over the universal scalar ring R=Q[I,J] in A_R=R[σ]/(σ³−3Iσ−J). The products are

    σ²=τ+2I,  στ=Iσ+J,  τ²=2I²+Jσ−Iτ.

Consequently the matrix of (a,b)↦ε(ab) on (1,σ,τ) is

    [[0,0,1], [0,1,0], [1,0,−I]],

with determinant −1. Direct multiplication proves ε(b_i d_j)=δ_ij for b=(1,σ,τ) and d=(τ+I,σ,1). This proves (1) over R, and by base change over every actual local chart. In particular no root difference, I, J, quartic coefficient, discriminant, or derivative of the cubic is inverted.

On the uncentered basis (1,σ,σ²), the dual basis is (σ²−3I,σ,1). Changing the third *test* from σ² to τ changes its dual partners: the dual basis to (1,σ,τ) is (σ²−I,σ,1). These two formulas are consistent because λ(τ)=λ(σ²)−2Iλ(1).

Define ε_r(a)=ε(ra). The normalized algebra-trace functional is

    η=Tr_A/3=ε_(τ+I).

Indeed η(1)=1 and η(σ)=η(τ)=0. More generally

    Tr_A(a)=ε((3σ²−3I)a)=ε(f'(σ)a),
    f(T)=T³−3IT−J.

Thus it is the multiplication-by-f'(σ) comparison between ε and algebra trace that becomes singular on branch fibers. The Frobenius functional ε itself remains perfect. Calling ε a normalized algebra trace would be incorrect.

### 2. Intrinsic line factors and globalization

The centered algebra splitting supplies a canonical projection

    E:A→L²,

onto its final summand. Multiplication followed by E is a perfect L²-valued pairing. It gives a global isomorphism

    A ≅ Hom_O(A,L²),
    A^∨ ≅ A⊗L^(−2).

Here E is intrinsic. The scalar functional ε is its local expression after trivializing L²; generally there is no canonical globally O-valued ε. Thus A is globally Frobenius with values in the line L², and locally an ordinary Frobenius algebra.

Choose a frame ℓ of L and let σ be its image. The local scalar I and J are the coefficients of the intrinsic maps L²→O and L³→O. When ℓ'=uℓ, including nonconstant invertible chart-transition functions,

    σ'=uσ,  I'=u²I,  J'=u³J,  τ'=u²τ,
    ε'=u^(−2)ε.

If λ takes values in a coefficient bundle F, set a_i=λ(b_i). Then a_0'=a_0, a_1'=u a_1 and a_2'=u²a_2. The expression inside ε in (1) transforms by u², so (1) agrees on overlaps. All Čech coefficient-line transitions are retained; this is not a global trivialization of O(1) or W.

For F=B₀⊗ω_Y the three coordinates are intrinsically cochains in

    F,
    F⊗L^∨ = W^∨⊗B₀⊗ω_Y(1),
    F⊗(L²)^∨ = (W²)^∨⊗B₀⊗ω_Y(2).

For Y=P⁴ their nonconstant ordinary twists are B₀(−4) and B₀(−3). The global coordinate inverse in (1) is a sheaf map; therefore it commutes with the Čech differential on a compatible cover. Variable chart frames cause no derivative-of-u terms because this is the ordinary Čech differential, not a differential operator in base coordinates.

### 3. Rank-six finite duality versus the rank-three even algebra

Let B=m_*O_X, rank six, with block exchange ι and even subalgebra A=B^+. Write

    π_+=(1+ι)/2:B→A.

A functional on A extends to B by λ↦λ∘π_+. Its restriction back to A is λ, with no factor two. For an arbitrary B-functional Λ, its even part is Λ∘π_+; its three evaluations at 1,σ,τ reconstruct exactly that even part, and cannot reconstruct an arbitrary odd part.

Finite duality m_*ω_X≅Hom(B,ω_Y) has trace

    Tr_m^ω(Λ)=Λ(1),    Tr_m^ω(wΛ)=Λ(w).

Hence the actual weighted cochains are a_0=Λ(1), a_1=Λ(σ), a_2=Λ(τ). No /6 and no /3 is applied to any of these evaluations.

Algebra trace is a separate map. Tr_B|_A=2Tr_A, and Tr_B vanishes on the odd summand, since it is invariant under ι. Therefore the extension of η to B is exactly Tr_B/6. The factors /6 or /3 appear in this normalized inclusion of the constant-dual summand and in centering, not in finite-duality trace itself.

In particular on the even dual, the canonical constant and retained projections are

    P_const λ=η·a_0,
    P_ret λ=λ−η·a_0=ε([a_1σ+a_2]·).                  (2)

The retained dual has rank two. Its weights σ and τ annihilate the constant-dual inclusion. Neither the existence of (2) nor a class lying in its image implies that the initial representative is already in that image.

### 4. Exact primitive on the even complex

Let c_A be a closed two-cochain in F⊗A^∨. Set a_i=c_A(b_i). If regular one-cochains p_i in their indicated line-twisted coefficient bundles satisfy

    δp_0=a_0,  δp_1=a_1,  δp_2=a_2,

then the following is a regular one-cochain:

    H_A=ε([p_0(τ+I)+p_1σ+p_2]·),
    δH_A=c_A.                                          (3)

The retained primitive is ε([p_1σ+p_2]·). If only p_0 is known, one has the literal identity

    c_A−δ(ηp_0)=P_ret c_A,

not c_A=P_ret c_A. Thus p_0 must be restored when correcting the original representative.

If one instead has δp_sq=c_A(σ²), then p_2=p_sq−2Ip_0 satisfies δp_2=a_2. Conversely p_sq=p_2+2Ip_0. Multiplication by the invariant section I is interpreted in the corresponding line twists and commutes with δ.

No input inspected supplies explicit p_1 or p_2 for the actual mixed source. Formula (3) gives them no automatic existence. It is a regular inverse to the three evaluation maps, not a new vanishing theorem.

### 5. Recovering the original mixed module correction: all boundaries and signs

Let D be the actual normalized mixed defect g_ik^(−1)R_ijk from [complete mixed source](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716) formula (6), with its End(E)-valued coefficient. Its mixed correction satisfies δx=−D; adding g_ij x_ij to the mixed transition changes the defect by δx.

First choose a scalar one-cochain k with δk=tr_E D and put

    h_sc=(k/2)Id_E,   D_0=D−δh_sc.

The division by two here is the rank of E, unrelated to either finite algebra rank. The imported scalar vanishing guarantees existence of k on an acyclic cover, not a displayed formula for k.

On a fixed compatible common complex, let c_B be the finite-duality image of D_0. Set c_A=c_B|_A and let i_+ extend A-functionals by π_+. The literal residual is

    c_−=c_B−i_+c_A.

If only the cohomology class is known even, the conclusion is existence of a regular one-cochain h_− with δh_−=c_−. It is not the conclusion c_−=0. In conjunction with (3),

    c_B=δ(h_−+i_+H_A).

Returning through the compatible finite-duality/cochain identification F, a primitive of the original D and the required correction are

    H_orig=h_sc+F^(−1)(h_−+i_+H_A),
    x=−H_orig.                                         (4)

The notation F^(−1) assumes the selected common complex where the identification is literal. For complexes connected only by refinement/quasi-isomorphism, use the actual chain comparison and its boundary homotopy; an abstract cohomology inverse does not provide an inverse on cochains.

More generally, if a chosen reconstructed representative c_model and the actual representative satisfy c_actual=c_model+δb, then

    x=−b−H_model.

If the comparison is instead written c_model−c_actual=δq, then x=q−H_model. This elementary sign rule applies independently to refinement, tracefree normalization, odd-part removal, pure-gauge changes, or any other representative comparison. Do not omit these boundary primitives. Formula (4) is a conditional construction only until all its required regular one-cochains are exhibited.

For example the input's pure-gauge comparison is D(u',v')−D(u,v)=−δ(g_ij^(−1)Q_ij). Thus a primitive for the new D is H_orig−g_ij^(−1)Q_ij, and its correction is x+g_ij^(−1)Q_ij, in the identified normalized coefficient convention.

### 6. The raw-source comparison boundary and weighted primitives

To connect (3) to the known alternating transgression, retain exactly the imported convention

    R_raw−j(c_B)=δq.

Here q is the regular comparison edge cochain whose existence follows from the class comparison; none of the inspected reports computes it. If the admitted comparison holds only after a deck projector, apply that projector consistently to R_raw, j(c_B), and q first. Its weights are deck invariant.

Write e for the full sign projector, w_0=1, w_1=σ, w_2=τ, and I_const for the injective normalized constant-functional realization upstairs (this symbol is unrelated to the quartic invariant I). The admitted finite-duality identification gives

    e(w_i R_raw)=I_const(a_i)+δe(w_i q).

If regular upstairs primitives H_i satisfy δH_i=e(w_i R_raw), then

    p_i=I_const^(−1)(H_i−e(w_i q))                    (5)

is the desired primitive *provided* the parenthesized cochain is in the compatible I_const-image. If H_i is not initially in that image, first use the established constant-coefficient projection/identification on that complex, or its supplied chain map; membership cannot be inferred merely because its differential is in the image. Formula (5) is to be read after this compatible projection. Its differential is exactly a_i.

The known H_0=P supplies the already-exact constant component, after this same q correction and coefficient identification. No H_1 or H_2 is supplied by the inputs. In particular e(σP)=e(τP)=0 for a sign-projected P, so weighting that known primitive does not fill the missing slots.

The two sorts of comparison boundaries are distinct: q compares the raw upstairs source to the actual finite-duality source; h_− corrects the discarded odd cochain, and ηp_0 corrects the discarded constant cochain. Class-level transfer statements alone do not authorize setting any of them to zero. If an explicit equivariant comparison already makes an odd part identically zero, that additional fact removes h_− in that comparison, but is not assumed here.

### 7. Exact checks and stopping point

check_reconstruction.py uses only the formal universal scalar algebra Q[I,J,σ]/(σ³−3Iσ−J) and free coefficient symbols. It checks the Gram matrix and determinant, dual basis, full functional reconstruction, normalized algebra trace, the f' trace identity, line-frame covariance, the formal primitive reconstruction, and the two nontrivial multiplication relations. Its small multiplication matrix represents only this abstract scalar algebra, never physical/source transition matrices. Checks use explicit exceptions, not assert, and pass both ordinary Python and python -O.

The completed deliverable is a global regular reconstruction map and the fully qualified primitive/sign formula. No actual weighted primitive has been found. At this October 19 stage, all thirty retained conditions remained unknown.
