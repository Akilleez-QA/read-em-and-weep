# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: fourth triple-diagonal ideal power

## Verdict

PASS over C, with the natural ungraded S4 descent linearization on A=q*O_Y(1), and with the fixed binary determinant lines normalized as in the existing coefficient proof.

The following are valid for ordinary ideal powers, including at quadruple collisions:

- Locally, (I_D^4 : v)=I_D after trivializing A^3.
- Globally, (q_*I_D^4)_sign is I_N tensor O_Y(-3).
- For EA=q*B0 tensor A^(-1), the resulting coefficient sheaf is (q_*(I_D^4 EA))_sign = B0(-4) tensor I_N.
- The reduced triple-root surface N in P4 is scheme-theoretically the complete intersection (t2,t3), of degrees 2 and 3.
- The fifth ideal power has exactly the same sign pushforward as the fourth.

No source value, source order, obstruction coordinate, or physical-source cancellation is evaluated. These are coefficient-sheaf statements, and do not by themselves determine an induced cohomology map.

## 1. The upstairs ideal remains a regular-sequence ideal at quadruple collisions

On a common affine root chart put a=x1-x4, b=x2-x4, c=x3-x4. Up to the nonzero normalization constants in the weight identities,

    I_D=(a(c-b), b(c-a)).

The two displayed quadrics have no common irreducible factor, and hence form a regular sequence in C[x4,a,b,c]. Their four minimal primes are

    (a,b), (a,c), (b,c), (a-b,b-c).

The Jacobian has rank two at generic points of each component. The complete-intersection quotient is Cohen–Macaulay and therefore satisfies S1, while this rank calculation proves that it is generically reduced. Consequently it is reduced. This includes the locus a=b=c=0: there is neither an embedded component nor a nilpotent thickening there.

Every ordered root configuration is contained in some common affine root chart. Thus this local description verifies the global reduced complete-intersection assertion. It also explains why a singular, reducible D still has a regular-sequence ideal at the quadruple diagonal. Smoothness of D is not required.

## 2. The colon calculation

Let R be a local ring of Z on a trivializing open for A, and let x,y be the two weight-difference generators of I=I_D R. The Vandermonde identity has the form

    v=c x y (x-y),

where c is a nonzero scalar, up to a harmless sign from the choice and order of generators. More generally, replacing c by a local unit has the same consequence.

Since x,y form a regular sequence, the standard associated-graded description is

    gr_I R = (R/I)[X,Y].

The initial class of v in I^3/I^4 is c XY(X-Y). Multiplication by this polynomial is injective over every coefficient ring R/I, even a ring with zero divisors: multiplication by X and Y is injective, and X-Y is monic as a polynomial in X over (R/I)[Y]. Equivalently its leading coefficient is a unit.

If fv belongs to I^4, its degree-three class gives

    (f mod I) c XY(X-Y)=0.

Injectivity implies f mod I=0, so f belongs to I. Conversely, I v is contained in I^4 because v belongs to I^3. Thus

    (I^4:v)=I.

This proof uses ordinary powers and the I-adic associated graded ring. It does not use symbolic powers or identify I-adic order with order in the maximal ideal of a quadruple collision. In fact, the weight generators are quadratic in small-diagonal coordinates there, but this does not affect their role as the two degree-one generators of gr_I R.

Globally, the invariant statement is that the inverse image of I_D^4 under multiplication v:A^(-3)→O_Z is I_D tensor A^(-3).

## 3. Alternating division, contraction, and the line twist

The Vandermonde is a sign-equivariant section of A^3. Its divisor is the sum of the six pair diagonals, each with multiplicity one. An alternating regular function on a quotient-adapted open vanishes on every pair diagonal: the corresponding transposition fixes that diagonal pointwise and acts trivially on a descended coefficient fiber.

Because Z is smooth, vanishing on these distinct prime divisors permits regular division by their product. Therefore multiplication by v identifies invariant sections of A^(-3) with sign sections of O_Z. This proves

    (q_*O_Z)_sign = O_Y(-3).

The colon calculation says that the alternating section v h belongs to I_D^4 precisely when the regular quotient h belongs to I_D tensor A^(-3). Since h is invariant, finite pushforward and projection formula give

    (q_*I_D^4)_sign
      = (q_*(I_D tensor A^(-3)))^S4
      = (q_*I_D)^S4 tensor O_Y(-3).

Let N be the reduced image q(D). The contraction of I_D to O_Y is exactly I_N. One way to see this is to apply the exact invariant functor in characteristic zero to

    0→I_D→O_Z→O_D→0.

The resulting kernel inside O_Y consists precisely of functions vanishing on the reduced image. Alternatively, on affine quotient charts the contraction of a radical ideal is radical, and its zero set is q(D). Hence

    (q_*I_D)^S4=I_N,

and the claimed sign pushforward follows.

Important distinction: this is an invariant contraction statement. It does not assert q*I_N=I_D. Indeed the descended generators t2,t3 pull back into I_D^2 and I_D^3 respectively, so the schematic inverse image of N is generally thicker than reduced D. No such false pullback identification is needed.

Finally, EA=q*B0 tensor A^(-1)=q*(B0(-1)). Projection formula therefore gives

    (q_*(I_D^4 EA))_sign
      = B0(-1) tensor (q_*I_D^4)_sign
      = B0(-4) tensor I_N.

Here the notation “sign summand” means the sign multiplicity sheaf after the fixed one-dimensional sign representation is suppressed. If it means the literal isotypic equivariant sheaf, that representation remains as an explicit tensor factor. The ordinary sheaf and line exponents are unchanged.

## 4. Scheme-theoretic equations for the triple-root surface

Write the three weight values as a,b,c with a+b+c=0. Their differences span the weight ideal. The trace invariants

    t2=2(a^2+b^2+c^2),
    t3=2(a^3+b^3+c^3)

use the full rank-six trace convention of PROOF.md: each pairing value occurs twice. They are S4-invariant sections of A^2 and A^3, and therefore descend to sections of O_Y(2) and O_Y(3).

Their common zero set upstairs is D. Indeed

    ab+ac+bc=-t2/4,    abc=t3/6,

so a,b,c are roots of

    T^3-(t2/4)T-t3/6.

If t2=t3=0, all three values are zero. Conversely zero weights give zero traces. Since a+b+c=0, zero weight differences are equivalent to zero weights. The finite surjective quotient therefore gives the set-theoretic equality V(t2,t3)=N downstairs.

The map

    P1×P1 → P4,    (l,m) ↦ l^3m,

has image N and is generically one-to-one: a quartic with one triple root and one distinct simple root determines l and m uniquely. Its pullback of O_Y(1) is O(3,1). Thus N is an irreducible surface and

    deg N=(3h1+h2)^2=6.

For completeness, this supplies a slightly more economical complete-intersection proof than separately proving irreducibility of t2. Since V(t2,t3) has dimension two in P4, the homogeneous ideal (t2,t3) has height two in the five-variable homogeneous coordinate ring. The nonzero quadratic and cubic therefore form a regular sequence. Their projective zero scheme X is a codimension-two complete intersection, is Cohen–Macaulay and unmixed, and has degree 2·3=6.

The support of X is the single irreducible surface N. The degree formula then says

    deg X = length(O_X at the generic point of N) · deg N.

Both degrees are six, so the generic length is one. Thus X is generically reduced. A Noetherian S1 scheme that is generically reduced is reduced; equivalently, Cohen–Macaulayness precludes embedded associated primes on which residual nilpotent structure could be supported. It follows that X=N as schemes, including along the quadruple-root curve.

Consequently the ideal sheaf has the Koszul resolution

    0→O_Y(-5)→O_Y(-2)⊕O_Y(-3)→I_N→0.

Tensoring by the locally free bundle B0(-4) gives

    0→B0(-9)→B0(-6)⊕B0(-7)→B0(-4)I_N→0.

The first map has the usual two-generator Koszul signs, for example (-t3,t2), and the second is multiplication by (t2,t3).

## 5. Fifth-power corollary

The added fifth-power claim in PROOF.md, section 7, also passes:

    (q_*I_D^5)_sign=(q_*I_D^4)_sign=I_N tensor O_Y(-3).

The associated-graded argument generalizes directly to

    (I^k:v)=I^(k-3),    k≥3.

For k=5, for example, the fourth-power calculation first forces f into I; then injectivity of multiplication by the initial cubic from degree one to degree four forces f into I^2. The reverse inclusion is immediate.

It remains to compare invariant sections of I and I^2. The regular-sequence generators give an equivariant conormal isomorphism

    I/I^2 = U tensor A^(-1)|_D,

with U the two-dimensional S4 representation of shape (2,2). On a triple-diagonal component, its pointwise-fixing S3 maps isomorphically to the S3 permuting the three pairings. Consequently the restriction of U is the standard two-dimensional S3 representation and has no invariants. The descended line A^(-1) is trivial as a stabilizer representation.

An invariant conormal section thus restricts to zero on each of the four components. Since D is reduced and I/I^2 is locally free over O_D, componentwise restriction is jointly injective, even where components meet. Therefore (q_*(I/I^2))^S4=0. Exact finite pushforward and exact invariant projection applied to

    0→I^2→I→I/I^2→0

now give (q_*I^2)^S4=(q_*I)^S4=I_N. Combining this with the fifth-power colon identity proves the claim, with the same line twist as before. Projection formula gives the identical equality with the coefficient EA.

There is also a consistency check from the explicit ideal equations: both pullbacks t2 and t3 lie in I^2, and they generate I_N downstairs. Thus every descended coefficient vanishing on N already pulls back into I^2. This gives a second proof of the same invariant equality once the complete-intersection equations have been established.

The assertion concerns equality of sign subsheaves under the Vandermonde identification, not equality of the upstairs ideals I^4 and I^5.

## 6. Scope and dependencies

The audit assumes characteristic zero, the actual descent linearization on A and B0, the stated weight-difference/Vandermonde identities, and the identification of t2,t3 with the two trace invariants. The nonzero normalization constants do not matter. One-dimensional binary determinant factors may be restored if a GL2-equivariant statement is intended; no GL2 action on B0 is inferred.

The earlier local complete-intersection argument was independently rechecked against its explicit equations in WEIGHT-DIFFERENCE-LOCUS.md and its audit. The line conventions and alternant divisor argument were checked against prerequisite weighted-koszul-cohomology, document PROOF.md. (see the unit INPUTS.md) This is a bounded algebraic verification, not a fresh verification of the imported physical source or its equivariance hypotheses.
