# Independent review: all six pinned inclusions are cycles

## Decision

**ACCEPTED:** the literal decoded inclusions satisfy `delta I_r=0` for all six pinned carriers, over their stated denominator localizations. This is independent of primitive A, all contraction and exactness claims, H0/P/H1 identities, the complementary inverse, and historical computation receipts.

Reviewed producer: `../cycle-inclusion-20261018/PROOF.md` and `check_cycle_metadata.py`. The proof was checked against a separate derivation, and the source binding was repeated by a new standalone checker using handwritten exponent tuples and index permutation rather than the producer's factor-word representation. No producer code is imported or executed by the independent checker. The producer's formulas and implementation were inspected during review; this is independent reconstruction and checking, not a claim of blind review.

The sole mathematical target here is the cycle equation. This review does not itself accept an integrated proof of A, prove the complementary inverse, verify geometric carrier coverage, or authorize source evaluation or external publication.

## 1. Independent primary derivation

Use independent notation `(t,a,b,c,d)=(v_r,v_(r+1),v_(r+2),v_(r+3),v_(r+4))` and let all ambient subscripts be relative to r. Set

    A1=A4=B2=B3=C0=0,  A0=p, B0=q.

Write `(e,f,g,h)=(C1,C2,C3,C4)`. Eight nonpivot equations of the displayed cyclic differential are exactly

    t e=d g-c p,   t f=c e+a q,
    t h=a f-b p,   t g=b h+d q,
    t A2=-b g,    t A3=-c f,
    t B1=a h,     t B4=d e.

Let `K=abcd-t^4` and `D=tK`. Iterating the first four equations gives

    K e=(b^2 d t+c t^3)p-(d^2 t^2+a^2 b d)q.

In the localization at D, both t and K are units. Thus the closing equation determines e, and the recurrence determines f,h,g, followed by the four forced coordinates. This proves existence and uniqueness in the prescribed coordinate slice without using any A or inverse assertion.

For additional detail, the four C coordinates over denominator D, with arbitrary p,q, are

    D e=(b^2 d t^2+c t^4)p-(d^2 t^3+a^2 b d t)q,
    D f=(b^2 c d t+c^2 t^3)p-(a t^4+c d^2 t^2)q,
    D g=(a b c^2 t+b^2 t^3)p-(a^2 b t^2+d t^4)q,
    D h=(a c^2 t^2+b t^4)p-(a^2 t^3+a c d^2 t)q.

These were derived from the recurrence rather than read as an inferred cyclic symmetry of chart zero. The two inclusion columns use `(p,q)=(1,0)` and `(p,q)=(0,t)`. In particular the second column's extra factor t is essential on charts 1 through 4. The independent checker contains the resulting full handwritten numerator exponent table, including A0 and B0 and every zero cell.

The two remaining equations vanish directly from the same recurrences:

    t Y0=-bd g+ac f+b t e-c t h
        =b(t e-d g)-c(t h-a f)=b(-cp)-c(-bp)=0,
    t Z0=ab h-cd e+d t f-a t g
        =d(t f-c e)-a(t g-b h)=d(aq)-a(dq)=0.

Since t is a unit, this proves all ten outputs vanish. No separate `ev delta=0` or `delta gamma=0` result is required.

The producer uses `(x,u,v,w,t)` for the five variable labels, which corresponds here to `(t,a,b,c,d)`. Its `Delta=x^4-uvwt` is `-K`; its denominator is exactly D. All four displayed two-binomial scalar identities have the stated signs. Its complete numerator table agrees with the independently derived table and its own factor-word code.

## 2. Independent auxiliary derivation

Here put `v0=1`, `(a,b,c,d)=(v1,v2,v3,v4)` and set

    A4=B2=B3=C0=C1=0,  B0=p, C4=q.

The eight nonpivot equations solve successively as

    C2=ap, C3=dp+bq, B1=aq, B4=0,
    A3=-acp, A0=d C3/c,
    A1=(b A0+q-a C2)/d, A2=c A1-b C3.

In particular

    A0=d^2p/c+bdq/c,
    A1=(bd/c-a^2/d)p+(b^2/c+1/d)q,
    A2=-a^2cp/d+cq/d.

The remaining outputs are

    Y0=d A2-a A3-cq=0,
    Z0=b B1+d C2-a C3=0.

On the localization at `D5=-a^2cd`, a,c,d are units. The first column has `(p,q)=(1,0)` and the second `(p,q)=(0,-d/a^2)`. Rewriting the eight solved coordinates and the two free coordinates over D5 gives exactly the producer's complete auxiliary numerator table. All 30 auxiliary cells and D5 are separately bound to the pinned input. No division by b or any unsupported unit is used.

## 3. Independent all-entry binding and adversarial controls

`check_independent_binding.py` reads `inputs/hm-pinned-model.json.txt`, copied byte-for-byte from the previously authenticated determinant-volume input, and verifies both immutable pins before interpreting its records:

- SHA256: `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`
- Git blob: `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`
- Immutable source: https://github.com/Akilleez-QA/read-em-and-weep/blob/31f5b074f7c212f9bb6498ed2920e0c93cc781a9/research/hm/null-operator-compiler/hm-pinned-model.json

It verifies all 150 delta cells using a fixed relative incidence table, all 180 inclusion cells using independently handwritten exponent tuples, and all six inclusion denominator records. This includes every zero cell and all six carrier records. For primary charts, the exponent operation is only a permutation of a fixed five-tuple followed by omission of the v0 coordinate; no polynomial products or coefficient sums are constructed.

The checker also rejects 194 inert negative controls:

- One independent sign/occupancy corruption in each of the 180 I cells.
- Four differential corruptions: sign, variable, extra edge, missing edge.
- Inclusion exponent, duplicate, Boolean sign, nonunit sign, malformed exponent, missing row, and extra column corruptions.
- A primary denominator corruption, an auxiliary denominator corruption, and a missing chart.

The decoder validates literal record shape and integer unit signs. A Boolean does not pass as an integer coefficient. Explicit exceptions preserve checks under optimization. Both

    python check_independent_binding.py
    python -O check_independent_binding.py

pass with byte-identical saved reports. No symbolic algebra library, source import, producer import, polynomial multiplication, matrix contraction, numeric source specialization, source jet, or historical evaluator is used. Mutants exist only as in-memory copies of inert JSON data and are never written back to the pinned input.

## 4. Dependency and claim audit

The proof dependency is exactly:

1. The displayed universal cyclic differential.
2. The primary four-step recurrence and auxiliary triangular equations.
3. The elementary fact that factors of a unit are units in a commutative ring.
4. Full literal identification of the actual delta, I, and di records with those formulas.
5. The source decoder interpretation that I is its stored numerator divided by di.

There is no invocation of a theorem whose premise already includes A. There is no inference from an H1 formula, a complementary inverse, determinant-one transitions, or the previous contraction consequences. Even the two normally omitted output rows are proved to vanish directly, so no hidden common-complex premise enters.

The algebraic theorem and the metadata test have distinct roles: the former proves the universal cycle equations; the latter establishes that every actual pinned entry is covered. The PASS report alone is not represented as a physical evaluation receipt. The result is therefore available as an independent premise for a later integrated A argument after the remaining complementary-inverse result is separately accepted.

## 5. Reviewed producer pin

The accepted producer proof SHA256 is

    e8425c8ea279c50d5682ca30f95a9ebf45ad2dc45e45a433585f28310c4fcdbe

and the inspected producer checker SHA256 is

    a8d683dd51f0ed716b78fa33e87bf29431569fd25340e9a619834e189275d4a1.

The producer subsequently added metadata-integrity controls and an evidence-paragraph reference; that addition was inspected and changes no mathematical formula or primary binding implementation. No mathematical or source-binding correction was required.
