# Exact frame-transfer defect for nonclosed degree-zero cochains

New bounded interface artifact, 2026-10-23. This is an abstract proof and a new
free-word verifier, not a rerun of a historical numerical spike. It supplies no
actual Horrocks–Mumford physical weight-four row-factorization, no qZ coefficient
calculation, and no weight-sixteen affine-square calculation.

## 1. Typed statement (including twists)

Let C,D be cochain complexes. On each chart a let their contractions onto
H_C,H_D concentrated in degree zero be (i_a^C,p_a^C,h_a^C) and
(i_a^D,p_a^D,h_a^D). The only assumptions needed, separately for C and D, are

    p_a i_a = 1,
    d h_a + h_a d = 1 - i_a p_a,
    d i_a = 0,   p_a d = 0.

No assumptions h_a²=0, h_a i_a=0, or p_a h_a=0 are used. All equations are
understood after restriction to the relevant overlap.

Let E:C→D have degree zero, not necessarily be a chain map, and put

    T = d_D E - E d_C,
    M_a = p_a^D E i_a^C,
    g_ba^C = p_b^C i_a^C,   g_ba^D = p_b^D i_a^D.

Then the EXACT defect, with both signs positive, is

    D_ba := M_b g_ba^C - g_ba^D M_a
          = p_b^D (T h_b^C + h_a^D T) i_a^C.                 (1)

This formulation applies to D=C(t) without silently identifying the source and
target twists. Each summand inside the parentheses is a degree-zero map C→D.

### Proof

Insert and subtract p_b^D E i_a^C:

    D_ba = p_b^D E (i_b^C p_b^C - 1) i_a^C
           + p_b^D (1 - i_a^D p_a^D) E i_a^C
         = -p_b^D E d_C h_b^C i_a^C
           + p_b^D h_a^D d_D E i_a^C.

The omitted terms vanish by d_C i_a^C=0 and p_b^D d_D=0. Substituting T into
both surviving terms gives (1), using those same two identities. This proves
(1) for arbitrary ranks and without homotopy normalization side conditions.

## 2. Inverses, cocycles, and the defect's triple-overlap law

For either complex K=C or D,

    g_cb^K g_ba^K
      = p_c^K (i_b^K p_b^K) i_a^K
      = p_c^K (1-d_K h_b^K-h_b^K d_K) i_a^K
      = p_c^K i_a^K = g_ca^K.

In particular g_aa^K=1 and g_ab^K is the two-sided inverse of g_ba^K. Expanding
and cancelling the middle terms gives the correctly typed triple-overlap law

    D_ca = D_cb g_ba^C + g_cb^D D_ba.                       (2)

It follows that the right side of (1) obeys (2), not that it vanishes. A
nonclosed cochain's projected matrices need not descend as an ordinary
Hom(H_C,H_D) section. If T=0, (1) is zero and the usual descent law holds.

## 3. What fixed-T primitive uniqueness does and does not say

If global degree-zero cochains E,E' have the same T, their difference F=E-E'
is closed. Thus p_a^D F i_a^C obeys the zero-defect descent law and defines a
global section of Hom(H_C,H_D). Consequently

    H^0(X, Hom(H_C,H_D)) = 0

implies equality of the projected matrices of E and E' in every chart. For a
twist this is the corresponding H^0(End(H_C)(t)) assertion, only when
H_D has actually been identified with H_C(t). This is uniqueness of the
projection, not uniqueness of the cochain, nor an existence theorem.

The same conclusion holds for local choices only if their projected
differences have separately been proved compatible on overlaps. Merely giving
arbitrary local primitives the same differential does NOT establish that
compatibility: their differences are locally closed, but unrelated local
closed cochains need not assemble into a global section. Global H^0 vanishing
cannot be applied to an unproved collection of local projections. In
particular this abstract lemma supplies neither physical row-factorization nor
the required actual global lifting data.

As a supplementary check, a global coboundary F=d_D K+K d_C, with K degree -1,
has p_a^D F i_a^C=0. Thus the resulting projection of a closed difference only
depends on its degree-zero cohomology class.

### Global factorization and the adjoint/scalar distinction

Let V be the vector space of GLOBAL degree-zero cochains and let Φ send E to
its collection of local matrices (p_a^D E i_a^C)_a. The codomain here is the
product of local Hom spaces; Φ(E) need not be a descended section. If the full
H^0(Hom(H_C,H_D)) vanishes, the preceding argument proves ker(d_Hom)⊆ker(Φ).
Therefore there is a unique linear map on im(d_Hom:V→ΓHom^1(C,D)) such that

    Φ = Φ_bar ∘ d_Hom.

This quotient-factorization assertion does not construct matrix rows for
Φ_bar, identify their physical weights, or prove any claimed row support.
It also applies only to differentials of global cochains, not arbitrary
collections of local primitives.

For D=C(t), if an application supplies the vanishing H^0(B(4))=0,
where B denotes the adjoint or tracefree endomorphism bundle, that premise
is NOT the full End(H)(4) vanishing. In a field
where the rank n is invertible, define the tracefree transfer by

    Φ^0(E)_a = M_a - (tr(M_a)/n) I.

Using compatible frames for H and H(t), tracefree projection commutes with
the conjugation and line-bundle transition factors. A global closed F then
has Φ^0(F) in H^0(End_0(H)(t)). Vanishing of this ADJOINT space makes Φ^0,
not necessarily Φ, factor uniquely through im(d_Hom). The scalar part can
survive. Indeed a global section s of O(t) gives the closed cochain E=s I
and transfer M=s I whenever multiplication by s is defined on the complex;
its tracefree projection is zero but its full transfer is nonzero if s≠0
and H has positive rank. At t=0, s=1 already gives the universal elementary
counterexample; for a stated twist the existence of s must be checked.
The verifier checks dI=Id and pIi=1 explicitly.

If the supplied vanishing holds only in a specified parity or equivariant
sector, the global closed differences must be restricted to that sector, and
one must justify that the induced cohomology map preserves it. Such a premise
cannot be upgraded to vanishing of the full H^0 space. This abstract interface
theorem does not authenticate any particular restricted or weighted HM
complex, physical jet frame, or claimed vanishing.

Any linear response that annihilates scalar matrices factors through Φ^0
and can inherit the factorization. For example tr(NM) is unchanged upon
removing the scalar part of M when tr(N)=0, with all source/target twists
correctly paired. No claim about the actual HM N or its pairing is made
without verifying those additional inputs.

## 4. Explicit two-term regression oracle

Take the split three-term complex

    A --inclusion--> A ⊕ H ⊕ B --projection--> B

in degrees -1,0,1. Let the base contraction pick H, and let the second
contraction be its conjugate by a chain automorphism which is the identity at
the endpoints and has middle block

    S_0 = [[1,x,y], [0,1,z], [0,0,1]].

For scalar commuting x,y,z and an entirely unrestricted degree-zero E with
middle entries E_ij, g_ba=1 and

    M_b-M_a = x E21 - z E32 - x z E31,
    p_b T h_b i_a = x E21 - x z E31,
    p_b h_a T i_a = -z E32.

Neither summand can be discarded; changing their relative sign also fails.
The y-coordinate cancels identically. Endpoint blocks E_-1 and E_1 are free,
not implicitly zero or constrained to make E closed.

## 5. Reproducible universal verifier

Run from this directory:

    python verify_nonclosed_frame_transfer_universal.py

The verifier uses only the Python standard library. Its coefficient engine is
the free noncommutative polynomial algebra with formal invertible generators
U_a and their inverses; adjacent inverse pairs are the only word reductions.
It does not use chosen field points, selected actual coefficients, symbolic
linear solves, or numerical matrices. Entries are formal blocks, so the
identities survive arbitrary size-compatible block-matrix substitutions.

It constructs three independent source frames and three independent target
frames, each with

    S_0 = [[1,X,Y], [0,U,Z], [0,0,1]],
    S_0^-1 = [[1,-X U^-1,X U^-1 Z-Y],
               [0,U^-1,-U^-1 Z], [0,0,1]],

and identity endpoint blocks. Thus g_ba=U_b^-1 U_a is a genuinely nontrivial,
noncommutative transition, not an artificially fixed identity. Every middle
block of E and both endpoint blocks are free symbols. It checks contraction
identities, the typed transfer formula for all nine chart pairs, two-sided
inverse/cocycle laws, all 27 typed triple-overlap identities, the closed limit,
and the explicit two-term example. Four missing-term/sign mutations are
required to fail. Its constructed contractions happen to be normalized; the
proof above, rather than an inference from those examples, establishes that
normalization is unnecessary.

Checked result on 2026-10-23:

    PASS: 166 exact free-word identities; 4 negative mutation tests; 0.016s
    PASS: independent source/target frames, endpoint blocks,
          all 27 triple overlaps, closed limit

This is a universal algebraic interface certificate. Any application to the
actual HM physical source, twists, and affine-square reduction still needs
its own verified input and global compatibility proof.
