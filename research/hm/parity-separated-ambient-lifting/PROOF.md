# Parity-separated ambient lifting and canonical fourth-order triple units

## 0. Result, inputs, and scope

This is a new universal formal-geometric step beyond fourth-order-global-gluing. It gives:

1. An even-order ambient lifting theorem in which the scalar pentagon obstruction disappears by reversal parity; no H^3(O) vanishing is needed at an even lifting order.
2. A canonical explicit fourth scalar unit coefficient

   e = b^4/24 + b c + (1/2) mu_2(b,b),

   replacing the existential e of the antecedent fourth-order theorem, with every coefficient below degree four unchanged.
3. The complementary odd-order gate: with prescribed parity products and fixed even lower overlap maps, the local homomorphism defect is an actual bivector that must vanish, not a defect repairable by a new map coefficient. If it vanishes, inner descent is automatic at the odd order and only the scalar H^3(O) obstruction remains.
4. The exact fifth-order local equation for the antecedent data, and a structural counterexample showing that arbitrary parity-preserving fifth products cannot be glued while preserving the lower maps.

The two involutions in the proof are different. The geometric group action, in the application inversion iota=[-1], fixes h. Formal reversal tau fixes ordinary functions and sends h to -h; it is an anti-automorphism of each parity star algebra. No complex conjugation, positivity, or metric is meant by the word unitary.

This is an ambient algebroid statement. It is not a module lift, a period identification, a solution of the six pure diagonal conditions, or an all-orders construction of local products or maps. No selected HM/source-instance function, module, physical matrix, retained detector, or jet is evaluated. The only computations are universal cochain identities.

The mathematical antecedents are the [fixed fourth-order global-gluing theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/1dfcd736ed29bee9467e8ff822f383156097f648/research/hm/bounded-ambient-deformations/fourth-order-global-gluing/PROOF.md) and the [regular third-order ambient construction](https://github.com/Akilleez-QA/read-em-and-weep/blob/2f4427fcec1b807cfdacacdbe8525fbc516c2f86/research/hm/null-order-three-ambient/third-order/RESULT.md). The [current first-star boundary](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6286052567) and the separate pure diagonal six-condition problem are unchanged. The result strengthens the fourth-order scalar conclusion and supplies a parity-separated induction criterion; it does not assert exhaustive literature novelty.

## 1. Formal setting and literal lower data

Let X be a smooth separated scheme over a characteristic-zero field k. Fix an affine cover with affine finite intersections, and a finite group G preserving each indexed open set. Work in the regular normalized differential Hochschild and ordinary Cech complexes. All data and restriction maps below are strictly G-invariant. The same argument works in an explicitly fixed G-equivariant acyclic model with the stated cohomology identifications.

Fix N >= 2 and put R_N=k[h]/(h^(N+1)). On each open U_i prescribe a unital associative differential product

  f *_i g = sum_(r=0)^N h^r mu_(r,i)(f,g),  mu_(0,i)(f,g)=fg,

satisfying reversal parity

  mu_(r,i)(g,f)=(-1)^r mu_(r,i)(f,g).                         (1.1)

For r>0 each mu_r is normalized. Thus the k-linear involution

  tau(sum h^r f_r)=sum (-h)^r f_r

is an anti-automorphism: tau(a *_i b)=tau(b) *_i tau(a).

Assume genuine literal descent is already given modulo h^N:

  F_ij : (O_j,*_j) -> (O_i,*_i),     F_ij=id+sum_(1<=r<N) h^r F_(r,ij),
  A_ijk=1+sum_(1<=r<N) h^r a_(r,ijk),

with F unital and differential, and

  F_ij F_jk = Ad_i(A_ijk) F_ik,
  A_ijk *_i A_ikl = F_ij(A_jkl) *_i A_ijl.                   (1.2)

Classical identifications on intersections are understood. In addition require

  F_(r,ij)=0 for every odd r<N,                             (1.3)
  tau(A_ijk)=A_ijk^(-1) modulo h^N.                        (1.4)

Condition (1.4) is essential and is not implied by geometric invariance. We call it reversal-unitarity. It will be checked, rather than presumed, for the fourth-order application.

All statements preserve the specified local products and every literal map/unit coefficient of degree <N. A lift of F with only an even new coefficient still satisfies tau F=F tau.

## 2. Two elementary parity lemmas

### Lemma 2.1. Lifting reversal-unitarity

Let A_hat be any lift to R_N of a lower reversal-unitary element with A_0=1. Its norm defect is

  tau(A_hat) * A_hat = 1+h^N c.

If N is odd, c=0 automatically and every top scalar coefficient gives a reversal-unitary lift. If N is even, there is a unique top scalar correction h^N e making the lift reversal-unitary, namely e=-c/2.

Proof. Applying tau to the norm gives

  tau(tau(A_hat) * A_hat)=tau(A_hat) * A_hat,

because tau is anti-multiplicative and tau^2=id. Since the lower norm is 1, the leading coefficient obeys (-1)^N c=c. Hence c=0 at odd N. Replacing A_hat by A_hat+h^N e changes the norm, to this precision, by

  h^N ((-1)^N+1)e,

since both lower constant factors equal 1. At even N this is 2h^N e, proving existence and uniqueness. All operations are regular and G-equivariant. Since A is invertible, norm 1 is equivalent to tau(A)=A^(-1). QED.

### Lemma 2.2. Products, homomorphisms, and adjoints

Products and inverses of reversal-unitary elements are reversal-unitary. An even unital algebra homomorphism preserves reversal-unitarity. The inner automorphism Ad(A) of a reversal-unitary element is an even differential operator.

Proof. If tau(A)=A^(-1) and tau(B)=B^(-1), then

  tau(A*B)=B^(-1)*A^(-1)=(A*B)^(-1).

The inverse claim follows by applying tau to A*A^(-1)=1. If F commutes with tau and is a unital algebra homomorphism, then tau(F(A))=F(tau(A))=F(A)^(-1). Finally

  tau Ad(A) tau(f)
   =tau(A^(-1))*f*tau(A)
   =A*f*A^(-1)=Ad(A)(f).

Commutation with tau is exactly vanishing of all odd operator coefficients in characteristic zero. QED.

An important consequence is that two reversal-unitary elements M,Q agreeing modulo h^N cannot first differ at an even N. Indeed C=M*Q^(-1)=1+h^N p is reversal-unitary, so (-1)^N p=-p; for even N, p=0. The argument does not require M and Q to commute. Their leading ratio is central to this precision, but no exact centrality is assumed.

## 3. General even-order lifting theorem

**Theorem 3.1.** Suppose N is even, the hypotheses of Section 1 hold, and

  H^2(X,T_X)^G=0.                                         (3.1)

Then the fixed prescribed local products admit a G-invariant reversal-compatible descent lift to R_N with even F and reversal-unitary A, preserving all literal lower coefficients. No hypothesis on H^3(X,O_X)^G is required. The top coefficient of each A is the unique reversal-unitary lift given by Lemma 2.1.

Proof.

### 3a. The local homomorphism defect is symmetric and exact

Take the zero top-coefficient lift F_hat of a lower F. Let

  D_ij(f,g)=F_hat(mu_j(f,g))-mu_i(F_hat f,F_hat g)
          =h^N R_ij(f,g).

The equality on the right uses the given lower homomorphism identity. Parity of mu and evenness of F imply

  R_ij(g,f)=(-1)^N R_ij(f,g)=R_ij(f,g).                     (3.2)

Compare the defect on the two associative parenthesizations of three inputs. Every contribution involving a positive-order product or a nonidentity lower map times h^N vanishes modulo h^(N+1), leaving precisely d_H R=0. This is the usual leading multiplicativity-defect identity, here in the ordinary commutative normalized differential Hochschild complex.

On every smooth affine intersection, differential HKR identifies HH^2 with bivectors and takes a cocycle class to its antisymmetric part. Thus the symmetric normalized differential cocycle R has zero class. Choose a normalized regular differential U with d_H U=R, where

  d_H U(f,g)=fU(g)-U(fg)+U(f)g.

Replacing F_hat by F_hat+h^N U changes D to h^N(R-d_H U)=0. Average U over G; the equation, regularity and normalization are preserved. Since N is even, the corrected F remains even and hence commutes with tau. Its leading identity makes it invertible.

### 3b. Normalize the units and eliminate the pentagon defect by parity

Choose the unique reversal-unitary lifts of all A by Lemma 2.1. This top correction cannot affect any inner automorphism at degree N: the ratio of two such lifts is 1+h^N a, and

  Ad(1+h^N a)=id modulo h^(N+1),

because ordinary functions commute and the quantum commutator has at least one extra h.

For four indices set

  M=A_ijk *_i A_ikl,
  Q=F_ij(A_jkl) *_i A_ijl.

Both M and Q are reversal-unitary by Lemma 2.2, since the F just constructed are even algebra homomorphisms. They agree modulo h^N by the lower pentagon. As N is even, the consequence following Lemma 2.2 yields M=Q in R_N. The scalar pentagon is therefore already exact, without a five-index calculation or scalar cohomology vanishing.

### 3c. The sole global obstruction is the derivation class

Define K_ijk by

  F_ij F_jk-Ad(A_ijk) F_ik=h^N K_ijk.

Both maps are algebra homomorphisms agreeing below degree N. Subtracting their multiplicativity equations shows

  K_ijk(fg)=K_ijk(f)g+f K_ijk(g).

Thus K is a regular invariant derivation-valued Cech 2-cochain. Compare the two bracketings of F_ij F_jk F_kl. Use the exact scalar pentagon of 3b to identify the corresponding inner conjugations. Transporting a leading h^N K by a map or a unit with classical identity does not change its coefficient. Consequently

  (delta K)_ijkl=K_jkl-K_ikl+K_ijl-K_ijk=0.

For clarity, this closedness would also hold with only the lower scalar pentagon: a pending unit ratio 1+h^N p has trivial adjoint modulo h^(N+1). It does not use the desired inner identity circularly.

By (3.1), affine Cech acyclicity and exactness of finite-group averaging, there is an invariant derivation-valued 1-cochain v with delta v=-K. Replace F_N by F_N+v. Its Hochschild differential is unchanged, so it remains a homomorphism; it remains even. K changes by delta v and vanishes.

The change in F has no effect on the scalar pentagon at degree N: its new term acts on A_jkl=1+O(h), and v(1)=0. Alternatively the parity argument of 3b applies again. All local products and all coefficients of degree <N remain literal. QED.

Without (3.1), [K] in H^2(T_X)^G is the exact remaining obstruction for this step after local maps have been solved; the scalar obstruction is still identically absent under reversal-unitarity.

## 4. Complementary odd-order gate

**Theorem 4.1.** Suppose N is odd and the hypotheses of Section 1 hold. Define the leading local homomorphism defects R_ij using the unchanged lower even maps, with the order-N map coefficient zero.

(a) Every R_ij is an antisymmetric differential Hochschild 2-cocycle and hence an actual biderivation. A descent lift preserving the prescribed products and all lower maps can exist only if every R_ij=0. Adding an arbitrary new order-N differential map coefficient cannot repair a nonzero R_ij.

(b) If every R_ij=0, keep F_N=0. Every lift of the A is reversal-unitary, and the inner equation is automatic through degree N. For this reversal-compatible lifting problem with the even maps fixed, so F_N=0, the remaining exact obstruction is the scalar class [P] in H^3(X,O_X)^G. In particular, if H^3(X,O_X)^G=0 there is an invariant reversal-compatible descent lift preserving all lower coefficients. This is not a classification of unrestricted odd-coefficient map choices.

Proof. The associativity argument from 3a again gives d_H R=0, while parity gives R(g,f)=-R(f,g). An antisymmetric Hochschild 2-cocycle over a commutative characteristic-zero algebra is a biderivation: the three cocycle equations on cyclic permutations of (f,g,k), together with antisymmetry, give R(fg,k)=fR(g,k)+gR(f,k). Antisymmetry gives the other Leibniz rule. This is a cochain identity, stronger than merely identifying its HKR class.

For any linear operator V, d_H V is symmetric in f,g. Thus an equation d_H V=R with R antisymmetric forces both sides to be zero. This proves (a), even if an odd map coefficient were allowed.

For (b), R=0 makes the unchanged even F a genuine algebra homomorphism in R_N. By Lemma 2.1 an arbitrary lift of each A is reversal-unitary. Both F_ij F_jk and Ad(A_ijk)F_ik are therefore even operators by Lemma 2.2. They agree modulo h^N, so their first possible coefficient of odd degree N vanishes. Inner descent follows without any H^2(T) correction.

Set

  P_ijkl=[h^N](A_ijk*A_ikl-F_ij(A_jkl)*A_ijl).

The now-valid homomorphism and inner equations and associativity imply delta P=0 by the five-index reassociation calculation. Explicitly, comparing two reductions of A_012*A_023*A_034 gives

  P_0234=-P_0124+P_1234+P_0134+P_0123,

which is delta P=0. Leading h^N defects see only classical identity maps and unit constants, so no twisted transport appears.

Adding h^N e_ijk to A changes P to P-delta e. It does not change the inner equation, by the one-order commutator delay, and at odd N it preserves reversal-unitarity by Lemma 2.1. Thus [P]=0 is necessary and sufficient for the remaining correction. If H^3(O)^G=0, an invariant primitive exists by averaging. QED.

For a complex abelian variety with G generated by geometric inversion, T_X=V tensor O_X, inversion is -1 on V and W=H^1(O_X), and hence H^2(T_X)=V tensor wedge^2 W and H^3(O_X)=wedge^3 W are both inversion-odd. Their invariant parts vanish. Under the explicit local associativity, parity, lower even-map and reversal-unitarity hypotheses, all even steps therefore exist; each odd step is controlled solely by the literal local equations R_ij=0. This is not an all-orders theorem: those odd equations and the prescribed local associative products have not been constructed here.

## 5. Fourth-order specialization: the scalar coefficient is explicit

Use the antecedent hypotheses exactly: mu_1={,}/2 is antisymmetric, mu_2 is common and symmetric, mu_(3,i) is antisymmetric, mu_(4,i) is symmetric, and the products are associative modulo h^5. The given lower maps are F=id+h^2 T. The triple units are

  A=1+h b+h^2 a+h^3 d,    a=b^2/2,    d=b^3/6+c.

They are reversal-unitary modulo h^4. Indeed ordinary terms cancel through degree three in tau(A)*A. The only possible degree-three differential term is -mu_1(b,b), which vanishes by antisymmetry; normalized operators vanish when another argument is 1. No condition on c beyond the already supplied genuine lower descent is needed for this norm statement.

Adjoin h^4 e. Its fourth norm coefficient is

  [h^4](tau(A)*A-1)
   =2e+a^2-2bd-mu_2(b,b)+mu_1(a,b)-mu_1(b,a)
   =2e+a^2-2bd-mu_2(b,b).

The last equality uses a=b^2/2 and the biderivation property of mu_1={,}/2. Since a^2-2bd=-b^4/12-2bc, the unique normalized choice is

  e=b^4/24+b c+(1/2)mu_2(b,b).                             (5.1)

Formula (5.1) is regular and invariant. The general theorem supplies the same kind of invariant differential U and derivation correction used in the antecedent, but now the scalar coefficient is fixed explicitly and its pentagon is forced by reversal. No H^3(O)^iota is used at degree four. The lower c remains existential exactly as in null115; (5.1) is an explicit expression in that supplied c, not a computation of c.

This does not assert that every scalar e supplied by the earlier existential proof was already reversal-unitary. It proves that the canonical e in (5.1) can be chosen instead, preserves every lower coefficient, and has all the desired fourth-order identities. Its difference from another fourth-order solution is a scalar Cech 2-cocycle; no uniqueness beyond the reversal-unitary normalization is claimed.

## 6. The exact fifth-order local obstruction

After Section 5 fix a particular obtained U and the canonical e. Suppose, as an additional input not proved here, that each local product has a specified antisymmetric mu_(5,i) making it associative modulo h^6. Write mu_1 for the common first coefficient. With

  F_ij=id+h^2 T_ij+h^4 U_ij,

the exact fifth homomorphism defect is

  R_(5,ij)(f,g)
   = mu_(5,j)(f,g)-mu_(5,i)(f,g)
     +T_ij(mu_(3,j)(f,g))
     -mu_(3,i)(T_ij f,g)-mu_(3,i)(f,T_ij g)
     +U_ij(mu_1(f,g))
     -mu_1(U_ij f,g)-mu_1(f,U_ij g)
     -mu_1(T_ij f,T_ij g).                                (6.1)

Derivation: the left homomorphism coefficient is mu_(5,j)+T mu_(3,j)+U mu_1. The right coefficient is mu_(5,i), the two mu_3 terms with one T, the two mu_1 terms with one U, and mu_1(Tf,Tg). No mu_2 or mu_4 terms occur because every map correction has even degree; any hypothetical F_5 contributes only -d_H F_5 to the defect. This also fixes the sign in (6.1).

By Theorem 4.1, R_5 is a regular invariant biderivation, and

  R_(5,ij)=0 on every overlap                              (6.2)

is necessary and sufficient for these fixed lower maps to be algebra maps at order five. If (6.2) holds, the odd inner equation is automatic. On the invariant abelian cover the remaining scalar fifth pentagon has a regular invariant primitive by H^3(O)^iota=0. Hence the supplied fixed parity fifth products have a fifth ambient extension with the same even maps if and only if (6.2) holds. The coefficient of the fifth triple unit is existential; no value is evaluated.

If a lower fourth map coefficient is deliberately changed by a derivation v, then the change in (6.1) is exactly L_v mu_1. Such a change preserves fourth inner descent precisely when delta v=0 (all other fourth data fixed). If the prescribed fifth product is instead changed by a biderivation B_i, the change in R_5 is B_j-B_i. These observations describe actual allowed repair directions; they are not a proof that a repair exists. In particular one cannot invoke a new F_5 to remove a nonzero R_5.

## 7. Structural exclusion of automatic arbitrary fifth-product gluing

The odd obstruction is not a merely formal warning. On an abelian variety of dimension at least two with the assumed invariant affine cover, choose a nonzero translation-invariant bivector B and a common invariant commuting-field Moyal product. Use lower F=id and A=1. These give genuine parity and reversal-unitary descent through order four. Prescribe Moyal coefficients through order five on one chart and replace mu_5 by mu_5+B on a second intersecting chart.

B is a normalized antisymmetric Hochschild 2-cocycle. Adding h^5 B preserves associativity modulo h^6 because its only contribution at this precision is d_H B=0. It preserves reversal parity and geometric inversion invariance. Thus every local hypothesis for a prescribed fifth parity product is satisfied.

Nevertheless, on that overlap (6.1) is R_5=B, which is nonzero. No order-five map correction can repair it while preserving all lower maps, because d_H F_5 is symmetric. This supplies a universal geometric exclusion of an unconditional fixed-product all-orders corollary. It does not evaluate the designated HM source or claim that its specific R_5 is nonzero. It also does not exclude repairs by changing the already fixed fourth maps or the prescribed fifth products.

## 8. Contribution and remaining frontier

The existing fourth-order theorem proved scalar solvability cohomologically. The new canonical reversal normalization computes its top scalar coefficient and shows why the even scalar obstruction is absent before any H^3 calculation. The general proof separates the obstruction tower by parity rather than repeating the fourth-order expansion at every even order.

The immediate next missing ambient dependency is now exact: provide associative antisymmetric fifth local coefficients and prove (6.2), possibly using the explicitly identified lower-map/product repair directions. Neither geometric inversion alone nor the even-order theorem provides that proof. Module lifting and the pure diagonal six-condition problem are unchanged.

If the top odd local products may vary, the companion ODD-BIVECTOR-REPAIR.md proves that the R_5 cochain is closed and that invariant bivector corrections remove it. In that variant, the next missing input is the local associative parity fifth extension itself.
