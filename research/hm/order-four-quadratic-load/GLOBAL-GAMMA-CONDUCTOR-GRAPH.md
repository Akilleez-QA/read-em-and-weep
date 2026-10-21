# Exact doubled-graph conductor of the Gamma inverse image

## Inputs and scope

Let S=f^{-1}(Gamma) in the resolved evaluation fourfold. The theorem UNIFORM-FLAT-EVALUATION-FIBRATION.md proves that S is integral and locally complete intersection, hence Gorenstein, and that its finite normalization is nu:Wtilde=Bl_{50}(W) -> S. This is not a claim that every fixed beta determinantal scroll is Gorenstein at its rank-zero points. Those points were removed in the fixed-fiber conductor proof, and general quadric sections avoid them.

Write b:Wtilde -> W, pi:W -> S(5), H=I+2F on S(5), h=xi+I for the fixed w-hyperplane on the ruling family, and F_i for the fifty blowup exceptional curves. All genericity conditions below are finite-type open restrictions on the already general ambient quadric Q.

## 1. The actual graph divisor

ADHPR, Remark4.9 and Proposition4.19, https://arxiv.org/pdf/alg-geom/9606013, give cubic vectors v+,v- with mu v+ - lambda v-=0 on S(5). Thus (v+,v-)=(lambda u,mu u) for a section u of K(3H-F), where K=V* is the rank-two ruling subbundle of the constant five-space. Membership in K holds on the dense smooth modular locus by the source incidence statement and therefore everywhere by regularity. Remark4.9(i) identifies the simultaneous zero locus with the finitely many singular points of the degree-fifteen model; its preimage in the finite modular normalization is finite. Hence u has no divisorial zeros.

On P(V), wedge the universal line O(-xi) in K with u. The resulting section has line-bundle class

    xi + (3H-F) + det K = xi +2H-2F = h+H.

Its zero divisor is precisely the closure J_P of the graph section. Over a zero of u the entire projective-line fiber is included, but these are curves, not additional divisor components. Therefore J_P is an irreducible effective Cartier divisor of the stated exact class, with no extra vertical divisorial component.

Put J_W=J_P intersect W. A general Q contains no image of any smooth modular graph fiber: these form a one-parameter family of integral curves, each imposing at least three independent quadratic conditions, so the bad incidence has dimension at most twelve in P14. (For the elliptic normal quintics the sharper bound is five.) This excludes horizontal-family graph fibers uniformly, not just the cusps. Over each of the finitely many cusp parameters J_P has only finitely many curve components. A general Q contains the image of none of these curves (and avoids any point images), so J_W has no vertical curve component. This assertion uses the globally defined basepoint-free w-map, not the rational first-row presentation.

## 2. The fifty marked points and strict transform

Let D_i be a lifted torsion section in W. The w-map is constant on D_i, equal to one root of Q intersect the corresponding fixed HM line. Consequently h.D_i=0, while pi*H.D_i=1. Thus J_W.D_i=1.

The marked-point dictionary in SMOOTH-MODULAR-EVALUATION-BLOWUP.md identifies P_i with the graph point on D_i: at the origin, the graph map of Proposition4.19 sends the origin to the origin, the ruling maps isomorphically to the fixed HM line, and its modular parameter equals kappa(z_i). Heisenberg translation gives all twenty-five lines. Since D_i is not contained in J_W and the total intersection is one, the local intersection at P_i is one. In particular J_W has multiplicity one at P_i. Therefore its strict transform J on Wtilde satisfies the exact linear equivalence

    J = b*(h+pi*H) - sum F_i.

J has no vertical components; it does not include the new exceptional curves F_i.

## 3. Canonical conductor calculation

Adjunction for Gamma in P3 gives det N_Gamma/P3=O_P1(22), because Gamma is a rational sextic. Combining this with the proved tautological identities on Wtilde gives

    nu*K_S = b*(pi*(5I+10F)+2h) - sum F_i,
    K_Wtilde = b*pi*(3H) + sum F_i.

Hence the conductor ideal on the smooth normalization, identified by finite Gorenstein duality, is invertible and has effective divisor Delta linearly equivalent to

    nu*K_S-K_Wtilde = 2[b*(h+pi*H)-sum F_i] = 2J.

The generic modular fiber is exactly the fixed-scroll curve analyzed in FIXED-BETA-SCROLL-CONDUCTOR-DESCENT.md. There its conductor is twice the graph intersection. Thus each horizontal component of Delta is the corresponding component of 2J with the same multiplicity. Since J has no vertical components, Delta-2J is an effective vertical divisor. It is linearly trivial by the canonical calculation. An effective nonzero divisor on a projective smooth surface has positive intersection with an ample divisor; therefore Delta-2J=0.

The exact global conductor ideal is consequently

    Hom_S(nu_*O_Wtilde,O_S) = O_Wtilde(-2J).

This is equality of the conductor ideal divisor, not just numerical equivalence. It does not assert that the conductor image has no special cusp behavior or that all its points have the same four-branch local model. On the open smooth modular locus its transverse local gluing is the four-branch first-jet model already proved.

## 4. Numerical consistency and the remaining condition

The existing intersection calculations give J^2=160 and J.K_Wtilde=320, hence p_a(J)=241 and chi(O_{2J})=-640. The normalization quotient on S has Euler characteristic -310 because chi(O_Wtilde)=55 and chi(O_S)=365. These are different sheaves and must not be identified.

The result determines the actual global conductor subscheme upstairs. Descending a candidate eigenline section still requires membership in the actual image of the structure sheaf of S modulo this conductor, with the appropriate line-bundle trivializations. Its existence does not prove that the twenty-dimensional adjoint boundary has a kernel, nor does the conductor computation imply vanishing. No selected instance computations or external writes occur here.
