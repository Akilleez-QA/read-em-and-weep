# Independent review: normalized actual scalar-channel projector

Verdict: PASS for the exact final proof identified below, relative to its
authenticated mathematical inputs. The actual-map argument establishes
tr(K_mult)=1/4 and K_mult^2=K_mult/4, identifies the primary V as the
image of the induced operator on E, and forces first-arrow image
character 1+2V+2D and dimension 17. No substantive gap remains in this
argument. This is a mathematical review, not proof-assistant verification.

Reviewed on 2026-10-23. No public writes or selected actual HM/source
instance evaluations were performed during this review.

## Exact reviewed artifacts

- PROOF.md: 12,423 bytes; SHA256
  `9e9fdc021f3c9dbec4f09dad1c0aa3e4a4a634227d6d65e50de7ac56fb88581b`.
- verify.py: SHA256
  `386629fb8240933905c46f4a087eb1704d4d53cb8c817e1e976355c55911b40e`.
- INPUTS.json: SHA256
  `74deb4e4adde9cd2f5b7258e7ba4620130d6c3f927027b6eb669a8ff0b2fa84e`.
- RESULT.json: SHA256
  `78ae557187faca317fb6ba3081841dc8836f21b8a0792346e80cb60737bf0f7c`.
- REPRODUCE.md: SHA256
  `227dc30190092e234bcfede646eac9dcacf15aa31233a4896372d2ae9adf9f5c`.

The initial version mixed a multiplicity line with the corresponding
three-dimensional actual V. This was corrected before approval:
K_mult acts on Hom_G(V,E), K_E=Id_V tensor K_mult acts on E, and
Q^-1 B0=E_prim=im K_E. Likewise V_s=V tensor ker s. Thus 4K_mult has
rank one on multiplicity space, whereas its induced projector on E has
rank three. The trace 1/4 in the theorem is the multiplicity trace, not
the trace of K_E. The final Section 6 also defines L_h explicitly.

## Independent original authentication

Every one of the five complete source originals was independently
fetched through the GitHub connector using its exact repository path
and immutable commit. The returned UTF-8 content was byte-compared with
the local copy. Byte length, SHA256, computed Git blob SHA1, and the
connector-returned Git blob all agree with INPUTS.json. Authentication
was not inferred merely from a supplied manifest or a local hash.

1. PR477, actual primary module injection:
   [original](https://github.com/Akilleez-QA/read-em-and-weep/blob/ff87076794e97238150485b12183c3cd0f4711e4/research/hm/adjoint-primary-extension/PROOF.md).
   Commit `ff87076794e97238150485b12183c3cd0f4711e4`;
   Git blob `1cb91b7f5b7da08b6653c7fa48487ff7c3fd7198`;
   SHA256 `0325c7b3cf237e27d4466e17c50cdb7f1a5cd874c310f32c03516acc250a2a38`;
   10,321 bytes.
2. PR1050, current monad and actual U=P:
   [original](https://github.com/Akilleez-QA/read-em-and-weep/blob/ec18a0fd62c4a9495adf6aad9564d379afc42b62/research/hm/canonical-negative-string/PROOF.md).
   Commit `ec18a0fd62c4a9495adf6aad9564d379afc42b62`;
   Git blob `8563bb31385dac0174b3d17bcae7bfa9dcfad716`;
   SHA256 `6c2f23ce2110ee91b05631e1e31932a5fe5ecb36e86731cb5e79518879f7b67d`;
   9,452 bytes.
3. PR1118, nonzero actual scalar second arrow:
   [original](https://github.com/Akilleez-QA/read-em-and-weep/blob/f794fb1295693e7d2d9067013e5bd019d2a284a9/research/hm/positive-middle-faithfulness/PROOF.md).
   Commit `f794fb1295693e7d2d9067013e5bd019d2a284a9`;
   Git blob `7aecc0dee5926977f4b7ce65e3ecef78c89506a3`;
   SHA256 `3e63ddf20c265068aa83dfd07db008437ca8a928e4699ce7060af281c5e668f5`;
   11,576 bytes.
4. PR1114, normalized repeated-V pencil:
   [original](https://github.com/Akilleez-QA/read-em-and-weep/blob/fc79bc119a251c16d386467333f55cd46dc75367/research/hm/repeated-v-channel-pencil/PROOF.md).
   Commit `fc79bc119a251c16d386467333f55cd46dc75367`;
   Git blob `ef68e9d6ce7583f2f146443f157ba895e2d16925`;
   SHA256 `4ecb2dfce5a532932e29063a4ee79c2431ab1c74b00c8a3eee16d6b9ddbf2e87`;
   12,440 bytes.
5. PR1120, preceding actual scalar cyclic-module slice:
   [original](https://github.com/Akilleez-QA/read-em-and-weep/blob/62587a0adde566cac718ee13c28ee13c239389e5/research/hm/scalar-cyclic-module/PROOF.md).
   Commit `62587a0adde566cac718ee13c28ee13c239389e5`;
   Git blob `af00766042cdc7e100731aa69b9ad8d32db0209f`;
   SHA256 `b47031d81c8c138aa5f1b4c4cee992f9ae04ee74adb8c403cedd2e74c51a2d2e`;
   10,894 bytes.

This authenticates the five immediate originals, not every transitive
historical reference. Their mathematical statements are inputs to the
reviewed theorem. PR1120 supplies explicit continuity with the preceding
slice; its global-levelness and complete-annihilator arguments are not
needed for the new normalized trace calculation.

## Mathematical audit

### 1. Actual primary injection, shifts, and parity

PR477 constructs its actual map from the evaluation Eagon--Northcott
resolution and Serre duality before proving injectivity. Its argument
specifically establishes graded polynomial-module compatibility, not
merely degreewise equivariant embeddings. Consequently polynomial
multiplication on L is Id_U tensor the primary multiplication.
The shift L_j=U tensor Aprim_(j-3), with K_j=H1(B(j-1)), places
primary degrees 0,1,2 in B-degrees 2,3,4 exactly as used.

The current normalized monad and its K-class are present in PR1050.
Acyclicity at twist zero gives Aprim_0=A+W'. At twists one and two,
the exterior Euler/Koszul complexes make the monad terms acyclic in
positive cohomology, hence Hq(F(t))=0 for q>=2. The primary h1
dimensions 10 and 10 from PR477, combined with the equivariant Euler
characters of dimension -10, imply h0=0. Thus the proof correctly
deduces actual primary characters, rather than identifying an Euler
character with H1 without a vanishing argument.

U=P is positive, and X=A and Z=P are the positive primary spaces.
The only possible positive target of V tensor Z in Aprim_2=1+A+T6
is Y=A, since V tensor P has no trivial summand. The degree and
physical parity conventions are consistent throughout. Polynomial
multiplication has no supercommutative sign introduced by these
representation parities.

### 2. H, B0, and the inverse-Q image are actual subspaces

The injected U tensor Z has precisely one scalar. Since the ambient
middle also has precisely one scalar, injectivity identifies this line
with the actual H. R-linearity puts its positive descendant B0 in
the primary target, and PR1118 supplies its nonvanishing. The primary
target has exactly one V, so B0 is that actual V.

The source primary subspace has one actual V, denoted E_prim.
If Q_X were zero, the actual Id_U tensor Q_X restriction would kill
E_prim, contradicting the full E injectivity of PR1114's actual Q.
Thus Q_X is nonzero; Schur's lemma on its irreducible source and
target of type A proves that it is invertible. This is not an
invertibility assertion based solely on equal dimensions.

It follows that Q(E_prim)=B0, and since Q on the full E is an
isomorphism, Q^-1 B0=E_prim. This supplies the needed actual
multiplicity location before any trace or scalar calculation.

### 3. Coevaluation and the factor 1/4

A nonzero h in H subset U tensor Z is a nonzero equivariant
isomorphism U* -> Z. Its induced identification U=Z* sends h to
Id_Z. Under the same identification the actual polynomial arrows
on U tensor X, U tensor Z, U tensor Y act by postcomposition.
In particular the transported scalar second-arrow embedding is
j(z)=Q_X^-1 b_z, not an unrelated isomorphic copy of V.

The invariant scalar projection on End(Z) is exactly
g -> (tr_Z(g)/4) Id_Z. It agrees with the restriction of the
ambient scalar projector because H is the same unique actual
scalar line. No complement choice can change this isotypical
projection.

The bilinear form beta(y,z)=tr_Z(a_y Q_X^-1 b_z) is invariant.
Uniqueness of the invariant bilinear form gives beta=c(y dot z).
For the very metric whose inverse quadratic defines Q, one has
q=sum_i e_i^2 and Q_X=sum_i b_i a_i. Rectangular trace cyclicity
therefore yields

    sum_i beta(e_i,e_i)
      = tr_X(Q_X^-1 sum_i b_i a_i)
      = dim X = 3.

The left side is c dim V=3c, so c=1. The normalized scalar
projection is consequently (y dot z)h/4. Applying the actual
second arrow and Q^-1 gives precisely
(1/4)(y dot z)j(x). This matches PR1114's F0(x,y,z)=x(y dot z)
with no averaging, symmetrization, or additional contraction factor.
All unknown primary-arrow scales cancel against the actual Q_X^-1.
The result uses dim X/(dim V dim Z)=1/4, not a selected evaluation.

### 4. Projector and exact first-arrow image

PR1118 gives rank K_mult=1 and identifies its image and kernel.
The nonzero image eigenvalue just proved is 1/4; the other is zero.
Hence K_mult^2=K_mult/4 and the canonical splitting follows.
The final proof correctly distinguishes multiplicity and actual
isotypical operators.

The two eigenvalues of Q^-1 C1 are -1/16 and -1/4; those of
Q^-1 C2 are 3/16 and 3/20. Both channel coefficients are invertible
on the two-dimensional multiplicity space. Each factors through its
actual first-arrow component, which must therefore have multiplicity
rank two. Together with scalar rank one this gives disjoint image
types 1+2V+2D, of dimension 17. No actual-instance matrix rank is
being computed or assumed.

### 5. Conditional negative-projector boundary

The final section retains the source hypotheses of PR1114 before
using PR1118's incidence criterion. Since the multiplicity image
and kernel of K_mult are distinct, L_h cannot equal both. This
justifies exclusivity only when the projected product vanishes.
Neither incidence is selected, and the case in which neither holds
is retained. The invariant multiplicity trace is not confused with
the separately projected product's trace. No source occurrence,
fourth/fifth obstruction, Smith exponent, or algebraicity statement
has been inferred.

## Bounded checker audit and reproduction

The verifier was inspected before execution. Its only mathematical
calculations are fixed nine-class character arithmetic in Q(sqrt(5)),
small degree symmetric/exterior representation identities, rational
normalization arithmetic, and universal algebra in a formal generator
k subject to k^2=k/4. It does not construct or evaluate actual
HM/source arrows, tensors, coefficients, matrices, points, parameters,
derivatives, jets, or selected ranks. No large scan occurs.

Both `python verify.py` and `python -O verify.py` were run independently.
Both exit successfully with 825 checks, and their outputs are
byte-identical to each other and to RESULT.json. Explicit exceptions
ensure the checks survive optimized mode.

The checker validates representation and rational consequences; it
does not prove the geometric injection, actual inverse-Q image, or
the normalized trace theorem by itself. Those points were audited
directly above from the full proof and the authenticated originals.
