# An explicit algebraic monad with a smooth abelian-surface section

This strengthens the concrete stable ribbon seed in [the stable ribbon seed in PR23](https://github.com/Akilleez-QA/read-em-and-weep/pull/23): the member specified here has a verified smooth connected abelian surface as the zero locus of a section of V=F(1,2). Consequently its Serre bundle is an actual member of the construction in Lange's paper, not merely a stable bundle with the same Chern classes.

The proof includes a complete modular Groebner certificate and a proper-specialization argument. It does not assert that a single affine computation, or a matrix rank modulo a prime, suffices to prove smoothness in characteristic zero.

## 1. Monad and gluing

Write A=(x0,x1)^T, B=(x2,x3)^T, z=t/s, a=zA−B and j=Ja=(−a2,a1)^T. Put

H(u,v)=(u^4+4u^2v^2+v^4)/4,
h(u,v)=−grad H=(−u^3−2uv^2,−v^3−2u^2v)^T,
k(z)=1+(2/3)z^2+z^4.

Let

K(z,A,B)=integral from 0 to 1 of Dh(B+τ(zA−B)) dτ,
D=z^2 K+k(z)j j^T.

This integral is simply a polynomial prescription over Q: expand the quadratic Hessian and integrate its coefficients. K is symmetric and

K a=h(zA)−h(B)=z^3h(A)−h(B).

On U_s, use α_s=(a,h(A))^T, β_s=(−h(A)^T,a^T). On U_t, use α_t=(a/z,h(B))^T, β_t=(−h(B)^T,(a/z)^T). The local monad is O_P3(−2)→O_P3(−1)^2⊕O_P3(1)^2→O_P3(2), with transitions

T_A=z^4,
T_B=[[z^5 I2,0],[D,z I2]],
T_C=z^2.

Then T_Bα_t=z^4α_s and β_sT_B=z^2β_t. The cohomology is G, and F=G(−3,0), V=G(−2,2). The cubic gradient has no common projective zero: if u and v are both nonzero, the two equations would imply u^2=−2v^2 and v^2=−2u^2, hence 3u^2=0. Thus the monad is locally free over characteristic zero and over Z[1/6].

The section σ=(0,Ja) of G gives precisely the regular Hamiltonian ribbon on the Segre graph. Hence the same Serre sequence, stability proof, and K-class as the simpler model apply:

0→O(−3,0)→F→I_Y(3,0)→0,

det F=O, c2(F)=4uv+2v^2, and F is O(1,1)-stable.

## 2. A second explicit section, now of V

On U_s use the shear coordinates

A=x0, C=x1, p=zx0−x2, q=zx1−x3.

Set h1=−A^3−2AC^2 and h2=−C^3−2A^2C. Define

M_s=[[z,1−z^2],[1−z^2,0]],
T_s=z(q^2−p^2−A^2+C^2)−pq+pA−qC−2AC.

A section W_s of the middle term of the V monad is

W_s=(M_s(p,q)^T, M_s(h1,h2)^T+T_s(−q,p)^T)^T.

On U_t, write w=s/t and use A=x2, C=x3, p=x0−wx2, q=x1−wx3. The formula is

M_t=[[w,w^2−1],[w^2−1,0]],
T_t=w(q^2−p^2−A^2+C^2)+pq−pA+qC+2AC,
W_t=(M_t(p,q)^T,M_t(h1,h2)^T+T_t(−q,p)^T)^T.

The verifier checks βW=0 and W_s=z^(−2)T_B W_t exactly. Thus W determines an actual global section of V. Let X be its zero scheme.

## 3. Spectral description of X

The matrix M is nowhere scalar, including at infinity. Its eigenline curve B is the bidegree-(2,2) curve in P1_base×P1_eigenline with finite-chart equation

(1−z^2)(1−r^2)−zr=0.

Its double cover of P1_base has discriminant

4z^4−7z^2+4.

This quartic is squarefree over Q and F_101. Hence B is a smooth connected genus-one curve. The t-chart has off-diagonal w^2−1, giving the same global curve.

Over a point of B choose an eigenline. The linear condition that a lie in that eigenline cuts a projective plane out of P3. These planes form a P2 bundle over B: they are the projectivizations of the rank-three preimage bundles under the everywhere-surjective map (A,B)↦tA−sB. This construction is projective over Z[1/30].

The zero scheme X is isomorphic to a relative plane cubic in this P2 bundle. Here are all its chart equations. Let b denote z or w, and let e=+1 on U_s and e=−1 on U_t. Put

o=e(1−b^2),
T=b(q^2−p^2−A^2+C^2)+e(−pq+pA−qC−2AC).

In the finite eigenline chart, substitute (p,q)=(p,rp), impose

Q=o(1−r^2)−br=0,
λ=b+or,
F_cubic=o h1−λ h2+pT=0.

In the reciprocal eigenline chart, substitute (p,q)=(rp,p), impose

Q=o(r^2−1)−br=0,
λ=or,
F_cubic=(b−λ)h1+o h2−pT=0.

The projective-plane coordinates are [A:C:p].

To see the scheme-theoretic identification, on a monad trivialization the condition that W vanish in cohomology is W=λ α, since α is a subbundle injection. Its equations are

(M−λI)a=0,
(M−λI)h+TJ a=0.

The identity adj(M−λI)J=J(M−λI), together with the two equations, implies det(M−λI)a=det(M−λI)h=0. Since the components of (a,h) generate the unit ideal locally, det(M−λI)=0 scheme-theoretically. Since M is nowhere scalar, its eigenspace is a line subbundle on the spectral curve. This recovers the spectral eigenline, including at a=0 and at branch points. On the two eigenline charts one nonzero row of M−λI gives exactly the displayed cubic; the other row is dependent. Conversely the cubic and eigenline equations imply W=λα. Thus no component or nilpotent structure was discarded in passing to the spectral description.

## 4. Complete smoothness certificate

For each of the two base charts and each of the two eigenline charts, take all three plane charts p=1, A=1 and C=1. For each of these 12 charts the script computes the Groebner basis over F_101 of

(Q, ∂F_cubic/∂A, ∂F_cubic/∂C, ∂F_cubic/∂p),

with the indicated plane coordinate set to 1. Every one of the 12 Groebner bases is (1). By Euler's formula (101 does not divide 3), F_cubic vanishes automatically at a common zero of its three homogeneous partial derivatives, so this is the full singular-fiber condition. The 12 charts cover the complete projective family, not merely a dense affine subset. Thus every geometric plane-cubic fiber in characteristic 101 is smooth.

The same plane bundle, cubic divisor and relative singular locus are defined over R=Z[1/30]. The relative singular locus is closed in a projective R-scheme and is therefore proper over Spec R. If its generic fiber were nonempty, its proper image in Spec R would be a closed set containing the generic point, hence all of Spec R. That would force a point over 101, contrary to the complete certificate. Consequently the characteristic-zero relative singular locus is empty.

Therefore X→B is a family of smooth plane cubics. It is smooth and surjective with geometrically connected fibers; since B is smooth and connected, X is a smooth connected projective surface. In particular W is a regular codimension-two section.

## 5. Identification as an abelian surface and as a Lange bundle

Since det V=O_P(2,4)=ω_P^(−1), adjunction gives ω_X=O_X. The map X→B implies q(X)≥1. By the classification of smooth projective complex surfaces with trivial canonical bundle, X is an abelian surface rather than a K3 surface. Equivalently one may combine the Serre sequence and its numerical Euler characteristic with the Albanese classification in this case.

Lange's paper constructs its V by the Serre correspondence from an embedded abelian surface X⊂P1×P3 with this determinant. Our actual section gives

0→O_P→V→I_X(2,4)→0.

Thus this monad provides explicit parameters and transition data for a bundle in that same abelian-surface Serre construction. No claim that every Lange bundle is covered by these parameters is required or proved.

## 6. A nonempty open net of abelian sections

For this specific V, h0(V)=3. Indeed, after twisting the monad by (−2,2), its middle bundle B_V fits into

0→O(−1,3)^2→B_V→O(3,1)^2→0.

The left term has no cohomology, so H0(B_V) has dimension 32. The target is O(0,4), with 35 global sections. The exact polynomial map on global sections has rank 26, as checked by the verifier. The source O(2,0) contributes three independent boundaries and has no H1. Thus h0(V)=32−26−3=3.

An explicit basis W1,W2,W3 can be written on U_s as

Wi=(Mi a, Mi^T h+Ti J a),

where

M1=[[z,0],[0,0]],          T1=−pq−2AC,
M2=(1−z^2)[[0,1],[1,0]], T2=z(q^2−p^2−A^2+C^2)+pA−qC,
M3=(1+z^2)[[0,1],[−1,0]], T3=−z(p^2+q^2)−5(pA+qC)+5z(A^2+C^2).

The verified section above is W1+W2. The transpose in the high component is important for the antisymmetric matrix M3.

The universal zero locus over P(H0(V))=P2 is projective. The locus where its fibers are smooth connected regular surfaces is open, and it contains [a:b:c]=[1:1:0] by the certificate. For any regular zero surface the Koszul sequence fixes χ(O_X)=χ(O_P)−χ(V*)+χ(det V*)=1−2+1=0. Hence nearby smooth connected regular zero surfaces, which also have trivial canonical bundle by adjunction, remain abelian. Thus there is a nonempty Zariski-open subset U of this projective net parametrizing smooth connected abelian-surface zero loci of the same fixed bundle V.

For the section aW1+bW2+cW3 the eigenline double cover has branch quartic

4(b^2−c^2)z^4+(a^2−8b^2−8c^2)z^2+4(b^2−c^2).

It is squarefree exactly when

(b^2−c^2)(a^2−16b^2)(a^2−16c^2)≠0.

This supplies an explicit open spectral condition; intersecting it with U still gives a nonempty open set containing [1:1:0]. We do not claim that this six-line complement is exactly the smooth-section locus, that all its cubic fibers are smooth without further checking, that distinct points give distinct isomorphism classes of abelian surfaces, or that the net exhausts all Lange bundles or all embedded abelian surfaces.

Run `python verify_lange_abelian_monad.py`. The calculation is exact, and ordinarily takes under 15 seconds. It verifies the global chain identities, global section, squarefree spectral cover, and all 12 complete modular singularity ideals. The remaining geometric inferences are the explicit spectral identification and proper-specialization argument written above. The verifier does not calculate mixed Atiyah classes.

Primary background: H. Lange, A Vector Bundle of Rank 2 on P1 × P3, https://arxiv.org/pdf/alg-geom/9506021 , sections 1 and 3. All displayed monad and section formulas, and the smoothness certificate, are new calculations in this note rather than quotations from that paper.

## First-order boundary

This explicit member satisfies the relative-monad hypotheses of [PR26](https://github.com/Akilleez-QA/read-em-and-weep/pull/26). Its symmetric elliptic-product pullback has nonzero mixed Atiyah classes and fails the weak first-order kernel equality. The present result supplies a reproducible abelian-surface construction, not a repaired carrier for the original theorem.
