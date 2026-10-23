# One-sided c-d-f preservation gives a raw three-dimensional cubic gate

## Result and precise hypothesis

Assume an actual source127 c-d-f occurrence and the one-sided condition Q(X_B)⊂Y_B in the simultaneous constant-block normal form. Here Q is the canonical invariant positive quadratic product, and T_a is the same actual negative quadratic family used in the original Bocksteins. Let S=[X_B→Y_B], M=[X→Y], and T=M/S, with the full differential Q+tT_a.

Then the internal second Bockstein of S vanishes globally on its surviving D. There is a canonical internal third symbol

    r:D O(-3)→E on X=P(A),
    0→A O(-1) --multiply by a-->D O→E→0.

The equivariant Hom space containing r has dimension THREE. Every nonzero member of this raw space is generically onto E. Consequently

    r≠0 iff the generic original fourth Bockstein is nonzero.

Neither alternative is selected. No assertion rκ=0, two-dimensional gate, secondary ν, source exclusion, or occurrence of one-sided preservation is made. The theorem re-establishes the exact interfaces in this c-d-f situation; it does not import a source126 full-radical compatibility hypothesis.

## Dependencies and exact reuse boundary

The preserved-B theorem is PR1001 at a7aa990e7705dd9dbf3d0fd34e437fa735c9e0f1, research/hm/cdf-preserved-b-symbol/PROOF.md, Git blob eebebae694f59e786aaebc64c3838d732b2a3832, copied as inputs/preserved-b.md. Its public original was independently fetched and authenticated; SHA256 e07a59e7b8e8d35b2f9a164515ff65eeddeca4baca4a0964c731b36b7713e38d. It proves the first-symbol/cohomology interfaces below from PR924/935 and the actual β₂ theorem.

The other inputs are exact immutable public proofs authenticated in INPUTS.json:

- PR979, db4c20c05f18d5e2494d99eb4c359828446919c9, research/hm/source126-typeII-internal-second/PROOF.md, blob 59e79d627214f092a4a9be9de6efe3448909e66d. Reuse only its UNIVERSAL rank-one exclusion for quadratic maps into E and its general correction method, not its full-J hypotheses or κ restriction.
- PR982, 25df67afcafd5f84c2c0cda7e6baee41fdbf8212, research/hm/source126-typeII-internal-third/PROOF.md, blob 9b1e90b99f24263b0e97f4d5721e04495454e9bf. Reuse only universal cubic Hom dimension, rank-one exclusion, and general normalization method; not third-order radical naturality or the two-dimensional conclusion.
- PR966, 4d0a6713a9c81fe669967e1d23838bdc8f4162b6, research/hm/source2-pureV-quadratic-discriminant/PROOF.md, blob 6197582777ccd6f8899ff16e16d335315fd52a99. Its universal map a·h followed by Sym⁶W→P has generic rank4. No source2 occurrence is assumed.
- Original third-zero theorem at db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-THIRD-BOCKSTEIN-VANISHES-IDENTICALLY.md, blob 7c09fe95015d7c8d932b3a27be302ca09888112d. It imports the same actual original β₂ generic rank3 with kernel D, and proves original β₃=0. Neither is a new computation here.
- PR924 at c6c25eaf0e5a67c27eee7c3ba4f000df55997692, blob 83f5aee293995257459229e6b323522224ce8f3d, supplies the negative-pencil algebra used only to explain the absent extra naturality hypothesis in Section5.

## 1. Actual interfaces, not analogy

The preceding one-sided c-d-f theorem proves

    H⁰(S)=H⁰(M)=A+D, H¹(S)=D,
    H⁰(T)=D, H¹(M)=H¹(T)=P.

The inclusion on H⁰ and projection η on H¹ are isomorphisms. The connecting map δ:H⁰(T)→H¹(S), defined by δ([x̄])=[Qx], is an isomorphism. Normalize the nonzero first internal A coefficient so that

    b_S,a(k,h)=a k,   k∈A,h∈D.

The quotient first symbol b_T is a nonzero scalar times h↦pr_P(a h). In particular it has generic rank4 by the universal theorem. The original β₂ is -b_T δ⁻¹ b_S. Thus, on the dense open where β₂ has rank3, its kernel is exactly D and its image is b_T δ⁻¹(aA). On the intersection with the rank4 locus of b_T, the induced map

    b̄_T:E(-1)→coker β₂

has rank one, with rank-one kernel. The scalar δ identification changes no rank or Hom-space assertion.

## 2. Construct and kill the global internal quadratic

Choose a G-equivariant right inverse H of Q_S onto its image. For h∈D the first internal symbol is zero, so

    u₁⁰(a,h)=-H T_a h,
    Q_S u₁⁰=-T_a h.

The class [T_a u₁⁰] in H¹(S)=D modulo aA is a global quadratic map

    s:D O(-2)→E.

Changing H adds a kernel-valued linear correction; its next class lies in aA, so s is independent of choices. This establishes global regularity and equivariance, including exceptional directions.

Every S¹ class maps to zero in H¹(M). Hence choose v₂∈M⁰ with Q_M v₂=-T_a u₁⁰. Its image in T is a Q_T-cycle with connecting class -[T_a u₁⁰]. Projecting its next error to H¹(T)=P gives the SAME original third differential:

    η β₃,M = -b̄_T δ⁻¹ s.

Here s is twisted by -1 before composing, so both sides have degree three. Changing u₁⁰ changes the expression only by the original second image, and changing v₂ contributes the globally zero original first symbol. This identifies actual page targets, not merely isomorphic representations.

The imported original third differential is zero. Therefore s has generic image in the rank-one kernel of b̄_T. But every nonzero equivariant quadratic map into E has generic rank two. For completeness, saturate a hypothetical rank-one image to O(k)⊂E. The source factor requires -2≤k≤1 and a D in Sym^(k+2)A, whose multiplicities are (0,0,1,0). Thus k=0, but H⁰(E)^G=0. The upper bound follows from H⁰(E(-2))=0 and more negative vanishings. On the smooth plane saturation is a line bundle by the depth lemma, and A5 has no character ambiguity. Hence s=0 generically and globally.

This argument uses NO κ naturality. In particular the separate one-dimensional quadratic subspace from the source126 radical theorem is unnecessary here.

## 3. Global cubic construction with choice independence

The vanishing of s says that the quadratic residual [T_a u₁⁰] factors through the injective multiplication subbundle A O(-1)→D O. There is a UNIQUE global equivariant linear A-valued polynomial k₁(a,h) with

    [T_a u₁⁰]=a k₁.

This is exact sheaf factorization, not division by a selected coefficient. Put u₁=u₁⁰-k₁, viewing A inside ker Q_S. Then

    Q_S u₁=-T_a h, [T_a u₁]=0 in H¹(S).

Set u₂=-H T_a u₁. It is quadratic and solves Q_S u₂=-T_a u₁. Define

    r_a(h)=[T_a u₂] modulo aA.

This gives r:D O(-3)→E globally. If two normalized u₁ choices differ, their difference is a kernel-valued linear polynomial whose A part is killed by multiplication by a; injectivity forces that part to be zero. The difference is D-valued. The resulting difference in r is an internal second class of that D-valued correction, already zero modulo aA. Altering u₂ by a quadratic kernel correction changes r only by aA. Thus r is canonical, equivariant, and independent of H and every lift.

## 4. Three-dimensional ambient space and exact fourth comparison

On the five A5 conjugacy classes of sizes (1,15,20,12,12), put

    χ_A=(3,-1,0,φ,1-φ), χ_D=(5,1,-1,0,0), φ=(1+√5)/2.

For h_n=χ_SymⁿA use h_n=χ_A h_(n-1)-χ_A h_(n-2)+h_(n-3). The defining exact sequence for E and plane H¹(O(n))=0 give χ_H⁰(E(n))=χ_D h_n-χ_A h_(n-1). Taking its inner product with χ_D for n=3 yields

    dim Hom_G(D O(-3),E)=3.

Every nonzero such map has generic rank two. Indeed a hypothetical saturated rank-one image O(k) has -3≤k≤1. The D multiplicities in Sym^(k+3)A are (0,0,1,0,2), leaving k=-1 or k=1. The first needs H⁰(E(1))^G≠0, which is false by the same characters; the second needs H⁰(E(-1))≠0, which is false by the exact sequence. This is the universal PR982 rank-one exclusion, independent of any radical action.

Use the normalized S corrections u₁,u₂ also in M. Since H¹(S)→H¹(M) is zero, choose v₃∈M⁰ with Q_M v₃=-T_a u₂. Its quotient cycle has δ class -[T_a u₂]. Therefore on the dense open with the stated constant ranks,

    η β₄,M = -b̄_T δ⁻¹ r.                       (★)

Both sides have degree four after twisting r by -1. The original first and third differentials vanish; quotienting by the original second image is exactly what kills the aA ambiguity. The displayed corrections are actual allowed representatives of the original fourth, so (★) is not a replacement obstruction.

One can check omitted terms in a reduced triangular complex with differential [[s(t),δ(t)],[0,q(t)]]. After the normalization, s₁|D=s₂|D=0. The quartic coefficient of the Schur complement -q(t)δ(t)⁻¹s(t) is -q₁δ₀⁻¹s₃ on D; every other term contains s₁ or s₂. Thus no higher quotient or connecting correction has been dropped.

If r=0, (★) gives generic original fourth zero. Conversely if (★) is zero, r has generic rank at most one, hence r=0 by the universal exclusion. Equivalently any nonzero r is onto E generically, so its composite with the rank-one b̄_T is nonzero. This proves precisely the claimed equivalence, not either side's actual value.

## 5. Why there is no justified two-dimensional reduction here

PR982 obtains its extra condition rκ=0 from a chain map j:T→S for the entire perturbed family, with j⁰ nonzero on D and j¹ zero on P. Its existence there comes from the full compatible radical. One-sided preservation here supplies an exact sequence of complexes but no such reverse map.

More specifically, no nonzero reverse map is induced by the fixed negative LINEAR pencil in the c-d-f normal form. If a full negative-pencil map N/N_B→N_B existed, composition with quotient and inclusion would be a negative-pencil endomorphism that kills N_B and has image inside N_B. PR924's entire represented algebra consists of scalar vertices F,B,L with its only radical arrow L→F. The B vertex is isolated. The image/vanishing conditions force all three scalars and the L→F arrow to zero. Hence that composite, and therefore the reverse map, is zero.

This does not rule out every possible two-term quadratic-family map constructed by other means. It proves that the specific full-negative-pencil radical mechanism cannot be imported. There is accordingly no established rκ=0 in this packet, and the only justified ambient cubic parameter count is three. No claim says all three parameters are realized, or that other actual geometry could not impose another relation.

The theorem stops at this raw cubic gate. No actual scalar, direction, matrix, rank or higher coefficient is evaluated; no secondary ν is asserted by the arguments given here; no source or pair is excluded. The hypothesis Q(X_B)⊂Y_B and the original fourth value remain open.
