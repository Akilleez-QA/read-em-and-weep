# Independent review: actual fifth-lift coexistence

## Verdict

**PASS.** No mathematical correction is required in the reviewed proof, conditional on its explicitly pinned structural inputs. This is a deductive mathematical review, not proof-assistant certification or an independent reproof of every upstream result.

Reviewed file: `PROOF.md`

Exact SHA256:

```text
beb5d356cd3ef1c33737430ed6e74634b8177a008741a80d6471211fa3cad324
```

The hash was checked directly before review. The proof was not edited.

## Source verification

The following full texts were fetched read-only at the exact immutable revisions cited in the proof:

1. [PR696, polynomial parameter descent](https://github.com/Akilleez-QA/read-em-and-weep/blob/958244d6d9d3b326f66c073a9d669717c953ec32/research/hm/scalar-parameter-descent/PROOF.md), especially section 1. This constructs an actual polynomial section J4 of bidegree (3,1) using fixed linear splittings of actual section spaces. It is not merely a statement about possible scalar families. Its h-linearity at fixed a therefore applies to the raw boundary map used here.
2. [PR685, third-lift uniqueness](https://github.com/Akilleez-QA/read-em-and-weep/blob/449a8df60662bd7a1d93e318ea4f7e6dab28e5ad/research/hm/third-lift-uniqueness/PROOF.md), sections 2–4. It realizes every s in A+D by classified completion changes, constructs the compatible fourth lift, and gives the boundary variation -beta2_a(s) in the q-t a convention. It also proves that even fourth-lift changes at fixed third completion have zero fifth boundary.
3. [PR766, uniform full-scalar exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/a43b46c98e53716978d0a7750843f2224b4d2408/research/hm/uniform-full-scalar-exclusion/PROOF.md), particularly its statement and section 4. It proves nonzero global rho4 for every nonzero source pair and supplies the common nonzero S4 and restriction formulas for every classified even J4.
4. [Actual fifth-boundary ladder](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md), section 2, equations (7)–(9). These give the exact sheaf sequence, raw target P4, and identification of the fourth value with the raw boundary modulo im(beta2_a).
5. [PR770, faithful fifth norm](https://github.com/Akilleez-QA/read-em-and-weep/blob/b242300110c33627eb77ee5ab36cc81fffa359e4/research/hm/faithful-fifth-norm/PROOF.md). It identifies the raw four-dimensional target and its faithful norm image, with the ordinary ideal square on the smooth weighted stack. Its quotient statement and fixed-K raw-zero statement are distinct, as required here.

## Findings

### 1. Raw fifth-lift existence

For fixed nonzero a, h -> aJ4(a,h) is linear by PR696. The connecting homomorphism is linear, so T_a maps the five-dimensional source H to the four-dimensional E. Its kernel is therefore nontrivial. Exactness of the actual restriction sequence turns raw zero into a global trace-free fifth lift, and averaging preserves the even restriction. This proves actual-family existence without selecting or evaluating a source and without assuming any second-symbol rank.

### 2. Entire quotient kernel and classification

The identification beta4_a=p_a T_a gives

    dim ker(beta4_a) >= 5 - (4 - dim V_a) = 1 + dim V_a.

For a quotient-zero source, T_a(h) need not itself vanish. PR685 realizes an s in the full A+D range with beta2_a(s)=T_a(h), and its compatible correction subtracts exactly that raw class. Thus the corrected representative has raw zero. Conversely, every classified representative with a fifth lift has raw zero, and invariance modulo V_a gives beta4_a(h)=0. The claimed equivalence is correct and does not identify quotient-zero with raw-zero for the original polynomial representative.

The sign is correct specifically for the stated ladder-compatible q-t a convention. No inversion of beta2_a or generic-rank hypothesis is used. Transporting the correction through the linear isomorphism tau_* also gives the stated norm-class correction, without replacing the stack square by a coarse annihilator square.

### 3. Twists and scalar coefficient

All relevant twists agree. The quadratic q has degree two; K=aJ4 has twist twelve. Hence the kernel in the restriction from 5Q to 4Q is B_Q(12-8)=B_Q(4). J4 squared has twist twenty, so its q^3 coefficient S4 has twist fourteen. K squared has twist twenty-four, with leading coefficient c=a^2 S4 of twist eighteen. Finally, the coefficient of the displayed q^3 cube has twist

    18 + 8 + 2 + 2 = 30,

which becomes thirty-six after multiplication by q^3, as required for K cubed. Cayley–Hamilton is valid after local trivialization of the twisting line bundle and glues with these power twists.

### 4. Every fifth lift has exact index four

For any fifth lift of any classified K at nonzero a,h, the restriction of its scalar square to 4Q is the fixed nonzero q^3 class. Consequently its scalar square has exact q-adic order three on 5Q. Its square is zero modulo q^5 because it belongs to (q^6), so K5^4=0.

The restriction of K5^3 to 4Q is nonzero: its last-layer coefficient is c a^4 h N. Nonzero source sections and c have nonzero product on integral Q, and multiplication on the torsion-free bundle B_Q(2) cannot annihilate the nonzero N. The last-layer injection preserves this nonvanishing. Therefore K5^3 is nonzero and the index is exactly four. Nothing about the freely varying fifth-layer correction can change either conclusion.

This is a statement about the global twisted endomorphism and its powers. It does not assert that c is a unit or that the same pointwise behavior holds at every closed point. The proof explicitly maintains that distinction.

### 5. Conditional higher-thickening law

For an assumed fixed-twist extension K_n on nQ, n>=4, the scalar square still has exact q-order three and leading coefficient c. The graded pieces are the appropriate Q twists of locally free sheaves. Whenever 3k<n, c^k and c^k a^4 h N are nonzero, so both K_n^(2k) and K_n^(2k+1) are nonzero. Whenever 3k>=n, both powers vanish by ideal divisibility. Thus the first vanishing exponent is exactly 2 ceil(n/3).

This uses integrality and torsion-freeness, not pointwise invertibility of c, and remains valid despite possible zeros of c on Q. The fixed twist twelve is essential and is stated correctly. The result is conditional on an extension existing; it does not establish any higher existence.

## Scope and restrictions

The conclusion genuinely combines actual-family fifth-lift existence with uniform nonzero fourth-square scalar. It does not determine beta4_a on any selected source, prove beta4 identically zero, infer higher integrability or algebraicity, or evaluate an actual HM coefficient or source.

Only read-only source retrieval, local text inspection, hash verification, and this local review-file write were performed. No actual HM/source evaluation, matrix or rank experiment, large computation, external write, or upstream verifier execution was performed.
