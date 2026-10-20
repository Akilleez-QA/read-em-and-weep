> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# Independent challenge: PR80 constant-scalar completeness

## Result

**Accepted as a conditional theorem, with no additional rank computation.** At PR80 head `97add51e0297c1a12d814a4a1adc9a3262a699ca`, the assertion that all 30 constant scalar maps at all 81 Laurent positions separate the rational D8 permutation-sign sector is correct under its explicit pinned model, kernel and geometric-linearization premises. The proof establishes that the entire kernel is pointwise fixed, not merely an invariant subspace or a conveniently named basis.

The new theorem is consistent with the existing inversion-positive twelve-dimensional target and its four-detector interface. It supplies no missing source values or source-to-finite-model comparison.

**A sharper limitation follows from the existing bridge:** at the single position `kappa=(-1,-1,-3,-3)` used by the four named detectors, even all 30 constant maps have rank only 20 on the full epsilon32 target and rank only 8 on the inversion-positive12 target. There is an explicit four-parameter family of nonzero positive epsilon classes invisible at that single position. Thus replacing “all81 positions” by “the familiar position, with all30 maps” is invalid, including after imposing inversion.

No physical-source arithmetic, elimination, finite-model oracle execution, repository write, publication, or merge was performed. Published ranks are premises; the new conclusions below are exact structural deductions.

This single-position family consists of negative-block constant scalar maps. It is **not** the positive finite-model detector ell(n,p)=p[7]-p[25] whose pulled-back row is the current Phi with78 staircase summands. No claim is made about that ell's restriction to epsilon, its nonzero value there, or its relation to the single-position rows. The public positive-kernel witness does not establish any of those claims. The source-dependent positive-Phi implementation and its transferred restriction remain separate work.

## 1. Exact theorem and kernel identification

Let F be the pinned rational full-deck-sign harmonic complex, with

    D1 x = (A x, T x),
    D2(n,p) = (B n, U n + C p),

and let S collect all 30 constant scalar maps at all 81 positions. The pinned `structural-relations.md`, section4, establishes `S D1=0` and identifies

    K = ker(S:H²(F) -> Q^2430)
      = im(ker C -> H²(F))
      = ker C / T(ker A),
    dim K = 30-10 = 20.

The inclusion here is essential: literal annihilation of pure-positive representatives and the independently certified dimension of the full scalar kernel establish equality. A numerical coincidence of dimensions without that inclusion would not suffice. The length-five map T is retained; replacing this quotient by ker C changes it.

For a field k, group G, character chi, linear S:H->V, and g in G with chi(g)!=1, the following elementary implication is enough:

    ker S is pointwise g-fixed
    ==> ker S intersect H[chi] = 0.

Indeed a class x in the intersection satisfies x=gx=chi(g)x. No equivariance of S or semisimplicity theorem is required for this implication itself. Here use g=(12), chi=epsilon, and 2 invertible.

Consequently, with the genuine geometric action of D8,

    S restricted to W=H²(F)[epsilon] is injective.

The separately authenticated dimension32 gives its rank32. The dimension32 calculation is not needed for injectivity. After additionally imposing the authenticated global inversion covariance, its restriction to the specified positive12 target has rank12. This also persists under any field extension of Q by flat base change.

## 2. Actual HPL inclusion and geometric signs

Read directly at source commit `08b73637d4136f91606aad332c46cafd064417f8`, the finite-model implementation has:

- `makeBasis(2,0)`: internal degree2, Cech degree0, line degree0, exponent tuple(0,0,0,0).
- `unprunedTransfer`, line154: the actual inclusion of a positive coordinate on all16 degree-zero A/B chart tuples.
- `fullDelta`: preserves each chart state, hence Cech degree.
- `fullH`, line171: requires a C/degree-one chart state to act.

Thus every positive input p satisfies H Delta i(p)=0 and H i(p)=0. For the pinned perturbation convention,

    I_A = (1+H Delta)^(-1)i,
    P_A = p0(1+Delta H)^(-1),

one gets I_A(p)=i(p) and P_A i(p)=p exactly. The all-B state in the pruned transfer is only computational notation and cannot be used as the geometric inclusion.

The coefficient complex is pulled back from the elementary-symmetric map to P4. Factor permutations fix its coefficient/matrix indices. The full-sign eigensheaf has the product linearization: y1 y2 y3 y4 is an ordinary product and gains no permutation sign. The positive line degree is zero; all four tensor Cech degrees are zero. There is therefore no Cech Koszul sign and no extra internal-degree sign from permuting resolution factors, since those factors are not being permuted.

It follows on every positive cochain, and hence on every positive cycle, that

    P_A rho(g) I_A(p) = P_A rho(g)i(p) = P_A i(p) = p.

In particular the entire K is the trivial D8 representation. Its pure-positive boundaries are fixed as well. This is stronger than observing that a single positive witness is invariant. It does not require the ordered contraction to be equivariant. General transferred group laws need only hold on cohomology; the displayed positive-subspace identity is exact already on those finite cochains.

The same reasoning fixes K under every factor permutation, not only D8. The full S4 decomposition in comment6130391535 has a trivial summand of dimension20, so with that extra published premise K is exactly the full S4-invariant summand. This refinement is unnecessary for the D8 argument.

### Failure controls

An invariant kernel is not enough: over Q, take H=Qe0+Qe1, g(e0)=e0, g(e1)=-e1, and S(xe0+ye1)=x. The kernel is g-stable but equals the sign line, so separation fails. PR80 avoids precisely this mistake by proving pointwise fixedness.

Twisting the geometric linearization by epsilon would turn constant classes into sign classes and invalidate the conclusion. This is why the specified pullback/product linearization matters. The proof is not invariant under an arbitrary relabeling of the action.

In characteristic2 the final equation 2x=0 proves nothing. In characteristic3, this final argument would be valid if the same kernel and geometric-membership hypotheses were independently established, but the rational kernel calculation and characteristic-zero choice-independence/HKR results do not establish those hypotheses by specialization. No F3 conclusion follows here.

## 3. Source membership and choice-identification boundary

The logical source statement is:

If r is a complete closed corrected geometric residual, its class is transported to H²(F) by the authenticated comparison, and that class lies in W for the specified geometric action, then

    [r]=0 iff every one of the specified scalar values is zero.

There are two different identification requirements:

1. The transported deformation data and the original data must represent the same first-order ambient deformation problem before full-sign second-jet choice independence applies. For D8 the combined automorphisms (12)d1, (34)d3 and (13)(24) stabilize the actual direction. The earlier applicability review explicitly transports the complete admissible ambient/module descent data. Full-sign choice independence is not a license to compare arbitrary, unidentified first-order presentations.
2. A proposed numerical vector or family of extracted coefficients must actually be the image of the complete residual under the authenticated regular cover/End/finite-model comparison. Abstract naturality does not authenticate a partial source, clipped coefficient domain, or a lone raw source term.

Comment6205127744 states the cohomological equality

    Rsharp = M(s)^0 + delta(s_p k_q + s_q k_p).

The complete closed central full-sign part has zero H² by the equivariant trace splitting and the O(-2,-2,-2,-2) scalar summand. Thus the complete Rsharp class is the same class as the original obstruction. Its D8 sector, and the global inversion covariance already proved for that class, carry over. The baseline M(0)^0 alone is not asserted closed, and individual unclosed central or gerbe pieces cannot be discarded using that argument.

The existing global inversion proof additionally supplies the regular first-lift identification, actual varying frame/flat line, parameter signs and codimension-four extension needed for inversion. It strengthens membership to positive12; it does not evaluate the twelve coordinates. No new source-membership gap was found in the conditional statement at the reviewed PR80 pin. The outstanding obligations are the explicitly acknowledged complete source comparison and scalar evaluations in any proposed evaluation implementation.

Comment6209078673 supplies seed/support/source-release bytes in PR79, but is not itself a scalar evaluation or an additional completeness proof. Its arrival does not discharge these obligations.

## 4. New single-position obstruction to a smaller family

This deduction uses the already authenticated global epsilon generator/detector bridge and the positive12 interface; it performs no new rank computation.

Write B=End(L), and set

    A0 = H²(B(-2)),  dim A0=20,
    A1 = H²(B(-1)),  dim A1=10,
    A2 = H²(B),      dim A2=2.

By the specified perfect/Serre pairing, the epsilon target W is A0* direct_sum A1* direct_sum A2*. Its inversion-positive part is A0+* direct_sum A1+*, of dimensions8+4; A2+=0.

Every constant scalar map corresponds, by the genuine-degree supertrace, to a global internal-degree+2 dual cycle E. The thirty freely chosen beta/E13 coordinates in `structural-relations.md`, section3, give exactly the K30 graph in the positive12 interface. Their complete cohomological quotient is A0=K30/im(d5), with ten independent d5 boundaries. Thus the thirty maps represent every class of A0, not just a proper subspace.

At the fixed Laurent position kappa=(-1,-1,-3,-3), put

    beta2 = v2²-v1 v3+2v0 v4,
    m1:A0->A1, e |-> v2 e,
    m2:A0->A2, e |-> beta2 e.

These are well-defined cohomological multiplication maps: multiplication by a homogeneous polynomial commutes with the full total differential, including the incoming d5 boundaries. The bridge's trace identity is coefficient-linear and independent of the choice of constant scalar row. Hence it applies to every E, giving the dual graph

    Phi(e) = 4(e, m1(e), m2(e)).

The first component is 4 times the identity. Therefore this graph is injective and has dimension20: the all-thirty-single-position family has **rank20 on W**, and kernel dimension12.

Both multipliers are inversion fixed. The specified Serre pairing is equivariant, with no determinant sign. Thus Phi is inversion equivariant and its positive graph has dimension dim A0+=8. It follows that the same family has **rank8 on W+**, leaving kernel dimension4.

An exact nonzero counterexample family is available without choosing a numerical source. For any nonzero eta in A1+*, let m1+* denote the dual of m1 restricted to A0+. Then

    x_eta = (-m1+*(eta), eta, 0) in W+

is nonzero because its second component is eta. For every e in A0, its single-position value is

    <x_eta, Phi(e)>
      = 4(-eta(m1(e+)) + eta(m1(e+))) = 0.

These classes form the entire four-dimensional single-position kernel on W+. They are synthetic cohomology classes; none is asserted to be the actual obstruction.

Equivalently, in primal geometry multiplication by v2 sends G1 in H²(B(-4))+ to v2 G1 in H²(B(-3))+. The family is simply

    (G0,G1,G2)=(-v2 G1, G1, 0).

Its specified epsilon representative is a(U-v2)G1. The polynomial trace identity at this particular q gives cancellation, while the direct-sum splitting shows the class is nonzero whenever G1 is nonzero. This is a concrete global cohomological counterexample, not merely a dimension count.

For comparison, the four named detector rows have rank4 on W+ and kernel dimension8, as already proved by the positive12 interface:

    h=2z6-2w1, j=2z7, p=2z2, r=2z3-2w3.

Increasing to all30 maps at that same position raises the rank to8, still short of12. Increasing to all30 at all81 positions gives rank12 on W+ by PR80. The remaining positions, or independently certified combinations replacing them, are essential to the complete family.

## 5. Sources checked and scope

Public sources, all read through the repository connector:

- PR80 theorem at `97add51e0297c1a12d814a4a1adc9a3262a699ca`: https://github.com/Akilleez-QA/read-em-and-weep/blob/97add51e0297c1a12d814a4a1adc9a3262a699ca/research/codex-swarm/constant-scalars-separate-epsilon.md ; blob f736cb42b4f2f7aadcf70a86588416f021a517cb.
- PR80 D01, D02 and V07 reports at that same pin.
- Kernel/scalar classification: https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/structural-relations.md ; blob d48c88141e80f0005cf598d4796d6f358d45f07a.
- Genuine contraction implementation: https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js ; blob 8f534fd7a074e333fa031a6d8c51b864faf76d42.
- Choice/closure scope: https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md ; blob 946f96670ecb8152eaae16195329f9eb1243b7ae.
- PR1 comments6130306841, 6130352358, 6130391535, 6140937153, 6205127744, 6205249609, 6205341120, 6205455951, 6205660472, 6206738230, 6209077249 and6209078673.

Existing separately reviewed mathematical inputs:

- `../hm-epsilon-projective-generator-bridge-20261016/THEOREM.md`, especially the global splitting and universal trace identity.
- `../hm-projective-detector-dual-audit-20261016/AUDIT.md`.
- `../hm-positive-twelve-detector-interface-20261016/THEOREM.md` and REVIEW.md.
- `historical imported premise hm-global-projected-inversion-20261016/THEOREM.md (see PUBLICATION-SCOPE.md)` and TWELVE-DIMENSIONAL-TARGET.md.
- `historical imported premise hm-mixed-tag-firstlift-independent-20261016/FINAL-GLOBAL-AUDIT.md (see PUBLICATION-SCOPE.md)`.

The review accepts no source-specific zero, nonzero, second-order lift, all-order extension, F3 specialization, smaller complete detector set, .
