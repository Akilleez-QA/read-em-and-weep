# Actual equivariant splitting constraints and Gauss persistence

## Result and scope

The actual equivariant cohomology and kernel presentations imply:

1. E has at most 28 formal equivariant splitting types, explicitly parametrized below. Every ordinary line summand has degree in {-2,-3,-4,-5,-8,-9,-10}; in particular none has degree below -10.
2. H0(E(2)) can vanish in only one of these types:

       E = (W'+2T6) tensor O(-3) + V tensor O(-4).    (1)

3. H0(E(3)) contains W'+2T6, and H0(Q*(3)) contains T6.
4. If the actual SF has generic rank three and its maximal rank-three plateau has k blocks below E and l blocks above it, then

       1<=k<=3,  1<=l<=3.

   Moreover l<=2 unless (1) holds. Thus l=3 forces the unique splitting (1).

The 28 types are compatible formal splitting data, not a realization theorem. No generic-rank-three exclusion follows here. The frozen lower bounds generic SF rank>=3 and positive-square rank>=27 remain unchanged. There is no new conclusion about maximal rank, smoothing, or the generic section count.

The argument uses no actual coefficients, actual matrix/rank tests, or local-model experiments. Its polynomial-jet argument is a universal proof for arbitrary sections, not a selected instance computation.

## 1. Actual input and conventions

Let G be the binary icosahedral group, W the standard center-odd two-space, W' its other two-space, A=Sym^2 W, V the other even three-space, P4 the even four-space, S4=Sym^3 W, D5=Sym^4 W, and T6=Sym^5 W. All these irreducibles are self-dual.

The actual bundles have equivariant presentations

    0 -> E -> M3 tensor O(-1) -> M4 tensor O -> 0,
    0 -> Q* -> M3* tensor O(-1) -> M2* tensor O -> 0,

where

    M2=A+2V+3P4+4D5,
    M3=3W'+3S4+6T6,
    M4=2V+4P4+3D5.

The second sequence is obtained by dualizing the actual locally free quotient presentation of D_lin and twisting by O(-1), since Q=D_lin(1). The uniform injectivity of the first multiplication map ensures this is an exact sequence of bundles. These presentations were established in the frozen positive double-hyperplane and uniform hyperplane notes.

We retain rank E=17, deg E=-54, H0(E(1))=0, and rank Q*=13, deg Q*=-54. E and Q* are center-even. E contains no constant subbundle and spans the constant ambient H; the dual statements hold for Q*. We use chi_G for equivariant Euler characteristic.

The first presentation gives

    H1(E(1)) = W'+3T6,
    chi_G(E(2)) = -V,
    chi_G(E(3)) = W'+2T6.                         (2)

The second gives

    H1(Q*) = M2,
    chi_G(Q*(3)) = T6-2W-S4.                     (3)

All identities are checked by exact abstract character arithmetic in the verifier. In particular the positive irreducible multiplicities in (2)-(3) imply

    H0(E(3)) contains W'+2T6,
    H0(Q*(3)) contains T6.                        (4)

Indeed the multiplicity of any irreducible in H0 equals its Euler multiplicity plus its nonnegative multiplicity in H1. No vanishing of the corresponding H1 is presumed.

## 2. Equivariant splitting is legitimate

For a finite group in characteristic zero, Birkhoff-Grothendieck splitting may be chosen equivariantly. One proof uses the canonical slope filtration, which is G-invariant. Its graded pieces of equal degree are R_j tensor O(-j). The extensions between successive distinct slopes split: Ext^1(O(b),O(a))=H1(O(a-b))=0 for a>b. Averaging any splitting over G makes it equivariant without changing its right-inverse property.

This equivariant splitting need not be canonical or compatible with the ambient connection. It is used only for bundle cohomology, not as a horizontal splitting of any Gauss flag.

Thus write

    E = direct sum_(j>=2) R_j tensor O(-j).         (5)

The lower bound j>=2 follows from H0(E(1))=0. The multiplicity spaces R_j are genuine representations. Since E is center-even, the central involution acts on R_j by (-1)^j. The standard linearization of O(-j) has exactly this sign; there is no additional character because G is perfect.

By equivariant Serre duality, using det W=1 and self-duality of Sym^n W,

    H1(E(1)) = sum_(j>=3) R_j tensor Sym^(j-3) W.   (6)

All terms on the right are genuine representations, so forbidden irreducible constituents cannot cancel.

## 3. Complete list of possible negative blocks

The right side of (6) is W'+3T6 and has dimension 20. For every nonzero irreducible summand R in R_j,

    (j-2) dim R <=20.

In particular j<=22. Checking the nine irreducible representations with their required central parity over this finite range gives exactly the following possibilities:

| j | R | Contribution R tensor Sym^(j-3) W |
|---:|---|---|
| 3 | W' | W' |
| 3 | T6 | T6 |
| 4 | V | T6 |
| 4 | P4 | W'+T6 |
| 5 | W' | T6 |
| 8 | 1 | T6 |
| 9 | W | W'+2T6 |
| 10 | 1 | W'+T6 |

Every other parity-compatible irreducible either contributes W or S4, another forbidden constituent, or exceeds an available multiplicity. This is a complete finite representation check, not a choice of a map or coefficient.

Let a,b,c,d,e,f,g,h be the multiplicities of these eight rows in order. Equation (6) becomes

    a+d+g+h = 1,
    b+c+d+e+f+2g+h = 3.                           (7)

At twist two the same blocks give

    H1(E(2)) = (c+g+h)V
               +(d+e+g+h)P4 +(f+g)D5.

Meanwhile H0(E(2))=R_2. The actual identity chi_G(E(2))=-V therefore forces

    R_2 = (c+g+h-1)V
          +(d+e+g+h)P4 +(f+g)D5.                 (8)

This is genuine precisely when

    c+g+h >=1.                                    (9)

There are exactly 28 nonnegative integer solutions of (7)-(9): ten with a=1, four with d=1, four with g=1, and ten with h=1. Each has total rank 17 and degree -54. Equations (7)-(8), together with the table, completely specify all 28 formal equivariant splitting types compatible with these cohomological constraints.

The coefficients in (8) vanish simultaneously only for

    (a,b,c,d,e,f,g,h)=(1,2,1,0,0,0,0,0).

This is exactly (1). Every other candidate has H0(E(2)) nonzero. Its possible dimension is one of 3,4,...,14; the exceptional candidate has dimension zero.

This classification does not assert that each type occurs for the actual multiplication pencil or can be embedded with the required Gauss rank. It gives necessary actual bundle data only.

## 4. A section bounds the length of a constant-rank Gauss plateau

The following lemma applies to any generic rank r, not only three.

Let

    F0 subset F1 subset ... subset Fm,
    Fk=E,   m=k+l,

be a maximal consecutive plateau of rank-r Gauss blocks. At each interior stage, the derivative kernel and forward transform satisfy

    ker beta_(Fi)=F_(i-1),    Fi^+=F_(i+1).        (10)

The inclusions come from differentiation; equal generic ranks and saturation give equality of sheaves. Exactly as in the frozen rank-two argument, every Fi with i<m contains no nonzero constant subbundle: above E any constant subbundle propagates backwards through the kernels in (10). Every Fi with i>0 spans the whole ambient constant space: below E a proper constant span would propagate forward to E. These arguments are independent of the value of r.

Suppose H0(E(d)) is nonzero. Saturate the image of a nonzero map O(-d)->E to a line L=O(-e). Then e<=d. The line is also saturated in the constant ambient bundle, because both successive quotients are locally free. Moreover e>=1: a nonnegative-degree line in a trivial bundle must have degree zero and be constant, contradicting H0(E)=0.

The inclusion O(-e)->H tensor O is represented on an affine coordinate chart by a polynomial vector

    f(z)=v0+v1 z+...+ve z^e.

The vectors f(z), f'(z),...,f^(e)(z) span the constant coefficient space <v0,...,ve>: the change of generators is triangular with nonzero factorial diagonal in characteristic zero. Therefore the e-th forward Gauss transform of L has reached its constant span, possibly earlier. Saturating extends this equality across the omitted parameter and across derivative ramification.

Inductively the j-th transform of L is contained in F_(k+j), whenever that stage exists, because differentiation and saturation preserve the inclusion. If l>d, its constant span would be contained in the interior stage F_(k+e), since e<=d<l. This contradicts (10) and its constant-subbundle consequence. Hence

    H0(E(d)) nonzero  implies  l<=d.               (11)

Apply the same argument to the dual reversed plateau, whose central bundle is E^perp=Q*. Its forward length is k, so

    H0(Q*(d)) nonzero  implies  k<=d.              (12)

This proof does not split the plateau into line curves. It uses just one saturated line supplied by a section, inside the original filtered bundle.

## 5. Consequence for a hypothetical rank-three SF

For generic SF rank three, monotonicity of outward Gauss increments gives a maximal rank-three plateau. A priori 1<=k<=5 and 1<=l<=4, since rank E=17 and codimension E=13. Its endpoints have SF rank one or two; no rank-one endpoint theorem is assumed for them.

Equations (4), (11), and (12) sharpen the bounds to

    1<=k<=3,   1<=l<=3.

For each of the 27 nonexceptional splitting types, H0(E(2)) is nonzero, so l<=2. If l=3, the actual splitting is necessarily (1). This is the promised bounded rank-three constraint, not a contradiction.

## Reproduction

Run `python verify_equivariant_splitting_gauss_persistence.py`.

The verifier checks the actual Euler characters, the complete finite list of allowed irreducible splitting blocks, all 28 coefficient tuples, their rank/degree and cohomology identities, and the unique twist-two-section-free type. The universal jet/saturation proof is supplied above; no actual polynomial vector or HM map is evaluated.
