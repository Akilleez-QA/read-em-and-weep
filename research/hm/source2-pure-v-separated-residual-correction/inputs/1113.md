# The common quadratic homotopy kernel and forced separated P correction

## Theorem

Retain the actual source2 nonzero pure-V compatible-radical hypotheses
and specifically the RESIDUAL-LARGE mechanism: P_h is contained in NR2
and its actual N8,2 projection is nonzero. Define

    Gamma(v)(a)=hT_a v.

On NR2 this takes values in Hom(A,I2), and

    rank Gamma|NC2=12,       ker Gamma|NC2=I2,
    rank Gamma|NR2=15,       K_{R,2}=ker Gamma|NR2 has dimension17.

More precisely there is an actual exact sequence

    0 -> I2 -> K_{R,2} --pi2--> (N8,2)_(V+P+D) -> 0.          (1)

This is a coefficient-space statement, NOT a horizontal splitting of
the residual negative module. The P and surviving D rows are proved
nonzero by a complete universal polynomial certificate; they are not
inferred just from their allowed characters.

Set J2=ker j2. On J2 the SAME Gamma has target Hom(A,I2), rank15 and
kernel K of dimension21, in degree two. In fact the common kernel of hT_a on all M2
is this K, though hT on all M2 does not have target I2. There is an
exact sequence

    0 -> K_{R,2} -> K --e0--> (N0,2)_P -> 0.                 (2)

Now additionally assume R=0. For any equivariant right inverse G of
Q: M2->Z=im Q, define the actual correction

    k:A tensor I4 -> M2,     k(b,p)=G T_b s(p),
    s:I4 -> P_h,             Qs=Id_I4.

Then

    K=F2 direct-sum k(A tensor I4),
    QK=F4=I4 direct-sum T_A P_h.                         (3)

The correction is injective. Its V and P restrictions are independent
of G, and its D restriction is canonical modulo I2. Contrary to a full
residual-placement guess, its P channel necessarily satisfies

    e0 k|P_in : P_in -> (N0,2)_P is an isomorphism.        (4)

Thus the first zero-fourth correction has a forced nonzero separated P
component. Its V and D channels lie in NR2; the P channel cannot lie
there. This does not evaluate a coefficient relative to an arbitrary
complement, decide R=0, prove a fifth obstruction nonzero, or identify
any positive/opposite-pencil source.

## 1. Actual input geometry and typing

Ten immutable originals are retained in INPUTS.json:
PR795, PR792, PR1064, PR1059, PR1069, PR1089, PR1019, PR1031 proof/model,
and the PR1036 verifier used only as an invariant-normalization source.
Their exact commits and paths are recorded there. In particular PR1064
is at bfc239e1c8624a0346394e1454b0bea3c976d40d, PR1069 at
41bc20cade3198306c492c0c46399d71eb0d51c4, and PR1089 at
f8dfebc8c12cbefd3b17422fa1220629e90af78e.

PR795 gives the genuine negative split N=N0 direct-sum NR and exact
residual quotient 0->NC->NR->N8->0, with the ORIGINAL fixed variables.
In degree two,

    N0,2=P+D, NR2=A+2V+2P+3D,
    NC2=Sym16 W=V+P+2D, N8,2=A+V+P+D.                  (5)

The actual endpoint reconstruction gives

    NC4=Sym18 W/H_t=P+D,
    H_t=A18+V18+P_t,  Sym18 W=A+V+2P+D.                (6)

Its negative quadratic multiplication is the ordinary product
(a,f)->[a f] in (6), not a map inferred from matching dimensions.
PR792 identifies I2 with the actual embedded F12 Sym4 W in Sym16 W.

In residual-large, PR1064 proves h:NC4/I4->I2 is an isomorphism.
Hence h annihilates the P=I4 in (6) and is nonzero on its unique D.
That D is the unique D18 constituent of Sym18; H_t contains no D.
Consequently hT on NC2 is, up to a nonzero equivariant identification,
EXACTLY quadratic multiplication followed by the D18 projection.
Its nonzero scale is not chosen or evaluated.

On NR2, negative stability gives T_a NR2 subset NR4 and PR1064 gives
h(NR4)=I2, so Gamma has target Hom(A,I2)=A+V+P+D, dimension15.
The canonical A in ker Q is inside NR2 by PR795. PR1019 supplies the
actual nonzero row hT_a a_A(x)=mu a x, mu nonzero.

The radical kills NR2. Since im j2=I2=D, it maps the D part of N0,2
isomorphically onto I2 and vanishes on the P part. Thus

    J2=ker j2=NR2 direct-sum (N0,2)_P.                  (7)

For v in J2, QhT_a v=j4T_a v=T_a j2v=0, so hT_a v lies in
im h intersect ker Q=I2. This justifies the J2 target before any rank
or kernel argument. We do NOT assign this target to hT on arbitrary M2.

## 2. Universal full-coefficient nonvanishing of every NC row

Use the fixed PR1031 representation and PR1036 invariant normalization.
Let F12 be the Wronskian of the V6 kernel of the pinned Pi:Sym6->P:

    F12=-2x^12-(44sqrt5/5)x^10y^2+66x^8y^4
        +(88sqrt5/5)x^6y^6+66x^4y^8
        -(44sqrt5/5)x^2y^10-2y^12.

This is fixed universal representation data, not an actual HM coefficient
or a selected endpoint. Form the invariant H20=(F12,F12)_2 using the
unnormalized transvectant convention

    (f,g)_r=sum_j (-1)^j binom(r,j)
             partial_x^(r-j)partial_y^j f
             partial_x^j partial_y^(r-j) g.

Define E18:Sym4 W->Sym18 W by d->(H20,d)_3. The exact19-by5
coefficient matrix E has rank5. It is equivariant and Sym18 contains D
once; therefore its image is precisely D18. With the apolar Gram matrix
(G18)_(i,18-i)=(-1)^i/binom(18,i), the map E^t G18 is a projection to
D* with kernel the other irreducible constituents. Self-duality identifies
D* with D; no normalization of the actual h is needed.

For each quadratic monomial x^(2-k)y^k, k=0,1,2, apply this projection
to every product with x^(16-i)y^i, i=0,...,16, and stack the three blocks.
This gives a15-by17 WHOLE coefficient matrix M for the common map.
Let I be the17-by5 coefficient matrix with columns F12 x^(4-i)y^i.
The exact certificate is

    rank E=5,       rank M=12,
    M I=0,          rank I=5.                            (8)

The checker supplies an explicit nonzero12-minor, using rows
0,1,2,3,4,5,6,7,8,9,13,14 and columns0,...,11, and records its exact
value in RESULT.json. Thus ker M=im I, not merely a containing subspace.
No quadratic direction has been selected: all17 input coefficients and
all three quadratic coefficients are retained.

Transport through the actual map in Section1 proves ker Gamma|NC2=I2.
Since NC2/I2=V+P+D and the target has each of these constituents once,
all THREE rows are nonzero. In particular the required P and D
nonvanishing are now proved, independently of the previously known
marked V argument. The whole-character calculation checks each stated
multiplicity and the uniqueness of D18.

## 3. Residual and full common kernels

The NC image is the full V+P+D part of Hom(A,I2). The canonical A row
from Section1 is nonzero and occupies its remaining A constituent.
Therefore Gamma|NR2 is onto and K_{R,2} has character

    (A+2V+2P+3D)-(A+V+P+D)=V+P+2D.                    (9)

Its intersection with NC2 is I2 by (8). Thus its actual quotient image
has character V+P+D inside the multiplicity-free N8,2. This is exactly
the indicated canonical isotypical subspace, proving (1).

Gamma|J2 is onto since NR2 already maps onto. From (7), its kernel has
character V+2P+2D and dimension21. The projection of K onto (N0,2)_P
is onto: any Gamma value of a vector in that P can be canceled by a
vector in NR2, using surjectivity just proved. Its kernel is K_{R,2}. This
proves (2), with no choice of a splitting.

For completeness let v in arbitrary M2 satisfy hT_a v=0 for all a.
Then T_a j2v=QhT_a v=0 for all a. The common kernel of L_a on I2=D
is zero: it is a G-subrepresentation of the irreducible D, and the
multiplication/projection map L is nonzero. Thus j2v=0, so v lies in
J2 and then K. This proves that K also describes the full common kernel,
without incorrectly declaring hT(M2) contained in I2.

The sandwich identity hT_a h=0 of PR1069 puts F2=I2+P_h in K_{R,2}.
By (9), its P is the UNIQUE P in K_{R,2}. Hence

    (K_{R,2})_P=P_h.                                      (10)

This actual identification will be essential for the correction placement.

## 4. Complete correction alignment under R=0

Now impose R=0. PR1089 proves the transfer B(a,b)=hT_a G T_b s is
symmetric, so its diagonal zero implies B=0. The actual correction k is
therefore in the common kernel K. Independently,

    Qk=T_b s,      j2k=hQk=hT_b s=0,

where the last identity is the sandwich, so the J2 typing is consistent.

PR1059 proves that the actual quadratic descendant projection
A tensor P_h->N8,4 is an isomorphism. Therefore T_A P_h has dimension12
and is disjoint from I4, whose quotient projection is zero. It follows
that Qk is injective on its12-dimensional source A tensor P=V+P+D,
so k itself is injective. If a vector of k(A tensor P) lay in F2,
its Q image would belong both to T_A P_h and to QF2=I4. These are
disjoint; injectivity would make that vector zero. Thus F2 and the
correction image are disjoint. Their dimensions9+12=21 fill K, proving
the first equality in (3). Applying Q proves its second equality.

This is an exact same-source image equality and correction decomposition,
not a claim that Q preserves NR or any negative-horizontal complement.
The decomposition depends on the equivariant inverse only in the D
channel: a change of G changes k by a map

    A tensor P=V+P+D -> ker Q=A+I2.

There is no V or P ambiguity, and the D ambiguity lands in I2. Therefore
k_V and k_P are canonical actual maps; k_D is canonical modulo I2.
Since J2 has no separated V or D summand by (7), k_V and k_D are residual.
In particular their quotient projections in (1) give the V and D parts,
with I2 retained as the D gauge.

## 5. The P correction must cross to the separated block

The P constituent of T_A P_h has nonzero projection to the P constituent
of N8,4, since the full quadratic descendant quotient is an isomorphism.
It therefore cannot be contained in I4. Suppose k(P_in) were contained
in NR2. It would then lie in the unique residual common-kernel P,
which is P_h by (10). Consequently its Q image would be I4, because
Q:P_h->I4 is an isomorphism. This contradicts the preceding nonzero
N8 projection. Hence e0 k|P_in is nonzero. By (7) its image is in the
actual separated (N0,2)_P; irreducibility makes it an isomorphism.
This proves (4) and is independent of G by Section4.

Thus the natural attempt to place the ENTIRE first correction into a
section of K_{R,2}/I2 is false under the zero-fourth hypothesis. The actual
residual P in that quotient is P_h itself, whereas the correction P
necessarily leaves NR. The V and D correction channels remain residual.
This is forced placement, not an arbitrary repeated-copy coordinate or
a coefficient evaluation. It does not contradict the residual placement
of P_h: the generator and its Q-preimage correction are different maps.

## Verification and limits

Run python verify.py and python -O verify.py to reproduce RESULT.json.
Ten immutable input digests are checked. The bounded universal coefficient
calculation verifies (8), the exact minor, and the pinned invariant via
its Wronskian. Exact characters check all kernel dimensions and ambiguity
claims. Written actual-map naturality and the retained hypotheses are
necessary for transporting this certificate to hT.

No actual source coefficient, endpoint, coupling, point, direction, jet,
instance matrix or source rank is evaluated. The residual-large mechanism
is retained throughout. Equations (3)-(4) additionally require R=0, which
is not selected or excluded. No conclusion about the original fifth,
positive cross-block tensor, opposite pencil, or full adjoint is asserted.
