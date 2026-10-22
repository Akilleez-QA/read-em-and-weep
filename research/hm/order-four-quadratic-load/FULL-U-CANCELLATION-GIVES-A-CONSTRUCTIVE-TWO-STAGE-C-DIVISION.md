# Full U cancellation gives a constructive two-stage c division

## Result and exact scope

This is a concrete continuation of `NEGATIVE-EULER-REPAIRS-HAVE-A-CANONICAL-FULL-SOURCE-BALANCE.md`, not a replacement for the whole-Q criterion in [PR682](https://github.com/Akilleez-QA/read-em-and-weep/blob/5a8249656bfb406d4a0a89994b0de6293e5acd8f/research/hm/source-completion-criterion/PROOF.md).

Fix the actual marked monad, alpha_U=a_m A+b_m B and alpha_A=c_m C, with all three scales nonzero. Let the target f=a h Z be the actual closed fixed-duality degree-one cochain. Suppose a global skew middle and source choice has cancelled the ENTIRE U residual, not only a principal projection. Suppose its remaining c residual

    R=(T alpha−alpha S−f_left)_A

is a tensor linear in the full A input, and has only these homogeneous components:

    VV coefficient E of positive/negative degrees (2,3),
    mixed coefficient F of degrees (3,2),
    no WW component.                                             (1)

These are the retained high components after the preceding full source balance removes the lower mixed/WW c companion. If other sectors survive, they must first be retained and balanced; the theorem does not discard them.

For the retained balanced U sector, exact cancellation is itself necessary for q0-divisibility: its VV coefficient has positive degree one, hence must vanish; the remaining mixed-only degree-(2,3) residual is q0-divisible only if zero. Indeed its quotient has positive coefficient degree zero, and exterior closure forces its contraction by the free positive vector v to vanish, so every mixed coefficient is zero. This assertion does not apply to additional unretained sectors.

Then E is entirely Cartan. Moreover there is an explicit regular construction of the remaining AA source and divided cochain if and only if two whole-polynomial tests pass: a scalar sextic restriction test and a residual mixed-form restriction test, given below. Neither test is a ramification-only test. Their values on a particular actual middle operator remain uncomputed.

## 1. Linearized isotropy forces the full Cartan coefficient

In an alternating frame let beta=alpha^t J. Fixed duality and closedness imply alpha^t J f_left is symmetric. Since T is skew and alpha is isotropic, alpha^t J(T alpha−alpha S−f_left) is also symmetric, for arbitrary source S; no trace-free condition on S is imposed.

Its U columns vanish by hypothesis. The off-diagonal block therefore gives

    alpha_U^t J R=0.                                              (2)

In the three-positive/one-negative form sector, the A-with-F term has coefficient degrees (4,2), whereas the B-mixed-with-E term has degrees (2,4). They cannot cancel. In the fixed coefficient frame the latter term is exactly

    (p^t J cliff(E)) tau_V ∧ j,       j=−w du+u dw,                (3)

for the arbitrary U input p. The nonzero b_m factor is retained in (2). Since the polynomial ring is a domain, (2)–(3) force cliff(E)=0. This is an entire polynomial identity, not a specialization to the positive conic.

## 2. First test and the regular AA source

Use the actual cubic marking f_cub:Sym^3 W→Cartan, and retain the normalization

    C(y)_VV=−f_cub(ell y),           ell=uT−wS.

The notation f_cub is distinct from the target cochain f. Put

    p=f_cub^(-1)E,
    sigma(v,w)=p(S=u,T=w;v,w).                                    (4)

Then sigma has degrees (2,6). The first test is

    sigma is divisible by the PHYSICAL q0(v).                     (5)

Equivalently its coefficient restriction to the entire positive conic is zero. Let r=sigma/q0, a negative binary sextic. Its canonical balanced polarization is

    Pol_3,3(r)=(S partial_u+T partial_w)^3 r/120,
    E0=f_cub Pol_3,3(r).                                          (6)

Evaluation at S=u,T=w recovers r. Thus p−q0 f_cub^(-1)E0 is divisible by ell in the polynomial ring. This also follows from the bihomogeneous ideal of the diagonal, which is the principal prime ideal (ell).

Write p1=f_cub^(-1)(E−q0 E0). The quotient y=p1/ell is obtained without localization by

    Omega=partial_u partial_T−partial_w partial_S,
    y=Omega p1/6−ell Omega^2 p1/60+ell^2 Omega^3 p1/720.            (7)

Here y has binary degree two and coefficient degrees (2,2). Add the AA source

    S_AA=−y/c_m.                                                  (8)

With the residual convention above this adds +C(y) to R, and hence

    (R+C(y))_VV=q0 E0.                                           (9)

No U column changes. Conversely, any AA source making the VV residual divisible by q0 implies (5), since evaluation kills ell. This direction also retains the source normalization c_m.

## 3. Second test and the full divided expression

Choose the following explicit closed form with VV coefficient E0:

    Z0=(partial_u E0 ∧ du+partial_w E0 ∧ dw)/3,
    V0=i_x Z0.                                                    (10)

Because E0 has negative degree three and no positive-coordinate coefficient, i_w Z0=E0. Set

    H=R+C(y)−q0 V0.                                               (11)

It has zero VV and WW components and is i_x-closed. Thus it is purely mixed, and the two contraction equations separately give i_w H=i_v H=0. Regular negative Koszul division gives

    H=L∧j,
    L=(partial_u H_4−partial_w H_3)/3,                            (12)

where H_i is the positive-one-form coefficient in du or dw. The positive one-form L has coefficient degrees (3,1), and i_v L=0.

The second test is

    every coefficient of L is divisible by q0(v).                 (13)

It is again a coefficient restriction to the WHOLE conic, retaining ambient form factors. Since q0 is coprime to u and w, (13) is equivalent to q0-divisibility of H. When it holds, the full c residual is

    R+C(y)=q0 [V0+(L/q0)∧j].                                     (14)

Both terms in brackets are regular and i_x-closed. Combined with the already zero U residual, fixed duality supplies the right arrow. Since the original target is closed and d^2=0, injectivity of multiplication by q0 proves that the divided degree-one cochain is closed. In the convention dC=f−q0 V, the actual divided cochain is the NEGATIVE of the bracketed residual quotient in (14).

This is a construction, not an appeal to abstract source globalization. Every coefficient expression is global in the fixed homogeneous frames and uses only regular differentiation, polarization, and the stated polynomial divisibility tests.

## 4. Choice independence and the remaining equation

A different choice of E0 with the same evaluation changes p1 by q0 times an ell-divisible expression. Consequently its AA source changes by q0 times a regular source, and R+C(y) changes by a q0 multiple. Changing the auxiliary closed lift V0 also changes (11) by a q0 multiple. For the literal retained-sector factorization H=L wedge j, compare lifts preserving that sector; divisibility itself is invariant under any regular change of V0. Therefore the truth of (13) is independent of these choices. The explicit choices (6), (7), and (10) remove this bookkeeping ambiguity.

The tests characterize completion by the remaining AA source in sector (1), with the previously balanced U-row source held fixed. They do not assert that all possible middle sectors, source freedoms, or prescribed divided classes have been exhausted. In particular they do not say that an arbitrary chosen c-principal source representative satisfies the forced balance of the preceding theorem.

The actual next construction must now supply a middle with full U cancellation and make the specific sigma and L vanish modulo q0. Vanishing at selected ramification inputs, or merely satisfying the twelve local restrictions, does not prove either whole-polynomial divisibility condition. A nonzero evaluation of sigma or an actual L coefficient on the conic would disprove the corresponding condition, but an intermediate local shadow must first be identified with that exact polynomial. No actual fourth value or complete original repair is asserted.

## Verification

`verify_c_column_cartan_division.py` checks the exact free-symbol pairing (3), all nine coefficients in the regular division (7), all seven sextic coefficients in (6), and the regular extraction (12). The proof of monad closedness uses the full cochain identities, as in PR682, not merely exterior i_x-closedness. The verifier makes no actual-source assignments, actual-instance rank calculations, or numerical scans.
