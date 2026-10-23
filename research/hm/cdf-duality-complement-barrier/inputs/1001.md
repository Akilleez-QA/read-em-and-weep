# A preserved c-d-f B block forces a nonzero internal first symbol

## Conditional theorem and scope

Assume an actual source127 c-d-f occurrence (stable label G3.11.cce6e3ba4eeb, necessary pair E14,Q148). Retain PR924's simultaneous constant-block coordinates and the same invariant product Q and negative quadratic multiplications T_a as PR935. Suppose only the ONE-SIDED condition

    Q(X_B) ⊂ Y_B.                                      (H)

No complementary preservation is assumed. Then necessarily:

1. ker(Q|X_B)=ker Q=A+D, im(Q|X_B)=V+2P+D, coker(Q|X_B)=D. Thus Q|X_B has rank 16, derived universally, not evaluated on an instance.
2. Y_B ⊂ im Q. On the quotient complex X_F→Y_F⊕Y_L the cohomology is D in degree zero and P in degree one, and its connecting map to coker(Q|X_B)=D is an isomorphism.
3. The internal first symbol of (Q|X_B)+t(T_a|X_B) vanishes on D and is a NONZERO scalar multiple of binary-form multiplication A⊗A→D on A. Consequently it is injective on A for every nonzero formal parameter a and has precisely D as its kernel.
4. The quotient first symbol D→P is a NONZERO scalar multiple of A⊗D→P, the projection of binary multiplication Sym²W⊗Sym⁴W→Sym⁶W=V+P.

These are necessary conditions if (H) holds, not a proof of (H), a source realization, or a source cut. In particular scalar commutant (PR935) does not prohibit a nonsplit preserved subcomplex. The conclusion distinguishes that one-sided possibility from the previously excluded direct-summand/projector branch.

## Inputs

PR939 at 9c43c9b3bb9cb99c809c37a8fe8f8429f4b3a79e supplies the quotient type; its PR920 pinned normal form is copied. PR924 at c6c25eaf0e5a67c27eee7c3ba4f000df55997692, Git blob 83f5aee293995257459229e6b323522224ce8f3d, supplies the simultaneous block negative pencil and actual lift classification. PR935 at a7707ba3e25592023eb69cc15686aa4ee1fdcb7c, research/hm/profile11-source127-cdf-bockstein-rigidity/PROOF.md, Git blob 187fe2a8c1499e11afdb5002091aa3c144e1b4a3, supplies the imported actual kernel/cokernel theorem, global first-Bockstein vanishing, and second-Bockstein nonzero on A and zero on D. These are the same two-term pencil Q+tT_a, not a different normal obstruction. Local exact input hashes are in INPUTS.json. No new actual coefficient is selected.

Write

    X_F=V+P+2D,  X_B=A+V+2P+2D,
    Y_F=P+D,    Y_B=V+2P+2D,    Y_L=V+P.

Every T_a preserves each indicated negative-pencil block. The actual cohomology of Q is K=A+D and C=P. Here A=Sym²W, D=Sym⁴W, and Sym⁶W=V+P.

## Step 1: the whole D kernel must enter B

Under (H), let S=[X_B→Y_B]. Its kernel K_B is a G-submodule of K. The unique A of X lies in X_B, and Q kills it. Therefore K_B is either A or A+D. If K_B=A, character subtraction makes Q|X_B onto Y_B. Since every T_a preserves these spaces, a right inverse of Q|X_B recursively lifts every vector of A to a kernel vector of Q+tT_a in X_B[[t]]. Every Bockstein on A would vanish. This contradicts the imported second nonvanishing. Hence K_B=A+D, proving statement 1 and identifying it with the entire actual K, not an unmarked abstract copy.

The quotient map Y_B→C=P factors through H¹(S)=D, and Hom_G(D,P)=0. Thus its image is zero: Y_B⊂im Q. Let U be the quotient complex [X_F→Y_F⊕Y_L], with Q followed by quotient projection. The long cohomology sequence is

    0→K_B→K→H⁰(U) --δ--> H¹(S)→C→H¹(U)→0.

The first nonzero arrow is an isomorphism and H¹(S)→C is zero, so δ is an isomorphism, H⁰(U)=D, H¹(U)=P. This is an actual connecting map for a short exact sequence of complexes, not a splitting of their differentials.

## Step 2: the two first symbols compose to the actual second

Let α_a:K=A+D→H¹(S)=D be the first symbol inside S, and γ_a:H⁰(U)=D→H¹(U)=P the first symbol inside U. Both are canonical and linear in a. Because the global first symbol vanishes, the original second is defined on all K, with target C=P. Up to the fixed connecting-map sign,

    β₂,a = -γ_a δ⁻¹ α_a.                        (1)

For clarity, choose a splitting of the underlying vector spaces, not complexes. Given k∈K, T_a k is in Y_B. A first correction z with Qz=-T_a k projects to a cycle of U. Its connecting class is -α_a(k), so [z] in H⁰(U) equals -δ⁻¹α_a(k). The second error T_a z projects to γ_a([z]) in H¹(U)=C. This proves (1). Altering corrections by a global Q-cycle changes the second error by the globally zero first symbol, so the formula is independent of all sections. No actual section or matrix is evaluated.

Since β₂ on A is nonzero, α|A and γ are nonzero. The binary identities

    A⊗A = 1+A+D,
    A⊗D = A+D+V+P

give one-dimensional Hom spaces for α|A:A⊗A→D and γ:A⊗D→P. Their representatives are ordinary binary multiplication and multiplication followed by the nonzero P projection, respectively. This proves the nonzero assertions in statements 3 and 4 without selecting their scalar values.

## Step 3: zero second on D forces zero internal first on D

The remaining map α|D:A⊗D→D also has multiplicity one. Its representative is the first transvectant

    τ(a,h)=a_x h_y-a_y h_x,  deg a=2, deg h=4.

Thus (1) restricted to D is a scalar multiple of

    (a,h) ↦ pr_P[a τ(a,h)] ∈ P⊂Sym⁶W.            (2)

The universal polarized map Sym²(Sym²W)⊗Sym⁴W→Sym⁶W given before the P projection is SL₂-equivariant and nonzero. For example its polynomial identity at the synthetic monomials a=x²,h=x³y is 2x⁶, and no HM datum is involved. Its image is therefore the entire irreducible SL₂-module Sym⁶W. Composition with the nonzero projection to P cannot be zero. Since characteristic is zero, diagonal a-values determine the polarized map; equivalently (2) is a nonzero polynomial family.

The actual γ scalar is already nonzero. The actual β₂ on D is identically zero by the imported theorem. Therefore the α|D scalar must be zero. This proves the remaining assertion in statement 3. Multiplication by any nonzero binary form a is injective in C[x,y], so α_a on A is injective at every nonzero parameter. This is a universal polynomial-domain statement, not a sampled rank.

## Projective form

On P(A), the internal first-symbol family has the exact sequence

    0→A O(-1) --multiply by a--> D O→E→0,

while the D part of K contributes the zero map. The quotient E is locally free of rank 2, has c1(E)=3H and c2(E)=6H², and det E=O(3). These follow from the everywhere injective multiplication and c(E)=(1-H)^(-3). They describe the forced internal first-page quotient only; no identification with an actual ambient bundle outside this parameter plane is asserted.

## Verification and stopping boundary

verify.py checks input hashes, McKay character arithmetic, all two kernel possibilities, the exact long-sequence characters, all three multiplicities, the universal transvectant/multiplication polynomial and its polarization, and the Chern identity. It checks universal formulas, not actual HM matrices or ranks. No coefficient values, selected source parameters, points, jets, consumed experiment or local-model spike are used. The remaining barrier is proving or refuting the one-sided invariant preservation (H) by actual geometry. None of these necessary conditions contradicts that preservation.
