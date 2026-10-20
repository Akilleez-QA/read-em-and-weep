# Universal transfer-sign regression

## Result and strict scope

The standalone `transfer_regression.py` passes **2,553 exact checks** under both ordinary Python and `python -O`. Each of three deliberately broken alternatives exits **1** under both interpreters. The script uses only Python's standard library (`fractions`, `argparse`, `sys`); it has no network, filesystem, external-process, dependency, or source-data access. All its algebraic inputs are hand-authored rational toy complexes.

This is a bounded regression of universal algebra formulas, **not** a verification of any physical HM matrix, curvature, obstruction, source coefficient, rank certificate, or actual lift. It does not evaluate the actual six conditions, establish their vanishing, evaluate physical/source data. Passing finite examples is not itself a proof of the general HPL theorem.

Formula inputs reviewed: `../null-first-staircase-ranks/first-staircase-ranks.md`, `../null-first-staircase-ranks/first-staircase-ranks-audit.md`, `../null-diagonal-target-transfer/diagonal-target-transfer.md`, `../null-diagonal-target-transfer/diagonal-target-transfer-audit.md`. No files containing actual matrices or source implementations were inspected or instantiated.

## Reproduce

From the directory containing the script:

```sh
python transfer_regression.py
python -O transfer_regression.py
```

Each prints the four weighted staircase values followed by:

```text
PASS 2553 exact checks; universal synthetic data only
```

Run each negative control in either mode:

```sh
python transfer_regression.py --mutant plus-series
python transfer_regression.py --mutant naive-projection
python transfer_regression.py --mutant omit-HR
python -O transfer_regression.py --mutant plus-series
python -O transfer_regression.py --mutant naive-projection
python -O transfer_regression.py --mutant omit-HR
```

All six commands were run and returned exit status 1. Their respective failure labels are `MUTANT plus-series violates DI=I dK`, `MUTANT naive-projection loses upper contribution`, and `MUTANT omit-HR fails Db=-R`. Failures are explicit `RegressionFailure` exceptions caught at the command-line boundary with `sys.exit(1)`. No check relies on a Python `assert` statement. Unexpected uncaught exceptions also result in a nonzero exit.

SHA-256 of the tested script: `db8a356897d6843ce23a0961dc3575f985d0724f492a84fc7434aaf32b3353fd`.

## Synthetic complexes

Bidegrees below are **(Cech, internal)**. For each height m=1,2,3,4, define total-degree-one vectors x_j at (m-j,1-m+j), j=0,...,m; total-degree-two y_j at (m-j+1,1-m+j), j=1,...,m+1. The only zigzag arrows are

- delta x_j = y_j for j=1,...,m;
- Delta x_j = a_(j+1) y_(j+1) for j=0,...,m;
- h y_j = x_j for j=1,...,m.

Every y is annihilated by both differentials. The retained complex has x_0 and y_(m+1), with i inclusion and p projection. For the rational examples the weights are the first m+1 entries of

`(2/3, -3/5, 5/7, 7/11, 11/13)`.

The transferred differential is independently checked against

`d_(m+1) x_0 = (-1)^m (product of a_j) y_(m+1)`.

The four computed nonzero coefficients are respectively 2/5, -2/7, 2/11, -2/13. The fourth-order **operator-series sign** is positive; a negative value in the weighted height-four example comes from the chosen input weights, not a changed series sign. The unit-weight height-four example separately gives d5 x_0 = +y_5.

Each example is augmented by independent lower-row arrows Delta v=(3/2)w and Delta s=(-2/3)t, with degrees v=1, w=s=2, t=3, plus a retained degree-two class c. No differential has c in its image, so this tests a genuinely surviving class rather than only acyclic examples.

Finally, add a contractible square with a:(0,0), b:(1,0), e:(0,1), f:(1,1), and

`delta a=b, delta e=f, Delta a=e, Delta b=-f, h b=a, h f=e`.

Here delta Delta a=+f and Delta delta a=-f are individually nonzero. Thus anticommutation is not tested solely by zero composites. All unspecified arrows vanish. The largest combined example has 19 basis vectors and finite Cech range 0,...,4.

## Checked identities

Checks run on every basis vector, so by linearity they cover the entire finite vector spaces, not merely selected source vectors.

- Correct bidegrees of delta, Delta, h; delta squared=Delta squared=0; delta Delta+Delta delta=0; D squared=0.
- Original SDR: pi=1, delta h+h delta=1-ip, hi=ph=h squared=0.
- Finite alternating inverses for I=(1+h Delta)^(-1)i, P=p(1+Delta h)^(-1), H=h(1+Delta h)^(-1), dK=p Delta I. Series termination is explicitly checked after the bounded expansion, not silently truncated.
- Perturbed identities: PI=1, DI=I dK, PD=dK P, DH+HD=1-IP, dK squared=0; also HI=PH=H squared=0.
- Nonzero lower arrows and retained nonexact c; nonzero anticommuting square composites.
- Nonzero higher differentials at heights 1 through 4. In the unit-height-four model, projection of p Delta(h Delta)^j x_0 is zero for j=0,1,2,3 and equals y_5 for j=4; the fifth h step vanishes.

The implementation represents matrices by exact Fraction-valued column maps. Expected staircase coefficients and explicit source/primitive values are checked independently of the inverse-series code.

## Full-source projection and primitive counterexample

In the unit-height-four example:

`I x_0 = x_0-x_1+x_2-x_3+x_4`, and `dK x_0=y_5`.

Take the closed upper source R=y_1 at bidegree (4,-2). Then

`pR=0`, but `PR=y_5`, and `HR=x_1-x_2+x_3-x_4`.

Thus simply discarding upper cochains loses a nonzero transferred source. A mixed source checks every staircase degree simultaneously:

`P(2y_1+3y_2+5y_3+7y_4+11y_5+13c)=8y_5+13c`,

whereas p gives 11y_5+13c. The surviving c component ensures the construction does not automatically force every source to be exact.

For R=y_1, take u=x_0 so dK u=PR. The full primitive is

`b=-Iu-HR=-x_0`, hence `Db=-y_1=-R`.

The defective primitive omitting HR instead has derivative -y_5 and residual

`D(-Iu)+R=y_1-y_5`, explicitly nonzero.

The plus-series mutant is tested on a height-one unit zigzag, where using `(1-h Delta)^(-1)` in place of `(1+h Delta)^(-1)` makes DI-I dK=2y_1 nonzero. An even four-h term alone would not distinguish the wrong nonalternating convention; this odd-height control does.

## Interpretation

These tests support the consistency of the universal sign and primitive contracts in the four reviewed notes. They establish concrete counterexamples to naive projection and omission of HR. They do not import, evaluate, or independently certify any of the notes' geometric/HM premises. The remaining actual obstruction question is unchanged.
