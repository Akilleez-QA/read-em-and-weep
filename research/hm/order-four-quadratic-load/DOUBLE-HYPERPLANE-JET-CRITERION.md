# A first-normal-jet criterion for square quadratic residuals

## Statement

Let C be the union of the 25 disjoint HM lines, let H=V(ell) contain no component line, and put Z=C intersect H. Thus Z consists of 25 distinct reduced points. Retain I_C(1)=I_C(2)=I_C(3)=0 on global sections and M_d=H^1(I_C(d)). Set

    A=H^0(I_(Z,H)(2)),  V=H^0(I_(Z,H)(3)),  a=dim A.

There is a canonical first-normal-jet obstruction map (relative to the equation ell)

    j_H : V -> H^0(O_Z(2))/eval H^0(O_H(2)).

Its target has dimension 15+a. It admits a direct description using restrictions to the component lines, without constructing M_2 or its intersecting subspaces. There is an exact sequence

    0 -> A -> ker(ell^2:M_1 -> M_3) -> ker j_H -> 0.       (1)

Consequently ell^2 is an injective Rao multiplier, equivalently gives the corresponding quadratic residual surjectivity, if and only if A=0 and j_H is injective.

Writing b=dim V, the exact defect is

    dim ker(ell^2)=a+b-rank(j_H),

so the automatic dimension bound is max(a,b-15).

In addition, the section cubics vanishing to second order at all points of Z lie in ker j_H. Hence

    dim ker(ell^2:M_1 -> M_3)
      >= a + h^0(I_(Z,H)^2(3)).                          (2)

Here the squared ideal is the sheaf ideal of the doubled reduced points in H. This is a first-jet obstruction, not an assertion that such a cubic exists for the HM section.

## 1. The map as a quotient of linewise normal derivatives

For f in V choose any ambient cubic lift F in H^0(O_P4(3)). On each component L of C, the section F|L vanishes at p=L intersect H. Since ell|L has a simple zero at p, there is a unique quadratic section g_L on L such that

    F|L = ell|L times g_L.

The values g_L(p), for all 25 lines, give a section g|Z of O_Z(2). Define j_H(f) to be its class modulo evaluated quadrics on H.

This is independent of the lift. Any other lift is F+ell G for an ambient quadric G, and changes g|Z by G|Z. Every quadric on H extends to P4, so the ambiguity is exactly the stated evaluation subspace. Rescaling ell rescales j_H and has no effect on its kernel. No line, cubic, coefficient, or rank is selected for evaluation in this construction.

Since H=P3, H^1(O_H(2))=0. The target is canonically H^1(I_(Z,H)(2)), and its dimension is 25-(10-a)=15+a.

## 2. Why the obstruction is precisely the double-hyperplane extension

Write Q=2H and D=C intersect Q, scheme-theoretically. The scheme D consists of length-two points directed along the original component lines. There is an exact sequence of sheaves supported on Q:

    0 -> I_(Z,H)(2) --ell--> I_(D,Q)(3)
      -> I_(Z,H)(3) -> 0.                               (3)

For a local proof choose ell as the normal parameter. The local ring of D is the ring of the corresponding smooth component line modulo ell^2. A function on Q reducing to zero on Z can be adjusted by ell times a function to vanish on D, because its residual value on D is ell times a value at the reduced point. Thus restriction onto I_(Z,H) is locally surjective. A function in the kernel is ell times g; it vanishes on D exactly when g vanishes on Z. This identifies the kernel with I_(Z,H)(-1) before twisting and proves (3). Away from Z the claim reduces to the usual double-hyperplane sequence.

The connecting homomorphism of (3) is, up to a fixed sign, j_H. Indeed a cubic lift F vanishes on D after subtracting ell G exactly when its linewise quotient values g|Z are evaluated by a quadric G. This is exactly the obstruction class above.

Since ell^2 is a nonzerodivisor on O_C, ideal restriction also gives

    0 -> I_C(1) --ell^2--> I_C(3) -> I_(D,Q)(3) -> 0.

The vanishing of the two global ideal spaces identifies H^0(I_(D,Q)(3)) with ker(ell^2:M_1->M_3). Taking cohomology of (3) now proves (1).

This replaces the earlier intersection kappa_H(V) intersect ell M_1 with an actual first-jet map between explicit section and evaluation-quotient spaces. It is not permissible to choose that map freely or infer its rank from its dimensions.

### Identification with the existing actual Rao module

Let kappa_H:V -> M_2 be the connecting injection from

    0 -> I_C(2) --ell--> I_C(3) -> I_(Z,H)(3) -> 0.

Let rho:M_2 -> H^1(I_(Z,H)(2)) be restriction from the degree-two sequence. Because H^2(I_C(1))=H^1(O_C(1))=0 for the disjoint union of lines, the same sequence gives a canonical identification

    coker(ell:M_1 -> M_2) = H^1(I_(Z,H)(2)).

Then j_H=rho composed with kappa_H, up to the uniform sign convention for connecting homomorphisms. This can be checked on local lifts: the boundary kappa_H is represented by the linewise quotient F|C divided by ell, and rho takes precisely its values on Z modulo evaluated quadrics. It also follows from the natural diagram relating the two successive ell restriction sequences to the ell^2 sequence. Therefore the jet map is the obstruction in the existing actual Rao module, not an additional assumed multiplication model.

## 3. Intrinsic directional-derivative interpretation

Choose a projective linear retraction toward H, defined near Z, by choosing a center outside H. It gives a splitting of the tangent-normal sequence along H. For each line L through p in Z, identify its normal tangent with N_(H/P4)|p using the nonzero derivative of ell along L. The difference between that tangent and the chosen normal splitting gives

    nu_p in T_H(-1)|p.

Together these form nu in H^0(T_H(-1)|Z). Because f vanishes on Z, its differential at those points is intrinsically defined as a section of Omega_H^1(3)|Z. The jet obstruction is the class of

    contraction(nu, df|Z) in H^0(O_Z(2))

modulo evaluated quadrics, up to the fixed normal-sign convention. One verifies this by lifting f using the chosen retraction and differentiating its restriction to L at p.

Changing the normal splitting changes nu by the restriction of a global section of T_H(-1). Its contraction with df is a global quadratic on H, so the quotient class is unchanged. This explains geometrically why the obstruction depends on the embedded first-order directions of the 25 lines, not only on the reduced configuration Z.

If f vanishes to second order at every point of Z, then df|Z=0, so j_H(f)=0. This proves (2). This lower bound is useful on strata with section quadrics, but is not an independent obstruction when A=0: the four first partial derivatives of a cubic singular at Z are quadrics vanishing on Z, so A=0 forces all derivatives, and hence the cubic, to vanish in characteristic zero.

## 4. Scope and exact remaining premise

The double-section D records first-order motion normal to H along the actual lines. It should not be confused with arbitrary first-order deformation of a cubic on a moving hyperplane: that different deformation problem may allow cubic correction terms, while the present obstruction quotients only by quadratic corrections F -> F+ell G. No equivalence to such a larger deformation problem is asserted. Nor is a limit of intersections of trace spaces claimed: such a statement would require separate flatness and base-change control.

The remaining sufficient premise is now explicit: find a proper H with A=0 and injective first-normal-jet map j_H. Neither injectivity nor even one suitable H is proved. This does not certify full quadratic adjoint invertibility, the 20-dimensional lift boundary, the original selected coefficients, or Q4 vanishing.

Current PR1 was read through its latest coordination entry, dated 2026-10-21 05:30:44 UTC, before this deduction. PR543 was read at head f4e61e37e8be9ad32936baa7c69a3433efdc8c2a, including its PLANE-TRACE-CRITERION.md content. The new result refines its repeated-linear intersection criterion by the double-hyperplane ideal extension and the explicit normal-jet quotient, and adds the doubled-point cubic obstruction. No experiment or public action was performed.
