# Independent review: fixed-context raw-scalar substitution

Verdict: accepted under the stated semantic premises. No counterexample to the bounded substitution theorem was found. This is not approval of a whole geometric denotation theorem, executable release, or an ID0 value.

## Scope and evidence

Reviewed the complete integrated PROOF.md, check_static.py and expected-context.txt, the pinned compiler and lift-schema text, the complete raw_engine text, and the inert candidate program text. The two permitted static runs passed identically in ordinary and optimized Python; their fresh outputs accompany this review. The input manifest binds 88 evidence files. No production import, source compilation/execution, model/owner/jet construction, actual polynomial product, patch application, or publication occurred.

Source bindings inspected:
- compiler: SHA256 28e95b87adefaba0d4ec886a7ab272f252f376bbb1fc26e0a387bc05f896a386
- lift schema: SHA256 3de33f88790e46bb62d4c400143ef62dea8b0b15d51bd18a4fb70689e3261f31
- raw engine: SHA256 c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9
- inert candidate program: SHA256 ad0603264992c2dfb425451f59d183a64d139b3c25db43b7866d7683851fc62a

## Exact accepted arrows

1. With other leaves fixed, scalar discrepancy epsilon = s' - s gives

   Delta E = (V_a epsilon(q,j,k) L_b - V_b epsilon(q,j,k) L_a
              + V_b epsilon(q,i,j) T_a - V_a epsilon(q,i,j) T_b)/2.

   Source.E has precisely these signs, endpoint derivatives, and scalar/matrix ordering. T_a is the ordered product gi(i,j) gi(j,k) D_a(g(j,k)) g(i,j). Interpreting gi as an inverse needs determinant one because Mat.inverse literally returns the adjugate; congruence needs only its unchanged literal denotation.

2. RawSource overrides only T, as the 1-by-1 wrapper of s_raw. Source's only calls to self.T are the two endpoint calls in E. Reading the complete methods and raw leaf implementation finds no indirect T dependency in the seven kinetic terms, three negative gerbe terms, tracefree baseline, or Fk terms. Hence Delta R is exactly the sum of the two complementary Delta E terms. Those other terms cancel in the difference; they are not asserted to vanish.

3. Delta J0(t)_(1,1) = I_(t0) transpose(Delta R(t)) P_(t0), with no reversed outer factors. The face differential retains the code's (-1)^j order. The stage recurrence applies H_(1-s,t0) followed by coefficients (1,-1,1). H acts on one varying block at a time. In particular its right-homotopy contribution is present only for an input block with v=1 and u<3; it is (-1)^r (IP) F_(u,1) H_(u+1), placed at (u+1,1). No product contains two varying residual blocks. Each recursive face uses its own first owner, and the enclosing homotopy uses the enclosing tuple's first owner. There is no extra row-End conjugation.

4. The candidate uses ell(J2)=J2_(3,1)[5,0]+J2_(2,0)[1,3]+J2_(2,0)[4,2]. It computes the lift on canonical owners, multiplies by sorting parity and the weights of the original owners, sums all assignments with staircase orientations, and only then extracts mask15. Thus the displayed Delta F identity in section 3 follows. No commutation of projection with multiplication is needed or asserted. A zero-parity branch cancels without evaluating the lift.

5. For differential-field equality at every scalar call, including calls reached through recursive faces, epsilon=0 implies all complementary derivatives vanish. The previous arrows give Delta F=0. With authenticated Laurent representatives and the terminal premises, the mathematical terminal agrees as well. The more general error response is additive and Q-linear; derivatives do not warrant K-linearity.

## Caches, support and operational boundary

PhysicalModel caches are indexed by self and the relevant owners/directions. weighted_assignment constructs a fresh model and source/lift per assignment and clears decorated model caches in finally. Source.residual and Lift.at have local memo tables. Under fresh or denotationally equivalent caches and pure exact operations, these do not introduce an extra scalar dependency or spoil finite-stage induction. Reusing stale cache entries after changing a leaf is outside the theorem. Equal numerical samples or zero-order jets are insufficient for differential-field substitution.

Block support is selected by degree and tuple structure, not by a residual value test. Fixed finite domains must include all calls reached by the entire weighted sum and recursive face deletion. Resource limits, changed exception behavior, mutation, and arbitrary callbacks are not covered by comparison of successful mathematical results.

actual_id0 still raises RuntimeError before argument-dependent work. All preterminal/terminal expressions describe an unreachable specification under semantic premises, not a successful current execution. The static checker does not prove its own prose report: AST/byte checks plus the mathematical inspection above support the conditional theorem. In particular, a text check for selector or projection alone would not prove the entire outer loop; the full pinned candidate loop was inspected here.

## What remains unproved

The accepted chain is:

conditional primitive/frame/raw-scalar denotation
  -> equality substitution in the fixed complete source
  -> fixed recurrence J0 through J3
  -> fixed selector and complete weighted sum
  -> equal mask15 preterminal rational
  -> equal certified mathematical terminal, when defined.

It is not:

raw scalar correctness -> intended geometric whole residual -> global cocycle/class -> intended ID0.

The historical A receipt remains imported, exact operations/localization remain premises, other source leaves and global raw/N14 comparison remain unauthenticated, and the recurrence does not establish the J3 closure equations. Owner/domain, regular extension, original-frame transport, retained pairing, and common-frame/global identification obligations remain. The terminal kernel equivalence is correctly conditional on authenticated same-frame Laurent representatives; it cannot replace Laurent certification with three local coefficient samples. The existing formal countermodel is correctly labeled an information-gap example, not a realizable pinned-model counterexample.

No substantive correction is required. For maximum precision when quoting the homotopy prose, retain the explicit condition v=1 on its second branch and call the response Q-linear rather than field-linear. The theorem already supplies the needed fixed-context and exact-derivative qualifications.
