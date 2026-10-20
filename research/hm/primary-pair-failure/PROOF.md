# The exact reduced primary failure locus for quadratic–cubic pairs

Work over C. Let F be the normalized Horrocks–Mumford bundle on P^4, E=F(3), S_d=H^0(O(d)), and M_j=H^1(F(j)). For nonzero u in S_2 and v in S_3 put

    r(u,v)=dim(uM_1+vM_0).

This is the dimension of a primary cohomology image, not the rank of a quadratic form. No selected pair is evaluated.

## 1. Equivariant cubic multiplication

Let N be the finite HM normalizer and H its Heisenberg subgroup. Use A=V_1 (dimension five), W=W' of character chi_2' (dimension two), and J of character chi_5 (dimension five). The normalized identities are

    M_0=A*,  M_1=A tensor W,  M_3=W,
    S_2=A* tensor sl(W),  S_3=A tensor (J direct sum W).       (1)

The primary reference is Horrocks–Mumford, Topology 12 (1973), 63–81, especially observation (2.2), Lemma 3.3, equations (4.2), (4.6), (4.12), and the appendix:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

These exact dualities and twists are recorded in PR449 and PR452. In particular F=E(-3); M_0 is A*, not A. The central weight of A is two modulo five; S_3 has weight 3·4=2, agreeing with Hom(M_0,M_3)=A tensor W. The determinant of W is trivial, identifying Sym^2(W) with sl(W).

Cubic multiplication gives an N-equivariant map

    pi:S_3 -> Hom(M_0,M_3)=A tensor W.                       (2)

The H-isotypic criterion (2.2) makes A tensor J and A tensor W irreducible and nonisomorphic N-modules. The latter occurs exactly once in S_3. The module M is generated in degree zero, as follows directly from the quotient presentation in HM (4.2), also recorded in PR167. Thus S_3 M_0=M_3 is nonzero, so (2) is nonzero. Schur's lemma proves that (2) vanishes on A tensor J and is a nonzero scalar isomorphism on A tensor W. Consequently pi is surjective with kernel

    K=A tensor J,  dim K=25.                                (3)

After absorbing this scalar in the identification, pi is the projection. This is a universal abstract representation identity; it supplies no binary-quartic-coordinate identification or selected multiplication matrix.

## 2. Exact failure criterion and projective bundle

PR449 proves that multiplication by every nonzero u has nonzero image. Its image is a line precisely when

    u=a tensor n_l,

where a is nonzero in A* and n_l is a nonzero member of Hom(W/l,l), viewed inside sl(W). Then uM_1=l. Otherwise uM_1=W. The reduced projective locus of these bad quadratics is

    B=P(A*) times P(W),

embedded in P(S_2) by O(1,2). Its dimension is five. Here projective spaces and projective bundles parametrize one-dimensional subspaces.

It follows exactly, for nonzero u and v, that

    r(u,v)<2
    iff [u] belongs to B and pi(v) belongs to A tensor l.    (4)

Indeed, on B the quadratic image is l, and the cubic image is the image of the linear map pi(v):A* -> W. Containment of that image in l is equivalent to membership in A tensor l. Off B the quadratic already covers W. On the failure locus r=1, never zero.

On B let L=pr_2^*O_{P(W)}(-1) be the tautological line subbundle of the trivial W bundle. Define the rank-thirty vector subbundle

    E_B=ker[S_3 tensor O_B -> A tensor (W tensor O_B/L)].     (5)

The surjection in (5) is induced by pi. The irreducible splitting in (1) identifies it, noncanonically as to scalar identifications but canonically as to the summands, with

    E_B ≅ (K tensor O_B) direct sum (A tensor L)
        ≅ O_B^25 direct sum O_B(0,-1)^5.                    (6)

The negative sign is essential: l is a tautological subspace of W, not its dual. The quadratic nilpotent line itself corresponds to l^2 under the symplectic identification, explaining O(1,2) for B but not changing L in (5).

The closed immersion P(E_B) -> B times P(S_3), followed by the Segre–Veronese embedding of B in P(S_2), has exactly the points in (4). Both this image and the reduced failure locus have the same reduced closed subscheme structure. Thus the reduced primary failure locus is

    X_red ≅ P_B(E_B) in P^14 times P^34.                    (7)

It is smooth and irreducible, with fibers P^29, dimension 5+29=34, and codimension 48-34=14. We do not assert that an arbitrary maximal-minor presentation of the degeneracy scheme is reduced, or make claims about embedded structure at affine vertices.

For each fixed bad nonzero u, precisely one projective linear P^29 of cubics fails to rescue it. Its complement is nonempty open, of failure codimension five. A good quadratic is rescued already, independently of the cubic.

## 3. Cubic rank strata and a uniform primary obstruction bound

The cubic alone has rank zero precisely on P(K)=P^24. It has rank at most one when pi(v) is a decomposable tensor (including zero). The rank-at-most-one cone in A tensor W has affine dimension 5+2-1=6, so its inverse image in S_3 has dimension 25+6=31. Its projectivization has dimension thirty and codimension four in P^34. Its rank-one stratum has dimension thirty; the rank-two stratum is open dense. In particular a rank-two cubic rescues every nonzero quadratic simultaneously, not merely a fixed bad quadratic. For a rank-one cubic with image l, the bad quadratics that remain bad are exactly P(A*) times {l}, a P^4 inside B. For a rank-zero cubic, all of B remains bad. These statements classify the opposite projection of (7) as well as its fibers over quadratics.

There is also a consequence for the full order-five obstruction. Put V=H^0(E), of dimension four; this V is not the five-dimensional A. Use

    T=H^1(B_0(5)), B_0=End_0(F),
    L_0=im[V tensor M_3 -> T],
    U=uH^1(B_0(3))+vH^1(B_0(2)),
    Q_5=T/U,  R=T/(L_0+U).

PR456 proves that the natural cup map V tensor M_3 -> T is injective, so dim L_0=8. Naturality of cups shows that L_0 intersect U contains the image of V tensor (uM_1+vM_0). This image has dimension exactly 4r(u,v). Hence

    0 -> L_0/(L_0 intersect U) -> Q_5 -> R -> 0,
    0 <= dim Q_5 - dim R <= 8-4r(u,v).                      (8)

For every nonzero quadratic the right-hand bound is at most four. Outside X_red it is zero; on X_red it is at most four, not necessarily equal to four. Non-primary source classes may enlarge L_0 intersect U. Thus primary coverage is sufficient, not necessary, for removal of the primary obstruction.

For globally coprime u,v let k count the HM evaluation-degeneracy lines contained in both forms. PR458 proves dim R<=6+k. Therefore (8) improves its general full bound to

    dim Q_5 <= 10+k for every such nonzero pair,
    dim Q_5 <= 6+k outside X_red.                           (9)

In particular k=0 gives the bounds ten and six respectively. Neither establishes vanishing of R or of the original fixed Q_5.

## 4. Dependencies, contribution, and limits

The structural dependencies are pinned here:

- PR449, quadratic multiplication and exact reduced cone: e4b6acdd27d8da8be4052c117ea2dca0f48f46ff, https://github.com/Akilleez-QA/read-em-and-weep/blob/e4b6acdd27d8da8be4052c117ea2dca0f48f46ff/research/hm/quadratic-failure-cone/PROOF.md
- PR452, exact primary representations: 3b1d18105fa8b8b39bd96d889a34bc81a860f181, https://github.com/Akilleez-QA/read-em-and-weep/blob/3b1d18105fa8b8b39bd96d889a34bc81a860f181/research/hm/cubic-defect-channels/PROOF.md
- PR167, degree-zero generation: 063da90fc4543304e87e701cdefcc08225412f17, https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md
- PR456, injective eight-dimensional primary target: 07c11a096970a58f5f275b1438d4df3a27a1c6dd, https://github.com/Akilleez-QA/read-em-and-weep/blob/07c11a096970a58f5f275b1438d4df3a27a1c6dd/research/hm/symmetric-evaluation/PROOF.md
- PR458, exact primary/residual sequence and residual bound: b46c3b48a8b10a7d0656fde247f2c3f258d1fd23, https://github.com/Akilleez-QA/read-em-and-weep/blob/b46c3b48a8b10a7d0656fde247f2c3f258d1fd23/research/hm/pair-interpolation/PROOF.md

Unlike PR461's punctured families under good-quadratic hypotheses, this identifies the reduced primary failure locus for all nonzero quadratic–cubic pairs, including bad quadratics. It also replaces the retained eight-dimensional primary upper bound by four uniformly for nonzero quadratics. The residual interpolation problem remains independent.

No original-pair membership, selected HM/source-instance evaluation, numerical rank, coefficient search, generator/checker, or large computation is used. No conclusion about actual-source membership, six pure conditions, higher-order lifting, or quantization algebraicity follows. The result is an authored mathematical proof, subject to scoped review, not formal machine verification.
