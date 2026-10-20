# Prior mathematical audit

This audit concerns the source manuscript. It is not a formal verification or a review of later normalized publication bytes.

# Independent audit of the rank-three swap-quotient argument

## Verdict

**PASS, with the stated conditional scope.** The numerical assertions and proofs in the updated `PROOF.md` are correct. In particular, the factor-swap signs, the quotient arithmetic genus 36, degree 35 and eight sections of its descended polarization, the Gorenstein assertion and omega_Y=M^2, the local delta invariants 12 and 8, and the normalization genus relation all check out independently.

The complete-intersection and global numerical conclusions require the **pure-curve alternative**. They do not exclude a surface component, prove that a rank-three middle exists, or prove global reducedness or irreducibility. The eight smooth branches and the delta calculations additionally require that the projective base of the initial net is **eight reduced points**. A regular sequence of initial quadrics alone establishes the tangent cone and multiplicity, but does not establish those reduced-branch conclusions.

The universal dimension upper bound and the prior repeated-input/dependent-triple lemma are used as established inputs rather than re-proved in this audit.

## 1. Complete intersection and ordinary Euler characteristic

Seven independent equations with pure codimension seven in the regular eight-dimensional ambient variety form a regular sequence. This remains true when the resulting curve is nonreduced; it also excludes embedded associated components. The Koszul resolution, adjunction and cycle computations consequently apply scheme-theoretically:

    omega_X = O_X(2,2),
    deg O_X(1,1) = binom(8,4) = 70.

For k=5,6,7, the dimensions of H^8(O(-k,-k)) are 1,25,225. Thus

    chi(O_X) = 1 - 21 + 7*25 - 225 = -70.

Every negative Koszul term with nonzero cohomology has total degree at least one. Hence H^0(O_X)=C and h^1(O_X)=71. No reducedness or normality is used.

## 2. Equivariant signs and quotient genus

Use the natural factor-swap linearization on O(-k,-k). The seven scalar equations are individually symmetric, so the equation space and all its exterior powers have trivial swap action. There is no additional exterior-power sign.

The only ambient cohomology relevant to negative terms is

    H^8(O(-k,-k)) = H^4(O(-k)) tensor H^4(O(-k)).

The Kunneth interchange sign is (-1)^(4*4)=+1. The action is therefore the ordinary tensor flip, of trace dim H^4(O(-k))=binom(k-1,4). The alternating sign of the Koszul term is already (-1)^k. Consequently

    chi^sigma(O_X) = 1 - 21 + 7*5 - 15 = 0.

Since the trace on H^0 is one, the trace on H^1 is one. Its invariant dimension is (71+1)/2=36. A finite characteristic-zero quotient has O_Y=(pi_*O_X)^sigma, with exact invariants and no higher direct images for pi. Therefore

    H^i(Y,O_Y) = H^i(X,O_X)^sigma,
    p_a(Y) = 36.

These statements are valid for a nonreduced pure complete-intersection curve.

## 3. Descent, degree and sections

The natural linearization on L=O_X(1,1) is trivial on the fiber at the sole fixed support point p. It descends to a line bundle M. Equivalently, the symmetric Segre morphism factors through the categorical quotient and pulls back its target O(1) to L; the descended bundle is the pullback on Y. Its ampleness also follows from finite descent of ampleness.

The action is free on X minus p. Thus the quotient there is a degree-two finite etale torsor, including in the nonreduced case. On fundamental one-cycles pi_*[X]=2[Y]. Applying the projection formula gives deg M=70/2=35, with all scheme multiplicities included.

After twisting the Koszul resolution by L, only its k=0 and k=1 terms contribute to total degree zero. They give the exact description

    H^0(X,L) = (V^* tensor V^*) / W_b.

The seven-dimensional kernel W_b lies in Sym^2 V^*. The invariant and anti-invariant dimensions are therefore 15-7=8 and 10. By descent and the projection formula,

    H^0(Y,M) = H^0(X,L)^sigma,
    h^0(Y,M) = 8.

There is no hidden additional section from higher Koszul cohomology: after this twist the nonzero negative cohomology terms have total degrees one and two.

## 3a. Quotient duality and the Gorenstein strengthening

The added assertion omega_Y=M^2 is correct, including when X and Y are nonreduced. Here is a local verification of the hypotheses and the invariant-duality step.

Let B be the local ring of Y at a closed point, and let A be the finite semilocal B-algebra obtained from pi_*O_X. A parameter of the one-dimensional ring B pulls back to a parameter at every local factor of A, because A is finite over B. Those factors are Cohen--Macaulay of dimension one, so this parameter acts injectively on A. It acts injectively on its Reynolds summand B as well. Thus B is Cohen--Macaulay, and A is a maximal Cohen--Macaulay B-module. This reasoning permits nilpotents.

Finite-map duality now identifies the canonical module of A with Hom_B(A,omega_B). Its natural group action is precomposition on the A argument. Consequently its invariant part is

    Hom_B(A,omega_B)^sigma
      = Hom_B(A_sigma,omega_B)
      = Hom_B(B,omega_B)
      = omega_B.

The middle equality follows from the Reynolds map: its kernel is the span of a-sigma(a), so the coinvariant B-module A_sigma is canonically B. This argument does not assume reducedness, normality, an etale quotient, or that omega_B is already invertible. It therefore establishes the needed identity without a circular Gorenstein assumption.

The adjunction isomorphism omega_X=L^2 is equivariant for the natural linearization. Swapping the two ambient tangent blocks of dimension four has determinant (-1)^16=+1, and the seven defining sections are invariant. Thus there is no sign-character twist of the canonical bundle. Projection formula and invariant descent give

    omega_Y = (pi_*omega_X)^sigma
            = (pi_*pi^*M^2)^sigma
            = M^2.

The right side is invertible, so Y is Gorenstein. As a numerical check, deg omega_Y=2*35=70=2*p_a(Y)-2.

## 4. The local even presentation

The change a=s+t, b=s-t and formal elimination of s are valid because the derivative in s is 2I. Uniqueness gives s(-t)=s(t). Substitution gives the stated even equations

    g(t) = -q(t,t) + (1/4)q(B(t,t),B(t,t)) + terms of degree at least six.

Thus the involution is exactly t -> -t, with no cubic terms in the equations. The local embedding dimension of X is four. If the three initial quadrics form a regular sequence, the regular-initial-sequence lemma identifies the associated graded ring with their complete intersection. Its Hilbert function is

    1, 4, 7, 8, 8, ...,

and its multiplicity is eight. Regularity of the initial sequence must not be omitted from this tangent-cone conclusion.

## 5. Reduced tangent cone, branches and delta invariants

An eight-point reduced projective base of three quadrics in P3 is a reduced zero-dimensional complete intersection. In particular, the initial quadrics do form a regular sequence. On the blowup, the Jacobian in the three projective coordinates is invertible at each base point. The formal implicit function theorem gives eight smooth branches with distinct tangent lines. The reduced associated graded ring also rules out any hidden nilpotents in the completed local ring.

Let A be this completed local ring, Abar its normalization, and ell a general linear function nonvanishing on every tangent direction. Then Abar is the sum of eight copies of C[[ell]], and

    A intersect ell^n Abar = m_A^n.

To verify the equality, a nonzero initial form of order d in gr_m A has a nonzero restriction to at least one tangent line, because the tangent cone is reduced. Its order on the corresponding smooth branch is exactly d. The normalization-defect filtration therefore has dimensions 8 minus the displayed Hilbert function. Its length is

    delta(A) = (8-1)+(8-4)+(8-7) = 12.

Each branch is fixed individually by the involution: its tangent line is fixed projectively, and no second branch has that tangent line. The linear function ell itself is anti-invariant and is a parameter on each branch. Hence sigma acts as (-1)^n on each degree-n piece of both A and Abar. Exactness of invariants applied to their finite-length difference gives

    delta(A^sigma) = (8-1)+(8-7) = 8.

This also verifies that the normalization of A^sigma is Abar^sigma, a sum of eight rings C[[ell^2]], so the quotient has eight smooth local branches.

An equivalent check is that the associated graded ring of the quotient is the second Veronese of gr_m A. Its Hilbert function is 1,7,8,8,..., which independently gives embedding dimension seven, multiplicity eight and delta eight.

## 6. A harmless strengthening concerning embedding dimension

The quotient embedding-dimension assertion needs less than the reduced-eight-point hypothesis. Write S=C[[t_1,t_2,t_3,t_4]]. Since the g_i are invariant, averaging coefficients in a relation gives

    (S/(g_1,g_2,g_3))^sigma = S^sigma/(g_1,g_2,g_3).

The invariant ring S^sigma is topologically generated by its ten quadratic monomials. Modulo the square of its maximal ideal, the three g_i have the three independent classes q_i. Thus the quotient cotangent space has dimension 10-3=7 whenever the residual rank is three. No regularity or reducedness assumption on the net is needed for this particular claim.

Under regular initial quadrics, the second-Veronese description of the quotient associated graded ring also remains valid without reducedness. Reducedness is what justifies the smooth-branch and normalization-defect interpretation.

## 7. Normalization genera and equality conditions

When X is additionally reduced and integral, its normalization is a smooth connected projective curve. The quotient of this normalization is the normalization of Y. A fixed point upstairs must map to a fixed point downstairs on X, so all ramification lies over p. The eight branches give exactly eight fixed points there, each with ramification index two. Therefore

    2g(X^nu)-2 = 2(2g(Y^nu)-2)+8,
    g(X^nu) = 2g(Y^nu)+3.

Subtracting the local delta contributions from the arithmetic genera yields

    g(X^nu) <= 71-12 = 59,
    g(Y^nu) <= 36-8 = 28.

The two upper-bound equalities are equivalent by the genus relation. Equality holds precisely when there are no further singularities of X: any additional singular point of an integral complex curve has positive delta. Freeness of the action away from p is consistent with the fact that the remaining total delta contributions on X are twice those on Y.

No numerical or sign correction to the updated draft is required. The unconditional embedding-dimension strengthening in Section 6 has now been incorporated into its statement and proof.
