# Independent audit: universal synthetic transfer regressions

20 October 2026. Existing bounded universal regression record; synthetic inputs only.

## Audited artifact and recorded checks

Artifact: transfer_regression.py.

SHA-256: db8a356897d6843ce23a0961dc3575f985d0724f492a84fc7434aaf32b3353fd.

Reviewed formal inputs: ../null-first-staircase-ranks/first-staircase-ranks.md, ../null-first-staircase-ranks/first-staircase-ranks-audit.md, ../null-diagonal-target-transfer/diagonal-target-transfer.md, and ../null-diagonal-target-transfer/diagonal-target-transfer-audit.md. Independently inspected the complete Python source and ran only that synthetic artifact, in ordinary and optimized Python, including its three built-in negative controls. No physical HM/source files or matrices were read or evaluated.

## Mathematical audit

The examples are actual bigraded complexes, not arbitrary ungraded matrices. Bidegrees are (Cech, internal). For height n, x_j has bidegree (n-j,1-n+j), and y_j has bidegree (n-j+1,1-n+j). Thus x_j has total degree one, y_j total degree two, delta raises Cech degree, Delta raises internal degree, and h lowers Cech degree. Each declared nonzero map is checked for its bidegree.

The zigzag has delta(x_j)=y_j for 1<=j<=n, h(y_j)=x_j, and Delta(x_j)=a_j y_(j+1). Its retained endpoints are x_0 and y_(n+1). Additional retained lower-row arrows v -> (3/2)w and s -> (-2/3)t exercise both incoming and outgoing finite differentials. A retained c class is explicitly absent from every differential image, preventing a falsely acyclic model.

The contractible square a,b,e,f has delta(a)=b, delta(e)=f, Delta(a)=e, Delta(b)=-f. Hence delta Delta(a)=f and Delta delta(a)=-f are separately nonzero. Anticommutation is therefore tested with real cancellation, not merely two zero composites. The suite checks delta^2=Delta^2=D^2=0 on every basis vector.

The unperturbed normalized contraction satisfies delta h+h delta=1-ip, pi=1, hi=ph=h^2=0. The chosen p is a projection onto the named retained basis, and i is its inclusion; representing both as the same column-map operation on a shared ambient dictionary is legitimate here. All relevant identities are checked basiswise.

The implemented transfer formulas are precisely I=(1+h Delta)^(-1)i, P=p(1+Delta h)^(-1), H=h(1+Delta h)^(-1), and dK=p Delta I, with alternating finite geometric series. Termination is checked explicitly rather than silently truncating. The suite verifies DI=I dK, PD=dK P, PI=1, DH+HD=1-IP, dK^2=0, H^2=PH=HI=0. Since these are linear maps over Q, basiswise checks establish the identities on the whole corresponding synthetic complex.

## Non-vacuity and sign controls

For height n the expected higher differential is independently assembled as (-1)^n times the product of the rational weights, taking x_0 to y_(n+1). Heights 1 through 4 give respectively 2/5, -2/7, 2/11, -2/13. These coefficients include the signed weights: the negative rational coefficient at height four does not mean the four-h geometric-series sign is negative.

The separate unit-weight height-four example proves the intended positive d5 sign directly. Its lift is x_0-x_1+x_2-x_3+x_4; the projected terms with zero through three h factors vanish, the term with four is +y_5, and the fifth h factor vanishes. Thus the fourth-order transfer is genuinely nonzero and cannot be replaced by a short staircase.

The plus-series negative control uses a unit-weight height-one example. The wrong lift x_0+x_1 has D-image 2y_1+y_2, whereas the wrong transferred endpoint gives y_2 on the other side of the chain-map identity. This explicitly detects the sign error which an even-height endpoint alone could miss.

For the height-four closed source R=y_1 in bidegree (4,-2), naive pR=0 but full PR=y_5. A mixed closed source 2y_1+3y_2+5y_3+7y_4+11y_5+13c projects under P to 8y_5+13c rather than the naive 11y_5+13c. All four higher-Cech corrections participate; the retained c component remains visible.

With u=x_0, dK u=PR. The complete primitive -Iu-HR is exactly -x_0, with derivative -R. Omitting HR instead gives derivative -y_5 and the explicitly nonzero residual y_1-y_5. Therefore both the full-source projection and homotopy-correction checks are substantive counterexamples, not equalities forced by zero data.

## Independent execution and failure behavior

Commands executed:

- python transfer_regression.py
- python -O transfer_regression.py
- Each of the above with --mutant plus-series, --mutant naive-projection, and --mutant omit-HR.

Both baseline runs report PASS 2553 exact checks and exit zero. The count includes checks that each geometric series terminates; it is not a count of 2553 independent mathematical theorems.

All six negative-control runs exit one, with the intended RegressionFailure message:

- plus-series: DI=I dK fails after 2557 checks.
- naive-projection: upper contribution is lost after 2555 checks.
- omit-HR: Db=-R fails after 2554 checks.

Checks use an explicit check function that raises RegressionFailure, not Python assert. Therefore optimization does not disable them. The main exception handler reports the failure to stderr and exits one, without printing the final overall PASS line. Earlier individual-height PASS lines may still appear on a failing negative-control run; scripts must respect the exit status. The negative controls are explicit deliberately false comparisons for the specified bad formulas, not a general-purpose mutation-testing framework.

All arithmetic in the examples is exact fractions.Fraction arithmetic with integer inputs or explicit integer numerator/denominator pairs. No floating-point tolerance, random sample, external dependency, network access, dynamic source loading, or physical dataset enters the artifact.

## Scope and remaining limitations

These regressions verify the stated universal sign conventions and provide concrete synthetic counterexamples to three invalid shortcuts. They do not establish imported HM cohomology, actual physical ranks, an evaluated curvature, any actual source coordinate, or any of the six remaining obstruction values. They do not exercise the geometric descent, equivariant averaging, the Moore-Penrose quotient projector, or actual Moyal multiplication; none of those is represented as tested by this artifact.

No blocking mathematical, grading, non-vacuity, optimized-mode, or failure-exit defect was found in the audited version.

## Author report cross-check

Also reviewed transfer-regression-report.md after it became available. Its bidegrees, indexing convention (weights numbered from one in prose and zero in Python), rational values, 19-vector maximum example size, explicit HR formula, mutant residual, hash, command results, and scope limitations agree with the inspected artifact and independent execution. No correction is required.
