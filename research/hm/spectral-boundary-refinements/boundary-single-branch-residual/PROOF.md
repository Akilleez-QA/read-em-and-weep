# Exact residual ideal of a single boundary branch

## Theorem and dependencies

Work over C with the tensor and determinant-defined schemes B→D of ../boundary-relative-rigidity/PROOF.md. Fix p∈D(C) with exactly one closed boundary rectangle b. Set A=O_{D,p}, a local Artin C-algebra, m its maximal ideal. The unique boundary branch is Spec(A/I). This note constructs I explicitly in two independently justified ways.

The relative construction in Sections 2–4 of ../boundary-relative-rigidity/SIMPLE_SPECTRUM_AUDIT.md does not require three branches: over A it gives free modules E of rank three and K, a symmetric β:E×E→K, a perfect scalar member q=λ₀β, and q-selfadjoint operators T_λ=q⁻¹(λβ). The closed vector-valued quadratic satisfies β₀(v,v)≠0 for all v≠0. The entire boundary is the common-eigenline scheme, and its unique closed line a₀ is q₀-nonisotropic. These are statements over the actual Artin ring, not its reduction. The predecessor PROOF.md, Section 5, also proves that the vertical tangent map at a₀ is injective.

Main conclusions:

1. In any projective chart at a₀, choose two scalar common-eigenline equations with invertible vertical 2×2 Jacobian. Their unique solution x*= (x*₁,x*₂)∈m×m is computable by a finite Newton process. Substituting x* into all remaining equations gives elements r_a∈A which generate exactly I.
2. A simple-spectrum scalar member always exists when there is a common eigenline; an elementary proof below excludes the defective possibilities rather than assuming diagonalizability. Its three spectral lines over A give vectors c₁₂=β(s₁,s₂), c₁₃=β(s₁,s₃), c₂₃=β(s₂,s₃), with s₁ reducing to a₀. Then I is exactly the coordinate ideal of (c₁₂,c₁₃), while the coordinate ideal of c₂₃ is A.
3. The first-order obstruction is explicitly T_pD→coker(J_vert), ξ↦[d_AF(ξ)]. Its kernel is the image of T_bB. Vanishing of this linear map alone does not imply I=0. Exact full-Artin lifting is equivalent to all residuals being zero.

Throughout the rest of this note m^r denotes an ideal power; ordered pairs in m are written m×m to avoid ambiguity.

## 1. Explicit projective equations

Choose an A-basis e₀,e₁,e₂ of E whose first reduction spans a₀. Represent the chart of lines with first coordinate a unit by

    v(x)=e₀+x₁e₁+x₂e₂.

Choose a basis λ₁,…,λ_k of K*, write T_a=(t^a_ij) for the matrix of T_{λ_a}, indexed 0,1,2, and put

    F_{a,i}(x)=t^a_i0+Σ_{j=1}²t^a_ij x_j
                 −x_i(t^a_00+Σ_{j=1}²t^a_0j x_j),   i=1,2.

These 2k polynomial equations say exactly that T_av(x) is a multiple of v(x), with its eigenvalue fixed by the zeroth coordinate. Thus they define the common-eigenline scheme on this chart over every A-algebra. The nonisotropic condition q(v,v) invertible is automatic in the local branch because its residue is nonzero. There is no extra equation from that open condition.

All F_{a,i}(0) lie in m. Let F be their column vector, N=2k, and

    J= (∂F/∂x)(p,0): C²→C^N.

The previously proved fiber tangent rigidity says ker J=0. Select two rows by a projection P:C^N→C² with M=PJ invertible, and let G=PF, using the same row-selection over A. The remaining rows are denoted H. A scalar equation for the identity operator may be redundant; select only rows that give the required minor. No independence of all the equations is assumed.

## 2. Finite exact Newton solution, not a formal existence assertion

Start x^(0)=0. At each step put

    x^(n+1)=x^(n)−DG(x^(n))⁻¹G(x^(n)).

Every x^(n) belongs to m×m. The determinant of DG there reduces to det M≠0, so the inverse is an actual matrix over A. Polynomial Taylor expansion shows that if G(x^(n)) lies in (m^r)×(m^r), then G(x^(n+1)) lies in (m^{2r})×(m^{2r}). Since G(0) lies in m×m, finitely many iterations give G(x*)=0 exactly. A nilpotence exponent m^L=0 bounds the required iterations by any n with 2^n≥L.

Uniqueness: for x,y∈m×m, polynomial differences give

    G(x)−G(y)=U(x,y)(x−y),

where U(x,y) reduces to M. Therefore U is invertible, and two zeros with closed value zero agree. This same proof works over any local Artin A-algebra R, for x,y in its maximal ideal, since the residue Jacobian remains invertible. Consequently x* is functorial: its image is the unique zero of G reducing to zero after every such base change. Newton is a finite exact operation on nilpotent coefficients, not a convergence claim in an analytic topology.

Define

    r=H(x*) ∈ A^{N−2},      I_res=(all coordinates of r).

For every local Artin A-algebra R, a boundary lift exists if and only if I_res maps to zero, and then its line is uniquely Rv(x*). Indeed every lift solves G and hence has x=x*, while the remaining equations are precisely r=0. The complement is v(x*)^⊥ and the original rectangle is recovered by the inverse-image construction in H from the predecessor proof.

This identifies I_res with I exactly, not just up to radical or tangent ideal. For example, the universal branch over A/I supplies a zero of all F and hence I_res⊂I. Conversely the constructed solution over A/I_res supplies a boundary lift, whose factorization through the unique branch implies I⊂I_res. Thus I=I_res. This also proves that changing the chart, matrix bases, or chosen invertible minor changes the displayed generators but not the resulting ideal.

Equivalent completed-ring check: translating x to x* and using the same invertible-Jacobian elimination gives A[[x₁,x₂]]/(G)≅A; the images of the other equations are exactly r. This is a local/completed assertion, not a claim that the full affine zero scheme of G has no other distant points.

## 3. The explicit linear obstruction and its meaning

Write d_A F(ξ) for applying ξ∈T_pD=Hom_C(m/m²,C) coefficientwise to F(0) modulo m². For a first-order pair deformation ξ and line deformation w∈C², the linearized equations are

    d_A F(ξ)+Jw=0.

Therefore

    ob:T_pD→coker J,        ob(ξ)=[d_A F(ξ)]

is a linear obstruction map. A lift exists precisely when ob(ξ)=0 and is unique because J is injective. Thus T_bB is identified with ker ob inside T_pD.

The selected equations solve w=−M⁻¹P d_A F(ξ). Define the projection

    Π=id_{C^N}−J M⁻¹P.

Its kernel is im J and its image is ker P, so it identifies coker J with ker P. Under this identification ob is Πd_A F. The nonselected coordinates are exactly the first derivatives of r, since differentiating G(x*)=0 gives dx*=−M⁻¹P d_A F. This ties the explicit residual ideal directly to the intrinsic lifting obstruction.

Choices of projective coordinates alter d_AF by an element in im J; changes of equation generators may change the presentation of the obstruction target. Its vanishing criterion and the tangent subspace are intrinsic. We do not claim this particular cokernel is a minimal intrinsic obstruction space.

Full-Artin criteria:

    I=0 ⇔ r=0 in A ⇔ the rectangle lifts over A
        ⇔ B_A≅Spec A over Spec A.

For a specified A→R, replace r=0 by its image being zero in R. By contrast ob=0 says only I⊂m². It implies I=0 if m²=0, but not in general. The abstract example A=C[t]/(t³), I=(t²) illustrates this logical distinction; no realization of that example by the original tensor is asserted.

## 4. An elementary simple-spectrum lemma in the presence of a branch

We prove the structural refinement without a hidden semisimplicity assumption. Work first over C. A common eigenvector v satisfies λβ₀(v,v)=α_λq₀(v,v) for every λ. Hence q₀(v,v)≠0, and the orthogonal splitting E₀=Cv⊥W has dim W=2. Selfadjointness yields

    T_λ=α_λ⊕S_λ,

where α_λ and S_λ depend linearly on λ and S_λ is q₀|W-selfadjoint. The cubic discriminant factors as

    disc(T_λ)=disc(S_λ) det(S_λ−α_λ id_W)².

The parameter space K₀* is an affine vector space with an integral polynomial ring. If no member has simple spectrum, one of the two displayed factors is identically zero.

Case 1: disc(S_λ) is identically zero. Put A_λ=S_λ−½tr(S_λ)id. In a q₀|W-orthonormal basis, a traceless selfadjoint matrix has form [[a,b],[b,−a]], and −det=a²+b² is a nondegenerate quadratic form in two variables. The linear image of λ↦A_λ lies in its null cone; polarization makes this image totally isotropic, so its dimension is at most one. If the image is zero, any isotropic vector z∈W is a common eigenvector. Otherwise A_λ=c_λN with N≠0, N²=0; ker N=im N is an isotropic line, because q₀(Nx,Nx)=q₀(x,N²x)=0. Again an isotropic z is a common eigenvector. In both cases λβ₀(z,z)=q₀(T_λz,z)=0 for all λ, contradiction.

Case 2: det(S_λ−α_λid) is identically zero. Determinant ac−b² is a nondegenerate quadratic form on the three-dimensional space of selfadjoint 2×2 matrices [[a,b],[b,c]]. The linear image of λ↦S_λ−α_λid is totally isotropic and therefore has dimension at most one. If it is nonzero, it is generated by a singular matrix N and has a fixed nonzero kernel vector z. If it is zero, choose any nonzero z∈W. Then T_λz=α_λz for all λ, so every vector in span(v,z) is a common eigenvector with the same tuple of eigenvalues. A homogeneous quadratic on a complex plane has a nonzero zero, so this plane contains a q₀-isotropic nonzero y. It gives β₀(y,y)=0, contradiction.

Both cases are impossible. The simple-spectrum members form a nonempty Zariski-open set. In particular the exactly-one-branch case cannot be dismissed as necessarily defective. The argument uses existence of a common line, but not existence of three common lines, commutativity of the full family, or simultaneous diagonalizability.

The independent supplement ../boundary-relative-rigidity/SIMPLE_SPECTRUM_AUDIT.md strengthens the lemma to all such β, including zero-branch fibers, by choosing a scalar quadric transverse to the smooth q-conic. Its proof explicitly handles repeated eigenspaces and defective Jordan blocks. The elementary argument above remains a separate proof sufficient for the present one-branch theorem.

## 5. Stronger exact spectral residual vectors

Choose λ_* with simple closed spectrum and lift it to K*. Let T=T_{λ_*}. Its three distinct closed characteristic roots lift uniquely to roots ρ₁,ρ₂,ρ₃∈A; this follows by the same simple-root Newton argument, followed by polynomial division. Their differences are units, and the characteristic polynomial is ∏(t−ρ_i). The idempotents

    e_i=∏_{j≠i}(T−ρ_j id)/(ρ_i−ρ_j)

are orthogonal, sum to id, and have free rank-one images L_i=e_iE. The lines are pairwise q-orthogonal, q|L_i is perfect, and E=L₁⊕L₂⊕L₃. Label L₁ so that its closed fiber is a₀ and choose generators s_i.

The eigenline scheme for T is exactly three disjoint copies of Spec A. On the chart of its i-th closed eigenline, a generator can be written s_i+Σ_{j≠i}x_js_j. The eigenvalue equation first gives μ=ρ_i and then (ρ_j−ρ_i)x_j=0, hence x_j=0 over every test ring. These charts cover the eigenline scheme since the closed eigenscheme has just those three points.

Define c_ij=β(s_i,s_j)∈K and J_ij as its coordinate ideal, equivalently the image ideal of the pairing K*→A, λ↦λ(c_ij). The full common-eigenline scheme is

    ⨿_{i=1}³ Spec(A/(J_ij+J_ik)),  {i,j,k}={1,2,3}.

Indeed common invariance of L_i is exactly β(L_i,L_i^⊥)=0 and its complement is L_j⊕L_k. Thus the spectral equations are exact over A and under every base change.

Since only L₁ is common in the closed fiber, J₁₂,J₁₃⊂m while the other two candidate schemes are empty. From J₁₂+J₂₃=A and locality it follows J₂₃=A (alternatively c₂₃ has a nonzero residue coordinate). Consequently

    I=J₁₂+J₁₃=(coordinates of c₁₂ and c₁₃),    J₂₃=A.

This is the requested explicit residual ideal in a particularly simple coordinate system. The two absent candidates cannot acquire lifts over any nonzero local Artin A-algebra, because their ideals already contain 1. The ideal and the branch are intrinsic; the generators depend on the separating scalar choice and bases.

Both scalar functionals λ₀ and λ_* annihilate every c_ij identically: λ₀(c_ij)=q(s_i,s_j)=0 and λ_*(c_ij)=q(Ts_i,s_j)=ρ_iq(s_i,s_j)=0. Their reductions are independent, since proportionality would make T₀ scalar. Therefore the simultaneous kernel

    K'=ker((λ₀,λ_*):K→A²)

is a free direct summand of rank rank(K)−2. The two residual vectors c₁₂,c₁₃ actually lie in mK' and give at most 2(rank K−2) generators for I. In the single-branch case c₂₃∈K' has a unit coordinate, so rank K≥3.

Their linear terms give explicit maps

    κ₁j:T_pD→K'₀,   κ₁j(ξ)=ξ(c₁j mod m²K'), j=2,3,

and T_bB=ker κ₁₂∩ker κ₁₃. Full lifting over A is equivalent to c₁₂=c₁₃=0, not merely κ₁₂=κ₁₃=0.

## 6. Compatibility of the two constructions and next-order lifting

In the spectral chart at L₁ the two equations for T alone are (ρ₂−ρ₁)x₂=0 and (ρ₃−ρ₁)x₃=0. They supply the invertible minor in Sections 1–2, and x*=0. All other operator equations then have constant residual coordinates λ(c₁j)/q(s_j,s_j), with q(s_j,s_j) units. This directly identifies the Newton residual ideal with J₁₂+J₁₃, without relying only on uniqueness of the abstract branch.

For completeness, the same explicit presentation supplies obstruction tests through all nilpotent orders. Let R'→R be a small extension of local Artin A-algebras with kernel M killed by the maximal ideal of R', and suppose the branch lifts over R. Evaluate the residual vector r in R'; its coordinates lie in M and, for this fixed presentation, are independent of auxiliary choices of a line lift because x* is functorial. They vanish exactly when the branch lifts to R', and the lift is then unique. Equivalently evaluate (c₁₂,c₁₃) in (M⊗_C K'₀)². Applying this successively to the m-adic quotients detects the first nonzero order of I; a zero first-order obstruction does not stop these higher tests.

More intrinsically, for a prescribed polar lift α′:A→R′ across any square-zero extension R′→R with kernel M and α(I)=0, restriction defines an A/I-linear map I/I²→M, [g]↦α′(g). It is well-defined because α′(I)⊂M and M²=0, and it vanishes exactly when the boundary lifts over that prescribed polar lift. For a small extension this factors through I/mI. The residual coordinate values satisfy all the relations among the generators, so they are not asserted to be independent obstruction coordinates.

This is an exact finite Artin obstruction procedure and a criterion, not a calculation of the residuals for an actual physical/source instance. It does not prove I=0, flatness, reducedness, or any actual obstruction value.
