# 10. The midpoint operator residue and its remaining global value

## 10.1 The actual third value has a global boundary description

The positive obstruction is now reduced to a specified global operator residue. This goes beyond classifying the lower Atiyah factor in [Section 9](09-actual-atiyah-factor.md), but does not yet evaluate the residue or decide the four-or-five alternative.

Work on the smooth weighted cone stack X, with physical hyperplane line O_X(1), the actual rank-two Serre bundle G, regular section σ, and det G = O_X(2). Write Γ = SL₂(F₅) for the equivariance group, distinguishing it from the bundle G. Let Z be its zero scheme and put

    M = ω_(2Z)(1),       2Z = V(I_Z²).

The ordinary square thickening 2Z of the Serre ideal is not the ambient double quadric 2Q₀. Write B_Q₀ for the adjoint bundle, pulled back to X when used in a stack sequence. With N = σσᵗJ and τ(v) = σvᵗJ + vσᵗJ, the identities are [K,N] = τ(Kσ) and τ(σ) = 2N.

Zero normal variation of the fixed actual probe permits computation at the midpoint first-normal bundle of [Section 8.9](08-finite-normal-extension-tower.md#89-the-midpoint-has-a-square-zero-adjoint-but-cannot-extend-to-q₃), with its actual square-zero lift Ñ. Retain the fixed nonzero scalar k in ζₐ = k At_F(Dₐ). The corrected cone operator O has twist four and symbol k a h Dₐ; the specified operator aO has twist six and symbol k a²h Dₐ. Its obstruction to lifting to the midpoint is the unquotiented secondary value Ψ(a,h,t(a)), where t(a) = [aζₐ].

The [actual operator comparison][OP] constructs a global positive section r(a,h) of M(4) = ω_(2Z)(5) and gives

    δ : H⁰(M(4))₊ → H¹(B_Q₀(4))₊ = P4,
    Ψ(a,h,t(a)) = δ(r(a,h)),
    ker δ = im[H⁰(G(4))₊ → H⁰(M(4))₊].

The equality uses one fixed Čech boundary sign. It is not a choice of a new probe. The two exact sequences defining δ are

    0 → O_X(2) → B_Q₀(4) → J₄ → 0,
    0 → J₄ → G(4) → M(4) → 0.

The centralizer has no H¹ or H² in this twist, so it contributes no omitted gluing obstruction. Locally the error of an operator lift on Ñ, after subtracting its lifted scalar eigenvalue and dividing by q₀, is tangent. Differences of these errors are commutators. Their classes therefore glue to r, and their boundary is the actual operator-lifting cocycle. Changing the global scalar lift changes r by the image of a global multiple of σ/2 and leaves δ(r) unchanged. The eventual third Bockstein is obtained only after a further quotient by the actual second-symbol image.

## 10.2 Invariant negative-defect acyclicity

The [first-normal defect theorem][AC] proves

    H⁰(M(-2))^Γ = H¹(M(-2))^Γ = 0,
    M(-2) = ω_(2Z)(-1).

Proper duality equivalently gives H⁰(O_(2Z)(1))^Γ = H¹(O_(2Z)(1))^Γ = 0. The key actual-map input is the nonzero midpoint bracket: evaluation identifies the invariant H¹ line of the gauge image with the invariant H¹ line of G(-2). Equal dimensions alone would not prove this identification. The cone input H²(B_Q₀(-2))^Γ is zero; it must not be replaced by the obstruction line at twist minus four.

For a genuine cocycle in this defect sheaf, acyclicity supplies an invariant correction, unique modulo the usual changes of local representatives. It does not make every local discrepancy a commutator or imply vanishing in the different positive twist M(4).

## 10.3 The corrected Hessian symbol matches the actual midpoint

The [full-frame comparison][HF] now closes the actual-symbol identification needed in Section 10.1. In homogeneous vertex Serre frames write σ = (f,g), with binary degrees three and five, and q₀ = νq, q = xz − y². The Hessian correction relative to the actual equation is divided by the unit ν. Determinant frames, diagonal generator changes and inverse GL₂ coordinate substitutions are compared with this unit retained.

A triangular change g ↦ g + pf, with p quadratic, can leave a tangent residue. For the specified Euler-gradient harmonic convention, that residue is

    −q₀ mix(H_f,H_p) S₁′/(16ν),
    S₁′ = [[f,0],[2g′,−f]].

Its coefficient lies in W′ O_L(-5). Both invariant H⁰ and invariant H¹ of that coefficient bundle vanish, so there is a unique invariant cochain primitive. The required q₀uᵢS₁,ᵢ terms must be added. The proof also normalizes the actual Serre residue on the entire nonreduced scheme, makes the determinant transitions exactly compatible, and checks all determinant-one stabilizers of the regular pair. Such stabilizers have the form I + tN and have zero residue in the full commutator quotient.

After these corrections, comparison with the actual Ñ defines a global invariant section of M(-2). Section 10.2 makes it zero. Thus the corrected Hessian system represents the actual midpoint nilpotent symbol modulo local normal conjugation on the vertex neighborhood. This does not identify the bare Hessian formula with Ñ, extend the spinor line to 2Q₀, or establish flatness of its kernel.

## 10.4 Harmonic constants and the local operator formula

Let L be the canonical harmonic lift for Δ = ∂ₓ∂z − ¼∂ᵧ². For even binary forms p,r of degrees 2m,2n, ambient multiplication has the exact first-normal correction

    L(p)L(r) = L(pr) + q L(B(p,r)) mod q²,
    B(p,r) = (p,r)₂/[2(2m−1)(2n−1)(2m+2n−1)].

Here (p,r)₂ is the unnormalized second transvectant. This is the actual ambient product in this splitting, not an arbitrary deformation of the cone algebra. [Product and operator calculation][HP].

For n = [[fg,−f²],[g²,−fg]], conversion from the Euler-Gram lift gives

    T_can = [[mix(H_f,H_g)/112, −det(H_f)/20],
             [det(H_g)/144, −mix(H_f,H_g)/112]],
    (L(n) + q L(T_can))² = 0 mod q².

The [universal constants][HC] are therefore 1/112, −1/20 and 1/144 in the canonical harmonic splitting. Relative to q₀ the correction is T_can/ν, and the unique quintic-generator primitive from Section 10.3 is still required.

The local diagonal formula explicitly retains the ambient product B, the actual corrected nilpotent term t, the cone connection A and the scalar lift. If Dq = ρq, H is the local coefficient of the specified symbol, and Λ includes the physical-line action, its degree-eight residue is represented by

    B(H,D(fg)) + B(A₁₂,g²) + B(A₂₁,f²) − B(Λ,fg)
      + H D(t₁₁) + (Hρ−Λ)t₁₁ + A₁₂t₂₁ − A₂₁t₁₂
      − Λ₁fg                                      mod (f²,g²).

The arbitrary normal operator-connection correction disappears in this quotient because its diagonal commutator is a multiple of f² or g². The actual symbol correction t and scalar term do not disappear. Even though the global twisted symbol annihilates q₀, a local equation frame can have ρ ≠ 0. A nonzero chart expression alone is not a nonzero global boundary.

## 10.5 The conic contributes zero to the boundary

The [support reduction][VC] proves that δ vanishes on the conic-supported summand of H⁰(M(4))₊. The positive part there is O_C(8), as follows from the full nonreduced filtration

    0 → O_Z → M → G|_Z → 0,

with first arrow given by the class of N. Every conic octic is the restriction of a pure-positive ambient quartic ρ. Its degree-eight vertex restriction vanishes on the entire actual (3,5) complete intersection, whose socle degree is six. Thus the global section ρσ/2 supplies the prescribed conic class and zero vertex component.

Consequently Ψ = δ(r_v), where r_v is the actual corrected vertex defect. It vanishes exactly when r_v is the vertex restriction of a global positive section of G(4); an unwanted conic part of such an image can be removed independently. The remaining computation is a global quotient, not merely a fiberwise residue test.

## 10.6 The exact degree-eight quotient and double-cubic bundle

On the negative projection line L = P(W), let M₈ be the cover-degree-eight piece of the actual vertex defect M(4). The exact global boundary on this piece is

    0 → H⁰(E₈) → H⁰(M₈) → P4 → 0,
         dimension 32    dimension 36    dimension 4.

The tangent coefficient and gauge bundles fit into

    0 → T6 O_L(-1) → E₈ → S4 O_L(7) → 0,
    0 → V O_L(-4) → J₈ → O_L(4) → 0,
    0 → J₈ → E₈ → M₈ → 0.

The actual gauge extension is twice the nonsplit quintic-generator class. Its boundary on sections is the nonzero D5 inclusion into P4⊕D5, not merely a permitted representation channel. The actual square-ideal map identifies J₈ with P4 O_L(-2). Consequently H⁰(J₈)=0, H¹(J₈)=P4, and H¹(E₈)=0.

The identification with the global operator boundary is through the actual wedge map and square-ideal boundary diagram. Intrinsically, E₈ is the fiber product of M₈ and Sym⁸(W′) O_L(2) over the degree-eight square-algebra quotient Q4(6). The quotient's 27-dimensional polynomial image and the five-dimensional scalar kernel give the 32-dimensional boundary kernel. Exactness supplies global G(4) representatives for these kernel classes; it does not assert that every specified polynomial tangent representative extends globally. [Exact operator quotient][DQ].

There is also an actual equivariant bundle description

    M₈ = π_* O_(2D)(-2,12) = A O_L(6) ⊕ V O_L(4),

where D=(f=0) has bidegree (3,3) in P(W′)×L and π projects to L. Here 2D is the double cubic divisor in that surface, distinct from both 2Z and 2Q₀. For a local diagonal residue r, the expression r/g² glues on 2D: under g′=g+pf, the actual change of r cancels that of g² modulo f². This retains the nonsplit generator transition rather than choosing a split quintic.

Pushing forward the double-divisor sequence gives

    0 → M₈ → Sym⁶(W′) O_L(6) → O_L(12) → 0.

The actual invariant f² lies in the unique common P4 channel of Sym⁶(W′)=A⊕P4 and Sym⁶(W)=V⊕P4. The established sextic evaluation sequence therefore identifies the kernel with the displayed split bundle. It has rank six, degree thirty and 36 sections, with character A⊕2V⊕3P4⊕3D5. Relative finite duality independently checks the same line factors. [Double-cubic description][DC].

These results identify the actual global quotient and its domain. The full corrected operator residue must still be inserted into it. A nonzero section can lie in the 32-dimensional kernel, and the eventual third Bockstein requires the additional quotient by the actual second-symbol image. No value of Ψ follows from these dimensions or splittings.

## 10.7 Both split square-boundary channels are nonzero

The scalar class of N gives the actual sequence

    0 → O_L(4) → M₈ → Q4(6) → 0.

Its injection has zero V O_L(4) component and is the nonzero dual complete-quadratic evaluation in A O_L(6). Thus

    Q4(6) = W O_L(7) ⊕ V O_L(4),
    h⁰(Q4(6)) = 16 + 15 = 31.

The [square-boundary theorem][BC] proves that the actual map H⁰(Q4(6)) → P4 is nonzero on each summand, hence onto P4 on each. For either positive-degree summand, an identically zero section boundary would split its pullback of the square-ideal sequence. Such a splitting would give a map from O(7) or O(4) into the polynomial bundle Sym⁸(W′) O(2), which is impossible by degree. Serre duality makes the extension-to-section-boundary test faithful; no actual matrix evaluation is used.

On V O(4), the boundary is the unique P4 projection in V⊗D5 = A⊕V⊕P4⊕D5, up to a nonzero scalar. The other section module is V⊕2P4⊕D5; nonvanishing does not determine the ratio of its two P4 channels. The two components of a particular operator residue can still cancel. Neither separate surjectivity nor the explicit splitting evaluates Ψ.

The actual cubic support, its intrinsic 9/36/27 section filtration and another nonzero boundary channel are developed in [Section 11](11-cubic-support-and-nilpotent-torsion.md).

## 10.8 The whole lower multiplication has uniform rank four

The negative eigenspace C⁻ of the Serre involution in the physical-positive thirty-space C from Section 9 has the actual identification

    C⁻ = ε H⁰(Q4(4)),      Q4(4) = W O_L(5) ⊕ V O_L(2).

Here ε is the additional Serre-marking character of weight −1, not physical inversion or the intrinsic coordinate linearization. The twenty-four sections of M₈(-2) map to C⁻ with exactly the three scalar sections of O_L(2) as kernel. The proof uses the actual global boundary and its finite action, not a guessed extension of polynomial representatives. [Negative-sector theorem][NS].

Naturality of the actual wedge and trace diagram then identifies multiplication by a negative quadratic a with

    H⁰(Q4(4)) → H¹(P4 O_L(-4)) → H¹(P4 O_L(-2)) = P4,
                       second arrow: cup product with a.

The square-ideal sequence gives the exact section quotient

    0 → Sym⁸(W′) → H⁰(Q4(4)) → P4 ⊗ H¹(O_L(-4)) → 0,
             9          21                    12.

Serre duality pairs H¹(O_L(-4)) perfectly with the negative quadratics A = H⁰(O_L(2)). Thus the actual map C → P4 has **rank four for every nonzero a**, not only generically or on square directions. The intersection of its kernels on C⁻ is the canonical nine-space Sym⁸(W′)=P4⊕D5. Including the annihilated positive Serre eigenspace C⁺ gives an eighteen-dimensional common kernel on C; each individual map instead has kernel dimension twenty-six.

This determines the whole lower multiplication. The corrected operator's defect has the form r=a r₁ with r₁ in M(2), and its particular degree-eight class must still be fed into this quotient, then reduced modulo the actual second-symbol image. Uniform surjectivity does not determine that input or its output Ψ.

## 10.9 A complementary global restriction and canonical last-jet route

Mr. Slop's [PR648][BD] proves that the operator boundary kills the entire scalar-rescaling space H⁰(O_Z(4))₊, not just its conic contribution. Global quartic rescalings represent every scalar class. The boundary therefore descends to the actual restriction quotient

    d: V_sec = H⁰(G|_Z(4))₊ → P4,
    ker d = K = im[H⁰(G(4))₊ → V_sec].

The source is vertex-supported, with character A⊕2V⊕4P4⊕2D5 and dimension thirty-five; K has dimension thirty-one and character A⊕2V⊕3P4⊕2D5. This removes the twenty-nine-dimensional scalar layer from the full 64/60 defect quotient. These are different spaces from the degree-eight 36/32 quotient in Section 10.6. The Koszul evaluation sequence independently identifies the same actual map, and duality identifies its transpose with the actual ordinary-square cohomology map. No arbitrary P4-coordinate projection is selected by characters alone.

[PR649][LJ] supplies the canonical choice geometrically. Let J be the ideal of the stack vertex line, not its coarse ideal. The deepest quintic odd Loewy layer gives

    T_last = H⁰(J⁴(G|_Z(4)))₊ = H⁰(W′ O_L(1)) = P4,
    V_sec = K ⊕ T_last,      d|_(T_last) an isomorphism.

Uniform cohomological lifting through transverse degree three makes K map isomorphically to the thirty-one-dimensional lower-jet quotient. Consequently a given v has a unique global-restriction image k with the same lower jets, and d(v)=(d|_(T_last))(v−k). A global section lifting k need not be unique; its restriction is. This canonical projection is not an arbitrary splitting into irreducibles, nor does it automatically kill a chosen homogeneous middle P4 component.

This is a complementary actual-global route to the residue calculation, alongside Section 10.6 and the nilpotent boundary in Section 11.3. PR650 now identifies these actual maps through the corrected first-normal quintic extractor, after subtracting a reduced kernel lift; see [Section 11.4](11-cubic-support-and-nilpotent-torsion.md#114-corrected-first-normal-extraction-equals-the-last-vertex-jet). The actual operator's highest-jet remainder v−k is still uncomputed. Neither the 35/31 quotient nor its canonical P4 slice is an additional nonzero value of Ψ.

## 10.10 Separate pair rigidity and the classical equation complex

Mr. Slop's [PR646 comparison][PAIR] at its stated immutable head gives an explicit marked-pair formulation. In degrees zero and one, the complex

    C_pair = [B(-2) → G*],       T ↦ Tσ,

is invariantly acyclic. Its actual Čech equations imply that any two existing equivariant first-normal tracefree square-zero adjoint pairs with the same central marking and determinant extension have a unique determinant-preserving marked isomorphism. This compares existing solutions; it does not construct arbitrary local data or permit a change of a prescribed underlying bundle without saying so. Its underlying midpoint uniqueness was already implicit in the earlier bracket theorem. The invariant H¹ of G* and of the gauge-image sheaf are both nonzero lines. Their cancellation occurs in the two-term complex; it does not erase the obstruction to gluing on a prescribed bundle.

PR646 also identifies the precise residual term of the classical linearized equation complex

    F_eq = [B(-2) → B → O_X(2)],
    C_pair → F_eq → O_(2Z)(2)[−2] → C_pair[1].

[PR647][EQ] then proves Hⁱ(O_(2Z)(2))^Γ = 0 for every i using the actual nonreduced filtration. The positive vertex layers are O_L(2), D5 O_L and V₈(2), with

    0 → P4 O_L(-6) → (P4⊕D5) O_L(-2) → V₈(2) → 0.

The invariant H¹ groups of both left terms vanish: the first has representation P4⊗D5 and the second P4⊕D5, with no trivial constituent. The other positive layers and the conic line of ordinary degree four likewise have no invariant cohomology; negative-parity layers have none by the central action. Exactness of invariants preserves this conclusion through the nonreduced filtration without splitting it or evaluating an actual matrix. It follows that F_eq is invariantly acyclic in every degree. Its nonzero local cokernel sheaf has not vanished; neither complex is asserted to be the full derived deformation theory with all higher syzygies. No higher-normal existence follows, and the midpoint obstruction to 3Q₀ remains.

These contributions concern invariant groups at negative and twist-two degrees. They do not kill the positive P4 operator target in Section 10.1. PR645 independently overlaps the negative-defect acyclicity of Section 10.2 and is not counted as an additional advance here.

## 10.11 Remaining value and evidence boundary

The actual operator-boundary comparison, corrected symbol matching, harmonic multiplication, zero conic boundary, exact 32-to-36-to-P4 quotient, its nonzero split boundary channels, uniform lower rank four, and the complementary canonical last-jet quotient are established at the source pins below. [Section 12](12-harmonic-cochain-and-family-gate.md) now gives the explicit leading actual cochain, its a² upper factor, and exact family coefficient reductions. It retains the diagonal and frame corrections and does not evaluate their combined class. The absolute value δ(r_v), and then its class modulo the actual second symbol, remain uncomputed. The numerical results remain generic SF ≥ 3, positive-square rank ≥ 27, and total section count four or five. The original repair and algebraicity questions remain open.

The sources provide authored geometric proofs and supplementary universal verifiers, not proof-assistant certificates. The verifiers test identities, characters and degree bookkeeping; no selected actual HM coefficients or actual-instance rank tests are used. The separate adjacent Gauss exclusions and cubic-pairing bound are recorded in [Section 4.13](04-positive-sector.md#413-further-rank-three-gauss-configurations-and-pairings-are-excluded).

## Pinned source references

[OP]: https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md
[AC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/FIRST-NORMAL-ADJOINT-DEFECT-IS-INVARIANT-ACYCLIC.md
[HF]: https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/MIDPOINT-HESSIAN-SYMBOL-MATCHING-BY-FULL-FRAME-COVARIANCE.md
[HP]: https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/UNIVERSAL-FIRST-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-RESIDUE.md
[HC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/UNIVERSAL-HARMONIC-HESSIAN-NILPOTENT-CONSTANTS.md
[VC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/8c26de8e5e68fd41945373ac1f6ee280f109d716/research/hm/order-four-quadratic-load/POSITIVE-MIDPOINT-OPERATOR-BOUNDARY-IS-VERTEX-ONLY.md
[PAIR]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9945accf7172732a6fe1754c95187e97ce6f2845/research/hm/tangent-complex-comparison/PROOF.md
[EQ]: https://github.com/Akilleez-QA/read-em-and-weep/blob/19982af9a6356cbf99d5d7e5307f31f9ac4d0af9/research/hm/residual-equation-cohomology/PROOF.md

[DQ]: https://github.com/Akilleez-QA/read-em-and-weep/blob/14fc90d90f74998c10ea9f2b45cf5b8aeac96bae/research/hm/order-four-quadratic-load/ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md
[DC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/14fc90d90f74998c10ea9f2b45cf5b8aeac96bae/research/hm/order-four-quadratic-load/ACTUAL-DEGREE-EIGHT-DEFECT-AS-DOUBLE-CUBIC-PUSHFORWARD.md
[BC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/14fc90d90f74998c10ea9f2b45cf5b8aeac96bae/research/hm/order-four-quadratic-load/ACTUAL-SQUARE-QUOTIENT-SPLITTING-AND-BOTH-BOUNDARY-CHANNELS.md

[NS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/ACTUAL-NEGATIVE-INVOLUTION-SECTOR-AS-SQUARE-QUOTIENT.md
[BD]: https://github.com/Akilleez-QA/read-em-and-weep/blob/83eb365e87fe3aef3488aa339b73636fa845f630/research/hm/positive-boundary-duality/PROOF.md
[LJ]: https://github.com/Akilleez-QA/read-em-and-weep/blob/d46dafc564e1ba97b0813491d16c32bd2e73e12f/research/hm/positive-restriction-channel/PROOF.md
