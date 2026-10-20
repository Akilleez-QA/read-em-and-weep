# Prior mathematical audit

This audit concerns the source manuscript. It is not a formal verification or a review of later normalized publication bytes.

# Independent audit: rank-three excess-surface model

**Verdict:** The theorem in `PROOF.md` is valid as an abstract existence statement over C. No substantive mathematical gap was found in the supplied proof. This audit independently recomputes the key claims; it is separate from the author's “Audit and limitations” section. It is a mathematical review, not formal proof-assistant verification. No actual-source evaluation, external-service write, or numerical sampling was performed.

## 1. The seven-dimensional kernel and all its squares

Use the stated convention xy=(x⊗y+y⊗x)/2. The displayed seven generators of K are independent: six have distinct off-diagonal monomials and the remaining one is b²−a². The linear map on Sym²E associated to q has coordinates (r_aa+r_bb,r_cc,r_dd), so its kernel is exactly K and has dimension seven.

For e=Aa+Bb+Cc+Dd, membership e²∈K is exactly

    A²+B²=0, C²=0, D²=0.

Over C, a nonzero solution has C=D=0, B≠0 and A=±iB. Its tensor is B²(b²−a²)+2AB ab. Thus v(e²)=B²c is nonzero and outside Ce. This checks every square, including both projective square lines, rather than generic squares alone. The square-locus scheme need not be reduced for this argument: the required condition is about nonzero actual tensors.

The common-factor subspace aU is contained in K and killed by v. Its factors a and z∈U\{0} are independent. These claims are correct.

## 2. Explicit middle equations and two genuine plane components

The linear map h on Sym²V has image dimension seven. Its restriction to uE gives the entire E summand, while projection to C³ gives the surjective map q. It kills u². A further diagonal zero would require a nonzero e with e²∈K and v(e²)=−2x0e, which the preceding calculation excludes.

The loci S=([a],P(U)) and S'=(P(U),[a]) satisfy every equation and are disjoint. They have dimension two and lie in the locus where u,x,z are linearly independent.

Independently differentiating at ([a],[b+sc+td]) on the charts x_a=z_b=1 yields, in the order of the four E equations and three q equations,

    dz0, dx0, s dx0+dx_b, t dx0,
    dz_a+dx_b, s dx_c, t dx_d.

For s,t≠0 the independent conditions can be taken as dz0, dx0, dx_b, dz_a, dx_c, dx_d. Their rank is exactly six, leaving dz_c,dz_d free. Consequently the scheme's embedding dimension is two. Its local dimension is at least two because it contains S, and at most the embedding dimension. The local ring is therefore regular of dimension two. Over C this proves smoothness there, as well as generic reducedness. A proper closed subset of an irreducible component cannot have the same dimension as that component; hence S is itself a component. Swapping the factors establishes the same for S'.

This proves the existence of these two components. It does **not** classify all components of the middle fiber, and the theorem correctly does not claim such a classification.

## 3. Universal operation and exclusion of every other middle

The wedge map V⊗Λ²V→Λ³V is surjective, giving dim W=50−10=40. Wedging each summand of f0 shows that its image is in W. Outer symmetry is manifest, and cyclic summation cancels terms pairwise.

For V=Cm⊕E_m, the u² analogue is killed, the mE_m block maps injectively to A0_m(V), and the Sym²E_m block is twice its symmetric matrix in E_m⊗(m∧E_m). These blocks are independent, so dim F_m=4+10=14 and dim A0_m(V)=4. In particular F_m/A0_m(V) is naturally Sym²(V/Cm).

For r∈K the tensor B0_u(r)−A0_u(v(r)) has the displayed block matrix with lower block 2M(r). This proves both injectivity of its parametrization by K and L∩A0_u(V)=0. If r has rank at least two, the second-factor support has dimension at least two. If r has rank one, then over C it is a scalar square; its lower block has one-dimensional row space, and the top row −v(r) is outside that row space by the square-avoidance calculation. Thus every nonzero tensor in L has second-factor support dimension at least two.

Here “support” can be made precise as the image of contraction V*→Λ²V. This subspace lies in u∧E for tensors in L. If the tensor were also in F_m, the support would lie in m∧V. Two independent support vectors u∧w1,u∧w2 force

    m∈span(u,w1)∩span(u,w2)=Cu.

The implication follows by wedging each support vector with m. Independence of the two support vectors means w1,w2 are independent in E, so the plane intersection is indeed Cu. Therefore L∩F_m=0 for every [m]≠[u], without a generic-middle restriction.

## 4. Simultaneous globalization to dimension twenty

After quotienting by L, dim Wbar=33. Over P(V)\{[u]}, the images of F_m have constant dimension fourteen. They are the images of an algebraic bundle map of constant rank, so they form the asserted rank-fourteen subbundle. This justifies using its projectivization in the incidence argument.

For a fixed middle there are thirteen parameters for a line in that image. Thirteen-planes in a 33-space containing a fixed line form Gr(12,32), of dimension 12·20=240. Including the four-dimensional middle parameter gives incidence dimension

    4+13+240=257 < dim Gr(13,33)=13·20=260.

Although the middle parameter space is open rather than proper, this is sufficient: the closure of the image of a finite-type algebraic incidence has dimension at most 257. Its complement is a nonempty open subset. Thus no properness assumption is missing, and the avoidance holds for all other middles simultaneously.

Avoiding the fixed seven-space F_u/L is also a nonempty open condition, since 13+7≤33. The Grassmannian is irreducible, so these two nonempty opens intersect. For the inverse image T of such a thirteen-plane, dim T=7+13=20 and dim J=40−20=20. The intersection equalities T∩F_u=L and T∩F_m=0 elsewhere follow directly from the quotient construction.

The construction is existential at this step: it specifies a nonempty open set of acceptable quotients, not numerical coordinates for a chosen quotient. That suffices for the stated existence theorem.

## 5. Repeated-input injectivity, residual ranks, and exact fiber

Repeated-input images A0_m(V) survive injectively: for m≠u the whole F_m survives, while at u the lower-block argument gives L∩A0_u(V)=0. Therefore the residual image dimension is

    dim F_m − dim(T∩F_m) − 4 = 10 − dim(T∩F_m).

It equals three at u and ten at every other middle. The uniqueness assertion is exact and global.

With the specified symmetric-product convention, h(ue)=e and f0(u,u,e)=A0_u(e). Consequently both linear middle maps have kernel

    Cu² ⊕ {r−u v(r): r∈K}.

This also independently checks that no factor of two is missing in the graph correction. Equal kernels imply equal images of the dual maps, i.e. the same seven-dimensional space of scalar bilinear equations. Their pullbacks to P(V)×P(V) thus define the same ideal sheaf and the same scheme, not merely the same closed points. The two verified plane components transfer to f's middle fiber.

## Scope and gaps

- **No substantive gap found** for the stated abstract theorem.
- The argument does not supply a prescribed target representation, a normalizer action, equivariance, or an identification with any actual source operation. These are explicit limitations, not conclusions of the construction.
- If an equivariance condition makes residual rank invariant under a group acting on middle lines, that group must preserve the unique exceptional line in this construction. An action moving that line is incompatible with this specific model.
- The proof refutes a dimension-at-most-one conclusion derived solely from its listed abstract hypotheses. It does not refute a theorem using additional source-specific hypotheses.
- No claim is made about the full list of exceptional-fiber components or reducedness at every point.

**Audit date:** 2026-10-19 (UTC).
