# Every negative direction has a finite lower positive obstruction

## Result

For every nonzero negative binary quadratic a, the actual pencil

    M(t)=q0+t a:H1(B)_+ -> H1(B(2))_+

has source dimension12, target dimension41, generic rank12, and rank11 at t=0. Its unique nonunit local Smith factor at t=0 is t^e times a unit, with

    2 <= e <= 12.

This is uniform over all nonzero a, including repeated-root quadratics. It gives a finite obstruction bound for extending the canonical nilpotent N. It does NOT imply that the twist-four positive pencil is generically surjective: polynomial multiples can kill the eventual lower obstruction.

## 1. The negative quadratic coefficient itself is injective

Over the complex numbers write a=u v with nonzero negative linear forms, allowing u=v. The actual hyperplane restriction sequences identify the kernels of

    u:H1(B) -> H1(B(1)),
    v:H1(B(1)) -> H1(B(2))

with images of H0(B_Hu(1)) and H0(B_Hv(2)), respectively. Both section spaces vanish for EVERY negative hyperplane by UNIFORM-HYPERPLANE-LOWER-VANISHING-AND-JUMP-BOUND.md. Thus both linear maps, and their composite a, are injective. Parity is tracked through the intermediate odd summand; their composite preserves the positive summand.

In particular the coefficient of t has rank12. Some twelve-minor of M(t) therefore has nonzero degree-twelve leading coefficient, proving generic injectivity along every such line without a generic-quadric assumption.

## 2. The unique Smith exponent

The invariant-cone closure gives H0(B_Q0(2))_+=C N and hence rank M(0)=11. Over C[[t]], row and column operations split eleven unit factors. Since M(t) is generically injective, its remaining one-column block has a nonzero common valuation e; equivalently its local Smith form has eleven units and one t^e. The forty-one target rows cause no additional nonzero source invariant factors.

POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md constructs xi-t zeta_a with residual divisible by t^2 and nonzero constant xi. Thus e>=2. Every maximal minor is divisible by t^e. Choose a nonzero maximal minor; its polynomial degree is at most twelve, so its valuation, and therefore e, is at most twelve.

The obstruction at order e is nonzero. Earlier lower Bocksteins on the continuing one-dimensional kernel vanish. This is a bounded, exact termination statement for the lower pencil, not an evaluation of which e occurs.

## 3. Relation to the remaining twist-four problem

At first order all twist-four kernel vectors h xi have correction -h zeta_a. Their second obstruction is -[a h zeta_a] in the four-dimensional P4 quotient. More generally a lower formal correction can be multiplied by h, but the resulting target obstruction is then projected to the different twist-four cokernel. A nonzero lower obstruction can be annihilated by this multiplication or projection. Therefore the uniform finite lower order does not by itself prove the desired rank37 at twist four.

The unresolved mathematical step is to prove that some actual higher twist-four obstruction has rank four (or otherwise prove generic surjectivity). No such rank is inferred from the lower Smith exponent.
