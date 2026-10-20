# Universal Čech transgression and multiplication primitives

## Result and boundary

In the audited linear resolution, with the conventions below,

    d₅(φ) = Fφ := T₀T₁T₂T₃T₄φ.

There is an explicit regular total-degree-one Čech cochain hφ of twist −2 with δhφ=Fφ. For every l there is an explicit regular total-degree-zero cochain b_lφ of twist −1 such that

    v_l hφ − H_lφ = δb_lφ,
    H_lφ := (−1)^l T₀⋯T̂_l⋯T₄φ.

In particular this is an actual homotopy identity, with no unidentified residual U₁ class. It gives the constant representative

    m₀₁₁(v_lD_k,D_i,D_j)
      = [D_k H_lφ_ij + H_lφ_ki D_j],
    φ_ab := (d₅)⁻¹(D_aD_b),

in the quotient by the derivative-wedge relations. This is a universal symbolic formula. No φ_ab is evaluated and no Massey value, nonvanishing, or image rank is computed.

## 1. Inputs, grading, and signs

We use the resolution and the already audited theorems in the derivative transgression relations manuscript (PROOF.md) and the definition of m₀₁₁ in the weight two massey manuscript (PROOF.md). Write K^t=C_t⊗O(t), −1≤t≤2, and d=Σ_i v_iD_i. All coefficient maps in this note stay abstract. The maps D_i have internal degree 1 and twist −1, anticommute, and square to zero. For homogeneous f put

    T_i f = D_i f − (−1)^deg(f) fD_i.

The T_i have internal degree 1 and anticommute, with T_i²=0. This follows directly from the graded commutator identity and D_iD_j+D_jD_i=0. Let φ∈Hom(C₂,C₋₁), internal degree −3. Fix the source generator 1/(v₀v₁v₂v₃v₄) of H⁴(O(−5)).

Use U_i={v_i≠0}, ordered 0<1<2<3<4. Čech cochains are alternating in their indices, with

    (c a)_{i₀…i_{p+1}} = Σ_s (−1)^s a_{i₀…î_s…i_{p+1}}.

On bidegree (r,p), where r is internal degree and p is Čech degree, use

    δ = ∂ + (−1)^r c,        ∂f=df−(−1)^rfd=Σ_i v_iT_i f.

Composition in the total complex uses (−1)^{p r′} times the Alexander–Whitney Čech cup-composition for bidegrees (r,p),(r′,p′). It has the total-degree Leibniz rule. In particular left multiplication by a global internal-degree-one cochain has no extra sign; right multiplication on Čech-degree-p components has the indicated sign. All final displayed constant compositions have Čech degree zero.

The spectral-sequence transgression convention is: complete the chosen source q₄ to h=q₄+q₃+q₂+q₁+q₀ so that δh is a global internal-degree-two cocycle; that cocycle represents d₅. This fixes all transgression signs in this note.

For comparison, the alternative total differential c+(−1)^p∂ is obtained by multiplying bidegree (r,p) by (−1)^(rp); its cup-product sign is (−1)^(r p′). The total-degree-one staircase below is unchanged because p(1−p) is even. The degree-zero homotopy changes on Čech degree p by (−1)^p. The final constant formula and H_l are unchanged.

## 2. Explicit staircase

For p=0,…,4 and an increasing index set I of size p+1, let J={0,…,4}\I in increasing order, m=|J|=4−p, and put

    a(I) = (−1)^(Σ_{j∈J}j + 3m − m(m−1)/2),
    (q_p)_I = a(I) T_Jφ / ∏_{i∈I}v_i,
    T_J = the increasing ordered product of the T_j (T_∅=1).

Its internal degree is −3+m=1−p, so total degree is 1. At twist −2 the line degree is −1−p, exactly the homogeneous degree of its denominator. It is a regular section on U_I. Thus every q_p is a legitimate Čech cochain, rather than a rational global primitive. The construction successively omits one denominator coordinate and applies the corresponding T_i.

For i∈I in position s, the number of members of J smaller than i is i−s. Consequently

    T_i T_J = (−1)^(i−s) T_{J∪{i}},
    a(I\{i}) = (−1)^(p−1+i) a(I).

Terms T_iT_J with i∈J vanish. Comparing the remaining terms denominator by denominator yields

    c q_{p−1} = (−1)^(p−1) ∂q_p,      1≤p≤4.

Thus ∂q_p+(−1)^(2−p)c q_{p−1}=0. The top term is exactly q₄=φ/(v₀⋯v₄). At p=0 the formula simplifies to

    (q₀)_i = (−1)^i T_{[0,4]\{i}}φ/v_i.

Its internal differential is independent of i:

    ∂(q₀)_i = (−1)^i T_i T_{[0,4]\{i}}φ = Fφ.

Define hφ=Σ_{p=0}⁴q_p. The preceding cancellations prove δhφ=Fφ. Since T_iFφ=0, the result is closed also directly. This proves the declared d₅ formula without expanding any D_i or φ.

## 3. Explicit multiplication homotopy; no residual class

For an alternating p-cochain a, p≥1, define insertion of l by

    (s_l a)_{i₀…i_{p−1}} = a_{l,i₀,…,i_{p−1}},

using alternating extension, zero for repeated indices. Initially this is read on U_l∩U_I. In the following application it extends regularly to U_I: each term of v_l q_p with inserted index l has denominator v_l∏_{i∈I}v_i, and its factor v_l cancels. Put

    b_lφ = Σ_{p=1}⁴ (−1)^(1−p) s_l(v_l q_p).

Each summand has internal degree 1−p, Čech degree p−1, total degree zero, and twist −1. Its denominator contains only coordinates indexed by its own Čech intersection. This proves regularity explicitly, including components whose intersection does not contain l.

Here is a direct component verification, avoiding any inference from vanishing cohomology. On positive Čech degrees, cs_l+s_lc=1. On degree zero, s_l c a has components a_i−a_l. Insertion commutes with ∂ on the common intersections. For Čech degree t≥1, the degree-t component of δb_lφ is

    (−1)^(−t) s_l∂(v_l q_{t+1}) + c s_l(v_l q_t)
      = s_l c(v_l q_t) + c s_l(v_l q_t)
      = v_l q_t.

For t=4 the first term is absent and the same equality holds because c q₄=0. For t=0 the only contribution is

    ∂s_l(v_l q₁) = s_l c(v_l q₀)
      = v_l(q₀)_i − v_l(q₀)_l.

But v_l(q₀)_l=H_lφ is the same constant coefficient map on every chart. Thus, as regular total cochains,

    δb_lφ = v_l hφ − H_lφ.

All identities can first be checked on the common localization; their regular extensions agree because the line-bundle summands inject into that localization. Also

    ∂H_lφ = v_lFφ.

This last identity follows either by applying δ once more or by the same anticommutation calculation. The explicit b_l proves exactness of the difference; mere closedness would not have ruled out a nonzero class in H¹(End H(−1)). No such dimension argument is used here.

## 4. Constant formula for the canonical mixed Massey operation

The imported derivative-relations theorem says d₅ is injective and its image is exactly span{D_aD_b:a<b}. Therefore φ_ab is defined uniquely for every ordered pair, with φ_ba=−φ_ab and φ_aa=0. This definition requires no evaluation of the inverse transgression.

Set α=v_lD_k, β=D_i, γ=D_j. These are closed degree-one representatives of weights 0,1,1. A valid defining system is

    h_βγ = hφ_ij,
    h_αβ = H_lφ_ki,

because δhφ_ij=D_iD_j and ∂H_lφ_ki=v_lD_kD_i. The defining-system cocycle is

    α hφ_ij + H_lφ_ki D_j.

Using the exact identity of Section 3 and the total-degree-one Leibniz sign for D_k gives

    α hφ_ij + H_lφ_ki D_j
      = D_k H_lφ_ij + H_lφ_ki D_j − δ(D_k b_lφ_ij).

The surviving representative is a global constant internal-degree-two map of twist −2. Its differential cancels explicitly:

    ∂(D_k H_lφ_ij) = −v_lD_kD_iD_j,
    ∂(H_lφ_ki D_j) = v_lD_kD_iD_j.

By the imported canonical Massey theorem, this represents the well-defined m₀₁₁ on the indicated inputs. By the imported target presentation its class is read in

    Z²_global / span{D_aD_b:a<b}.

The formula is canonical relative to the fixed coordinate system, resolution, source orientation, and declared signs. The actual cohomology operation is independent of defining-system choices as proved in the imported theorem. Section 5 establishes that these weight-zero classes span U₀. This note does not evaluate the displayed representatives, their quotient classes, or their image.

## 5. Coverage of every weight-zero input

Import the target-projective Kodaira–Spencer injectivity theorem from [the projective target directions manuscript](../foundation-p01/COEFFICIENT-FAMILY.md). That theorem states injectivity of the PGL₅ family after pullback to its fixed X and tensoring by its fixed line bundle N. Naturality of Kodaira–Spencer classes therefore implies injectivity already downstairs: a zero class for the family g*H on P⁴ would pull back, and remain zero after tensoring, contradicting the imported theorem for any nonzero projective tangent direction. This implication does not need injectivity of arbitrary pullback on Ext groups.

For a coordinate tangent B=(B_kl) the varying differential is

    d(v+εBv) = d(v) + ε Σ_{k,l} B_kl v_lD_k.

Thus its downstairs Kodaira–Spencer class is represented, with the fixed deformation convention, by Σ B_kl v_lD_k. Let G be the global degree-zero endomorphism whose restriction to K^t is t·Id. Directly on K^t,

    ∂G = dG−Gd = −d,
    Σ_i v_iD_i = d = −∂G.

Hence scalar B gives the Euler boundary. Conversely the imported projective injectivity proves that any cohomological relation among the 25 classes [v_lD_k] comes from a scalar B. Therefore their span is canonically gl₅/k·Id and has dimension 24. The classical input dim H¹(End H)=24, also recorded as dim U₀ in [the weight two massey manuscript](../foundation-p04/WEIGHT-TWO-TRANSFER.md), shows that this span is all U₀.

Consequently Section 4 determines m₀₁₁ on every input by trilinearity. More explicitly, for

    a = Σ_{k,l} B_kl[v_lD_k],
    b = Σ_i x_i[D_i],    c = Σ_j y_j[D_j],

one has the universal quotient formula

    m₀₁₁(a,b,c)
      = [Σ_{k,l,i,j} B_kl x_i y_j
           (D_k H_lφ_ij + H_lφ_ki D_j)].

The expression is independent in the quotient of the scalar ambiguity in B, since Section 4 identifies it with the canonical cohomology operation and the scalar direction is a boundary. No extra relation beyond that boundary is assumed. This establishes coverage of all inputs, not a computation of any output or of the operation's image.

