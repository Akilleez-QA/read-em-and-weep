# Forced D support and the two weighted-source block quotients

Work over C on T=P(W*) with standard G=2I linearizations. Fix the actual complement choices permitted by the input below. No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix or instance rank is evaluated.

## 1. Immutable interface and the role of choices

BRANCHES is PR1009 at commit0d75f42c4e79654c8fbef57e6ce56a1f06cdf9a1, research/hm/common-target-branches/PROOF.md. INPUTS.json records its exact Git blob. It constructs actual fiberwise-injective presentations

    λ≠0: 0→L⊕E18 O(-1)→R24 O→Q→0,
           L=W O(-3),
    λ=0: 0→L⊕E18 O(-1)→R24 O→Q3→0,
           L=A O(-2),
    E18=W'⊕S⊕2T6,
    R24=A⊕V⊕2P⊕2D.

The source splitting and constant target complement are explicitly choice-dependent. Fix such choices for this proof. The weighted subbundle L is then an actual subbundle of the source, not an abstract substitute. Our new constructions are inherited from its actual map. We do not claim that L, the subsequent A-component scalar, or its D coefficient image is unchanged when earlier complements are changed.

We prove that its actual D component must be nonzero, and classify its block cokernel B:

    L=W O(-3): B=A O⊕A O(2), or B=(W⊕S) O(1);
    L=A O(-2): B=A O⊕W O(3), or B=S O(1)⊕O(2).

The first option in each line occurs exactly when the A component vanishes, and the second exactly when it is nonzero. The classification is relative to the fixed inherited choices, not a new canonical scalar gate.

## 2. Only A and D can occur, and D is forced

For L=W O(-3), the coefficient representation is

    W⊗Sym³W=A⊕D.

For L=A O(-2), it is

    A⊗Sym²W=1⊕A⊕D.

The constant target R24 has no trivial constituent. Thus in either case the actual L map has support only in A⊕2D, and each of its A and D intertwining spaces is one-dimensional before accounting for the two D multiplicities.

The A-only universal map has deficient fiber rank. Write l for a local generator of the tautological kernel line in W. In the W case it is, up to scalar,

    v ↦ det(v,l) l².

Its image lies in the single line spanned by l², so it cannot inject a rank-two source. In the A case it is the first transvectant of a quadratic f with l², equivalently a nonzero scalar multiple of l times the contraction of f by l using det. It kills l² and has rank two, so it cannot inject a rank-three source. These descriptions prove universal identities for arbitrary l; no actual HM parameter is selected.

Since the actual source map is fiberwise injective, its D component cannot vanish. Its coefficient image selects an actual irreducible copy D_b inside the two D copies in R24. The D channel is the universal multiplication map

    W O(-3)→D_b O,     v↦l³v,
    A O(-2)→D_b O,     f↦l²f,

respectively, up to nonzero identification of D_b with Sym⁴W. Both are subbundle inclusions.

Put L8=A⊕D_b and R16=R24/L8, so R16≅V⊕2P⊕D. The actual weighted-source map factors through L8 O and remains injective on every fiber.

## 3. The universal D quotients and their extension classes

The two multiplication subbundles have exact quotient sequences

    0→W O(-3)→D O→A O(2)→0,                     (1)
    0→A O(-2)→D O→W O(3)→0.                     (2)

To see this uniformly, polarize a binary quartic into its degree-(2,2) or degree-(1,3) factors and evaluate the last factors against the tautological quotient W O→O(1). The first map has kernel l³W and the second kernel l²A. The surviving monomials map onto the claimed quadratic or linear factor. This proves both sequences for every tautological line without any selected actual evaluation.

Let α:L→A O be the actual A component and define the actual rank-six or rank-five bundle

    B=coker[L --(α,d)--> (A⊕D_b) O],             (3)

where d is the forced nonzero D component. Because d is a subbundle inclusion, (3) gives an extension

    L=W O(-3): 0→A O→B→A O(2)→0,
    L=A O(-2): 0→A O→B→W O(3)→0.                (4)

Equivariant Serre duality gives

    dim Ext1_G(A O(2),A O)=dim Hom_G(A,A)=1,
    dim Ext1_G(W O(3),A O)=dim Hom_G(W,A⊗W)=1.

The class of (4) is the pushout class of (1) or (2) along α, up to an irrelevant sign. The connecting map from Hom_G(L,A O) is injective because Hom_G(D_b O,A O)=Hom_G(D,A)=0. Its domain is one-dimensional by the coefficient identities in Section2. Therefore it is an isomorphism onto the displayed one-dimensional Ext space.

Consequently the extension (4) splits if and only if α=0. This implication uses actual maps and their connecting homomorphism, not the inference that a one-dimensional Ext space forces a nonzero class.

## 4. Determine both nonzero extension middle bundles

If α=0, equation (3) immediately gives the split types A O⊕A O(2) or A O⊕W O(3).

Suppose α≠0. The complete coefficient map of L→(A⊕D_b) O is onto: both irreducible target components have nonzero maps from their unique coefficient channels. Dualizing (3) and taking global sections therefore gives H0(B*)=0. The bundle B is globally generated as a quotient of a constant bundle, so every ordinary splitting degree is nonnegative; the dual vanishing makes every degree strictly positive.

In the W case B has rank6 and degree6. Thus B is ordinarily O(1)^6. Twisting (3) by O(-1) and taking cohomology gives

    H0(B(-1))=H1(W O(-4))=W⊗A=W⊕S.

Hence the equivariant type is

    B=(W⊕S) O(1).

In the A case B has rank5 and degree6, so its ordinary degrees are 2,1,1,1,1. The maximal degree-two line is equivariant; since G has no nontrivial one-dimensional characters, it is O(2) with its standard linearization. After averaging an ordinary splitting, write B=O(2)⊕M O(1). Again (3) gives

    H0(B(-1))=H1(A O(-3))=A⊗W=W⊕S.

The O(2) summand contributes W to these sections, so M=S. Thus

    B=O(2)⊕S O(1).

This determines the nonzero middle types without choosing an actual α value or computing a selected matrix rank.

## 5. The actual residual target after removing the weighted subbundle

Define Y=R24 O / image(L). This is a locally free bundle because the actual source map is fiberwise injective. Quotienting the original nested subbundles by L gives actual exact presentations

    λ≠0: 0→E18 O(-1)→Y22→Q→0,
    λ=0: 0→E18 O(-1)→Y21→Q3→0.                 (5)

The targets have degree6, and ranks22 or21 respectively. Their induced source maps inject on every fiber because their quotients Q or Q3 are locally free.

There is a canonical extension relative to the fixed inherited choices,

    0→B→Y→R16 O→0.                               (6)

All four possible B types above are globally generated and have H1(B)=0. Thus Ext1(R16 O,B)=0, and (6) admits an equivariant splitting, not a canonical one. In particular

    Y≅R16 O⊕B,
    R16=V⊕2P⊕D,

with B as classified in Sections3–4. These isomorphisms describe the target bundle but do not replace the actual map in (5) by an arbitrary map into that split model.

The rank and degree checks are

    rank Q=22−18=4,    rank Q3=21−18=3,
    deg Q=deg Q3=6−(−18)=24.

## 6. A forbidden alignment in the two D copies

The choice dependence yields a stronger invariant exclusion. Let S0⊂E18 be its unique S-isotypic summand. Its actual map S0 O(-1)→R24 O has coefficient support only in A⊕2D because S⊗W=A⊕D. Its D coefficient vector v in the two-dimensional D multiplicity space is nonzero: otherwise a rank-four source subbundle would map into the rank-three A target, contradicting fiberwise injectivity.

Let d denote the nonzero D coefficient vector of the weighted source, using arbitrary nonzero identifications of its one-dimensional universal D channel. Both spaces of permitted shifts of the weighted complement into E18 O(-1) are one-dimensional:

    Hom_G(W O(-3),E18 O(-1))=C,
    Hom_G(A O(-2),E18 O(-1))=C.

Indeed the coefficient identities W⊗Sym²W=W⊕S and A⊗W=W⊕S leave only the unique S in E18. A generator is multiplication by l² into S0 in the W branch, or multiplication by l in the A branch. Composing with the S0-to-D channel, which is multiplication by l, gives multiplication by l³ or l² respectively. These are exactly the weighted D channels, with a nonzero universal composition constant.

Adding t times this shift to the weighted-source inclusion is an invertible triangular automorphism of the source for every t∈C. It changes the D coefficient vector to d+t c v for a fixed nonzero c, while retaining the same actual fiberwise-injective presentation. Section2 therefore applies for every t: this new vector cannot vanish.

If d and v were proportional, their nonzero values would allow a t with d+t c v=0, a contradiction. Hence

    d∧v ≠ 0.

Thus the weighted source and the unique S source necessarily span both actual D multiplicity directions. The conclusion is independent of rescaling the universal channels and is preserved by the allowed weighted-complement shifts. It is a genuine exclusion of a possible coefficient alignment, not an evaluation of either vector or of an instance matrix. The corresponding A component may still change under those shifts, so its zero/nonzero block distinction remains choice-dependent.

## 7. Contribution and limitations

The weighted and unique S sources have forced independent D coefficient directions. In particular, the actual weighted source cannot be supported only in A: its D coefficient image is forced nonzero for every inherited choice of complements. The universal D block then has exactly the split or nonzero extension types displayed above, and removing it yields actual presentations with only E18 O(-1) left in the source.

The A-component zero/nonzero distinction can depend on earlier source-complement choices; no invariance or canonical new scalar is asserted. The old λ branch and all seven actual C possibilities remain unselected. The new content is forced D support, the complete block-middle classification and the inherited residual targets, not an additional source-pair exclusion or an actual-instance evaluation.
