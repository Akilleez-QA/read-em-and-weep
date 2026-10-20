> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Independent audit: degree-twenty-four exclusion

Status: PASS. Independently checked Sections 6 and 7 of ADDENDUM.md. No outstanding mathematical corrections.

Section 6: If no plane quartic exists, at most two quintics exist. In the coprime case the residual point in CI(5,5) gives six sextics by linkage. In the common-quartic case the residual to that quartic is exactly one point, so the trace has length twenty-three inside CI(4,6); linkage gives seven trace sextics. A quadratic multiplier invertible on the finite scheme produces a trace sextic not vanishing on D, proving the strict bound of six on D. Every case contradicts the required surface sextic count. Thus the plane section is CI(4,6).

Section 7.1: The depth inequalities for a reflexive E exclude all codimension-three and codimension-four associated points of Z. At ambient codimension three, its local dimension is one, hence it is Cohen--Macaulay there. The closed non-CM locus is consequently finite, and a general hyperplane avoids it, giving a pure CM curve C.

Section 7.2: If C has no quartic, two independent quintics exist and remain independent on a general plane. Their restrictions are the unique plane quartic times independent linear forms, so their gcd has degree four. For fixed global quintics, coprime residual factors remain coprime on a general plane because their common locus has dimension at most one. Their global gcd therefore has degree four. Its vanishing on all sufficiently general plane sections implies vanishing on C, including its nilpotent structure: choose the plane equation regular on both O_C and the cokernel of multiplication by the gcd, so the multiplication image restricts exactly. A nonzero one-dimensional image has a nonzero general plane section. The remaining possible image is zero-dimensional and is excluded by purity. Thus C has a quartic. A coprime sextic and equality of degrees identify C with CI(4,6) by unmixedness of the complete intersection.

Section 7.3: The required negative-twist vanishing follows, in particular, from the explicit Ext^4/Serre-duality proof already audited in degree-fifteen-quintic-obstruction/PROOF.md, Section 3: absence of closed associated points kills sheaf Ext^4, and Serre vanishing kills the remaining local-to-global terms. This avoids relying on a choice of filtration. The complete-intersection curve has ambient polynomial restriction surjective in every nonnegative degree and no negative sections. The regular hyperplane sequence then inductively proves the same ambient-section surjectivity for Z and H1(I_Z(t))=0 for all t. Its curve quartic lifts, contradicting the established z4=0.

Conclusion: the rank-eight pair (24,12) is excluded, leaving only (19,17). This is a necessary restriction, not an exclusion or realization of rank eight. All arguments are universal; no actual operation or HM instance was evaluated.

Final revision verified: Section 7.2 now explicitly restricts the multiplication image through a plane regular on its cokernel; Section 7.3 now includes the full Ext^4 argument used above. Both revisions pass, with no outstanding corrections.
