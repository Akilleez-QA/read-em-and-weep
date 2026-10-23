# No D incidence in either branch; the small transfer is nonzero

**Craig Ward · 23 October 2026 · PR1075**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/672852c59ebeb95a0329a34c1081f25476a2ff8f/research/hm/source2-pure-v-small-transfer-nonzero/PROOF.md).

## Later positive-component consequence through PR1077

[PR1077](106-positive-component-smith-profile.md) now derives the exact positive 41→37 Smith profile outside the 28-point exceptional support, with maximal generic row rank 37. That is a later consequence using additional original Bockstein premises, not a claim of this PR1075 theorem alone. Neither theorem proves full adjoint invertibility.

## The newly decided alternatives

Under conditional compatible pure-V hypotheses, let U_Q=Q(NC2) and NC4=I4⊕D_C with its actual unique D summand. In every remaining branch D_C is not contained in U_Q. Therefore

    U_Q∩NC4=I4   if dim F4=9,
    U_Q∩NC4=0    if dim F4=16.

The second conclusion now covers all endpoint-sixteen branches, including nonzero N0 projection. The earlier residual-large qualification is superseded.

In endpoint nine, the [incidence criterion](104-transfer-scalar-incidence.md) then forces γ≠0 in R=γR₁. Thus that branch has exactly the **nonzero conic coefficient stratum [1:0]** and, by the completed scheme and original-fourth ideal transfer theorems, exactly Z plus twelve reduced ambient conic points, total length 46. Its zero-gate alternative is excluded. The numerical scalar remains unknown; neither endpoint branch nor source occurrence is selected.

## Injective polynomial prolongation

For any linear j:Sym⁴W→Sym¹⁶W, define P(j)=μ(Id_W⊗j)Δ, where Δ(f)=(x⊗f_x+y⊗f_y)/5 on Sym⁵W. Writing f_i=j(x^(4−i)y^i), its six outputs are ((5−i)x f_i+i y f_(i−1))/5. If they all vanish, the polynomial-domain recurrence forces f0=0, then successively every f_i=0. Thus j↦P(j) is injective even without equivariance.

For equivariant j, if its prolongation landed in I3=f12 Sym⁵W, irreducibility and Schur's lemma would make it scalar multiplication by f12. Euler's identity and injectivity then force j to have image I2=f12 Sym⁴W. Consequently any actual D complement J to I2 in NC2 has a nonzero prolonged T image distinct from I3. Together these two T copies exhaust the T-isotypical part of NC3. This does not assume SL2 equivariance of j or select a D complement by its character alone.

## Contradiction from actual Q multiplication

Suppose D_C⊂Q(NC2). The actual restriction kernel I2 permits an equivariant D complement J mapping isomorphically to D_C. The full actual joint-negative kernel is NC4, so W D_C=0. Since Q is multiplication by the same polynomial in consecutive degrees,

    Q3(lv)=l Q2(v).

It follows that Q3 kills WJ and also WI2=I3. Prolongation therefore makes it kill the entire T-isotypical component of NC3. The unique V_C⊂NC2 satisfies W⊗V=T, so Q3 kills its negative descendants too. Hence W Q2(V_C)=0, putting Q2(V_C) in the full joint kernel NC4.

But Q2 is injective on V_C, since ker(Q|NC2)=I2=D. Its nonzero V image cannot lie in NC4=P+D. This contradiction proves the all-branch no-D-incidence assertion. Equivariance and multiplicity-free P+D then reduce the whole intersection to U_Q∩I4, already known branchwise.

This is actual polynomial commutation of Q in degrees two and three, not an extension of h or a claim that Q preserves NC or NR. The universal rank-85 prolongation certificate supports the recurrence argument; it is not an actual-source rank calculation.

## Consequences and retained boundaries

Endpoint nine now has nonzero diagonal R, full bilinear transfer B and alternating transfer Alt(B), by the normalized small-branch equivalences. Its conditional component scheme is the conic length-46 scheme, not the distinct C₅ length-46 scheme. The converse from conic-line membership to endpoint nine is still not proved.

The theorem does not give full adjoint invertibility, a new Smith-normal-form conclusion, source realization, endpoint exclusion or complete repair. It does not identify the matching-character sum NC4⊕U_Q with NR4. Four necessary source-dual pairs remain.
