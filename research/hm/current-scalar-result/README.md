# Exact-Q replay of the current scalar image

The recorded result is that all 81 coordinates of the current scalar image are
zero over Q: 46 coordinates from exact contractions and 35 from integral
structural relations. The map is

    L(X) = X_02[0,0] - X_13[10,0].

In the flattened negative component this is slot 0 minus slot 70, equivalently
coefficient n[index] minus n[5670 + index]. The Laurent basis has each exponent
in {-3,-2,-1}, with the last exponent fastest.

**This does not prove vanishing of the full obstruction.** The scalar detector
has a kernel. The result only concerns this pinned current scalar map.

## Reproduce

Requires Python 3, standard library only. From this directory:

```sh
python verify_result.py
python test_verify_result.py
```

Run without `-O`. Paths are relative to the checker, so these commands also work
from another working directory. No network, external files or packages are used.

The replay hashes every supplied data file, derives the 132 integer coefficients
of G(T,z)^(-70) modulo (T^6,z^22), and contracts the 24 supplied full quotients.
Here

    G(T,z) = 1+z + T(1+3z+z^2) + T^2(z+z^2).

For a monomial m in {0,1,2}^4, coordinate index is
sum_i (2-m_i)3^(3-i), and Laurent exponent is -m_i-1. For an active permutation
(i,j,k,l), m_i=2, S=sum(m), d=3+m_j, L=21-m_l. The selected source exponent is

    a_i=272, a_j=212-r, a_k=159-S+r-ell, a_l=48+ell,

with 0<=r<=d and 0<=ell<=L. Its retained slot is (r,30+S,ell), multiplied by
[T^(d-r)z^(L-ell)]G^(-70) and the permutation sign. Numerical targets have
3<=S<=6; only homogeneous slots 33 through 36 are interpreted. Absent higher
homogeneous slots are never treated as zeros.

The replay reproduces 432 edge selections, 44,280 requested rows, 12,144
distinct physical source exponents, 656 nonzero requested rows, 320 nonzero
distinct source coefficients and 152 nonzero signed edge selections. Their
46 target sums are all exactly zero. It also checks the 47-row identity minor,
the 35 structural-zero indices, and all 47 relation residuals.

## Evidence and reproducibility boundary

- `final-result.json` is the unchanged recorded final result. Its SHA-256 is
  `0ae5a9176b5d47afe85ae3a144fed2df55079396ae5e789461ef9358ea98f791`.
- `quotients/` contains all 24 unchanged terminal quotient exports, totaling
  about 87 KB, with integer coefficients and common denominator 64.
- `relation-rows.json` is an unchanged compact relation record. It records
  historical modular ranks, but this replay does not infer rational rank
  stability from them. The integral certificates and their application to the
  actual rational class belong to the separate scalar-proof package.
- `data-pins.json` freezes these public data files. The historical full-archive
  manifest digest `547b8b476613a06e32eec8581835194642bc4603b1218a96e7951ab9955320cd`
  identifies a 626-artifact archive; that archive is not bundled here and its
  digest is not itself a public reproduction of its contents.

**The portable checker is a supplied-quotient replay. It does not regenerate the
geometric source DAGs or independently establish that these supplied quotients
are its coefficients.** The source and terminal computations were checked in
the recorded calculation, but publishing their end-to-end regenerators remains
a distinct reproducibility task. This small package does not hide that gap.

The zero assignments for the 35 structural coordinates use the proved
integral identities. The standalone arithmetic check of an identity minor does
not by itself prove those identities hold for the actual class. Consult the
scalar-proof package for that mathematical dependency and its explicit source
hypotheses.
