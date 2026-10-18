# Independent mathematical and static-source audit

## Verdict

Accepted as a conditional exact reduction of the explicit paired current-derivative family of the complete source-adjoint remainder. It establishes neither vanishing nor a rational-divergence certificate for that remainder. No physical/model/source/owner/jet value, matrix-polynomial product or retained coefficient was computed; source files were inspected as inert text and ASTs only.

## Direct mathematical review

For commuting derivations, differentiation of A inverse gives curl L = -[L_a,L_b]. Since G=BA, its logarithmic current is T=L+U. Subtracting curl L from curl T gives curl U = -[U_a,U_b]-[L_a,U_b]-[U_a,L_b]. Both mixed terms are necessary. The literal source k is -1/4 times the antisymmetric product of inverse and transition derivatives, so k_ij=[L_a,L_b]/4 with positive sign. Thus curl U=-4(k_ik-k_ij), with k_ik formed from T, not from U alone.

The full scalar functional K includes p, original-owner/path weights, all outer/HPL/selector factors, the single existing transpose, and the finite-frame convention. Its coefficient derivative K_;d(X)=V_d(K(X))-K(V_d X) is A-linear by Leibniz. Perfect trace pairing on the full matrix module permits K(X)=tr(CX) without changing that existing transpose. The derivative is tr((V_d C)X); no coefficient factor may be silently treated as constant.

Source.E has signs +,-,+,- with axes a,b,b,a and endpoints jk,jk,ij,ij. Taking the established adjoint gives -s_jk/2 times curl K(L), and +s_ij/2 times curl K(U). Substituting the two curls gives exactly formula (6): the added curvature terms are +2(s_ij+s_jk)K(k_ij)-2s_ij K(k_ik). Cyclicity gives tr([L_a,C]U_b)=-tr(C[L_a,U_b]); consequently formula (9) has the stated covariant signs. No scalar-leaf derivative or extra integration by parts is introduced.

Static comparison with the supplied frozen compiler confirms seven ordered kinetic terms, three negative gerbe terms, left normalization then trace-free projection, both original Fk branches, and both E branches. RawSource overrides T alone. Formula (7) leaves this entire algebraic contribution untouched. Formula (8) merely collects existing k terms; F_q-2s_q,ij is not zero by this argument. Second transition derivatives in the baseline and dependencies of the kernel remain. The thirty retained tests remain unresolved. No full-four-slot exterior alternation or separate-branch closure was invoked.

## Checks and boundaries

The main free-word checker was reviewed, including inverse reduction and cyclic reduction. Its fifteen explicit checks survive optimized Python. The added fixed hashes bind the eight-branch metadata, inert compiler/raw-engine snapshots and supplied source-adjoint proof/review. Hashes bind bytes, not provenance or truth. The independent checker uses a separate abstract four-current word expansion and static AST checks for baseline/Fk retention. It never imports the main checker or frozen sources. The sixteen disposable-copy mutation runs cover source/metadata/proof corruption and algebraic sign, transported-mixed-term and kernel-derivative changes in both Python modes.

The proof of the inherited full source circuit, commuting curve derivations, common-frame convention and residue interpretation remains conditional on the cited prerequisites. The two immediate upstream proof/review documents are included for inspection; their further dependencies are external and are not newly replayed or authenticated here. This is not a self-contained formalization of geometric premises.
