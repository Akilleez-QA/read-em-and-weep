# Independent exact-candidate review

Verdict: PASS for the stated necessary quotient specialization, conditional on the pinned PR920 normal-form theorem. This review is supporting verification, not an additional progress claim or a proof-assistant certificate.

## Mathematical checks

I read the complete normal-form proof at commit `1528ff8ea56b21e03f7501a962bdaa6728a75904`, including Sections 6–9 and the retained lift parameters. Its conclusion supplies actual constant C10, saturated intersection F, the quotient O(18), and the direct universal inclusions after projecting by C10. These are sufficient for the quotient diagram used here; no removal of the retained off-diagonal maps is required.

For a fiber ell=Cx of the tautological line, U_k^n is spanned by x^(n-j)y^j for 0<=j<=k. The perfect invariant apolar pairing pairs j with n-j. Its annihilator is therefore ell^(k+1) Sym^(n-k-1)W, with twist -(k+1). Dualizing this annihilator yields precisely Sym^(n-k-1)W O(k+1), not its negative twist. Constant rank gives a bundle quotient. The determinant-one condition justifies the self-duality used; no omitted determinant character remains.

Consequently the projected quotient is S O(7) plus Sym7 W O(1). The actual quotient Q is an extension of that bundle by O(18). The relevant Ext direction is Ext1(R,O(18)), giving H1(O(11)) and H1(O(17)), both zero. Equivariant averaging of a bundle right inverse is valid over C and preserves the right-inverse identity. This proves an equivariant bundle splitting, not its uniqueness, a constant ambient splitting, or a horizontal splitting of the source. The alternative Ext direction is not being used. Sym7 W=Wp+T is also consistent with the binary-icosahedral recurrence: Sym6 W=V+P, W tensor V=T, W tensor P=Wp+T, and Sym5 W=T.

Dualization gives Q* = O(-18)+S O(-7)+Wp O(-1)+T O(-1). Rank 13, degree -54, and the stated section counts 54 and 41 agree independently. The normal-form dependency is explicit; this review does not assert actual HM realization or a complete repair.

## Catalogue and executable checks

I independently retrieved the five pinned source files through the repository connector and checked their returned Git blob identities. All five final local input files now reproduce those Git object hashes and their recorded SHA256 values. An initial extra terminal newline in the imported inputs was corrected before this final review.

The original source at index 127 has defect zero and exactly the displayed A/B endpoint multisets; its permitted coefficient tuples include the c-d-f tuple. The campaign E catalogue identifies that tuple and source block multiset uniquely as E14. The original unrestricted dual catalogue identifies the derived negative block multiset uniquely as Q148, and the campaign Q catalogue agrees entry-for-entry. The source label's 32 distinct remaining pairs all have E14 and include (14,148). Therefore precisely 31 alternatives are removed, with no stable-label removal. The filter is keyed to this exact source label and pair rather than deleting Q IDs globally.

I inspected verify.py and reran it under both ordinary Python and `python -O`. Each run returned: `PASS 351 symbolic/identity checks; 10 negative controls; cdf32=1+31; no label cut`. Checks include universal apolar index orientation, both Ext directions, rank/degree/section arithmetic, pinned inputs, exact catalogue uniqueness, endpoint and source identity, duplicate/malformed pair rejection, untouched other labels, and independent source2 composition. This is finite symbolic/accounting validation, not evaluation of actual HM coefficients or a substitute for the geometric argument above.

## Exact reviewed bytes

SHA256:

- PROOF.md: `8263fd71ba117d916411829cc2063c73ae70ca04433d2237b0c05600542301b0`
- verify.py: `f63fa73ad1a2cd36dff9f69964f2b3f57ccaf9215bb179acd579b3f8a63be4e9`
- input-pins.json: `ba4a9d0676fc30d5f6981b309ab73e5ef0f432a223c0a7b5ffe2ea19e0ce1e1c`
- targeted-filter.json: `b6f8ec4d37c5712fcd0e3113796204bc1bedc9fdf2080625758de3052f8e346d`
- inputs/normal-form.md: `5cc83c225a03ba670b7859d1a64aec161611ec9cc35fffe79479fdd5b7dadf62`
- inputs/catalog.json: `7c085250359b5445e8ef8da3f35763d495d5319660ca34c63aaf447078658bd5`
- inputs/dual.json: `9aac29c629b7eb7d2e507eb663571221626a435b995809f05ecad627db126fab`
- inputs/frontier.json: `486c673e7ddb1c0b427f4a819abd1b4854d775d1bbc1a90a3859574cd6995496`
- inputs/original.json: `6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb`

Any substantive change to the proof, checker, pins, inputs, or result invalidates this exact-byte verdict until rechecked. Documentation added after this review is outside its exact-byte scope.
