# Symmetry-certified normalization families admit a two-orbit calibration

New bounded deduction, 2026-10-23. Written mathematics, not Lean certification.
No actual HM source, coefficient, point, matrix, rank or calibration is evaluated.
PR866 is unchanged; PR880's algebra adapter is not duplicated.

## Result and exact qualification

The actual positive binary representation is U=Wprime, not the negative W.
The trace space of PR866 is

    T=Sym^12 U = 1 + V + P4 + D5.                         (S1)

For an arbitrary fixed source, the stated hypotheses of PR815/866 do NOT
make its normalization error eta a G-invariant vector. Thus those hypotheses
alone do not replace thirteen calibration coordinates by one.

There is, however, a sharp new FAMILY bound. If a proposed physical packet
additionally certifies that its globally glued error is a coherent
G-equivariant family, homogeneous cubic in the negative quadratic a and
linear in the positive source h, then

    eta in H=Hom_G(Sym^3 A tensor D5,T),   dim H=10,
    projection_1 eta=0.                                  (S2)

The universal output span is exactly V+P4+D5, of dimension twelve. This is
not a claim that every such abstract family is realized by actual contractions.

For this ten-dimensional family space, the entire h-family values at ANY
one semisimple C5 axis p and ANY one C5-fixed square s detect the family:

    (Ev_p,Ev_s):H -> axis data + square data is injective. (S3)

The separate maps have kernels of dimensions four and three, respectively.
The norm observation still contains the varying multiplier a^3 h. Section 5
retains that multiplier and proves why full quadratic-in-h observations
implement (S3); it is not replaced by a fixed linear functional.

## 1. Sources, representation identification and missing certificate

The six exact source copies and immutable URLs/Git blobs are recorded in
SOURCE-MANIFEST.json. They are:

- PR815, `0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42`: actual source-response
  types, full corrected source and trace coefficient bundle.
- PR866, `25b1d2927294fffbc393e6ac2285f5a58cfd6c60`: the mixed error
  rho_AB-rho_AA=-a^3 h eta and its prior-globality requirements.
- Next-weight interface, `3d21e93865152ec961ceaf32d48f845399158b69`:
  its Sections 1 and 3 identify Sym^12(Wprime)=1+V+P4+D5 and the relevant
  trace sequence. Its global-conic extension theorem is NOT assumed for a
  merely glued scalar eta.
- Canonical multiplied lift, `3333cce744b3bd8e4472969f599588fec3e20d52`:
  U=Wprime, the negative quadratic three-space A, and the equivariant linear
  family zeta_a represented by the natural Hamiltonian deformation.
- Canonical correction, `4e16e69c776bd85506341b5bb785f0d8a396bd3e`:
  b=L_can(a,h) is equivariant, polynomial linear in a and linear in h.
- PR658 axis geometry, `95004606fb8b2ec51ecd97e2fde0d6d0ff328407`:
  the six semisimple axes, their absence from the discriminant conic Delta,
  and their no-conic general-position property. We use its geometry only,
  not its different four-channel fourth-gate conclusion.

Here G=2.A5; all representations used below have trivial central action and
therefore factor through A5. Put A=Sym^2 W and V=Sym^2 U, the DISTINCT
three-dimensional irreducibles. The positive source is D5=Sym^4 U. All
these even representations are self-dual. Determinant markings are retained;
no identification U=W or interchange of A and V is made.

PR866 only requires authenticated contractions, aligned frames, source rows,
and compatible twists. Those conditions do not state that two arbitrary
contraction packets are coherently G-equivariant over the parameter family.
Finite symmetry of the ambient bundle does not establish that for chosen
local splittings. An equivariant family satisfies

    eta(g a,g h)=g eta(a,h),

not eta(a,h)=g eta(a,h) for fixed a,h. The latter follows only for elements
fixing the inputs (with any line characters correctly retained).

Even the central/physical-positive restriction does not cut (S1): its cover
degree is twelve, so the central element acts as +1 on ALL thirteen vectors.
No ambient extension of the separate cone Serre involution is assumed here.

The extra certificate required for (S2) is therefore explicit: one fixed,
source-independent comparison operator, with genuine coherent G-action and
the fixed physical extraction, together with an equivariant polynomial
corrected-source family and prior global gluing of eta. Alternatively one
may directly certify these properties for the resulting eta family. This
note supplies neither certificate for the actual pending implementation.

## 2. Why cubic-in-a and linear-in-h is the correct family type

Write the full source of PR815 as

    T(a,h)=a(V_h(a)-b(a,h) Z_a)-q W_h(a).              (S4)

Z_a is linear in a. The preceding equation dC_h=a h Z_a-q V_h makes its
right-hand input quadratic in a and linear in h. Coherent linear choices
of the finite-dimensional global cochain lifts preserve this bidegree, so
V_h and C_h may be chosen of bidegree (2,1). Since b is of bidegree (1,1),
a(V_h-b Z_a), W_h, and E_h may coherently be chosen of bidegree (3,1).
Here b is the canonical correction, or a supplied correction independently
certified to have this bidegree. Identifying an arbitrary Schur-gauge
correction with L_can requires its own comparison, as the pinned source says.
For the source subspaces where the ladder proves existence, linear
splittings exist; averaging finite-dimensional linear splittings preserves
the equations and makes them G-equivariant. This is an EXISTENCE argument
for compatible family choices, not proof that an arbitrary supplied packet
used those choices or that local physical contractions are equivariant.
Application to the full family requires the entire homogeneous source
module to lie in the relevant image. Pointwise existence only on a restricted
source locus does not certify a polynomial family over all of A tensor D5.

The PR866 comparison operator is linear in its degree-one input. If fixed
independently of a,h and correctly equivariant, it therefore yields a cubic
a/linear h family of global trace sections. Polarization in characteristic
zero identifies exactly its universal coefficient space with H in (S2).
The corrected term -a b Z_a has the SAME degree (3,1); dropping it is not
licensed by this grading. The -q W_h term remains the certified full-source
argument even though the cone comparison admits the expression with S.

Without coherent linear family choices or equivariance, these degrees alone
impose no proper output subspace of T: abstract families f(a)ell(h)v, with
f a cubic, ell a linear functional and v ranging through T, satisfy the
degree/globality restrictions. This is a logical countermodel to a
symmetry-free reduction, not a claim of actual HM contraction realizability.

## 3. Exact decomposition and the ten family channels

On A5 classes (1,2,3,5a,5b), put phi=(1+sqrt(5))/2 and phibar=1-phi.
The character table is

    1 : (1, 1, 1, 1, 1)
    A : (3,-1, 0, phi,phibar)
    V : (3,-1, 0,phibar,phi)
    P4: (4, 0, 1,-1,-1)
    D5: (5, 1,-1, 0, 0).

The class sizes are (1,15,20,12,12). The symmetric-cube character formula
or the standard binary harmonic splitting gives

    Sym^3 A=A+V+P4,
    A tensor D5=A+V+P4+D5,
    V tensor D5=A+V+P4+D5,
    P4 tensor D5=A+V+P4+2D5.

Thus

    Sym^3 A tensor D5=3A+3V+3P4+4D5.                (S5)

There is NO trivial constituent. With (S1), Schur's lemma yields

    dim H=3+3+4=10,
    Hom_G(Sym^3 A tensor D5,1)=0.                    (S6)

Each of V,P4,D5 occurs in the domain, so all three can occur in abstract
equivariant maps. Pure tensors a^3 tensor h span Sym^3 A tensor D5 by
polarization. Consequently the span of outputs across all such maps and
inputs is precisely V+P4+D5. This proves sharpness of the twelve-dimensional
universal output bound without choosing actual data.

For a truly invariant single vector, (S1)^G is one-dimensional. This is a
different assertion and is NOT the correct family condition. In fact the
invariant output of every family in H is ZERO, not an unknown invariant
scalar. Arbitrary nonzero fixed inputs do not convert a family into an
invariant vector. The actual image may be smaller than (S5) permits, but
no such further source-image statement is supplied here.

## 4. Two complete source-family observations are sufficient

Regard a family as a T-valued, h-linear cubic on P(A). Its values lie in
T tensor O(3), and this line factor is never omitted.

### 4.1 One semisimple axis has a four-dimensional kernel

Let Z6 be the six semisimple axes. No conic contains them, so evaluation
of quadrics at Z6 is an isomorphism between six-dimensional spaces. Choose
an auxiliary linear form nonvanishing on this finite set; its existence
makes evaluation of cubics surjective. Hence h0(I_Z6(3))=10-6=4.

The stabilizer N of an axis is dihedral of order ten. Its order-five
rotations act by +1 on the axis line in A; a normalizer involution acts
by -1. The O(3) fiber therefore carries the sign character epsilon.
Indeed that involution exchanges the two nontrivial C5 eigenlines; its
determinant on their sum is -1, while det(A)=1, forcing -1 on the axis.
The six-axis value module is Ind_N^A5 epsilon, with character
(6,-2,0,1,1)=A+V. Since Sym^3 A=A+V+P4,

    H0(I_Z6(3))=P4.

An equivariant h-family vanishing at one axis vanishes at all six. Exactness
of finite-group invariants therefore gives

    ker Ev_p=Hom_G(P4 tensor D5,T),  dim ker Ev_p=4.   (S7)

The full axis observation target Hom_N(D5,T tensor epsilon) has dimension
six. For instance its character inner product is (5*13-5)/10=6, since
D5 has character zero on nonidentity rotations. Thus Ev_p is onto this
six-dimensional target. This is a universal representation rank derived
from exact sequences, not an actual-instance rank computation.

### 4.2 One C5-fixed square has a three-dimensional kernel

Let s be either square eigenline associated with any C5 axis, on the
discriminant conic Delta. Its A5 orbit consists of twelve distinct points.
A finite point stabilizer on P(W) is cyclic in characteristic zero. Since
this stabilizer contains C5 and A5 has no cyclic subgroup of larger order,
it has order five, proving the orbit count 60/5=12.
A cubic restricts to a binary sextic on Delta=P(W). If Ev_s eta=0 as a
map on the ENTIRE D5 source, equivariance makes every component vanish at
all twelve points. A nonzero binary sextic cannot do so. Every component
of eta is therefore divisible by the discriminant equation delta.

Conversely delta multiples vanish on Delta. Since delta is invariant,

    ker Ev_s=delta Hom_G(A tensor D5,T),
    dim ker Ev_s=3,    dim im Ev_s=7.                 (S8)

The raw C5-equivariant fiber target has dimension thirteen, not seven;
seven is the image dimension of the cubic family space. Its O(3) character
depends on the square eigenline and is retained. The dimension thirteen
follows regardless of that character because D5 restricts to the regular
C5 module. No actual value or nonzero image of the physical eta is inferred.

### 4.3 The two kernels meet trivially

Suppose both observations vanish. By (S8), eta=delta ell for an equivariant
h-linear, a-linear family ell. Since delta is nonzero at every semisimple
axis, (S7)'s zero at p implies ell vanishes on all six axes. Their nonzero
representatives span A (their span is nonzero and G-stable, and A is
irreducible). A linear map zero there is zero. Therefore ell=eta=0,
proving (S3). The chosen axis and square need not be associated.

No ordinary value on one h vector suffices for this argument: both tests
refer to the whole source-family map. This is also not PR658's ideal-sheaf
jet test; eta is an ordinary T-valued cubic, with no imposed I_Sigma factor.
The two observation maps together have a ten-dimensional image; the separate
image dimensions six and seven must not be added as independent counts.

## 5. Retain the varying physical multiplier in the observations

Use the PR866 identity, with x denoting the base point on L=P(W), not the
direction a in P(A):

    error(a,h;x)=rho_AB-rho_AA=-a(x)^3 h eta(a,h).     (S9)

The binary form h belongs to D5=Sym^4 U, eta to Sym^12 U, and the error to
Sym^16 U with its prescribed base line. Thus error is quadratic in h even
though eta is linear in h. A linear observation on the h-family cannot
silently replace the actual quadratic norm-error family.

For any linear map L:D5->Sym^12 U, define the universal multiplication map

    J(L)(h)=h L(h),
    J:Hom(D5,Sym^12 U)->Hom(Sym^2 D5,Sym^16 U).       (S10)

This is injective. Indeed choose only FORMAL coefficient variables H_j for
the universal quartic h=sum H_j m_j. The polynomial ring in H_j and the
binary variables is an integral domain; its nonzero universal h annihilates
no nonzero polynomial L(h). Thus h L(h)=0 implies L(h)=0 coefficientwise.
Equivalently each diagonal H_j^2 coefficient is m_j L(m_j); every nonzero
binary monomial m_j is a non-zero-divisor. The polarized convention is
J(L)(h1,h2)=(h1 L(h2)+h2 L(h1))/2.

After prior globality, eta is constant in the L direction, as in PR866.
For any formal choice of p,s as in Section 4, there exists a nonempty open
set of x with p(x)s(x) nonzero: two nonzero binary quadratics have only a
finite union of zero loci. At ANY such x, equality of the entire binary
degree-sixteen error vectors AS QUADRATIC FAMILIES IN h at p and s implies,
by (S9)-(S10), Ev_p eta=Ev_s eta=0. Theorem (S3) then forces eta=0 globally
as a family. Conversely eta=0 gives both equalities.

This is a fixed-base-fiber calibration theorem with two parameter-orbit
tests and the varying multipliers fully retained. It chooses no actual
point, evaluates no source, and does not produce the independent reference
rho_AA. At a base fiber where either parameter quadratic vanishes, that
parameter's norm observation gives no such conclusion. With unproved
globality, equivariance, degree bounds, or an unauthenticated reference,
the calibration theorem cannot be applied.

## 6. Exact scope of the advance

Unconditionally relative to PR815/866's stated packet hypotheses, the
thirteen-dimensional reconstruction blind space remains: actual coherent
equivariance of the chosen response packet is missing. The new proven
interface says precisely what that extra certificate buys: invariant-output
vanishing, at most ten equivariant family parameters, and an injective
two-orbit full-source calibration with the physical multiplier intact.

The package does not prove actual family-map equivariance, compute physical
rows, select a source or point, shrink the actual source image, establish
rho16/beta4, exclude a geometric source, or repair the original theorem.
The companion character/multiplier verifier is a bounded reproducible
diagnostic for the universal arithmetic, not Lean certification.
