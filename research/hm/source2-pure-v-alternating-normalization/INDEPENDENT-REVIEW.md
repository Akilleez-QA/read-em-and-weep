# Independent review: exact alternating normalization

## Verdict and artifacts

**PASS**. With the pinned apolar and Hamiltonian conventions, the exact alternating difference coefficient is −2, and the alternating half has coefficient −1. The zero equivalences are valid for the conditional endpoint-nine factorization, not for an arbitrary bilinear family or a specialized direction.

Reviewed SHA256:

- `PROOF.md`: `ae1701aa293132a5268021a8bc529409de8af87feb55503138142949d8751335`
- `verify.py`: `ebf0fd76789395c50d71dd62a200a6d7ede67a03c0f568497a3ef45116f6afc3`

## Authentication

Both originals were freshly retrieved at the exact immutable repository paths and commits in `INPUTS.json`. Retrieved bytes match the retained files; independently computed SHA256 and Git blob hashes match the manifest:

| Input | Commit | Git blob |
|---|---|---|
| PR1031 | `7150cf97eeebe473bcd7c61c1f968c73625d92ef` | `0694e96e2d17a53b68d625ec6065f8bf513cd083` |
| PR1069 | `41bc20cade3198306c492c0c46399d71eb0d51c4` | `827cd956e2eb574fd7d40d408e0450c8581fd7d2` |

This authenticates these two retained proofs, not every earlier dependency recursively. PR1069 supplies the actual endpoint-nine factorization; the present polynomial calculation does not establish that premise on its own.

## Adjoint and quotient normalization

For the antidiagonal Gram matrices in the proof, the full multiplication adjoint from sextics to quartics is exactly the unnormalized second transvectant divided by 60. The factor is 2!·6·5, with the sign convention fixed by the same invariant pairing in both degrees.

The quotient adjoint must act on the included sextic E(p). The identities Pi E=Id and G6 E=Piᵀ GP give L_b*=M_b*E, so its formula is `(b,E(p))_2/60`. Treating quotient coordinates as sextic monomial coefficients would not give a justified normalization. The proof and verifier correctly use the orthogonal inclusion and complex bilinear, not Hermitian, adjoints.

## Independent coefficient-tensor check

An independent calculation reconstructed the transvectant matrices directly from falling-factorial monomial formulas, without symbolic differentiation or importing the production checker. It verified every coefficient of the alternating identity: all three quadratic coefficient indices for a, all three for b, and all seven sextic coefficient indices. The resulting full matrix identity is

`rho_D(a) T_b − rho_D(b) T_a = −2 T_[a,b]`,

where T denotes the unnormalized second transvectant. The same independent calculation checked all three coefficient matrices of `60 G4⁻¹ M_bᵀ G6=T_b`.

These are complete coefficient-tensor checks, not evaluations at selected quadratic directions. They confirm the sign, the factor −2, and validity on the entire sextic space. Dividing by 60 and composing with E gives the pinned quotient identity without any additional scalar. A coherent rescaling of the invariant forms scales both sides equally and does not change −2 when rho and bracket conventions are fixed.

## Conditional consequences

The retained endpoint-nine theorem gives the full ordered family B(a,b)=gamma rho_D(a)L_b*, not merely its diagonal. Substitution yields difference −2 gamma L_[a,b]* and alternating half −gamma L_[a,b]*. The stated recovery formula adds this alternating half to the symmetric polarization of R, with the correct minus sign.

The bracket maps the entire exterior square of the quadratic representation onto that representation, and L* is nonzero. Consequently L_[a,b]* is a nonzero polynomial family. Together with the pinned nonzero R1, this proves the equivalence of gamma=0, identically zero R, identically zero B, and identically zero alternating part in this branch. It does not infer any of them from vanishing at one parameter value.

For a general bilinear family, the diagonal cannot determine the alternating part. The proof retains this distinction for endpoint sixteen and does not assert full-pencil commutation even in the zero case. No actual gamma or branch is selected.

## Reproduction and scope

Both `python verify.py` and `python -O verify.py` passed all 20 checks with byte-identical output. The independent full coefficient-tensor and adjoint checks above also passed. No historical source-evaluation program was executed, and no actual source coefficient, direction, point, jet, matrix, or instance rank was evaluated. The mathematical applicability of the endpoint-nine factorization rests on the authenticated written theorem, not on these universal calculations alone.
