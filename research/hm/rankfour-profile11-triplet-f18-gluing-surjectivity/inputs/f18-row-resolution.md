# The canonical degree-eighteen jet-kernel has a nonzero alternate-triplet row

## Publication input provenance, scope, and conclusion

This packet proves a universal nonvanishing statement and one conditional
actual bundle consequence. It has not been published. A new independent
review of the entire frozen proof and both complete freshly authenticated
direct originals is required before publication. The preparatory audit and
its earlier review are not dependencies or a review of this packet.

The complete direct originals, retained without excerpts, are:

* PR1239 at immutable commit
  `360b7e8f55b05ca5740a10cb3ed844a594766f70`,
  `research/hm/rankfour-profile11-triplet-stationary-section-kernel/PROOF.md`,
  retained in `inputs/stationary-section-kernel.md`: 24,626 UTF8 bytes,
  SHA256 `7835e0a0e6769163dca0ad2ed0a62e3c79a491dc6ebc39e5f8c988d9a9ec6de2`,
  Git blob `2bc33710e6e3b5867955f6a3171786e10f1c08cb`.
* PR1207 at immutable commit
  `af136934955f1bcc700ee768e2debb983e75451d`,
  `research/hm/rankfour-profile11-triplet-shared-d-gluing/PROOF.md`,
  retained in `inputs/shared-d-gluing.md`: 20,361 UTF8 bytes,
  SHA256 `7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7`,
  Git blob `3d051410e80a33f1c4d78d3403bb186595bb72c3`.

Both complete proofs were freshly fetched on 2026-10-24 through read-only
GitHub connector path reads at those immutable commits and separate blob
reads, without line-range limits. The complete path, blob, and retained local
bytes agree, including the computed Git blob identifiers. INPUTS.json records
exact retrieval timestamps, methods, URLs, bytes, hashes, and blob pins;
INPUTS.md and PROVENANCE.md state assertion-level use. The complete originals
were read, not replaced by their summaries or checkers. Raw connector replies
are local evidence only, outside the frozen publication core.

The actual application retains the common full-positive triplet branch,
original t=0, original local delta=12, residual simultaneous rank-seven k=2
geometry, and remaining original kernel K1, together with every complete
transitive actual-geometric hypothesis of both originals. These hypotheses
remain assumptions, not independently reproved here. The two complete direct
proofs themselves supply every imported fact below; there are no additional
direct dependencies on the longer orthogonal-top route.

Work on X=P(W*) for the fixed complex determinant-one binary-icosahedral
representation W. Put H_n=Sym^n W, A=H2, and write V for V_alt. From PR1239
retain its canonical torsion quotient tau, its P-isotypic projection gamma,
and its canonical stationary P-subspace P0:

    gamma = pi_P tau : H18 -> T_P,
    ker(gamma|H18[P]) = P0,
    Lambda15 = ker gamma,
    A18 direct-sum P0 = ker tau.

Section 1 below deduces that P0 itself is basepoint-free and projectively
stationary to first order on the whole reduced invariant orbit Z12. The
conclusion proved below is

    gamma(H2 · H16[V]) != 0.                              (C1)

Equivalently, the V row of the standard complete-jet map at twist two is
nonzero. Under precisely the common retained actual branch of PR1239 and
PR1207 this excludes PR1207's second F18 alternative and forces

    F18 = D(-2) + (W' + T6)(-3),
    H0(F18(2)) = D,     H1(F18(2)) = 0.                   (C2)

These are necessary conditional bundle statements. Nothing realizes or
excludes the whole K1 branch, changes the original t or delta, evaluates an
actual HM source, or proves higher-order matching or algebraicity.

## 1. Fixed universal facts and notation

Both direct originals use the physical W, not W'. The fixed identities needed
here are

    H0=1, H1=W, H2=A, H3=S4, H4=D, H5=T6,
    H6=V+P, H8=P+D, H16=V+P+2D, H18=A+V+D+2P,
    A tensor P=V+P+D,   A tensor V=P+D.                 (1)

The last identity follows directly from the A5 character table printed in
PR1239; it is a single fixed character product. V and P are self-dual as
representation types. No actual coefficient space is identified with its
dual by saying this.

The group has no nontrivial one-dimensional characters. The projective orbit
lengths are 12,20,30,60, and Z12 is the unique length-twelve orbit. Consequently
there is no nonzero invariant section in H6 or H22. Also a nonzero invariant
section of O(20) cannot vanish on Z12: its residual effective invariant divisor
would have degree eight. These conclusions use orbit degrees only, not an
invariant polynomial representative.

Let

    S = H6[P],   E = H16[V].

S is basepoint-free because its degree is six and the smallest invariant
divisor degree is twelve. E is also basepoint-free. Its only possible nonempty
fixed divisor would be Z12; that would put E inside f12 H4, of type D rather
than V, where f12 denotes only the invariant equation line of Z12.

P0 is basepoint-free as well. Any fixed divisor would be Z12 and would force
P0=f12 H6[P], since both are four-dimensional P spaces. This contradicts
PR1239's proved injectivity of tau on f12 H6, while tau(P0)=0. Its first-jet
image on Z12 therefore maps onto the value line and is contained in PR1239's
line L_A, because tau(P0)=0. The intrinsic stationarity criterion there shows
that P0 itself is projectively stationary on Z12, not only A18 direct-sum P0.

## 2. The universal quadratic syzygy of S

Write the evaluation sequence of S as

    0 -> M_S -> S tensor O_X --p--> O_X(6) -> 0.          (2)

It is exact in bundles, with rank(M_S)=3 and deg(M_S)=-6. The V summand of
S tensor H2 maps to zero under multiplication into H8=P+D, by (1). Thus it
gives a nonzero equivariant bundle map

    s : V(-2) -> M_S -> S tensor O_X.                    (3)

Here V names this particular forced copy in H0(M_S(2)); the notation does not
choose a scalar identification with any actual coefficient space.

We prove that s has generic rank three. If its image I had rank one, then I
is a line bundle O(d), with -2<=d<=0: it is a quotient of V(-2), so I(2) is
globally generated, and it injects into S tensor O. But an equivariant
nonzero map V(-2)->O(d) would require V in H_(d+2), which is absent in degrees
0,1,2.

If its image had rank two, its kernel would be an equivariant line O(-k).
Because V first occurs in H6, a nonzero map O(-k)->V(-2) requires k>=8.
Then deg(I)=k-6>=2. This is impossible for a rank-two subsheaf of the trivial
bundle S tensor O: taking its determinant gives a nonzero map from O(deg I)
to the trivial bundle wedge^2 S tensor O, forcing deg I<=0. Kernels and images
here are torsion-free sheaves on the smooth curve and hence bundles; the
linearizations of the line bundles introduce no character because G has none.

Thus s has generic rank three. As a map to M_S its determinant has degree
zero, since both bundles have degree -6. A nonzero degree-zero determinant
has no zero, so s is an isomorphism everywhere. We have established

    0 -> V(-2) --s--> S tensor O_X --p--> O_X(6) -> 0.    (4)

No minor, coefficient, selected point, or instance rank was evaluated. The
rank statements follow from universal degree and representation arguments.

## 3. S is everywhere second-jet-spanned

The full Wronskian of the four-dimensional degree-six system S is nonzero
and has degree

    4(6-3)=12.                                          (5)

Its divisor is invariant. Since Z12 is the unique invariant orbit of degree
twelve and all other orbits are larger, this divisor is exactly Z12 with
multiplicity one. The Wronskian multiplicity at a point is the weight
sum(a_i-i) of its vanishing sequence a0<a1<a2<a3. A strictly increasing
four-term sequence of nonnegative integers with weight one can only be
(0,1,2,4); weight zero can only be (0,1,2,3). Consequently S has exactly
sequence (0,1,2,4) on Z12 and (0,1,2,3) everywhere else.
In particular the second-jet evaluation is onto at every point, and

    0 -> O_X(-12) -> S tensor O_X
      --j^2 p--> P_X^2(O_X(6)) -> 0                    (6)

is exact in bundles. Its kernel degree is -12 because the principal-parts
filtration has graded lines O(6),O(4),O(2). Its equivariant line is indeed
O(-12), since G has no nontrivial character. This argument is a universal
invariant-divisor/Wronskian proof, not evaluation of a selected jet.

## 4. The P product Q is the degree-eighteen curve orthogonal to S

Let B=Hom_G(E*,V), a one-dimensional constant space on which G acts trivially.
Its canonical evaluation B tensor E* -> V is an isomorphism. Compose the
transpose of E's evaluation, twisted by -2 and tensored with B, with s:

    q : B tensor O_X(-18) -> B tensor E* tensor O_X(-2)
                           -> V(-2) --s--> S tensor O_X. (7)

No generator of B and no scalar normalization is chosen. E is basepoint-free
and s is a bundle inclusion, so q is nowhere zero. Its scalar sections span
Q tensor B* inside H18 tensor B* for a unique irreducible P-subspace Q of H18.
The entries of s are quadratic sections. The adjoint of s, with the indicated
canonical evaluation, is a nonzero embedding

    S* -> H2 tensor E tensor B*.

Since P occurs once in H2 tensor E=P+D, the scalar system of (7) is exactly
the P component of the product H2·E, with its harmless constant B* factor.
In particular that product component is nonzero. This is a statement about
the standard multiplication, not about an unverified identification of actual
coefficient spaces.

The defining property of (4) gives the natural orthogonality identity

    p q = 0 : B tensor O_X(-18) -> O_X(6).              (8)

Here p is S's evaluation and q has values in S, the genuine dual of its
constant scalar coefficient domain S*. Its section image is Q tensor B*.
Pairing directions are fixed by (2) and (7); no invariant bilinear form on S
was selected.

## 5. No stationary Q can satisfy this orthogonality

We prove Q != P0. Suppose otherwise. Because constant projective
isomorphisms preserve stationarity, q would be projectively stationary on
Z12, using the universal stationarity of P0 proved in Section 1 above.

Compose q with the first-principal-parts evaluation of S. Its value
projection is zero by (8), so the composite lies in Omega_X tensor O(6)=O(4):

    (j^1 p) q : B tensor O_X(-18) -> O_X(4).                     (9)

This equivariant map lies in B* tensor H22^G. There is no such
nonzero section by the orbit-degree argument in Section 1. Thus (9) is zero.
It follows that the second-principal-parts composite lands in its last
filtration line:

    (j^2 p) q : B tensor O_X(-18) -> Omega_X^2 tensor O(6)=O(2).  (10)

This lies in B* tensor H20^G. We show it vanishes along Z12.

The needed differential implication is a general formal first/second-jet
lemma. In arbitrary local frames write a row r for p and a column z for q.
Identities (8) and (9) say r z=0 and r' z=0. Differentiating the latter formal
identity gives

    r'' z + r' z' = 0.

At a stationarity point of q, z' lies in the line spanned by z. Therefore
r' z'=0 there, and r'' z=0. This is precisely the vanishing of (10). The
statement is independent of all frames because both lower jet composites
already vanish. This is a general local proof applied uniformly to the
entire invariant orbit, not a selection or evaluation of a point, actual
coefficient, parameter, or jet. It introduces no connection or inverse map.

Consequently (10) vanishes on Z12. A nonzero invariant section of O(20)
cannot do this, as its residual invariant divisor would have degree eight.
Thus (10) is identically zero. By (6), q must factor through O(-12). But an
equivariant map

    B tensor O(-18) -> O(-12)

lies in B* tensor H6^G, and no nonzero one exists. This contradicts
the nowhere-zero q in (7). Therefore

    Q != P0.                                            (11)

This is the decisive structural nonvanishing step. It uses the degrees
6,20,22 and the second-jet kernel of the fixed degree-six P system; it uses
no chosen f12 representative or numerical coefficient identity.

## 6. Exact direction of the complete-jet contraction

Let i denote the standard complete first-jet-annihilator inclusion

    i : H16 tensor O_X(-2) -> H18 tensor O_X.             (12)

At a variable tautological line ell in W*, the fixed determinant pairing
identifies ell with its annihilating linear form in W. The inclusion is
multiplication by the square of that vanishing linear form. Twisting (12)
by two and taking global sections gives

    i_2 : H16 -> H18 tensor H2.

The square of the determinant pairing gives a nondegenerate identification
H2*->H2. Contracting i_2 with any element of H2* therefore yields multiplication
by the corresponding element of H2. This is the actual standard complete-jet
inclusion, not merely an abstract representation-theoretic map with the same
source and target.

Put

    c=(gamma tensor id) i_2 : H16 -> T_P tensor H2.       (13)

Because the determinant-square pairing is nondegenerate, contraction proves

    c|E=0  iff  gamma(H2·E)=0.                           (14)

By (1), H2 tensor E has just P and D. Gamma kills the D part, while Section 4
proved its P product is the nonzero irreducible subspace Q. Thus the right
side of (14) is equivalent to Q=P0. Equation (11) disproves it, so

    c|H16[V] != 0.                                      (15)

This proves (C1) with the required map directions and determinant contraction.

## 7. Conditional actual consequence

PR1239 identifies the actual scalar-section space, through its actual map
j18, with Lambda15=ker gamma. The actual first-jet-annihilator is therefore
the intersection of Lambda15 tensor O with the standard complete kernel
(12). PR1207 supplies the actual everywhere first-jet-spanning needed for
the quotient map to be onto. Hence the actual sequence is

    0 -> F18 -> H16(-2) -> T_P tensor O_X -> 0,

with its map exactly induced by (12) and gamma. At twist two its global-section
map is (13), not a transported rank-seventeen bound or an arbitrary map of
these representation types.

Source and target have types

    H16=V+P+2D,   T_P tensor H2=V+P+D.

By (15), the unique V row is nonzero and hence an isomorphism on its V
constituent. PR1207 proved that the only two allowed actual kernels have
H0 at twist two equal respectively to D and D+V. The second alternative
therefore cannot occur. Its first alternative, and its split extension
consequence from PR1207, remain:

    F18=D(-2)+(W'+T6)(-3),
    0 -> V(-4) -> E0 -> F18 -> 0

splits equivariantly as a bundle extension. No splitting is asserted
horizontal, and no additional conclusion about the actual map F18->Q in
PR1207 or the larger branch is inferred.

## 8. Verification obligations and boundary

The proof reduces the missing row to an explicit contradiction among universal
principal-parts maps. The essential checks are: the syzygy inclusion (4), the
second-jet kernel (6), the naturally directed pairing (8), the formal implication
from stationarity to (10) vanishing on Z12, and the determinant contraction
(14). Each is proved above; none can be replaced by a numerical character
check. Independent review should scrutinize these maps and the conditional
use of the complete direct originals.

No actual coefficients, HM parameters, selected points, eigenlines, jets,
tensors, matrices, instance ranks, P representative, or scalar normalization
were evaluated. No invariant polynomial representative, broad scan, historical
enumerator, local Codex task, quotient connection, horizontal splitting, or
inverse-map derivative was used. Higher principal parts serve only as a
universal obstruction to a first-order stationarity condition. This is not a
claim of higher-order branch matching or algebraicity.
