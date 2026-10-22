# The rank-one cubic image in (1,3) is impossible

## Result and scope

In the remaining maximal rank-three Gauss profile (k,l)=(1,3), the
canonical cubic derivative image J cannot have rank one. Together with
the established rank-three cubic-image exclusion, this forces rank J=2.
This does not exclude (1,3), generic SF rank three, or improve the frozen
global lower bounds. No actual coefficients, points, instance matrices,
rank experiments, or scans are used.

Crucially, J is NOT identified with the full actual derivative image I.
The latter has rank three throughout this argument. Write S for the
saturation of I in Q(1), and C for the saturation of J in Q(1).
All splittings below are equivariant bundle splittings, not horizontal
splittings.

## 1. The high line

The actual source is

    E(3)=U O + V O(-1),      U=W'+2T6, dim U=14.

Persistence gives H0(E^-(3))=0, so U injects into H0(J). If rank J=1,
global generation and central parity give J=O(e) for odd e>=13.
The positive actual Q* identities from
ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md are

    M3=sum R_j Sym^(j-1) W,
    M2=sum_(j>=2) R_j Sym^(j-2) W.

Every individual block must fit both positive character budgets. As
j dim R<=54, this is finite and exhaustive. The maximum eligible j is
28, so the maximum ordinary degree in Q(1) is 29. Combining e<=29,
U<=Sym^e W, and nonzero equivariant Hom(O(e),Q(1)) leaves exactly

    e=17,19,29.

The only receiving Q* blocks for these lines respectively are

    e=17: (16,1), (17,W), (28,1);
    e=19: (18,1);
    e=29: (28,1).

The saturated line C=O(f) also has U in its sections and a nonzero
map to Q(1), so f belongs to the same three-element list. The torsion
length f-e is an invariant effective divisor degree. The divisor gap
and semigroup <12,20,30> show that the possible pairs are only

    (e,f)=(17,17),(17,29),(19,19),(29,29).

This does not assume that J is saturated.

## 2. A degree bound on the full saturated image

The reversed dual plateau has ranks 4,7,10,13,16. Let Kd=(Q*)^- be
the rank-ten stage, Kd2 its rank-seven kernel, and L0 the rank-four
stage. With A=Q*/Kd, negative-transpose duality gives

    S=A*(1),             deg Kd=deg S-57.

This is the saturation of the FULL rank-three derivative image, not
of J. The two interior derivatives and lowest-stage persistence give

    H0(Kd(3)) <= H0(S*(2))+H0(S*)

in representation order. Explicitly, with D=deg S,

    chi_G(Kd(3))=T6-2W-S4-chi_G(S*(4)),
    chi(Kd(3))=D-17.                                  (1)

For clarity, the first target is A(1)=S*(2); the second derivative
has target (Kd/Kd2)(1), which embeds into A(-1)=S*.
H0(L0(3))=0 closes the two-step section bound. This uses no assertion
about derivatives beyond either plateau endpoint.

Since E(4) generically surjects S(1), every ordinary degree of S is
at least -1. Since C=O(f) embeds into S with f>=17, at least one
ordinary summand of S has degree >=17. That summand contributes
nothing to either H0(S*(2)) or H0(S*). Each of the other two summands,
whose degrees are at least -1, contributes at most 4+2=6. Therefore

    D-17 <= 12,             D<=29.                    (2)

This is a new bound appropriate to the quartic complement: it does
not incorrectly assume that S itself is globally generated.

## 3. Splitting off the saturated high line

Because S and C are saturated in Q(1), B=S/C is a rank-two bundle.
The map U O -> S lands in C; thus the remaining source gives a
GENERICALLY surjective map

    V O(-1) -> B.                                     (3)

It follows that both ordinary degrees b1,b2 of B are at least -1.
Since b1+b2=D-f<=12, each is at most 13. In particular
H1(O(f-bi))=0 for f>=17, so the sequence

    0 -> O(f) -> S -> B -> 0

splits, and may be split equivariantly by averaging. Consequently

    S=O(f)+B,     f in {17,19,29},
    deg S<=29,   every degree of B lies in [-1,13].    (4)

Each equivariant irreducible block R O(b) of B must satisfy

    dim R<=2, center(R)=(-1)^(b+1),
    Hom_G(V,R Sym^(b+1) W) != 0.                     (5)

Only generic surjectivity is needed for these necessary conditions;
we do not assume (3) is everywhere surjective or classify its kernel.

## 4. Exhaustive eight-candidate contradiction

Enumerating all rank-two sums satisfying (4)-(5) yields the following
necessary possibilities. The last column gives a negative irreducible
multiplicity in

    H0(S*(2))+H0(S*)-chi_G(Kd(3)),                    (6)

which must be genuine by (1).

| f | B | D | T6 multiplicity in (6) |
|---|---|---|---|
| 17 | W' O(2) | 21 | -1 |
| 17 | W O(4) | 25 | -2 |
| 17 | W O(6) | 29 | -2 |
| 17 | W' O(6) | 29 | -2 |
| 17 | O(5)+O(5) | 27 | -2 |
| 19 | W' O(2) | 23 | -1 |
| 19 | W O(4) | 27 | -2 |
| 19 | O(5)+O(5) | 29 | -2 |

There is no candidate with f=29. Every listed candidate violates (1),
so rank J=1 is impossible. The enumeration is deliberately an overlist:
it need not establish that any displayed B admits a generically
surjective map (3), or that any full target splitting realizes it.

## Reproduction and preserved limitations

Run python3 verify_extremal_13_rank_one_cubic_image_exclusion.py.
The verifier imports and reruns the predecessor exact-character
reduction, checks all eligible individual target blocks, line degrees,
saturation defects, every possible rank-two complement, and all eight
negative character multiplicities. Sections 2-3 supply the geometric
arguments; finite arithmetic is not a substitute for those arguments.

The original files are unchanged. The cubic-image rank-two branch and
all unrelated unresolved global bounds remain open.
