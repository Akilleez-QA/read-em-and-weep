# Conditional discriminant factor and exact divisorial torsion of the pure map

## 1. Conditional global factor

Let j:S7* -> K8 be the actual sheaf-injective pure vertex-square map. Let R(r,s)=delta_r(q0 ell_s^8) be its raw ordered-root cross block, D the diagonal, and lambda its leading order-two diagonal scalar. All statements that assume lambda=0 below are conditional; no actual value of lambda is selected.

The established three-coupling argument shows

    lambda=0 implies R is divisible by D^4.

Put b(z)=ell(z)^8. This means delta_t(q0 b''(t))=delta_t(q0 b'''(t))=0 identically in t. The actual same-root-square identities also give delta_t(q0 b'(t))=0. Differentiating these identities as identities of sections of the actual relative target gives

    delta'_t(q0 b'(t))=0,
    delta'_t(q0 b''(t))=0.

For a double root, take the actual pure source c(z)=ell(z)^2(u0+(z-t)u1). Its Hermite formula is

    J0=b''u0/2+b'u1,
    J1=b'''u0/6+b''u1/2,
    j=-delta_t(q0 J0)
      -(z-t)[delta_t(q0 J1)+delta'_t(q0 J0)].

Every term vanishes under the conditional identities above. This uses the varying boundary and the varying source coefficient, not two reduced-root evaluations. Therefore j restricted to the discriminant is zero as a bundle morphism. Since the discriminant Delta is a Cartier conic, j factors globally and uniquely:

    j = Disc times j1,       j1:S7* -> K8(-2).

At the generic DVR of Delta, both elementary divisors of j have valuation at least one. Hence coker(j) has divisorial torsion cycle at least 2 Delta, of projective degree at least four. This conclusion alone does not force the residual map to have rank two.

## 2. Exact generic diagonal order determines the torsion multiplicity

Let k be the exact generic vanishing order of R along D. It is finite because the actual raw section is nonzero. Set e=k-2.

Work at the generic point of Delta, complete, and choose centered root coordinates with roots z and -z. The root algebra is

    A=K[[epsilon]],    B=A[z]/(z^2-epsilon),

where epsilon is a local equation of Delta. Trivialize the source root line and the four-dimensional target bundle near the generic root. In natural root-value coordinates the actual same-root block is zero and the cross block is

    -R(r,s)/(s-r)^2.

Here is a direct derivation retaining the whole actual quotient. Let P(z)=(z-r)(z-s), choose the A-valued linear interpolation c(z) of ell_r^2 u_r and ell_s^2 u_s, and divide

    a(z)c(z)=P(z)H(z)+A0+z A1.

Then A1=(b(s)u_s-b(r)u_r)/(s-r), and differentiation at r gives

    H(r)=[a'(r)c(r)+a(r)c'(r)-A1]/(r-s).

The boundary delta_r kills a(r)c'(r) and b(r). It also kills a'(r)ell_r^2: differentiating b(r)=a(r)ell_r^2 expresses this as b'(r)-a(r)(2ell_r v), both killed by the actual same-root boundary. Consequently

    delta_r(q0 H(r))=R(r,s)u_s/(r-s)^2.

Positive multiplication is the negative of this quotient boundary; the common overall sign has no effect below. This proves the exact natural-root formula, not merely its leading order. There is no independent derivative column left over and no missing complementary-root divisor.

Writing R=(s-r)^k T_k and evaluating r=z,s=-z, the map is consequently

    B -> B^4,       u(z) |-> z^e v(z) u(-z),          (1)

up to nonzero constants and invertible root-line frame factors, with v(0) nonzero. Equality holds first off epsilon=0; both sides extend regularly and the target is torsion-free, so it holds over A. Nonzero v(0) is precisely the exactness of the diagonal order k.

Some coordinate of v is a unit in B. Thus multiplication by v is a split B-linear injection B->B^4. The involution u(z)->u(-z) is an A-linear isomorphism. The only torsion in the cokernel of (1) therefore comes from multiplication by z^e on B.

If e=2m, this multiplication is epsilon^m times the identity. If e=2m+1, its matrix in basis 1,z is epsilon^m times

    [0 epsilon; 1 0].

The two DVR elementary exponents are consequently

    floor(e/2), ceil(e/2).

In particular the exact divisorial torsion multiplicity along Delta is

    k-2,

so the Delta contribution to the torsion cycle is exactly (k-2) Delta. This is a generic codimension-one assertion; it does not classify isolated degenerations or off-discriminant torsion.

## 3. Universal finite order possibilities

An invariant raw section divisible by D^k belongs to

    H0(F4(2-k) external-tensor O(8-k))^G.

The character calculation gives dimensions, for k=2,...,8:

    types I,II,III:  3,2,2,1,0,0,0;
    types V,VI:     3,2,2,1,1,0,0;
    types IV,VII:   3,2,2,1,1,1,1.

For k>=9 the second factor has no sections. The invariant spaces form a nested divisibility filtration, so equal successive dimensions mean equality of the corresponding spaces. Thus the possible exact generic raw diagonal orders are

    I,II,III: 2,4,5;
    V,VI:    2,4,6;
    IV,VII:  2,4,8.

No actual order is chosen. Conditional on lambda=0, delete order two. Combining with Section 2 gives the exact possible Delta torsion multiplicities:

    I,II,III: 2 or3;
    V,VI:    2 or4;
    IV,VII:  2 or6.

Their degrees as divisors in the parameter plane are twice these numbers. When lambda is nonzero, k=2 and the Delta torsion multiplicity is zero, recovering the independent Hermite injectivity test.

## 4. Sharper determinant bounds in the no-off-discriminant types

For types I,II,V, the established divisor theorem excludes all off-discriminant divisorial torsion of Q6=coker(j). Thus its total divisorial torsion degree is exactly 2(k-2).

If the residual map has generic rank two, its kernel N has c1(N)=-d, with even d>=6. The actual quotient map injects S5*/N into the torsion of Q6; the former has divisorial degree d-4. Generic lengths of an injected torsion subsheaf cannot exceed those of its ambient torsion at any prime divisor. Therefore

    d-4 <= 2(k-2), equivalently d <= 2k.

In types I and II, the rank-two alternative forces lambda=0 and k=4 or5. Its possible d values are consequently

    k=4: d in {6,8};
    k=5: d in {6,8,10}.

In type V the possible k are4 or6, giving

    k=4: d in {6,8};
    k=6: d in {6,8,10,12}.

These are necessary alternatives, not realized kernels. Types III,IV,VI,VII are not included in this bound: an off-discriminant contribution has not been excluded in their lambda=0 branch.

## Sources and limits

PURE-CROSS-BLOCK-THREE-COUPLINGS-AND-DIVISOR-GATE.md supplies raw diagonal divisibility and the seven target types. THREE-TARGET-TYPES-WITHOUT-OFF-DIAGONAL-TORSION.md supplies the fully varying pure Hermite formula. TWO-ROOT-DIVIDED-DIFFERENCE-SMOOTHING-FORMULA.md supplies natural-root normalization. PURE-VERTEX-SQUARE-INJECTION-AND-RANK-TWO-TO-SIX-GATE.md supplies actual sheaf injectivity and the torsion quotient.

The companion test verifies only universal representation spaces and the abstract quadratic root-algebra elementary exponents. No actual coefficient, matrix, selected fiber, rank, or scalar is evaluated. These conditional consequences neither establish lambda=0 nor settle residual injectivity.
