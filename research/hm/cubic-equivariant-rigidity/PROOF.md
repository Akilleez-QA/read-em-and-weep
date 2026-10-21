# Abstract Artin rigidity with the Heisenberg action retained

## Inputs and statement

Work over C with the cubic image V=V51 and its fixed projective Heisenberg action U=(Z/5)^2. The action is part of the deformation data; base Artin C-algebras carry the trivial U-action. An equivariant deformation has an identification of its special fiber with V respecting the given U-action.

Pinned dependencies:

- PR610, e4898406ed2552dd40e9695f9fda3d9f1d270301: the 120 normalization marks are the exceptional eigendirections p_ij, i!=j, over the five centers of each of six Heisenberg pentads.
- PR611, 12b28d33627cc0e8b283d142dc16439a51bb5e00: normalization nu:M=Bl_Z(P4)->V and its conductor preimage Omega of 120 reduced marks.
- PR614, 73fbf75838c91804ca637b5916d6aac217240958, research/hm/cubic-global-deformations/PROOF.md: the natural equality Theta_V=nu_*(Theta_M tensor I_Omega), the vanishing H0(Theta_M)=H0(Theta_V)=0, local Artin rigidity, and the canonical exact sequences

    0 -> pgl(A) -> direct-sum_z T_z P4 -> H1(Theta_M) -> 0,
    0 -> direct-sum_p T_p M -> H1(Theta_V) -> H1(Theta_M) -> 0.

  Here p ranges over Omega and z ranges over Z. All these constructions are natural and U-equivariant. It also identifies T1(V)=H1(Theta_V) and gives the local trivializations and overlap-cocycle description for Artin deformations.

Theorem. T1(V)^U=0. Every U-equivariant abstract deformation over a local Artin C-algebra is uniquely equivariantly isomorphic to the constant deformation, with identity special-fiber marking. Consequently the same conclusion holds if the full normalizer Gamma action is retained. This does not assert abstract rigidity after forgetting the action: dim T1(V)=576.

## 1. No invariant normalization deformation

Let g generate one of the six projective directions, and choose its five one-dimensional eigenspaces L_i, with eigenvalues zeta^i, i in F5. The center z_i=P(L_i) is fixed by g. Its tangent space is Hom(L_i,A/L_i), with the four weights k-i for k!=i. None is zero, hence (T_zi P4)^<g>=0.

For any U-invariant element of direct-sum_z T_z P4, its component at z must be fixed by the stabilizer U_z. This stabilizer contains the corresponding direction g, so that component is zero. Every component is therefore zero and

    (direct-sum_z T_z P4)^U=0.

In characteristic zero, invariants for the finite group U are exact by averaging. The first exact sequence above then gives H1(Theta_M)^U=0. No numerical rank computation or source-instance evaluation is involved.

## 2. No invariant motion of the conductor marks

Over z_i, the exceptional divisor is P(T_zi P4). The mark p_ij corresponds to its tangent eigenline in direction L_j, with j!=i. It is fixed by g.

Use the universal blowup chart of the origin in the affine coordinates x_k, k!=i, where g acts with weights k-i. On the chart in direction j set t=x_j and a_k=x_k/x_j for k!=i,j. At p_ij all four coordinates t,a_k vanish. Their tangent weights are

    j-i, and k-j for the three indices k!=i,j.

All four are nonzero modulo five. Thus (T_pij M)^<g>=0. This chart is a universal local blowup calculation in abstract eigenspaces; it does not evaluate any selected source point or derivative.

Every mark in Omega is of this form. As in Section 1, a U-invariant element of the direct sum of mark tangent spaces has a component fixed by the stabilizer at each mark. Since that stabilizer contains g, every component vanishes. Hence

    (direct-sum_p T_p M)^U=0.

Taking U-invariants in the second canonical exact sequence gives

    H1(Theta_V)^U=0,

and thus T1(V)^U=0. In particular T1(V)^Gamma=0 whenever the action is extended to Gamma.

## 3. From invariant tangent vanishing to equivariant Artin rigidity

We spell out the induction so that an invariant tangent statement is not silently upgraded to a higher-order assertion.

Let B'->B be a small extension of local Artin C-algebras, with kernel I annihilated by the maximal ideal of B'. Suppose an equivariant deformation X' over B' is already equivariantly identified over B with V times Spec B. A constant lift exists.

By the local Artin rigidity in PR614, choose local trivializations of X' on affine opens, compatible with this fixed reduction trivialization. Relative to the constant lift, their overlap maps are identity plus derivations with values in I. The resulting Cech one-cocycle defines a class

    c in H1(Theta_V) tensor_C I.

Changing these local trivializations changes the cocycle by a coboundary. Conversely a zero class gives an isomorphism X' to the constant lift inducing the prescribed reduction identification. This is precisely the marked small-extension lift torsor with the constant lift as origin; it applies to these locally trivial deformations without requiring any assertion that global T2(V) vanishes.

The U-action on X', together with equivariance of the chosen reduction identification, makes this class U-invariant. Equivalently, pulling the lift back by any u and comparing through its lifted action leaves its marked isomorphism class unchanged; the constant lift is fixed, so the action on the torsor is the ordinary linear action on H1(Theta_V) tensor I. The base action is trivial, and Section 2 gives c=0.

The resulting isomorphism lifting the prescribed reduction is unique: the difference of two such isomorphisms is an infinitesimal automorphism, belonging to H0(Theta_V) tensor I=0. This uniqueness also proves equivariance. For each u, conjugating the isomorphism by the lifted action on X' and the constant action on V gives another isomorphism with the same reduction; it must be the same one.

Every local Artin C-algebra can be reduced to C by a finite chain of small extensions. Starting with the marked special fiber and applying this argument inductively proves existence and uniqueness of the equivariant constant trivialization. If X' carries Gamma, first obtain the U-equivariant trivialization. For each gamma in Gamma, its conjugate has the same marked reduction; the identical uniqueness argument makes this trivialization Gamma-equivariant as well. Alternatively repeat the induction with Gamma, since its invariant tangent subspace is contained in the zero U-invariant subspace.

## Scope and contribution

The new conclusion is formal abstract rigidity when the specified U-action is retained, despite the 576-dimensional space of deformations without that action. The proof closes the higher-order step by local cocycles and uniqueness, not merely by counting invariant tangent dimensions.

The action is fixed and complex-linear, and the Artin base action is trivial. No claim is made for varying group embeddings without an identified special-fiber action, nontrivial actions on the base, algebraization or convergence, the surface T75, or the original full adjoint system. No selected coefficient, point, derivative, matrix or rank is evaluated; no large computation is used. These are mathematical proofs, not machine-checked formal proofs.
