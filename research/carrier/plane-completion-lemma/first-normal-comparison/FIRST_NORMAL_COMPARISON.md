# Exact first-normal comparison with the completed plane object

Date: 2026-10-11. This package constructs the first-normal section correction and the actual common-refinement identification. It does not identify an ancestor, carrier or defect, and it does not change the earlier plane-completion artifacts.

## Result and necessary signed dictionary

The frozen first-normal middle cochains admit an exact first-order realization on our completed plane object with the prescribed section E0 and positive pairing +t0 h, under the explicit vector-transition dictionary below. Regular section corrections are exported; no existence assertion is inferred merely from an obstruction dimension.

For a symmetric Hamiltonian tensor η=Σ cij ui uj, define the symplectic endomorphism

    Aη(x)=Σ cij [ui Ω(uj,x)+uj Ω(ui,x)].

A diagonal term is counted twice. In the pinned polynomial notation, Aη(E0)={η,E0}. We use j→i **vector** transitions

    g̃ij=(1−h Aηij) gij modulo h².

This minus sign is part of the comparison, not an omitted detail. In our Čech convention, the positive-pairing boundary and the class of Aη(E0) are equal. A negative vector action cancels that boundary; a positive vector action would double it.

The pinned source explicitly specifies its Poisson bracket, tensor convention, infinity-to-finite transport, and positive BCH bracket terms. The inspected files do not explicitly state the signed dictionary between those tensors and j→i vector logarithms. Accordingly this note supplies a verified **order-one convention bridge**. It does not assert that an undeclared opposite dictionary was intended or erroneous. Translating higher logarithms/BCH under this dictionary is outside this first-normal result.

## 1. Immutable source and independently read data

Input commit: `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`.

- Model and positive-pairing statement: https://github.com/Akilleez-QA/read-em-and-weep/blob/6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb/research/carrier/formal-five-parameter-chart/formal-chart.md
- Frozen cochains: https://github.com/Akilleez-QA/read-em-and-weep/blob/6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb/research/carrier/formal-five-parameter-chart/data/first_jet.json
- Slot conventions: https://github.com/Akilleez-QA/read-em-and-weep/blob/6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb/research/carrier/formal-five-parameter-chart/data/README.md
- Explicit Poisson/BCH conventions: https://github.com/Akilleez-QA/read-em-and-weep/blob/6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb/research/carrier/formal-five-parameter-chart/audit_original_cover/check_original_cover.py

The local `first_jet.json` is byte-pinned by SHA-256
`2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10`.
The checkers import no producer code and no supplied evaluation or obstruction matrices. They read the actual frozen quadratic tensors and contract them directly with E0 using Ω.

Write a0=X³+Y³ (called `a` in the checkers), S=X²+Y², F=XY, w=W⁶, g=S−zW², C=S²+zSW²+z²W⁴, T=−3S+2F. The four chart parameters remain a,b,c,d and are distinct from a0. All calculations are exact over Q.

## 2. Direct middle-cochain and evaluation checks

The coordinate order is (P,E0,E1,E2). For a term c ui uj, the evaluation vector is

    c [ui Ω(uj,E0)+uj Ω(ui,E0)].

The four pairing entries Ω(Bj,E0) are (0,0,−F,−g) on the finite base chart and (0,0,−F,−g/z) on the infinity chart. Thus this check includes the diagonal factor and does not substitute a stored evaluation table.

Before using evaluations, the checker verifies the **full quadratic** finite, infinity and mixed Čech defects are divisible by their actual relation r. The mixed tensor transport is z⁻⁴ Sym²(TB), including TB[E0,E1]=zC. Hence these really are cochains in Sym²(G)L⁻¹I after quotienting A. It separately verifies the resulting evaluated vectors form a G I cocycle with the vector transport TB.

The image of the origin's evaluated cocycle in H²(AI), in the original X,Y,W Laurent basis, is exactly

    Δ = z³/(W² X Y⁴) − z³/(W² X⁴ Y)
        + z²/(W⁴ X Y²) − z²/(W⁴ X² Y).

Each of the a,b,c,d directions has zero class. The c,d evaluations are already identically zero, since their tensors are multiples of E0².

This Δ equals the fixed-middle positive-pairing boundary computed from the completion. One independent cover-change formula is useful for checking the sign. Define M by

    (X⁸,Y⁸,W⁶)ᵀ = M (W⁶,g,F)ᵀ,

    M = [[z³X², X²C, F(F²−S²−2SX²)],
         [z³Y², Y²C, F(F²−S²−2SY²)],
         [1,0,0]].

Then det M=C F (X²−Y²)(F²−S²). Because the completion's second radical coordinate is −g, its boundary on the standard cover is

    Π[−z a0 det M/(X⁸Y⁸W⁶)] = Δ,

where Π retains exactly the monomials with all three plane exponents negative. The minus sign comes from −g, not from a numerical fit.

## 3. Completion frames on the original coordinate cover

To make section corrections regular on the same cover as the frozen cochains, construct local completions on D(X),D(Y),D(W). A covector λ with λ(r_E)=1 defines the extra-coordinate pairing ψ=a0 λ.

For U=X or Y put

    L_U = F(F²−S²−2SU²).

The finite-chart covectors are

    λ0,X=(z³/X⁶, −C/X⁶, L_X/X⁸),
    λ0,Y=(z³/Y⁶, −C/Y⁶, L_Y/Y⁸),
    λ0,W=(1/W⁶,0,0).

The infinity covectors are

    λ∞,X=(1/X⁶,0,L_X/X⁸),
    λ∞,Y=(1/Y⁶,0,L_Y/Y⁸),
    λ∞,W=(z⁻³/W⁶,z⁻²C/W⁶,0).

Every displayed covector is regular on its named open and base chart, and each equation λ(r_E)=1 is checked exactly.

For either base chart, let d=det(λX,λY,λW), with the covectors as rows. Put

    bij=a0 (λi × λj),
    cij=−K(a0²d)ij,
    wij=(cij,bij) in B.

Here K is the explicitly implemented ordered X,Y,W monomial Čech homotopy, removing the first coordinate with nonnegative exponent with its ordered-simplex sign. The checker verifies Π(a0²d)=0 and δc=−a0²d. Consequently

    δw = (a0 d) r,

so qj↦qi+wij gives exact rank-four quotient transitions. These are newly specified frames for the same completed plane object, not an assumed ancestor cover.

The base-overlap maps for these frames are also computed, not left implicit. With TE the E-block of TB define

    μi=z³ TE⁻ᵀ λ∞,i,
    bi=z a0 (λ0,i × μi).

The residual of bi+TB w∞,ij−z w0,ij−bj is central in G. Its P coefficient is a closed scalar one-cochain κij. Taking ti=K(κ)i gives the exact base shift Ki=(ti,bi). The checker verifies every residual and primitive, so q∞,i↦zq0,i+Ki is an actual algebraic base map on the coordinate cover.

## 4. Explicit common-refinement identification with the earlier quotient frames

Let the earlier radical patches be indexed i=1,2,3, where r_i is a unit, and let the coordinate patches be indexed U=X,Y,W. Work on their intersections, refining by the ordinary projective trivializations when needed. The identification is identity on the given B/A=G and sends

    q_coordinate,U ↦ q_radical,i
       + a0[(e_i*/r_i) × λU] + t_iU P.

The E part is the cross product above. The following scalar terms make this identification commute with the actual previously constructed plane and base transitions. Define

    kX=Y²(2X³+Y³)/X⁷,
    kY=X²(X³+2Y³)/Y⁷.

Rows are i=1,2,3 and columns are X,Y,W. On the finite base chart use

    t0 = [[C kX/w, C kY/w, 2Y²/w],
          [−z³ kX/g, −z³ kY/g, (2Y²−TF/g)/w],
          [0,0,(2Y²+C/F)/w]].

For the infinity chart put u=z⁻¹, k=W²−uS and D=W⁴+uSW²+u²S²=z⁻²C. Use

    t∞ = [[0,0,(2u²Y²−D TF/S³)/w],
          [kX/k,kY/k,(2u²Y²+u³TF/k)/w],
          [0,0,(2u²Y²+D/F)/w]].

Every denominator is a geometric unit on the named radical/coordinate intersection. There are no unwanted base poles: finite coefficients are regular in z, infinity coefficients in u. These isometries fix the relation and all of B, preserve the local forms and are invertible (identity diagonal with a last-column shift). The refinement checker tests their plane compatibility on both sides and their compatibility with the **actual earlier** finite-to-infinity isometry, not merely an abstract existence theorem.

Their restriction to G is identity. In particular the action Aη(E0), already a G-valued vector, transfers to the earlier quotient frame simply by its explicit relation projection Ri. The distinguished P inclusion and E0 section are unchanged by this identification.

## 5. Explicit regular section corrections

Let Eij=Aηij(E0) be the directly evaluated frozen cochain. For the origin, write the first-normal coefficient as

    ξi=t0 qi+si,

where t0 has finite representative z and infinity representative 1. For parameter directions, only the corresponding si is needed.

For the origin set yij=Eij−t0wij; for a direction set yij=Eij. Its B-valued Čech differential is r f for an explicitly computed scalar top-cochain f. The checker verifies Πf=0, then constructs

    ζ=Kf,
    s=K(y−rζ).

It checks δζ=f and δs=y−rζ coefficient by coefficient. Thus, in G,

    δs+t0w=E       (origin),
    δs=E           (directions).

These are precisely the section equations for the vector-transition convention (1−h Aη). The mixed base equation is checked separately on every original plane open:

    Ki + TB s∞,i − s0,i − Ah_i(E0) = 0 in G

for the origin, with Ki omitted for the directions. Relation-valued remainders and their regularity are checked explicitly. This rules out a purported solution that works on the two base charts but fails to glue between them.

The exported coefficients are in `FIRST_NORMAL_SECTION_CORRECTIONS.json`. Their nonzero Laurent-term counts are:

- origin: finite27, infinity16;
- a direction: finite9, infinity11;
- b direction: finite7, infinity6;
- c,d directions: both zero.

Every correction is regular on its named plane and base open. Their coefficient characters are checked: finite slot j has weight 1+d_j, while infinity slot j has weight d_j−5. Since si is G-valued, it does not change the D pairing. Therefore

    ṽ=v+h(t0q+s),   β(ṽ)=+t0h modulo h².

On the common refinement, transfer this section by replacing q with q_radical plus the explicit shift in §4 and projecting with the earlier Ri. This provides the requested section in the previously constructed quotient frames, rather than only in an abstractly isomorphic completion.

## 6. Evidence boundary and reproduction

Run `python check_first_normal_comparison.py` and `python check_refinement.py`. The first checker has 746 exact checks; the refinement checker has 153 checks covering 1,080 scalar matrix/vector entries. The first checker uses only rational Laurent arithmetic; the second uses exact symbolic rational functions and checks the geometric denominator conditions from the explicit formulas separately in this note. Neither uses a numerical tolerance.

This closes the first-normal compatibility problem for **our completed plane object with the stated signed dictionary**. It constructs positive-pairing section corrections and an explicit common-refinement map using the frozen middle tensors. It does not prove that an unspecified ancestor restricts to this object, produce an algebraic carrier, compute a reflexive hull or defect, or assert a higher-order sign convention not explicitly compared here.

Verification environment: Python3.12.14 and SymPy1.14.0. Normal and Python−O executions produced byte-identical check receipts and section coefficients. Independent review separately rebuilt the cover-change determinant and all five evaluated cohomology classes, checked the signed section equation, and inspected the regular refinement maps. The signed order-one realization is accepted within the scope stated above.
