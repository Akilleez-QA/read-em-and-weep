# The extremal (3,1) dual cubic image has rank at most two

## Result and scope

In a hypothetical maximal rank-three Gauss plateau (k,l)=(3,1), the
restricted dual cubic derivative

    psi: T6 O -> E*(1)

has generic rank one or two, never three. If its rank is one, its image
is O(9) or O(11). These are necessary restrictions, not realizations or
an exclusion of the entire profile. The generic SF lower bound remains
three and the positive-square lower bound remains 27.

This is a new argument for (3,1), not a reuse of a closed (3,2) case.
Only universal characters, hypothetical bundle degrees, and sheaf
arguments are used. No selected coefficient, actual-instance map, rank
experiment, parameter scan, or local model is used. Frozen files are
unchanged.

## 1. Inputs and the available persistence

Use the global actual splitting constraints in
ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, including the retained
global input H0(E(1))=0 and its 28 necessary primal types. This vanishing
is not deduced from the forward length l=1. All ordinary degrees of E
are between -10 and -2. Use the cubic-corner and adjacent notes for
notation, the five necessary Q* types when k=3, and the invariant divisor
semigroup <12,20,30>. No formal type is asserted to occur.

Write the plateau as

    F0 subset F1=K2 subset F2=K subset F3=E subset F4,
    ranks 8,11,14,17,20.

Here K=E^- and K2=E^{--}. Persistence supplies exactly the needed facts

    H0(K(1))=0, H0(K2(2))=0, H0(F0(3))=0.

The dual reversed plateau has central bundle Q* at index one. Its
backward kernel Kd is at index zero, so H0(Kd(3))=0. Consequently the
restriction of beta_(Q*)(3) to the canonical evaluation bundle T6 O
is injective on global sections. Thus psi is nonzero and its image J
is globally generated, center-odd, and has rank at most three.

## 2. A finite overlist for the image blocks

Every equivariant direct summand R O(e) of J satisfies:

- 0 <= e <= 11 and dim R <= 3;
- R has central parity (-1)^(e+1);
- T6 occurs in R Sym^e W;
- R O(e) admits a nonzero equivariant map to E*(1) for at least one
  of the 28 necessary primal types.

The first bound follows from global generation and the maximal ordinary
line degree 11 of E*(1). The source is the irreducible T6, so a nonzero
projection to each image summand gives the third condition. Exact
character arithmetic leaves precisely the following individual blocks:

    V O(1), W' O(2), V O(3), W' O(4), V O(5), W' O(6),
    A O(7), W O(8), O(9), A O(9), W O(10), O(11).

These conditions deliberately overlist possible images. They do not
assert generation or injectivity for any candidate map. In particular
rank one forces O(9) or O(11), as claimed.

## 3. The two-step section inequality for a rank-three image

Suppose rank J=3. Let Sbar be its saturation in E*(1), and put
D=deg Sbar. The negative-transpose identity for the two second fundamental
forms identifies its generic subspace with the annihilator of K.
Since both are saturated,

    Sbar=(E/K)*(1), P:=E/K=Sbar*(1), deg K=D-57.

The inclusion J subset Sbar dualizes to P subset J*(1). No equality of
the image and its saturation has been presumed.

The next derivative maps are

    K(3) -> P(1),                 kernel K2(3),
    K2(3) -> (K/K2)(1),          kernel F0(3).

Moreover K/K2 embeds, as its actual derivative image, into P(-2).
Therefore persistence H0(F0(3))=0 and left exactness give

    h0(K(3)) <= h0(P(1)) + h0(P(-1))
             <= h0(J*(2)) + h0(J*).

Riemann--Roch gives h0(K(3)) >= deg K+56 = D-1. All blocks in the
list have positive ordinary degree, so h0(J*)=0. In particular

    deg J - 1 <= D-1 <= h0(J*(2)).                 (1)

Among all sums of the listed blocks of total rank three, only
J=V O(1) satisfies (1). An irreducible rank-three block other than
V O(1) has degree at least nine and no sections after dualizing and
twisting by two. A line-plus-rank-two block has degree at least thirteen
and at most two such sections. Three line blocks have degree at least
27 and none. This also covers combinations not co-occurring in any
primal type, so does not silently assume their realizability.

For J=V O(1), (1) yields 3 <= D <= 7. The saturation defect D-3 is
an invariant effective divisor degree and is less than 12. Hence D=3,
Sbar=J, and

    P=V O, deg K=-54.                             (2)

## 4. Force two more backward quotients

Since K/K2 embeds into P(-2)=V O(-2), its twist by one has no sections.
The second derivative above and H0(F0(3))=0 imply H0(K2(3))=0. Thus
H0(K(3)) injects into H0(P(1))=T6.

The actual Euler identity chi_G(E(3))=W'+2T6, together with (2), gives

    chi_G(K(3)) = W'+2T6 - V Sym^3 W = T6-S4.

The positive T6 coefficient forces H0(K(3)) to contain T6. It follows
that H0(K(3))=T6 and its derivative onto H0(P(1)) is an isomorphism.
These sections generate P(1); consequently the derivative K(3)->P(1)
is surjective as a sheaf, and

    K/K2=V O(-2), rank K2=11, deg K2=-48.          (3)

This is an actual sheaf-image assertion proved from generation, not a
claim inferred from the equality of generic ranks alone.

## 5. The forced kernel splitting makes the endpoint horizontal

Equations (2)-(3) and H0(K2(3))=0 give

    H1(K2(3))=S4,
    chi_G(K2(4))=-A+2V+P4.

All ordinary summands of K2 have degree at most -4. In its equivariant
splitting, the negative contributions to H1(K2(3))=S4 can only be
S4 O(-5) or O(-8): test R Sym^(j-5) W for j>=5, whose positive dimension
bounds j<=8. Since S4 is irreducible, precisely one of these occurs.
The first choice would make the coefficient of O(-4) equal to
-A+2V+P4, which is not genuine. The second contributes A to H1(K2(4)),
forcing

    K2=(2V+P4) O(-4) + O(-8).                     (4)

Now its derivative maps to (K/K2)(-2)=V O(-4), with kernel F0.
The only equivariant components are constant maps from the two V O(-4)
blocks. The P4 component vanishes by Schur's lemma, and the O(-8)
component vanishes because Hom_G(1,V Sym^4 W)=0. The derivative has
rank three because F1=K2 is an interior stage. Hence it is surjective
and

    F0=(V+P4) O(-4) + O(-8),
    K2/F0=V O(-4).                               (5)

The endpoint derivative takes values in (K2/F0)(-2)=V O(-6).
There is no map from the O(-4) blocks by degree; the remaining component
vanishes because Hom_G(1,V Sym^2 W)=Hom_G(V,A)=0. Thus beta_(F0)=0.
In characteristic zero a subbundle of a constant bundle with zero second
fundamental form is constant: its Grassmannian classifying map has zero
differential and is constant. This contradicts (5), whose degree is -36,
or equivalently the absence of any nonzero constant subbundle in F0.

Therefore the rank-three assumption on J is impossible.

## Reproduction

Run python3 verify_extremal_31_cubic_image_rank.py. The verifier checks
the entire individual-block overlist, every rank-three combination,
the section inequality, saturation bound, exact Euler characters, both
possible negative kernel blocks, and the final Hom vanishings. The
geometric persistence and sheaf arguments are proved above.
