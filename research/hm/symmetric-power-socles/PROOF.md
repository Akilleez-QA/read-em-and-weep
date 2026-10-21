# Exact socles of the higher symmetric powers

Work over C. Let S=Sym(T), dim T=5, m=S_+, and H_j=H²(End_0(F)(j−5)). Put W=H_0=W′, E=A*, and M_p=Sym^p_S(H). Polynomial degree and symmetric-power degree p are distinct. All symmetric powers are ordinary module symmetric powers, not super-symmetric powers or deformation obstruction groups.

PR494 gives the complete Hilbert functions, the degree-two multiplication model, and the last nonzero representations:

- (M_p)_0=Sym^p W, (M_p)_1=T⊗Sym^p W;
- (M_p)_2=E⊗Sym^(p+2)W, with scalar multiplication induced by S_2=E⊗Sym²W and ordinary binary multiplication;
- (M_3)_3=(E⊗W)*=A⊗W, (M_4)_3=E*=A;
- M_3 and M_4 vanish above degree three, and M_p vanishes above degree two for p≥5.

We prove their entire socles:

Soc(M_3)=(M_3)_3=A⊗W, dimension ten;

Soc(M_4)_2=E⊗T_4, dimension twenty, and Soc(M_4)_3=A, dimension five;

Soc(M_p)=(M_p)_2=E⊗Sym^(p+2)W, dimension 5(p+3), for p≥5.

There are no socle components in any unlisted degrees. Thus M_3 is level of degree three and type ten, M_4 is not level and has type twenty-five, and every M_p with p≥5 is level of degree two and type 5(p+3).

## 1. A common-radical exclusion

Let Γ be the finite Heisenberg subgroup. It acts irreducibly on T and acts trivially on W. For any nonzero covector λ∈W*, evaluating the binary quadratic factor gives a nonzero Γ-equivariant linear map

π_λ:S_2=E⊗Sym²W→E.

It is nonzero because evaluation on Sym²W at a nonzero covector is nonzero. Define the symmetric bilinear map B_λ:T×T→E by B_λ(t,v)=π_λ(tv). Products tv span S_2, so B_λ is nonzero.

Its common radical K_λ={v∈T : B_λ(t,v)=0 for every t∈T} is Γ-stable. Indeed, equivariance transforms B_λ(t,gv) into gB_λ(g^(-1)t,v). Irreducibility of T makes K_λ either zero or all of T. The latter would make B_λ zero, which was excluded. Therefore K_λ=0 for every nonzero λ.

This is a universal invariant-subspace argument for the entire binary family. It does not select or evaluate any polynomial coefficients of an HM instance, or calculate a numerical matrix rank.

## 2. No socle in degrees zero or one

The first multiplication T⊗(M_p)_0→(M_p)_1 is an isomorphism, so no nonzero degree-zero element is killed by m.

Let z∈(M_p)_1=T⊗Sym^pW be killed by every t∈T. Evaluate its binary factor at λ and write v_λ=(id_T⊗ev_λ)(z)∈T. Under the degree-two multiplication model, evaluation of t z at λ equals B_λ(t,v_λ). Thus v_λ lies in K_λ and is zero for every nonzero λ. A vector-valued homogeneous binary polynomial vanishing at every covector is zero, so z=0. Hence Soc(M_p)_1=0 for every p≥1.

For p≥5, the degree-two support cutoff now proves the asserted levelness and complete socle, since every element in the final degree is killed by m.

## 3. The cubic and quartic symmetric powers

Use quotient-normalizer notation U=Sym²W_0 and U′=Sym²W′ for the two three-dimensional representations, Qspin for the spin four-dimensional representation, T_4=W_0⊗W′ for the ordinary four-dimensional representation, J_5 for the five-dimensional representation, and R_6 for the six-dimensional one. Here W_0 denotes the other two-dimensional representation, so it is not confused with the generator space W=W′.

The binary character identities are

Sym⁴W′=J_5, Sym⁵W′=R_6, Sym⁶W′=U⊕T_4.

They follow from the standard two-dimensional Clebsch–Gordan recursion and the character-table products W′⊗J_5=Qspin⊕R_6 and W′⊗R_6=U⊕T_4⊕J_5. The latter is the W_0↔W′, U↔U′ Galois conjugate of the identity already used in PR478. The normalizer tensor identity dual to T⊗A*=A⊗(U⊕W′) is

V⊗A=E⊗(U⊕W′), where V=T*.

The degree-two socle is the kernel of the equivariant joint multiplication map

δ_p:(M_p)_2→Hom(T,(M_p)_3).

For p=3, its source E⊗R_6 is irreducible. The map is nonzero: M_3 is generated in degree zero and its degree-three component is nonzero, so multiplication from degree two onto degree three cannot vanish. Its invariant kernel is therefore zero.

For p=4, the source is E⊗(U⊕T_4), while the target is V⊗A=E⊗(U⊕W′). The irreducible E⊗T_4 summand is absent in the target, so it lies in the kernel. The total map is again nonzero by generation and the nonzero last component. Its only possible remaining source is E⊗U, which is irreducible; the restriction there is consequently injective. Thus the kernel is precisely E⊗T_4. Together with the absence of lower socles and the support cutoff, this proves the stated complete socles of M_3 and M_4.

The argument uses equivariance of the joint multiplication map and invariance of its kernel. It does not assume an arbitrary individual scalar multiplication is equivariant, nor infer nonzero maps merely from matching representations.

## 4. Terminal free-resolution modules

For a finite-length graded module over the five-variable polynomial ring S, the last Koszul homology is its socle tensored with Λ⁵T. The determinant character is trivial here. Therefore the fifth free modules in minimal graded resolutions are exactly

F_5(M_3)=10S(−8),

F_5(M_4)=20S(−7)⊕5S(−8),

F_5(M_p)=5(p+3)S(−7) for p≥5.

Equivalently, reversing graded duality at the respective top degree, the dual of M_3 is generated only in degree zero by ten generators, the dual of M_4 has five generators in degree zero and twenty in degree one, and the reversed dual of M_p for p≥5 is generated only in degree zero by 5(p+3) generators. These are new constraints on the actual minimal resolutions, beyond their Hilbert functions and annihilators. They do not select the remaining parameters of H or R.

## 5. Forced penultimate upper Betti entries

The socles also determine the upper corner of the penultimate free module. Write β_(i,j) for the number of S(−j) summands in F_i. A finite-length module supported through degree d has regularity d, so β_(i,j)=0 when j>i+d. Consequently the coefficient of t^(d+4) in (1−t)^5 Hilb(M_p,t) is β_(4,d+4)−β_(5,d+4): no lower homological term can occur there.

For p≥5 the Hilbert function is (p+1,5(p+1),5(p+3)), with d=2. The coefficient of t⁶ is

−5(p+1)+5·5(p+3)=20p+70.

The level socle gives β_(5,6)=0. Therefore β_(4,6)=20p+70, in addition to β_(5,7)=5(p+3).

For p=3 the Hilbert function is (4,20,30,10), with d=3. The coefficient of t⁷ is −30+5·10=20. The level socle gives β_(5,7)=0, hence β_(4,7)=20, in addition to β_(5,8)=10.

For p=4 the Hilbert function is (5,25,35,5), again with d=3. The coefficient of t⁷ is −35+5·5=−10. Here β_(5,7)=20, so β_(4,7)=10, in addition to β_(5,8)=5.

Only these upper-corner entries and the entire last free module are claimed. The calculation does not determine the full minimal resolutions or choose any unresolved H or R parameter.

## Dependencies and scope

- PR494 at 72ab9a7524aef8c9d1c1fd989f8b0e83826dc916, symmetric-power Hilbert functions and multiplication model: https://github.com/Akilleez-QA/read-em-and-weep/blob/72ab9a7524aef8c9d1c1fd989f8b0e83826dc916/research/hm/higher-symmetric-powers/PROOF.md
- PR478 at 142b0b52f4ad0ddea526ae044774e4f1dd599aef, normalizer tensor identities: https://github.com/Akilleez-QA/read-em-and-weep/blob/142b0b52f4ad0ddea526ae044774e4f1dd599aef/research/hm/cubic-ghost-exclusion/PROOF.md
- PR479 at b57cf851bb244706acfe6c6485d4dfa54ceb6519, T⊗A* identity: https://github.com/Akilleez-QA/read-em-and-weep/blob/b57cf851bb244706acfe6c6485d4dfa54ceb6519/research/hm/quadratic-shadow-exclusion/PROOF.md
- Horrocks–Mumford, Lemma 2.2 and Appendix character table: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Authored structural derivation with independent and root mathematical reviews, conditional on these inputs. Not formally proof-assistant checked. No selected actual HM/source-instance evaluation, numerical multiplication matrix or rank computation, coefficient search or large computation was performed. Original fixed-pair/source values, higher-order lifting and algebraicity remain unresolved and distinct from module symmetric powers.
