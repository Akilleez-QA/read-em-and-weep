# A generic parameter detects the complete equivariant normalization family

Conditional structural corollary of PR889 at
`72ac7ecc5447415fa8452f12ed6ec16921a600f4`.

This is a written representation-theoretic argument, not Lean certification.
No actual HM source, parameter, base point, coefficient, matrix, derivative,
or instance rank is selected or evaluated. The actual coherent-action,
source-family, globality, and reference-authentication requirements of PR889
are unchanged.

## 1. Fixed universal representations

Work over the complex numbers. Let G=A5, or equivalently use the even
representations of 2.A5. Keep the negative quadratic representation A and
the inequivalent positive quadratic representation V distinct. Write

    S = Sym^3 A = A + V + P4,
    D = D5 = Sym^4 U,
    T = Sym^12 U = 1 + V + P4 + D5,  U=Wprime,
    H = Hom_G(S tensor D,T).

PR889 proves the displayed decompositions and

    dim Hom_G(A tensor D,T) = 3,
    dim Hom_G(V tensor D,T) = 3,
    dim Hom_G(P4 tensor D,T) = 4.

In particular dim H=10. The decomposition of S is multiplicity-free.
Denote its three canonical isotypic projections by pi_A, pi_V, pi_P.
For a nonzero vector a in A define

    J(a) = { R in {A,V,P4} : pi_R(a^3) is nonzero },
    S_a = span{ (g a)^3 : g in G }.

Here a^3 is an element of the primal representation Sym^3 A. No
identification between polynomial functions and their duals is needed.
The zero/nonzero conditions and all conclusions depend only on [a] in P(A).

For F in H define its complete source-family observation at a by

    Ev_a(F):D -> T,    Ev_a(F)(h)=F(a^3 tensor h).

This is a T-valued linear map on the ENTIRE source representation D,
not an observation at one selected source vector and not one scalar
functional on the positive binary coefficient vector.

## 2. Exact observation-kernel theorem

For every nonzero a,

    S_a = direct sum of R over R in J(a),                         (G1)

and, using the canonical direct-sum decomposition of H,

    ker Ev_a = direct sum over R not in J(a) of
                   Hom_G(R tensor D,T).                         (G2)

Consequently

    dim ker Ev_a = 3*[pi_A(a^3)=0] + 3*[pi_V(a^3)=0]
                    + 4*[pi_P(a^3)=0],                          (G3)
    dim im Ev_a = 10 - dim ker Ev_a.                            (G4)

The brackets are indicator symbols. Equations (G3)-(G4) are universal
conditional dimension formulas; they do not claim that every formal
combination of indicators occurs, or calculate an actual physical rank.

### Proof

Finite-group representations over C are semisimple. A G-stable subspace
of a multiplicity-free direct sum of pairwise inequivalent irreducibles
is a direct sum of some of those irreducibles. The submodule generated
by a^3 must contain R precisely when its projection to R is nonzero.
For example, the central isotypic projectors belong to C[G], so applying
pi_R to a^3 keeps the result inside S_a; a nonzero vector in the
irreducible R generates all of R. This proves (G1).

Suppose Ev_a(F)=0. For every g in G and h in D, equivariance gives

    F((g a)^3 tensor h) = g F(a^3 tensor g^-1 h) = 0.

Since h varies through all of D, F vanishes on S_a tensor D. The converse
is immediate. Thus the kernel consists exactly of maps which factor
through (S/S_a) tensor D. The multiplicity-free direct-sum decomposition
identifies those maps with the right side of (G2). Taking the three
dimensions 3,3,4 proves (G3)-(G4).

Notice why full source-family data matter: the displayed equivariance
identity uses g^-1 h, not a single unchanged source input.

## 3. A nonempty open of individually separating parameters

Let

    Omega = { [a] in P(A) : pi_A(a^3), pi_V(a^3), pi_P(a^3)
                              are all nonzero }.

Then Omega is a nonempty G-stable Zariski-open subset of P(A). For every
[a] in Omega, Ev_a is injective on the ten-dimensional space H.

### Proof

For each R, the map a -> pi_R(a^3) is a homogeneous cubic polynomial
map. It is not identically zero: otherwise pi_R would vanish on every
pure cube, and pure cubes span Sym^3 A by polarization in characteristic
zero, contradicting the nonzero summand R. Each zero locus is therefore
a proper closed cone. P(A) is irreducible, so the intersection of the
three nonempty open complements is nonempty. Equivariance makes it
G-stable. On this open J(a) contains all three irreducibles, and (G2)
gives ker Ev_a=0.

This is an existence theorem and a symbolic criterion, not a choice of
an actual parameter. It does not certify that a supplied physical packet
is defined, polynomial, and equivariant over the full homogeneous source
module, or that it permits any particular parameter to be used.

## 4. What the special two-orbit theorem sees

PR889 identifies the semisimple-axis vanishing cubics with P4, and the
C5-fixed-square vanishing cubics with delta A. Thus its two special
observations have exactly the missing-channel patterns

    axis:  J(p) = {A,V},      kernel dimension 4, image dimension 6;
    square: J(s) = {V,P4},    kernel dimension 3, image dimension 7.

The first pattern and second pattern are disjoint in their invisible
channels. Their combined observation is therefore injective, as PR889
also proves geometrically. The shared visible coefficient space has
dimension three, namely Hom_G(V tensor D,T). This explains why the
combined dimension is 10 rather than 6+7=13.

More formally, let H_A,H_V,H_P denote the 3,3,4-dimensional direct
summands of H. Axis data identify H/H_P with H_A+H_V; square data identify
H/H_A with H_V+H_P. Each data space has its induced quotient map to H_V,
and the image of the joint observation is their fiber product over H_V.
This does not impose a canonical equality between raw binary coordinates
at different parameter points; the quotient maps use the specified
evaluation identifications and their line fibers.

The generic theorem does not invalidate the useful special-orbit theorem.
The special test sites have explicitly controlled geometry and stabilizers,
whereas applying the generic theorem requires a certificate that the
parameter lies in Omega. Neither result supplies actual observations.

## 5. Conditional physical calibration with the multiplier retained

Assume all of PR889's physical-family gates, including prior globality,
coherent G-equivariance, cubic dependence on a, linear dependence on h,
canonical or independently compared correction, full homogeneous-source
image membership, and independently authenticated reference data.
Then the mixed error has the certified form

    error(a,h;x) = -a(x)^3 h F(a^3 tensor h),                     (G5)

where x is a point of the negative base line P(W), not a positive binary
evaluation point. Fix abstractly any [a] in Omega and any x with a(x)
nonzero. Such x exist because a is a nonzero binary quadratic.

The following are equivalent:

1. F=0 globally as an equivariant family.
2. The entire binary degree-sixteen error vector at (a,x) is zero as a
   quadratic polynomial family in h.

Indeed PR889's injective universal multiplication map L -> [h -> h L(h)]
and the nonzero scalar a(x)^3 turn condition 2 into Ev_a(F)=0. Section 3
then gives F=0. The reverse implication is immediate.

Thus one generic PARAMETER's complete h-family, at one eligible base
fiber, is structurally sufficient. The varying source multiplier remains
inside the quadratic family. No scalar numerical binary evaluation, no
source-zero cancellation, and no observation at an uncertified reference
is substituted for this full-vector family equality.

## 6. Evidence and scope

The only specialized representation and physical inputs are the exact
PR889 proof and its six pinned sources. In particular the present argument
does not import the fourth-gate ideal-sheaf jet theorem as an ordinary
value theorem, nor infer actual global-operator extension from trace gluing.

The generic observation criterion and the exact isotypic-support formula
are additional consequences not stated in the inspected PR889 package or
its six source copies. This is a bounded comparison of those documents,
not a claim of novelty against the full literature or repository history.

No actual coherent physical family is authenticated here, no calibration
is performed, and no geometric source is excluded. The unconstrained
thirteen-dimensional reconstruction ambiguity remains unless PR889's
extra family gates are independently established.
