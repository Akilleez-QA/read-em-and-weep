> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

# Codex-V01 independent coverage review

Sources: public PR1 comments 6141530883,6141322825,6142342077,6205249609,6205341120,6205455951,6205660472; primitive/source pin08b73637d4136f91606aad332c46cafd064417f8. New authenticated fingerprint PR79 commit5df68750f766b18a746e50bff662b09829225ab1, path research/hm/null-support-certificates/seed-fingerprint.json. Reviewer V02 independently corroborates reconstructed partition; concrete report corrections below remain pending.

## Independent exact correspondence: PASS

Created and ran ONLY metadata binder Codex-V01-bind.py beside this report. It reconstructs ALL78 dictionaries independently, compares entry/coefficient/kappa/staircase/row/seed, both selector words, tail and all owner arrays. No source-polynomial arithmetic. Fingerprint SHA256 abbd6fdd01c7b7d0f2c0c272238f4d0c11a3d9c6301f82b7d36e25c12e33eb92. Source pin/schema/star/standard-bit/legal-mask conventions checked.

For local rank r: q2 cloud seed=r; q3 seed=6+r; q4 seed=30+r. Standard coordinate i (zero-based) uses bit3-i; LEGAL MASK coordinatei uses biti. Canonical auxiliary carrier is5; its sorting key only is-1. Never conflate the bit dictionaries or encode star as a primary carrier.

RESERVED: cloud seed4 = q2 localrank4, row2, M11[12,6], coefficient-2, kappa(-1,-2,-2,-2), standard(3,11,15), no deleted prefixes, residual tail(0,1,2), left I0/right P0. Its E12 cell belongs to null, removed from C02 WITHOUT reranking. The unpublished704-tuple scan remains reserved. Fingerprint is not an executable full-domain lowering or a completed scan. Other E12 cells are now ordinal-bindable; resource/source-lowering requirements remain.

## Reconstructed tuple contract

K=(q,row,sigma,channel). Sigma enumerates lexicographic permutations of coordinates1..q; start active coordinates at0, inactive coordinates at1, flip active coordinates in sigma order. Orientation=(-1)^inversions(sigma). Build coordinate tuples first, then serialize using the authenticated standard dictionary. Matrix indices zero-based.

Row order:
q2 CCBB kappa(-1,-2,-2,-2): M11[9,3]:1; M11[10,4]:1; M11[12,6]:-2.
q3 CCCB kappa(-1,-2,-3,-3): M10[0,3]:1; M10[2,6]:2; M21[10,1]:1; M21[12,5]:2.
q4 CCCC kappa(-1,-2,-3,-4): terminal -M20[0,0],+M31[10,0]. Their effective factored-selector coefficients are BOTH+1 before orientation because J2/block signs cancel. Fingerprint/binder verifies this distinction.

Local rank=row_index*q!+lexrank(sigma), reset row_index per q. C01/C02 q2 E12 halves[0,3)/[3,6); C03/C04 same E34. C05/C06 q3 E12[0,12)/[12,24); C07/C08 same E34. C09/C10 q4 E12[0,24)/[24,48); C11/C12 same E34. With reserved seed4 removed from C02:155 new cells+1 incumbent. All78 seeds expand ONE detector, not78 independent functionals. E12 means correction E12(T34F34); E34 means E34(T12F12).

Full label contract: preserve each (standard,carrier,mask), inserted/deleted-prefix owner, pole multiplicity, source-first sorting permutation/sign. Alternate the authenticated cochain; never reevaluate its nonlinear residual after arbitrary reordering. Only repeated FULL vertices give alternating zero; tail carriers may repeat. Every full label needs exactly one zero/unresolved/reserved record.

## Concrete checks and required repairs

Root check_contracts.py tiny self_test PASSES. Its rows/permutations match this contract. It checks proposed ownership keys and worker identity existence, not textual claim semantics, chart tuples/signs, cloud binding or full labels. Receipt explicitly says coverage unproved, incumbent pending, obstruction undecided: no false coverage claim.

Read C01-C07,C09-C11,V02. C08/C12 absent at inspection. BLOCK C09: it defines E12 as matrix entry R12 and contracts all five Rsharp terms, hence owns wrong channel. Its bit2^(i-1) also opposes the now authenticated standard mapping. Replace with E12(T34F34) four derivative families; rerun metadata correspondence. C01-C07,C10-C11 use complementary primitives correctly.

C01/C03 counts16,40,96 are flag-only enclosures, not exact occupied label domains. Public6142342077 section4 proves only carriers* or4 at all-infinity: at most32 labels there. C02's18 minimum1 carrier tuples overinclude final carriers1,2,3; under this fixed-family identity they reduce to4. Treat counts as conservative supersets pending actual outer54 formula binding. Leading-carrier zero proofs may remain valid over supersets. C03 correctly conditions exclusion on partition binding; independently check primitive support before accepting.

C02 rank3 symbolic primitive/partition zero is not an incumbent scan. No full source-label enumeration, occupied-support certificate or obstruction verdict is accepted. Next: repair C09, bind full-domain lowering/outer54 identities, then audit one-status-per-label coverage.
