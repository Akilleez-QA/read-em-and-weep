# Rigidity of existing first-normal pairs and the remaining equation complex

## New comparison results and exact scope

Let X=P_stack(1,1,2,2), with physical O(1)=O_wt(2), coarse map pi:X->Q, omega_X=O(-3), and finite group Gamma=SL_2(F_5). Let G be the actual rank-two Serre bundle, L=det G=O(2), sigma its regular section, B=End_0(G)=pi*B_Q, and N=J(sigma^2) in H0(B(2)). Define, in cohomological degrees zero and one,

    C = [ A=B(-2) --e_sigma--> E=G(-2)=G* ],
    e_sigma(T)=T sigma.

The established commutator and defect results give an exact sequence of actual sheaves

    0 -> O(-4) --N--> B(-2) --e_sigma--> G*
      -> D=omega_(2Z)(-1) -> 0.                       (1)

Here 2Z is the ordinary square thickening of the regular zero ideal of sigma. Using PR645, the entire complex, not only its final quotient, is invariantly acyclic:

    HyperH^n(X,C)^Gamma=0 for every n.               (2)

Write J_im=im(e_sigma). The established contrasting conclusion is

    H1(J_im)^Gamma = C,
    H1(J_im)^Gamma -> H1(G*)^Gamma is an isomorphism. (3)

Thus neither the tangent sheaf nor the gauge-image sheaf is invariantly acyclic. Their nonzero degree-one classes cancel only in the two-term complex. A prescribed underlying normal bundle cannot be replaced by a variable one in using (2).

The new results are the actual comparison statements built on these groups:

- Any two existing Gamma-equivariant first-normal tracefree square-zero adjoint pairs, with the same fixed central marking and determinant extension, have a unique determinant-preserving marked isomorphism (Section 4).
- The three-term classical linearized equation complex is an extension of C by O_(2Z)(2)[-2]; hence its invariant hypercohomology is exactly H^(n-2)(O_(2Z)(2))^Gamma (Section 6).

The first statement is proved through the actual transition and section differences, not merely by naming an abstract deformation complex. Its underlying uniqueness is already implicit in the midpoint theorem and nonzero affine bracket; the added content is the explicit marked-pair Cech/complex comparison and unique-isomorphism formulation, not a new midpoint uniqueness phenomenon. The second retains an explicit local equation term that homogeneous pair rigidity does not remove. Neither makes arbitrary Hessian local formulas compatible, constructs higher normal lifts, or evaluates the absolute positive cubic obstruction.

## Pinned mathematical inputs and nonduplication check

Repository: Akilleez-QA/read-em-and-weep.

1. [PR645 invariant normal defect vanishing](https://github.com/Akilleez-QA/read-em-and-weep/blob/9bbdc4582a75f6a3b36f84b071972dd8c5313d5e/research/hm/invariant-normal-defect-vanishing/PROOF.md): H^i(D)^Gamma=0 for all i. It also proves that the actual evaluation map on H1 is an isomorphism between invariant lines, using the nonzero midpoint bracket rather than dimensions alone.
2. [PR543 global normal defect](https://github.com/Akilleez-QA/read-em-and-weep/blob/a0ccfe44a4d2b528622d591888b8cc1cddb47792/research/hm/order-four-quadratic-load/GLOBAL-NORMAL-ADJOINT-DEFECT-DUALIZING-TWIST.md): the tangent kernel is the image of multiplication by sigma, the commutator factors through evaluation, and D=omega_(2Z)(-1).
3. Same immutable PR543 head, WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md: sigma is a regular section, det G=O(2), B=pi*B_Q, and exactness of tame coarse pushforward. This does not identify the naive pullback of the coarse spinor with the stack spinor.
4. Same head, NORMAL-QUADRATIC-NONZERO-BY-SERRE-RESIDUE-DOUBLE-COVER.md, Section 2: H0(G*)=0, H1(G*)=1+V, H2(G*)=0. Its corrected three-channel dependency is PR643 at 356a3b8d2da36f5b3e2034cc5c6adf82757a33cc.
5. Same head, NORMAL-QUADRATIC-BRACKET-COMPONENT-SHADOW-GATE.md: H0(B(-2))=0, H1(B(-2))^Gamma=C, H2(B(-2))^Gamma=0.
6. Same head, MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md: an actual midpoint first-normal bundle with invariant square-zero adjoint exists. The endpoint bracket variation is nonzero. This supplies a reference object if the comparison theorem below is applied to actual coarse first-normal bundles; existence is not deduced from tangent acyclicity.

### Live frontier update and distinct contribution

The further dependency is [null’s actual third-value operator comparison](https://github.com/Akilleez-QA/read-em-and-weep/blob/17c039f361f7f1083ee2cf5607f04cc263de0ce4/research/hm/order-four-quadratic-load/ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md). It independently gives the untwisted centralizer sequence and applies its positive twist FOUR to the actual operator section r in H0(omega_(2Z)(5))_+, whose boundary in H1(B_Q(4))_+=P4 is the actual secondary value. That specified operator comparison is now established there; evaluation of its actual residue remains open.

The regular-sequence kernel below is therefore an independent verification of a newly overlapping lemma, not a claim of priority for that kernel. A subsequent [negative-defect proof by null](https://github.com/Akilleez-QA/read-em-and-weep/blob/a9082a22472000723d62fe3479bef20aa09baf91/research/hm/order-four-quadratic-load/FIRST-NORMAL-ADJOINT-DEFECT-IS-INVARIANT-ACYCLIC.md) also establishes the two exact sequences at twist minus two, invariant centralizer vanishing, and the invariant H1 isomorphism of the image with G*. Those overlapping results and PR645 are treated here as established foundations, independently verified below, not additional new proof steps.

The distinct contributions retained here are the concrete existing-pair rigidity comparison in Section 4 and the full three-term classical equation-complex triangle in Section 6. The all-degree hypercohomology vanishing is the derived bridge between the common foundations and pair rigidity. No inference transfers this negative-twist vanishing to null's positive-twist operator residue.

## 1. Exact kernel without dividing by local generators

Work on a smooth chart and trivialize G and L. Write sigma=(f,g), where (f,g) is a regular sequence, and T=[[a,b],[c,-a]]. The equation T sigma=0 is

    fa+gb=0,   fc-ga=0.                              (4)

Reducing the first equation modulo f and using that g is a nonzerodivisor modulo f gives b in (f), say b=-ft. Since f is a nonzerodivisor, the first equation then gives a=gt. The second equation becomes fc=g^2 t. Again reduce modulo f. The square of g is a nonzerodivisor modulo f, so t=fu for some u. Cancellation of the nonzerodivisor f gives

    a=fgu,   b=-f^2u,   c=g^2u.                     (5)

Conversely (5) solves (4). The parameter u is unique since f^2 is a nonzerodivisor. Thus the kernel is free of rank one, generated by N up to its fixed sign convention. This calculation uses the regular-sequence hypotheses, not a fraction-field division or an assumption that the ideal is principal.

Globally N is a section of B(2). Multiplication by N therefore gives the map O(-4)->B(-2), and the local calculation identifies its image with the kernel everywhere, including Z. The determinant/normal twists are forced: (-4)+2=-2. This proves the first part of (1).

The intrinsic identity

    [T,J(sigma^2)] = J(2 sigma (T sigma))             (6)

shows that the normal gauge map A->B factors through e_sigma, followed by the injective map

    m:E=G(-2) -> B,   v -> J(2 sigma v).

By the square syzygy resolution, im(m) is exactly ker(B --tr(N·)--> O(2)). Hence E is the actual sheaf of linearized tracefree square-zero corrections, not an arbitrary substitute of the same rank. Changing the harmless nonzero scalar in m or the sign of the commutator does not change the complex's isomorphism class. Input 2 identifies the cokernel with D, proving (1).

## 2. The missing centralizer is invariantly acyclic

For the physical line O(-4), Serre duality gives

    H^i(O(-4)) = H^(3-i)(O(1))*.

The physical line O(1) has H0=V+W, with no Gamma invariants, and no higher cohomology. For example its coarse pushforward is O_Q(1), whose cohomology follows from

    0 -> O_P4(-1) -> O_P4(1) -> O_Q(1) -> 0.

All maps are equivariant. The canonical line carries no extra Gamma character (Gamma is perfect); exactness of invariants in characteristic zero preserves the duality pairing. Therefore

    H^i(O(-4))^Gamma=0 for every i.                 (7)

In particular O(-4) is not being asserted to be acyclic before taking invariants: its H3 is (V+W)*.

The only cohomology sheaves of C are O(-4) in degree zero and D in degree one. The truncation triangle is

    O(-4) -> C -> D[-1] -> O(-4)[1].                (8)

Here D[-1] places D in degree one. Apply equivariant derived global sections. By (7) and PR645 both outer terms are acyclic, proving (2). Equivalently, the hypercohomology spectral sequence has no nonzero invariant terms. This proves the statement in all degrees rather than just the deformation and obstruction degrees.

## 3. The gauge image retains the fixed-bundle obstruction

Splitting (1) into two short exact sequences gives

    0 -> O(-4) -> A -> J_im -> 0,
    0 -> J_im -> E -> D -> 0.

Equations (7) and PR645 identify, in every degree,

    H^i(A)^Gamma = H^i(J_im)^Gamma = H^i(E)^Gamma,

and these identifications are induced by the actual maps, not chosen vector-space isomorphisms. The known primary groups therefore give H0(J_im)^Gamma=0, H1(J_im)^Gamma=C, and H2(J_im)^Gamma=0. In particular (3) follows.

This supplies a precise answer to the caution that quotient acyclicity alone does not remove cohomology in the image. Here that image cohomology is nonzero and is exactly accounted for by variation of the underlying bundle. It is not removed by a gauge choice on a prescribed bundle.

## 4. Exact comparison of existing first-normal pairs

For the actual coarse hypersurface Q, put Y=2Q and let I_(Q/Y)=O_Q(-2). Fix the determinant extension and markings on Q. Consider two existing first-normal pairs (F_1,N_1),(F_2,N_2) on Y, both restricting to the fixed cone bundle F_Q and fixed N, with trace N_i=0 and N_i^2=0. The determinant condition restricts infinitesimal changes of frame to tracefree endomorphisms.

The complex on Q is pi_*C. This is justified by exact tame pushforward, the projection formula pi_*B(-2)=B_Q(-2), and preservation of the actual tangent kernel in (6). It does not require an extension of the stack spinor line to Y or a hypothetical smooth stack thickening over Y. Its equivariant hypercohomology equals that of C on X.

Choose a sufficiently fine affine or etale cover and local determinant-preserving identifications of the two underlying bundles that reduce to their fixed markings. Such identifications exist locally for two vector bundles with identified reduction across a square-zero ideal; their determinant discrepancy is corrected locally since 2 is invertible. Under these identifications, transition differences give a Cech cochain

    a in Cech^1(A),

and adjoint differences give b in Cech^0(E). Since both pairs already exist globally and both are square-zero, their homogeneous comparison equations are, up to one consistent sign convention,

    delta a=0,   delta b=e_sigma(a).                (9)

Indeed products of two normal differences vanish in I_(Q/Y)^2, and the difference of the two nilpotence equations is precisely the tangent equation in Section 1. Changing local bundle identifications by x in Cech^0(A) changes (a,b) by (delta x,e_sigma(x)). Thus comparison classes lie in HyperH^1(C), with marked infinitesimal automorphisms HyperH^0(C).

For Gamma-equivariant pairs this is the equivariant complex. A finite group over C has exact invariants, so its cohomology is HyperH^*(C)^Gamma; equivalently one can use an invariant refinement and average the linear comparison cochains. Equation (2) implies that any two such equivariant pairs have a unique determinant-preserving marked isomorphism. The midpoint input supplies an actual reference pair, but is not reproved here.

This is a theorem about differences between existing pairs. It does NOT infer existence of a pair from H2(C)^Gamma=0, nor assert that arbitrary locally chosen objects have a coherent total descent cocycle. Those assertions would require checking their inhomogeneous nilpotence equations and their actual double- and triple-overlap defects.

## 5. Prescribed normal bundle and Hessian formulas

If the underlying first-normal bundle and its transition functions are held fixed, transition variation a is disallowed. Locally square-zero adjoint lifts, when they exist, form an affine torsor under E. Their overlap differences form an E-valued cocycle, with obstruction in

    H1(E)^Gamma=C.

This is a genuine nonzero possible obstruction space. Allowing the bundle extension to change by a class in H1(A)^Gamma changes this obstruction by the actual evaluation map, an isomorphism by Section 3. Thus precisely one invariant normal-extension parameter can cancel a given affine obstruction, provided the local lifts and their overlap cocycle have first been established. This is compatible with the already proved midpoint theorem; it does not permit replacing a prescribed endpoint bundle by the midpoint without acknowledging that change.

For a local Hessian recipe, square-zero correctness alone says its differences lie in E. It does not say that a difference lies in J_im. The image in D is the exact local obstruction to expressing that difference as a regular normal gauge. Global invariant acyclicity of D cannot make a nonzero section of D on a single chart vanish. The generator-change calculation already exhibits this distinction.

Consequently one must still establish, for the actual Hessian transition data, the transformation law for the normal parameter, determinant factors, base/coordinate changes, and off-cone lift choices. To preserve local gauge classes, their D-valued residues must be compatible, not just their nilpotence equations. To glue on a prescribed normal bundle, the E-valued overlap class must vanish without varying that bundle. For the specified positive operator, null's newly pinned note supplies its actual Cech comparison at twist four and retains the boundary of its residue r. That result is not a consequence of (2); the negative-twist acyclicity cannot be transferred to its different twist and positive-isotypic target. An arbitrary different operator would still require its own comparison.

## 6. The full equation complex has a further local term

For an explicit additional comparison, define the three-term linearized equation complex

    F_eq = [ B(-2) --ad_N--> B --tr(N·)--> O(2) ]

in degrees zero, one, and two. The composition vanishes by cyclicity of trace. The inclusion C->F_eq is the identity in degree zero and m in degree one. It is a monomorphism of complexes after fixing the consistent scalar convention in (6).

The regular square sequence identifies the image of B->O(2) with I_Z^2(2), including at Z: in a regular frame its three coefficients are nonzero scalar multiples of f^2,fg,g^2. Its kernel is m(E). Therefore the quotient complex has only one cohomology sheaf, O_(2Z)(2), in degree two. There is a distinguished triangle

    C -> F_eq -> O_(2Z)(2)[-2] -> C[1].

Consequently the actual invariant hypercohomology of the three-term complex satisfies

    HyperH^n(F_eq)^Gamma = H^(n-2)(O_(2Z)(2))^Gamma.

This is an exact reduction, not an assertion that the groups on the right vanish. The twist is TWO, not the twist ONE whose acyclicity PR645 proves. No vanishing is imported between them. This term records local linearized equation cokernels, whereas C describes differences of already valid local solutions. Neither complex is asserted to be the full derived deformation theory with all higher syzygies or a differential-operator complex. The distinction supplies an explicit remaining map/term rather than treating homogeneous difference acyclicity as automatic existence.

## Verification and contribution

The kernel was independently derived from the two regular-sequence equations; twists were checked globally from N in B(2). The truncation triangle and the two short exact sequences separately yield the same cohomological conclusion. The Cech calculation uses only square-zero products and compares already existing objects. No selected actual HM/source coefficients, points, matrices, rank evaluations, numerical experiment, or large computation was used. This is an authored structural proof relative to the pinned inputs, not a proof-assistant certificate.

The new steps are the explicit rigidity classification of existing marked equivariant first-normal pairs and the remaining local term in the classical equation complex. The common invariant acyclicity and nonvanishing gauge-image cohomology supply their independently checked foundation; neither is presented as a new result beyond PR645 and the subsequently overlapping negative-defect note. The newly established positive operator comparison is credited to null above; its actual residue evaluation, actual Hessian descent, and the absolute positive cubic gate remain separate.
