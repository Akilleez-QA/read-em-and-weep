# The actual harmonic nilpotent has a nonzero second-normal residue

## Scope and conclusion

This is a local obstruction to extending the **fixed, already normalized** first-normal nilpotent. It is not a fourth Bockstein, a construction of a global second-normal midpoint, or a computation of the full next connection error.

Use the actual marked regular X-chart frame and the harmonic equation `q=u0 u2-u1²`, with positive cone coordinates `(u0,u1,u2)=(X²,XY,Y²)` and a separate negative base coordinate `z`. Write

`Ncorr=L(n)+q L(T)`.

The previously checked first-order equation is `Ncorr²=0 mod q²`. Its scalar coefficient at `q²`, of lowest weighted degree eight, has a **nonzero** class in

`K[X,Y]/(f,g_x)²`, where `K=C(A,B,c,lambda,z)`.

All parameters are unassigned, and `A B c lambda != 0`. The calculation is an exact universal polynomial identity. In particular, no regular second-normal correction can make this fixed lift square-zero modulo `q³` across the common-zero locus at the generic vertex point, on the indicated base chart. This does not assert failure after inverting `f` or `g_x`: off that locus the ideal is the unit ideal and this obstruction vanishes. Higher-weight actual conic and endpoint-frame terms cannot change this conclusion. Nothing here excludes changing the specified first-normal nilpotent itself.

## 1. Fixed data and harmonic normalization

The sources are `ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md`, `ACTUAL-LOWEST-NORMAL-CONNECTION-HAS-AN-EXPLICIT-NEXT-ERROR-TERM.md`, and their verifiers. Put

```
f = A X²Y + B Y³z + Ac X³z² - Bc XY²z³,
g = -lambda (B XY⁴/z³ + A X³Y²/z⁴)/(2Ac),
p = lambda XY/(2Ac z⁴) - lambda X²/(2A z²) + lambda B Y²/(A²z),
g_x = g + p f,
P = [[1,0],[p,1]],
n_d = [[fg,-f²],[g²,-fg]],
n = P n_d P^-1 = [[f g_x,-f²],[g_x²,-f g_x]].
```

The weighted degree of a matrix is its diagonal cover degree. Thus `n` has weight eight, and its entries have cover degrees `(8,6;10,8)`.

For positive binary degrees `d,h`, use the unnormalized even transvectants

```
B1(F,G) = (F,G)_2/[2(d-1)(h-1)(d+h-1)],
B2(F,G) = (F,G)_4/[8(d-1)(d-3)(h-1)(h-3)(d+h-3)(d+h-5)].
```

The respective expressions are zero if either degree is less than two or four. The matrix versions use ordered matrix multiplication with these scalar bilinear products. The complete harmonic identity is

`L(F)L(G)=L(FG)+q L(B1(F,G))+q² L(B2(F,G)) mod q³`.

Its all-degree normalization and complete abstract-basis checks are in `verify_second_normal_harmonic_product_and_defect.py`.

Let `v=lambda X/(8cz⁴)`. The fixed divisor-frame correction is

```
(T_d)11 = (f,g)_2/112 + v f,
(T_d)12 = -(f,f)_2/40,
(T_d)21 = (g,g)_2/288 + 2v g,
(T_d)22 = -(T_d)11.
```

The actual regular-chart correction is **not** naive substitution of `g_x` into that formula. It is

`T=P T_d P^-1+B1(P,n_d)P^-1+B1(P n_d,P^-1)`.

This retains the complete first harmonic frame transport. Its entries are regular, have cover degrees `(4,2;6,4)`, and are trace-free. The verifier checks the exact square-zero equation

`nT+Tn+B1(n,n)=0`.

If the physical equation is `q0=nu q`, the same actual matrix is `L(n)+q0 L(T/nu)` and the residue below is multiplied by `nu^-2`. This fixed nonzero normal-line factor must not be dropped when comparing normalizations.

## 2. The complete scalar octic

The coefficient is

`E2=T²+B1(n,T)+B1(T,n)+B2(n,n)=chi I`.

Both ordered mixed products are essential. Scalarity follows from the rank-two trace-free square identity and is also checked exactly. The unreduced `chi` is polynomial in `X,Y,z` in the actual regular frame. Its cover degree is eight.

Here is a compact exact description, retaining the full scalar rather than only its residue:

`chi = Q f² + a f g_x + R`,

where

```
a = 2B lambda(3A+Bc²z⁵)/(3Az),
Q = -B lambda²/(140A³c²z⁷) *
    (-105A²X²c²z⁴ +70A²XYcz² -35A²Y²
     -172ABX²c⁴z⁹ +60ABXYc³z⁷ +245ABY²c²z⁵
     +64B²Y²c⁴z¹⁰),
R = -B lambda² Y⁴/(4Ac²z⁷) *
    (A²X⁴ -3ABX⁴c²z⁵ -4ABX³Ycz³ +2ABX²Y²z
     +2B²X²Y²c²z⁶ -4B²XY³cz⁴ +B²Y⁴z²).
```

Although this division formula uses Laurent functions of `z`, its left side is regular. We only need the nonempty vertex chart `z != 0`, and may work over its function field to disprove regular ideal membership.

## 3. Why this is a nonzero obstruction, not merely a nonzero polynomial

At cover degree eight, the square ideal has exactly the generators

`(f,g_x)²_8 = f² Sym²<X,Y> + K f g_x`.

The term `g_x²` starts at degree ten. Divide homogeneous octics first by `f²`, whose leading term is `A²c²z⁴X⁶`, in lexicographic order `X>Y`. The remainder of `f g_x` then has leading term

`[A lambda/(2cz⁴)] X⁵Y³`.

Both coefficients are nonzero in `K`. Subtracting its unique multiple leaves an X-degree-at-most-four remainder. This elimination is unique: a nonzero homogeneous quadratic multiple of `f²` has an X-degree-six-or-higher leading term, while the residual `f g_x` pivot has X-degree five. Thus `R` is the unique normal remainder in degree eight, not an arbitrary representative.

Its `Y⁸` coefficient is

`-B³ lambda²/(4Ac²z⁵) != 0`.

Therefore `[chi]=[R] != 0` in the actual square-ideal quotient. This proof uses no coefficient specialization or rank computation.

For a hypothetical trace-free second correction `S=[[a2,b2],[c2,-a2]]`,

`{n,S}=tr(nS) I`,

`tr(nS)=2f g_x a2+g_x² b2-f² c2`.

At the weight relevant to this octic, `S` has weight zero: `a2,c2` have positive cover degrees zero and two, whereas `b2` would have degree minus two and therefore vanishes for a regular correction. The possible change is exactly the ideal component just eliminated. Allowing a traceful correction does not help: its scalar half-trace contribution is still `tr(nS)`, in the same ideal. Hence no regular second correction can kill this residue.

## 4. Why the leading residue belongs to the actual extension

This uses the established actual filtered comparison, not an identification of the full actual bundle with a homogeneous model.

The fixed marked regular triangular frame and its complete harmonic `T` were used in Sections 1–3. Exact finite conic transport has ordinary leading frame change `I-s n`, of weight eight. It changes `n` only above weight eight and the first correction only above weight four. Its finite terms must be retained in the full lift, but cannot enter the scalar weight-eight coefficient: the three contributing weights are `4+4`, `8+4-4`, and `8+8-8`.

Similarly, the actual endpoint transition differs by `q eta`, with `eta` of weight zero. Its failed nilpotent gluing contributes `[eta,n]` of weight eight to `T`, hence only weight twelve or higher to this square coefficient. This does **not** assert that the first-normal nilpotent glues at the endpoint.

A regular additional first-normal frame `I+qB` has minimum weight minus two. Its change `[B,n]` has weight at least six, so any resulting change of the scalar coefficient starts above weight eight. Ordinary marked frame changes transport the full square by conjugation; omitting the induced second correction changes its scalar coefficient only by `tr(nS)`, precisely the ideal already quotiented out. Consequently the computed nonzero class is the actual leading local residue, independent of those uncomputed higher terms.

## 5. Global scalar residue of the midpoint pair

There is a general gluing statement that does not require extending the midpoint bundle to the third neighborhood. Start with its actual bundle and twisted nilpotent on the **second** neighborhood. The midpoint matching source supplies this genuine first-normal pair; the corresponding assertion is not available at the endpoint.

Choose trace-free local matrix lifts and arbitrary local transition lifts to the third neighborhood. Trace-free lifts always exist in characteristic zero by subtracting half the trace; their squares are scalar. If arbitrary traceful matrix lifts are used instead, define the scalar residue by half-trace throughout: only that scalar component, not the whole matrix square, has the following transformation law. If two lifts of the same first-normal matrix differ by `q0² Z`, then their square coefficients differ by `tr(nZ)`. On an overlap, conjugate one lift by the lifted transition first. The same argument shows that the two scalar coefficients agree modulo the image of

`tr(n·): End_0(G)(-2) -> O_X`,

which is exactly `I_Z²` by the actual trace sequence. Arbitrary failures of the lifted transitions on triple overlaps do not obstruct this equality: conjugation preserves the scalar square, while changes of the local matrix lift have already been killed in the quotient. Thus the local residues glue canonically to a section of `O_2Z=O_X/I_Z²`, intrinsic to the fixed first-normal pair.

The line cancellation is essential: `N` has twist two, `N²` has twist four, and `q0²` has twist four. Therefore its coefficient is an ordinary scalar, not an unspecified determinant-valued section. Relative to `q` instead, the conversion factor remains `nu^-2` as in Section 1.

For the actual degree-eight vertex quotient the exact relation sequence is

`0 -> P4 O_L(-8) -> Sym8(Wprime) O_L(-4) -> Q4 -> 0`.

The already established splitting is `Q4=W O_L(1) ⊕ V O_L(-2)`. Hence

`H0(Q4)=W tensor W = 1 ⊕ A`,

and its invariant line is one-dimensional. The actual pair and scalar-square construction are equivariant, and the earlier filtration comparison identifies the nonzero residue computed here with their degree-eight vertex associated-graded class. Consequently that class is a nonzero multiple of the invariant generator called `n8` in the actual normal-trace sources.

The conic component can also be excluded, but requires an actual transverse slice, not merely the observation `N|C=0`. Use the fixed positive plane `P(V)` in the ambient projective space. Its conic is defined by the restriction of `q0`. The slice thickening defined by `q0²` lies in the second neighborhood of X, so the genuine midpoint nilpotent restricts there. Because its restriction to C is zero, division by q0 on this slice gives a canonical section of `End_0(G|C)`: the nilpotent twist two and the normal twist two cancel. The actual conic balance, equivalently `F|C=W O_C0(-1)`, identifies its global section representation with `sl(W)`, which has no invariant. Equivariance therefore forces the restricted nilpotent to vanish on the entire slice thickening. Any local lift to the slice defined by `q0³` is then divisible by `q0²`, so its square has zero `q0²` coefficient. Thus `chi|C=0`.

Distinguish this slice thickening from the ordinary `2C` inside X. The latter has negative conormal bundle `W O_C0(-2)`, with no global sections, hence `H0(O_(2C))=C`. Its scalar residue component is therefore entirely zero. At the vertex there is no constant term, since the actual leading residue has positive cover degree eight. Finally the already established global invariant space is

`H0(O_(2Z))^G = C·1 ⊕ C·e_v ⊕ C·n8`.

It follows that the **full global scalar residue of the fixed midpoint pair** is `chi_bar=c_chi n8` with `c_chi != 0`. The conic balance and conormal bundle are pinned in `ACTUAL-NORMAL-TRACE-HAS-NONZERO-NILPOTENT-COMPONENT.md`; the invariant scalar space is pinned in `ACTUAL-NORMAL-VARIATION-TRACE-HAS-A-GLOBAL-NULL-HOMOTOPY.md`, Section 1. No absolute coefficient relative to a separately marked n8 is asserted.

This sharpens the **midpoint nilpotent-extension obstruction** only. In particular it does not assert that the endpoint first-normal nilpotent glues, or that its fourth Bockstein is nonzero.

Sources for the graded sequence and splitting are `VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md`, equation (2), and `ACTUAL-SQUARE-QUOTIENT-SPLITTING-AND-BOTH-BOUNDARY-CHANNELS.md`.

## 6. Exact differentiated-square constraint, without an N2

Let `Dq=rho q`, and use the **complete** actual symbols and connection, including any `q H1` symbol and all finite-transport terms:

```
Ehat = Hhat D Ncorr + [Ahat,Ncorr] - Lambdahat Ncorr,
Ehat = q L(R1) + q² L(R2) mod q³.
```

The cone error is zero. There is an exact algebraic identity

`{Ncorr,Ehat}=(Hhat D-2Lambdahat)(Ncorr²)`.

Since `Ncorr²=q²L(chi)I mod q³`, taking the scalar half-trace of the `q²` coefficient gives

`tr(n R2)+tr(T R1)+tr B1(n,R1)
 = H0 D chi+2(H0 rho-Lambda0)chi`.

Before taking half-trace, the left side contains both `B1(n,R1)` and `B1(R1,n)`. Their traces agree by the symmetry of the second scalar transvectant. No `N2` has been introduced, and no full vanishing of `R1` is assumed. This identity is a necessary constraint on the full next error, not its computation. In particular, the separately computed old-K summand cannot replace `R2` here.

The cone preservation equation implies that `H0 D` preserves the ideal generated by the entries of `n`, so the displayed relation descends to its square-ideal quotient. There is a useful limitation: for a regular pair of degrees three and five,

`Hilb(S/(f,g_x)²)=(1-t⁶-t⁸-t¹⁰+t¹¹+t¹³)/(1-t)²`.

This polynomial has degree eleven, length forty-five, and degree-eight dimension five. The scalar differentiated relation raises degree eight by four, into degree twelve, where the quotient is zero. Thus its **unreduced** identity is substantive, but this particular degree-twelve quotient cannot detect a further obstruction. The nonzero degree-eight nilpotence residue above remains unaffected.

## Verification

Run `python verify_actual_nilpotent_second_normal_residue.py`.

The verifier checks the complete first-order square-zero identity, scalarity and regularity of the full octic, exact homogeneous division and its nonzero pivots, the displayed residue and nonzero coefficient, the universal second-correction image, and the Hilbert-series/differentiated-square bookkeeping. Parameters remain symbolic throughout. All previously frozen sources are unchanged.
