# Homotopy-choice invariance of the complete correction

## Result and scope

Changing auxiliary homotopies does not supply a reduction of the remaining target by itself. With the underlying kernel and its derivative fixed, the defect and connection corrections must change together. Their paired change is a Čech boundary on every input, including nonclosed inputs, provided the primitive belongs to the actual regular sheaf complex. Selecting a nicer-looking K without updating the connection correction generally changes the answer.

This is a bounded formal theorem. No physical source or retained-test value is evaluated; no new cancellation is asserted.

## 1. Typed setup

Let (A,Δ), (B,δ_B), (C,δ_C) be cochain complexes over a field. For f:X→Y homogeneous of degree k, set

    d_Hom f = δ_Y f − (−1)^k f δ_X.

Fix degree-zero chain map Π:B→C and degree-two chain map T:A→B. Put M=ΠT. Fix their coefficient derivatives Π′,T′, hence M′=Π′T+ΠT′. The target/source scalar differentials are fixed under the derivative; the row differential Δ need not be. A homotopy presentation consists of

    Qdot_m : B^m → C^(m−1),
    Q_n    : A^n → B^(n+1),
    E_n    : A^n → B^(n+2),

satisfying

    Π′ = d_Hom Qdot,
    T′ = E − d_Hom Q.

In the supplied normal form E=E_conn=−LΓJ2+D. Define

    K_n = Qdot_(n+2) T_n − Π_(n+1) Q_n : A^n → C^(n+1).

Then the established presentation identity is

    M′ = d_Hom K + ΠE.                                      (1)

All comparisons below use the same complexes, Δ, Π, T, Π′ and T′. Changing frames, owner systems, L or ambient restrictions is outside this theorem unless independently transported into this fixed setup.

## 2. Exact changes induced by the two auxiliary homotopies

Suppose a second valid presentation has

    Qdot_new = Qdot + U,       |U|=−1,
    Q_new    = Q + V,          |V|= 1,
    E_new    = E + F,          |F|= 2.

Keeping Π′ fixed is equivalent to d_Hom U=0. Keeping T′ fixed is equivalent to

    F = d_Hom V = δ_B V + VΔ.                               (2)

Consequently

    K_new = K + J,       J=UT−ΠV,       |J|=1,
    d_Hom J = −Π d_Hom V = −ΠF.                             (3)

These are operator equalities in every input degree. For example,

    J_n = U_(n+2)T_n − Π_(n+1)V_n,
    F_n = δ_B V_n + V_(n+1)Δ_n,
    δ_C J_n + J_(n+1)Δ_n + Π_(n+2)F_n = 0.                 (4)

Conversely, any U,V of the stated degrees with d_Hom U=0 produces a valid new presentation if E is changed by (2). If E itself is required to remain fixed, actual inner homotopy changes must satisfy d_Hom V=0. At the projected identity (1) alone, the weaker requirement is Πd_Hom V=0; that weaker condition does not guarantee the original identity for T′.

In particular, changing Q while retaining the literal −LΓJ2+D formula unchanged is not a free operation. Either the change is Hom-closed, or the connection-side expression must be recomputed/reallocated to include d_Hom V. This theorem does not assert that an arbitrary altered Q is realizable by the original geometric overlap construction with all its extra identities and bounds.

## 3. General presentation-change theorem

More generally, assume K and E satisfy (1), and propose degree-one J and degree-two F. The proposed pair K+J,E+F satisfies the same equation (1) if and only if

    ΠF = −d_Hom J.                                         (5)

Thus a non-Hom-closed J demands compensation. Such compensation need not exist: −d_Hom J must lift through postcomposition by Π in the appropriate degree-two Hom space. A projected lift alone need not arise from changes of Qdot,Q, and need not satisfy the geometric domain requirements. If F=0, (5) is precisely d_Hom J=0. If d_Hom J=0, compensation is unnecessary at the projected level, although changes F with ΠF=0 are invisible there.

For any Z∈A^n, define the positive paired correction

    P_(K,E)(Z) = K_(n+1)Δ_n Z + Π_(n+2) E_n Z ∈ C^(n+2).

No assumption ΔZ=0 is made. Equation (5) gives the exact variation

    P_(K+J,E+F)(Z) − P_(K,E)(Z)
      = J_(n+1)Δ_n Z + Π_(n+2)F_n Z
      = −δ_C J_n Z.                                       (6)

The complete kernel derivative is, before any boundary is removed,

    M′Z = δ_C K_n Z + P_(K,E)(Z).

Its variation is identically zero, since the boundary variation δ_C J_n Z cancels (6).

This proves invariance in C^(n+2)/im δ_C. It proves invariance of an actual cohomology class only when the paired correction is a cocycle. That closure is not automatic in an arbitrary complex. With the derivative conventions above,

    δ_C P_(K,E)(Z) = δ_C M′Z
                  = M′ΔZ + MΔ′Z.

Here d_Hom M′=MΔ′ follows by differentiating the chain-map identity for M. Thus closure follows, for example, in a terminal target degree, or when the displayed right side vanishes. The theorem does not silently freeze Δ′ or infer closure from the word “defect.”

## 4. Application to the complete remainder, including weights and trace

For each direction d, group the connection and nonclosed-defect terms in the supplied remainder as −p[ΠE_d Z_d+K_dΔZ_d]. This grouping includes both −LΓ_dJ2 and D_d inside E_d. The separate (V_d p)MZ_d term and the complete baseline/current-curl are fixed.

Let Φ denote the fixed degree-zero chain map consisting of staircase transfer and full-sign extraction. Multiplication by the authenticated global dual test p is restriction-compatible. The boundary-free representative of the remainder is

    R_red = Φ[pMR* − Σ_d((V_d p)MZ_d + pP_(K_d,E_d)(Z_d))].

The full remainder is

    R_full = R_red − δ_tensor Φ[pΣ_d K_d Z_d].

For valid changes J_d,F_d, equation (6) gives

    R_red,new − R_red = +δ_tensor Φ[pΣ_d J_d Z_d],           (7)
    R_full,new − R_full = 0.                                (8)

A genuine sheaf-boundary conclusion requires more than a rational formal identity:

1. Both presentations and the necessary restrictions are defined on the same admitted regular cochain domains, or an independently justified common comparison.
2. Φ[pΣ_d J_d Z_d] is a regular degree-three cochain in the canonical-valued target complex for n=2. It has the actual homogeneous transitions, characters and all required owner weights. If both old and new boundary primitives already have established domains, their difference provides this condition directly.
3. The paired terms and any trace/residue functional are defined in that same target complex, and the functional annihilates its genuine boundaries.

Under these premises, (7) is a genuine Čech boundary, the closed representatives have the same cohomology class, and their admitted Serre traces agree. The full remainder (8) agrees algebraically even before tracing. If only rational meromorphic primitives are available, a boundary there does not automatically yield a boundary in the regular complex. No new pole envelope or owner-domain theorem for a proposed replacement homotopy is supplied here.

## 5. Why a Hom-closed change cannot erase a nonzero defect class

For any degree-one Hom-closed J,

    δ_C J_n + J_(n+1)Δ_n = 0,
    J_(n+1)Δ_n Z = −δ_C(J_n Z).                             (9)

Therefore a Hom-closed modification of K changes KΔZ by a boundary even when Z is nonclosed. Under the regular-domain conditions, it cannot alter a nonzero cohomology class of KΔZ whenever that defect is a cocycle. More generally it cannot alter its class in cochains modulo boundaries, whether or not it is closed.

The individual defect need not be closed: δ_C(KΔZ)=(d_Hom K)ΔZ. Accordingly, one should not assign it a cohomology class without verifying this vanishes in the relevant degree/domain. A Hom-closed change can simplify a representative or erase a defect that was already exact; (9) does not assert that every exact defect can be removed by an admissible Hom-closed J, since extension and geometric restrictions may obstruct that choice.

If a non-Hom-closed change makes the defect disappear, the lost contribution is transferred to ΠF, modulo the boundary in (6). Any genuine simplification must account for that transfer and prove the replacement domain. This rules out a reduction merely from selecting a nicer K, while leaving open an independently established simplification of the entire paired expression.

## 6. Synthetic counterexample to dropping compensation

This example is an abstract finite cochain complex, not a source evaluation. Work over any field and a formal parameter t. Let

    A^2 = k z,   A^3 = k w,   Δz=w,   Δw=0,
    B^4 = C^4 = k c,

with all other groups zero and δ_B=δ_C=0. Let Π be the identity B→C, and define the degree-two chain map T(t) by T(t)z=t c and T(t)w=0. Then Π′=0, T′z=c, T′w=0, and Δ′=0.

Take Qdot=0, E=0, and degree-one Q given by Qw=−c and Qz=0. Then

    d_Hom Q(z)=−c,     T′=E−d_Hom Q,
    K=−Q,             Kw=c,     Kz=0,
    P_(K,E)(z)=c.

Now choose Q_new=0 and Qdot_new=0. Thus V=−Q, J=−K, and

    d_Hom V(z)=c,     d_Hom J(z)=−c.

The mandatory compensation is E_new=d_Hom V, so E_new z=c. The valid new paired correction remains c, entirely in its connection part:

    P_(0,E_new)(z)=c.

If one improperly keeps E_new=0, the computed paired correction becomes zero and (1) fails by c. Since C^3=0, c is not a boundary and represents the nonzero class in H^4(C). Thus omitting compensation can delete a genuine nonzero cohomology class, even though the replacement K=0 looks maximally simple. In this example Jz=0, so the correctly compensated paired change is exactly zero, consistent with (6).

## Sources

- https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-complete-remainder-normal-form/RESULT.md, especially §§2 and 5.
- DEPENDENCY-REVIEW.md, especially §§1, 5, 6 and 9.

The displayed algebra establishes conditional choice invariance. It does not authenticate the underlying geometric premises or prove the complete target vanishes.
