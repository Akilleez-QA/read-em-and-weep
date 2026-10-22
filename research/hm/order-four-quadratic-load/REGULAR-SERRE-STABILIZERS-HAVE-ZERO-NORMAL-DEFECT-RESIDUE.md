# Regular Serre stabilizers have zero normal defect residue

## Exact frame-change theorem

Let R be a local ring in characteristic zero, let f,g be a regular sequence, set sigma=(f,g)^t, and put

    N=sigma sigma^t J=[[fg,-f²],[g²,-fg]],
    J=[[0,-1],[1,0]].

Every P in SL2(R) satisfying P sigma=sigma has the form

    P=I+t N,  t in R.                                 (1)

Indeed, the rows of P-I are syzygies of the regular pair, so

    P-I=[[a g,-a f],[b g,-b f]].

Since its determinant is zero, detP=1+a g-b f. Thus a g=b f. Regular-sequence cancellation gives a=f t and b=g t, proving (1). This is a sheaf-local statement and does not assume the complement of the zero scheme is the whole domain.

Now let R_tilde be a first-normal thickening with ideal (q), q²=0, and let N_hat be ANY trace-free square-zero lift of N. If t_tilde lifts t, then

    P_hat=I+t_tilde N_hat

is determinant one, lifts P, and fixes N_hat by conjugation. The inverse is I-t_tilde N_hat. Trace zero and N_hat²=0 give detN_hat=0 by Cayley-Hamilton, so detP_hat=1 exactly.

Any other determinant-one lift of P differs from P_hat by a factor I+qK, with K trace-free on the reduced ring. Its effect on N_hat differs by q[K,N]. Therefore:

    A determinant-preserving Koszul stabilizer contributes ZERO
    to the tangent-modulo-conjugation normal residue M(-2).       (2)

The statement is about the full commutator quotient, not a degree truncation. It applies equally to the actual midpoint lift and to a locally constructed Hessian square-zero lift.

## Consequence for changing regular Serre frames

If two determinant-compatible frame transitions carry the same regular section pair to the same target pair, their quotient is exactly such a stabilizer. Hence their contributions to the normal defect residue agree. One may therefore compute that residue using any convenient determinant-compatible lift of the generator transition. No unexamined Koszul-stabilizer residue remains.

This removes one explicit obstruction to using UNIVERSAL-QUINTIC-GENERATOR-HESSIAN-COVARIANCE.md. Its elementary transition g->g+p f has determinant one, and (2) shows that changing a determinant-one frame realizing this SAME generator transition cannot introduce a further residue.

## What is not proved here

A general change of generator normalization or of physical/stack line frames need not have determinant one in the chosen coordinates. One must compare its determinant with the physical O(2) and normal-equation trivializations, rather than silently apply (2). Scalar changes act trivially on the adjoint matrix by conjugation, but their physical-line and equation factors still require explicit accounting. Likewise this lemma does not identify an arbitrary local Hessian lift with the actual midpoint lift.

Once ALL non-stabilizer transition residues have been accounted for and corrected, comparison with the actual midpoint gives a global invariant section of M(-2). The separately proved H0(M(-2))^G=0 then forces that comparison residue to vanish. This final implication is conditional on the complete transition comparison, not a substitute for it. No absolute third-value claim follows from (2) alone.

## Reproduction

Run verify_regular_serre_stabilizer_normal_residue.py. The script verifies the universal syzygy determinant formula, N²=0, and the stabilizer conjugation identity. The arbitrary square-zero-thickening argument is the ring-theoretic proof above. No actual source coefficients, actual-instance rank test, or parameter scan are used.
