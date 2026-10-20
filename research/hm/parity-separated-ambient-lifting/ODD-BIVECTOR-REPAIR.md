# Odd local defects form a Cech bivector cocycle

## Result and distinction from fixed-product gluing

This is the next structural step after Theorem 4.1 of PROOF.md. It retains all that theorem's explicit regularity, associativity, reversal parity, even lower maps, reversal-unitary lower triple units, and geometric invariance hypotheses. N is odd. All products are associative modulo h^(N+1), and the literal lower descent is valid modulo h^N.

The fixed-product obstruction R_(N,ij) cannot be repaired by a new map coefficient. If, instead, the top local product coefficients are allowed to change by biderivations, its exact obstruction is a Cech cohomology class:

  [R_N] in H^1(X, wedge^2 T_X)^G.

In particular, on an inversion-equivariant abelian variety this class vanishes. Every supplied collection of associative parity local odd extensions can therefore be adjusted in its top coefficients only to admit the unchanged even overlap maps. If H^3(O_X)^G also vanishes, the scalar units can then be repaired and the entire odd ambient descent step completed. This does not construct the required local associative extensions and does not apply to immutable prescribed top products.

## 1. An inner identity before local multiplicativity is repaired

Let F be the zero order-N-coefficient lift of the lower even maps, and let A be any lift of the lower triple units. Lemma 2.1 of PROOF.md makes A reversal-unitary automatically at odd N. Consequently F_ij F_jk and Ad(A_ijk)F_ik are both even operators, whether or not F is yet multiplicative at the top order. Their equality holds below degree N by hypothesis. Since N is odd, it also holds in degree N:

  F_ij F_jk = Ad(A_ijk) F_ik modulo h^(N+1).                (1.1)

This deduction does not use a pending homomorphism identity. Ad(A_ijk) is a genuine automorphism of its target associative product because it is conjugation by a unit; F_ik may still have its leading defect.

## 2. Additivity of leading multiplicativity defects

For a map L from a source algebra to a target algebra define

  D_L(f,g)=L(f*_source g)-L(f)*_target L(g).

If F and G reduce to the identity and their defects start in degree N, then the exact identity

  D_(FG)(f,g)
   =F(D_G(f,g))+D_F(G(f),G(g))

implies, at its leading degree,

  [h^N]D_(FG)=R_G+R_F.                                    (2.1)

Only the classical reductions act on a leading h^N term. If H is an actual algebra automorphism reducing to the identity, similarly

  [h^N]D_(HG)=R_G.                                        (2.2)

Apply (2.1) to the left side of (1.1) and (2.2) to its right side. Equality of the maps implies equality of their multiplicativity defects, hence

  R_(N,ij)+R_(N,jk)=R_(N,ik).

Equivalently,

  (delta R_N)_ijk=R_(N,jk)-R_(N,ik)+R_(N,ij)=0.            (2.3)

By Theorem 4.1 each R_N is an actual biderivation, not only a Hochschild cohomology class. Thus (2.3) is an ordinary invariant Cech cocycle identity with coefficients in wedge^2 T_X.

## 3. Repair by top local bivectors

Change only the order-N local products by normalized biderivations B_i:

  mu_(N,i)'=mu_(N,i)+B_i.

These modifications preserve associativity to the stated precision because the only new associator term is the ordinary Hochschild differential d_H B_i=0. Since N is odd and B_i is antisymmetric, they preserve reversal parity. They do not affect any lower product, map, or unit coefficient.

The leading homomorphism defect changes by

  R_(N,ij)'=R_(N,ij)+B_j-B_i=R_(N,ij)+(delta B)_ij.         (3.1)

No positive-order map term acts on h^N B. Therefore the class [R_N] is necessary and sufficient for a repair of this specified kind. If it vanishes, choose invariant B with delta B=-R_N using affine Cech acyclicity and finite-group averaging. The unchanged maps become genuine algebra homomorphisms. The inner identity remains automatic by parity, now for the modified products and their reversal-unitary lifted units. The remaining scalar pentagon is the one from Theorem 4.1 and is repaired when its H^3(O)^G class vanishes.

Changing mu_N does not alter reversal-unitarity of the units at this precision: a normalized h^N bidifferential correction evaluated on A=1+O(h) and tau(A)=1+O(h) first contributes in degree N+2. Similarly its contribution to any unit conjugation starts beyond the present degree. These observations also verify directly that the literal lower unit data are retained.

## 4. Abelian inversion specialization

For an abelian variety, with V=H^0(T_X) and W=H^1(O_X),

  H^1(X,wedge^2 T_X)=wedge^2 V tensor W.

Geometric inversion fixes h, acts as -1 on V and on W, and hence acts as -1 on this group. Its invariant part is zero. It also acts as -1 on H^3(O_X)=wedge^3 W. Consequently the odd repair of Section 3 always exists under the explicit local extension hypotheses.

For N=5 after the canonical fourth-order theorem, the formula R_5 in PROOF.md is thus a closed invariant bivector-valued Cech 1-cochain. If fifth local coefficients may vary, choose B_i with B_j-B_i=-R_(5,ij) and replace mu_(5,i) by mu_(5,i)+B_i. This makes the exact fifth map equation hold without altering T, U, b, c, or the canonical fourth unit coefficient. The scalar fifth correction then exists by the invariant H^3(O) vanishing.

## 5. What this advances, and what it does not

The main proof identifies the literal fifth obstruction for fixed products. This addendum proves that, once associative parity fifth local extensions are available and their top coefficients may vary, the overlap obstruction is removable without changing the established even maps. Thus the next genuinely missing ambient input becomes the existence/construction of local associative parity fifth extensions of the fixed fourth products, not an additional unknown global overlap class.

This refines the distribution of the known unrestricted ambient lifting freedom. It is not another proof of the existing unrestricted all-orders HH^3-invariant vanishing result: it specifically preserves all lower data and the zero odd overlap coefficient, and confines the odd overlap repair to top local bivectors. No module, period, selected-source value, or six-condition vanishing is implied.
