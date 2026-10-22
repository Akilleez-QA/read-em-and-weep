# The smallest rank-two first quotient is impossible

## Result and scope

In the hypothetical maximal rank-three Gauss plateau (k,l)=(3,1),
with rank-two dual cubic image, the first quotient

    A0 = E/K = O(2) + W' O(-1)

is impossible. This excludes all four primal types surviving the
(n,e)=(4,2) section-envelope test. The other four first quotients and
the rank-one dual-image branch are not excluded. In particular the
established bounds SF >= 3 and positive-square rank >= 27 are unchanged.

The proof uses actual derivative kernels, equivariant bundle Hom spaces,
and canonical polynomial evaluation kernels. It does not assume
quadratic-section injectivity from l=1, horizontal equivariant splittings,
or a lift through a proposed extension. No actual coefficients, points,
source matrices, rank experiments, or parameter scans are used.

## 1. Inputs and two forced splittings of K

Use EXTREMAL-31-FIVE-QUOTIENT-SECTION-ENVELOPES.md and its verifier.
Write K2=E^{--} and F0=E^{---}; these have ranks 11 and 8, while K has
rank 14. Global H0(E(1))=0 is an established input. The cited test proves
H0(K(2))=0 and leaves exactly the following coefficient tuples:

    (0,0,1,1,0,1,0,0), (0,1,1,1,0,0,0,0),
    (1,1,1,0,0,1,0,0), (1,2,1,0,0,0,0,0).

Put X=H0(K(3)). In the first and third types H0(E(3))=W'+S4+2T6;
in the second and fourth it is W'+2T6. The actual quotient sequence,
and the previously proved derivative envelope, give

    H0(E(3))-2T6 <= X <= min(H0(E(3)),W'+W+S4).

Both inequalities are in irreducible multiplicity order, and their
bounds agree. Therefore X=W'+S4 or W', respectively. The equivariant
Euler characteristics are

    chi_G(K(3))=W',
    chi_G(K(4))=V+2P4+D5.                              (1)

Consequently H1(K(3)) is S4 or zero. Since H0(K(2))=0, all splitting
summands of K have degree at most -3 and its degree -3 coefficient is X.

If H1(K(3))=0, all degrees are at least -4, and (1) yields

    K = W' O(-3) + (V+P4+D5) O(-4).                    (2)

If H1(K(3))=S4, positivity of the splitting contributions to H1 says
that its entire tail below degree -4 is either S4 O(-5) or O(-8).
For clarity, this is a finite abstract statement: rank K=14 and
 deg K=-54, with all degrees at most -3, bound a possible degree -j
by j<=15. For 5<=j<=15 and the required central parity, the only
irreducible blocks whose nonzero R Sym^(j-5) W is bounded by S4 are
(j,R)=(5,S4),(8,1). The companion verifies this enumeration.
The first choice would force the degree -4 coefficient to be
V+P4-A, which is not a representation. The second gives

    K = (W'+S4) O(-3) + (V+P4) O(-4) + O(-8).         (3)

Thus these are forced splittings, not proposed extensions.

## 2. Determine the actual first derivative kernel

The actual derivative is

    delta: K -> A0(-2) = O + W' O(-3),
    ker(delta)=K2,

and its generic rank is three. Its induced map on cubic sections has
zero kernel. Indeed the next derivative and H0(F0(3))=0 inject
H0(K2(3)) into H0((K/K2)(1)), which embeds in
H0(A0(-1))=W. But H0(K2(3)) is also a subrepresentation of X,
and neither possible X contains W.

It follows that delta restricts to a nonzero scalar isomorphism on
the W' O(-3) summand, onto the W' O(-3) target. Its component from
that summand to O is zero, since Hom_G(W',Sym^3 W)=0.
This actual isomorphism allows elimination of all other components
into the low target by a triangular automorphism of the source.
It does not alter their components into O. This is a legitimate
kernel computation, not an assertion of a horizontal splitting.

In (2), the only remaining summand admitting an equivariant map to O
is D5 O(-4). Its Hom space is one-dimensional, because D5=Sym^4 W.
The scalar is nonzero by generic rank three. Its map is therefore the
standard, everywhere-surjective polynomial evaluation. The usual
SL2-equivariant evaluation exact sequence, restricted to G, gives

    ker(D5 O(-4) -> O)=S4 O(-5).

Thus the actual kernel is

    K2 = (V+P4) O(-4) + S4 O(-5).                     (4)

In (3), only S4 O(-3) admits a map to O. In particular,
Hom_G(V,Sym^4 W)=Hom_G(P4,Sym^4 W)=0 and
H0(O(8))^G=0. The nonzero S4 map is again evaluation, with kernel
A O(-4). Hence

    K2 = (A+V+P4) O(-4) + O(-8).                      (5)

In both cases delta is surjective as a sheaf, not just generically.
Therefore the actual quotient K/K2 is O+W' O(-3).

## 3. The next derivative has rank at most one

The actual next derivative must have generic rank three:

    K2 -> (K/K2)(-2) = O(-2) + W' O(-5).             (6)

But its component into W' O(-5) vanishes identically in both cases.
For (4), degree excludes maps from the degree -4 blocks, and the
remaining Hom is Hom_G(S4,W')=0. For (5), degree again excludes the
-4 blocks, and the remaining Hom is

    Hom_G(O(-8),W' O(-5))
      = (W' Sym^3 W)^G = Hom_G(W',S4) = 0.

Thus (6) factors through the single line O(-2), and its generic rank
is at most one. This contradicts rank three at K2, an interior stage
of the stated plateau. The smallest quotient is excluded.

## Reproduction

Run:

    python3 verify_extremal_31_small_quotient_exclusion.py

The verifier imports and executes the existing section-envelope
certificate without modifying it, checks all four forced section
representations, the tail enumeration, both K coefficients, the
required Hom vanishings and the polynomial-evaluation character
identities. The sheaf kernel arguments are supplied above; the script
does not pretend that abstract character arithmetic alone proves them.
