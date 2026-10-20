# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 04 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# Normalization Gysin factorization and the exact cusp detector quotient

## Result and notation

Work over C. Put Y=P⁴, B=End₀(HM), i:N→Y the reduced triple-root (2,3) complete intersection, ν:S=P¹×P¹→N its normalization, and j:C≅P¹→N its quadruple-root curve. The diagonal Δ⊂S maps isomorphically to C. Set

    T=B(-4)|N,  G=ν*T=ν*B⊗O_S(-12,-4),
    Q=B|C⊗O_C(-18),  H=G∨⊗ω_S=ν*B⊗O_S(10,2),
    A=H²(Y,B(-4)), V=H²(N,T), W=H²(S,G),
    r:A→V, p:V→W, r_S=p r.

Here A has dimension ten, B is identified with B∨ by the trace pairing, and degrees on C refer to P¹, not the ambient hyperplane degree. The canonical fourth-power Koszul boundary is δ_N=r∨:V∨→A∨=H²(Y,B(-1)), with the compatible adjunction/Koszul convention from the preceding proof.

The restriction of δ_N to the guaranteed conductor subspace H⁰(S,H) is exactly the duality Gysin map

    δ_S=(r_S)∨:H⁰(S,H)→H²(Y,B(-1)).                       (1)

This is a map identity, not only equality of dimensions. The correct domain twist is (10,2), not (12,4).

Write

    K=coker[H¹(S,G) --h→ H¹(C,Q)],
    A₀=ker r_S,  β:A₀→K,

where K injects canonically into V via the normalization connecting homomorphism, and β is r on A₀ with its target restricted to K. Then there are canonical exact sequences

    0→ker r→A₀ --β→ im β→0,
    0→im δ_S→im δ_N→(im β)∨→0.                          (2)

Consequently

    rank δ_N = rank δ_S + rank β,
    dim im[H²(Y,B(-4)I_N)→A]
      = 10-rank δ_S-rank β = dim ker β.                  (3)

No splitting of (2) is claimed. The second sequence isolates the genuinely cusp-supported ADDITIONAL detector quotient: it consists precisely of the restrictions of N-detectors to the ambient classes already invisible on S. Merely taking all sections on C would overstate this quotient.

A regular Čech primitive on S gives a constructive representative for β: if c∈A₀ is represented by an ambient closed two-cochain z and dP=ν*r(z), then

    β(c)=[D(P)] modulo im h,                             (4)

where D:ν_*G→j_*Q is the intrinsic cusp derivative quotient. Thus an ambient class has a fourth-power representative exactly when its normalized restriction has a regular primitive P AND [D(P)] belongs to im h. Every primitive and H¹ indeterminacy is retained.

## 1. Finite duality identifies the conductor inclusion

Previous work proves the exact local model A_loc=C[s,d²,d³]⊂R=C[s,d], its conductor d²R=(d²,d³)A_loc, and globally

    I=I_{C/N}=ν_*O_S(-2Δ),
    0→O_N→ν_*O_S→j_*O_C(-2)→0.

Since N is Gorenstein with ω_N≅O_N, finite duality identifies

    ν_*ω_S = Hom_N(ν_*O_S,ω_N).

For completeness the local Hom identification is completely concrete. A linear map R→A_loc extends over the common fraction field to multiplication by an element a of that field. Evaluation at 1 shows a∈A_loc; the condition aR⊂A_loc says exactly that a belongs to the conductor. Conversely multiplication by every conductor element is such a map. Thus Hom_A_loc(R,A_loc)=d²R. Tensoring with a local generator of ω_N gives

    ν_*ω_S ≅ I⊗ω_N,
    ω_S ≅ O_S(-2Δ)⊗ν*ω_N = O_S(-2,-2).                 (5)

The second is the compatible dualizing identification on S, not a claim that ordinary differential pullback gives an isomorphism. Under finite duality, Tr_ν^ω is evaluation at 1 on Hom(ν_*O_S,ω_N). Under (5), it is precisely the inclusion Iω_N→ω_N. There is no scalar degree division, and no ordinary algebra-trace pairing is being substituted for the duality trace.

Tensor with T∨. Projection formula gives the sheaf map

    ν_*(G∨ω_S) --Tr→ T∨ω_N

as the conductor inclusion T∨Iω_N→T∨ω_N. Its section map

    J:H⁰(S,H)→H⁰(N,B(4)|N)

is therefore exactly the guaranteed descending inclusion already identified geometrically. Serre duality and its functoriality identify J with p∨.

The only general duality input here is natural perfect duality for proper Cohen–Macaulay schemes, and the finite-morphism Hom description of the right adjoint. The naturality statement is recorded in Stacks Project, Duality for proper schemes over fields, Remarks 48.27.3 and 48.27.6: https://stacks.math.columbia.edu/tag/0FVU . The finite right-adjoint formula is in its duality theory, https://stacks.math.columbia.edu/tag/0AU3 . The specific conductor calculation above verifies exactly what that abstract map is in this geometry.

## 2. Compatibility with the two-step Koszul boundary

The prior fourth-power proof identifies r∨ with the composite of the connecting maps from

    0→B(-1)→B(2)⊕B(1)→B(4)I_N→0,
    0→B(4)I_N→B(4)→B(4)|N→0.

Use its ordered equations of degrees 2 and 3 and the induced adjunction trivialization of ω_N. Functoriality of duality gives

    δ_N J = r∨ p∨ = (p r)∨ = δ_S.                       (6)

Equivalently, for x∈A and s∈H⁰(S,H),

    ⟨x,δ_N J(s)⟩_Y = ⟨r(x),J(s)⟩_N
                    = ⟨r_S(x),s⟩_S.

This pairing identity fixes the comparison without choosing cohomology bases. The map S→Y is not a closed immersion; δ_S here means the proper-duality transpose of restriction, equivalently the composite of finite trace and the codimension-two Gysin map for i. It is not an unjustified immersion Gysin construction on S. Changing the common Koszul orientation changes the chosen identifications by a common sign and leaves all images and criteria unchanged.

## 3. The exact cusp quotient, with H¹ retained

Tensor the normalization sequence by T:

    0→T→ν_*G --D→ j_*Q→0.

Because ν is finite and C is a curve, its cohomology gives

    H¹(S,G) --h→ H¹(C,Q) --∂→ V --p→ W→0.

Hence K=coker h embeds into V by ∂, with image ker p. This supplies β uniquely: ∂β(x)=r(x) for x∈A₀. In particular ker β=ker r.

The transpose J=p∨ is injective. To identify the detector quotient without choosing complements, restrict linear functionals on A to A₀. Every δ_S-functional restricts to zero. Conversely the annihilator of A₀ in A∨ is exactly im((r_S)∨)=im δ_S. Restriction on im δ_N therefore has kernel im δ_S. Its image is the transpose image of β: indeed every element of K∨ extends to V∨ (finite-dimensional linear algebra), and r∨ of such an extension restricts to β∨ of that element. The transpose image is canonically (im β)∨, embedded in A₀∨. This proves the second sequence in (2).

This is stronger than an unqualified normalization long exact sequence: it restricts the cusp correction to the actual ambient subspace ker r_S and identifies the exact quotient of the actual detector image. The full group K can be large even when β=0.

There is an equally exact section-side description. The conductor sequence, twisted by B(4), is

    0→ν_*H→B(4)|N→j_*(B|C⊗O_C(16))→0.

Set E_C=B|C⊗O_C(16), and let η:H⁰(C,E_C)→H¹(S,H) be its connecting map. Then

    K∨ ≅ H⁰(N,B(4)|N)/JH⁰(S,H) ≅ ker η.                (7)

One can also obtain this sequence by dualizing the normalization sequence. The finite normalization module is maximal Cohen–Macaulay over the Gorenstein surface N, so its positive sheaf Ext into ω_N vanishes. For the curve term, closed-immersion duality gives Ext¹_N(j_*Q,ω_N)=j_*(Q∨ω_C). Hence the dual sheaf sequence is exactly the conductor sequence, including its quotient E_C. This does not require C to be a Cartier divisor in N.

Under the natural Serre pairings, E_C=Q∨ω_C; the transpose of h is η up to the conventional common connecting sign. In particular its kernel is exactly the annihilator of im h. Thus no claim that every cusp section lifts to N, or that the preceding H¹ map vanishes, is needed. The genuinely additional cusp detector space is the image of

    ker η = K∨ --β∨→ A₀∨,                              (8)

not all of H⁰(C,E_C), and not necessarily all of K∨. Its kernel consists of the functionals annihilating im β.

The restricted-monad bound previously proved gives B|C≅O⊕O(d)⊕O(-d), d∈{0,2,…,20}. Therefore

    dim K = 51+max(d-17,0)-rank h ≤ 54,
    rank β ≤ min(10-rank δ_S, 51+max(d-17,0)-rank h).     (9)

Equivalently dim K=h⁰(E_C)-rank η. These are structural bounds with unevaluated maps; they do not claim a useful nonzero lower bound on fourth-power image or actual rank. The positive-twist bound 5 is inapplicable here.

## 4. Regular primitive and cusp-gluing test

Take an affine cover of Y, refine so the relevant bundles are locally free in chosen frames, and restrict it to N and pull it back to S. Finite preimages and intersections of these affine opens are affine. The resulting Čech complexes compute coherent cohomology on N,S,C; the short exact sequence above is degreewise exact because its sections are taken on affine intersections.

Let z be a closed two-cochain for B(-4) representing c∈A₀. Its normalized restriction is exact by the definition of A₀, so choose a regular one-cochain P of G with

    dP=ν*r(z).

Apply the sheaf quotient D. Since D kills sections pulled back from T, dD(P)=D(dP)=0. For the connecting convention ∂[q]=[d(lift q)], the lift of D(P) is P itself and its differential is r(z). Therefore ∂[D(P)]=r(c). This proves (4) with a positive sign for that convention.

If P is replaced by another primitive, their difference is a closed one-cochain of G. Its derivative changes [D(P)] by an element of im h, exactly the indeterminacy divided out in K. If z changes by an ambient coboundary dR, replace P by P+ν*r(R); D of the added term is zero. Refinements preserve the same cohomology class. The construction is thus independent of all representatives and allowed choices.

In local coordinates the quotient is componentwise ∂/∂d at d=0, with fixed s=(3a+b)/4. For bundle coefficients use frames pulled back from N: their transition matrices lie in C[s,d²,d³] and have zero first d derivative. This is why D is a genuine sheaf map and commutes with Čech differential. A freely chosen transverse derivative or arbitrary S-frame without transition corrections would not justify this calculation.

If β(c)=0, choose a closed one-cochain Z on S such that [D(Z)]=[D(P)]. Then D(P-Z)=de for some zero-cochain e of Q. Affine surjectivity of D lets one lift e to a zero-cochain E of G. Set

    P'=P-Z-dE.

Now D(P')=0 and dP'=ν*r(z). Degreewise exactness gives P'=ν*p_N for a regular one-cochain p_N of T. Injectivity implies dp_N=r(z). Conversely any such primitive on N pulls back to a P with D(P)=0. Thus (4) is a constructive descent-of-primitive criterion, not merely a dimension identity.

For t∈ker η, choose a section s_N of B(4)|N lifting t. For c∈A₀, the value of its additional detector is

    ⟨c,δ_N(s_N)⟩_Y = ⟨β(c),t⟩_C
                    = ⟨[D(P)],t⟩_C,

using the compatible duality/connecting convention. Changing s_N by a conductor section has zero pairing with c by (6). Changing P changes its derivative class by im h, which t annihilates by (7). This describes the cusp quotient as an actual well-defined pairing.

## 5. Exact stopping criteria and scope

- A class c has a fourth-power representative iff r_S(c)=0 and β(c)=0; β is only defined after the first condition.
- The fourth-power image is zero iff β is injective on ker r_S. In particular injectivity of r_S suffices, but is not necessary.
- The cusp adds no detector directions iff β=0, equivalently im δ_N=im δ_S.
- All ten classes have fourth-power representatives iff r_S=0 and β=0 (then β is defined on all A).
- No canonical direct-sum splitting between normalized and cusp detector images has been asserted.

The remaining task is the map-level behavior of normalized restriction and this regular primitive-gluing class. No actual source, polynomial instance, numerical rank, physical obstruction value, or monad map has been evaluated.  This resolves the map-compatibility dependency and isolates the genuine cusp test; it does not settle first-ten vanishing or the full retained thirty-condition problem.

## Dependencies

- ../nullcone-normalization/PROOF.md: normalization, conductor, intrinsic quotient, descent.
- ../conductor-cohomology-bounds/PROOF.md: guaranteed conductor subspace and restricted-monad bounds.
- ../fourth-power-cohomology/PROOF.md: fourth-power image, Koszul/duality comparison, ten-dimensional ambient space.
- AUDIT.md: fresh independent audit.
