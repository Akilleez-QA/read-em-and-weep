# Formal abstract deformations breaking every special-fiber automorphism

Work over C and let V=V51 be the cubic image. All deformations have identified special fiber V; all automorphisms in this note are over the fixed base, not over a reparametrization. Put T=T1(V).

## Pinned dependencies

- [PR614](https://github.com/Akilleez-QA/read-em-and-weep/pull/614), commit 73fbf75838c91804ca637b5916d6aac217240958, research/hm/cubic-global-deformations/PROOF.md: T=H1(Theta_V), H0(Theta_V)=0, and existence of abstract lifts over every small extension of local Artin C-algebras. The affine-gluing proof supplies compatible reduction identifications, not just tangent unobstructedness.
- [PR617](https://github.com/Akilleez-QA/read-em-and-weep/pull/617), commit 7f240b04bc4f03cfe73ffd64cae17c453dd895e6, research/hm/cubic-scalar-constraints/PROOF.md, Section 6: U=(Z/5)^2 is normal in Gamma, Gamma/U=SL2(F5), |Gamma|=3000, and the centralizer of U in PGL5 is precisely U.
- [PR624](https://github.com/Akilleez-QA/read-em-and-weep/pull/624), commit 4fc9f009922b51369bfcaf4953919cb2f4c6c334, research/hm/cubic-unpolarized-automorphisms/PROOF.md: the full complex algebraic automorphism group Aut(V) is this Gamma, not merely its polarized subgroup.
- [PR626](https://github.com/Akilleez-QA/read-em-and-weep/pull/626), commit 8c25863b2c17de5c652fc2ced74163c0a6364a0a, research/hm/cubic-symmetry-deformation-strata/PROOF.md: T restricted to U equals 24 Reg0(U), where Reg0(U) is the direct sum of all 24 nontrivial characters. Its Sections 3-4 establish naturality of marked-lift torsors and relative automorphisms H0(Theta_V) tensor I across a small extension with kernel I.

These inputs concern abstract deformations, not the embedded Hilbert functor.

## 1. Faithfulness of the full automorphism action

Changing the special-fiber marking defines the natural Gamma-action on the abstract deformation functor and hence a linear representation rho:Gamma -> GL(T). We choose the marking convention giving a left action; the fixed-class condition for an automorphism is independent of this convention.

The restriction to U is faithful: a nonidentity u in U is detected by a nontrivial complex character, and every such character occurs in T. Let K=ker(rho). Then K is normal in Gamma and K intersection U={1}. For k in K and u in U, the commutator [k,u] belongs to K by normality of K and belongs to U by normality of U. Consequently it is identity. Thus K centralizes U. The centralizer identity from PR617 gives K subset U, and therefore K={1}.

In particular every nonidentity gamma in Gamma has a proper fixed linear subspace T^gamma. Since C is infinite and Gamma is finite, the complement

    T_free = T minus union_{1 != gamma in Gamma} T^gamma

is a nonempty Zariski-open subset of the 576-dimensional vector space T. Every class in T_free has trivial Gamma-stabilizer. No selected class or source-instance evaluation is needed for this existence assertion.

## 2. Exact codimension of the first-order symmetry locus

Let B=T minus T_free. Then B has codimension exactly 288 in T.

For nonidentity u in U, the characters trivial on u are the five characters of U/<u>, of which four are nontrivial. Thus dim T^u=4*24=96 and its codimension is 480.

For gamma outside U, let A be its nonidentity image in SL2(F5), acting on the character group of U by the dual action. The 24 nontrivial character spaces T_chi each have dimension 24; gamma permutes them according to A. On any orbit of length l, a fixed vector is determined by its component in one character space, so the fixed space has dimension at most 24 and the codimension contributed by this orbit is at least 24(l-1). This statement does not assume that gamma has order l, or that its maps around the cycle multiply to identity.

If A has no fixed nonzero character, all orbits have length at least two, so there are at most 12 orbits and dim T^gamma<=288. If A has a fixed nonzero character, its determinant one and dimension two imply that both eigenvalues are one. Since A is not identity, A=1+N with N nonzero, N^2=0; in characteristic five its order is five. Its fixed space is a one-dimensional F5-line, containing exactly four nonzero characters; the remaining twenty characters form four orbits of length five. Even allowing all four fixed character spaces to contribute their full dimensions, dim T^gamma<=24*(4+4)=192. Thus every nonidentity element of Gamma has fixed-space codimension at least 288.

For equality, use the universal Heisenberg realization on the five-dimensional space with basis e_i, i in F5. The linear involution J(e_i)=e_(-i) conjugates both the shift and phase generators to their inverses. Its projective class belongs to the full normalizer Gamma and induces -Id on U, and J^2=1. Its action on T therefore exchanges the 24 nontrivial character spaces in 12 pairs, with the two maps in each pair mutually inverse. The fixed vectors on each pair form a 24-dimensional graph. Hence dim T^J=12*24=288 exactly. This uses the universal representation, not selected source coordinates or evaluations.

A finite union of linear subspaces has dimension the maximum of their dimensions. The bounds and this involution prove dim B=288, or codim B=288, as claimed. This strengthens the existence of symmetry-breaking directions by quantifying their exceptional complement.

## 3. Compatible formal deformations with no automorphisms

Theorem. For every v in T_free, there exists a compatible system of flat abstract deformations X_n over A_n=C[t]/(t^(n+1)), n>=0, with X_0=V and first-order class [X_1]=v. For every n>=1,

    Aut_{A_n}(X_n) = {1}.

In particular the group of compatible automorphisms of this formal deformation system over the fixed base C[[t]] is trivial. Every nonidentity automorphism of V already fails to lift to X_1.

Proof. First choose X_1 representing v, with the chosen identification of its special fiber with V. Given X_n, the map A_(n+1) -> A_n is a small extension with kernel generated by t^(n+1), annihilated by the maximal ideal. Abstract unobstructedness supplies X_(n+1) with an identification of its reduction with X_n. Recursion gives the stated compatible system. This construction is a formal deformation system; no effectiveness or algebraization assertion is needed.

Let a be an A_n-automorphism of X_n for n>=1, and let gamma be its restriction to the identified special fiber. By PR624, gamma belongs to Gamma. Reducing a modulo t^2 gives an automorphism of X_1 inducing gamma. The natural marking action therefore fixes its deformation class v: an extension of gamma identifies the corresponding re-marked first-order deformation with the original one. Since v belongs to T_free, gamma=1.

It remains to exclude automorphisms inducing identity on V. Induct on n. The kernel of reduction of automorphisms across A_n -> A_(n-1) consists of global derivations into the square-zero ideal t^n O_(X_n). Flatness and maximal-ideal annihilation identify this ideal with O_V tensor_C (t^n), so that kernel is H0(V,Theta_V) tensor_C (t^n)=0. For n=1 the reduction is identity on V, hence a is identity. For n>1 its reduction is identity by induction, and the same zero kernel finishes the proof. This argument does not assert that arbitrary automorphisms lift; only the kernel of reduction is used.

The zero tangent vector is fixed by Gamma, hence is not in T_free. Thus these systems are nonconstant already to first order. This proves the theorem.

## 4. Contribution and limitations

PR626 constructs deformations retaining specified cyclic symmetries. The new step shows that the full 3000-element automorphism group acts faithfully on the abstract tangent space and constructs formal directions retaining no nonidentity special-fiber automorphism whatsoever, with rigidity of all relative automorphisms at every positive Artin order. The complete finite group, including elements outside U, is excluded by the normal-kernel/centralizer argument rather than by checking selected elements or coordinates.

This is an abstract fixed-base formal result. It makes no assertion about convergence, algebraization, an effective family, generic-fiber automorphism groups, base-changing automorphisms, or preservation of the cubic/HM presentation. It does not close the original selected-source, full-adjoint, higher-lifting, or Weil-class algebraicity problems. No selected coefficients, points, derivatives, matrices, ranks, or large computations enter the proof.

The argument is a mathematical proof dependent on the pinned inputs. It is not a proof-assistant formalization.
