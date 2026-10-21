# Conductor gluing realizes both symmetry-allowed section counts

Work over C. Let V=V51, let nu:M->V be its normalization, let L0=O_V(1), and put D=nu*L0. Write U=(Z/5)^2 for the projective Heisenberg subgroup and H for its order125 central extension. A fixed polarization class is not an honestly U-linearized line bundle.

## Pinned inputs

All PRs are in https://github.com/Akilleez-QA/read-em-and-weep.

- PR610, e4898406ed2552dd40e9695f9fda3d9f1d270301, research/hm/cubic-joint-characters/PROOF.md: the sixty double values arise by pairing the twenty exceptional flags in each of six eigenbasis pentads. The pairing is (i,j)->(2i-j,3i-2j). The actual cubic quotient sends each repeated-index tensor L_i^2 L_j, i!=j, to a nonzero vector in a one-dimensional joint-character space.
- PR611, 12b28d33627cc0e8b283d142dc16439a51bb5e00, research/hm/cubic-branch-transversality/PROOF.md, Sections 3–5: M=Bl_30(P4), and the normalization conductor is the reduced set Sigma of sixty double values, with inverse image Omega consisting of120 points. The structure algebra is the subalgebra of nu_*O_M with equal values at the two points over each y in Sigma. For any one pentad, its ten double-value lines are ten distinct joint-character lines and exhaust the ten-dimensional cubic dual space. Also H0(O_M)=C and H1(O_M)=0.
- PR615, 24bc9b741c287f8ac207bd9df4de4c07c50bea2f, research/hm/cubic-polarized-deformations/PROOF.md, Section2: S=H0(M,D)=H0(V,L0) has dimension10; every normalization section already descends for L0. L0 is very ample.
- PR634, 895e3a61098f50eccc0a4dc22b58606a28125355, research/hm/cubic-algebraic-deformation-slices/PROOF.md: marked underlying scheme automorphisms reducing to the identity are trivial over every local Artin base, using H0(Theta_V)=0.
- PR637, a5fd5de0044a12bc7bb33f3431b1aa7eae7031b6, research/hm/cubic-equivariant-polarization-splitting/PROOF.md, Section3: the sixty nodes form twelve U-orbits of length five, two for each pentad. No node stabilizer exchanges its two branches. Orienting the two branches at one node and transporting by U gives a consistent orientation on its orbit. The U-fixed marked pair-class germ has dimension twelve and constant underlying abstract class.
- PR638, e45aed7546876fcba949918232e7716283dd8f59, research/hm/cubic-linearization-obstruction/PROOF.md: H acts honestly on L0 with primitive central weight -3 modulo5. Every representation with this central weight has dimension divisible by five. Nonconstant U-fixed polarized formal arcs have generic h0 in {0,5}.

The results below resolve occurrence of both values and exhibit algebraic families; they use no selected coefficient, point, derivative, matrix or rank evaluation.

## 1. An algebraic conductor-gluing torus

For each y in Sigma choose an ordering p_y^+,p_y^- of its two inverse images. The pullback D has a specified identification of its two fibers at y, supplied by L0. For a collection of units lambda_y over a C-algebra R, define L_lambda on V_R by the condition on local sections of nu_*D_R

    s(p_y^+) = lambda_y s(p_y^-),

where the original identification is understood. Equivalently, it is the kernel of the surjective sheaf map

    nu_*D_R -> direct-sum_(y in Sigma) (L0)_y tensor R,
    s |-> (s(p_y^+) - lambda_y s(p_y^-))_y.              (1)

Away from Sigma this is just D transported by the normalization isomorphism. At a node the conductor fiber product identifies O_V with pairs of functions of equal residue. After trivializing D, replacing the residue identification by multiplication by the unit lambda gives a free rank-one module over that fiber product. This assertion can be checked in the semilocal normalization: Chinese remainder supplies a function with residues lambda and1; it is a unit near both points, and multiplication by it identifies the usual equal-residue module with the new module. The same construction over the parameter ring works locally around each parameter point. Thus L_lambda is invertible, not merely torsion-free. Its pullback is D_R. Formula (1) also proves compatibility with base change, since the last sheaf is a finite free R-module and the map is surjective locally.

Apply this construction universally over the algebraic torus T60=(G_m)^60. At its identity it gives L0. Two parameters give line bundles isomorphic over the identity of V_R only if they coincide: an isomorphism pulls back to an automorphism of D_R, hence multiplication by a global unit in R*, since H0(M_R,O)=R. Such a scalar multiplies both branch values equally and cannot change any gluing ratio. Over local Artin algebras, a marked pair isomorphism might initially include an underlying scheme automorphism reducing to the identity. PR634 makes that automorphism trivial. The scalar argument therefore also proves injectivity for marked pair classes over those algebras and establishes nonconstancy of the formal arcs below.

More intrinsically, these are all line bundles with specified pullback isomorphism class D: each such bundle supplies one residue identification at every paired fiber, and any two pullback identifications differ by a common scalar. The conductor fiber-product description reconstructs the bundle from these data. No additional identification between different gluing parameters occurs because M is connected and has only constant global units. In particular there is no division by a further diagonal G_m in these sixty ratios.

The product V x T60 is projective over T60. Since the identity restriction L0 is ample, openness of relative ampleness supplies an open neighborhood T_amp of the identity on which the universal L_lambda is relatively ample. We use this neighborhood whenever calling the family polarized; we do not need a global ampleness assertion for every torus point.

## 2. The twelve-dimensional fixed subtorus

Orient the pairs U-equivariantly on each orbit, as permitted by PR637. Let O_1,...,O_12 be the twelve node orbits. Set lambda_y=lambda_i for y in O_i. These choices define a subtorus T12=(G_m)^12 of T60.

To check invariance without assuming a U-linearization of L0, first apply the same gluing construction to the trivial line bundle on M, obtaining P_lambda on V. The constant linearization of O_M preserves its gluing precisely because the ratios are constant along the oriented U-orbits. It descends to an honest U-linearization of P_lambda. Now L_lambda=L0 tensor P_lambda, so its class is U-fixed, and its H-linearization has the same primitive central weight as L0. This is consistent with the nonexistence of an honest U-linearization of L_lambda itself.

The identity tangent coordinates of T12 are the twelve orbitwise conductor differences. They form H1(O_V)^U by PR637. Thus this torus provides actual algebraic pure-polarization directions for the previously constructed twelve-dimensional fixed formal germ. For the constructions below we need only its injectivity on classes and its U-fixed property, not an identification of all possible algebraic deformations with this torus.

## 3. The exact section equation

All global sections of D descend for the original L0. Therefore, after the original fiber identifications,

    s(p_y^+) = s(p_y^-) = ev_y(s)  for every s in S.

Global sections on the constant normalization commute with any extension of the ground C-algebra: H0(M_R,D_R)=S tensor R. Taking H0 in (1) yields the exact description

    H0(V_R,L_lambda)
      = {s in S tensor R : (1-lambda_y) ev_y(s)=0 for every y}.
                                                               (2)

For a U-orbit O_i, let

    E_i:S -> T_i=direct-sum_(y in O_i) (L0)_y,
    K_i=ker E_i.

The target has dimension five. Equation (2) becomes

    H0(V_R,L_lambda)=intersection_i ker((1-lambda_i) E_i).        (3)

Over a field, an index with lambda_i=1 imposes no constraint, while any other index imposes exactly E_i(s)=0. This is an actual cohomology formula, not a semicontinuity estimate or a calculation at a selected point.

## 4. Every single orbit cuts exactly five sections

Each E_i is H-equivariant for the existing H-linearization of L0. The center acts with the same primitive weight on S and on T_i. The target representation T_i is irreducible: every nonzero H-subrepresentation has dimension divisible by five by the elementary eigenspace-cycle argument of PR638, and T_i itself has dimension five.

Evaluation E_i is nonzero because L0 is globally generated: at every y there is a section with nonzero value. Therefore its H-stable image is all of T_i. Consequently

    rank E_i=5,    dim K_i=5.                                   (4)

Twisting the gluing on a single orbit, with lambda_i different from1 and all other ratios equal to1, gives h0=5 exactly. In particular the arc lambda_i=1+t and lambda_j=1 for j!=i is nonconstant and U-fixed; its generic h0 is five. It arises from an algebraic curve in T12 through the identity, restricted to T_amp. Thus this is more than existence of a formal system.

## 5. A pentad gives complementary kernels and zero sections

Fix any of the six eigenbasis pentads. Its ten nodes are the union of two U-orbits, say O_i and O_j. PR611 Section3 proves that their ten projective evaluation lines in S* are ten distinct joint-character lines for the honest abelian group used in PR610. Every line is nonzero, and they exhaust S*. Hence the actual combined evaluation map is an isomorphism

    E_i direct-sum E_j : S -> T_i direct-sum T_j.                 (5)

One may also read this directly from PR610: the twenty repeated-index flags pair in ten two-element equal-weight classes, and each such weight occurs once in the actual cubic quotient. The geometric first-jet nonvanishing makes all ten evaluation lines nonzero. No new coefficients or ranks are evaluated here.

Equation (5) proves K_i intersection K_j=0. If both lambda_i and lambda_j differ from1, equation (3) forces every section to vanish. In particular the algebraic arc

    lambda_i=1+t,   lambda_j=1+t,   all remaining lambda=1

is U-fixed and nonconstant, lies in T_amp after restricting its curve around t=0, and has generic h0=0. This realizes the other value permitted by PR638.

More generally, the open subset of T12 where these two ratios both differ from1 has h0=0, irrespective of the other ten ratios. It is nonempty and dense; intersecting it with the nonempty open T_amp retains that property. Thus the general member of this algebraic twelve-dimensional polarized family has no sections of its original polarization in degree one. Ampleness does not imply that a line bundle itself has a section; sufficiently high powers remain ample and have sections.

On the two-dimensional subtorus varying just this pentad's two ratios, the section counts are completely determined: h0=10 at (1,1), h0=5 when exactly one ratio differs from1, and h0=0 when both differ from1. These are field-valued, set-theoretic strata. We do not identify the scheme structure of a Fitting or Brill–Noether locus, nor claim that all twelve kernels K_i are pairwise distinct.

## 6. The reduced support of the positive-section locus

There is a structural description even without deciding which of the twelve kernels coincide. Each K_i is an H-subrepresentation of dimension five with primitive central character, hence is irreducible by the same divisibility argument as in Section4. Thus K_i intersection K_j is zero unless K_i=K_j.

Partition {1,...,12} into classes C according to equality of K_i. For any field-valued torus point, let A(lambda)={i:lambda_i!=1}. Formula (3) proves that h0 is10 if A(lambda) is empty, five if A(lambda) is nonempty and contained in one class C, and zero otherwise. Define the coordinate subtorus T_C by lambda_j=1 for j outside C. Then the set of complex points with a positive section is exactly the union of the T_C, and h0=5 on each T_C away from the identity. Distinct such subtori meet only at the identity. This determines the reduced closed support, including after restriction to T_amp, but not its cohomological determinantal scheme structure.

For each of the six pentads its two kernels are complementary by (5), so an equality class C contains at most one index from each pentad. Consequently |C|<=6. The positive-section support in T12 has dimension at most six, hence codimension at least six. No pairwise-distinctness assertion about all twelve K_i is needed. Equality-class sizes, and therefore the sharper exact dimensions and component count, remain undetermined here.

## 7. Delayed loss at finite Artin orders

The same equations quantify higher-order section loss without replacing it by first-order information. Put R_n=C[t]/(t^(n+1)) and k>=1. For the single-orbit arc lambda_i=1+t^k, a C-linear splitting S=K_i direct-sum S_i of the surjective map E_i identifies its section module with

    (K_i tensor R_n) direct-sum (T_i tensor Ann_Rn(t^k)).          (6)

It follows that its C-dimension is

    5(n+1) + 5 min(k,n+1).

When n<k all ten central sections lift. When n>=k, the image of reduction to H0(V,L0) is exactly K_i, of dimension five: the annihilator term is t^(n+1-k)R_n and has zero residue. Over C[[t]], the section module is simply K_i tensor C[[t]].

For the two complementary orbits of Section5, both with ratio1+t^k, equation (5) instead gives

    H0(V_Rn,L_lambda) = S tensor Ann_Rn(t^k),                    (7)

after the fixed evaluation isomorphism. Its C-dimension is 10 min(k,n+1). Again all ten central sections lift through orders n<k; none has a nonzero central value at any order n>=k. Over C[[t]] the global section module is zero. This makes the delayed loss of the complete section system explicit while the underlying scheme is the constant V throughout.

## Contribution and limitations

Both symmetry-allowed generic section counts, zero and five, occur in explicit algebraic conductor-gluing families through the original polarization. The general member of a twelve-dimensional U-fixed polarization family has zero sections, and a single node-orbit variation has five. Two orbit coordinates from any one pentad give the exact field-valued 10/5/0 stratification above. The positive-section support throughout the twelve-dimensional torus is a union of coordinate subtori of dimension at most six, indexed by equality classes of orbit kernels. The finite-order formulas distinguish arbitrarily delayed section loss from a first-order claim.

The constructions concern V51 and its original degree-one polarization. They neither produce an honest U-linearization of that polarization nor alter its order-five obstruction. They do not determine the full scheme structure of section-jump loci, the full-Gamma linearization criterion, null's higher adjoint Bocksteins, selected source-instance gates, or Weil-class algebraicity. This is a mathematical derivation from the pinned inputs, not proof-assistant verification.
