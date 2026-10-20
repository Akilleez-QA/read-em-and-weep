# Target refinement: canonical negative lines have residual rank at least six

## Statement

For the actual twenty-dimensional target J3=A*⊗Sym³W_h, every point of every canonical negative reflection line P(W) has residual middle rank at least six. This strengthens the previously proved rank-five bound without evaluating the operation.

We use the parity notation of PROOF.md and distinguish the historical spinorial representation W_h from the negative eigenspace W of V.

## 1. The positive target has no P4 constituent

The parity computation in POINTWISE_ADDENDUM.md gives dim A−=2 and

    J3,+ = A*−⊗Sym³W_h,    dim J3,+=8.

Both factors have negative central action, so J3,+ is an A5 representation.

Let g∈G=SL2(F5) have order three. Every two-dimensional representation on which the central involution z acts negatively has determinant one, since G is perfect. Moreover g cannot act as the identity on such a representation. Indeed the kernel is normal; if it contained g, its image in A5 would be a nontrivial normal subgroup, hence all of A5. The remaining quotient of G would have order at most two and must be trivial by perfectness. That would also kill z, contradiction. Thus the eigenvalues at g are the two primitive cube roots, and its trace is -1.

Apply this to A*− and W_h. The trace of Sym³W_h at g is t³-2t=1 for t=-1. Consequently

    tr(g|J3,+) = (-1)(1) = -1.

Suppose J3,+ contained the irreducible four-dimensional A5 representation P4. Its semisimple complement would have dimension four. The only possible A5 representation types of dimension four are P4, 1⊕T, 1⊕T', and 1^4. At an order-three element, the character values of 1,T,T',P4 are 1,0,0,1. Adding the P4 constituent to those possible complements therefore gives trace 2 or 5, never -1. Contradiction.

Hence J3,+ contains no P4 constituent.

## 2. Exclude even rank four on the canonical lines

The audited `../canonical-line-parity-exclusion/PROOF.md` proves the parity blocks have constant ranks on each canonical line and that the even rank is at least four. Section 4 of `../canonical-line-rank-five-strengthening/PROOF.md` proves that an even block of rank four necessarily has constant image bundle

    I+ = P4⊗O.

The derivation there depends only on even rank four, not on equality in the total residual-rank-five bound: its source is O(-1)⊗(W⊗T), with irreducible six-dimensional coefficient representation, and its full coefficient span is a quotient of T⊕P4⊕P5.

Such an image would embed a copy of P4 in J3,+, which Section 1 excludes. Therefore the even rank is at least five on the canonical line. The audited odd strengthening already gives odd rank at least five there. Thus

    rank b ≥ 10,    rank Q = rank b-4 ≥ 6.

Normalizer equivariance proves the same assertion on all twenty-five canonical negative reflection lines.

## Limits

The conclusion is pointwise on those lines. It does not classify other rank-five or rank-four points. The only new calculation is an abstract order-three character calculation on the target; no actual-operation coefficient, selected source input, matrix rank, or source map is evaluated.
