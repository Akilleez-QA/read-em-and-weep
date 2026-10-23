# The canonical invariant product rules out one c-d-f compatibility branch

## Result and scope

Assume an actual c-d-f occurrence and the immutable hypotheses of PR927. Import the previously proved geometric character theorem for multiplication by the canonical invariant positive quadric q₀. No selected multiplication map or instance rank is newly evaluated.

The nonscalar positive-aggregate-compatible idempotent cannot have type (0,1,1,w), for any radical shear w. Only (0,1,0,0) remains possible. In particular, any nonzero B-source quotient row χ_B already forces the actual compatible algebra to be scalar. Otherwise the algebra is C² exactly when both cross-block aggregate maps vanish. In that residual case its invariant-product restrictions have forced kernels, images and cokernels described below.

This rules out an endomorphism-compatibility alternative, not the c-d-f source. The scalar alternative and the remaining C² branch are not excluded or realized. No frontier count changes.

## 1. Exact original inputs

All paths are in Akilleez-QA/read-em-and-weep. The two exact input files and their Git blob IDs are listed in audit-inputs/manifest.json.

1. PR927, commit 38235cda736a554ca2c16af504a56e1daf756624, research/hm/profile11-source127-cdf-aggregate-sharpness/PROOF.md, blob 4dd68998c565b3a34ac95bc8dfa447144a5c9d60. It gives the represented c-d-f algebra, aggregate generation, exact idempotent alternatives and their quotient-support criteria.
2. POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md, commit eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c, research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md, blob 019c1f31773476f0a4877d88632ce5d46fbd4b9f. The actual cone-spinor and preservation theorems prove the kernel character A+D for the canonical invariant positive product, hence image 2V+3P+3D and cokernel P. Its derivation is geometric and universal for the actual HM bundle; it is not a coefficient or matrix-rank experiment.

We retain every named representation's PR927 convention, in particular dimensions A=V=3, P=4, D=5. Let

    X=N₂=X_F⊕X_B,
    X_F=V+P+2D, X_B=A+V+2P+2D;
    Y=N₄=Y_F⊕Y_B⊕Y_L,
    Y_F=P+D, Y_B=V+2P+2D, Y_L=V+P.

These are normal-form coordinates. The seven-dimensional quotient Π=Y/im q_- is intrinsic; the complement Y_L is not declared canonical. An endomorphism e=(a,b,d,w) acts on X by a on X_F and b on X_B, and on Y by diagonal a,b,d with only off-diagonal map η_w:Y_L→P⊂Y_F. This map vanishes on the V constituent.

For the actual aggregate q_+:Sym²(T₊)⊗X→Y write Q:X→Y for its restriction to the canonical invariant positive line, represented by a nonzero q₀. Scaling that representative does not change its kernel/image/cokernel. Invariance makes Q G-equivariant. The second input proves exactly

    ker Q≅A+D, im Q≅2V+3P+3D, coker Q≅P.       (1)

The rank33 and kernel dimension8 are consequences of (1); they are imported results, not newly selected-instance evaluations. Since q₀ belongs to the positive quadratic space, every q_+-compatible endomorphism satisfies

    e₄ Q=Q e₂.                                  (2)

No converse to (2) is assumed.

## 2. A universal constituent bottleneck

Let p₀,p₁ be equivariant idempotents on finite-dimensional G-modules X,Y. If a G-map f:X→Y intertwines them, it restricts to maps

    ker p₀→ker p₁,     im p₀→im p₁.

For an irreducible ρ, semisimplicity bounds its image multiplicity by

    m_ρ(im f) ≤ min(m_ρ ker p₀,m_ρ ker p₁)
                +min(m_ρ im p₀,m_ρ im p₁).       (3)

Indeed the two source and target eigenspaces are direct sums, f is block diagonal, and the rank of each multiplicity-space map cannot exceed either endpoint dimension. This is a universal representation bound, not the evaluation of any actual multiplicity matrix.

If the image character equals the sum of these maxima for every irreducible, both block maps attain their maximal possible multiplicities. Their image, kernel and cokernel characters then follow by exactness. This does not specify the actual embedding of a repeated constituent or choose bases.

## 3. Exclusion of the scalar-target-supported idempotent type

PR927 proves that any nonscalar aggregate-compatible algebra is C² and has its unique idempotent with source scalars (0,1) of exactly one of the forms

    p_F=(0,1,0,0),    p_B(w)=(0,1,1,w).

Suppose p_B(w) is compatible. Its source kernel and image are X_F,X_B. Its target kernel is exactly Y_F; its target image is

    Y_B⊕{η_w(z)+z:z∈Y_L},

which is G-isomorphic to Y_B⊕Y_L. This accounts for every shear w, including zero, rather than pretending the off-diagonal action vanishes.

Apply (3) to ρ=V and f=Q. The source and target multiplicities are

    kernel block: 1→0,
    image block:  1→2.

Thus im Q could contain at most one V. Equation (1) says it contains two. This contradiction excludes p_B(w) for every w.

An equivalent dimension check uses the maximum image characters P+D from X_F→Y_F and V+2P+2D from X_B→Y_B⊕Y_L. Their total dimension is30, strictly below the known33. The constituent contradiction is the primary argument and remains unchanged by shear.

Combining with PR927 yields the exact remaining alternatives:

    D(q_+)=C·1,
    or D(q_+)=C·1⊕C·p_F.                         (4)

PR927's criterion now gives the complete actual decision rule:

- If χ_B is nonzero, D(q_+) is scalar, whether or not χ_F vanishes.
- If χ_B=0, D(q_+) is C² exactly when Q_FB=Q_BF=0; otherwise it is scalar.

Indeed only p_F can occur in a nonscalar algebra, and its equations are exactly χ_B=Q_FB=Q_BF=0. This is stronger than requiring both quotient rows nonzero. It does not assert that χ_F is always nonzero. If χ_F=0, the two V constituents in im Q force the invariant restriction of Q_BF on the V in X_F to be nonzero: otherwise that source V maps to no target V, leaving the sole V in X_B to supply at most one copy. That branch is consequently scalar as well.

This statement concerns compatibility on the fixed negative pencil and the positive aggregate. It neither demands nor asserts a full-module lift.

## 4. The precise invariant-product footprint of the surviving C² branch

Assume the second alternative of (4). For p_F the target kernel is Y_F⊕Y_L and the target image is Y_B. Hence Q splits into

    Q_F:X_F→Y_F⊕Y_L,
    Q_B:X_B→Y_B.

The maximum image characters allowed by equivariance are

    Q_F: V+P+D,       dimension12,
    Q_B: V+2P+2D,     dimension21.                (5)

Their sum equals the exact image character in (1). Each actual block multiplicity is bounded above by the corresponding entry of (5), and their sums equal those upper bounds for every irreducible. Thus equality must hold in both blocks. It follows that

    ker Q_F≅D, im Q_F≅V+P+D, coker Q_F≅P;
    ker Q_B≅A, im Q_B=Y_B, coker Q_B=0.          (6)

The displayed equality im Q_B=Y_B is an actual surjectivity consequence, not just a representation isomorphism. In contrast (6) does not select which copy of D is the kernel inside X_F or which P line in the target multiplicity space is the F-block image.

There is also a forced quotient-support statement. The only V in Y_F⊕Y_L lies in the quotient Π, since Y_F has no V. Therefore the restriction of the invariant quotient product to the unique V in X_F is an isomorphism onto Π's V constituent. This does not force its P component to be nonzero: the single image P can have zero or nonzero projection to the P in Π. The full aggregate χ_F is onto Π by PR927 when χ_B=0, but its non-invariant quadratic channels may be needed to supply that P.

The total kernel A+D in (1) therefore separates across the two source blocks as D in X_F and A in X_B whenever the residual nonscalar branch occurs. This is a conditional structural footprint that subsequent theorems can test without assuming a global splitting.

## 5. What this adds to the preceding formal sharpness theorem

PR927's three formal aggregate maps satisfy only its explicitly listed interface. The new invariant-product theorem was not among those hypotheses. Those original formal maps send every positive quadratic into Y_L, whereas the actual Q has image character (1), so they are not counterexamples to the new result.

Likewise admitting positive-linear factors through the correct K₄⁺ representation does not force the actual invariant product or all marked mixed equations. The factorization theorem and this branch theorem answer different missing dependencies: the former realizes a weaker formal interface; the latter uses an additional actual geometric input to rule out one actual compatibility type.

No assumption says c-d-f must possess any nonscalar compatible idempotent. The scalar option remains; even the surviving idempotent need not lift through every parity or degree. Therefore exclusion of p_B(w) does not exclude c-d-f, remove a source-dual pair, or resolve actual-HM membership. No selected source parameter, point, coefficient, derivative, matrix, numerical rank or large computation is used.
