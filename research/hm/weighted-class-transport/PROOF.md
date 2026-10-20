# Normalize the complete source through the root-deck trace

## Decision

At the exact admitted source scope of PR426 and its PR134 comparison, the actual complete raw obstruction class supplies the source-class equality needed by the weighted coefficient tower, after an explicit normalization:

    R0^ω = (1/64) Tr_ρ^ω(Ω R̃raw),
    [R0^ω] = j4(C).

Here ρ:C⁴→(P¹)⁴ has degree 16; Ω=Ω12∧Ω34 is the volume marking used in PR134; R̃raw is a regular quotient-cover representative of the same complete all-four-odd raw class; and j4 is precisely PR387's inclusion dual to Tr_p/4. The trace acts on coefficient entries, not on endomorphisms. The corresponding E-valued R0 is obtained using exactly PR387's fixed canonical-line identification.

The natural degree-16 descent Dρ=(1/16)Tr_ρ^ω(Ω·) instead satisfies

    Dρ j64 = 4 j4.

Thus identifying the two maps merely because both were called j would miss a factor four. This construction discharges the class-equality premise for the explicitly normalized representative. It does not construct a representative in I_D⁷E or I_D¹²E, identify any earlier coefficient-extraction output with R0, or prove a new obstruction vanishing.

## 1. Exact source and tower

Use distinct spaces and maps:

    T=C⁴ --ρ, degree 16--> Z=(P¹)⁴ --p, degree 4--> X=P²×P²
      --π=pρ, degree 64--> X --m, degree 6--> Y=P⁴,
    q=mp.

C denotes the stipulated smooth elliptic curve, not the affine line. The root double covers are the ones in the source. Their product deck group is Δ=(Z/2)⁴ and χ is its all-four-sign character. The pair permutation group is K=⟨(12),(34)⟩. S4 permutes the four ordered factors. The three degree numbers 16, 4, and 6 belong to three different maps.

Let B0=End0(HM) on Y. The genuine root line cancels in the normalized endomorphism coefficient:

    End0(N⊗(qρ)*HM) = (qρ)*B0.

The source class is the complete Rraw of the corrected source edition used in PR426:

    M=g_ik^(-1) D,
    Rraw=tf(M)+δrow(sraw,q kp+sraw,p kq).

D has all seven kinetic terms and all three negative gerbe terms. This is not the isolated M0, an E term, an Fk term, a detector, or an implementation output. The corrected first-order equation includes U_r,ik. The source presentation F=id and complementary-factor support remain hypotheses supplied in those source editions, not assumptions for an arbitrary ambient.

The exact input from PR134 §§3–4, rebound in PR426's closure §4, is

    [Rraw]=j64(C),
    j64(η)=f with fΩ=π*η.                           (1)

One can project Rraw to χ without changing the admitted χ class. In the admitted homogeneous source this projection is unnecessary; writing it explicitly also covers the weaker full-character formulation. C is the canonical corrected paired obstruction, with the same boundary, complete ambient and End marking as in PR134. All its source, localization, regularity, genuine-equivariance, characteristic-zero and pure-boundary rigidity premises remain.

The exact source editions are listed in SOURCES.md. No selected source instance was evaluated.

## 2. Distinguish the two pullback normalizations

For a finite flat map f:V→W of smooth varieties of the same dimension, define the regular dual-trace inclusion

    J_f^un: ω_W → f_*ω_V,
    η ↦ [b ↦ η Tr_f^func(b)]

using finite duality f_*ω_V=Hom_W(f_*O_V,ω_W). The normalized inclusion is J_f^norm=J_f^un/deg(f).

The ordinary differential pullback f*η is J_f^un(η), not J_f^norm(η). To check the convention, on the étale locus finite duality identifies a form θ with b↦Tr_f^ω(bθ). For θ=f*η this functional is b↦η Tr_f^func(b). Both the ordinary differential pullback and this dual-trace map are already defined regular morphisms to a locally free coefficient sheaf. Equality on the dense étale locus proves equality globally. This argument extends no undefined rational map and inverts no discriminant.

The Grothendieck trace/counit is evaluation at 1. Hence

    Tr_f^ω(f*η)=deg(f)η.

In particular PR387's map

    j4(φ)=φ∘(Tr_p^func/4)

corresponds to p*η/4 on canonical forms, whereas (1) corresponds after multiplying by Ω to π*η with no divisor 64.

## 3. Global factorization through the intermediate duals

The cleanest calculation is in finite-duality modules over Y. Put

    A=m_*O_X, R=q_*O_Z, S=(qρ)_*O_T,
    N=B0⊗ω_Y,
    D=Hom_Y(A,N), U=Hom_Y(R,N), V=Hom_Y(S,N).

Finite flatness follows for ρ from the product of finite smooth-curve double covers and for p,m from PR387. In particular the ranks in the algebra tower A⊂R⊂S are 4 and 16. Finite duality identifies D,U,V with the pushed-forward canonical-form coefficients on X,Z,T respectively.

Let res_ρ:V→U be restriction of a functional to R. It is exactly the canonical-form trace Tr_ρ^ω, pushed forward to Y, with the B0 coefficient retained. Multiplication by Ω sends the raw coefficient f to its top-form coefficient fΩ; call this map VΩ.

Equation (1) and §2 give

    (VΩ j64)(φ) = φ∘Tr_(S/A)^func.

Function-trace transitivity gives Tr_(S/A)=Tr_(R/A)∘Tr_(S/R). For r∈R, multiplication by r on the rank-16 R-module S is scalar multiplication, so Tr_(S/R)(r)=16r. Thus

    [res_ρ VΩ j64(φ)](r)
      = φ(Tr_(R/A)(16r))
      = 16 φ(Tr_(R/A)(r))
      = 64 j4(φ)(r).

Therefore the following is an identity of regular coefficient-sheaf maps, not merely a class or dimension comparison:

    Bρ := (1/64) res_ρ VΩ,
    Bρ j64 = j4.                                    (2)

Equivalently, for natural deck descent

    Dρ := (1/16) res_ρ VΩ,
    Dρ j64 = 4j4,   Bρ=Dρ/4.                       (3)

There is no factor six here. That factor appears only in PR387's later constant inclusion i(η)(a)=η Tr_m(a)/6.

As a consistency check, trace transitivity on forms yields

    Tr_p^ω Bρ(f)
      = (1/64)Tr_π^ω(fΩ)
      = Ψ(f),                                        (4)

where Ψ is precisely PR426's inverse band marking on the appropriate pair sector. Because Tr_p^ω j4=Id, (4) is consistent with Ψ j64=Id. Using Dρ rather than Bρ in (4) would give 4Ψ, revealing the same missing factor.

## 4. Root character, orientation and regularity

The volume Ω has deck character χ. Hence multiplication by Ω sends χ-valued functions to Δ-invariant top forms. The scalar root line in the carrier has already cancelled in End; its signs cannot be used to change the coefficient normalization.

For one smooth root double cover h:C→P¹, the odd function line is O(-2). Multiplication by the chosen nowhere-vanishing elliptic one-form turns odd functions into invariant one-forms. The normalized canonical trace (1/2)Tr_h^ω is the inverse of ordinary pullback on invariant forms. Taking four external products proves that Dρ is a regular coefficient isomorphism from the all-four-odd coefficient to q*B0⊗ω_Z. This also follows directly from exact finite-group invariants and the finite-duality dual of the Δ-Reynolds projector.

An elementary local check at a simple branch point makes the absence of poles explicit. With x=u², the odd functions are u a(x), invariant one-forms are u a(x)du, and dx=2u du. Pullback and normalized trace therefore identify invariant forms with forms downstairs without division by u. The product argument covers intersections of branch factors. This local calculation is only a universal check of the sheaf map; it is not an actual-source evaluation.

Under factor permutations, Ω transforms by sgn(g), in addition to the ordinary action on its coefficient functions. Naturality of canonical trace consequently gives

    Dρ(g·f)=sgn(g) g·Dρ(f).

Thus Dρ is equivariant after the canonical recipient is twisted by permutation sign. The ordinary all-odd line on Z is Aline^(-2), where Aline=q*O_Y(1), whereas

    ω_Z = Aline^(-2)⊗sgn.

This is exactly PR387/419's sign conversion. The K-sign source becomes K-invariant canonical forms, and block exchange (13)(24) is even. Exchanging the two surface volume factors has sign (-1)^(2·2)=+1. No additional minus sign or mixed factorial appears.

To obtain an E-valued cochain, E=q*B0⊗Aline^(-2), use PR387's fixed underlying binary-volume identification a:E→q*B0⊗ω_Z. Define R0=a^(-1)R0^ω and j0=a^(-1)j4. No choice of an unrelated scalar line identification is silently substituted. Keeping determinant/volume lines throughout gives the same result before fixing them.

## 5. Construct the source representative without evaluating it

A trace of a cochain can be taken literally only when its sections are defined on the appropriate full inverse-image opens. Do not apply (2) entrywise to unrelated physical root-chart intersections.

Choose a finite affine cover {U_i} of Y. Its pullbacks to X,Z,T are affine, and their finite intersections are affine, since the maps are finite and the spaces separated. These covers compute the cohomology of the relevant locally free coefficients. They are stable under the deck and permutation groups. A common regular affine refinement with the given source cover gives quasi-isomorphisms of Čech complexes. In particular the admitted source class [eχRraw] has a regular cocycle representative R̃raw on the T pullback cover.

This claim does not require surjectivity of a chosen cochain refinement map. Both covers compute the same derived global sections; their common refinement identifies their cohomology. Choose a cocycle on the quotient-adapted cover whose class maps to the given source class. The two cocycles differ by a boundary after comparison. Averaging this representative with eχ makes it pointwise χ-valued and preserves its class and closedness.

Now define, on that quotient-adapted cover,

    R0^ω=Bρ(R̃raw)=(1/64)Tr_ρ^ω(Ω R̃raw),
    R0=a^(-1)R0^ω.                                  (5)

All maps in (5) are regular sheaf maps and commute with δ. Therefore R0 is a closed regular E-valued 2-cochain. It is constructed from the same actual complete raw class, not defined tautologically as j0(C). Applying (2) to the input equality (1) proves

    [R0]=j0(C).                                      (6)

Different choices of quotient-cover representative change R0 by a regular boundary. This is an existence and cohomological construction. It does not give a closed formula for the physical frame-transfer cochain or certify an implementation of that transfer.

For precision about the comparison boundary, choose a regular corrected cocycle c representing C on the X cover. On the T cover there is a regular 1-cochain b such that

    R̃raw-j64(c)=δb.

Project b to χ if necessary. Then β=Bρ(b) is regular and

    R0^ω-j4(c)=δβ.                                   (7)

Equation (7) explicitly locates the boundary that weighted primitive arguments must retain. It asserts its existence from the already proved class equality; it does not claim that its coefficients have been computed.

## 6. The next useful consequence: normalized weighted transport

For any global weight w∈H⁰(X,m*O_Y(d)), use the same construction in twist d. Projection formula and R-linearity of res_ρ give

    Bρ,d((ρ*p*w)f)=(p*w)Bρ,0(f).

Together with PR387's proven weight and projector identities this gives

    e_sign[(p*w)R0]
      = j_d i_d(Tr_m^ω(wC)).                         (8)

The sign is in PR387's ordinary E convention. For a representative comparison (7), multiplication and averaging carry its boundary to δ[e_sign((p*w)a^(-1)β)]. The coefficient of the right side of (8) is exactly one. The degree-six divisor belongs to i_d, not to the evaluation Tr_m^ω(wC).

For the naturally descended, unrescaled raw representative Rnat=a^(-1)Dρ(R̃raw), the correct formula instead is

    [Rnat]=4j0(C),
    e_sign[(p*w)Rnat]=4j_d i_d(Tr_m^ω(wC)).           (9)

Thus vanishing tests are unchanged by this nonzero scalar, but exact values and primitive-comparison formulas must use (8) or (9) consistently. This applies to the global σ and τ of the weighted papers, with their stated section normalizations.

## 7. Precisely what is and is not resolved

Resolved under the imported exact source premises:

- The full degree-64 source-band inclusion factors through the degree-16 deck pushforward and the distinct degree-four normalized-dual-trace inclusion.
- The factor is explicitly four for natural deck descent, and exactly one after the stated rescaling.
- A closed regular representative of the complete raw class in the weighted recipient exists, with [R0]=j0(C), and its regular comparison boundary transports through weights and projectors.

Not resolved:

- No I_D⁷E or historical I_D¹²E representative is produced. Multiplication by a nonzero constant preserves ideal membership if it has separately been proved; it cannot create it.
- The equality (6) belongs to the representative constructed from this source. If a different high-order candidate is proposed later, its class must still be compared to [R0]; one cannot combine this equality with ideal membership of an unrelated cocycle.
- No unweighted or weighted primitive, actual retained value, pure-square result, module lift, higher-order quantization or algebraicity is inferred.
- An earlier source's division by y1y2y3y4 and its “stated constant frame normalization” cannot be identified with (5) without reading and comparing that exact coefficient map. The PR387 R0 is a hypothetical high-order representative, not an independently defined physical output that can be matched by notation.
- All original source/localization/regularity/marking premises remain. This argument composes them; it is not an implementation or source-runtime certificate.

This resolves the coefficient-to-class comparison with an explicit normalization; it does not claim the earlier full-source theorem was absent or assign a new obstruction value.
