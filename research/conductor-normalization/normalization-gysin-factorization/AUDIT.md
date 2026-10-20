# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: normalization, duality, and the cusp correction

## Verdict

The proposed universal factorization and cusp-correction theorem is correct. In particular:

1. The transpose of normalization pullback on top cohomology is the **dualizing trace**, whose image is the conductor. It is not an asserted trace homomorphism from normalized functions to singular functions.
2. The smooth-normalization contribution to the fourth-power Gysin image is precisely the restriction of the singular Gysin map to the order-two conductor subspace.
3. The remaining image is canonically the dual of the image of the residual restriction map into the cusp kernel. This is a quotient statement, not a preferred direct-sum splitting.
4. The dual cusp space is a kernel involving an H¹ group on the normalization. That group and its boundary map cannot be dropped.
5. The proposed Čech representative has the stated positive sign when the connecting homomorphism is defined by the differential of a lift.

No instance of a source, polynomial, monad map, rank, jet, or obstruction has been evaluated. The three specified local proof files and the resulting local PROOF.md draft were read. This audit writes only this local audit file; no external-service state was changed.

## 1. Setup and imported facts

Use the trace pairing to identify B with B∨. Put

    T = B(-4)|N,
    G = ν*T,
    A = H²(Y,B(-4)),
    V = H²(N,T),
    W = H²(S,G).

Write r:A→V for restriction, p:V→W for normalization pullback, r_S=pr, and K=ker p. The imported normalization sequence is

    0 → T → ν_*G → j_*Q → 0,
    Q = B_C ⊗ O_C(-18).

Because ν is finite and Q is supported on the curve C, its long exact sequence yields

    H¹(S,G) → H¹(C,Q) → V → W → 0.

Consequently p is surjective and

    K ≅ coker[H¹(S,G) → H¹(C,Q)].                  (1)

All isomorphisms used below come from these actual maps. The notation ω_N≅O_N and the identification A∨≅H²(Y,B(-1)) use the compatible trace, adjunction, and Serre-duality identifications already used in the fourth-power proof. Retaining ω_N explicitly until the final twists avoids any ambiguity from a scalar choice of its trivialization.

## 2. Finite duality and the conductor trace

For a finite map, duality identifies

    ν_*ω_S ≅ Hom_N(ν_*O_S,ω_N).

Under this identification the trace ν_*ω_S→ω_N is evaluation at 1. This is precisely the morphism dual to O_N→ν_*O_S. Projection formula then identifies the dual of T→ν_*G with

    ν_*(G∨⊗ω_S) → T∨⊗ω_N.                       (2)

The image of this map is its conductor subsheaf. This assertion can be checked directly, without confusing dualizing trace with trace on functions.

In the local product-cusp model

    A₀ = C[s,d²,d³] ⊂ R₀ = C[s,d],

every A₀-linear map R₀→A₀ extends over the common fraction field to multiplication by a rational function q. Its value at 1 is q, and the condition that its image lie in A₀ is exactly

    qR₀ ⊂ A₀.

Thus

    Hom_A₀(R₀,A₀) = d²R₀ = I_{C/N},

and evaluation at 1 is the inclusion d²R₀→A₀. Tensoring with the invertible ω_N gives

    ν_*ω_S ≅ I_{C/N}⊗ω_N ⊂ ω_N.                 (3)

For a differential check, if u=d² and v=d³, a residue generator of ω_N for v²-u³=0 is, up to the fixed orientation sign,

    ds∧du/(2v) = d^(-2) ds∧dd.

A regular generator ds∧dd on S is therefore d² times this pulled-back residue generator. Hence

    ω_S ≅ ν*ω_N ⊗ O_S(-2Δ).

In particular, after adjunction ω_N≅O_N,

    ω_S = O_S(-2,-2),
    G∨⊗ω_S = ν*B ⊗ O_S(10,2).

This also shows why the finite trace here cannot be replaced by a claim that arbitrary normalized functions descend: d belongs to R₀ but not A₀. The degree-one rational trace is not an O_N-valued trace on all of ν_*O_S.

By Serre-duality functoriality, the transpose

    p∨: W∨ → V∨

is H⁰ of (2). Thus it is exactly the conductor inclusion

    H⁰(S,ν*B⊗O_S(10,2))
      → H⁰(N,B(4)|N).

Writing δ_N=r∨ and δ_S=(r_S)∨, contravariance gives

    δ_S = δ_N p∨.                                (4)

Accordingly δ_N on the conductor subspace is precisely δ_S. There is no assertion that δ_N is determined by this subspace.

## 3. The dual cusp sequence and its retained H¹ boundary

The normalization sheaf ν_*G is maximal Cohen–Macaulay on N. This can be checked in the cusp model because (s,d²) is an R₀-regular parameter sequence, and tensoring with a locally free T preserves that property. Away from C the map is an isomorphism. Since N is Gorenstein of dimension two, this implies

    Ext¹_N(ν_*G,ω_N) = 0

as a sheaf. Also Hom_N(j_*Q,ω_N)=0, because the source is supported in codimension one and the target is locally free on the integral surface.

Dualizing the normalization sequence therefore gives the short exact sequence

    0 → ν_*(G∨⊗ω_S)
      → T∨⊗ω_N
      → Ext¹_N(j_*Q,ω_N) → 0.                    (5)

The curve C is Cohen–Macaulay of codimension one in the Gorenstein surface N. Closed-immersion duality, or the local cusp calculation of the preceding section, identifies

    Ext¹_N(j_*Q,ω_N) ≅ j_*(Q∨⊗ω_C).

Here ω_C=O_C(-2) and B_C∨≅B_C, so

    Q∨⊗ω_C = B_C⊗O_C(16).

After the same adjunction trivialization, (5) is the ordinary conductor ideal sequence tensored with B(4)|N:

    0 → ν_*(ν*B⊗O_S(10,2))
      → B(4)|N
      → j_*(B_C⊗O_C(16)) → 0.                    (6)

Let κ be its connecting map

    κ:H⁰(C,B_C(16)) → H¹(S,G∨⊗ω_S).

The start of the long exact sequence of (5), together with the dual of 0→K→V→W→0, now gives canonically

    K∨ ≅ V∨/p∨W∨
       ≅ ker κ.                                  (7)

In particular, it is incorrect in general to replace K∨ by the entire H⁰(C,B_C(16)). The boundary κ is the dual, with compatible connecting/Serre-duality sign conventions, of

    H¹(S,G) → H¹(C,Q).

Equivalently, (7) follows by dualizing the cokernel in (1). A different global sign convention for connecting morphisms can change the displayed adjoint comparison by a minus sign; it changes neither its kernel nor (7). One can avoid any sign ambiguity by defining κ directly as the boundary of (5) and using the induced Serre identifications.

No vanishing of H¹(S,G∨⊗ω_S) is available from the imported facts. Likewise, the positive-twist bound h¹(Q₄)≤5 has no application to this negative-twist restriction. Here the cusp term is Q=Q_{-4}, whose possible H¹ dimensions in the imported bound are 51, 52, or 54, before quotienting by H¹(S,G).

## 4. The canonical image quotient

Put

    E = ker r_S,
    β = r|E:E→K.

The target is K because p(r(e))=r_S(e)=0 for e∈E. Also

    ker r = ker β ⊂ E.                           (8)

For any finite-dimensional map f, im f∨ is the annihilator of ker f. Hence

    im δ_N = (ker r)^⊥,
    im δ_S = E^⊥,

as subspaces of A∨. Restriction of functionals A∨→E∨ maps im δ_N onto the annihilator of ker β in E∨. The latter is canonically (im β)∨ via the quotient E/ker β≅im β. Its kernel on im δ_N is exactly E^⊥=im δ_S. Thus

    0 → im δ_S → im δ_N → (im β)∨ → 0,           (9)

or, canonically,

    im δ_N / im δ_S ≅ (im β)∨.

Explicitly, for λ∈im δ_N the quotient functional is

    β(e) ↦ λ(e),    e∈E.

It is well defined because λ vanishes on ker r=ker β. Surjectivity follows by extending a linear functional from im β to V and applying r∨. This proof checks both canonicity and the direction of the dual; no choice of complement is used.

Taking dimensions gives the purely formal identity

    rank δ_N = rank δ_S + rank β.                 (10)

This does not evaluate any of the three ranks. The fourth-power ambient image is still ker r, so (8) locates it precisely as ker β inside ker r_S. In particular, normalization alone can enlarge the candidate kernel: the extra test is β=0 on an individual class.

## 5. Čech representative and sign

Choose an affine acyclic Čech cover on Y, restrict it to N, and pull it back along finite ν. These are acyclic covers for the coherent sheaves in the displayed sequences. Let c∈E and choose a closed ambient 2-cochain a representing c. Its restriction a_N represents r(c).

Because r_S(c)=0, there exists a 1-cochain P on S with values in G such that

    dP = ν*a_N.

Here P is simply a primitive on the normalization; no canonical choice or special gauge is needed. Let D be the quotient map ν_*G→j_*Q from the normalization sequence. It is the intrinsic first-normal-derivative quotient in pulled-back frames, not an arbitrary transverse derivative.

Then

    dD(P) = D(dP) = D(ν*a_N) = 0.

Thus D(P) is a Q-valued 1-cocycle. With the standard lift-boundary convention

    ∂[q] = [d(lift of q)],

its lift P satisfies

    ∂[D(P)] = [a_N] = r(c).

Consequently the canonical description (1) sends

    [D(P)] mod im H¹(S,G)

exactly to β(c), with a positive sign under the convention just specified.

Independence checks:

- If P is replaced by P+Z with dZ=0, the class [D(P)] changes by the image of [Z]∈H¹(S,G), which vanishes in the cokernel (1).
- If a is replaced by a+dh for an ambient 1-cochain h, take P+ν*(h|N). Its derivative quotient is unchanged because D kills sections pulled back from T. Any additional change of primitive is handled by the preceding point.
- Refining the cover commutes with all the maps and computes the same sheaf-cohomology connecting morphism.

The construction is therefore an intrinsic description of β, not an evaluation of β on any selected source.

## 6. Additional full-draft check: constructive descent and scalar pairing

The full PROOF.md draft was inspected after the independent derivation above. Its constructive improvement of the primitive criterion is valid. If β(c)=0, choose a closed one-cochain Z on S with [D(Z)]=[D(P)]. Then D(P-Z)=de for a Q-valued zero-cochain e. Affine degreewise surjectivity supplies a G-valued zero-cochain E lifting e. Therefore

    P′ = P-Z-dE

satisfies D(P′)=0 and dP′=ν*a_N. Degreewise exactness then supplies a unique T-valued one-cochain p_N with P′=ν*p_N, and injectivity implies dp_N=a_N. This proves actual descent of a corrected regular primitive, with no omitted cohomological obstruction.

The final pairing in the draft is also correct with its explicitly stated compatible convention. More intrinsically, let t∈ker κ be viewed as an element of K∨ by (7), and choose a lift s_N∈H⁰(N,T∨⊗ω_N). For c∈ker r_S,

    ⟨c,δ_N(s_N)⟩_Y = ⟨β(c),t⟩,

where the right side is the canonical K × K∨ evaluation. In the curve description it is represented by the Serre pairing ⟨[D(P)],t⟩_C. The equality follows from the compatibility of the lift boundary with dualizing the extension. Changing s_N by a conductor section changes the left side by zero, while changing P changes the curve class by im h, annihilated by t. Thus the stated scalar formula adds no extra choice and needs no additional sign caveat beyond the compatible duality/connecting convention already in the draft.

The full-draft stopping criteria and formal dimension bounds are consistent with (8)–(10); none evaluates a rank or implies a new positive lower bound.

## 7. Scope and final assessment

Every requested identity follows from the imported cusp normalization sequence, finite/Serre duality, and finite-dimensional linear algebra. The only bookkeeping cautions are to use dualizing trace rather than a nonexistent descent trace on arbitrary functions, keep the dual H¹ boundary, distinguish a primitive on S from a canonical chosen primitive, and synchronize the ordinary connecting sign convention. None requires a change to the proposed theorem.

Sources audited locally:

- ../nullcone-normalization/PROOF.md
- ../conductor-cohomology-bounds/PROOF.md
- ../fourth-power-cohomology/PROOF.md

- PROOF.md: full-draft check, especially §§3–4 and the constructive corrected primitive.
