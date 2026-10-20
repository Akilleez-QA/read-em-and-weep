# The raw scalar's deck character and complementary stripped derivative

## Result and exact scope

Fix the two original owner occurrences i,j, and distinct coordinate directions a,b. Let s_(a,b;ij) be exactly `PhysicalModel.s_raw((a,b),i,j)` in the frozen raw engine. On X=C^4, C: y^2=x^3-x, this is a meromorphic scalar of deck character {a,b}. Its character coefficient is a meromorphic section

    sigma_(a,b;ij) of O_Y(-2 e_a-2 e_b),   Y=(P^1)^4.

The coefficient is extracted from a free module, including at every ramification divisor; it is not obtained by declaring division by y_a y_b to preserve regularity. The scalar and its character coefficient have owned carrier vector (5,5) and legal vector (2,2).

For any complementary direction d not in {a,b}, the actual invariant derivative has character {a,b,d}, and its coefficient is

    T_d sigma = partial_x_d sigma       on a finite factor,
    T_d sigma = -partial_t_d sigma      on an infinity factor.

These coefficients glue in O_Y(-2 e_a-2 e_b-2 e_d) and have owned vectors **carrier (6,6), legal (3,3)** on all 16 standard product charts. No additional infinity equation or absent-owner legal factor is used. This discharges the raw-scalar complementary-stripping premise in the ownerwise residual/lift ledger, using the independently supplied raw-block 5/1 theorem.

This is a theorem for the displayed scalar leaf and its complementary derivatives. It does not attribute the complete residual, its lift, or a terminal scalar kernel to a sheaf or obstruction class; prove residual closure; certify a derivative implementation or normalized jets. The existing weights 54/29 and standard allowance 5251 are unchanged.

## 1. Source binding and geometric inputs

The source snapshots are read only as inert text/AST:

- [Frozen raw engine](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-realization/raw_engine.py), SHA256 c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9.
- [Frozen compiler](https://github.com/Akilleez-QA/read-em-and-weep/blob/491306fd2f7f8a04c29784afa48a6cb8a467f154/research/hm/null-raw-regular-extension/inputs/compiler.py.txt), SHA256 28e95b87adefaba0d4ec886a7ab272f252f376bbb1fc26e0a387bc05f896a386.

Their authenticated local copies and the dependency snapshots are pinned in `source-pins.json`. No new remote read is claimed. No source module, model, matrix, polynomial, physical source, or jet is evaluated.

The accepted product-root proof fixes the actual model and frames: N is the external product of O_C(O); the four resolution terms have N powers (-1,1,3,5), and their local legal frames are e_m^k with e_m=nu_m e_ref and nu_m=product(y_r/x_r)^(m_r). The standard square-line frame ell_A has ratio c_(m,A)=e_m^2/ell_A=nu_m^2 tau_A, tau_A=product_(r in A)t_r. Homogeneous primitive entries and all carrier/legal clearing factors descend to base coordinates on Y. The accepted homogeneous proof provides their global, all-chart carrier clearances. We use the raw-block theorem's explicit all-chart formula and 5/1 coefficient bound, rather than an affine pole estimate.

The mathematical operation denoted by the raw `Mat.D` is entrywise V_d. The fixed geometric derivation is

    V(x)=y, V(y)=(3x^2-1)/2;
    t=1/x, u=y/x^2, u^2=t(1-t^2),
    V(t)=-u, V(u)=(3t^2-1)/2.

This is the rational denotation used in the proof. A static contract that calls `.V(d)` does not prove arbitrary software implementation semantics.

## 2. Exact raw scalar and its degree-zero frame meaning

For resolution block r, write k_r=(-1,1,3,5)_r and epsilon_r=(-1,1,-1,1)_r. Put B_(o,d)^r=`blocks(o,d)[r]` and q_d=q_(ij,d). The literal `raw_scalar_formula` is

    s_(a,b;ij) = (1/4) sum_r epsilon_r {
        tr(B_(i,a)^r B_(j,b)^r)-tr(B_(i,b)^r B_(j,a)^r)
        +(k_r/2)[q_a(tr B_(i,b)^r+tr B_(j,b)^r)
                 -q_b(tr B_(i,a)^r+tr B_(j,a)^r)]
      } -(15/8)q_a q_b.                                      (1)

Every one of the four blocks, both endpoints in each linear term, both wedge orders, all signs and the final q_a q_b term are retained.

There is no unaccounted root-line weight in (1). In a single resolution degree, both source and target of B have the same ambient line N^k, so End has degree zero. Changing from e_m^k to the common rational frame e_ref^k multiplies an ambient basis by the scalar nu_m^k, whose conjugation acts trivially on endomorphism coefficients. A connection itself has an inhomogeneous frame term, but B is the difference of two connections. Explicitly, if the source split basis is U_m and its inverse is Q_m, the raw block is

    B=-(V U_m)Q_m-k alpha_m(V)Id.

In the common frame U_common=nu_m^k U_m, its split connection gains -k Vlog(nu_m)Id, while the old connection coefficient becomes k alpha_m(V)-k Vlog(nu_m). Their difference is the same B. This is the exact product-root/raw-block comparison, including the old connection, not an assumption that a connection coefficient is tensorial. Products B_i B_j and their traces in (1) are therefore scalar rational functions in a common ambient trivialization. The source q_d is a scalar connection-difference coefficient, identified by the product-root proof. Hence (1) has homogeneous degree zero. No full residual membership assertion is needed for this scalar typing.

The raw call chain is also exact: `s_raw` passes the a and b blocks of both owners and their corresponding q's into (1); `RawSource.T` returns that raw scalar, overriding `Source.T`. `source_and_lift` instantiates `RawSource(model.M)`. Thus the scalar used in E is this leaf, rather than the separate N14 combined-solver construction in the base compiler.

## 3. Pure characters for B and q, bound to the actual frames

Write z_(A,r)=y_r on a finite factor of standard chart A and z_(A,r)=u_r on an infinity factor. The coordinatewise deck involutions negate z_(A,r). The source's unweighted primitive entries depend only on the coefficient coordinates v, hence on the x's; the raw column and row factors use only nu_m^2 and its inverse, also base-rational. Applying V_d to such an even coefficient yields y_d times its x_d derivative, and the retained old coefficient is m_d y_d/[x_d(x_d^2-1)]. Thus every actual raw B_(o,d) has pure character {d}. This statement permits the zero entry, which belongs to every character subspace.

At infinity the source-frame linkage must be retained. If a matched homogeneous column has degree w and its inverse row degree -w, the exact source entries satisfy

    U_source=c_(m,A)^(-w) U_A,
    Q_source=c_(m,A)^( w) Q_A.

Leibniz gives a derivative term and w(V_d log c)U_AQ_A. The actual old coefficient alpha_m remains present. The raw-block theorem proves directly that all these terms have the form

    B_(o,d)^r=z_(A,d) b_(o,d),A^r,
    H_(o,A)^5 L_(o,d),A b_(o,d),A^r regular on the base chart. (2)

The coefficient is explicitly formed by replacing V_d on base functions by partial_x_d or -partial_t_d and replacing Vlog c and alpha(V) by the following scalar coefficients:

| chart | legal bit | (Vlog c)/z | alpha(V)/z | legal L |
|---|---:|---|---|---|
| finite | 0 | 0 | 0 | 1 |
| finite | 1 | (x^2+1)/[x(x^2-1)] | 1/[x(x^2-1)] | x(x^2-1) |
| infinity | 0 | -1/t | 0 | t |
| infinity | 1 | 2t/(1-t^2) | t/(1-t^2) | 1-t^2 |

Consequently (2) is a coefficientwise all-chart bound, not a result of dividing a cleared regular B by z at a branch point. We do not re-prove its carrier ledger here; it is the precise supplied raw-block dependency.

For q the exact source is simpler. Put delta_d=m_(j,d)-m_(i,d), so

    q_d=delta_d y_d/x_d,
    q_d=z_(A,d) kappa_(ij,d),A,
    kappa_finite=delta_d/x_d,
    kappa_infinity=delta_d/t_d.                              (3)

If delta_d=0 this is zero. Otherwise the two actual endpoint bits are 0 and 1. On a finite chart the bit-one endpoint's legal section x(x^2-1) clears kappa; on an infinity chart the bit-zero endpoint's legal section t clears kappa. In particular an infinity q pole is not charged to the bit-one endpoint's unit 1-t^2. Padding by both endpoint legal sections is always valid: on either chart their product times kappa is delta_d times x^2-1 or 1-t^2, respectively. There is no carrier denominator and no absent endpoint.

Both B and q therefore have a single odd basis factor in precisely their direction. In (1), every monomial has one factor in direction a and one in the distinct direction b. Its character is {a,b}; there is no occurrence of z_a^2 or z_b^2 to reduce. All constant coefficients and traces preserve this character.

## 4. Branch-safe extraction and the scalar's line

For a standard base chart let R_A be its polynomial coordinate ring. The coordinate ring of its preimage in X is

    S_A=R_A[z_1,z_2,z_3,z_4]/(z_r^2-f_(A,r)),
    f_finite=x_r^3-x_r,   f_infinity=t_r-t_r^3.

As an R_A-module it is free with the 16 square-free basis elements z_S=product_(r in S)z_r. This follows successively by division by each monic quadratic; it requires neither invertibility of f_(A,r) nor etaleness. It remains true at every branch divisor. Localizing by any nonzero base clearing factors preserves this free decomposition. Character {a,b} is exactly the summand R_A z_a z_b, also after that localization.

Define sigma_A as the coefficient of z_a z_b in this free decomposition of s. Equivalently, substitute (2)-(3) in (1) and remove their displayed, distinct formal basis factors. This is a coefficient projection, an R_A-linear map from the free module to R_A. If an invariant base clearing factor C_A makes C_A s regular, then the same projection gives C_A sigma_A regular. One never infers this by multiplying by the rational inverse of z_a z_b in a branch-point local ring. The rational shorthand s/(y_a y_b) on the dense finite nonbranch locus identifies the same coefficient, but is not the regularity argument.

On switching coordinate r from finite to infinity, u_r=t_r^2 y_r. Since s is degree zero, the coefficient law is

    sigma_A=(product_(r in A intersect {a,b})t_r^-2)
                  sigma_finite, after coordinate substitution. (4)

This is precisely O_Y(-2e_a-2e_b), with O(0) in each complementary direction. The source/frame comparison of section 2 is what excludes an additional square-line or root-line factor in (4). Descent along the finite flat double covers thus gives an actual meromorphic section of this line, not a bare affine parity statement.

The literal coefficient families have the two-owner bounds

| family | carrier at (i,j) | legal at (i,j) |
|---|---|---|
| b_i b_j | (5,5) | (1,1) |
| kappa b_i | (5,0) | (2,1) |
| kappa b_j | (0,5) | (1,2) |
| kappa kappa | (0,0) | (2,2) |
| sigma | (5,5) | (2,2) |

Here a legal allowance at an owner bounds the power of each of its four legal sections. The sharper direction-specific factors can be padded to this convention. Each product adds powers at the actual occurrence; the sum takes maxima. Therefore, in every chart,

    C_A sigma_A regular,
    C_A=H_(i,A)^5 H_(j,A)^5
          product_(r=0)^3 L_(i,r),A^2 L_(j,r),A^2.           (5)

The carrier and legal factors are global homogeneous sections with their own transitions; (4)-(5) are a genuine cleared-section statement. Equal carrier labels or equal divisors do not identify two different occurrences. No maximum replaces addition when two factors at one occurrence are multiplied.

## 5. Complementarity proves the all-chart derivative law

Let d not in {a,b}. In chart A, V_d kills z_a,z_b and acts on base functions by z_d partial_A,d, where partial_A,d is partial_x_d on a finite factor and -partial_t_d on an infinity factor. Consequently the exact product rule gives

    V_d s = z_a z_b z_d (partial_A,d sigma_A).                (6)

Equation (6) establishes the coefficient without dividing a regular derivative by any vanishing z. It also proves the new pure character {a,b,d}. The statement often written V_d sigma/y_d=partial_x_d sigma is only the finite-chart abbreviation for (6), with sigma interpreted in its coefficient line.

There is no missing connection term in the complementary direction. The transition multiplier (4) depends only on a,b. Its derivative in d vanishes. Under a switch of d itself, sigma_infinity=sigma_finite(1/t_d), while

    -partial_t_d sigma_infinity
          =t_d^-2 (partial_x_d sigma_finite)(1/t_d).         (7)

Thus the derivative coefficient picks up precisely the new O(-2) transition in d. Under switches of a or b, the undifferentiated transition factor commutes with partial_A,d; under any other switch nothing changes. These single-factor statements prove compatibility on every overlap of all 16 charts. Equivalently, a line pulled back from the three other P1 factors has a canonical differential in the d direction; the invariant vector field identifies its relative differential with the new odd summand, including the sign in (7).

The factor t_d^-2 in (7) is a line transition on an overlap, where t_d is invertible. It is not an additional pole factor to append to the local infinity formula. The latter is -partial_t_d sigma_A, bounded directly on the complete infinity chart by the next section. This distinction prevents an unowned infinity pole from entering the ledger.

Complementarity is essential. If d=a or b, V_d also differentiates the odd basis factor, and (4) has a nonconstant transition in d. For example V_a z_a=(3x_a^2-1)/2 on a finite factor; the result loses rather than gains that character. The theorem does not apply the rule (6) in those directions.

## 6. Owned quotient-rule clearance on every chart

Write (5) as sigma_A=N_A/C_A, with N_A a polynomial base coefficient. For any list of the actual nonconstant denominator factors F_n and positive powers e_n, an ordinary coordinate derivation obeys

    partial(N/product F_n^e_n)
       =(partial N)/product F_n^e_n
        -sum_n e_n N(partial F_n)/(F_n product F_m^e_m).     (8)

Multiplication by product F_n^(e_n+1) clears every term. Factors with zero allowance are not added, and polynomial factors stay polynomial. Constants or factors independent of this coordinate have zero derivative and cause no problem. Reducible factors or repeated divisors are permitted: (8) differentiates the named factors with their full multiplicities. Distinct owners keep their factors even when those factors coincide.

Apply (8) to each already-transported chart coefficient (5), with partial=partial_A,d. Then

    H_(i,A)^6 H_(j,A)^6
      product_r L_(i,r),A^3 L_(j,r),A^3
          (T_d sigma)_A is regular.                        (9)

Only legal factors in direction d need a new derivative allowance, but uniform legal three is a harmless weaker certificate. All original powers in (5) are positive, so its owner vector becomes exactly the claimed sufficient bound (6,6)/(3,3). This is not an assertion of exact attained orders. No new owner, affine v0 inverse, curve-branch inverse, or additional standard equation is introduced.

The derivative of the full cleared numerator and every denominator is retained. In particular carrier sections depend on all four coordinates; they must not be frozen merely because a,b are the scalar's character directions. The proof works with their homogeneous local representatives, whose all-chart regularity was supplied by the primitive and raw-block theorems. At infinity t has valuation two on C; (9) is a named-section power bound and preserves that ramification multiplicity.

Together (7) and (9) prove the all-chart extension in the declared output line. This is stronger than a finite quotient-rule estimate and supplies exactly the stripped scalar derivative used by the existing ownerwise bound.

## 7. Connection to the actual E slots and retained frontier

The frozen residual sets p=(0,1), q=(2,3) and calls E(p,q,t) and E(q,p,t). Inside E, the derivatives of T(solver_pair,...) occur only in the two directions of p. The raw override of T is (1), so every one of its eight displayed scalar-derivative slots is complementary. The source has no call here to a same-pair stripped derivative. The checker statically binds this wiring and the raw override.

Consequently the ownerwise proof's two rows `(D s_jk)L` and `(D s_ij)U` may use (6,6)/(3,3) on precisely the scalar's existing endpoints. This closes that explicit premise without changing the numerical residual/lift ledger. The other hypotheses of that ledger retain their own scope: exact derivative denotation, transported matrix/sheaf attribution for the complete source, closure, HPL/class comparison, terminal scalar-kernel attribution, and obstruction values are not inferred from this leaf theorem.

## 8. Static controls and evidence limits

`check_scalar_metadata.py` authenticates inert source/dependency bytes, binds selected complete function ASTs and the exact E/residual/raw wiring, and tests integer character, line-transition, local-sign, owner and denominator-exponent metadata. It enumerates all 16 standard charts, all 256 endpoint legal-mask pairs, all four q directions, and all ordered distinct scalar pairs with their complementary directions. It uses no rational-function engine and evaluates no actual source, model, polynomial, matrix, or jet.

Active negative controls reject a same-pair derivative, repeated scalar directions, wrong scalar character, a missing infinity derivative sign or line shift, charging an infinity q pole to its bit-one endpoint, branch-unit division, merging owner occurrences, undercharging derivative denominators, and deleting a literal endpoint term. These controls check source conventions. The branch-safe module argument, frame comparison, line compatibility and quotient-rule proof above establish the mathematical result; metadata does not replace them.
