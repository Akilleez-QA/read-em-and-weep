# Regular normalized trace transport through the ordered-root tower

## Status and precise contribution

This note explicitly normalizes and completes the coefficient-level finite-duality/split-invariants mechanism in the earlier finite-trace and retained-projector arguments. It is not a claim to a newly discovered geometric theorem. It proves the split maps and projector compatibility needed by the conditional full-target collision criterion, for the specified classical tower and coefficient bundles. It does not identify a physical raw source with these coefficients, prove equality of an actual raw class with a paired class, or construct a high-collision-order representative.

Work over C. Put Z=(P¹)^4, X=P²×P² and Y=P⁴. Let p:Z→X take each ordered pair of roots to its binary quadratic and let m:X→Y multiply the two quadratics. Write q=m p. Set G=S4 and K=⟨(12),(34)⟩. Thus X=Z/K, Y=Z/G, deg(p)=4 and deg(m)=6. The maps are finite: a binary polynomial has finitely many root factorizations, including at repeated roots. They are flat by the Cohen–Macaulay-to-regular equal-dimension flatness criterion; all three varieties are smooth. In particular deg(q)=24 and the corresponding function algebras are locally free.

Use distinct notation for the algebra and polarization:

    A=m_*O_X,  R=q_*O_Z,  L=q*O_Y(1)=p*O_X(1,1).

Let B₀ be any vector bundle on Y (in the application B₀=End₀(F), with F the normalized HM bundle). For every integer r set N_r=B₀⊗O_Y(r−5). The proof requires no GL2 action on B₀.

## 1. Finite duality and the regular split

Finite locally free duality, including its evaluation counit, gives

    D_r=Hom_Y(A,N_r)=m_*m^!N_r,
    T_r=Hom_Y(R,N_r)=q_*q^!N_r.

All Hom symbols here are sheaf Hom. Regarding R as a locally free rank-four A-algebra, define its normalized relative trace

    t_p:R→A,  t_p(b)=Tr_(R/A)(b)/4.

The trace is the trace of the A-linear multiplication endomorphism of R. It is A-linear, compatible with restriction and trivialization, and sends a∈A to a. Define

    j_r:D_r→T_r,          j_r(φ)=φ∘t_p,
    ρ_r:T_r→D_r,          ρ_r(ψ)=ψ|_A.

Then ρ_r j_r=Id, since t_p|_A=Id. Thus j_r is a split coefficient-sheaf inclusion, not merely an injection. Its complement is ker(ρ_r). Every construction is regular on all of Y, including the branch discriminant and the quadruple-root locus.

In particular no inverse of the function-trace pairing A→Hom(A,O_Y), no inverse discriminant and no inverse ramification equation occurs. The possibly degenerate trace pairing at a branch point is irrelevant: t_p is a map out of R, not a purported identification of R with its dual.

Finite pushforward has no higher direct images on quasi-coherent sheaves. Applying cohomology to the split maps therefore gives, for every i and r,

    H^i(X,m^!N_r) → H^i(Z,q^!N_r)

with left inverse induced by ρ_r. This proves injectivity in degree two and in every twist without the invalid inference that arbitrary sheaf injections induce H² injections.

## 2. Relative trace is the intermediate Reynolds map

For g∈G use the ordinary action on functions and its dual action

    (g·ψ)(b)=ψ(g⁻¹b)

on T_r; G acts trivially on the coefficient bundle pulled back from Y. Let e_K=(1/4)Σ_(h∈K)h on R. Since A=R^K, e_K has image A. On the dense distinct-root locus the rank-four algebra is the function algebra of a K-torsor, so Tr_(R/A)(b)=Σ_(h∈K)h(b). Both sides are regular A-linear maps between locally free sheaves. Their equality on a dense open implies equality everywhere. Hence e_K=t_p, viewed as a map R→A followed by A→R.

It follows also directly that

    im(j_r)=T_r^K.

Indeed j_r(φ) is K-invariant. Conversely a K-invariant ψ satisfies ψ=ψ∘e_K and therefore equals j_r(ψ|_A). This is a specified coefficient-sheaf identification, not an inference from equal dimensions of cohomology.

The same argument gives the normalized full Reynolds map e_G on R:

    e_G(b)=Tr_(R/O_Y)(b)/24 ∈ O_Y⊂R.

The use of a dense open in this paragraph proves an identity between already defined regular maps on vector bundles. It does not extend a rational map with possible poles by assertion.

## 3. The degree-six constant inclusion and full projector

Let t_m=Tr_(A/O_Y)/6. Define

    ε_r:D_r→N_r,          ε_r(φ)=φ(1),
    i_r:N_r→D_r,          i_r(η)(a)=η·t_m(a).

Then ε_r i_r=Id because Tr_(A/O_Y)(1)=6. Under finite duality, ε_r is the Grothendieck trace/counit for m with coefficients N_r. Thus i_r is a split constant inclusion and i_r ε_r is a canonical projector. It need not be defined by choosing any decomposition of A into line bundles.

Write P_G for averaging on T_r with the dual G action. Since an inverse permutation runs through the same group,

    (P_G j_r(φ))(b)
      = j_r(φ)(e_G(b))
      = φ(1)·Tr_(R/O_Y)(b)/24.

Transitivity of finite locally free traces gives

    Tr_(A/O_Y)(Tr_(R/A)(b))=Tr_(R/O_Y)(b).

Consequently

    (j_r i_r ε_r(φ))(b)
      = φ(1)·Tr_(A/O_Y)(Tr_(R/A)(b)/4)/6
      = φ(1)·Tr_(R/O_Y)(b)/24,

and we have the global coefficient identity

    P_G j_r = j_r i_r ε_r.                         (1)

In particular j_r i_r is split, with left inverse ε_rρ_r. The factors 1/4 and 1/6 account for the rank-four intermediate quotient and rank-six quotient, respectively. Their product is 1/24. Evaluation φ↦φ(1), including weighted evaluation below, is not divided by six. These normalizations have no relation to rank-two endomorphism trace removal or to a degree-64 source-band marking.

## 4. Every twist and multiplication by a weight on X

Because A and R are locally free,

    D_r=D_0⊗O_Y(r),   T_r=T_0⊗O_Y(r).

Under these identifications j_r=j_0⊗Id and ρ_r=ρ_0⊗Id. This establishes the coefficient split for positive, zero and negative twists.

A weight w∈H⁰(X,m*O_Y(d)) need not descend to Y. Its multiplication on the dual coefficient is the map

    M_w:D_r→D_(r+d),   (M_wφ)(a)=φ(w a),

interpreted locally in a trivialization of O_Y(d); the change-of-trivialization factors show that these expressions glue. Equivalently use multiplication by w on m^!N_r. The corresponding ordered-root weight is p*w, defining M_(p*w):T_r→T_(r+d).

A-linearity of t_p gives, in each such trivialization,

    M_(p*w) j_r(φ)(b)=φ(t_p(wb))=φ(w t_p(b))
                       =j_(r+d) M_w(φ)(b).

Thus

    M_(p*w) j_r = j_(r+d) M_w.                     (2)

In particular this applies to σ of degree one and τ of degree two whenever they are the stated global sections on X. The construction of those sections is a separate input. No claim that either is a Y scalar is needed. Weighted finite-duality trace is exactly

    ε_(r+d)(M_wφ)=φ(w).

Combining (1) and (2) yields the regular identity

    P_G M_(p*w) j_r(φ) = j_(r+d) i_(r+d)(φ(w)).    (3)

This does not assert that P_G commutes with arbitrary w-multiplication; generally it does not. The identity applies after the specified intermediate inclusion and uses the weighted evaluation on the right.

## 5. Canonical bundles and the sign conversion

For a finite map between smooth varieties of equal dimension,

    q^!N_r=q*N_r⊗ω_Z⊗q*ω_Y⁻¹.

Using ω_Y=O_Y(−5), the cancellation is

    q^!N_r=q*B₀⊗ω_Z⊗L^r.

After fixing the usual binary-coordinate volume convention, the underlying line bundle ω_Z is L⁻². Thus as underlying bundles

    q^!N_r≅q*B₀⊗L^(r−2),
    m^!N_r≅m*B₀⊗O_X(r−3,r−3).

These identities keep the canonical equivariance; forgetting it loses a sign. Locally an ordered top form on Z is

    dz₁∧dz₂∧dz₃∧dz₄.

Permuting the four one-dimensional factors multiplies this ordered wedge by sgn(g), in addition to the ordinary permutation of tensor factors. Hence, with ordinary ungraded factor-permutation linearization on L,

    ω_Z ≅ L⁻²⊗sgn

as G-linearized lines. Any fixed one-dimensional determinant-of-the-binary-coordinate-space factor can be carried throughout or fixed by a coordinate-volume choice. G permutes factors but does not act on that fixed coordinate space; it does not alter the permutation-sign statement. No equivariant action of binary-coordinate changes on B₀ is being asserted.

Put E_r=q*B₀⊗L^(r−2) with ordinary factor-permutation linearization. The natural finite-duality recipient q^!N_r is E_r⊗sgn. Transporting underlying vectors through this identity changes the natural G action to sgn(g) times the ordinary action. Therefore its invariant average P_G is precisely

    e_sign=(1/24)Σ_(g∈G)sgn(g)g

on E_r in the ordinary convention. Formula (1) becomes, in this convention,

    e_sign j_r = j_r i_r Tr_m^ω,                  (4)

where Tr_m^ω denotes ε_r with coefficients, not the normalized function trace. Notationally j_r in (4) includes the specified underlying canonical-bundle identification.

The K-invariant canonical-form image corresponds to the K-sign image in E_r. Let c exchange the two P² factors of X, and lift it to s=(13)(24) on Z. Then s normalizes K, preserves relative trace, and j_r is compatible with c and s. Exchanging two local two-forms on X has sign (−1)^(2·2)=+1; s is also even. Thus the block-even part of D_r maps to invariants under H=⟨K,s⟩ in the canonical convention, and to the character sgn|_H in the ordinary E_r convention. Its values are (−1,−1,+1) on (12),(34),(13)(24). No S4 action on X itself or on a mixed deformation ambient is required.

## 6. Consequence for the conditional collision criterion

In the notation E=E_0=q*B₀⊗L⁻², the theorem supplies the following purely geometric data for r=0,1,2 (indeed for all r):

1. A regular split coefficient inclusion, hence an injective map H²(X,m^!N_r)→H²(Z,E L^r) after the canonical-sign conversion.
2. Compatibility with σ and τ multiplication, with the exact target twists.
3. Equality of full sign projection with the included finite-duality constant projection, and split injectivity of the constant inclusion after transport.

For the historical order-twelve criterion, suppose independently that C is a paired degree-two class and that a closed regular cochain R₀ with values in I¹²E represents j_0(C). If the separately proved ideal-power vanishings apply to the resulting σ and τ products, equations (2)–(4) and the split constant inclusion convert their sign vanishing into vanishing of Tr_m^ω(σC) and Tr_m^ω(τC). That is the exact geometric dependency closed here.

The already-published sharper criterion in [SHARPEST-BOUND.md, §4](https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md) gives the sufficient coefficient orders 7,8,9 for r=0,1,2. Accordingly a common closed regular unweighted representative R₀∈I⁷E with [R₀]=j_0(C) suffices: σR₀ has order at least eight and τR₀ order at least nine. The same equations (2)–(4) supply the geometric transport and split constant inclusions for this sharper existing criterion. Its weight-zero vanishing likewise kills the constant coordinate. This is an application of an existing bound, not a new numerical bound or an optimality assertion.

Neither an actual closed I⁷E or I¹²E representative nor its equality [R₀]=j_0(C) for an actual source is proved by this coefficient theorem. In particular the arbitrary fact that a class belongs to H²(Z,E), the canonical K-sign character, or ordinary low-order ideal membership does not supply a closed I¹²E representative. Those are separate source-comparison and high-order-lift questions. The maps do not compute any class or prove the retained obstruction zero. Ordinary ideal order is not deformation order, and nothing here asserts algebraicity of a deformation.

## 7. Verification status

The displayed maps, splittings, trace transitivity, weight identity and sign conversion have explicit algebraic derivations above. This is an authored mathematical proof, not a proof-assistant certificate. Historical mathematical reviews of predecessor arguments are identified as historical in the companion extracts; their verdicts do not certify this newly written normalization. Independent review of this note should check in particular (2), the sign conversion in §5, and the unresolved distinction in §6.
