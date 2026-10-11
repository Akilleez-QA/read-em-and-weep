# The framed homogeneous five-coordinate formal chart

Work over a characteristic-zero field; all supplied coefficients and computations are rational. Write `O(b,p)` for a line bundle on `Y = P^1 × P^2`. The ambient formal neighborhood is the completion of the zero section in the normal line `O(0,1)`, equivalently the completion along `P^1 × P^2` inside `P^1 × P^3` (projection away from a point outside the plane identifies a neighborhood with this line bundle). All normal orders use the original conormal line `I = O(0,-1)` and the original homogeneous normal coordinate `h`. Fix the plane object, its alternating form, `alpha`, the section `v`, and the sign `beta(v)=+t0 h`. Here `t0` is the chosen base-coordinate section: its first scalar representative is `z` on the finite base chart and `1` on the infinity chart. The choice is also pinned by the supplied nonzero evaluation target.

## 1. Fixed model and the scope of the theorem

The model has

```
A = O(3,-6),  P = O(3,-3),  L = O(4,-2),
B = P ⊕ E,  G = B/A,  v = E0,
```

with ordered `B` coordinates `(P,E0,E1,E2)` of filtration degrees

```
(base,plane) = (3,-3), (0,0), (4,-4), (3,-4).
```

Put `S=X^2+Y^2`, `F=XY`, `a0=X^3+Y^3`, `g=S-zW^2` and `C=S^2+zSW^2+z^2W^4`. The actual finite and infinity relation vectors and infinity-to-finite transition are

```
r0 = (-a0, W^6, -g, F),
ri = (-a0, S^3, -z^-1 g, F),
TB = diag(z^3,1,z^4,z^3), with the extra entry TB[E0,E1]=z C.
```

Thus `TB ri=z^3 r0`. The ordered plane cover is `D(X),D(Y),D(W)`, with both base charts. The alternating entries on `E` are

```
omega(E0,E1)=F, omega(E0,E2)=g, omega(E1,E2)=W^6
```

on the finite chart, and `F,z^-1 g,S^3` on the infinity chart. These fix the tensor-bracket convention used by the replay.

The fixed rank-four quotient object is assumed symplectic with values in `L`, with the stated `alpha` and `G=alpha^perp`; its full plane construction is an input. The relevant sheaves are

```
U_k = A B L^-1 I^k,
W_k = Sym^2(B) L^-1 I^k,
n_k = Sym^2(G) L^-1 I^k,
0 -> U_k --multiplication by r--> W_k -> n_k -> 0.
```

`n_k` is the sheaf of infinitesimal symplectic endomorphisms fixing `alpha`. The local exactness of the resolution follows because `A` is a line subbundle of `B`. The actual off-diagonal transition is retained, so the filtration below is not treated as a splitting.

Use weights

```
wt(z,X,Y,W,h) = (2,1,1,0,-1),
d_finite(P,E0,E1,E2) = (3,0,2,2),
d_infinity(P,E0,E1,E2) = (3,6,0,2).
```

At order `k`, the required finite `W` coefficient weight is `k-4+d_i+d_j`; for `U` it is `k-4+d_i`. Infinity uses `k-8` in place of `k-4` and the infinity frame weights. Mixed cochains use the finite frame. The actual transport maps are `TU=z^-1 TB` and `TW=z^-4 Sym^2(TB)`. They preserve these grades. The structured plane object is supplied with the compatible homogeneous symplectic linearization, including its completion coordinate. On `D(X)`, for example, the local normal generator is `h/X`; assigning a weight to `h` does not treat it as a global regular function.

**Theorem, relative to these fixed-model and supplied-map inputs.** There is a noncanonical framed homogeneous formal chart with coordinates `(a,b,c,d,lambda)`. Every corresponding two-jet extends compatibly to all orders. Extensions of the same two-jet are uniquely isomorphic by a homogeneous symplectic gauge equal to the identity through order two. The construction can be made coefficientwise over `Q[a,b,c,d,lambda]` with no parameter division.

The theorem is relative to the plane framing. It neither classifies the quotient by nontrivial automorphisms of the plane object nor constructs an algebraic family of carriers or reflexive hulls.

## 2. Exactly four first-order coordinates and one second-order coordinate

At each step the coupled difference problem is the two-term complex

```
C_k = [ n_k --evaluation at v--> G I^k ],  in degrees 0 and 1.
```

Gauge coboundaries are already quotiented out in cohomology. They must not be subtracted again from a parameter count.

For `k>=1`, `H^0(G I^k)=0`: every `B I^k` filtration line has negative plane degree, and `H^1(A I^k)=0`. The base degrees of `U_k` are `2,-1,3,2`; plane intermediate cohomology vanishes, giving `H^1(U_k)=H^3(U_k)=0`. Also `H^0(W_k)=0`: the only possibly nonnegative plane line is `E0^2`, whose base degree is `-4`. Hence `H^0(n_k)=0`. The hypercohomology exact sequence gives

```
H^1(C_k) = ker[H^1(n_k) -> H^1(G I^k)].
```

There are no extra global section choices or global positive-normal-order framed stabilizers.

The complete prescribed order-one `U` source has dimension 22. Its `D1` map has rank 19, and evaluation on its three-dimensional kernel has rank one. The fixed-pairing kernel therefore has dimension two. Its ordered coordinates are `a nu_X+b nu_Y`.

Here `[X^u Y^v W^w]*` denotes the actual negative Laurent monomial `X^(-u-1)Y^(-v-1)W^(-w-1)`. The nonzero components of `nu_Y` are

```
AP  = 2z[W^5]* + z^2[Y^2 W^3]*,
AE1 = z[Y W^5]* + z^2[Y^3 W^3]* + z^3[Y^5 W]*,
AE0 = 3[Y W]*  (forced by the triangular transport),
AE2 = 0.
```

`nu_X` is obtained by swapping `X,Y`. The complete vectors, origin and ordered finite/infinity/mixed Čech representatives are fixed in `data/first_jet.json`; the program reconstructs them term for term.

The additional `H^1(W_k)` line is `E0^2 = O(-4,2-k)`. For `k=1,2`, all other filtration lines have `H^0=H^1=0`, so this line supplies the full `H^1(W_k)`. The genuine base Laurent band is `z^-1,z^-2,z^-3`. The required character yields exactly

```
order 1: c z^-2 X E0^2 + d z^-2 Y E0^2,
order 2: lambda z^-1 E0^2.
```

`H^1(U_k)=0` makes these classes inject into `H^1(n_k)`. Their contraction with `v=E0` is identically zero. Thus they survive the section constraint. At order two the prescribed `D2` source has dimension 15 and rank 15, so it contributes no further kernel. The first-order affine fiber has dimension four, and the second-order correction torsor above it has dimension one. Fixing the literal first connecting preimage leaves `c,d,lambda`, rather than all five coordinates.

## 3. Exact scalar obstruction and polynomial preimage

`D2_hom` has 16 target rows and 15 source columns, with a one-dimensional cokernel. The first lift varies affinely in `(a,b,c,d)`. The order-two BCH defect uses exactly two brackets; the subsequent relation division, triangular base primitive, Čech homotopy and target-coordinate extraction are rational linear maps. Consequently the entire obstruction vector has total degree at most two.

The replay evaluates the origin, eight signed coordinate points and six pairwise positive sums. These 15 exact rational evaluations determine every coefficient of a four-variable quadratic polynomial. It also checks three off-grid points. This is a coefficient identity justified by the degree bound, not numerical evidence about unspecified higher-degree terms.

The reconstructed 16-vector is

```
(-a/2+b^2-3/4,
 -a^2-3a/2-b/2,
 -a^2-a+b^2+3b/2+5/4,
 a/2+b^2-3/4,
 -a-b/2,
 -a^2-3/4,
 a+b^2-3/4,
 3/4-b/2,
 3a/2-1/4,
 3/4-a,
 -a^2+3a/2+b/2,
 a+2b,
 b,
 3a/2-1/4,
 a/2+3/4,
 0).
```

Its normalized left-cokernel functional is identically zero on this vector. A determinant-one 15-row minor gives the exported polynomial vector `y(a,b,c,d)` satisfying `D2_hom y = obstruction` exactly. The full block, row/column indices, detector and preimage are in `certificates/quadratic_certificate.json`. No inversion of a parameter occurs. The absence of `c,d` in this representative is an output of the calculation, not an assumption.

The section matrix `N2` has shape `114 x 84` and a maximal minor of determinant 16. Thus the full `H^1(G I^2)` is zero, and the second section correction exists. It is unique for fixed middle data because `H^0(G I^2)=0`. Adding `lambda z^-1 E0^2` gives all second-middle classes relative to the selected polynomial second lift.

## 4. Complete higher blocks and uniform section ranks

The complete prescribed `Dk` blocks for `k=3,4,5,6` have respective sizes `9,5,2,1` and determinant 1. The package exports each matrix `Mk` and constant rational inverse `Rk`, checking both `Mk Rk=I` and `Rk Mk=I`. Constant rational coefficients are polynomial coefficients over `Q[a,b,c,d,lambda]`, so these inverses work uniformly in the five parameters.

Completeness matters here. At orders three and four the target basis includes the actual forced lower coordinates. At orders five and six the additional `E0^2` constraints are the complete supplied maps `C5,C6`. Their prescribed raw columns are `[532,540]` and `[664]`. Each is literally zero in the corresponding `C` matrix, belongs to its recomputed free set, and is outside its pivot set. No prescribed kernel vector has a hidden pivot correction of another weight. The code checks every `C` row and every nonzero `D` entry for the grading. These are complete character spaces, not selected obstruction spans.

For `k>=3`, `H^1(W_k)=0`. Together with `H^1(U_k)=H^3(U_k)=0`, the exact sequence identifies `H^1(n_k)` and `H^2(n_k)` with the kernel and cokernel of the complete `Dk` block. Both prescribed components vanish at orders three through six.

The section matrices have

```
N3: 176 x 112, maximal minor determinant -512,
N4: 252 x 144, maximal minor determinant -16384.
```

All row and column indices are exported; the replay computes these determinants over `Q`. Both are units over the polynomial parameter ring, although not units in `Z`. Since `H^1(B I^k)=0`, injectivity of `Nk` proves the full `H^1(G I^k)=0` at orders three and four. The parameter `lambda` is part of the two-jet; its cross terms at order three are included in the next obstruction. They cannot introduce a new obstruction class because the complete prescribed group there is zero.

## 5. The all-order weight bound

For a filtration line `O(b,p)`, a possible `H^2` representative has `b>=0`, `p<=-3` and is a sum of

```
z^e X^(-u-1)Y^(-v-1)W^(-w-1),  0<=e<=b,  u,v,w>=0.
```

Its secondary weight is at most `2b-2`. The `-2` from the actual negative Laurent basis is essential. This is the standard projective-space Čech computation; see [Stacks, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XT).

For a `W` slot `(i,j)`, the base degree is `b_i+b_j-4`. Comparing the weight bound with `k-4+d_i+d_j` gives the necessary inequality

```
k <= 2(b_i+b_j-4)+2-d_i-d_j.
```

The seven lines with nonnegative base degree have cutoffs

```
P^2:0; PE1:3; PE2:1; E0E1:0;
E1^2:6; E1E2:4; E2^2:2.
```

The remaining three lines have base degrees `-1,-4,-1` and no `H^2`. Thus every one of the ten actual filtration lines has zero prescribed `H^2` for `k>=7`. Exactness of taking a character and successive long exact sequences give `H^2(W_k)_hom=0`. This argument preserves off-diagonal gluing and does not require a late `Ck` map to be surjective. Since `H^3(U_k)=0`, it follows that `H^2(n_k)_hom=0`.

The possible `H^2(U_k)` lines `AP,AE1,AE2` have respective cutoffs `3,6,4`; `AE0` has base degree `-1`. Thus `H^2(U_k)_hom=0` for `k>=7`, and `H^1(W_k)=0` gives `H^1(n_k)_hom=0` as well.

Finally, `H^1(G I^k)` injects into `H^2(A I^k)`. The latter has base degree 3 and required coefficient weight `k`; its maximum weight is `2·3-2=4`. Therefore the prescribed section obstruction group is zero for `k>=5`. These inequalities depend only on the fixed model and its linearization, never on `(a,b,c,d,lambda)`.

## 6. Formal existence, regularity, and gauge uniqueness

Suppose a compatible homogeneous structured lift has been constructed through order `k-1`, `k>=3`. Take the unchanged lower logarithms and exponentiate one order further. The resulting degree-`k` cocycle defect is an `n_k`-valued two-cocycle: this follows by linearizing associativity, with the original twisted Čech differential. Its character is prescribed because multiplication adds normal orders and telescopes the frame weights. The vanishing above supplies a homogeneous regular correction. For `k=3,...,6` one uses the constant rational inverses of the complete blocks; beyond six the weight vanishing supplies the primitive.

This is constructive on the original cover. Project to the all-negative plane Laurent terms. A `U` relation defect can be split in the base components with transitions `z^2,z^3,z^2`, then its actual off-diagonal term is subtracted and the `z^-1` component is split. Every Laurent monomial admits this finite/infinity split for these degrees. The remaining plane-exact part is removed by the ordered homotopy that chooses the first plane coordinate with nonnegative exponent. It changes no exponent, hence preserves regularity. For positive Čech degrees it satisfies `delta K+K delta=1-Pi`, with `Pi` the all-negative top-cohomology projection. The elementary support-pattern checks in `check_weights.py` verify its signs.

The symplectic infinitesimal correction exponentiates formally, fixes `alpha` and changes no lower coefficient. Its action respects the relation quotient. The corrected middle transition has a section mismatch in `G I^k`; the cocycle equations make it closed. The full section vanishing at orders two through four, and the prescribed vanishing thereafter, supply its regular correction. In the symplectic presentation this lies in `alpha^perp`, so it preserves `beta(v)=+t0 h`.

Every operation is polynomial with rational coefficients or a fixed rational linear map. Laurent denominators use only original geometric coordinates. Tensoring the rational complexes and their splittings with `Q[a,b,c,d,lambda]` therefore gives compatible coefficients over that entire parameter ring, with no parameter division. At each fixed normal order the coefficient is finite. The transitions have unchanged invertible constant terms and are invertible formally.

For two extensions of the same two-jet, after identification through order `k-1` their degree-`k` middle difference is a prescribed `n_k` one-cocycle. Its class vanishes, so an order-`k` homogeneous symplectic gauge removes it. The section difference is then a global section of `G I^k`, hence zero. The gauges are identity modulo increasing powers of the normal ideal, and their product converges formally. A difference between comparison gauges would have a first nonzero term in `H^0(n_k)=0`. This proves relative uniqueness, including absence of a hidden framed stabilizer.

Compatible finite-order local modules give the usual finite modules over the completed local rings; see [Stacks, Section 30.23 and Lemma 30.23.1](https://stacks.math.columbia.edu/tag/0EHN). This use of completion is not an algebraization claim.

## 7. What remains outside the result

Changing later primitives above a fixed two-jet does not change the framed formal isomorphism class. Changing an early coordinate may do so. Determining how an algebraic carrier's isolated defect varies requires a relative carrier presentation, total-space reflexive hull, central reduction and central hull in the correct order, with any relevant flatness and base-change hypotheses proved. None of those operations is computed here. No family-wide defect value or zero-defect member follows from this formal chart.
