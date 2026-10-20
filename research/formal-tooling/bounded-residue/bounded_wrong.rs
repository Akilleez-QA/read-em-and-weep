use verus_builtin::*;
use verus_builtin_macros::*;

verus! {
// A bounded executable coefficient selector, universal over its input values.
// This is one term's residue contribution, not a Laurent-polynomial evaluator.
fn residue_term(e0: i64, e1: i64, e2: i64, e3: i64, e4: i64, coefficient: i64) -> (r: i64)
    ensures r == (if e0 == -1 && e1 == -1 && e2 == -1 && e3 == -1 && e4 == -1 {
        coefficient
    } else { 0 }),
{
    if e0 == -1 && e1 == -1 && e2 == -1 && e3 == -1 && e4 == -1 { coefficient } else { 0 }
}

// Exactly two terms, explicitly unrolled; conservative safe-addition bounds.
fn residue_two(a0: i64, a1: i64, a2: i64, a3: i64, a4: i64, ca: i64,
               b0: i64, b1: i64, b2: i64, b3: i64, b4: i64, cb: i64) -> (r: i64)
    requires
        -4611686018427387903 <= ca <= 4611686018427387903,
        -4611686018427387903 <= cb <= 4611686018427387903,
    ensures r == (if a0 == -1 && a1 == -1 && a2 == -1 && a3 == -1 && a4 == -1 { ca } else { 0 })
               + (if b0 == -1 && b1 == -1 && b2 == -1 && b3 == -1 && b4 == -1 { cb } else { 0 }) + 1,
{
    let x = residue_term(a0, a1, a2, a3, a4, ca);
    let y = residue_term(b0, b1, b2, b3, b4, cb);
    x + y
}
}
