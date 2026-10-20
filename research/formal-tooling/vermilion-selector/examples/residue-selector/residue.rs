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

// A term extending across the missing-coordinate face has nonnegative e0,
// hence contributes zero to the (-1,-1,-1,-1,-1) coefficient selector.
fn missing_face_zero(e0: i64, e1: i64, e2: i64, e3: i64, e4: i64, coefficient: i64) -> (r: i64)
    requires e0 >= 0,
    ensures r == 0,
{
    residue_term(e0, e1, e2, e3, e4, coefficient)
}
}
