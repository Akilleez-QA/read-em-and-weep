# Structural cycle proof for all six pinned inclusions

## Result and precise scope

For each of the six pinned carrier records, the decoded inclusion satisfies

    delta I_c = 0.

This proof uses a universal sparse cyclic system, two explicit kernel formulas, and an exhaustive inert signed-label binding. It does not assume primitive A, any contraction or exactness claim, a determinant normalization, a complementary inverse, or a historical successful check. It also does not import or execute the source, multiply actual polynomial matrices, expand actual stored polynomial products, specialize a physical point, or run a physical source or jet.

Interpret the source records in an exact commutative Q-algebra, with each displayed inclusion denominator invertible. The decoder interpretation is the ordinary meaning of a stored list of signed monomial records: numerator divided by `di`. The proof is algebraic on these localizations. It establishes neither that a particular physical point belongs to a carrier nor an aggregate obstruction verdict.

The authenticated model snapshot has SHA256

    635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926

and Git blob `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`. Its immutable source is recorded in `source-pins.json`.

## 1. Universal cyclic differential

Work initially with five commuting indeterminates v_0,...,v_4. Subscripts in this section are modulo five. Write the 15 source coordinates as

    (A_0,...,A_4, B_0,...,B_4, C_0,...,C_4)

and the ten output coordinates as (Y_0,...,Y_4,Z_0,...,Z_4). Define

    Y_i = v_(i-1) A_(i+2) - v_(i+1) A_(i-2)
          + v_(i+2) C_(i+1) - v_(i-2) C_(i-1),
    Z_i = v_(i+2) B_(i+1) - v_(i-2) B_(i-1)
          + v_(i-1) C_(i+2) - v_(i+1) C_(i-2).

The literal checker compares this pattern to every one of the 150 stored delta entries, including all zeros, after setting v_0=1. Thus the displayed operator is the pinned operator, with no uninspected entries.

Cyclically shift the subscripts so that a primary chart c becomes zero. Write

    (x,u,v,w,t) = (v_c,v_(c+1),v_(c+2),v_(c+3),v_(c+4)).

All A, B, C indices in the next section are relative to this c.

## 2. Primary kernel formula from four scalar recurrences

Set the five coordinates

    A_1=A_4=B_2=B_3=C_0=0

and leave A_0=a and B_0=b free. The equations Y_1,...,Y_4,Z_1,...,Z_4 are exactly the four forced-coordinate equations

    A_2 = -v C_3/x,       A_3 = -w C_2/x,
    B_1 =  u C_4/x,       B_4 =  t C_1/x,

together with the four-step recurrence

    x C_1 = t C_3 - w a,
    x C_2 = w C_1 + u b,
    x C_4 = u C_2 - v a,
    x C_3 = v C_4 + t b.                         (1)

These equations follow by reading the four nonzero coordinate terms of each row. No matrix product is being formed.

Put

    Delta = x^4 - uvwt,       d = -x Delta = xuvwt - x^5,
    Q = tv^2 + x^2w,         R = uw^2 + x^2v,
    S = u^2v + x^2t,         T = wt^2 + x^2u.

Assume d invertible. This already makes both x and Delta invertible, so every displayed division is legal. Closing the recurrence (1), in the order C_1 -> C_2 -> C_4 -> C_3 -> C_1, gives

    Delta C_1 = -x Q a + t S b.

The other three coordinates, obtained from the same recurrence, are

    C_1 = (-x Q a + t S b)/Delta,
    C_2 = (-w Q a + x T b)/Delta,
    C_3 = (-v R a + x S b)/Delta,
    C_4 = (-x R a + u T b)/Delta.                (2)

For a short independent hand verification of this generic recurrence solution, the only scalar identities needed are

    tvR - x^2Q = -w Delta,
    x^2T - wtS =  u Delta,
    uwQ - x^2R = -v Delta,
    x^2S - uvT =  t Delta.

Each is a two-binomial distributive cancellation in five arbitrary commuting symbols. These are universal identities, not products computed from the stored source. They respectively verify the four equations in (1).

The two as-yet unused output equations vanish without a separate complex or exactness premise:

    Y_0 = [v(x C_1 - t C_3) - w(x C_4 - u C_2)]/x
        = [v(-wa)-w(-va)]/x = 0,
    Z_0 = [t(x C_2 - w C_1) - u(x C_3 - v C_4)]/x
        = [t(ub)-u(tb)]/x = 0.

Consequently (2) and the four forced-coordinate equations give a kernel vector for every a,b. In fact the solution with the prescribed five zero coordinates and prescribed a,b is unique, because recurrence closure determines C_1 and then every remaining coordinate. Uniqueness is not needed for the result.

### The two primary inclusion columns

Choose (a,b)=(1,0) for the first column and (a,b)=(0,x) for the second. Write both over the common denominator d=-x Delta. Their complete numerator table is

| Coordinate | First numerator | Second numerator |
| --- | --- | --- |
| A_0 | d | 0 |
| A_1 | 0 | 0 |
| A_2 | -v^2 R | x^2 v S |
| A_3 | -w^2 Q | x^2 w T |
| A_4 | 0 | 0 |
| B_0 | 0 | x d |
| B_1 | x u R | -x u^2 T |
| B_2 | 0 | 0 |
| B_3 | 0 | 0 |
| B_4 | x t Q | -x t^2 S |
| C_0 | 0 | 0 |
| C_1 | x^2 Q | -x^2 t S |
| C_2 | x w Q | -x^3 T |
| C_3 | x v R | -x^3 S |
| C_4 | x^2 R | -x^2 u T |

The checker contains a handwritten signed factor-word form of this table. For each c=0,...,4, it merely renames x,u,v,w,t to their cyclic variable labels, omits the v_0 label because v_0=1, and compares bags of signed labels with the source's exponent records. Every one of the 150 primary inclusion entries and all five denominators match. No source polynomial arithmetic is used to establish that binding.

Thus the five stored primary inclusions are precisely the two universal kernel vectors just proved.

## 3. Auxiliary kernel formula by sparse elimination

For this section set v_0=1 and write

    (a,b,c,d) = (v_1,v_2,v_3,v_4).

These letters are independent of the preceding section's notation. Set

    A_4=B_2=B_3=C_0=C_1=0,

and leave B_0=p and C_4=q free. The eight nonpivot equations of the same differential are

    Y_1 = A_3 + c C_2,
    Y_2 = -c A_0 + d C_3,
    Y_3 = b A_0 - d A_1 - a C_2 + q,
    Y_4 = c A_1 - A_2 - b C_3,
    Z_1 = -d p + C_3 - b q,
    Z_2 = -B_1 + a q,
    Z_3 = B_4,
    Z_4 = a p - C_2.

They vanish on the following solution, read in the order C_2,C_3,B_1,B_4,A_3,A_0,A_1,A_2:

    C_2 = a p,                 C_3 = d p + b q,
    B_1 = a q,                 B_4 = 0,
    A_3 = -ac p,
    A_0 = (d^2/c)p + (bd/c)q,
    A_1 = (bd/c - a^2/d)p + (b^2/c + 1/d)q,
    A_2 = -(a^2c/d)p + (c/d)q.                 (3)

The unused two equations also vanish directly:

    Y_0 = d A_2 - a A_3 - c q = 0,
    Z_0 = b B_1 + d C_2 - a C_3 = 0.

Take the first column to have (p,q)=(1,0) and the second (p,q)=(0,-d/a^2). The common denominator is

    h = -a^2 c d.

When h is invertible, a,c,d are invertible; no other variable must be a unit. Expressing (3) with denominator h gives the complete auxiliary numerator table:

| Coordinate | First numerator | Second numerator |
| --- | --- | --- |
| A_0 | -a^2d^3 | bd^3 |
| A_1 | a^4c-a^2bd^2 | b^2d^2+cd |
| A_2 | a^4c^2 | c^2d |
| A_3 | a^3c^2d | 0 |
| A_4 | 0 | 0 |
| B_0 | -a^2cd | 0 |
| B_1 | 0 | acd^2 |
| B_2 | 0 | 0 |
| B_3 | 0 | 0 |
| B_4 | 0 | 0 |
| C_0 | 0 | 0 |
| C_1 | 0 | 0 |
| C_2 | -a^3cd | 0 |
| C_3 | -a^2cd^2 | bcd^2 |
| C_4 | 0 | cd^2 |

Every one of these 30 literal entries and the denominator h matches the pinned auxiliary chart by the same signed-label comparison. Therefore its two decoded columns are exactly the kernel vectors proved above.

## 4. Evidence boundary and reproduction

`check_cycle_metadata.py` verifies the immutable SHA256 and Git blob first. It then verifies all 150 delta cells, all 180 inclusion cells, and six inclusion denominators. It treats a monomial only as an integer sign and a bag of variable-name labels. It does not construct a polynomial object, add coefficients, cancel terms, multiply source entries, or execute source code. The expected signed-factor lists were written from the universal tables above, rather than computed from actual matrix products.

Run, with only the Python standard library:

    python check_cycle_metadata.py
    python -O check_cycle_metadata.py

Both pass; the reports are retained. `check_metadata_controls.py` additionally rejects seven deliberately wrong metadata expectations or input-byte mutations, in ordinary and optimized runs. These integrity controls are not physical or algebraic evaluations. Explicit exceptions are used, so optimization cannot disable the checks. The metadata pass establishes exhaustive source binding. The preceding hand argument establishes the mathematical identity; these are distinct claims.

This closes delta I=0 for the six pinned rational matrices, subject only to decoder semantics and their stated localizations. It supplies one ingredient toward a proof of primitive A; it is not itself a claim that primitive A or the entire contraction system has been established. No permission to run the physical source, publish, or change production guards is implied.
