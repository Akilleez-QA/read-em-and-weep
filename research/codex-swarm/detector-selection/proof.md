# Why the selected weighted outputs give 32 independent rational tests

## Pinned complex and bases

The constant model is the perfect four-term P4 complex with ranks `(5,15,10,2)` and its End complex. It is read at commit `f968b53943ba2312f09fbc3e8f9d462e86bcaa34`, path `research/hm/d8-small-certificates/p4/check_hm_p4_all_twists.js`, Git blob `7adc1d6a733636204b1dd613870c168717be6277`.

The exact basis function orders tuples `(u,v,target row,source column,m0,m1,m2,m3,m4)`, with `v-u` the internal degree. Monomials use the source's recursive ascending-exponent order. Both matrices and multiplication targets use these same full tuples; a numerical index alone is not an identification of Hom direction or monomial.

The source's `matrix(1,-1)` and `matrix(2,-1)` give

`B1 : Q^245 -> Q^400`, `C1 : Q^400 -> Q^150`.

At twist zero, `matrix(1,0)` and `matrix(2,0)` give

`B0 : Q^1225 -> Q^1200`, `C0 : Q^1200 -> Q^350`.

The rational ranks are `rank B1=240`, `rank C1=150`, `rank B0=848`, `rank C0=350`. The independent saved certificate at the same commit, Git blob `304d031083bb2a19fb9bc012cfd338bbe0129980`, records complete unit-pivot ranks with zero residual tail. These are inherited rational upper bounds; the new producer blob-authenticates their receipt and ties its matrices to the same constructor/basis. The source also gives `h^2 End(K)(-1)=10` and `h^2 End(K)=2`.

## Twenty starting classes and the trace orientation

At twist minus two, the ordinary map is `E : Q^80 -> Q^50`, of rank 50. Its saturated 30-dimensional kernel has free coordinates 50 through 79. Let `K_j` denote the kernel vector with free coordinate `j` equal to one. The free coordinate corresponds to positive `M13[target b,source i]` with `j=15b+i`.

The published d5 certificate at commit `e6e8d272e760a432dbbc1053b88c8eae03a47304`, `research/hsd/twist-minus2-d5/NOTE.md`, Git blob `0a1d5d00a85e13bcf535a2001577eb0eafc77f43`, identifies the ten quotient relations

`[K_r]+[K_(25+r)]=0`, `[K_(10+r)]+[K_(20+r)]=0`, for `r=0,...,4`.

It follows that `I20={(i,0):5<=i<=10} union {(i,1):0<=i<=14,i!=5}` selects twenty independent classes in `H^2 End(K)(-2)`. This d5 quotient premise is inherited, not recomputed by the present producer.

For the scalar row `L_(i,b)` defined in README, the supertrace-dual cycle is `c_(i,b)=-K_(15b+i)`. In coordinates it has

- `M13[b,i]=-1`;
- `M02[5b+k,a]=-gamma[i,a,k]`;
- all other entries zero.

The producer reconstructs these entries from the authenticated gamma and checks `E c=0` as an exact integer equation. With complex degrees `0,1,2,3`, `str(X K_j)=-L_(i,b)(X)`; Hom directions are reversed in this identification. A uniform shift of the whole resolution changes a common sign and does not change rank.

## Multiplication and the new rank certificates

Multiplication by `v_k` maps each starting cycle to a cycle in the 400-dimensional twist-minus-one degree-two term. Multiplication by `v_k v_l` maps it into the 1,200-dimensional twist-zero term. These are multiplication of constant-resolution sections by homogeneous base monomials, not multiplication of any physical source polynomial.

The producer verifies `C1 B1=0` and `C0 B0=0` over the integers. It then checks all 100 single-variable and 300 quadratic multiplication candidates are exact integer cycles. It iterates I20 in its displayed order (first `b=0,i=5..10`, then `b=1,i=0..14` excluding 5). Within each class, single variables use `k=0..4`, and quadratic monomials use `k=0..4,l=k..4`. The selection is deterministic under this order; it is not a claim about global lexicographic order on `(i,b,k)`.

Over F_101, sparse elimination gives

`rank B1 = 240`, `rank[B1 | Q10] = 250`,

`rank B0 = 848`, `rank[B0 | Q2] = 850`.

Here `Q10` and `Q2` are the actual selected candidate columns whose labels are retained in `selection.json`. A nonzero modular minor of an integer matrix remains a nonzero rational minor. Therefore the rational augmented ranks are at least 250 and 850. Since the *separately authenticated rational boundary ranks* are 240 and 848, the selected quotient classes have rank at least 10 and 2 over Q. The exact cycle equations and the inherited rational cohomology dimensions bound them above by 10 and 2. They are bases of the respective cohomology groups.

Matching modular boundary ranks alone would not justify the rational quotient conclusion. For example `B=(101,0)^t`, `q=(1,0)^t` has a modular rank increment but no rational quotient increment. The independent rational boundary-upper-rank premise prevents that error here. No modular cohomology stability or characteristic-three source theorem is assumed.

The independent verifier now also removes reliance on the saved upper-rank receipt for these two ordinary boundary ranks: it separately reconstructs the arrows/bases and obtains exact integer unit-pivot ranks 240 and 848 with zero remaining rows, maximum intermediate bit lengths two and four. It likewise obtains outgoing ranks 150 and 350, hence quotient dimensions ten and two. Its different modular pivot order verifies the selected augmented ranks 250 and 850. The earlier twenty-class d5 quotient premise remains inherited.

## Output-polynomial bridge and inherited geometric premises

On `Y=(P1)^4`, let

`Q = X1 X2 Y3 Y4 + Y1 Y2 X3 X4`.

The previously proved invariant splitting is

`R^D8 = A directsum A Q directsum A Q^2`, with `A=Q[v0,...,v4]`.

It uses Q's three distinct S4 conjugates and the exact Hilbert numerator `1+t+t^2`. The full-sign deck eigensheaf has natural line `O(-2)^4`; the canonical sheaf differs from this linearization by permutation sign. Equivariant Serre duality therefore identifies the dual of the epsilon obstruction space with

`H^2 End(K) directsum H^2 End(K)(-1) Q directsum H^2 End(K)(-2) Q^2`,

of dimensions `2+10+20=32`. The scalar target is `H^4 O(-4)^4`, whose epsilon dual is the invariant polynomial subspace of `H^0 O(2)^4`. Consequently a selected class `v_k c_(i,b)` labels the actual scalar output test `(L_(i,b),v_k Q)`, and a selected `v_k v_l c_(i,b)` labels `(L_(i,b),v_k v_l)`. The twenty initial classes label `(L_(i,b),Q^2)`.

These are 32 WEIGHTED Laurent pairings, not 32 individual Laurent positions. In the pinned finite-chart normalization `v_k=e_k(x)` (without binomial normalization or coefficient signs), `f=sum_m f_m x^m` gives the request `sum_m f_m c[k(m)]`, `k(m)=sum_(nu=1)^4 (2-m_nu)*3^(4-nu)`. The exponents requested from the scalar are `-m_nu-1`. The scalar must be in the authenticated original frame, including division by the deck product and the `tau^-4` conversion.

Thus the explicit twenty plus ten plus two weighted labels in README separate the conditional rational epsilon sector. This bridge inherits the source-pinned perfect-complex, supertrace, invariant-splitting and geometric-membership proofs in `small-scalar-detector-route.md`, `twenty-map-completeness.md`, and PR1 comments `6130352358`, `6130391535`, and null's acceptance `6210564082`. The present rank selection does not re-prove characteristic-zero source membership or compute a physical pairing.

Actual use on Rsharp still requires the complete corrected representative, its authenticated regular transport and all owned frame/gerbe/top-homotopy data. Thirty-two zero values would then prove vanishing of that epsilon class; a single authenticated nonzero value would prove nonvanishing. These values remain uncomputed. In particular, classification of the constant scalar rows does not give the special old-scalar carrier merger or source-cost bounds for the other maps; applying the old 78-summand compiler to them would need its own proof. Independent D03 accepts the conditional P4/Serre/output-polynomial bridge and this normalization, with no source evaluation claimed.
