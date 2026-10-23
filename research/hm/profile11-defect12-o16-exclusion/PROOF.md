# Saturation of the positive line excludes three defect-twelve O(16) labels

## Result and scope

The following three maximal profile-(1,1) labels are impossible:

    G3.11.1e318198128e:
      A_q=O(-10)+O(-8)+O(16), B_q=O(-18)+O(-6)+O(8);
    G3.11.6795493ae8cd:
      A_q=O(-10)+O(-8)+O(16), B_q=O(-18)+O(-4)+O(6);
    G3.11.a5d4e292b34e:
      A_q=W O(-9)+O(16),     B_q=O(-18)+O(-4)+O(6).

All three original determinant defects equal twelve. Nevertheless, the positive O(16) image is already saturated. The defect is confined to the remaining quotient directions. This is enough to apply the top-block and polar obstruction of the zero-defect O(16) theorem. Its remaining constant-span case is then excluded directly from the actual connection, without assuming that the full derivative image is saturated.

This proves exactly the three named exclusions. It does not exclude any unnamed label or source2, and does not establish the original global rank goal. No selected actual coefficients, parameters, points, derivative values, matrices, source-instance ranks, selected-model experiments, scans, or large computation are used.

## 1. Immutable dependencies and complete source overlists

The original data are at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

of Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files used are:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md;
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md;
- ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md;
- one-one-endpoint-necessary-pairs.json;
- rank-three-quotient-frontier-144.json.

The stable labels have source_index25,26,36, respectively. The first two have exactly the four compatible source tuples

    (0,0,0,0,0,2,0,1), (0,0,0,0,1,1,0,1),
    (0,0,1,0,0,1,0,1), (0,1,0,0,0,1,0,1).

The third has those four together with

    (0,0,0,0,0,1,1,0), (0,0,0,0,1,0,1,0),
    (0,0,1,0,0,0,1,0), (0,1,0,0,0,0,1,0).

These are the identical source overlists used by the zero-defect O(16) theorem, PR802 at commit

    e484640a6565c278321bf6557860262c1ac1b7df,

in

https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

We use only its Sections 2-5, which analyze the top positive quotient, its exact kernel and internal derivative, and its quadratic first polar. Their saturation hypothesis will be proved independently here. We do not import its original-defect-zero identity E^+/E=A_q(2), its exact projected forward quotient, or its use of saturation of the whole original derivative image.

Explicitly the first four sources are

    E0 = (P+2D) O(-2)+2 O(-8)+O(-10),
    U6 = (2P+D) O(-2)+Wp O(-5)+O(-8)+O(-10),
    E3 = (V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    E6 = (P+D) O(-2)+T O(-3)+O(-8)+O(-10),

and the additional four are

    E10 = (P+2D) O(-2)+O(-8)+W O(-9),
    U13 = (2P+D) O(-2)+Wp O(-5)+W O(-9),
    E12 = (V+P+D) O(-2)+V O(-4)+W O(-9),
    E13 = (P+D) O(-2)+T O(-3)+W O(-9).

The representation notation and names U6,U13 are as in the cited theorem. E is the actual saturated rank17, degree-54 bundle in the constant thirty-space H O. Put Q=(H O)/E. Its actual quotient A_q=E/E^- has an injective transpose map

    i:A_q -> B_q^*(-2) -> Q(-2).                       (1)

The first injection need not be saturated. The second is saturated because B_q is a locally free quotient of Q*. The derivative of E is the composite of the onto quotient E->A_q with (1). Also H0(E^-(2))=0.

## 2. The positive summand is saturated even though the total defect is twelve

The middle bundles in (1) are, respectively,

    O(16)+O(4)+O(-10),
    O(16)+O(2)+O(-8),
    O(16)+O(2)+O(-8).                                  (2)

The O(16) summand of A_q has no map to either lower summand in (2). Its restriction under i is nonzero, because i is injective. Therefore it is a nonzero scalar isomorphism onto the O(16) summand of (2).

It follows that i(O(16)) is saturated in Q(-2). Indeed it is a direct summand of the saturated middle bundle in (1), so its quotient in Q(-2) is locally free. No assertion about the saturation of i(A_q) follows or is needed.

For every listed source, let F=R O(-2) be its canonical top block. Since A_q/O(16) has only negative degrees -8,-10 or -9, the actual quotient restricts to p:F->O(16). The strict-top vanishing injects R into H0(O(18)); dim R is at least nine. A common zero divisor would be invariant of degree at least twelve and leave at most seven independent sections, which is impossible. Thus p is onto.

Set K0=ker p and let J be the image of its actual internal derivative K0->(E/F)(-2). Whenever J is saturated, the actual full derivative image I of F is saturated and has

    0 -> J -> I -> O(16) -> 0,
    0 -> F -> F^+ -> I(2) -> 0.                         (3)

The proof uses only saturation of i(O(16)), now established, and saturation of J. It is the same locally free quotient argument as Section 2 of PR802. In particular no global zero-defect assumption is used in (3).

## 3. Transfer of the top-block and polar reduction

All inputs to Sections 2-5 of PR802 are now present: the same exact source list, the same actual quotient A_q, the onto top map, and the same saturated positive image. Here is the resulting reduction, including its precise dependency boundary.

For E0,E10 the internal map vanishes, and the quadratic Gauss gap excludes rank F=14 with F^+/F=O(18). For U6,U13 the exact top kernel is

    (Wp+T) O(-3)+V O(-4)+O(-6);

its internal map vanishes by degrees. The gap excludes rank F=13 with that same quotient. For E3,E12 the two exact kernel possibilities are

    T O(-3)+P O(-4)+O(-6),
    (Wp+T) O(-3)+Wp O(-5)+O(-6).

Their only apparent degree exception is the zero equivariant map O(-6)->V O(-6). The gap excludes rank F=12. These arguments need only (3), not the global derivative saturation.

For the W O(-9) quotient, E6 is also excluded because only its O(-10) summand can map to W O(-9), giving image rank at most one. Thus only E6 remains for the first two labels and E13 for the third. Write, respectively,

    E=(P+D) O(-2)+T O(-3)+L,
    A_q=O(16)+L,
    L=O(-8)+O(-10), or L=W O(-9).                     (4)

For F=(P+D) O(-2), the complete top-kernel possibilities from PR802 Section 3 are

    V O(-4)+P O(-4)+O(-6),
    Wp O(-3)+V O(-4)+Wp O(-5)+O(-6),
    T O(-3)+O(-6)+O(-10).

The first two give J=0. The third has only a possible O(-10) internal image, and every nonzero such image is saturated: its quintic T component is the complete tautological line, or its lower scalar component is an isomorphism. If J=O(-10), first-polar generation and the exact characters force

    F^+=A O+(Wp+T) O(-1).

The three-channel contradiction of PR802 Section 5 applies verbatim. It uses the actual constant A quotient, the Euler maps P O(-2)->Wp O(-1) and D O(-2)->T O(-1), and the nonzero degree-seven two-section map from the Euler kernel to the multiplication cokernel. The latter has no invariant base divisor. The projected first polar would contain a forbidden constant subspace or itself be a horizontal negative bundle. Every saturation used there follows from (3), so this case remains excluded at defect twelve.

Consequently the only unexcluded possibility after the transferred reduction is

    J=0,
    F^+=C0 O,    dim C0=10,
    C0=A+V+P,
    (C0 O)/F=O(18).                                    (5)

The constant assertion follows because (3) gives a saturated rank-ten degree-zero subbundle of H O. Its character is Sym18 W-(P+D)=A+V+P. Thus this is a genuine constant subspace of H, not an abstract bundle splitting.

## 4. Constant projection remains saturated

The map of C0 O into Q has image precisely the positive O(18)=i(O(16))(2), and its kernel is F. This is the actual derivative-image sequence (3) with J=0. By Section 2 this image is saturated in Q. Therefore

    E intersect (C0 O)=F,
    (E+C0 O)/E=O(18),

and E+C0 O is saturated in H O. Constant projection consequently gives an actual saturated embedded bundle

    Z=(E+C0 O)/(C0 O)=E/F=T O(-3)+L                   (6)

in the constant quotient (H/C0) O.

This saturation is proved from the positive image, not inferred merely from local freeness of E/F. The original raw derivative image may still have defect twelve, and we do not identify Z^+/Z with L(2).

## 5. A direct horizontal-top contradiction, without full derivative saturation

The original derivative of E factors as

    E -> A_q -> Q(-2).

Projecting its target to (H O/(E+C0 O))(-2) kills the entire positive O(16) image by (5). It also kills the derivative contribution from F, since C0 is constant and contains F and its first osculation. Thus it descends to the actual derivative of Z in the constant quotient, and factors as

    Z=E/F -> A_q/O(16)=L
      -> (H O/(E+C0 O))(-2).                           (7)

The factorization is enough; saturation of the final image is not asserted.

Let M=T O(-3) be the actual canonical top block of Z in (6). Every map M->L is zero by ordinary degrees. Equation (7) therefore gives beta_Z|M=0, so the derivative of M lands in Z. Its remaining internal component is the O-linear map

    M -> (Z/M)(-2)=L(-2).

This map also vanishes by ordinary degrees. Hence the derivative of M lands in M itself: M is horizontal inside the actual constant (H/C0) O.

A horizontal subbundle of a constant bundle over P1 in characteristic zero has constant Grassmannian map and therefore degree zero. But M has rank six and degree -18. This contradiction excludes (5).

The source reduction was exhaustive, so all three complete labels stated at the beginning are excluded.

## Contribution and limitations

The new point is that saturation of the highest positive line can survive a nonzero determinant defect. That partial saturation is enough both for the quadratic polar analysis and for a genuine constant projection. The final contradiction needs only a derivative factorization that kills the negative top block, not an exact saturated projected forward quotient.

No argument treats a jumping full fiberwise intersection as a sheaf intersection, assigns a connection to an abstract complement, assumes E^+ is an interior stage, reruns a numerical envelope, or evaluates selected actual data. The only conclusions are the three specified exclusions; unnamed branches, source2, and the global goal remain separate.
