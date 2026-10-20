# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: the degree-minus-one socle detector

## Verdict

The proposed exact sequence is correct under the stated vanishing hypotheses. A nonzero socle class can have zero `d₂` image and survive to a nonzero `d₃` image. Consequently, checking only the map from the socle to the `H¹`-row does not detect every socle class.

With the notation below, the exact sequence is

\[
0\longrightarrow
\operatorname{coker}(d_2:L_1\to N_3)
\xrightarrow{\ (d_3|_{\ker(d_2|_S)})^{-1}\ }
S\xrightarrow{d_2}
\ker(d_2:L_2\to N_4)
\longrightarrow0.
\]

The displayed left arrow includes the inverse image into `S`. No splitting is asserted. The `d₂` and `d₃` maps are genuine spectral-sequence differentials, not just the multiplication maps on the individual cohomology groups.

This audit independently derives the result from the setup, reads the two supplied background artifacts, and checks the companion `PROOF.md`, including its constructive inverses. It does not evaluate an HM multiplication matrix, a source class, a differential rank, or an obstruction rank.

## 1. Exact complex and all first-page vanishings

Let `V=C⁵`, choose the ordered coordinate basis, and set

\[
K^p=\Lambda^p V\otimes B(p-1),\qquad
\delta(\eta)=\sum_{i=0}^4e_i\wedge\eta\,x_i,
\qquad 0\le p\le5.
\]

At every point at least one coordinate is a unit in a local trivialization. Contraction with the corresponding dual vector, divided by that coordinate, contracts the wedge Koszul complex. Thus `K` is an exact complex of sheaves. Its hypercohomology is zero in every degree.

The column-first spectral sequence has

\[
E_1^{p,q}=\Lambda^p V\otimes H^q(B(p-1)),\qquad
d_r:E_r^{p,q}\longrightarrow E_r^{p+r,q-r+1}.
\]

It is bounded and therefore converges to the zero hypercohomology without any convergence qualification. In particular, every `E∞` term is zero; different filtration pieces cannot cancel each other to avoid this conclusion.

Selfduality and Serre duality on `P⁴` give, for `t=p-1`,

\[
H^3(B(t))\simeq H^1(B(-t-5))^*,\qquad
H^4(B(t))\simeq H^0(B(-t-5))^*.
\]

Here `-t-5=-p-4≤-4`. Hence the assumed `H¹` and `H⁰` vanishings kill both rows for every `0≤p≤5`. The assumptions also give

- `E₁^{p,0}=0` for `p=0,1`;
- `E₁^{p,2}=0` for `p≥3`, since `p-1≥2`;
- no terms outside `0≤p≤5`, `0≤q≤2`.

The only potentially nonzero rows are therefore

\[
\begin{array}{c|cccccc}
q=2&H^2B(-1)&5H^2B(0)&10H^2B(1)&0&0&0\\
q=1&H^1B(-1)&5H^1B(0)&10H^1B(1)&10H^1B(2)&5H^1B(3)&H^1B(4)\\
q=0&0&0&10H^0B(1)&10H^0B(2)&5H^0B(3)&H^0B(4)\\\hline
&p=0&p=1&p=2&p=3&p=4&p=5.
\end{array}
\]

All horizontal arrows on this page are coordinate Koszul multiplication, with row-dependent signs under the totalization convention in Section 5. These signs do not change row kernels or images. The positive-twist vanishing `H¹B(t)=0` for `t≥7` is unnecessary for this argument.

## 2. Exhaustive differential audit

Write `Tᵢ=E₂^{i,2}` for `i=0,1,2`, `Lₚ=E₂^{p,1}`, and `Nₚ=E₂^{p,0}`. Then

\[
T_0=S=\ker\bigl(H^2B(-1)\to V\otimes H^2B(0)\bigr)
=\operatorname{Soc}(H^2B(*))_{-1}.
\]

There is no incoming `d₁` at column zero. The possible `d₂` arrows are exactly

\[
\begin{aligned}
T_0&\to L_2,&T_1&\to L_3,&T_2&\to L_4,\\
L_0&\to N_2,&L_1&\to N_3,&L_2&\to N_4,&L_3&\to N_5.
\end{aligned}
\]

There are no incoming `d₂` arrows into the `T` terms, because row three is zero. All other `d₂` arrows have a zero source or target.

The only possible `d₃` arrows are

\[
\begin{aligned}
\ker(T_0\to L_2)&\longrightarrow N_3/\operatorname{im}(L_1\to N_3),\\
\ker(T_1\to L_3)&\longrightarrow N_4/\operatorname{im}(L_2\to N_4),\\
\ker(T_2\to L_4)&\longrightarrow N_5/\operatorname{im}(L_3\to N_5).
\end{aligned}
\]

The kernels and quotients are the `E₃` terms, not unmodified `E₂` terms. There are no `dᵣ` arrows for `r≥4`: their source or target row lies outside rows zero through two. Thus `E₄=E∞=0`.

Every one of the three displayed `d₃` arrows is an isomorphism. Each source has no other incoming or outgoing arrow after reaching page three, and the same is true of each target apart from that displayed arrow.

For completeness, disappearance of the middle row gives

\[
\begin{aligned}
&d_2:L_0\to N_2\text{ is an isomorphism},\\
&d_2:L_1\to N_3\text{ is injective},\\
&\operatorname{im}(T_0\to L_2)=\ker(L_2\to N_4),\\
&\operatorname{im}(T_1\to L_3)=\ker(L_3\to N_5),\\
&T_2\to L_4\text{ is surjective},\qquad L_5=0.
\end{aligned}
\]

The first isomorphism uses both the middle-row vanishing and the fact that `N₂` has no `d₃` incoming arrow. These additional identities are formal consequences, not independent rank computations.

In particular, the possible arrows from `T₁` to `N₄` and from `T₂` to `N₅` have not been forgotten. They do not interfere with the stated exact sequence. They show why one should not presume `L₂→N₄` or `L₃→N₅` to be surjective.

## 3. Exact-sequence derivation

Set `a=d₂:S→L₂`, `b=d₂:L₂→N₄`, and `c=d₂:L₁→N₃`. Because `d₂²=0`, `im(a)⊂ker(b)`. More precisely,

\[
E_3^{2,1}=\ker(b)/\operatorname{im}(a).
\]

No higher differential can meet `(2,1)`: the possible incoming `d₃` source has column `-1`, and any outgoing `d₃` has negative second index. Consequently this `E₃` term is already `E∞`, hence zero. This proves `im(a)=ker(b)`.

At `(0,2)` and `(3,0)`,

\[
E_3^{0,2}=\ker(a),\qquad E_3^{3,0}=\operatorname{coker}(c).
\]

Their only remaining differential is `d₃:E₃^{0,2}→E₃^{3,0}`. Both must die, so `d₃` is an isomorphism. Taking its inverse and then the inclusion of `ker(a)` into `S` proves the sequence in the verdict.

An equivalent vanishing criterion is

\[
S=0\quad\Longleftrightarrow\quad
\bigl(d_2:L_1\to N_3\text{ is surjective}\bigr)
\text{ and }
\bigl(d_2:L_2\to N_4\text{ is injective}\bigr).
\]

The first map is already formally injective. Neither condition follows merely from the dimensions of its source and target.

## 4. Finite twists and what the detector actually needs

Using the ordered exterior powers, the four terms are explicitly

\[
L_1=
\frac{\ker(5H^1B(0)\to10H^1B(1))}
{\operatorname{im}(H^1B(-1)\to5H^1B(0))},
\]

\[
L_2=
\frac{\ker(10H^1B(1)\to10H^1B(2))}
{\operatorname{im}(5H^1B(0)\to10H^1B(1))},
\]

\[
N_3=
\frac{\ker(10H^0B(2)\to5H^0B(3))}
{\operatorname{im}(10H^0B(1)\to10H^0B(2))},
\]

\[
N_4=
\frac{\ker(5H^0B(3)\to H^0B(4))}
{\operatorname{im}(10H^0B(2)\to5H^0B(3))}.
\]

The formal presentation of `L₁` contains `H¹B(-1)`, but calculating its denominator is unnecessary for calculating the image of `L₁→N₃`: the cochain differential can be applied to the entire numerator, and it annihilates that denominator. Consequently the outer-term vanishing criterion requires only the positive section twists `1,2,3,4`, the `H¹` twists `0,1,2`, their coordinate maps, and the two secondary differentials. The companion proof's stronger omission of the negative `H¹` input is valid. The degree-zero `H¹` contribution is still required; a strictly-positive-twist criterion is not established. The full first page uses only twists `-1` through `4`. There is no infinite positive-twist tail hidden in this statement.

Knowing these vector spaces and their `d₁` maps gives the `E₂` terms, but does not in general determine `d₂`. Cochain lifts or equivalent derived data are needed. In particular, a claim to have computed the detector solely from cohomology dimensions would be stronger than what is proved here.

## 5. Explicit Čech construction and signs

Use the standard affine cover `Uᵢ=D₊(xᵢ)` and its ordered Čech complex. Every finite intersection is affine, so Čech cohomology computes the coherent-sheaf cohomology in question. Write

\[
C^{p,q}=\check C^q(\{U_i\},K^p),\qquad
\partial:C^{p,q}\to C^{p,q+1}.
\]

The maps `δ` and `∂` commute. Fix the total differential

\[
D=\partial+(-1)^q\delta\quad\text{on }C^{p,q}.
\]

Then `D²=0`, and the first-page horizontal differential is `(-1)^qδ` under the usual identification with sheaf cohomology. Its row cohomology is the same quotient of kernels by images as that of `δ`. This is the convention used in the companion proof.

### The first socle differential

For `s∈S`, choose a representative `a∈C^{0,2}` with `∂a=0`. The socle condition says that `δa` is a Čech boundary. Choose

\[
u\in C^{1,1},\qquad \partial u=\delta a.
\]

Since `D(a-u)=δu`, the class `d₂(s)` is represented by `δu∈C^{2,1}`. It is Čech closed and a Koszul cocycle. Replacing `u` by another solution changes it by a Čech cocycle, so `δu` changes by a `d₁` boundary. Replacing `a` by `a+∂r` permits replacement of `u` by `u+δr` and leaves `δu` unchanged.

### The remaining socle differential

Suppose `d₂(s)=0` in `L₂`. This means that, after subtracting a Čech-closed element of `C^{1,1}` from `u`, one can arrange that `δu` is a Čech boundary. Make that adjustment and choose

\[
v\in C^{2,0},\qquad \partial v=\delta u.
\]

Then

\[
D(a-u-v)=-\delta v.
\]

The `0`-cochain `-δv∈C^{3,0}` is Čech closed, hence is a global section, and it is a Koszul cocycle. Its class in

\[
N_3/\operatorname{im}(d_2:L_1\to N_3)
\]

is `d₃(s)` with this convention.

There are two essential choice checks:

1. Changing `v` by a global section of `K²` changes `-δv` by a `d₁` boundary, which vanishes in `N₃`.
2. Changing the adjusted `u` by a Čech cocycle `z∈C^{1,1}` whose `δ` image is Čech-exact changes the answer by `-d₂([z])`, where `[z]∈L₁`. Indeed, `v'-v` has Čech boundary `δz`, so `d₂([z])` is represented by `δ(v'-v)` and the change in `d₃` is its negative. Thus the ambiguity is precisely the image of `d₂:L₁→N₃`.

This is why the target must be the quotient by `im(d₂:L₁→N₃)`. Omitting this quotient generally makes the alleged `d₃` value depend on choices.

More generally, for a source cocycle `z∈C^{p,1}` representing an `E₂` class, choose `b∈C^{p+1,0}` with

\[
\partial b=\delta z.
\]

Then `D(z+b)=δb`, so `d₂([z])` is represented by `δb`. This applies in particular to both maps `L₁→N₃` and `L₂→N₄` in the exact sequence. If `z` is replaced by `z+δw` for a Čech cocycle `w`, its image does not change, proving the denominator omission in Section 4 directly.

Other standard totalization conventions can change the displayed signs. They produce isomorphic spectral sequences and the same kernel, image, quotient, and vanishing conclusions. A signed chain-level formula must state its convention; an unsigned assertion of the exact sequence is unaffected.

## 6. Formal example: all socle classes can hide from `d₂`

The following finite double complex is an abstract example, not an HM cohomology calculation and not a claim of geometric realization by this bundle. It demonstrates that the page shape and total acyclicity alone do not remove the `d₃` contribution.

Over a field, take one-dimensional spaces at the following bidegrees and zero elsewhere:

\[
a:(0,2),\quad u:(1,2),\quad
b:(1,1),\quad v:(2,1),\quad
c:(2,0),\quad w:(3,0).
\]

Set the nonzero horizontal and vertical maps to

\[
\delta a=u,\quad\delta b=v,\quad\delta c=w,
\qquad
\partial b=u,\quad\partial c=v.
\]

All other maps are zero. The two differentials commute, and every horizontal row is exact. Thus this example has both row exactness and zero total cohomology, as in the Koszul–Čech situation.

On taking vertical cohomology, the pairs `b→u` and `c→v` cancel. The only `E₁`, hence `E₂`, terms left are

\[
S=E_2^{0,2}=\mathbf k[a],\qquad
N_3=E_2^{3,0}=\mathbf k[w].
\]

In particular `L₁=L₂=N₄=0`. The map `S→L₂` is zero, while

\[
d_3([a])=-[w]
\]

is an isomorphism. Directly, with the convention of Section 5,

\[
Da=u,\qquad Db=u-v,\qquad Dc=w+v,
\qquad D(a-b-c)=-w.
\]

The total differential from the span of `a,b,c` to the span of `u,v,w` is invertible, so total acyclicity can also be checked immediately.

This supplies the requested explicit failure mode: zero `d₂` value is not a certificate that a socle class is zero. The residual class is completely detected by `d₃` only after taking its correct quotient target.

## 7. Check of the constructive inverses in the companion proof

Both constructions in its Section 5D are valid with the stated total differential.

For a global Koszul-degree-three cycle `c`, any total primitive `y+a+b` has components of bidegree `(0,2),(1,1),(2,0)`. The equation `D(y+a+b)=c` is precisely

\[
\partial y=0,\quad \delta y+\partial a=0,
\quad-\delta a+\partial b=0,\quad\delta b=c.
\]

The socle transgression therefore uses primitives `-a,-b` and gives `d₃([y])=[c]`. Two total primitives differ by a total cycle, which is a total boundary by acyclicity. Its column-zero component is a Čech boundary, so `[y]` is well-defined. A horizontal boundary in `c` has a primitive supported in column two; an `h`-image has a primitive `z+u` supported in columns one and two. Neither changes `[y]`. This proves directly that the construction factors through `Q`.

For surjectivity onto `Z`, the companion proof begins with a row-two `H¹` representative `z` and `u` satisfying `∂u=δz`. Zero `g` value means `δu` is a global horizontal boundary, so subtracting a suitable global section from `u` makes `z+u` a total cycle. A total primitive has component equation `-δa+∂b=z`, and the first socle primitive `-a` yields `f([y])=[z]`. Thus the construction indeed realizes a lift. It makes no unjustified claim that the lift is canonical.

## 8. Compatibility with the pairing reduction

The supplied pairing proof identifies the cubic/linear defect as

\[
c-e=\dim\bigl(t_3K\cap S\bigr).
\]

The present sequence determines the formal two-stage detector structure of `S`. It does not evaluate that intersection. Even a proof that `S≠0` would not alone show that `t₃K` meets it nontrivially. Conversely, proving `S=0` by both outer-term conditions would force this particular defect to vanish while leaving the independent quadratic-image defect unresolved.

## Sources and audit scope

- Read `../sharper-hm-regularity/SHARPEST-BOUND.md`, particularly the verified bound `H²B(t)=0` for `t≥2`.
- Read `prerequisite primary-pairing-constraints, document PROOF.md (see the unit INPUTS.md)`, particularly the socle identification in Section 4.
- Independently derived the theorem from the supplied setup, then read and checked the companion `PROOF.md`, including its sign convention, finite-input improvement, formal example, and Section 5D constructions.
- No external writes, actual HM matrices, large computations, rank evaluations, or selected source instances were used.
