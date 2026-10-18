# Independent integrated review

## Finding and evidence boundary

The conditional transition/source-leaf proof is sound, with the distinctions below. This bundle integrates the transition proof with the historical determinant evidence. It is portable and unpublished. Its public repository sources are stored as inert `.txt` files; only `check.py` and `test_negative_pins.py` are intended to run. Neither imports, executes nor evaluates the bundled production code. Model bytes are hashed and JSON chart metadata is inspected; no actual model polynomial product, source leaf, owner or jet is evaluated.

The pin URLs identify the immutable public locations recorded by the preceding recovery audit. This independent review verifies supplied bytes, SHA256/Git blob consistency and selected manifest/dependency bindings; it does not make a new network/provenance attestation. Private connector responses are intentionally absent. A hash identifies bytes, not a successful execution, mathematical truth or a trusted signing identity.

## Mathematical review

1. **Quotient cocycle:** the resolution and annihilation hypotheses suffice. Inserting `I_j P_j = Id - gamma H0_j - H1_j delta` between `P_i` and `I_k` kills the two error terms independently. There is no requirement of equal literal inclusion images, or cross-carrier `P_i H1_j=0`. `delta gamma=0` is required for the quotient interpretation, not for the displayed cocycle reduction. The common ambient complex/transport premise remains essential.
2. **Reciprocal factors and transpose:** for `D_i=diag(nu_i,nu_i^-1)`, `G_ij=D_i^-1 T_ij D_j` and `g_ij=G_ij^t=D_j T_ij^t D_i^-1`. Thus `G_ij G_jk=G_ik` but `g_jk g_ij=g_ik`. The raw source and JavaScript formulas agree in this order. The determinant is unchanged by either reciprocal factor.
3. **Determinant one versus constant:** the contraction only proves invertibility and a multiplicative determinant cocycle. Constant nonunit determinant can make logarithmic derivatives traceless, but the raw adjugate still equals `det(g) g^-1`, not the inverse. Invariant volume normalization of these specific ordered quotient bases is the missing scalar premise. Triviality of a determinant line alone does not supply it.
4. **Source.gi and tf:** `Source.gi` routes to the raw adjugate, with the compiler explicitly recording its determinant-one premise. The `tf` operator itself always has trace zero in rank two with 2 invertible. Applying it does not correct an erroneous inverse upstream.
5. **K, k, F and signs:** with the genuine inverse, `mu(B,A)=(D_a B D_b A-D_b B D_a A)/2`, `K=mu(g^-1,g)`, `k=-K/2`, `C=g_ik^-1 mu(g_jk,g_ij)` and `F=b-tr(C)/2`, with `b=(15/4)q_ij,a q_jk,b`. Under traceless logarithmic derivatives, `delta K=2C-tr(C)Id`, hence `delta k=-C+tr(C)Id/2`. The checker independently expands the noncommutative words and checks the multilinear rank-two identity on all 81 basis combinations. It does not establish the separate transgression theorem `delta s=F`; the implication from that premise to `delta(sId+k)=bId-C` is correct.
6. **Root line:** invertibility of the localized ratios, the particular line N and old square-line identification, ambient/frame transport, and the derivative dictionary remain explicit geometric premises. A line frame represented by `y/x` is not automatically a globally invertible regular function. Infinity connection transport is `-t dt/(1-t²)` and must not be reset to zero. The normalized `nu[0]=1` retains nonzero derivative slots; it is not the constant function. Reciprocal factors cannot fix a nonunit determinant, and common omitted line factors cancel only in the combinations justified by the physical-frame identification.

## Historical determinant receipt: exact obligation

Let the stored numerator matrices be `rawP_i` and `rawI_j`, and their stored denominators be `dp_i` and `di_j`. The producer sets

    N_ij[r,t] = sum(k=0..14) rawP_i[r,k] rawI_j[k,t]
    q_ij = dp_i di_j

and requires

    N_ij[0,0] N_ij[1,1] - N_ij[0,1] N_ij[1,0] = q_ij².

The source decodes `P_i=rawP_i/dp_i` and `I_j=rawI_j/di_j`, so this is precisely `det(P_i I_j)=1` where those denominators are units. The square is essential. The exact producer loop has all 36 ordered pairs on six stored charts; an entry is appended only after its equality passes. The stored receipt has exactly that ordered list, including the sixth carrier. It does not separately enumerate owners, masks or infinity charts. Extension to those labels requires the valid reciprocal-factor/frame-transport arguments.

The producer uses finite integer coefficient convolution and coefficientwise subtraction, removing zero coefficients. Its input checks require six charts, I of size 15×2, P of size 2×15 and nonzero denominator polynomials. **Correction to the previous audit wording:** its duplicate-exponent guard detects an exponent already stored with a nonzero coefficient. An earlier zero-coefficient occurrence is omitted from the dictionary, so not every syntactic duplicate is rejected. This nuance does not change the exact equality the producer tests; this review does not certify every model polynomial's encoding by running that decoder.

The CLI hashes the exact raw bytes that it parses. The attribution manifest pins the receipt and producer; dependency pins and the geometric manifest bind the model and source formulas. The top-level verifier's static code checks the source dependencies before invoking the producer. This bundle verifies the selected available manifest entries, not the complete original package or its executable behavior.

The receipt claims PASS and 36 exact identities without point sampling. It supplies no process transcript, signed runner attestation or per-pair polynomial witness. Schema agreement, common manifest membership and matching hashes cannot prove the historical process ran successfully. Accepting the historical computation claim is a separate evidence policy. If independent computation is required, the outstanding route is an authorized exact run, an independently checkable model-bound certificate, or a geometric proof of these frames' volume normalization. This package grants no execution authorization and proves no new actual-model determinant identity.

## Runnable review and negative controls

Run from any directory with Python 3:

    python check.py
    python -O check.py
    python -OO check.py
    python test_negative_pins.py

Use the bundle-relative script path if the current directory differs. All guards use explicit exceptions rather than `assert`, so optimization does not disable them. The checker covers twelve exact Python method ASTs, JavaScript anchors, the producer pair-loop AST, public byte pins, selected manifests, historical coverage/model metadata, free-word cocycle and delta-K reductions, invented contraction countermodels, and rank-two basis identities.

Negative controls reject changed input bytes, the missing denominator square, swapped denominator owners, missing ordered coverage, a different model hash, the reversed delta-K sign and reversed reciprocal factors. The separate harness corrupts each bundled input in an isolated copy and requires rejection both normally and under optimization. None of these tests executes the determinant producer or any other bundled production source.
