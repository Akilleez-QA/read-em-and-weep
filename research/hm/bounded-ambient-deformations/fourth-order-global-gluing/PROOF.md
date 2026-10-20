# Fixed explicit fourth-order products admit invariant ambient descent

## Scope and inputs

This is a conditional universal formal-geometric theorem, applied to the symbolic hypotheses already audited in the explicit-third-order and fourth-order-local-product notes. No actual source function, source derivation, module, matrix, or retained detector is evaluated. All equalities are modulo h^5 unless another modulus is specified.

Let X be a complex abelian variety, with inversion iota=[-1], h fixed, and a fixed individually iota-stable affine cover with affine finite intersections. All data and restrictions are regular, normalized, differential, and strictly iota-invariant. Classical overlap identifications are understood. Assume a literal associative algebroid presentation modulo h^4 is already given by

mu_i=m+h mu1+h² mu2+h³ mu3_i,
F_ij=id+h² T_ij,
A_ijk=1+h b_ijk+h² b_ijk²/2+h³(b_ijk³/6+c_ijk).

Here mu1={ , }/2, mu2 is common and symmetric, T_ij are derivations, and all third-order homomorphism, inner, and unit identities hold. The third coefficient may vary: it need not be a fixed Moyal product. Assume every local product has a specified invariant symmetric fourth coefficient mu4_i making it associative modulo h^5. In particular use the already proved explicit coefficient mu4_i=M4+N_i+K_i from the fourth-order-local-product theorem, with its disjoint-pair coefficient dependence. The new symbol K below denotes an overlap defect, not that local correction.

**Theorem.** There exist regular invariant normalized differential U_ij and regular invariant scalar e_ijk such that the unchanged prescribed local products, together with

F_ij=id+h² T_ij+h⁴ U_ij,
A_ijk=1+h b_ijk+h² b_ijk²/2+h³(b_ijk³/6+c_ijk)+h⁴ e_ijk,

satisfy all associative algebroid descent identities modulo h^5. Every displayed coefficient below order four is preserved literally. The theorem does not assert an explicit formula for U or e, a fixed-Moyal all-order extension, a module lift, or a period identification.

## 1. The order-four overlap equation and its sign

Write Delta mu_r=mu_r^j-mu_r^i and

d_H U(f,g)=fU(g)-U(fg)+U(f)g,
L_T mu2(f,g)=T(mu2(f,g))-mu2(Tf,g)-mu2(f,Tg).

Expanding F_ij(mu_j(f,g))=mu_i(F_ij f,F_ij g), its order-four left coefficient is

mu4_j(f,g)+T_ij(mu2(f,g))+U_ij(fg),

and its right coefficient is

mu4_i(f,g)+mu2(T_ij f,g)+mu2(f,T_ij g)+(T_ij f)(T_ij g)+(U_ij f)g+f(U_ij g).

Thus precisely

d_H U_ij=R_ij := Delta mu4+L_Tij mu2-(T_ij f)(T_ij g).                 (1)

The varying third coefficients enter the already satisfied order-three equation Delta mu3+L_T mu1=0; they do not enter (1). This calculation uses F3=0 literally. For nonzero prescribed F3=S, equation (1) would additionally contain L_S mu1 and its symmetry argument would need new justification.

R_ij is symmetric because mu4_i and mu2 are symmetric and multiplication is commutative. It is normalized. It is a Hochschild 2-cocycle: take the trial F=id+h²T, whose homomorphism defect begins at h⁴R; compare its values on the two associative parenthesizations of three inputs. Since the two products are associative and all lower homomorphism defects vanish, the h⁴ coefficient is d_H R=0. Only classical multiplication occurs in this coefficient, since h·h⁴=0 in the quotient.

For a smooth affine intersection, differential HKR identifies degree-two Hochschild cohomology with bivectors; the class of a 2-cocycle is represented by its antisymmetrization. Therefore a symmetric differential 2-cocycle has zero class. Consequently (1) has a regular normalized differential solution U on each intersection. This is an assertion in the normalized differential Hochschild complex; the primitive has finite differential order, without any uniform bound across orders being claimed. Averaging the primitive with iota preserves (1) and normalization. Hence choose invariant U and obtain genuine algebra homomorphisms through order four, with unchanged local products.

## 2. Exact fourth-order conjugation coefficient

For a triple suppress indices and write b=b_ijk, c=c_ijk, H_b={b,-}. The local third coefficient in this section is the target mu3_i, which is antisymmetric for the explicit product M3+rho_i/2. For a general third coefficient replace 2mu3_i(b,f) below by mu3_i(b,f)-mu3_i(f,b).

Set a=b²/2 and d=b³/6+c. Symmetry of mu2 gives

[A,f]_star=h²H_b f+h³H_a f+h⁴(2mu3_i(b,f)+H_d f).

The inverse through order two is A^{-1}=1-hb+h²(b²-a). Indeed mu1(b,b)=0. From Ad(A)f-f=[A,f]_star star A^{-1}, its fourth coefficient is

2mu3_i(b,f)+H_d f-bH_a f+(b²-a)H_b f-mu1(H_b f,b).

Using H_a=bH_b, H_d=(b²/2)H_b+H_c and antisymmetry of mu1, all ordinary b²H_b terms cancel, leaving

Ad(A)=id+h²H_b+h⁴J_ijk,
J_ijk(f)=2mu3_i(b,f)+{c,f}+(1/2)H_b²f.                            (2)

The order-three coefficient vanishes. The coefficient e of A has no effect on Ad(A) through order four: its classical commutator is zero and its first possible quantum commutator is order five. Formula (2) retains the prescribed third unit correction c; dropping it would generally change the fourth inner equation.

## 3. Inner defects are a closed derivation-valued cochain

Take e=0 for now and the U obtained above. Define K_ijk by

F_ij F_jk-Ad(A_ijk)F_ik=h⁴ K_ijk.

Equations (2) and the composition expansion give exactly

K_ijk=U_ij+U_jk-U_ik+T_ij T_jk-J_ijk-H_bijk T_ik.                 (3)

Every map on either side of the defining difference is an algebra homomorphism and the maps agree modulo h⁴. Subtracting their multiplicativity identities at order four shows

K_ijk(fg)=K_ijk(f)g+fK_ijk(g).

Thus K is a regular invariant derivation, not an arbitrary differential operator.

For completeness its Cech closedness does not assume the pending fourth unit equation. Define the scalar unit defect

P_ijkl=[h⁴](A_ijk star_i A_ikl-F_ij(A_jkl) star_i A_ijl).

It is defined because that equation holds modulo h⁴. Compare the two ways to compose F_ij F_jk F_kl. The contributions of the K terms give

K_ijk+K_ikl-K_jkl-K_ijl.

The remaining difference is between conjugation by A_ijk star A_ikl and conjugation by F_ij(A_jkl) star A_ijl. These units differ by h⁴P. Conjugation by their ratio 1+h⁴p is the identity modulo h⁵, because the classical algebra is commutative. Therefore

(delta K)_ijkl=K_jkl-K_ikl+K_ijl-K_ijk=0.                         (4)

Transport of leading defects by F or inner conjugations has no effect at this order, since those maps reduce to the identity. This justifies the untwisted Cech differential in (4).

For an abelian variety T_X is the trivial bundle with fiber V=H^0(T_X). Inversion acts as -1 on V and on W=H^1(O_X), so H²(T_X)=V tensor Lambda²W is entirely odd. Exactness of averaging and affine Cech acyclicity imply H²(Cech(T_X)^iota)=0. Choose an invariant derivation-valued 1-cochain v with delta v=-K. Replace U by U+v. Its Hochschild differential does not change; (1) remains true. Formula (3) changes K by delta v, so inner descent now holds exactly modulo h⁵. No mu4_i, T, b, or c was altered.

## 4. Scalar pentagon closedness and repair

With those corrected maps keep e=0 and define P as above. The P cochain is regular and invariant. To verify delta P=0 directly, use five increasing indices 0,1,2,3,4 and compare two reductions of A012 star A023 star A034. Replacing successive adjacent products by their unit equations yields, at the h⁴ coefficient,

P0234=-P0124+P1234+P0134+P0123,

hence

(delta P)01234=P1234-P0234+P0134-P0124+P0123=0.

Here is why no hidden transport terms remain: one reduction first replaces A023 A034; the other successively replaces A012 A023, A013 A034, A123 A134 and then A012 A024. Multiplicativity of F01 transports products, while the already repaired identity F01F12=Ad(A012)F02 identifies the middle expressions. Each P appears multiplied by units reducing to 1 and transported by maps reducing to the identity, so these factors do not change its leading h⁴ coefficient. Associativity removes parenthesis ambiguity. This proves the claimed five-index identity in the truncated algebra itself.

H³(O_X)=Lambda³W is entirely odd; hence its invariant part vanishes. The invariant affine Cech complex therefore supplies a regular invariant scalar 2-cochain e with delta e=P. Adding h⁴e to A changes its unit defect by

e_ijk+e_ikl-e_jkl-e_ijl=-(delta e)_ijkl.

Consequently the corrected defect is P-delta e=0. This change does not alter conjugation through order four and therefore retains the homomorphism and inner equations already solved. The U correction also never affected P through order four: U acts on the leading coefficient 1 of a triple unit, and U(1)=0; its first possible action on hb is order five.

All A remain invertible by their leading unit coefficient, all F remain invertible by their leading identity coefficient, and every correction is invariant and regular. This completes the proof.

## 5. Arity zero and precise limits

The classical Hochschild differential on an arity-zero function a is (d_H a)(f)=fa-af=0. This vanishing is exactly why a fourth scalar unit cannot repair an order-four inner derivation defect; that defect must instead be removed by v using H²(T_X)^iota=0. Arity zero must nevertheless be retained: its Cech differential repairs the pentagon, and H³(O_X)^iota is the relevant remaining obstruction. Quantum commutators of h⁴a begin only at h⁵, not at the current lifting order. No arity-zero term has been silently discarded.

The result depends essentially on: (a) genuine lower descent modulo h⁴, including the prescribed regular invariant c; (b) common symmetric mu2 and F3=0; (c) invariant associative symmetric mu4_i; (d) smooth affine intersections for differential HKR; (e) the two invariant Cech cohomology vanishings. Without (c), the exact first missing condition is [R_ij]=0 in differential HH² on each overlap; without either cohomology vanishing, the subsequent exact obstructions are [K] in H²(T_X)^iota and [P] in H³(O_X)^iota. No general assertion that arbitrary prescribed local products glue at all higher orders follows.

Sources used as already audited symbolic inputs:
- antecedent fourth-order-local-product / PROOF.md and AUDIT.md.
- antecedent third-order-automorphism-obstruction / PROOF.md.
- antecedent ambient-lifting-relative-moduli / PROOF.md and EXPLICIT_THIRD_ORDER_SOURCE_AUDIT.md.
- Public source identification: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260064519 .
