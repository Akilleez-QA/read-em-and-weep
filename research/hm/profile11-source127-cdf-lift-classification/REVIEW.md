# Independent review of the c-d-f lift classification

## Verdict and exact reviewed version

**PASS, with the scope stated in the proof.** The scalar and quartic lifts are removable by regular operations of the stated kind. The resulting equivalence classes of the displayed abstract inclusions, over the fixed base and fixed G-action, are exactly the members of the PR876 family. The two excluded projective parameter points are distinct. No mathematical blocker was found.

This review was completed independently on 2026-10-23 after reading the entire submitted proof, the entire pinned PR920 canonical-tower proof, the entire pinned PR876 family proof, the original actual and strict-top notes, and the relevant original source-catalog records. It binds the following exact files:

- `PROOF.md`, SHA256 `373546019cfbaa6f2a8acfd9653acc1201cb43bafaaeac90f574878ef20ab3e6`.
- `verify.py`, SHA256 `f6d1471702080f93d5820ccb817432528b32da1685a79a9f738ce6d9df6e7a2a`.
- `REPRODUCE.md`, SHA256 `f11460dda09e7796af902ffe2e9c336705d2cc21940b1fecd74d948067b05918`.
- `audit-inputs/manifest.json`, SHA256 `724ef8e88893cf77faf16af5feb0ea9e6639b6a799387f03857d9795503e056f`.

The reviewer did not modify the proof or verifier. After the initial review, the author made one terminology correction in Section 6: “the determinant-condition kernel is exactly the projective line represented by f12 times the P6 covariant line” became “the determinant-condition kernel is exactly the one-dimensional covariant line represented by f12 times the P6 covariant line”. I verified byte-for-byte that reversing this sole replacement recovers the initially reviewed proof SHA256 `e4b3b67f37b39b2134455132e4d967665d80251e2d7f5b92c5dd77a2dc1c9261`, with no other changes. The correction properly distinguishes a linear covariant line from its projectivization, which is one point; it changes no mathematics. The unchanged verifier was rerun successfully. Approval binds the final proof hash listed above, not a future revision.

The theorem is conditional on the exact canonical-tower hypotheses and interface recorded in Section 1. It is not a statement that source splitting alone forces the displayed quotient or Gauss profile. Its conclusion concerns embedded constant-bundle inclusions, allowing regular source reparametrization, under G-equivariant constant ambient isomorphisms over the identity of P1. It neither identifies an actual HM parameter nor extends the isomorphisms to additional fixed HM maps. It makes no moduli-scheme or family-level trivialization assertion and excludes no source or stable label.

## 1. Six-input provenance and original source identity

For each of the six local source files I recomputed Git's blob hash from the exact bytes, using SHA1 of `blob <byte length>\0<contents>`. Every result agrees with the frozen manifest. The pinned reference/path pairs are those recorded in the manifest and reproduction note; no moving branch, replacement dependency, or unpinned local version was used.

The four original inputs are pinned to commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, under `research/hm/order-four-quadratic-load`:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, local `ACTUAL.md`: 9,672 bytes; Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`; SHA256 `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`, local `STRICT-TOP.md`: 4,983 bytes; Git blob `d7506dae49b4be43230450c4132bd5db91f137ef`; SHA256 `53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08`.
- `one-one-endpoint-necessary-pairs.json`, local `pairs.json`: 58,635 bytes; Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`; SHA256 `6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb`.
- `rank-three-quotient-frontier-144.json`, local `frontier.json`: 378,361 bytes; Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`; SHA256 `a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad`.

The two complete proof dependencies are:

- PR876 at commit `7c7f25911ae1df3590c2b4ffe541c21bae9b1574`, path `research/hm/profile11-source127-cdf-open-family/PROOF.md`, local `OPEN-FAMILY.md`: 13,611 bytes; Git blob `659a90911244172b222f366d8b7dea9b88e88814`; SHA256 `181c81c415427abef3b0e046a2791eea39bbbb65084c64afdab9227c515d1547`.
- PR920 at commit `1528ff8ea56b21e03f7501a962bdaa6728a75904`, path `research/hm/profile11-source127-cdf-normal-form/PROOF.md`, local `NORMAL-FORM.md`: 20,293 bytes; Git blob `718b5245560a84568492874bab8d8c34730e8319`; SHA256 `5cc83c225a03ba670b7859d1a64aec161611ec9cc35fffe79479fdd5b7dadf62`.

This is an exact byte-level check against the supplied immutable manifest, not a fresh assertion about mutable GitHub branch state.

The original record `pairs[127]` has defect zero, contains the tuple `(0,0,1,1,0,1,0,0)`, and has the exact A and B quotient rows `(-8,2,16)` and `(-18,-4,6)`, respectively, all with trivial coefficient representation. The corresponding frontier case is `G3.11.cce6e3ba4eeb`, source index 127, original defect zero, profile `11`. Its existing status remains `not_excluded`.

Using the actual note's tuple convention, c=d=f=1 gives the negative blocks `(V+P)(-4)+O(-8)` and forces the top block `(P+D)(-2)`. Thus the proof uses the original source tuple, not a reduced or relabeled surrogate. The original presentations supply the stated cohomology and degree constraints, while the strict-top note proves the negative-kernel vanishing by the second fundamental form and saturation, without assuming a horizontal splitting of E.

## 2. Audit of the whole canonical-tower dependency

I checked the chain of geometric conclusions in the pinned PR920 proof, including the points needed to turn character information into actual constant spaces and saturated bundle maps.

1. The positive Gauss preimage has Euler character `A-V-2P-D`. Its A-isotypical space of constant sections is exactly one copy: it maps only to the high line, injects there because `H0(E)=0`, and that high line's coefficient system contains A once. The A-to-O(18) map has no base divisor. A common divisor has degree at most 16; the only possible positive invariant degree in that range is 12, and removing it would require A in `Sym6=V+P`, which is absent.

2. The rank-two kernel of this map has negative degrees summing to -18. The listed scalar possibilities and W/Wp alternatives are exhaustive with the prescribed central parity. Its H1 character leaves W(-9) and the scalar pair O(-8)+O(-10); the latter cannot map injectively to A O because `Hom_G(O(-8),A O)=0`. The remaining kernel is therefore W(-9), as an actual bundle. The original negative external row is supplied only by the scalar source block, forcing this kernel to lie in the original `E_hat=F+B_src`.

3. Projection by A gives a saturated E' and a genuine direct decomposition `E'=E0+O(-8)`. The degree bound `[-4,0]` for E0 follows from generation after twist four and its injection into a constant bundle. In particular, it is not an assumption about the connection.

4. The standalone derivative of E0 is justified by the extension calculation, not only its external row. The preimage of O(2) is an extension of O(2) by O(-10). Its equivariant extension group is `H1(O(-12))^G=(Sym10 W)^G=0`; the splitting is unique since the corresponding Hom is zero. The map to O(-10) then vanishes by the actual degree bound. This proves the saturated standalone O(2) derivative image and removes the possible internal derivative toward the scalar block.

5. In the equivariant splitting of E0, the degree-zero and degree-minus-one part has zero external derivative by its characters and zero internal derivative by degrees. Horizontality and saturation therefore force its negative part to vanish. For the negative quotient E1, the top coefficient must inject into the complete D coefficient space of O(2); this leaves C2 equal to zero or D. The Euler equations and genuine-representation conditions then give exactly the three alternatives printed in PR920. In particular, the excluded 2V alternative would require the nongenuine representation `T-Wp`.

6. The original P(-2) injects after projection by A because it has no map to A O. Its presence eliminates both first alternatives: rank excludes an injection into V O, while an injection into P O would require a nonzero invariant determinant of degree eight. The surviving constant space is V+P. The ensuing generic containment of W(-9) in F extends to a sheaf containment because the complementary source is torsion-free. Saturation and degree zero then make `F/W(-9)` isomorphic to that actual constant V+P. This constructs C10 and the exact quotient O(18), rather than merely inferring them from ranks.

7. Both V and P components of the residual B derivative are nonzero by the preserved-negative-subbundle obstruction. The complete degree-six system consequently starts the genuine Euler-kernel flag. At every lower step, the derivative cannot vanish and the relevant equivariant map is the complete evaluation system. This gives all saturated kernels down to O(-10), and all reverse first spans, not just generic ranks. The full coefficient span of this last line is Sym10: a proper quotient has dimension at most eight, and dimension eight contradicts the negative degree of the rank-eight saturated first span B+.

8. Full span of the projected whole inclusion then forces the scalar coefficient space to be all of Sym8 and to be disjoint from the Sym10 coefficient space. This is the actual quotient decomposition used by the submitted proof.

9. Finally, `F(1)=(P+D)O(-1)` is acyclic, so the actual degree-nineteen multiplication map is an isomorphism and the high quotient parameter lies in the exact PR876 open set. The raw first-polar image of F is generated after twist one and has defect degree at most ten; invariant-divisor degree at least twelve eliminates that defect. PR920 explicitly retains arbitrary regular u and v across C10. The submitted proof addresses those retained lifts and does not assume their prior removal.

The canonical nature of the tower is also sufficient for the later uniqueness argument: A is defined from the positive Gauss preimage, the high source piece is its intrinsic slope piece, and the subsequent constant space is the space of constant sections of the specified quotient. Constant ambient equivalence preserves these constructions.

## 3. Audit of the whole PR876 family and the exact open set

Write `M_R(n)=Hom_G(R,Sym^n W)`. The degree-eighteen quotient contains the unique nonzero A and V components and a projective P covariant `p in P(M_P(18))`. Its multiplication map has the exact blocks

    W: a_W; S: a_S; Wp: p_Wp(p);
    T: [v_T, p_T(p)].

The pinned proof establishes the nonzero and isomorphism assertions geometrically:

- The A-to-W channel is nonzero by the degree-eighteen Euler sequence, vanishing left invariant space, and vanishing H1.
- The A-to-S channel is fiberwise injective multiplication by the formal vector.
- The V-to-T channel is nonzero because `V tensor W -> T` is an isomorphism and tensoring a nonzero covariant with the formal vector does not give zero.
- The P-to-Wp channel is onto with a one-dimensional kernel by the Wp-tensored Euler sequence.
- The P-to-T map is fiberwise injective multiplication `W tensor Wp -> Sym2 W tensor Wp`, hence injective on covariants. Both covariant spaces have dimension two, so it is an isomorphism.

Consequently the exact definition is

    Omega = { [p] : p_Wp(p) != 0 and det(v_T,p_T(p)) != 0 }.

Both expressions are nonzero linear forms on the two-dimensional multiplicity space. Before the new argument, PR876 proves only that their projective zeros are at most two points; it does not already prove distinctness.

For p in this open set, the complete degree-nineteen multiplication map implies no common basepoint in q_p. Acyclicity of its kernel after twist one forces pure degree -2, and the Euler character gives exactly `(P+D)O(-2)`. The first-polar argument eliminates all raw derivative defect using the bound ten and the minimum invariant divisor degree twelve. The two residual blocks have the stated universal exact quotients, saturated derivative images, and full coefficient spans. Their actual constant direct sum therefore gives the displayed A and B Gauss quotients; using additivity here is legitimate because the direct sum has already been constructed.

I also checked the forward and reverse plateau arguments: the standard blocks have the claimed consecutive rank gains, and the nondegenerate high quotient curve has generic second osculating rank three by the characteristic-zero Wronskian argument. No assertion of everywhere unramified higher osculation is required. Thus every p in Omega really supplies a compatible abstract inclusion with both maximal plateaux of length one. The pinned proof's within-family uniqueness is consistent with, but does not substitute for, the submitted exhaustion argument.

## 4. Scalar lift, quartic dimensions, and the exact jet convention

The standard scalar line j has a coefficient isomorphism from Sym8 W onto C9. Accordingly a regular map `O(-8)->C10 O` is exactly a degree-eight C10-valued coefficient system, and composition with j identifies it with one and only one constant map `C9->C10`. This is the full coefficient identification, not merely the assertion that j spans generically. The associated triangular ambient map is invertible, equivariant, fixes C10 and C11, removes v, and does not change u.

For the quartic lift,

    Hom_G(C11,C10) = C^2,
    T=Hom_G((V+P)(-4),O(18)) = C^2.

The first dimension comes from the common A and V components; the second from the unique V and P in Sym22. Neither dimension statement alone proves that the map `R(w)=q w i` is invertible.

Here is the exact interpretation of the kernel used to prove it. For a nonzero formal vector spanning ell, the invariant alternating form identifies that vector with a covector whose kernel is ell itself. Under the induced identification of symmetric powers with binary forms, an element of `ell^4 Sym6 W` is precisely a degree-ten form divisible by the fourth power of the linear equation of that point. It therefore vanishes there to order at least four, and every such form lies in this subspace. This convention does not interchange the chosen point with an unrelated dual point.

Thus `U_6^10=ell^4 Sym6 W` is exactly the kernel of evaluation of jets of orders zero through three. The quotient is the rank-four principal-parts bundle `S O(7)`. Equivalently, the standard invariant perfect pairing on Sym10 pairs this kernel with the annihilator of `ell^7 Sym3 W`, and dualizing the standard osculating Euler sequence gives the same quotient. This verifies both the kernel and the quotient using the same self-duality convention; it is not an appeal to a transpose having an unrelated kernel. Its rank and degree are also correct: 11-7=4 and 0-(-28)=28.

## 5. Universal Wronskian proof and removal of the quartic lift

The D summand is a genuine five-dimensional constant subspace of Sym10. Restriction to an affine chart is injective on homogeneous degree-ten forms, so it becomes a five-dimensional space of polynomials of degree at most ten. Any four-dimensional subspace admits a basis with distinct degrees: the filtration by degree increases by at most one at a time, and elimination against leading coefficients constructs such a basis.

For increasing degrees `n0<n1<n2<n3` and nonzero leading coefficients a_i, the coefficient of the highest possible power in the Wronskian is

    (product a_i) det((n_i)_j), 0 <= i,j <= 3.

Its power is `sum n_i - (0+1+2+3)`, which is nonnegative because four distinct nonnegative integers have sum at least six. No lower-degree term of any polynomial can contribute to that highest power. The falling-factorial polynomials have successive degrees zero through three and are monic; changing from them to ordinary powers is triangular with diagonal one. Their determinant is therefore the Vandermonde product, up to the fixed ordering sign, and is nonzero for distinct degrees in characteristic zero. This also covers degrees smaller than some derivative order: individual falling factorials may vanish, but the full determinant does not.

Consequently the order-three jet map of these four independent sections is generically an isomorphism onto its four-dimensional target. The restriction from the full D space is generically surjective. This reasoning chooses no actual HM/source coefficients, no actual parameter or point, and performs no derivative-value or instance-rank calculation.

If `R(w)=0`, exactness of the universal quotient factors `q w` uniquely through a regular bundle map

    gamma:S O(7)->O(18).

The factor is equivariant by uniqueness. Since C10 has no D, a constant equivariant w kills D, so `gamma pi_D=0`. Generic surjectivity of pi_D implies that gamma vanishes over the function field. As a regular morphism between locally free sheaves on the integral curve P1, gamma is then zero everywhere. **Everywhere surjectivity or saturation of pi_D is not needed and is not asserted.**

Now `q w=0`. The constant coefficient map of q is injective because `H0(F)=0`; hence w=0. The two-dimensional map R is therefore injective and consequently an isomorphism. This proves the necessary nondegeneracy rather than inferring it from multiplicities.

The uniquely corresponding constant shear removes `t=q u`. The remaining `u'=u-w11 i` lies in the sheaf kernel F, so exactness factors it through a regular equivariant map `B->F`, not just a rational map. Its graph is removed by a triangular automorphism of `F+B+L_-`. This operation does not alter the generated embedded subbundle. The scalar and quartic shears act on different complement coordinates, and their order does not restore a removed lift.

All claimed normal-form changes are therefore regular. The proof never applies connection-rank additivity to an extension before removing it.

## 6. Independent reconstruction of the two distinct exceptional lines

This section was checked independently of the numerical dimension assertions.

Choose only the invariant line `M_1(12)`, represented by a nonzero f12. Multiplication by f12 in the polynomial ring is injective. Because `M_V(6)` and `M_V(18)` are each one-dimensional, it identifies the unique V18 covariant line with `f12 M_V(6)`. It also sends the nonzero one-dimensional space `M_P(6)` injectively to a line

    L_det = f12 M_P(6) subset M_P(18).

First consider the T channel at degree six. The map `V tensor W -> T` is an isomorphism. A nonzero V-valued degree-six covariant tensor the formal nonzero homogeneous vector cannot be the zero polynomial covariant. Its T7 image is therefore nonzero. For the P channel, use `P=W tensor Wp` and `T=Sym2 W tensor Wp`. At every nonzero formal vector, multiplication `W->Sym2 W` is injective; tensoring Wp preserves injectivity. Thus a nonzero P6 covariant likewise has nonzero T7 image. Since `M_T(7)` is one-dimensional, these two images span the same line.

Both channel operations commute with multiplication by the scalar invariant f12. Their degree-eighteen images consequently satisfy

    p_T(f12 M_P(6)) = span(v_T) subset M_T(19).

In particular the determinant linear form vanishes on L_det. The PR876 map p_T is an isomorphism between two-dimensional spaces and v_T is nonzero. Therefore its determinant kernel has dimension one and is exactly L_det. This identifies the exceptional covariant line without selecting an actual-source parameter.

It remains to prove that the other channel does not vanish there. The exact sequence is

    0 -> Wp O(5) -> P O(6) -> Wp O(7) -> 0.

The invariant H0 dimensions are respectively zero, one, and one, from `Sym5=T`, `Sym6=V+P`, and `Sym7=Wp+T`. The left H1 vanishes because its ordinary line degree is positive. Taking invariants is exact for this finite group in characteristic zero. Hence the map from the middle invariant section space to the right invariant section space is an isomorphism, not merely a map between equal-dimensional spaces. It follows that the degree-six P-to-Wp channel is nonzero on every nonzero P6 covariant.

Multiplication by f12 commutes with this Euler channel as well. It cannot annihilate the resulting nonzero polynomial covariant. Consequently

    p_Wp(f12 M_P(6)) != 0.

The determinant kernel is therefore not the Wp-channel kernel. Each is one-dimensional inside the two-dimensional P18 multiplicity space, so their projectivizations are two distinct points of the parameter P1. Combining this with the exact PR876 definition above proves

    Omega = P1 minus exactly two distinct points.

The phrase “exceptional line” here refers to a one-dimensional covariant subspace before projectivization; the excluded object in P1 is its projective point. No dimension-only inference of nonzero maps or distinctness is used.

## 7. Exhaustion, uniqueness, and the unproved actual question

The canonical-tower theorem provides p in the exact open set Omega and the two standard quotient blocks while retaining u and v. Sections 4 and 5 above remove precisely these retained lifts. This establishes exhaustion of the inclusions under the stipulated hypotheses. PR876 supplies the converse abstract construction for every p, with the quotient, saturation, full-span and plateau conditions already checked.

Any G-equivariant constant ambient equivalence over the fixed base preserves the canonical tower and induces an automorphism of its high line quotient. The latter is a nonzero scalar. C10 contains A, V and P each once, so an equivariant isomorphism between corresponding C10 spaces acts by an independent nonzero scalar on each constituent after the fixed identifications. It cannot move the projective P coefficient line in `M_P(18)`. Hence equivalent inclusions have equal p. Conversely the same p gives the same normal form up to the allowed coefficient identifications and source reparametrization.

No quotient by arbitrary base changes has been introduced. No claim is made about other monad maps, about realizing any p in actual HM data, about an algebraic universal trivialization of the lifts, or about a moduli scheme. The remaining actual-realization/extension question is genuinely untouched. This boundary is mathematically essential and is correctly preserved throughout the submission.

## 8. Verification run and evidence boundary

The frozen `verify.py` completed successfully with the two printed PASS/scope lines. I inspected its source before execution. It uses only standard-library exact arithmetic in Q(sqrt(5)), the fixed nine-class character table, bounded symmetric-power recurrences, six-input byte authentication, and the fixed symbolic falling-factorial identity. It does not construct or evaluate an actual source instance.

In addition, fixed abstract Euler-character checks confirmed the original E cohomology at twists zero through three; the positive-preimage Euler character; both needed W(-9) cohomology characters; all three E0 Euler identities; the products V A and P A; absence of scalar invariants in degrees fourteen and sixteen; and the stated abstract quotient and twist-minus-one cohomologies of PR876. These were small representation identities, not parameter scans or instance-rank tests.

The checker is supporting evidence only. It does not prove generic jet surjectivity, regular lift factorization, the nonzero exceptional channels, or parameter uniqueness. Those assertions were reviewed geometrically in full above. No selected actual HM/source coefficients, parameter values, base points, derivative values, matrices, ranks, or large computations were used. No external writes or publication were performed.

**Final conclusion:** the frozen proof is sound for its stated classification problem, including the new assertion that the two exceptional parameter points are distinct. The submitted restrictions and remaining actual-HM compatibility problem are preserved.
