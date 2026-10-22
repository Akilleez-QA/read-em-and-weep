# The actual normal operator square shadow from harmonic transitions

## Result and scope

For a pure quintic-generator transition P=I+p E21, the corrected cone operator's normal square-ideal shadow has an explicit universal formula involving only its cone connection and the actual transition p. In particular the unknown cochain primitive in the corrected Hessian symbol need not be differentiated explicitly to compute this transition contribution.

The formula below gives the leading actual degree8 shadow in the two-chart framed presentation described in Section4. It does not evaluate its global cohomology class or claim it is nonzero. Diagonal, root-line, and physical q0 frame factors are retained; their harmonic discrepancies are proved zero, not suppressed.

## 1. Cone operator and harmonic lifts

Work in fixed local cover coordinates and a physical equation frame q0=nu q, q=xz-y^2. Write the corrected cone operator of twist4 as

    O=H D+A,    H=k a h,

where A is tracefree, D=D_a, and all determinant-line actions have the conventions of ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md. On the chosen overlap the homogeneous transition is

    P=[[1,p],[0,1]] transposed = [[1,0],[p,1]].

The actual p is a positive binary quadratic with its base line factor retained. Put A11=b, A12=c, A21=d for the SOURCE connection A=A_i. These source coefficients occur in formulas (1)-(2), although K and the trace pairing are in the target j-frame. The transported cone connection is

    A'=P A P^-1-H(DP)P^-1,

so its entries are

    A11'=b-pc,  A12'=c,
    A21'=d+2pb-p^2c-H Dp.

Let L be the canonical harmonic lift and B the proved first product correction,

    L(u)L(v)=L(uv)+q L(B(u,v)) modulo q^2.

Here p,c,Dp have cover degree2, while b,H have degree4. The derivation D preserves the harmonic splitting: it acts on the base and linearly on the positive cover coordinates, including the required Euler frame term. This is the natural linear-coordinate equivariance of the harmonic splitting, not a choice setting Dq to zero in every local frame.

## 2. Exact first-normal discrepancy

Use the harmonic matrix lift of A on each side, with derivative part L(H)D. Define K by

    L(A')-[P L(A)P^-1-L(H)(DP)P^-1] = q K modulo q^2.

Since p is quadratic, its lift is linear in x,y,z and P is an exact determinant-one matrix. Expanding with the harmonic product formula gives

    K12=0,
    K11=B(p,c),
    K21=-2B(p,b)+B(p^2,c)+B(p,p)c+B(H,Dp),
    K22=-K11.                                     (1)

The term B(p,p)c must be retained: the ordinary square of L(p) is not L(p^2). All B terms in (1) use their respective input degrees; no common denominator is substituted incorrectly.

The discrepancy K is in the TARGET j-frame: K=L(A_j)-transport(L(A_i)). Accordingly the matrix paired with it is N_j=[[f g_j,-f^2],[g_j^2,-f g_j]], where g_j=g_i+p f. In equation(2) the symbol g means g_j, not g_i. The square-ideal shadow is therefore

    trace(N_j K)=2f g_j B(p,c)
      -f^2[-2B(p,b)+B(p^2,c)+B(p,p)c+B(H,Dp)].     (2)

Writing the same formula using g_i instead requires the extra term 2p f^2 K11; it cannot be silently omitted. Relative to the actual equation q0 the coefficient is (2)/nu. It has cover degree8 and belongs to the actual I_Z^2(4)_8=P4 O_L(-4). Its cohomology class is the lower normal operator obstruction after the actual trace/square-ideal map. Multiplication by a then gives the third-value target, subject to the fixed boundary sign and the actual second-symbol quotient.

## 3. Why a matched nilpotent symbol suffices for this shadow

The full-frame Hessian matching theorem identifies the corrected Hessian symbol with the actual midpoint symbol modulo local normal conjugations. To exhibit the reference normal transition, remain on a PURE triangular overlap with the same physical q0=nu q frame. Set m=mix(H_f,H_p)/(16nu). The frozen universal covariance identity and the exact cone tangent transport give

    N_H,j-L(P)N_H,i L(P)^-1 = -q0 m S1,j,
    L(P)S1,i L(P)^-1 = S1,j modulo q0.

The actual invariant primitive is chosen with u_j-u_i=m in these frames. Hence, for N_corr,i=N_H,i+q0 u_i S1,i,

    N_corr,j-L(P)N_corr,i L(P)^-1
      =q0(-m+u_j-u_i) S1,j=0 modulo q0^2.

Thus the required reference transition is EXPLICITLY L(P) for this pure component. The primitive is retained and cancels the whole residual, not merely its class. Variable p causes no omitted term in this algebraic transport identity; its derivative is already present in the operator formula(1). This argument does not say that an uncorrected Hessian symbol is preserved by L(P).

After making the local normal conjugations supplied by that theorem, an actual normal transition and this reference transition differ by 1+q0 C, where [C,N]=0. For a regular pair f,g the tracefree centralizer consists of c0 N. One proof first solves over the fraction field and then uses regularity of f,g to remove denominators; a regular rational scalar multiplying all f^2,fg,g^2 is regular across their codimension-two zero set. Scalar centralizer terms, if using unrestricted frames, also have zero pairing with N.

The cone operator satisfies O_ad(N)=lambda N. Therefore changing the normal transition by 1+q0 c0 N changes its normal operator discrepancy by a multiple of N:

    -[H D(c0)+lambda c0+H r0 c0] N,

in the missing-correction convention displayed immediately below (the opposite transport convention changes the overall sign), where r0=Dq0/q0 denotes the ordinary derivative of the local equation representative. The global vector field annihilates the physical section q0 with its natural line action; this does NOT imply that its ordinary derivative in every local equation frame vanishes. The additional equation-frame scalar therefore remains in the expression. Its trace pairing with N is zero because N^2=0.

More generally, if an unassembled normal transition correction is 1+q0 Q and is NOT proved centralizing, its shadow contribution is

    trace(N([Q,A]-H DQ-H r0 Q))
      =(lambda-H r0-H D)trace(NQ),

where H D N+[A,N]=lambda N and r0=Dq0/q0 in the same ordinary local convention. Only in a frame with r0=0 does this simplify to the shorter formula. It cannot be discarded. The displayed exact transport is what licenses the centralizer comparison for the pure component; the same license must be established separately for other frame factors. Hence this centralizer ambiguity cannot change the square-ideal shadow. Local changes of the chosen operator lift alter (2) only by the corresponding square-ideal Cech coboundary.

This is a comparison of the actual shadow, not an identification of the whole actual normal bundle with an arbitrary triangular extension.

## 4. Two-chart assembly and the degree bound for stabilizers

Use a fixed global Wprime basis and the two standard charts of L, with its root gerbe for the cover variables. On their overlap, positive-cover frames change by a base scalar. Cubic/quintic diagonal line factors are also base functions. No variable arbitrary GL2 coordinate change is required in this presentation.

Harmonic lift commutes exactly with these base functions. A diagonal generator matrix P_d therefore satisfies L(P_d A P_d^-1)=P_d L(A)P_d^-1, while the term H D(P_d)P_d^-1 is a base function times H and also lifts exactly. Positive-cover scalar changes preserve the harmonic Cartan summand; the transformed derivation includes its linear Euler term. Differentiating this equivariance shows that D commutes with the splitting in these frames. The fixed-determinant compensator is likewise a base function times H, and has zero harmonic-product discrepancy. Hence the diagonal and root-line factors contribute no first-normal harmonic-product discrepancy. The actual equation factor q0=nu q is still retained, so the displayed cochain is divided by nu and transported in the actual P4 O_L(-4) frame.

In the oriented cone frames furnished by the full-frame matching theorem, any difference between an actual cone transition and the homogeneous diagonal/triangular transition is an SL2 stabilizer I+tN, with t regular. It is not enough to ignore such a factor merely because its cone operator correction is centralizing: a harmonic lift of cN need not equal c times the corrected normal N.

Instead use the explicit degree bound. The homogeneous N has weighted cover order8 (diagonal8, upper6, lower10); the relevant cone connection has weighted order4 (diagonal4, upper2, lower6). A regular t has nonnegative cover degree. Thus I+tN changes this leading connection only in weighted order at least12. Taking its first-normal discrepancy lowers cover order by4, since q has cover degree4, so the resulting K has weighted order at least8. Pairing with N has cover degree at least16. It cannot affect the degree8 shadow in (2). This also accounts for the difference between harmonic and symbol-compatible lifts of the stabilizer terms. The reference stabilizer I+t N_corr exists exactly and has determinant1, but no stronger all-degree cancellation is being assumed here.

The corrected Hessian matching and the explicit pure-overlap transport in Section3 then identify the actual degree8 trace shadow with (2), with the base line factors just described. Normal changes preserving the matched symbol contribute only the centralizer shadow already proved zero. With the two-chart presentation there is a single overlap cocycle; no omitted triple-overlap assertion is needed. This is a cohomological comparison on the actual bundle, not an actual-instance rank experiment or an assumed identification with a separate ambient extension.

## 5. Pin down the two cone connection entries used by the formula

Only A11 and A12 occur in (2). They can be obtained without an arbitrary choice of the remaining local operator matrix. Put

    H Df=m f+n g.

The decomposition is unique in cover degree7: a relation between f times quartics and g times quadratics would require a syzygy coefficient of degree-1. On D, the quotient n=H Df/g is global. More explicitly H has bidegree(4,2), f has (3,3), and g has (5,-5), so n belongs to O_D(2,10). A change of local line connection adds a multiple of f to Df and does not affect this restriction. The divisor sequence has kernel O_Y(-1,7), whose cohomology along the positive projective line vanishes in both degrees. Therefore

    H0(O_Y(2,10)) -> H0(O_D(2,10))

is an isomorphism. It gives a unique global polynomial n in Sym^2(Wprime) tensor H0(O_L(10)). Locally m=(H Df-n g)/f, and under g_j=g_i+p_ij f one has m_j=m_i-p_ij n.

Let Lambda be the EFFECTIVE local scalar defined by

    H Dn_matrix+[A,n_matrix]=Lambda n_matrix.

It includes the required adjustment from the global physical line scalar to the chosen local determinant/spinor frame. It must not silently be replaced by that global scalar. Since A is tracefree and the operator preserves the line generated by sigma,

    A12=-n,    A11=Lambda/2-m.                       (3)

The effective Lambda is supplied by the actual canonical Serre-residue correction and the natural line actions. Substituting (3) into (1)-(2) expresses the remaining class in terms of the actual cubic, its quintic trivialization, the actual nonsplit transition p, and that fixed scalar correction. The Hessian primitive is not an additional unknown in this shadow formula.

The unresolved step is to evaluate the resulting class in H1(P4 O_L(-4)) and its contraction by a, modulo the actual second-symbol image. The nonzero extension e and the nonzero lower multiplication map alone do not imply a nonzero value.
