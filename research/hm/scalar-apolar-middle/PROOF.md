# Complete scalar apolar Hilbert function and minimal generators

## Result

For the net T=im Ψ*⊂S₅* of the audited finite-normalizer quintic pairing, let I=Ann_S(T) and A=S/I. Then

    H_A=(1,5,15,25,15,3),    length(A)=64,
    I₃≅V₁⊗W′,              dim I₃=10.

The scalar ideal has exactly ten minimal cubic generators and fifteen minimal quartic generators, and no others. Their representations are

    G₃=V₁⊗W′,    G₄=V⊗χ₃.

The linear syzygies among the scalar cubics form V⊗W′, of dimension ten. These statements concern the scalar ideal, not the vector-valued relation module presenting the middle cohomology module.

No selected HM, source, cofactor, Ψ coefficient, or rank instance is evaluated.

## 1. Inputs and conventions

Work over C with S=Sym X, X=V*, dim X=5. All representations refer to the specified finite normalizer N=H₅⋊SL₂(F₅), not a continuous SL₂ action. The following are imported from the audited proofs ../apolar-middle-module/PROOF.md and AUDIT.md and ../middle-module-relations/PROOF.md and AUDIT.md:

- T≅χ₃′ is a three-dimensional nonzero subspace of S₅*.
- I=Ann_S(T) is the faithful scalar annihilator of the actual middle module.
- I₀=I₁=I₂=0, dim A₄=15, dim A₅=3, and A_d=0 for d≥6.
- The first contraction δ₁:X⊗T→S₄* is injective.
- S₂=V₃⊗χ₃′ and S₃=V₁⊗(χ₅⊕W′), with V₃=V₁*.
- W′, χ₃′, and χ₅ are self-dual irreducible quotient-group representations.

The symmetric-cube identity is the dual of Horrocks–Mumford Lemma 3.3(vi), already recorded and audited in middle-module-relations. The source is Horrocks and Mumford, Topology 12 (1973), 63–81, https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf . The appendix gives

    χ₃′⊗χ₃′=1⊕χ₃′⊕χ₅.

For clarity, Λ²χ₃′=χ₃′ and Sym²χ₃′=1⊕χ₅. These can equally be checked by the symmetric/exterior square character formulas on that finite character table. The H₅-isotypic evaluation equivalence shows that V₃ tensored with each of these quotient irreducibles is irreducible for N, and preserves their inequivalence.

Write D_d=S_d*. For a∈S_e and f∈D_d, contraction means (a⌟f)(b)=f(ab). No factorial convention is required.

## 2. The scalar middle rank is forced by representations

Consider second contraction

    δ₂:S₂⊗T→D₃,   a⊗f↦a⌟f.

It is N-equivariant. Its source and target are

    S₂⊗T = V₃⊗(1⊕χ₃′⊕χ₅),
    D₃    = V₃⊗(χ₅⊕W′).

The sole common irreducible is V₃⊗χ₅, occurring once on each side. Thus δ₂ either vanishes or maps this 25-dimensional summand isomorphically to the identical target summand, killing the other source summands.

The zero alternative is impossible. If δ₂=0, then f(ab)=0 for every a∈S₂, b∈S₃, f∈T. Products S₂S₃ span S₅, so every f∈T would vanish identically, contradicting dim T=3. Therefore

    im δ₂=V₃⊗χ₅,    ker δ₂=V₃⊗(1⊕χ₃′).

By the definition of apolar annihilation, im δ₂=I₃^⊥⊂D₃. Hence A₃*=V₃⊗χ₅, and the complementary summand in S₃ is exactly

    I₃=V₁⊗W′.

This identifies the actual invariant subspace, not just its dimension: the symmetric cube is multiplicity-free. It proves dim A₃=25 and dim I₃=10. Combining with the imported entries gives the announced Hilbert function, whose sum is 64.

## 3. Exactly fifteen minimal quartics

Let G_d=I_d/(X I_(d−1)); this is the space of minimal degree-d ideal generators. Since there are no relations below degree three, G₃=I₃ has dimension ten. Also dim I₄=70−15=55. If K=ker[X⊗I₃→I₄] and k=dim K, the source has dimension 50 and therefore

    dim G₄=55−(50−k)=5+k.

We determine k structurally. The primary source Lemma 3.3(vii), printed p.70, states Sym⁴V=V*⊗(χ₄⊕Q⊕χ₃⊕χ₃′), where Q=χ₄# is the spinorial four-dimensional representation and χ₄ is the nonspinorial one. Dualizing gives

    S₄=V⊗(χ₄⊕Q⊕χ₃⊕χ₃′).

Since A₄*=X⊗T=V*⊗χ₃′, the ideal component is

    I₄=V⊗(χ₄⊕Q⊕χ₃).

For the source, use X⊗V₃=V₁⊗(χ₃⊕W′) from Lemma 2.4(ii). In source conventions θ(ζ)=ζ² and V_i=θ^iV, with V_i*=V_(i+2). Applying θ and then dualizing yields X⊗V₁=V⊗(χ₃′⊕W): θ interchanges W,W′ and χ₃,χ₃′. The appendix products χ₃′⊗W′=W′⊕Q and W⊗W′=χ₄ now give

    X⊗I₃=V⊗(W′⊕Q⊕χ₄).

Thus multiplication can be nonzero only on two multiplicity-one common irreducibles, V⊗Q and V⊗χ₄, of dimension twenty each. Its image dimension belongs to {0,20,40}.

We use a strict universal scalar polynomial-shadow inequality: for a nonzero proper subspace L⊂S_d with n≥2 and d≥1,

    dim(XL)/dim S_(d+1) > dim L/dim S_d.

Here is a proof including strictness. Pass to the degree-d leading monomial set B of L. A uniform degree-d exponent vector a, followed by incrementing coordinate i with probability (a_i+1)/(n+d), produces a uniform degree-(d+1) exponent vector. Hence the shadow C has |C|/dim S_(d+1)≥|B|/dim S_d. Equality would require that no exponent outside B can increment into C. Every degree-d predecessor of every element of C would then lie in B. The bipartite degree-d/degree-(d+1) divisibility graph is connected: moving one exponent unit from coordinate i to j connects two degree-d monomials through a common degree-(d+1) multiple, and such moves connect all degree-d monomials. Thus equality forces B empty or all, contrary to the hypotheses. Leading monomials of XL contain C, proving the strict inequality for L itself. This is universal polynomial algebra, not an instance evaluation.

Apply it to I₃, of dimension 10 in S₃ of dimension 35. It yields dim(XI₃)>70·10/35=20. Both twenty-dimensional blocks must therefore be isomorphisms, giving

    XI₃=V⊗(Q⊕χ₄),    dim(XI₃)=40,
    K=V⊗W′,          dim K=10,
    G₄=V⊗χ₃,         dim G₄=15.

The space K is precisely the linear syzygy space among the ten scalar cubic generators.

## 4. Injective first derivatives exclude sextic generators

Since I₅^⊥=T, orthogonal complements identify

    (XI₅)^⊥={f∈D₆ : x⌟f∈T for every x∈X}.

Take f in this space, and write t_x=x⌟f∈T. Contractions commute, so for all x,y∈X,

    δ₁(x⊗t_y)=x⌟t_y=y⌟t_x=δ₁(y⊗t_x).

Injectivity of δ₁ gives x⊗t_y=y⊗t_x in X⊗T. When x and y are independent, applying a functional on X which is one on x and zero on y gives t_y=0; reversing their roles gives t_x=0. Every nonzero x has an independent partner, hence all t_x vanish. Since contraction by X detects a nonzero sextic (products XS₅ span S₆), f=0.

Thus (XI₅)^⊥=0 and XI₅=S₆=I₆. Every degree above six is obtained by multiplying S₆, so no minimal generators occur in degrees six or above. This is an exact structural exclusion, using the already established injectivity of first derivatives rather than any sextic rank computation.

## 5. There are no minimal quintics

We now close the remaining generator possibility. The strict shadow inequality applies to I₄, a nonzero proper 55-dimensional subspace of S₄ of dimension 70. Thus

    dim(XI₄)>126·55/70=99,
    dim G₅=123−dim(XI₄)≤23.

We show G₅ has no H₅-invariants. The imported quintic representation is S₅^H₅=χ₃⊕χ₃′, whereas A₅≅T*=χ₃′; hence I₅^H₅=χ₃. Split S₄=I₄⊕A₄ equivariantly. Full polynomial multiplication X⊗S₄→S₅ is surjective. But

    (X⊗A₄)^H₅=(V*⊗V⊗χ₃′)^H₅=χ₃′.

Since finite-group invariants are exact and χ₃,χ₃′ are inequivalent, the χ₃ invariant summand of S₅ must be reached from X⊗I₄. Its image lies in I₅, so (XI₄)^H₅=I₅^H₅ and G₅^H₅=0.

The center μ₅ of H₅ acts trivially in total degree five, so G₅ restricts to a sum of characters of H₅/μ₅≅(F₅)². The normalizer quotient SL₂(F₅) acts transitively on the 24 nontrivial characters. Consequently their multiplicities in any N-module are equal; an N-module with no H₅-invariants is either zero or has dimension at least 24. Since dim G₅≤23, necessarily

    G₅=0,    XI₄=I₅.

Together with Section 4, this proves that I is minimally generated by precisely the ten cubics and fifteen quartics already identified.

## 6. Level structure and Hilbert-numerator checks

A is a level Artinian algebra of socle degree five and type three. Indeed if 0≠[a]∈A_d with d<5, the definition of I provides f∈T and b∈S_(5−d) with f(ab)≠0. Writing b as a linear combination of products of linear forms shows some such product does not kill [a]; therefore [a] cannot be killed by every linear form. Thus there is no lower-degree socle, whereas A₅ has dimension three and is annihilated by X.

The Hilbert numerator is

    (1−t)⁵ H_A(t)
      =1−10t³−5t⁴+52t⁵−45t⁶−10t⁷+20t⁸−3t¹⁰.

Its degree-four coefficient confirms β_(1,4)−β_(2,4)=15−10=5. The first free module is therefore S(−3)¹⁰⊕S(−4)¹⁵, and β_(2,4)=10. The endpoint of the minimal S-resolution is S(−10)³, reflecting the three-dimensional degree-five socle in five variables. There is no asserted self-duality of this type-three algebra, and the Hilbert numerator does not by itself determine the remaining Betti numbers.

## Boundary

The previously open scalar Hilbert entry and all scalar ideal generator degrees, numbers, and representations are completely determined. Higher scalar syzygies remain undetermined beyond the stated linear cubic syzygies and resolution endpoint. The separate vector-valued quadratic/cubic relation problem is not settled by these scalar results. No cofactor transversality, source nonvanishing, physical obstruction, or selected multiplication-rank assertion follows. The proof uses static audited inputs, finite representation identities, universal contraction arguments, and local file writes only.
