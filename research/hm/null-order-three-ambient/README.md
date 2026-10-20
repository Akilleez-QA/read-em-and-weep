# Explicit order-three ambient extension

## Current result

`third-order/RESULT.md` constructs the product and overlap correction modulo h⁴; its scalar unit coefficient c exists under the stated regular equivariant acyclic Čech hypotheses. `total-de-rham/RESULT.md` gives the explicit closed total cocycle β=(ζ,α,b). Neither result identifies the actual period or extends the module.

## Dependencies and review

Depends on the scalar-pentagon and literal-ambient-extension packets. `third-order/REVIEW.md` is the existing independent review of all four order-three descent identities and of the total de Rham lift, including the sign of the bivector correction. The scalar coefficient is existential, not an explicit computed function. Public discussion: [order-three ambient result](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260064519).

## Historical exploratory reports: status, not extra conclusions

`historical-exploration/` preserves relevant earlier alternatives and their corrections rather than treating them as additional settled consequences of the current result. They depend also on the module-boundary-audits packet.

- `twisted-endomorphism/RESULT.md`: conditional honest endomorphism descent, assuming the twisted module exists; `FORMAL-WEYL.md`: precise local formal derivation statement.
- `twisted-period/RESULT.md`: intermediate conditional trace-class discussion. Its open torsor premise is superseded by `FORMAL-TORSOR.md` under the stated holomorphic differential symplectic hypotheses; module existence and actual period comparison remain open.
- `twisted-period/PERIOD-AUDIT.md`: corrects an overbroad claim that a general twisted index theorem is missing. Such a framework exists; the specific normalized comparison is not proved.
- `trace-density-candidate/RESULT.md` and `test.py`: universal exterior-algebra candidate, not the actual period or a physical vanishing certificate. No separate saved output or independent review file was present; the historical result describes its symbolic check, which was not rerun.

The explicit total cocycle strengthens the candidate input but does not retroactively prove the proposed period identity c=ω/h−hβ. Historical gaps closed later are labelled above; surviving conditional results remain conditional.

## Unresolved boundary

No module extension, mixed/full-sign vanishing, period normalization, or detection of the semiregularity kernel follows. The thirty retained conditions are not computed.

## Imported source pin

The literal scalar presentation is PR16, commit `c8aec970fd65a105f39f4e8aeb8a17f0f0053f89`, blob `a58834ab61e18a5dedd8a7bf20bec7121bfa9165`: [second-order-algebroid.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md). It is linked, not recopied. Source assertions are imported at this pin, not re-evaluated.

This packet preserves existing proofs and audits. No checker, geometric source evaluation, or experiment was rerun for publication.


## Published predecessor pins

- [B2a](https://github.com/Akilleez-QA/read-em-and-weep/tree/99411ca8810ba70158126e9bebd01eb79104003c/research/hm/null-scalar-pentagon)
- [B2b](https://github.com/Akilleez-QA/read-em-and-weep/tree/9e3d8dc8525a7d11ae919dfac2126794c9bdc366/research/hm/null-literal-ambient-extension)
- [B3 (historical exploratory reports only)](https://github.com/Akilleez-QA/read-em-and-weep/tree/d1422e5f9137ae64ec207c496a0391712ce93263/research/hm/null-module-boundary-audits)
