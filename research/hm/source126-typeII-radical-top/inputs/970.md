# Polar integrability forces joint P-row rank two in source126 Types I and II

## Result and boundary

For every source126 Type I or Type II constant inclusion in the pinned balanced normal form, the joint P-row map

    Type I: R_P:J→Hom_G(2P,P),
    Type II: R_P:J→Hom_G(3P,P)

is injective, hence has rank two. In Type I it is an isomorphism. In particular no nonzero radical element has zero P row. This improves PR959's nonzero-row theorem to full joint-row independence by a polar-integrability argument, not a genericity assumption.

Combined with PR954, this excludes J_Q=J for the single invariant positive product Q. Hence, in Type I,

    D_Q=C·1⊕J_Q, J_Q²=0, dim J_Q≤1.

In Type II, combining the rank-two conclusion with PR961 leaves only its triple (r,epsilon,d)=(2,0,0): the common-annihilator subcomplex is27→24 and its quotient is NOT acyclic.

A possible compatible radical line is not excluded. The Type I source itself, its source-dual pairing, the other residual templates, and the original proof-repair question are not resolved. No actual HM coefficient, point, matrix, parameter value or selected rank is evaluated.

## 1. Exact inputs and polar conventions

INPUTS.json retains eight immutable source proofs: PR856, PR858, PR862, PR944, PR946, PR954, PR959 and PR961. PR961 is pinned at cc3215b97a5c92a9253a9774d0f25ade0648b6e5, research/hm/source126-typeII-joint-annihilator/PROOF.md. PR959 was fetched at commit06919d6651dc9e747128a4c09c515bb3b0f41e09, path research/hm/source126-typeI-polar-row/PROOF.md, and matched to its reviewed bytes. PR954 is pinned at1dfd8f6b2b7d39d41de2619737b6cf4cfb951e75.

The balanced top and actual Y configuration shared by Types I and II are

    C=A+V+P+D,
    F=(P+2D)O(-2)⊂C O, C O/F=O(28),
    Y=W O(-9)=U_1^10⊂(A+V+D)O.

Write D=Sym⁴W, A=Sym²W. PR858 identifies Y with the ACTUAL first polar of the degree-ten line, after a genuine constant gauge. Thus its inclusion can be written as df10 for a formal equivariant (A+V+D)-valued degree-ten covariant f10, with the standard symplectic identification for its two-dimensional source. Any change between equivariant identifications W O(-9)→Y is a constant scalar, since End_G(W)=C. There is no variable-dependent change of source frame.

PR862 identifies J with actual constant maps b:Hbar→C whose restrictions to R=X⊕Y land in F. The constant spans are span X=P in Type I and span X=P+D in Type II, while span Y=A+V+D in both. Type I radicals kill X and have zero constant P coefficient. In Type II this need not hold for arbitrary radicals; Section2 proves it for the hypothetical zero-P-row element. Restriction on R is injective, since R spans Hbar. PR946 identifies the P bundle component with the fourth-endpoint P row by natural Serre duality. This uses the actual bundle direct sum X⊕Y, not a Type II constant or reconstructed-pencil splitting.

PR959 proves two facts used here. First, the unique nonzero equivariant map Y→D O(-2) is, up to scalar, the first polar dr8 of the unique D-valued degree-eight covariant r8, twisted by -2. Second, if a homogeneous quadratic polynomial matrix p:D→U satisfies p dr8=0, then p=0, for any constant target U. Its proof uses the absence of linear syzygies in the degree-eight D coefficient system.

## 2. Reduce a zero P row to an integrable quadratic inclusion

Suppose 0≠j∈J has zero P row. Its bundle map R→F then lands in 2D O(-2). In Type I it already kills X. In Type II its restriction to X=O(-8) vanishes because

    Hom_G(O(-8),D O(-2))=Hom_G(D,Sym⁶W)=0,

as Sym⁶W=V+P. Because X spans P+D in Type II, the constant coefficients b_P and b_D vanish. Thus in BOTH types the constant P coefficient is zero, j|X=0 and j|Y is nonzero. Its map Y→F lands in 2D O(-2). As Hom_G(Y,D O(-2)) is one-dimensional, its two components are c1 dr8,c2 dr8 for constants not both zero. Consequently it factors as

    Y --dr8--> D O(-2) --p--> C O,

where p is the inclusion of the constant multiplicity line (c1,c2) in 2D O(-2), followed by F⊂C O. In particular p is an injective subbundle map. In homogeneous coordinates it is a degree-two polynomial matrix.

The constant P projection of b is zero. Thus p_P dr8=0, and PR959's quadratic-nonannihilation theorem forces p_P=0. On the other hand j|Y=b df10=d(b f10), since b is constant. After absorbing the harmless common scalar into p, we have the equality of polynomial one-forms

    p dr8=d(b f10).

Therefore its exterior derivative, or curl, is zero. We next show that its D target component can be integrable only when p_D=0.

## 3. Compute the universal D-channel curl

The space Hom_G(D⊗Sym²W,D) is one-dimensional. Indeed the ordinary SL2 decomposition is Sym⁴W⊗Sym²W=Sym⁶W⊕Sym⁴W⊕Sym²W, and on G these restrict to (V+P)⊕D⊕A. Thus the unique quadratic D-to-D channel is the ordinary infinitesimal sl2 action, up to a nonzero scalar.

Use formal coordinates w=(x,y) and the standard generators E,F,H on D=Sym⁴W, with [H,E]=2E, [H,F]=−2F, [E,F]=H. A nonzero representative for that channel is

    m(x,y)=x²E−xyH−y²F.

This is the action of the traceless matrix w⊗ω(w,−), with ω(w,z)=x z_y−y z_x. It is equivariant and not the zero polynomial map. Thus p_D=c m for some scalar c.

For any D-valued homogeneous degree-eight polynomial r, the curl of m dr is

    Ωr=(∂x m)∂y r−(∂y m)∂x r
       =2xE∂y r+H(x∂x−y∂y)r+2yF∂x r.

To compute this on r8 without choosing its coefficients, give D-valued polynomials their natural action (g·r)(w)=g r(g^(-1)w). The generators on the polynomial factor are

    E_ext=−y∂x, F_ext=−x∂y, H_ext=−x∂x+y∂y.

For the Casimir C=H²+2EF+2FE, whose scalar on SymⁿW is n(n+2), the displayed operator satisfies the exact identity

    Ω=(C_D+C_ext−C_total)/2.

This follows by expanding the Casimir of the sums of the internal and external generators; the two factors commute. In particular Ω is SL2-equivariant.

The tensor space D⊗Sym⁸W* decomposes under SL2 as

    Sym¹²W ⊕ Sym¹⁰W ⊕ Sym⁸W ⊕ Sym⁶W ⊕ Sym⁴W.

Its G-invariant line is contained entirely in Sym¹²W: Sym¹⁰W=A+V+D, Sym⁸W=P+D, Sym⁶W=V+P and Sym⁴W=D have no invariants, whereas Sym¹²W has one. Since r8 is a nonzero G-equivariant covariant, it represents that invariant line. Therefore

    Ωr8 = (4·6+8·10−12·14)/2 ·r8 = −32 r8 ≠0.

Equivalently one can check the scalar on the highest vector u⁴y⁸ in the Cartan summand and use SL2 equivariance. This also fixes the contragredient sign convention explicitly. No claim of an SL2 action on the actual HM bundle is made: SL2 is used only on these universal binary-form representation spaces.

The D component of the integrability equation in Section2 is c Ωr8=0. Characteristic zero and r8≠0 force c=0, hence p_D=0.

## 4. The remaining saturated inclusion is impossible

We have proved p_P=p_D=0. Therefore the subbundle p(D O(-2)) lies in (A+V)O. It is saturated in C O: the multiplicity line D O(-2) is a direct summand of F, and both F/(D O(-2)) and C O/F are locally free. Hence it is saturated in (A+V)O as well.

The quotient has rank6−5=1 and degree0−(−10)=10. Its equivariant line bundle is O(10), with no character twist because G is perfect. Since the top quotient q:C O→O(28) kills F, its restriction to (A+V)O factors through

    O(10)→O(28).

This restriction is nonzero: otherwise the nonzero constant space A+V would give global sections of F, whereas H0(F)=0. Yet Hom_G(O(10),O(28))=H0(O(18))^G=0. The latter vanishing follows directly from the fixed McKay recurrence (and is checked by the bounded verifier). This contradiction excludes every nonzero j in ker R_P.

Thus R_P is injective in both types, and its source has dimension two. It has rank two; in Type I its target also has dimension two, so it is an isomorphism. No independence was inferred from the ranks of individual rows.

## 5. Consequence for invariant compatibility

PR954 proves that hypothetical full-J compatibility with Q forces det R_P=0, by the actual A second-Bockstein obstruction on a common-annihilator subpencil. Section4 proves det R_P≠0 for every Type I inclusion in the fixed normal form. Therefore J_Q cannot equal J, and dim J_Q≤1. PR944 supplies the surrounding local square-zero algebra statement.

This does not force J_Q=0, prove existence of a compatible line, or rule out Type I source occurrence. It removes the full two-dimensional radical compatibility alternative, not a source-dual catalogue pair. For Type II, PR961 permits only (r,epsilon,d)=(1,0,0),(1,0,1),(1,1,0),(2,0,0) under full-J compatibility. Rank two leaves only (2,0,0), so

    U=A+2V+2P+2D, dimension27,
    Z=2V+2P+2D, dimension24.

The restricted Q has kernel A+D and cokernel D; the induced quotient has kernel D and cokernel P. Its nonzero D kernel means that quotient is NOT removable by an acyclic filtered contraction. The internal A first symbol remains the nonzero binary-quadratic multiplication of PR961, killed upon passage to the original cokernel. This is a necessary conditional reduction, not an exclusion of full-J compatibility in Type II. Type III is unchanged.

## Verification scope

verify.py authenticates eight immutable inputs, derives all required symmetric-power invariant multiplicities, and verifies the curl/Casimir identity on the entire45-dimensional space of D-valued degree-eight polynomials with exact integer arithmetic. It separately generates all13 Cartan-summand basis vectors and checks Ω=−32 on each. These are universal representation calculations, not selected HM coefficients, root samples or source-instance ranks. The written proof supplies the geometry and actual polar identifications; the computation is not proof-assistant certification.
