# A checked order-two realization on the completed plane object

Date: 2026-10-11. This is an explicit finite-normal-order construction, through h² with h³=0. It preserves the frozen first-normal and sign-dictionary packages. It does not construct an ancestor or algebraic carrier, compute a reflexive hull or defect, or infer an unverified higher jet.

## Result

The supplied second-middle tensors, with the explicit negative-vector logarithm dictionary and the previously constructed plane completion, admit regular second-order section corrections for the entire polynomial family (a,b,c,d,lambda). The section retains the prescribed positive pairing +t0 h modulo h³.

The verifier checks the actual middle tensors against newly computed raw quadratic BCH terms, constructs every section correction, and tests all mixed base equations. It uses neither supplied N2 ranks/minors nor a stored assertion of section existence. There are 1,685 successful order-two checks, a targeted mutated-input rejection, and 405 exported nonzero Laurent terms in the second-section corrections. The first-order support independently reruns its 746 checks as well.

## 1. Inputs, provenance and chosen gauges

Pinned source commit: `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`.

The actual second-middle tensors are present at
https://github.com/Akilleez-QA/read-em-and-weep/blob/6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb/research/carrier/formal-five-parameter-chart/audit_original_cover/certificate.json

under each of the fifteen `coefficients` entries, in

    original_cover_primitive.finite_W_primitive,
    original_cover_primitive.infinity_W_primitive,
    original_cover_primitive.mixed_W_primitive.

The certificate's SHA-256 is
`c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4`,
verified against its pinned SHA256SUMS. The bundled first_jet.json is pinned by
`2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10`.

The source's exact primitive contract is documented at
https://github.com/Akilleez-QA/read-em-and-weep/blob/6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb/research/carrier/formal-five-parameter-chart/audit_original_cover/README.md

The selected gauge is explicit:

1. The plane object and original-coordinate-cover q frames are those constructed in the frozen first-normal package.
2. The first middle logarithm η is the literal frozen origin plus a,b,c,d directions.
3. The second middle logarithm κ is the coefficientwise exported W primitive above, plus the independent mixed cochain lambda·z⁻¹E0².
4. First and second section representatives use the same ordered X,Y,W monomial Čech homotopy, with the first coordinate having nonnegative exponent as pivot and the ordered-simplex sign.
5. The vector logarithm is −h Aη−h²Aκ. All comparisons use j→i vector transitions and the verified opposite-BCH dictionary.

No second-order gauge is selected by a parameter-dependent inverse or by comparing to a stored section answer. The coefficientwise section answers are generated here.

`first_order_support.py` is an unchanged copy of the first-normal checker, running against its own bundled pinned input in this directory. It imports no source producer code. Running it does not modify the frozen earlier package.

## 2. Exact middle equations

For η=Σ cij ui uj, use

    Aη(x)=Σ cij[ui Ω(uj,x)+uj Ω(ui,x)],

with diagonal terms counted twice. The universal sign calculation gives the required second-logarithm equations

    δκF = ½{ηF,01,ηF,12},
    δκI = ½{ηI,01,ηI,12},
    TκI−κF−δκH = ½({h_i,TηI,ij}−{ηF,ij,h_j})

in Sym²(G)L⁻¹I². In each equation the verifier directly rebuilds the right-hand side from the frozen first tensors. It computes every constant, linear and quadratic parameter coefficient by its ordered pairs, without sampling parameter values.

The difference between the two sides is checked to be divisible by the actual relation r in Sym²(B). The quotient is reconstructed and all tensor entries are checked, so this is not inferred from a D2 preimage or rank flag. Infinity-to-finite tensor transport is z⁻⁴Sym²(TB), including its triangular term.

Every supplied κ coefficient is separately checked for order-two plane degree, character, allowed plane poles and allowed finite/infinity base powers. The independent lambda term is a closed mixed order-two cochain, also checked directly.

Since A is Lie-homomorphic and the negative dictionary reverses BCH, these tensor identities imply the actual exponential vector transitions satisfy their cocycles modulo h³. Every Aη and Aκ is infinitesimally symplectic and fixes P; hence the truncated exponentials preserve the alternating form and distinguished isotropic line to this order. Invertibility follows from their unchanged invertible constant terms.

## 3. The second-section equation, including action on q

Write the local section as

    ṽi=v+h ξi+h² σi,     v=E0,
    ξi=t0 qi+si.

Here si is the already exported first-order section correction; t0 is z on the finite base chart and 1 on the infinity chart. For parameter directions the corresponding first coefficient has no q term.

The vector transition is

    g̃ij=[1−hAηij+h²(½Aηij²−Aκij)] gij modulo h³.

The first-order equation is gij ξj=ξi+Aηij v. Expansion therefore gives

    gij σj−σi
      = Aκij v+Aηij ξi+½Aηij²v.                (*)

The checker evaluates all three terms. In particular it does not drop Aη(t0q). On coordinate patch i the full completion has

    Ω(Bj,qi)=(1, a0(λi)_0, a0(λi)_1, a0(λi)_2),

where a0=X³+Y³ and λi is the previously constructed covector with λi(r_E)=1. This full four-entry functional is used in every action evaluation. Omitting it would test the wrong section equation.

The analogous mixed base equation is

    TB σI,i−σF,i
      = AκH,i v+AηH,i ξF,i+½AηH,i²v.

It is checked independently on all three original plane opens for every parameter coefficient.

All terms on the right side of (*) lie in G. Thus σ is sought in G I², with no D component. Such a correction preserves β(ṽ)=+t0h without introducing an h² pairing coefficient.

## 4. Explicit construction, not a dimension argument

For each of the fifteen parameter monomials, let y be the B-valued one-cochain obtained from the right side of (*). The verifier performs these exact operations on each base chart:

1. Compute δy and reconstruct its scalar relation quotient f by checking δy=r f in every B component.
2. Check the all-negative plane projection Πf is literally zero.
3. Set ζ=Kf and verify δζ=f.
4. Set σ=K(y−rζ), and verify δσ=y−rζ entry by entry.
5. Check the mixed base equation modulo r, separately from the two plane computations.

No invocation of the abstract H¹(GI²)=0 result or supplied N2 matrix is needed for these explicit primitives. The zero top projection and each regular primitive are actually checked.

Every exported second-section coefficient has BI² plane degrees

    (−5,−2,−6,−6)

in the ordered P,E0,E1,E2 slots. The finite coefficient character is 2+d_j, and the infinity character is d_j−4. All base powers and allowed plane denominators are tested. Hence these are regular homogeneous cochains on the stated original cover, not unrestricted rational solutions.

The section representatives are in `SECOND_NORMAL_SECTION_CORRECTIONS.json`. Nonzero term counts, finite/infinity, are

- constant: 40/72;
- a: 26/66; b: 25/59;
- c: 3/0; d: 2/0;
- a²: 17/40; ab: 9/24; b²: 12/10;
- ac,ad,bc,bd,c²,cd,d²: 0/0.

The total is 405. Vanishing section coefficients do not imply the corresponding middle coefficients or parameter directions vanish.

The free lambda second-middle class is mixed z⁻¹E0². Its action on v=E0 is identically zero, and lambda does not occur in the first-order terms. Its order-two section correction is therefore exactly zero. This says nothing about lambda-dependent terms at order three.

## 5. Transfer to the earlier explicit quotient frames

The first-normal package supplies actual, regular common-refinement isometries to the earlier radical-patch quotient frames. They are identity on G and independent of h. Conjugation by those isometries carries Aη and Aκ to the same Hamiltonian tensors in the earlier frames, while fixing P and E0.

The first coefficient ξ transfers with the explicit q-frame shift already checked there. The new coefficient σ lies in G, so it transfers simply by the earlier quotient projection Ri of its displayed B representative. This realizes the second jet on the previously constructed plane completion, rather than merely on an abstractly unrelated model. No new first- or second-order comparison gauge is silently assumed.

## 6. Sensitive negative control

The normal data pass before mutation. The checker then adds 1 to the **actual origin finite01 second-middle primitive** coefficient of

    X⁻¹Y⁻¹W² E0².

It reruns the finite triangle-defect calculation through the same relation-quotient gate. The resulting nonzero residual is exactly that monomial in the E0² slot, so the gate rejects it as required. The checker verifies the residual itself; an unrelated exception is not accepted as a successful control. No source file is changed.

## 7. Reproduction and scope

Run `python check_second_normal_comparison.py`. Only the Python standard library is needed for this package; arithmetic uses exact Fraction coefficients. Exception-based checks stay active under Python−O.

This constructs a locally free symplectic bundle on the second normal neighborhood of the zero section in Tot(O(0,1)), its fixed P inclusion and section, over the polynomial parameter ring Q[a,b,c,d,lambda], with β(ṽ)=+t0h modulo h³. All operations use rational constants and geometric-coordinate inversions, without parameter division.

It does not classify all second jets independently of the prior parameter theorem. It does not identify an ancestor restriction or unprovided source frame, algebraize the formal family, construct a carrier/reflexive hull, prove base change or compute a defect. The certificate's partial lambda-dependent order-three data are not used and are not a complete third jet.

Independent review checked the section expansion, the action on q, the selected literal-primitive gauge and parameter summation, and separately audited all 405 exported terms for degrees, characters and regularity. That review was derivation/code inspection and an output-grade audit, not a separate full equation rerun.

Normal and Python−O runs completed with byte-identical standard output and all four generated JSON artifacts. The earlier first-normal and sign-dictionary manifests were reverified unchanged after this run.
