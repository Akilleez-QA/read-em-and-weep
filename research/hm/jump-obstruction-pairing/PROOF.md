# Quadratic obstructions at HM restriction jumps

## Result

Work over C with the normalized HM bundle F on P(V)=P⁴ and B=End₀F. Import the audited results in ../generic-restriction-deformations/PROOF.md and ../quintic-restriction-jump-loci/{PROOF,NONZERO-COROLLARY}.md. In particular the actual multiplication pairing is Φ=cΨ with c≠0, and the ambient orbit Kodaira–Spencer map sl(V)→H¹B is an isomorphism.

Fix an equation p of a smooth quintic X, put E=F|X, and set

    H=Ext¹_X(E,E), O=Ext²_X(E,E), A=H¹B⊂H,
    U=H²B(−5), T=H²B=U*, M=Φ(p), K_p=ker M.

The restriction sequence gives maps δ:H→K_p and j:coker M→O. (K_p is not the 123-dimensional kernel of the universal map Ψ.) Write a_v∈A for the restricted orbit tangent of v∈sl(V), and use the action on equations

    (g·p)(w)=p(g⁻¹w),   v·p=(d/ds)|₀ exp(sv)·p.

Let β(x,y)=[x,y]=x∪y+y∪x be the symmetric degree-one Yoneda bracket; the primary obstruction is q₂(x)=β(x,x)/2. Then the following formula is exact, with the cochain conventions specified below:

    β(a_v,x)= j([Φ(v·p)(δx)]) .                         (1)

The square brackets on the right mean passage from T to coker M. Consequently the mixed bracket is entirely determined by a derivative of the known universal linear map, without evaluating an HM cochain representative. Under compatible Serre-duality normalizations,

    ⟨β(a_v,x),y⟩_X = Φ(v·p)(δx,δy).                  (2)

Changing the normalization of the CY volume form changes both sides of the duality identification by its common scalar, and does not affect any vanishing or rank assertion.

New consequences:

1. The sole unknown part of the primary cyclic cubic after (2) is a cubic on K_p: one coefficient at rank one, four coefficients at rank zero, after choosing a splitting H=A⊕K_p. This is a statement about primary obstructions only, not higher Kuranishi terms.
2. At a rank-one point, mixed obstructions vanish identically exactly when every projective orbit direction is tangent to the determinant quadric there.
3. There is a nonempty Zariski-open dense subset of the smooth rank-one jump stratum on which mixed obstructions are nonzero. At every such point the minimal hull has dimension exactly 24, embedding dimension 25, and is singular and obstructed. Its quadratic initial equations span, in suitable orbit-adapted tangent coordinates, precisely (t₁z,z²) in degree two.

No selected quintic, HM map, source, cofactor or numerical rank instance is evaluated.

## 1. The derivative/Bockstein lemma, including its sign

Choose any functorial acyclic resolution C•(B) and C•(B(−5)); the restriction complex is represented by the cone with

    L_p^n=C^n(B)⊕C^{n+1}(B(−5)),
    D_p(b,c)=(db+pc,−dc).

The maps from the first summand and to the second summand induce j and δ, respectively. This fixes the cone and connecting-map signs. For p_s=p+s q over C[s]/(s²),

    D_{p_s}=D_p+sD',   D'(b,c)=(qc,0).

If x=[(b,c)]∈H¹(L_p), then dc=0 and db=−pc. The Bockstein of x in this first-order family, defined by lifting a cocycle and dividing its differential by s, is

    [D'(b,c)]=j([m_q(δx)])∈H²(L_p).              (3)

Here m_q:H²B(−5)→H²B is multiplication by q. The class is well-defined modulo im M. Formula (3) follows directly from the displayed cochains and needs no splitting of the restriction exact sequence. It also proves that this Bockstein has no component in the quotient H³B(−5) of H²(L_p).

Now choose g_s=exp(sv). The isomorphism g_s:X_p→X_{g_s·p} identifies F|X_{g_s·p}, pulled back to the fixed X_p, with (g_s*F)|X_p. Thus the moving-equation complex in (3), with q=v·p, computes the same cohomology deformation as the endomorphism bundle of the orbit family on fixed X.

For clarity, in a differentiable trivialization of a holomorphic bundle deformation, its Dolbeault operator is ∂̄_E+sα with [α]=a_v. On endomorphism-valued forms it is

    d_s=d+s[α,−].

Therefore its Bockstein on H¹ is exactly [α,x]=β(a_v,x), not its negative. Changing a differentiable trivialization adds a chain homotopy to the derivative and leaves its induced cohomology map unchanged. Applying (3) proves (1). This argument is about a vector-bundle family over the dual numbers, so a compatible resolution can equivalently be chosen in the algebraic category; the Dolbeault description merely identifies its deformation differential and fixes the bracket sign.

The use of the action g·p=p∘g⁻¹ is essential: g_s maps X_p to X_{g_s·p}. Choosing the opposite equation action without changing a_v would reverse the derivative sign.

## 2. Serre compatibility and the primary cubic

Use trace and Serre duality on P⁴ to identify T with U*. On X, choose the adjunction trivialization of K_X and its sign so that the restriction/connecting adjointness reads

    ⟨j(t),y⟩_X=⟨t,δy⟩_{P⁴},    t∈T, y∈H.     (4)

This is the usual Serre-duality adjointness for the restriction triangle. It can also be taken as the precise normalization of the one-dimensional trace H³O_X→C: the scalar connecting map H³O_X→H⁴O(−5) is an isomorphism, and its sign is chosen consistently with the displayed cone. With the opposite convention for this scalar trace, a minus sign appears in both (4) and (2); formula (1) is unchanged. In particular we do not assert a sign independent of a choice of CY trace.

Adjointness implies that j(coker M) is the annihilator A^⊥ in O=H*, and that its induced pairing with H/A=K_p is perfect. Indeed it annihilates A because δA=0; both its dimension and dim(H/A) are dim K_p. Formula (2) follows from (1) and (4).

For degree-one classes define

    C(x,y,z)=⟨β(x,y),z⟩_X.

This trilinear form is symmetric. At the Dolbeault cochain level it is the integral of tr((xy+yx)z) against the chosen holomorphic volume form. Cyclic permutation of three degree-one factors has sign (−1)^(1·2)=+1; swapping x and y is built into the bracket. These generate all permutations. No cyclic minimal-model theorem or analytic critical-locus theorem is needed for this primary statement. Moreover β(A,A)=0, either by (1) and δA=0, or by the actual smooth orbit family and polarization of its second-order liftability.

Choose any vector-space splitting H=A⊕K_p, writing elements as a_v+z. Define

    L(v)(z,w)=Φ(v·p)(z,w),    L:sl(V)→Sym²K_p*.

Then C is zero on terms with two A arguments, is L on A⊗Sym²K_p, and has an as-yet undetermined restriction G∈Sym³K_p* on three normal arguments. Equivalently the homogeneous cubic

    W₃(a_v+z)=C(a_v+z,a_v+z,a_v+z)/6
             = L(v)(z,z)/2 + G(z,z,z)/6          (5)

has gradient q₂ under O=H*. This proves the stated reduction of unknown primary coefficients. Changing the splitting can change G, as expected; L is intrinsic. The dimensions dim Sym³K_p* are one and four when dim K_p is one and two.

In particular q₂(z), paired with an orbit tangent a_v, equals L(v)(z,z)/2. Thus a nonzero derivative supplies not only mixed brackets but a nonzero normal-normal obstruction component dual to the orbit tangent. It would be incorrect to retain only mixed obstruction equations and omit this cyclic companion.

## 3. Rank one: transversality and the exact quadratic ideal

Suppose rank M=1 and choose a nonzero u∈K_p. Then

    λ_p(v)=Φ(v·p)(u,u)

is a linear functional on sl(V); rescaling u rescales λ_p by a nonzero square. Linear algebra of a rank-one symmetric two-by-two matrix gives

    (d det)_M(N) = nonzero scalar × N(u,u).

Indeed choose a basis with M=diag(μ,0), μ≠0 and u the second basis vector; the derivative is μN₂₂. Consequently λ_p(v)≠0 precisely when the derivative of det Φ at p in direction v·p is nonzero. Since det Φ=c²Q, this is exactly orbit transversality to Q=0. It is well-defined on projective tangent directions because Φ(p)(u,u)=0, so adding a multiple of p to v·p changes nothing.

If λ_p≠0, choose t₁=λ_p on A, complete it to orbit coordinates t₁,…,t₂₄, and write z for the scalar normal coordinate in the chosen u direction. Formula (5) reads

    W₃=t₁z²/2 + γz³/6.

Its partial derivatives span z²/2 and t₁z+γz²/2. Thus the degree-two Kuranishi equations span exactly the two-dimensional space generated by z² and t₁z; all remaining quadratic equations are zero or linear combinations of these. Factors of 2 are harmless over C. Here is the precise minimal Kuranishi justification for the word “exactly.” In the trace-free Dolbeault DGLA choose a contraction onto cohomology, with inclusion i, projection P, and degree −1 homotopy h. The formal gauge-slice solution is constructed recursively as η(x)=i(x)−h[η(x),η(x)]/2. Its Kuranishi map is k(x)=P[η(x),η(x)]/2; the Maurer–Cartan equation is equivalent on this slice to k(x)=0. This is the usual DGLA hull construction, and the trace-free H⁰ vanishes here. Since η(x)=i(x)+terms of order at least two, the quadratic part of k is P[i(x),i(x)]/2=q₂(x). All generators of the Kuranishi ideal start in degree at least two, so its degree-two part is exactly the linear span of the components of q₂, rather than merely containing that span. An isomorphism to any other minimal hull transports this statement by its tangent-space linear isomorphism. Higher-degree equations are not determined.

For the minimal hull R=C[[t₁,…,t₂₄,z]]/I, its associated graded ring is therefore a quotient of

    C[t₁,…,t₂₄,z]/(z²,t₁z),

which has Krull dimension 24. Dimension is preserved by passage to the maximal-ideal associated graded ring for this complete Noetherian local ring. The embedded orbit germ from ../generic-restriction-deformations/JUMP-STRATA.md gives dim R≥24, so dim R=24. Since its tangent dimension is 25, R is not regular; it is not a formally smooth deformation hull. Neither reducedness nor a complete description of its components follows from this argument.

## 4. Generic transversality without evaluating any point

Let Δ=V(Q)⊂P(S₅). It is an irreducible rank-three quadric with vertex P(ker Ψ). Suppose every v∈sl(V) is tangent at every point of the smooth rank-one quintic stratum Ω∩(Δ\vertex). This is a nonempty open subset of the irreducible Δ by the established smooth-fiber theorem. Hence each quadratic polynomial v·Q vanishes densely on Δ, and therefore

    v·Q=χ(v)Q

for some scalar χ(v), since Q is irreducible and both degrees are two. The line CQ would be an sl(V)-subrepresentation. As sl(V) is perfect, its one-dimensional character χ is zero. The connected group SL(V) would then fix Q.

But there is no nonzero SL₅-invariant quadratic polynomial on S₅=Sym⁵V*. An invariant quadratic would polarize to a nonzero equivariant map S₅→S₅*. Both modules are irreducible, so this would be an isomorphism. They are not isomorphic: their highest weights are respectively 5ω₄ and 5ω₁ (with the opposite labeling convention these are interchanged), which differ for SL₅. This contradiction proves some orbit derivative is nonzero somewhere on the smooth rank-one stratum.

The condition that all 24 derivatives vanish is Zariski closed on this stratum. Its complement is therefore nonempty open dense, and every point of that complement satisfies Section 3. This proves generic actual obstructedness on the rank-one jump stratum without selecting a quintic, computing any Φ value, or evaluating any derivative rank instance.

This does not prove transversality at every rank-one point. It also supplies no automatic nonvanishing at vertex points. There the valid, useful test remains L:sl(V)→Sym²U*, v↦Φ(v·p), and the unknown cubic G has four coefficients after a splitting. No unproved pointwise rank assertion is made.

## 5. A vertex criterion requiring only the infinitesimal polynomial action

At a smooth-quintic vertex point M=0, let W_p be the image of

    L:sl(V)→Sym²U*,    v↦Φ(v·p).

If the binary quadratics in W_p have no common zero in P(U), then the hull has dimension exactly 24 and embedding dimension 26, and is singular and obstructed. In particular, surjectivity of L is sufficient. This is a conditional criterion, not an evaluated rank assertion.

Indeed (5) shows that the primary obstruction components dual to the 24 orbit directions are exactly the quadratic forms L(v)(z,z)/2, independent of the four unknown coefficients of G. If these forms have no common nonzero zero, their homogeneous ideal in C[z₁,z₂] has radical (z₁,z₂), by the Nullstellensatz. The associated graded hull is a quotient of the polynomial ring in t and z modulo these forms, whose dimension is 24. The embedded orbit germ gives the reverse inequality. Thus the criterion requires only the known universal pairing applied to infinitesimal polynomial action, and not the unknown normal cubic or any higher obstruction computation.

At a rank-one point with λ_p=0, the only remaining primary datum is γ in (5). If γ≠0 the same dimension argument from the equation z² still gives dimension 24 and actual obstruction; if γ=0 the entire primary obstruction vanishes and higher terms remain undetermined. Nothing here claims either value of γ.

## 6. Dependencies, scope, and references

All HM-specific facts are imported from the named audited local proofs: the cohomology rows, symmetry and nonvanishing of Φ, the exact restriction sequence, the orbit Kodaira–Spencer isomorphism, the embedded 24-dimensional orbit germ, and the irreducible quadric with nonempty smooth-quintic rank-one stratum. The new proof uses the elementary cochain Bockstein calculation, trace cyclicity, and highest-weight theory; it never assumes that every cohomology jump is obstructed.

For general DGLA deformation conventions and the Maurer–Cartan primary obstruction, a primary reference is Marco Manetti, “Deformation theory via differential graded Lie algebras”: https://arxiv.org/abs/math/0507284 . The operative formula here is proved explicitly in Sections 1–2, including its factor 1/2 and action-sign convention.

The conclusions concern ordinary bundle deformations on the FIXED smooth quintic X, equivalently fixed determinant by the scalar H¹/H² vanishings already established. They do not calculate source-dependent obstructions, ordered products without symmetrization, higher Massey products, the full Kuranishi ideal, or a selected physical-source or cofactor rank.
