# A local dihedral counterconfiguration for the coefficient-independence inference

## Result and exact scope

The order-three normalizer D=Dic_3, its weight/parity restrictions, the displayed source and target multiplicities, the cyclic/outer-symmetry identities, and nonzero coefficient maps on both S_4 and R_6 do **not** imply h wedge C_tilde wedge D_tilde is nonzero. This remains false even when the symmetric-T map g is an isomorphism and the alternating-T map k is an isomorphism onto its selected local R_6 summand.

This is a counterexample to a **local inference**, not to the original geometric statement. Its chosen S_4/R_6 splittings are D-equivariant splittings with the correct restricted representation types; they are not asserted to be the splittings furnished by the full binary-icosahedral complement. The construction does not satisfy or claim full N-equivariance, global repeated-input injectivity, the actual normalizer kernel relations, or the global one-dimensional Hom_N constraint. In particular it does not produce a rank-three point of the actual operation or decide any of the remaining supports 1000, 3000, 4000, or empty.

The motivating obstruction is the verified parity-pencil condition in ../order-three-parity-pencil-rigidity/PROOF.md. The coefficient identities used here are defined and rederived explicitly below; no unproved coupling assertion is assumed. No actual cubic coefficient or selected source rank matrix is evaluated here.

## 1. The local group and actual restricted input types

Let omega be a primitive cube root of unity. Present D by

    a^3=1, j^4=1, j a j^{-1}=a^{-1}, c=j^2.

On T choose t_0,t_1,t_2 with a-weights 0,1,2 and

    j t_0=-t_0, j t_1=t_2, j t_2=t_1.

On W_v choose w_1,w_2 with a-weights 1,2 and

    j w_1=w_2, j w_2=-w_1.

These are the usual restrictions of the positive three-space and negative two-space. They satisfy all the displayed group relations, and c has the required signs. The choices of eigenvector scales are permissible: j^2=1 on T and j^2=-1 on W_v.

Put E=Sym^2 T tensor W_v. Its weight-zero part has basis

    e_1=t_1^2 tensor w_1,
    e_2=t_0 t_2 tensor w_1,
    e_3=t_0 t_1 tensor w_2,
    e_4=t_2^2 tensor w_2.

The action is

    j e_1=e_4, j e_4=-e_1,
    j e_2=-e_3, j e_3=e_2.

Choose its local S_4 weight-zero summand to be span(e_1,e_4), and its local R_6 weight-zero summand to be span(e_2,e_3). Each has j-eigenvalues i,-i, exactly as the weight-zero restrictions of S_4 and R_6 do.

These choices extend to a D-module splitting

    E = W_loc direct sum S_loc direct sum R_loc,
    dimensions 2,4,6,

with the correct restricted types W_v, S_4, R_6. Indeed the a-weight multiplicities of E are (4,4,4); after its weight-zero space has been assigned, its eight-dimensional nonzero-weight sector is four copies of the unique odd two-dimensional D representation with nontrivial a-action. Assign one copy to W_loc, one to S_loc, and two to R_loc. This also proves that this local splitting need not be the full-complement splitting: the local group leaves these assignments free.

## 2. The local maps and cancellation

Take the local odd target J_-=E with that decomposition, and take

    g:E -> J_- to be the identity.

Thus every one of its W_loc, S_loc and R_loc component scalars is nonzero; in particular both coefficient maps singled out in the unresolved reduction are nonzero.

Put F=Lambda^2 T tensor W_v. Its weight-zero part has basis

    z_1=(t_0 wedge t_1) tensor w_2,
    z_2=(t_0 wedge t_2) tensor w_1,

and j z_1=z_2, j z_2=-z_1. Define

    k(z_1)=e_3+2 e_2,
    k(z_2)=e_2-2 e_3.

This map commutes with j and a. Its two images are independent (their coefficient determinant is -5), so it is an isomorphism F_0 -> (R_loc)_0. The remaining four-dimensional nonzero-weight sectors of F and R_loc are both two copies of the same odd two-dimensional D module. Choose any D-isomorphism between them. This extends k to a D-isomorphism F -> R_loc.

Use the universal reconstruction from outer symmetry and cyclic zero:

    f(t_a,t_b,w)=-g(t_a t_b,w)/2+k(t_a wedge t_b,w)/2,
    f(t_a,w,t_b)=g(t_a t_b,w).

These are a valid D-equivariant cubic operation on the sector with two T arguments and one W_v argument. Explicitly the third cyclic term is -g/2-k/2, so the cyclic sum is zero; outer reversal is built into the definition. There is no hidden consistency condition from the argument symmetries: the multidegree sectors of the Schur module are independent. Moreover the local operation can be made surjective onto the whole twenty-dimensional restricted target. Indeed

    S_(2,1)T = (T tensor Lambda^2 T)/Lambda^3 T
              = (T tensor T)/1 = T direct sum P_5 = J_+.

Here the equalities are representation isomorphisms, using the invariant metric, orientation, and Sym^2 T=1 direct sum P_5. Choose such an isomorphism on the pure-T sector, keep the preceding odd-sector maps, and set the remaining sectors to zero. The even sector then surjects onto J_+, while g already surjects onto J_-. This realizes the same coefficient cancellation in a surjective D-equivariant cubic map to the full restriction of J. Surjectivity does not assert full-N equivariance or global repeated-input injectivity.

The three formal coefficients are now

    h=-e_1/2,
    C_tilde=e_2,
    D_tilde=-e_3/2+k(z_1)/2=e_2.

Consequently h is nonzero, and C_tilde and D_tilde have the same nonzero image in J_-/C h. In particular

    h wedge C_tilde wedge D_tilde=0.

This calculation evaluates the explicitly defined **abstract local counterconfiguration**, not the actual geometric operation. It uses no model of that operation, selected source point, rank computation, or source tensor.

### Optional local binary-image injectivity

The construction can also preserve the two-dimensional binary image for U=span(t_1,w_1), without claiming global repeated-input injectivity. In the previously unassigned sector with two W_v arguments and one T argument, use the analogous symmetric map g_even(w_a w_b,t)=f(w_a,t,w_b). Choose a nonzero p in (J_+)_0. Assign

    g_even(w_1^2,t_1)=p,
    g_even(w_2^2,t_2)=j p.

The two source vectors span a D-stable subspace on which a=1 and j interchanges them. Since j^2=1 on J_+, these assignments are equivariant. Extend by zero on a D-stable complement and take its alternating map to be zero. The same cyclic reconstruction then gives f(w_1,w_1,t_1)=-p/2. Together with f(t_1,t_1,w_1)=h=-e_1/2, these opposite-parity nonzero vectors make the binary coefficient map S_(2,1)U -> J injective. Thus its fixed image H_U has dimension two, and the odd quotient remains J_-/C h. This modification leaves the displayed cancellation unchanged and preserves surjectivity.

## 3. Relation to the parity-pencil obstruction

The negative quotient coefficients just constructed are C=D=v, with v nonzero. At the level of the local parity-pencil normal form, choosing alpha=beta=1 yields columns

    (s, t v), (t, s v).

Its rank is two generically and at both endpoints, and is one at the distinct off-endpoint pair t=s and t=-s. Thus the minors of the two-column local block do not exclude a reflection pair. This paragraph is only a statement about that abstract block. Its alpha=beta=1 choices are not asserted to be the positive coefficients of the cubic extension in Section 2. Nor is it asserted that accompanying B_1 and B_2 blocks have rank two there or that the whole block pencil comes from an N-equivariant operation.

## 4. What is, and is not, resolved

The failed implication has now been isolated rigorously: local dihedral representation types plus nonvanishing of the symmetric and alternating component maps do not force the needed exterior product. Even invertibility of g on its full weight-zero space is insufficient.

There are still two potentially decisive additional inputs: the **actual full-complement embedding** of S_4 and R_6 in E, and the relative coupling selected by the **full N-equivariant kernel**. The theorem dim Hom_N(S_(2,1)V,J)=1 fixes the actual map up to scalar, but this local construction makes no claim to meet that theorem's full-N hypothesis. No conclusion about the selected scalar ratio can therefore be extracted from the counterexample.

No new rank-three support is excluded. The current C3 frontier remains open; the counterconfiguration must not be described as progress toward a geometric exclusion.
