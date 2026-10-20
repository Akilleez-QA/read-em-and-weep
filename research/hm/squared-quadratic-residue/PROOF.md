# Squared-quadratic residues and the local septic mismatch

Work over C on P^4. Let F be the normalized Horrocks–Mumford bundle, B=End_0(F), E=F(3), V=H^0(E), D=det V, and C the disjoint union of its twenty-five evaluation-degeneracy lines. Fix nonzero globally coprime forms u in S_2 and v in S_3, where S_d=H^0(O(d)). Set a=u^2, of degree four, and

    A=H^1B(5), L=im[V tensor H^1E -> A],
    U=a H^1B(1)+v H^1B(2), P=A/U, R=A/(L+U).

Thus P is precisely the previously unresolved P_5^(2,1) of PR463. The structural results below apply to general such forms. They describe the actual paired collision coefficient only when u=t_2,v=t_3 are the descended pair in PR437/PR463.

## 1. The simultaneous residue criterion, with the primary term retained

PR457 proves the canonical residue models and their multiplication naturality. PR463 extends the same resolution to degree one, whose primary image is zero. Consequently

    H^1B(1)^* = D^* tensor [H^0O_C(4)/res S_4],
    (H^1B(2)/P_2)^* = D^* tensor [H^0O_C(3)/res S_3],
    (A/L)^* = D^* tensor [H^0O_C/C],

where P_2 is the injective image V tensor M_0, M_j=H^1F(j). Restriction is injective in degrees three and four. Multiplication by a and v, followed by projection to A/L, has transpose

    [lambda] -> ([lambda a|C], [lambda v|C]).

The determinant line is common, as proved by the resolution-duality identification in PR457. It is not a choice of independent normalizations on the lines. Therefore R^*=D^* tensor W, where W is the space of constant tuples lambda on the component lines, modulo diagonal constants, for which there exist f in S_4 and g in S_3 with

    f|line=lambda_line a|line, g|line=lambda_line v|line.       (1)

The extensions f,g are unique for each tuple. There is an exact sequence

    0 -> L/(L intersect U) -> P -> R -> 0.                    (2)

In particular (1) alone describes the residual quotient, not the entire P.

Let r_v be the rank of the abstract primary multiplication v:M_0 -> M_3, with 0<=r_v<=2. Naturality puts V tensor vM_0 in L intersect U. Since dim V=4 and the primary cup map into A is injective, dim L=8 gives

    0 <= dim P-dim R <= 8-4r_v.                              (3)

No direct primary contribution comes from H^1B(1), whose primary image is zero. This does not say that its entire image misses L. PR462 classifies r_v using the normalizer projection; it is not evaluated here. If r_v=2 then P=R canonically. Primary coverage is sufficient, not asserted necessary.

## 2. Septic obstruction and its exact kernel

Let k count the lines contained in both V(u) and V(v). Define

    T=H^0(I_C(7)) intersect (a,v)_7,
    Phi:W -> T, [lambda] -> vf-ag.                           (4)

Changing lambda by c changes (f,g) by c(a,v), so Phi is well-defined. If vf=ag, global coprimality implies f=ca and g=cv: in the polynomial UFD, a divides f, and both have degree four. Thus lambda=c on every line where at least one of a,v is nonzero. The remaining k entries are free. Conversely tuples supported on these k lines satisfy (1) with f=g=0. At least one line is not common-contained, since quartic restriction is injective and a is nonzero. These supported tuples are independent modulo constants. Hence

    0 -> C^k -> W -> im Phi -> 0.                            (5)

This proves dim P>=dim R>=k, without any avoidance hypothesis.

## 3. Exact correction when the pair has common zeros on C

There is a local mismatch map that determines im Phi without assuming C avoids V(u,v). For each component line l put a_l=a|l, v_l=v|l and define

    K_l={(p,q) in H^0O_l(4) directsum H^0O_l(3): v_l p=a_l q},
    E_l=K_l / C(a_l,v_l),    E=directsum_l E_l.              (6)

The span in (6) is zero if both entries vanish. For H in T, choose H=vf-ag. Define epsilon(H) to be the classes of (f|l,g|l) in E_l. Such pairs lie in K_l since H vanishes on C. Any two representations differ by c(a,v), by global coprimality and degree equality. Thus epsilon is well-defined and linear.

By definition, epsilon(H)=0 exactly when on every line there is a constant lambda_l with (f|l,g|l)=lambda_l(a_l,v_l). These constants form (1); on common-contained lines they can be freely chosen. Consequently

    0 -> C^k -> W --Phi--> T --epsilon--> E                  (7)

is exact at W and T. No surjectivity onto E is asserted. In particular

    dim R=k+dim ker epsilon,
    max(k, k+dim T-dim E) <= dim R <= k+dim T.                (8)

The mismatch spaces have a direct divisor interpretation, retaining multiplicities. If (a_l,v_l) is not identically (0,0), choose a greatest common divisor h_l of degree d_l in the binary homogeneous polynomial ring, with gcd(0,b)=b. Write a_l=h_l a'_l, v_l=h_l v'_l. Coprimality of the nonzero reduced pair implies

    K_l={(a'_l b,v'_l b): b in H^0O_l(d_l)},
    E_l is isomorphic to H^0O_l(d_l)/C h_l,
    dim E_l=d_l.                                           (9)

For the cases with one zero entry this follows directly: if a_l=0,v_l!=0, p=0 and q is arbitrary cubic, so d_l=3; if v_l=0,a_l!=0, q=0 and p is arbitrary quartic, so d_l=4. If neither vanishes, division in the binary UFD proves the formula. Multiplication by the nonzero reduced pair is injective, and the original pair corresponds exactly to b=h_l. If both vanish, K_l is the full space in (6) and dim E_l=5+4=9. Therefore

    dim E=9k + sum_(non-common-contained l) d_l.             (10)

A choice of scalar for h_l changes the displayed isomorphism, not E_l or epsilon. Formula (9) measures the common divisor of u_l^2 and v_l, not merely reduced common support. In particular tangencies and multiplicities are not discarded.

If C intersect V(u,v) is empty, every d_l=0 and k=0. Thus E=0 and (7) gives W isomorphic to T. Conversely k=0 by itself only makes Phi injective: nonzero local divisor spaces may remain, and the correct image is ker epsilon, not automatically all of T.

Together with r_v=2, (7) gives an exact full criterion

    P=0 if and only if k=0 and ker epsilon=0.               (11)

Under avoidance and r_v=2 this simplifies to T=0. Neither hypothesis is asserted for the original pair.

## 4. Consequence for the entire actual order-four coefficient

For the actual descended pair, PR463 identifies the dual of the paired order-four H^2 coefficient as

    P_5^(2,1) directsum Q_4 directsum Q_5.

The present (5) gives dim P_5^(2,1)>=k. PR463 gives dim Q_4>=2k from line-linear supported multipliers, and PR458 gives dim Q_5>=k from constant supported multipliers. They are separate direct summands, so

    dim H^2(Z,I_D^4 E_pair)_chi >= 4k.                       (12)

Thus any common-contained HM line rigorously excludes whole order-four coefficient vanishing. This statement requires no evaluation of a selected pair; whether the actual pair has such a line remains open. It does not infer a source value from the nonzero coefficient group.

## Dependencies and scope

- PR457, canonical duality and fixed cubic residue model, commit 961694c4f3c805f0d58508811a42da4030dce7a6:
https://github.com/Akilleez-QA/read-em-and-weep/blob/961694c4f3c805f0d58508811a42da4030dce7a6/research/hm/fixed-cubic-interpolation/PROOF.md
- PR463, degree-one residue model, three order-four summands, Q_4 bound, commit 8ec3631dcd6937e6cc7491d0200c1c78b5d21434:
https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md
- PR462, cubic primary classification and injective primary image, commit a10049b8f7c57f30476c6f9c5554685583ea8c1b:
https://github.com/Akilleez-QA/read-em-and-weep/blob/a10049b8f7c57f30476c6f9c5554685583ea8c1b/research/hm/primary-pair-failure/PROOF.md
- PR458, Q_5 supported-line bound, commit b46c3b48a8b10a7d0656fde247f2c3f258d1fd23:
https://github.com/Akilleez-QA/read-em-and-weep/blob/b46c3b48a8b10a7d0656fde247f2c3f258d1fd23/research/hm/pair-interpolation/PROOF.md

The contribution is the missing squared-quadratic residue criterion, an exact local correction to the septic intersection when avoidance fails, and the resulting four-dimensional-per-common-line exclusion at order four. H^0(I_C(7)) is the saturated septic target: neither the six-dimensional quintic space nor the forty-dimensional sextic space is substituted for it. No septic dimension, generic fixed-cubic residual surjectivity, original-pair rank or intersection value is claimed. Actual-source membership, pure conditions, higher-order lifting and algebraicity remain separate. No selected HM/source-instance evaluation, numerical matrix/rank, parameter search, generator/checker or large computation was performed. Authored mathematical reasoning for independent review, not formal verification.
