# Independent review: canonical mixed syzygy

Verdict: PASS for the conditional theorem as stated. This review makes no actual coefficient or rank selection and performs no public write.

## Frozen artifacts

SHA256:
- PROOF.md: 7c7ce11281d5597de87d7958770ba04c33226acff8e8afdfcb311d6ff297293b
- verify.py: 3e54a6dc6b3b6ed540e99b9271f15b30a9e1bc5799f46394372c4009173ea692
- INPUTS.json: a0ed4d204534937e35e266ae2335fa2ecf59f84bc87fb97a0e9a872703a268ec
- RESULT.json: cb3f433bbaf1d682ab14e28306a9bd96058e38ec594d909c8e24814084bf8cc1

## Independent authentication and replay

All five complete original proofs were freshly fetched from Akilleez-QA/read-em-and-weep at the immutable commits in INPUTS.json. Each returned Git blob SHA and full UTF-8 content matched the manifest and retained file:

- PR1048: 0710577541a79a5d8d56e5aa693a8fc01c559112
- PR1054: 64e6bf9f1bf46440700ebab7c90a18f9d8155fd8
- PR1068: 5ae07c02624d70c0ccd33d7ec34202504173ff83
- PR1069: 827cd956e2eb574fd7d40d408e0450c8581fd7d2
- PR1071: 7198f55b877a604ade7c1759799b84bd3885d2c5

Independent `python verify.py` and `python -O verify.py` runs passed all 34 checks. Their outputs were byte-identical to one another and RESULT.json. The checker uses explicit exceptions, so optimization does not remove its checks. Its rank normal form is universal, not an actual source matrix.

## Mathematical review

1. All negative linear variables belong to the same fixed W. M2 and M4 have positive central parity; M3 and M5 have negative parity. The invariant quadratic preserves parity, while X and Y reverse it. Q3 X_l = l Q2 is actual module associativity, not an extension of h or an additional compatibility assumption on j.
2. F3 lies in both kernels: Q2 F2=I4, the actual joint-negative-kernel theorem kills W I4, and j3 X_l h=X_l j2 h=0. The definition of K3 and quotient by F3 therefore uses actual embedded subspaces.
3. T_b s lies in Z, so k_b is defined. Q3 H cancels by commutative multiplication, and j3 H=0 follows from j2 G_Q T_b s=h T_b s=0. The determinant factorization is a tensor identity, not a chosen direction evaluation.
4. Independence is correctly limited to equivariant right inverses. Their difference maps Z to I2 because Z has no A constituent; consequently the change in H lies in W I2=I3, hence in F3. No claim of a canonical representative H in M3 is made.
5. For v in K3, Q2 hY_n v=Y_n j3v=0 puts the pairing in I2. Sandwich vanishing kills F3, giving the stated canonical quotient pairing. The literal composition reproduces B(nl,mr)-B(nm,lr).
6. The kernel of Sym2(Sym2 W) to Sym4 W is the trivial representation. Since Hom_G(P,D)=0, both symmetric transfer channels kill it. Thus their cancellation does not require diagonal R=0. The formal Poisson identity and the Alt convention give exactly +4 kappa, with no missing factor of two or adjoint normalization.
7. The W-prime summand of W tensor P cannot contribute to the pairing because W tensor W-prime=P has no D. If kappa is nonzero, products nr span A and the nonzero L-star channel forces the T restriction of Hbar to be nonzero, hence injective. Semisimplicity adds this quotient copy to the two T copies in F3. The actual combined multiplicity map has source dimension six and target dimension four, so its kernel multiplicity at least three implies rank at most three.

The result does not prove kappa nonzero, rank four, vanishing of the full transfer, an endpoint realization, or exclusion of source2. It neither assumes Q preserves NC/NR nor extends h as a graded module map. The canonical syzygy and its alternating-channel detection are the new deductions; the imported sandwich and transfer identities are not relabeled as new results.
