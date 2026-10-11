# The +2 (mod 4) copies are the pair-swap involution

Pinned package: `b1fdcdd666ed188250d6def3616733f1417fca81` (#57).

The six identical coefficient arrays are the orbits of one carrier involution.
They are not a packaging defect. The signed readings on an orbit do not cancel.

## Which symmetry

Index the four factors of `Y=(P^1)^4` by `0,1,2,3`. Define

```text
iota(i) = i + 2 (mod 4),
```

the involution `(0 2)(1 3)`. In one-based labels this is `(1 3)(2 4)`.

It is not the Heisenberg cycle. The Horrocks–Mumford monad in #2 is indexed
modulo 5, and #14 transports charts by `r -> r+j (mod 5)`. That cycle moves
the five coordinates `v_0,...,v_4`. It does not permute the four factors by 2.

The four factors enter through the degree-24 quotient

```text
(P^1)^4 -> Sym^4 P^1 = P^4
```

of #2. The full symmetric group acts by permuting factors. The second-order
bivector of #31 keeps only one involution in that group:

```text
pi = V1 wedge V2 + V3 wedge V4,    Vi = yi d/dxi.
```

Applying `iota` exchanges the two wedges, so `iota_* pi = pi`. The same swap
preserves the gerbe class of #14,

```text
q1 cup q2 + q3 cup q4,
```

and the full-sign formulae of #31: the product `u12 u34 + u34 u12`, the
cross bidifferentials, and the Moyal bracket

```text
(d13 g)(d24 g) - (d14 g)(d23 g) - (d23 g)(d14 g) + (d24 g)(d13 g).
```

If `g` is constant on the symmetric quotient, differentiation gives
`d_a g(x) = d_{iota(a)} g(iota x)`. Each product above is unchanged, not
negated. The normalizing factor `y1 y2 y3 y4` is likewise invariant, because
`iota` is the product of two transpositions and has sign `+1`.

#36 and #37 build one numerator on these four coordinates and then extract
axes. An `iota`-invariant numerator therefore has identical reversed windows
for an orientation `e=(i,j,k,l)` and for `iota e`. #34 sums those orientations
as separate inputs and says the functional does not assume a permutation
symmetry. The equality is a symmetry of the numerator, not a collapse built
into the sum.

A transposition such as `(0 1)`, or the Heisenberg shift modulo 5, does not
preserve `pi`. Orientations outside an `iota` orbit are not identified.

## What the sign and the selector do

`sign(iota)=+1`, so `sign(iota e)=sign(e)`. The paired signed contributions
are the same quotient, read with the same sign, on two rectangles. The
rectangles differ because `m=(2,2,2,0)` is not `iota`-invariant: `iota` swaps
axis 1, where the weight is 2, with axis 3, where the weight is 0. Thus `d=6+m_j`
and `L=22-m_l` move, and the readings do not cancel.

Exact pair sums, each nonzero:

| Orbit | Signs | Selectors `(d,L)` | Signed values | Sum |
| --- | --- | --- | --- | ---: |
| 0123, 2301 | +1, +1 | (8,22), (6,20) | 8655/16, 131/2 | 9703/16 |
| 0132, 2310 | -1, -1 | (8,20), (6,20) | -2817/16, -169/2 | -4169/16 |
| 0213, 2031 | -1, -1 | (8,22), (8,20) | 18831/8, 42869/16 | 80531/16 |
| 0231, 2013 | +1, +1 | (8,20), (8,22) | -21601/8, -41517/16 | -84719/16 |
| 0312, 2130 | +1, +1 | (6,20), (8,20) | 1457/8, 21869/16 | 24783/16 |
| 0321, 2103 | -1, -1 | (6,20), (8,22) | -803/4, -22917/16 | -26129/16 |

The six orientations whose first index is 1 are sent to first index 3.
Those partners are absent from the active sum, because `m_3=0`. Nothing in
`iota` equates 1023, 1032, 1203, 1230, 1302, 1320 with each other or with
the six orbits above. Their coefficient arrays are six further polynomials.

## What 0/1 means

The eighteen signed readings use **12** quotient polynomials: six polynomials
read twice, and six polynomials read once. The forced relation is

```text
Q(iota e) = Q(e),
```

not `signed(iota e) = -signed(e)`.

Both blocks happen to vanish separately. The twelve paired readings sum to
`0/1`, and the six unpaired readings sum to `0/1`. The separate zeros are
arithmetic facts about these selectors. They are not pairwise cancellation
along `iota`, since every pair sum above is nonzero, and the six unpaired
orientations have no active partner.

So `0/1` is the sum of twelve selector readings of an `iota`-invariant
numerator, with six of the polynomials contributing two readings. It is still
one coordinate of one scalar map. It is not the vanishing of the whole
`L_minus` image and not the vanishing of the full obstruction.

```sh
python3 research/hsd-review/57/symmetry/check_involution.py
```

Exit status `0` requires the same gate as the aggregate checker: pinned
arithmetic, 18 orientations, precisely those six equal-list pairs, matching
paired signs, 12 distinct lists, six active singletons, and total `0/1`.
A surviving pair symmetry is not enough. The tests do not regenerate the
source DAG.
