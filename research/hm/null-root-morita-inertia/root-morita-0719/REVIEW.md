# Independent audit of exact line untwisting

## Verdict

PASS for the stated universal algebra construction. No order, inverse, sign, or bimodule-coherence correction is required in equations (1)–(5). The external-product statement is correct under its explicit external-algebroid hypothesis. The report and `../trivial-inertia-0719/RESULT.md`, read together, do **not** close the strict-versus-weak action gap or establish a prescribed coarse ambient identification.

The conclusions depend on the qualifications already stated: actual local unit lifts, genuine ambient coherence, a genuine line rather than a rational class, and a small-extension kernel on which positive deformation parameters act trivially. Equality of characteristic evaluations is not a replacement for a comparison of ambient classes or full descent data.

## 1. Ambient gauge and pentagon

Set c_ij=q_ij^{-1}. The standard nonabelian change of presentation is

    F^c_ij=Ad(c_ij)F_ij,
    A^c_ijk=c_ij F_ij(c_jk) A_ijk c_ik^{-1}.

Substitution gives exactly equation (1). In particular the order is q_ij^{-1}, then F_ij(q_jk)^{-1}, then A_ijk, then q_ik. Neither q_ij nor F_ij(q_jk) can be exchanged in general.

The pentagon proof uses the valid identity

    A_ijk F_ik(x)=F_ij F_jk(x) A_ijk.

After this substitution, the original pentagon is applied without commuting a lifted line unit through A_ijk. The right-hand expansion cancels only adjacent inverse factors. This verifies the full coherence, rather than just equality of inner automorphisms modulo the center.

Classical reduction of A^L is one because ℓ_jk ℓ_ij=ℓ_ik, and classical reduction of F^L is the identity because the classical algebra is commutative. Differentiality follows coefficientwise from multiplication by formal elements and the stipulated differential products and overlap operators.

For two choices q and q̃, the comparison gauge is indeed c_ij=q̃_ij^{-1}q_ij. Its classical reduction is one. This is an equivalence of presentations, not a preferred equality of representatives.

## 2. Bimodule coherence and inverse functors

For P, right semilinearity uses

    (F_ij(p)q_ij)(q_ij^{-1}F_ij(b)q_ij)
      =F_ij(pb)q_ij.

The inverse triple unit has the precise order

    (A^L_ijk)^{-1}
      =q_ik^{-1} A_ijk^{-1} F_ij(q_jk) q_ij.

Consequently

    A_ijk p_ik(p)(A^L_ijk)^{-1}
      =A_ijk F_ik(p) A_ijk^{-1} F_ij(q_jk)q_ij,

which is p_ij p_jk(p). This proves equation (2).

For Q, direct composition gives

    q_ij^{-1}F_ij(q_jk)^{-1}A_ijk F_ik(x)A_ijk^{-1}
      =A^L_ijk qmap_ik(x) A_ijk^{-1}.

Multiplication of P⊗Q descends by F_ij, and multiplication of Q⊗P descends by F^L_ij. These are the appropriate identity bimodules on the two sides. Thus this is genuine invertible bimodule transport, not merely a comparison of endomorphism algebras.

The reductions of P and Q are respectively L and L^{-1}; the functor Q⊗_A(-) therefore has the claimed untwisting direction.

## 3. Rows, defects, and the small-extension normalization

The left multiplication in H_ij=q_ij^{-1}G_ij is necessary. For rows, identifying a local tensor x⊗v with the row xv gives

    qmap_ij(x) φ_ij(v)
      =q_ij^{-1}F_ij(xv)G_ij
      =F^L_ij(xv)H_ij.

This also independently verifies the side on which q_ij^{-1} must occur.

For arbitrary G, substitution gives exactly

    D^L_ijk=q_ij^{-1}F_ij(q_jk)^{-1}D_ijk.

No use of module descent occurs in this calculation. In particular it applies to candidate transition lifts with nonzero defects.

For a small extension R'→R with kernel I satisfying m_(R')I=0, all positive deformation terms disappear when multiplying an I-valued defect. The multiplier becomes ℓ_ij^{-1}ℓ_jk^{-1}=ℓ_ik^{-1}. Since this is a classical scalar, the displayed normalized identity follows:

    g_ik^{-1}D^L_ijk=(ℓ_ik g_ik)^{-1}D_ijk.

The normalization by g_ik^{-1} on the left is consistent with the row convention of `../../null-module-boundary-audits/module-lifting/RESULT.md`. Its endomorphism-frame transport is g_ij^{-1}(-)g_ij. Tensoring by a classical scalar line leaves this transport unchanged, so the two normalized defects live in the same endomorphism Čech complex.

This classical normalization should not be generalized to an arbitrary square-zero ideal merely from I²=0. The stronger annihilation property of a small extension is what lets all lower positive-order coefficients drop out. Equation (4), by contrast, is exact without that simplification.

Local module morphism matrices stay unchanged under the tensor-coordinate identification above. The displayed morphism descent equation therefore transforms correctly, including its order. Degreewise application preserves differentials, composition, and the local exactness furnished by the regular bimodules. A deformation-groupoid comparison across several coefficient rings uses compatible choices or reductions of the q's; independently selected q's give equivalent, rather than literally identical, presentations.

## 4. Square-zero expansion

Let K=F_ij(q_jk)⋆q_ij and write ℓ=ℓ_ik. Its classical coefficient is ℓ and its first-order coefficient is

    K_1=r_jk ℓ_ij+v_ij(ℓ_jk)ℓ_ij+ℓ_jk r_ij
          +μ_i(ℓ_jk,ℓ_ij).

Normalization of μ gives

    (A_ijk⋆q_ik)_1=r_ik+a_ijk ℓ.

Since A^L=K^{-1}⋆(A_ijk⋆q_ik), its first-order coefficient is

    a^L_ijk=(r_ik+a_ijk ℓ-K_1)/ℓ.

One can obtain this without any inverse expansion: solve K⋆(1+ε a^L)=A⋆q_ik and use μ_i(ℓ,1)=0. This proves the entire triple-unit formula in (5), including the order-sensitive term −μ_i(ℓ_jk,ℓ_ij)/ℓ_ik and the minus sign of v_ij(ℓ_jk)/ℓ_jk.

Likewise, first-order inner conjugation by the star inverse of ℓ gives

    v^L_ij(f)−v_ij(f)
      =ℓ_ij^{-1}[μ_i(f,ℓ_ij)−μ_i(ℓ_ij,f)].

The r_ij terms cancel here. For μ_i(f,g)=(1/2)π(df,dg), this is π(df,d log ℓ_ij), as claimed. Thus retaining only a scalar gerbe adjustment would lose actual unary overlap data.

Equation (6) is the tensor-line characteristic identity under the supplied Atiyah/HKR convention. It follows by expanding At(E⊗L)=At(E)+c1(L)Id and retaining the stipulated minus-gerbe sign. It does not by itself prove a full HKR cochain comparison, and the report correctly does not use potential nonfaithfulness of characteristic evaluation to infer one. Any application needing the precise ambient HKR class must retain the specified comparison and total-sign conventions, or use the actual formulas (1) and (5).

## 5. External product and mixed coefficients

An actual external tensor algebroid supplies commuting factor subalgebras and factorized F and A. With q=q^z⊗q^h, each factor of (1) separates in precisely its original order. This proves literal factorization of the transported chosen presentation, and the regular bimodules factor as stated.

The st contributions displayed for products, overlap maps, triple units, and lifted q are all required and correct. No use of st=0 is valid under the stated coefficient algebra. The same tensor bookkeeping works for square-zero coefficient line sheaves.

This audit does not replace the explicit external-algebroid hypothesis by matching pure restrictions, an external classical space, or a factorized line. In particular factorization of the ambient does not factor a general E or solve its mixed module obstruction.

## 6. Strict versus weak action: the gap remains open

Putting F, A, and q on every arrow of a specified action/Čech groupoid yields the claimed coherent stack transport. It does not force the new group-multiplication coherence units to be one. Even where induced automorphisms happen to compose strictly, a nontrivial central multiplication coherence can still remain in the weak-action data.

The invariant-basis theorem in `../trivial-inertia-0719/RESULT.md` assumes a genuine group action both on the local algebra and on its semilinear module. The proof averages that actual action and uses invariance of the resulting basis. It is not a proof for a projective or inner-coherent action.

The hypotheses also include locality, finite freeness, invertibility of the group order, trivial action on the whole residue field, and trivial action on the module residue fiber. The reduction ideal must be genuinely stable. Once those hypotheses hold, the theorem's invariant-basis and coefficient-reduction arguments are sound without a flatness assumption. Its actual reduction ideal is I∩D^G, not a proposed ideal identified only by characteristic classes or a linear trace.

Accordingly the two reports imply only the following conditional sequence:

1. Construct the coherent line Morita transport using genuine lifted line data on the full groupoid.
2. Supply a strict local realization or a separate stack-theoretic effectiveness argument appropriate to coarse descent.
3. Verify the local ring, residue, freeness, inertia, and coefficient-ideal hypotheses in that realization.
4. Apply the invariant-basis theorem there.
5. Independently identify the resulting coarse algebra and coefficients with the proposed target model, if such an identification is required.

Step 1 is established by the report under its lifting hypotheses. Steps 2, 3, and 5 are not supplied by adjoining the invariant-basis theorem. No assertion that they are supplied should be inferred from the phrase “equivariant Morita transport.”

## Scope of this audit

This was a static symbolic audit of the two requested reports and the relevant universal row-obstruction and tensor-line conventions in their cited reports. No physical source or jet values are evaluated in this argument. No retained obstruction value was evaluated. The original result files were not changed.
