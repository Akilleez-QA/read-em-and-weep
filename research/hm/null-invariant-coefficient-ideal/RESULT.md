# Determinant coefficient ideal and canonical-form multiplication

## Result

Let C be the stipulated smooth elliptic curve, X=C×C, Y=Sym²(P¹)=P², and p:X→Y the degree-eight quotient by G=W₂=(Z/2)²⋊S₂. Work in characteristic zero. Let χ(ε,σ)=ε₁ε₂ sign(σ), and let the square-zero parameter s transform by χ. For the stipulated nonzero translation bivector π, normalize the global top form Ω by Ω(π)=1.

Then the actual invariant square-zero coefficient ideal

    I=(p_*(s O_X))^G

is isomorphic to ω_Y=O_P²(-3), by the unique map Φ satisfying

    p*Φ(s f)=f Ω.                                         (1)

This is valid across all ramification, including infinity and ramification intersections. For invariant degree-zero functions a,b, the stipulated product m+sπ/2 satisfies

    Φ([a,b]_⋆)=da∧db,
    Φ(a⋆b-ab)=½ da∧db                                    (2)

in its original additive splitting. Thus the first-order multiplication really has the canonical ω-valued commutator, with coefficient one, not eight.

Qualification about “canonical”: the intrinsic choice-free statement is (p_*ω_X)^G≅ω_Y. Identifying the abstract one-dimensional representation kχ with H⁰(X,ω_X) requires a nonzero volume choice. The stipulated π makes that choice canonically by Ω(π)=1. The character by itself determines the line-bundle isomorphism class, not its scalar normalization.

For the specified two-pair external product, the actual mixed ideal is ω_z⊠ω_h=O(-3,-3). This does not identify the full root-transported unary maps, gerbe units, or an independently prescribed corrected ambient, and constructs no module.

## Sources actually inspected and limits

1. Historical context: [6265444022](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6265444022), which supplies genuine action after the ordered-cup gauge and explicitly leaves the invariant comparison open.
2. [research/hm/null-pair-swap-coherence/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/0050df8fa957b9f7f5e1b21137c63bffc646a1eb/research/hm/null-pair-swap-coherence/RESULT.md), especially §§3–6: parameter character, genuine group action, mixed external product, and limits.
3. [research/hm/null-actual-source-factorization/physical-factorization/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/physical-factorization/RESULT.md): exact stipulated product, identity overlaps before root transport, complementary supports, and actual external-product units. Its pinned physical formula source is [PR79 PROOF.md lines 35–82](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-second-order-raw-closure/PROOF.md#L35-L82). The present audit uses the already supplied static audit, not a new execution or certification of those physical formulas.
4. [research/hm/null-actual-source-factorization/classical-root/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/classical-root/RESULT.md): actual elliptic quotient, origin at infinity, full signed-permutation action, and the distinction between root inertia and canonical-volume character. Its carrier source is [the pinned carrier definition](https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md#L11-L15).
5. Universal mathematical references: [Stacks 0AX4, finite duality and evaluation at 1](https://stacks.math.columbia.edu/tag/0AX4); [Stacks 0FKW, finite relative dualizing module](https://stacks.math.columbia.edu/tag/0FKW); [Stacks 00R3, miracle flatness criterion](https://stacks.math.columbia.edu/tag/00R3); [Stacks 0C18, canonical sheaf and ramification divisor](https://stacks.math.columbia.edu/tag/0C18). The explicit invariant, ramification, and multiplication arguments below are given here, not delegated to these references.

Only static source reading and universal algebraic geometry were used. No physical source/model/jet evaluation, matrices, imports, physical-parameter search, experiments occurred. The symbols x,y below are universal curve coordinates for an algebraic proof, not executed physical leaves.

## 1. Finite duality proves the invariant canonical line globally

The quotient factors as the finite degree-four map C²→(P¹)² and degree-two symmetrization (P¹)²→P². Both X and Y are smooth surfaces. The finite map p is flat: at each local ring the regular target, Cohen–Macaulay source, and zero-dimensional fibers satisfy miracle flatness. Therefore B=p_*O_X is locally free of rank eight.

Finite duality, with canonical sheaves normalized over the ground field, gives the G-equivariant isomorphism

    p_*ω_X ≅ Hom_OY(B,ω_Y).

The action on the right is precomposition by the inverse G action on B. Let e=(1/8)Σ_g g be the Reynolds projection onto B^G=O_Y. A G-invariant functional ℓ satisfies ℓ=ℓ∘e, so it is uniquely determined by ℓ(1). Conversely any η∈ω_Y determines ℓ(b)=e(b)η. Thus evaluation at 1 is an isomorphism

    (p_*ω_X)^G → ω_Y.                                    (3)

This already proves a genuine line, globally, not only on the free locus. It includes all codimension-two intersections without any unproved extension assertion.

Normalization must nevertheless be fixed. Under duality the pullback p*η corresponds on the generic étale locus to b↦Tr_{K(X)/K(Y)}(b)η. Hence the duality trace (evaluation at 1) sends p*η to 8η. Equality holds globally since both sides are regular and agree generically. Therefore the inverse of pullback on invariant top forms is

    descent = (1/8) Tr_p,                                (4)

not unnormalized trace. In particular pullback itself is an isomorphism ω_Y→(p_*ω_X)^G. Equation (1) uses (4).

A nowhere-zero elliptic differential α is negated by inversion. For Ω=pr₁*α∧pr₂*α, inversion in either factor negates Ω and exchange negates Ω. Thus Ω has precisely character χ. Multiplication f↦fΩ is a G-equivariant identification O_X⊗kχ≅ω_X once the generator of kχ has been assigned to Ω. Combining it with (4) proves the claimed ideal identification.

Without a chosen Ω, let L=H⁰(X,ω_X), with its natural G representation. Evaluation O_X⊗L→ω_X is canonical. The canonical version is (p_*O_X⊗L)^G≅ω_Y. Writing L as the abstract character kχ suppresses a one-dimensional scalar choice. Normalizing against the already stipulated nonzero π resolves exactly this ambiguity.

## 2. Actual branch geometry and local check

Let the four branch values of x:C→P¹ be b₁,…,b₄, including infinity. On Y a point is an unordered effective divisor of degree two on P¹. The reduced branch divisor of p consists of:

- Four lines L_b: the divisors containing the specified branch value b.
- The diagonal conic Q: divisors of the form 2a.

Above the lines, the ramification components on X are the eight curves {r}×C and C×{r}, r∈C[2]. Above Q are the diagonal Δ and antidiagonal Γ_-={(a,-a)}. These are the fixed divisors of the reflections in W₂. Generic inertia on every component is order two, hence every component has ramification multiplicity one. No additional divisorial branch component occurs: a nontrivial stabilizer in codimension one must be one of these signed-permutation reflections. Intersections may have larger inertia, already covered by §1.

At a generic ramification component choose a transverse parameter z with reflection z↦-z and quotient parameter u=z², with tangent parameter w. A G-invariant form on the local double-cover part has the shape

    z h(u,w) dz∧dw = ½ h(u,w) du∧dw.

This exhibits why an anti-invariant coefficient vanishes on the ramification divisor without causing the descended canonical form to vanish. It is a Jacobian factor, not an extra downstairs divisor twist.

For a finite Weierstrass chart y²=F(x), take α=dx/y and Ω=(dx₁/y₁)∧(dx₂/y₂), so its inverse bivector is (y₁∂x₁)∧(y₂∂x₂). Write u=x₁+x₂ and v=x₁x₂. Deck-odd coefficients have form y₁y₂ h(x₁,x₂). Swap-oddness forces h antisymmetric, hence divisible by x₁-x₂, with symmetric quotient. Consequently

    (p_*O_X⊗χ)^G = J k[u,v],
    J=y₁y₂(x₁-x₂),
    du∧dv=J Ω,
    π(u,v)=J.                                          (5)

These are identities of coordinate rings; they remain true at finite branch intersections. Infinity is not omitted by the proof: it is one of the four lines in the branch description, and §1 proves the extension globally.

An independent degree check: multiplication of the χ coefficient line M with itself gives a map M²→O_Y. On the generic point of each of L_b and Q, its local generator squares to a unit times the branch equation, by z²=u. Elsewhere it is invertible. Therefore M²≅O_Y(-Σ_b L_b-Q)=O_Y(-6). Since Pic(P²)=Z with no 2-torsion, M≅O_Y(-3). This confirms the canonical-line degree and shows that ignoring the swap conic gives the wrong line. This calculation concerns ordinary multiplication in p_*O_X; within the square-zero ideal I itself all such products are zero because s²=0.

## 3. The actual invariant square-zero algebra and bracket

Let D=O_X⊕sO_X with product

    (a+sα)⋆(b+sβ)
       =ab+s(aβ+αb+½π(da,db)).

The action combines geometry with s↦χ(g)s. Because π has character χ, this action preserves the product. Its invariant direct image A=(p_*D)^G fits into an exact sequence of sheaves of k-algebras

    0 → I → A → O_Y → 0.

Exactness uses the finite-group Reynolds projector. I²=0. It is central, and its O_Y-module structure is well-defined independently of lifts because I²=0. In the specified original additive splitting, A=O_Y⊕I as k-vector sheaves. In fact this carries the evident coefficient-wise O_Y-module structure from that presentation, but inclusion of degree-zero functions is not an algebra map for ⋆.

Let a,b be local downstairs functions and choose their degree-zero invariant lifts. Their commutator is sπ(d p*a,d p*b). On a surface, with Ω(π)=1,

    π(d p*a,d p*b) Ω = d(p*a)∧d(p*b)=p*(da∧db).

Applying (1) proves (2). Since I is central, the commutator does not depend on the chosen lifts. In the original splitting multiplication is exactly

    (a,η)⋆(b,θ)=(ab,aθ+bη+½ da∧db),

where η,θ are canonical forms. This formula is associative because the wedge-of-differentials term is a Hochschild 2-cocycle; expanding d(ab)=a db+b da gives the cocycle identity directly. It describes the original invariant local multiplication. It does not assert that the original algebroid triple units are trivial merely because this local algebra can be written globally.

The term “ω-valued bracket” refers to the alternating biderivation O_Y×O_Y→ω_Y. It is not an ordinary scalar-valued Poisson bracket on Y, and no Jacobi operation with arbitrary ω-valued inputs is being asserted. The extension's commutator is the canonical wedge biderivation.

## 4. Quotient ideal is not a flat scalar deformation parameter

Upstairs D is flat over k[s]/s², but G acts nontrivially on that base. Its invariant base ring is

    (k[s]/s²)^G=k.

The element s itself is not invariant. Downstairs the surviving nilpotent ideal is the sheaf I≅ω_Y, not a globally generated trivial parameter line O_Y·s. Indeed H⁰(P²,I)=0. A globally defined flat first-order deformation of O_Y over scalar dual numbers would identify its reduction ideal with O_Y, which is incompatible with I≅O(-3). Locally one may choose a generator of I and obtain a local scalar dual-number description; such choices do not glue to a fixed global base parameter.

The invariant sheaf A is the total noncommutative square-zero extension. I is its kernel on reduction. The equality I≅ω_Y is neither A≅ω_Y nor an identification of invariant base rings with geometric coefficient ideals. This distinction persists under any equivalent presentation.

## 5. External product and the mixed ideal

Let X_z,X_h be the two pairs, Y_z,Y_h their P² quotients, B=Y_z×Y_h, and let s,t have their separate determinant characters. Use precisely the stipulated external product over k[s,t]/(s²,t²), with G_z×G_h and without quotienting further by block exchange.

On affine product opens finite pushforward is the external tensor product of the two finite pushforwards. The commuting Reynolds projectors e_z,e_h imply

    (M_z⊠M_h)^(G_z×G_h)=M_z^G_z ⊠ M_h^G_h

for the particular modules here. This is justified by the projector image, not a claim that arbitrary invariants commute with arbitrary tensor products over invariant rings. Therefore the four additive coefficient summands of the original invariant total algebra are

    O_B,
    L_z=ω_z⊠O_h,
    L_h=O_z⊠ω_h,
    K=ω_z⊠ω_h.

The last is precisely (p_*(st O_(X_z×X_h)))^(G_z×G_h), hence the actual mixed ideal. Its form identification sends st f to the descent of f(Ω_z⊠Ω_h), with each factor normalized as above.

Define J_s=(p_*(sD_total))^G and J_t analogously. Then, intrinsically,

    J_s∩J_t=J_s J_t=K,
    J_s²=J_t²=0,
    J_s/K≅L_z,       J_t/K≅L_h,
    (J_s/K)⊗_O_B(J_t/K) → K is an isomorphism.

The last map is induced by multiplication: (s a)⋆(t b)=st ab, since every correction has a second s or second t. Under the canonical-line identifications it is ordinary external tensor multiplication. The nilradical N=J_s+J_t satisfies N²=K and N³=0.

Do not call the full ideals J_s and J_t line bundles over O_B: each also contains K, and N acts nontrivially on them through the other pure ideal. Their pure quotients and K are the intrinsic O_B-modules just displayed. The original presentation has additive decompositions J_s=L_z⊕K and J_t=L_h⊕K, but this is not a reason to assign those splittings to a separately root-transported ambient. Likewise the invariant scalar base of this independently signed two-parameter quotient is just k; st by itself is not invariant under either separate character.

## 6. Exact boundary of this repair

This proves the actual coefficient-line and local multiplication part of the invariant comparison for the stipulated original coherent pair ambient and its stipulated external product. The global ramification and determinant character have been accounted for, and the bracket normalization is fixed.

Conjugation/root-Morita changes of ambient can alter unary overlap maps, additive splittings, and triple units. At first square-zero order the commutator is preserved by an equivalence inducing the identity on reduction and coefficient ideal; this is not identification of the equivalence or its coherence. Even a matching bracket and matching coefficient line do not fix gerbe data, full Hochschild/Čech representatives, or mixed cross terms after transport.

Still required for the proposed corrected downstairs model: actual quotient-atlas and equivariant overlap-bimodule hypotheses, their restriction-compatible effectiveness, and comparison of all unary maps and actual central triple units through st, with compatible reduction and chosen normalization. No full unary/gerbe/HKR identification, mixed module existence, or vanishing of an obstruction follows here. All thirty retained physical values remain unknown.
