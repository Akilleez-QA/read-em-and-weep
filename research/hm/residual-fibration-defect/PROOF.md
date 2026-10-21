# The residual morphism: Stein property, torsion defect and nonflat fibers

Status: authored structural proof, independently mathematically reviewed in REVIEW.md; not formally checked. Work over C. No selected actual HM/source instance is evaluated.

## 1. Exact dependencies and statement

Let S be the actual primary surface, ν:X=S(5)→S its finite normalization, and π:X→B=P1 the modular elliptic fibration. Write H=ν*O_S(1). We use:

- PR572, commit **a20545dcc4c0e26dc1bb8af17852db63696ec7b1**, `research/hm/residual-canonical-decic/PROOF.md`: the residual morphism g:S→Γ factors upstairs as gν=hπ, where h:B→Γ is normalization of the integral canonical decic Γ. The curve Γ has exactly six ordinary nodes q_U, whose preimages are the six specified pairs {a_U,b_U} of the twelve cusps.
- PR574, commit **3c92fdc469f6870520e7a9d905b5ab9199a5bf37**, `research/hm/primary-conductor/PROOF.md`: the exact normalization sequence 0→O_S→ν_*O_X→T→0, where T has length one at each of the thirty transverse surface double points. At such a point, the completed local ring is C[[u1,u2]] ×_C C[[v1,v2]], and the normalization quotient is the difference of the two residues.
- The exact surface dictionary in PR570, commit **e5e55594ef2b99cefb81c4c02b22cb45e1ff0025**, and global primary equality in PR573, commit **6c2dbd48edea0577acf063a60e1edbbbe92ced5c**. In particular these are statements about the actual primary scheme, not an abstract numerically similar model.
- Barth–Hulek–Moore, “Shioda's Modular Surface S(5) and the Horrocks–Mumford Bundle,” §4.3, printed p58, and §4.5, Propositions 9–10, printed pp63–64. The twelve singular fibers are reduced I5 pentagons. Their images are paired, with exactly five shared vertices per pair; the sixty source vertices are identified in pairs to thirty surface double points. Each individual pentagon maps isomorphically to its image, and there are no other identifications. Also K_X=3F, χ(O_X)=5, H.F=5.

Public BHM source: https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

We prove

(1) g_*O_S=O_Γ;

(2) 0→K→R¹g_*O_S→h_*O_B(-5)→0,
    where K is the entire torsion subsheaf and has dimension four at each q_U, hence length 24;

(3) R^i g_*O_S=0 for i≥2;

(4) the scheme fiber at each q_U is reduced, consisting of the two I5 pentagons glued at their five paired vertices. Its arithmetic genus is six, whereas a fiber over the smooth locus of Γ is a smooth elliptic curve. The morphism g is not flat at any q_U.

No splitting of (2), no flat cohomology-and-base-change assertion, and no lift or algebraicity assertion is made.

## 2. Matching the six base nodes with the thirty surface nodes

Suppose BHM identifies a vertex on F_a=π^{-1}(a) with a vertex on F_b=π^{-1}(b). The source points have the same image p in S. Therefore

h(a)=g(p)=h(b).

The two fibers are distinct. By PR572, the only distinct points of B with the same h-image are the specified six cusp pairs. Thus BHM's pairing is exactly {a_U,b_U}; it is not an extra choice of pairing or an assumption about direction labels. Conversely BHM pairs all twelve singular fibers. Each q_U therefore has exactly five surface double points p_{U,j}, 1≤j≤5, lying above it. Their two source preimages are the five paired vertices of F_{a_U} and F_{b_U}.

An ordering (a_U,b_U) consistently orients all five difference maps. Numbering the five vertices is unnecessary; no canonical numbering or basis is claimed.

## 3. Pushforward and the canonical difference injection

The elliptic fibration π is proper and flat, with connected reduced fibers and smooth total space. Thus π_*O_X=O_B. Its relative dualizing line bundle is

ω_{X/B}=ω_X⊗π*ω_B^{-1}=O_X(5F)=π*O_B(5).

Relative duality for this flat Gorenstein family gives R¹π_*O_X=O_B(-5); the higher direct images vanish because its fibers have dimension one. These statements can equivalently be obtained from the fundamental line bundle of the modular elliptic surface of Euler characteristic five. The section and reduced I5 fibers exclude multiple-fiber corrections.

Since ν and h are finite and gν=hπ,

R^i g_*(ν_*O_X)=h_*(R^iπ_*O_X).

Also R^i g_*T=0 for i>0: T is supported on finitely many points. Pushing forward the PR574 normalization sequence gives

0→g_*O_S→h_*O_B→g_*T→R¹g_*O_S→h_*O_B(-5)→0,       (5)

and R^i g_*O_S=0 for i≥2.

We identify the middle map without presuming the answer for g_*O_S. At q=q_U, orient the two branches by (a_U,b_U). A local section of h_*O_B pulls back to a function constant along each π fiber. At each of the five paired vertices its normalization quotient is therefore the same difference

f(a_U)−f(b_U).

After choosing residue coordinates on the five length-one summands of T, the map has the form

h_*O_B → k(q)^5,      f ↦ (d,d,d,d,d),    d=f(a_U)−f(b_U).       (6)

Reversing one quotient coordinate changes that entry's sign, not the map's intrinsic kernel or rank. The scalar difference map is surjective on the stalk: the semilocal normalization over q has distinct maximal ideals at a_U,b_U, so its residue map onto k(a_U)⊕k(b_U) is surjective by the Chinese remainder theorem. Equivalently the completed calculation is immediate in C[[s]]⊕C[[t]].

The normalization quotient of the ordinary nodal curve is

Q:=h_*O_B/O_Γ,      Q_q≅k(q).

Its local quotient map is exactly f↦f(a_U)−f(b_U). Hence (6) factors canonically as the quotient onto Q followed by an injection

ι:Q↪g_*T.                                                   (7)

This description is independent of the coordinate signs. Away from the six nodes both Q and g_*T vanish. Its kernel in h_*O_B is precisely O_Γ. Exactness of (5) proves g_*O_S=O_Γ, including its natural O_Γ-algebra structure. Thus the finite morphism in the Stein factorization of g is the identity.

Define K=coker(ι). At each q_U it is the quotient of a five-dimensional vector space by the one-dimensional diagonal difference image. Therefore it is annihilated by the maximal ideal, has dimension four, and has total length 24. Equation (5) becomes (2).

The sheaf h_*O_B(-5) is torsion-free of rank one on the integral curve Γ: a nonzero local function on Γ pulls back to a nonzero function on the normalization and acts injectively on its line bundle. Any torsion subsheaf of R¹g_*O_S consequently maps to zero in this quotient and lies in K. Conversely K has finite support and is torsion. This proves that K is exactly the maximal torsion subsheaf, not merely a length-24 subsheaf of it.

## 4. Scheme fibers, including the singular points

For q outside the six nodes, h is an isomorphism near q and its unique preimage is not a cusp. Normalization ν is an isomorphism near that entire smooth π fiber. Thus the scheme fiber g^{-1}(q) is a smooth elliptic curve of O_S(1)-degree five.

At q=q_U, the set-theoretic fiber consists of the images of F_a and F_b, where {a,b}={a_U,b_U}. We now check its scheme structure everywhere, not just its support.

At any point other than the five shared vertices, ν is an isomorphism and the base map factors through one branch of Γ. The maximal ideal of q pulls back to the local parameter of π at a or b. The corresponding I5 fiber is reduced, so the fiber is reduced at all these points.

At a shared vertex p, complete the rings. The nodal base and the transverse surface have completed rings

R=C[[s,t]]/(st),
A=C[[u1,u2]] ×_C C[[v1,v2]]
 =C[[u1,u2,v1,v2]]/(u_i v_j:1≤i,j≤2).

On the first normalization branch, s is a parameter of B at a and t vanishes; on the second, t is a parameter at b and s vanishes. Because each I5 fiber has two reduced transverse components at its vertex and the total elliptic surface X is smooth, local coordinates can be chosen with

s=u1u2,   t=v1v2

on their respective branches. Any invertible factors in these equations can be absorbed into one of the two coordinates. Thus the completed homomorphism is

s↦(u1u2,0),      t↦(0,v1v2).

It follows that the completed fiber ring is

A/(s,t) ≅ (C[[u1,u2]]/(u1u2)) ×_C (C[[v1,v2]]/(v1v2))
        ≅ C[[u1,u2,v1,v2]]/(u_i v_j,u1u2,v1v2).              (8)

The first displayed ring is a subring of the direct sum of two reduced nodal-curve rings, and hence is reduced. More explicitly it is the union of four coordinate axes with their common residue identified. Completion is faithfully flat, so reducedness of the completion implies reducedness of the algebraic fiber stalk. There is no hidden multiplicity in the scheme fiber.

The two pentagons intersect scheme-theoretically in exactly the five reduced points: in (8), quotienting by the sum of their branch ideals gives C. Consequently, if C_q=g^{-1}(q), there is the exact sequence

0→O_{C_q}→O_{F_a}⊕O_{F_b}→⊕_{j=1}^5 k(p_{U,j})→0,         (9)

with the last map the differences at paired vertices. Each pentagon is connected with arithmetic genus one and Euler characteristic zero. Their glued union is connected, and (9) yields

χ(O_{C_q})=0+0−5=−5,     h⁰(O_{C_q})=1,     h¹(O_{C_q})=6.

Thus p_a(C_q)=6. Each pentagon has degree five under O_S(1), so the reduced union has degree ten. Twisting (9) gives the fiber Hilbert polynomial

P_{C_q}(n)=10n−5,

whereas a smooth fiber has polynomial 5n. The morphism g is projective and O_S(1) is relatively ample. In a projective flat family its fiber Hilbert polynomial is locally constant. Every open neighborhood of a node in the integral curve Γ meets its smooth locus. The two distinct polynomials therefore prove that g is not flat over any q_U.

## 5. Scope and verification boundary

The results are structural consequences of the exact previously published primary geometry, normalization gluing, and residual curve. The only local calculations are universal fiber-product and semistable-fiber calculations. No actual coefficient, selected source point, matrix rank, or selected HM instance is evaluated. The argument does not assert a canonical splitting of R¹g_*O_S, a base-change isomorphism at the singular base, or any first-/higher-order target lift or algebraicity result.
