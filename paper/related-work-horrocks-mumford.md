# Horrocks–Mumford proof-repair: bounded prior-art comparison

Literature comparison dated 22 October 2026. This bounded related-work note concerns the exact marked statements in this paper and the primary sources below. It is not a novelty or priority certificate, an exhaustive literature review, or an independent proof audit.

## Main assessment

The exact marked equivariant quadric conclusions are candidates for original contributions. No matching theorem was identified in the sources examined. That negative observation does not establish novelty: older papers may use different language, and several relevant works were read only in part or at abstract level. The methods and much underlying HM geometry have substantial precedents.

## Claim-by-claim comparison

| Current claim and exact scope | Closest checked prior art | Assessment and boundary |
| --- | --- | --- |
| For the specified family of general smooth inversion-even quadrics, the odd sector vanishes and the positive sector has dimension four or five. The relevant section group is **H⁰(Q, End₀(F)\|Q ⊗ O_Q(4))**, not untwisted H⁰(End₀(F)\|Q). The multiplication map is H¹(B(2))₊ → H¹(B(4))₊, dimensions 41 → 37. | Decker [D] computes HM monads and cohomology modules; Boralevi [B] classifies restrictions to planes and jumping strata. | The precise twist-four quadric bound is a candidate contribution. Neither source supplies the same theorem in passages checked. Do not conflate four sections of the classical HM bundle with four/five sections of this restricted twisted adjoint. The exact general dimension remains unresolved. |
| For the actual pencil q₀ + ta: first Bockstein zero; second zero on D5 and generically rank three on A; third zero, including the additional specialized kernel line at each of six axes. | [D] provides the established monad/cohomology framework. General obstruction and spectral-sequence methods are not inventions of this project. | Candidate contribution is evaluation of these **actual maps**, not the existence of an equivariant map or a representation decomposition. Third vanishing does not evaluate fourth order. The surviving Smith exponent is 4–31 if finite, or the cokernel persists. |
| Exactly two **marked, G-equivariant, fixed-determinant** formal-extension classes of the fixed cone restriction F\|Q; first-normal affine line has exactly two extendable points, supplied by ambient F_r and F_−r; higher continuation is unique. | Classical HM deformation calculations include Manolache [M]; [D] studies monad/module constructions. | This is a candidate specific formal-neighborhood classification, not a claim of only two global HM bundles. The restrictions, marking and determinant are indispensable. Classical ambient deformation/moduli statements are different. |
| An explicit canonical equivariant linear physical-positive family U_a in H⁰(B\|2Q(4)) restricts to aN and is square-zero; it lifts **aN**, not N. | Abo–Peterson [AP] §2.1 relates infinitesimal hyperplane-neighborhood sheaves to twisted nilpotent endomorphisms; Hulek–Van de Ven [HV] reconstruct HM from a double quintic-scroll structure. | Nilpotents and nonreduced geometry in bundle constructions are established. The candidate contribution is this particular marked quadric lift and its family-level canonicity. Canonicity of an induced family is not uniqueness of cochain representatives. |
| For indicated actual global primitives, corrected J3=(ah−qb)U_a−q²C_h in H⁰(B\|3Q(8)) has J3²=0. | [AP], [HV] are methodological/contextual precedents, not matching theorems. | Candidate specific third-neighborhood square-zero statement. It does not compute C_h, extend the midpoint bundle to 3Q, or show fourth-boundary vanishing. |
| Specific maximal rank-three Gauss profiles, including the entire (2,2) profile, are excluded; (1,1), (1,2), (2,1) remain necessary possibilities. | Laksov [L] treats associated bundles, stationary behavior, rank conditions and Plücker formulas; Boralevi [B] combines numerical restrictions with bounded resolution lists. | The project-specific equivariant exclusions may be original; derivative flags, degree bounds, ramification restrictions and finite candidate elimination are established approaches. Remaining profiles are not realizations, and rank three itself is not excluded. |
| Fixed scalar formulas, source-gauge corrections, endpoint scales, and Euler–Koszul splittings. | [D] includes explicit Koszul/self-dual monad descriptions and basis-dependent matrices; [AP] gives explicit homological algorithms. | Separate invariant conclusions from chosen-coordinate identities. A new normalization or a newly displayed coefficient is not automatically a new invariant theorem. Publish the choices and transformation law; explain which geometric statement survives them. |

## Primary sources and scope of examination

[D] Wolfram Decker, “Monads and cohomology modules of rank 2 vector bundles,” Compositio Mathematica 76 (1990), 7–17.
https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf
Read extracted text around Proposition 2 and the HM cohomology-module discussion, printed pp. 12–17, including the Koszul/self-dual monad construction and explicit resolution discussion. Some mathematical displays are lost in the PDF text extraction; this is not a full line-by-line technical verification. Supports precedence for HM module/monad calculations, not the precise present adjoint maps.

[HV] Klaus Hulek and Antonius Van de Ven, “The Horrocks-Mumford bundle and the Ferrand construction,” Manuscripta Mathematica 50 (1985), 313–335.
https://link.springer.com/article/10.1007/BF01168835
Read the publisher abstract only. It states that an appropriate normal line subbundle of a smooth surface yields a rank-two bundle with a section vanishing doubly, recovering HM from the quintic scroll. Full article was not examined; no claim that every possible overlapping statement has been ruled out.

[AP] Hirotachi Abo and Chris Peterson, “Implementation of Kumar’s Correspondence,” arXiv:math/0601423 (2006).
https://arxiv.org/html/math/0601423
https://arxiv.org/pdf/math/0601423
Read introduction and §2.1, plus selected example excerpts. In §2.1, modules on H_m correspond to sheaves on H carrying a twisted endomorphism φ with φ^m=0. This is a hyperplane construction, not the current singular-quadric extension theorem. The article attributes the underlying correspondence to N. M. Kumar (1997); Kumar’s original paper was not separately read.

[B] Ada Boralevi, “The Horrocks-Mumford bundle restricted to planes,” arXiv:math/0602002, version 2 (6 June 2006).
https://arxiv.org/pdf/math/0602002
Read abstract, Proposition 2.1, Corollary 2.2, and excerpts of the jumping-plane discussion. The work obtains six possible minimal resolutions, four stable and two unstable, and studies the associated Grassmannian loci. Its objects are plane restrictions, not twist-four adjoint restrictions to quadrics.

[M] Nicolae Manolache, “On the Normal Bundle to Abelian Surfaces Embedded in P⁴(C),” institute preprint 34/1985, June 1985.
https://imar.ro/~increst/1985/34_1985.pdf
Read introduction/construction excerpts and indexed Proposition 2 passage: the HM-containing moduli component is smooth of dimension 24 along the 24-dimensional SL₅ orbit, recovering earlier Decker results. OCR is poor; not a complete proof audit. This establishes a relevant older ambient-deformation context, not the marked two-root theorem.

[L] Dan Laksov, “Wronskians and Plücker formulas for linear systems on curves,” Annales scientifiques de l’É.N.S. 17 (1984), 45–66.
https://www.numdam.org/item/10.24033/asens.1465.pdf
Read introduction, including formulation through rank conditions on maps of associated bundles and stationary properties. No exact equivalence with the project’s Gauss-profile argument was proved. Appropriate methodological background, not evidence that the particular exclusions were previously known.

[W] Klaus Altmann, Andreas Hochenegger and Frederik Witt, “The Weil Decoration of the Horrocks-Mumford Bundle,” arXiv:2603.22979, submitted 24 March 2026, revised 4 June 2026.
https://arxiv.org/abs/2603.22979
Read bibliographic/abstract-level information; the version-1 introduction was also consulted. The work generalizes the relation between reflexive rank-one sheaves and Weil divisors to higher-rank reflexive sheaves via Weil decorations, with HM applications. **Weil decorations/Weil divisors are not the same notion as the project’s Weil Hodge classes.** Shared terminology does not supply a Hodge-class algebraicity result or show duplication of the current repair.

## Search and verification limits

Targeted searches combined Horrocks–Mumford with quadric/restriction, End/endomorphism/adjoint/symmetric square, Bockstein, formal extension, nilpotent, and Gauss. Broad osculating/Plücker searches supplied methodological context. Results were evaluated against primary papers or publisher records; irrelevant keyword collisions were not evidence.

This was not an exhaustive MathSciNet/Zentralblatt citation search, complete backward/forward citation audit, or consultation with an HM specialist. The project statements are taken from this paper and its immutable source ledgers. Correctness and novelty are independent questions.

## Positioning of the present work

Monadic and cohomological descriptions of the Horrocks–Mumford bundle, its restrictions, and constructions using nonreduced schemes have a substantial history. The focus here is the specified marked equivariant quadric problem: the actual twist-four adjoint multiplication pencil and its successive obstruction maps, together with the indicated nilpotent lifts on its infinitesimal neighborhoods. These results concern particular maps and marked objects, rather than a new general obstruction theory or a new construction of the Horrocks–Mumford bundle.

No blanket novelty or priority claim follows from this comparison. The exact generic section dimension, actual fourth obstruction and original Weil-class algebraicity objective remain unresolved. The latest asymmetric and Cartan refinements are summarized in [Chapter 26](26-asymmetric-quotients-and-coupled-cartan-frontier.md); the bounded source survey does not certify priority for those additions.
