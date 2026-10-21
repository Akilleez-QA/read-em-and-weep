# Conductor, cohomology and dualizing defect of the primary surface

Status: authored structural derivation, independently mathematically reviewed in REVIEW.md; not formally checked. Work over C. No selected actual HM/source instance is evaluated.

## 1. Exact dependencies and scope

The primary scheme is D=D9(e) for e:3Q(-1)→10O on P4. PR573, commit **6c2dbd48edea0577acf063a60e1edbbbe92ced5c**, proves the global equality D=S with the exact coordinate-copy BHM surface S15, including equality of ideal sheaves, not merely equality of supports. Its geometric dictionary is PR570, commit **e5e55594ef2b99cefb81c4c02b22cb45e1ff0025**.

Let ν:X=S(5)→S be the finite normalization and H=ν*O_S(1). The input geometry is:

- X is a smooth connected projective elliptic surface over P1, H=I+2F, H²=15 and K_X=3F, so H.K_X=15.
- S is smooth off a reduced set Z of thirty points. Each point identifies two distinct smooth points of X, and the two image surface branches have transverse tangent planes in smooth P4.
- Accordingly the completed local ring at p∈Z is
  A=C[[u1,u2,v1,v2]]/(u_i v_j:1≤i,j≤2)
   =C[[u1,u2]] ×_C C[[v1,v2]].

The source is Barth–Hulek–Moore, “Shioda's Modular Surface S(5) and the Horrocks–Mumford Bundle,” Section 4.3, printed p58 (explicitly χ(O_X)=5, K_X=3F, pg(X)=4 and q(X)=0), and Section 4.5, Propositions 9–10, printed pp63–64 (degree15, sixty source points paired to thirty image double points, and transversality).

Public source: https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

All statements here concern this primary surface D=S. They do not concern the distinct quadratic-parameter eightfold, fixed-beta surfaces, or the actual middle connecting map δ. They imply no original-target lift or algebraicity result.

## 2. Normalization quotient and conductor

Write B1=C[[u1,u2]], B2=C[[v1,v2]], with maximal ideals m1,m2. The normalization of A is B=B1⊕B2. There is an exact sequence of A-modules

0 → A → B → C → 0,                         (1)

where the last map is (f,g)↦f(0)−g(0). Indeed, equality of the two residues is precisely the defining condition of the fiber product. Its cokernel has length one, not two or four. Relabeling the two branches changes the displayed quotient coordinate by a sign and has no effect on its length or subsequent statements.

The conductor is

Ann_A(B/A)=m1⊕m2=m_A.                       (2)

For if an element has common residue c, its action on B/A is multiplication by c. Thus it annihilates B/A exactly when c=0. As an ideal of B, this is again m1⊕m2. Faithful flatness of completion and finiteness of normalization transfer these calculations to the algebraic stalks. Away from Z normalization is an isomorphism.

Consequently there is a global exact sequence

0 → O_S → ν_*O_X → T → 0,                  (3)

where T is an O_Z-module whose fiber at each of the thirty points has dimension one; in particular T is isomorphic, noncanonically, to ⊕_{p∈Z} k(p). The conductor ideal is exactly I_{Z/S}, not a thickening of Z.

Let W=ν^{-1}(Z)_red, the reduced set of sixty source points. Equation (2) also proves the equality of subsheaves of ν_*O_X

I_{Z/S}=ν_*I_{W/X}.                         (4)

Here W is a codimension-two subscheme of a smooth surface, not an effective Cartier divisor. In particular I_{W/X} must not be treated as an invertible O_X(-W).

## 3. Structure-sheaf invariants and Hilbert polynomial

Finite ν has no higher direct images on coherent sheaves, so H^i(S,ν_*O_X)=H^i(X,O_X). Both S and X are integral proper connected schemes over C; their global functions are C and pullback identifies the constants. The cohomology sequence of (3), using q(X)=0 and pg(X)=4, is therefore

H^0(O_S)=C,
H^1(O_S)≅H^0(T),     dim H^1(O_S)=30,
H^2(O_S)≅H^2(O_X),   dim H^2(O_S)=4.        (5)

Thus χ(O_S)=−25 and the arithmetic genus χ(O_S)−1 is −26. We use h²(O_S)=4 rather than silently applying a smooth-surface definition of geometric genus to this nonnormal surface.

Twist (3) by O_S(n). Projection formula gives

0 → O_S(n) → ν_*O_X(nH) → T(n) → 0,        (6)

and T(n) has length thirty for every integer n. Smooth surface Riemann–Roch on X gives

χ(O_X(nH))=χ(O_X)+(n²H²−nH.K_X)/2
          =5+(15/2)n(n−1).

Therefore the Hilbert polynomial, with equality to Euler characteristic for every integer n, is

P_S(n)=χ(O_S(n))=(15/2)n(n−1)−25.           (7)

This is a polynomial of integer values, since n(n−1) is even. It records degree15 and sectional arithmetic genus16. More explicitly, a general hyperplane avoids Z and is smooth on the smooth locus by Bertini. Its inverse image is a general member of the pulled-back hyperplane subsystem of |H| on X; ν is an isomorphism there. It is connected: H¹(O_X(-H))=0 by smooth Serre duality and Kodaira vanishing, and the divisor exact sequence identifies its global functions with C. Adjunction on X gives

2g−2=H.(H+K_X)=30, hence g=16.

Alternatively the exact hyperplane sequence yields P_C(n)=P_S(n)−P_S(n−1)=15n−15. Adjunction was applied on X, not on the non-Cohen–Macaulay surface S.

There is also an exact positive-twist calculation. BHM, the beginning of Section 4.5 on printed p63, identifies H⁰(X,H)=V* of dimension five: the actual coordinate map uses this complete system, as transferred by PR570. These five coordinate sections all descend to S, so the map H⁰(X,H)→H⁰(T(1)) in (6) is zero. Moreover H²(X,H)=H⁰(X,K_X−H)=0: an effective divisor of class K_X−H would have intersection −5 with the nef fiber class F. Riemann–Roch gives χ(O_X(H))=5, hence H¹(X,H)=0. The same exact sequence yields

(h⁰(O_S(1)),h¹(O_S(1)),h²(O_S(1)))=(5,30,0). (7a)

## 4. A persistent negative-twist deficiency

This is a further consequence, not just the value at n=0. The line bundle H is ample: it is the pullback of O_S(1) under a finite morphism. For n<0, H^0(X,O_X(nH))=0 by ampleness. Serre duality on the smooth X and Kodaira vanishing applied to K_X+(-n)H give H^1(X,O_X(nH))=0. Hence (6) yields

H^1(S,O_S(n))≅H^0(T(n)),  h^1(O_S(n))=30  for every n<0.

Together with (5), this holds in dimension for all n≤0. Also for n<0,

h²(O_S(n))=h²(O_X(nH))=5+(15/2)n(n−1).      (8)

If I_S denotes the ideal sheaf in P4, projective-space intermediate-cohomology vanishing and 0→I_S(n)→O_P4(n)→O_S(n)→0 imply

h²(P4,I_S(n))=30 for all n≤0.              (9)

Thus the thirty-point non-Cohen–Macaulay defect survives every negative twist. This excludes an ACM model for the primary surface structurally and independently of any selected coefficient or rank calculation.

## 5. Canonical sheaf and the additional dualizing-complex term

Let i:S↪P4, Ω=ω_P4=O_P4(-5), and regard the sheaves in (3) as ambient coherent sheaves. Set B=ν_*O_X. At a node, after completion B is the direct sum of the two regular codimension-two branch rings. Each has a length-two Koszul resolution over the regular four-dimensional ambient ring. Away from the nodes, the same statement is the usual smooth codimension-two local calculation. Therefore B is a Cohen–Macaulay ambient module of codimension two, even though O_S is not, and

Ext^j_P4(B,Ω)=0 for j≠2,
Ext²_P4(B,Ω)=ν_*ω_X.                       (10)

The second equality is finite duality, or equivalently the local canonical-module calculation for the two branches, glued by the canonical sheaf of smooth X. At a node the first statement follows directly by resolving each branch ideal, generated by two regular parameters; no Cohen–Macaulay assertion about S is used.

The finite-length sheaf T has only one nonzero ambient sheaf Ext:

Ext^j_P4(T,Ω)=0 for j≠4,
T^D:=Ext⁴_P4(T,Ω),  length(T^D)=30.         (11)

This is also the four-parameter Koszul calculation; T^D is the zero-dimensional dualizing dual of T. Each stalk is one-dimensional over k(p). Applying sheaf Hom(-,Ω) to (3) and using (10)–(11) gives

ω_S:=Ext²_P4(O_S,Ω)≅ν_*ω_X,
Ext³_P4(O_S,Ω)≅T^D,
Ext^j_P4(O_S,Ω)=0 for j≠2,3.              (12)

Equivalently the dualizing complex R Hom_P4(O_S,Ω)[4] has precisely

H^(-2)=ν_*ω_X,       H^(-1)=T^D.           (13)

It is not the single shifted sheaf ω_S[2]. No splitting of this two-term complex is claimed.

The canonical sheaf is not invertible at a node: its completed module is B1⊕B2 with canonical-form generators on the two branches. Modulo the maximal ideal of A it has two independent generators, whereas an invertible A-module has one. It does have h^0(ω_S)=4, h^1(ω_S)=0 and h^2(ω_S)=1, because ν is finite and these are the corresponding smooth-X canonical cohomology groups. In particular h^1(ω_S)=0 does not dualize h^1(O_S)=30. The missing contribution is exactly the length-thirty term H^(-1) in (13).

This isolates the root cause of failed naive canonical-sheaf duality or smooth-surface adjunction: S is depth one at Z, and its dualizing object has an additional cohomology sheaf. It is not legitimate to infer an invertible canonical bundle on S, a Cartier canonical divisor, or ordinary surface Serre duality from the formula ω_S=ν_*ω_X.

## 6. Verification boundary and contribution

The only source-specific inputs are the pinned scheme equality and BHM's explicitly stated smooth normalization invariants and transverse double-point description. The quotient length, conductor, all Euler characteristics, the negative-twist obstruction and the two Ext sheaves are derived here. The local assertions can be checked independently by the two-branch fiber product and its two branch Koszul resolutions; the global assertions follow by exact sequences, smooth-surface Riemann–Roch, and smooth-X duality/vanishing.

This advances the primary-scheme lane from geometric identification to its exact global numerical and dualizing defect. It supplies a fixed Hilbert polynomial and persistent cohomological obstruction against purported locally CM/ACM replacements. It neither evaluates nor proves nonvanishing of the separate actual connecting determinant δ, and supplies no higher-order lift or algebraicity certificate.
