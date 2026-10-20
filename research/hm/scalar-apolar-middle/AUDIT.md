# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-apolar-syzygies-PUBLICATION-CHECK.md](../hm-apolar-syzygies-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit: scalar apolar Hilbert function and exact ideal generators

## Verdict

The scalar apolar algebra and generator statements are correct, conditional on the explicitly imported audited geometric and finite-normalizer inputs. In particular:

- The Hilbert function is exactly (1,5,15,25,15,3), of length 64.
- The scalar ideal has ten minimal cubic generators, forming V₁⊗W′.
- Their linear syzygies form V⊗W′ and have dimension ten.
- The ideal has exactly fifteen minimal quartic generators, forming V⊗χ₃.
- There are no minimal generators in degrees five or higher.
- The algebra is level of socle degree five and type three.

The full minimal free resolution is not determined by these statements or by the Hilbert numerator alone. These are scalar ideal results, distinct from the vector-valued relation module of the middle-cohomology module.

## 1. Audited dependencies and primary character checks

I read both the proof and independent audit in ../apolar-middle-module and ../middle-module-relations, as well as ../quintic-pairing-representation/PROOF.md. The imported facts needed here are the exact scalar annihilator I=Ann_S(T), T≅χ₃′⊂S₅*, its dimension three, absence of scalar annihilators below degree three, injectivity of δ₁:X⊗T→S₄*, and the already known Hilbert entries outside degree three.

For the additional degree-four identities I read the original Horrocks–Mumford paper, Topology 12 (1973), 63–81:

https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Lemma 3.3(vii), printed page 70, gives Sym⁴V=(χ₄⊕χ₄#⊕χ₃⊕χ₃′)⊗V*. Here χ₄#=Q is the spinorial four-dimensional representation; χ₄ is the other four-dimensional representation. All these quotient characters are self-dual. Hence

    S₄=V⊗(χ₄⊕Q⊕χ₃⊕χ₃′).

The Galois convention is relevant and checks precisely. In §1, θ(ζ)=ζ² and V_i=θ^iV, with V_i*=V_(i+2), subscripts modulo four. Thus X=V*=V₂. Starting from Lemma 2.4(ii),

    X⊗V₃=V₁⊗(χ₃⊕W′),

apply θ to obtain V₃⊗V=X⊗(χ₃′⊕W), then dualize to obtain

    X⊗V₁=V⊗(χ₃′⊕W).

The same Galois action interchanges W and W′ and interchanges χ₃ and χ₃′. The appendix tensor identities used in the argument are

    χ₃′⊗χ₃′=1⊕χ₃′⊕χ₅,
    χ₃′⊗W′=W′⊕Q,
    W⊗W′=χ₄.

These preserve the distinction between the two four-dimensional representations. The finite Heisenberg-isotypic evaluation equivalence makes V, V₁ or V₃ tensored with each irreducible quotient representation irreducible for N, preserving inequivalence. No continuous SL₂ action is presumed.

## 2. Exact degree-three scalar apolar quotient

The second contraction δ₂:S₂⊗T→S₃* is equivariant. Its source is V₃⊗(1⊕χ₃′⊕χ₅) and its target is V₃⊗(χ₅⊕W′). The sole common irreducible is V₃⊗χ₅, with multiplicity one and dimension 25.

The map cannot vanish: if it did, every f∈T would vanish on every product S₂S₃, which spans S₅. This contradicts T≠0. Semisimplicity and Schur's lemma therefore identify its image with the entire common summand and its kernel with V₃⊗(1⊕χ₃′).

The annihilator-orthogonal description im δ₂=I₃ perpendicular is exact: p∈S₃ is orthogonal to every second derivative precisely when f(ap)=0 for all a∈S₂ and f∈T, which is the definition of p∈I₃. Duality gives A₃=V₁⊗χ₅ and I₃=V₁⊗W′. In particular dim A₃=25 and dim I₃=10. The announced full Hilbert function and length follow immediately.

## 3. Strict scalar polynomial-shadow bound

The strict form of the normalized shadow inequality is valid for every nonzero proper scalar subspace L⊂S_d:

    dim(XL)/dim S_(d+1) > dim L/dim S_d.

Here the applications have five variables and positive d. Take a leading-monomial set B of L; it is nonempty and proper, and its shadow lies in the leading-monomial set of XL. A uniform degree-d exponent vector a followed by incrementing coordinate i with probability (a_i+1)/(n+d) has uniform degree-(d+1) output b. Consequently the normalized shadow size is at least the normalized size of B.

For strictness, equality would mean no positive-probability transition from outside B into its shadow. Hence every degree-d predecessor of each shadow monomial must itself belong to B. But the graph on degree-d monomials that joins two monomials sharing a degree-(d+1) multiple is connected: one may move a unit of exponent from any nonzero coordinate to any other coordinate, one step at a time. Membership in B would therefore propagate from any one member to all degree-d monomials, contradicting properness. The inequality is strict already for the monomial shadow and hence for XL.

This is a universal scalar polynomial argument. It neither evaluates a selected polynomial subspace nor assumes the same strictness for arbitrary free-module subspaces with different occupied components.

## 4. Exact quartic generators and linear cubic syzygies

Injectivity of δ₁ identifies A₄* with X⊗T, so A₄=V⊗χ₃′. The degree-four decomposition above then gives

    I₄=V⊗(χ₄⊕Q⊕χ₃).

Combining the exact cubic module with the tensor identities gives

    X⊗I₃=V⊗(W′⊕Q⊕χ₄).

For the multiplication map to I₄, the W′ summand must die because the target has no isomorphic constituent. The remaining two common irreducible blocks each have dimension twenty, each with multiplicity one. Therefore the rank can only be 0, 20 or 40.

Strict shadow gives dim XI₃>70·10/35=20, so its rank is exactly forty. Its kernel is V⊗W′, of dimension ten, and its image is V⊗(Q⊕χ₄). The quotient I₄/XI₃ is consequently V⊗χ₃, of dimension fifteen. This proves the exact quartic generator number and representation; it does not merely bound them.

## 5. Exclusion of minimal quintic generators

Since dim I₄=55 and dim S₄=70, strict shadow gives dim XI₄>126·55/70=99. Thus G₅=I₅/XI₄ has dimension at most 23.

The H₅-invariant part of S₅ is χ₃⊕χ₃′, and A₅=χ₃′, so I₅^H₅=χ₃. Choose an N-equivariant splitting S₄=I₄⊕A₄. Ordinary polynomial multiplication X⊗S₄→S₅ is surjective, including on H₅ invariants because finite-group invariants are exact. Meanwhile

    X⊗A₄=(X⊗V)⊗χ₃′=(1⊕Z)⊗χ₃′,

where Z has no H₅ invariants. Thus its invariant part is χ₃′ and cannot reach the inequivalent χ₃ target. That entire target must be reached from X⊗I₄. It follows that (XI₄)^H₅=I₅^H₅ and G₅^H₅=0.

The H₅ center acts trivially in total polynomial degree five, so G₅ restricts to a sum of characters of H₅/μ₅. Its trivial character is absent. The 24 nontrivial characters form one N-orbit, and N-stability makes their multiplicities equal. Therefore any nonzero G₅ has dimension at least 24, indeed divisible by 24. This contradicts the upper bound 23, proving G₅=0.

The strict inequality is essential: the non-strict bound alone would allow a 24-dimensional quotient. Likewise the invariant-sector argument is essential to exclude smaller representations factoring through N/H₅.

## 6. Exclusion of sextic and higher generators

The perpendicular space to XI₅ consists of sextic functionals f whose first derivatives t_x=x contraction f all lie in T. Commuting contractions gives

    δ₁(x⊗t_y)=δ₁(y⊗t_x).

Injectivity of δ₁ then gives x⊗t_y=y⊗t_x. For independent x,y, applying dual functionals on X separately forces both t_x and t_y to vanish. Each x has an independent partner, so all first derivatives vanish. Products XS₅ span S₆, so f itself vanishes.

Thus XI₅=S₆=I₆. Multiplication by further linear forms generates every higher degree, so there are no minimal ideal generators in degrees six or higher. Together with G₅=0 and the exact degree-three/four calculations, this proves that I is generated exactly by its ten cubic and fifteen quartic minimal generators.

## 7. Socle and numerical checks

For a nonzero class a∈A_d with d<5, apolarity supplies f∈T and b∈S_(5−d) with f(ab)≠0. If every linear form killed a, then every positive-degree polynomial, including b, would kill a, a contradiction. There is therefore no lower-degree socle. The top A₅ has dimension three and is entirely socle, proving level type three and socle degree five.

Direct coefficient arithmetic gives

    (1−t)⁵H_A(t)
      =1−10t³−5t⁴+52t⁵−45t⁶−10t⁷+20t⁸−3t¹⁰.

The degree-four coefficient agrees with fifteen quartic generators and ten degree-four first syzygies: −15+10=−5. The final free module of the minimal resolution is S(−10)³ by the degree-five socle in five variables. No self-duality of the type-three algebra follows, and the numerator does not determine all remaining Betti numbers or exclude higher equal-degree ghost terms.

## Scope

This audit used static proof reads, primary finite-representation source reading, universal polynomial-shadow and contraction arguments, small formal Hilbert-numerator arithmetic, and this local audit-file write. It made no external writes and selected or evaluated no HM, source, cofactor, Ψ coefficient, polynomial instance, point, jet or rank instance. No selected-instance computation or large computation was performed. All inherited geometric and representation dependencies remain explicit. No source nonvanishing, cofactor transversality or physical obstruction value is inferred.

## Reviewed proof fingerprint

The complete strengthened PROOF.md was read after revision, including its strict-shadow proof, exact quartic calculation, and quintic-generator exclusion. No mathematical correction was required.

SHA-256: 7f4f532730d7e4436e654819343423f9f393bf2927987446dd406181bfbeea31.
