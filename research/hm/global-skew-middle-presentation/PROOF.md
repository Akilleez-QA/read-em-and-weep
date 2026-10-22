# A complete global presentation of skew middle operators

## Scope

Over C let H=V direct-sum W have dimensions 5=3+2, let U have dimension two, and fix the determinant lines used by the monad. On P=P(H*) write x for the universal covector and

    F=ker(H O -> O(1)), K=Lambda^2 F=Omega^2(2), E=U tensor K.

The wedge pairing and the alternating form on U give a nondegenerate alternating pairing beta:E tensor E -> L, where L=det(U) tensor det(H) tensor O(-1). Fixed determinant trivializations identify L with O(-1); all formulas below retain these trivializations, rather than changing any channel scalar.

This note supplies a complete global linear presentation of determinant-skew middle operators E -> E(4), and a substantial vertex-preserving subfamily. It does not solve their coupled monad-source equations or prescribe their twelve ramification values. In particular it does not confuse the scalar interpolation theorem in PR675 with operator realization.

## 1. Honest global generators

For omega in U tensor Lambda^3 H, put p_omega=i_x omega. Then i_x p_omega=0 and p_omega is a section of E(1). For two such sections define

    T_(p,q)(eta)=p beta(q,eta)+q beta(p,eta).

The determinant inverse is understood in this formula. Since beta(q,eta) takes values in L(1)=O, T_(p,q) has twist one, not twist two. Both terms are K-valued. Direct expansion and alternation of beta give

    beta(T eta,zeta)+beta(eta,T zeta)=0.

Thus each cubic polynomial c(x) times T_(p,q) is an actual global determinant-skew map E -> E(4). No formal exterior-space operator is being asserted to preserve K without checking it.

The bundle of skew endomorphisms identifies with Sym^2(E) tensor L^(-1). Consequently

    sp(E)(4) = Sym^2(E(1))(3)

after the fixed determinant-line identification.

## 2. Complete global presentation, including every relation

Let G_i=U tensor Lambda^(3+i) H, for i=0,1,2, with dimensions 20,10,2. The Koszul complex of the universal nonzero covector gives

    0 -> G_2 O(-2) -> G_1 O(-1) -> G_0 O -> E(1) -> 0.  (1)

The differentials are contraction with x. Form the graded symmetric square of this locally free resolution: degree-one generators are odd, degree-zero and degree-two generators even, and the differential follows the graded Leibniz rule. In characteristic zero this is an exact resolution of Sym^2 E(1). Indeed (1) locally splits as its degree-zero cohomology plus contractible complexes, and their graded symmetric square has precisely that cohomology. Twisting by three yields

    0 -> Sym^2 G_2 O(-1)
      -> G_2 tensor G_1 O
      -> (Lambda^2 G_1 direct-sum G_2 tensor G_0) O(1)
      -> G_1 tensor G_0 O(2)
      -> Sym^2 G_0 O(3)
      -> sp(E)(4) -> 0.                            (2)

Every line bundle appearing in (2) is acyclic in positive cohomological degrees on P4, including O(-1), which has no cohomology at all. Taking global sections therefore gives an exact presentation, with all higher relations, not merely a generating family:

    0 -> C^20 -> C^425 -> C^3000 -> C^7350
      -> H0(P,sp(E)(4)) -> 0.                      (3)

Thus the dimension of the unrestricted global operator space is

    7350-3000+425-20 = 4755.

The final surjection is precisely the cubic-weighted transvection construction of section 1. Its kernel has dimension 2595 and is exactly the image of the preceding Koszul-Leibniz map. This is a complete ansatz: omitting complementary mixed-to-VV coefficients is an additional restriction, not a consequence of globality or determinant skewness. All dimensions follow from universal bundles; no actual coefficient matrix or rank is evaluated.

For a finite symmetry group respecting the determinant markings, (1)-(3) are equivariant. Taking invariants remains exact by averaging. This gives a complete invariant presentation too, but does not assert that arbitrary prescribed invariant source-parameter data have compatible preimages under the further monad equations.

## 3. Exact vertex restriction

Let Z=P(W*) be the entire negative vertex line. Along Z,

    F|Z=V O direct-sum det(W) O(-1),
    E(1)|Z=(U tensor Lambda^2 V) O(1)
             direct-sum (U tensor V tensor det(W)) O.

Both constant factors have dimension six. Restriction of G_0 onto H0(Z,E(1)|Z) is onto: the U tensor Lambda^2 V tensor W summand contracts to the first summand and the U tensor V tensor Lambda^2 W summand to the second; its kernel is U tensor Lambda^3 V. Cubic polynomials on P restrict onto cubic polynomials on Z. Multiplication of binary forms is onto in every nonnegative degree, so the transvection presentation proves that restriction is onto:

    H0(P,sp(E)(4)) -> H0(Z,sp(E)(4)|Z).

The three symmetric-square blocks on Z are O(5)^21, O(4)^36, O(3)^21. Hence the target has dimension

    21*6+36*5+21*4=390,

and the space of global twist-four operators vanishing along Z has dimension 4365. This identifies the exact global freedom available after imposing a specified vertex middle-operator value, if that value has been fixed. It does not identify vanishing of an operator with vanishing of an entire cochain defect.

## 4. Vertex-cubic vanishing does not force a ramification zero

There is a stronger useful subfamily: take c in H0(I_Z^3(3)), namely any cubic in the positive coordinates alone, and multiply the transvections of section 1 by c. Every such operator vanishes to order at least three along Z.

At any x=(v,w) with v and w both nonzero, these operators span the entire fiber sp(E)_x tensor O(4)_x. Indeed contractions of constant three-forms span E(1)_x by the Koszul surjection; symmetric transvections span the symplectic Lie algebra; and some positive cubic c is nonzero at x. This is a surjectivity statement of sheaves on the complement of the positive-coordinate zero locus, not an evaluated rank computation.

For completeness, for any nonzero Y in E_x and any nonzero linear functional ell on E_x, the functional T -> ell(TY) is nonzero on sp(E_x). Choose p with ell(p) and beta(p,Y) both nonzero; two proper linear hyperplanes cannot cover a complex vector space. Then the diagonal transvection gives ell(T_(p,p)Y)=2 ell(p) beta(p,Y), which is nonzero.

At a distinguished ramification input, the actual lambda-Cartan-VV functional on E_x is nonzero. To check this intrinsically, take any positive two-form alpha and any e in W with w(e)=1. The expression alpha-e wedge i_v alpha lies in K_x and projects to alpha in the VV sector. Therefore the VV projection K_x -> Lambda^2 V is onto; tensoring with U and applying the nonzero Cartan quotient functional preserves the asserted nonzeroness. The actual shared input Y is nonzero: it is the fiberwise injective left monad subbundle arrow applied to the source vector with components -u/a_m and z/c_m. This source vector is nonzero because z(w) is nonzero. Here the full U arrow is a_m A+b_m B and the full quadratic-source arrow is c_m C; their pinned nonzero channel scalars are retained.

More generally, for any finite set of such physical points and nonzero input/functionals at them, there is one operator in the vertex-cubic-vanishing subfamily with all these scalar evaluations nonzero. For each point the zero condition is a proper linear hyperplane in this finite-dimensional global family. A finite union of proper linear subspaces cannot exhaust it.

This last assertion is nonvanishing, not independent interpolation. In applying it to the twelve ramification pairs one must fix the relative positive/negative scalings, or equivalently physical points on their joining lines. The assertion holds for every such finite choice but does not make a canonical choice or assert nonvanishing along each entire joining line. The operator need not be equivariant or have the source-parameter weights of a desired correction. No actual point or coefficient is chosen or evaluated in this argument.

## 5. What dependency is now isolated

The full global twist-four skew ansatz is (3); the vertex restriction is surjective with the exact kernel dimension above; and even third-order vertex vanishing leaves no pointwise symplectic/K-valued obstruction to the required mixed functional. Consequently failure of the negative-wedge lifts to change the ramification value is a property of that filtered family, not a universal restriction on global K-preserving determinant-skew middle operators before imposing the coupled monad-source equations.

What remains is the image of this explicitly presented global space under the simultaneous, correctly weighted ramification functional together with the two monad-arrow/source equations. Neither scalar interpolation nor fiberwise surjectivity establishes that image. This note supplies no full primitive, no value of the fourth Bockstein, no higher-order lift, and no algebraicity claim.

## Public dependencies

- [PR675 scalar interpolation](https://github.com/Akilleez-QA/read-em-and-weep/blob/14aa94109bd251bc5921038142a4ea95fe605202/research/hm/ramification-interpolation/PROOF.md): scalar interpolation and its explicit limitations.
- [Actual nonzero mixed middle value](https://github.com/Akilleez-QA/read-em-and-weep/blob/f7071d29886c83151028576bf32e001c347cafc9/research/hm/order-four-quadratic-load/ACTUAL-RAMIFICATION-DETECTS-A-NONZERO-MIXED-FORM-MIDDLE-VALUE.md): distinguished nonzero mixed input and forced functional.
- [Full six-space vertex correction](https://github.com/Akilleez-QA/read-em-and-weep/blob/0b55b84466c62c24f05f7e691f3e7a3d528b7ebf/research/hm/order-four-quadratic-load/FULL-SIX-SPACE-SKEW-LIFT-CANCELS-THE-VERTEX-RESIDUAL.md): vertex correction and negative-wedge filtration exclusion.

Run `python verify.py` for bounded universal contraction-squared, transvection-skewness, Koszul-square dimension, and vertex-dimension checks. The script does not check the geometric exactness argument or full monad-arrow equations. Status: geometric proof with independent review and the indicated elementary checks, not proof-assistant formalization. No selected actual HM/source-instance evaluation is used.
