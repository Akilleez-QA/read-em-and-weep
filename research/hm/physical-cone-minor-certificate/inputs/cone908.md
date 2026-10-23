# A global cone construction of the physical source response without choosing W

2026-10-23. Bounded written theorem and algorithmic interface, not Lean.
No actual coefficients, points, matrices, ranks, primitives or response values
are evaluated. PR889, PR894 and PR904 remain unchanged.

## Result and precise domain

Let C_t^j=Gamma(X,D_M^j(t)) be the COMPLETE fixed-duality trace-free monad
complex, and C_Q^j=Gamma(Q,D_M^j(4)|Q). Write d_t,d_Q for their differentials
and r for restriction. For the actual invariant cone Q=(q=0), there is a
short exact sequence of GLOBAL complexes

    0 -> C_2 --q--> C_4 --r--> C_Q -> 0.             (1)

The global cone complex computes the actual H*(B_Q(4)). In particular,

    im(d_Q:C_Q^0->C_Q^1)=r(im(d_4:C_4^0->C_4^1)).   (2)

Thus the entire global cone exact-source domain equals PR904's descended
domain. It is NOT a larger extension to arbitrary cone or ambient sources.

Fix the canonical Atiyah Z and the same coherent preceding division V and
correction b as the canonical probes, or independently compared data for
which the pinned raw-cubic identity holds. In particular q[v]=a h zeta_a.
An arbitrary division V and an unrelated correction b are not covered.
The already proved GLOBAL raw-cubic factorization gives

    s_Q=r(S),  S=a(V-bZ),
    s_Q in im d_Q                                  (3)

over the entire cubic-a/linear-h family, without choosing W or presuming
dE=S-qW. The authenticated cone physical weight-four extraction therefore
defines a source row on s_Q. This is a W-free construction of the SOURCE
RESPONSE LEG, not a cone-only construction of the full scalar rho16: the
full ambient lower projection y and its physical normalization remain.

Conversely, solving d_Q e_Q=s_Q and lifting e_Q globally produces

    W=(S-dE)/q,

a unique closed global cochain for that lift, with dE=S-qW. W is recovered,
not guessed. This does not validate an unrelated supplied W, which still
requires PR894's full compatibility certificate.

## 1. Immutable inputs and the gaps being closed

SOURCE-MANIFEST.json authenticates eight exact source copies.

- ladder, 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, Section 1:
  every SHEAF TERM D_M^j(t) has zero positive cohomology for t>=2.
  The listed terms are line bundles, K(t), K(t+1), and End(K)(t);
  the latter has the stated three-part Schur decomposition and Bott
  dominance at t+1>=3. Section 2 explains why the restricted monad
  still resolves the actual locally free F on the cone and its thickenings.
- ambient_cohomology, 4e16e69c776bd85506341b5bb785f0d8a396bd3e,
  Section 2: ACTUAL H^i(B(t))=0 for i!=1 at t=2,4, using the tail
  boundary and its dual restriction map, not just an Euler difference.
  This is a separate statement from termwise acyclicity.
- q_exact, eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c: actual positive
  kernel K=A+D5, image I=2V+3P4+3D5 and cokernel P4 for q:M2->M4,
  where M2=A+2V+3P4+4D5 and M4=2V+4P4+3D5.
- canonical_division, 2f81e3510505ad842fb9bb00ff3a667cd36ea17f,
  Section 3: before choosing w, the global fixed-probe identity
  pi[a v_h]=beta2_a(b)=pi[a b zeta_a] in coker(q)=P4.
- canonical_correction, 4e16e69c776bd85506341b5bb785f0d8a396bd3e,
  Sections 1-2: the canonical comparison is before quotienting by the
  second image, and b is a global linear sheaf map across the exceptional
  fibers. An arbitrary Schur gauge requires its own comparison.
- next_weight, 3d21e93865152ec961ceaf32d48f845399158b69, Section 3.2:
  every GLOBAL ACTUAL section of B_Q(4) has zero marked physical
  weight-four coefficient, despite H0(E4) having dimension thirteen.
- pr815, 0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42, Section 5:
  actual full-monad contractions, the physical source row, the lower
  nonclosed projection y and the affine scalar response formula.
- torsor904, b5999dfd50f8469a5d686f331fdf653cbb3be785: source-row
  descent on r(im d_4), compatible-W invariance, and its strict domain
  and physical-normalization boundaries.

Only termwise acyclicity and local resolution from ladder are used to
prove (1). Its later existence assertion for E or W is NOT used to prove
(3). The construction is therefore not a circular appeal to its output.
U=Wprime remains the positive binary representation, with A=Sym^2 W
distinct from V=Sym^2 U. Physical inversion, not the separate cone Serre
involution, defines the positive sector inherited from PR894/904.

## 2. Global restriction really is surjective, degree by degree

Each D_M^j is locally free: it is a term of the full Hom complex of a
finite locally free monad, followed by the fixed characteristic-zero
duality/trace-free direct summand. Multiplication by the Cartier equation
q therefore gives an exact sequence of sheaves

    0 -> D_M^j(2) --q--> D_M^j(4)
      -> D_M^j(4)|Q -> 0.                           (4)

The positive cohomology of both ambient terms vanishes by the pinned
termwise theorem, for EVERY cochain degree j. The long exact sequence
therefore gives both

    C_4^j -> C_Q^j is onto,
    H^i(Q,D_M^j(4)|Q)=0 for every i>0.              (5)

The first conclusion needs H1 of the twist-two SHEAF TERM, not merely
H1(B(2)) or a formal statement about a derived restriction. In fact
H1(B(2)) is nonzero. Confusing those two claims would invalidate (1).
The second conclusion follows from H^i(D_M^j(4))=0 and
H^(i+1)(D_M^j(2))=0. These are uniform termwise vanishings, not choices
of primitives on an open cover. The restrictions commute with d, giving
the short exact sequence of global complexes (1).

The singularity of Q does not introduce extra sheaf cohomology of the
restricted monad complex: locally M is a direct sum of F in degree zero
and split contractible complexes. This decomposition survives restriction
because all summands are locally free. Hence its restricted full Hom
complex is quasi-isomorphic to End(F_Q), and its retained summand to B_Q.
Equivalently Hom and restriction commute termwise for locally free terms.
It is not the Ext complex of an ambient pushforward on X.

Finally the hypercohomology spectral sequence has only its sheaf-H0 row
by (5). It collapses and identifies, naturally,

    H^j(C_Q,d_Q)=H^j(Q,B_Q(4)).                     (6)

This proves the GLOBAL cochain comparison required here. Local exactness
alone, or a hypercohomology-zero class without this comparison, would not
justify a global primitive in C_Q^0.

## 3. Entire global cone image and its actual obstruction

Commutativity r d_4=d_Q r always gives r(im d_4) subset im d_Q. If a
global cone source equals d_Q e_Q, surjectivity C_4^0->C_Q^0 supplies a
global E with rE=e_Q. Then d_Q e_Q=r(d_4 E). This proves the reverse
inclusion in (2), with no rank comparison or local-to-global guess.
Throughout, im d_Q means d_Q Gamma(D_M^0(4)|Q), not the potentially
different space Gamma(im of the sheaf differential).

For arbitrary CLOSED positive cone sources the obstruction is not zero:
the adjoint restriction sequence and H2(B(2))=0 give

    H1(B_Q(4))_+=M4/qM2=P4.                        (7)

The same exact sequence gives H0(B_Q(4))_+=K=A+D5. Thus a closed cone
source need not be exact. For cubic-a/linear-h equivariant families the
obstruction space is Hom_G(R,P4), of dimension three, where
R=Sym^3 A tensor D5=3A+3V+3P4+4D5. This is an obstruction-family
dimension, not a dimension or rank of a concrete cone differential.

The specified S is closed, because V and Z are closed and scalar
multiplication commutes with d. The canonical raw-cubic factorization is

    pi[S]=pi[a v]-pi[a b zeta_a]=0.                 (8)

It is an equality of global polynomial families, not only a statement
on a dense set or a restricted source locus. Under the natural map (7),
(8) is precisely [s_Q]=0 in H1(B_Q(4))_+. Equation (6) now proves (3).
For this membership implication alone, H2(B(2))=0 is unnecessary:
exactness already kills the restriction of every class in im q. The
extra vanishing identifies the entire obstruction group in (7).
This argument chooses neither a W with q[W]=[S] nor an ambient E with
dE=S-qW. Both would be possible later, but are not premises of (3).

Coefficientwise the map R->ker d_Q lands in im d_Q. Exactness of
Hom_G(R,-) for finite G over C supplies one equivariant linear lift
R->C_Q^0. Polarization identifies it with a single homogeneous cubic-a,
linear-h polynomial e_Q. This uses the entire source module, not separate
pointwise primitive choices. The same finite-group averaging applies to
the restriction surjections in (5) whenever coherent family lifts are
desired. No physical contraction is made equivariant by this argument.

## 4. Direct construction of the cone physical source row

Supply an authenticated local contraction of the ACTUAL restricted monad
onto F_Q, in the fixed physical frames. For a global cone degree-zero
cochain e define

    P_i^Q(e)=(p_i^Q e i_i^Q)_0,
    f_i^Q(e)=[P_i^Q(e)]_[4],
    ell_i^Q(e)=tr(n8_i f_i^Q(e)).                  (9)

These are local matrix/coefficient maps, not intrinsic adjoints for
arbitrary nonclosed e. If d_Q e=0, however, e induces a genuine global
section of B_Q(4). The actual global-cone coefficient theorem gives
f_i^Q(e)=0. Negative-degree boundaries project to zero by the chain-map
identities of the contraction. It follows that both maps in (9) factor uniquely through
the ENTIRE global exact-source image:

    F_i^Q:im d_Q -> local weight-four matrices,
    Lambda_i^Q:im d_Q -> local degree-twelve trace coefficients,
    F_i^Q(d_Q e)=f_i^Q(e),
    Lambda_i^Q(d_Q e)=ell_i^Q(e).                   (10)

This does NOT use H0(B_Q(4))=0: that space has a positive eight-space.
The nontrivial geometric fact is that its full physical coefficient is
zero. Replacing it with an arbitrary associated-graded section or a
supported middle-block extraction would not prove (10).
Nor does it force either factor row to be zero: a primitive of a nonzero
source is not closed. The row is not a map on H1(B_Q(4)), since every
source in its domain has zero cohomology class.

If the cone contraction is the restriction of the ambient contraction
used in PR815, with the same marking and harmonic convention, then

    ell_i^Q(rE)=ell_i(E),
    Lambda_i^Q(rT)=Lambda_i(T) for T in im d_4.     (11)

Together with (2), (11) identifies (10) with PR904's descended row, now
on an independently authenticated full global cone differential model.
An independently chosen cone contraction does not automatically satisfy
this physical matching for nonclosed cochains. It requires the actual
comparison/normalization certificate; equality on induced closed sections
alone is not enough. No global invariance of the individual local row is
claimed.

In complete cone-cochain coordinates a legitimate remaining certificate
is L_i^Q=Lambda_i^Q D_Q, where L_i^Q is independently assembled from (9)
and D_Q is the FULL global cone differential. This is a construction
interface, not an evaluated row, an assumed matrix, or a claim of a
quantified computational saving.

## 5. Constructive equivalence: solve on the cone, recover W

Suppose d_Q e_Q=s_Q. By (5), lift e_Q to E in C_4^0. Then

    r(S-dE)=0.

Exactness of (1) in degree one gives a UNIQUE W in C_2^1 satisfying

    qW=S-dE.                                      (12)

This quotient denotes the inverse of the injective sheaf/global map onto
its image, not localization or pointwise division where q vanishes.
Because dS=0 and d^2=0,

    q dW=d(S-dE)=0,

and q is injective in degree two, so dW=0. Thus the recovered pair is
compatible: dE=S-qW. The converse is immediate by restriction. This is
an equivalence of actual global constructions, not a merely dimensionally
possible lift.

For entire polynomial families, each restriction and image surjection
in this argument is a fixed linear G-map between finite-dimensional
spaces. Equivariant linear sections preserve the cubic-a/linear-h
coefficient module. Division through q in (12) is unique and G-equivariant,
since q is invariant. E has physical twist four and W twist two; q has
twist two. No parameter denominator or exceptional-fiber inverse occurs.

Changing an ambient lift by E'=E+qY gives

    W'=W-dY,                                      (13)

so the cohomology class of recovered W is independent of that lift.
Different cone primitives may give the compatible torsor of PR904;
their physical coefficient and source-row value agree by (10).
Neither a primitive nor W needs to be chosen to evaluate the factor row
Lambda_i^Q(s_Q), once that row has actually been independently furnished.

## 6. The W-free response formula and the gates that remain

With the same authenticated physical normalization as the fixed ambient
lower projection y_i of PR815, the source-response formula becomes

    rho16_i=Q_i+a^3 h tau_i(y_i)-a^3 h Lambda_i^Q(s_Q). (14)

Equation (3) licenses its source-row argument before any W choice.
Equation (12) supplies a compatible ambient pair if one is later needed,
and (11) proves agreement with the original formula. PR904 ensures
independence of the compatible choice. The full ambient y_i, including
its third normal coefficient and all affine lower data, is not recovered
from this cone row. Nor are the actual local contractions, markings,
frame transport or row values constructed here.

For an arbitrary SUPPLIED W, every S-qW has the same cone restriction
s_Q, even when its ambient cohomology defect is nonzero. The cone test
therefore cannot validate that W. PR894's 27-dimensional compatibility
sector lies in im q and is invisible after restriction; its certificate
must still be checked for that supplied packet. Recovering a new W by
(12) is a different construction, not certification of the old one.

The theorem proves equality of domains, global cone exactness of the
canonical source, and a constructive W-free source-response route. It
does not claim a larger source domain, a smaller computed matrix, ambient
norm invariance, a fifth-boundary value or a complete proof repair.
