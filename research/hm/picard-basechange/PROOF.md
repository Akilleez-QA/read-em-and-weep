# Picard obstruction under arbitrary faithful-column base change

Status: authored structural proof; independently mathematically reviewed (PASS); not formally checked. Work over C. No selected actual HM/source-instance evaluation, large computation, higher-order lifting, or algebraicity claim is made.

## 1. Pinned input and precise scope

The inputs are [PR584 at df1e09bb456974ec43ab598709bd60d0378cfedf](https://github.com/Akilleez-QA/read-em-and-weep/blob/df1e09bb456974ec43ab598709bd60d0378cfedf/research/hm/picard-defect-singularity/PROOF.md) and [PR585 at 257777c4451d16201202d18f227ff82d5e30956c](https://github.com/Akilleez-QA/read-em-and-weep/blob/257777c4451d16201202d18f227ff82d5e30956c/research/hm/picard-blowup/PROOF.md). Their geometric input is [PR583 at ce046d10a03a609aee3d0125b3264dd36bb9d598](https://github.com/Akilleez-QA/read-em-and-weep/blob/ce046d10a03a609aee3d0125b3264dd36bb9d598/research/hm/universal-picard/PROOF.md), with its pinned dependencies. We assume the actual normalization/residue identification established there. We do not replace it by a complex guessed from dimensions.

Fix one residual node and write

    A = C[t_z^{±1}: z∈Z],                 P = Spec A,
    δ = (t₂−t₁,t₃−t₁,t₄−t₁,t₅−t₁)ᵀ,    I = (δ₁,δ₂,δ₃,δ₄),
    Z₀ = V(I).

There are thirty ratio parameters; the other twenty-five remain independent units. Put

    R = C[[s,t]]/(st),    Rbar = C[[s]] ⊕ C[[t]],    m = (s,t).

All node rings below are algebraic tensor products, not implicitly completed tensor products. The pinned input gives the actual node complex, in degrees zero and one,

    C_A = [E_A --δβ--> A⁴],
    E_A = {(f,g)∈Rbar⊗C A : f(0)=t₁g(0)},    β(f,g)=g(0),          (1)

and its residue sequence

    0 → m_A → E_A --β--> A → 0.                                  (2)

Here m_A=m⊗C A. Branch scaling identifies E_A with R⊗C A; the inclusion of m_A is still the inherited conductor inclusion, with its specified branch scaling. Also

    0 → A --δ--> A⁴ → K_A → 0.                                   (3)

The overall sign of δ is immaterial; fix the positive convention throughout. Our claims concern this actual node complex and ordinary additive cohomological splitting. They do not assert multiplicative formality or any new original HM/source evaluation.

## 2. Base-change theorem

Let A→B be a homomorphism to a nonzero noetherian C-algebra. Write τ for the image of t₁, J=IB, δ_B for the pulled-back column, T_B=R⊗C B, m_B=m⊗C B, and

    E_B = {(f,g)∈Rbar⊗C B : f(0)=τg(0)},
    K_B = coker(δ_B:B→B⁴).

Assume precisely the faithful-column condition

    Ann_B(J)=0, equivalently δ_B:B→B⁴ is injective.                (FC)

Then:

1. The actual parameter-derived pullback is

       C_B := C_A ⊗ᴸ_A B ≃ [E_B --δ_Bβ--> B⁴].                   (4)

2. Its cohomology is H⁰(C_B)=m_B and H¹(C_B)=K_B. In addition,

       K_A⊗ᴸ_A B ≃ K_B,    Tor^A_j(K_A,B)=0 for all j>0.          (5)

3. Its actual Postnikov class κ_B∈Ext²_{T_B}(K_B,m_B) satisfies

       Ann_B(κ_B)=J,             Bκ_B ≅ B/J.                     (6)

4. At each p∈Spec B the recomputed localized class has annihilator JB_p. Consequently the actual node family is cohomologically split on a parameter neighborhood of p exactly when p∉V(J).

No flatness of B over A, regularity of B, smoothness, or regular-sequence assumption on the four pulled-back differences is needed. Noetherianity is convenient for the geometric formulation; the ring calculation itself works for any nonzero commutative C-algebra satisfying (FC).

### Proof of (4) and (5)

E_A≅R⊗C A is A-flat, and A⁴ is A-free. Thus the bounded flat complex (1) computes its own parameter-derived pullback. Sequence (2) stays exact after arbitrary base change because its quotient A is A-free. It becomes

    0 → m_B → E_B --β--> B → 0,    E_B ≅ T_B.                    (7)

The definition of E_B agrees with that tensor pullback: it is the kernel of the surjection Rbar⊗C B→B sending (f,g) to f(0)−τg(0), whose original quotient A was free. Because β is surjective, injectivity of δ_B gives ker(δ_Bβ)=ker β=m_B and coker(δ_Bβ)=K_B. Finally (3), a two-term free resolution of K_A, computes all its Tor groups; (FC) kills its only potentially nonzero positive Tor. This proves (4)–(5).

### The residue class over arbitrary B

There is a natural branch-residue identification

    V_B := Ext¹_{T_B}(B,m_B) ≅ B².                               (8)

Here B carries the T_B action through residue T_B→B. To check (8) without a base-change theorem requiring A-flatness, start with the finite-rank free R-resolution of C beginning

    ... → R² --diag(s,t)--> R² --diag(t,s)--> R² --(s,t)--> R → C → 0.

Tensor over the field C with B. This remains exact and is a free T_B-resolution of B. Because its terms have finite rank, applying Hom into m_B produces exactly the original Hom complex tensored over C with B. Its cohomology therefore tensors over C as well. Decomposing m≅R/(t)⊕R/(s) gives Ext¹_R(C,m)≅C².

The coordinates can be fixed intrinsically by the normalization residue sequence

    0 → m_B → Rbar⊗C B → B² → 0.

Its boundary identifies B² with V_B: this follows by tensoring the corresponding isomorphism over C, or by the preceding free resolution and naturality. In these coordinates the extension η_B of (7), pulled back along b↦(τb,b), is

    η_B = (τ,1).                                                 (9)

In particular its second coordinate is a unit even when B is singular, reducible, or nonreduced.

### The actual Postnikov class and its annihilator

Condition (FC) supplies the short exact T_B-module sequence

    0 → B --δ_B--> B⁴ → K_B → 0.                                 (10)

The two-extension of the actual complex (4) is

    0 → m_B → E_B --δ_Bβ--> B⁴ → K_B → 0.                        (11)

It is the Yoneda splice of (7) and (10), rather than an arbitrary class with the same fibers. Applying Ext_{T_B}(−,m_B) to (10) gives

    V_B⁴ --δ_B*--> V_B --∂--> Ext²_{T_B}(K_B,m_B).

The first map has image JV_B. Hence the connecting map induces an injection

    (B/J)² = V_B/JV_B ↪ Ext²_{T_B}(K_B,m_B).                      (12)

By Yoneda compatibility, κ_B=∂η_B, up to a harmless simultaneous convention for sign. Its preimage in (12) is (τ mod J,1 mod J). A scalar b kills that vector exactly when b∈J, proving (6), including the case J=B when κ_B=0.

### The exact parameter-local splitting locus

For every p∈Spec B, localization preserves (FC), and the same proof applied directly to the C-algebra B_p gives (12) with B_p in place of B. This recomputation avoids imposing an unnecessary noetherianity or Ext-localization hypothesis on the algebraic tensor ring T_B. If J⊂p, the representative has nonzero unit second coordinate in B_p/JB_p, so its Postnikov class is nonzero. A splitting on any parameter neighborhood would induce a splitting there, which is impossible.

If J⊄p, some δ_i is invertible on a principal parameter neighborhood. Elementary row operations there take the column to (1,0,0,0)ᵀ. They turn (4) into

    [E_B --β--> B] ⊕ B³[-1] ≃ m_B ⊕ B³[-1]

on that neighborhood. This proves the stated equivalence. It is a parameter-local statement, not a claim that splittings on the complement glue globally.

## 3. What the hypothesis excludes

For arbitrary A→B, with N=Ann_B(J), the flat-complex argument still gives (4), and there is an exact sequence

    0 → m_B → H⁰(C_B) --β--> N → 0,    H¹(C_B)=K_B,              (13)
    Tor^A_1(K_A,B)=N,    Tor^A_j(K_A,B)=0 for j≥2.               (14)

Indeed H⁰(C_B)=β⁻¹(N); surjectivity of β proves (13). Thus (FC) is necessary and sufficient for the canonical conductor inclusion to identify H⁰(C_B) with m_B, and for the sequence (10) to be exact. Without it, (11) is not a two-extension with those endpoints, so the annihilator argument cannot simply be reused.

The extreme case is a map factoring scheme-theoretically through Z₀. Then J=0, δ_B=0, and

    C_B=[E_B --0--> B⁴] = E_B ⊕ B⁴[-1].                          (15)

This family really is cohomologically split, but its degree-zero cohomology is E_B, not the old m_B. Its newly computed Postnikov class is zero. This applies, in particular, to closed uniform fibers and to arbitrary restrictions entirely inside Z₀. It does not contradict (6): such nonzero B fail (FC).

For an integral B the dichotomy is especially clean: either J=0 and (15) holds, or J≠0 and (FC) holds automatically. In the second case the obstruction survives exactly at parameter points over Z₀. Dominance is sufficient but not necessary: even a nondominant integral curve not wholly contained in Z₀ falls in the second case. A mixed or nonreduced base with N≠0 need not satisfy either simple conclusion; (13) is the correct starting point there.

## 4. Dominant modifications and alterations cannot remove the obstruction

Let f:Y→P be a dominant morphism with Y integral and locally noetherian. At every y∈Y the map A→O_{Y,y} is injective: a regular function vanishing in that local ring vanishes on a nonempty open of the integral Y, hence at its generic point; dominance sends that point to the generic point of P. Thus each original nonzero δ_i remains nonzero in the domain O_{Y,y}. In particular (FC) holds.

The theorem, applied on affine opens and to these local rings, yields

    H⁰(Lf* C_A)=m_Y,    H¹(Lf* C_A)=f* K_A,
    local Ann(κ_Y)=I O_Y.                                        (16)

Here the notation Lf* means parameter-derived pullback; all node modules carry R⊗C O_Y. Formula (16) is read locally, and the annihilator ideals agree on overlaps. At every y∈f⁻¹(Z₀), no parameter neighborhood admits a cohomological splitting. In contrast, the further derived restriction to the residue field of y is a different operation and may split as in (15).

A proper dominant such f is surjective: its image is closed by properness and dense by dominance. Since Z₀ is nonempty, f⁻¹(Z₀) is nonempty. Therefore no proper dominant integral modification or alteration can make the pulled-back node family cohomologically split everywhere. The argument does not require generic finiteness, birationality, smoothness, or a regular source. In particular it applies to proper dominant integral alterations, and strengthens the specific blowup conclusion of PR585.

Properness matters for the existence of an obstructed point, not for persistence at a point that exists. The dominant open immersion P\Z₀→P avoids Z₀ entirely and has no such local obstruction. Accordingly one must not claim that every dominant morphism has an obstructed point.

## 5. Arc contact order and ramification

Let γ:Spec B→P with B=C[[u]]. Use ν_u(0)=+∞ and suppose δ_B is not identically zero. Define the finite contact order

    m = min_i ν_u(δ_i) ≥ 0.

Then J=(u^m). Write δ_B=u^m v with v∈B⁴ unimodular: at least one coordinate of v is a unit. Permuting that coordinate to the first position, scaling its row by its inverse, and subtracting multiples of it from the other rows produces U∈GL₄(B) with

    Uδ_B = (u^m,0,0,0)ᵀ.

These are actual target row operations on (4). Consequently

    K_B ≅ B³ ⊕ B/(u^m),
    C_B ≅ [E_B --u^m β--> B] ⊕ B³[-1].                          (17)

The class of the first block is the splice

    0 → m_B → E_B --u^m β--> B → B/(u^m) → 0.

The same long Ext argument for 0→B --u^m--> B→B/(u^m)→0 injects

    (B/(u^m))² ↪ Ext²_{T_B}(B/(u^m),m_B)

and represents the block class by (τ mod u^m,1 mod u^m). Thus the actual full Postnikov class has

    Ann_B(κ_B)=(u^m),    Bκ_B≅B/(u^m),    length_B(Bκ_B)=m.       (18)

For m>0, the generic arc point lies off Z₀, the closed point lies on Z₀, and m is exactly the scheme-theoretic intersection/contact length with Z₀. Equation (18) detects that length in the cyclic obstruction, not merely in the defect's torsion. For m=0 the arc misses Z₀, B/(u^m)=0, and the family splits. An arc contained in Z₀ has infinite contact order, fails the nonzero-column assumption, and instead has the split form (15); there is no legitimate infinite-length version of (18).

Now make a ramified parameter change B→B'=C[[v]], u↦v^e, with e≥1. The pulled-back differences have minimum v-adic valuation em, so the same row operations and Ext computation give

    K_B' ≅ B'³ ⊕ B'/(v^{em}),
    C_B' ≅ [E_B' --v^{em} β--> B'] ⊕ B'³[-1],
    Ann_B'(κ_B')=(v^{em}),    length_B'(B'κ_B')=em.              (19)

These are the recomputed actual class and cohomology after parameter-derived pullback. For m>0 no finite ramification kills the obstruction: it multiplies its thickness by e. More generally, the same valuation conclusion holds for u↦a(v)v^e with a(v) a unit; absorb the resulting unit into the first target row. This is a universal Picard parameter test, not evaluation of any selected original HM source or a lifting/algebraicity theorem.

## 6. Conclusion

The faithful-column condition, rather than smoothness or regularity, is the algebraic boundary of the unchanged-cohomology argument. Under it the actual cyclic obstruction is exactly B/IB. Integral dominant base changes retain the obstruction wherever they meet the uniform locus, and proper dominant ones must meet it. Transverse or higher-contact arcs record the obstruction as a finite-length residue block whose length is contact order; ramification increases that length. Restrictions wholly inside the uniform locus split for a different reason: derived base change changes H⁰ through Tor.
