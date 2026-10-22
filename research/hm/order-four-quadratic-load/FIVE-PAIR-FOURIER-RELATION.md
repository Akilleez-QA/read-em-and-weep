# The intrinsic five-pair relation for an exceptional hyperplane block

## 1. Transported binary quadratics

Use the coordinate block x_0=0 and its five lines tau^b L_00, b in F_5, with L_00 parametrized by (0,u,v,-v,-u). The Heisenberg action is trivial on the evaluation section space, so these transported parameters are the same kappa parameter on Gamma. Let zeta be a primitive fifth root and write

    q_b(u,v)=q(zeta^b u,zeta^(2b)v,-zeta^(3b)v,-zeta^(4b)u)
             = A_b u^2+B_b uv+C_b v^2.

Here q is an arbitrary quadric in the four coordinates of the block. With q_ij denoting its monomial coefficients, direct substitution gives

    A_b=q_11 zeta^(2b)-q_14+q_44 zeta^(3b),
    C_b=q_22 zeta^(4b)-q_23+q_33 zeta^b,
    B_b=q_12 zeta^(3b)-q_13 zeta^(4b)-q_24 zeta^b+q_34 zeta^(2b).

Thus the Fourier supports are respectively {0,2,3}, {0,1,4}, and {1,2,3,4}. The ten displayed coefficients are independent, so these support conditions characterize the entire ten-dimensional restriction image, not merely necessary equations.

## 2. Determinantal relation on five unordered pairs

Represent the five chosen unordered pairs by nonzero binary quadratic factors

    f_b=a_b u^2+b_b uv+c_b v^2,

each defined up to its own nonzero scalar. They arise from a block quadric exactly when there are scalars lambda_b, all nonzero, with q_b=lambda_b f_b. The Fourier support conditions give

    sum zeta^(-b) a_b lambda_b=0,
    sum zeta^(-4b) a_b lambda_b=0,
    sum zeta^(-2b) c_b lambda_b=0,
    sum zeta^(-3b) c_b lambda_b=0,
    sum b_b lambda_b=0.

Define M(f) to have its b-th column

    (zeta^(-b)a_b, zeta^(-4b)a_b,
     zeta^(-2b)c_b, zeta^(-3b)c_b, b_b)^T.

The determinant is not the zero polynomial: for example the coefficient of a_0 a_1 c_2 c_3 b_4 is the product, up to sign, of two nonzero two-by-two Fourier minors, since the corresponding fifth-root ratios are distinct. Then D(f)=det M(f)=0 is the desired intrinsic codimension-one relation. It is a well-defined divisor on (P^2)^5: changing the scalar representative of f_b multiplies the determinant by that scalar. It has multidegree (1,1,1,1,1). On the dense open where rank M=4 and its kernel generator has no zero coordinate, the determinant equation is also sufficient, and reconstructs a unique projective block quadric by inverse Fourier transform. The nonzero-kernel-coordinate condition is essential on the boundary: det M=0 alone may permit only a zero restriction on one of the five lines.

This is a symbolic identity in arbitrary coefficients, not a selected coefficient or rank experiment.

## 3. Irreducibility and geometry

The rational restriction map P^9 -> (P^2)^5 has irreducible nine-dimensional image by the ten-root argument. Its image closure is therefore an irreducible hypersurface contained in (D=0).

Its projection onto any four P^2 factors is dominant: eight independently generic points on four skew lines impose eight independent conditions on block quadrics, and adjoining a ninth point proves the quadrics through them do not generically contain any of the relevant lines. Thus the defining irreducible equation of the image must depend on every one of the five factor variables; otherwise its projection omitting a variable on which it did not depend would fail to be dominant. Since D has degree one in each factor, that irreducible equation already consumes its full multidegree. D has no additional factor and defines the image closure with multiplicity one.

In particular this is an irreducible divisor of Segre multidegree (1,1,1,1,1), birational to P^9 via block-quadric reconstruction. The determinant presentation is linear in the five middle coefficients b_b, and has total degrees two in the a_b, two in the c_b, and one in the b_b: expanding by the final row leaves two A rows and two C rows. No conclusion about quartic surfaces singular at the resulting kappa points is built into this relation.

## 4. Ordered roots and the decic

If the two roots in pair b are [s_b:t_b] and [s'_b:t'_b], one may use

    f_b=(t_b u-s_b v)(t'_b u-s'_b v),
    a_b=t_b t'_b,
    b_b=-(t_b s'_b+s_b t'_b),
    c_b=s_b s'_b.

Substitution into D yields an explicit polynomial of degree one in each of the ten ordered root coordinates. It is unchanged by exchanging the two roots of a pair. Its zero set is independent of all root representatives.

The product F=product_b f_b is the binary decic recording the ten roots after forgetting the five-pair assignment. The determinant is naturally an equation on PAIRED decics; it must not be declared an equation in the coefficients of F alone without eliminating the pairing. An exact pairing-free characterization is: F belongs to the image if it admits a factorization into five labeled quadratic factors satisfying D=0 (and, on the actual open, the nonzero-kernel conditions).

The multiplication morphism (P^2)^5 -> P^10 is finite and has generic degree 10!/(2!)^5=113400. Therefore the image of D is again an irreducible hypersurface in decic coefficient space. One can obtain a polynomial equation by taking the norm/product of the determinant over all labeled pairings; this norm is generally a power of the reduced irreducible equation. Since the pullback of a coefficient hyperplane has class sum h_b, the pushforward cycle has degree 113400. This number is the norm-cycle degree, NOT a claim that the reduced image hypersurface has that degree; its degree is 113400 divided by the generic degree of D onto its image, which is not determined here.

The five-pair relation is preserved by cyclic relabeling b -> b+1 and reversal b -> -b: the Fourier row scalings and row/column permutation signs cancel. These are actual symmetries of this presentation. No larger invariant-theoretic identification is asserted without proof.

## 5. Remaining comparison

All thirty exceptional hyperplane blocks are transported to this one by configuration-preserving Fourier/chirp changes, so the same construction applies after their induced parameter changes. This provides the exact codimension-one exceptional root relation needed for a comparison with the locus of ten Gamma-points admitting an integral quartic double at all ten. Equality, disjointness, or containment between those two loci remains unproved.
