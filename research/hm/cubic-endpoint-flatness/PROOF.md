# Endpoint dual numbers and the finite flat three-sheeted inverse-image curve

Status: structural mathematical derivation over C, conditional on the pinned predecessors below. No actual HM/source coefficients, selected point instances, numerical matrix ranks, scans, or computer-algebra calculations are used. The alternative r=2 remains conditional and is not asserted to occur.

## 1. Immutable dependencies and theorem

The direct input is PR605 at commit `9df4c45d0c76ded1075a0652707bdbcd1f424189`, file `research/hm/cubic-exceptional-fibers/PROOF.md`:

https://github.com/Akilleez-QA/read-em-and-weep/blob/9df4c45d0c76ded1075a0652707bdbcd1f424189/research/hm/cubic-exceptional-fibers/PROOF.md

Its predecessor is PR604 at `a4a0b5ed6e9dd0c18e3a263d1b3f8d9a49f2bf8d`, file `research/hm/cubic-embedding-locus/PROOF.md`. All actual-primary/modular dictionary and source dependencies of these predecessors remain assumptions here. This note neither re-audits nor replaces them.

Use the predecessor's finite normalization Phi:M=Bl_Z(P4)->V subset P9, with M smooth, pi:M->P4 the blowup of the thirty nodes, and bilinear identity

    B(Phi(m)) pi(m)=0.

Assume r=2. Fix an arbitrary one of the sixty component lines ell with endpoints z,w. Set

    Q=Sigma_ell=Phi(ell_tilde),
    p_z=ell_tilde intersect E_z,    p_w=ell_tilde intersect E_w,
    alpha=Phi(p_z),                beta=Phi(p_w).

The two target points are distinct. For every y in Q, P(ker B(y))=ell. The exceptional restrictions Phi|E_z and Phi|E_w are linear embeddings, and Phi|ell_tilde is an isomorphism to Q. The reduced inverse image is the chain

    A_z union ell_tilde union A_w,
    A_z=(Phi|E_z)^(-1)(Q),   A_w=(Phi|E_w)^(-1)(Q),

of three projective lines, each mapped isomorphically to Q. Its junctions are p_z,p_w, with distinct tangent lines at each junction. Away from alpha,beta the complete fibers are three reduced points. At alpha the fiber has one unramified point in E_w and one point p_z whose tangent kernel has dimension one; at beta the roles reverse. At these ramified points the local fiber algebra is C[t]/(t^e), with e>=2 not determined in PR605.

**Theorem.** Under these inputs:

1. At every one of the 120 endpoint ramification points, e=2. Every endpoint fiber is the disjoint union of a dual-number point Spec C[t]/(t^2) and a reduced point. All fibers over Q have length three.
2. The full scheme-theoretic inverse image N=Phi^(-1)(Q), not only its reduction, is reduced. Its morphism f:N->Q is finite flat of degree three. Thus N is exactly the reduced three-line chain above.
3. Under the three component identifications with Q, its finite algebra is

       f_*O_N = {(a,b,c) in O_Q^3 :
                   a(alpha)=b(alpha), b(beta)=c(beta)}.

   As an O_Q-module it is isomorphic to

       O_Q direct-sum O_Q(-alpha) direct-sum O_Q(-beta)
           isomorphic to O_P1 direct-sum O_P1(-1)^2.

4. At either junction, the completed local curve map is

       C[[s]] -> C[[s,u]]/(u(u-s)),    s |-> s.

   Equivalently the source is an ordinary node C[[u,v]]/(uv) and the target parameter is s=u+v. The other sheet is unramified. This is a normal form only for the curve N->Q, not for the ambient fourfold morphism or image V.
5. The trace-discriminant divisor of f is exactly 2alpha+2beta.

## 2. Fixed-target incidence holds scheme-theoretically

The identity B(Phi(m))pi(m)=0 is an identity of morphisms/sections on the reduced smooth scheme M, not merely a restriction on closed-point support. It is initially the polynomial syzygy identity off the exceptional divisor and extends across M; alternatively the predecessor states it globally.

Restrict to the scheme-theoretic fiber over a closed target y. Choose a target affine projective chart containing y and normalize its homogeneous lift by the chosen nonzero coordinate. In the fiber algebra all target affine coordinate functions become their constant values at y. Incidence consequently specializes to

    B(y) pi=0

as equations in that algebra. A source affine projective chart likewise converts these into the pullbacks of the linear equations of the projective kernel P(ker B(y)). Because that kernel is exactly ell, its linear equations generate the ideal sheaf of ell. Therefore the scheme fiber is contained in the scheme-theoretic inverse image pi^(-1)(ell). This argument is stronger than the set-theoretic containment used for support classification and introduces no new rank evaluation.

## 3. A universal endpoint chart forces e=2

Work at p_z. Choose affine linear coordinates x_1,...,x_4 centered at z, with ell given locally by x_2=x_3=x_4=0. On the blowup chart around the direction p_z write

    x_1=t,    x_i=t u_i (i=2,3,4).

Then p_z has t=u_2=u_3=u_4=0; E_z has t=0; and ell_tilde has u_2=u_3=u_4=0. Let F be the local scheme-fiber algebra at p_z and n its maximal ideal. Section 2 yields the exact relations

    t u_i=0 in F,    i=2,3,4.                              (1)

The one-dimensional tangent kernel is dual to n/n^2. A nonzero vector k in this kernel must have nonzero t component: otherwise it is tangent to E_z, contradicting the injectivity of d(Phi|E_z). It also has some nonzero u_i component: otherwise it is a nonzero multiple of the tangent to ell_tilde, contradicting the injectivity of d(Phi|ell_tilde). Hence the images of t and of at least one u_i in the one-dimensional space n/n^2 are both nonzero.

Nakayama gives n=(t). For the chosen i there is h in F with u_i=t h, and h has nonzero residue because u_i is nonzero modulo n^2. Thus h is a unit. Substituting into (1) gives t^2 h=0 and therefore t^2=0. Since t is nonzero modulo n^2, it is not zero in F. As F has residue field C and n=(t), this proves

    F isomorphic to C[t]/(t^2).

The identical argument works at p_w. The other fiber point is reduced by the predecessor, so the total endpoint fiber length is three. This proof uses no cubic degree bound and no selected coefficients: scheme-theoretic linear incidence, the universal blowup chart, and the two immersive restrictions suffice.

## 4. Constant fiber length gives flatness and reducedness

Equip Q with its reduced line structure, and form N=M times_V Q. Its map f to Q is finite, being a base change of Phi. Its fibers agree scheme-theoretically with the fibers of Phi over points of Q. By the predecessor and Section 3 all have length three.

Let A=f_*O_N, a finite coherent O_Q-algebra. Its generic rank is three. Here is a justification that does not assume reducedness of N: the known reduced support has exactly three components mapping isomorphically to Q, so A tensor C(Q) surjects onto C(Q)^3 and has dimension at least three. At any closed point the dimension of the fiber is three, and a finite module over a DVR has rank at most its fiber dimension. Hence the generic rank is exactly three.

At every closed point q of the smooth integral curve Q, the finite module A_q over its DVR O_(Q,q) has the form

    O_(Q,q)^3 direct-sum T_q,

where T_q is a finite torsion module. Its fiber dimension is three plus the number of nonzero cyclic summands of T_q. Since the fiber dimension is three, T_q=0. Thus A is locally free of rank three and f is finite flat of degree three.

Moreover A tensor C(Q)=C(Q)^3, by the dimension-three surjection above. Flatness over the integral curve makes A inject into this generic algebra. A nilpotent section would map to zero there, so it must already be zero. Therefore N is reduced. The predecessor's support classification consequently identifies N with the reduced chain as a scheme, not only set-theoretically.

## 5. Gluing algebra and curve-map normal form

Two distinct smooth curve branches with distinct tangent lines at a junction have reduced scheme-theoretic intersection there: the intersection tangent space is the intersection of their tangent lines, hence zero, and Nakayama on the local zero-dimensional intersection algebra gives the residue field C. The exceptional curves A_z,A_w are disjoint, so there is no triple intersection.

The usual exact sequence for a union of two closed subschemes, iterated across the two junctions, gives

    0 -> O_N -> O_(A_z) direct-sum O_(ell_tilde)
                       direct-sum O_(A_w)
      -> C_(p_z) direct-sum C_(p_w) -> 0,

where the last map takes the differences of values on the meeting components. Push forward by the finite map and identify each component with Q. This gives exactly the tuple algebra in the theorem.

As a module the explicit isomorphism is

    (b,d,e) |-> (b+d,b,b+e),

with b in O_Q, d in the ideal O_Q(-alpha), and e in the ideal O_Q(-beta). This proves the asserted splitting; it is a module splitting, not a product decomposition of algebras.

At alpha choose a target uniformizer s. The third component is locally separate, while the two meeting components give the completed local algebra

    {(a,b) in C[[s]]^2 : a(0)=b(0)}.

This is C[[s,u]]/(u(u-s)) via s |-> (s,s) and u |-> (s,0): every such pair is b(s)(1,1)+((a-b)/s)(s,0), and the displayed relation is exact. Setting v=s-u yields uv=0 and s=u+v. The calculation at beta is identical. In particular the double fiber s=0 agrees with Section 3, but here follows from the now-established complete curve scheme.

## 6. Exact trace-discriminant divisor of the curve cover

For a finite locally free algebra A of rank three on Q, its trace pairing is (a,b) |-> Tr(m_(ab)), where m_(ab) denotes multiplication by ab. The determinant of this pairing is a section of (det A)^(-2). Here it is generically nonzero because the generic algebra is C(Q)^3.

Off alpha,beta, the tuple description identifies A with O_Q^3, whose trace pairing has determinant one in its idempotent basis. At alpha the completed algebra is the product of the junction algebra R[u]/(u^2-su) and the separate sheet R, with R=C[[s]]. The rank-two factor has basis 1,u and trace matrix

    [ 2    s  ]
    [ s   s^2 ],

since Tr(1)=2, Tr(u)=s, and Tr(u^2)=s^2. Its determinant is s^2. The separate sheet contributes the one-by-one matrix [1], and mixed products between the two algebra factors vanish. Thus the complete rank-three trace discriminant has order exactly two at alpha. The same calculation at beta gives order exactly two there. Consequently its effective discriminant divisor is exactly

    2 alpha + 2 beta.

Its degree four also agrees with det A=O_Q(-alpha-beta) from Section 5. This is the trace discriminant of the finite flat curve cover N->Q. It is not a claim about an ambient branch divisor of Phi or the scheme structure of the singular locus of V.

## 7. Contribution and boundary

The formerly undetermined endpoint exponent is exactly two. This in turn resolves the full inverse-image curve scheme, proves finite flat degree three over every bad line in the conditional r=2 case, and supplies its explicit finite algebra, local nodal curve-map form, and exact trace-discriminant divisor. The derivation is purely structural.

No value of r is selected or excluded. The theorem does not compute the ambient singularity type of V, the scheme of its singular locus, the ambient differential-failure scheme, or the exact failure locus of the surface image. It does not resolve the separate full-adjoint, higher-lifting, or algebraicity goals. The normal form is explicitly limited to the inverse-image curve and its map to Q.
