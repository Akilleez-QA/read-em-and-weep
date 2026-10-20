# Root-line transport of the canonical-coefficient characteristic class

## Outcome and conventions

The physical bundle and the plane bundle have canonically the same endomorphism sheaf after pullback, but their characteristic evaluation maps differ. The difference includes a nonzero middle HKR component, not only a scalar gerbe adjustment.

Use the Atiyah/Chern normalization

    tr At(E)=c1(E),     (1/2)tr At(E)^2=ch2(E).

Cup products include the usual total Čech–forms (or Dolbeault–forms) signs. In the row/gerbe convention of the supplied module-lifting report, define the HKR components by

    κ_E(π,v,b) = (1/2)ι_π At(E)^2 + v⌟At(E) − b Id_E.       (1)

Thus the middle-component sign is explicitly fixed by its displayed characteristic pairing, and the scalar triple-unit/gerbe component contributes minus b. The bivector component corresponds to the first-order product (1/2)π(df,dg). These are the ordinary characteristic-HKR conventions matching the given source, not a Todd-modified Mukai-coordinate convention.

Under the normalized finite canonical trace and the supplied root data, the physical direction (π,0,b), with b=−15Π and Π=(1/2)ι_πℓ², induces the following cohomologically corrected plane direction:

    (P, D_P(H/2), −2H²)
      ∈ H⁰(Λ²T_S⊗ω_S) ⊕ H¹(T_S⊗ω_S) ⊕ H²(ω_S),        (2)

where S=P², P is the identity morphism Λ²Ω¹_S=ω_S→ω_S, H=c1 O_S(1), and H² is its canonical-form-valued cup square. The notation D is defined intrinsically below, including its signs. Its characteristic evaluation on E vanishes. The middle component is nonzero.

This proves a cohomological comparison. It does not construct a fractional line on P², a chain-level equivalence, a Morita bimodule, an explicit Čech primitive, a mixed-order lift, or a comparison of physical higher coefficients.

## 1. Universal tensor-line formula

Let A=At(E), let L be a genuine line upstairs, and put ℓ=At(L)=c1(L). Then

    At(E⊗L)=A+ℓ Id.

For a bivector with any coefficient line K, define D_πℓ∈H¹(T⊗K) by the intrinsic contraction identity

    (D_πℓ)⌟A = ι_π(ℓ A).                                (3)

Equivalently, contract one cotangent factor of ℓ against π, with the Koszul sign prescribed by (3). Equation (3), rather than an unannounced choice of left versus right contraction, fixes the middle-coordinate convention. This operation is the contraction isomorphism Ω¹→T⊗ω when π=P on a surface, so D_P(H/2) is nonzero.

The total degrees of the Atiyah factors are even. Since ℓ is scalar, the two cross terms coincide. Therefore

    (1/2)ι_π(A+ℓ Id)^2
       = (1/2)ι_π A² +(D_πℓ)⌟A +(1/2)ι_πℓ² Id.

Including an arbitrary middle and gerbe component gives

    κ_(E⊗L)(π,v,b)
      = κ_E(π, v+D_πℓ,
                  b−v⌟ℓ−(1/2)ι_πℓ²).                    (4)

Formula (4) is an equality of characteristic cohomology classes under End(E⊗L)=End(E). It is not a statement that the same unmodified ambient class has the same action on both bundles. The intrinsic formula remains meaningful without choosing any numerical generator of H²(K).

For the supplied physical bundle F=N⊗p*E, use ℓ=c1N=(1/2)p*H. Apply (4) to p*E. There is no assertion that N descends to P², nor that O(1/2) exists there. H/2 is used solely as a rational/complex cohomology class.

## 2. Finite pushdown and canonical normalization

Let Y=C×C and p:Y→S have degree eight, with the supplied deck/swap character χ and Lχ=(p_*O_Y)_χ. Throughout, p* denotes ordinary pullback and p_* denotes finite direct image.

Choose Ω∈H⁰(ω_Y) dual to π, so ι_πΩ=1. The intrinsic identification of the character line with the canonical line is

    j_Ω(l)=(1/8)Tr_p(l Ω): Lχ→ω_S.

More invariantly Lχ⊗H⁰(ω_Y)≅ω_S. Normalized trace, not bare trace, is essential: it makes the descended symbol P exactly the wedge map. Its compatibility with cup products, pullback, and contraction gives, for the classes used here,

    j_Ω(ι_π p*η)=η,    η∈H²(S,Ω²_S),

and the corresponding middle-component contraction identity. This follows from the trace-pullback identity Tr_p(p*η)=8η; equivalently check the sheaf identity on the étale locus and extend. No coordinate or Jacobian evaluation is required.

Set h=p*H and ℓ=h/2. Then

    j_Ω(Π)=j_Ω((1/2)ι_πℓ²)=H²/8.

Thus b=−15Π descends as −15H²/8. Formula (4) supplies the extra middle class D_P(H/2) and changes the gerbe coordinate by a further −H²/8. The resulting gerbe is −16H²/8=−2H², proving (2).

Using unnormalized finite trace multiplies all three canonical-coefficient components by eight. Arbitrary volume or determinant trivializations likewise rescale their joint normalization; they cannot remove the middle component. Keeping ω_S and j_Ω avoids those ambiguities.

## 3. Numerical and rank-two checks

For the stable plane rank-two bundle, c1(E)=−H and c2(E)=4H². Consequently

    ch2(E)=−(7/2)H².

The normalized formal Chern expression (no fractional line is asserted) is

    ch(E)e^(H/2)|degree 2
      = ch2(E)+(H/2)c1(E)+2(H/2)²/2
      = −(15/4)H².                                       (5)

This is the trace of the bivector characteristic evaluation after root normalization. Its scalar-inclusion coordinate is half of (5), namely −15H²/8. This agrees exactly with the pushed-down physical b=−15Π.

Alternatively, evaluate the corrected plane class (2). Its trace is

    −(7/2)H² −(1/2)H² −2(−2H²)=0.                        (6)

The second term is the middle contraction tr((D_P(H/2))⌟At(E))=(H/2)c1(E). The last term includes rank two and the minus-gerbe convention. On a stable plane, trace is an isomorphism Ext²(E,E⊗ω_S)→H²(ω_S), so (6) already proves vanishing.

There is a stronger rank-two identity that does not require simplicity. Put

    A₀=At(E)−(1/2)tr At(E) Id.

Then

    A₀²=(1/2)tr(A₀²) Id.                                (7)

In the present plane case A₀=At(E)+(H/2)Id. Hence the root-normalized bivector evaluation is scalar before any appeal to the dimension of the stable-plane obstruction group. Its tracefree component vanishes universally. The pushed-down physical gerbe −15H²/8 cancels this root-normalized bivector evaluation. Equivalently, after tensor-line transport, the gerbe −2H² in (2) cancels the combined unnormalized bivector-plus-middle evaluation, which is −2H² Id. This concerns the correctly transported full first-order direction, not the uncorrected bracket alone.

## 4. Proof of the rank-two identity and the global fourfold consequence

On a compact complex projective manifold, choose a Hermitian metric and use the Chern-curvature representative of the Atiyah class, with its normalization fixed by the Chern identities above. Curvature entries are ordinary differential 2-forms, hence commute in the exterior algebra: their total degree is even. Subtract half the scalar trace curvature to obtain a traceless 2×2 matrix R₀ over this commutative even-form algebra. Cayley–Hamilton gives

    R₀²+det(R₀)Id=0,
    tr(R₀²)=−2det(R₀),

and therefore R₀²=(1/2)tr(R₀²)Id. This identity of forms descends to (7). It does not require globally trivializing the vector bundle: trace subtraction and the asserted identity are invariant under change of frame. No physical matrix products are being evaluated; this is the universal rank-two curvature identity.

If det(F) is holomorphically trivial, choose a determinant-one Hermitian metric in a fixed determinant trivialization. Its Chern curvature is traceless, so At(F)²=(1/2)tr At(F)² Id directly. More generally, vanishing real first Chern class on a compact Kähler manifold permits a flat determinant metric and gives the same conclusion in cohomology. Merely having rank two, without determinant normalization, would not suffice for the unnormalized identity.

In the stipulated actual abelian fourfold situation, assume the supplied genuine root/determinant identity for F and c2(F)=15θ². The former supplies c1(F)=0 (indeed the stated determinant trivialization when N² is the corresponding pullback O(1)). Then globally, without restricting to simple fibers,

    At(F)² = ch2(F) Id = −15θ² Id,
    ev_F(π)=(1/2)ι_π At(F)² = −15Π Id,
    Π=(1/2)ι_πθ².

For a supplied first-order ambient direction with bivector π, no nonzero middle HKR class, and gerbe class b=−15Π, equation (1) yields κ_F(π,0,b)=0 globally. In the established locally free square-zero algebroid lifting framework, vanishing is exactly the obstruction criterion, so an abstract global first-order module lift exists. This conclusion is conditional only on those explicit ambient HKR/source identifications and the supplied genuine geometric bundle identities. It provides no specific cochain primitive and does not identify a prescribed physical first-order module representative.

It is important to check the middle source class: a higher-order ambient unary term does not contribute to the first-order HKR class, but an actual first-order unary class would contribute v⌟At(F) and cannot be silently discarded. Likewise, a Todd-modified HKR convention must first be converted back to (1); mixing coordinates would change the displayed scalar/middle components. No Todd factor belongs in the ordinary characteristic expansion exp(At) used here, and the source fixes the bivector 1/2 and gerbe-minus conventions independently.

The global first-order vanishing does not prove an order-two module lift, any higher formal lift, any fixed-physical-two-jet assertion, or any of the thirty mixed obstruction values. It also does not prove that the corrected plane torsor is identified with a physical torsor by a chain-level transport. A relative first-order application requires the full relative ambient class and its compatible family normalization, rather than a fiberwise endomorphism-sheaf identification alone.

## Sources and limits

Inputs: ../../null-pair-quotient-bracket/canonical-bracket-0517/RESULT.md; ../../null-factor-surfaces/relative-surface-0502/COTANGENT_TARGET.md; ../../null-module-boundary-audits/module-lifting/RESULT.md; ../../null-simple-fiber-moduli/simple-fiber-0518/RESULT.md; ../../null-simple-fiber-moduli/family-lift-torsor-0523/RESULT.md. All calculations above are universal Atiyah, Chern, finite-duality, and curvature identities. No physical source or jet values are evaluated in this argument.
