# The (6,2) quotient has only eight possible K splittings

## Checked result and scope

For the remaining rank-two dual-image quotient A0=O(4)+W'(-1), the bundle K has exactly eight necessary equivariant splitting shapes. Its actual next kernel Q=E^{--} reduces further to three explicit shapes or one small residual high-map problem. These are necessary lists, not existence assertions or a full exclusion. SF >= 3 and positive-square rank >= 27 are unchanged.

Use the five-quotient, section-envelope, and three completed exclusion certificates in this directory. All arithmetic below is abstract exact representation arithmetic. No selected actual coefficients, points, source matrices, actual-instance rank experiments, or scans are used. No existing file was changed.

Write S=S4, T=T6, P=P4, D=D5. Numerals in parentheses are line-bundle degrees. K has rank 14 and degree -56. Its actual derivative is

    delta: K -> O(2)+W'(-3),  ker delta=Q.

It has generic rank three. Persistence gives H0(Q(2))=0 and H0(Q(3))<=S. The latter follows by injecting sections through the next derivative into H0(A0(-1))=S, using H0(E^{---}(3))=0. These are actual Gauss kernels, not horizontal choices of splitting.

## 1. Complete positive-tail enumeration

The established inputs are

    H0(K(2))=dD, d=0 or 1;
    d(S+T)<=X=H0(K(3))<=W'+S+T;
    chi_G(K(3))=0, chi_G(K(4))=2V+2P.

All degrees are at most -2, and rank/degree bound a tail degree -j by j<=30. Put R2=dD and R3=X-R2 tensor W. Each tail C(-j), j>=5, contributes positively C tensor Sym^{j-5} W to H1(K(3))=X. Enumerate multisets with exactly that contribution. The degree -4 coefficient is forced by

    R4=2V+2P - R2 tensor Sym^2 W - R3 tensor W
                     - sum_tail C chi_G(O(4-j)).

Requiring R3 and R4 genuine gives exactly these eight shapes:

    1. (2V+2P)(-4).
    2. T(-3)+(V+P)(-4)+O(-10).
    3. D(-2)+(V+P)(-4)+O(-8)+O(-10).
    4. D(-2)+(V+P)(-4)+W(-9).
    5. W'(-3)+(2V+P)(-4)+W'(-5).
    6. (W'+T)(-3)+V(-4)+W'(-5)+O(-10).
    7. D(-2)+W'(-3)+V(-4)+W'(-5)+O(-8)+O(-10).
    8. D(-2)+W'(-3)+V(-4)+W'(-5)+W(-9).

Each has rank 14 and degree -56. Notably no T(-5), V(-6), D(-6), or W'(-9) block survives R4 positivity, so their potential low maps need not be classified for this case.

## 2. The six evaluation cases

In cases 2 and 6, the T(-3) component to O(2) is nonzero: otherwise T contributes to H0(Q(3)), contrary to its bound by S. It is complete quintic evaluation, with kernel D(-4).

In cases 3,4,7,8, the D(-2) component to O(2) is nonzero by H0(Q(2))=0. It is complete quartic evaluation, with kernel S(-3).

In cases 5 through 8, W'(-3) maps by a nonzero scalar isomorphism to W'(-3), since a zero map would put W' in H0(Q(3)); its high component vanishes because W' is absent from Sym^5 W. Eliminate other low components by subtracting this isomorphism. Then eliminate other high components using the appropriate quartic or quintic evaluation. The required lifts exist: their obstruction line degrees j-k are at least -1 when the evaluation kernel is C(-k) and the extra source is B(-j). Average lifts to make them equivariant.

In cases 2 and 3, after eliminating high components the P(-4) low map must be nonzero. The only other low contributor is a single line O(-10), which cannot have generic rank two. The P low map is the tensor-Euler evaluation

    0 -> W'(-5) -> P(-4) -> W'(-3) -> 0.

All deeper low components lift through it since H1(O(j-5))=0 for j>=8.

Case 4 needs care: W(-9)->W'(-3) can have generic rank two with a degree-12 determinant divisor. Do not assume it is surjective. If the P low component were zero, generic rank forces this W map to be generically injective, hence injective as a sheaf. After the quartic high elimination, its actual kernel would be

    Q=S(-3)+(V+P)(-4),
    K/Q=O(2)+W(-9).

The next derivative Q->O+W(-11) then has no low component by degree, contradicting generic rank three. Thus the P component is nonzero after all. Tensor Euler and the same lifting argument apply without requiring any surjectivity of the W(-9) map itself.

Consequently the actual kernels are:

    cases 2,6:   Q=(D+V)(-4)+W'(-5)+O(-10);
    cases 3,7:   Q=S(-3)+V(-4)+W'(-5)+O(-8)+O(-10);
    cases 4,8:   Q=S(-3)+V(-4)+W'(-5)+W(-9).

In all these cases delta is everywhere surjective, so K/Q=O(2)+W'(-3). No horizontal splitting has been assumed.

## 3. Cases 1 and 5 reduce to the same high map

In case 1, only the two P(-4) copies can map to the low target. Generic rank three forces a nonzero linear combination. Change basis in their multiplicity space to make just one the nonzero tensor-Euler map. Its kernel, together with the other blocks, is

    J=(2V+P)(-4)+W'(-5).

The full kernel Q is exactly ker(f:J->O(2)), where f is the restriction of the actual high component. This restriction is nonzero by generic rank three. Case 5 yields exactly the same problem after removing its W'(-3) low isomorphism.

At least one of the V or P components of f must be nonzero. Indeed, otherwise only W'(-5) contributes. A nonzero W' septic polynomial pair is basepoint-free: its common-zero divisor would be invariant of degree at most seven, below the minimum nonempty icosahedral orbit size twelve. It then has kernel O(-12), and

    Q=(2V+P)(-4)+O(-12).

Delta is surjective in this situation. In the next derivative Q->O+W'(-5), only the single O(-12) line can reach the rank-two low target. Its low rank is at most one, so the full rank is at most two, contradicting three.

Thus the remaining problem is precisely a nonzero high map

    f:(2V+P)(-4)+W'(-5) -> O(2)

with at least one nonzero sextic component on 2V+P. Any such nonzero irreducible sextic series is basepoint-free by the same invariant-divisor argument, so f, and hence delta, is everywhere surjective. The residual actual-map restrictions have not been asserted sufficient for a Gauss realization.

## Reproduction

Run python3 verify_extremal_31_first_remaining_quotient_reduction.py.

It reuses the frozen envelope verifier, exhausts positive tails through degree 30, verifies all eight rank/degree shapes, the common Euler characters, every special Hom assertion, evaluation character, and lifting inequality used above. The sheaf arguments are supplied in this proof, not inferred from the arithmetic. The (6,2) quotient remains open, now reduced to three explicit Q shapes and the single displayed residual map.
