# Invariant exclusion of the maximal-degree exceptional direction

Assume the model and first-stage hypotheses of [README.md](README.md), over an algebraically closed field of characteristic zero. Suppose the nonzero exceptional direction h₀ lies in the canonical maximal O(2) subbundle of U=O(2)⊕O(1)². Then every first-stage pair satisfying the full central gluing and isotropy criterion has ordinary-fiber rank failure. Consequently it cannot define a globally surjective last monad map. This holds for every actual primitive presentation 0→O(-4)→O⁴→U→0; there is no monomial, ramification, or genericity hypothesis.

## 1. Why the subscroll and normalizations are legitimate

The maximal line subbundle A≅O(2) of U is canonical: Hom(O(2),O(1))=0, so the Harder–Narasimhan maximal subbundle is unique. With the projective-bundle convention p_*O_Y(1)=U, the quotient U→U/A defines a canonical closed subscroll

    Σ=P(U/A)⊂P(U),  U/A≅O(1)².

In any splitting U=A⊕O(1)² it is X=0. Thus the argument is not using a supposedly canonical *complement* to A. A different splitting changes coordinates but not this quotient subscroll.

Choose t=0 at the exceptional base point, and scale the frame X so that h₀=-X. For the image of the fixed ambient linear form h, its coefficients in the split U have degrees 2,1,1. Consequently

    h_Y=-X+t k,

where k is regular on the entire finite base chart; its restriction to Σ is a constant binary linear form. The local ambient lift is h=h_Y+ell k₀ with regular k₀. Keeping this term is necessary for a completely general presentation.

The actual extension splits on both standard affine base charts. Changing these splittings by regular Hom(U,O(-4))-sections reduces its three Čech components to

    D_X∈span(t⁻¹,…,t⁻⁵),
    D_Y,D_Z∈span(t⁻¹,…,t⁻⁴).

Such changes preserve regular local lifts: the finite lift of h still has a regular coefficient k₀. They do not change the intrinsic coordinates or section q on U. On the infinity chart a is a unit, so Q_D=0 and Q_C=q/a are regular regardless of the chosen extension splitting. Thus reduced representatives and this infinity-chart normalization can be imposed simultaneously.

## 2. The connecting matrix really is invertible for all actual presentations

Twist the actual exact extension by O(-1). Both cohomology groups of its middle term O(-1)⁴ vanish, so

    δ:H⁰(U(-1))→H¹(O(-5))

is an isomorphism. In the finite-chart basis (X,tX,Y,Z), its columns are the classes of D_X,tD_X,D_Y,D_Z. Modulo exponents ≥0 and ≤-5 these are precisely

    M=[(d₁,d₂,d₃,d₄)ᵗ,
       (d₂,d₃,d₄,d₅)ᵗ,
       (y₁,y₂,y₃,y₄)ᵗ,
       (z₁,z₂,z₃,z₄)ᵗ].

The shift in the second column is correct. The matrix is invertible because the extension's middle term is O⁴, not because arbitrary extension coefficients would have this property. The exact checker `verify_maximal.py` reconstructs these columns independently and additionally checks a dense nonmonomial sample with determinant 1282. The sample is a consistency check; the exact-sequence argument proves the universal statement.

## 3. Complete first-stage and primary calculation

The coefficient degrees of q∈H⁰(Sym²U(-1)) are 3,2,1 on X², the mixed terms, and the low binary terms respectively. Vanishing on Λ=(t,X) gives

    q_i=X G_i+t F_i,
    q_i|Σ=t b_i,
    (∂_X q_i)|Σ=g_i+t l_i+t² m_i,

with G_i constant linear, b_i constant quadratic in Y,Z, and g_i,l_i,m_i constant binary linear forms. This accounts for all 13 intrinsic first-stage parameters. Each section has its additional independent scalar λ_i from the vertical torsion, so the full first-stage dimension is 14 per column.

Put C_i=F_i+kG_i. An allowed full finite-chart lift is

    Q_C,i=C_i,  Q_D,i=G_i+ell λ_i.

On Λ, Q_C,i=b_i+k g_i and Q_D,i=g_i, giving the exact primary cubic

    P=b₁g₂-b₂g₁=0.

For clarity, an explicit regular isotropy solution with r=0 is available even when k₀≠0. Write

    H=F₁G₂-F₂G₁=X W+t H₁.

This is possible precisely when P=0: take W=H(0,X,Y,Z)/X and then H₁=(H-XW)/t. With λ=λ₁ and μ=λ₂, choose

    u=H₁+kW,
    v=λ C₂-μ C₁-k₀W,
    w=W.

Direct substitution gives t u-ell v-h w=Q_C,1 Q_D,2-Q_C,2 Q_D,1. In particular the ambient lift contributes the term -k₀W in v; omitting it from a claimed full isotropy solution would be incorrect. This gives the required regular local solution.

## 4. Full corrected overlap, including ambient and torsion terms

Let q_shift be the same intrinsic quadratic expressed in the transported infinity lifts, whose difference from the finite lifts is ell(D_X,D_Y,D_Z). Then

    Q₁=(q_shift/t,0),  A=L⁻¹(Q₁-Q₀)=VᵗJ.

Reduction modulo ell gives

    A₁,i=(Dq_i+k₀G_i+h_Yλ_i)/t,
    D=D_X∂_X+D_Y∂_Y+D_Z∂_Z.

Quadratic terms in the coordinate shift are proportional to ell², and disappear only after the correct division by ell and reduction modulo ell. They were retained in the independent matrix test.

Take R₁=0 on the infinity chart; it solves isotropy because Q_D=0. For

    C=-R₀-Q₀V-(1/2)L VᵗJV,

the quotient map M→I_D O_Y(-7,3) is represented by (t,-h) applied to the first column. Since (t,-h)L=(t ell,0) and (VᵗJV)₁₁=0, the image is exactly

    T=-ρ₀-q₁A₁,2+q₂A₁,1,
    ρ₀=-h_Yv.

This derives the sign from the full matrix convention. The half correction is retained in C; its projection happens to vanish. Dropping it before establishing that C is a syzygy is not justified.

Restrict to Σ and set B₁=b₁l₂-b₂l₁, B₂=b₁m₂-b₂m₁, W_Y=b₁∂_Yb₂-b₂∂_Yb₁, W_Z=b₁∂_Zb₂-b₂∂_Zb₁. **Before** imposing the primary condition, direct calculation gives

    T|Σ = -(D_X+k₀)P
           -tD_X B₁-t²D_X B₂-tD_Y W_Y-tD_Z W_Z
           +t k(v-b₁μ+b₂λ).

This identity contains every ambient-lift, first-stage torsion, and local-isotropy contribution needed for the projection. After P=0, the final term is regular and divisible by t; it contributes to none of the forbidden Laurent exponents. No assertion that these terms disappear from the full 27-dimensional obstruction is needed or made.

## 5. The projected ideal and the zero Laurent coefficient

The image of the sheaf homomorphism

    I_(t,h_Y²) O_Y(-7,3) → O_Σ(-7,3)

is precisely t O_Σ(-7,3), because h_Y|Σ=t k and hence (t,h_Y²)|Σ=(t). This is a morphism to the image sheaf, not an assumption that tensor restriction preserves an exact sequence. It induces a valid map on H¹, so a zero full central class has zero projected class.

Each low cubic Y³,Y²Z,YZ²,Z³ has ambient coefficient degree -4. On the finite chart the projected image consists of polynomials divisible by t, so allowable exponents are ≥1. On the infinity chart it is the whole O(-4) frame, with transported polynomial exponents ≤-4. The exact quotient therefore retains

    t⁻³,t⁻²,t⁻¹,t⁰.

Equivalently its four coefficient summands are O(-5), each with h¹=4. In particular the exponent-zero equation is part of the actual projected obstruction; treating the target as O(-4) would lose it. Terms with exponent -4 are valid infinity boundaries, not extra equations.

In coefficient order (0,-1,-2,-3), the four equations are

    M (B₁,B₂,W_Y,W_Z)ᵗ=0.

The exact checker `verify_maximal.py` obtains this from the complete projected matrix expression above, not from the claimed coefficient formula. Different local choices of R add the corresponding finite/infinity boundaries, and cannot cancel any of these retained coordinates.

## 6. Proportionality and the actual rank contradiction

Since M is invertible over the ground field, the polynomial identities force B₁=B₂=W_Y=W_Z=0. Euler's identity also gives W_Y=ZΔ and W_Z=-YΔ. Writing b₁=aY²+bYZ+cZ² and b₂=AY²+BYZ+CZ² yields

    Δ=(Ab-Ba)Y²+2(Ac-Ca)YZ+(Bc-Cb)Z².

In characteristic zero, Δ=0 is exactly vanishing of the three 2×2 minors of the two coefficient vectors. They have rank at most one, including either or both quadrics being zero. Thus b₁,b₂ are proportional without any assumption of simple roots.

If they both vanish, choose any constant section of Σ≅P¹×P¹. Otherwise choose a projective root of their common nonzero binary quadratic, which exists over the algebraically closed field. The resulting constant minimal section Γ lies scheme-theoretically in V_Y(q₁,q₂), because q_i|Σ=t b_i everywhere on the base. Its quotient U→O(1) gives deg O_Y(0,1)|Γ=1.

The global-residue lemma in §6 of [central-criterion.md](central-criterion.md) makes the invariant cubic residue a *global regular* section on the common-zero scheme, including the exceptional point. Pullback to Γ is therefore a section of

    O_Γ(-7,3)≅O_P¹(-4),

and is identically zero. A hypothetical pole at the exceptional point cannot rescue it. On every ordinary fiber t≠0, the rank-minor ideal on ell=0 is generated by q₁,q₂,ρ; therefore each ordinary point of Γ is an actual rank failure. The central completion torsion scalar cannot alter this global residue on Γ.

This proves the claimed exclusion for all presentations in the stated direction stratum. It does not require an exceptional-fiber rank argument, first-stage independence, generic regularity of the quadrics, stability, or a mixed-Atiyah conclusion.

## 7. Reproducible checks and limits

The self-contained exact checker [verify_maximal.py](verify_maximal.py) verifies the generic projected matrix identity, the regular isotropy solution with its ambient-lift correction, all 13 intrinsic first-stage monomials, the connecting-map columns, the Čech exponent window, the four projected coefficient equations, and the binary-minor identity. It imports only SymPy, not an obstruction tensor or another verifier.

The canonicality, connecting-map isomorphism, passage to the image sheaf, and negative-degree residue contradiction are geometric arguments supplied above. Finite symbolic and rational checks corroborate them; the checks alone are not a proof of the global statements.

The direction with nonzero image in U₀/O(2)₀ remains outside this theorem. This result makes no claim of full τ=1 closure, existence of a carrier, stability, or mixed-Atiyah vanishing.
