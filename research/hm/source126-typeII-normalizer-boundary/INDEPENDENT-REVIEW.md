# Independent review: known-normalizer symmetry boundary

Reviewed the complete proof, finite-group checker, six authenticated repository inputs, and the primary source's Section 1. No mathematical blocker found in the explicitly restricted known-normalizer conclusion.

## Final bytes and replay

- PROOF.md: bb4d5f56f16709b0b77906f22afbfd931d406eea9c51e4aaf094f7132321d2fb
- verify.py: 8bb7eab81bbe26161becfb9485cdc27bc2b86c20a5130232023e780d0c3a8e7b
- INPUTS.json: f8d7b39427698f03e052b81c363aa704c439566c6609ea48eb02de65886f473d
- RESULT.json: 2e218e857c477f67551b56bb7dea5af04a78ca29e7bb9cd6d23e5483e4792d70

Normal and optimized executions each passed 33 checks with identical stdout and RESULT.json. The six source files match their manifest SHA256 and Git blob identifiers.

## Source and mathematical checks

1. Independently opened Aure–Decker–Hulek–Popescu–Ranestad, https://arxiv.org/pdf/alg-geom/9606013v2, Section 1, printed pages 4–6. The text explicitly gives the order-125 Heisenberg group, scalar center mu5, and the order-15000 semidirect product N5=H5 semidirect SL2(F5) embedded in SL5. It also identifies inversion and its positive-plane/negative-line eigenspaces. Thus the complement premise is an embedded action, not a substitution of an abstract quotient for a subgroup.
2. The pinned cone input identifies the chosen G action as V plus W, dimensions three and two, with central signs plus and minus, and identifies the rank-three invariant quadric's vertex as the same negative line P(W). The pinned inversion-even input Section 7 explicitly identifies its 25 distinct Heisenberg translates with the actual negative eigenspace lines. These are the geometric facts used in the stabilizer argument.
3. Projectivizing divides the linear normalizer order by five, giving 3000. The complement embeds projectively, has order 120, and fixes the chosen line. Its central involution is not an ambient scalar. At least 25 orbit members and the upper bound 3000/120=25 force equality, proving the full line stabilizer inside this group is exactly G.
4. A projective symmetry of the rank-three quadric preserves its singular vertex line, so its stabilizer is contained in G. Conversely the retained invariant quadric is fixed by G. Hence its projective stabilizer inside the known normalizer is exactly G, as is the stabilizer of the distinguished quadric and the G-stable negative family.
5. The exhaustive affine semidirect-product checker verifies the conjugation formula (v,g)(0,-I)(v,g)^(-1)=(2v,-I), all 25 conjugates, the order-120 centralizer, and perfectness of the complement. These supplement the actual geometric orbit proof; the affine origin is not substituted for an unauthenticated geometric line.
6. The canonical octic map is G-equivariant, hence its Hom-space vector is G-fixed. The established stabilizer therefore contributes no new nontrivial character. Changing scalar lifts or linearizations of the same projective action is not an extra same-object symmetry.
7. The retained block-scaling theorem explicitly proves ambient nonisomorphism, not merely failure of a selected equivariant gauge: the nonzero ratio changes sign, and simplicity plus perfectness upgrades equivariant nonisomorphism to ordinary nonisomorphism. Its cone-restriction isomorphism is insufficient for an ambient naturality constraint. The even degree-eight parameter sign alone is positive in any event.

## Boundary

This excludes a specific proposed extra-character route using the known actual Heisenberg normalizer. It does not classify the full projective automorphism group of the HM bundle, rule out every possible outside symmetry, determine the actual octic scalar, or eliminate a source pair. An outside same-bundle, same-pencil action would require additional authenticated geometry and its compatible endpoint action. No actual HM coefficient, parameter or instance rank was evaluated. The finite tests are exact universal group arithmetic, not proof-assistant verification.
