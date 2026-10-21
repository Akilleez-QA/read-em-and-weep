# Relative cyclic resolutions and the exact comparison ranks

Work over C on P=P(W), with S=Sym(T), and use the actual H module. Write K_w=Ann_S(w), L_w=S/K_w, M=image(S O(-1) -> H O), and B=M-perp. Thus M=(S/K) O(-1), and C=(H O)/M=A O(1). No selected source evaluation or coefficient/rank search enters the argument.

## Pinned inputs

[PR499, commit 1112189481554b0353c64178e3adc0dede2c3fbe](https://github.com/Akilleez-QA/read-em-and-weep/blob/1112189481554b0353c64178e3adc0dede2c3fbe/research/hm/middle-euler-ghost-exclusion/PROOF.md): the pure H resolution, in particular Tor2(H)_4=V(1+U').

[PR500, commit 86d7e1b5d3aee770ea3e7652c950b29bca1aba10](https://github.com/Akilleez-QA/read-em-and-weep/blob/86d7e1b5d3aee770ea3e7652c950b29bca1aba10/research/hm/scalar-last-ghost-exclusion/PROOF.md): I3 has dimension10, its cubic multiplication has kernel dimension10, and I4/(TI3)=V U.

[PR490, commit 1c5ad353bb5f1808150f64cde3c29b92c6e13d91](https://github.com/Akilleez-QA/read-em-and-weep/blob/1c5ad353bb5f1808150f64cde3c29b92c6e13d91/research/hm/dual-tensor-bridge/VERIFICATION.md): the actual trace identification N=Sym²_S H=D5(R), compatible with multiplication.

[PR514, commit d915ed6a7f0c679343447106707692eb7bdee6f7](https://github.com/Akilleez-QA/read-em-and-weep/blob/d915ed6a7f0c679343447106707692eb7bdee6f7/research/hm/cyclic-submodule-duality/PROOF.md): K_w/I=D5(A_w), generated in degree3, and the cyclic/coisotropic exact sequences.

[PR516, commit 89b66cbede7513c4f196fdbda0ee3bb77c53d2e0](https://github.com/Akilleez-QA/read-em-and-weep/blob/89b66cbede7513c4f196fdbda0ee3bb77c53d2e0/research/hm/gorenstein-resolution/PROOF.md): dim Tor1(L_w)_4=5+u-rho and a=5+u-rho-sigma.

[PR524, commit bde039960aafbf3ac8be7921eb48ca4800fbb1fd](https://github.com/Akilleez-QA/read-em-and-weep/blob/bde039960aafbf3ac8be7921eb48ca4800fbb1fd/research/hm/quartic-klein-reduction/PROOF.md): a is5 on the reduced twelve-point orbit Omega and0 elsewhere.

[PR528, commit bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa](https://github.com/Akilleez-QA/read-em-and-weep/blob/bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa/research/hm/middle-family-parity/PROOF.md): relative twists C=A O1 and B=D5(C).

[PR529, commit be7f9aa7d6a469d37d467de65cceb2ba459ad8f1](https://github.com/Akilleez-QA/read-em-and-weep/blob/be7f9aa7d6a469d37d467de65cceb2ba459ad8f1/research/hm/exterior-channel-nonvanishing/PROOF.md): u has the same0/5 pattern; relative Tor2(A)_4 has free part V O8 and torsion supported on Omega. Its free quotient is equivariantly V O8, since the finite binary group is perfect.

For the original Heisenberg and normalizer representations, see Horrocks and Mumford, [A rank 2 vector bundle on P4 with 15,000 symmetries](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf), Section 3.3 and the appendix. The exact family and multiplication identifications used here are those of the pinned proofs above.

Representation conventions: U'=Sym²W, dim U=3, dim W0=2, T A_rep=V(U'+W0). The central involution acts positively on U,U' and negatively on W,W0, while its action on O(d) is (-1)^d.

The actual binary multiplication models in degrees one and two are pinned in [PR494, commit 72ab9a7524aef8c9d1c1fd989f8b0e83826dc916](https://github.com/Akilleez-QA/read-em-and-weep/blob/72ab9a7524aef8c9d1c1fd989f8b0e83826dc916/research/hm/higher-symmetric-powers/PROOF.md); these identify multiplication by the binary generator with ordinary binary multiplication, not merely matching dimensions.

## 1. Moving cyclic annihilator bundles

For d=3,4, dualizing the actual multiplication map R_d O -> H_d O1 by the trace pairing gives

0 -> H_(5-d) O(-1) -> N_(5-d) O -> (K_d/I_d)* -> 0.

For d=3, the map is E times multiplication by the tautological binary linear form:

Sym³W O(-1) -> Sym⁴W O.

Its cokernel is O4, so K3/I3=A_rep O(-4). For d=4, use T times W O(-1)->Sym²W O, whose cokernel is O2; hence K4/I4=V O(-2).

The extensions by constant I3 and I4/(TI3) split equivariantly: the relevant H¹(O4) and H¹(O2) vanish, and one averages a splitting over the finite group. Thus the new part of cubic multiplication, after removing fixed cubic products, is

f: (U'+W0) O(-4) -> U O + O(-2),

with a common irreducible factor V suppressed. Its W0 summand vanishes by central parity. The lower row on U'O(-4) is onto everywhere, because K_w/I=D5(A_w) is generated in degree3 at every fiber. It is the binary quadratic evaluation row, up to nonzero scalar.

## 2. The remaining three-column map is injective everywhere

Away from Omega, relative Tor2(C)_4=V O9. The map from Tor2(H)_4=V(1+U')O to this bundle is zero by central parity. It follows that rho=0 off Omega, and consequently Tor1(L_w)_4 has dimension5 there. Therefore the reduced map f has rank3 generically.

At least one maximal minor involving the lower row is nonzero: a rank-three image with nonzero lower coordinate cannot have all minors involving that coordinate zero. Such minors have degree4+4+2=10. The intrinsic common divisor of all maximal minors is invariant under the binary group. It is bounded by the divisor of any nonzero lower-row minor, so has degree at most10. It is therefore empty because every nonempty projective orbit has at least12 points. Hence f has rank3 at every point.

It follows that f induces a subbundle injection U'O(-4)->UO+O(-2). Its cokernel is a line bundle of degree (-2)-(-12)=10. Restoring V:

Tor1(S/K)_4 = V O10.

The relative cubic linear-syzygy bundle is

10 O + (V W0) O(-4).

Indeed its quotient by the fixed ten-dimensional cubic-syzygy bundle is exactly the killed W0 summand, and the extension splits by H¹(O4)=0.

In particular every cyclic quotient L_w has exactly five minimal quartic generators, including w in Omega. The exact identity 5=5+u-rho proves

rho(w)=u(w),    sigma(w)=5-u(w),

since a=u. Thus rho is0 off Omega and5 on Omega, whereas sigma is5 off Omega and0 on Omega. Rank semicontinuity cannot be applied to the original rho target, which is not a vector bundle across Omega.

## 3. Corollary: the relative elementary modification realizing sigma

The comparison map admits the following elementary-modification description, strengthening the pointwise rank theorem.

Since B=D5(A O1), its degree3 and4 pieces are A_rep O(-3) and V O(-1). The degree4 Koszul differential is therefore

V[(U'+W0)O(-3) -> O(-1)].

The U' row is quadratic evaluation, its kernel is W O(-4), and the W0 row vanishes by parity. Thus

Tor1(B)_4 = V[W O(-4) + W0 O(-3)].

The target Tor1(M)_4 is V O9. Central parity annihilates the W0 O(-3) summand in this comparison map. On the remaining W O(-4), it is a nonzero row of degree13. The exact fiber result above shows that its common zero set is Omega. Its common divisor is invariant and has degree at most13. Since the only possible nonempty invariant divisor of degree at most13 is the reduced orbit Omega of degree12, the common divisor is exactly Omega, with multiplicity one.

Dividing by the invariant degree12 Klein section leaves a basepoint-free degree-one row W O(-4)->O(-3). Hence the actual comparison fits

0 -> V[O(-5)+W0 O(-3)] -> Tor1(B)_4 -> V O(-3) -> 0,

and its image inclusion in Tor1(M)_4 is the elementary modification

0 -> V O(-3) --Klein12--> V O9 -> V O9|Omega -> 0.

Ordinary bundle identities are displayed; any identification of the residue line with a trivially linearized O_Omega is not asserted. The rank-five image degenerates on the twelve simple points because its inclusion into the target vanishes there, while the quotient onto the image bundle remains surjective.

## Scope

These are structural claims about the actual parameter family, conditional on the pinned published inputs. They resolve the two quartic comparison ranks and identify their degeneration without evaluating a selected HM instance. They do not determine the middle obstruction b, the original fixed scalar pair, higher-order lifting, or algebraicity. The argument is authored and subject to independent review, not formally checked.
