# A fixed repeated-input and fixed dual-line certificate for the cubic

## Result

Use the modules, literal derivative-basis classes D_i (i in F_5), and conventions of [the cubic massey module reduction manuscript](../../canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md). For every N-equivariant trilinear map f:V^3 -> J3 with outer reversal and cyclic zero,

    f != 0  iff  f(D_0,D_0,D_1) != 0.

In the literal opposite-cochain convention this selected value belongs to the one-dimensional diagonal weight space (4,4) of J3. Its Serre-dual line in J2 is exactly

    C q,    q = e_(+,V,2).

Here e denotes the Z-zero quotient basis of [the derivative transgression relations manuscript](../../../derivative-transgression-relations/EXPLICIT-COEFFICIENT-QUOTIENT.md), not a raw entry before passing to the quotient. Thus the single fixed scalar

    c(f) = < f(D_0,D_0,D_1), q >_Serre

vanishes if and only if f vanishes. This statement selects inputs and a dual class symbolically; it does not determine c(f), construct a defining system, or assert nonvanishing of the actual cubic.

## 1. The symmetric-pair map is injective for nonzero f

Define the linear map

    Psi: Sym^2 V -> Hom(V,J3),
    Psi(u odot v)(w) = ( f(u,v,w) + f(v,u,w) )/2,

where u odot v denotes the class of u tensor v in the symmetric quotient. In particular Psi(u^2)(w)=f(u,u,w). This is N-equivariant, with the usual conjugation action on Hom.

If Psi=0, then f is antisymmetric in its first two arguments. Combining this with outer reversal gives, for arbitrary x,y,z,

    f(x,y,z) = -f(y,x,z) = -f(z,x,y)
             = f(x,z,y) = f(y,z,x)
             = -f(z,y,x) = -f(x,y,z).

Consequently f=0 in characteristic zero. Notice that cyclic zero is not needed for this step.

The primary-source decomposition imported in [the equivariant massey multiplicity manuscript](../../foundation-p05/ELIGIBLE-MULTIPLICITY.md) is

    Sym^2 V = A tensor Sym^2 W'.

The three-dimensional Sym^2 W' is irreducible, and A restricts irreducibly to H5. The normal-subgroup argument in [the full hm image symmetry manuscript](../../../full-hm-image-symmetry/PROOF.md) therefore makes Sym^2 V an irreducible fifteen-dimensional N-module. Hence for nonzero f the nonzero map Psi is injective. Since D_0^2 is a nonzero element of Sym^2 V,

    L: V -> J3,    L(v)=f(D_0,D_0,v)

is nonzero. This avoids assuming that f itself is symmetric in its first two arguments.

## 2. The stabilizer forces a four-dimensional nonzero slice

Let T be the quadratic diagonal subgroup s_i=alpha^i beta^(i^2), with alpha^5=beta^5=1, and let P_2 be the permutation matrix specified by (P_2 v)_i=v_(2i). Its determinant is -1. For a subgroup of N in SL5 use the corrected lift -P_2, together with T, and call the resulting subgroup K.

The diagonal derivative weights in the opposite-cochain convention are

    wt(D_i)=(-i,-i^2).

These five weights are distinct; D_0 has the trivial T-character. The formal differentiated chain identity transports D_w to D_(G^-1 w). For the row-index convention of P_2 this sends D_i to D_(2i); the corrected lift -P_2 sends it to -D_(2i). Thus K preserves both CD_0 and

    M = span(D_1,D_2,D_3,D_4).

The four distinct diagonal weight lines of M are permuted transitively by multiplication by 2. Every K-invariant subspace of M splits into T-weight lines and must be a union of their transitive orbit. Hence M is irreducible. This also proves the needed assertion in the equivalent left-action convention; reversing all actions changes no invariant subspace.

More generally, preservation of CD_0 suffices for stability of ker L. Indeed, if g D_0=chi(g)D_0, equivariance gives

    L(gv)=chi(g)^(-2) g L(v).

Here chi is trivial on T and is -1 on the corrected multiplier. In particular no mistaken claim that every chosen lift fixes D_0 is required.

Cyclic zero gives 3 f(D_0,D_0,D_0)=0, so CD_0 is contained in ker L. Since L is nonzero, its restriction to M is nonzero. Irreducibility of M makes that restriction injective. Thus

    ker L = CD_0,    dim im L = 4.

The dimension statement is a universal representation-theoretic consequence, not a computed rank of the actual operation. In particular L(D_1) is nonzero whenever f is nonzero. The reverse implication is immediate.

## 3. Exact target and dual normal-form labels

For T the determinant is one, since the sums of i and i^2 over F_5 are both zero modulo 5. The equivariant Serre trace therefore takes values in the trivial T-character. The perfect pairing is

    J3 x J2 -> H^4(O(-5)) -> C.

The selected input has weight

    2 wt(D_0) + wt(D_1) = (-1,-1) = (4,4).

The imported explicit J2 quotient has distinct weights

    (a, 2a^2 + delta),
    delta(-U)=1, delta(+U)=2, delta(-V)=3, delta(+V)=4,
    a=3i.

The inverse character of (4,4) is (1,1). Solving 3i=1 gives i=2, and delta=1-2(1)^2=-1=4. Hence its unique J2 line is C e_(+,V,2). Equivalently, the (4,4) line in J3 is the dual of this line. It is one-dimensional and pairs perfectly with it. Therefore c(f)=0 exactly when the selected cubic value is zero, completing the claimed equivalence.

Converting to the usual left action negates all these diagonal weights simultaneously. It does not change the selected literal quotient class q. The determinant correction on the multiplier matters for odd twists but has no effect on the diagonal weight computation. No permutation determinant character is silently inserted into the diagonal Serre pairing.

The fixed q is a nonzero cohomology class: it is one of the proved quotient basis classes. Its resolution-Hom representative has elementary B entry (+,V_2), with its uniquely determined closed A block. This is a static basis specification, not multiplication of derivative matrices. One must not replace q by an arbitrary raw B-coordinate functional or ignore the Z-elimination relations.

## 4. A single abstract residue, with the representative boundary explicit

For this section specialize f to the actual canonical operation m111; the preceding representation-theoretic criterion applies to every symmetry-eligible f. Choose closed degree-one representatives a,b,c of D_0,D_0,D_1 and adjacent primitives satisfying dh_ab=ab and dh_bc=bc. The canonical cubic has representative

    C111 = a h_bc + h_ab c

of degree two and twist -3. Choose any closed degree-two representative eta_q of the already fixed class q at twist -2 in the regular Thom-Whitney model. With the ordered cover and residue normalization of [the ordinary trace-residue normalization](../../foundation-p06/TRACE-RESIDUE.md),

    c(f) = [x_0^-1 x_1^-1 x_2^-1 x_3^-1 x_4^-1]
             integral_[01234] tr(C111 eta_q).

This follows from the same trace-cup Serre pairing argument. Its factors have degrees two and two, so their interchange inside the trace has no Koszul minus sign. No rank-two trace-splitting factor 1/2 is part of this Serre normalization.

This formula does not import the special orbit-first reduced C_r(X;b,c) formula into a nonexistent weight-three case. It uses the ordinary cubic defining cocycle. The dual class is now preselected, rather than existentially quantified. An explicit regular eta_q and the adjacent primitives remain to be supplied if one wants an executable scalar expression; none is constructed or evaluated here.

