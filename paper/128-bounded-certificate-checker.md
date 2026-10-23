# 128. Bounded rational checking of supplied finite certificates

[PR1112's immutable interface](https://github.com/Akilleez-QA/read-em-and-weep/blob/937b29af67c5256f009f79308ba1d43c600a20a1/research/hm/source2-finite-certificate-checker/README.md) and [executable checker](https://github.com/Akilleez-QA/read-em-and-weep/blob/937b29af67c5256f009f79308ba1d43c600a20a1/research/hm/source2-finite-certificate-checker/check_certificate.py) implement the finite theorem of [chapter126](126-finite-sequential-obstruction.md). This is a code contribution, **not a new actual source certificate or a selected rank**.

Over Q[a0,a1,a2], the checker accepts supplied maps and twenty-four homogeneous corrections and tests

    x0=s,   Qx0=i_P,   Qx_i=−T x_(i−1), 1≤i≤23.

It checks full polynomial coefficients, dimensions, degrees, exact rational serialization and content digests. Optional supplied nonsingular generator actions are checked by exact substitution, not sample evaluation. Group relations, generating property and actual representation provenance remain external obligations; an empty list explicitly reports equivariance not checked. Algebraic fields are unsupported and must not be rounded to rationals.

Coefficient collection gives (Q+tT)Σt^i x_i=i_P+t²⁴Tx23. With the separately authenticated actual identities Qd=0 and Td=i_P Ld, the original correction has residual −t²⁵Tx23Ld. **Tx23 need not vanish.** The known lower pivots would then force maximal-minor order at least31, beyond degree30. That last inference uses the mathematical theorem's actual-source hypotheses, not arbitrary matrix shapes.

The program never authenticates actual geometry, searches for corrections or determines actual original positive rank. A matching or caller-supplied digest binds bytes, not source identity. Even original dimensions41→37 with P dimension4 do not suffice. All executed examples are universal or synthetic; no actual certificate is included. Rejection of one input is not nonexistence of another certificate and does not prove rank37.

Fixed limits include eight megabytes, dimension64, eight supplied generators, 100000 terms and five million arithmetic steps. A resource stop is explicitly inconclusive, not a mathematical rejection; these bounds do not guarantee capacity for every dense original-size certificate. The retained tests cover exact coefficient changes, signs, invalid serialization, optional actions, nonzero terminal tails and provenance limitations. They are not formal certification of the repair.
