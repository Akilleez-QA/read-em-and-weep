# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: high-pole conductor obstruction

This audit reads the normalization/conductor proof, the discriminant-pole exclusion proof, the effective-collision bound, and the present directory's draft `PROOF.md`. It uses only their displayed bundle sequences and regularity inputs. No source representative, selected matrix rank, polynomial instance, or obstruction value is evaluated.

## Verdict

The draft's parameterized conductor theorem, its finite-section correction, its source-to-top-symbol map, and its explicit sign correction are valid. In particular, under the original 11-regularity bound:

- H¹(T,ν*B(t))=0 for t≥11.
- At t=14 the canonical conductor cokernel is H²(B(8)); at t=15 it is H²(B(9))=0.
- A third-layer obstruction coming from a first-coordinate primitive is exactly Δ²[c₁], rather than an arbitrary element of H²(B(8)).
- The five relations/four generators do not by themselves give the global-section presentation: extra global relations H¹(B(t−6)) and missing global sections H²(B(t−6)) must be retained.

There is, however, an additional consequence of the *already admitted HM monad* that is stronger than 11-regularity alone: H²(B(t))=0 for every t≥4. Consequently H²(B(8)) is actually zero under the full existing premises, and **both retained third layers are universally removable**. This does not decide any original retained obstruction. A separate conditional improvement from F being 5-regular is recorded below.

## 1. Normalization vanishing and the canonical quotient

Write M=ν_*O_T, L_t=B(t)|D, G_t=ν*L_t and Q_t=B(t)⊗Q. For an m-regular B, tensoring the normalization resolution gives

    0 → B(t−2)^5 → B(t)⊕B(t−1)^4 → ν_*G_t → 0.

For t≥m the middle H¹ terms and the left H² term vanish. Since ν is finite, this proves H¹(T,G_t)=0. For t≥m+1 the left H¹ term also vanishes; hence every global normalized section lifts through the displayed middle term. The unit summand maps to zero in Q_t, proving

    im[H⁰(T,G_t)→H⁰(Q_t)]
      = im[H⁰(B(t−1))^4→H⁰(Q_t)]                  (t≥m+1).

The sequences

    0 → L_t → ν_*G_t → Q_t → 0,
    0 → B(t−6) --Δ→ B(t) → L_t → 0

then give, for t≥m+1, the canonical identification

    H⁰(Q_t)/im H⁰(B(t−1))^4
       --∂dsc→ H¹(D,L_t) --∂D→ H²(B(t−6)).

Each arrow is an isomorphism. This uses actual connecting maps; no dimension calculation or surjectivity assumption on global sections replaces them.

Given a closed layer cochain s and a normalized primitive a with δa=ν*s, the quotient section q=dsc(a) is global. The layer is zero if and only if q lies in the displayed generator image. In that case a global normalized correction makes a descend, and the descended zero-cochain removes the layer by a Čech coboundary. At these twists H¹(B(t))=0, so no additional closed-meromorphic-one-cochain ambiguity remains.

## 2. The correct finite section sequence

Set K_t=im[B(t−2)^5→B(t−1)^4] and

    V_t=coker[H⁰(B(t−2))^5 --A→ H⁰(B(t−1))^4].

The two exact sequences

    0 → B(t−6) → B(t−2)^5 → K_t → 0,
    0 → K_t → B(t−1)^4 → Q_t → 0

give, for t≥m+1,

    0 → H¹(B(t−6)) → V_t → H⁰(Q_t)
      → H²(B(t−6)) → 0.                              (A)

Indeed H⁰(K_t)/im H⁰(B(t−2))^5≅H¹(B(t−6)), and H¹(K_t)≅H²(B(t−6)). These are the two distinct defects of the naive global presentation:

- H¹(B(t−6)) measures relations between global generator sections not obtained from global coefficients in the five displayed sheaf relations.
- H²(B(t−6)) measures global Q_t sections not expressible by global coefficients in the four displayed generators.

For t=14 this gives H¹(B(8)) and H²(B(8)); for t=15 it gives H¹(B(9)) and H²(B(9)). Under only the coarse B 11-regularity input, the last group at t=15 vanishes but H¹(B(9)) need not. Under all the already admitted HM premises, Section 5 below also kills the t=14 last group. It still does not kill H¹(B(8)) or H¹(B(9)). Thus surjectivity of V_t→H⁰(Q_t) must not be confused with its injectivity.

## 3. Sign audit

Use the draft's convention Cj=(Δ,0), where C₀ is the unit row of C and A consists of the other rows. For q∈H⁰(Q_t), choose local lifts b in B(t−1)^4 and then e with δb=Ae. Write δe=jf. The ordinary two-step boundary from the Q resolution is [f].

The image a of (0,b) in ν_*G_t satisfies

    δa = image(0,Ae) = image(−C₀e,0).

Therefore ∂dsc(q) is represented on D by −C₀e, and its next boundary is determined by

    δ(−C₀e)=−C₀jf=−Δf.

Consequently

    ∂D∂dsc(q)=−[f].

The draft correctly defines the final arrow in (A) using −[f]. Its claim that this arrow equals the canonical composition is therefore sound. Without that explicit minus sign, it would have the opposite sign. Exactness and generator membership are unaffected, but identifying the actual obstruction requires the chosen convention.

## 4. Which top symbols can arise

Let F=B(a), and let h be a k-pole primitive for a regular two-cocycle c. The top symbol lies in F(kD)|D. The connecting map for

    0 → F((k−1)D) → F(kD) → F(kD)|D → 0

sends its class to the image of [c] in H²(F((k−1)D)). In twist notation this is precisely Δ^(k−1)[c]. Equivalently, if the twisted representative b satisfies δb=Δ^k c, division of δb by the displayed kernel injection Δ gives Δ^(k−1)c. This establishes the sign positively with the draft's connecting convention.

Hence the conductor class of a first-coordinate three-pole primitive maps to

    Δ²[c₁] ∈ W*⊗H²(B(8)),

and the second maps to Δ²[c₂]∈(W²)*⊗H²(B(9)). Before inserting any additional vanishing, the actual first-coordinate top obstructions form im(Δ²), and the kernel is exactly the space of original classes admitting a two-pole primitive. There is no justification for treating every element of H²(B(8)) as an actual top obstruction.

This statement remains valid when the target is subsequently proved zero. In that case the source-to-top map vanishes universally; the original source classes may remain nonzero in lower pole layers.

## 5. Stronger consequence from the existing monad alone

To avoid confusing the normalization sheaf M with the monad middle term, denote the latter by E. The effective-collision proof supplies the normalized HM bundle F, its kernel K, and exact bundle sequences

    0 → K → E=2Ω²(2) → C=5O → 0,
    0 → A=5O(−1) → K → F → 0.

It also proves F is 6-regular and F∨≅F(1), so F∨ is 5-regular. Its Section 3 proves 2Ω²(3) is 0-regular. Thus E=2Ω²(2) is 1-regular, simply by twisting that bundle down by one.

Tensor the two exact sequences by F∨. All bundles are locally free, so exactness is preserved. By the same projective tensor-regularity theorem already admitted in the effective-collision proof:

    F∨⊗C is 5-regular,
    F∨⊗E is 6-regular,
    F∨⊗A is 6-regular.

For t≥4 the relevant portions of cohomology are

    H¹(F∨⊗C(t)) → H²(F∨⊗K(t)) → H²(F∨⊗E(t)),
    H²(F∨⊗K(t)) → H²(End(F)(t)) → H³(F∨⊗A(t)).

The first outer groups vanish for t≥4, so H²(F∨⊗K(t))=0. The final H³ group vanishes already for t≥3. Therefore

    H²(End(F)(t))=0 for every t≥4,
    H²(B(t))=0 for every t≥4.                         (B)

The final implication uses the characteristic-zero trace splitting End(F)=O⊕B. No H⁰-surjectivity or selected rank is used. In particular, this argument does not attempt the invalid inference that the original kernel K has small regularity simply from the regularities of E and C: it bounds one higher-cohomology group after tensoring, using only the displayed long exact sequences.

Consequences under the already established premises:

1. Both H²(B(8)) and H²(B(9)) vanish. Thus both retained third layers are universally removable, and both retained original classes admit primitives with at most two discriminant poles.
2. At t=14 and 15, all global Q_t sections are generated by the four normalization sections with global coefficients. The possible extra relations H¹(B(8)) and H¹(B(9)) remain until separately excluded.
3. Combining (B) with the established H¹(B(t))=0 for t≥10 gives H¹(D,L_t)=0 for t≥10. Thus every layer with twist at least 10 is removable, a sharper uniform threshold than the coarse regularity-only threshold 15.
4. None of these statements provides a regular primitive or computes any of the thirty retained values. The obstruction remains in the principal parts of order at most two.

More generally the same argument proves Hⁱ(B(t))=0 for 2≤i≤4 and t≥6−i from the existing F∨ 5-regularity. Only the i=2 case is needed here.

## 6. Conditional improvements from a sharper independent HM input

This audit has not independently verified an external HM cohomology table. The following are logical consequences if a separate audit establishes F is 5-regular:

- F∨ is 4-regular, and tensor regularity gives B 9-regular.
- The normalization theorem therefore applies with m=9: normalized H¹ vanishes for t≥9, and the generator-image/canonical-quotient conclusions apply for t≥10.
- H¹(B(8))=H¹(B(9))=0. Together with H²(B(8))=H²(B(9))=0, (A) becomes a genuine isomorphism V_t≅H⁰(Q_t) at t=14 and 15.
- Repeating Section 5 with F∨ 4-regular sharpens (B) to H²(B(t))=0 for t≥3. Hence every second-coordinate original class admits a **single-pole** primitive because F₂(D)=(W²)*⊗B(3). The first coordinate still has the universal two-pole bound by B(8).
- With H¹(B(t))=0 for t≥8 and H²(B(t))=0 for t≥3, H¹(D,L_t)=0 for t≥9. In particular every second-coordinate double layer is removable without a closed-cochain correction.

The stronger single-pole conclusion requires the independently improved F input, whereas the two-pole conclusion for both coordinates does not.

## Scope

The audit distinguishes (i) what follows from B's coarse 11-regularity alone, (ii) additional consequences of the HM monad and F∨ 5-regularity already proved in the existing local input, and (iii) conditional consequences of a separately verified F 5-regularity bound. No actual source/rank/polynomial evaluation or external source-app write was performed. The only write is this local audit artifact.

## Final draft review

The subsequently integrated `PROOF.md`, SHA-256 `f632cac385025b0ab0655ea14eaef2b6826256911e1b4243d2b617f8ad5f1767`, is accepted. Its Section 5 includes the unconditional monad improvement proved above, and its Section 6 correctly gives the combined threshold t≥max(m−1,r+5). Its Section 7 is also correct under its expressly conditional sharper F input: both double-pole principal-parts groups canonically recover the original classes; the second single-pole group must be quotiented by im H¹(B(3)); and the transition from one to two poles is surjective with exactly that kernel. No H¹(B(3)) vanishing is silently inferred. The sharper F input itself remains outside this audit's source verification.
