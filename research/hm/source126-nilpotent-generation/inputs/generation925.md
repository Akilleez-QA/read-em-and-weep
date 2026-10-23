# Degree-zero generation forces the c-d-f positive radical channel

## Result and scope

Assume an actual occurrence of the source127 c-d-f edge, with the simultaneous fixed-variable pencil identification of PR924. The aggregate positive-quadratic action has a forced surjective radical component:

    im(j4 q_+)=im j4=P

for every nonzero element j of the one-dimensional represented radical. Consequently the common-radical-kernel subpencil cannot extend with its prescribed intersections to a graded submodule of the actual five-variable cohomology module. Its radical-image subpencil does extend.

More generally, a negative-pencil endomorphism compatible with q_+ is determined by its two scalars on N2. The entire positive-quadratic-compatible subalgebra is therefore either the common scalar algebra C or a copy of C^2. We give the exact finite alternatives for its possible extra idempotent below.

The new premise is actual degree-zero generation, used through a parity-factorization identity. Scalar rigidity alone would not prove these assertions. No individual positive quadratic, actual source parameter, coefficient, point, matrix or instance rank is evaluated. This is a conditional necessary compatibility theorem, not a source exclusion, a realization of the abstract family, or a full-module lifting theorem.

## 1. Immutable inputs and actual grading

All paths are in Akilleez-QA/read-em-and-weep. The manifest and reproduction instructions authenticate three exact inputs.

1. PR476 at 3aa461bc3581fb72fbf923fbe869ddee023b435a, research/hm/five-generator-module/PROOF.md, Git blob 3d308f6fbdb5c224a085b41eec26e917a6031692. Section 3 proves the actual graded cohomological cover S_coord tensor K0 -> K. This is not merely a representation isomorphism or an abstract presentation with the same dimensions.
2. PR818 at f4a73af666900ad2cb34a756d24b88e19dd6feaa, research/hm/negative-truncation-extension/PROOF.md, Git blob 2ba0a7eee6ef2eb5413683e85618d7902dca3970. Section 1 fixes the actual inversion grading and negative-variable actions. Sections 4-5 define q_+, its necessary window-compatibility test, and the exact marked-submodule criterion. No source2-specific dimensions or splitting is imported.
3. PR924 at c6c25eaf0e5a67c27eee7c3ba4f000df55997692, research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md, Git blob 83f5aee293995257459229e6b323522224ce8f3d. Sections 2-4 give the entire represented c-d-f algebra, including singular endomorphisms and the simultaneous covariant identification with both actual negative tensors. Section 6 gives the nonzero P radical action used here. Section 7 gives the full intrinsic filtration dimensions.

Work over C. Write

    T_coord=T_+ direct-sum W, dim T_+=3, dim W=2,
    S_coord=Sym(T_coord),
    K_d=H1(End_0(F_HM)(d-1)),
    N2=K3^+, N3=K4^-, N4=K5^+.

Here T_+ is the inversion-even coordinate space and W is the inversion-odd coordinate space. Multiplication has its actual sign rule. The maps A_w:N2->N3 and B_w:N3->N4 are actual multiplication by the same w in W. Products commute because this is an S_coord-module.

The two even quadratic actions are

    q_+:Sym2(T_+) tensor N2 -> N4,
    q_-:Sym2(W) tensor N2 -> N4,
    q_+(pq tensor x)=m_p m_q x,
    q_-(uv tensor x)=B_u A_v x.                 (1)

The domain of q_+ contains all positive quadratics. Surjectivity of an aggregate component of this map is not a statement about one fixed quadratic.

## 2. The parity-factorization lemma

Let M be any graded module over Sym(T_+ direct-sum W), with compatible involution, generated in degree zero. For either sign sigma and every n>=3,

    M_n^sigma=Sym2(T_+) M_(n-2)^sigma
                 + Sym2(W) M_(n-2)^sigma.       (2)

To prove this, choose an involution eigenbasis of the coordinate space. Every monomial of degree n>=3 contains two variables of the same sign, by the two-class pigeonhole principle. Their product belongs to Sym2(T_+) or Sym2(W) and is inversion-even. Removing this pair leaves a monomial of degree n-2 with the same inversion sign as the original monomial.

The degree-zero cover Sym(T_coord) tensor M0 -> M is involution-equivariant. Taking an eigenspace is exact in characteristic zero, or directly by the projection (1+sigma iota)/2. Thus every element of M_n^sigma is a sum of images of monomial tensors with that total sign. Decompose the generator factor into its two eigenspaces as needed. Removing an even pair preserves the total sign including the generator factor; no assumption that all generators have the same parity is made. The remaining tensor maps to M_(n-2)^sigma. This proves the inclusion into the right side of (2); the reverse inclusion is the multiplication sign rule.

Apply (2) to the actual degree-zero-generated K, with n=5 and sigma=+. We obtain the exact spanning equality of actual images

    N4=im q_+ + im q_-.                         (3)

This is not a direct-sum assertion, a relation-free model, or a choice of a lift in the quotient. Relations cannot invalidate the equality because it is obtained by applying the actual equivariant cover to a spanning identity in the free module.

## 3. Forced positive radical channel

The PR924 algebra has coordinates e=(a,b,d,w), where w belongs to a one-dimensional space J, and multiplication is

    (a,b,d,w)(a',b',d',w')
       =(aa',bb',dd',a w'+d' w).               (4)

Its radical is J, realized as (0,0,0,w). For every nonzero j in J, the same actual covariant functor gives

    j2=0,
    j4:N4,L=V+P -> P subset N4,F=P+D,           (5)

with j4 a nonzero scalar multiple of the P projection and zero on the other N4 blocks. In particular im j4 is a four-dimensional irreducible P. This is the genuine represented action proved in PR924, not an arbitrary abstract radical with unknown component ranks.

Pencil commutation gives, for all u,v in W,

    j4 B_u A_v=B_u j3 A_v=B_u A_v j2=0.

Thus j4 annihilates im q_-. Applying it to (3) now proves

    im j4=j4(im q_+)+j4(im q_-)=im(j4 q_+).

Together with (5), this is the asserted surjection

    j4 q_+:Sym2(T_+) tensor N2 -> im j4=P.      (6)

In fact the full scalar-target projection of q_+ is onto N4,L=V+P. The block projector p_L=(0,0,1,0) belongs to C_N, has p_L,2=0, and acts on N4 as projection onto this scalar-target block. The same negative commutation gives p_L,4 q_-=0. Applying p_L,4 to (3) proves the asserted onto statement. The radical channel (6) is its further P projection.

The assertion holds for every nonzero radical element, and its intrinsic content is unchanged by rescaling j or changing normal-form coordinates. It uses degree-zero generation and actual negative commutation, not full-module scalar rigidity and not values of the missing positive tensor.

## 4. Exact marked-filtration consequence

Let U=JN and Vker=Ann_J N be the intrinsic radical-image and common-kernel subpencils. PR924 gives

    dim U=(0,8,4), dim Vker=(41,46,33),
    U subset Vker,
    Vker2=N2, Vker4=ker j4.

The PR818 marked-submodule theorem says that a negative subpencil X extends to a G-stable graded S_coord-submodule L with exactly

    L3 intersect K3^+=X2,
    L4 intersect K4^-=X3,
    L5 intersect K5^+=X4

if and only if q_+(Sym2(T_+) tensor X2) is contained in X4.

For U the condition is automatic because U2=0. For Vker it would require j4 q_+=0, contradicted by (6). Therefore U has a minimal marked extension, Vker has no marked extension, and the entire nested marked pair cannot extend.

There is also a direct check of the obstruction that does not use sufficiency of that criterion. Any graded submodule containing N2 at degree three contains both quadratic images in (3), hence all N4 at degree five. It cannot have degree-five positive intersection equal to the proper subspace ker j4. This verifies the same nonextension using generation alone.

No source theorem requires Vker to extend. The nonextension is thus a new obstruction to a specific route, not a contradiction to c-d-f occurrence.

## 5. At most one residual nonscalar compatibility direction

For any e in the fixed negative-pencil commutant C_N define

    Theta_+(e)=e4 q_+-q_+(1 tensor e2).          (7)

It vanishes on common scalars. Suppose e2=lambda identity and Theta_+(e)=0. Then e4=lambda identity on im q_+. The two negative commutation equations likewise give

    e4 q_-=q_-(1 tensor e2)=lambda q_-.

Equation (3) therefore forces e4=lambda identity on all N4.

In the exact algebra (4), e2 is scalar precisely when a=b=lambda, since its two nonzero blocks have dimensions 17 and 24 and the scalar-source block contributes zero. The N4 action has diagonal scalars a,b,d on blocks of dimensions 9,21,7, and the off-diagonal arrow w induces the faithful nonzero P map in (5). Hence e4=lambda identity then forces d=lambda and w=0. Consequently

    e2 scalar and Theta_+(e)=0
          imply e is the common scalar.         (8)

In particular Theta_+ is injective on the two-dimensional subspace a=b=0, with coordinates (d,w). This subspace also injects into C_N/(C identity). The latter quotient has dimension three, so the kernel of its induced compatibility map has dimension at most one. These are structural injectivity and dimension bounds, not ranks obtained by evaluating an actual compatibility matrix.

There is a sharper algebraic description. Let D_+=ker Theta_+. The identity

    Theta_+(ef)=e4 Theta_+(f)
                     +Theta_+(e)(1 tensor f2)

shows that D_+ is a unital subalgebra. The algebra homomorphism

    pi:D_+ -> C^2, e=(a,b,d,w) -> (a,b)

is injective by (8) with lambda=0, and its image contains the common scalar diagonal. A complex linear subspace of C^2 containing that diagonal is either the diagonal or all C^2. Therefore

    D_+ is either C identity or isomorphic to C^2. (9)

In the second case there is a unique p in D_+ with (a,b)=(0,1). Since pi is an injective algebra map, p^2=p. Writing p=(0,1,d,w), formula (4) yields

    d^2=d, d w=w.

Thus exactly the following finite types are possible:

    p=(0,1,0,0),
    or p=(0,1,1,w) for one w in J.              (10)

The proof does not choose between these types or assert that either is attained. In the second algebra case, uniqueness of p fixes w for the actual compatibility map; (10) does not assert that all w are simultaneously compatible. Both p and its complement then satisfy the positive-quadratic criterion, so their image subpencils have marked submodule extensions. Those extensions need not be complementary in other degrees or eigenspaces, and a full-module splitting is not inferred.

## 6. Remaining boundary

PR924 deliberately left the radical P-channel conditional. Equation (6) resolves that particular dependency using the additional generation argument, while leaving the already-reviewed algebra theorem unchanged. It does not determine the full positive tensor or prove that a positive-quadratic-compatible endomorphism extends through all five-variable window squares, much less through the entire module. The actual full module still has only scalar degree-zero endomorphisms by PR818.

The remaining concrete compatibility alternatives are (9)-(10), and the separate actual-HM membership problem for the abstract c-d-f family remains open. No premise forces the radical-kernel filtration, the proper idempotent in (10), or an ambient shear to extend to the full module. No source, source-dual pair, stable label or frontier count is removed by this theorem.
