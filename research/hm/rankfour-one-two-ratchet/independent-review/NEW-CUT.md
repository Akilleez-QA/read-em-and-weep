# A near-top multiplicity obstruction for the remaining cubic W-prime quotient

## Exact statement

Retain the actual saturated inclusion E in the original thirty-dimensional constant Gauss ambient, the physical binary-icosahedral marking, the fixed connection, and the four necessary source types. In source D, let K be the actual derivative kernel and B=E/K. Then

    B = O(-8) + W' O(-3) + O(14)

is impossible. The assertion uses neither the upper endpoint splitting nor any assumption on its determinant torsion. It therefore excludes both corresponding tuples in the independently checked ordered rank-four (1,2) three-tuple reduction, including the tuple with second defect twelve.

Here S=Sym3 W, D=Sym4 W, T=Sym5 W, and V is the physically marked other three-space. This is not a realization assertion or a closure of the entire ordered profile.

## 1. Actual cubic kernel information

The complete rank-independent cubic-channel proof at PR1140, immutable head 7a2488bcd36d95f79b5198001111b1a31fe5c3ba, proves for the actual source-D kernel

    H0(K(3)) = 0 or S.

It also proves that K has no degree above -3. The result is not merely the weaker dimension or single-channel visibility statement. It is valid for this actual quotient independently of the derivative rank. The relevant input is retained in inputs/pr1140-cubic-visibility.md with byte and Git-object authentication.

Exact equivariant Euler subtraction in 0 -> K -> E_D -> B -> 0 gives

    chi(K(3)) = -W',
    chi(K(4)) = D + 2V.                            (1)

Thus H1(K(3)) is W' or S+W', matching the two alternatives for H0(K(3)). No vanishing of H0(Q*(1)) is involved.

## 2. Complete kernel splitting classification

For a block R O(-j), j>=5, its contribution to H1(K(3)) is

    R tensor Sym^(j-5) W,

of dimension (j-4) dim R. Every contribution is genuine, so no forbidden constituent can cancel. If H1(K(3)) has dimension d, every negative block has j<=4+d. Consequently the complete ranges are j<=6 for W' and j<=10 for S+W'. Central parity is retained.

Within those finite domains, the complete list of blocks whose H1 contribution is contained in S+W' is

    S O(-5) contributes S;
    W' O(-5) contributes W';
    O(-8) contributes S.

The W'-only case has only W' O(-5). All remaining blocks have degree -3 or -4. The degree-minus-three coefficient is already fixed by H0(K(3)), and (1) determines the degree-minus-four coefficient exactly.

If H0(K(3))=0, the only possibility is

    K = (D+2V) O(-4) + W' O(-5).                  (2)

If H0(K(3))=S, using S O(-5) to provide the extra S in H1 would require the degree-minus-four coefficient 2V-A, which is not a genuine representation. Here S tensor W=A+D. Using O(-8) instead has H1(O(-8)(4))=A and yields the sole possibility

    K = S O(-3) + 2V O(-4) + W' O(-5) + O(-8).   (3)

Both (2) and (3) have rank thirteen and degree minus fifty-four. The classification is complete from the actual cubic kernel alternatives, not from a truncated numerical search or a presumed splitting of a connection.

## 3. Two coefficient copies versus one derivative row

The actual derivative of K has its coherent image in

    B(-2) = O(-10) + W' O(-5) + O(12).

For either possible K, consider its two equal-degree V O(-4) summands. Their derivative to the first two displayed target blocks is zero by ordinary degree. Their only possible target is O(12), and

    dim Hom_G(V O(-4), O(12))
      = multiplicity of V in Sym16 W = 1.        (4)

Therefore the linear map from the two-dimensional coefficient multiplicity space to this one-dimensional Hom space has a nonzero kernel. A coefficient line in that kernel supplies a full equivariant direct summand L=V O(-4) of K killed by its actual second fundamental form. This is a simultaneous multiplicity obstruction, not an independent nonzero-Hom test for each copy and not a claim about a selected actual rank.

Since the derivative of L lands in K, its intrinsic second fundamental form factors through (K/L)(-2). Every degree of K/L is at most -3, so every degree after that twist is at most -5. Hence

    Hom(L,(K/L)(-2))=0.

It follows that L is horizontal in the original constant ambient. L is saturated there: it is a direct summand of K and K is saturated in the ambient. A saturated horizontal subbundle in characteristic zero is constant. Its degree is -12, a contradiction.

This excludes the proposed B in both cases and for every upper torsion character.

## 4. Exact certificate and boundary

The independent checker derives all tensor multiplicities by exact conjugacy-class inner products over Q(sqrt5), without importing the author's McKay implementation. It checks the full j<=6/j<=10 domains, both retained K splittings, the nongenuine discarded coefficient, (1), (4), and both internal Hom vanishings. Normal, optimized, and different-working-directory runs agree. Executable mutations deleting the cubic alternative or truncating the tail domain are rejected.

In the independently checked ordered rank-four (1,2) reduction, this cuts three necessary tuples to the single necessary tuple

    E=E_D;
    a=-58, b=-22, delta1=delta2=0;
    B=O(-8)+W' O(-1)+O(14);
    Z0=W' O(-5)+V O(-4).

This note does not exclude that final tuple. No actual coefficients, parameter values, jets, tensors, matrices, or instance ranks are evaluated, and no public or upstream writes are made.
