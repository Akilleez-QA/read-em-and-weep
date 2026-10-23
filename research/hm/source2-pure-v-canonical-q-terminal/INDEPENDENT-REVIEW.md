# Independent review: canonical invariant-quadratic terminal line

Verdict: PASS. The actual marked image T_Q, saturated subpencil, terminal incidence, and conditional specific cross-block projection are proved without selecting a coefficient or fifth class.

## Frozen SHA256 hashes

- PROOF.md: 64b8b659df676bbca022d3e3bbfbfd0dba2c2fa2a82a3681d70b737d57d8db7d
- verify.py: 9cbf50f3bcfec82853bf2092732254e922f3b4593c65ca96e4b7dd837d1a462e
- INPUTS.json: c32c2bd3e3b3d69637e8d34e0539e4f05ed2aee2f02885d485fbe8cf9fc609d7
- RESULT.json: 06c04ae0dfff181124a6e3b0e8a711eb47b4fa54eb4c0d3ce3b938d609d925b2

## Authentication and replay

All six full public proofs were freshly fetched at their immutable manifest commits. Returned contents matched retained files byte-for-byte and returned Git blob hashes matched the manifest:

- PR1075: a9d464fd0d4a696e7dc956e6c7af2f3e80a0480e
- PR1068: 5ae07c02624d70c0ccd33d7ec34202504173ff83
- PR1089: 7459702e0b6c28aa6605ca34e2cbd98a9d366417
- PR1094: dd21bc9302ea9ffcd84dddf72ce7a676c326600d
- PR1064: 20b3b58b92d4c44d1097d47a9e952c4dfa25b569
- PR1072: 65dda3e16ded2b79ad84c583f248b09c425e9881

Independent normal and optimized executions passed all39 checks, with byte-identical output equal to RESULT.json. Explicit exceptions preserve the tests under optimization. The two Euler-chart computations are affine-chart identities with a remaining free parameter, not actual direction evaluations.

## Actual-map review

1. The polynomial NC identifications, the embedded I2 and I3, and ker(Q2 restricted to NC2)=I2 are all-branch premises in PR1075. Its old endpoint-nine conclusion is not used. Actual multiplication by the same invariant quadratic supplies Q3(lv)=l Q2(v) with the displayed central parities.
2. Q3 kills the actual I3=W I2. Factoring its restriction through NC3/I3 and using the full actual image im Q3=3T gives an upper bound of one T. This is only an upper bound until the nonvanishing argument is supplied.
3. Q2 injects the marked V_C. If both negative variables killed V_Q, the full joint-negative-kernel theorem would put this nonzero V in NC4=P+D, impossible. Therefore W V_Q is nonzero. Actual commutation embeds this image in Q3(NC3); irreducibility of W tensor V=T and the preceding upper bound prove equality and the coefficient isomorphism. No arbitrary T constituent is identified by character alone.
4. That actual coefficient isomorphism transports the universal tautological inclusion to the restricted arrow. Tensoring the binary Euler sequence by V_Q gives the claimed locally free quotient V_Q O(1), proving saturation and the stated rank and degree. This does not split the full negative pencil.
5. Since NC3 lies in ker j3, ell(T_Q)=Theta(NC3). The actual delta isomorphism NC3 to W tensor NC4 makes Theta(NC3)=X(W tensor h(NC4)). The restriction h takes NC4 into I2, kills I4, and factors through the sole D quotient. It is either zero or onto I2; in the latter case ordinary multiplication onto I3 proves nonzero, hence invertible, ell on T_Q. PR1064 supplies the nonzero case precisely under residual-large hypotheses.
6. If residual tau vanishes, NR5 lies in ker ell whereas T_Q meets that kernel trivially. Thus its e0 projection is injective. If e0 vanished on V_Q, genuine negative stability would put W V_Q=T_Q inside NR5, a contradiction. Equivariance and the unique V in N0,4 then identify e0(V_Q) with that actual constituent. Projector commutation gives e0(T_Q)=W(N0,4)_V and the restriction of ell0 is an isomorphism there.

The proof retains tau as unselected, does not compare it across instances, and makes no assertion that the cross-block condition conversely forces tau zero. It neither assumes Q preserves the negative decomposition nor extends its projector to positive intermediate spaces. No corrected fifth class or positive cyclicity conclusion follows from the terminal line alone, as explicitly stated.

No actual coefficient, point, direction, jet, source matrix or instance rank was evaluated. No public write was performed.
