# Source2 has no nontrivial invariant-product-compatible pencil idempotent

## Result and boundaries

Work over C and retain all actual-source hypotheses and fixed-variable
identifications of PR790 and PR791. Let N be the actual source2 negative
pencil, C_N its full degree-preserving G-equivariant endomorphism algebra,
and Q:N2 -> N4 the canonical invariant positive-coordinate quadratic
multiplication. Define

    D_Q = {e in C_N : e4 Q = Q e2}.

Then, for either residual quotient-coupling class and every balanced endpoint,

    D_Q = C·1 direct-sum J_Q,
    J_Q = D_Q intersect J,    J_Q^2=0,    0 <= dim J_Q <= 1.       (1)

Here J is the two-dimensional radical of C_N. In particular D_Q is local,
commutative, has dimension one or two, and its only idempotents
are zero and one. Equivalently no nontrivial simultaneous decomposition
of the fixed negative pencil can be preserved by Q.

This is a NEW restriction on compatibility with the positive invariant
product, not a new calculation of C_N, not scalarity, and not exclusion
of source2 or its catalogue pair. It does not concern endomorphisms of the
entire HM module. A surviving nilpotent in J_Q is not excluded here.

## 1. Exact published inputs and the actual-map interface

INPUTS.json records immutable commits, public paths, SHA-256 hashes and
Git blob identifiers; inputs/ contains exact copies of the originals.
The direct dependencies in Akilleez-QA/read-em-and-weep are:

- PR790, af0e03d26da5e47d18ae732291aca46f4d448dc5,
  research/hm/source2-first-constant-block/PROOF.md. Section 6 identifies
  the reconstructed maps with the original actual negative multiplications,
  with the same fixed variables, not just equal characters.
- PR791, 2cd033a4a5ba549d07330427cd779364cb83c0fb,
  research/hm/source2-pencil-endomorphism-algebra/PROOF.md. This gives
  the full algebra, its two-dimensional square-zero radical and fully
  faithful fixed-pencil reconstruction, including noninvertible maps.
- PR795, 3f811311d76914a555c7e7d0c5b887b41805aa6c,
  research/hm/source2-radical-filtration/PROOF.md. Sections 2-3 and 6
  give the genuine first block, residual evaluation sequence and endpoint
  characters. Its quotient splitting is NOT used as a horizontal splitting.
- At eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c in
  research/hm/order-four-quadratic-load/:
  POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md and
  POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md.
  They give the actual invariant image and global first vanishing for
  the exact pencil q0+t a, for every negative quadratic a in Sym²W.
- At 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0 in the same directory,
  ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md. Under its proved
  invariant-cone and uniform cubic/quintic filtration hypotheses, the
  SAME actual second Bockstein is a nonzero quadratic family on A.
- PR935, a7707ba3e25592023eb69cc15686aa4ee1fdcb7c,
  research/hm/profile11-source127-cdf-bockstein-rigidity/PROOF.md.
  We acknowledge its surjective-block obstruction argument. We repeat
  that general argument with the distinct source2 blocks below; none of
  its c-d-f-specific algebra or source hypotheses is transferred.

All upstream hypotheses of these published results remain in force.
No actual coefficient, parameter, derivative, matrix or instance rank is
selected or evaluated. This is a conditional written mathematical proof,
not a proof-assistant certificate.

Write A,V,P,D for irreducibles of dimensions 3,3,4,5. The actual invariant
multiplication theorem supplies embedded kernel, image and cokernel types:

    ker Q=A+D,   im Q=2V+3P+3D,   coker Q=P.                    (2)

In particular N2 has precisely one A. PR790 transfers the original fixed
negative linear maps to N. Every e in C_N therefore intertwines every
actual negative quadratic T_a:N2 -> N4, a in Sym²W, because it intertwines
both linear arrows and hence their compositions and linear combinations.
This statement does not extend e to any additional module degrees.

## 2. Actual source2 algebra and endpoint characters

The genuine constant first splitting reconstructs to N=N0 direct-sum NR.
The residual sequence is 0 -> NC -> NR -> N8 -> 0. When the quotient
coupling is ZERO, PR791 permits a constant gauge with R=A0 direct-sum C;
then this residual sequence itself splits as fixed pencils and

    N=N0 direct-sum N8 direct-sum NC.                            (3)

Only in that case do we use the three separate summands. For nonzero
coupling NR remains a single algebra vertex; no splitting of it is assumed.
The endpoint characters from the genuine evaluations in PR795 are:

    block     degree two                 degree four
    N0        P+D                        V+2P+D
    N8        A+V+P+D                    V+P+D
    NC        V+P+2D                     P+D
    NR        A+2V+2P+3D                 V+2P+2D.

Their total is (A+2V+3P+4D, 2V+4P+3D), of dimensions (41,37).
The source2 algebra in pencil orientation has radical arrows from N0
into NC (and hence into NR), and kills NR. This is the OPPOSITE of the
ambient Q* algebra orientation. With target scalar a, source scalar d
and b in J its triangular product is

    (a,d,b)(a',d',b')=(aa',dd', a b'+d' b).                      (4)

For zero coupling the scalar on N8 is an independent isolated factor;
for nonzero coupling a is the common scalar on NR. Thus C_N/J is C³ or
C² respectively, and J²=0 in both cases. Dimensions are five and four.

## 3. All idempotents, including radical shears

An idempotent e has diagonal bits at the algebra vertices. Write e=d0+b
with b in J, and let epsilon_s,epsilon_t be the bits at the source N0
and target NC (or NR). The equation e²=e says

    (epsilon_t+epsilon_s-1)b=0.                                (5)

If the two bits agree, b=0. Otherwise take c=b/(epsilon_s-epsilon_t).
Because J²=0, the unit g=1+c has inverse 1-c and

    g d0 g^(-1)=d0+b=e.                                        (6)

Consequently every proper idempotent is radical-conjugate to a proper
nonempty vertex-subset projector. This covers the six subsets for (3)
and the two subsets for N0+NR. The conjugating unit need not commute
with Q. We use (6) ONLY to identify image and kernel G-characters of e,
not to transfer Q compatibility to d0. If e itself is Q-compatible,
Q is block diagonal between its image/kernel decompositions, so the
character bounds below apply to those actual subspaces.

For an equivariant map of finite G representations, each image
multiplicity is bounded by the minimum of the two endpoint
multiplicities. Apply this separately to image(e) and kernel(e).
Complementary vertex subsets give the same bound.

For N0 separated from NR, the two bounds are P+D and V+2P+2D;
for NC separated from N0+N8 they are P+D and V+2P+2D again.
Their sum is V+3P+3D, dimension 30, whereas the actual image (2) has
TWO copies of V and dimension 33. Therefore none of these projectors
or their radical shears can be Q-compatible.

This disposes of both nonzero-coupling subsets and four of the six
zero-coupling subsets. Only N8 versus N0+NC remains. Its bounds are

    N8:        V+P+D,
    N0+NC:     V+2P+2D,                                      (7)

whose sum is precisely 2V+3P+3D. The N8 vertex is isolated from J, so
(5) already forces b=0 for its projector and its complement. Even
without this observation, saturation of (7) would be enough for the
argument below.

## 4. The last N8 projector contradicts the actual second Bockstein

Suppose the N8 projector is Q-compatible. Since (7) sums to the actual
image character, equality is forced constituent by constituent in both
bounds. In particular

    Q:N8_2 -> N8_4 is onto, with kernel A.                      (8)

Both N0_2 and NC_2 have no A; N8_2 has exactly one. Therefore this
kernel A is the unique A-isotypical subspace of N2, hence exactly the
actual A in ker Q, not an unverified isomorphic substitute. Every T_a
preserves the block, by the fixed negative-pencil splitting (3):

    T_a(N8_2) subset N8_4 for every a.                          (9)

Choose any linear right inverse s:N8_4 -> N8_2 of Q in (8). For k in
this A, put u=-s T_a k. Then Qu=-T_a k, while T_a u belongs to N8_4,
which is contained in im Q. Thus [T_a u]=0 in coker Q.

To identify this with the EXACT imported obstruction, rather than a
formal surrogate, recall the first-vanishing theorem. It writes k=h xi
with h in A, fixes zeta_a by a xi=q0 zeta_a, and uses correction
u0=-h zeta_a. Its canonical second class is

    beta2_a(k)=-[a h zeta_a]=[T_a u0].                         (10)

Both u and u0 solve Q u=Q u0=-T_a k. Their difference is in ker Q.
The global first-Bockstein theorem states [T_a v]=0 for EVERY v in
ker Q and EVERY a, so [T_a(u-u0)]=0. Equations (8)-(10) give beta2_a(k)=0
for all k in A and all a. This contradicts the actual nonzero A-to-P
quadratic family at the exact second-Bockstein pin.

Equivalently the entire kernel in this hypothetical surjective block
has formal lifts: on the block M(t)=Q+tT_a,

    k(t)=k-s(M(t)s)^(-1)M(t)k

satisfies M(t)k(t)=0 and k(0)=k, because M(t)s=1+tT_a s is formally
invertible. This identity explains the obstruction geometrically but
is NOT used to identify a higher gate or an unrelated lifting map.
The explicit first-correction comparison above suffices for the actual
second obstruction. No global formal splitting of the actual module
or bundle is asserted.

All proper idempotents in D_Q have now been excluded.

## 5. Polynomial idempotent separation forces scalar diagonal

D_Q is a unital subalgebra: its intertwining equation is preserved under
composition and addition. Let h in D_Q, and let Lambda be the distinct
values of its image in C_N/J. Put p(z)=product over lambda in Lambda of
(z-lambda). Then p(h) belongs to J and p(h)²=0. If Lambda has at least
two values, polynomial Chinese remaindering yields f(z) with f(lambda)
equal to zero or one, not all equal, and f'(lambda)=0 for every lambda.
Then f²-f is divisible by p². Thus f(h) is a nontrivial idempotent in
D_Q, contradicting Sections 3-4. Consequently every element of D_Q
has a common scalar lambda at all algebra vertices. Subtracting lambda·1
leaves an element of J_Q. This proves (1).

The ideal J_Q has square zero, so this algebra is commutative and local;
(lambda·1+j) is invertible exactly when lambda is nonzero, with inverse
lambda^(-1)·1-lambda^(-2)j. Section 6 further excludes dim J_Q=2. No inference forces J_Q to
vanish. For example,
C[epsilon]/(epsilon²) is nonscalar but has no nontrivial idempotents.
This example is only a logical negative control, NOT an actual source2
realization or a claim that every possible J_Q dimension occurs.

## 6. The whole radical cannot remain compatible

There is a stronger obstruction than absence of idempotents. PR795 proves
that the full radical annihilator is a genuine fixed-negative subpencil,
with endpoint characters and dimensions

    U=Ann_J N2=A+2V+2P+3D,    dim U=32,
    Z=Ann_J N4=2V+2P+2D,     dim Z=24.                        (11)

Suppose J_Q=J. Every j in J preserves ker Q, because Q j2=j4 Q.
The actual ker Q=A+D is multiplicity-free with nonisomorphic irreducible
summands. Since j2 is G-equivariant, its restriction is scalar on each;
since j²=0, both scalars are zero. Hence

    ker Q subset U.                                          (12)

For x in U and j in J, j4 Qx=Q j2 x=0. Thus Q(U) subset Z. The
restricted kernel is exactly ker Q, of dimension eight, by (12), so
Q|U has rank 32-8=24. Equation (11) makes Q:U -> Z onto. In fact the
characters also agree: U-(A+D)=2V+2P+2D=Z.

The annihilator is a subpencil: if J kills a vector, then it kills its
image under either negative arrow because every j intertwines that arrow.
Consequently T_a(U) subset Z for all negative quadratics a. Its kernel
contains the unique actual A in ker Q. Apply the Section 4 right-inverse
argument to U and Z. That argument requires only surjectivity and
preservation of these two subspaces, NOT a direct-sum complement or an
idempotent. It again forces the same actual second Bockstein to vanish
on A, contrary to the pinned geometric nonvanishing theorem.

Therefore J_Q is a proper subspace of the two-dimensional J, so

    dim J_Q <= 1.                                            (13)

Together with Section 5, this proves the strengthened result (1). If
J_Q is nonzero, choosing any nonzero j identifies D_Q abstractly with
C[epsilon]/(epsilon²). Otherwise D_Q=C. We do not assert that either
alternative is actually realized, identify the possible compatible
line, or exclude source2.

## 7. Evidence and scope

verify.py checks all eight proper diagonal subsets, exact constituent
bounds and unique-A saturation, the radical conjugation algebra over
bounded exact rational test inputs, and the formal second-correction
identity in a universal block model. It also checks the exact annihilator saturation used in Section 6.
These diagnostics support the
written universal argument; they do not prove the imported geometric
nonvanishing theorem or instantiate any actual source.

The necessary source2 catalogue pair remains (E13,Q21), and this theorem
makes no change to the four-pair frontier. It removes the entire
semisimple non-scalar compatibility alternative, while retaining a
possible one-dimensional compatible square-zero radical.
