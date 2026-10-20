# Source-bound classical root factorization and full stabilizer audit

## Checked result

The actual carrier line is a genuine external product, not merely a rational half-hyperplane class:

    N = O_C(O) ⊠ O_C(O) ⊠ O_C(O) ⊠ O_C(O)
      = N_12 ⊠ N_34,
    N_12² = p_12*O_P²(1),  N_34² = p_34*O_P²(1),
    N² = f*O_P⁴(1).

It admits a genuine canonical invariant-divisor linearization under the whole signed permutation group (Z/2)^4 ⋊ S4. This includes each full pair quotient group G_2=(Z/2)^2⋊S2, their product, and block exchange. There is no classical projective-linearization obstruction.

For g=(ε,σ) fixing a point a=(a_1,...,a_4), the character of its action on the N fiber is exactly

    χ_N,a(g) = ∏_{i : a_i=O} ε_i.                 (1)

The permutation itself has no extra sign. In particular inversion has character +1 at the three finite two-torsion points and −1 at O. This nontrivial root inertia prevents N from descending as a line to the pair coarse quotient; it does not prevent equivariant Morita untwisting on the action groupoid. With the canonical linearization on F=N⊗f*HM, untwisting by N removes its classical inertia exactly.

This closes the genuine classical product-root and root-linearization premise for the already established upstairs external-product Morita construction. It does NOT construct the full quantized pair-swap action/coherence, prove invariant Morita-atlas hypotheses, or identify the resulting algebra with the corrected downstairs model. All thirty retained physical obstruction values remain unknown.

## 1. Exact source pins and scope of reading

Historical context: [comment 6263865869](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6263865869), which establishes the upstairs mixed external product modulo (s²,t²) and explicitly leaves the root/groupoid comparison open.

The carrier source is pinned to PR2 head 3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f, blob fc0b0c7cf512d93c7a4ea976f986b7332b926f51. Use the pinned carrier links below; the already public source is not duplicated.

- [Carrier definition, lines 11–15](https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md#L11-L15) explicitly defines Θ as the sum of four origin divisors, N=O_X(Θ), f through the four x-maps and symmetric product, and F=f*HM⊗N (called E in that source).
- [Actual root transition and cover, lines 66–68](https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md#L66-L68) supplies the N scalar transition in F, specifies O_C(∞), and gives frames 1 and y/x on its two genuine trivializing opens. Thus the origin in Θ is infinity O, not the affine point (0,0).
- [Pinned physical root-source frames](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md#L33-L45) are the anchor already audited in [research/hm/null-root-line-geometry/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-root-line-geometry/PROOF.md). That report's one-factor-to-product premise is supplied by the preceding PR2 definition, rather than assumed again here.
- [Full pair geometric quotient and product map](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260407782) identifies m:P²×P²→P⁴ and m*O(1)=O(1,1).
- [Existing pure result and explicit swap caveat](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260293233) uses the invariant-divisor deck linearization but expressly does not assert literal swap equivariance of its short Alexander–Whitney representative.

The new results below are elementary divisor, tensor-line, and group-action deductions from the pinned carrier. No physical source/model/jet evaluation or experiment is asserted.

## 2. Product line and square identity as genuine line isomorphisms

For Cartier divisors D_i, the canonical multiplication map identifies O(sum D_i) with the tensor product of O(D_i). Taking D_i=pr_i*O proves the fourfold external product immediately from the source's definition. Grouping factors yields N=N_12⊠N_34.

Let x:C→P¹ denote the stipulated double cover. Its pole divisor is 2O, so x*O_P¹(1)=O_C(2O). The binary-form multiplication map (P¹)^r→Sym^r(P¹)=P^r pulls O(1) back to O(1,...,1): each polynomial coefficient is homogeneous of degree one in each linear factor, and these coefficients have no common zero. Consequently the pair map p:C²→P² has

    p*O(1)=O_C(2O)⊠O_C(2O)=N_pair².

The same argument for four factors proves f*O(1)=N². Equivalently f=m∘(p_12×p_34) and m*O(1)=O(1,1). All these are actual line bundle isomorphisms. They do not introduce O_P²(1/2).

On the source's product root cover the frames are

    n_m = ∏_i pr_i*(e_mi),  e_0=1, e_1=y/x.

Their transitions split by pairs. Refinement by the projective carrier charts preserves this line identity; the refined opens need not themselves be Cartesian products.

## 3. Genuine full linearization, including permutation arrows

Let ι:C→C be y↦−y. Every deck involution fixes O, and every permutation preserves Θ. A group preserving a Cartier divisor has a canonical genuine linearization of its divisor sheaf: it acts by pullback of rational functions, preserving the pole bound. The group laws hold exactly because pullbacks compose, not merely up to a scalar. Restriction maps and divisor-sheaf multiplication commute with this action.

Thus N is genuinely linearized under W_4=(Z/2)^4⋊S4. Under the product identification, this is the external tensor action with the ordinary symmetry isomorphism of line bundles. These are degree-zero lines, so exchanging two factors has no Koszul sign. This proves all group relations, including conjugation of the deck generators by swaps and the square of block exchange.

An explicit arrow check uses the actual rational frames. Define g by

    (g a)_i = ε_i a_(σ^-1 i),

where ε_i=-1 means inversion on that elliptic coordinate. Then

    g* n_m = (∏_i ε_i^mi) n_(σ^-1 m),
    (σ^-1 m)_j = m_(σ j).

The equality holds as rational sections on the corresponding translated root opens. It is induced by the preceding genuine rational-function action, so it is compatible with every transition and composable pair of arrows. It is not an averaging prescription for a projective action.

The squared-line isomorphism is equivariant with the quotient-pullback linearization. One direct verification is that the pullback of the hyperplane section detecting a root at infinity has divisor 2Θ and is invariant under signed permutations; the invariant rational section 1 of O(2Θ) has the same divisor. This identifies the lines and their actions. Pairwise the identical argument gives equivariant N_pair²=p*O(1).

## 4. Exact inertia at every stabilizer

At a finite point, e_0=1 is a valid frame, invariant under inversion. At O, e_1=y/x is a valid divisor-sheaf frame and inversion sends it to −e_1. Equivalently the local uniformizer z=y/x² changes sign and the frame 1/z changes sign. This proves the one-factor characters, including all four branch points.

For any point a of C⁴ use frame e_1 in the coordinates at O and e_0 in all other coordinates. If g fixes a, the set I(a)={i:a_i=O} is permutation invariant. The explicit arrow formula therefore returns this product frame to itself with multiplier ∏_(i∈I(a)) ε_i. This proves (1) for the ENTIRE stabilizer, including elements that combine inversions and permutations and points on intersections of ramification strata.

Useful pair cases:

- A deck generator fixing a finite two-torsion coordinate acts by +1 on N_pair, including at (0,0), (1,0), and (−1,0) in that coordinate.
- The same generator fixing an O coordinate acts by −1.
- The pure transposition at (a,a) acts by +1, including at (O,O).
- An inversion-decorated transposition fixing (a,−a), with a finite, acts by +1. Formula (1) also covers the two-torsion degenerations.
- At (O,O), the character is ε_1 ε_2 and remains independent of the permutation sign.

The corresponding fourfold formula includes pair exchange without another sign. In particular this root character must not be confused with the canonical-volume coefficient character, which is negative under an inner swap. The root line, a canonical two-form, and a full-deck-sign cohomology sector have different actions.

The square N² has trivial stabilizer action everywhere. A different linearization of N can twist these characters by a global group character, so (1) is specifically the canonical divisor linearization just constructed. It is the one compatible with the canonical rational section 1. Because C⁴ is connected projective and its invertible regular functions are constants, all alternative linearizations differ in this way.

No such character twist makes N inertia-trivial everywhere. Already one deck generator fixes a locus with that coordinate O, where its canonical character is −1, and loci with the coordinate a finite branch point, where it is +1. A constant character cannot make both +1. Equivalently N_pair cannot be a pullback line from P²: if N_pair=p*L, its square would force p*(L²⊗O(-1)) trivial, whereas restriction to a one-coordinate curve gives 2·deg(L)=1 for L=O(deg L). Thus coarse non-descent is an actual obstruction, not a missing choice of linearization.

## 5. Carrier inertia and what the Morita step now gains

Write B=P²×P², p=p_12×p_34, and E_B=m*HM. The actual carrier identity is

    F = N⊗p*E_B.

Give p*E_B its canonical pullback action under G_2×G_2 and N the preceding divisor action. Their tensor product is a genuine action on F. The displayed source carrier transitions are exactly the line scalar times the HM pullback transitions, so this supplies an equivariant structure on that actual geometric carrier, not on an unrelated root candidate. Under block exchange use m∘τ=m and ordinary tensor symmetry; it also extends. Under all W_4 use the invariant map f directly.

For a stabilizer g, the pullback factor has the identity action on its fiber. Hence

    ρ_F,a(g)=χ_N,a(g)·Id,
    N^-1⊗F = p*E_B

has trivial classical inertia. The cancellation is literal and includes all ramification strata. End(F) was already inertia-trivial, but that alone would not have recovered this root character.

Combining the actual N=N_12⊠N_34 with the established upstairs ambient product modulo (s²,t²), the ordinary nonequivariant Morita-transport formulas can choose factorized local lifts and yield a factorized transported ambient. Nilpotent unit lifting supplies the local invertible lifts of these genuine scalar transitions; it does not require a global module quantizing N in the unchanged ambient.

For a full equivariant quantum statement, the groupoid cocycle of the classical line is now available on both Čech and group arrows. It can be used in the universal transport formulas ONCE the actual ambient groupoid maps and all their coherence units are supplied. The classical carrier identification does not prove that a separately chosen quantum module or its frozen representative has this specific lifted equivariant action.

## 6. Remaining precise gap

There is no remaining obstruction at the level of existence of the classical product root, its full genuine linearization, its square, or its stabilizer characters. The outstanding issue is quantum ambient coherence and comparison.

The pair group includes the inner swap. It reverses the pair bivector, and the parameter must transform accordingly. On the ordered Alexander–Whitney representative it sends q_1∪q_2 to q_2∪q_1, which need not equal −q_1∪q_2 literally. Graded commutativity in cohomology is not that literal cochain identity. The pinned PR1 pure theorem expressly retains this caveat. The present line linearization supplies no missing ambient swap gauge or its group/Čech associativity units.

Consequently the invariant-gluing theorem cannot yet be applied merely by citing this audit. It still needs the actual coherent weak ambient action on a specified quotient atlas, transported overlap bimodules and coherence, permissible strictification with compatible restrictions, and the required residue-inertia condition for those bimodules. Classical inertia cancellation of F is necessary information but does not itself verify every overlap-bimodule hypothesis.

After that one must identify the full transported/invariant algebra with the independently specified corrected P²×P² ambient, including mixed coefficient multiplication. Neither the root square identity nor normalized trace supplies this identification. No mixed module existence or retained obstruction value has been inferred.
