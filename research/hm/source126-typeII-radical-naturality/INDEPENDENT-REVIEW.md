# Independent verification: Type II radical naturality and second-symbol factorization

Reviewed 2026-10-23 against final bytes:

- PROOF.md SHA256 `80b75be005ec917057de75b4dabb7e23dbce2af95f8bc22ccfa2fd12e24e6f82`
- verify.py SHA256 `6e48c31c29c4c57730d55d6807daec490e18a8932e15d9a3c9943873fa3e09c8`
- INPUTS.json SHA256 `17aec3de91ac47c22dabd9c73539b5b83122cb3138a3ed56df78a3ce4736b218`
- RESULT.json SHA256 `5ed789441ef5f0c7d4fe766682168ab556b0f2edbf2addfd70f08531d7210aff`

## Outcome

The scalar-selection theorem and factorization are valid under the stated actual Type II full-J hypotheses, relative to the six pinned interfaces. No mathematical blocker was found. The proof genuinely forces the internal D scalar mu to zero; it does not merely bound it or select a synthetic example. The quotient first symbol is correctly identified with the nonzero multiplication-mod-V family. The original full-J occurrence and complete repair remain unresolved.

## Checks of chain and obstruction arguments

1. **Actual subcomplexes.** The sole (2,0,0) footprint gives U=F2 as an actual subspace, since the known inclusion has equal dimension. The common-annihilator definition gives j2(U)=j4(Z)=0, while the radical representation gives images in U and Z. Thus each j descends to a well-defined map from the quotient complex T to the subcomplex S. Full-J Q compatibility and fixed negative-pencil commutation together make it a chain map for every Q+tT_a, not just at the central fiber.

2. **Cohomology and connecting maps.** S contains the exact original kernel A+D. Therefore H0(S)→H0(M) is the actual identity, and the long exact sequence makes delta:H0(T)=D→H1(S)=D injective and hence invertible. The map H1(S)→H1(M) is zero, and eta:H1(M)=P→H1(T)=P is an isomorphism by exactness. These are map-level facts, not conclusions from character equality alone.

3. **Some induced H0 radical map is nonzero.** Every j induces j^0:D→A+D and j^1:P→D. Equivariance forces j^1=0 and the image of j^0 into the D summand. If all j^0 vanished, choose a lift x of any quotient kernel vector. Because Qx lies in Z, every j2x is a degree-zero S cycle. Vanishing of its cohomology class means the vector itself is zero: the two-term complex has no incoming boundaries. Then all radicals kill x, so x belongs to U, contradicting a nonzero quotient kernel class. Thus at least one j^0 is an isomorphism onto D. This avoids confusing cohomological vanishing with representative vanishing in degrees where boundaries could exist.

4. **Naturality selects mu.** First Bockstein naturality is the representative identity b_S,a j^0=j^1 b_T,a, induced by exact family commutation. Since the right side is zero and some j^0 covers all of the D kernel, the internal first symbol vanishes on D for every a. The pinned one-dimensional transvectant channel then gives mu=0. Its nonzero A multiplication channel is retained. This does not imply original first-Bockstein nonvanishing; the original first symbol remains zero.

5. **Bundle consequence.** Nonzero-quadratic multiplication injects A into D for every projective a, so the selected internal family has constant rank three. Its kernel is exactly D tensor O(-1), and its cokernel E is locally free of rank two in the displayed presentation. Consequently c(E)=(1-H)^(-3), giving c1=3H and c2=6H^2. There is no projective rank-drop locus in this selected internal branch. The previously proved nonzero-mu discriminant geometry remains a valid conditional universal computation but cannot occur under the present actual full-J hypotheses.

6. **Exact sign and canonical comparison.** For k in the original kernel, choose Qu=-T_a k using original first-vanishing. Its quotient class is a T cycle and delta([ubar])=[Qu]=-b_S,a(k). The quotient projection of the second class [T_a u] is b_T,a([ubar]), which gives eta beta2_M,a=-b_T,a delta^(-1)b_S,a. The minus sign is tied to the explicitly stated delta convention and was independently checked. Changing u by an original kernel vector changes its second class by the original first symbol, which is zero. In particular the comparison with u0=-h zeta_a identifies the result with the imported canonical actual second Bockstein, not an unrelated obstruction. The formula holds on all A+D; its D restriction is zero after scalar selection.

7. **Nonzero quotient family and unique channel.** Nonvanishing of the original second family on A forces b_T to be nonzero through the exact factorization. Since A tensor D=V+P+D+A has exactly one P, the full bilinear quotient family is a nonzero scalar times multiplication to Sym6 W followed by quotient by its unique V constituent. Fixed equivariant identifications of the irreducible copies only rescale the factors. They do not introduce an unproved parameter-dependent change or move projective directions in the fixed A.

8. **Transfer of the ten-direction theorem.** The retained PR966 proof was read at its universal-family statement and supporting length-two restriction, immersion, Fitting-scheme, and orbit arguments. It proves that this same multiplication-mod-V family has rank four outside a reduced orbit of ten nonsquare directions and rank three there, with all nonzero squares of rank four. Once the entire actual quotient family is identified by fixed invertible scalar maps, its ranks and determinantal scheme transport. No source2 occurrence or compatible pure-V radical is imported into Type II. The proof explicitly confines the transfer to that universal family.

## Reproducible evidence

Executed `python verify.py` and `python -O verify.py`. Both passed 101 checks, and the complete JSON outputs were byte-identical, matching RESULT.json at the hash above. Tests include exact synthetic chain commutation, the forced zero internal D channel, arbitrary-correction independence, the negative second-factorization sign, multiplication rank certificates, Chern arithmetic, and SHA256/Git-blob authentication of all six retained inputs.

The synthetic complexes are diagnostics for the universal algebra and are not actual HM realizations. This review verifies the new argument relative to pinned interfaces rather than independently reproving all prior geometric dependencies; it is not proof-assistant certification.

## Scope retained

The theorem assumes actual Type II and compatibility of the entire radical. It does not prove that hypothesis realizable, exclude the surviving footprint or source126, select or exclude a compatible radical line, remove a source-dual pair, cancel the non-acyclic quotient, or establish original generic full rank. Its new content is conditional mu=0, the exact original second-symbol factorization, and identification of the actual quotient first-symbol family.
