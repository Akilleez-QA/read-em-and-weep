# A fixed-minor certificate for the global cone physical response

2026-10-23. New constructive linear-algebra interface for the global cone
source leg. This is a conditional written deduction, not an evaluated HM
packet, a new source-case exclusion, or a proof-assistant certificate.

## 1. Exact dependencies and the new construction

The input copies are independently fetched at immutable commits:

- PR908, e49c18ba7bd8e6b817431b3ca13523f680d36bd1,
  research/hm/physical-global-cone-response/PROOF.md,
  SHA256 aafd5ee2b8a0a1d0876886b4db361c05d2a34cc41ab59e44ecec54580061cfcc.
- PR914, 76a68a1b0c3e4adbcc92a6c501211659d1eb9e22,
  research/hm/cone-normalization-matching/PROOF.md,
  SHA256 d5805f030eab27138adc250b98700749419e246cc7b1f5652a4c73647861a29e.

PR908 proves, for the fixed actual invariant cone Q, that the complete
finite-dimensional global differential

    D = d_Q : C_Q^0 -> C_Q^1

has exact-source image equal to the restriction of the ambient exact-source
image. It also proves that each authenticated physical extraction L_i on
C_Q^0 kills ker D, and hence has a unique factor on im D. It does not supply
an actual matrix for that factor. Its canonical entire cubic-a/linear-h
source family lands in im D before a choice of W.

The present result replaces a nullspace basis, a primitive for each source,
and a guessed extension of the response row by TWO polynomial matrix
identities and ONE fixed nonzero minor. It gives an explicit source formula,
a complete membership residual, and a change-of-pivot certificate. The
minor is in the fixed global cone differential, not in a or h. Consequently
this construction does not localize away from div(a), and introduces no
source-parameter exceptional locus. The actual differential and physical
extraction still must be independently furnished and authenticated.

PR914 supplies a separate conditional source-specific normalization gate
for an independent cone contraction. It is not used to prove the linear
algebra here. In particular the minor certificate does not prove that an
arbitrary factor row is a physical row, or that it matches the ambient y.

## 2. Typed data and the two certificates

Let k be a field and D in Mat(m,n;k). For the intended application k=C and
D is the FULL fixed global cone differential in fixed bases, not a supported
middle block or a differential specialized at a chosen source parameter.
Let R_i be the k-algebra of regular functions on an authenticated physical
chart, and let L_i in Mat(p,n;R_i) denote the separately constructed marked
physical extraction. Vector-valued weight-four coefficients and scalar trace
coefficients are both covered by choosing the output coordinates p. No
relationship between them is inferred merely from these equations.

Choose equally sized ordered row and column sets I,J, of size r, and put

    B = D[I,J],    Delta = det B != 0,
    N = E_J adj(B) P_I : k^m -> k^n.

Here P_I selects source-coordinate rows and E_J includes selected primitive
columns. If r=0 use Delta=1 and N=0; that case is valid precisely when the
certificates below force D=0 and L_i=0. No claim about actual r is made.

The required identities, in their stated full dimensions, are

    K_D := Delta D - D N D = 0,                    (M1)
    K_L := Delta L_i - L_i N D = 0.                (M2)

They involve only multiplication, addition and one determinant/adjugate.
Division by the fixed scalar Delta is used only after its nonvanishing is
authenticated. These identities must hold on ALL columns, not only columns
J; checking the pivot block alone is vacuous. M2 is a coefficientwise identity
of regular functions, not a finite collection of point evaluations.

### Rank certificate

The nonzero minor gives rank D >= r. M1 writes every column of D as a
combination of the r columns D[:,J], so rank D <= r. Thus M1 plus the minor
is equivalent to rank D=r. This avoids assuming that a convenient nonzero
minor is maximal. If the minor is too small, M1 detects it.

Define

    T = N/Delta,     P = D T.

M1 gives D T D=D. Moreover P^2=P, im P=im D, and P is the identity on im D.
Indeed P maps into im D, and for Dx its value is DTDx=Dx. This proves both
idempotence and the image assertion without a rank-nullity shortcut.

### Descent certificate

Assuming the rank certificate, M2 is equivalent to L_i(ker D)=0. M2 implies
this immediately by applying it to x with Dx=0. Conversely, D(x-TDx)=0 by
M1. If L_i kills the kernel, then L_i x=L_i T D x for every x, proving M2.
The same reasoning holds after scalar extension to R_i: over the field k
all the relevant linear sequences split, so tensoring with R_i preserves
them. No claim about arbitrary nonflat base change is needed.

Hence a verified actual L_i from PR908 necessarily satisfies M2, and M2
is also a finite independent check on a furnished candidate extraction.
Passing M2 only proves descent, not physical authenticity: many nonphysical
maps kill ker D. Authentication comes from the actual monad contraction,
physical frame/marking and coefficient extraction, as in PR908/914.

## 3. Explicit source-only formula and exact membership residual

On the licensed domain im D, the factor is

    Lambda_i(s) = L_i T s
                = L_i[:,J] adj(B) s[I] / Delta.    (M3)

Only r entries of s and the r selected extraction columns occur in this
formula. If s=Dx, then M2 gives L_iTs=L_ix; thus it is independent of the
primitive and is exactly PR908's factor, by uniqueness on im D. The formula
does not prove a quantified computational saving because neither actual
matrix dimensions nor assembly cost has been established here.

A general s belongs to im D if and only if

    K_s := Delta s - D N s = 0.                   (M4)

Necessity follows from M1. Sufficiency is constructive: e=Ts satisfies
De=s. The selected rows I of K_s vanish identically for every s, since
P_I D E_J=B and B adj(B)=Delta 1. Consequently the remaining m-r coordinates
are a complete, nonredundant-dimensional residual system. The residual map
has rank m-r, because its kernel is im D of dimension r. These are linear
algebra coordinates in C_Q^1, NOT the dimension of the closed-source
cohomology obstruction. PR908's P4 obstruction after imposing closure is
not being identified with this m-r count.

Even though L_i T is a defined linear extension to all k^m, physical use
of (M3) is only on im D. An off-image vector can have K_s != 0 and a perfectly
well-defined numerical value L_iTs. That number has no licensed physical
source-row meaning. It must not be inserted into the response formula.
For PR908's canonical polynomial source, M4 is already implied by its
geometric membership theorem. For a supplied unrelated source, M4 remains
a necessary gate. For a supplied unrelated W, even M4 on its cone restriction
cannot validate ambient compatibility, as PR908 explicitly explains.

## 4. Pivot changes, regularity and the entire parameter family

For two certified pivots alpha,beta, write T_alpha,T_beta. On an exact
source s, D(T_alpha-T_beta)s=0. M2 therefore gives

    L_i T_alpha s = L_i T_beta s.                 (M5)

Equivalently (L_i T_alpha-L_i T_beta)D=0. The two extended rows need NOT
agree on the entire source-coordinate space. Their difference can be a
nonzero functional on coker D. Thus equality on the exact image, not equality
of arbitrary ambient row representatives, is the correct pivot invariant.
The tests include a concrete counterexample to whole-row equality.

For fixed Q and fixed global-cochain bases, D, B, Delta and T are independent
of the source parameters a,h. Delta lies in k^*, so is invertible in EVERY
R_i, including at div(a). All source-family degrees are preserved by T:
if s is cubic in a and linear in h, so is e=Ts, and its extracted response
has the degrees prescribed by the actual L_i. No sourcewise Gaussian
elimination or rootwise division has occurred. No actual pivot is selected
here; the theorem says what a valid future fixed pivot must certify.

If one instead varies Q or other data so D itself varies, the result is
only valid on the locus where Delta is invertible and M1/M2 hold. It does
not assert extension across Delta=0 or constant rank there. The tests exhibit
a variable differential whose selected pivot fails under specialization.
That family is a diagnostic counterexample, not an actual HM evaluation.
For example over k[t], D=[t] and s=1 satisfy the cleared membership identity
Delta s=D N s with Delta=t and N=[1], but t e=1 has no solution in k[t].
The primitive 1/t exists only after localization. Thus a nonzero polynomial
pivot is insufficient for global integral membership; the fixed-field
scalar hypothesis (or invertibility on the stated chart) is essential.

An equivariant source-family primitive can be obtained from the fixed T
without demanding an equivariant pivot: for finite G in characteristic zero,
replace T on im D by the Reynolds average of g T g^{-1}. Since D is
G-equivariant, the averaged map is still a right inverse on im D. Its
physical value agrees with the original T because their difference is in
ker D. The physical contraction/extraction itself is not made equivariant
by this averaging argument. This optional step uses no source denominator.

## 5. Physical response and what this does not solve

When the authenticated extraction is the trace row in PR908, and the same
physical normalization as the fixed full ambient lower packet is established,
the source contribution can be written without a chosen W or a per-source
primitive as

    rho16_i = Q_i + a^3 h tau_i(y_i)
                    - a^3 h L_i[:,J] adj(B) s[I]/Delta.     (M6)

This follows from PR908's formula and M3, not from a new value of rho16.
For an independently authenticated cone contraction, PR914's full-cover
regularity, tensor compatibility, physical alignment, paired globality and
separately proved mixed-scalar gluing can certify source-specific matching.
M1/M2 do not imply any of those gates. They also do not recover full ambient
y, any normal derivative, the affine lower term Q_i, the full response
matrix, a fourth/higher obstruction value, or the original repair.

The new deliverable is a complete kernel-free certificate and explicit
fixed-minor evaluator for the previously abstract global-cone factorization.
No actual D or L_i has been assembled, no actual rank/minor/source/coefficient
has been evaluated, and no source label or witness is removed. The remaining
construction is now precisely: supply authenticated complete D and L_i,
certify one fixed maximal minor with M1/M2, retain the physical matching
certificate, then use M3 only on its exact-source domain. The reproducible
code verifies this interface on universal polynomial families and synthetic
finite-dimensional counterexamples; it is not a surrogate HM computation.
