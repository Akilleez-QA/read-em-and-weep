# Canonical positive-linear factorization and the actual middle representation

## Result and scope

For any finite-dimensional equivariant symmetric aggregate q:Sym²(T)⊗X→Y, its canonical minimal positive middle representation is the image M(q) of the curried map T⊗X→T*⊗Y. A prescribed G-representation P supports a two-step positive-linear factorization of q if and only if M(q) embeds in P. This is a character-containment criterion in characteristic zero, not merely a total-dimension bound.

Applied to PR927's three formal maps, the actual positive coordinate space is T=V, and all three minimal middle modules are V⊗Π=1+A+V+P₄+2D. The authenticated actual middle K₄⁺ has character 1+4A+2V+3P₄+3D, so each formal map factors through this very prescribed middle representation. Its unused complement has character 3A+V+2P₄+D. Thus positive-linear factorization through the correct actual middle character, together with positive-positive commutativity, does not decide PR927's scalar versus C² alternatives.

These are formal choices of two positive arrows on the prescribed representation spaces, not the actual multiplication arrows. The other actual parity maps, their negative-variable kernels, mixed squares, lower-degree generation and Euler relation are not replaced or asserted satisfied. No full-window or actual-HM realization follows.

## 1. Immutable input interface

All paths refer to Akilleez-QA/read-em-and-weep. The manifest records exact original Git blobs.

1. PR927, commit 38235cda736a554ca2c16af504a56e1daf756624, research/hm/profile11-source127-cdf-aggregate-sharpness/PROOF.md, blob 4dd68998c565b3a34ac95bc8dfa447144a5c9d60. This fixes the c-d-f negative pencil, N₂=K₃⁺, N₄=K₅⁺, the intrinsic quotient Π≅V+P₄, and the three formal maps with scalar, F-supported C² and B-supported C² compatible algebras. It does not supply positive-linear factors.
2. NEGATIVE-VERTEX-EVALUATION-SCALAR.md in research/hm/order-four-quadratic-load, commit db51525015bb7c5e825833d550d08dedf6f6ea96, blob 4d2737b94c19b84816382984db9ecb91af66ef0e, Section 4. Its actual normalizer conventions identify the coordinate five-space H=V⊕W, with V=Sym²(W′) positive and W negative, and the normalized equivariant HM monad

       N*⊗O(-1) → W′⊗Ω²(2) → N⊗O,
       N=A⊕W′, A=Sym²W.

   All named irreducibles are self-dual. Its companion verify_negative_vertex_scalar.py at the same commit, blob 9eb58f03edde15dd612087440d8180e9e16d1755, supplies the fixed nine-class character convention. We use no actual monad differential.
3. EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md in the same directory and commit, blob c9af11e07dd1c4535d9afee94a3c134607d534a3. It states the actual ambient H⁰B(3)=0 and dimensions H¹B(3)=(46,54). It also retains the actual opposite-parity universal negative map

       0 → A O(-6) → K₃⁻⊗O(-1) → K₄⁺⊗O → C → 0.

   This is a genuine existing map with a rank-three kernel bundle, not a zero map that may be discarded. Its cokernel C may have torsion supported at the twelve exceptional parameters; the kernel bundle remains exact while exceptional fiber sections may fail base change. No torsion-free-cokernel or constant fiber-kernel assertion is used below.
4. SHARPEST-BOUND.md, commit 063da90fc4543304e87e701cdefcc08225412f17, research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md, blob 58785a8799c43fd2c7da089d0ddc5e05822132a9. This proves H²B(t)=0 for t≥2 and records the actual section resolution and primary cohomology vanishings used to check H³B(3)=H⁴B(3)=0 below.

We write P₄ for the four-dimensional irreducible to avoid confusion with a general middle representation P. All arguments are over C and G is finite.

## 2. Canonical factorization theorem

Let q:Sym²(T)⊗X→Y be G-equivariant. Define

    C_q:T⊗X → Hom(T,Y)=T*⊗Y,
    C_q(t⊗x)(s)=q(st⊗x),
    M(q)=im C_q.

The map C_q is equivariant, so M(q) is a genuine subrepresentation. Factor C_q as its surjection a₀:T⊗X→M(q) followed by inclusion into Hom(T,Y). Evaluation gives

    b₀:T⊗M(q)→Y,    b₀(s⊗f)=f(s).

Then b₀(s⊗a₀(t⊗x))=q(st⊗x), which is symmetric in s,t. Thus (a₀,b₀) is a canonical two-step factorization with the required positive-positive commutativity. No choice of a point, basis or coordinate value is involved.

Suppose a:T⊗X→P and b:T⊗P→Y realize q in the same way. Curry b to b̃:P→Hom(T,Y). The identity b̃a=C_q implies that b̃ restricts to an equivariant surjection im a→M(q). Semisimplicity therefore makes M(q) isomorphic to a subrepresentation of im a, hence of P.

Conversely, if an equivariant embedding i:M(q)→P exists, choose an equivariant retraction π:P→M(q). Define a=i a₀ and b=b₀(1⊗π). Their composites give q and are symmetric. This proves the necessary-and-sufficient criterion.

Equivalently, every irreducible multiplicity of M(q) must be at most its multiplicity in P. M(q) is minimal in this representation-order sense and in total dimension. For any factorization, the reachable part im a modulo its unobservable subspace im a∩ker b̃ is canonically isomorphic to M(q). In particular a factorization of total middle dimension dim M(q) has no unused or unobservable middle part and is isomorphic to the canonical one.

This theorem does not say that an arbitrary q has small enough M(q), that character containment recovers the actual factors, or that symmetric two-step composites extend to additional degrees.

## 3. Deriving the actual positive middle character

Let B=End₀(F). The determinant of normalized F is O(-1), equivariantly: any difference from the standard linearization is a character of the perfect group G and hence trivial. Therefore

    B(3)=Sym²(F)(4).

We first justify replacing its Euler character by minus H¹. The actual H⁰B(3)=0 is input 3. Input 4 proves H²B(3)=0. For completeness its tensor-section resolution of End(F)(3) has terms

    E₀=15F⊕4F(1), E₁=35F(-1),
    E₂=20F(-2), E₃=2F(-4)

in homological degrees 0,1,2,3. The same input gives F*=F(1), H¹F(s)=0 for s<0, and H⁰F(s)=0 for s<3. For H³ of the resolved sheaf the only potentially controlling groups are H³E₀ and H⁴E₁. Serre duality makes these sums of H¹F(-4)*, H¹F(-5)* and H⁰F(-3)*, all zero. For H⁴ only H⁴E₀ matters, and its summands are H⁰F(-4)* and H⁰F(-5)*, again zero. Splitting the resolution into short exact sequences proves the required higher vanishings. Trace splitting transfers them to B. Hence

    [K₄]=[H¹B(3)]=-χ_G(Sym²(F)(4)).

Here is a finite, fully symbolic formula for that Euler character. Let t denote the class of O(1), H=V⊕W, L₂=Λ²H, N=A⊕W′ and S_n=SymⁿH. The equivariant Euler sequence gives [Ω²(2)]=L₂-Ht+t². The authenticated monad therefore yields

    [F]=Σ_(i=-1)^2 c_i t^i,
    c_-1=-N,
    c_0=W′L₂-N,
    c_1=-W′H,
    c_2=W′.

For a virtual representation c, let ψ²(c) be its second Adams operation, whose character at g is χ_c(g²). The λ-ring identity Sym²(z)=(z²+ψ²z)/2 is valid for virtual bundle classes in equivariant K-theory. Since ψ²(t)=t², and all line twists below lie between two and eight,

    χ_G(Sym²(F)(4))
      = (1/2) Σ_(i,j=-1)^2 c_i c_j S_(i+j+4)
        +(1/2) Σ_(i=-1)^2 ψ²(c_i) S_(2i+4).       (1)

Every line bundle in (1) is nonnegative, so its Euler characteristic is exactly S_n; duality causes no additional line-character sign. The source conventions are self-dual, so the coordinate space and its dual have the same displayed characters.

Evaluating (1) on the nine fixed abstract conjugacy classes, or using their tensor identities, gives

    K₄=1+4A+2V+3P₄+3D+3W′+3S+6T₆,
    K₄⁺=1+4A+2V+3P₄+3D,
    K₄⁻=3W′+3S+6T₆.                            (2)

The central signs select these eigenspaces. Their dimensions are 46 and 54. The negative character independently agrees with the authenticated N₃ of the negative pencil; it is not used to infer the positive character by dimension alone. Formula (1), not an assumed generic differential rank, gives (2).

The accompanying bounded verifier uses the exact Q(√5) character table and explicit square-class map. It checks all nine class values and integral multiplicities. It evaluates no actual HM tensor, instance, parameter, coefficient, point, or matrix.

## 4. The three formal aggregates admit the prescribed positive middle

By input 2 the actual T₊ is V. Its self-duality and odd dimension give a nondegenerate invariant symmetric bilinear form ε:Sym²V→C: an irreducible invariant bilinear form is nondegenerate and cannot be alternating in dimension three. This is an abstract form, not a chosen value of actual coordinate multiplication.

Retain the same fixed negative pencil and normal-form section i:Π→N₄ as PR927. Its three auxiliary surjections r:N₂→Π are respectively r_F+r_B, r_F and r_B, with the unused source block sent to zero. For each one let

    q(st⊗x)=ε(s,t) i r(x).

The nondegenerate ε induces an isomorphism ε♯:V→V*. Currying gives

    C_q=(ε♯⊗i)∘(1⊗r):V⊗N₂→V*⊗N₄.

Since every r is onto Π, all three minimal middle representations are exactly

    M(q)≅V*⊗Π≅V⊗(V+P₄)
         =1+A+V+P₄+2D,                       (3)

of dimension 21. The identities V⊗V=1+V+D and V⊗P₄=A+P₄+D give (3).

Subtracting (3) from the genuine character (2) leaves

    K₄⁺-M(q)=3A+V+2P₄+D,

a genuine 25-dimensional representation. The theorem in Section 2 therefore supplies equivariant arrows

    a:V⊗N₂→K₄⁺, b:V⊗K₄⁺→N₄

whose symmetric composites are each specified q. Explicitly choose an equivariant embedding j:V⊗Π→K₄⁺ and a retraction π. Set a(t⊗x)=j(t⊗r(x)), and, if π(k)=Σ t_i⊗z_i, set b(s⊗k)=Σ ε(s,t_i)i(z_i). Then b_s a_t(x)=ε(s,t)i r(x), symmetric in s,t.

All fixed negative-pencil data, its negative-square image and kernel, the intrinsic Π, aggregate generation and the projected radical surjections from PR927 remain unchanged. Its exact compatible-algebra calculation consequently still gives the scalar case and both C² idempotent types. The factorization is existential and noncanonical; no choice is made of actual HM positive coefficients.

## 5. The retained mixed-square dependency

Character containment settles only the two positive arrows. To state precisely what it does not settle, put U=K₃⁻, P=K₄⁺ and Z=K₅⁻. In addition to the fixed negative arrows A_w:N₂→N₃ and B_w:N₃→N₄ and the newly formal a_t,b_t, the actual window retains

    c_t:U→N₃, d_t:N₃→Z,
    γ_w:U→P, δ_w:P→Z.

All of these are actual multiplication maps in an actual occurrence. Commutativity requires, for every formal variable t,s∈V and u,w∈W,

    δ_w a_t=d_t A_w,     b_t γ_w=B_w c_t,
    d_t c_s=d_s c_t,     δ_w γ_u=δ_u γ_w.       (4)

The two negative arrows already satisfy B_wA_u=B_uA_w, and Section 4 enforces b_ta_s=b_sa_t. Equations (4) are not supplied by Section 4. In particular the actual γ has the nonzero universal-kernel structure recalled in input 3 and cannot be silently set to zero.

There are elementary additional gates for these equations. Define C:W⊗U→V*⊗N₄ by C(w⊗u)(t)=B_w c_t(u), and D:V⊗N₂→W*⊗Z by D(t⊗x)(w)=d_t A_w(x). Currying γ and δ in the natural way gives γ:W⊗U→P and δ̃:P→W*⊗Z. The two mixed equations imply

    ker γ ⊆ ker C,     im D ⊆ im δ̃.           (5)

These follow from C=b̃γ and D=δ̃a. Neither (5), much less sufficiency for the coupled equations, is claimed for our formal factors. Fixed actual maps and their embeddings remain genuine missing data.

One could create a bare commutative three-degree model by deleting all arrows from U and all arrows into Z, retaining only A,B,a,b. That observation is not a realization preserving the actual window: it discards γ and its known kernel, and if Z≠0 it violates generation into Z. We do not use it as evidence of actual-window compatibility.

## 6. Contribution and remaining boundary

PR927 deliberately stopped before positive-linear factorization. Sections 2–4 resolve that dependency for all three of its formal constructions on the authenticated actual positive middle representation, not a freely enlarged substitute. Therefore this extra factorization condition alone still cannot choose the scalar or C² aggregate branch. The obstruction, if one exists, must use additional marked-map/mixed-square data, actual relation embeddings, or another actual-HM theorem.

No source exclusion, actual occurrence, full-window extension, full-module splitting, coefficient evaluation, or frontier-count change follows. This is an authored universal proof with a bounded fixed-character check, not formal proof-assistant certification.
