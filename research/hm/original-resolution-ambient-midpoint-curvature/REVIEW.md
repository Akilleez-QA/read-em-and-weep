Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

# Independent final-byte review

## Verdict and binding

**Accepted as a conditional structural proof.** No correction to PROOF.md is required.

Reviewed on 2026-10-18. This review binds exactly the 9,873-byte PROOF.md with SHA-256:

`292c4faf593e0d46552cd5c98bbc32732e9a18c23da547d760f01f1ff0d517cb`

I read the persisted proof independently after restoration, rather than adopting an earlier acceptance report. I also inspected relevant static passages of the stored transgression source and restored overlap-domain/HPL dependencies. This is not a fresh audit of their entire transitive premise chain. The sibling's source-verification report is provenance information, not a substitute for the mathematical checks below.

## Mathematical checks

1. **Average connection.** Flatness of both endpoints gives F(t)=t(t-1)[A_a,A_c], hence Fbar=-[A_a,A_c]/4. The average preserves d. The formula for its action on j_iX follows from A=-j_iL+dXi, the negative bracket map j_i, and internal closure of j_iX. No Cech closure of X is needed, and no flatness of the average is inferred.

2. **Explicit graded homotopy.** With B=j_iL and D=dXi, differentiating the two mixed terms in R gives -[B_a,D_c]-[D_a,B_c]. Differentiating the antisymmetrized final term gives [D_a,D_c], since both D factors have degree zero. Thus [A_a,A_c]=[B_a,B_c]+dR=-j_i[L_a,L_c]+dR. R is skew in a,c and has internal degree -1. This proves Fbar=-j_iFmid-dR/4 and [Fbar,j_iX]=j_i[Fmid,X]-d[R,j_iX]/4 with the printed signs. Substituting A=-B+D also verifies the equivalent edge expression for R.

3. **Actual C4 replacement.** The four printed tuples and signs agree with the stored transgression formula, whose coefficient is +1/64 on [U_b,[[L_a,L_c],L_d]]. This equals the printed -1/16 expression using Fmid=-[L_a,L_c]/4. Two applications of the bracket anti-homomorphism give a positive nested-bracket lift. Substitution of the preceding curvature formula gives precisely j_iC4=E_C/16+dN_C/64. Internal closure of the lifted L and U supplies the required derivation identities. The result concerns this slot with its actual owner and transported U, not a full S4 alternation or a replacement of other quartic terms.

4. **Exact-input HPL.** Starting with Jtilde2(dN)=-H delta H d delta N, use Hd=1-j pi-dH on delta N. Its projection vanishes because its internal degree is -1; the delta-squared term vanishes. Apply Hd again to delta H delta N, whose degree is -2, to obtain delta H delta N-dH delta H delta N. The final selector kills the d term and commutes with delta. The boundary sign is therefore positive. This argument uses neither Cech closure of N nor closure of a row precursor. It is consistent with the retained stage-two minus sign.

## Occurrencewise ledger

The arithmetic has been checked independently using only short integer tuples. Products add at the same occurrence, while sums take maxima after omission embeddings; equal labels never merge positions.

- R: (18,10)/(5,4), from jL and Xi or Xi and dXi. Using dXi=A+jL is sufficient and adds no differential-coefficient premise.
- N_C: (35,24,5)/(12,12,3), the sum of R, jL and jU allowances.
- Its selected boundary primitive: (39,35,24,5)/(12,12,12,3), giving uniform 39/12.
- E_C: (27,24,5)/(9,10,3), from the edge curvature bound (10,10)/(2,2), jL and jU.
- Its selected stage-two output: (35,31,27,24,5)/(9,10,10,10,3), giving uniform 35/10.

Every allowance is dominated occurrencewise by the unchanged full-comparison weights 54/29. The primitive has four positions and its boundary five. This does not confuse them with the six positions of a boundary of a degree-four output.

## Domain and trace conclusion

The argument establishes rational sheaf membership before applying pole inequalities. It uses genuine connection differences in a common frame, tensorial Xi, preserved character under H and j, and the four distinct directions in each tuple. Both selected expressions have internal degree -2 and full character, so the stated root-line convention places their coefficients in O_Y(-4,-4,-4,-4). Character extraction is the free-cover coefficient projection, including at branch points, without dividing by odd generators.

Given the admitted regular degree-compatible selector and the established full ordinary comparison, the homogeneous clearing sections and regular partition factors make the degree-three primitive a legitimate regular coefficient cochain. Original target tags make the inherited standard factors units on the full intersection. A partial-prefix interpretation still requires its suffix clearing factors. Commutation of the full comparison with delta and multiplication by the established global test make the difference in (T) an admissible Serre-trace boundary. This justifies (S); internal exactness by itself would not justify it.

## Explicit limits

Acceptance retains the stated contraction, negative bracket-map convention, flat normalized endpoint connections on that contraction, genuine transported currents and their bounds, regular selector, coefficient-line covariance, full comparison, and global-test premises. It does not establish arbitrary implementation semantics or freshly prove those retained premises.

Only C4 is replaced. Q4, M2, the covariant-adjoint derivative with the full kernel, overlap/current-F families, and retained corrections remain. No total cancellation, rational-divergence certificate, detector value, zero obstruction, or source-specific nonzero value follows. The review performed static text reading, file hashing, and tiny integer ledger checks only. It performed no physical source/model/matrix/polynomial/point/jet/residual evaluation.
