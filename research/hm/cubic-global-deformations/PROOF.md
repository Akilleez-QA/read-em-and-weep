# Global tangent cohomology and unobstructed abstract deformations of the cubic fourfold image

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected actual HM/source coefficient, matrix, point evaluation, numerical rank test, search, or computer algebra is used. All local coordinates and character decompositions below are universal proofs, not evaluations of the selected source instance.

## 1. Pinned inputs and statement

The scope and evidence boundaries are those of PR1, `research/README.md` at `2531056eae05fdf31e8fb4ca3affc5907073ad73`. This result concerns the cubic image, not a repair of the original algebraicity theorem.

Use these immutable inputs in Akilleez-QA/read-em-and-weep:

- PR611, `12b28d33627cc0e8b283d142dc16439a51bb5e00`, `research/hm/cubic-branch-transversality/PROOF.md`: V=V_51 has finite normalization nu:M->V, where M=Bl_Z(P4), Z consists of thirty distinct points. V is smooth outside sixty reduced points Sigma. Their normalization preimages form a reduced set Omega of 120 points. The completed rings are A_4, with A_d=C[[u_1,...,u_d]] x_C C[[v_1,...,v_d]]. The normalization quotient is the residue-difference quotient at each pair. The surface image T=T_75 has the same model with d=2 and smooth normalization Y.
- PR612, `799697070309151169a3517d5b0f263766ed0ffc`, `research/hm/cubic-jacobian-singular-schemes/PROOF.md`: completed finite algebraic differential modules are represented by continuous differentials, with relations v_j du_i+u_i dv_j. In particular, completion is not being replaced by unrestricted algebraic differentials of a power-series ring.
- PR613, `4b2a87f3530445fead1e6ad5ffea1fb06b85cc65`, `research/hm/cubic-local-rigidity/PROOF.md`, especially Section 8: the algebraic cotangent cohomology sheaf T^1_Q=Extsheaf^1(L_(Q/C),O_Q) vanishes for Q=V and Q=T. Its Sections 3–7 establish formal local rigidity and nonsmoothability.
- PR610, `e4898406ed2552dd40e9695f9fda3d9f1d270301`, `research/hm/cubic-joint-characters/PROOF.md`, Sections 1–2, using PR587 `865ab24e91333688d7ae76303d7d594aae8521f8`: Z is the thirty eigenlines of the six projective directions in an irreducible five-dimensional Heisenberg module A with faithful central character. For one order-five lift g its eigenspaces are lines L_i; another lift s cyclically permutes them. The five s-eigenlines also belong to Z.

Write Theta_Q=Hom(Omega_(Q/C),O_Q) for the tangent sheaf, to distinguish it from the surface named T. Write T^i(Q)=Ext^i(L_(Q/C),O_Q) for global cotangent cohomology, always using the full cotangent complex.

**Theorem.**

1. For either finite normalization h:N->Q just specified,

       Theta_Q = h_*(Theta_N tensor I_(Omega/N)).                     (1)

   This is a natural sheaf isomorphism: vector fields downstairs correspond exactly to vector fields upstairs vanishing at every normalization preimage of the pinched points.
2. For the fourfold image V,

       H^0(V,Theta_V)=0,    dim H^1(V,Theta_V)=576,
       H^i(V,Theta_V)=0 for i>=2.                                   (2)

   Its abstract first-order deformation space is canonically T^1(V)=H^1(V,Theta_V), so has dimension576. These deformations are locally trivial.
3. Every flat finite-type abstract deformation of V over a local Artin C-algebra is Zariski locally trivial. Its abstract deformation functor is formally unobstructed: every such deformation lifts across every small extension of local Artin C-algebras. This assertion is proved by explicit affine gluing below, not inferred from vanishing of global T^2(V).

No vanishing of local or global cotangent T^2 is asserted. No algebraization, convergence, explicit miniversal family, embedding-preserving deformation statement, or preservation of the cubic/HM presentation is asserted. Formula (1) also applies to the surface, but its numerical tangent cohomology and unobstructedness are not computed here.

## 2. Derivations of the two-branch algebra

Let U=C[[u_1,...,u_d]], W=C[[v_1,...,v_d]], A_d=U x_C W, and m_U,m_W their maximal ideals. A continuous derivation delta:A_d->A_d is determined by its variable images. Apply it to u_i v_j=0:

       v_j delta(u_i)+u_i delta(v_j)=0.                             (3)

Projection to U gives u_i pr_U(delta(v_j))=0. Since U is a domain, pr_U(delta(v_j))=0. Projection to W gives pr_W(delta(u_i))=0. The two components of an element of A_d have equal constant term. Thus delta(u_i) belongs to m_U direct-sum0 and delta(v_j) belongs to0 direct-sum m_W.

Conversely arbitrary choices of these images define continuous derivations of the two branches vanishing at their origins. They preserve the equal-residue subring and annihilate every mixed relation, so yield a derivation of A_d. Consequently

       Der_cont,C(A_d,A_d) = m_U U^d direct-sum m_W W^d.             (4)

This argument actually holds for d>=1. The restriction d>=2 is needed only for the separate local rigidity input.

For globalization, the residue-difference exact sequence of PR611 identifies O_Q as the subalgebra of h_*O_N with equal residues at each pair. A vector field in Theta_N tensor I_Omega sends every local function to one with zero residue at both points of each pair. It therefore preserves O_Q, defining a natural map from the right side of (1) to its left side. It is an isomorphism off Sigma. At a point of Sigma its completion is precisely (4), because completion of the finite algebraic differential module represents continuous derivations, and Hom for finitely presented modules commutes with flat completion. Completion of h_* of a coherent sheaf splits into the two completed branches. Hence the map is an isomorphism after faithfully flat completion at every remaining stalk, proving (1). This constructs the map before checking it formally; it does not assume that arbitrary derivations automatically extend to a normalization.

Since h is finite, (1) also gives

       H^i(Q,Theta_Q)=H^i(N,Theta_N tensor I_Omega).                 (5)

## 3. Tangent direct images of a blowup at reduced points

Let pi:M=Bl_Z(P4)->P4, with exceptional divisor E_z=P(T_z P4) over z. Here projectivization parametrizes lines. Let j_z:E_z->M and let Q_z be the tautological rank-three quotient

       0 -> O_Ez(-1) -> T_z P4 tensor O_Ez -> Q_z ->0.              (6)

The differential of pi fits into the exact sequence

       0 -> Theta_M -> pi^*Theta_P4 -> direct-sum_z j_z*Q_z ->0.    (7)

To verify both exactness and the precise twist, work on the universal blowup chart x_1=t, x_i=t a_i for i=2,3,4. The differential sends partial_t to e_1+sum a_i e_i, and partial_ai to t e_i. It is injective: its determinant is t^3, a nonzerodivisor. Its cokernel is annihilated by t and is the quotient of the constant four-dimensional tangent space along E by the tautological line spanned by (1,a_2,a_3,a_4). These descriptions agree on overlaps and prove (7). Equivalently Q_z=Theta_P3(-1); it is not Theta_P3 or O_Ez(1)^3.

For this blowup, pi_*O_M=O_P4 and R^i pi_*O_M=0 for i>0. One local verification uses the blowup of affine four-space at its origin, which is the total space of O_P3(-1). Its affine projection to P3 has structure algebra direct-sum_(r>=0) O_P3(r), whose higher cohomology vanishes. The pushforward on the affine base is its original polynomial algebra, and the calculation is compatible with restriction to base opens. Standard affine charts of P4 around each center, shrunk to exclude the other centers, reduce the assertion to this calculation; off Z the blowup is an isomorphism. Projection formula gives the same higher-direct-image vanishing for pi^*Theta_P4.

The sequence (6) and the cohomology of O_P3 and O_P3(-1) give

       H^0(E_z,Q_z)=T_z P4,    H^i(E_z,Q_z)=0 for i>0.              (8)

Push (7) forward. The map Theta_P4 -> direct-sum_z T_z P4 is the ordinary sheaf restriction/evaluation map and is surjective as a map of sheaves. This is NOT an assertion of surjectivity on global sections. Equations (7)–(8) yield

       pi_*Theta_M=Theta_P4 tensor I_Z,
       R^i pi_*Theta_M=0 for every i>0.                            (9)

Thus Leray identifies H^i(M,Theta_M) with H^i(P4,Theta_P4 tensor I_Z). The Euler sequence on P4 gives h^0(Theta_P4)=25−1=24 and H^i(Theta_P4)=0 for all i>0. The exact restriction sequence now yields

       0 -> H^0(Theta_M) -> C^24 -> direct-sum_(z in Z) T_z P4
         -> H^1(Theta_M) ->0,
       H^i(Theta_M)=0 for i>=2.                                   (10)

Since the middle target has dimension30*4=120,

       h^1(Theta_M)=96+h^0(Theta_M).                              (11)

No fat-point interpolation, actual point evaluation, or generic-position assumption has entered this computation.

## 4. The infinitesimal stabilizer vanishes universally

A global projective vector field is represented by an endomorphism a of A modulo scalars. Its vanishing at a projective line L is equivalent to a(L) subset L. By (10), H^0(Theta_M) is the space of endomorphism classes preserving all thirty node lines individually. This is the infinitesimal stabilizer; a possibly nontrivial finite permutation group of the node set does not affect it.

Preservation of the five g-eigenlines makes a diagonal with respect to the decomposition A=direct-sum_i L_i. Pick any eigenline K of the other lift s, and a nonzero v in K. Every projection v_i to L_i is nonzero: the relation s(v)=lambda v, together with s(L_i)=L_(i+1) and invertibility of s, implies that vanishing of any one projection forces vanishing of all of them. Since K is a node line, a(v)=mu v. If a acts on L_i by alpha_i, comparison of the nonzero components gives alpha_i=mu for every i. Thus a is scalar, proving

       H^0(Theta_M)=0,    h^1(Theta_M)=96.                         (12)

This uses arbitrary abstract eigenspaces and the group commutator structure. It neither selects nor evaluates coordinates of the actual nodes, and it does not invoke numerical rank of an evaluation matrix.

## 5. The 120 normalization marks and the exact dimension576

Because M is smooth and Omega consists of120 distinct reduced points, tensoring its ideal sequence by the locally free Theta_M gives

       0 -> Theta_M tensor I_Omega -> Theta_M
         -> direct-sum_(p in Omega) T_p M ->0.                     (13)

The last term is a skyscraper sheaf of total dimension120*4=480. Its higher cohomology vanishes. Equations (5), (12), and (13) give

       0 -> C^480 -> H^1(V,Theta_V) -> C^96 ->0,                   (14)
       H^0(V,Theta_V)=0,
       H^i(V,Theta_V)=H^i(M,Theta_M)=0 for i>=2.

Equation (14) is a canonical exact sequence with its intrinsic tangent-space terms; the identifications of those terms with coordinate vector spaces are noncanonical. In particular h^1(Theta_V)=480+96=576, without asserting a canonical splitting.

As a consistency check, before proving any automorphism vanishing, (11)–(13) already imply the universal cancellation

       h^1(Theta_V)=576+h^0(Theta_V).

The marked-point evaluation rank cancels; it need not be computed. The Heisenberg argument makes both relevant infinitesimal automorphism spaces zero, fixing the answer exactly.

## 6. Global first-order cotangent deformations

For a finite-type complex scheme Q, the local-to-global cotangent spectral sequence is

       E2^(p,q)=H^p(Q, Extsheaf^q(L_(Q/C),O_Q))
          => Ext^(p+q)(L_(Q/C),O_Q).

Its low-degree exact sequence reads

       0 -> H^1(Theta_Q) -> T^1(Q) -> H^0(T^1_Q)
         -> H^2(Theta_Q) -> T^2(Q).                               (15)

The cotangent complex has no positive cohomological degrees, so the displayed edge in total degree one has no negative-q contribution. By PR613, T^1_Q=0 for both images. Thus T^1(Q)=H^1(Theta_Q). Applied to V, this proves the576-dimensional abstract first-order statement. The classes are locally trivial because their local cotangent deformation classes vanish, or directly because they are represented by tangent-valued transition cocycles on affine overlaps.

The last term of (15) is NOT shown to vanish. In particular H^2(Theta_V)=0 does not imply T^2(V)=0: higher local cotangent groups can contribute to global degree two. The next section proves unobstructedness by a separate existence argument.

## 7. Affine rigidity supplies the missing gluing step

We give details because arbitrary singular varieties cannot be treated by invoking the smooth infinitesimal lifting property. Graf–Schwald explicitly discuss this gap in an often-quoted general locally trivial obstruction argument: [The Kodaira problem for Kähler spaces with vanishing first Chern class, Theorem1.4 and following remark](https://arxiv.org/html/2001.06339v2). Their normality-based theorem is not being applied to our nonnormal V.

The primary algebraic tool used here is the ring deformation torsor theorem, [Stacks Project, Lemma92.16.1](https://stacks.math.columbia.edu/tag/08SM): when lifts over a square-zero extension exist, marked isomorphism classes of lifts form a torsor under cotangent Ext^1, and infinitesimal automorphisms are cotangent Ext^0. We use it only with a small extension B'->B of local Artin C-algebras, kernel K, and m_(B')K=0.

**Affine lemma.** If U=Spec R is an affine open of V, its abstract Artin deformations are trivial. Moreover, every B-algebra automorphism of the trivial deformation R tensor B that induces the identity on R lifts to a B'-algebra automorphism of R tensor B' across a small extension.

Proof: the cotangent T^1 module of R is the global sections of the vanishing sheaf T^1_V on U, so Ext^1_R(L_(R/C),R)=0. The same group with target R tensor_C K vanishes, since K is finite-dimensional. For small extensions, a trivial deformation over B has a constant lift. The ring-lift torsor therefore has one element, and every flat lift with a fixed reduction identification is isomorphic to this constant lift. Induction through small extensions proves affine rigidity, including compatibility with a previously fixed trivialization.

For the automorphism assertion, take two copies of the constant B'-lift, and identify their reductions with R tensor B using the identity for one and the prescribed automorphism for the other. They are two marked lifts of the same B-algebra. The same zero torsor supplies a B'-isomorphism inducing the prescribed automorphism (or its inverse, depending on the marking convention; invert if needed). The controlling Ext group for the trivial B-algebra with target R tensor K equals Ext^1_R(L_(R/C),R) tensor_C K by cotangent flat base change and m_B K=0. This proves the assertion without a smoothness assumption or a general claim that automorphisms of arbitrary singular deformations lift.

An open subset of an Artin deformation lying over an affine open of the special fiber is affine: affineness is invariant under nilpotent thickenings. Consequently the affine lemma applies to restrictions of arbitrary scheme deformations. Since V is separated, finite intersections of affine opens are affine; all of them satisfy the lemma as well.

## 8. Formal unobstructedness by explicit overlap correction

Let X_B be any abstract deformation of V over B. Choose a finite affine open cover {U_i} of V. By Section7 the corresponding restrictions of X_B are trivial, with chosen trivializations inducing the special-fiber identity. Their overlap identifications alpha_ij form a cocycle and are the identity modulo m_B.

To lift X_B over a small extension B'->B, start with the trivial B'-deformation on each U_i. By the affine lemma on U_i intersect U_j, each alpha_ij lifts to an isomorphism alpha'_ij of the trivial overlap deformations; choose alpha'_ji to be its inverse. On a triple overlap the cocycle failure reduces to the identity over B, so is uniquely 1+c_ijk, where

       c_ijk belongs to Gamma(U_i intersect U_j intersect U_k,Theta_V) tensor_C K.

The square-zero condition makes 1+c an automorphism precisely when c is a derivation. Because every transition is the identity on the special fiber and m_(B')K=0, its conjugation action on these derivations is trivial. Associativity on quadruple overlaps therefore gives the ordinary additive Cech two-cocycle condition for c.

A finite affine cover with affine intersections computes coherent cohomology on the separated scheme V. By (2), H^2(V,Theta_V)=0. Thus c is a Cech coboundary. Modify the chosen overlap lifts by automorphisms 1+b_ij, for an appropriate tangent-valued one-cochain b with coefficients in K. The modified triple defects are zero, so these lifts satisfy the cocycle condition and glue the local trivial B'-deformations. Their gluing is flat and finite type over B', and reduces to the prescribed X_B. Properness, when included in the deformation convention, is preserved under the nilpotent thickening of the base.

Every surjection of local Artin C-algebras factors into small extensions, so this proves formal unobstructedness of the abstract deformation functor. It also shows explicitly why nonzero potential obstruction groups do not obstruct these deformations: local constant lifts exist, all necessary transition lifts exist by affine rigidity, and the remaining gluing class is killed by H^2(Theta_V)=0.

This conclusion is an Artin lifting statement. We have not constructed or algebraized a universal formal family, nor claimed that every such deformation continues to be a cubic image in P9 or the blowup-and-pinch presentation of the original HM data. The576-dimensional tangent space demonstrates failure of infinitesimal global rigidity, while the previously proved local nonsmoothability remains fully compatible with these locally trivial global deformations.

## 9. Contribution and boundary

The new step resolves the global tangent-sheaf dependency left open in PR613 and computes its cohomology exactly. It upgrades local rigidity plus the blowup geometry to576 abstract first-order directions and a separate proof of unobstructed Artin lifting. No first-order source-instance evaluation was needed: the only stabilizer input is the universal two-direction Heisenberg argument.

The distinction among local rigidity, global infinitesimal rigidity, vanishing of an obstruction group, actual unobstructedness, and algebraization is maintained throughout. Nothing here resolves the original full-adjoint, prescribed-source, higher-lifting or Weil-class algebraicity gates without a separate theorem connecting those problems to these abstract cubic-image deformations.
