# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 07 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# Simple-pole cofactor comparison and its secondary obstructions

Work over C on Y=P4. Write B=End_0(F), self-dual by the trace pairing, and let Δ define the degree-six binary-quartic discriminant D. Denote its normalization by ν:ṼD=P1×P2→D. All groups are on Y unless indicated. Imported verified facts are H2(B(t))=0 for t≥2, h2(B(-4))=10, h2(B)=2, and h2(B(1))≤30. No vanishing at t=1 is assumed. Constant weight lines may be tensored throughout.

## 1. The exact comparison diagram

Let K=B(-4), P=B(2), C=4B(1), U=5B, L=P|D and M=ν_*ν*L. Write the normalization presentation as R_mat=(b;A):U→P⊕C. Its unit kernel is j:K→U, whose entries are the signed quartic maximal minors of A. Choose their common scalar so that b j=Δ; then A j=0. There is a commutative diagram with exact rows:

    0 → K --Δ→ P       → L → 0
        j↓      incl↓    n↓
    0 → U --R_mat→ P ⊕ C   → M → 0.

Thus with positive Čech connecting homomorphisms,

    δ_M n_1 = α ∂,       α=H2(j):H2(K)→H2(U).              (1)

This is a ten-dimensional to ten-dimensional map. It is not a computed 10×10 matrix or an asserted rank. To check the sign directly, lift an L one-cocycle s to a P one-cochain p. Write dp=Δ k. Then d(p,0)=R_mat(jk), so both sides of (1) equal [jk], with no minus sign.

Let T=H2(K), I=im[H1(P)→H1(L)], and J_P=im[H1(P)→H1(M)]. Since H2(P)=0, ∂ induces an isomorphism H1(L)/I≅T. Naturality induces

    f:T→Nbar:=H1(M)/J_P.

The cohomology of the lower row gives the exact sequence

    0 → E → Nbar --δbar→ ker β → 0,                     (2)
    E=coker[H1(A):5H1(B)→4H1(B(1))],
    β=H2(A):5H2(B)→4H2(B(1)).

For clarity, quotienting by the P image turns the image of H1(P⊕C) into H1(C)/pr_C im H1(R_mat); this is exactly E, not automatically 4H1(B(1)). No injection of H1(P) into either H1 group is claimed. The right term is ker β, not all 5H2(B). Its target has dimension at most 120, but need not vanish. Equation (1) becomes

    δbar f=α,       im α⊂ker β.                          (3)

In particular invertibility of α, if ever proved, would force β=0; it would not force H2(B(1))=0.

## 2. The precise secondary invariant

On ker α, equation (2) defines a canonical map

    ζ:ker α→E,       ζ(x)=f(x) viewed in E.              (4)

This requires no splitting of (2). Explicitly, for a representative s and p as above, if α([k])=0 choose a U one-cochain u with du=jk. Then

    v=(p,0)-R_mat u

is a closed (P⊕C) one-cochain. Modulo the P image, its C component is -A u, and

    ζ([k])=[-A u] in coker[H1(A)].                      (5)

Changes in p, s and u change this expression only by the displayed quotient relations. Formula (5) also records the correction minus sign. Nonzero α(x), or α(x)=0 with ζ(x)≠0, proves x≠0. Their simultaneous vanishing says only f(x)=0: normalized principal parts can be killed after an allowed closed P correction. It does not yet establish a regular primitive.

## 3. The remaining conductor obstruction and its sign

Let Q=L⊗(ν_*O_ṼD/O_D), so 0→L→M→Q→0. The normalization quotient presentation is

    0 → K --j→ U --A→ C → Q → 0.                       (6)

Let γ:H0(Q)→H1(L) be the conductor connecting map and κ=∂γ:H0(Q)→T. Exactness and the P-image quotients imply

    ker f=im κ=ker ζ,                                  (7)
    0 → im κ → ker α --ζ→ E

is exact (no surjectivity onto E is asserted). Indeed if n_1 ξ is an image from H1(P), subtract that same P image from ξ; the result lies in ker n_1=im γ. Conversely every γ class normalizes to zero.

The two-step connecting map d2:H0(Q)→H2(K) from (6) has the opposite sign from κ under the following explicit convention. Lift q to a C zero-cochain c, choose u with dc=A u, and write du=j k. Define d2(q)=[k]. The normalized lift of q is a=image(0,c). Its differential is image(0,A u)=image(-b u,0), so γ(q)=[-b u mod Δ]. Since d(-b u)=-Δ k,

    κ=-d2.                                             (8)

This distinguishes the plus naturality sign in (1) from the minus two-step/conductor comparison sign. In particular im d2⊂ker α without any rank assumption.

The exact remaining finite space is

    im κ ≅ H0(Q) / γ^{-1}(I),                           (9)

where γ^{-1}(I) contains im H0(M). Equivalently it is

    (H0(Q)/im H0(M)) / γbar^{-1}(I∩im γ).

Here γbar identifies H0(Q)/im H0(M) with im γ. Formula (9) retains both the global normalized-section ambiguity and the allowable closed-P ambiguity.

For a specified polar class x, if α(x)=ζ(x)=0, choose ξ representing x and a closed P correction so that the adjusted ξ normalizes to zero. Choose a normalized primitive a for an adjusted L cocycle s. Its quotient q=dsc(a) is a global Q section, with γ(q)=ξ_adj, the corrected representative class. The final criterion is q∈γ^{-1}(I), equivalently [q]=0 in (9). This is precisely x=0. The choice of correction, representative, and normalized primitive changes no class in (9).

Scheme-theoretically this uses the already established conductor Z=N∪W downstairs and E_cond=2R+S upstairs. The quotient Q is ν_*(ν*L|E_cond)/(L|Z), with the conductor-square maps. At the quadruple-root locus it retains the tangency R∩S and cannot be replaced by separate generic cusp and double-branch tests.

## 4. Transpose identity and a structural conductor criterion

Serre duality on P4 and trace self-duality identify the transpose of α as

    α*:5H2(B(-5))→H2(B(-1)),
    (η_i)↦Σ_i j_i η_i.                                (10)

Both spaces have dimension ten. This is the transpose, not an inverse or a duality trace divided by a degree. The sign is fixed by

    <j x,η> = <x,j^T η>.

Multiplication by quartics has degree zero and both cohomology degrees are two, so no Koszul sign is introduced. The dual of β is the compatible A^T map 4H2(B(-6))→5H2(B(-5)); α*β*=0. Any basis changes or common cofactor scalar must be made compatibly in the comparison diagram.

There is a geometric next reduction without evaluating this matrix. Let I_Z⊂O_Y be the reduced conductor ideal. Hilbert–Burch and the cofactor orientation give

    0→4B(-6) --A^T→5B(-5) --j^T→C_Z→0,
    C_Z=B(-1)⊗I_Z,
    0→C_Z→B(-1)→B(-1)|Z→0.                           (11)

The first exact sequence follows by tensoring the verified conductor ideal resolution by B(-1). Let h:H2(C_Z)→H3(4B(-6)) be its connecting map, let a:H1(Z,B(-1)|Z)→H2(C_Z) be the second sequence's connecting map, and let r:H2(B(-1))→H2(Z,B(-1)|Z) be restriction. Put

    V_Z=ker[H3(4B(-6))→H3(5B(-5))] / im(h a).

For η∈ker r choose a lift θ∈H2(C_Z), and define t(η)=[hθ]∈V_Z. This is well-defined because lift changes are im a. Exactness proves

    im α* = {η∈ker r : t(η)=0}.                        (12)

Proof: a lift θ comes from H2(5B(-5)) exactly when hθ=0; if hθ lies in im(h a), change θ by a class in im a to arrange this. The reverse direction is immediate. Thus invertibility of the square α is equivalent to r=0 and t=0 on all H2(B(-1)). These are conductor-restriction and Hilbert–Burch lift conditions, not assumptions of their vanishing. The uncomputed H3 terms in (11) are dual to H1(B(1)) and H1(B), matching the secondary terms already present in (2). This provides a structural next target on the conductor surface, with no claim that mere support or dimension proves the criterion.

The criterion also gives a canonical exact sequence

    0→V_Z→coker α*→im r→0.                            (13)

Here t is surjective onto V_Z: h is surjective onto its stated kernel by the Hilbert–Burch long exact sequence, and every θ maps to an η∈ker r. Thus V_Z is identified with ker r/im α* by (12). In particular the dual of the primary invisible space ker α has exactly this conductor-restriction/lift filtration. The dimension identity dim ker α=dim V_Z+dim im r is formal, not a numerical rank calculation.

## 5. A quantitative exclusion of dropping the conductor lift changes

The independently verified primary HM table gives h1(B)=24 and H1(B(k))=0 for k≤-2; stability of F gives H0(B(k))=0 for k<0. Thus by Serre duality H3(B(1))=H4(B(1))=0. The previously derived Riemann–Roch polynomial is

    χ(B(t))=3 binom(t+4,4)−(15/2)t²−(75/2)t−25.

Consequently

    h1(B(1))=55+h0(B(1))+h2(B(1))≥55.

Let W_Z=ker[4H3(B(-6))→5H3(B(-5))], the numerator defining V_Z. By Serre duality and the rank bound by target dimension,

    dim W_Z≥4h1(B(1))−5h1(B)≥220−120=100.

Since V_Z injects into coker α*, whose dimension is at most ten, the lift-change map satisfies the unconditional formal lower bound

    rank(h a)=dim W_Z−dim V_Z≥90.                    (14)

More precisely it is at least 90+4h0(B(1))+4h2(B(1)). This does not compute its actual rank. In particular the image of the conductor H1 lift changes cannot be discarded or set to zero: it removes at least ninety dimensions from the raw Hilbert–Burch obstruction space.

There is an even stronger lower bound for the size of the source of those lift changes. Put G_Z=B(-1)|Z. The four-term exact sequence obtained from (11) gives

    χ(G_Z)=χ(B(-1))−5χ(B(-5))+4χ(B(-6))
          =5−5(-22)+4(-55)=−105.

Because G_Z is supported on the projective surface Z, its cohomology above degree two vanishes. Hence

    h1(Z,G_Z)=105+h0(Z,G_Z)+h2(Z,G_Z)≥105.           (15)

The lower bounds (14) and (15) are distinct: the first concerns the image of the composed lift-change map; the second concerns its domain. Neither identifies its kernel or proves α invertible. These follow from the verified HM table, Riemann–Roch, and exactness alone, with no actual matrix or source evaluation. Primary-table provenance and the polynomial derivation are recorded in ../hm_primary_source_verification.md and ../fourth-power-cohomology/PROOF.md, Sections 1–2.

## 6. Relationship to regular reconstruction

If the first weighted source has a simple-pole primitive p, its polar class maps under ∂ to the original first retained class. It has a regular primitive exactly when x=0; subtracting a closed meromorphic P one-cochain is allowed and accounts for I. The present comparison cannot eliminate the independent twenty-dimensional second coordinate. Even if both are eventually proved zero, the source-to-model comparison and mixed correction still have the established signs: a raw-source primitive is corrected by subtracting the comparison boundary, and for D=D_model+dh the module correction is -h-H_model. No cofactor sign changes those statements.

## Scope
