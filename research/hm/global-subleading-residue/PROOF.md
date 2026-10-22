# Global vanishing of the actual first-subleading nilpotent residue

## Statement and dependency boundary

Let Γ=SL2(F5), let W be the negative binary representation, let U=W' be the positive binary representation, and put L=P(W), V=Sym²U. Use the actual invariant cone Q and its canonical invariant nilpotent N in H0(Q,End_0(F)(2)). In regular physical eigenframes ordered cubic-first, write its first two weighted pieces as

    N=n_8+D_12+terms of matrix weight at least 16.

Then the scalar residue of D_12 modulo weight-four commutators canonically defines a section of the actual equivariant vector bundle

    C=coker(U⊗O_L(-5) --f_3--> Sym⁴U⊗O_L(-2)).       (1)

This section is Γ-invariant and is zero. Consequently, locally over every point of L, there is a regular weight-four trace-free X such that

    D_12=[X,n_8].                                    (2)

This is a global vanishing of a residue, not a construction of a single global gauge or a splitting of the quintic-generator extension. It supplies a chartwise elimination of the zero-normal first-subleading coefficient in the fifth-norm formula. It does not eliminate the other normal coefficients or determine the surviving global obstruction.

### Sources used

The following original sources are pinned at commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, under research/hm/order-four-quadratic-load/:

- [INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md), §§2–5: actual saturated equivariant S→E and the invariant N obtained by symmetric squaring.
- [VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md), §§1–3: uniform actual Loewy layers, regular leading cubic/quintic pairs at every point of L, cubic relation K3=O(-2)⊂Sym³U⊗O(1), and the nonsplit quintic extension.
- [NO-PRESERVING-POSITIVE-CONE-EXCESS.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/NO-PRESERVING-POSITIVE-CONE-EXCESS.md), §§2–3: relative regular-pair construction and the actual cubic-annihilator presentation.
- [UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md): precisely the quotient (1) is equivariantly V⊗O_L, and H0(C)^Γ=0. This is not the different cubic relation quotient A⊗O(2).

We also use [PR774](https://github.com/Akilleez-QA/read-em-and-weep/blob/eec909bef4a7e6998737773d5eadd0ad562e79d9/research/hm/matrix-jet-filtration/PROOF.md) for the physical matrix filtration and regular local eigenframes on all of L. The local algebra input is the exact first-subleading nilpotent sequence proved in [PR776, commit c885531e345cc67d1848b0cd8baa0f02ca786f47](https://github.com/Akilleez-QA/read-em-and-weep/commit/c885531e345cc67d1848b0cd8baa0f02ca786f47), “First-subleading nilpotent jets modulo regular gauge.” The application uses [PR775](https://github.com/Akilleez-QA/read-em-and-weep/blob/af2fc052d3da2c4abc315dca268ed65b62f5cde5/research/hm/first-subleading-norm-formula/PROOF.md).

## 1. The local exact sequence is regular in families

On a sufficiently small open subset of L, trivialize the coefficient line bundles and use homogeneous binary variables. The actual leading pair f=f3, g=g5 is regular in every fiber. The symmetric-square construction gives

    n=u [[fg,-f²],[g²,-fg]],

where u is a base unit. The actual inclusion identifies the spinor module with the Koszul kernel by a module isomorphism. Since End_R(S)=R, the scalar multiplier of that isomorphism is a unit. Symmetric squaring and the determinant trivializations preserve this property. Indeed the coefficient comes from the chosen local trivializations of the reflexive spinor square and determinant line, which are isomorphisms; it is not an additional scalar function allowed to vanish. The identification can be checked off the vertex and extends by reflexivity. Thus n does not acquire an unaccounted base-zero factor.

A weight-d trace-free matrix has diagonal, upper and lower degrees d,d−2,d+2. Write Z12 for the kernel of D↦nD+Dn on weight-twelve trace-free matrices. Fiberwise the local algebra theorem gives

    0 → sl2(S)_[4] --ad_n→ Z12 → (S/(f))_4 → 0,       (3)

normalized so that v n maps to [v]. Its proof uses only regularity of (f,g); repeated roots of f cause no problem.

For clarity, (3) is valid over the base, not merely over C(L). The ambient polynomial coefficient modules are vector bundles on the base open. Fiberwise dim Z12=18, and the commutator map has rank15; these dimensions follow from the universal parametrization

    D/u=[[gp+fr,-2fp],[2gr,-gp-fr]],  p∈S7, r∈S9,

and the degree argument for fS4⊕gS2=S7. Constant rank makes Z12 and its commutator quotient vector bundles. The scalar map S4→Z12/ad_n factors through S4/fS1, because

    [ ℓ [[f/2,0],[g,-f/2]], n ] = fℓ n.

The induced map S4/fS1→Z12/ad_n is an isomorphism on every fiber, hence a vector-bundle isomorphism. Its inverse is the regular residue map ν. No rational inverse with possible base poles is used. In particular ν(D)=0 implies a regular local X in (2), and this X is unique in a fixed frame.

Finally N²=0 gives nD+Dn=0 at weight20, so its actual first-subleading coefficient belongs to Z12.

## 2. Descent under physical frame changes

Use the standard negative-coordinate charts of the weighted cone. Their coordinate changes preserve transverse homogeneity. Trivializations of O_Q(2) induced by these negative-coordinate charts change by base units only. Thus no positive-degree term is introduced by a line-bundle trivialization in this atlas.

By PR774 any physical frame transition has weighted expansion

    T=T0(1+Y4+terms of weight at least 8),
    T0=[[a,0],[c2,d]],

where a,d are base units and c2 is a binary quadratic. Its inverse has the same nonnegative weighted form. Including the base-only line-bundle transition h and the homogeneous coordinate substitution, conjugation transforms the first two pieces by

    n'=h T0 n T0^{-1},
    D'=h T0(D+[Y4,n])T0^{-1}.                       (4)

The source and target coordinate substitutions in (4) are understood. A scalar coefficient v transforms as an ordinary cover-degree-four function.

The leading cubic changes only by a base unit and homogeneous coordinate substitution: T0 sends (f,g)^t to (af,c2 f+dg)^t. Thus its cubic principal ideal, and hence the quotient by cubic multiples, is preserved. This does not choose or require a global quintic lift.

Conjugation intertwines commutators. More importantly, scalar multiplication commutes with conjugation and with h:

    h T0(v n)T0^{-1}=v n'.

Consequently the canonical scalar isomorphism in §1 intertwines the T0 action. The additional term from Y4 is a commutator and has zero residue. Therefore ν(D') is exactly the coordinate transform of ν(D), with no additive correction. This proves descent. It also shows independence of all physical eigenframe lifts, even though D itself depends on such a lift.

The argument does not assert a splitting of the filtered endomorphism sheaf. Rather, the discrepancy between two local splittings is exactly the commutator in (4), which disappears in the quotient. Nor is the conclusion based on treating a generic quotient as a global bundle.

## 3. Identify the actual global target and its linearization

An ordinary scalar of cover degree four has coefficient bundle Sym⁴U⊗O_L(-2). The actual cubic relation is

    O_L(-2) --f3→ Sym³U⊗O_L(1),

so its coefficient tensor is a section of Sym³U⊗O_L(3). Hence its degree-four multiples inside the scalar bundle have source U⊗O_L(-5): multiplication adds the twist 3, giving -5+3=-2. This identifies the descended target with exactly (1).

The cubic relation is the unique nonzero invariant cubic channel, and is nowhere zero as a binary form at every base point, as proved in the cited sources. The scalar subbundle in (1) is therefore the actual globally defined relation subbundle, not a choice made from a generic cubic. Section 2 shows that changing the quintic generator by c2 f3 has no effect on this identification.

Every operation used for descent is natural under the Γ action: the physical eigenline, the fixed negative/positive coordinate decomposition, the symmetric-square N, conjugation, and multiplication by scalars. The Γ action on the chosen coordinate atlas is homogeneous in transverse variables; its induced O_Q(2) transition is base-only. Thus the descent is Γ-equivariant with the usual coordinate linearization of (1), not with an unspecified representation twist.

The canonical N is actually Γ-invariant by the symmetric-square construction in the cited spinor-filtration note. Accordingly its descended residue is an element of H0(L,C)^Γ. The published exact universal quotient theorem gives

    C ≅ V⊗O_L,   H0(L,C)^Γ=V^Γ=0.

It follows that ν(D)=0 globally. This proves the statement and (2), without selecting any actual coefficient or value. Perfectness excludes a character ambiguity in the linearisations already used in the source; no choice of a Γ-equivariant trivializing frame has been assumed here.

## 4. Chartwise fifth-norm simplification

In PR775 write the source multiplier as s (to distinguish it from f3). The cone restriction is K|Q=sN, hence A0=s n8 and B0=s D12. On any of the regular charts above, choose X from (2), lift its even entries by the fixed harmonic lift H, and conjugate by 1−H(X). This is a regular formal ambient change of frame. To total weight16 it gives

    K'_[12]=K_[12],
    K'_[16]=K_[16]+[K_[12],H(X)],
    B'_0=B0+[A0,X]=0.

All other B_j must be transformed by the same gauge. The full bilinear norm pairing is unchanged, since

    tr(K_[12][K_[12],H(X)])=0.

Subsequently the local q⁴ correction of PR775 sets B'_4=0, changing only the source-multiplied relation class already quotiented there. Therefore the first-subleading norm representative has nine rather than thirteen retained ordered terms:

    sum over 1≤j≤3, 0≤i≤3, i+j≤4
        tr H_(4−i−j)(A_i,B'_j).

There are four terms for j=1, three for j=2, and two for j=3. The fixed scalar-reference subtraction and the exact full-source/global beta2 quotient remain unchanged. The local representatives are used in that existing global quotient; no global choice of X or B'_4 correction is asserted.

This removes the actual first-subleading scalar residue and its entire zero-normal B0 contribution structurally. It does not set B1,B2,B3 to zero, compute beta4, prove fifth-neighborhood lifting, or settle algebraicity. The statement concerns a higher-order local input simplification; it is not a new first-order obstruction claim.

## Verification status

The proof checks separately: all-point regularity, the exact degree-four scalar twist, the cubic-multiple twist, naturality under the lower-triangular T0, disappearance of the T4 commutator, and actual Γ-invariance of N. The fiberwise exact sequence is justified by explicit universal polynomial identities, then extended by constant rank, not by a selected matrix-rank evaluation. This is an authored deductive proof, not proof-assistant verification. No selected actual HM/source-instance evaluation, model experiment, or large computation is used.
