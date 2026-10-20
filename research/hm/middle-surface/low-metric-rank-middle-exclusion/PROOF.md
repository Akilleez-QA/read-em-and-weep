# Residual-rank-one middle surfaces cannot have generic metric rank at most two

## Theorem

Work over C. Let V have dimension five and let f:V³→J be a fixed outer-symmetric, cyclic-zero trilinear operation. Assume that for every nonzero u the repeated map A_u:V/Cu→J, r↦f(u,u,r), is injective. Write U=O_{P(V)}(−1), E=(V⊗O)/U, and let Q be the residual middle map defined below.

Then the following statements hold on reduced supports.

1. The locus D₁ where residual rank is one is closed and projective: residual rank zero is impossible.
2. On D₁ there is a regular, everywhere surjective line-valued quadratic h:Sym²E→M, with rank-nine kernel K, and local actual corrections K→E⊗U. On squares their splitting changes lie in the square's own line tensored with U.
3. The closed locus D_low⊂D₁ where the quadratic-form rank of h is at most two has dimension at most one.

In particular no integral projective middle surface with surface image in P(V) can be generically residual rank one and generically metric rank at most two. Metric rank and residual rank are different: throughout D₁ the residual rank is exactly one, while h can have quadratic-form rank 1, 2, 3, or 4.

Under the separately established hypothesis (H), that the projective rank-drop middle support has dimension at most two, and the imported higher-residual-rank fiber bounds, every affine independent-zero component of dimension eight must have a two-dimensional middle image of residual rank one and generic metric rank at least three. The low-metric-rank portion has affine dimension at most seven.

## 1. The residual map and rank-zero exclusion

Repeated injectivity gives a rank-four subbundle

    A:U²⊗E → J⊗O_{P(V)},     I=im A.

Its quotient J/I is locally free. Locally choose a splitting s:E→V⊗O. The map

    Q_s:U⊗Sym²E → J/I,
    u⊗ab ↦ f(s(a),u,s(b)) modulo I

is independent of s: changing s by d:E→U adds two repeated-image terms, and the term with two added middle vectors is zero. Thus Q_s glues to Q. Its rank≤1 locus is closed, defined by the two-by-two minors.

At a point of residual rank zero, trivialize U and choose a splitting. Every middle numerator lies in im A_u, and its unique inverse defines a linear correction v:Sym²E→E. This correction has no compatible square: for e≠0, v(e²) cannot lie in Ce. Indeed, if it did, f(e,u,e)=−2A_e(u) would make A_e(u) proportional to A_u(e). Both are nonzero by repeated injectivity, so write A_e(u)=cA_u(e) with c≠0. Outer symmetry and the cyclic identity give

    A_{u+te}(e)=A_u(e)−tA_e(u).

At t=c^(−1), this vanishes despite e being independent of u+te, contradicting repeated injectivity.

On P(E)=P³, v(e²) modulo Ce is a nowhere-zero section of (E/O(−1))⊗O(2). Its top Chern class is 15H³, as follows from

    c((E/O(−1))⊗O(2))=(1+2H)^4/(1+H).

A nowhere-zero section of a rank-three bundle has rank-two locally free quotient and forces its third Chern class to vanish. This contradiction excludes every residual-rank-zero point.

Consequently D₁=(rank Q≤1)_red is closed projective. No extension of a correction through an actually existing rank-zero point is claimed or needed: there are no such points.

## 2. Regular metric and exact correction weight

On D₁, Q has constant geometric rank one. Because D₁ is reduced, its larger minors vanish as functions; locally an invertible rank-one minor puts Q in split constant-rank form. Thus its image T is a line subbundle and its kernel is locally free. Define M=T⊗U* and untwist Q to obtain

    h:Sym²E → M,      K=ker h,      rank K=9.

This h is everywhere surjective. The associated symmetric bilinear map E→E*⊗M defines its metric rank, whose rank≤2 locus is closed by minors. This defines D_low, with reduced structure if necessary.

For each local splitting s, the numerator on U⊗K lands in I. Inverting A:U²⊗E→I gives a regular map

    U⊗K → U²⊗E,

or equivalently v_s:K→E⊗U. This establishes the U twist, without choosing a global middle vector. Under s↦s+d, the change on ab is d(a)b+d(b)a, and on e² it is 2d(e)e∈Ce⊗U. These formulas include the middle-line weight and all scalar factors. The preceding repeated-pencil argument proves square avoidance for these actual corrections at every point of D₁. All constructions commute with pullback.

## 3. A finite isotropic-hyperplane cover

Suppose an integral projective surface B maps to D_low with a two-dimensional middle image. It suffices to treat the case that B is a reduced closed integral surface in D_low, but allowing an arbitrary such morphism does not change the argument. Restrict U,E,h,K to B.

Let Z⊂Gr_B(3,E) be the zero locus of Sym²R_univ→M. This is projective over B. A nonzero rank-two quadratic in four variables over an algebraically closed field factors as ℓ₁ℓ₂ with distinct linear factors. An isotropic hyperplane must be ker ℓ₁ or ker ℓ₂: its polynomial coordinate ring is a domain, so the product restricts to zero only if one factor does. A rank-one quadratic ℓ² has the unique isotropic hyperplane ker ℓ. Since h is nowhere zero, these are all geometric fibers. Their underlying sets have respectively two or one points; fiber schemes need not be reduced.

Therefore Z→B is quasi-finite and proper, hence finite. Choose a reduced irreducible component C dominating B. Its generic degree d is one or two, since characteristic zero makes its function-field extension separable and its geometric generic fiber has at most two points. The finite map C→B is surjective. Take a smooth projective resolution S→C (including normalization if needed). The composite p:S→B is proper and generically finite of degree d; it need not be finite or étale.

Pullback of the Grassmannian tautological exact sequence gives a genuine rank-three subbundle R⊂p*E with line-bundle quotient N, and Sym²R⊂p*K everywhere. This remains true over exceptional curves and rank-two-to-rank-one degeneration. No radical subbundle or extension of rational factors is assumed.

## 4. The square-avoidance section and its Chern class

Suppress pullbacks to the smooth projective surface S. Write

    a=c₁(U*),   n=c₁(N),   r=c₁(R),   z=c₂(R).

Let π:Y=P_S(R)→S parameterize lines, with L=O_Y(−1) and ξ=c₁(L*). Restrict each actual correction to L²⊂Sym²R⊂K and project E→E/L. The splitting-change term lies in L⊗U, so these local maps glue to a section of

    F=(π*E/L)⊗π*U⊗L^(−2).

Square avoidance makes this section nowhere zero at every point. Hence c₃(F)=0 in CH³(Y).

Because 0→U→V⊗O_S→E→0, c₁(E)=a and c₂(E)=a². Terms of base codimension three vanish. If Q'=π*E/L, then

    c₁(Q')=a+ξ,
    c₂(Q')=a²+aξ+ξ²,
    c₃(Q')=a²ξ+aξ²+ξ³.

The twisting line bundle has first Chern class t=2ξ−a. The rank-three formula

    c₃(Q'⊗line)=c₃(Q')+t c₂(Q')+t² c₁(Q')+t³

therefore gives exactly

    c₃(F)=15ξ³−10aξ²+5a²ξ.

The lines-convention projective-bundle relation is

    ξ³+rξ²+zξ=0,

because c₃(R)=0 on S. The integral projective-bundle direct-sum decomposition then gives

    15r+10a=0 in CH¹(S),
    15z−5a²=0 in CH²(S).

From 0→R→E→N→0,

    r=a−n,       z=a²−an+n².

Consequently

    15n−25a=0,
    10a²−15an+15n²=0.

These equalities are integral. In particular one must not remove the common factor five and assert an integral Picard identity without controlling torsion. Rationally they say 3n=5a and 3z=a², which force a²=0.

An exact integral elimination is also available. Multiply the second displayed relation by three, and subtract (15n−25a)(3n+2a)=0. This yields

    80a²=0 in CH²(S).

Thus deg_S(a²)=0. On the other hand, projection formula gives

    deg_S(a²)=d deg_B(c₁(U*)²)>0,

because B's middle map has surface image. This is the contradiction.

## 5. Dimension and equality-case consequences

If D_low had dimension at least two, an integral projective surface in a component (obtained by hyperplane sections when necessary) would contradict Section 4. Hence dim D_low≤1. This conclusion does not use (H), smoothness of D₁, or constant metric rank.

The imported universal K9 theorem bounds the separately projectivized independent-zero fiber over every residual-rank-one middle by three. Therefore the locus over D_low has separately projectivized dimension at most 1+3=4; restoring the three nonzero input scales gives affine dimension at most seven.

Under (H) and the imported bounds for residual rank at least two, an affine independent-zero component of dimension eight must have a projective middle surface B of residual rank one and generic fiber dimension three. Since B cannot lie in D_low, its generic metric rank is three or four. Its rank≤2 metric boundary, if any, has dimension at most one. The argument does not exclude that boundary or generic metric rank three/four, nor does it construct an affine dimension-eight component.

## Imports and scope

The proof directly verifies the extension and weights needed here rather than assuming a ternary support extension. It parallels the finite isotropic-plane construction in /research/hm/middle-surface/degenerate-ternary-surface-constraints/PROOF.md. The rank-zero eigenline obstruction appears in /research/hm/middle-surface/rank-one-boundary-support/PROOF.md, Section 7. Fiber and equality-case conclusions use /research/hm/universal-polar/rank-one-residual-fiber-model/PROOF.md and GLOBAL_FRONTIER.md; hypothesis (H) remains a separate input.
