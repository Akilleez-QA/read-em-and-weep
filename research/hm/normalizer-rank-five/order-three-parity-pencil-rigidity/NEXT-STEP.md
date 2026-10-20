# The unresolved six-dimensional coefficient coupling

## Purpose

This note identifies the exact representation-theoretic sector containing the obstruction vectors C,D of PROOF.md. It does not determine their values or assert their independence. It is an unresolved next-step note, not part of the current independently verified proof packet. The canonical-line strengthening is already independent of this unresolved step.

Retain the notation T,W_v,W_0 of TARGET-STRENGTHENING.md. Write T'=Sym^2 W_v, so T,T' are the inequivalent three-dimensional A_5 representations. Let S_4 denote the odd four-dimensional irreducible and R_6 the odd six-dimensional irreducible. The elementary binary-icosahedral tensor identities give

    Sym^3 W_0=Sym^3 W_v=S_4,
    T tensor W_v=R_6,
    P_5 tensor W_v=S_4 direct sum R_6.

These identities can be checked by ordinary character arithmetic. In particular the symmetric-cube character x^3-2x is unchanged when the two two-dimensional characters are interchanged; the six-dimensional Clebsch-Gordan constituent here is Sym^5 W_v, and its character has squared norm one.

## 1. Actual target and universal odd source

The identity Lambda^2 V=A tensor W_0 gives

    A_+ tensor W_0=T tensor W_v=R_6.

A_+ is a three-dimensional positive-parity representation. It is nontrivial and irreducible: otherwise, since A_5 has no nontrivial one- or two-dimensional representations, its tensor product with W_0 would be reducible. It cannot be T, because T tensor W_0=W_0 direct sum S_4 is reducible. Therefore A_+=T'. It follows from Clebsch-Gordan for W_v that

    J_-=T' tensor S_4
        =W_v direct sum S_4 direct sum R_6.

The odd part of the universal cubic coefficient module is

    (S_(2,1)V)_-
       =S_(2,1)W_v
         direct sum (Sym^2 T tensor W_v)
         direct sum (Lambda^2 T tensor W_v)
       =2W_v direct sum S_4 direct sum 2R_6.

The first W_v comes from the pure W_v-cubic sector. The sector with two T arguments and one W_v argument is

    Sym^2 T tensor W_v
       =W_v direct sum S_4 direct sum R_6,
    Lambda^2 T tensor W_v=R_6.

Consequently the six-dimensional constituent occurs twice in the relevant source and once in the target. Multiplicity one in the target does not identify these two source maps.

## 2. The three formal coefficient vectors

Use abstract order-three eigenvectors t_0,t_1,t_2 of T, and w_1,w_2 of W_v. Their subscripts are weights modulo three. Define the symmetric-T and alternating-T coefficient maps by

    g(t_a t_b,w)=f(t_a,w,t_b),
    k(t_a wedge t_b,w)=f(t_a,t_b,w)-f(t_b,t_a,w).

Outer symmetry makes g symmetric in its two T arguments. Cyclic zero gives the formal identity

    f(t_a,t_b,w)
      =-g(t_a t_b,w)/2+k(t_a wedge t_b,w)/2.

Thus, before quotienting by the odd binary-image line, the three relevant formal coefficients are

    h=-g(t_1^2,w_1)/2,
    C_tilde=g(t_0 t_2,w_1),
    D_tilde=-g(t_0 t_1,w_2)/2+k(t_0 wedge t_1,w_2)/2.

Here h spans (H_U)_-, and C,D in PROOF.md are the images of C_tilde,D_tilde modulo that line. All three have a-weight zero. Since W_v has no weight-zero vectors,

    (J_-)_0=(S_4)_0 direct sum (R_6)_0,
    dimensions 2+2.

The desired independence of C,D is exactly the nonvanishing of

    h wedge C_tilde wedge D_tilde

in the third exterior power of this four-dimensional space.

## 3. What multiplicities determine, and what they do not

The actual cubic map is nonzero by repeated-input injectivity. Its image is the full irreducible normalizer target J, so its restriction onto the S_4 target constituent is nonzero. The only source copy of S_4 is in g. Thus g has a nonzero scalar on S_4.

On R_6 there are two equivariant coefficient maps: the R_6 summand of g, and k. After fixing abstract intertwiners, write their scalars as lambda and mu. At least one is nonzero, because the full image contains the R_6 target constituent. If lambda is nonzero, g is an isomorphism on its four-dimensional weight-zero source S_4 direct sum R_6. However D_tilde also receives the mu term, so this observation alone does not prove the displayed exterior product is nonzero.

The remaining issue is precisely whether the alternating-T contribution can cancel the R_6 component of the unique linear relation among the S_4 projections of h,C_tilde,D_tilde. This requires either a universal proof excluding cancellation for every nonzero permitted pair (lambda,mu), or an additional normalizer-equivariance identity fixing and controlling that relative coupling. Multiplicity counts, the C3 weight dimensions, and the reflection parity normal form by themselves do not supply that identity.

The full normalizer multiplicity-one theorem constrains the overall cubic map, but it does not by itself calculate its restriction to this two-copy R_6 multiplicity space. No such restriction coefficient has been determined here.

## Evidence boundary

All displayed coefficients are formal restrictions of the universal equivariant map. None was evaluated, and no selected coefficient matrix, rank instance, or numerical tensor was computed. This note records a bounded next step rather than an exclusion theorem. Its only write is this local artifact.
