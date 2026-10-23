# Independent review of the source113 bc exclusion

## Verdict and frozen artifact

**PASS for the entire stated bc source edge. No blocking mathematical gap found.**

This review binds to `PROOF.md` SHA256
`6816de6aa8f051b3de04f73f06c5d5583024aebe2b4aec66ec02967525f635ad`.
The inspected executables are `characters.py`, SHA256
`25d2c28c294298624ee50ce73b2a55422913f7e78b4817c7cb6e813e5004f1fc`,
and `verify.py`, SHA256
`3f22a6cd6f17e5914218ca447df4073ffe67dc24f1953b718bc2fdeb905187cb`.

The conclusion concerns only original source index113, stable label
G3.11.ad509d55173f, tuple `(0,1,1,0,0,0,0,1)`. It excludes both
high-subsystem divisor branches. It does not exclude the entire label,
other source tuples, or establish a global frontier decrement.

## Provenance and source audit

I fetched and read the exact immutable dependencies:

- [PR861 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/7b5b3371a82cb92f46ea60895e45617d0891a5b0/research/hm/profile11-source113-cf-reduction/PROOF.md).
- [PR868 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/fb398486839583f8fbd561d6dfaa6ab7b9d3ad67/research/hm/profile11-source113-cf-exclusion/PROOF.md).

Both URLs resolved, and the corresponding PR metadata had exactly these
head commits at review time. Both PRs were open, not merged; their
immutable contents, rather than merge status, are the dependencies.

I independently fetched the original actual-bundle presentation and
strict-top lemma at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`,
saved audit copies, and verified all four advertised Git blob hashes:

- Actual presentation: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- Strict-top lemma: `d7506dae49b4be43230450c4132bd5db91f137ef`.
- Original endpoint catalog: `fe0afa410d89340d3082dc814277f89fbb582c19`.
- Original stable-label catalog: `8b5971092f9ef762584912609fd5e9301c4e271d`.

The ten catalog tuples are distinct and exactly the full set with
`a=d=g=0`, `h=1`, `b+c+e+f=2`, not merely ten entries satisfying those
conditions. The bc tuple belongs to that set. The original decoder gives
`E=(V+P)(-2)+T(-3)+V(-4)+O(-10)`, rank17 and degree -54. Both catalogs
give A=(-10,2,16), B=(-18,-4,8), defect zero and source_index113 for the
stated label. I also checked the pinned
[endpoint definitions](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md):
the negative quotient really is `B=Q*/(Q*)^-`. Defect zero identifies
the actual saturated positive quotient with `A(2)`.

## Independently checked arguments

1. **Exhaustive high-line alternatives and kernels.** Strict-top makes
   the seven sections independent; their common divisor has degree at
   most12, hence is zero or the reduced twelve-orbit. For the onto
   branch, I checked the full eleven-atom support using parity and
   `(j-3)dim U<=12`, not just the four proposed kernels. The negative W
   in the twist3 Euler character forces O(-6) or W(-7), consuming the
   sole A budget. The residual S and P budgets then give precisely the
   four displayed kernels and force their degree -3 coefficients.

2. **The new bc vanishing is source-correct.** The internal target is
   exactly `T(-5)+V(-6)+O(-12)`. Every Hom from each of the four kernels
   vanishes, including W(-7) to T(-5) or V(-6), O(-6) to T(-5), and
   O(-8) to T(-5) or V(-6). Thus the raw image maps isomorphically to
   the external O(16). Its saturation follows because O(16) is saturated
   in Q(-2), and the intervening quotient E/F is locally free. The
   resulting actual subbundle M has degree -14+18=4, impossible in a
   constant bundle. This is not a transfer of the different cf internal
   image calculation.

3. **The divisor branch uses actual saturation and connection.** The
   residual complete degree6 system has kernel T(-3), with no internal
   derivative channel. The raw span has rank8, degree -8. Its saturation
   defect is at most8, whereas a nonzero invariant defect has degree at
   least12; hence it is already saturated. First partials of a quadratic
   embedding generate its first span after twist1, so all degrees are
   0 or -1. Rank and degree force all eight to be -1, and twist1
   cohomology gives Sym7 W. Its derivative kills F, is nonzero, and a
   linear bundle reaches its constant coefficient span in one step.
   Consequently C has dimension9, and C/M=O(8). Cohomology identifies
   this with complete degree8 evaluation; the actual derivative kernel
   is F and the first-jet quotient is C/F=W O(7).

4. **Both intersections are justified for bc.** If C were contained
   in E+, the nonzero map W O(7) to O(18) is onto: its degree11 common
   divisor is invariant and cannot be nonempty. Nonzero follows because
   C cannot lie in negative E. Its kernel O(-4) cannot inject into the
   actual bc remainder `T(-3)+V(-4)+O(-10)`, by the three stated Hom
   vanishings. Hence C intersect E+=M by saturation. Differentiation of
   E intersect C then lies in M, giving E intersect C=F because M^-=F.
   No saturation of the projected remainder is assumed here.

5. **The double divisor and its upper bound remain valid.** Naturality
   of the actual second fundamental forms yields `j(-2)=f12 phi`;
   no splitting complement is assigned a connection. In Q/L the fiber
   characters of O(8), O(-8), O(4) are respectively exponents 2,8,6
   modulo10, so k vanishes on the reduced twelve-orbit. Locally the
   first column is divisible by f12 in L and the second column modulo
   L is also divisible by f12, forcing every rank-two minor to contain
   f12 squared. The two projected inclusions have exactly the same
   cokernel, so their torsion divisors agree. For bc the projected
   remainder still has rank10 and degree -40 and spans a 21-space.
   The injection of its constant dual into H0(Z*) gives delta<=29.
   Subtracting 2D12 leaves an invariant effective divisor of degree<=5,
   necessarily zero. Thus delta=24 exactly, not merely a lower bound.
   The saturation U contains saturated L and has quotient O(20).

6. **The dual contradiction uses the original endpoint.** The two
   extension types have the same equivariant K-class. The original
   presentation gives H1(Q*)=M2, H0(Q*)=0 and the stated twist3 Euler
   character. Therefore R=(Q/U)* has rank11, degree -16, H1(R)=D and
   chi(R(3))=-W+Wp+S+4T. I checked the complete degree<=-2 support:
   only D(-2) or O(-6) can supply the D budget. The former forces a
   nongenuine character; the latter forces the genuine degree -1
   coefficient 2Wp+T. Strict-top applies to the actual saturated Q*
   with degrees<=-1 and injects H0(R(1)) into H0(B(1))=Sym9 W=S+T.
   The two Wp constituents make this impossible. No stronger vanishing
   H0(Q*(1))=0, source transfer of B, or horizontal splitting is used.

## Execution and limitations

I inspected and ran `verify.py`; it passed. Additional fixed abstract
checks verified exact distinct catalog membership and the complete
eleven-atom kernel and two-atom dual support lists. The geometric
arguments above were checked separately; executable success alone is
not their proof.

No actual source coefficients, selected parameters or points, derivative
values, instance matrices or ranks, models, source scans, or large
computations were used. This is an independent mathematical review,
not proof-assistant certification. It takes the pinned actual HM bundle
presentations and group action as inputs rather than reconstructing
that underlying geometry. No publication was performed. No blockers
remain within the stated source-edge scope.
