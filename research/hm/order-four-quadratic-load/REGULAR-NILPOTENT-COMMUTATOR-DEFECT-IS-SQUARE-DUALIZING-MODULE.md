# The regular nilpotent commutator defect is the square dualizing module

Let R be a smooth local ring in characteristic zero, let (f,g) be a regular sequence, and I=(f,g). Put

    N=[[fg,-f^2],[g^2,-fg]],
    S1=[[f,0],[2g,-f]],   S2=[[g,-2f],[0,-g]].

Then

    ker(tr(N·):sl2(R)->R) / im(ad N)
      = R<S1,S2> / (f S1, g S2, g S1-f S2)
      ≅ I/(f^2,g^2)
      ≅ Ext^2_R(R/I^2,R).                              (1)

The displayed first isomorphism sends S1 to f and S2 to g. The final isomorphism includes the chosen local orientation. In particular the annihilator of (1) is exactly I^2. A first-order square-zero discrepancy is therefore not automatically an infinitesimal conjugation: the obstruction lives on the entire square thickening.

## Proof

For T=[[x,y],[z,-x]], tr(NT)=2fg x+g^2 y-f^2 z. The Hilbert–Burch resolution of the regular-sequence square gives a free basis S1,S2 for this syzygy module. This can also be checked directly: reduction modulo f gives y=f y1. Substitution and regular-sequence cancellation modulo g then give z=g z1 and x=(f z1-g y1)/2. Hence T=(z1/2)S1-(y1/2)S2. Independence follows from the two off-diagonal entries.

For H=diag(1,-1), E=E12, F=E21, direct multiplication gives

    [N,H]=g S1-f S2,
    [N,E]=-g S2,
    [N,F]=-f S1.

These are all commutators because H,E,F form a basis of sl2. The map R^2->I/(f^2,g^2), (u,v)->u f+v g, has precisely the three stated relations. Indeed if u f+v g=a f^2+b g^2, regular-sequence syzygies give u-a f=c g and v-b g=-c f.

Dualize the Hilbert–Burch resolution with syzygy columns (f,0,2g) and (g,-2f,0). The resulting Ext^2 has relations f e1+g e2, f e2, g e1. Substitution e1=S2,e2=-S1 gives exactly (1). Equivalently this is the usual complete-intersection linkage description by (f^2,g^2).

The annihilator is ((f^2,g^2):I)=I^2. The inclusion I^2⊂ann is direct; the reverse follows from (f^2,g^2):f=(f,g^2), (f^2,g^2):g=(f^2,g), and the regular-sequence intersection identity.

## Change of generators and scope

For g'=g+p f and P=[[1,0],[p,1]],

    N'=P N P^(-1),
    S1'=P S1 P^(-1),
    S2'=P(S2-p S1)P^(-1).

Thus the presentation I/(f^2,g^2) must NOT be transported by merely replacing g with g'. Its denominator ideal changes. The intrinsic commutator quotient, or equivalently its dualizing-module description with the appropriate line factors, is what glues. In the global HM geometry the determinant, spinor and normal-equation twists still require explicit comparison; (1) alone does not identify a global normal bundle or compute its secondary obstruction.

For a homogeneous binary (3,5) complete intersection, its transverse Hilbert series in the displayed quotient presentation is

    (t^3+t^5-t^6-t^8-t^10+t^16)/(1-t)^2.

Its length is45, its degree4 piece has dimension2, and its degree8 piece has dimension6. In particular a nonzero linear L gives a nongauge class L S1, since L f has degree4 whereas (f^2,g^2) starts in degree6. This explains the specific residue in UNIVERSAL-QUINTIC-GENERATOR-HESSIAN-COVARIANCE.md by an exact obstruction module, rather than a degree heuristic alone.

Run verify_regular_nilpotent_commutator_defect.py. It checks universal matrix identities and Hilbert bookkeeping only; it uses no actual HM coefficients or map ranks.
