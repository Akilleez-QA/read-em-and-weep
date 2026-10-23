# The actual positive middle is jointly faithful

## Result and boundaries

Work over C with the actual normalized Horrocks--Mumford bundle F on
P4, B=End_0(F), and G=SL2(F5). The coordinate space is T=V+W, where
V is the positive three-space and W the negative two-space. Put

    N2=H1(B(2))_+, P3=H1(B(3))_+, N4=H1(B(4))_+,
    a:V tensor N2 -> P3, b:V tensor P3 -> N4.

All arrows are actual multiplication. Let btilde:P3 -> V* tensor N4
be the curry of b. Then

    btilde is injective.                                      (1)

In fact simultaneous positive multiplication on the whole H1(B(3)),
before selecting its central parity, is injective. This is not
injectivity of multiplication by any one chosen positive coordinate.

Consequently, if R=im a is the actual reachable middle of PR931 and
Cplus=btilde a is the full curried positive quadratic multiplication,

    ker Cplus=ker a,
    im Cplus=btilde(R) is canonically isomorphic to R.           (2)

Its exact character is 1+3A+2V+3P+3D and dimension43. The whole
P3 has dimension46 and embeds by btilde; it is not identified with
the 43-dimensional image in (2). Neither image is a subspace of
the 37-dimensional N4: both are in V* tensor N4.

Let H=(P3)_1 and B0=b(V tensor H). Then

    b|V tensor H is injective, B0 is an actual V.                (3)

Thus the scalar second arrow cannot vanish. In the notation and
normalization of PR1114, K=Q^{-1}d s has rank exactly one, and

    ker K=ker s, im K=Q^{-1}(im d).                              (4)

This excludes K=0 but NOT a nonzero nilpotent K or trace K=0.

The root cause is the absence of linear relations among the actual
degree-five adjoint sections, combined with the three-positive-coordinate
Koszul complex. It is an additional geometric/module constraint, not
a rearrangement of PR1114's rank-one identities.

Under all PR1114 Section4 residual-large and R=0 hypotheses only, its
vanishing criterion sharpens to

    p_V e0 b(V,a(V,V_h))=0
        iff B0=V_R OR V_h=V_s,       V_R=(NR4)_V.                (5)

Here equality B0=V_R replaces an inclusion that previously allowed B0=0.
Neither actual incidence in (5) is decided. No source occurrence,
Smith exponent, fifth-class value, or algebraicity conclusion follows.

## 1. Immutable inputs

INPUTS.json authenticates four complete originals by exact commit,
Git blob, SHA256 and byte count.

* PR485, 251d9a62e97b36ad61191bfa603cdb384a3839f3,
  research/hm/section-tail/PROOF.md:
  H0(B(t))=0 for t<=4, H0(B(5))=Sym2 U with U=H0(F(3)),
  and the ACTUAL multiplication
  T tensor H0(B(5)) -> H0(B(6)) is injective.
  Section3 proves this by the symmetric-evaluation complex and primary
  section resolution, not by a selected multiplication calculation.
* PR931, e28d3b74d4288239426ad1e675e806310fadf8be,
  research/hm/positive-reachable-middle/PROOF.md:
  R=ker[P3 -> H1(B|L(3))_+], with L=P(W*), and the exact characters
  P3=1+4A+2V+3P+3D, R=1+3A+2V+3P+3D and
  ker a=1+4A+4V+5P+7D.
* PR1114, fc79bc119a251c16d386467333f55cd46dc75367,
  research/hm/repeated-v-channel-pencil/PROOF.md:
  E=(N2)_V and F4=(N4)_V are full copies of 2V; actual Q:E->F4
  is an isomorphism. The scalar first multiplicity map s is onto,
  its second map is d, K=Q^{-1}d s, and all effective coefficients
  retain b and the full V-isotypical target projection.
  Its conditional source hypotheses and projector criterion are
  used only in Section5 below.
* PR1050, ec18a0fd62c4a9495adf6aad9564d379afc42b62,
  research/hm/canonical-negative-string/PROOF.md:
  actual H0(B(5))=1+P+D, all positive.
  This is used only for the independent scalar-only check in Section4.

No full section resolution, later uncertain source classification, or
selected coordinate value is needed. PR485 supplies precisely the
low-degree natural multiplication fact; we recheck its derivation next.

## 2. Why actual degree-five sections have no linear relation

To avoid any shift ambiguity, write U=H0(E0), E0=F(3), so B(5)=Sym2 E0.
PR485 retains the actual primary section embedding

    T tensor U -> H0(E0(1)).                                  (6)

It is injective because the primary section module has four generators
in degree0, fifteen new generators in degree1, and no first relation
before degree2. Equivalently this follows directly in degree1 from
its pinned minimal free resolution. These are shifts for Gamma_*E0,
not the shifts of G_j=H0(B(j-1)).

The exact symmetric-evaluation complex of PR485, twisted by1, has
its middle two image sequences. Since line-bundle intermediate
cohomology vanishes on P4 and the line-residue bundle Lc^2(1)
has degree -1 on each evaluation-degeneracy line, it gives

    H0(B(6)) =
      [U tensor H0(E0(1))] / [Lambda2 U tensor T].               (7)

The denominator is the actual alternating evaluation inclusion.
By (6) it lies inside the embedded subspace
U tensor (T tensor U). On that subspace, its quotient is canonically

    [T tensor U tensor U] / [T tensor Lambda2 U]
        = T tensor Sym2 U.                                    (8)

The multiplication diagrams of the symmetric-evaluation complex
identify (8) with the image of natural multiplication on
H0(B(5))=Sym2 U. As an embedded subspace modulo exactly its displayed
denominator, it injects into (7). Hence

    T tensor H0(B(5)) -> H0(B(6)) is injective.                  (9)

Restricting (9) to V subset T remains injective. This argument uses
actual augmentations, not merely dimensions of section spaces. In the
shift convention G_j=H0(B(j-1)), it agrees with the absence of
degree7 first syzygies for the degree6 generators. No matrix, minor,
section coefficient or actual-instance rank is evaluated.

## 3. Exact Koszul identification of the joint kernel

Here is a direct sheaf chase, without a spectral-sequence ambiguity.
For any locally free sheaf A on P4, take the three independent forms V
cutting out L. At the relevant twist their regular Koszul complex is

    0 -> Lambda3 V tensor A(3)
      -> Lambda2 V tensor A(4)
      -> V tensor A(5) -> A(6) -> A(6)|L -> 0.                 (10)

Let Z be the image of Lambda2 V tensor A(4) in V tensor A(5).
Regularity gives both

    0 -> Lambda3 V tensor A(3)
      -> Lambda2 V tensor A(4) -> Z -> 0,
    Z=ker[V tensor A(5) -> A(6)].                              (11)

Suppose H0(A(4))=0. The first long exact sequence then identifies

    H0(Z) =
      ker[Lambda3 V tensor H1(A(3))
           -> Lambda2 V tensor H1(A(4))].                     (12)

The second equality in (11), followed by left exactness of H0, gives

    H0(Z)=ker[V tensor H0(A(5)) -> H0(A(6))].                  (13)

Thus (12)-(13) are natural identifications of the ACTUAL kernels.
The left Koszul differential is simultaneous multiplication, with
the usual exterior signs. The canonical identity
Lambda2 V = V* tensor Lambda3 V identifies its kernel with
Lambda3 V tensor the joint multiplication kernel. For the actual G
action det V is trivial; a determinant trivialization merely rescales
this identification and cannot affect vanishing.

Apply (12)-(13) with A=B. PR485 gives H0(B(4))=0, and (9) makes
the right kernel zero. Therefore

    H1(B(3)) -> V* tensor H1(B(4)) is injective.                 (14)

Taking positive central parity is exact and V is positive, proving (1).
Neither H2 nor H3 vanishing is needed. In particular no contribution
from higher Koszul cohomology was silently omitted.

Actual coordinate associativity and commutativity identify Cplus with
btilde a. Injectivity of btilde proves (2), including the actual kernel
equality and the actual isomorphism R->im Cplus. PR931 supplies the
stated characters and dimensions.

## 4. The scalar middle is not annihilated

The trivial isotypical part H=(P3)_1 is one-dimensional and actual.
Restriction of (1) to H is nonzero. Since V tensor H is irreducible
of type V, b|V tensor H is nonzero and hence injective. Its image B0
is therefore an actual embedded V in the full F4=(N4)_V. This proves
(3) without replacing b by an arbitrary equivariant map.

There is a useful second verification of this scalar exclusion that
does NOT require the stronger section injectivity (9). Equations
(12)-(13) and H0(B(4))=0 embed the joint kernel into

    V tensor H0(B(5)) = V tensor (1+P+D)
                     = 2A+2V+2P+2D.                          (15)

This representation has no trivial constituent. By exactness of finite
group invariants over C, the joint kernel has no trivial constituent
either. Thus H cannot be annihilated. The dimensions here are30, not
the46-dimensional middle or37-dimensional final cohomology. The
section character input is actual section exhaustion from PR1050,
not an Euler-character substitution.

Now retain PR1114's actual multiplicity spaces, Q, s, d and full
target projector. The map s is onto a line by its first-arrow
reachability argument. Equation (3) says d is nonzero, so d is
injective from that line. Therefore Q^{-1}d s has rank exactly one,
ker K=ker s and im K=Q^{-1}(im d). No value of any multiplicity
entry or trace has been chosen. In particular a rank-one nilpotent
operator is still possible.

On the full repeated-V E, the scalar composite C0=d s is consequently
nonzero. The scalar coefficient channel cannot be discarded globally,
even when a particular actual V_s=V tensor ker s is in its kernel.

## 5. Conditional incidence comparison and remaining work

Assume all residual-large and R=0 hypotheses in PR1114 Section4.
Retain its actual negative projector e0, actual V_h and actual
V_R=(NR4)_V. That source theorem makes V_R one copy of V, and gives

    p_V e0 b(V,a(V,V_h))=0
       iff B0 subset NR4 OR V_h=V_s.                           (16)

By (3), B0 is a nonzero V subspace of F4. Thus its inclusion in NR4
is equivalent to equality B0=V_R. This proves (5). We do not move
e0 to P3, discard the second arrow, or identify repeated copies by
characters.

For clarity, there is a further purely conditional distinction. In
PR1114 multiplicity notation let L_h=ker(lambda), where
lambda=rho Q. The two alternatives in (5) become

    im K=L_h, OR ker K=L_h.                                    (17)

They can hold simultaneously only if im K=ker K, equivalently
K is nonzero nilpotent, equivalently tr K=0. Conversely, if tr K=0,
rank K=1 gives im K=ker K, so the two alternatives are equivalent.
If tr K is nonzero they are mutually exclusive. These statements
organize the remaining incidences; they do NOT decide the trace or
either incidence and are not presented as a second root-cause proof.

The no-linear-section-relation argument closes PR931's explicit
second-arrow-kernel dependency and excludes the zero-scalar-arrow
case permitted by PR1114's abstract local models. It does not exclude
their nonzero nilpotent or remaining image dimensions12,14,17.
It supplies no theorem that a universal local model extends to HM.

No selected actual HM/source coefficient, parameter, point, derivative,
jet, tensor, matrix or instance rank was evaluated. The numeric
dimensions above are deductions from exact sequences and authenticated
representation characters. The bounded checker authenticates inputs
and checks fixed representation and degree bookkeeping only. The
written proof and independent review carry the geometric actual-map
argument.

The next concrete unresolved question remains the POSITION of the
now-known nonzero B0 relative to V_R, or of V_s relative to V_h.
This theorem does not decide source occurrence, the actual Xi alignment
of PR1115, any fourth/fifth symbol value, a final Smith exponent,
or Weil-class algebraicity.

