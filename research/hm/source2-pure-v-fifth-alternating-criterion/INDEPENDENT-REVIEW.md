# Independent review: residual fifth criterion and all-orders continuation

## Conclusion and immutable binding

The combined theorem is sound under its stated residual-large actual-source hypotheses. This review binds to `PROOF.md` SHA256 `5d270f437e6ed0a5e297d68353d67408406fcaa52e8ff30723e7f38e5679e966` and `verify.py` SHA256 `a5998e9ddb61341b7259df63b106c0e9c8fbf7c4c108455bb174b96a49c8dab8`.

Conditional on R=0, the fifth vanishes exactly on the stated alternating isomorphism line. On that line the actual fixed normalization propagates polynomial corrections to all orders, so the original positive generic rank is36. Otherwise the first remaining exponent is5; nonzero R gives exponent4. No actual Schur value, occurrence of a branch, or realization of an arbitrary isomorphism is selected. The conclusion concerns the original 37-by41 component, not the full adjoint or the separated endpoint-sixteen mechanism.

## Actual separated-image factorization

The factorization of e0q through Gamma is justified by the actual equality QK=F4⊂NR4, not by an assumed Q-invariance of NR. The canonical A is killed by e0q and maps under Gamma onto the unique A constituent H_A. For the mixed preimage w=GT_a k(b,p), actual identities put w in J2: j2k=0 makes its q-preimage equation soluble, and j2w=B(a,b)p=0 follows from R=0 and the already proved symmetry of B.

The forced nonzero separated P correction identifies e0k with eta E8 rho_P, with eta nonzero. This is an actual nonvanishing result inherited from the common-kernel theorem, not a generic scalar assumption. These mixed preimages have separated Q images spanning M8(A⊗P), because rho_P is onto. The actual separated multiplication theorem makes M8 injective of dimension12. Since H/H_A also has dimension12, the induced xi is an isomorphism onto precisely that descendant space. Xi is therefore an actual equivariant isomorphism. The fixed choice E8 changes its scale and eta reciprocally, preserving the criterion.

## Independent normalization and diagonal audit

Independently of the production verifier, I reconstructed all three full formal channel maps from the authenticated universal model, retaining both quadratic arguments and every P coefficient. Their complete matrices have ranks5,4,3, respectively. Their alternating combination has rank12. Direct symbolic expansion verifies

    J_P+J_V-J_D = -3((a,b)_1,Ep)_2

and, after the required rho_P input and diagonal evaluation, gives exactly 60C2, 60C4 and 60(C2-C4). These are universal coefficient identities, not direction or source-instance evaluations.

The raw fifth lift is j2x3=-hT_a x2, with x1=-k and x2=GT_a k. Its H_A contribution is an allowed m-valued cubic gauge, not necessarily raw zero. The retained exact identity C4-C1/4=-m(a²,Ep)_4/720 gives

    [C]=-15 eta(lambda_P-lambda_V)[C1]
        -60 eta(lambda_D+lambda_V)[C2].

The classes [C1],[C2] are independent by the pinned fifth theorem. Equivalently span(C2,C4) meets the nonzero gauge line trivially. Consequently the zero criterion is exactly lambda_D=-lambda_V and lambda_P=lambda_V. All three coordinates can be nonzero on that line. The cancellation is literal in the diagonal cubic channel combination, not a mistaken inference from mixed nonvanishing. The original fifth comparison adds its stated endpoint sign without changing the vanishing equivalence.

## All-orders actual-map induction

The fixed normalization N is well-defined on J2 through its canonical isotypic A projector and the nonzero actual channel Gamma a_A=mu m. It preserves q and e0, remains in J2, and removes the entire A component of Gamma. Hence Gamma N=(xi|H')^{-1}e0q. This does not choose a horizontal residual splitting or extend h to other degrees.

The initial x0=s satisfies qx0=i_P, x0∈J2 and Gamma x0=0 by the sandwich identities. Suppose x_i lies in J2 and hT_a x_i=0. Then j4T_a x_i=T_a j2x_i=0, so y=-GT_a x_i exists. Applying h to its q equation gives j2y=-hT_a x_i=0, placing y in J2 before N is applied. Thus x_(i+1)=N(y) preserves the required q equation.

The genuine separated projection of any J2 vector is P-valued. Writing e0x_i=E8 v_i(a) therefore gives Gamma x_(i+1)=-Xi(a,v_i(a)). On the alternating line its evaluation at the same a is zero for every such polynomial P argument. It is essential that this identity holds for arbitrary v_i, not merely rho_P(a)p at the fifth stage. This proves the induction with fixed linear operators, preserving equivariance and homogeneity globally. No division by a direction-dependent minor or assumption that higher kappa gauges vanish is used.

As a consistency check, Q(J2)=ker h follows from hQ=j2 and dimensions: kerQ=A+I2 is contained in J2, so dim Q(J2)=36-8=28=dim ker h. The induction does not assume any larger Q-stable residual subspace.

Truncating the resulting strings at x23 supplies the authenticated finite criterion. A later finite pivot would make every nonzero maximal minor have order at least31, contradicting degree at most30. The existing lower pivots retain generic rank36. Since the original minors are polynomials in the pencil variable and all direction coordinates, their generic identical vanishing also proves rank at most36 everywhere on that fixed slice. This does not assert a constant special-fiber rank, or extend to other quadratic directions.

## Production replay and immediate-input authentication

The verifier was inspected and replayed normally and with Python optimization. Both 46-check outputs agree byte-for-byte with each other and with RESULT.json. Its abstract normalization matrices are correctly described as algebraic certificates, not actual source matrices. Reproduce with `python verify.py` and `python -O verify.py`.

All eight immediate public resources were freshly fetched at the exact manifest commits and paths during this review. Remote bytes match the retained input bytes, SHA256 and Git blob hashes:

| Input | Commit | Git blob |
|---|---|---|
| 1069 | `41bc20cade3198306c492c0c46399d71eb0d51c4` | `827cd956e2eb574fd7d40d408e0450c8581fd7d2` |
| 1089 | `f8dfebc8c12cbefd3b17422fa1220629e90af78e` | `7459702e0b6c28aa6605ca34e2cbd98a9d366417` |
| 1031 | `7150cf97eeebe473bcd7c61c1f968c73625d92ef` | `0694e96e2d17a53b68d625ec6065f8bf513cd083` |
| model | `7150cf97eeebe473bcd7c61c1f968c73625d92ef` | `a7ca4755e50c85fe7fc20a757125127a05de4056` |
| 1058 | `1435873de29d39e14ceee3de8d879e90f90b437a` | `3d42713aaaf4078e3a1b44d8eb3d9f545daa880c` |
| 1104 | `287a94911cdfec629529490e5c1642ddbe610b31` | `cf560b059d337f64a79a3f39ee7a962c27143843` |
| 1113 | `09b03061644e417b44b2ea97a00c73618794c268` | `923cdf608b02448fd24d2f415e06a22e5664ec73` |
| 1107 | `5b52eedce3420ccc3e407e97201bcdd056501bbf` | `a8f57401d93c296d23a5ed55cd09d8893222e7c1` |

Exact paths and SHA256 values are in INPUTS.json. Authentication covers these immediate inputs, not a fresh recursive reproof of their geometric ancestry. No actual source coefficients, parameter values, points, directions, jets or source-instance ranks were evaluated.
