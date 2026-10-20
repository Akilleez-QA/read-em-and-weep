Publication scope: this is an abstract finite-module construction, independently reviewed symbolically in CANDIDATE-AUDIT.md. The historical pending-audit sentence is superseded only for that bounded construction. It does not realize a reflexive defect.

# An abstract length-sixteen module passing the existing relation budget

## Statement and limitation

There are abstract finite-length H-equivariant modules P with precisely the residual presentation and Hilbert function in PROOF.md, and with

    s=4, beta1=10, a_H(Tor1(P,C))=0.

Thus the presently established necessary inequality beta1+a_H<=2s+2 is attained. This is **not** a construction of a reflexive module whose isolated Ext² defect has finite dual P. It gives no physical source/model instance, rank instance, or global realization. Any exclusion at length sixteen must use an additional necessary condition, not merely nonexistence of the residual homogeneous module.

## 1. Presentation and full H action

Work in the abstract ring R=C[[x1,x2,x3,x4]], with canonical B-weights wt(x_i)=(i,3i²). Indices are in F5*, and all subscripts are read modulo five. Let lambda be any nonzero complex scalar satisfying lambda^4 !=1, and let epsilon=1 or -1.

Take four generators t_j of B-weight (j,0), and impose

    x_i t_{3i}=0,                                      (M_i)
    x_i t_i=lambda x_{-i}t_{3i},                       (L_i)
    x_i t_{-i}=-epsilon x_{-i}t_i.                    (C_i)

There are four independent M_i, four independent L_i, and two independent C_i (the equations indexed by i and -i are proportional). The respective relation B-representations are O3, O2, and the pair (0,±2).

Choose a generator of C4 whose action on indices is i→2i, replacing the canonical generator by its inverse if necessary. Normalize bases so that g x_i=x_{2i}, and set g t_i=t_{2i}. Every displayed relation is carried to the relation with twice the index. In particular g² acts on the two-dimensional C-relation space by epsilon. This defines the full semidirect-product action with B, not just a B action.

Let omega be the central μ5 character on W. Let μ5 act on every t_j by omega^{-1}. Then the central character on all degree-one relations is trivial. These actions commute with B and C4, giving an H-equivariant presentation for the full direct product H=μ5×(B⋊C4). The normalization of the W basis is legitimate because the C4 action cycles four distinct B-weight lines and g^4=1.

## 2. Quadratic normal forms

For each j, x_{2j} kills t_j by (M_{2j}). The remaining six quadratic monomials on t_j are named

    A_j=x_j²t_j,          B_j=x_j x_{3j}t_j,
    C_j=x_j x_{-j}t_j,    D_j=x_{3j}²t_j,
    E_j=x_{3j}x_{-j}t_j,  F_j=x_{-j}²t_j.

Here C_j names a monomial, distinct from the label (C_i) for a relation. Multiples of the defining relations give

    A_j=0, E_j=0,
    B_j=lambda B_{3j},
    C_j=-epsilon F_{-j},
    D_j=-(epsilon/lambda)F_{3j}.

The four-cycle j→3j and lambda^4!=1 imply B_j=0. Thus all quadratics are spanned by the four F_j.

These F_j are independent. One direct verification is to use the displayed formulas as a linear map from the free degree-two space to a vector space with independent basis f_j, sending F_j to f_j and every monomial containing x_{2j} on t_j to zero. It annihilates every defining relation multiplied by every variable:

- multiples of M_i are zero by construction;
- for L_i, multipliers i,2i,3i,-i give respectively 0=0, 0=0, B_i=lambda B_{3i}, and C_i=lambda D_{3i};
- for the clock relation x_{-j}t_j=-epsilon x_jt_{-j}, multipliers j,-j,2j,3j give respectively C_j=-epsilon F_{-j}, F_j=-epsilon C_{-j}, 0=0, and 0=0.

All these identities hold under the normal-form map. Consequently the degree-two quotient has dimension exactly four, with basis F_j and B-representation O1.

## 3. Cubic normal forms and termination

Put G_j=x_j F_j. The quadratic identities imply

    x_{2j}F_j=0,   x_{3j}F_j=0,   x_{-j}F_j=0,
    G_{-j}=-epsilon G_j.

For the third zero identity, use F_j=-epsilon lambda D_{2j}=-epsilon lambda x_j²t_{2j}; the factor x_{-j} kills t_{2j}. The other two zero identities follow from M and E. For the relation among G_j, multiply C_j=-epsilon F_{-j} by x_{-j}.

Thus cubics are spanned by two G_j modulo the opposite-index relation. They are independent. For an explicit check of all possible ambiguities, define a cubic normal-form map to a two-dimensional space with symbols g_j satisfying g_{-j}=-epsilon g_j. On t_j the only monomials assigned nonzero values are

    x_j x_{-j}²t_j -> g_j,
    x_{3j}³t_j -> -(epsilon/lambda)g_{3j}.

Every other cubic monomial maps to zero. This respects every variable multiple of every quadratic identity in Section 2:

- multiples of A_j, B_j, E_j, or a monomial containing the forbidden x_{2j} all map to zero;
- C_j=-epsilon F_{-j}, multiplied by x_{-j}, gives g_j=-epsilon g_{-j}; its other three multiples map to zero;
- D_j=-(epsilon/lambda)F_{3j}, multiplied by x_{3j}, gives the second displayed value; its other three multiples map to zero.

The quadratic kernel is generated by precisely the identities already verified in Section 2. Therefore this map factors through the cubic quotient, proving its dimension is two. Its weights are (0,±1).

Finally every variable kills G_j. The variables x_{2j},x_{3j},x_{-j} already kill F_j; multiplication by x_j kills G_j because x_j²t_j=0. Hence degree four is zero, as are all higher degrees. The presentation therefore has Hilbert function

    (4,6,4,2),

and length sixteen. Completion changes none of these finite graded pieces.

## 4. Minimal relations and full representation imbalance

The ten displayed relations are independent in degree one: the four M_i have O3 weights, the four L_i have O2 weights, and the clock pair has weights (0,±2). They generate the relation submodule by definition of the presentation. Thus there are exactly ten minimal relations, with no additional minimal nonlinear generators:

    Tor1(P,C)=O3+O2+clock_pair_epsilon.

The central μ5 character of this space is trivial by the top twist chosen above. The O3 and O2 representations are dual: their B-orbits are negatives, and the induced four-cycle representation on each is unique up to isomorphism. The two-dimensional clock pair is self-dual for either epsilon. Indeed its B-weights are opposite and its C4 square is epsilon=epsilon^{-1}; equivalently it is the induced representation of the orbit with order-two stabilizer character epsilon, which equals its dual stabilizer character.

Therefore Tor1(P,C) is self-dual as a representation of the full H, and a_H=0. Since s=4 and beta1=10, beta1+a_H=2s+2=10. This is an equality-case abstract module, not an isolated-defect realization certificate. In particular no claim is made that an actual Tor map arising from a reflexive self-dual module has the additional structure needed to realize it.

## Scope and audit status

This construction and normal-form proof concern universal abstract local algebra. They use no physical source/model matrices, actual operation/input/rank instance, jet, residue, or detector evaluation; no external writes, installation, or large computation occurred. The parameter restrictions and normal forms are established symbolically by hand. Independent audit pending.
