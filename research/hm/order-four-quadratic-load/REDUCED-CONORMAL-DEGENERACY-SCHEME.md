# The conormal degeneracy scheme is the reduced conic and six reduced points

## Statement

In the setting of PROJECTED-VERONESE-QUADRICS-AND-CONORMAL-DEFECT.md, let theta be the conormal differential of the actual three quadratic equations of T. Its determinantal rank-drop scheme on R=P2 is exactly

    D_2(theta) = C0 disjoint-union Z6,

with both the invariant conic C0=(q0=0) and the six-point axis scheme reduced. Thus the previously established equality of supports upgrades to an equality of schemes. This is not a finite degeneracy scheme.

## Proof

Use the intrinsic bilinear notation from the scaffold theorem:

    Q(x,y)=M(x)y=N(y)x,
    Phi(p)=[q0(p)p:g(p)].

The Jacobian restricted to the parametrized surface is

    J(p)=[ N(g(p)) | q0(p) M(p) ].                    (1)

Its maximal minors generate the determinantal ideal of theta. Indeed the Euler relation places these differentials in the projective cotangent bundle, and their vanishing along T places them in its conormal subbundle. Both inclusions of vector bundles are locally split, so passing between the affine-coordinate Jacobian, the projective cotangent bundle, and the conormal bundle does not change the ideal of maximal minors.

The scaffold theorem proves:

- The maximal minors of M generate I_Z6. Its rank is three outside Z6 and two at each point of Z6.
- The four cubics g map the blowup of Z6 to the smooth cubic S=(det N=0). In particular N(g(p)) has rank two whenever g(p) is nonzero.
- The conic C0 avoids Z6.

Also

    det N(g(p))=0                                    (2)

identically on R. This follows either from the cubic surface or directly from N(g(p))p=M(p)g(p)=0.

Fix p in C0. The all-N maximal minor in (1) is zero by (2), and every other maximal minor has a factor q0. Hence the determinantal ideal is contained in (q0). At p, two columns of N(g(p)) are independent. Since M(p) has rank three, one of its columns is outside their span. The corresponding mixed maximal minor of (1) is q0 times a unit in the local ring. Therefore the determinantal ideal is exactly (q0) near p. In particular there is no thickening of the conic and no embedded component along it.

Now fix p in Z6. Here q0 is a unit. The maximal minors drawn from the M-block in (1) generate I_Z6 locally, which is the reduced point ideal m_p. Conversely all maximal minors vanish at p: g(p)=0 makes the N-block zero, and M(p) has rank two. Thus the determinantal ideal is contained in m_p and contains m_p, so it equals m_p.

Away from C0 union Z6, the M-block is q0 times a rank-three matrix, so its maximal minors generate the unit ideal. These local descriptions prove the asserted global equality of schemes.

Because the quadratic net is a regular sequence, the same scheme is the singular scheme of its complete-intersection threefold restricted to T. This statement does not describe the entire singular scheme away from T and does not identify the virtual Chern number 24 with a scheme length. No selected coefficients, actual rank evaluations, scans, or experiments are used.
