# Independent review: compact pure-lift rigidity and mixed boundary

## Verdict

**Checked; no blocking error found.** Under the explicitly imported physical geometric/equivariance identification and Ext¹ character table, each fixed corrected compact pure problem has one lift up to unique reduction-preserving isomorphism. The external tensor construction gives a genuine specified mixed ambient algebroid, and its fiber-product boundary has a unique compatible lift. These conclusions do not establish mixed existence.

Reviewed `RESULT.md`, the earlier corrected-relative and root-characteristic results, `../../null-factor-surfaces/relative-surface-0502/DECK_ADDENDUM.md`, `../../null-pair-quotient-bracket/pair-quotient-0512/RESULT.md`, and §4 of the named `closure-and-characters.md` source. Only static reading and universal formal reasoning were used. No physical source or jet values are evaluated in this argument.

## 1. Imported Ext¹ table and exact eigensummands

The named source explicitly gives **per-character** dimensions

    (79, 2, 0, 0, 0)

for deck weights zero through four. It also supplies symmetry between equal-weight subsets and multiplicities `(1,4,6,4,1)`, giving total dimension `87`. The report correctly treats this as an imported computation, not a newly proved rank theorem. In particular each weight-two character and the weight-four character have zero Ext¹.

The finite pushforward argument is valid in every coherent-cohomology degree: finite maps have no higher direct images, projection formula applies to the locally free pullback endomorphism bundle, and characteristic-zero character projectors are exact. The selected pair-full-sign/inner-odd summand is `ω_P²`, up to its fixed constant-line normalization; the other pair's trivial-deck/inner-even summand is `O_P²`.

Consequently `H¹(X,A⊗K_z)` is the specified inner-swap subspace of the weight-two `(1,1,0,0)` physical Ext¹ space and must vanish. The factor-exchanged assertion follows identically. Selecting full sign and both inner-odd parities identifies `H¹(X,A⊗ω_X)` with a subspace of the weight-four Ext¹ space, proving the conditional mixed-uniqueness H¹ vanishing too. No extra permutation sign is introduced after the equivariant sheaf pushdown has fixed the action.

All three deductions depend on the genuine equivariant geometric identification of the physical endomorphism sheaf with the pullback of `A`; an unrelated numerical complex would not suffice. The report states this dependency.

## 2. H⁰ from dense stable fibers

For each stable plane fiber, stability and the negative canonical twist imply

    H⁰(End(E_h)⊗ω_P²)=0.

A section of the locally free sheaf `A⊗K_z` therefore vanishes at every point above the stable open. Since that subset is dense in the integral compact product, the section is identically zero. The same argument applies after factor exchange. It also applies to `A⊗ω_X`, because the additional base canonical factor restricts on each fiber to a one-dimensional constant factor.

This argument establishes the needed H⁰ vanishings independently of the imported Ext¹ table. It does not require stable restrictions at the exceptional parameters.

## 3. Pure-lift uniqueness

For a fixed square-zero algebroid and fixed reduction identification, nonempty lift classes form a torsor under `H¹(A⊗K)`, and reduction-preserving automorphisms are the additive group `H⁰(A⊗K)`. Their respective vanishings prove uniqueness of the isomorphism class and uniqueness of each comparison isomorphism. The previously checked global corrected-relative calculation supplies nonemptiness on the compact product.

Thus “unique up to unique reduction-preserving isomorphism” is justified for each fixed pure ambient problem. It does not imply literal equality of presentations or a preferred transition cochain. Ordinary automorphisms of the reduction are excluded by the fixed-reduction condition, as required.

## 4. External tensor ambient and fiber-product boundary

The corrected classes are pulled back from their separate plane factors, so choose genuine factor algebroid presentations and form their external tensor product. On algebraic affine product opens, tensoring the factor algebras over C gives the claimed four coefficient pieces. Sheafification and the tensor-product descent maps extend this construction. This interpretation avoids incorrectly treating the noncommutative factor algebras as ordinary central O-algebras for a naive O-linear pullback.

The tensor algebra is associative and its product coherence units satisfy descent because the factors do. The mixed ideal is `J=K_z⊗K_h`; it squares to zero and is annihilated by both pure ideals. Quotienting it kills the cross products and gives exactly the fiber product of the two pure algebroids over their common reduction. Cross terms in the original multiplication, gluing maps, and triple units are specified by this construction and cannot be omitted.

The two pure module lifts with specified reductions can be joined along E. Locally, choose bases compatible with the reduction; a change of reduction basis lifts across the square-zero surjection, so the fiber product module is free of the same rank over the boundary algebra. Its descent and triple coherence are inherited componentwise. Conversely, restricting a boundary lift gives the pair of pure lifts with these reduction identifications.

Equivalently the boundary ideal is `K_z⊕K_h`, with no cross products. Its H¹ ambiguity and H⁰ automorphism groups both vanish. The boundary lift therefore exists and is unique up to unique reduction-preserving isomorphism. This is compact global compatibility, not merely fiberwise compatibility. A comparison induced by factor exchange is coherent by uniqueness when the ambient presentation and classical reduction carry the stated exchange identification.

## 5. Scalar mixed freedom, target, and uniqueness boundary

Künneth gives `Hⁱ(X,ω_X)=0` for `i=0,1,2,3` and a one-dimensional H⁴. In particular there is no nonzero global scalar mixed gerbe class in H² available to tune the compact mixed obstruction. Trace splitting then identifies the full degree-two mixed obstruction target with its tracefree summand.

The imported dimensions `32+30=62` refer to the full target and its block-exchange splitting. The additional `2+30` decomposition is within the block-even 32-space. The report does not conflate these two 30-dimensional spaces or infer an actual obstruction's parity from their dimensions.

Any compact mixed obstruction has zero trace because the target of trace is H²(ω_X)=0. Its restriction to the stable open consequently has zero scalar component and lies in `H¹(U,V⊗ω_U)`. Scalar classes available only on that open are not global tuning parameters. Restriction may have a kernel, so open vanishing would not settle compact mixed existence.

The verified H¹ and H⁰ vanishings for `A⊗ω_X` show that a mixed lift, **if it exists for the fixed ambient and fixed boundary**, is unique up to unique reduction-preserving isomorphism. They do not imply that its H² obstruction vanishes.

## 6. Open torsor and remaining scope

The unique compact pure lift supplies a preferred restriction class once the compact corrected problem is fixed. This is compatible with other open lifts differing by `H⁰(U,V)`: such open lifts need not extend compactly. The report correctly avoids concluding that this space of global sections is nonzero solely from the rank of V.

No calculation here evaluates the mixed obstruction, identifies the chosen external-tensor ambient with a physical two-jet, transports physical boundary data, or proves extension of an arbitrary open lift. These remain distinct tasks beyond the rigidity and compatibility theorem reviewed here.
