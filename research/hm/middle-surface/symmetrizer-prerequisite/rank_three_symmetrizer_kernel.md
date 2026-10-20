# Rank-three symmetrizer lemma in dimension four

Let E be a four-dimensional complex vector space and let B:E→E have rank three. Define

L_B(ab) = (B(a)b + aB(b))/2 on Sym²E.

Then dim ker L_B ≤ 3. Equality holds if and only if B is diagonalizable and its eigenvalue multiset is {0, λ, λ, −λ} for some λ ≠ 0.

## Proof

Work with D_B = 2L_B, which has the same kernel. Decompose E into its generalized eigenspaces E_α. The decomposition

Sym²E = (⊕_α Sym²E_α) ⊕ (⊕_{α<β} E_α E_β)

is D_B-invariant. On each indicated summand, D_B is the scalar α+β times the identity plus a nilpotent operator (with α=β on the symmetric-square summands). Indeed the nilpotent terms act on the two tensor factors, commute, and hence have nilpotent sum; restriction to symmetric tensors preserves this property. Thus the summand is invertible unless α+β=0.

Since rank B=3, dim ker B=1. Consequently the zero generalized eigenspace E_0 consists of a single nilpotent Jordan block J_k, where 1≤k≤4. Let U be the sum of the nonzero generalized eigenspaces, of dimension 4−k. The mixed summand E_0 U is invertible. Therefore

dim ker D_B = dim ker D_{J_k}|Sym²E_0 + dim ker D_B|Sym²U.

### The zero block

Choose e_0,...,e_{k−1} with J_ke_0=0 and J_ke_i=e_{i−1}. Direct calculation gives:

- k=1 or 2: kernel = span{e_0²}, of dimension 1.
- k=3 or 4: kernel = span{e_0², e_1²−2e_0e_2}, of dimension 2.

For completeness, for k=4 write q=Σ_{0≤i≤j≤3}a_{ij}e_ie_j. Its image is

Dq = a_01 e_0² + (a_02+2a_11)e_0e_1 + (a_03+a_12)e_0e_2
     + a_13 e_0e_3 + a_12 e_1² + (a_13+2a_22)e_1e_2
     + a_23 e_1e_3 + a_23 e_2² + 2a_33 e_2e_3.

The vanishing of these coefficients leaves exactly a_00 and a_11 free, with a_02=−2a_11 and all other coefficients zero. For smaller k, omit nonexistent indices, giving the assertions above.

### The nonzero blocks

Only summands E_λ E_{−λ}, λ≠0, can contribute. Their dimensions are (dim E_λ)(dim E_{−λ}).

- If k=1, dim U=3. At most one opposite eigenvalue pair occurs. Its two multiplicities are either (1,1) or (2,1), so its entire summand has dimension at most 2. Thus dim ker D_B≤1+2=3.
- If k=2, dim U=2. The possible opposite pair has multiplicities (1,1), hence contributes at most 1. Thus dim ker D_B≤1+1=2.
- If k=3, dim U=1. No opposite pair occurs, and the kernel dimension is 2.
- If k=4, U=0, and the kernel dimension is 2.

This proves the bound.

### Equality

Dimension three requires k=1 and an opposite pair of multiplicities (2,1). After changing the sign of λ if necessary, write U=E_λ⊕E_{−λ}, with dimensions 2 and 1. On E_λ E_{−λ}, D_B identifies with N_λ⊗I, because the one-dimensional −λ space has zero nilpotent part. Its kernel has dimension two exactly when N_λ=0. All eigenvalue blocks are then semisimple. Conversely, that diagonal eigenvalue configuration gives the independent kernel directions e_0² and the two products E_λ E_{−λ}, so equality holds.

## Immediate linear-algebra consequence for the intended application

For every nine-dimensional linear subspace W⊂Sym²E, dim L_B(W)≥9−3=6. Thus if W is the linear span of the quadratic Veronese image of a surface F and dim W=9, the products mB(m) span at least a six-dimensional space. This statement requires that the same fixed rank-three linear map B describes all ordered factors and that the product space is identified with Sym²E. It does not by itself establish those geometric hypotheses.
