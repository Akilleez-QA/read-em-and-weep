# Relative restriction cohomology and the Tor correction at jumps

## Theorem

Retain the notation and established inputs of [PROOF.md](PROOF.md). Let Ω⊂P(S₅) be the smooth-quintic locus, π:𝒳→Ω the universal smooth quintic, and 𝔅 the restriction to 𝒳 of the pullback of B=End₀F. Put

    A=H¹B (dimension 24), U=H²B(−5) (dimension 2),
    T=H²B=U*, D=H³B(−5) (dimension 24).

Here O(j) denotes the restriction of O_P(S₅)(j) to Ω. The universal pairing is a morphism of vector bundles

    f: U⊗O(−1) → T⊗O,

induced by Φ=cΨ. Define 𝒦=ker f and 𝒞=coker f. Then R⁰π_*𝔅=R³π_*𝔅=0, and there are canonical exact sequences

    0→A⊗O→R¹π_*𝔅→𝒦→0,                       (1)
    0→𝒞→R²π_*𝔅→D⊗O(−1)→0.                  (2)

These are sheaf exact sequences, without a constant-rank assumption on f.

If c≠0, then 𝒦=0 as a sheaf even though f has nonzero kernels on many fibers. Consequently

    R¹π_*𝔅 ≅ A⊗O                               (3)

is a rank-24 vector bundle on ALL of Ω. The sheaf 𝒞 is a rank-one maximal Cohen–Macaulay sheaf on the determinant quadric Δ=Ω∩V(Q), extended by zero to Ω. It is a line bundle on Δ\P(K), but is not locally free as an O_Δ-module at any point of Ω∩P(K). Sequence (2) is locally split as O_Ω-modules, without a claimed canonical or global splitting. Thus R²π_*𝔅 is not a vector bundle along Δ.

At every closed point x=[p]∈Ω, with residue field k(x)=C and tautological line ℓₓ=O(−1)⊗k(x), the natural base-change maps satisfy

    0→(R¹π_*𝔅)⊗k(x)→H¹(Xₚ,B|Xₚ)
      →Tor₁^{O_Ω}(𝒞,k(x))→0,                  (4)

    (R²π_*𝔅)⊗k(x) ≅ H²(Xₚ,B|Xₚ).            (5)

For c≠0 the Tor group in (4) is canonically ker(fₓ:U⊗ℓₓ→T), and has dimension 2−rank Φ(p). This accounts for the individual H¹ dimensions 24,25,26 despite the constant rank of R¹. The use of ℓₓ is necessary for a canonical projective-parameter formula; choosing the equation p trivializes that line and recovers the earlier pointwise sequence.

If c=0, then 𝒦=U⊗O(−1), 𝒞=T⊗O. Both relative middle cohomology sheaves are vector bundles of rank 26 by (1)–(2), and both natural fiber maps are isomorphisms. We do not use or decide which scalar case holds.

## 1. Universal sequence

Let q:P⁴×Ω→Ω be projection and j:𝒳→P⁴×Ω the inclusion. The universal equation is a section of O_P⁴(5)⊠O(1), so the correct sequence is

    0→B(−5)⊠O(−1)→B⊠O→j_*𝔅→0.             (6)

The negative tautological twist cannot be omitted. For each i, product cohomology and the projection formula identify the two left direct images with HⁱB(−5)⊗O(−1) and HⁱB⊗O. The given cohomology rows turn the long exact direct-image sequence into

    0→A⊗O→R¹π_*𝔅→U⊗O(−1) --f→ T⊗O
      →R²π_*𝔅→D⊗O(−1)→0,

and give the asserted vanishing in degrees zero and three. Multiplication by the universal equation is exactly the universal family of the maps mₚ, so f is induced by Φ under the fixed Serre identification T=U*. This proves (1)–(2).

## 2. Injective sheaf map and its quadric cokernel

Assume c≠0. Locally trivialize O(−1) and choose bases. Up to a nonzero scalar, f is represented by

    M = [a b; b d],       det M = Q=ad−b².

The three linear coordinates a,b,d are independent. Ω is an integral open subset of P¹²⁵; Q is nonzero, since the previous proof establishes a smooth quintic with Q≠0. On every nonempty trivializing open its local equation is a nonzero element of the local domain. From adj(M)M=Q·I, a local section in ker M is killed by Q. The source is locally free over a domain, so that section is zero. Thus 𝒦=0 globally and

    0→U⊗O(−1) --f→ T⊗O→𝒞→0                (7)

is a locally free resolution. This injectivity is a sheaf assertion; tensoring (7) with a residue field need not preserve it.

The other adjugate identity shows Q𝒞=0. Its zeroth Fitting ideal is (Q), so its scheme-theoretic support is the reduced irreducible divisor Δ. More explicitly its annihilator is exactly (Q): on the integral quadric, 𝒞 has generic rank one, so no nonzero element of O_Δ can annihilate the whole module. Its first Fitting ideal, computed over Ω, is (a,b,d), the vertex ideal.

For a point y∈Δ let R=O_Ω,y, a regular local domain, and M_y the cokernel stalk. Resolution (7) gives projective dimension at most one. This nonzero Q-torsion module is not R-free, so its projective dimension is exactly one. Auslander–Buchsbaum gives depth_R M_y=dim R−1. Since Q annihilates it, depth as an R/(Q)-module is the same, and dim R/(Q)=dim R−1. Thus it is maximal Cohen–Macaulay over the quadric local ring. At its generic point its rank is one.

Away from the vertex, at least one entry of M is a unit locally on Ω. Elementary invertible row and column operations turn M into diag(1,uQ) for a unit u. Its cokernel is locally R/(Q), proving local freeness of rank one on Δ there. At a vertex point all three entries are in the maximal ideal, so 𝒞⊗k(y) has dimension two. A locally free rank-one O_Δ-module would have one-dimensional fiber. Hence it is not locally free there. Every part of the vertex and divisor under discussion meets Ω by the previous theorem.

Since the quotient in (2) is a vector bundle, (2) splits locally. In particular R²π_*𝔅 has projective dimension at most one and has nonzero torsion 𝒞 exactly along Δ; it cannot be locally free there. No local splitting of vector spaces has been promoted to a global canonical splitting.

## 3. Derived base change and the Tor exact sequence

The morphism π is smooth projective, and 𝔅 is locally free on 𝒳, hence flat over Ω. The derived direct image E=Rπ_*𝔅 is perfect and obeys derived base change:

    E⊗ᴸk(x) ≅ RΓ(Xₚ,B|Xₚ).

This is the proper-flat cohomology-and-base-change theorem; see [Stacks Project, cohomology and base change III](https://stacks.math.columbia.edu/tag/07VJ) or [VI](https://stacks.math.columbia.edu/tag/0A1G). Applying it here does NOT say that each individual cohomology sheaf commutes with base change.

For c≠0, write E¹=R¹π_*𝔅=A⊗O and E²=R²π_*𝔅. There are no other cohomology sheaves. The truncation triangle is

    E¹[−1]→E→E²[−2]→E¹.

Tensor it derivedly with k(x). Since E¹ is locally free and E² has projective dimension at most one, the associated long exact sequence reduces in degrees one and two to

    0→E¹⊗k(x)→H¹(Xₚ,B|Xₚ)
      →Tor₁(E²,k(x))→0,
    E²⊗k(x) ≅ H²(Xₚ,B|Xₚ).

The canonical map on the left in the first line is the usual cohomology base-change map. Sequence (2), whose quotient is locally free, identifies Tor₁(E²,k(x)) with Tor₁(𝒞,k(x)). Resolution (7) then gives the exact sequence

    0→Tor₁(𝒞,k(x))→U⊗ℓₓ --fₓ→ T
      →𝒞⊗k(x)→0.                              (8)

Thus (4)–(5) follow, and both ker fₓ and coker fₓ have dimension 2−rank Φ(p). Tensoring (2) is exact on the left because its quotient is locally free, so (5) also recovers the individual H² exact sequence

    0→coker fₓ→H²(Xₚ,B|Xₚ)→D⊗ℓₓ→0.

Consequently the H¹ base-change map is an isomorphism exactly off Δ; it is injective with one-dimensional cokernel on the rank-one stratum and two-dimensional cokernel at the vertex. The H² map remains an isomorphism on all strata, even though R² is not locally free.

When c=0, (1)–(2) are extensions of vector bundles by vector bundles. Their middle terms are therefore locally free of rank 26. The same truncation argument has no Tor term and proves base change in both degrees. In that case ker f is a rank-two bundle, unlike the zero sheaf occurring when c≠0.

## 4. Consequences and limits

For c≠0, the cohomology jump is not encoded by a rank jump of the sheaf R¹π_*𝔅. It is encoded by failure of its formation to commute with specialization, measured exactly by Tor₁ of the quadric cokernel. On a rank stratum, recomputing relative cohomology after base change can therefore produce a different degree-one sheaf from merely restricting R¹π_*𝔅.

For 𝔈=F|𝒳, the relative self-Ext cohomology sheaves are Rⁱπ_*End(𝔈), since 𝔈 is locally free. The scalar summand contributes O in degree zero, zero in degrees one and two, and O(−1) in degree three, as follows directly from the universal scalar restriction sequence. Thus the middle relative self-Ext sheaves are exactly those above. The top scalar twist is O(−1), although every individual top Ext space has dimension one; this is another reason to keep tautological twists explicit.

These statements concern cohomology sheaves over the smooth-quintic parameter space and deformation spaces on fixed fibers. They do not assert unobstructedness, a global moduli vector bundle, a global splitting of (2), or nonvanishing of c. No selected polynomial or HM multiplication value was evaluated. Only local proof files were written.
