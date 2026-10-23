# Independent review: pure-V square restriction and transverse fourth space

The entire final proof and checker were reviewed. No mathematical blocker found. All conclusions remain conditional on the authenticated pure-V source2 branch; no actual coefficient, direction or instance rank was evaluated.

## Frozen bytes and replay

- PROOF.md: 733af12ac58149699a3124afae532d143c82f69b0fcbc26810193880c3d6b6e0
- verify.py: 31513cc77f17fc94e90dc5ae4a614cdb1e806efce0b574fc8e1bd4ec9912fcff
- INPUTS.json: 10ee0a83e599a20bd8867c7008f7b3aa93c636f264db34d27e8c911e9b1f1b3b
- RESULT.json: 59618411b763dc9f8f377e99741d7a2142db4c0db7cb97fb7651085a388a76b9

Independent normal and optimized executions both passed29 checks with identical stdout. All four stored dependency SHA256 and Git blob identifiers passed. Independently fetched exact public files at the manifest commits: PR1025 blob d036adcf5bc2bfc53e07cd752ff180c5993251f7; PR966 blob6197582777ccd6f8899ff16e16d335315fd52a99; PR1000 blob0ca1301de04a630cb184c4429f5b59e09698c6c9; old-fourth blobfd33060d7ce479f9c21bc7e1b47c471cfdebec50. Each agrees with the retained copy.

## Mathematical checks

1. The sequence 0→J(1)→J(3)→O_Delta(9)→0 is exact. Disjointness of Z from the conic identifies the restriction with the indicated line bundle, and multiplication by the discriminant is injective on the torsion-free ideal sheaf. The plane twist9 pulls back to binary degree18.
2. The inherited resolution gives H0(J(1))=D and H1(J(1))=A, not zero; equivariant Serre duality introduces no nontrivial determinant character. H1(J(3)) vanishes. Hence the full-section restriction really has kernelD and cokernelA. This important non-surjectivity is retained in the proof.
3. Exactness of Hom_G(P,-) kills both end terms, proving the P-multiplicity restriction is an isomorphism of two-dimensional spaces. The independent exact character calculation confirms Sym18W=A+V+2P+D and the whole-section Euler dimensions5−21+19−3=0.
4. PR1025 supplies the actual canonical inclusion J→cokerB and the corrected original-fourth comparison. Its quotient is cokerL, supported away from Delta. Consequently the inclusion is an isomorphism near Delta; PR966 makes L surjective there. These are actual sheaf facts, not inferred from dimensions.
5. The composition D(-4)→P(-3)→J→cokerB has the correct fourth degree and target. Its restriction vanishes exactly when s restricts to zero. Thus res∘T is injective, and dimension2 of both source and old restriction target proves it is an isomorphism. The resulting image is a complement to the old discriminant-divisible two-dimensional kernel.
6. The claimed canonical qualification is precise: the complement is inherited from the fixed geometric maps; scalar rescaling of T leaves both its image and T(res∘T)^(-1) unchanged. The proof correctly does not identify this with an arbitrary old coordinate splitting or force individual old invisible coordinates to vanish.
7. The final vanishing equivalence concerns the entire surviving-D family and the entire discriminant restriction, not one square point or the extra specialized A-kernel. The distinct old lifting correction also named L is explicitly distinguished.
8. The two cited old detection notes describe the unrestricted four-channel space, not this pure-V transverse subspace. No duplicate of the claimed complement was found there. Old scheme, rank and character facts remain identified as inputs rather than reclaimed results.

The checker supplements the sheaf and naturality proof; it is not proof-assistant verification and does not decide either coefficient of the actual gate.
