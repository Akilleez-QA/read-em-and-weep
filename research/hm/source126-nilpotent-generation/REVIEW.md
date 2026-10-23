# Independent review of source126 generation restriction

Verdict: accepted for the conditional theorem stated, relative to the four pinned mathematical inputs. This is a mathematical review with bounded executable regression checks, not proof-assistant verification and not a complete proof repair.

Reviewed immutable candidate:

- PROOF.md SHA256: 69242887f52e5f92066c57c7f7630a143e4cca1e8dcd92565b1ea1c03fccba91
- verify.py SHA256: 3b6d7eb3979cd0da2daf725e6448c08318233e2906d315b08345c20d206e9835

## Dependency and grading check

Read the four immediate source files recorded in INPUTS.json, including their scope boundaries. PR925 Section 2 is a universal degree-zero-generation lemma despite its c-d-f application elsewhere. It applies to N2=K3 positive and N4=K5 positive, where Kd=H1(End0(F_HM)(d-1)). PR933 uses exactly these H1 twists 2 and 4 and proves equality of actual subspaces im(q+)=im(Q), not only equality of characters. Its global theorem has no c-d-f assumption. Both use the canonical invariant quadric in the positive-coordinate symmetric square. Negative products are the same fixed-variable B_u A_v. Thus N4=im(Q)+im(q-) is available under the actual source126 occurrence assumption, without a full-module extension of any pencil endomorphism.

## Independent argument checks

1. If e2=0, both negative-pencil intertwining equations give e4 B_u A_v=0. Applying e4 to the actual spanning identity proves im(e4Q)=im(e4). This requires no direct-sum claim and no Q compatibility. When compatibility is imposed, it forces e4=0.

2. The radical is represented by constant maps b:Hbar to C that carry R into F and vanish on C. Since R spans Hbar, restriction to R is injective. For F=F0 tensor omega on P1, equivariant Serre duality gives Hom(R,F)=Hom(H1(R),F0) naturally: a morphism R to F0 tensor omega pairs H1(R) with H0(R* tensor omega) and then applies the trace H1(omega) to C. It is the induced H1 map, not an unrelated isomorphism of equal-dimensional spaces. The determinant character is trivial for the specified subgroup of SL2. Hence j4=0 forces j=0.

3. PR944 gives D_Q=C1 plus J_Q. Radical maps have zero action on the F source block, whose N2 dimension is 27. Therefore a zero first endpoint forces the scalar coefficient to vanish, and then the preceding argument forces the radical coefficient to vanish. The first-endpoint restriction on the whole D_Q is faithful.

4. In Type III, J_X is a genuine nonzero constant arrow supported on the span P+D of X. Its restriction to X cannot be zero. Its induced H1 map is nonzero by the preceding duality argument. The source V+P and target P+2D have a unique common irreducible, the single P on each side. Schur's lemma therefore gives rank four, not merely an upper bound. N2_X=0 gives j_X,2=0, so im(j_X,4 Q)=P. This excludes the pure X radical direction from J_Q. Projection J_Q to the one-dimensional J_Y is injective; a nonzero survivor has a unique normalized graph form y+t x. Neither its existence nor its parameter has been determined.

5. The Type III X vertex projector is an actual negative-pencil endomorphism, with first component zero and fourth-component image V+P. Applying the same image identity gives the additional onto row p_X,4 Q of rank seven. This does not assert that the splitting is Q-stable; the projector is specifically incompatible.

6. The kernel/cokernel warning is correct: square-zero equivariant actions on multiplicity-free A+D and P vanish, but that does not imply the full radical map vanishes. The supplied synthetic endpoint example correctly demonstrates the missing generation premise and explicitly does not pretend to be an actual HM pencil.

## Reproduction

Ran python verify.py and python -O verify.py from this directory. Both completed with 1,326 checks, including 1,008 parity regressions, and identical stated conclusions. The input authentication recomputed the four exact Git blob identifiers and SHA256 hashes. The McKay recurrence, unique common P channel, dimensions four and seven, synthetic negative control, and finite graph-line checks passed. The finite tests support the written general proofs; they do not establish geometry by sampling.

## Limits

The remaining mixed radical direction is unresolved. Types I and II still have the prior radical dimension upper bound two. No source-dual pairing or stable label is removed. No actual HM parameter, coefficient, point, derivative, matrix, or selected-instance rank was evaluated. No external experiment was restarted. No full-module lifting, scalarity, realization, or complete repair is claimed.
