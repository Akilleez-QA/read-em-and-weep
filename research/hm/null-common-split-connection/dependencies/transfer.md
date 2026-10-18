# Differentiated contraction: exact stage-two transfer

## Result

The derivative of the entire inner stage-two HPL word has an exact decomposition into a scalar Čech boundary, an explicitly nonclosed-input term, an induced-cohomology connection term, and three insertions of the derivative of the original-resolution differential. This is a formal operator identity, not a vanishing theorem or a domain certificate. No actual model, owner, source, jet or matrix-polynomial value was evaluated.

Use the contraction, common-frame restriction and single-transpose conventions of dependencies/hpl.md and the general-input projection identity in dependencies/endpoint.md. Denote the internal End differential by d, original-resolution Čech operator by δ, row Čech operator by Δ, and coefficient derivative by a prime. The latter is a genuine coefficient derivative, retaining variation of the source differential. Operators carry the leading owner selected by their place in the word; no H is moved past δ.

For the moment δ'=0 and L'=0; §6 gives all extra terms otherwise. Set

    Q = δj,             J1 = Hδj,             J2 = -HδJ1,
    a = πj',            t = Hj',              S = HH',
    U = Sδj - Hδt,
    W = -SδJ1 + HδU,
    E = -H d' J2 + HδH d' J1 + HδHδH d'j.

J1 here is the unsigned word Hδj, regardless of the input Čech degree; J2 has its actual common sign for both degrees two and three. Every H has the internal-degree index dictated by its input. Then

    J2' = dW - δU - UΔ + J2 a + E.                 (1)

Since Ld=0 and L commutes with the admitted restrictions,

    L J2' = -δ(LU) - (LU)Δ + (LJ2)a + LE.         (2)

Thus for each input Z the inner derivative is replaced by

    (LJ2')(Z) = -δ((LU)Z) - (LU)(ΔZ)
                         + (LJ2)(aZ) + L(EZ).   (3)

These are identities of operators/cochains in the same formal localization. The outer weights and retained test remain outside this statement. Multiplying the boundary by nonconstant outer weights requires the existing outer comparison/Ward accounting, not silently declaring the weighted expression a boundary.

## 2. Actual End normalization

The imported contraction gives h²=hA=Bh=0, E0=AB and BA=1. Hence hE0=E0h=0. For an internal-degree-r endomorphism F,

    H_r(F)=hF+(-1)^r E0 Fh.

Direct word expansion gives

    H_(r-1) H_r(F)
      = h²F + (-1)^r hE0 Fh
          + (-1)^(r-1) E0 hFh - E0² Fh² = 0.

Similarly Hj=0 and πH=0 follow from hA=Bh=0. Thus this is normalization of the actual supplied End homotopy, not a replacement by some arbitrary normalized homotopy. Its source-specific validity inherits the existing contraction/primitive premises. It is not a new verification of primitive A or arithmetic denotation.

## 3. Differentiation identities retaining every variation

Differentiate dH+Hd=1-jπ, H²=Hj=πH=0 and dj=0. The exact identity is

    H' = dS - Sd - H d'H + H'jπ - jπ'H.            (4)

Proof: multiply the differentiated contraction equation on the left by H and use H²=Hj=0, then use dH+Hd=1-jπ to solve for H'. In the last term πH'=-π'H. Thus π' is retained in the universal identity.

Also, using dj'=-d'j,

    j' = dt - H d'j + ja.                         (5)

In internal degree -1, both projection terms in (4) vanish by support. In input degree zero, jπ'H vanishes because π' still has support only in degree zero, while H'jπ=-tπ follows by differentiating Hj=0. Consequently

    H0' Q = dS Q - H d'J1 - tΔ,                  (6)

where dQ=0 and πδj=Δ are the already authenticated general-input identities. The nonclosed term tΔ is not discarded.

## 4. Stage-one and stage-two algebra

Substituting (5)–(6), using dδ=δd and the absence of projection in negative degree, gives

    J1' = δt + dU - tΔ + J1 a + B,
    B = -H d'J1 - HδH d'j.                       (7)

For example Hδdt=Hdδt=δt-dHδt; this is the source of U, not a commutation of H and δ.

Now dJ1=δj-jΔ, so dδJ1=-δjΔ. Use the negative-input-degree case of (4) in

    J2' = -H'δJ1 - HδJ1'.

The d terms combine as d(-SδJ1+HδU)=dW. The remaining nonclosed terms combine as

    -SδjΔ+HδtΔ = -UΔ.

The remaining differential-variation terms are -H d'J2-HδB, exactly E. This proves (1). No assumption [d',δ]=0 or [V,d]=0 has been used.

Types provide an additional check: U raises Čech degree by one and lowers internal degree by two; W raises Čech degree by two and lowers internal degree by three; E and J2' raise Čech degree by two and lower internal degree by two. Therefore both δU and UΔ have the required arity. In particular degree-two endpoint inputs use U on degree-three defects in the second term; this is an operator extension, not a wrong-arity production call.

## 5. The two remaining defects are concrete

For j(R)=A R^t B, π(F)=(BFA)^t, let C=BA'. Differentiating BA=1 yields B'A=-C. Therefore

    a(R)=πj'(R)=R C^t-C^t R.

This is the induced row-endomorphism connection term, not an unspecified scalar. It is generally nonzero even with a perfectly compatible split connection. It retains derivatives of both the inclusion and projection; their paired normalization is used, not their constancy.

For the underlying resolution differential D_K,

    d'(F)=D_K' F-(-1)^|F| F D_K'.

Thus all three E terms explicitly retain the derivative of the actual original-resolution differential. One must use the same common-frame D_K as in the imported contraction. A finite-chart array, a prescribed-frame differential and a common-frame differential cannot be substituted for each other without their connection transformation.

For each of the four current/scalar endpoint inputs Z_d in endpoint-defect-transfer-public, ΔZ_d is already the specified scalar-free current–F cup expression. Accordingly the term -(LU)(ΔZ_d) in (3) is a scalar-free replacement of that derivative subfamily, through the different transfer operator LU. The boundary still contains Z_d, and aZ_d and EZ_d still can contain raw scalars. No cancellation of them is asserted. The equality alone supplies no new global pole/domain estimate for LU or its boundary; the earlier bound for a different Ward homotopy cannot simply be reused.

## 6. Moving ambient restrictions, selector and connections

If the chosen coefficient derivative does not commute with original-resolution restrictions, retain the literal extra terms

    E_restr = -H δ' Hδj - HδH δ'j.

The full selected derivative then is

    (LJ2)' = L'J2 - δ(LU) - (LU)Δ
                     + (LJ2)a + L(E+E_restr).     (8)

Here the unprimed identity Lδ=δ_scalar L remains required. If the scalar-side derivative/frame changes, its effect must also be included in L' and the coefficient connection, rather than inferred away.

A local split connection from the authenticated physical/common split frame can make d,H,j,π parallel relative to the induced cohomology connection. That statement is conditional on using that SAME splitting and all transports. It does not imply δ is parallel: different leading owners have different split connections, and their differences appear in δ's first-face commutator. Nor does it make L parallel automatically. Passing to such a connection moves terms from E and a into overlap/selector connection defects; it does not remove the complete inner derivative without those defects. No global compatible connection or vanishing Atiyah class is assumed here.

A simple formal countercontrol is the acyclic complex over k(t), C^-1→C^0 with differential multiplication by t and homotopy multiplication by t^-1 in reverse. It has j=π=0, H²=0 and dH+Hd=1. Nevertheless H'=-t^-2≠0 and (4) reduces exactly to H'=-H d'H. Claiming a parallel H under the ordinary coefficient derivative while omitting d' is already false in this two-term example. This uses an invented scalar indeterminate, not physical/model data.

## 7. Scope

This is a real term-family reduction for the specified stage-two inner word, with all signs and projection endpoints retained. It neither asserts that the full remainder is zero nor establishes zero trace of the new boundary without a domain theorem. It uses only static/formal identities and supplied dependency text. It is not an external publication or a new current-branch attestation.

## 8. Nonclosed inputs, degree labels and varying row differential

All contraction identities are identities of coefficient families on one localization, so differentiating them is legitimate; pointwise identities at a single unvarying parameter value would not suffice. For each input degree n write U_n, W_n, a_n, E_n and J2_n for the preceding words acting on that degree. Equation (1) means literally

    J2_n' = d W_n - δ U_n - U_(n+1) Δ_n
                         + J2_n a_n + E_n.

Likewise (3) uses U_(n+1)(Δ_n Z). It makes no closure assumption on Z. The unsigned intermediate J1_n=Hδj is not identified with the signed HPL J1^(n) when n is odd. The actual HPL J2^(n) is the displayed minus word for every n. If Z itself varies, differentiation of the output adds J2_n(Z') (or LJ2_n(Z') after selection) to this kernel derivative.

The row differential generally varies even if ambient δ'=0. Differentiating its actual projection identity gives

    Δ' = π'δj + πδj'.

There is a useful explicit compatibility identity:

    Δ' = Δa - aΔ - π d'J1 - πδH d'j.             (9)

Indeed π'j=-a, and differentiation of πd=0 and πH=0 gives

    π' = -aπ - π d'H - πH'd.

Apply this to δj; its final term vanishes since dδj=0. Substitute (5) in πδj', whose dt term vanishes since πd=0. This proves (9). Therefore even in the case d'=0 the correct conclusion is Δ'=[Δ,a], not Δ'=0. In equation (1) there is no missing extra Δ' term: it is a derivative of the literal word -HδHδj, and only the unprimed projection identity was used. Equation (9) supplies its differentiated compatibility separately. The degree-explicit first two terms of (9) are Δ_n a_n-a_(n+1)Δ_n.

A nonzero formal row-variation control is an abstract rank-two cohomology frame change with transition g=diag(t,1), over k(t), and a constant off-diagonal basis endomorphism e12. The transport law itself is

    transport(e12)=t^-1 e12,
    θ=g^-1g'=t^-1 e11,
    transport'(e12)=-t^-2 e12
                    =[transport(e12),θ] ≠ 0.

This is an invented basis-symbol example, not an actual source/model matrix-polynomial computation. It can be realized with a zero internal differential and H=0, j_i and π_i inverse frame identifications, and fixed ambient Čech restriction. All normalized contraction identities hold. The kernel J2 is zero in that control, while the row differential has the displayed nonzero first-face derivative. Thus it cleanly refutes inferring Δ'=0 from fixed ambient δ, or adding a free unweighted Δ' term to the stage-two kernel formula. It does not independently test nonzero stage-two values; the formal derivation above is what covers them.
