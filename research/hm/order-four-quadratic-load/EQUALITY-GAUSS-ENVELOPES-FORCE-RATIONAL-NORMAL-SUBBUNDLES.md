# Equality Gauss envelopes force rational-normal subbundles

## Result and scope

Among the 26 retained quotient labels, seven attain equality in one maximal-profile degree envelope. Equality rigidifies every graded Gauss quotient and its composite derivative image. In these seven cases, the longest chain additionally forces a complete rational-normal osculating subbundle in the actual central bundle.

This excludes the primal height vector (7,6,1) for G3.21.45ca6278cbfc and the dual height vector (7,3,0) for G3.21.d610e381ed75. Their respective other maximizing vectors (8,5,1) and (8,2,0) survive this argument. No label or profile is claimed excluded. This is a connection-and-equivariance consequence, not an inference from matching Euler characters or an assumed jet-bundle identification.

## 1. Equality rigidifies each image

Use the finite degree-envelope hypotheses and notation F_j, Q_j, J, with distinct ordinary target degrees lambda_1>lambda_2>lambda_3. Suppose deg F equals the maximal allowed degree capacity. The actual derivative ranks select an allowed height vector h. Every bound

    deg Q_j <= sum_(i<=q_j) lambda_i - 2j q_j

must be equality, and h must maximize the capacity: otherwise their sum is strictly below deg F.

Let T_q be the sum of the q highest-degree line summands of J. For an injection U -> J(-2j) of rank q attaining this degree bound, its determinant has the maximal possible degree. Since the top q-fold wedge summand is unique and all other wedge summands have strictly lower degree, its determinant map is a nonzero constant into that top line and zero into every other wedge summand. Thus the generic image is exactly T_q(-2j), and the map factors through it. Its determinant is nowhere zero, so U -> T_q(-2j) is an isomorphism everywhere. In particular there is no torsion loss. For q=3 the same determinant argument gives the full target.

Apply this to every composite Q_j -> J(-2j). Their images are exactly T_(q_j)(-2j); the intermediate arrows Q_j -> Q_(j-1)(-2) become the standard inclusions under these composite identifications. This describes the associated graded flag and all its induced derivative arrows, not a splitting of F or of its connection.

## 2. The longest chain generates a full rational-normal system

Write S for the central bundle, so F=S^- and J=S/F. In all seven equality cases the highest line of J is O(6) with trivial coefficient representation, and the longest height h=h_1 is 7 or 8, strictly larger than h_2. Consequently the last nonzero Gauss kernel is the equivariant line

    C=F_(h-1)=Q_h=O(6-2h)=O(-e),  e=2h-6.

Starting with C, differentiate with the actual constant connection. Its k-th saturated forward transform lies in F_(h-1-k) for 0<=k<=h-1, and the next lies in S. The composite highest-line symbols in Section 1 are isomorphisms. Hence, for 0<=k<=h, the successive derivatives have a nonzero component in a new graded quotient and are independent. The k-th transform therefore has rank k+1. This statement follows from the Leibniz rule: lower derivatives lie in the preceding filtration step, so the new leading derivative is exactly the composite graded symbol. Saturation does not alter generic rank.

The inclusion C -> H tensor O is given by an equivariant linear map Sym^e W -> H. Let V be its constant polynomial span. The preceding rank statement gives dim V>=h+1. The exact binary-icosahedral decompositions are

    Sym^8 W = P + D,       dimensions 4+5;
    Sym^10 W = A + V3 + D, dimensions 3+3+5.

All constituents are distinct. When h=7, e=8, every proper quotient has dimension at most 5<8. When h=8, e=10, every proper quotient has dimension at most 8<9. Semisimplicity therefore forces the polynomial map to be injective in either case. Thus C is the complete rational-normal degree-e system inside a constant Sym^e W subspace, rather than a projection of it.

Its k-th osculating bundle is proved directly as follows. At a parameter line L in W its fiber is

    L^(e-k) Sym^k W subset Sym^e W.

Differentiating a local generator x^e produces exactly this space. Multiplication therefore gives a fiberwise injective equivariant bundle map

    O(k-e) tensor Sym^k W -> Sym^e W tensor O.

It has the same fibers as the saturated k-th forward transform, so they are equal. Taking k=h gives the necessary saturated inclusion in S:

    h=7: (Wp+T) tensor O(-1) subset S, rank 8;
    h=8: (P+D) tensor O(-2) subset S, rank 9.

Saturation follows also because this osculating bundle and S are both subbundles of the same constant bundle. No jet-bundle classification is used.

## 3. Explicit seven-label consequences

Dual equality has B degrees (6,-4,-18), rank L=10, deg L=-38. Its maximizing heights are (7,3,0) and (8,2,0), for the four labels

- G3.11.6795493ae8cd;
- G3.11.a5d4e292b34e;
- G3.11.cce6e3ba4eeb;
- G3.21.d610e381ed75.

Accordingly Q* must contain one of the two saturated osculating subbundles in Section 2. For G3.21.d610e381ed75 specifically, the actual source/plateau note, Section 4 equation (12), gives H0(Q*(d)) nonzero implies k<=d. Since this profile has k=2, H0(Q*(1))=0. Its height (7,3,0) would contradict this by forcing O(-1)(Wp+T) into Q*. Thus this label must use (8,2,0) and has a saturated O(-2)(P+D) subbundle in Q*. This cut does not apply to the other three dual labels, whose k=1.

Primal equality has A degrees (6,2,-8), rank K=14, deg K=-54. The labels G3.11.942927348917 and G3.12.8e9af2d08af9 have the unique maximizing height (8,6,0). The label G3.21.45ca6278cbfc has maximizing heights (7,6,1) and (8,5,1).

For (7,6,1), Section 2 gives an injection O(-1) tensor (Wp+T) -> E. Twisting by one contradicts the actual input H0(E(1))=0. Thus this height is impossible. All three primal labels must use h_1=8, and therefore necessarily satisfy

    (P+D) tensor O(-2) subset E,
    P+D subset H0(E(2)).

This is a new necessary extension/connection restriction. It does not say that every extension with these graded pieces is realizable, nor that the remaining height choices are impossible.

## Reproduction

Run verify_equality_gauss_rational_normal_subbundles.py. The bounded verifier pins the 26-label certificate, maximal-profile certificate, baseline quotient data, PR715 theorem, and actual source/plateau note. It independently enumerates all permitted heights in all 52 orientations, finds precisely the seven equality labels, lists every forced graded quotient, checks degrees and no-loss numerical identities, verifies the two symmetric-power decompositions using integer McKay recurrence, and records the two newly impossible heights and the remaining choices. The geometry is proved above; arithmetic alone is not a proof of the connection statement. No actual-instance coefficient or rank evaluation is used.
