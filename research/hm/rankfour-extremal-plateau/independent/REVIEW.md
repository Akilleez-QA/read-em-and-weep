# Independent review: exclusion of the rank-four maximal (3,3) plateau

## Verdict

**PASS, conditional on the stated actual geometric premises.** The reviewed proof excludes generic second-fundamental-form rank four with maximal ordered plateau lengths `(k,l)=(3,3)` on the fixed physical parameter line. I found no mathematical gap in the final proof. The independent controls reproduce its numerical, cohomological, parity, and representation-theoretic deductions without evaluating any actual HM coefficient, parameter, jet, matrix, or rank, and without importing a rank-three exclusion or rerunning a historical source enumeration.

This does not exclude rank four in another profile, prove rank at least five, establish square-map surjectivity, or repair the original theorem. Relative to an already justified overlist of 27 bad coarse profile bins, this removes exactly one bin, leaving 26; the nine bad rank values 4 through 12 are unchanged.

## Frozen reviewed artifacts

These exact files are retained under `reviewed/`. The review applies to these bytes, not to an unversioned future replacement.

- `PROOF.md`: `7fac6f279bc25dcc0561743dfae189dd70f2cf98e81ad11371745f1c954d4e6a`
- `verify.py`: `debf8427b38d9fc7a0d1f71c11b0096edf4f730d6d0189af2eaea7aec7e275cd`
- `RESULT.json`: `61f319f9c67382d9d96c9bb5d66b32db6b17bc8cf3c0cb23f29824cf05dbf200`
- `CANDIDATES.json`: `0a3a59920d50b5f098c439fa84fa7be44fbfda906ec95634369209c390625ef8`
- `INPUTS.json`: `8c9546d1d7fa5c4646ff4aaf388271d6bb5a8daa98e3e5442235b8525a158cb5`

The original actual splitting/persistence theorem is retained with SHA256 `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`. For an independent check of the general changing-rank derivative construction, the original rank-two necessary-bound note is retained with SHA256 `868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c`; only its general sheaf/derivative facts are used, not its rank-two conclusion. The author's rank-three comparison source and orbit-ramification source are also retained in the frozen packet, but neither rank-three inequalities nor orbit-size gaps are needed here.

The manifest `INPUTS.json` authenticates all ten copied input artifacts. Hashes authenticate exact text, not the truth of all transitive geometric prerequisites.

## 1. Domain and geometric premise audit

The argument stays on the actual `T=P(W*)` over `C`, with the fixed physical standard representation `W`, its determinant-one linearization, and `G=SL2(F5)`. The standard even three-space `A=Sym^2 W` is not exchanged with the other three-space `V`.

The actual sequence is `0 -> E -> H O -> Q -> 0`, with ambient dimension 30, rank/degree `(17,-54)` for E, and `(13,-54)` for Q*. The input that E has no constant subbundle and spans H is essential. These are not consequences of rank and degree alone.

For the hypothetical plateau, `F0 < ... < F6`, `E=F3`, and `rank Fi=5+4i`. Interior sheaf kernels and saturated forward transforms identify the neighboring stages. The regular induced maps `Li -> L(i+1)(-2)` have generic rank four. Saturation ensures these maps extend over exceptional parameters; they are not maps only over the generic point. No endpoint derivative rank is assumed to equal four.

A constant subbundle in any Fi with i<6 propagates back into E; a proper constant span of any Fi with i>0 propagates forward to contain E. Thus neither can exist. The reversed annihilator filtration `Di=F(6-i)^perp` has the corresponding properties in H*. This uses the actual annihilator Q* at the center, not an independently rotated or dualized coefficient pencil.

The persistence argument applies at i=0 as well. Although F0's derivative rank may be smaller than four, its derivative lies in F1 because F0 is the derivative kernel of F1. Hence the forward transforms of a line in F0 remain within the displayed stages; equality of F0's first transform with F1 is not needed. The same observation applies to D0.

For a saturated line O(-e) in Fi, the derivative span reaches its constant coefficient span in at most e steps. This is the universal polynomial identity, not an evaluation of chosen coefficients or jets. If i+e<6, that span lies in an interior stage, a contradiction. Therefore `H0(Fi(d))=H0(Di(d))=0` when i+d<6. In particular the top degrees of F0, F1, F2 are at most -6, -5, -4, respectively, and D0 has degree at most -6.

## 2. Endpoint equality and the index check

Let `a=deg F0`, `b=deg F6=deg D0`, `ci=deg Li`, and `delta_i=c(i+1)-ci-8>=0`. The ranks and persistence give `a<=-30`, `b<=-6`. Exact elimination of c1 gives

    a+b = -36 + delta1+2delta2+3delta3+2delta4+delta5.

All five weights are positive. Consequently a=-30, b=-6 and every determinant defect is zero. This does not require an invariant-divisor lower bound, or even the additional even-parity constraint on the defects.

Thus the six increment degrees are `(-16,-8,0,8,16,24)`. The regular generically invertible adjacent maps have zero torsion-cokernel length, so they are actual equivariant bundle isomorphisms. Put `B=L3`; then `Li=B(2i-6)`, with rank B=4 and degree B=0.

The potentially dangerous index is correct in the final packet: **L1=B(-4)**, not L2. Therefore the exact F0-to-F1 sequence twisted by 5 has quotient B(1).

F0 has five ordinary summands all of degree -6. F1 has eight of degree -5 and one of degree -6. Perfectness and central parity identify the single degree -6 coefficient as the trivial representation. Hence `H1(F1(5))=0`, and the quotient sequence gives `H1(B(1))=0`. The left term F0(5) is acyclic as well. It follows that every B degree is at least -2; rank four and total degree zero force every B degree to be at most 6.

## 3. Independent derivation of the source Z, without old enumeration

Persistence gives every E degree at most -3. The actual rank 17 and degree -54 leave deficit three relative to seventeen degree -3 summands. At odd degree a coefficient representation has even dimension at least two, so a degree -5 block already costs deficit at least four and cannot occur. The only possibilities below degree -3 are therefore:

- one dimension-three even coefficient R at degree -4;
- one trivial coefficient at degree -6.

The actual identity `H1(E(1))=W'+3T6` is imported from the actual coefficient presentation. A degree -6 trivial tail contributes `Sym^3 W=S4`, which is forbidden. The dimension-three even possibilities at degree -4 are A, V, and 3 copies of the trivial representation. Multiplication by W gives forbidden W/S4 constituents for A or 3·1, but `W V=T6`. Thus R=V and the degree -3 coefficient is `U=W'+2T6`:

    E=U O(-3)+V O(-4).

This newly derived three-unit deficit argument proves the needed Z shape without consulting the historical 28-type list, the four-source classification, or any rank-three coverage theorem.

## 4. Both F2 tails and the full long exact sequence

F2 has rank 13, degree -54, and top degree at most -4. Its ordinary degree deficit is exactly two. There are precisely two partitions, refined by central parity:

    F2=R11 O(-4)+X O(-5),  X=W or W';
    F2=R12 O(-4)+O(-6).

In the first case `H1(F2(3))=X` and `H1(F2(4))=0`. In the second case these are respectively W and 1, by `H1(O(-3))=W` and `H1(O(-2))=1`. In particular the possible degree-four H1 is never A.

The actual source Z gives `H0(E(3))=U` and `H1(E(3))=0`. Since `H0(F2(3))=0`, the exact sequence forces

    H0(B(3))=U+W or U+W'.

The representation equality follows from the long exact sequence and semisimplicity. It does not assume a section map is onto before its cokernel is checked.

## 5. An independent short quotient classification

Central parity, rank four, degree zero and the derived window [-2,6] give a finite abstract problem. Exact character positivity against either cubic target permits only these individual blocks:

    1 O(-2) : W
    P O(-2) : T6+W'
    V O(-2) : T6
    W' O(-1): T6
    1 O(2)  : T6
    W O(3)  : 2T6+W'
    1 O(4)  : T6+W'.

All other parity-compatible irreducible blocks either contribute a forbidden constituent or exceed a target multiplicity. Each target contains W', so one of P O(-2), W O(3), or O(4) must occur. P O(-2) uses all rank four but has nonzero degree -8. W O(3) contributes degree 6 in rank two, while the remaining two ordinary degrees are each at least -2, so total degree cannot be zero. Thus O(4) occurs. The remaining rank three and degree -4 can only be `O(-2)+W' O(-1)` from the eligible list.

Consequently

    B=O(-2)+W' O(-1)+O(4),
    H0(B(3))=W+W'+2T6.

There is no U+W' solution. This direct positive-character argument is independent of the author's enumeration. The independent checker also enumerates the complete forced-window multiset problem and reproduces its 20 shapes and the same unique survivor; this is a new universal rank-four classification, not an old source-instance enumeration.

## 6. Final obstruction

Euler additivity at twist four gives

    chi(E(4)) = 2D+3V+3P,
    chi(B(4)) = A+2D+V+P,
    chi(F2(4)) = 2V+2P-A.

Its ordinary dimension is 11, consistent with rank and degree. Restoring either permitted H1(F2(4)) correction, namely 0 or 1, still leaves coefficient -1 at the physical A. Therefore H0(F2(4)) would not be a genuine representation. This excludes the unique cubic survivor and the entire hypothetical corner.

The contradiction is not an ordinary dimension contradiction. The trivial H1 correction has been included and does not repair the nontrivial A constituent.

## 7. Reproduction and computational boundary

`check.py` is independently implemented and does not import the author's verifier. It reconstructs the nine character rows from exact binary-icosahedral trace classes in Q(phi), phi^2=phi+1, checks weighted orthogonality and all McKay tensor products used, proves the endpoint identity by coefficient vectors, derives Z from the small deficit, filters the quotient blocks, and checks both H1 corrections.

Normal Python, optimized Python, and execution from `/tmp` produce identical `RESULT.json` files. The author's frozen verifier also runs normally and under optimization, both reproducing its supplied `RESULT.json` with its declared 768 controls. Its candidate artifact is checked against its derived list. The count printed by that verifier is recorded before the additional final candidate-artifact consistency assertion, which does not affect its result or mathematical claim.

The scripts authenticate source bytes and check universal arithmetic. They do not prove the original HM presentations, saturation theorem, or persistence geometry by computation. Those geometric premises have been inspected in the retained written sources and remain explicitly conditional. No forbidden actual-instance calculation or external write was performed.
