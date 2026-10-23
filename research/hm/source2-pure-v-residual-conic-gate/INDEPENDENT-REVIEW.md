# Independent review: residual-large conic lift line

Verdict: PASS for the conditional residual-large theorem. The remaining scalar may vanish. Nothing is transferred to the nonzero-N0 mechanism.

## Frozen artifact hashes (SHA256)

- PROOF.md: b162f972d89c1631aed511bd4745935306b3c021237d36a61f8ddcd6e78139f9
- verify.py: e064058e32e293a47d21f8eeb4722e244cc815184b6f704c9056b0b62d9c568d
- INPUTS.json: 09e0b416da52e35938a1248728f52c2bc1760d4d069bea95badc7d70b3e1d4ab
- RESULT.json: 29191e53a00fb72e6f906c56aa1842159bd5cb4b8583fd657bea7ebc3577c086

## Authentication and independent replay

All nine immutable files were freshly fetched at the manifest commits. Their complete contents and returned Git blob hashes matched the retained bytes and manifest:

- PR1079: 3d426673e0793030335604b661d2f8a7cfb299bb
- PR795: 9358ec81c552913fac20f3a92d7b9f7c58105656
- PR1068: 5ae07c02624d70c0ccd33d7ec34202504173ff83
- PR1072: 65dda3e16ded2b79ad84c583f248b09c425e9881
- PR1059: 2b00a40de04a7084ff2f08c767fdd2f4f13ae5f4
- PR1031 proof: 0694e96e2d17a53b68d625ec6065f8bf513cd083
- PR1031 model: a7ca4755e50c85fe7fc20a757125127a05de4056
- PR1094: dd21bc9302ea9ffcd84dddf72ce7a676c326600d
- PR1036: 718f987511b5bf6144a85fc14e8ef343612a4491

Independent normal and optimized executions passed all 36 checks and produced byte-identical output matching RESULT.json. The verifier raises explicit exceptions; optimization does not remove its tests. Its literal Pi, Gram matrices, inclusion, adjoint and R1 definitions were compared against the authenticated PR1031 model without executing that historical file.

A separately written direct-expansion certificate is at verify_independent.py, SHA256 16ba6d676b60fa2d0bc357bbbf3b209fe354c0079ef5bf62b28230b0cb9fa14e. It reconstructs polarization by extracting the degree-two part of f(x+u,y+v), independently of the production binomial matrix implementation. Its six checks pass normally and with -O: relation rank18, C2 rank6, exact annihilation of the relation space, the full cubic-descendant identity, Spencer coefficient -12, and diagonal coefficient360. All coefficients remain formal.

## Actual-map and normalization review

1. PR1072 supplies genuine separated submodules and actual next arrows through degree five, including the cancellation of the determinant rotations. The ambient exact Koszul sequence therefore restricts to the residual summand. PR1068 identifies NC3 to W tensor NC4 as an actual isomorphism, with terminal image zero. Quotienting this acyclic subcomplex gives the exact residual quotient sequence in Section2. This does not require a horizontal NC/N8 splitting.
2. In the inherited variables, ordinary binary Koszul multiplication converts that sequence into the stated quotient of A tensor Sym7 by W Delta_(2,6)(Sym8). The map C2 has that entire relation space as its kernel, not merely an isomorphic character. Thus its cubic-descendant formula computes the actual residual terminal map, up to the permitted single target normalization.
3. The residual-large hypothesis makes pi2 s nonzero. The unique P in A tensor Sym4 lies in its top Sym6 constituent, so comparison with the authenticated orthogonal P inclusion yields one nonzero scalar eta. This uses the existing actual projection and multiplicity one, not an identification of arbitrary repeated P copies. The restriction of ell to the actual NR5 may be zero; its scalar tau remains unselected.
4. The identity C2(c Delta_(2,4)f)=(c,f)_2 and PR1094's exact Spencer comparison give D(U_p)=eta tau(c,f_p)_2. The proposed inverse is equivariant. The full Spencer kernel consists only of scalar endomorphisms, and Hom_G(P,1)=0 eliminates any residual scalar-identity family.
5. The signs and constants agree with the inherited conventions: D((q,f)_3)=-12(c,f)_2; the invariant bilinear adjoint is (a,f)_2/60; and (a squared,f)_3=360 rho_D(a)L_a*. The resulting coefficient is -30 eta tau. A coherent overall scalar change cannot introduce the independent R2 channel.
6. PR1031's independence of R1 and R2 and PR1036's conic-line identification therefore give beta=0, with R either zero or on span(R1). The proof does not infer eta tau nonzero from eta nonzero, and does not use the excluded endpoint-nine mechanism to constrain this residual-large mechanism.

No selected source coefficient, negative direction, point, jet, actual matrix or instance rank was evaluated. No public write was performed. The novel conclusion is the residual-large line constraint; imported terminal multiplication, Spencer isomorphism and universal basis results remain explicitly attributed.
