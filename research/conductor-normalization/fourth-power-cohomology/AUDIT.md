# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: fourth-power ideal cohomology

## Verdict

**Pass.** The proof correctly rules out the suggested vanishing of H³(B(−9)), retains all unverified positive-twist H² groups, and identifies the actual fourth-power image by a two-step Koszul boundary. It neither proves that this image is proper nor that it is zero or nonzero.

Audited version of `PROOF.md`: SHA-256 `455c07aad8e90ede5b9c3d6274c2aeedb6e2dcc179454c2917551ab54765de04`.

This audit independently checked the formal deductions from the imported geometric theorem and the recorded primary cohomology proposition. It did not repeat a new visual inspection of the primary scan or re-prove the imported geometric theorem.

## 1. Imported inputs and source boundary

The geometric input is the actual subsheaf inclusion

    C = B(−4)I_N → B(−4),
    I_N = (t₂,t₃), with degrees 2 and 3.

It is stronger than an abstract isomorphism with the fourth-power sign pushforward: the agreement of inclusions is essential for identifying the induced cohomology map. The imported proof supplies exactly that agreement, including at quadruple collisions. Its SHA-256 is `9ce10b76777c65cef689dd1fae40b2cd2e2a4452472fe91ec63d8586de9eaf9d`.

The recorded Decker–Schreyer proposition supplies

    h¹(End(HM)) = 24,
    h¹(End(HM)(−1)) = 5,
    h¹(End(HM)(k)) = 0 for all k ≤ −2.

The source-verification note has SHA-256 `b14f1c1c08b24c015da73ad081a462e0b100831d01db004c96c678e5fc310071`. Its complex-field and classical-HM scope match this proof. In characteristic zero, End(HM)=O⊕B, and the line-bundle summand contributes no intermediate cohomology on P⁴. Therefore the cited H¹ data apply to B. The primary proposition does not establish positive-twist H¹ or H² vanishings.

The stability used is that of the rank-two HM bundle. It implies Hom(HM,HM(k))=0 for k<0. No stability assertion for B itself is necessary. The trace pairing identifies B with B∨.

## 2. Independent Riemann–Roch and duality checks

With c₁(HM)=−H and c₂(HM)=4H², the formal root difference satisfies d²=−15H². Hence

    ch(B) = 1 + exp(d) + exp(−d)
          = 3 − 15H² + (75/4)H⁴.

The Euler polynomial is

    χ(B(t)) = 3 binom(t+4,4) − (15/2)t² − (75/2)t − 25
            = (t⁴ + 10t³ − 25t² − 250t − 176)/8.

In particular χ(B(4))=−85 and χ(B(−1))=5. Serre duality on P⁴ gives

    Hⁱ(B(t))∨ ≅ H⁴⁻ⁱ(B(−t−5)).

At t=4, H³ and H⁴ vanish by the negative-twist primary H¹ proposition and the stability-based negative H⁰ vanishing. Thus

    h¹(B(4)) = 85 + h⁰(B(4)) + h²(B(4)) ≥ 85,
    h³(B(−9)) = h¹(B(4)) ≥ 85.

This is a strict disproof of the zero-group shortcut, not a conclusion about the fourth-power image.

At t=−1, the same inputs give h⁰=h³=h⁴=0 and h¹=5, so χ=5 implies h²(B(−1))=10. Duality then gives h²(B(−4))=10. This independently checks the ambient dimension used in the proof.

## 3. Exact dependence of H²(C)

The Koszul resolution and twists are correct:

    0 → B(−9) → B(−6)⊕B(−7) → C → 0,
    s ↦ (−t₃s,t₂s),
    (a,b) ↦ t₂a+t₃b.

For μᵢ induced by the first map, the long exact sequence gives

    0 → coker μ₂ → H²(C) → ker μ₃ → 0.

Dualizing the finite-dimensional vector spaces and using ambient Serre duality yields exactly

    0 → coker α¹ → H²(C)∨ → ker α² → 0,
    αⁱ:Hⁱ(B(1)⊕B(2)) → Hⁱ(B(4)),
    αⁱ(a,b)=−t₃a+t₂b.

The signs and the order of the B(1), B(2) summands agree with the transpose of the displayed Koszul map. No splitting of either short exact sequence is asserted. In particular, the potentially nonzero H²(B(1)), H²(B(2)), and H²(B(4)) have not been discarded.

If H²(B(1))=H²(B(2))=0 is proved separately, then ker α²=0, giving the conditional simplification stated in the proof. Neither the nonzero H¹(B(4)) nor this conditional simplification forces a nonzero cokernel: the relevant map can be surjective. Equivalently μ₃ can be injective even though its domain is nonzero.

## 4. Duality on the singular surface and the image criterion

The restriction exact sequence gives

    M := im[H²(C) → H²(B(−4))] = ker r,
    r:H²(B(−4)) → H²(N,B(−4)|N).

N is the imported reduced codimension-two complete intersection of degrees 2 and 3. It is therefore projective Cohen–Macaulay and Gorenstein of pure dimension two, with ω_N≅O_N. Smoothness is not required. Since B(−4)|N is locally free on N, Serre duality gives

    H²(N,B(−4)|N)∨ ≅ H⁰(N,B(4)|N).

Combined with ambient duality, the transpose of r is the codimension-two Gysin map

    δ_N:H⁰(N,B(4)|N) → H²(B(−1)).

The displayed two-stage boundary realizes it correctly:

    0 → K=B(4)I_N → B(4) → B(4)|N → 0,
    0 → B(−1) → B(2)⊕B(1) → K → 0.

The first boundary lands in H¹(K); the second lands in H²(B(−1)). These are the correct ambient dual twists. Koszul orientation and the choice of the trivialization of ω_N may change the comparison by a nonzero scalar; this cannot affect the image or any annihilator statement.

Consequently

    M = (im δ_N)⊥,
    M∨ ≅ H²(B(−1))/im δ_N,
    dim M = 10 − rank δ_N.

Thus M=0 exactly when δ_N is surjective; M is the entire ten-space exactly when δ_N=0. A nonzero δ_N is precisely the condition that M be proper. None of these alternatives is decided here.

## 5. Secondary-map refinement

The added σ construction is well-defined and exact. Set L=B(2)⊕B(1), W=H²(B(−1)), and

    V=ker[W→H²(L)],
    Q=coker[H¹(L)→H¹(B(4))].

For x∈V, exactness gives a lift y∈H¹(K). Its image in Q is independent of the lift, because two lifts differ by the image of H¹(L). This defines σ:V→Q.

If σ(x)=0, adjust y by an image from H¹(L) to put it in ker[H¹(K)→H¹(B(4))]. The latter kernel is the image of H⁰(B(4)|N). Conversely every boundary from H⁰(B(4)|N) gives such a lift. Therefore

    im δ_N = ker σ ⊂ V ⊂ W.

For completeness, the full image dependence can also be expressed as

    0 → im σ → M∨ → im[W→H²(L)] → 0.

This follows by taking the quotient of 0→V→W→W/V→0 by ker σ. It makes explicit why retaining positive-twist H² groups matters. If those groups vanish, V=W and M∨≅im σ, exactly as stated in the proof. This is a formal relation; no secondary map, multiplication map, or rank has been evaluated.

## 6. Source-representative scope

A finite quotient admits inverse-image affine Čech covers, and the sign projector is exact in characteristic zero. The imported sheaf identification therefore identifies closed sign cochains with coefficients in the fourth ideal power with cohomology classes of C. The image criterion concerns all such closed representatives.

The converse in the proof is correct: a class in M admits some closed fourth-power representative on such a cover. It does not imply fourth-power membership for a particular preselected source or representative. Likewise, ambient cohomological vanishing does not imply that an already fixed representative has fourth-power membership.

The fifth-power extension is valid under the separately imported equality of sign-pushforward subsheaves, including their inclusion into the same target. It does not equate the ordinary fourth and fifth ideal powers themselves.

## Boundaries

This audit establishes the displayed formal cohomological deductions over C, using the already verified classical HM and geometric inputs. It does not certify any further positive-twist vanishing, physical-source membership, actual obstruction value, pairing, instance rank, polynomial instance, jet, or physical specialization. Only static proof files, formal Riemann–Roch arithmetic, exact sequences, duality, and document hashes were inspected. No external writes were made.
