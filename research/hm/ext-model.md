# A finite exact Ext model for a Horrocks–Mumford pullback

## Statement

Let C be the elliptic curve y²=x³−x, let X=C⁴, and let N be the exterior product of the four degree-one origin line bundles. Write
q:X→Y=(P¹)⁴
for the product of the x maps and
ρ:Y→Sym⁴(P¹)=P⁴
for the symmetric quotient, using coordinates v_k=e_k(x₁,x₂,x₃,x₄), 0≤k≤4, on the finite chart. Let f=ρq. For the normalized Horrocks–Mumford bundle H, put E=f*H⊗N.

The calculation below gives
dim Ext^j_X(E,E)=(1,87,7372,87,1),  j=0,…,4.

For a deck character indexed by a subset S⊂{1,2,3,4}, its dimensions depend only on |S|:

| Weight | Ext⁰ | Ext¹ | Ext² | Ext³ | Ext⁴ |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 79 | 352 | 0 | 0 |
| 1 | 0 | 2 | 448 | 0 | 0 |
| 2 | 0 | 0 | 514 | 0 | 0 |
| 3 | 0 | 0 | 448 | 2 | 0 |
| 4 | 0 | 0 | 352 | 79 | 1 |

Each row describes one character; multiplicities are 1,4,6,4,1. The trace-free dimensions are (0,83,7366,83,0).

The dependency-free companion program `verify-hm-ext.js` reconstructs the matrices, performs exact elimination, checks kernels and expected outputs, and prints its results. The following derivation specifies what it computes. No claim about a second-order deformation obstruction follows merely from these dimensions.

## 1. An explicit four-term line-bundle complex

Let V have basis e₀,…,e₄ and volume vol(e₀,…,e₄)=1. Indices are cyclic modulo 5. Define

w_i⁺=e_{i+2}∧e_{i+3},   w_i⁻=e_{i+1}∧e_{i+4}.

These ten oriented bivectors form a basis of Λ²V. Let B=(Λ²V*)² and define the surjective constant map

b(η⁺,η⁻)_i=η⁺(w_i⁻)−η⁻(w_i⁺).

Its kernel W has dimension 15, with basis

U_i=(dual(w_i⁺),0),
V_i=(0,dual(w_i⁻)),
Z_i=(dual(w_i⁻),dual(w_i⁺)).

For v∈V, write
φ_v(w)(u₁,u₂)=vol(v,w,u₁,u₂).

The Euler coresolution identifies Λ²Q(−1)=Ω²(2) with the kernel of
ι_v:Λ²V*⊗O→V*⊗O(1).
Define
γ_i(v)=(φ_v(w_i⁺),φ_v(w_i⁻))∈W.

The complex

L⁻¹=5O(−1) → L⁰=W⊗O → L¹=(V*)²⊗O(1) → L²=C²⊗O(2)

has maps γ, paired contraction ι_v, and paired evaluation at v. Its only cohomology is H in degree zero. Indeed, insert the Euler coresolution into the HM monad and cancel the constant surjection B→5O. The identities bγ=0, ι_vγ=0 and ι_vι_v=0 make this an actual complex. The program checks the two remaining consecutive compositions as polynomial identities.

After pulling back to X and tensoring N, this becomes

5N⁻¹ → 15N → 10N³ → 2N⁵.

Put K=ρ*L on Y. Its strict endomorphism DG algebra has

End(K)^r=O(r,r,r,r)^{m_r},

where
m₀=354,  m_{±1}=245,  m_{±2}=80,  m_{±3}=10.

The differential is the graded commutator [d,−], and multiplication is matrix composition.

## 2. Deck characters and a strict product-aware model

The finite flat double-cover algebra is

D=q_*O_X=⊕_S O(−2S).

On the finite chart, write y_S=∏_{i∈S}y_i. Its multiplication is

y_S y_T=(∏_{i∈S∩T}(x_i³−x_i)) y_{S△T}.

Thus derived global sections of the strict sheaf DG algebra End(K)⊗D compute RHom_X(E,E). Tensoring the original object by N does not change this endomorphism algebra.

Use the tensor product of the two-chart Čech complexes in each P¹ factor. Alexander–Whitney cup product, branch-algebra multiplication, matrix composition and the usual totalization signs give a strict DG product on this bounded Čech model. The number of charts and complex degrees is finite, although its Laurent-polynomial cochain spaces are not finite-dimensional.

## 3. A finite-dimensional contraction

For O(n) on P¹, express both chart components in the finite-chart frame:

C⁰=C[x]⊕xⁿC[x⁻¹],   C¹=C[x,x⁻¹],   d(a,b)=b−a.

Call the first degree-zero component A, the second B, and the degree-one component C.

H⁰ has monomial basis x^e for 0≤e≤n. Its inclusion is x^e↦(x^e,x^e), and its projection selects the nonnegative part of B.

H¹ has monomial basis x^e for n<e<0. Inclusion uses the Laurent representative, and projection keeps these exponents.

A contracting homotopy on C¹ is

h(x^e)=
- (−x^e,0) if e≥0;
- (0,x^e) if e<0 and e≤n;
- 0 otherwise.

It satisfies dh+hd=id−ip. Tensor the contractions in the order

H=Σ_j (ip)₁⊗⋯⊗(ip)_{j−1}⊗h_j⊗id_{j+1}⊗⋯⊗id₄,

with Koszul signs from preceding Čech degrees.

For internal degree r and Čech degree p, let Δ=(−1)^p[d,−]. The exact finite transferred differential is

D_fin=pΔ(Σ_{j=0}⁴(−HΔ)^j)i.

The sum terminates because H lowers Čech degree. This formula retains all higher hypercohomology differentials. Keeping only pΔi is not sufficient.

The underlying finite space has dimension 80,384. Its dimensions in total degrees 0,…,4 are

354, 18,296, 43,084, 18,296, 354.

These are dimensions of the model, not the cohomology.

Corrected inclusion and projection from the same perturbation lemma transfer the Čech product. In particular, m₂(x,y)=Pμ(Ix,Iy), with higher tree operations providing an A∞ model. This preserves the Yoneda product; the finite vector space is not asserted to be a strict DG algebra. The certificate computes its differential ranks, not its product table.

## 4. Exact rank certificates

The program uses coefficient matrices for γ, contraction and evaluation, substituting v_k=e_k(x). The elementary symmetric polynomials are represented as sums of squarefree monomials. Čech homotopies and harmonic projections are exponent tests.

For characters of weights 2,3,4, degree one has only the r=−3,p=4 source. The nonzero transferred components needed to test its kernel have lengths 1,3 and 5:

| Weight | Initial map | Rank | Length-three map on preceding kernel | Rank | Length-five map on preceding kernel | Rank |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 720×640 | 450 | 354×190 | 100 | 720×90 | 90 |
| 3 | 2160×1280 | 1250 | absent | — | 240×30 | 30 |
| 4 | 6480×2560 | 2550 | absent | — | 80×10 | 10 |

Matrices are written as rows×columns. These calculations prove Ext¹ vanishes in every character of weights 2,3,4.

For weight one, the initial 240×320 matrix has rank 150. Combine its 170-dimensional kernel with 354 diagonal H¹ terms. The resulting 2160×524 matrix, combining the length-five and length-two components, has rank 522. There are no degree-zero boundaries in this character, so Ext¹ has dimension 2.

For weight zero, the initial 80×160 matrix has rank 50. Combine its 110-dimensional kernel with 3920 ordinary degree-one terms. The resulting 6480×4030 matrix has rank 3598, leaving 432 cycles. The 3920×354 degree-zero boundary matrix has rank 353. Therefore Ext⁰ has dimension 1 and Ext¹ has dimension 432−353=79.

All displayed ranks are characteristic-zero ranks. Sparse integer elimination uses unit pivots where possible and verifies zero residual rows. The weight-one final matrix requires a fraction-free BigInt tail after 497 unit pivots; that tail contributes 25 further pivots. The largest integer intermediate in the remaining unit-pivot calculations is 98. The program checks that Number arithmetic remains exact and verifies the constructed kernels. It also verifies that the trivial-character boundary lands in the computed cycle space.

## 5. Recovering the remaining degrees

On Y, let h=h₁+⋯+h₄. Then

ch(End H)=4−15h²+(75/4)h⁴.

With s_i=−1 for i∈S and +1 otherwise, Riemann–Roch gives

χ_S=450−30e₂(s₁,s₂,s₃,s₄)+4∏s_i.

This is 274,446,514,446,274 in weights 0,1,2,3,4, respectively.

The canonical volume form on X has full-sign deck character. Hence Serre duality pairs character S with its complement. Combining the Ext⁰ and Ext¹ calculations, duality and the character Euler characteristics gives the table above.

The scalar summand H*(O_X) has one dimension in degree |S| for each character S. Removing it gives the trace-free dimensions.

## 6. What this does and does not imply for deformations

Every Ext¹ class has deck weight zero or one. Composition multiplies characters by symmetric difference. Consequently every Yoneda square of an Ext¹ class has zero full-sign component. This conclusion does not require a description of a deformation family.

The result does not evaluate a baseline second-order obstruction, and it does not prove all Yoneda squares vanish. Those are separate questions.

For later bidifferential calculations, the canonical vector field on a finite elliptic chart satisfies

V(a(x)+b(x)y)=b′(x)(x³−x)+b(x)(3x²−1)/2+a′(x)y.

On the infinity chart t=1/x and u=y/x²,

u²=t−t³,   V(t)=−u,   V(u)=(−1+3t²)/2.

These formulas preserve the double-cover transition and toggle its character. The Čech product and contraction retain the data needed to transfer such local operations. However, entrywise differentiation of line-resolution matrices is not automatically a global chain derivation: line-bundle transitions, derivatives of the differential and the corresponding Atiyah data must be included. A naive Moyal substitution into fixed line terms is not justified by the Ext calculation.
