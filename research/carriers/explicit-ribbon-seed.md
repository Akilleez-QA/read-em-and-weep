# An explicit stable rank-two field-2 monad on P1 × P3

This is a concrete algebraic bundle, not just a Chern-character prescription. The specific simplest member below has not been identified with the bundle obtained from an abelian surface in Lange's paper. Nevertheless, its local freeness, stability, determinant, Chern classes, and ribbon Serre sequence are proved explicitly, so it is an independent seed with the required numerical invariants.

## Coordinates and the finite global monad

Let P=P1_[s:t] × P3_[x0:x1:x2:x3], with u,v the hyperplane classes. On U_s put z=t/s and on U_t put w=s/t. On their overlap w=z^(-1). Define

- a_s=(z x0−x2, z x1−x3)^T,
- h_s=(−x0^3,−x1^3)^T,
- a_t=(x0−w x2, x1−w x3)^T=a_s/z,
- h_t=(−x2^3,−x3^3)^T.

On each base chart take the monad

O_P3(−2) --α--> O_P3(−1)^2 ⊕ O_P3(1)^2 --β--> O_P3(2),

where α=(a,h)^T and β=(−h^T,a^T). Thus β α=0 identically. Define

S0=z^2 x0^2+z x0 x2+x2^2,
S1=z^2 x1^2+z x1 x3+x3^2,
D=−z^2 diag(S0,S1).

The gluing maps send t-chart coordinate vectors to s-chart coordinate vectors. For the untwisted cohomology bundle G they are

T_A=z^4,
T_B=[[z^5 I2,0],[D,z I2]],
T_C=z^2.

The precise identities are

T_B α_t=α_s T_A,     β_s T_B=T_C β_t.

Indeed D a_s=z^5 h_s−z^2 h_t, and D is symmetric. These identities give a global monad

O_P(4,−2) → B → O_P(2,2),

where B is the explicitly specified extension

0→O_P(1,1)^2→B→O_P(5,−1)^2→0.

Set F=G(−3,0). Equivalently, the monad for F is

O_P(1,−2) → B_F → O_P(−1,2),

with

0→O_P(−2,1)^2→B_F→O_P(2,−1)^2→0,

and transitions obtained by multiplying T_A,T_B,T_C by z^(−3). Thus they are z, [[z^2 I2,0],[−z^(−1)diag(S0,S1),z^(−2)I2]], and z^(−1).

These are finite algebraic transition data for all terms and all differentials. Pulling them back along the chosen map from C^4 gives a literal monad model for the bundle on the abelian fourfold.

## Local freeness

On U_s, if a_s=0 and h_s=0, then x0=x1=0, and then a_s=0 forces x2=x3=0, impossible in P3. Consequently α_s is a subbundle injection and β_s is a bundle surjection. The identical argument on U_t applies. Their middle cohomology G, and hence F, is therefore locally free of rank two.

The matrices also preserve the standard alternating form up to z^6: T_B^T J4 T_B=z^6 J4, since D is symmetric. After twisting by O(−3,0), the alternating form is globally untwisted.

## Actual ribbon and Serre section

The local vectors σ=(0,0,−a2,a1)^T lie in ker β. They satisfy T_B σ_t=σ_s, so give a global section σ of G=F(3,0).

Its zero ideal is the ideal of the 2×2 minors of the two columns [α,σ]. Since α is everywhere unimodular locally, this is exactly the zero ideal of the induced section of the rank-two cohomology bundle. It equals

I_Y=(a1^2,a1 a2,a2^2,x0^3 a1+x1^3 a2) on U_s,

and the analogous ideal using x2,x3 on U_t. The support is

Z={t x0−s x2=t x1−s x3=0} ≅ P1×P1,

parametrized by ([s:t],[p:q])↦([s:t],[sp:sq:tp:tq]). Its conormal bundle is O_Z(−2,−1)^2 in intrinsic Z coordinates. The quotient defining Y is

N*_(Z/P) → L=O_Z(−2,2),    (a1,a2)↦(−q^3,p^3) ε.

The cubics have no common zero. The ribbon is locally a codimension-two complete intersection: where one cubic is a unit its ideal can be written (linear relation, remaining normal coordinate squared). Thus σ is regular, and the actual sequence is

0→O_P→G→I_Y(6,0)→0,

or

0→O_P(−3,0)→F→I_Y(3,0)→0.

In particular adjunction gives ω_Y=O_P(4,−4)|Y, with no unsupported assumption about arbitrary cubic pairs.

## Stability and numerical invariants

For H=O_P(1,1), the slope of O_P(a,b) is a+3b, and μ_H(F)=0. If a line subsheaf O_P(a,b) destabilizes, then a+3b≥0. Its map to the left term O_P(−3,0) of the Serre sequence must vanish, so there is a nonzero section of I_Y(3−a,−b). In particular a≤3 and b≤0. For b≤−2 the slope inequality is impossible. For b=−1 it forces a=3, but H0(I_Y(0,1))=0 because Z projects onto a nondegenerate quadric in P3. For b=0, H0(I_Y(c,0))=0 because Y dominates P1. This excludes all destabilizing line subsheaves. Rank-one torsion-free subsheaves reduce to their double duals on the smooth ambient variety. Thus F is H-stable.

The exact K-class is

[F]=2[O(2,−1)]+2[O(−2,1)]−[O(1,−2)]−[O(−1,2)].

Consequently rank F=2, det F=O, c2(F)=4uv+2v^2=2(u+v)^2. Its Chern character is 2−4uv−2v^2+(4/3)uv^3. V=F(1,2) has c1=2u+4v and c2=8uv+6v^2, the same as Lange's V.

## Explicit five-parameter Serre-extension variation

Let j=J a_s=(−a2,a1)^T. Replacing D by

D_k=D+k(z) j j^T

for any polynomial k(z) of degree at most four gives another valid global monad: D_k is symmetric, D_k a_s=D a_s, and a_s^T D_k=a_s^T D. Local α and β, the ribbon, the regular section, and the stability proof remain unchanged. Thus this gives a concrete five-parameter set of extensions, consistent with h1(O_P(−6,0))=5. No assertion that these parameters give an injective or exhaustive moduli chart is needed here.

The verifier also reports global-section ranks for selected k values. Those extra ranks are not used in the existence or stability proof. The construction is not identified here with Lange's original abelian-surface family. It gives a directly checkable stable bundle with the same normalized Chern classes. The mixed Atiyah class remains uncomputed.

Background source: H. Lange, A Vector Bundle of Rank 2 on P1 × P3, sections 3 and 5, https://arxiv.org/pdf/alg-geom/9506021 . The construction and verification above are independent calculations rather than a formula quoted from that paper.

## Abelian pullback and remaining test
Let C be an elliptic curve with degree-two map x:C→P1 and put X=C4. The finite degree-96 map f=(x,Sym3∘x3) pulls O(1,1) back to twice the product principal polarization theta. Because P1×P3 has trivial etale fundamental group, the finite stable-pullback theorem applies: f*F is stable, has determinant O, and c2=8theta². See [Biswas–Das–Parameswaran, Theorem2.5](https://arxiv.org/html/2203.03246).

The rank-two scalar-curvature and relative product-family arguments from PR21 apply to this explicit seed as well. Thirteen of the sixteen character-annihilating first-order directions evaluate to zero. The three mixed directions are permuted by S3 and have distinct deck characters, so one representative determines their rank0-or3 alternative. None of these actual mixed Ext² classes is evaluated by the monad verifier.

Run `python research/carriers/verify_hamiltonian_ribbon_monad.py` with Python3 and SymPy. Exact assertions check chain gluing, the section, the alternating pairing, its zero ideal, and the K-character. Local freeness and stability use the accompanying proof.
