# Pair quotient: canonical global 32/30 bridge and relative rank-12 recipient

## Result

Work over C, with the locally free HM bundle and its genuine geometric permutation action as in the supplied reports. Put X=P²_z×P²_h, let m:X→P⁴ multiply binary quadratics, and put A=m*End(HM), A₀=m*End₀(HM). Then the full-deck-sign sector odd under both inner swaps is canonically, up to fixed constant determinant-line conventions,

    H²(X,A₀⊗ω_X)=H²(X,A⊗ω_X).

The block exchange τ(z,h)=(h,z) has dimensions 32 and 30 on its + and − eigenspaces. The + space is the D8 permutation-sign target. Its full S4 alternating projector has a canonical 2-dimensional image and a canonical 30-dimensional kernel. The kernel is not obtained by choosing individual Horrocks summands: it is the cohomology of the dual trace-zero summand of m_*O_X, restricted to block-even parity. A noncanonical splitting calculates its dimension as 10+20.

For s:X→P²_h, the global tracefree relative complex gives the exact sequence

    0 → H¹(P²,R¹s_*(A₀⊗ω_X))
      → H²(X,A₀⊗ω_X)
      → H⁰(P²,R²s_*(A₀⊗ω_X))
      --d₂→ H²(P²,R¹s_*(A₀⊗ω_X)).                 (1)

The R² sheaf is supported on the exceptional plane parameters. On the good open U, R¹ is precisely the rank-12 cotangent-deformation bundle V twisted by O_h(-3), with constant determinant factors understood. Consequently restriction of (1) gives the previously derived H¹(U,V(-3)) recipient. Block exchange interchanges the two projections; (1) is not automatically compatible with its projectors or with the full alternating projector.

No actual obstruction class is evaluated, and no one of the thirty remaining values is shown to vanish.

## 1. Finite flat multiplication, including the discriminant

A fiber of m over a nonzero quartic consists of its ordered factorizations into two quadratic forms, up to independent scalars. Over C every quartic has such a factorization. Even with repeated roots there are only finitely many quadratic subdivisors of its degree-four root divisor. Thus m is surjective and quasi-finite. It is projective, hence finite. A square-free quartic has exactly binomial(4,2)=6 ordered quadratic factors, so the generic degree is six.

Both X and P⁴ are smooth of dimension four. At any source point over a target point, a system of parameters in the regular target local ring remains a system of parameters in the finite source local algebra. The source is Cohen–Macaulay, so these parameters are a regular sequence. The local flatness/miracle-flatness criterion therefore gives flatness. Equivalently, the finite source module is maximal Cohen–Macaulay over a regular local ring and hence free. Consequently F=m_*O_X is locally free of rank six on all P⁴, not merely off the discriminant. Higher finite direct images vanish.

The coefficients of a product of binary quadratics are sections of O_X(1,1), without a common zero, so

    m*O_P⁴(1)=O_X(1,1).

## 2. ACM and the splitting, with block-exchange linearization

For all integers n, finite projection formula identifies Hⁱ(P⁴,F(n)) with Hⁱ(X,O_X(n,n)). On P², a line bundle has no H¹, its H⁰ can be nonzero only for n≥0, and its H² only for n≤−3. Künneth therefore gives

    Hⁱ(X,O(n,n))=0,    i=1,2,3, for every integer n.

In particular the potentially dangerous H² terms H²(O(n))⊗H⁰(O(n)) and their reversals vanish because their nonvanishing ranges are disjoint. Horrocks' splitting criterion applies to the locally free F and gives a sum of line bundles.

The graded section Hilbert series is

    Σ[n≥0] binomial(n+2,2)² tⁿ = (1+4t+t²)/(1−t)⁵.

No positive-degree line summand is possible because H⁰(F(−1))=0. Comparing the Hilbert numerator of the split bundle therefore proves

    F ≅ O ⊕ O(−1)^4 ⊕ O(−2).                    (2)

This is an isomorphism type, not a canonical decomposition into named summands.

The involution τ is over P⁴ and acts on H⁰(O_X(n,n)) as the ordinary swap of two copies of H⁰(P²,O(n)). Its trace is binomial(n+2,2). Hence its graded generator trace numerator is

    (1−t)⁵ Σ[n≥0] binomial(n+2,2)tⁿ
       = (1−t)² = 1−2t+t².

The eigensheaves F⁺,F⁻ are locally free direct summands, and inherit the intermediate-cohomology vanishing, so Horrocks applies to them separately. Adding and subtracting the trace numerator and the dimension numerator gives

    F⁺ ≅ O ⊕ O(−1) ⊕ O(−2),
    F⁻ ≅ O(−1)^3.                                (3)

Thus no assumption about an equivariant choice of a nonequivariant splitting is needed. The eigen decomposition itself is canonical; its line-bundle splitting generally is not.

## 3. Why the elliptic and inner-swap sector is ω_X with block sign +

Let Y=(P¹)^4, and let q:Y→X quotient by H=< (12),(34) >. The full elliptic-deck-sign summand on Y is the line M=O_Y(−2,−2,−2,−2) with its ordinary product linearization. For each pair, the inner-swap-odd pushforward of O(−2,−2) is O_P²(−3), as established in DECK_ADDENDUM.md. Taking the two pairs therefore gives

    (q_*M)_(inner −,−)=O_X(−3,−3).

The block exchange sends the first odd pair factor to the second and vice versa. These are degree-zero sheaves, so their exchange introduces no Koszul sign. The induced action on O(−3,−3) is the ordinary product swap.

This is also the geometric linearization of ω_X: swapping two surfaces contributes (−1)^(2·2)=+1 to their top-form product. Fixed determinant lines in ω_P²≅O(−3) can be retained throughout; they are constant lines and introduce no missing base twist. In particular the canonical-twist statement is equivariant, not just an equality of underlying line-bundle classes.

Finite equivariant pushforward, projection formula and exactness of character projectors now identify the full-deck-sign/both-inner-odd global cohomology with H²(X,A⊗ω_X). The scalar summand contributes H²(X,ω_X)=0 by Künneth, so replacing A by A₀ is canonical and does not alter this group. The root line N cancels in End as in the supplied reports.

## 4. Dimension 32 versus 30 from finite duality

Finite duality gives a canonical τ-equivariant isomorphism

    m_*ω_X ≅ Hom(F,ω_P⁴)=F*⊗O_P⁴(−5).

Thus (3) yields isomorphism types

    (m_*ω_X)⁺ ≅ O(−5) ⊕ O(−4) ⊕ O(−3),
    (m_*ω_X)⁻ ≅ O(−4)^3.                         (4)

Let B=End(HM). The trace pairing identifies B*=B. Serre duality on P⁴ therefore gives

    h²(B(−5))=h²(B)=2,
    h²(B(−4))=h²(B(−1))=10,
    h²(B(−3))=h²(B(−2))=20.

These are precisely the imported characteristic-zero twist ranks, not new rank computations. Projection formula applied to (4) proves

    dim H²(X,A⊗ω_X)⁺ = 2+10+20 = 32,
    dim H²(X,A⊗ω_X)⁻ = 3·10 = 30.

The block-odd 30 and the kernel inside the block-even 32 are different spaces. Their equal dimensions do not identify them.

## 5. Canonical identification of the fully alternating two-dimensional piece

There is a canonical algebra trace tr:F→O, with tr(1)=6. Thus

    F=O·1 ⊕ F₀,    F₀=ker(tr),

with projector onto constants (1/6)·unit∘tr. Dualizing gives

    m_*ω_X = ω_P⁴ ⊕ (F₀*⊗ω_P⁴).                 (5)

The inclusion of ω_P⁴ is dual to tr/6; the retraction to ω_P⁴ is the dual of the unit. Formula (5) is canonical and τ-equivariant. The constant summand is τ-even. Consequently the 32-space has a canonical rank-two direct summand H²(P⁴,B⊗ω_P⁴) and a canonical complementary space H²(P⁴,B⊗(F₀⁺)*⊗ω_P⁴) of dimension thirty. Only the further representation of that complement as twists −4 and −3 is noncanonical.

To see that the rank-two projector is exactly full alternation, not merely some rank-two projector, use the full S4 quotient ρ:Y→P⁴. As an S4-linearized line,

    ω_Y = M ⊗ sign,

because permutation of four one-dimensional canonical factors contributes permutation sign. Therefore the alternating part for M corresponds to the invariant part for ω_Y. Finite duality identifies ρ_*ω_Y with Hom(ρ_*O_Y,ω_P⁴). Its invariant part is canonically ω_P⁴, because (ρ_*O_Y)^S4=O_P⁴ and invariants are exact in characteristic zero. Under the H quotient, the inner-odd part of M is the H-invariant canonical part, namely ω_X. The full alternating projector is consequently the canonical constants/trace projector in (5).

Equivalently, on the generically étale locus the trace averages over the six ordered pair decompositions. For a block-even class, decompositions occur in pairs, and this is the average over the three unordered pair partitions. The orientation signs converting M to ω_Y recover the signed three-term alternating formula in PROOF.md. Equality extends globally by the canonical finite-duality construction; there is no need to discard the branch locus or pick a graded free-generator basis.

Thus this geometric 2+30 split agrees with the authenticated S4 sign projector on the D8-sign space. It does not assert that the 30-dimensional D8 kernel is itself an S4 subrepresentation.

## 6. Global Leray, exceptional terms, and the rank-12 bundle

Set K=A₀⊗ω_X and s:X→H=P²_h. On the dense good open U, plane stability implies H⁰(A₀,h)=H²(A₀,h)=0; Serre duality then also gives H⁰(A₀,h⊗ω_P²)=H²(A₀,h⊗ω_P²)=0. The surviving H¹ has dimension twelve. Relative duality and cohomology/base change give

    (R¹s_*K)|U = V⊗ω_H,
    (R²s_*K)|U = 0,

where V=R¹s_*(A₀⊗pr_z*ω_P²)|U is the dual of the plane deformation bundle W, as in COTANGENT_TARGET.md.

Moreover s_*K=0 globally: it is torsion-free on the integral base (multiplication by a nonzero base function is injective on the locally free sheaf upstairs), and it vanishes generically. The sheaf T=R²s_*K is coherent and supported on H\U. Top-degree cohomology/base change identifies its fibers with the corresponding H²; after Serre duality their vanishing is equivalent to simplicity of the plane restriction. There is no claim here that H\U is finite, that T is locally free there, or that T equals the naive ordinary dual of a vanishing R⁰ sheaf.

In the Leray spectral sequence E₂^(p,q)=Hᵖ(H,R^qs_*K), the q=0 row vanishes and p,q≤2. In total degree two, E₂^(1,1) survives unchanged, whereas E₂^(0,2) survives precisely as the kernel of

    d₂:H⁰(H,T)→H²(H,R¹s_*K).

This proves (1), including its initial injection and the necessary outgoing differential. In particular the map to H⁰(T) is not asserted surjective. The quotient of H²(K) by the gluing term is ker(d₂), not automatically all exceptional sections.

Restricting to U kills T and gives the canonical identification

    H²(s⁻¹U,K) ≅ H¹(U,V⊗ω_H)=H¹(U,V(−3)),

with the fixed constant-line convention. This is precisely the recipient already obtained from the elliptic pair cover. The same exact-sequence argument also applies directly to the original elliptic projection r and G=End₀(F), since r_*G=0 globally; finite pair pushforward identifies the indicated character portion with the sequence above.

The global exact sequence and its restriction are natural under maps preserving s. However τ interchanges s with the other projection. It carries this entire filtration and edge map to the analogous filtration for that other projection, and generally sends s⁻¹U to a different open subset. Hence one cannot simply put +, −, or the full alternating projector on every term of (1). The 32/2/30 projectors are canonical on the global cohomology, while their comparison with one rank-12 relative presentation requires the two fibrations and their overlap. Restriction need not be injective, and the rank twelve does not bound the dimension of its H¹.

## Scope

Inputs: the three reports in relative-surface-0502 and https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-permutation-sector/PROOF.md. This argument uses only universal binary-form multiplication, finite flatness, coherent cohomology, Hilbert characters, trace and duality. No physical source or jet values are evaluated in this argument. The actual obstruction values and the compatibility of local module lifts remain uncomputed.
