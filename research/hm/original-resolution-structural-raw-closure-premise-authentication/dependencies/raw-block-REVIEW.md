Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

# Independent review: all-chart raw connection-block bound

## Verdict and exact version

**ACCEPTED.** The literal raw blocks have owned carrier/legal bound **5/1** on all standard product charts, in the precisely declared product-root model and exact mathematical derivation convention. This closes the imported raw-B5/1 premise of the accepted ownerwise residual/lift theorem. No mathematical correction is required.

The reviewed producer `PROOF.md` has SHA-256

    7fe40702b668068a85e3e7639b3c1b99dc80476c0778aa94592df0b516d1add9.

An exact copy is `inputs/reviewed-PROOF.md`. The raw source has SHA-256

    c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9.

The four block bounds, in source rank order (5,15,10,2), are

    0/1, 5/1, 2/1, 0/1.

The proof also establishes the same clearance for the directly defined single-odd-factor coefficient in its correct O(-2) line. It does not infer this stronger statement by dividing a regular curve function by a vanishing odd factor.

This audit independently derived the chart normalization, common-frame connection cancellation, scalar tables, and matched-factor ledger before reading the producer draft. It then read that draft, the complete frozen raw source, the first-order source, the accepted structural-A and homogeneous proofs/reviews, both accepted product-root reviews, and the accepted ownerwise proof/review. All seven producer dependency snapshots were compared byte-for-byte with these accepted local originals; results are in `dependency-comparisons.json`. Immutable remote provenance is inherited from those packages. No fresh remote read is claimed.

No physical source or model was imported or executed, no actual primitive polynomial or matrix product was constructed or evaluated, no detector or jet was evaluated. The clearing weights 54/29 and standard-factor exponent 5251 remain unchanged.

## 1. Dependencies are sufficient and noncircular

The accepted homogeneous theorem supplies regular polynomial representatives after own-carrier square clearance for H0,H1,I,P, including the auxiliary carrier's genuine double v0 pole. It also supplies polynomial gamma,delta,ev, constant L, and own-carrier-one clearance for W and eta. These are statements about the specified homogeneous lifts on every standard chart, not merely finite rational functions.

The accepted structural contraction supplies the inverse identities for the actual split pairs

    U0=[gamma,I,H1W], Q0=[H0;P;Ldelta],
    U1=[W,eta],       Q1=[L;ev].

In particular Q0 and Q1 are actual inverse matrices in the declared bundle frames. The proof uses that fact only for the split-connection interpretation and the scalar common-frame identity. Its carrier ledger retains every literal product and does not simplify gamma H0, IP, H1W Ldelta, or eta ev using A.

The accepted product-root theorem identifies the actual root N, the explicit N²-to-coefficient-line isomorphism, physical column factors, ambient powers (-1,1,3,5), and old connections. Thus those are available geometric inputs. It does not merely infer a chosen root from equality of its square with another line.

The ownerwise theorem is used to state the downstream consequence. Its old imported raw-block estimate is not an ingredient in this proof, so the dependency elimination is not circular. The rational meaning of `Mat.D` as the invariant V is still a stated semantic convention; parsing the source is not a general proof of the exact-field implementation.

## 2. Exact source columns, inverse rows, and standard charts

I checked the complete `PhysicalModel.blocks` AST, including U0,Q0,U1,Q1, the scaling comprehensions, the minus sign on the moving term, old-connection subtraction, all four ranks, and the two extreme zero moving terms. The source differentiates U only. It does not differentiate Q. Both inverse-row scalings are reciprocal to the corresponding column scalings.

The homogeneous U column degrees, in the actual source order, are

    gamma: 1, I0: 0, I1: 1, H1W: -1, W: 0, eta: -1,

with multiplicities (5,1,1,8,8,2). The Q row degrees are their negatives. These degrees follow from the individual accepted primitive types; in particular H1W has degree -1 and Ldelta has degree +1. The raw multipliers are exactly nu^(-2d), with reciprocal row multiplier nu^(2d). The unequal I-column factors are essential.

On a common standard chart A,

    v_A=tau_A v_ref, ell_A=tau_A^-1 ell_ref,
    c=e_m²/ell_A=nu_m² tau_A.

For a matched degree-d pair, homogeneity gives

    U_ref=tau_A^-d U_A, Q_ref=tau_A^d Q_A.

Therefore its actual source matrices satisfy

    nu^-2d U_ref=c^-d U_A,
    nu^2d Q_ref=c^d Q_A.

This is the required exact replacement of the finite source expression. Simply substituting c for nu² while leaving U_ref unchanged would be wrong. Both v and c acquire the same standard-chart factor, so these actual physical matrices agree before differentiation on all overlaps. No square root of tau is used.

## 3. The common ambient derivative is present twice and cancels

For an ambient N^k term, changing actual legal coefficients to the common rational reference changes the split pair by

    U_common=nu^k U_source, Q_common=Q_source nu^-k.

Since U_source Q_source=Id, its split-connection coefficient becomes

    -(V U_source)Q_source-k Vlog nu Id.

The old connection in the same common frame is

    k alpha_m(V)Id-k Vlog nu Id.

Subtracting gives exactly the raw expression

    B=-(V U_source)Q_source-k alpha_m(V)Id.

The signs are correct in all four powers k=-1,1,3,5. The scalar ambient term cancels because it occurs in both connections, rather than because it was ignored. This also explains the extreme blocks: +alpha Id5 and -5alpha Id2, although their local moving bases are identities. Since each resolution term is one N-power tensored with a constant vector space, conjugation of its degree-zero End coefficient by the common ambient frame is scalar and leaves the matrix unchanged.

## 4. Legal tables and complete literal expansion

Write h=x²-1 and s=1-t². On the finite chart the odd basis element is y; at infinity it is u=y/x² and u²=ts. The invariant derivation acts on base functions by y partial_x and -u partial_t, respectively.

The independently derived table is:

| Chart / legal bit | c factor | L | (Vlog c)/z | alpha(V)/z |
|---|---|---|---|---|
| finite / 0 | 1 | 1 | 0 | 0 |
| finite / 1 | h/x | xh | (x²+1)/(xh) | 1/(xh) |
| infinity / 0 | t | t | -1/t | 0 |
| infinity / 1 | s | s | 2t/s | t/s |

Here z is y or u. The finite bit-one logarithmic derivative follows from 2x/h-1/x=(x²+1)/(xh). At infinity Vlog t=-u/t and Vlog s=2tu/s. The transported old form is -t dt/s, whose contraction is +tu/s. Resetting that old connection to zero at infinity would be wrong. The legal sections are the homogeneous sections Y and X(X²-Y²), with the degree-three change of representative included; xh does not remain an unweighted xh at infinity.

Each row's own L clears both last columns. Their cleared pairs are (0,0), (x²+1,1), (-1,0), and (2t,t). Thus the logarithmic and old-connection terms have legal power one and carrier power zero on the entire standard chart. In particular the infinity bit-zero t denominator is charged even though t is a unit on the original legal intersection. The argument proves extension across that boundary after clearance, rather than relying on unit regularity on the open.

For a degree-d matched pair, the physical derivative identity is

    -V(c^-d U)c^d Q=-(VU)Q+d(Vlog c)UQ.

Consequently the rank-15 logarithmic group is

    beta(gamma H0+I1P1-H1W Ldelta),

and the rank-10 logarithmic group is -beta eta ev. I0P0 has coefficient zero. Both branches of V(H1W) remain present. The old diagonal terms are -alpha Id15 and -3alpha Id10. This verifies all signs, factors and omissions against the source: no derivative, logarithmic contribution, or old term is discarded.

## 5. The carrier maximum is five, not a maximum across factors

For a local homogeneous representative F with H^n F polynomial and n>0,

    partial F=[H partial(H^n F)-n(H^n F)partial H]/H^(n+1).

This formula proves the claimed derivative allowance directly; it applies to reducible H with its full multiplicities. A polynomial derivative remains polynomial and needs no carrier charge.

The seven ordered derivative words have carrier bounds

    (Dgamma)H0                  0+2=2,
    (DI0)P0                    3+2=5,
    (DI1)P1                    3+2=5,
    (DH1)W Ldelta              3+1+0+0=4,
    H1(DW)Ldelta               2+2+0+0=4,
    (DW)L                      2+0=2,
    (Deta)ev                   2+0=2.

Their legal charge is zero. The nonzero logarithmic words have carrier bounds 2,4,3,1, respectively, and legal charge one. The old diagonal words have 0/1. These are sums within each literal product and maxima only across added terms. In particular the derivative of I and its paired P select the same owner, so the carrier charge is 3+2=5; taking max(3,2) would fail.

This gives exactly (0/1,5/1,2/1,0/1) in the source's rank order. It uses neither transition/inverse cancellation nor any trace, curvature, cocycle or residual-closure identity.

## 6. Branches, stripped coefficients, and occurrence multiplicities

The proof first writes each block as z b using the displayed formulas: replace V on base coefficients by partial_x or -partial_t and replace beta and alpha(V) by the table's last columns. Thus b itself is an explicit rational function of the base coordinates whose numerator becomes polynomial after H^5L clearance. No argument divides an arbitrary regular function by y or u at a zero of that function.

This distinction resolves the finite branch points y=0 and the infinity point u=0. The free quadratic coordinate algebras with bases (1,y) and (1,u) then show directly that clearing b also clears B=z b. The proof is valid at those points wherever the relevant carrier/legal sections allow them and proves the stated meromorphic clearance across their excluded divisors.

Since u=t²y, invariance of B gives

    b_infinity=t^-2 b_finite(1/t).

This is exactly the single-odd-character O(-2) coefficient law. It is the gluing law of b, not an extra unowned t^-2 pole to add to its independently established infinity representative. The same proof holds for all 16 product charts and all legal masks, because V_d acts on only the d-th factor of c.

At O, t has order two. The named-factor power bounds retain that multiplicity under pullback; the proof never treats t as a curve uniformizer. The global H and L sections carry their prescribed degrees, and their local cleared representatives glue in the corresponding cleared coefficient line.

There is one actual owner in a `blocks(o,d)` call. In later words, multiple factors selecting that same occurrence add powers there. Distinct occurrences retain separate factors even if their carrier labels or divisors coincide. At a shared prime divisor, the multiplicity-weighted contributions add; equal labels never justify replacing their product by a maximum. No absent endpoint or unrelated standard tag supplies a factor.

## 7. Independent static and formal controls

`check_independent_blocks.py` parses inert source AST and performs integer or formal-word operations only. It authenticates 14 reviewed input/dependency snapshots; its three complete method contracts cover `Mat.D`, `PhysicalModel.nu`, and `PhysicalModel.blocks`, with separate rank checks. It derives column and matched-row degrees from the individual factor words rather than assigning a common degree to I or P.

The independent controls cover 6,144 group/chart/direction exponent cases, 1,024 legal-mask/chart/direction cases, all seven ordered Leibniz words, the four nonzero logarithmic words, the four ambient-power cancellation identities, odd coefficient gluing, and occurrence multiplicities. Fifteen active rejection controls detect:

1. Wrong inverse-row scaling.
2. Wrong source old-connection sign.
3. Wrong raw derivative direction.
4. Wrong first physical column factor.
5. A missing I1 multiplier.
6. Missing tau in c=nu²tau.
7. The omitted W derivative branch.
8. Reversed matrix-factor order.
9. Maximum instead of sum at one owner.
10. Missing old common-frame derivative.
11. Missing infinity bit-zero logarithm.
12. A false flat reset of the old infinity connection.
13. Legal-zero clearance.
14. The wrong stripped gluing exponent.
15. Merging distinct equal-label occurrences.

Normal and optimized Python reports are byte-identical (`normal.json`, `optimized.json`). Checks use explicit exceptions, so optimization does not remove them. These controls bind syntax and discriminate finite metadata mistakes; the scalar identities, sheaf interpretation, and quotient-rule proof above supply the mathematics. The tests are not proof of arbitrary interpreter or arithmetic semantics.

I also read the complete producer checker before running it. Its normal and optimized reports are byte-identical and recorded separately as `producer-normal.json` and `producer-optimized.json`. It authenticates nine inert inputs and checks 1,024 legal/chart/direction combinations, 15 ledger rows and eight rejection controls. It imports no physical source or pinned model. Its bounded static claim is accurate.

## 8. Exact consequence and retained frontier

The accepted ownerwise theorem may replace its raw-B5/1 input with this source-bound all-chart theorem without changing any of its numerical constants. Its accepted residual 16/10 and block-sensitive J3 24/10 conclusions remain conditional on their other stated requirements. This review does not silently discharge their complementary stripped derivative convention, complete residual assigned-sheaf membership, exact implementation semantics, HPL/class comparison, closure, or obstruction interpretation.

In particular this packet provides no actual terminal value, detector evaluation, Ward/residue computation, algebraicity conclusion. It replaces one precise imported mathematical pole premise with a direct proof in the accepted model.
