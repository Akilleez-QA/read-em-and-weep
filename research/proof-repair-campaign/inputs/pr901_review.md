# Independent review of the forced cubic-polar and scalar-row reduction

## Verdict and scope

**PASS, conditional on the stated original actual/source assumptions.** The frozen proof establishes the stated partial reduction for the three source127 tuples. I found no mathematical gap in the divisor calculation, the coherent-image argument, either universal quadratic injection, the V-only branch exclusion, the full-eight-dimensional-span exclusion, or the concluding actual cubic-polar flag.

The conclusion is deliberately limited. For a-c-c-f it forces a nonzero internal scalar row and the constant span V+D, while leaving its additional internal V component unrestricted. For a-c-f-f and a-b-c-f it retains both stated first-span alternatives. It does not exclude any of the three entire sources, remove the stable label G3.11.cce6e3ba4eeb, change a necessary-pair count, or establish realizability or the final generic-rank goal.

This review is independent of the archived earlier cubic-reduction package. I did not use that package as a dependency. I read the complete frozen proof, verifier, reproduction note, ACTUAL.md and STRICT-TOP.md, and inspected the exact source127 and stable-label catalog records. I ran the supplied bounded verifier and separately rederived the representation identities by the fixed W-McKay recurrence, rather than treating the verifier's PASS line as a geometric proof. No selected actual HM/source coefficient, parameter, point, derivative, matrix, instance rank, model, scan, or large computation was used. The proof and verifier were not edited.

## Frozen artifacts and immutable inputs

The reviewed artifacts have these SHA256 hashes:

- PROOF.md: `3989b8ae25e8f8f717f3f7ae3e0989480ad0b4dddd87f0cd648018b98b7a2c05`
- verify.py: `ac74b56e2f007c6a6ebdcccc0948daa30c559afb128d791eb3b9c290cea86620`
- REPRODUCE.md: `9c47621f8dead52a48df2e6257c5f2a9c2c54323e03ba4470fc1b47b1a941913`
- audit-inputs/manifest.json: `cdec01cc7a1790cfa272ff3ad390f4b1117bff2ba3482ee92254152676387e26`

All four source files were verified against their exact Git blob identities at commit `db51525015bb7c5e825833d550d08dedf6f6ea96` of Akilleez-QA/read-em-and-weep:

- ACTUAL.md: Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`; SHA256 `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`.
- STRICT-TOP.md: Git blob `d7506dae49b4be43230450c4132bd5db91f137ef`; SHA256 `53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08`.
- pairs.json: Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`; SHA256 `6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb`.
- frontier.json: Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`; SHA256 `a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad`.

The manifest supplies the original immutable source URLs. The source127 record has defect zero, A=[(-8,one),(2,one),(16,one)] and B=[(-18,one),(-4,one),(6,one)]. Its compatible_E_types contain all three tuples in the proof. The frontier record has id G3.11.cce6e3ba4eeb, profile 11, source_index 127, original_defect 0, the same A and B, and status not_excluded. These catalogs are necessary-data records, not assertions of actual realizations.

The actual/source premise used here is a hypothetical realization with the stated equivariant saturated E in H O, the indicated splitting, and its defect-zero external Gauss quotient. In particular the actual quotient is E^+/E=O(-6)+O(4)+O(18). Since E^+ is saturated, this quotient is saturated in Q, and its direct high line L=O(18) is saturated in Q. This does not imply that every subimage inside L is saturated.

The displayed ambient character can also be recovered from the original actual presentations: H=chi(E)+chi(Q)=M3 W-M4-M2=2A+2V+2P+2D. The original ACTUAL equivariant splitting argument and its center-parity convention justify applying equivariant Birkhoff-Grothendieck splitting to the small kernels and quotients in this proof. The proof uses the strict-top principle only in its legitimate geometric form: a negative saturated subbundle cannot become horizontal in a constant bundle.

## 1. Independent bounded representation check

I used the fixed tensor-by-W graph with edges

    1-W, W-A, A-S, S-D, D-T, T-P, P-Wp, T-V,

together with Sym^(n+1) W=W Sym^n W-Sym^(n-1) W. This is a computation in the abstract representation ring only. The recurrence through n=19 gives:

    Sym4 W = D,
    Sym5 W = T,
    Sym6 W = V+P,
    Sym7 W = T+Wp,
    Sym12 W = 1+A+D+P,
    Sym14 W = A+D+V+P,
    Sym18 W = A+D+V+2P,
    Sym19 W = W+S+2T+Wp.

The only positive invariant degree at most fourteen is twelve, with multiplicity one. The same recurrence gives

    Wp W=P,
    Wp Sym2 W=T,
    Wp Sym3 W=D+V,
    V W=T,
    V Sym2 W=D+P,
    D W=S+T.

These confirm the high-factor multiplicities, the missing lower channels, the two universal quadratic Hom spaces, the degree-fourteen obstruction, and the coefficient identities used for the cubic flag. The supplied verifier also completed successfully, including all four Git blob tests and the fixed single-V H1 budget. Its scope is arithmetic and immutable-source checking; the geometric deductions are audited below.

## 2. The high map and its nonsaturated image

The external negative row of R=Wp O(-3) vanishes by degree. Its O(2) row vanishes because Wp is absent from Sym5 W. If the high row vanished as well, its full second fundamental form would land in (E/R)(-2), whose maximum degree is -4. There is no map from O(-3) to this target. Since R is a direct summand of saturated E, it is saturated in the ambient constant bundle. It would therefore be a negative horizontal saturated subbundle, a contradiction.

Both relevant Wp covariant spaces, at degrees seven and nineteen, are one-dimensional. Multiplication by the nonzero invariant f12 injects the former into the latter and hence is an isomorphism. The residual degree-seven row has no common zero divisor: such a divisor would be invariant, nonempty and of degree at most seven. Consequently the actual high row has exactly divisor twelve, raw image O(4), and kernel O(-10).

The proof correctly keeps separate:

    raw high image O(4) in O(16) in Q(-2),
    and its saturation O(16).

Equivalently after twisting, it keeps O(6) mapped into L=O(18) by f12. It never invokes a saturated-external-image argument for this raw image. The degree-twelve divisor is reduced because any repetition would make its invariant reduced support nonempty of degree less than twelve.

## 3. Internal channels, raw polars, and saturation

The internal derivative of the high kernel K0=O(-10) is not the restriction of a nonexistent map from the whole R to a lower splitting block. The proof correctly computes it separately. Its complete possible rows are:

    a-c-f-f: scalar rows to 2O(-10);
    a-c-c-f: V(-4) and scalar O(-10);
    a-b-c-f: T(-5) and scalar O(-10).

The D(-4) and V(-6) targets contribute no Hom. Each nonzero V or T row is a basepoint-free map from a line, since its potential common divisor has degree at most six or five. A nonzero scalar row is an isomorphism onto a constant scalar multiplicity line. Thus J is either zero or a saturated O(-10), including when several allowed components are simultaneously nonzero.

For the exact raw derivative image I, projection to the external quotient gives an exact sequence with quotient the raw O(4), not its saturation. Hence

    0 -> J -> I -> O(4) -> 0,
    0 -> R -> Mraw -> I(2) -> 0.

When J=0, Mraw has rank three and degree zero. A locally free subsheaf of a trivial bundle has no positive splitting degree, so it must be a constant three-space. The Euler character is -Wp W+Sym6 W=V. Its constant inclusion is saturated, while its image in Q is still the nonsaturated O(6) in L.

When J is nonzero, Mraw has rank four and degree -8. The first polar of the cubic inclusion is the image of Wp W O(-2)=P O(-2); Euler's identity places the value inside this polar image. It surjects onto Mraw. Equal rank and degree make that map an isomorphism. Any subsequent saturation defect in the trivial ambient bundle would have degree at most eight, whereas a nonzero invariant defect has degree at least twelve. Thus the raw polar is already saturated.

The coefficient span is a quotient of the multiplicity-free V+D. A saturated rank-four degree-minus-eight bundle cannot fill a constant space of dimension four, and a smaller space cannot contain it. This leaves exactly D or V+D. Finally N=E intersect M has N/R=O(-8), with M/N=O(6) and the same f12 external embedding. All these claims are at the level of coherent sheaves, not just generic ranks.

## 4. Coherent projection excludes the constant-V a-c-c-f branch

In this branch C=V O has E intersect C=R, so the coherent projected image of E is isomorphic to E/R. It need not be saturated. The top B=V O(-2) has no negative or middle external row. Its high degree-eighteen V row is divisible by f12, because both the degree-six and degree-eighteen V covariant spaces have dimension one. This also includes the zero row.

Thus the derivative of B lands in the twist of the actual coherent inverse image E+C of the raw O(6) image. This establishes the necessary regularity after projection without dividing by f12. The projected B is isomorphic to B, and modulo it the derivative lands in

    (E/(R+B))(-2)=D(-4)+2V(-6)+O(-10).

Every such map from B vanishes by degree. The projected coherent lattice B is therefore preserved by the trivial connection. In characteristic zero its generic subspace is constant. A proper lattice in that fixed constant subspace would have a positive determinant zero divisor, whose logarithmic derivative creates a pole in the induced determinant connection. Preservation forbids that pole. Hence the lattice must be the full constant bundle, contradicting degree -6.

This is a valid coherent divisibility argument. It does not incorrectly extend the conclusion to a-c-f-f, whose high D row has no analogous degree-six factor space, or to a-b-c-f, which has no such top V block.

## 5. The two universal saturated quadratic injections

For P, the nonzero P O->O(6) covariant is onto because its common divisor would have invariant degree at most six. Its kernel K has rank three, degree -6, H0(K)=0 and H1(K)=V. Every equivariant atom U(-j) with j at least two contributes the genuine U Sym^(j-2) W to that H1 budget and satisfies (j-1)dim U at most three. The only admissible atom is V(-2): parity excludes j=3 within the budget, and the possible scalar at j=4 contributes A instead of V. Atoms of degree -1 contribute no H1 but cannot occur once V(-2) has filled the rank. Thus K=V(-2).

For D, a nonzero Wp(-3)->D O cannot have generic rank one. Its coherent rank-one image would be an equivariant O(e), e at most zero, requiring Wp in Sym^(e+3) W with degree at most three. That never occurs. Its rank-two degeneracy divisor has degree at most six and is invariant, so it is empty. The map is a saturated injection. Dualizing gives a surjection D O->Wp O(3), whose kernel has the same rank, degree, H0 and H1 as above, and hence is V(-2).

Both relevant quadratic Hom spaces have dimension one. Therefore every nonzero V(-2)->P O or V(-2)->D O is one of these saturated injections. No evaluation of a chosen source map is involved.

## 6. The V-only internal branch forces the contradiction

If the scalar internal row vanishes in a-c-c-f, the V(-4) row is nonzero. Projection by the constant span C kills the derivatives of R, so it kills a nonzero line in the projected top block B(-2). But every nonzero irreducible component of the constant projection of B is a V(-2)->P or D map. By the preceding universal lemma each is injective. Therefore the projection of B must vanish altogether, and B lies in C.

The case C=D is impossible immediately: B+R is a saturated rank-five direct summand of E, hence saturated in the ambient bundle. Its containment in a constant five-space would make it that five-space, contrary to degree -12. Thus C=V+D. The V component of B vanishes by the coefficient identity V Sym2 W=P+D, so B lies in the D summand and D/B=Wp O(3).

The proof of B^+=D is valid also at the lattice level. Its derivative into Wp O(1) is nonzero and cannot have generic rank one, because a rank-one image O(e), e at most one, would require V in Sym^(e+2) W of degree at most three. Its generic rank is therefore two. The raw polar is a quotient of T O(-1), so its splitting degrees are at least -1 and its degree is at least -5. As a full-rank subsheaf of constant D its potential invariant defect is at most five; hence no defect exists.

The nonzero projection R->V O is similarly a saturated rank-two inclusion with quotient O(6), and its first span is generically V. Therefore D+M has generic span C. Both are inside saturated E^+, giving the actual containment C in E^+.

Projection by D yields the exact quotient extension

    0 -> Wp O(3) -> C/(B+R) -> O(6) -> 0.

There are no maps from either end to O(4) or O(-6), including the potentially delicate Hom(Wp O(3),O(4)), which is zero because Wp is absent from W. Thus the entire quotient maps only to L. Its restriction to D is nonzero, since a constant D inside E is impossible.

For that D-valued degree-eighteen row, independence of its five coefficient sections bounds any common divisor by fourteen. The invariant possibilities in that range leave only twelve. Dividing f12 would require D in Sym6 W, which is absent. Hence the D row, and therefore C->L, is onto. This is a genuine basepoint-free assertion, not just generic surjectivity.

It follows that X=E intersect C has rank seven and degree -18. Its quotient by B+R is a rank-two degree-minus-six bundle injecting into

    D(-2)+2V(-4)+O(-8).

The quotient is center-even and admits equivariant splitting. All its degrees are at most -2. At degree -2 its coefficient representation has dimension at most two and even parity, so it consists only of trivial coefficients, which cannot map to D at equal degree. At degree -3 the only possible irreducible coefficients are W and Wp; neither maps to D(-2), since D W=S+T, or to the lower-degree targets. Thus all its degrees are at most -4, forcing degree at most -8. This contradicts -6 and excludes exactly the V-only internal row.

## 7. The scalar negative row excludes the five-dimensional span

Only the original O(-8) source summand can supply the negative external O(-8) row. That row is nonzero in the actual rank-three quotient and hence is a scalar isomorphism. Once the internal scalar row is nonzero, N/R=O(-8) has nonzero scalar projection to that summand. Its induced negative derivative row is consequently nonzero as well. The possible additional V component does not affect this conclusion.

If C=D had dimension five, M=P(-2) would be saturated in C with quotient O(8). The derivative of M kills R because R^+=M. Its restriction to N factors through

    O(-8)=N/R -> (C/M)(-2)=O(6).

This is an equivariant scalar degree-fourteen map. Since there is no invariant of degree fourteen, it vanishes. Derivatives of N would then stay in M, whose image in Q has only the high O(6) component. That contradicts the nonzero negative row just established. This argument correctly uses the raw image M/N=O(6) rather than silently replacing it by L.

Therefore every surviving a-c-c-f realization must have C=V+D, M=P(-2), and nonzero internal scalar row, with its additional V row still allowed.

## 8. Independent derivation of the final actual cubic flag

The full coefficient map Wp Sym3 W->C is an isomorphism. Put U=Wp and let ell=O(-1) be the tautological line in W O. The universal cubic filtration inside U Sym3 W O is

    R=U ell^3,
    M=U ell^2 W,
    F2=U ell Sym2 W,
    C=U Sym3 W O.

These are actual subbundles with locally free successive quotients. The Euler sequences, or the quotient W O/ell=O(1), give

    M/R=U O(-1),
    F2/M=U O(1),
    C/F2=U O(3).

The universal second fundamental form of M kills exactly R and induces the nonzero characteristic-zero scalar isomorphism

    M/R -> (F2/M)(-2).

Also F2=U Sym2 W O(-1)=T O(-1), so F2=M^+ and M^-=R. This proves the stated identities without choosing a source point or evaluating any actual coefficients or derivatives.

Since N/R=O(-8) is saturated in M/R, its image under this isomorphism is saturated as well. After twisting by two, the preimage of that image inside F2 is a saturated rank-five bundle Y with

    Y/M=O(-6), deg Y=-14, F2/Y=O(8).

This preimage is exactly N^+: differentiating R already generates the raw M, and differentiating N modulo M gives precisely the indicated line. Thus no extra saturation or unspecified defect is hidden in Y. Saturation in F2 also gives saturation in the ambient constant bundle.

Finally Y lies in E^+ because N lies in E. The negative projection vanishes on M, and the nonzero scalar negative row on N/R induces a nonzero map Y/M=O(-6) to the negative O(-6) component of E^+/E. Such a map is a scalar isomorphism. The proof does not need, and does not claim, an identification of the entire E^+ intersect C.

## Final binding and assessment

After the initial audit, the author corrected the single Section 6 cross-reference to name E^+/E=O(-6)+O(4)+L explicitly. Reversing exactly that one text replacement reproduces the initially reviewed proof's SHA256 `7bff230d3d3431e2831994187a82e30a01754e800b24a421439cdd8785d5a5ff`. I verified there were no other proof-byte changes, the verifier remained unchanged, and the verifier passed again. This review binds the final proof hash listed above.

The supplied verifier's success message describes geometric topics whose numerical ingredients it checks; those geometric conclusions depend on the proof and the reasoning audited above, not on the executable alone. With that normal distinction and the stated original actual/source premises, the consolidated partial reduction is sound and ready to be used only at its expressly limited scope.
