# Independent structural review

Verdict: PASS for the scalar-selector obstruction and stabilized realization, with the scope clarification below. This is a human-readable mathematical review, not a formal proof-assistant check. No selected actual HM/source-instance coefficients, points, matrices, ranks, or experiments were used.

## Checks

1. A polynomial vanishing on eleven entire lines has every relative-degree coefficient zero on the corresponding eleven base points. A nonzero remaining coefficient would be supported at one point. Its Gamma translates span all twelve one-point supports, even if the line-bundle stabilizer character is nontrivial. The restriction image is Gamma-stable, so its dimension would be twelve. All coefficient-domain dimensions for degrees zero through three are strictly less than twelve. The exclusion is sound; it does not exclude operator-valued cancellation or operators that already vanish on other lines for reasons unrelated to a scalar cutoff.

2. Twisting the complete-intersection Koszul sequence by (4,2) gives (0,-4), two copies of (2,-1), and I_R(4,2). Kunneth gives zero cohomology for (2,-1), h1(0,-4)=3, and h2(0,-4)=0. Therefore h0(I_R(4,2))=3 and h1(I_R(4,2))=0. The fifteen-dimensional space restricts onto twelve values. Every binary quartic in the positive variable is an ambient positive quadratic after the Veronese parametrization, so the ambient lift is justified.

3. A (2,2) ambient selector restricts to a scalar multiple of t^2 s^2 on its selected line and to zero on each other line. This preserves skewness and center parity when multiplied into PR679's twist-four operators. The resulting twist-eight operator vanishes on the full negative vertex and produces the intended normalized quintic times t^2 s^2. There are independently three coefficients on twelve lines, dimension 36. This is a realizable subspace of the full twist-eight receiving space, not necessarily the whole twist-eight receiving space.

4. The coefficient line bundles shift by (4,2), giving (7,9), (11,7), and (15,5). Their C10 weight exponents 3p+q are 30,40,50, all zero modulo ten. Their induced section modules are consequently the permutation module 1+A+V+D. The selector coefficient itself has exponent 14, not zero modulo ten. It has no nonzero invariant section on the transitive orbit. There is no canonical equivariant unit identifying the original target with the shifted target, despite pointwise frame-dependent normalizations. The construction proves surjectivity onto the shifted subspace; it cannot transport the original equivariant forcing without additional data.

5. The shifted receiving subspace is Gamma-stable. Restrict the operator domain to its inverse image; the resulting linear map is equivariant and onto. In characteristic zero, averaging any linear lift of a map from a finite-dimensional Gamma representation gives an equivariant lift. This justifies the parameter-family statement without requiring any individual selector or linewise lift to be equivariant.

## Scope

The scalar localization cost is exactly four. The fixed twist-four simultaneous operator image remains undetermined. The stabilization cannot be inverted globally by division: the selectors vanish at both endpoints and only give local units away from them. No coupled source solution, Bockstein, higher-order, or algebraicity conclusion follows.

The final revised proof includes the realizable-subspace/preimage qualification, the changed stabilizer characters, the lack of an invariant multiplier unit, and the shifted parameter-family dimension eighteen. Independently ran verify.py: PASS. Its bounded arithmetic checks support the degree/cohomology/character bookkeeping; they do not machine-formalize the transitivity or operator-lifting argument and do not evaluate the actual source instance.

## Added joining-scroll extension check

Section 5 also passes. With the lines convention, O_X(-1) embeds in p*(O(-2,0) plus O(0,-1)); the dual tautological evaluation has kernel p*O(2,1) tensor O_X(-1). Factoring H O_X through p*(O(2,0) plus O(0,1)) gives exactly the asserted extension of F_X. Exterior squaring an extension by a line bundle gives the displayed extension of E_X, with N of rank six and splitting O(-2,0)^2 plus O(-1,-1)^4. Since K has rank three, the wedge pairing on Lambda^2 K vanishes, giving the Lagrangian claim.

On the negative-endpoint section with negative coordinate fixed, F_X is constant rank four and E_X is constant rank twelve. The F quotient is O(2); the E quotient is U tensor (O(1)^2 plus O(2)). Every morphism from either positive-degree quotient to its trivial middle bundle is zero. A splitting would supply a nonzero right inverse, a contradiction. Thus both extensions are genuinely nonsplit globally on the full scroll. This does not extend the claim to the finite union of ramification lines and does not settle the fixed-twist interpolation map. No selected ramification point was evaluated in the argument.
