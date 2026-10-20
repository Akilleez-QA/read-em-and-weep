# Component, double-conic, and cofactor detector filtration

## 0. Result and scope

Work over C on Y=P^4. Set B=End_0(F), G=B(-1), Z=N∪W, and E=N∩W=2C inside W=P^2. All these schemes and the Hilbert–Burch presentation are the ones verified in the dependencies below. Degrees written on C refer to C=P^1; O_Y(1)|C=O_C(4), whereas O_W(1)|C=O_C(2).

Let

    A=H^2(Y,G),  J=im α*,  Q=A/J,

where α*:5H^2(B(-5))→A is the cofactor transpose. Both its domain and A have dimension ten. We construct a canonical filtration of Q with successive pieces

    V_Z,   im β_nil,   im β_red,   im r_comp.             (0.1)

Here β_red is defined only on the kernel of component restriction, β_nil only on the further kernel of reduced-conic gluing, and V_Z is the full Hilbert–Burch lift quotient. No complement is chosen. In particular this is not a splitting into four independently defined ambient maps. The nilpotent gluing test has an explicit dual detector space, cut out by the component H^1 maps and by actual extension across the ribbon. Sections on C cannot be freely substituted for these detectors.

The exact dimension consequence is

    dim ker α = dim V_Z + rank β_nil + rank β_red
                + rank r_comp ≤ 10.                     (0.2)

The ranks here remain unevaluated. The paper also gives a necessary and sufficient cochain algorithm, including the ambiguity in each choice. It uses no source instance, HM matrix, selected rank evaluation, or large computation.

## 1. A second filtration inside the gluing cokernel

Write

    L=B_C(-8),  M=B_C(-4),
    0→L --ι→ G_E --π→ M→0,                             (1.1)
    ε:H^0(M)→H^1(L).

Retain the actual ribbon sequence; E has no global retraction onto C. Let

    P_1=H^1(G_N)⊕H^1(G_W),
    v_1:P_1→H^1(G_E),    v_1(z_N,z_W)=z_N|E-z_W|E,
    I=im v_1,   U=ker[H^1(G_E)→H^1(M)].

Since L is supported on a curve, H^2(L)=0. Consequently

    U≅H^1(L)/im ε,
    D_E=H^1(G_E)/I,
    D_red=H^1(M)/π_*(I),
    D_nil=U/(U∩I)
         ≅ H^1(L)/ι_*^{-1}(I).                         (1.2)

These give a canonical short exact sequence

    0→D_nil→D_E→D_red→0.                               (1.3)

Proof: π_* is surjective, and the kernel of the induced quotient map is (U+I)/I, canonically U/(U∩I). This retains both kinds of relations: ε from lifting through the ribbon, and component H^1 relations whose reduced difference vanishes in cohomology. In particular the nilpotent quotient is not obtained by merely quotienting H^1(L) by ε.

More computationally, with

    P_1^0=ker[π_*v_1:P_1→H^1(M)],

one has U∩I=v_1(P_1^0), so

    D_nil≅coker[P_1^0 --v_1→ U].                        (1.4)

No choice of component primitive or normal coordinate enters these definitions.

## 2. The ambient filtration and its exact quotients

Mayer–Vietoris for the scheme intersection is

    0→G_Z→G_N⊕G_W --v→G_E→0.

Because H^2(G_E)=0, its connecting map embeds D_E into H^2(G_Z), and yields

    0→D_E --∂→H^2(G_Z)
      →H^2(G_N)⊕H^2(G_W)→0.                           (2.1)

Let r:A→H^2(G_Z) and r_comp=(r_N,r_W). Define

    A_1=ker r_comp.

For η∈A_1, the class r(η) lies in the embedded D_E; write

    β_E:A_1→D_E,    ∂β_E(η)=r(η),
    β_red:A_1→D_red,
    A_2=ker β_red.

On A_2, β_E has values in D_nil; denote the resulting map by β_nil. Finally set

    A_3=ker β_nil=ker r.

The established cofactor criterion supplies a surjection

    t:A_3→V_Z,   ker t=J,
    V_Z=ker[4H^3(B(-6))→5H^3(B(-5))]/im(h a),           (2.2)

where a and h are the positive connecting maps for

    0→GI_Z→G→G_Z→0,
    0→4B(-6) --A^T→5B(-5) --j^T→GI_Z→0.

Hence

    J⊂A_3⊂A_2⊂A_1⊂A

induces the canonical filtration

    0⊂A_3/J⊂A_2/J⊂A_1/J⊂Q,                           (2.3)

with identifications

    A_3/J≅V_Z,
    A_2/A_3≅im β_nil,
    A_1/A_2≅im β_red,
    A/A_1≅im r_comp.                                  (2.4)

This proves (0.1)–(0.2), since dim Q=dim ker α for a square map and its transpose. It also refines the conductor-restriction term exactly:

    rank r = rank r_comp + rank β_red + rank β_nil.     (2.5)

It is possible that D_nil is nonzero but β_nil=0, or that all ribbon cohomology directions are killed by I. The ambient filtration deliberately records only the actual ambient images.

A useful strengthened constraint on the mandatory lift relations follows. Write

    W_Z=ker[4H^3(B(-6))→5H^3(B(-5))], R=im(h a),
    c=rank r_comp, g=rank β_red, n=rank β_nil.

Using dim W_Z≥100+4h^0(B(1))+4h^2(B(1)) and

    dim V_Z=10-rank α-c-g-n,

we obtain the exact identity and its lower bound

    dim R=dim W_Z-10+rank α+c+g+n
         ≥90+4h^0(B(1))+4h^2(B(1))+rank α+c+g+n.        (2.6)

Thus every proved independent component or gluing obstruction forces an additional mandatory lift relation, beyond the earlier uniform lower bound. This does not supply any positive value for c, g, n, or rank α.

The internal lift ambiguity also retains its global-section layer. Set

    D_0=coker[H^0(G_N)⊕H^0(G_W)→H^0(G_E)],
    K_1=ker v_1, λ=h a,
    R_0=im[λ∂:D_0→W_Z].

The exact sequence 0→D_0→H^1(G_Z)→K_1→0 induces

    λbar:K_1→W_Z/R_0,
    V_Z≅(W_Z/R_0)/im λbar,
    im λbar≅R/R_0.                                   (2.7)

Thus the final obstruction never uses a preferred lift of a compatible component H^1 pair. Such lifts differ by D_0, and their λ-values differ by precisely R_0. Since dim R_0≤dim D_0≤h^0(G_E)≤30, (2.6) sharpens the previously known compatible-component relation bound to

    dim im λbar≥60+4h^0(B(1))+4h^2(B(1))
                   +rank α+c+g+n.                    (2.8)

One may replace the subtraction of 30 in this estimate by the actual dim R_0 or by the upper bound dim D_0. These are symbolic constraints, not evaluated ranks.

## 3. Dual detectors: actual ribbon sections with component constraints

The ribbon E is a Cartier plane quartic and is Gorenstein. Adjunction on W gives

    ω_E=O_E(1)                 (plane twist),
    G_E=B_E⊗O_E(-2),
    H_E=G_E^∨⊗ω_E≅B_E⊗O_E(3).                        (3.1)

The last identification uses trace self-duality of B. Serre duality for the proper Gorenstein curve E gives H^1(G_E)^∨=H^0(H_E). Define

    T_E=ker[v_1^∨:H^0(H_E)→P_1^∨].                    (3.2)

Then D_E^∨=T_E canonically: its sections annihilate the entire component H^1 image, not just the reduced image. Component duality can make the target explicit:

    P_1^∨=H^1(N,B_N(1))⊕H^1(W,B_W⊗O_W(-1)).           (3.3)

Here N is Gorenstein with ω_N=O_N, W has ω_W=O_W(-3), and the twist (1) on N is ambient. Any connecting-map sign in the dual presentation leaves the annihilator (3.2) unchanged; the pairings themselves below use (3.2) as their definition.

The canonical dual ribbon sequence is

    0→M^∨ω_C=B_C(2)→H_E --q→L^∨ω_C=B_C(6)→0.          (3.4)

This is a sequence of sheaves on E, with both end terms pushed forward from C. For clarity, the kernel is I_{C/E}H_E: its degree on C is -4+6=2, and the quotient is H_E|C of degree 6. These agree with duality for (1.1), which reverses the two end terms. No O_C-module splitting of H_E is used.

Set

    T_red=T_E∩H^0(B_C(2)),
    T_nil=q(T_E)⊂H^0(B_C(6)).                          (3.5)

Then canonical duality yields

    T_red=D_red^∨,
    T_nil=D_nil^∨,
    0→T_red→T_E --q→T_nil→0.                           (3.6)

For the second identification, dualizing U=H^1(L)/im ε embeds U^∨ into H^0(B_C(6)). The map q on sections is the transpose of ι_* under Serre duality. Thus q(T_E) is precisely the annihilator of U∩I inside U^∨. Equivalently, extend a functional on U annihilating U∩I to H^1(G_E) while making it vanish on I. Such an extension exists by finite-dimensional linear algebra; it corresponds to a section in T_E. Its ambiguity is exactly T_red.

In particular any t∈T_nil must satisfy BOTH:

- t extends to a section of H_E (the connecting map from (3.4) kills t);
- at least one such extension annihilates im v_1.

The first is the annihilator-of-im-ε condition. The second is an additional component condition and cannot in general be read off from C alone. Neither all H^0(B_C(6)) nor merely the kernel of its extension boundary is the correct nilpotent detector space.

The actual ambient detectors are

    β_red^∨:T_red→A_1^∨,
    β_nil^∨:T_nil→A_2^∨.                               (3.7)

Their images are canonically (im β_red)^∨ and (im β_nil)^∨. They have no preferred extensions to all of A^∨. Concretely a section of T_E supplies a functional on A_1 by pairing with β_E; on A_2 its value depends only on its image in T_nil. Therefore

    0→im β_red^∨→im β_E^∨→im β_nil^∨→0                (3.8)

is exact, where the last arrow is restriction from A_1^∨ to A_2^∨. The proof is the annihilator identity for A_2=ker β_red; extensions of functionals on im β_E give the converse. In particular (3.8) concerns actual ambient detector images, not the possibly much larger full spaces T_red and T_nil.

There is also an exact dual filtration on ker α=Q^∨: the annihilators of A_i/J have successive quotients, in reverse order, (im r_comp)^∨, (im β_red)^∨, (im β_nil)^∨, and V_Z^∨. This identifies all four detector layers without selecting a splitting.

## 4. Explicit cochain construction and necessary/sufficient criterion

Use an affine acyclic cover of Y and its restrictions to the closed subschemes. Coherent sheaf sequences are sectionwise exact on each affine intersection, so every cochain lift below exists. Write d for the Čech differential, and use the positive connecting convention ∂[s]=[d(lift s)].

### Step 1: component primitives

Represent η∈A by a G-valued closed two-cochain x. The first test is

    dp_N=x|N,   dp_W=x|W                              (4.1)

for regular one-cochains p_N,p_W. Such primitives exist exactly when r_comp(η)=0. Define

    t_E=p_N|E-p_W|E.

Then dt_E=0. Its class in D_E is β_E(η), because the lift (p_N,p_W) has differential (x|N,x|W). The sign is positive.

### Step 2: reduced-conic matching

The second test is

    [π t_E]∈im[π_*v_1:P_1→H^1(M)].                    (4.2)

Equivalently choose a closed pair of component one-cochains z=(z_N,z_W) and a zero-cochain e of M such that

    π(t_E-vz)=de.

Lift e to an E zero-cochain e_E. The closed cochain

    s=t_E-vz-de_E

has πs=0, hence has a unique expression s=ιℓ for an L-valued one-cochain ℓ. Since ι is injective, dℓ=0. Its class

    [ℓ] modulo ι_*^{-1}(I) ∈ D_nil                    (4.3)

is β_nil(η). Different choices of z, e, and e_E alter this class only by the denominator in (4.3). This follows either from (1.3) or directly: changes are closed E cochains whose classes differ by I, and which land in U, so their L classes differ by ι_*^{-1}(I). Changes of lift of a global M section account for im ε inside that denominator.

For a nilpotent detector τ∈T_nil choose σ∈T_E with qσ=τ. Its value is

    ⟨β_nil(η),τ⟩ = ⟨[t_E],σ⟩_E
                   = ⟨[ℓ],τ⟩_C.                    (4.4)

The component correction vz pairs to zero with σ, and de_E is a coboundary. Changing σ by T_red pairs to zero because η∈A_2. Changing ℓ by the denominator in (4.3) pairs to zero by (3.6). This constructs actual well-defined detectors; the equality fixes the duality-compatible convention without an arbitrary transverse derivative.

### Step 3: first-order matching and a primitive on Z

The third test is

    [ℓ]∈ι_*^{-1}(I),                                 (4.5)

equivalently β_nil(η)=0. Together with step 2, this means [t_E]∈I. Choose a closed component pair z' with [vz']=[t_E], so

    t_E-vz'=df_E

for an E zero-cochain f_E. Lift f_E to a component zero-cochain pair f=(f_N,f_W), using the sheaf-surjective difference map v. Replace the component primitives by

    (p_N,p_W)-z'-df.

Their differentials remain (x|N,x|W), and their difference on E is zero. They glue to a regular one-cochain p_Z of G_Z with

    dp_Z=x|Z.                                         (4.6)

Conversely any such p_Z makes both gluing tests vanish. Matching only on C would not justify (4.6).

### Step 4: the Hilbert–Burch lift ambiguity

Lift p_Z to a G one-cochain p. Then

    θ=x-dp

is a GI_Z-valued closed two-cochain. Lift θ through j^T to a two-cochain u of 5B(-5). Since j^Tdu=dθ=0, there is a unique three-cochain w of 4B(-6) satisfying

    A^T w=du.

Injectivity of A^T gives dw=0, and its class lies in W_Z. The final test is

    [w]=0 modulo R=im(h a),                            (4.7)

that is t(η)=0 in V_Z. Changing p_Z by a closed z_Z changes [θ] by -a[z_Z] and [w] by -h a[z_Z]. Thus exactly R, rather than zero or an arbitrarily smaller quotient, is the lift ambiguity. Ordinary changes of cochain lifts add coboundaries or the usual exact-sequence indeterminacies and do not change the class in V_Z.

If (4.7) holds, choose a closed z_Z with h a[z_Z]=[w] and replace p_Z by p_Z+z_Z. Lift this change to p; the new [w] is zero. Write w=dv for a two-cochain v of 4B(-6). Replacing u by u-A^T v makes du=0 without changing j^Tu=θ. Consequently

    x=j^T u+dp,   du=0,                               (4.8)

and η∈im α*. Conversely (4.8) implies all four tests, choosing p_Z=p|Z and θ=j^Tu. Thus the four-stage criterion is necessary and sufficient, not only a list of necessary obstructions.

If η changes by an ambient coboundary dR, add R|N,R|W to the component primitives. Their E difference is unchanged. At the last step change p by R, leaving θ unchanged. This verifies independence from the original representative as well.

## 5. Bounds and safeguards

Let B_C=O⊕O(d)⊕O(-d), with d∈{0,2,…,20}; put a_d=max(d-7,0), t_d=max(d-3,0), and ρ=rank ε. Imported line-bundle cohomology gives

    dim U=21+a_d-ρ≥17,
    h^1(M)=9+t_d,
    h^1(G_E)=30+a_d+t_d-ρ≤60.

The refined gluing dimensions are exactly

    dim D_nil=21+a_d-ρ-rank(v_1|P_1^0),
    dim D_red=9+t_d-rank(π_*v_1),
    dim D_E=dim D_nil+dim D_red.                       (5.1)

Thus at least seventeen ribbon directions exist before the component quotient, but there is no positive lower bound here for D_nil or rank β_nil. All four actual ambient obstruction dimensions share the single budget (0.2). In particular one cannot add a putative seventeen-dimensional obstruction to a ten-dimensional ambient space.

Full invertibility of α is equivalent to simultaneous vanishing of r_comp, β_red, β_nil, and V_Z. Each successive map is then defined on all of A because preceding tests vanish. For a single specified η, only its four successive tests need vanish; V_Z itself need not be zero.

No actual component restriction, gluing value, splitting type, cofactor rank, or retained source has been evaluated. The construction preserves the complete ribbon, its ε ambiguity, component H^1 relations, global primitive ambiguity, and Hilbert–Burch lift-change relations.

## Dependencies

- https://github.com/Akilleez-QA/read-em-and-weep/blob/21b252420c0011b2cbc119cab2983a6d4ad2e966/research/conductor-normalization/conductor-double-conic-intersection/PROOF.md and AUDIT.md: E=2C, ribbon, component Mayer–Vietoris, splitting bounds, relation filtration.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/21b252420c0011b2cbc119cab2983a6d4ad2e966/research/conductor-normalization/simple-pole-cofactor-comparison/PROOF.md: square cofactor transpose, surjective lift invariant t, mandatory relation bounds.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/f3f85ffc04213778c8c4fbd60e1e7e04b56cfd65/research/conductor-normalization/normalization-gysin-factorization/PROOF.md: the compatible pattern of restricting dual detectors to an already-invisible ambient subspace; used as a comparison, not to identify different twists or obstruction groups.
