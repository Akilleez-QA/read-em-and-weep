# Independent final-byte review

Verdict: PASS, conditional on the retained actual-map premises of the pinned input. Reviewed on 2026-10-23. No mathematical correction is required.

## Reviewed identities

- PROOF.md SHA256: `2659282737eac4d62801ec50d484e9768236485271f7afab6ecf8537726e88c8`
- verify.py SHA256: `931177443e26d1de4869724f78641830f09a8a2e8e1a704d270dda2edf50fcc8`
- INPUTS.json SHA256: `0ccb6f8bcc9a041fad2fc70f92e628427dddf57e5ef2c4b6c142a6ab19bc6a16`
- REPRODUCE.md SHA256: `858db7cbee558bf490e6c1d42ae09eafb2184e9fe8f4bab93f3b664c63d7d7fe`
- Immediate input: commit `f96962f2219e096821c3dec50712cc0108abea8f`, `research/hm/forced-secondary-w-extension/PROOF.md`; SHA256 `ca7b2dade4fca80b5e6fc729f4a95ee56a828558fc4e28b3f08f607b1a524b00`; 9376 bytes; Git blob `c4a42690aa45b980f098120ff623d682d97822ea`.

The review inspected the complete proof, checker, manifest, reproduction instructions and immediate input. It independently ran `python verify.py` and `python -O verify.py`; both exited successfully with the reported PASS. Those runs independently validated the cached original input bytes against the manifest. This review did not independently refetch the public commit; remote publication identity is provided by the pinned manifest and the parent's fetch verification.

## Mathematical audit

1. Constant evaluation is genuinely a subbundle here, not merely a sheaf injection: its composite into the trivial ambient bundle is the same fixed-vector-space inclusion at every fiber. The quotient consequently embeds in the corresponding trivial quotient.
2. The exclusion of P uses an actual evaluation subbundle and the incompatible W' constituent after twisting, not a generic-rank assumption. It excludes P also when D is simultaneously present. Semisimplicity and multiplicity one then leave exactly H0(K)=0 or D and force the connecting map's P channel to be nonzero.
3. In the zero-section case, strictly negative splitting degrees give h0(K(1))<=9. The exact twist-one sequence gives the representation equality H0(K(1))=T6+H1(K(1)); any nonzero quotient of S+T6 has dimension at least four. Hence H1(K(1)) vanishes. The resulting degrees and coefficient representations are exactly T6 O(-1) and A O(-2).
4. In the D-section case, the quotient has no sections by H1(D O)=0 and embeds in a trivial bundle, so its degrees are strictly negative. This precedes the splitting assertion and avoids circular reasoning. Ext1(K',D O)=0 follows from those degrees, and averaging supplies an equivariant complement without making it canonical.
5. The rank-four quotient has no degree -1 summand because its possible twist-one sections are either zero or T6. Once its degrees are at most -2, its possible twist-two sections are either zero or D, again excluded by rank four. Degree -12 then forces four copies of O(-3); the Euler representation identifies their coefficient as S.
6. Equivariant Birkhoff–Grothendieck is valid for finite G in characteristic zero: the canonical degree filtration is preserved, ordinary splittings can be averaged, and pure-degree bundles become representation tensors after the standard twist. The standard binary linearization makes H1(O(-2)) trivial, as required for both coefficient identifications.
7. The two types are exhaustive possibilities under the premises, not a demonstration that both occur. Their distinction is precisely vanishing of the actual D channel. No value of that channel, secondary-boundary rank, selected actual data, or opposite-pencil conclusion is supplied or implied.

## Checker scope

The exact quadratic-field arithmetic verifies the bounded abstract character identities, orthogonality, dimensions and stated degree calculations. Explicit exception checks remain active under optimization. It verifies input integrity but does not mechanize the bundle proof or certify the original actual-map premises; those limitations are accurately stated. No selected actual HM coefficients, points, jets, matrices or instance ranks are evaluated.
