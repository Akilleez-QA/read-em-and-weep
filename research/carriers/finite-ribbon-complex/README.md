# A finite split complex and exact mixed Atiyah certificate

This gives a finite split replacement of the explicitly glued monad in [the ribbon seed construction](../explicit-ribbon-seed.md), together with an exact nonvanishing certificate for its mixed Atiyah class.

For the simplest member `k=0`, the four Euler-image components `u beta_j`, where `beta_j = partial d / partial x_j`, are linearly independent in `H^2(End(F)(-2,-1))`. A `144 x 144` boundary matrix has rank `132`; adjoining the four actual cocycles raises its rank to `136`. The relevant spectral-sequence spot survives to cohomology. This proves the mixed Atiyah class is nonzero. No numerical approximations or computer-algebra assumptions about generic rank are used.

The split model and its comparison maps also apply to the full five-parameter family `D -> D + k(z) (Ja)(Ja)^T`, `deg k <= 4`. The Atiyah and Ext computations in this certificate are specifically for `k=0`.

Requires Python 3 and SymPy. From the directory containing these files, run:

```sh
python model.py
python model.py --all-parameters
python audit_atiyah.py
```

The model checks pass over exact rational polynomial rings; the second retains all five formal parameters. The final command verifies the actual Atiyah cocycles, the surviving spectral-sequence spot, an explicit dual detector, and the optional higher-differential computations. It writes `exact_certificate.json`, a sparse, human-inspectable certificate.

## 1. Terms and conventions

Write `O(p,q)=O_{P1}(p) box O_{P3}(q)`, with coordinates `[s:t]` and `[x0:x1:x2:x3]`. Set `X=(x0,x1)^T`, `Y=(x2,x3)^T`, and on `s!=0` put `z=t/s`.

The following complex is in cohomological degrees `-2,-1,0,1`:

```text
L_G^-2 = O(0,-2)^3
L_G^-1 = O(1,-2)^4 + O(0,-1)^8
L_G^0  = O(1,-1)^10 + O(1,1)^2
L_G^1  = O(2,2).
```

Its only nonzero cohomology sheaf is `H^0(L_G)=G`. Twisting every term by `O(-3,0)` gives:

```text
L_F^-2 = O(-3,-2)^3
L_F^-1 = O(-2,-2)^4 + O(-3,-1)^8
L_F^0  = O(-2,-1)^10 + O(-2,1)^2
L_F^1  = O(-1,2),
```

with `H^0(L_F)=F` and no other cohomology. Its ranks are `3 -> 12 -> 12 -> 1`.

Matrix order in degree zero is the five quotient generators for `(x0,x2)`, the five for `(x1,x3)`, and the two subbundle generators. In degree minus one it is the four generators resolving `A`, followed by four kernel generators for each quotient block.

## 2. Explicit differentials for k=0

Let `M_n(s,t)` be the `n x (n-1)` matrix whose column `j` is

```text
t e_j - s e_(j+1),       0 <= j <= n-2.
```

Let `T_n(Xi,Yi)` be the `n x (n-1)` matrix whose column `j` is

```text
-Yi e_j + Xi e_(j+1).
```

Here `Xi,Yi` denotes one of the pairs `(x0,x2)` or `(x1,x3)`.

Define `M_Q=diag(M_5,M_5)` and the `8 x 3` matrix

```text
H = vertical_stack(T_4(x0,x2), T_4(x1,x3)).
```

The `12 x 4` matrix `alpha_hat` has first ten rows

```text
vertical_stack(T_5(x0,x2), T_5(x1,x3))
```

and last two rows

```text
(0,0,0,-x2^3)
(0,0,0,-x3^3).
```

The `12 x 8` matrix `delta` has top ten rows `M_Q` and bottom two rows

```text
-s (x0^2, x0*x2, x2^2, 0, 0, 0, 0, 0)
-s (0, 0, 0, 0, x1^2, x1*x3, x3^2, 0).
```

Finally, `beta_hat` is the row

```text
(s*x0^3, s*x0^2*x2, s*x0*x2^2, s*x2^3, t*x2^3,
 s*x1^3, s*x1^2*x3, s*x1*x3^2, s*x3^3, t*x3^3,
 t*x0-s*x2, t*x1-s*x3).
```

The differentials are

```text
d^-2 = vertical_stack(M_4, -H)
d^-1 = horizontal_stack(alpha_hat, delta)
d^0  = beta_hat.
```

The exact polynomial identities are

```text
alpha_hat M_4 = delta H,
beta_hat alpha_hat = 0,
beta_hat delta = 0.
```

Every entry has precisely the bidegree dictated by its source and target line bundles.

## 3. Derivation and a global quasi-isomorphism

There are standard evaluation resolutions

```text
0 -> O(0,-1)^4 -> O(1,-1)^5 -> O(5,-1) -> 0,
0 -> O(0,-2)^3 -> O(1,-2)^4 -> O(4,-2) -> 0.
```

Their right maps are respectively the rows

```text
(s^4,s^3*t,s^2*t^2,s*t^3,t^4),
(s^3,s^2*t,s*t^2,t^3).
```

Pulling `B` back along two copies of the first evaluation map produces an extension of `O(1,-1)^10` by `O(1,1)^2`. It splits because `H^1(O(0,2))=0`. The explicit chosen splitting gives

```text
0 -> K=O(0,-1)^8 --delta--> E=O(1,-1)^10+O(1,1)^2 -> B -> 0.
```

For one block `(Xi,Yi)`, the local map `E -> B` on `s!=0` is

```text
q_i = p_i0 + z*p_i1 + z^2*p_i2 + z^3*p_i3 + z^4*p_i4,
h_i = b_i + R_i p_i,
R_i = (0, -Xi^2, -z*Xi^2-Xi*Yi,
       -z^2*Xi^2-z*Xi*Yi-Yi^2,
       -z^3*Xi^2-z^2*Xi*Yi-z*Yi^2).
```

On `t!=0`, with `w=s/t`, its lower block is

```text
R_i,t = (w*Xi^2+w^2*Xi*Yi+w^3*Yi^2,
         w*Xi*Yi+w^2*Yi^2,
         w*Yi^2, 0, 0),
```

and the quotient evaluation row is `(w^4,w^3,w^2,w,1)`.

Call these maps `phi_s,phi_t`. They satisfy

```text
phi_s diag(z*I_10,z*I_2) = T_B phi_t.
```

The chain comparison `q:L_G -> [A -> B -> C]` is:

- degree `-2`: the zero map to zero;
- degree `-1`: the `A` evaluation row on the first four terms, zero on `K`;
- degree `0`: `phi`;
- degree `1`: the identity of `C`.

All chain identities and gluing identities are checked in the script. Its kernel identifies globally with

```text
K_A -> K_A + K -> K,
a |-> (a,-Ha),       (a,k) |-> Ha+k,
```

where `K_A=O(0,-2)^3`. This kernel is contractible: the maps back are `(a,k) -> a` and `k -> (0,k)`. Thus `q` is a global quasi-isomorphism. This proves exactness and identifies the actual cohomology bundle, rather than merely its K-class.

A global strict chain-homotopy inverse is not asserted. The standard line-bundle evaluation sequences do not split globally. Explicit local strict inverses and homotopies are given next.

## 4. Polynomial strong deformation retracts on both base charts

`local_model(data, 's')` and `local_model(data, 't')` return matrices `q`, `i`, and `H` satisfying

```text
q i = identity,
identity - i q = d H + H d,
H^2 = 0, q H = 0, H i = 0.
```

Every matrix entry is polynomial in the relevant base chart coordinate and in the homogeneous `P3` variables, with the indicated line-bundle degrees. No denominators in a `P3` coordinate are introduced.

Here is a reproducible matrix recipe. On the `s` chart choose the first basis vector `r_A=e_0` and `r_Q=e_0` as sections of the evaluations. On the `t` chart choose `r_A=e_3`, `r_Q=e_4`. Let `R_Q=diag(r_Q,r_Q)` and let `V_Q` be the two-block quotient evaluation. The degree-zero section of `phi` is

```text
sigma_0(q,h) = (R_Q q, h - R R_Q q).
```

Let `K_n` denote a polynomial left inverse to `M_n` on its kernel image. Explicitly:

```text
s chart: (K_n y)_j = -sum_(r=j+1)^(n-1) z^(r-j-1) y_r,
t chart: (K_n y)_j =  sum_(r=0)^j w^(j-r) y_r.
```

Let `K_Q=diag(K_5,K_5)`, `K_A=K_4`, and let `T` be the first ten rows of `alpha_hat`. Set

```text
kappa = K_Q(T r_A - R_Q a),
i^-1  = (r_A,-kappa),
i^0   = sigma_0,
i^1   = identity.
```

The homotopy matrices are

```text
H^-1(p,k) = K_A(p-r_A V_A p),
H^0(p,b)  = (0,K_Q(p-R_Q V_Q p)),
H^1       = 0.
```

For the untwisted model the local original monad has `a_s=zX-Y`, `h_s=-X^3` and `a_t=X-wY`, `h_t=-Y^3`. Twisting by `O(-3,0)` changes the transition matrices but none of these local differential identities.

## 5. Full five-parameter family

Keep `alpha_hat`, `H`, and `M_Q` unchanged. Put

```text
j(z)=J(zX-Y),
D(z)=D_0(z)+D_k(z),
D_k(z)=k(z)j(z)j(z)^T,
k(z)=k0+k1*z+k2*z^2+k3*z^3+k4*z^4.
```

Write `D_m` and `Dk_m` for the coefficient matrices of `z^m`; missing coefficients are zero.

For quotient block index `b=0,1` and kernel index `j=0,1,2,3`, replace the bottom two entries of column `4b+j` of `delta` by

```text
s * (D_(4-j))[:,b].
```

For quotient block index `b=0,1` and generator index `j=0,...,4`, replace entry `5b+j` of `beta_hat` by

```text
(beta_hat at k=0)_(5b+j) - s * (Y^T Dk_(5-j))_b.
```

The last two entries of `beta_hat` remain `(tX-sY)^T`. The explicit local maps `phi` use

```text
R_s,j = nonnegative_z_part(D(z) z^(j-5)),
R_t,j = R_s,j - D(z) z^(j-5),   substituted z=1/w.
```

The family identity `D_k(z)(zX-Y)=0` proves that `alpha_hat` stays unchanged. Its symmetry also proves the corresponding left-annihilation identity used in `beta_hat`. All comparison, exactness, and strong deformation retract checks pass with the parameters formal.

## 6. API for the split model

```python
import model as m
data = m.build()  # k=0
# Or: data=m.build(sum(m.ks[i]*m.z**i for i in range(5)))
d = data['d']            # degrees -2,-1,0; exact differential matrices
terms = data['terms_F']   # source/target bidegrees for F
chart = m.local_model(data, 's')
```

`d` and the split terms remove the need to represent the nonsplit `B` in a derived Hom complex. The matrices `q,i,H` compare representatives in this split model exactly with representatives in the original monad. The calculation below uses the actual derived Hom differential and cocycles, not only their Chern characters.


## 7. Actual Atiyah cocycles and their nonvanishing certificate

Let `C^p = direct_sum_i Hom(L_F^i,L_F^(i+p))(-2,-1)`, with differential

```text
partial(f) = d f - (-1)^p f d.
```

The Euler sequence of `P3` is

```text
0 -> Omega^1_P3 -> O_P3(-1)^4 -> O_P3 -> 0.
```

The four components of the Euler image of the relative Atiyah class are represented in the split model by

```text
beta_j = partial d / partial x_j,         j=0,1,2,3.
```

These are genuine degree-one Hom cocycles: differentiation of `d^2=0` gives `d beta_j + beta_j d=0`. Their multiplication by the generator `u` of `H^1(O_P1(-2))` has the literal Cech representative

```text
Z_j = beta_j / (s t).
```

On the `P3` coordinate cover this is the same polynomial representative on every single chart. `audit_atiyah.py` checks separately that every `Z_j` has zero Cech differential and zero Hom differential.

The hypercohomology spectral sequence has

```text
E1^(p,q) = H^q(C^p).
```

The only nonzero rows for `End(F)(-2,-1)` are:

```text
q=4: p=-3,-2,-1       dimensions 36 -> 68 -> 28, ranks 36,28
q=1: p= 0, 1         dimensions144 ->144,       rank132
q=0: p= 2, 3         dimensions 80 -> 60,       rank 60.
```

These entries follow directly from `H^0(O_P1(a))`, `H^1(O_P1(a))`, `H^0(O_P3(b))`, and `H^3(O_P3(b))`. `cohomology_groups.py` prints their individual line-bundle summands. `spectral_d1.py` represents the top cohomology by homogeneous Laurent monomials all of whose coordinate exponents are negative; polynomial multiplication followed by projection gives the exact induced maps.

Let `A` be the `144 x 144` map in the `q=1` row. Let `B` be the `144 x 4` matrix obtained by projecting the four literal `Z_j` to that row. Its columns retain exactly the monomials with negative `s` and `t` exponents. The exact identities and ranks are

```text
rank(A) = 132,
rank([A,B_j]) = 133                 for every j,
rank([A,B]) = 136.
```

The certificate includes a sparse rational `4 x 144` matrix `W` with just 38 nonzero entries, satisfying

```text
W A = 0,
W B = I_4.
```

These matrix identities independently certify that the four classes are linearly independent modulo boundaries, without relying solely on a black-box rank report. The precise basis ordering, all entries of `A,B,W`, and the two `q=4` maps are saved in `exact_certificate.json`.

### Why the E2 classes survive

After the displayed `d1` maps, the only nonzero `E2` spots are

```text
E2^(-2,4) = Q^4,
E2^( 0,1) = Q^12,
E2^( 1,1) = Q^12,
E2^( 2,0) = Q^20.
```

In particular, the tempting possible incoming map

```text
d4: E4^(-3,4) -> E4^(1,1)
```

has zero source, because the `36 -> 68` map has full column rank already on `E1`. All other incoming and outgoing higher differentials at `(1,1)` also have zero source or target. Hence

```text
E2^(1,1) = E_infinity^(1,1),
```

and the four independent classes represent four independent actual elements of `H^2(End(F)(-2,-1))`.

### Consequence for the mixed Atiyah class

Write `A1(F)` and `A3(F)` for the two components of the Atiyah class and set

```text
Delta = A1(F) cup v - u cup A3(F).
```

Apply the Euler inclusion on the `Omega^1_P3` factor. The first summand maps to zero: the scalar hyperplane class `v` maps to zero under the Euler sequence. The second maps, up to the common sign convention for the Atiyah class, to the four classes `-u beta_j`. The certificate proves that this vector is nonzero. Therefore `Delta` is nonzero.

## 8. Optional complete Ext and higher-differential audit

The nonvanishing proof above does not require the remaining higher differentials. They are computed separately to ensure that intermediate pages are not mistaken for actual cohomology.

`cech_transfer.py` gives a monomial-by-monomial contraction of the coordinate Cech complex of `P1 x P3`. For a monomial whose negative-coordinate support is a proper subset, choose the first vertex outside that support and use the usual simplex contraction. The product contraction has the graded tensor-product sign. Its identities are checked on 640 monomial/subset basis vectors, exhaustively covering every possible negative support and compatible Cech subset.

For the total differential `delta_Cech + (-1)^q partial_Hom`, the transferred higher maps are evaluated by exact zigzags. Every intermediate lift is checked to solve its Cech-boundary equation; no missing intermediate cohomology component is assumed away.

For `End(F)(-2,-1)`, the only remaining possible differential is

```text
d2: E2^(0,1) = Q^12 -> E2^(2,0) = Q^20.
```

The exact transfer gives rank `12`. Consequently

```text
h^2(End(F)(-2,-1)) = 4 + 12 + (20-12) = 24,
h^i(End(F)(-2,-1)) = 0              for i != 2.
```

For the untwisted `End(F)`, the nonzero `E1` terms are

```text
q=4: p=-3            dimension 3,
q=0: p=0,1,2,3       dimensions394 ->1336 ->1240 ->315,
                     exact ranks393,922,315.
```

Thus its only possible higher differential is

```text
d5: E5^(-3,4) = Q^3 -> E5^(2,0) = Q^3.
```

The exact five-step Cech transfer has rank `3` after quotienting by the image of the `q=0` `d1`. This gives

```text
h^0(End(F)) = 1,
h^1(End(F)) = 21,
h^i(End(F)) = 0                    for i >= 2.
```

The raw `d2` and `d5` columns are also included in the JSON certificate. These cohomology dimensions concern the displayed `k=0` member only.

## 9. Contents of the reproducible bundle

- `model.py`: split complex, full formal family, global comparison, chart deformation retracts.
- `cohomology_groups.py`: line-bundle cohomology inventories and `E1` tables.
- `spectral_d1.py`: exact induced Hom differential on line-bundle cohomology.
- `cech_transfer.py`: explicit Cech contraction and checked higher-differential zigzags.
- `audit_atiyah.py`: one-command complete audit, actual cocycles, ranks, and dual certificate.
- `exact_certificate.json`: generated sparse rational matrices and basis labels.

No external account, network access, or proprietary computer-algebra system is required.
