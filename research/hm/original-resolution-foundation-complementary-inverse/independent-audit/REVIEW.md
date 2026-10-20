# Independent review: the six complementary inverses

## Verdict

ACCEPTED for the precisely pinned rational/localized theorem

    T_i M_i=Id8,  M_i T_i=Id8,  T_i=M_i^(-1),  i=0,...,5.

Here M=L delta E_S and T=E_S^t H1 W in the previously fixed increasing S and cyclic nonpivot target orders. This review independently derives the solve, checks every inverse coefficient and denominator sign, and separately binds all 900 stored H1 cells and all 384 selected delta cells. No primitive A, historical contraction receipt, A-dependent determinant normalization, physical matrix product, source evaluation, source import, or remote write was used.

The reviewed producer proof is `../complementary-inverse-20261018/PROOF.md`; the reviewed immutable local snapshot is `inputs/reviewed-PROOF.md`. Input and review hashes are recorded in `review-pins.json` and `SHA256SUMS`. There is no new remote-source authentication claim in this review.

## 1. Independent derivation of the primary inverse

Write u1,...,u8 for ambient coordinates in the cyclic transported order s, and z1,...,z8 for the selected target coordinates. Let

    Delta=abcd-t^4,   D=t Delta.

The independently inspected selected delta records give

    z1=t u2+c u6,       z2=-t u5+d u7,
    z3=-a u6+t u8,      z4=-t u1-b u7,
    z5=t u7-b u8,       z6=-t u3+a u8,
    z7=t u4-d u5,       z8=c u5-t u6.

Localizing at D makes both t and Delta units. Solve the cycle in the order u6,u8,u7 in terms of u5:

    u6=(c u5-z8)/t,
    u8=(z3+a u6)/t,
    u7=(z5+b u8)/t.

Substitution in z2=-t u5+d u7 gives, with the sign checked independently,

    Delta u5=t^3 z2-bdt z3-dt^2 z5+abd z8.

The other cycle coordinates are

    Delta u6=ct^2 z2-bcd z3-cdt z5+t^3 z8,
    Delta u7=abc z2-bt^2 z3-t^3 z5+abt z8,
    Delta u8=act z2-t^3 z3-acd z5+at^2 z8.

These identities follow by the three displayed substitutions, using Delta=abcd-t^4. The four forced coordinates are

    u1=-(z4+b u7)/t,    u2=(z1-c u6)/t,
    u3=(a u8-z6)/t,     u4=(z7+d u5)/t.

Consequently the inverse numerators over D are

    D u1=-ab^2c z2+b^2t^2 z3-Delta z4+bt^3 z5-ab^2t z8,
    D u2=Delta z1-c^2t^2 z2+bc^2d z3+c^2dt z5-ct^3 z8,
    D u3=a^2ct z2-at^3 z3-a^2cd z5-Delta z6+a^2t^2 z8,
    D u4=dt^3 z2-bd^2t z3-d^2t^2 z5+Delta z7+abd^2 z8,
    D u5=t^4 z2-bdt^2 z3-dt^3 z5+abdt z8,
    D u6=ct^3 z2-bcdt z3-cdt^2 z5+t^4 z8,
    D u7=abct z2-bt^3 z3-t^4 z5+abt^2 z8,
    D u8=act^2 z2-t^4 z3-acdt z5+at^3 z8.

Every sign and power agrees with producer equations (1)-(4). The four coefficients +/-Delta are degree four in the formal labels, whereas dh=D is degree five. In particular, the forced-coordinate numerators contain Delta, not D. This distinction matters on nonfinite primary carriers and is checked independently on each carrier.

All substitutions are reversible over the D localization. For any z they construct one solution, and uniqueness follows from the closing equation and forced recurrence. Thus the linear map represented by the displayed coefficient table is the two-sided inverse. Neither a computed determinant nor a sampled source value is needed.

## 2. Independent derivation of the auxiliary inverse

Use S=(0,1,2,3,6,9,12,13), target order (1,2,3,4,6,7,8,9), and a=v1,b=v2,c=v3,d=v4. The literal selected equations are

    z1=u4+c u7,        z2=-c u1+d u8,
    z3=b u1-d u2-a u7, z4=c u2-u3-b u8,
    z5=u8, z6=-u5, z7=u6, z8=-u7.

They give u8=z5,u5=-z6,u6=z7,u7=-z8 first, followed by

    u4=z1+c z8,
    u1=(-z2+d z5)/c,
    u2=-b z2/(cd)-z3/d+b z5/c+a z8/d,
    u3=-b z2/d-c z3/d-z4+ac z8/d.

The z5 coefficient of u3 is zero because the two terms b z5 cancel. The stated source normalization is E=dh=-a^2cd, not +a^2cd. Multiplying these handwritten formulas by E gives exactly producer equation (8), including positive a^2cd in the u5 and u7 rows, negative a^2cd in the u6 and u8 rows, and negative a^2c^2d in the u4,z8 slot. All factors required for the solve are units in the E localization. The solve is unique and supplies both inverse directions without determinant normalization.

## 3. Source identification and coordinate audit

The source model has SHA256

    635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926

and Git blob fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761. The inert decoder excerpt has SHA256 c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94. Its text explicitly identifies H1=evm(c.H1,c.dh), delta=evm(data.delta,one), and the stated W/L orders. No part of this source was executed or imported.

The independent checker uses sparse dictionaries indexed by the handwritten coordinates, with signed letter words rather than the producer's dense numeric-label tables. It only converts one formal word at a time into the stored sign/exponent representation, checks fixed bytes, and compares records. It never combines source expressions or source cells. For r=0,...,4, the relabeling is (t,a,b,c,d)=(v_r,v_(r+1),v_(r+2),v_(r+3),v_(r+4)); v0 labels disappear. The auxiliary case uses the independent table above.

Results:

- All 384 selected delta cells agree, including all empty cells.
- All 900 H1 cells agree, including all 516 cells outside the selected 8x8 submatrices.
- All six dh records agree with D or E, including signs and homogeneous powers.
- Every ambient partition and target pivot is correct.
- Nine adverse in-memory metadata controls are rejected: primary sign, primary exponent, auxiliary sign, missing auxiliary coefficient, outside-S leakage, pivot-column leakage, denominator sign, minor sign, and pivot order.
- The normal and optimized Python reports are byte-identical. Checks use explicit exceptions and survive optimization.

The source proof correctly handles the difference between unsorted cyclic s and increasing S. If E_s=E_S Pi, then M_s=M Pi and T_s=Pi^(-1) T; therefore T_s M_s=Pi^(-1)(TM)Pi. There is no extra determinant sign in this equality of maps.

All H1 pivot columns are literally zero, so selecting nonpivot columns gives H1W without a physical product. All H1 rows outside S are literally zero. These statements are included in the full-cell checks; they are not assumptions inherited from A.

The producer's static checker and controls were read as text. Its arithmetic control is a separately invented three-cycle with a forced coordinate and an unrelated four-coordinate triangular system; it reads no model, uses no source values, and is not a specialization of this eight-coordinate source. Such controls test the elimination method but do not replace the source-binding proof. This independent review needs no numerical control for the actual source.

## 4. Exact consequence for A, and its dependency condition

The inverse theorem above is independent of the following composition. Only after the previously accepted retraction/support theorem, quotient projection Pgamma=0, common syzygy delta gamma=0, pivot splitting, and C: ev delta=0 are supplied for these same pinned formulas, set

    N=[gamma | I | E_S],
    R=gamma H0+IP+H1delta-Id15.

N is invertible by the already proved block triangular decomposition. Its first two inverse block rows are H0 and P. The previously established exact normal form, with the new TM=Id8 inserted, becomes

    N^(-1) R N = [ 0  0           0 ]
                 [ 0  0           0 ]
                 [ 0  T(Ldelta I) 0 ].

Equivalently,

    R=E_S T(Ldelta I)P.

T is now proved invertible. Thus the equivalences are exact:

    A  iff  Ldelta I=0  iff  delta I=0.

The last step uses delta=WLdelta from C and the pivot splitting; the reverse implication is immediate by applying L. The remaining reduced family has 8x2=16 displayed scalar positions per carrier, 96 over all six carriers. This is a count of displayed positions, not an independence or minimal-generator claim. No invertibility or contraction consequence of A has been used to establish any premise in this composition.

This review does not assert delta I=0. If that identity is separately proved and independently accepted for the same pinned source, then this composition proves A. Only at that point may the earlier A-dependent contraction and determinant consequences be invoked, still subject to all of their remaining geometric, localization, frame, and semantic premises.

## 5. Scope boundary

No physical source product, polynomial expansion of actual source expressions, source specialization, source jet, production evaluation, external publication, or remote mutation was performed. The accepted result is the rational/localized complementary inverse and its conditional placement in the exact A reduction. Legal regular extension, full physical-frame interpretation, retained-test values, and the global obstruction are not proved by this review.

Reproduce the independent static check with `python check_independent_binding.py` and `python -O check_independent_binding.py`. Their reports are bundled as `normal.json` and `optimized.json`.
