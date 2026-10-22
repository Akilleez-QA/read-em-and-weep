# Three target types have no off-discriminant divisorial torsion

## Theorem

Let T2 be the actual nonzero invariant pure cross-block section of F4 external-tensor O(6) on T x T, obtained by dividing the raw boundary by the diagonal squared. For each of the following possible target types,

    I.   F4=P4 O(6),
    II.  F4=W' O(5) directsum W' O(7),
    V.   F4=O directsum V O(8),

the section T2 has NO divisorial common zeros away from the diagonal. Consequently Q6=coker[S7*->K8] has no divisorial torsion away from the discriminant.

In any of these three types, if the actual leading diagonal scalar is nonzero, the residual map W tensor S6* -> K8 has generic rank FOUR. Equivalently, residual generic rank two in these types forces the leading scalar to vanish. Neither the actual target type nor the scalar value is selected here.

## 1. Small invariant divisors on the ordered-root surface

Let E_div be the closure of the divisorial common-zero cycle of T2 off the diagonal D. Its canonical defining section spans a G-stable line in H0(O(p,q)). Since G=SL2(F5) is perfect, this is an invariant section f. The standard linearizations are used on both factors.

The divisor does not contain D. Therefore f|D is a NONZERO binary invariant of degree p+q. Each nonzero component of T2 has bidegree (d_i,6), with d_i<=18 in the seven allowed types. Hence 0<=p<=18 and 0<=q<=6.

The universal binary-icosahedral character calculation gives invariant degrees up to24 exactly

    0,12,20,24.

For nonempty E_div it follows that

    p+q is 12,20,or24.                               (1)

This is stronger than merely bounding q. It applies to the whole common-divisor cycle with multiplicities. It does not say every invariant biform of these degrees occurs as an actual common factor.

Because f is invariant, dividing by it would give a nonzero invariant section of

    F4(-p) external-tensor O(6-q).                    (2)

We now exclude this for the three types.

## 2. Type I: P4 O(6)

Here p<=6 and q<=6. The only possibility in (1) is (p,q)=(6,6). Dividing would leave a constant invariant vector in P4. There is none. Thus no such divisor exists.

## 3. Type II: W' O(5) plus W' O(7)

Here p<=7,q<=6. Equation (1) leaves (6,6) or (7,5). In either case the degree-five summand cannot contribute to (2), and the degree-seven summand leaves a section transforming as W' tensor W. Since the two binary two-spaces W and W' are inequivalent irreducibles, this has no invariant. Thus no such divisor exists.

## 4. Type V: O plus V O(8)

Here p<=8,q<=6. The possible pairs are (6,6),(7,5),(8,4). The degree-zero summand cannot contribute. The residual bidegree in the other summand is respectively (2,0),(1,1),(0,2). Their binary coefficient representations are A,1+A,A, where A=Sym^2 W. The positive V is the OTHER genuine three-space, not A. Consequently none of their tensor products with V has an invariant. This excludes the common divisor.

By the exact off-diagonal block formula, the pullback divisorial torsion cycle of Q6 away from D equals E_div plus its root swap. Thus the three exclusions above imply the claimed absence of off-discriminant divisorial torsion, while allowing isolated bad fibers.

## 5. Actual Hermite calculation on the discriminant

The remaining issue is the discriminant itself; independent reduced-root values cannot be used there. Fix an affine root coordinate z, a double root t, h=z-t, and a scalar root section u0+h u1 in the pure S7* source. Put b0(z)=ell(z)^8, in the Cartan subspace.

Here is the precise source embedding, including its derivative correction. In the full A-valued root source it is c(z)=ell(z)^2(u0+h u1), with ell(z)=ell_t+h v. Its linear remainder has

    c0=ell_t^2 u0,
    c1=ell_t^2 u1+2 ell_t v u0.

Thus the pure source is not obtained by holding the A-valued coefficient constant. We may nevertheless keep the full polynomial representative ell(z)^2(u0+h u1): replacing it by its remainder modulo h^2 changes it by h^2 d(z), hence changes the division quotient by a(z)d(z), where a(z) is the actual square map. The actual boundary delta_z(q0 a(z)d(z)) vanishes identically, including its z derivative, because every a(z)d(z) is a same-root square. Keeping the full representative is therefore legitimate in the varying-boundary Hermite formula. It gives a(z)c(z)=b0(z)(u0+h u1) exactly. The common O_P(1) source twist is trivialized in this affine chart; no complementary-root division is used at the double root.

With this justification, the actual scheme-theoretic division formula gives, modulo h^2,

    J0=b0''(t)u0/2+b0'(t)u1,
    J1=b0'''(t)u0/6+b0''(t)u1/2,
    j(u0+h u1)=-delta_t(J0)-h[delta_t(J1)+delta'_t(J0)],

where q0 is understood in each argument of delta. This is the actual varying boundary, not a constant boundary evaluated twice.

Write

    c=delta_t(q0 b0''(t))/2.

The identities delta_z(q0 b0(z))=0 and delta_z(q0 b0'(z))=0 hold for all z because the value and first derivative are actual squares. Differentiating the second identity gives

    delta'_t(q0 b0'(t))=-delta_t(q0 b0''(t))=-2c.

It follows that the reduced-root output is -c u0, and the coefficient of u1 in the nilpotent output is +c. The u0 nilpotent output can be arbitrary; it does not affect independence. Whenever c is nonzero, the u0 column has nonzero reduced value while the u1 column has zero reduced value and nonzero nilpotent value. Thus j is fiber-injective there.

The section c is exactly the diagonal restriction of the divided-squared cross block, up to the fixed nonzero frame normalization. Its invariant space is one-dimensional. If its scalar is nonzero, c is nonzero at the generic point of T, so j is generically fiber-injective along the discriminant. There is then no divisorial torsion of Q6 on that discriminant.

No second-derivative vanishing is assumed. The low Sym^4 component of an actual square prevents that shortcut.

## 6. Conditional residual injectivity

For types I,II,V, Sections 2-4 exclude off-discriminant divisorial torsion. If the leading diagonal scalar is nonzero, Section 5 excludes it on the discriminant too. Hence Q6 is torsion-free in codimension one.

But a residual generic rank-two kernel N would satisfy c1(N)=-d with even d>=6 and would give a torsion subsheaf

    S5*/N subset Q6

of divisorial degree d-4>=2. This contradicts absence of divisorial torsion. Therefore residual generic rank is four in this conditional situation.

This uses the previously proved actual kernel identification and finite Chern gate; it does not use genericity of an arbitrary three-parameter section. The scalar and target type remain actual open data.

## Reproducibility

verify_pure_divisor_type_exclusions.py checks the binary invariant degrees through24 and all remaining representation spaces (2). It also emits necessary bidegree candidates for the other four types; these are possibilities, not realized divisors. It depends only on the universal character definitions in verify_pure_cross_block_couplings.py. No actual coefficients, matrix ranks, or selected fibers are computed.

Dependencies: PURE-CROSS-BLOCK-THREE-COUPLINGS-AND-DIVISOR-GATE.md; PURE-VERTEX-SQUARE-INJECTION-AND-RANK-TWO-TO-SIX-GATE.md; the actual root/Hermite division formula; and the finite Chern gate. No complete repair or actual scalar value is claimed.
