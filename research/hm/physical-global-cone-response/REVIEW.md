# Independent mathematical and replay review

2026-10-23. Verdict: **PASS for the bounded written theorem and diagnostic scope below.**

This review inspected the complete final proof, the complete standalone checker,
README, the source manifest, the remote-authentication record, both saved test
outputs, and all eight source copies. It did not modify any of them.
The initial proof was also inspected at SHA256
`d13a177f468cca9d61b82fc395401521e6a46edb3cb9653af6b7db556a2be4fb`.
The final proof explicitly binds the preceding division and correction to the
canonical or independently compared probes; that tightening removes the only
wording ambiguity identified during review.

## Exact bytes reviewed

| File | SHA256 |
| --- | --- |
| `PROOF.md` | `aafd5ee2b8a0a1d0876886b4db361c05d2a34cc41ab59e44ecec54580061cfcc` |
| `verify_global_cone_response.py` | `0b0346434133e56bea2ca95f1fd71cf6f804bf4cd3cd5bce2598ee1558b49116` |
| `SOURCE-MANIFEST.json` | `7c8d36fd483dc1d00cfc345c8006bc7d3436d3327f4a31bd7c7e56548dd0d977` |
| `README.md` | `7376fefd3420bc3c060e59fe2670f749b85e26449443e86addb10c4ded6958db` |
| `REMOTE-AUTHENTICATION.json` | `e37536754c031eb5794fee324ffb0c669298db418b608d903af8b8143f5f2a0b` |
| `TEST-NORMAL.txt` | `5b24b6045ca1d1d49e56a2f15e44d954f0609dc7d1bfa4bc2baa82ea266f1f77` |
| `TEST-OPTIMIZED.txt` | `5b24b6045ca1d1d49e56a2f15e44d954f0609dc7d1bfa4bc2baa82ea266f1f77` |
| `inputs/torsor904.md` | `ba6c3b70f54275292b3324960f2698f9cab807d87c65bd02048fcb4738152ffd` |
| `inputs/ambient_cohomology.md` | `a1aac107838f647cd66b78a1b88a4ab39fea35afbe72d70214d40a9c141189de` |
| `inputs/ladder.md` | `1827de5e5358d10c7a7d498b7b8ca767da8510cd632b40818fb5add1356e5c1d` |
| `inputs/q_exact.md` | `fc43f4c854b95b487b196cacc2c92d1dde74404bd630e8b39a2baca165749276` |
| `inputs/canonical_division.md` | `fbe769ab1e929005377bf684940f83990156654c8e9a3675eb7e9649ed21a180` |
| `inputs/canonical_correction.md` | `dfaff0ebd7045c587343b0e5619f1894c7ce2e06aaab46719171edde1a4a96ab` |
| `inputs/pr815.md` | `78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236` |
| `inputs/next_weight.md` | `5fe2492d2286588fc55396523ce9d3477741d3a36669e407aa78bca8ae68a492` |

An independent integrity pass recomputed each input's byte length, SHA256 and
Git-blob SHA1 using the `blob <length>\0` prefix. All agreed with the manifest.
This verifies the local copies against the manifest, not a reviewer-performed
remote GitHub retrieval or an independent proof of every upstream theorem cited
inside them. The author separately reports fresh exact-commit GitHub reads in
REMOTE-AUTHENTICATION.json. This review checked that all eight records' commits,
paths, reported remote Git blobs, and local SHA256 values agree with the source
manifest; it does not claim to have independently performed those remote calls.
README accurately summarizes the theorem, reproduction commands, and limits.

## Mathematical checks

1. **Global exactness is justified term by term.** The Cartier sequence for
   each locally free monad term is exact. The twist-two term's H1 vanishing
   makes restriction onto the global cone term surjective. The twist-two and
   twist-four positive cohomology vanishings together make every restricted
   term acyclic. This does not assert the false statement H1(B(2))=0.

2. **The singular cone is allowed.** The bounded locally free monad with
   locally free cohomology splits locally into F and contractible summands.
   Restriction preserves these splittings, including on the singular cone.
   Its full Hom complex therefore still resolves End(F_Q), with the retained
   characteristic-zero summand resolving B_Q. It is not an Ext complex of
   an ambient pushforward. Restricted-term acyclicity then identifies global
   complex cohomology with actual sheaf cohomology.

3. **The exact-source domains agree.** A cone primitive lifts in cochain
   degree zero, so d_Q Gamma(D^0|Q)=r(d_4 Gamma(D^0)). The proof correctly
   distinguishes this space from Gamma(im of the sheaf differential).
   The actual obstruction for closed positive cone sources remains P4;
   its family multiplicity Hom_G(R,P4) has dimension three. Neither is a
   claim that all closed cone sources are exact.

4. **Canonical source membership is noncircular.** The pinned global raw
   cubic equality says pi[aV]=pi[abZ] before the second-symbol quotient.
   Thus [S] lies in the ambient q-image, and its restriction has zero actual
   cohomology class. The global-complex comparison, not local exactness,
   supplies a global cone primitive. No W or compatible ambient primitive
   is assumed in that argument. H2(B(2))=0 is needed to identify the entire
   obstruction group as P4, not to kill this particular restriction.

5. **Family lifts are uniform.** For the stated coherent polynomial source,
   polarization gives a G-linear map from the full module R into the global
   source image. Semisimplicity for the finite group over C splits the
   relevant surjections. This produces one cubic-a/linear-h lift, rather
   than unrelated pointwise choices. Division by q is the inverse of an
   injective map onto its image and introduces no parameter denominators.
   This averaging argument does not make a physical contraction equivariant.

6. **The physical row has the stated domain and qualification.** Every
   closed global cone cochain induces a genuine global section of B_Q(4).
   The pinned physical coefficient theorem kills its complete marked
   weight-four coefficient, despite nonzero H0(B_Q(4)). Negative boundaries
   project to zero by the contraction chain identities. Thus both the full
   coefficient extraction and its trace factor uniquely through the global
   differential image. They are not maps from H1, and they are not arbitrary
   supported-middle extractions. Agreement with PR904 requires the stated
   restricted ambient contraction or a genuine comparison certificate for
   nonclosed cochains; agreement only on closed sections would not suffice.

7. **Recovery and response signs agree.** With d_Q e_Q=rS and rE=e_Q,
   exactness gives the unique W with qW=S-dE. Injectivity of q in the next
   degree proves dW=0. Replacing E by E+qY gives W-dY, not W+dY. The formula
   Q+a^3h tau(y)-a^3h Lambda_Q(rS) retains the PR815 minus sign and the full
   ambient nonclosed projection y. The cone row does not reconstruct y or
   authenticate an unrelated supplied W.

## Independent connecting-map sign check

Let (E,W) and (E',W') be two recovered compatible pairs for the same S,
and let k=r(E'-E). Then k is closed and

    d(E'-E)=q(W-W').

With the pinned connecting convention delta[k]=[d(lift)/q], this gives

    delta[k]=[W-W'].

This independently confirms the orientation of the recovered compatible-W
torsor. If the cone primitive itself is unchanged, E'-E=qY and the formula
reduces to W'=W-dY. If the primitive changes by a closed cone cochain, its
physical coefficient still vanishes, so the factor-row value is unchanged.
This deduction uses no evaluated primitive or actual source specialization.

## Checker replay

Both commands were independently run on the exact checker bytes above:

    python verify_global_cone_response.py
    python -O verify_global_cone_response.py

Both returned:

    PASS: 108 exact integrity/character/q-cochain checks; 8 negative controls.
    No actual HM evaluation; geometry and physical matching remain written inputs.

The checker uses explicit exception-based tests, which remain active with
Python optimization. Its character power maps, Q(phi) arithmetic, source
integrity checks, formal q-division operations, and two recovery signs were
inspected. Its free differential encodes a generic compatible pair; those
tests are formal diagnostics and do not prove geometric existence. The proof
supplies existence separately through termwise acyclicity and the canonical
raw-cubic identity.

The final coefficient-linearity test mixes E with qY, so both summands have
physical twist four. Both modes were rerun after that final checker change.
The previously reviewed checker at SHA256
`d1f46fcfdd05443409b195db36a23daec0a45a3900f8afe620be8f4e27621076`
is superseded by the final checker hash in the table above.

## Limits of the PASS

No actual HM coefficients, points, matrices, ranks, primitives, response
values, or fifth-boundary values were evaluated. No installation, remote
publication, or modification of predecessor artifacts was performed. This is
not Lean or proof-assistant certification. The full source-backed geometric
inputs are inherited; actual contractions, markings, harmonic normalization,
the comparison with ambient y, and a concrete response-row certificate remain
unfurnished. The result neither enlarges PR904's exact-source domain nor
removes PR894's compatibility test for an arbitrary supplied W, and it does
not complete the underlying proof repair.
