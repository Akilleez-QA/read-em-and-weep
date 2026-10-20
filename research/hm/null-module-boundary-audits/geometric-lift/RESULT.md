# Regular lifting: strict extension classes and the gluing obstruction

## Bounded result

The image condition `K(im Δ) ⊂ im Π + im δ_C` is insufficient even as an inclusion of coherent sheaves, even when every stalk admits an actual correction, and even when every term of the complexes is a vector bundle. The missing condition is strict regular lifting, followed by descent. For a specified boundary-valued map `u:S→C[-1]`, its exact extension obstruction is

    u_*[0→S→B→B/S→0] ∈ Ext¹_{Ch(O_X)}(B/S,C[-1]).       (1)

It vanishes exactly when a globally regular Hom-closed extension U exists. Here Ext is Yoneda Ext in the abelian category of complexes, not Ext in the derived category. If regular extensions already exist on a cover, the remaining obstruction is the Čech/sheaf H¹ class of their differences in the sheaf of strict chain maps `B/S→C[-1]`.

An explicit example on P¹ below satisfies the original factorization of K and has zero image obstruction, but no global actual correction. Its obstruction is the nonzero extension class of `0→O(-2)→O(-1)²→O→0`.

All constructions here are universal homological algebra or newly specified examples. No actual source/model/jet evaluations, physical matrix products, production imports, geometric experiments were performed. This does not evaluate the retained remainder or any trace.

## 1. Category and conventions

Let X be a ringed space; for the geometric examples it is a scheme. Work in the abelian category of O_X-modules, or in quasi-coherent modules where the indicated kernels, cokernels, and extensions remain in that category. Let A,B,C be bounded cochain complexes and Δ,δ_B,δ_C their differentials. All maps are O_X-linear regular sheaf morphisms. A restriction to an admitted open domain is handled by replacing X by that domain; transition functions and bundle twists are part of the sheaves, not discarded during lifting.

Retain degree-two chain map T:A→B, degree-zero chain map Π:B→C, degree-minus-one Qdot:B→C, degree-one Q:A→B, and

    K=Qdot T−ΠQ.

An actual free-compensation correction consists of globally defined regular maps U,V with

    |U|=−1,  δ_C U+Uδ_B=0,  |V|=1,
    (K+UT−ΠV)|W=0,  W=im Δ;  F=dV.

Write S^m=T(W^{m−2})⊂im δ_B^{m−1}. Regard S as a subcomplex of B with zero differential. Put D=C[-1], so D^m=C^{m−1} and d_D=−δ_C. A closed degree-minus-one map U is precisely a strict chain map B→D. A boundary-valued u:S→D is automatically a chain map.

“Image” means sheaf image. Sections of a sheaf image need only lift locally; they need not lift to global sections. A condition on fibers is weaker still. None of these distinctions can be suppressed by choosing vector-space complements.

## 2. Exact obstruction for extending one specified u

Let e_B be the extension of complexes

    e_B: 0→S→B→B/S→0.

For a specified regular boundary-valued map u:S→D, form its pushout:

    0→D→D ⊔_S B→B/S→0.                                (2)

**Theorem.** A strict chain map U:B→D restricting to u exists if and only if the Yoneda class of (2), namely u_*e_B, vanishes in Ext¹_Ch(B/S,D).

Proof. Apply the Hom–Ext exact sequence in the abelian category of complexes:

    Hom_Ch(B,D) → Hom_Ch(S,D)
       → Ext¹_Ch(B/S,D).

The connecting map sends u to the pushout class. Alternatively, an extension U defines a retraction of the injection D→D⊔_S B by `[d,b]↦d+U(b)`, with the pushout relation `(u(s),−s)=0`; hence (2) splits. Conversely a retraction restricts along B to the required U. This is a strict chain-map statement, so it includes all differential-compatibility equations. ∎

The possible U, when nonempty, form a torsor under Hom_Ch(B/S,D). A degreewise splitting of e_B alone is insufficient: the splitting must also satisfy the differential equations. Passing to chain homotopy classes or replacing Ext¹_Ch by a derived-category group changes the problem. In particular, the exact complex C in §5 is zero in the derived category, while its strict lifting obstruction is nonzero.

This is a direct application of Yoneda pushouts and the Hom–Ext boundary map; see [Stacks Project, Extensions](https://stacks.math.columbia.edu/tag/010I).

## 3. Four exact lifting stages for the original removal problem

The following replaces every unrestricted splitting in the earlier vector-space sufficiency proof. These stages are existential with compatible choices: vanishing for unrelated choices is not sufficient.

### Stage A: choose a boundary representative as a regular morphism

Use grading m matching S⊂B and define

    N^m=im(δ_C:C^{m−2}→C^{m−1}),
    I^m=im(Π:B^{m−1}→C^{m−1}),
    J^m=N^m∩I^m,   H^m=(N^m+I^m)/I^m≅N^m/J^m.

The assumed sheaf-image inclusion for K, together with its factorization, implies that

    h=−[Qdot|S]:S→H

is a well-defined graded morphism. This uses the sheaf-surjection W→S and equality of sheaf images; it requires no choice of its section.

The obstruction to a regular u:S→N with quotient h is the pullback class

    a(h)=h^*[0→J→N→H→0] ∈ Ext¹_Gr(S,J).                (3)

It vanishes exactly when such a u exists. The choices form a torsor under Hom_Gr(S,J). For bounded grading, Ext¹_Gr is the finite product of the degreewise sheaf Ext¹ groups.

### Stage B: extend that u as a closed regular U

For a choice from Stage A require

    b(u)=u_*e_B=0 ∈ Ext¹_Ch(B/S,C[-1]).                  (4)

Choose a strict extension U if it vanishes. Then `g=(K+UT)|W` takes values in `im Π` in the required degrees.

### Stage C: lift g through Π

Here use the graded notation M⟨1⟩^r=M^{r+1}; this notation imposes no differential condition. Set I_Π=im Π and N_Π=ker Π. The obstruction is

    c(g)=g^*[0→N_Π⟨1⟩→B⟨1⟩→I_Π⟨1⟩→0]
        ∈ Ext¹_Gr(W,N_Π⟨1⟩).                           (5)

It vanishes exactly when there is a graded regular V_W:W→B⟨1⟩ with ΠV_W=g.

### Stage D: extend V_W to A

For a choice in Stage C require the pushout obstruction

    d(V_W)=(V_W)_*[0→W→A→A/W→0]
        ∈ Ext¹_Gr(A/W,B⟨1⟩)                            (6)

to vanish. Its vanishing is equivalent to a graded regular V:A→B⟨1⟩ extending V_W. No closedness is imposed on V because compensation is free; set F=dV afterward.

**Exact criterion.** Under the sheaf-image inclusion, global regular free-compensation removal exists if and only if there are successive choices u,U,V_W making (3)–(6) vanish. Sufficiency follows by construction. For necessity, any actual U restricts on S to a boundary-valued u (because Uδ_B=−δ_C U); its reduction is h because removal holds on W. Actual V supplies V_W and all required splittings. Thus these conditions are complete, not merely necessary.

Fixed compensation or fixed E adds equations on V and is outside this free-compensation theorem. No conclusion about cancellation of the paired term or the other remainder families follows.

## 4. Cover-level formulation and the exact gluing class

For fixed u with local strict extensions U_i on an open cover {X_i}, define

    E_U = underline Hom_Ch(B/S,D).

On overlaps, U_j−U_i vanishes on S and is a chain map, hence defines a section e_ij of E_U. These sections satisfy e_ij+e_jk=e_ik. Altering local extensions changes this cocycle by a Čech coboundary. The local extensions glue after permissible adjustments exactly when this cocycle is a coboundary; equivalently their E_U-torsor is trivial, with class in H¹(X,E_U). On a chosen cover use its Čech class; arbitrary-cover torsors are classified by sheaf H¹. No acyclicity assumption is needed for the torsor formulation.

There is an equally exact one-step version for the entire removal problem, avoiding choices in Stages A–D. Define sheaves

    P = Z^−1 underline Hom(B,C) ⊕ underline Hom^1(A,B),
    R = underline Hom_Gr(W,C⟨1⟩),
    L:P→R,   L(U,V)=(UT−ΠV)|W,
    N_L=ker L,   I_L=im L,   k=−K|W.

Then global removal exists exactly when:

1. k is a section of I_L, meaning an actual regular correction exists locally; and
2. the connecting class ∂k in H¹(X,N_L) for `0→N_L→P→I_L→0` vanishes.

The first condition is stronger than the naive output-image condition and can fail because of local module-extension obstructions. The second is precisely descent of locally valid actual corrections. The exact global-sections sequence proves both directions. If coherent data and suitable finiteness hypotheses make these kernel/image sheaves quasi-coherent, affine X eliminates the H¹ gluing obstruction; it does not automatically eliminate the local lifting condition.

For perspective on the latter issue, take R=k[t], B=(R --t--> R) in degrees 0,1, and C=(R --id--> R) in degrees −1,0. The R-linear boundary map u:tR=Bnd_B¹→Bnd_C⁰=R given by u(t)=1 cannot extend to B¹=R: R-linearity would require tU¹(1)=1. Its graded pushout class is the generator of Ext¹_R(R/(t),R)≅R/(t). This is an example for the specified-u extension lemma, not a claim that this particular u is forced by a globally regular Qdot in the original removal problem.

## 5. Global counterexample satisfying the original factorization

Let X=P¹_k with homogeneous coordinates [x:y]. Consider the exact complex

    C^−2=O(-2) --i--> C^−1=O(-1)² --p--> C⁰=O,
    i(c)=(-yc,xc),   p(a,b)=xa+yb.

All other C degrees are zero. Let

    B⁰=O --id--> B¹=O,
    A^−2=O --id--> A^−1=O.

All other A,B degrees are zero. The degree-two T:A→B is identity in both displayed degrees. Set Π=0, Q=0, E=0, and define Qdot:B→C of degree −1 by

    Qdot⁰=0:O→O(-1)²,
    Qdot¹=id:O→O.

Then K=Qdot T has K^−2=0 and K^−1=id. In particular W^−1=O and

    K(W^−1)=O=Bnd_C⁰.

Thus the sharp vector-space image condition holds as an equality of sheaves. It holds at every stalk and on every fiber. Since p is locally a split surjection, actual closed U eliminating K exist on each standard affine chart.

Globally, Π=0 means removal forces U¹=−id. Closedness in degree zero then reads

    p U⁰+U¹ id=0,  hence p U⁰=id_O.

But a regular O-linear U⁰:O→O(-1)² is a pair of global sections of O(-1), and H⁰(P¹,O(-1))=0. It cannot be a section of p. V cannot help because ΠV=0. Hence global actual removal is impossible for every choice of free compensation.

The nonexistence argument for this particular example is stronger than O-linearity. Any globally defined k-linear sheaf morphism U⁰, including any regular finite-order k-linear differential operator, sends the global section 1 of O to a global section of O(-1)². That section must be zero, so pU⁰(1)=1 is impossible. This uses compatibility with restrictions and existence on all of X, not module linearity. It does not apply to merely rational operators, non-global choices, or operators whose codomain/domain has changed.

The Ext¹ criteria in §§2–3 remain specifically criteria in the stated O_X-module/complex categories. They must not be asserted for a different category of differential operators without reconstructing the appropriate exact problem there. The example's global-section argument extends its own nonexistence claim, not the general Ext¹ theorem.

The original presentation identities can be retained without imposing an artificial derivative mismatch: take Π(t)=t dQdot, T(t)=T constant, Q=0, E=0. At t=0 this gives Π=0, Π′=dQdot, T′=0=E−dQ, and M′=dK+ΠE. The degree-zero dQdot has component id:B⁰→C⁰ and zero B¹→C¹; it is a chain map. Thus this is a genuine formal instance of the given factorization and derivative identities, not merely an arbitrary K.

### Explicit obstruction and cover cocycle

On X_x={x≠0} and X_y={y≠0}, sections of p are

    s_x(1)=(1/x,0),   s_y(1)=(0,1/y).

The inverses here mean regular local sections of O(-1) on the indicated charts, not globally admitted denominators. Choosing U⁰=s_x or s_y and U¹=−id gives the local actual corrections. Their difference satisfies

    s_y−s_x=(-1/x,1/y)=i(1/(xy)).

Thus the obstruction cocycle is `1/(xy)` in O(-2) on the overlap. In the x-chart coordinate z=y/x, relative to frame x^−2 it is z^−1. It is not a coboundary, since

    k[z,z^−1] / (k[z] + z^−2 k[z^−1])

has nonzero class z^−1. Consequently the obstruction is the generator of H¹(P¹,O(-2))≅k, or equivalently the nonzero Yoneda class

    [0→O(-2)→O(-1)²→O→0] ∈ Ext¹(O,O(-2)).

This directly exhibits the required transition incompatibility. Standard projective-space cohomology, including the two groups used here, is given in [Stacks Project, Cohomology of projective space](https://stacks.math.columbia.edu/tag/01XS).

## 6. What is now settled, and what remains

The unrestricted vector-space sufficiency argument has four genuine regular replacements: boundary-representative lifting, strict chain-map extension, Π-lifting, and extension from input boundaries. Equations (3)–(6) identify their exact Yoneda classes, with compatible choices. Equation (1) isolates the requested closed-U obstruction; §4 identifies its descent class and supplies a complete all-at-once criterion.

The P¹ example proves that even stalkwise actual solvability cannot certify a global regular auxiliary change. It also proves that derived equivalence of the target complex cannot replace strict regular lifting. A proof in the actual geometric setting must specify the admitted sheaves/modules and show these classes vanish, or construct compatible regular lifts directly. Additional character, comparison-weight, or domain restrictions must be encoded in that category or checked separately; they are not implied by these abstract vanishing statements.

Nothing here proves the actual four-family remainder is zero, evaluates a retained detector, or upgrades an arbitrary algebraic functional into a geometrically admitted trace.

## Inputs read

- [RESULT.md](../retained-remainder/RESULT.md)
- [COMPENSATION-LIFTING.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/0c7f3f16ddea65616b2c6d4629c8b44f6fdae625/research/hm/null-homotopy-compensation/COMPENSATION-LIFTING.md)

The proofs and examples above are independent deductions from those formal inputs. The two linked primary mathematical references support only the general extension formalism and standard projective-space cohomology; the application to this lifting problem is established here.
