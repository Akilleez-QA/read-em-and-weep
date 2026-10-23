# Section envelopes reduce the five rank-two quotient overlists

## Result and scope

Assume the hypothetical (k,l)=(3,1) rank-three Gauss plateau, with dual
cubic image of rank two. Retain the five first quotients proved in
EXTREMAL-31-RANK-TWO-DUAL-IMAGE-FIVE-QUOTIENTS.md. Write them uniformly as

    A0 = E/K = O(n-2) + W' O(1-e),
    (n,e) = (4,2), (6,2), (8,2), (6,4), (8,4).

The global input H0(E(1))=0, not the forward length l=1, supplies all
28 primal splitting types from
ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md.
A new necessary test reduces their counts as follows, in the displayed order:

    twist-two envelope:  9, 22, 23, 16, 22;
    with cubic envelope: 4, 21, 21, 10, 21.

Thus only 77 of the original 140 quotient/primal-type pairs survive
these tests. These are necessary overlists, not existence statements.
No whole quotient shape is excluded and neither the rank-one dual-image
branch nor the entire (3,1) profile is excluded. The established bounds
SF >= 3 and positive-square rank >= 27 remain unchanged.

The companion verifier uses exact abstract characters and the frozen
28-type list. It does not use actual coefficients, points, matrices,
rank evaluations, or parameter scans. Existing files are unchanged.

## 1. Keep the two meanings of the numeral two separate

Let K=E^- and let K2=E^{--} denote a different bundle, not a twist.
The plateau stages are F0, K2, K, E, F4, of ranks 8,11,14,17,20.
Persistence gives H0(K2(2))=0 and H0(F0(3))=0.
The derivative map

    K(2) -> A0

has kernel K2(2). Therefore its map on sections is injective. Put

    R = H0(E(2)),   S = H0(K(2)).

Because K embeds in E and the derivative has the stated kernel,

    S <= R,                    S <= H0(A0),
    R-S <= H0(A0(2)).                              (1)

Here <= is irreducible-multiplicity order in the semisimple representation
category of the binary icosahedral group. The last inequality is just
left exactness for 0 -> K(2) -> E(2) -> A0(2) -> 0.
It does not assert the last map is surjective on sections.
Nor does this argument assume injectivity of a quadratic-section
second-fundamental-form map at forward length one.

For all five cases, since e>=2,

    H0(A0) = Sym^(n-2) W,
    H0(A0(2)) = Sym^n W + W' H0(O(3-e)).             (2)

The global 28-type classification gives R=vV+pP4+dD5 with v,p,d>=0.
The following exact characters give explicit versions of (1):

    (n,e)  H0(A0)     H0(A0(2))   necessary bounds on (v,p,d)
    (4,2)  A          P4+D5       v=0, p<=1, d<=1
    (6,2)  D5         V+2P4       v<=1, p<=2, d<=1
    (8,2)  V+P4       2P4+D5      v<=1, p<=3, d<=1
    (6,4)  D5         V+P4        v<=1, p<=1, d<=1
    (8,4)  V+P4       P4+D5       v<=1, p<=2, d<=1.

For (4,2), S=0 because A is absent from R. Thus R really does inject
into P4+D5 in this case, as a conclusion rather than an assumption.
For n=6, S=dD5 is forced by (1), since H0(A0(2)) has no D5.
For n=8, S=vV+sP4, where 0<=s<=min(p,1), and p-s is at most two
when e=2 and at most one when e=4. These conditions prove both the
necessity and the formal sufficiency of the displayed multiplicity
bounds for the test (1), not for geometric realizability.
Exhausting the 28 types gives 9,22,23,16,22 survivors respectively.

## 2. Cubic upper and lower envelopes

Set X=H0(K(3)), E3=H0(E(3)), and C=chi_G(K(3)). The earlier five-quotient
proof established the derivative bound

    X <= B := H0(A0(1)) + H0(A0(-1)).                (3)

It follows from the derivatives K(3) -> A0(1) and
K2(3) -> (K/K2)(1), the inclusion K/K2 -> A0(-2), and
H0(F0(3))=0. In addition, the inclusion and quotient sequence give

    X <= E3,           E3-X <= H0(A0(3)).            (4)

Euler characteristic gives X-C=H1(K(3)), a genuine representation.
There is one further multiplication constraint:

    S tensor W <= X.                               (5)

To justify (5) without assuming arbitrary section multiplication is
injective, note that H0(K(1))=0, since K embeds in E. Every ordinary
splitting degree of K is therefore at most -2. Its entire twist-two
section representation S is the coefficient of its degree -2 summand.
The canonical evaluation subbundle S O(-2) embeds in K. Twisting this
inclusion by three and taking sections proves (5). No equivariant
splitting is asserted horizontal.

All ingredients can be computed without choosing a map. With U=W'+2T6,

    C = U - Sym^(n+1) W - W' chi_G(O(4-e)),
    B = Sym^(n-1) W + H0(O(n-3)) + W' H0(O(2-e)),
    H0(A0(3)) = Sym^(n+1) W + W' H0(O(4-e)).         (6)

For a primal type E=sum R_j O(-j),

    E3 = sum_(j<=3) R_j Sym^(3-j) W.                (7)

Negative Euler terms in (6) use chi(O(d))=-Sym^(-d-2)W for d<=-2;
chi(O(-1))=0. No higher-cohomology vanishing is assumed in this formula.

## 3. The finite, reproducible necessary test

For each of the five cases and each of the 28 types, enumerate only
irreducible multiplicity vectors S satisfying (1). There are finitely
many because S<=R and S<=H0(A0).
For each such S and each irreducible rho, define

    lower_rho = max(0, [S W]_rho, C_rho,
                         [E3-H0(A0(3))]_rho),
    upper_rho = min([E3]_rho, B_rho).                (8)

A representation X can satisfy all necessary constraints (3)-(5) and
Euler positivity if and only if lower_rho<=upper_rho for every rho.
Indeed necessity follows term by term, and for this abstract test
sufficiency is witnessed by X with multiplicities lower_rho. This
formal witness is not a bundle or a geometric derivative.

Keeping a primal type if at least one S passes (8) gives exactly
4,21,21,10,21 survivors. In particular 63 quotient/type pairs are
excluded from the original 140-pair overlist. The additional cubic
test excludes 15 pairs beyond the twist-two test's 92 survivors.

Run:

    python3 verify_extremal_31_five_quotient_section_envelopes.py

For every surviving tuple and its abstract S and minimal-X witnesses:

    python3 verify_extremal_31_five_quotient_section_envelopes.py --json

The coefficient order (a,b,c,d,e,f,g,h) is exactly that of the original
28-type classification; the script prints its irreducible order too.
The verifier imports and runs the previous five-quotient verifier and
its cited universal verifiers, checks the seed characters, proves the
equivalence of the explicit quadratic bounds to (1) for all 28 inputs,
and checks each retained cubic witness against every inequality.
The sheaf and persistence arguments are supplied above, not inferred
from an arithmetic assertion of geometric realizability.
