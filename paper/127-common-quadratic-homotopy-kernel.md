# 127. Actual common homotopy kernels and the forced separated correction

## Hypotheses and theorem

Retain source2's actual nonzero pure-V compatible radical and the **residual-large** mechanism: P_h⊂NR2 with nonzero N8,2 projection. [PR1113, full immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/09b03061644e417b44b2ea97a00c73618794c268/research/hm/source2-pure-v-common-homotopy-kernel/PROOF.md) studies Γ(v)(a)=hT_a v. On NC2 its rank is twelve and kernel is exactly I2; on NR2 it is onto Hom(A,I2)=A+V+P+D, of dimension fifteen. Thus

    K_(R,2)=ker(Γ|NR2)=V+P+2D, dimension 17,
    0 → I2 → K_(R,2) → (N8,2)_(V+P+D) → 0.

**This is degree two.** It is not the older degree-four K_R=ker(h|NR4), of dimension sixteen. Neither exact sequence is a horizontal splitting of NR.

On J2=ker j2=NR2⊕(N0,2)_P, the same Γ has rank fifteen and kernel K of dimension twenty-one, with

    0 → K_(R,2) → K → (N0,2)_P → 0.

K is also the common kernel of every hT_a on all M2. The proof does not incorrectly give hT(M2) target I2: if hT_a v=0 for all a, then T_a j2v=0; the common L-kernel on irreducible I2 is zero, so v already belongs to J2.

## Why every needed row is nonzero

Actual NC quadratic multiplication is Sym²W⊗Sym¹⁶W→Sym¹⁸W/H_t. The unique D constituent survives H_t, and h is nonzero on it. Therefore Γ on NC2 is the genuine product followed by this D projection, up to a nonzero identification.

The universal whole-coefficient certificate constructs D18 using E18(d)=(H20,d)_3 and its apolar projection. The stacked matrix has size15×17 and rank12, annihilates the rank-five inclusion F12 Sym⁴W, and has an explicit nonzero twelve-minor. Thus its kernel is exactly I2. All three V, P, D rows are nonzero, not just permitted by character. The canonical nonzero A row completes surjectivity on NR2. No actual source coefficient or chosen quadratic direction is evaluated.

## The actual first correction when R=0

Add the still-unselected hypothesis R=0. For an equivariant right inverse G of Q and the canonical s:I4→P_h, put k(b,p)=G T_b s(p). Symmetry of the actual transfer makes hT_a k(b,p)=0. The quadratic descendant quotient is an isomorphism, giving injectivity of k and

    K=F2 ⊕ k(A⊗I4),       QK=F4=I4 ⊕ T_A P_h.

The dimensions are 21=9+12. The V and P correction maps are independent of G; the D map is canonical modulo I2. V and D remain in NR2. **The P correction cannot remain there:** the unique P in K_(R,2) is P_h itself, whose Q image is I4, whereas the correction P has nonzero N8,4 projection. Consequently

    e0 k|P_in : P_in → (N0,2)_P

is an isomorphism. The generator P_h remains residual; its Q-preimage correction is a different map. This forced separated component is not an exclusion of residual-large or R=0, nor a selected fifth value or positive/opposite source.

## Earlier canonical V alignment

[PR1108, full immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/c1e2c2e0013a45ff2345a687d2077d7f7e322cef/research/hm/source2-pure-v-correction-v-kernel/PROOF.md) already identifies E_V=(NR2)_V=V_C⊕V_h, where V_h=ker Γ|E_V and π2 maps V_h isomorphically to (N8,2)_V. Nonvanishing on the marked V_C follows from Θ(WV_C)=ℓ(T_Q)=I3. Under R=0, k(V_in)=V_h canonically and

    V_h=ker(e0Q2|E_V),       Q2(V_h)=(NR4)_V.

The induced factorization Γ=χ e0Q2 on E_V fixes neither χ's scalar nor the remaining triangular entry. PR1113 extends this actual V alignment to all correction channels, while showing why a wholly residual correction is impossible. No splitting of the entire negative module or positive stability is asserted.
