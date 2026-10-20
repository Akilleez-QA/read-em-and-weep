# Independent audit: weighted Koszul obstruction sequence

## Scope convention

The assertions below concern coefficient geometry, finite-group actions and the stated coherent cohomology. References to unevaluated coordinates mean that this argument does not evaluate them; they are not a claim about the latest status of every other argument. The raw-source regularity, coefficient/character identification and raw-to-canonical class comparison are separate hypotheses wherever a source application is discussed. No first-order lifting theorem, higher-order obstruction vanishing, formal integrability or algebraicity follows merely from these coefficient statements.

## Verdict

The sheaf and cohomology argument is correct at the imported regular-source, finite-cover, and HM-cohomology scope. The triple-diagonal ideal imposes no restriction on the full ten-dimensional weighted sign target. The exact 20 → 30 → 10 sequence and the regular kernel/primitive criterion are valid. They supply no source-specific vanishing or nonvanishing.

The mathematical review incorporates two presentation qualifications: retain determinant lines when asserting GL2 naturality, and restrict the fixed-weight identification to the retained H-character slice (dimension 30), rather than the full slice (dimension 32).

## Independent checks

1. Actual coefficient. The [committed source-character proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md) §2 verifies intrinsic all-four deck character of the normalized mixed source, including cancellation of scalar root-frame signs. Its §4 identifies the full odd pushforward line. For rho:C^4→Z, the full odd factor in rho_*O is A^-2. End(N⊗pi*HM)=pi*End(HM), so its tracefree character coefficient is E=q*B0⊗A^-2. Permuting odd scalar factors is ungraded and introduces no sign. This establishes the claimed actual coefficient, subject to imported regularity; it is not inferred from a supposed S4 action on the fixed deformation ambient.

2. Diagonal restriction. Every triple-diagonal component has a pointwise-fixing transposition acting trivially on E A, because this coefficient descends from Y. A sign section therefore vanishes on each component. Reducedness is essential: componentwise vanishing then forces the section itself to vanish, even at quadruple collisions. Thus (q_*(EA|D))_sign=0 as a sheaf, not merely generically. Exact finite pushforward and exact character projection imply (q_*I_D EA)_sign=(q_*EA)_sign and the cohomology isomorphism in every degree.

3. Koszul endpoints. Tensoring the audited rank-two weight resolution by E and taking sign gives first term B0(-3), because the Koszul determinant has permutation sign and q_*O invariants equal O. The last term is B0(-4): equivalently the Vandermonde generates the sign line of q_*O in degree three, so (q_*EA)_sign=B0(-1)⊗O(-3). Finite duality gives the same answer without inverting the discriminant. Both arguments work at branch points.

4. Middle multiplicity. Write S for the abstract Specht (2,2) representation and M_S=Hom_S4(S,q_*O_Z). The order-eight partition stabilizer H has Ind_H^S4(1)=1⊕S. Hence (q_*O_Z)^H=O⊕M_S. The left side is the function bundle of the unordered-pair partition quotient, and its tracefree part is the previously audited G of type O(-1)⊕O(-2). Therefore M_S has exactly that type. Since S is self-dual and sign-self-twisted, (U⊗q_*E)_sign has underlying bundle B0(-3)⊕B0(-4), so its H2 dimension is 20+10=30. This independently checks the manuscript's equivalent 32−2 argument, without making the retained paired space an S4 representation.

5. Exactness on H2. Serre duality and B0 self-duality give H3(B0(-3))=H1(B0(-2))*=0. The latter is an admitted Ext input, also compatible with the publicly pinned HM cohomology dependencies in DEPENDENCIES.md. Consequently the last H2 arrow is onto. Exactness and dimensions 20,30,10 make the first H2 arrow injective. No unstated H1(-4) vanishing is needed. Alternatively, the unnumbered proposition on printed p. 218 of W. Decker and F.-O. Schreyer, *Pullbacks of the Horrocks-Mumford bundle*, J. reine angew. Math. 382 (1987), 215–220, gives H¹(End(F)(k))=0 for k≤−2; the scalar trace splitting gives the same vanishing for B0. [Public page](https://gdz.sub.uni-goettingen.de/id/PPN243919689_0382?tify=%7B%22pages%22%3A%5B222%5D%2C%22view%22%3A%22info%22%7D). This classical input is optional because the split coefficient proof below already makes every connecting map zero.

6. Kernel criterion. For a closed target cochain t, cohomological surjectivity provides a closed middle representative mapping to t modulo a boundary. Surjectivity on affine-overlap sections lifts that boundary and corrects the representative to a closed lift r with mu(r)=t exactly. If [r]=alpha[a], write r=alpha(a)+delta b to obtain t=delta(mu b). Conversely, lift a primitive h of t to b; r−delta b then lies uniquely in alpha's image, and its preimage is closed by injectivity. This proves the stated equivalence and avoids assuming an arbitrary two-generator factorization has closed coefficients.

7. Weighted trace comparison. Multiplication by the genuine weight and sign projection is the actual middle-to-target map. The source transfer/sign-to-constant comparison remains the imported premise from comment 6274541018. On the retained H-sign slice, a fixed nonzero pairing weight yields a nonzero one-dimensional representation contraction and identifies the quotient with the existing weighted duality trace, up to the specified projector normalization. No extra division by six is introduced into duality trace itself. That normalization affects neither the kernel nor the conclusion about ideal membership.

## Determinant-line qualification

All bare O(k) identities above are S4-equivariant identities after fixing the binary determinant lines. They should not be advertised as canonical GL2 identities with those lines suppressed. With the convention D=det(V*), U_weight=D²⊗S, the relevant multiplicity bundle is D²O(-1)⊕D⁴O(-2), and the sign line of q_*O is D⁶O(-3). Thus the corresponding endpoints retain D⁴⊗H2(B0(-3)) and D⁶⊗H2(B0(-4)). Also omega_Z=D⁴⊗A^-2⊗sign. No GL2 action on HM is required; tensoring O_Y-linear coefficient maps by B0 is sufficient. The elliptic-cover coefficient can be handled with its chosen actual S4 linearization without asserting a GL2 symmetry of that cover.

## Boundary

This review proves sheaf/representation consequences. It does not evaluate a source or prove a regular primitive for the actual weighted class. The source regularity and class-transfer premises remain imported and explicitly bounded.

## Revised version: stronger splitting and alternant check

The revised §4 is correct and improves the proof: omit B0 from the equivariant Koszul construction to obtain the exact bundle sequence 0→O(-3)→M0→O(-4)→0. A sheaf extension of two line bundles is locally free, and its extension class lies in H1(O(1))=0. It therefore splits globally. Projection formula identifies the B0 sequence with its tensor product by B0. Consequently all cohomology connecting homomorphisms vanish, and the 20→30→10 sequence does not depend on the HM Ext1 input. The latter argument remains only an independent check. A chosen global splitting also directly provides the closed regular lift required in §5.

The revised §6 is correct. The six brackets define distinct prime pair-diagonal Cartier divisors on smooth Z. A sign section of the descended coefficient vanishes along each, so it lies in the product of their divisor ideals. This can be checked componentwise in a local frame, or by divisor valuations on the normal variety. Dividing out the product defines a regular section of q*B0⊗A^-4, invariant under S4, globally; no meromorphic inversion is needed. Each bracket belongs to the small-diagonal ideal J, yielding membership in J^6 EA. This concerns the fully sign-projected cochain in a quotient-adapted cover, not an arbitrary unprojected weighted remainder factorization. The order-six bound is universal and cannot imply that its descended ten-dimensional class is zero. Determinant lines for the bracket product are subject to the same stated convention as above.

## Further corollary: the cube of the weight ideal

The added cube-of-ideal corollary is valid. Each weight difference is a section of I_D⊗A. The three explicit differences are nonzero scalar multiples of the three complementary products of pair brackets. Their product therefore contains each of the six brackets exactly once, so

(σ1−σ2)(σ1−σ3)(σ2−σ3)=c·v, with c≠0.

This is a homogeneous identity in H0(A³), placing v in H0(I_D³⊗A³). Every sign section of EA is v times a regular invariant section of EA^-3. Consequently every such section belongs to I_D³ EA, and hence to I_D^r EA for r=1,2,3. Since these are equivariant subsheaves of EA, their sign pushforwards coincide with the sign pushforward of EA. Finite pushforward and exact character projection give the stated cohomology isomorphisms in every degree for these three powers.

The exponent three is sharp as a universal local ideal-membership assertion. At a generic point of Δ123 away from the fourth root, put u=x1−x3 and w=x2−x3. Here I_D=(u,w), while v is a unit times u w(u−w). Its degree-three initial form is nonzero, so v is in I_D³ but not I_D⁴. A nonvanishing invariant coefficient from a local descended bundle frame gives a sign section of EA with precisely this order. Thus universal fourth-power membership fails. This local sharpness neither evaluates the actual source nor establishes any failure of a cohomology isomorphism for the fourth ideal power; no such claim is made.

## Relation to the committed proof

The full alternant and cube-of-ideal argument reviewed in the last two sections is already committed in [PR158](https://github.com/Akilleez-QA/read-em-and-weep/blob/aab61d34a84c9b8b5a908606a7beb7212d45fe7c/research/conductor-normalization/ideal-power-contractions/WEIGHT-GEOMETRY-INPUTS.md). PROOF.md cites that argument instead of copying its text. The review is retained in full mathematical scope; its source-character and comparison premises remain conditional. It certifies neither an actual raw equality nor an I_D⁷E/I_D¹²E representative.
