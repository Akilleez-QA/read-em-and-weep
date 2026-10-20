# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit of the sharper simple-pole corollary

## Verdict and precisely stated input

Accepted using the separately proved positive-twist vanishings

    H¹(B(t))=0 for t≥7,
    H²(B(t))=0 for t≥2,

together with the normalization, conductor, hypersurface sequences, and compatible Čech framework already established in this directory's dependencies. The sharper theorem is recorded in ../sharper-hm-regularity/SHARPEST-BOUND.md and its primary-source verification in ../sharper-hm-regularity/AUDIT.md. I read those local inputs to check the exact statements; this audit does not independently revisit their external primary source.

Reviewed artifact: `SHARPER-COROLLARY.md`, SHA-256

    70a9c866b99d2c918009bc257be0a3ac8984dea5079377687fa61fd09428c41b.

The conclusions and all their stated endpoints are correct. In particular, the distinction between normalized lifting at t=8 and guaranteed generation by four global coefficients at t=9 must remain.

## 1. Both universal pole bounds are one

For F₁=W*⊗B(−4) and F₂=(W²)*⊗B(−3), the one-pole twists are B(2) and B(3). The assumed H² bound annihilates both target cohomology groups. Therefore every regular two-cocycle becomes a boundary in F_i(D) on the admitted compatible finite affine Čech cover. This proves existence of a meromorphic primitive with at most one discriminant pole in each coordinate.

No primitive for an actual source has thereby been calculated. Existence for every cohomology class is fully compatible with a nonzero original class, because allowing a pole changes the coefficient sheaf.

## 2. Every specified higher-pole primitive can be reduced

For each k≥2 use the exact sequence

    0 → F_i((k−1)D) → F_i(kD) → F_i(kD)|D → 0.

The outer groups controlling H¹(F_i(kD)|D) are H¹(F_i(kD)) and H²(F_i((k−1)D)). At k=2 they are, respectively,

    H¹(B(8)), H²(B(2)) for i=1,
    H¹(B(9)), H²(B(3)) for i=2.

All vanish under the stated hypotheses, and increasing k only raises these twists. Thus H¹ of every layer of order at least two vanishes.

For a specified primitive h, its top symbol s is a closed one-cochain. Write s=δa, lift a to a zero-cochain in F_i(kD) on the affine cover, and subtract its coboundary from h. The result has one lower pole order and the same differential. Iteration reaches order at most one. This proof uses neither a new closed-meromorphic-one-cochain correction nor a choice of a different source representative.

## 3. The principal-parts quotient retains the entire obstruction

The one-pole long exact sequence gives

    H¹(F_i(D)) → H¹(P_i,1) → H²(F_i) → 0.

Hence the precise identifications are

    H¹(P₁,1)/im[W*⊗H¹(B(2))] ≅ H²(F₁),
    H¹(P₂,1)/im[(W²)*⊗H¹(B(3))] ≅ H²(F₂).

The maps whose images are used are those in the displayed principal-parts long exact sequences. They are not asserted to be injective. The corollary correctly makes no claim that H¹(B(2)) or H¹(B(3)) vanishes.

At two poles the middle twists B(8),B(9) have both H¹ and H² zero, so H¹(P_i,2) canonically identifies with H²(F_i). Naturality then proves that H¹(P_i,1)→H¹(P_i,2) is surjective, with kernel exactly the corresponding image of H¹(F_i(D)). Thus the ten and twenty dimensions, taken as the previously established input, remain intact after quotienting the one-pole ambiguity.

## 4. Normalization and divisor-layer vanishing start at t=8

Tensor the normalization resolution by B(t):

    0 → B(t−2)^5 → B(t)⊕B(t−1)^4 → ν_*ν*L_t → 0,
    L_t=B(t)|D.

For t≥8 its controlling H¹ groups have twists t and t−1, both at least seven. The controlling H² group has twist t−2, which is at least six and hence in the assumed H² vanishing range. Finite pushforward therefore gives H¹(T,ν*L_t)=0.

The hypersurface sequence

    0 → B(t−6) --Δ→ B(t) → L_t → 0

gives H¹(D,L_t)=0 for t≥8, since H¹(B(t))=0 and H²(B(t−6))=0. Thus the conductor descent sequence gives surjectivity

    H⁰(T,ν*L_t) → H⁰(Q_t)                    (t≥8).

This conclusion really includes t=8, the first coordinate's second-pole layer. No claim about generators is needed to obtain either descent surjectivity or layer removal.

## 5. Four global generators and global relations have different endpoints

Every global normalized section lifts to H⁰(B(t))⊕H⁰(B(t−1))⁴ when H¹(B(t−2))=0, which is guaranteed for t≥9. The unit summand maps to zero in Q_t. Therefore for t≥9,

    im[H⁰(T,ν*L_t)→H⁰(Q_t)]
      =im[H⁰(B(t−1))⁴→H⁰(Q_t)]=H⁰(Q_t).

Splitting the Q resolution through K_t=im[B(t−2)⁵→B(t−1)⁴] gives in that same range

    0 → H¹(B(t−6)) → V_t → H⁰(Q_t) → 0,
    V_t=coker[H⁰(B(t−2))⁵→H⁰(B(t−1))⁴].

Here the missing-section term H²(B(t−6)) is zero because t−6≥3. The extra-relations term H¹(B(t−6)) is guaranteed to vanish only for t−6≥7, or t≥13. Thus V_t≅H⁰(Q_t) is proved by these thresholds for t≥13. The corollary does not assert nonvanishing of extra relations below that threshold or minimality of any endpoint.

## 6. Why t=8 cannot be silently included in the four-generator claim

At t=8 define the map induced by the leftmost differential in the Q resolution

    u=H¹(j⊗B(8)):H¹(B(2)) → H¹(B(6))⁵.

Here j:O(−6)→O(−2)⁵ is the leftmost map in the Q resolution. Since A is a 4×5 linear matrix, its signed maximal minors form a degree-four kernel vector. The kernel is O(−6), so this vector equals j up to a nonzero scalar; their generated ideal is the already proved downstairs conductor ideal. Thus the corollary's identification of the quartic entries is correct without evaluating them.

Because H¹(B(7))=0 and H²(B(2))=0, splitting the resolution shows

    0 → ker(u) → V₈ → H⁰(Q₈) → coker(u) → 0.

Indeed H⁰(K₈)/im H⁰(B(6))⁵=ker(u), while H¹(K₈)=coker(u). The stated thresholds do not determine whether u is surjective, so they do not establish four-global-generator surjectivity at t=8. Nevertheless every Q₈ section lifts to a global normalized section by Section 4. Global normalized sections not lifted by the displayed four generator summands can account for the difference.

This exact endpoint calculation strengthens the corollary's caution without adding any rank claim.

## 7. Remaining boundary and scope

The remaining simple-pole layers occur at twists two and three. Neither normalized H¹ vanishing nor divisor-layer H¹ vanishing has been established there by these hypotheses. Removal to a regular primitive is exactly the original obstruction problem, allowing precisely the closed simple-pole corrections encoded in Section 3.

No source representative, selected rank, polynomial instance, physical jet, or actual obstruction coordinate was evaluated. No external source was modified. The original `AUDIT.md` was left intact.
