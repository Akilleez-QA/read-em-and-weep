# No reverse c-d-f chain map survives the invariant and all negative quadratics

## Result

Assume an actual source127 c-d-f occurrence and one-sided preservation Q(X_B)⊂Y_B. Let S=[X_B→Y_B] and T=[X_F→Y_F⊕Y_L] be the actual subcomplex and quotient for Q+tT_a, with a∈Sym²W arbitrary. Then

    Hom_G((T,Q_T,{T_a,T}),(S,Q_B,{T_a,B}))=0.

Here a morphism is a parameter-independent endpoint pair (f₂,f₄), independent of t and a, intertwining Q and EVERY negative quadratic. No middle-degree extension is assumed.

For the negative quadratics ALONE the reverse Hom space is instead exactly

    Hom_G(Y_L,Y_B)=Hom_G(V+P,V+2P+2D), dimension3.

Every nonzero member has f₂=0, kills Y_F, and fails to extend to the full negative linear pencil. Thus even-data reconstruction is false without qualification. The new theorem proves the precise extension lemma on the F component, classifies the entire lost target-only ambiguity, and shows actual invariant-product generation kills that ambiguity.

In particular there is no reverse two-term map with nonzero D cohomology action that could furnish the radical-style κ-naturality used in other branches. This is an exclusion of that map mechanism, not of the c-d-f source, one-sided preservation, or any cubic value.

## Immutable inputs and conventions

- PR924, c6c25eaf0e5a67c27eee7c3ba4f000df55997692, research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md, blob83f5aee293995257459229e6b323522224ce8f3d: simultaneous original negative linear arrows, covariant reconstruction, exact block bundles, full represented algebra including singular maps.
- PR935, a7707ba3e25592023eb69cc15686aa4ee1fdcb7c, research/hm/profile11-source127-cdf-bockstein-rigidity/PROOF.md, blob187fe2a8c1499e11afdb5002091aa3c144e1b4a3: actual generation Y=im Q+im q₋ (using its pinned PR925/933), for the SAME invariant Q and negative quadratic aggregate.
- PR1001, a7aa990e7705dd9dbf3d0fd34e437fa735c9e0f1, research/hm/cdf-preserved-b-symbol/PROOF.md, blobeebebae694f59e786aaebc64c3838d732b2a3832: actual one-sided subcomplex and quotient conventions. Only their existence is needed here, not its internal symbol calculation.

Exact originals are copied and authenticated in INPUTS.json. All representations and maps below are actual marked blocks or universal formal maps. No selected actual datum is evaluated.

Write the negative linear pencil on each block i as

    A_l^i:N₂,i→N₃,i, B_l^i:N₃,i→N₄,i,
    B_m^i A_l^i=B_l^i A_m^i, l,m∈W.

The quadratic action is T_(lm)^i=B_m^i A_l^i. Over characteristic zero every such bilinear product is recovered from the full Sym²W family, including mixed products by polarization. Commuting with every square consequently means commuting with every pair (m,l), not just two chosen squares.

## 1. A precise endpoint-to-middle reconstruction lemma

Let M,N be two such linear pencils. Assume

    W⊗M₂ --A--> M₃ is onto,                    (G)
    N₃ --(B_u,B_v)--> N₄⊕N₄ is injective.     (J)

Suppose f₂:M₂→N₂ and f₄:M₄→N₄ intertwine all quadratic products. There is a UNIQUE f₃:M₃→N₃ intertwining both linear arrows.

Define it on generators by

    f₃(Σ_i A_li^M x_i)=Σ_i A_li^N f₂(x_i).

If the source sum is zero, apply B_m^N to the proposed target sum. Quadratic intertwining gives

    Σ_i B_m^N A_li^N f₂(x_i)
      = f₄ Σ_i B_m^M A_li^M x_i = 0

for every m. Condition (J) makes the target sum zero. Thus the definition is well-defined. Surjectivity (G) gives existence everywhere and uniqueness. The first intertwining equation holds by definition; the second holds on every generator by the quadratic identity and hence everywhere by (G). If the original endpoint maps are equivariant, uniqueness makes f₃ equivariant.

Both hypotheses matter. Without (G), the action on an ungenerated middle summand is not reconstructed. Without (J), the displayed relation check gives only a class in the common B-kernel, not zero. In particular one must not assert reconstruction merely because both pencils arose from bundles.

## 2. The lemma applies to the actual F→B blocks

PR924 gives

    Q_bundle,F=O(18), E_F=(P+D)O(-2),
    Q_bundle,B=Sym³W O(7), E_B=(V+P)O(-4).

The reconstructed F source and middle are

    N₂,F=H⁰(O(16))=Sym¹⁶W,
    N₃,F=H⁰(O(17))=Sym¹⁷W,

and A_l is ordinary multiplication by the same negative variable. Thus (G) is the universal surjection W⊗Sym¹⁶W→Sym¹⁷W. Its kernel is Sym¹⁵W. This uses no selected source parameter from the balanced F family.

For B, the actual block presentation is

    0→E_B→N₃,B O(-1) --B--> N₄,B O→0.

Twist by one and take global sections. Its constant-coefficient kernel is

    ker[N₃,B→N₄,B⊗H⁰(O(1))]=H⁰(E_B(1))
      =H⁰((V+P)O(-3))=0.

This is precisely (J), with the determinant-one convention identifying the same two fixed coefficient arrows. It is not an evaluated joint rank. The direct block presentation follows naturally from PR924's simultaneous reconstruction and actual constant decomposition.

Hence EVERY equivariant F→B endpoint map commuting with all negative quadratics extends uniquely to a full linear-pencil map F→B.

But there is no nonzero such full map. Composing with the full-pencil F projection and B inclusion would yield an element of PR924's entire represented endomorphism algebra whose only possible block is F→B. That algebra has three scalar vertices F,B,L and only the radical arrow L→F; its B vertex is isolated. Therefore the composite and the F→B map are zero. This covers singular maps, not merely automorphisms.

## 3. Exhaustive classification of reverse even maps

The source quotient negative pencil is the direct sum of F and L, with

    N₂,L=H⁰(Q_bundle,L(-2))=0,
    N₄,L=V+P,
    N₄,B=V+2P+2D.

A reverse quadratic map is a pair

    f₂:X_F→X_B, f₄:Y_F⊕Y_L→Y_B.

Restricting f₄ to Y_F gives an F→B endpoint map. By Section2, both f₂ and f₄|Y_F vanish. The remaining map f₄|Y_L is unconstrained by negative products because N₂,L=0 and every negative quadratic from X_F lands in Y_F. Conversely any such target-only map satisfies every quadratic intertwining equation.

Thus the entire equivariant reverse even Hom space is exactly Hom_G(Y_L,Y_B). Its dimension is 1·1+1·2=3. This is a canonical target-only description for the fixed normal form, not a generic dimension calculation. All nonzero members fail full-linear extension, since any extension would give a full negative-pencil map (F⊕L)→B, again impossible by the isolated B vertex.

This explicit three-dimensional ambiguity is the exact information lost by omitting degree3. It is the smaller counterexample within the actual negative-pencil module class requested by the reconstruction question; unlike an arbitrary artificial pencil it uses the actual block structures without evaluating them.

## 4. Adding Q kills the entire ambiguity

Now impose the actual one-sided condition, so Q descends to Q_T:X_F→Y_F⊕Y_L. An intertwiner with Q also satisfies

    f₄ Q_T=Q_B f₂=0.

By Section3, f₄ already kills every negative quadratic image. The actual generation identity from PR935 is

    Y=im Q+im q₋.

Project this identity modulo Y_B. The B source contributes zero in this quotient for Q by the one-sided hypothesis and for negative quadratics by the actual block decomposition. Therefore

    Y_F⊕Y_L=im Q_T+im q₋,T.

The map f₄ kills both generating images, hence f₄=0. Since f₂=0 was already proved, the joint reverse Hom space is zero.

No scalar-commutant argument is being substituted for this Hom calculation: an even map need not extend in general, as the three-dimensional family shows. The proof first establishes extension precisely on F→B using (G),(J), then uses actual generation to dispose of the remaining endpoint-only ambiguity.

## 5. Consequence for naturality and remaining boundary

A parameter-independent reverse chain map T→S for Q+tT_a simultaneously for all a is exactly a fixed endpoint pair intertwining Q and every T_a. The theorem proves it is zero, so in particular no such map induces a nonzero scalar D→D on Q-cohomology. The radical-style derivation of rκ=0 cannot be resurrected by weakening full-linear compatibility to all-negative-quadratic compatibility in this branch.

This does not prove that every other geometric argument for rκ=0 is impossible. It says this specific chain-map mechanism is absent. It does not exclude one-sided Q preservation, imply its complementary preservation, select the raw cubic, or reduce its three-dimensional ambient Hom space. Maps for a SINGLE chosen quadratic direction, or maps depending on t or a, are different questions and are not classified. The excluded radical-style maps are constant endpoint maps.

The checker verifies all universal representation, polynomial generation and relation identities, the explicit loss when (J) is removed, the actual negative bundle vanishing degrees and the three-dimensional even-map ambiguity. It never evaluates actual coefficients, points, jets or matrix ranks. The proof uses the authenticated bundle presentations and generation theorem rather than a one-shot or local-model experiment.
