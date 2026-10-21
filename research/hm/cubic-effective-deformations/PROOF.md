# Effective projective deformations over the formal DVR

Work over C. Put A=C[[t]], A_n=A/(t^(n+1)), and V=V51. An abstract formal deformation here means a compatible cartesian system of flat finite-presentation schemes X_n/A_n, with X_0 identified with V. Automorphisms fix the base, not just its closed point.

## Pinned inputs

- [PR611](https://github.com/Akilleez-QA/read-em-and-weep/pull/611), commit 12b28d33627cc0e8b283d142dc16439a51bb5e00, research/hm/cubic-branch-transversality/PROOF.md: V is projective, L_0=O_V(1) is ample, and H2(V,O_V)=0; indeed h^i(O_V)=(1,60,0,0,0).
- [PR614](https://github.com/Akilleez-QA/read-em-and-weep/pull/614), commit 73fbf75838c91804ca637b5916d6aac217240958, research/hm/cubic-global-deformations/PROOF.md: abstract Artin lifts exist compatibly across small extensions, T1(V) has dimension 576, and H0(Theta_V)=0.
- [PR627](https://github.com/Akilleez-QA/read-em-and-weep/pull/627), commit 7c3f76f2e55c5cc0c3356972b5d7d676544c943a, research/hm/cubic-formal-symmetry-breaking/PROOF.md: a nonempty open T_free in T1(V) exists, and every v in it admits such a compatible system with first-order class v and Aut_(A_n)(X_n)={1} for every n>=1.

## 1. Every abstract formal deformation is effective

Theorem. Every system X_n as above is the completion of a flat projective finitely presented scheme X over Spec A. Moreover one may choose an ample invertible sheaf L on X restricting to L_0 on V, and compatible identifications of all reductions with the prescribed system.

For each n, X_n is proper over A_n: properness is invariant under nilpotent thickenings of finite-type morphisms, applied to X_0 -> X_n over Spec C -> Spec A_n. Finite presentation is already part of the deformation hypothesis. See [Stacks, morphisms of thickenings](https://stacks.math.columbia.edu/tag/0CF2).

Suppose L_n has been chosen. The ideal J_n of X_n in X_(n+1) is square-zero and, by flatness over A_(n+1), is O_V tensor_C (t^(n+1)A/t^(n+2)A); in particular it is O_V as an additive sheaf. On the common underlying topological space the exact sequence

    1 -> 1+J_n -> O_(X_(n+1))^* -> O_(X_n)^* -> 1

identifies 1+J_n with the additive sheaf J_n. Thus the obstruction to lifting L_n lies in H2(V,O_V), which vanishes. Choose L_(n+1) and a reduction isomorphism to L_n. Starting with L_0 and iterating gives a compatible system of invertible sheaves. No uniqueness is asserted: H1(O_V) is nonzero. The obstruction sequence is [Stacks, Picard groups of thickenings](https://stacks.math.columbia.edu/tag/0C6Q).

Apply [Stacks, strong formal effectiveness for polarized schemes, Lemma 99.14.11](https://stacks.math.columbia.edu/tag/0D4T), shifting its indices by one, with rings A_n. Its hypotheses are exactly compatible cartesian reductions, proper flat finite-presentation X_n, and an ample first sheaf L_0. Since lim A_n=A, it supplies X/A proper, flat, finitely presented and an ample L with compatible identifications of X_n and L_n. Properness and an ample invertible sheaf over the affine Noetherian base imply projectivity: a sufficiently high power defines an immersion into projective space, which is closed because X is proper. This proves the theorem. The Noetherian version [Stacks 089A](https://stacks.math.columbia.edu/tag/089A) also algebraizes the polarized system; 0D4T records flatness directly.

## 2. Audit: why one high power works at all Artin orders

The effectivity theorem does not require lifting the ten sections of L_0. To make the distinction explicit, choose one m with L_0^m very ample and H1(V,L_0^m)=0 by [Serre vanishing, Stacks 0B5T](https://stacks.math.columbia.edu/tag/0B5T). Set r=h0(V,L_0^m). For all n>=0, flatness gives

    0 -> L_0^m -> L_(n+1)^m -> L_n^m -> 0.

Induction yields H1(X_n,L_n^m)=0 and surjectivity of all transition maps on H0. Choose lifts at each order of a compatible basis, beginning with a basis of H0(V,L_0^m). These r sections generate L_n^m: the evaluation cokernel is zero modulo t, hence zero by nilpotence and Nakayama. They define f_n:X_n -> P^(r-1)_(A_n), compatibly in n.

Each f_n is a closed immersion. It is proper, since X_n is proper over A_n and the target is separated. The underlying spaces of source and target are their special-fiber spaces, so f_n is quasi-finite since f_0 is a closed immersion. Thus f_n is finite; see [Stacks 02OF](https://stacks.math.columbia.edu/tag/02OF). On affine target opens the cokernel of O_target -> (f_n)_*O_(X_n) reduces to zero modulo t, because finite pushforward commutes with base change and f_0 is a closed immersion. Nilpotence kills that cokernel. Therefore f_n is a finite closed immersion.

For completeness, the lifted r sections are a basis of H0(X_n,L_n^m). Their span is all of H0 by induction: subtract a lifted expression for a section on X_(n-1); the remainder is in the image of H0(L_0^m), which consists of t^n times the chosen sections. The displayed exact sequences give dim_C H0(X_n,L_n^m)=(n+1)r. The resulting surjection A_n^r -> H0 has equal finite C-dimensions and is an isomorphism. Consequently the construction gives one fixed projective ambient dimension for the entire system, not dimensions growing with n. No original-degree section-lifting claim is being used.

## 3. Formal faithfulness and symmetry-breaking effectivity

Lemma. If X is proper over A and Y is separated of finite type over A, two A-morphisms f,g:X -> Y agreeing on every X x_A A_n are equal.

The equalizer is a closed subscheme of the Noetherian scheme X; let I be its coherent ideal. Agreement modulo every t^(n+1) means I is contained in t^(n+1)O_X for every n. At any point x of the special fiber, t lies in the maximal ideal of O_(X,x), so [Krull intersection, Stacks 00IP](https://stacks.math.columbia.edu/tag/00IP) gives I_x=0. The closed support of I is therefore disjoint from the special fiber. It is proper over Spec A, so its image is closed. Every nonempty closed subset of Spec A contains the closed point. The support is empty, I=0, and f=g.

Apply this with Y=X. It proves injection

    Aut_A(X) -> lim_n Aut_(A_n)(X_n).

For every v in T_free, algebraize a PR627 system using Section 1. Its positive-order automorphism groups are trivial, hence Aut_A(X)={1}. The family is nonconstant as a marked deformation, since its first-order class v is nonzero. Thus PR627's symmetry-breaking formal systems are actual projective flat families over the formal DVR, with no nonidentity automorphism over that DVR.

## 4. Scope

This closes the effectivity dependency for compatible abstract one-parameter deformations of V, including the full-group symmetry-breaking systems. It does not assert that a chosen power-series family converges analytically, descends to a curve of finite type over C, or retains the original cubic embedding or HM presentation. In particular a high-power embedding is different from lifting all original degree-one sections.

Triviality is for Aut_(C[[t]])(X), not Aut_(C((t)))(X_generic) or its geometric counterpart: a generic-fiber automorphism need not extend to this model, and no extension theorem is claimed. This result also does not settle the original prescribed-source/full-adjoint/higher-lifting/Weil-class algebraicity questions. The scheme over C[[t]] is an algebraic scheme over that ring, not a finite-type C-family or an algebraic cycle solving those separate questions.

No selected source coefficients, points, derivatives, matrices, ranks, or large computations are used. This is a mathematical argument conditional on the pinned inputs, not proof-assistant formalization.
