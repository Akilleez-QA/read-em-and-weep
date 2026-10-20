# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 09 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# A bounded two-stage coordinate-syzygy detector for the degree-minus-one socle

## Result and scope

Let B=End₀(F) for the normalized stable Horrocks–Mumford bundle on P⁴, and M_k=H²(B(k)). Put S=Soc(M)₋₁. The exact coordinate Koszul complex produces canonical maps between finite-dimensional groups L_p,N_p defined below, and a canonical exact sequence

    0 → Q → S → Z → 0,                                      (1)
    Q = N₃ / im(d₂:L₁→N₃),
    Z = ker(d₂:L₂→N₄).

The left injection is the inverse of a canonical d₃ isomorphism onto Q, followed by inclusion in S. In particular

    S=0 iff d₂:L₁→N₃ is surjective AND d₂:L₂→N₄ is injective, (2)
    dim S = dim Q + dim Z.

These are bounded, intrinsic tests. They require no chosen bases, matrix ranks, or instance evaluation. They do require the indicated derived/cochain maps: replacing them by bare multiplication maps or dimension counts is not justified. The target section groups have twists 1 through 4; degree-zero H¹ relations are retained. A test using strictly positive twists alone is NOT asserted.

## 1. Imported input and vanishing checks

The source records are ../sharper-hm-regularity/SHARPEST-BOUND.md and ../fourth-ideal-pushforward/COHOMOLOGY-INDEPENDENT-AUDIT.md. They give

    B∨=B, H¹B(t)=0 for t≤−2, H²B(t)=0 for t≥2.

Stability of F gives H⁰End(F)(t)=0 for t<0. Simplicity of stable F and the trace-free splitting also give H⁰B(0)=0. Serre duality on P⁴ gives

    H³B(t)=H¹B(−5−t)*,
    H⁴B(t)=H⁰B(−5−t)*.

For every t=−1,0,1,2,3,4, the dual twist lies between −9 and −4. Thus H³ and H⁴ vanish for every term below. No low nonnegative H¹ vanishing is assumed. The stronger bound H¹B(t)=0 for t≥7 is not needed here.

## 2. The exact six-term complex and all relevant E₂ entries

Choose homogeneous coordinates x₀,…,x₄. Let V=H⁰(O(1))* have the dual basis e₀,…,e₄ and set

    K^p = Λ^p V ⊗ B(p−1), 0≤p≤5,
    δ(s⊗w)=Σ x_i s⊗(e_i∧w).

Thus K is

    0→B(−1)→5B→10B(1)→10B(2)→5B(3)→B(4)→0.

The coordinates have no common zero on P⁴; locally one is invertible and contraction by its dual divided by that coordinate contracts the Koszul complex. K is exact, so its hypercohomology is zero. A finite affine Čech cover gives a double complex C^{p,q}=Čech^q(K^p), whose commuting vertical and horizontal differentials are d and δ. We use total differential D=d+(−1)^qδ. Then E₁^{p,q}=H^q(K^p), d₁=(−1)^qδ, and the underlying row cohomology groups are those of δ. All displayed d₂,d₃ signs refer to this convention.

Write A_p=Λ^pV⊗H¹B(p−1) and G_p=Λ^pV⊗H⁰B(p−1), with δ induced by multiplication. Define

    L_p=ker(A_p→A_{p+1}) / im(A_{p−1}→A_p),
    N_p=ker(G_p→G_{p+1}) / im(G_{p−1}→G_p),

with absent terms zero. E₂ has only these rows:

    q=2: S, T₁, T₂, 0, 0, 0;
    q=1: L₀,L₁,L₂,L₃,L₄,L₅;
    q=0: 0, 0, N₂,N₃,N₄,N₅.

Here

    S=ker(M₋₁→V⊗M₀),
    T₁=ker(V⊗M₀→Λ²V⊗M₁)/im(M₋₁→V⊗M₀),
    T₂=coker(V⊗M₀→Λ²V⊗M₁).

In particular S is exactly the socle, not a quotient of it: column −1 is absent. The zero entries in row 2 for p≥3 use H²B(t)=0 for t≥2. The first two zeros in row 0 use H⁰B(−1)=H⁰B(0)=0.

All possibly nonzero d₂ arrows are

    S→L₂, T₁→L₃, T₂→L₄,
    L₀→N₂, L₁→N₃, L₂→N₄, L₃→N₅.           (3)

Other arrows either leave the rectangle or meet zero rows/entries. The only potentially nonzero d₃ arrows are from the surviving portions of S,T₁,T₂ to the corresponding row-zero quotients at columns 3,4,5. All d_r for r≥4 vanish. This lists the competing incoming arrows, including the essential L₁→N₃ ambiguity.

## 3. Derivation of the exact filtration

Put f=d₂:S→L₂, g=d₂:L₂→N₄ and h=d₂:L₁→N₃. Since d₂²=0, im f⊂ker g. More precisely

    E₃^{2,1}=ker g / im f.

There is no further incoming arrow: for d₃ it would start at (−1,3), and for larger r its p coordinate is still negative. There is no further outgoing arrow because its target q is negative. Hence E₃^{2,1}=E∞^{2,1}=0, and im f=ker g=Z.

No higher-page incoming arrow ever reaches (0,2), so E₃^{0,2}=ker f. Its only remaining outgoing arrow is

    d₃:ker f → E₃^{3,0}=N₃/im h=Q.              (4)

The source has no later outgoing arrow; the target has no outgoing arrow and no other possible later incoming arrow. Exact total hypercohomology forces both eventual groups to vanish. Therefore (4) is an isomorphism. This proves (1), canonically relative to the coordinate Koszul complex. Coordinate changes induce isomorphisms of the entire construction; there is no canonical splitting of (1).

Notably T₁,T₂ and their d₂ arrows do not alter either target in (1). They matter elsewhere on the spectral sequence, but cannot be silently substituted into the L₁→N₃ quotient.

## 4. Finite positive-target presentation

With H^i_t=H^i(B(t)), the groups needed in (1) are explicitly

    L₁ = ker[V⊗H¹₀→Λ²V⊗H¹₁] / im[H¹₋₁→V⊗H¹₀],
    L₂ = ker[Λ²V⊗H¹₁→Λ³V⊗H¹₂] / im[V⊗H¹₀→Λ²V⊗H¹₁],
    N₃ = ker[Λ³V⊗H⁰₂→Λ⁴V⊗H⁰₃] / im[Λ²V⊗H⁰₁→Λ³V⊗H⁰₂],
    N₄ = ker[Λ⁴V⊗H⁰₃→Λ⁵V⊗H⁰₄] / im[Λ³V⊗H⁰₂→Λ⁴V⊗H⁰₃].

To compute im h it suffices to use the numerator of L₁, since h annihilates its denominator. Consequently the negative group H¹₋₁ need not be computed for either Q or Z. The data consist of H¹ at twists 0,1,2; H⁰ at twists 1,2,3,4; the displayed multiplication maps; and the cochain transgressions below. H² at twists −1,0 is needed only when detecting an already specified class rather than using criterion (2) to test the whole socle.

## 5. Constructive maps and their exact ambiguities

All cochains below carry their displayed (p,q) bidegrees. Cochains are taken in the same affine Čech resolution; wedge signs are already contained in δ.

### 5A. Row-one d₂ maps h and g

Represent a class in L_p, p=1 or 2, by z∈C^{p,1} with dz=0. The row-cycle condition says δz is vertically exact. Choose u∈C^{p+1,0} with

    du=δz.

Then δu is a global section and a horizontal cycle, and

    d₂[z]=[δu]∈N_{p+2}.                          (5)

Indeed D(z+u)=δu. Replacing u by a global section changes δu by a horizontal boundary, exactly the denominator of N_{p+2}. Changing z by a vertical boundary changes u by the matching horizontal cochain and leaves δu unchanged. Changing z by δw for a vertical cocycle w leaves δz unchanged, hence does not change (5). These facts prove both that (5) descends to L_p and that the H¹₋₁ denominator can be omitted when calculating im h.

### 5B. First detector of a socle class

Represent y∈S by y∈C^{0,2}, dy=0. Being in the socle means δy is vertically exact. Choose a∈C^{1,1} such that

    da=δy.

Then δa is a vertical cocycle and a horizontal cycle, and

    f(y)=[δa]∈L₂.                                (6)

The sign follows from D(y−a)=δa. Changing a by a vertical cocycle z alters δa by δz, exactly a row boundary. Changing y by dc is absorbed by a↦a+δc. Thus f is canonical. Moreover g f=0: for z=δa the required primitive in (5) can be chosen u=0 because δz=0.

### 5C. Second detector, available only when f(y)=0

If f(y)=0, choose a vertical cocycle z∈C^{1,1} and b∈C^{2,0} satisfying

    δa−δz=db.

Replace a by a−z. Now da=δy and db=δa. The section δb is global and a horizontal cycle. The second detector is

    d₃(y)=−[δb] in N₃/im h.                      (7)

Indeed D(y−a−b)=−δb. For fixed y, two allowable a's differ by a vertical cocycle w, with δw vertically exact because both admit b. Thus w represents a class in L₁; the change of δb is exactly d₂[w], modulo a global horizontal boundary. This is precisely im h and no smaller quotient is justified. A change of b by a global section contributes a horizontal boundary. A change of representative y by dc is absorbed by a↦a+δc, leaving b unchanged. These verify all cochain ambiguities in (7).

The constructive criterion is now sharp: for y∈S, if f(y)≠0 then y≠0; if f(y)=0 then y=0 iff the quotient class (7) is zero. Vanishing of (7) means exactly that the section −δb differs from δu for some row-one cycle and its primitive du=δz by a global horizontal boundary. Raw vanishing of δb is unnecessarily strong and dependent on choices.

### 5D. Constructive realization of both exact-sequence arrows

The injection Q→S can also be constructed without leaving cochains. Represent a class in Q by a global horizontal cycle c∈C^{3,0}. It is D-closed. Total acyclicity supplies a degree-two primitive v=y+a+b with bidegrees (0,2),(1,1),(2,0) and Dv=c. The component equations are

    dy=0, δy+da=0, −δa+db=0, δb=c.

They show [y]∈ker f and, using the primitives −a,−b in (7), d₃[y]=[c]. Different total primitives differ by a total boundary; their first components differ by a vertical boundary, so [y] is independent of that choice. If c changes by a horizontal boundary, a primitive supported in column 2 accounts for it and contributes no y. If c changes by an h-image, the primitive z+u from (5), with z in column 1, likewise contributes no y. This is exactly the canonical injection in (1).

Surjectivity S→Z has a matching construction. Represent ℓ∈Z by z∈C^{2,1}, dz=0, and choose u∈C^{3,0} with du=δz. Since g(ℓ)=0 in N₄, there is a global h∈C^{3,0} with δu=δh. Replace u by u−h, so z+u is D-closed. A total primitive y+a+b then satisfies

    dy=0, δy+da=0, −δa+db=z, δb=u.

Taking −a as the first primitive for y gives f([y])=[z]=ℓ. No canonical choice of this lift is asserted: any two lifts differ by the Q-layer. These constructions use exactness to establish finite criteria; they do not compute actual HM primitives.

## 6. Why the first detector alone is incomplete

The failure is structural, not merely a warning about unknown ranks. Consider the following finite double complex over C. Its nonzero basis elements are

    y:(0,2), A:(1,2), a:(1,1), B:(2,1), b:(2,0), C:(3,0).

Set dy=0, da=A, db=B; set δy=A, δa=B, δb=C; all other arrows zero. The differentials commute and square to zero. With D=d+(−1)^qδ the total differential from degree two to degree three is

    y↦A, a↦A−B, b↦B+C,

an isomorphism, so total cohomology vanishes. Vertical cohomology has exactly y at (0,2) and C at (3,0). Hence S=C, every L_p=0, N₃=C, the first d₂ is zero, and d₃(y)=−C is an isomorphism. This obeys the row support and acyclicity used in the detector theorem.

This is an abstract counterexample to deriving completeness of the first detector from those formal premises, not a different HM bundle or an evaluated HM differential. In particular f(y)=0 does not certify y=0, even under exact total cohomology. Likewise one cannot replace Q by N₃: im h records an actual change-of-primitives ambiguity.

## 7. Restriction to the cofactor defect

Use prerequisite primary-pairing-constraints, document PROOF.md (see the unit INPUTS.md), §4. Put K=ker[t₂:M₋₄→M₋₂] and

    D=t₃K∩S.

That proof identifies the first cofactor loss c−e with dim D. Restrict f to D and set D₀=D∩ker f. Then

    0→D₀→D→f(D)→0,
    d₃|D₀:D₀↪Q,
    f(D)⊂Z.

Thus D has two canonical detector layers, f(D)⊂Z and d₃(D₀)⊂Q, and

    c−e = dim f(D)+dim d₃(D₀) ≤ dim Z+dim Q = dim S.

For a specified x∈K, first check that y=t₃x is in S (all five coordinate products vanish in M₀). If so, (6) and, when necessary, (7) detect whether y is nonzero. The equality D=0 is equivalent to both its detector layers being zero. S=0 is sufficient for D=0 but not necessary; replacing D by the full socle would lose the cubic-image restriction. No claim is made that every socle class lies in t₃K, or that this construction determines the other cofactor loss or the separate secondary obstruction.

## Status

No actual HM multiplication, cofactor matrix, differential rank, physical source, or source membership was evaluated. The contribution is an exact two-layer finite presentation, explicit cochain ambiguity control, and a counterexample to the first-differential shortcut. It does not assert that either layer vanishes for the actual HM bundle.
