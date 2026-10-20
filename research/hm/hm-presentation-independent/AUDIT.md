# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-normalizer-foundations-PUBLICATION-CHECK.md](../hm-normalizer-foundations-PUBLICATION-CHECK.md) for the final-publication review.

# Independent static audit

**Result: valid. No mathematical correction is required.** This audit covers `PROOF.md`, including its direct structural check, against the supplied inert `hm-pinned-model.json` and `ext-model.md` §1. Only text inspection and formal exterior-algebra reasoning were used. No source/model execution, polynomial matrix products, numerical ranks, point substitutions, jets, or contraction-certificate evaluations were performed.

## Coefficients and orientations

The ordered cyclic bivectors are

- w+ = (e2∧e3, e3∧e4, e4∧e0, e0∧e1, e1∧e2);
- w− = (e1∧e4, e2∧e0, e3∧e1, e4∧e2, e0∧e3).

The wrapping order is essential and is preserved throughout. With the stated U,V,Z basis, all nonzero entries of the literal gamma table agree with the following row descriptions; the integer in parentheses is the source column:

- U0: v1(2), v4(3); U1: v2(3), v0(4); U2: v1(0), v3(4); U3: v4(0), v2(1); U4: v0(1), v3(2).
- V0: −v3(1), −v2(4); V1: −v3(0), −v4(2); V2: −v4(1), −v0(3); V3: −v0(2), −v1(4); V4: −v2(0), −v1(3).
- Zi: vi(i).

Every remaining gamma entry is zero. These signs also follow directly from the volume pairing: the two U cases are positive, the two V cases negative, and the Z case positive. Cyclic transport introduces no extra sign because a five-cycle has positive sign.

Every literal delta column agrees with the displayed D-ab formulas, including D40, D20, D31, and D42 in their displayed orientations. Each ev row is evaluation on its own five-coordinate block. Constants in these affine tables homogenize to v0. Thus the identification uses the actual ordered tables, with no hidden basis adjustment.

## Geometry and exactness

The twist identification is correct for projective space of lines: T=Q(1), det(Q)=det(V)⊗O(1), and the fixed volume gives Λ²Q(−1)=Λ²Q*=Ω²(2). The factor v in φ-v is the tautological O(−1) factor. The resulting rank-two bundle has first Chern class −1 and is normalized.

The direct structural argument is sound. Off-diagonal mixed wedges vanish by repeated indices; the diagonal complement wedges have sign (−1)^i. Their independence proves fiberwise injectivity, and hence the subbundle property. The cross pairing is nondegenerate. Precisely, after trivializing the line factors, β_i(u)=ω(u,α(e_i)); this fixes the adjoint convention and proves surjectivity. The alternating-form argument proves the zero composition.

Euler cancellation then proves exactness at degrees −1,1,2 and identifies the only cohomology as ker(β)/im(α). It is locally free of rank two. The local-splitting assertion, preservation under arbitrary pullback, and faithful-flat descent/base-change argument are all valid.

## Sources and scope

[Horrocks–Mumford, §2, pp. 67–69](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf) explicitly supplies the global local-splitting theorem and the same ordered bivectors in Lemma 2.5. [Lee, §2.1, pp. 617–618](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2F4234A65F6728D2661912E5E8A2956C/S0008414X00006751a.pdf/a-modular-quintic-calabiyau-threefold-of-level-55.pdf) confirms the ordered pair (f+,f−) and right-hand map (−f−*,f+*). Thus its right-hand map is exactly −b under the stated volume identification.

The supplied ext-model definitions agree with the proof; its [pinned repository location](https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md) was verified separately by the coordinating review. This audit closes only the exact-presentation dependency P. It does not verify the prescribed I,P,H0,H1, the historical identity A, any raw-primitive claim Q, or other imported certificates in the global-Hom argument.

## Final-byte binding

This audit binds to `PROOF.md` with SHA-256:

`ed549d3b6d19c1fbef269d390a6313269a369d8616a9343991e43585460915b7`

The checksum was independently obtained from the final proof file by text hashing only; no model or source code was executed.
