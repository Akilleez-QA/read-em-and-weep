# The last low rank-two quotient (n,e)=(8,4) is impossible

## Result and scope

In the hypothetical rank-three Gauss plateau (k,l)=(3,1), with rank-two dual cubic image, the entire first-quotient case

    A0 = E/K = O(6) + W' O(-3)

is impossible. Together with the existing smallest- and middle-quotient exclusions, this leaves only (n,e)=(6,2),(8,2) in that branch. The rank-one dual-image branch is not excluded. The established bounds SF >= 3 and positive-square rank >= 27 remain unchanged.

The inputs are the five-quotient and section-envelope certificates and the actual Gauss kernels and persistence used by the smallest- and middle-quotient proofs. This proof uses only universal equivariant bundles, exact characters, and actual-map kernel arguments. The companion enumerates abstract irreducible multiplicities, not coefficients, points, matrices, rank evaluations, or parameter scans. Existing files are unchanged.

Write P=P4, T=T6, and S4 for the four-dimensional odd irreducible. Write Q=K2=E^{--} for the next bundle, not a twist. It has rank 11, while K has rank 14 and degree -54. All K summands have degree at most -2. The actual derivative

    delta: K -> O(4) + W' O(-5)

has generic rank three and kernel Q. Persistence gives H0(Q(2))=0. The following derivative, together with H0(E^{---}(3))=0, also gives

    H0(Q(3)) <= H0(A0(-1)) = T.                       (1)

All representation inequalities are irreducible multiplicity inequalities.

## 1. Complete tail exhaustion

The section envelopes and Euler characteristics give

    S := H0(K(2)) = vV+sP,                 v,s in {0,1},
    T <= X := H0(K(3)) <= W'+2T,
    chi_G(K(3)) = T-S4,
    chi_G(K(4)) = -A+2V+2P+D5.                        (2)

The last identity follows from the common Euler character of the 28 primal types and subtraction of A0(4); it is independently checked against each type in the companion. Thus X=aW'+tT with a in {0,1}, t in {1,2}. The degree -2 coefficient is S and the degree -3 coefficient is the genuine representation

    R3 = X - S tensor W.

The tail below degree -4 has H1 at twist three exactly

    H = X-T+S4 <= W'+T+S4.

An irreducible block C O(-j), j>=5, contributes C tensor Sym^(j-5)W. All contributions are positive. Since rank K=14, degree K=-54 and all degrees are at most -2, any j is at most 28. Central parity and this positivity leave exactly the following eligible individual blocks (their H1 contributions are shown):

    W'(-5): W'          S4(-5): S4        T(-5): T
    V(-6): T            P(-6): W'+T      D5(-6): S4+T
    W'(-7): T           O(-8): S4        V(-8): W'+S4+T
    W(-9): S4+T         W'(-9): S4+T     O(-10): T
    O(-12): W'+T        O(-14): S4+T.

The companion exhausts all multisets of these blocks whose contribution equals H, and all four choices of S for each X. For each, the actual degree -4 coefficient is forced by

    R4 = chi_G(K(4)) - S tensor Sym^2 W - R3 tensor W
                          - sum_tail C chi_G(O(4-j)).       (3)

Requiring R3 and R4 to be genuine leaves exactly thirteen splittings. Six have no map at all to W'(-5):

    X=T,  S=0 or V,  tail O(-8),                    R4=S+V+P;
    X=2T, S=0 or V,  tail O(-8)+O(-10) or W(-9),   R4=S.

The remaining seven are exactly these three families:

    A: X=W'+T,  S=0,V,or P,
       tail W'(-5)+O(-8),                         R4=S+V;
    B: X=W'+2T, S=P or V+P,
       tail W'(-5)+O(-8)+O(-10),                  R4=S-P;
    C: X=W'+2T, S=P or V+P,
       tail W'(-5)+W(-9),                         R4=S-P.

These statements include the coefficient and degree tests, not merely a list of low-map candidates. In particular P(-6), V(-8), and O(-12) need no separate rank discussion: none survives (3). Every displayed splitting has the required rank and degree.

For A/B/C the only summand admitting any map to W'(-5) is the single W'(-5) itself. Rank three forces its scalar component to be nonzero, hence an isomorphism. Its map to O(4) vanishes because W' is absent from Sym^9 W. All other low components vanish. Therefore delta's kernel is exactly the kernel of the remaining high map to O(4). We now determine it for arbitrary actual high maps, not selected ones.

## 2. Two universal sextic evaluation lemmas

Every nonzero G-stable polynomial series of degree 6 or 7 is basepoint-free: its common-zero divisor would be G-invariant, of degree at most 7, whereas every nonempty invariant divisor on P1 has degree at least 12. This uses the standard icosahedral orbit sizes 12,20,30,60. No polynomial coefficients are required.

A nonzero map V(-2)->O(4) is therefore surjective. Let L be its kernel. Then rank L=2 and degree L=-10. Its twist-two sections vanish because the associated nonzero irreducible polynomial inclusion V->Sym^6 W is injective. Thus all degrees of L are at most -3. Such a rank-two bundle has h0(L(4))<=2. But H0(L(4)) embeds in

    V tensor Sym^2 W = P+D5,

which has no nonzero subrepresentation of dimension at most two. Hence H0(L(4))=0, forcing both degrees to be -5. The coefficient is determined at twist five by

    V tensor Sym^3 W - Sym^9 W = W'.

Consequently

    ker(V(-2)->O(4)) = W'(-5).                       (4)

Likewise a nonzero P(-2)->O(4) is surjective, with kernel M of rank three and degree -12, with degrees at most -3. Therefore h0(M(3))<=2. This space embeds in P tensor W=W'+T. If nonzero it must equal W', forcing M=W'(-3)+O(-6). But this would give H1(M(3))=W, whereas

    chi_G(M(3)) = P tensor W - Sym^7 W = 0.

Since W and W' are distinct, this is impossible. Thus H0(M(3))=0, all degrees are at most -4, and rank/degree force all three to be -4. Its twist-four character gives

    P tensor Sym^2 W - Sym^8 W = V,
    ker(P(-2)->O(4)) = V(-4).                        (5)

Whenever either summand occurs in S, its high map is nonzero: otherwise it supplies forbidden sections of Q(2). If both occur, their maps combine, after scalar rescaling of the two inequivalent summands, to full sextic evaluation. Its kernel is T(-3).

## 3. Family A

### S=0

After removing the low isomorphism, the source is

    (W'+T)(-3) + V(-4) + O(-8).

The W'(-3) high map is nonzero by (1). The V(-4) high map is zero because V is absent from Sym^8 W.

If the T(-3) high map is nonzero, the first two irreducible series comprise all Sym^7 W. After independent scalar rescalings this is complete septic evaluation, with kernel (V+P)(-4). Any O(-8) high map lifts through that evaluation since its obstruction lies in H1(O(4))=0. Subtracting the lift computes the actual kernel as

    Q = (2V+P)(-4) + O(-8).                          (6)

If the T(-3) high map is zero, the W' septic pair is basepoint-free, with kernel O(-10). Adding O(-8) gives a kernel extension

    0 -> O(-10) -> J -> O(-8) -> 0.

Its equivariant extension space is H1(O(-2))=C. The zero class gives O(-10)+O(-8); any nonzero class gives W(-9), by the Euler sequence twisted by -8. Thus in this subcase

    Q = T(-3)+V(-4)+L,
    L = O(-8)+O(-10) or W(-9).                       (7)

This explicitly treats the potentially nonliftable O(-8) component; no unsupported lifting is used.

### S=V

The remaining source is V(-2)+W'(-3)+2V(-4)+O(-8). Both first maps are nonzero, the second by (1). Let J be the kernel of their sum to O(4). Equation (4) gives

    0 -> W'(-5) -> J -> W'(-3) -> 0.

This extension is nonzero. Otherwise the W'(-3) high map would lift through V(-2), whereas Hom_G(W'(-3),V(-2))=0. The invariant extension space is one-dimensional, since it is the invariant part of End(W') tensor H1(O(-2)). The nonzero extension is W' tensor W(-4)=P(-4), from the Euler sequence tensored by W' and twisted by -3. The maps from 2V(-4) and O(-8) lift through the combined evaluation because the obstructions have line degrees 0 and 4. Therefore Q again has form (6).

### S=P

Now the remaining source is P(-2)+(V+P)(-4)+O(-8). Use (5). Every remaining high map lifts: the obstruction line degrees are 0 and 4. Its actual kernel is again (6).

## 4. Families B and C

Write L=O(-8)+O(-10) in B and L=W(-9) in C.

If S=P, the remaining source is P(-2)+T(-3)+L. Equation (5) supplies kernel V(-4). Every T(-3) high map lifts since H1(O(-1))=0; the deeper maps also lift. Thus Q has form (7).

If S=V+P, there is no degree -3 coefficient, and the remaining source is (V+P)(-2)+V(-4)+L. Both sextic summand maps are nonzero, so their combined map is full sextic evaluation with kernel T(-3). Every other high map lifts, with obstruction line degrees at least 1. Again Q has form (7).

All lifts can be averaged over the finite group to be equivariant and subtracted by triangular source automorphisms. These are computations of kernels of the actual maps. No splitting is assumed horizontal. Every high evaluation used is everywhere surjective. Consequently delta is everywhere surjective and

    K/Q = O(4)+W'(-5).

## 5. The next derivative cannot have rank three

In every case Q is one of exactly three possible bundle shapes:

    (2V+P)(-4)+O(-8),
    T(-3)+V(-4)+O(-8)+O(-10),
    T(-3)+V(-4)+W(-9).

The next derivative has target

    (K/Q)(-2) = O(2)+W'(-7).

There is no map from any of these Q to W'(-7). Degree excludes the -3 and -4 blocks. For the deeper blocks the relevant invariant spaces vanish by

    W' tensor W = P,
    W' tensor Sym^3 W = V+D5,
    W' tensor Sym^2 W = T.

The last identity excludes W(-9): equivalently W tensor Sym^2 W=S4+W contains no W'. Hence the derivative factors through O(2), so has generic rank at most one. This contradicts the plateau's required rank three, excluding the entire (8,4) case.

## Reproduction and limits

    python3 verify_extremal_31_last_low_quotient_exclusion.py

The companion checks both Euler identities, all 14 eligible tail blocks through degree 28, all exact tail multisets, all 13 genuine splittings, the seven low-map survivors, the universal evaluation and extension characters, lifting degrees, and all final Hom vanishings. The invariant-divisor, splitting, actual nonzero-map, extension, and sheaf arguments are proved above; character arithmetic is not offered as a substitute for those arguments. Neither remaining quotient case nor the rank-one dual-image branch is settled here. Global bounds remain unchanged.
