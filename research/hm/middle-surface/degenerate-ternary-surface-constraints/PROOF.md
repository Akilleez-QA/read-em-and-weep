# Every generically degenerate ternary middle surface: isotropic-cover constraints

## Result and hypotheses

Work over C. Let B be an integral projective surface, with regular subbundles U ⊂ H ⊂ V⊗O_B of ranks 1 and 4, where dim V=5. Put E=H/U, N=V/H, a=c1(U*), n=c1(N). Assume the actual fixed-family and repeated-input-injectivity hypotheses of the intrinsic metric extension theorem, including the support-valued correction on a dense good open. Thus that theorem supplies:

- a surjective, everywhere nonzero metric h:Sym²E→M with M a line bundle;
- local regular actual corrections v_s:ker h→E⊗U, whose splitting change on a square r² is 2r d(r), and hence lies in Cr⊗U;
- square avoidance: v_s(r²) does not lie in Cr⊗U for every nonzero isotropic r at every geometric point.

Assume the generic rank of h is at most two. It need not have constant rank: generic rank two and rank-one boundary points or curves are allowed. Assume also that the middle map B→P(V) has surface image, equivalently A=∫_B a²>0. All intersection products on a singular B below mean intersections of Cartier divisor classes with [B].

Then necessarily

    2A − B₁ + C = 0,      B₁=∫_B an, C=∫_B n².

In particular a and n are not numerically proportional. This excludes every such generically degenerate middle surface with constant support H, or with support polarization numerically proportional to the middle polarization. If the Cartier numerical divisor space of the original B is one-dimensional, it is excluded too; this statement uses proportionality on B, not a supposed Picard-number invariance under resolution.

More precisely, there are a finite surjective integral cover q:C→B of generic degree d∈{1,2} and a smooth projective resolution ρ:S→C such that f=qρ:S→B carries a rank-two subbundle R⊂f*E with Sym²R⊂ker(f*h). Let P⊂f*H be its inverse image and p=c1(det P*). On S (suppressing f* on a,n),

    7p=9a+3n in Pic(S),
    7c2(R)=a²+n² in CH²(S),
    30(2a²−an+n²)=0 in CH²(S).

Thus the quadratic equality holds rationally in Chow and integrally as an equality of degrees. If the original B is smooth, projection formula further gives

    30d(2a²−an+n²)=0 in CH²(B),

and hence the uniform integral torsion identity 60(2a²−an+n²)=0 on B. The numerical conclusion does not require smooth B.

The cover q is finite; f generally is only proper and generically finite. No étale assertion is made across rank-one degeneration, nor is a degree-two choice necessarily needed when the generic conic already splits.

## 1. Choosing an isotropic plane without losing rank-one boundary points

Let G=Gr_B(2,E), with universal rank-two subbundle R_G. Let Z⊂G be the closed zero locus of Sym²R_G→M. It is projective over B. Because rank h≤2 holds on a dense open and rank≤2 is closed, it holds everywhere. The surjectivity of h excludes the zero form everywhere.

Over an algebraically closed field of characteristic zero, a nonzero ternary quadratic of rank two factors as a product ℓ₁ℓ₂ of distinct linear forms. A two-dimensional linear subspace on which the quadratic vanishes must be one of ker ℓ₁ or ker ℓ₂: its polynomial coordinate ring is a domain, so the product restriction can vanish only when one factor vanishes. At rank one the quadratic is ℓ², and its unique isotropic plane is ker ℓ. Consequently every geometric fiber of Z has a finite underlying set, of cardinality two or one. The scheme fibers may be nonreduced at rank one; no reducedness or flatness claim is needed. In particular Z→B is quasi-finite, and being proper it is finite.

Choose an irreducible component of Z dominating B, with its reduced structure C. It exists because Z has a nonempty generic fiber. Its image is all B, by properness. Its generic degree is at most two: over the function field a rank-two ternary form has a one-dimensional radical, and the residual binary form acquires an isotropic line over an extension of degree at most two. A rank-one form has a unique isotropic plane already defined over the function field. Equivalently the reduced geometric generic fiber has at most two points and characteristic zero makes the field extension separable.

The restriction of R_G is a genuine subbundle on C: its quotient remains locally free because both are pulled back from the Grassmannian universal exact sequence. Normalize C and take a projective resolution S; the composite f:S→B is proper generically finite of the same degree d. Pullback retains the rank-two subbundle R⊂f*E, with locally free quotient T=f*E/R. The equation Sym²R⊂ker(f*h) holds scheme-theoretically, since C lies in the zero locus Z. The actual corrections and their identities pull back, including square avoidance at exceptional curves; those identities hold in every fiber and are not generic assertions.

This construction handles rank-two-to-rank-one degeneration directly. It uses neither an extension of the radical as a subbundle nor a claim that the two planes remain distinct at the boundary. It also does not require extension of a normalized complement.

## 2. An isotropic-plane lemma, with no radical assumption

All bundles in this section are on S. Let π:Y=P_S(R)→S parameterize lines, L=O_Y(−1), ξ=c1(L*), u=c1(U), e=c1(E), r=c1(R). On L²⊂Sym²R⊂ker h, project the correction modulo L. The shear lands in L⊗U, so these local maps glue and square avoidance makes the resulting section of

    F=(π*E/L)⊗π*U⊗L^(−2)

nowhere zero. Therefore c2(F)=0. Its expansion and the projective-bundle relation are

    c2(F)=c2(E)+ue+u²+(3e+5u)ξ+7ξ²,
    ξ²+rξ+c2(R)=0.

The integral projective-bundle direct-sum decomposition then gives

    3e+5u=7r,
    c2(E)+ue+u²=7c2(R).

The flags U⊂P⊂H⊂V⊗O_S have ranks 1,3,4,5. Hence

    e=a−n, u=−a, r=a−p,
    c2(E)=a²−an+n²,
    c2(R)=a²−ap+p²−pn+n².

These yield 7p=9a+3n and 7c2(R)=a²+n². To verify the integral elimination without dividing in Chow, the second identity is

    −6a²+7ap−7p²+7pn−6n²=0.

Multiply by seven and substitute 7p=9a+3n in every resulting term. The result is −30(2a²−an+n²)=0. The Picard equality is the actual line-bundle identity

    (det P*)^7 ≅ (U*)^9⊗N³.

At no point was R=rad(h) used. Total isotropy Sym²R⊂ker h is exactly the needed input.

## 3. The recovered Grassmannian map, nefness, and binary alternative

The section of F is a line subbundle

    K=L²⊗π*U^(−1) ⊂ π*E/L.

Let W be its inverse image under π*H→π*E/L. It is a rank-three subbundle of V⊗O_Y with filtration factors π*U, L, K. Consequently det W=L³. The map g:Y→Gr(3,V) satisfies g*O(1)=O_Y(3). Thus ξ is nef and semiample, and R* is nef. Also

    π_*(ξ³)=r²−c2(R)=p(n−a)−n²
             =(3a²+2n²)/7 in CH²(S)_Q.

Since a,n are nef and ∫_S a²=dA>0, ξ³ has positive degree. Hence g has three-dimensional image and is generically finite onto that image.

Restrict the correction to Sym²R and project to T⊗U. The shear lies in R⊗U, so this gives a canonical binary quadratic β:Sym²R→T⊗U. It cannot vanish identically in any fiber: otherwise the correction on P(R_x)=P¹ would have its square-avoidance section in (R_x/L)⊗U_x⊗L^(−2), a line bundle of degree three, which cannot have a nowhere-zero section.

Its discriminant δ is a section of D=(det R*)²⊗(T⊗U)², and

    d₀=c1(D)=4p−4a−2n,      7d₀=8a−2n.

If δ is not identically zero, its zero divisor is effective (possibly empty), giving ∫_S ad₀≥0. By scaling all intersection numbers by d and using the quadratic identity, the original surface satisfies

    2A≤B₁≤4A,      0≤C≤2A.

If δ vanishes identically, β is everywhere rank one. Its radical is a line subbundle S₁⊂R, with

    (R/S₁)²≅T⊗U,      S₁²≅(R/S₁)⊗U,
    3c1(S₁*)=p.

For the second isomorphism, restrict the correction to S₁² and project to (R/S₁)⊗U; square avoidance makes this map nowhere zero. These alternatives concern β on the selected smooth cover. They do not assert that β, its radical, or its divisor descends to B. The unconditional numerical quadratic identity does descend.

## 4. Descent and the new exclusion

Projection formula for the proper generically finite map f gives

    ∫_S f*a f*n = d∫_B an,

and the analogous equalities for squares. Thus the integral degree of the torsion identity on S gives d(2A−B₁+C)=0 and therefore 2A−B₁+C=0 on B. For smooth B, pushforward of the full Chow identity gives the asserted 30d torsion identity. Resolution can add divisors, but cannot invalidate the pullback equalities or this projection formula.

If n=t a numerically on B for a real t, the equality becomes

    0=(t²−t+2)A=((t−1/2)²+7/4)A,

which is impossible when A>0. In particular constant support gives n=0 and is excluded. The same argument excludes one-dimensional N¹(B)_R, when this denotes Cartier divisors modulo numerical equivalence. One must not instead argue that a finite cover or resolution preserves Picard number: neither does in general.

The intersection matrix on the span of a,n has determinant

    AC−B₁²=−(4A²+3AC+C²)<0,

consistent with Hodge index. This is not an exclusion of every degenerate surface when a and n are independent.

## Exact frontier and next useful step

This result extends the previously audited rank-one surface exclusion to every generically degenerate ternary metric branch. It is conditional on regular support U⊂H and the actual supported correction; it does not itself establish support extension. It applies to entire complete surfaces, not to a degenerate boundary curve inside a generically nondegenerate surface. Generic rank-three metrics have no isotropic two-plane and are untouched.

The next useful bounded question is whether the two isotropic planes on the generic rank-two branch, after a common splitting cover, impose an additional relation beyond the identical Chern constraints for either plane. Their intersection is the generic metric radical, but it need not remain a line subbundle across rank-one degeneration. A valid strengthening must track the coincidence/degeneracy locus and its effective divisor or torsion correction, rather than assume a globally split pair of planes. Alternatively, analyze the rank-one binary β alternative on the isotropic cover; its line identities alone reproduce the same quadratic equation and are not a contradiction.

Mathematical inputs: rank-one ternary constraints and the intrinsic metric extension in the accompanying radical-constraint proof. The intrinsic-extension audit is retained separately.
