# Independent review of the single-line symbol transfer

## Verdict

No mathematical blocker found. For the u=0,k=1 single-compatible-element rows, the proof establishes the actual interfaces needed to recover internal second vanishing and the canonical two-dimensional cubic gate without assuming full-J compatibility. The applicable rows are Type I(5,4), Type II(5,4)/(10,9), and Type III(10,9). The cubic value remains unselected.

## Checked actual interfaces and transfer

1. Kernels of the individual endpoint actions form a subcomplex for the whole actual pencil. Square-zero action descends to a chain map from the quotient to this subcomplex.
2. The single-line character theorem gives H0(S)=A+D, H1(S)=D, H0(T)=D, H1(T)=P. The actual kernel inclusion and long exact sequence give the connecting and projection isomorphisms with the stated sign convention.
3. The descended degree-zero action on quotient cycles is injective: its vanishing means the actual endpoint image is zero, hence the lift lies in ker(j2). There are no boundaries in degree zero. Equivariance therefore makes it a nonzero scalar onto the D kernel. Degree-one action is zero because Hom(P,D)=0.
4. First-symbol naturality kills the internal D channel. The only A channel is multiplication. If its scalar were zero, an S-valued first correction would make the original second A obstruction vanish because H1(S) maps to zero in H1(M). This contradicts the actual retained nonvanishing theorem. Thus the coefficient is nonzero, without importing the full-J conclusion.
5. The original second comparison follows directly from the connecting map applied to a first correction. It forces the quotient first family to be nonzero; the unique representation channel identifies it with universal multiplication modulo V6. The imported rank and kernel facts therefore apply to the actual quotient family, without a source2 occurrence assumption.
6. The internal quadratic symbol construction, rank-one exclusion, and third comparison use precisely these now-established interfaces. Imported original third vanishing forces the internal second to be globally zero.
7. The normalized internal cubic construction and its choice independence then apply. On the quotient-first-surjective open, kernel classes lift through every finite order, so the one radical map suffices to give r kappa=0. The universal dimension, nonflex restriction witness, and cubic rank-one exclusion depend only on A,D,E. They yield the same two-dimensional space and exact generic zero/nonzero comparison with original fourth.
8. The u=1,k=0 quotient is instead acyclic and may be removed formally; it is not assigned the non-acyclic D interface. The u=k=1 rows retain their separate top obstruction. No full-J collective image identity is used here.
9. The secondary-null-homotopy construction is explicitly not transferred. The single generator acts nontrivially on cohomology, so the kernel line required for that construction is absent. This is the essential limitation preventing an unjustified conclusion about a secondary scalar or cubic vanishing.

## Independent tests and frozen bytes

Read the complete proof and checker. Independently ran normal and optimized Python; both passed41 checks with identical stdout. The checker authenticates five pinned inputs, verifies each row's cohomological dimensions, tests a synthetic single-generator diagram and correction signs, retains the full formal fourth-order correction terms, and checks the absence of a null line for a nonzero one-dimensional scalar action. These are universal or synthetic controls, not actual HM evaluations.

- PROOF.md: `9245cd7a00161735d86b56bb1efaf8b3ec505b82fce8c2a6d525b2ca3ea0ae70`
- verify.py: `f62590cfed7a320cd45946145e4c91de1f1bd635d5bd9a2cafdd3a7b055a4005`
- INPUTS.json: `be08ff23031f54c14fe76cede06a6701884ea653b04dac8cf2b4749f4586724e`

No actual instance, nonzero cubic value, source occurrence, or complete repair is certified. The mathematical dependencies remain explicit and the finite tests are not proof-assistant verification.
