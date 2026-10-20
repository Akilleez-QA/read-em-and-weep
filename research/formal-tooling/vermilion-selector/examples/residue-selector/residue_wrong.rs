use verus_builtin::*;
use verus_builtin_macros::*;
verus! {
fn false_residue(coefficient: i64) -> (r: i64)
    ensures r == 0,
{ coefficient }
}
