# Smooth Hilbert germ and formal projective rigidity of the cubic image

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected HM/source evaluation or computation is used.

## 1. Inputs and scope

Let V=V_51 subset P9 be the integral canonical cubic image of M=Bl_Z P4 under its complete ten-dimensional cubic system S. The projective embedding is nondegenerate because S is the full defining section space.

Dependencies in Akilleez-QA/read-em-and-weep:

- PR611 at 12b28d33627cc0e8b283d142dc16439a51bb5e00: V is the finite birational image of M, with the specified two-branch singularities; its Hilbert polynomial is P_V(n)=binom(3n+4,4)-30 binom(n+3,4)-60.
- PR614 at 73fbf75838c91804ca637b5916d6aac217240958: H0(V,Theta_V)=0; abstract deformation tangent has dimension576 and is formally unobstructed.
- PR615 at 24bc9b741c287f8ac207bd9df4de4c07c50bea2f identifies the embedded Hilbert tangent with the normal-sheaf tangent and gives dimension99+dim ker b.
- The independently reviewed structural descent nonvanishing proof at repository commit c48c8ce745396028965f9bb64454a22e351b2b36, path research/hm/cubic-descent-nonvanishing/PROOF.md, SHA256 70c2d77d9ba9e1b66c4d0b6dcf2258f8f2aedb84c7fd296b524667ff45abb719, proves ker b=0, hence embedded tangent dimension99.

We prove that the Hilbert scheme Hilb^(P_V)(P9) is smooth of dimension99 at [V], the PGL10 orbit is open around [V], and every embedded deformation over a local Artinian C-algebra is obtained by a unique projective coordinate change reducing to the identity. This is an all-orders embedded statement obtained from the Hilbert scheme, not an inference that vanishing of a first-order vector space alone always controls an unrelated deformation functor.

It does not contradict the576-dimensional abstract deformation space: those abstract deformations do not in general retain this line bundle with this complete embedding.

## 2. The infinitesimal projective stabilizer is zero

Let G=PGL10. Its orbit map at V is

    a:G -> Hilb^(P_V)(P9),       g -> g(V).

An infinitesimal stabilizer vector restricts to a global derivation of O_V, hence to an element of H0(Theta_V). This element is zero by PR614. We must also exclude an ambient projective vector field vanishing identically along V; zero intrinsic vector fields alone would not suffice for an arbitrary degenerate subscheme.

Represent such an ambient vector field by an endomorphism A of the ten-dimensional coordinate vector space, modulo scalars. Its value at [v] is the class of Av modulo Cv. Consequently its zero locus consists of projective eigenvectors of A, a finite union of projectivized eigenspaces. This remains true if A is not diagonalizable; generalized eigenvectors outside the eigenspaces do not give zero values.

The integral V is irreducible. If the field vanishes on V, its support is contained in one eigenspace's projectivization. Since V is nondegenerate, that eigenspace must be the entire vector space. Thus A is scalar, and the projective vector field is zero.

It follows that Lie Stab_G(V)=0 and the differential da_e is injective. Since dim G=99 and dim T_[V] Hilb=99, it is an isomorphism.

## 3. The Hilbert local ring is regular

The scheme-theoretic stabilizer is a finite-type closed subgroup of G. Its tangent space at the identity is zero, so its local dimension there is zero. Translation gives dimension zero everywhere. The orbit has dimension dim G-dim Stab=99 and is locally closed. These usual orbit facts apply to an algebraic group acting on a finite-type scheme; equivalently they follow from constructibility of the orbit map and its fibers, which are stabilizer cosets. The orbit has its reduced smooth structure over C.

The closure of this99-dimensional locally closed orbit passes through [V], so the local dimension of the Hilbert scheme there is at least99. It is at most its tangent dimension99. Hence

    dim O_(Hilb,[V]) = dim m/m^2 =99.

The local ring is Noetherian, so this equality is precisely regularity. Since the Hilbert scheme is of finite type over the algebraically closed field C, it is smooth at [V]. In particular its local ring is reduced and has a unique local irreducible component.

For reference, the regular-local-ring criterion is in Stacks Project, Section10.60, https://stacks.math.columbia.edu/tag/00KD. Regularity at a closed point is equivalent to smoothness for a finite-type algebra over an algebraically closed field by Lemma10.140.2, https://stacks.math.columbia.edu/tag/00TQ. No unproved vanishing of an obstruction group is substituted for this local dimension argument.

## 4. Open orbit and the Artinian lifting statement

Shrink to a smooth neighborhood of [V] in the Hilbert scheme. Both G near its identity and this neighborhood are smooth of dimension99, and da_e is an isomorphism. The Jacobian criterion for a morphism between smooth varieties of equal dimension makes the orbit map etale at the identity. After restricting to a suitable neighborhood of the identity it is etale, and its image is open. That image consists entirely of projective translates of V, proving that the orbit is open around [V].

For a local Artinian C-algebra R with residue field C, an embedded flat deformation V_R subset P9_R with special fiber V is an R-point of the Hilbert scheme reducing to [V]. An etale morphism is formally etale: given the special-fiber lift e in G, it has a unique lift over each square-zero extension. Induction through a nilpotent filtration of R therefore gives a unique g_R in PGL10(R), reducing to the identity, with

    V_R = g_R(V times Spec R).

The chosen neighborhood imposes no extra restriction on these infinitesimal lifts, since Spec R has only its closed point topologically. The lifting fact is the finite-presentation equivalence of etale and formally etale maps, Stacks Project Lemma10.150.3, https://stacks.math.columbia.edu/tag/00UP.

Equivalently the orbit map identifies completed local rings at e and [V]. The Hilbert completion is a formal power-series ring in99 variables, with these variables supplied by projective-coordinate motion. There are no non-projective formal embedded deformation parameters. This does not assert that the global orbit is closed or that all schemes with this Hilbert polynomial are projectively equivalent.

## 5. Boundaries

The conclusion concerns embedded deformations in P9 with the stated Hilbert polynomial. It gives no rigidity for all abstract deformations, for the original primary degree15 surface, for the associated degree75 surface, or for null's full-adjoint problem. It also does not identify a prescribed original source or prove the original algebraicity goal. Those objects and deformation problems remain distinct.
