# Canonical cusp components are finite cubic ruled images

Use the canonical ruling bundle V on the smooth modular surface S(5), with V globally generated, det V=I+3F, and corrected fixed-coordinate polarization h=ξ+I on P_S(V). The global fixed-coordinate morphism is base-point-free by the source bilinear morphism and its Veronese factorization. This note concerns that canonical family, independently of identifying the actual cusp determinantal nets.

Each modular cusp fiber is a reduced I5 pentagon. Its five components D are smooth rational curves. The 25 torsion sections meet each component in five distinct smooth points, by translation transitivity on the five components. Since their sum is C_S=5I, one has

    I.D=1,    F.D=0.

Therefore V|D is a globally generated rank-two bundle on P1 of degree one. By splitting on P1 it is O directsum O(1). The corresponding ruling component R_D=P_D(V|D) is F1. If C0 is its negative section and f its ruling fiber, then

    ξ|R_D=C0+f,
    h|R_D=C0+2f.

In particular h is ample on every component, with h²=3 and h.K_R_D=-5. The canonical fixed-coordinate map contracts no curve on a cusp component. The full map from the ruling family to (modular parameter, fixed ambient point) is consequently finite: it is proper, and its fibers inside any smooth scroll or cusp component are zero-dimensional. This does not say that each cubic ruled image is embedded, nor that distinct components have disjoint images.

For a general source quadric, its pullback on each R_D is a smooth connected curve G_D in |2h|. Its genus is

    2g(G_D)-2=(2h).(2h+K_R_D)=12-10=2,
    g(G_D)=2.

The global double cover W->S is unramified over the finitely many nodes of all twelve pentagons for general Q: over each node, the corresponding ruling line has two distinct quadric roots. Thus over each cusp, the five genus-two components meet transversely in two points for each adjacent pair, with no other intersections. Their dual graph has five vertices and ten edges, so its arithmetic genus is

    5*2+(10-5+1)=16,

matching the smooth normalized fibers. This is a semistable fiber description of the CANONICAL double cover, not a statement that the raw evaluation inverse image has already been normalized or resolved correctly at the cusp.

Identifying the entire raw special evaluation net would additionally require its scheme structure and any extra vertical components. COMPACT-DOMINATING-NORMALIZATION.md avoids that stronger requirement: componentwise finiteness and the unit-component incidence identity suffice for the normalization of the component dominating Gamma. No equality with the entire raw special net is asserted here.
