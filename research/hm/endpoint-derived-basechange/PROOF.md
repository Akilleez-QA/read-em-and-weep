# The order-six jump lives in relative degree three

## Theorem and precise setting

Work over C and retain the marked coefficient lines of PR437 and PR439.
Let T=Spec C[s,(1+alpha s)^(-1)] and g(s) be the algebraic translated-root curve of PR443. Thus alpha is nonzero, g(0)=1, u_s=u_0+(2s+alpha s^2)ell^2, and v_s=v_0((1+sD)x). Fix b in T(C), put A=O_{T,b}, z=s-b, and let K be the fraction field of this discrete valuation ring. Completion A=C[[z]] is also allowed. All statements below use this one specified family, not arbitrary deformations.

Let I_Delta be the ordinary ideal of the reduced union of the four triple diagonals, as in PR437. Write p:Z_A=(P^1)^4_A -> Spec A, q_g=g(s)q_0, and

    E_g=q_g^*B tensor (q_g^*O(1))^(-2),  B=End_0(F),
    C=I_Delta^6 E_g,
    H^i_A=(R^i p_* C)_chi,
    Q_A=coker[(u_s,v_s):(H^1(B(4)) direct sum H^1(B(3))) tensor A
                              -> H^1(B(6)) tensor A].

The cohomology in the definition of Q_A is on the fixed complex P^4. Let e be the multiplicity of t=2b+alpha b^2 in the monic quadratic f of PR442/443, so 0<=e<=2. The known bounds are z^e Q_A=0 and length Q_A<=15e. The theorem is:

1. H^2_A=0, even when the special-fiber H^2 is nonzero.
2. There is a canonical identification, with the fixed weight lines understood,

       tors_A H^3_A = Ext^1_A(Q_A,A) direct sum Ext^1_A(Q_A,A).

   Therefore z^e tors H^3_A=0 and length(tors H^3_A)=2 length Q_A<=30e<=60. This identifies the exact torsion, not all of H^3_A; a finite free quotient can remain.
3. For A_n=A/(z^n), n>=1, derived base change for the A-flat sheaf followed by the universal coefficient sequence gives canonically

       H^2(Z_{A_n},C_{A_n})_chi = Tor_1^A(H^3_A,A_n).

   With the parameter z fixed, this is the z^n-annihilated submodule of tors H^3_A. In particular, if

       Q_A = direct sum_j A/(z^{a_j}),  1<=a_j<=e<=2,

   then the C-length of this fat-fiber H^2 is 2 sum_j min(n,a_j). Its length stabilizes for n>=2, at 2 length Q_A. For n>=e it is isomorphic to tors H^3_A via the displayed parameter-dependent Tor description.
4. At b=0, the geometric closed fiber is the original fixed coefficient geometry. The familiar dual identity H^2(C_0)^vee=Q_0 direct sum Q_0 remains intact. It is not obtained by tensoring H^2_A, which is zero: the entire base-change defect is supplied by degree-three torsion.

This resolves the relative-cohomology identification deliberately left open in PR442/443. It does not evaluate Q_0, prove its vanishing, or establish actual source membership, the six pure conditions, a module lift, or algebraicity of a quantization/module. Algebraicity here is only that of the coefficient family already constructed in PR443.

## 1. Flatness and relative coefficient resolution

The ideal I_Delta^6 on Z is constant over the base field C, hence its scalar extension is A-flat. Tensoring by the locally free E_g preserves A-flatness. Thus C is A-flat. This is a statement about the sheaf, not flatness of its higher direct images or Q_A.

The target automorphism g(s) and its specified GL lift transport the full filtered identity of PR437 over A. Indeed all operations there are polynomial ideal identities, finite pushforward, line-bundle twists, and the exact character projector in characteristic zero. Equivalently, apply that identity with the arbitrary coefficient g(s)^*B on the fixed target and then transport by g(s). The fixed B on the moving target gives the sheaf

    G = B_A(-3)K_5(u_s,v_s) direct sum B_A(-4)K_4(u_s,v_s)
                                  direct sum B_A(-5)K_3(u_s,v_s)

on Y_A=P^4_A, and H^i_A=R^i pi_*G, for pi:Y_A -> Spec A. No projective invariance of B is assumed.

The pair (u_s,v_s) is the image of the original regular sequence under an automorphism over A. The three adjacent-monomial resolutions of PR439 therefore remain exact over A, including at all collision strata. Their generator and syzygy bundles, denoted F_0 and F_1 for each summand, are constant sums of twists of B_A. Explicitly:

    B(-5)K_3: F_1=B(-12), F_0=B(-8) direct sum B(-9);
    B(-4)K_4: F_1=B(-11) direct sum B(-12),
               F_0=B(-8) direct sum B(-9) direct sum B(-10);
    B(-3)K_5: F_1=B(-12) direct sum B(-11),
               F_0=B(-9) direct sum B(-8) direct sum B(-9).

The matrices, before twisting, have columns respectively

    (u_s^2,-v_s),
    (v_s,-u_s,0), (0,v_s,-u_s),
    (v_s,-u_s^2,0), (0,v_s,-u_s).

Every R^i pi_*F_j is the fixed complex vector space H^i(F_j|_C) tensor A, hence is finite free and commutes with every A-algebra base change. This follows directly from a finite affine Cech cover over C and flatness of all C-modules. It does not assert such commutation for G.

## 2. The relevant long exact sequence

PR167 gives H^2(B(t))=0 for t>=2 and H^1(B(t))=0 for t>=7. Trace identifies B^vee with B. Serre duality on P^4 then shows R^2 pi_*F_0=R^2 pi_*F_1=0 for all three resolutions above. For example their dual positive twists are at least three. Put

    L:R^3 pi_*F_1 -> R^3 pi_*F_0,
    J:R^4 pi_*F_1 -> R^4 pi_*F_0.

The long exact sequence of 0->F_1->F_0->G_j->0 gives

    R^2 pi_*G_j=ker L,
    0 -> coker L -> R^3 pi_*G_j -> ker J -> 0.       (1)

The module ker J is a submodule of a finite free A-module, so it is finite free over the DVR A. In particular (1) splits as A-modules, although no canonical splitting is asserted. More intrinsically the injection in (1) canonically identifies tors(coker L) with tors(R^3 pi_*G_j). No unknown H^4 group is discarded.

For K_3, R^3 pi_*F_1=H^1(B(7))^vee tensor A=0. Thus ker L=coker L=0 and its relative R^3 is free. It contributes neither relative R^2 nor degree-three torsion.

For K_4 and K_5, relative Serre pairing for constant bundles, or ordinary Serre duality applied coefficientwise to each polynomial entry of the displayed matrix, identifies L with the A-dual of a map P:V->W of finite free modules. The surviving target W is H^1(B(6)) tensor A; the other target summand is H^1(B(7)) tensor A=0. The positive maps are

    K_4: P(a,b,c)=v_s a-u_s b,
          V=(H^1(B(3)) direct sum H^1(B(4)) direct sum H^1(B(5))) tensor A;
    K_5: P(a,b,c)=v_s b-u_s c,
          V=(H^1(B(4)) direct sum H^1(B(3)) direct sum H^1(B(4))) tensor A.

Both have cokernel exactly Q_A. Signs and unused source summands change neither that canonical quotient nor the transpose identification with the actual resolution. Since Q_A is torsion, P tensor K is surjective; hence P^vee tensor K is injective. Its domain is free over a domain, so P^vee itself is injective. Equation (1) now proves H^2_A=0 for the entire three-summand coefficient.

## 3. The torsion-dual algebra lemma

Let P:V->W be any map of finite free modules over a DVR A whose cokernel Q is torsion. Put N=ker P and I=im P. Both N and I are finite free. The exact sequence 0->N->V->I->0 splits, since I is free. Dualizing it and 0->I->W->Q->0 gives

    0 -> I^vee -> V^vee -> N^vee -> 0,
    0 -> W^vee -> I^vee -> Ext^1_A(Q,A) -> 0.

Here Hom_A(Q,A)=0 and Ext^1_A(W,A)=0. Combining the sequences yields canonically

    0 -> Ext^1_A(Q,A) -> coker(P^vee) -> N^vee -> 0. (2)

Because N^vee is free and Ext^1_A(Q,A) is torsion, the latter is exactly the torsion submodule of coker(P^vee). A decomposition Q=direct sum A/(z^{a_j}) verifies

    Ext^1_A(Q,A) is isomorphic to direct sum A/(z^{a_j}).

The invariant factors, length and annihilator agree; an isomorphism of Q with its Ext dual is not claimed canonical. Formula (2), in contrast, is canonical for P. Apply it to the two positive maps of Section 2 and then (1). This proves the claimed canonical doubled Ext description.

This is why ordinary duality is wrong here: Hom_A(Q_A,A)=0 for this torsion module, while Ext^1_A(Q_A,A) carries all its invariant factors. It also shows why the free part of relative R^3 cannot be silently identified with zero.

## 4. Base change and fat fibers

For completeness, take the standard finite affine cover of Z_A. Its intersections are affine. The Cech complex computing C is bounded and consists of A-flat modules: C is A-flat and taking sections of a quasi-coherent sheaf on an affine scheme preserves exact sequences, including the flatness tests. Tensoring this complex with any A-module computes the corresponding derived base change. For A_n, flatness of C means the tensor complex computes ordinary C_{A_n}, not a derived sheaf with extra Tor terms.

Over a DVR every module has flat dimension at most one. The hyper-Tor spectral sequence therefore gives the natural short exact universal coefficient sequence

    0 -> H^i_A tensor A_n -> H^i(Z_{A_n},C_{A_n})_chi
                   -> Tor_1^A(H^{i+1}_A,A_n) -> 0. (3)

The character projector is an A-linear idempotent and commutes with these operations. With i=2 and H^2_A=0, (3) is the canonical asserted identification.

The free part of H^3_A has zero Tor_1. Resolving A_n by multiplication by z^n on A identifies Tor_1(H^3_A,A_n) with the z^n-kernel on tors H^3_A. Decomposing Q_A as in the theorem gives two copies of A/(z^{min(n,a_j)}) as abstract A-modules, and hence length 2 sum min(n,a_j). No invariant factor is evaluated.

There is an important functorial warning. Stabilization of lengths, and the parameter-dependent identifications with tors H^3_A for n>=e, do NOT mean the restriction maps from the (n+1)-st to the n-th thickening are isomorphisms. Under the z^n-kernel descriptions, the map induced by A_{n+1}->A_n is multiplication by z. Indeed a chain map between the resolutions [A --z^(n+1)--> A] and [A --z^n--> A] is z in degree -1 and identity in degree zero. Consequently the transition maps on these H^2 groups are multiplication by z, and every composite of e successive restrictions is zero. For e<=2, two successive restrictions annihilate the whole fat-fiber H^2 tower. Its inverse limit is therefore zero, in agreement with relative H^2=0; there is no compatible nonzero formal H^2 class hidden in the special-fiber jump.

At n=1, (3) describes the special fiber canonically. The original Serre-dual description Q_b direct sum Q_b is recovered by PR439's field calculation. It is not necessary to choose an identification between Q_A and its Ext dual to state that field result.

## 5. Consequence and limits

The new conclusion is stronger than a numerical torsion bound: every exceptional order-six fiber class is a base-change jump from relative degree three, and none extends to a compatible infinite sequence of classes in these parameter thickenings. Even though the finite-thickening dimensions stabilize by thickness two, their restriction maps are nilpotent, not isomorphisms. Thus “the entire quotient is determined by the first parameter jet” in PR443 must not be read as persistence of geometric H^2 under restriction through all thickenings.

This excludes that particular formal-extension route for a nonzero exceptional coefficient class. It is not a claim about lifting the actual obstruction source, nor a proof that its value or Q_0 is nonzero. The generic coefficient vanishing and the original fixed endpoint remain logically separate. Parameter order is not collision order or quantization order.

## Exact public dependencies

- PR443, commit bc5a8ba31104bc66b180984a1fdfc7f17ceb1eef: algebraic curve, actual transported geometry, local bounds and fixed special fiber.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/bc5a8ba31104bc66b180984a1fdfc7f17ceb1eef/research/hm/rank-one-algebraic-transport/PROOF.md
- PR442, commit 2072baf63868a309366a7d3ae54dc1132e56adb7: length-two controller and exponent bound.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/2072baf63868a309366a7d3ae54dc1132e56adb7/research/hm/endpoint-pencil-torsion/PROOF.md
- PR439, commit bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b: exact three resolutions and field endpoint.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b/research/hm/paired-collision-endpoint/PROOF.md
- PR437, commit 50e82ed233cd7729c38608194f990376eb832418: full filtered character coefficient identity with arbitrary coefficient bundle.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/50e82ed233cd7729c38608194f990376eb832418/research/hm/paired-collision-filtration/PROOF.md
- PR167, commit 063da90fc4543304e87e701cdefcc08225412f17: positive cohomology vanishings, used through PR439.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md

Current PR1 and PR440--443 were read on 2026-10-20. PR1's latest read comment was null's 13:24:02 UTC scoped review closure for 442, explicitly retaining the then-open relative R2 identification; 443--444 were outside that completed review set. The novelty comparison is bounded to these exact dependencies and this discussion, not an exhaustive literature claim. No selected actual HM/source-instance evaluation, multiplication matrix, sample rank, checker, or large computation was run. This is an authored mathematical argument requiring scoped review, not formal verification.
