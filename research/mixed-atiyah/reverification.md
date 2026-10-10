# Independent re-verification of the mixed Atiyah certificate

Source pin: `research/mixed-atiyah-nonvanishing` at `0e9c5d6146385c75ac29e4d58acf110a044c1422`. The matrices were rebuilt here and compared with that commit. Nothing on that branch is modified.

## Agreement

The explicit symmetric m=2 seed has mixed evaluation rank 3. The full HH² evaluation has rank 15 and kernel dimension 13. The character annihilator still has dimension 16. No discrepancy was found with the published certificate.

## Recomputed rank

`verify-mixed-atiyah.js` rebuilds the k=0 split ribbon complex and the degree-one Hom differential on the H¹ row of `End(F)(-2,-1)`. All arithmetic is BigInt and fraction-free. The published Python scripts are not executed. The published dual matrix W is an input only as a matrix to be checked.

Exact outcome on the recomputed matrices:

- The boundary is 144×144 of rank 132. Twelve cleared kernel vectors satisfy A K = 0.
- Adjoining the four cocycles `u β_j` raises the rank to 136. Each one alone raises it to 133.
- The published W satisfies W d1 = 0 and W B = I₄. Every 3×3 principal minor of that identity has determinant 1.
- The q=4 map 36→68 has rank 36, so the source of the incoming d₄ is zero. The q=0 map 80→60 has rank 60, so the E₂ target in bidegree (3,0) is zero. The q=2 and q=3 rows are empty. The four classes therefore survive in H².
- Entrywise hashes of d1, of B, and of both q=4 maps match the sparse certificate at the pinned commit.

The same program rebuilds the exterior-algebra action at d=8 over Z, after clearing the denominator 3 in the Chern character. The character action has rank 12 and the annihilator has dimension 16. The thirteen compensated and product directions are independent and lie in the annihilator. The three symmetric mixed kappa directions complete that space to rank 16.

## Why the mixed rank is 3

The four independent classes are the Euler image of Δ(F) = A₁(F) ∪ v − u ∪ A₃(F). A nonzero image forces Δ(F) ≠ 0. The End-valued descent already recorded for this seed identifies one mixed evaluation with a nonzero multiple of Δ(F). The three mixed classes have distinct deck characters and are permuted by S₃, so their rank is 3. With the thirteen directions already known to evaluate to zero, the evaluation kernel has dimension 13 and the full HH² evaluation has rank 15.

Those thirteen Ext vanishings, and the inclusion of the evaluation kernel in the character annihilator, are the reductions already on the symmetric seed. This check recomputes their linear-algebra split and recomputes the nonvanishing certificate. It does not replace those geometric inputs. It does not say anything about other squareclass-two carriers, or about the Horrocks–Mumford ambient obstruction.

Run `node research/mixed-atiyah/verify-mixed-atiyah.js`. The program exits nonzero unless every pinned rank, hash, vanishing, and the identity W B = I₄ still hold.
