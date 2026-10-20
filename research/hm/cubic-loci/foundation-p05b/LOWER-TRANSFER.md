# Lower-weight HM target and canonical image alternatives

## Result and scope

Let Z=U0=H¹(End H), V=U1=H¹(End H(−1)), and J1=H²(End H(−1)). With the usual left action of N=H5⋊G, G=SL2(F5), the literal equivariant Euler complex proves

    J1 ≅ V⊗W′,

where W′ is the other irreducible two-dimensional G-module. In particular J1 is irreducible of dimension ten. Every canonical ordered downstairs operation m001, m010, m100 therefore has linear image zero or J1. Its retained positive coefficient transfer has image zero or the entire canonical four-dimensional lower filtered detector subspace. Neither alternative is selected here.

Subject only to N-equivariance, outer reversal, and cyclic zero, the compatible family of these three orderings has eight parameters:

    dim Hom_N(Z⊗Z⊗V,J1)=8.

Section 7 computes its actual two-Z-slot decomposition as four symmetric and four alternating parameters.

This does not assert realization, nonzero values, or exclusion of additional geometric identities. The full N action is used only downstairs; no N action on the coefficient cover or physical source is asserted.

## 1. Imported inputs and ordinary twist conventions

Use the audited literal equivariant complex and N-linearizations in [the full hm image symmetry manuscript](../../full-hm-image-symmetry/PROOF.md), the natural identifications U0=End0(V), U1=V and permutation multiplicity proof in [the equivariant massey multiplicity manuscript](../foundation-p05/ELIGIBLE-MULTIPLICITY.md), and strict filtered cohomology and ordered cup vanishings in [the weight two massey manuscript](../foundation-p04/WEIGHT-TWO-TRANSFER.md). The retained lower filtration and involution dimensions are in [the filtered massey target manuscript](../foundation-p04/FILTERED-TARGET.md) and AUDIT.md.

Write A=V1 and T=Sym²W. The literal complex has coefficients

    K−1=A⊗O(−1),  K0=A*⊗T⊗O,
    K1=V*⊗W⊗O(1), K2=W⊗O(2).

W is self-dual with determinant one; T is self-dual. The primary source is Horrocks–Mumford, Topology 12 (1973), 63–81:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
Its §§1–2 define the Galois-conjugate modules Vi=θ^iV, θ(ζ)=ζ², with Vi*=Vi+2; W has character χ2 and W′=θW. Its Lemma 3.3(v) and §2 give Sym²V=A⊗Sym²W′ and Λ²V=A⊗W. The appendix identifies W and W′ as irreducible, with characters conjugated by θ; θ² fixes their characters. These are representation identities from the primary source, not End-cohomology assertions.

## 2. Literal equivariant Euler cancellation

Set U^r=⊕i Hom(K_i coefficients,K_(i+r) coefficients). At twist −1 the sheaf in internal degree r is U^r⊗O(r−1). All r≤0 are acyclic: their twists range from −4 to −1. Only r=1,2,3 remain, with H⁰ coefficients 1,V*,Sym²V*, respectively. There is no negative H⁴ endpoint at this twist. Thus, in the representation ring of N,

    χ(End H(−1))=−U¹+U²⊗V*−U³⊗Sym²V*.

The actual Hom coefficients are

    U¹=(A*)²⊗T ⊕ A⊗V*⊗T⊗W ⊕ V⊗W²,
    U²=A*⊗V*⊗W ⊕ A⊗T⊗W,
    U³=A*⊗W.

Substitution cancels the A⊗V*⊗T⊗W terms. Using (V*)²−Sym²V*=Λ²V*=A*⊗W gives

    χ=(A*)²⊗(W²−T)−V⊗W²
      =(A*)²−V⊗(1⊕T).

The independent cohomology row has only H¹ and H² at twist −1. Its natural identification H¹=V consequently yields

    [J1]=[(A*)²]−[V⊗T].

Apply θ³ to the primary identities for Sym²V and Λ²V. Since θ³V=A*, θ³A=V, θ³W=W′, and θ³(Sym²W′)=Sym²W=T, this gives the actual decomposition

    (A*)² = Sym²(A*) ⊕ Λ²(A*)
           ≅ (V⊗T) ⊕ (V⊗W′).

Therefore [J1]=[V⊗W′]. Complex representations of the finite group N are semisimple, so equality of classes determines the actual representation J1≅V⊗W′. This use of Euler additivity does not evaluate any differential or infer a module from its dimension.

V restricts irreducibly to H5. Evaluation identifies every H5-isotypic representation of this central character with V tensored by its G-multiplicity module. Consequently V⊗W′ is N-irreducible because W′ is G-irreducible. This proves the target assertion. The ordinary twist−1 central character is c, matching U1=V; all representations and maps convert together in the opposite pullback convention.

## 3. Canonical lower operations and zero indeterminacy

The strictness proof in [the weight two massey manuscript](../foundation-p04/WEIGHT-TWO-TRANSFER.md) §2 proves every ordered cup product U0·U0, U0·U1, U1·U0 is zero. Its reasoning is important: full K·K=0 and injection of filtered H² imply zero in the requisite filtered complex; passing to its symbol and using coefficient multiplication 1·v=v proves the mixed downstairs vanishings. The level-zero inclusion is also injective, by the Reynolds unit retraction or bundle splitting.

For (p,q,r) a permutation of (0,0,1), take representatives in the twist-graded End algebra and adjacent primitives in twists −(p+q), −(q+r). Set

    m_pqr(a,b,c)=[α h_bc+h_ab γ] ∈ J1.

All required adjacent products vanish. The indeterminacy is

    a·H¹(End H(−q−r)) + H¹(End H(−p−q))·c.

Every term is an ordered mixed U0/U1 product and is zero. Explicitly, for 001 the terms are U0·U1 and U0·U1; for 010 they are U0·U1 and U1·U0; for 100 they are U1·U0 and U1·U0. The familiar boundary correction identities for replacing representatives respect twists. Thus each operation is canonical, trilinear, natural, and has zero indeterminacy; it is not a selected minimal-model operation.

N-equivariance follows by transforming defining systems and using uniqueness of the output class. Its linearized image is an N-submodule of the irreducible J1, hence zero or all ten dimensions. This applies separately to each ordering, although the identities below relate them.

## 4. Exact lower transfer and retained dimension

Let C1 denote the degree-one coefficient-generator module, avoiding confusion with the historical module A=V1. Canonically C1=3[31]⊕[22]. For a,b∈K0=U0 and a third class with symbol v⊗u∈C1⊗U1, filtered primitives exist in levels equal to the sums of adjacent weights. In particular a pair of K0 inputs has a level-zero primitive. Projection of the defining system to gr1 gives

    gr1 M(a,b,lift(v⊗u)) = v⊗m001(a,b,u),

and the corresponding formula in the other two orderings. Comparing with factorized downstairs primitives is legitimate because their differences are closed and the mixed cup products above vanish. No multiplicative splitting is needed.

Changing the lift adds a K0 input; the resulting difference lies in H²(End H), whose [22] projection is zero. Since the retained filtration-zero subspace is zero, its level-one target identifies canonically with the retained part of gr1 T. Thus the projected formula describes the actual lower filtered detector, not merely an arbitrary choice of a leading representative. Its image for a fixed ordering is precisely

    L⊗e_+ im(m_pqr),

where L is the nonzero D8-trivial line in [22]. The coefficient line is inversion-positive and the stipulated twist−1 target has involution trace −2, hence positive dimension four. Therefore each lower ordered retained image is either zero or the entire four-dimensional canonical subspace Tret,≤1. No complement in the twelve-dimensional target is selected. Nothing here asserts that all other triples have no lower component.

## 5. Eight symmetry-eligible parameters

Let F(a,b,u)=m001(a,b,u), a,b∈Z, u∈V. Outer reversal and cyclic zero are equivalent on these weight patterns to

    m100(u,b,a)=F(a,b,u),
    m010(a,u,b)=−F(a,b,u)−F(b,a,u).

Conversely any trilinear F defines a compatible triple by these formulas; no symmetry in the two Z slots is imposed on F itself. Thus the eligible family is Hom_N(Z⊗Z⊗V,V⊗W′).

As proved using character-line projectors in the multiplicity proof, the G-module

    R=Hom_H5(V,Z⊗V)

is the permutation module on the 24 nonzero vectors of F5², hence C[G/P] for a unipotent subgroup P of order five. The same proof uses End0(V) directly here. Evaluation gives Z⊗V≅V⊗R. Applying it twice, while keeping the two Z inputs ordered, gives

    Z⊗Z⊗V ≅ V⊗R⊗R.

Consequently the intertwiner space is Hom_G(R⊗R,W′). The induced-module tensor identity and Frobenius reciprocity identify it with

    Hom_P(R|P,W′|P).

For P acting on nonzero vectors (x,y), its nonidentity generator acts as (x,y)↦(x+y,y), after a choice of basis. The four vectors with y=0 are fixed; for each of the four nonzero y, the five x values form one regular orbit. This is a symbolic orbit decomposition, not an evaluated representation matrix. Therefore

    R|P ≅ 4·1 ⊕ 4·C[P].

The primary character table gives W′|P=χ^b⊕χ^(−b), b≠0 mod 5. Each regular summand contributes two dimensions and each trivial summand contributes none. Hence

    dim Hom_N(Z⊗Z⊗V,J1)=8.

Equivalently each of the four regular orbits contributes two one-dimensional weight components after choices of generator and eigenvectors. This is an abstract eight-component certificate, not a calculation of the actual operation. Any nonzero eligible F has full ten-dimensional image by irreducibility, and retained four-dimensional image. The middle ordering depends only on the symmetric part in the two Z slots; this argument alone does not compute the symmetric/alternating multiplicity split, since the twice-applied evaluation isomorphism does not identify that slot swap with the naive swap of R factors. Section 7 computes the split by a different, slot-compatible identification.


## 6. Conditional full twelve-dimensional retained span

Let I be the linear span of all full retained upstairs M-values in Tret, and L=Tret,≤1 its canonical four-dimensional subspace. If m001 is nonzero, Section 4 gives L⊂I. If m011 is nonzero, the audited upper-weight irreducibility and coefficient-transfer theorem gives that I→Tret/L is surjective, with quotient dimension eight. For any t∈Tret choose i∈I with the same quotient class; then t−i∈L⊂I. Hence I=Tret, of dimension twelve.

This argument uses a subspace and quotient and requires no canonical direct-sum splitting. Thus one nonzero lower downstairs value and one nonzero upper downstairs value would suffice for full retained span. Under the established perfect sign-valued Serre pairing, this would separate the full twelve-dimensional retained physical sector. Neither nonzero value is supplied, and no verdict about an actual physical obstruction or residual is inferred. The converse is not claimed: other input-weight channels could also contribute to the full retained image.

## 7. Phase-sensitive slot split: four symmetric and four alternating

The unresolved split mentioned in §5 can in fact be computed without assuming that the iterated R-factor identification preserves the flip. Tensor-Hom adjunction, which does preserve the two Z slots, gives

    Hom_N(Z⊗Z⊗V,V⊗W′)
      ≅ Hom_N(Z⊗Z,End(V)⊗W′)
      ≅ Hom_N(Z⊗Z,(1⊕Z)⊗W′).

Use the canonical Heisenberg section ω(1,x), x∈F5², from the primary paper §1. Write E_x for its operator on V. The E_x are the distinct H5/C-character lines of End(V), with E_0=Id, and Z is spanned by the E_x for x≠0. For the canonical semidirect complement G, its lifts implement the automorphisms ω(α,x)↦ω(α,gx). Therefore

    g E_x g^(−1)=E_(gx).

There is no phase in this action. A scalar ambiguity in the lift cancels in conjugation. This is an abstract group/representation identity, not a construction or evaluation of actual matrices. The alternating commutator pairing identifies vector labels with H5/C-character labels equivariantly, so the character of E_x⊗E_y is labeled by x+y.

In the zero-character sector, Z⊗Z is spanned by E_x⊗E_(−x), x≠0, and G permutes this basis exactly as R=C[G/P]. Its contribution to the displayed Hom space is Hom_G(R,W′), which vanishes because W′ has no P-invariants. Thus the entire zero-character sector contributes neither symmetric nor alternating intertwiners.

The remaining character sectors form one G-orbit. Fix a nonzero sum s. Its G-stabilizer P is order five, and its source character space has basis

    E_x⊗E_(s−x),   x∈F5²\{0,s}.

The target character space is E_s⊗W′. P fixes E_s exactly, by the phase-free conjugation identity. Hence restriction to this source character space identifies all nonzero-character intertwiners with P-intertwiners from the permutation module on the 23 displayed x-values to W′. The actual Z-slot flip is exactly

    x ↦ s−x.

It commutes with P. Choose vector coordinates s=(1,0), with a generator of P acting by (a,b)↦(a+b,b). Among the permitted x, the b=0 sector has three fixed points a∈F5\{0,1}. All its representations are P-trivial, so it contributes no maps to W′ in either flip parity. The four b≠0 sectors are regular P-orbits. The actual flip sends b to −b and pairs these four orbits into two pairs. Each such pair, with its equivariant exchanging involution, has one regular P-module in each of its ± eigenspaces: explicitly the maps v↦v±flip(v) identify one orbit module with those eigenspaces. Therefore the nontrivial-character source has two regular P-modules in each slot parity, aside from the irrelevant trivial modules.

Since dim Hom_P(C[P],W′)=dim W′=2, this proves

    dim Hom_N(Sym²Z⊗V,J1)=4,
    dim Hom_N(Λ²Z⊗V,J1)=4.

This calculation includes the actual slot permutation and removes the phase ambiguity rather than imposing a naive swap on R⊗R. The total agrees with the independent eight-parameter calculation. Consequently m010=−2F_sym: its vanishing removes exactly the four symmetry-eligible symmetric parameters, leaving four alternating parameters. This is a statement about the eligible parameter space; it neither proves m010 vanishes nor shows that any of the remaining parameters is realized geometrically.
