# Cubic zero frames in every derivative arithmetic-progression three-plane

## Result

Work over C. Fix m in F_5 and nonzero d in F_5, and set

    e_- = D_(m-d), e_0 = D_m, e_+ = D_(m+d),
    W = span(e_-,e_0,e_+).

The canonical cubic f restricted to W factors through an eight-dimensional Schur space. The induced linear map has seven-dimensional image and kernel exactly

    C·τ(e_-,e_0,e_+),
    τ(x,y,z) = x⊗(y∧z) − z⊗(x∧y).

Consequently, an independent ordered triple (x,y,z) in W has f(x,y,z)=0 if and only if, for nonzero scalars a,b,c, it is either

    (a e_-, b e_0, c e_+), or (a e_+, b e_0, c e_-).

Scheme-theoretically, on the frame open in W³ the cubic zero scheme is the disjoint union of these two copies of (G_m)³. It is reduced and smooth of dimension three and codimension six in that nine-dimensional open. This is a restriction to a fixed derivative three-plane, not a classification of independent triples in all of V³ or of transverse directions leaving W³.

## Imports and evidence boundary

Read [the cubic explicit weight basis manuscript](../../cubic-witness-detectors/cubic-explicit-weight-basis/PROOF.md), [the two plane cubic zero scheme manuscript](../two-plane-cubic-zero-scheme/PROOF.md), and [the cubic massey module reduction manuscript](../../canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md). The imported facts are trilinearity, outer reversal, cyclic zero, structural nonvanishing of f(u,u,v) for independent u,v, and the weight/support conclusions of the explicit-basis theorem. In particular, on the AP set above, f(e_-,e_0,e_+)=0 and the other two middle-index order classes are nonzero negatives of each other.

All arguments below use abstract tensors, universal coordinate rings, and weight separation. The seven-dimensional image is a structural dimension theorem, not a computed rank of an HM/source/model matrix. No actual products, matrices, evaluated Massey values, points, jets, residues, or polynomial instances are computed. 

## 1. Universal Schur realization and normalization

For any three-dimensional vector space W, let

    K = ker(W⊗Λ²W → Λ³W),

where the arrow is exterior multiplication. This is the standard Schur_(2,1)W realization and has dimension eight. The universal tensor τ lies in K: its two exterior products are equal. It obeys outer reversal and cyclic zero.

The tensors τ span K. In a basis e_1,e_2,e_3, the six tensors τ(e_i,e_i,e_j)=e_i⊗(e_i∧e_j), i≠j, span its six repeated-index multidegrees. The remaining all-distinct multidegree has dimension two and is spanned by any two of its three middle-index order classes. Outer reversal and cyclic zero are the only relations among those three classes. These statements follow by expanding the displayed tensor in W⊗Λ²W; thus the quotient of W^⊗3 by the two argument identities maps isomorphically to K.

Accordingly there is a unique linear map T:K→J3 satisfying

    f(x,y,z)=T(τ(x,y,z)).

This normalization agrees with the two-plane formula and requires no choice of a scalar for f.

## 2. Weight separation forces the kernel

All index arithmetic in this section is in F_5. A repeated triple with repeated index i and remaining index j=i+h has target weight (a,3a²+δ), where

    a=−(2i+j), δ=h².

Put a_0=−3m=2m. The six repeated-index basis tensors in K have weights as follows:

    (i,j)=(m-d,m):       (a,δ)=(a_0+2d,d²)
    (i,j)=(m,m-d):       (a,δ)=(a_0+d,d²)
    (i,j)=(m,m+d):       (a,δ)=(a_0-d,d²)
    (i,j)=(m+d,m):       (a,δ)=(a_0-2d,d²)
    (i,j)=(m-d,m+d):     (a,δ)=(a_0+d,4d²)
    (i,j)=(m+d,m-d):     (a,δ)=(a_0-d,4d²).

Here the pair (a,δ) determines the actual weight (a,3a²+δ). The first four are distinct because d≠0, and the last two are distinct from them because 4d²≠d². Structural repeated-input nonvanishing makes all six images nonzero. They therefore span six distinct one-dimensional target weight lines.

The all-distinct two-dimensional subspace of K has weight

    (a,δ)=(a_0,3d²).

Since 3d² is nonsquare whereas d² and 4d² are square, this line is different from all six preceding lines. By the imported AP theorem, the restriction of T on this two-dimensional space has nonzero image, of dimension exactly one, and kills τ(e_-,e_0,e_+). This tensor is nonzero, so it spans the kernel on that subspace.

The seven distinct target weight lines exclude cancellation across the seven source weight spaces. Hence im(T) has dimension seven and

    ker(T)=C·τ(e_-,e_0,e_+).

This argument uses no GL(W)-equivariance assertion about T.

## 3. Identification with traceless endomorphisms

There is a natural isomorphism

    Φ: W⊗Λ²W → End(W)⊗det(W),
    Φ(u⊗(v∧w))(t)=u⊗(t∧v∧w).

Under Φ, exterior multiplication corresponds to trace, so K identifies with sl(W)⊗det(W). To verify the signs, put ω=e_-∧e_0∧e_+ and H=diag(1,0,−1) in the displayed ordered basis. Then

    Φ(τ(e_-,e_0,e_+))=H⊗ω.

Indeed the first term is the projector onto Ce_- and the second is the projector onto Ce_+, with a minus sign. Thus H has three distinct eigenvalues 1,0,−1.

Identify the frame open with GL(W) by (x,y,z)=(g e_-,g e_0,g e_+). Naturality of τ and Φ gives

    Φ(τ(x,y,z))=det(g)·gHg^(-1)⊗ω.

As det(g) is nonzero, the kernel criterion is exactly

    gHg^(-1) ∈ C·H.

Only the universal tensor is used naturally here. The fixed map T need not intertwine the GL(W)-action on any target.

## 4. Field-valued frame classification

Write gHg^(-1)=μH. The left side has eigenvalues {1,0,−1}, forcing μ=1 or μ=−1. For μ=1, g preserves all three eigenspaces, so g is diagonal. For μ=−1, g fixes the zero eigenspace and swaps the positive and negative eigenspaces. Hence g is a diagonal matrix times the permutation exchanging e_- and e_+.

This proves exactly the two displayed families. In particular it does not allow arbitrary mixtures of the endpoint lines, even though the endpoints span a distinguished two-plane.

## 5. Scheme structure on the frame open

The kernel computation is linear over C. Choose a complement to ker(T) in K and a left inverse on its image. It follows that the ideal of f=Tτ equals the ideal of the image of τ in K/ker(T). This ideal equality persists under every base change. On GL(W), Φ and the invertible determinant factor therefore identify this ideal with the condition that gHg^(-1) lie in the line CH, as a scheme condition rather than only on complex points.

Introduce its unique line coordinate μ: the scheme is isomorphic to the closed subscheme in GL(W)×A¹ defined by

    gHg^(-1)=μH.

Uniqueness and regularity of μ follow, for example, by taking the (1,1) entry of gHg^(-1). Taking the trace of the square of this matrix identity yields

    2=2μ², hence μ²=1.

Since 2 is invertible, the coordinate ring splits as the product of its μ=1 and μ=−1 quotients. On μ=1 the relation is gH=Hg. Its off-diagonal entries vanish because the pairwise differences between the three eigenvalues are units. Thus this piece is precisely the diagonal torus. On μ=−1 the relation is gH=−Hg. The only permitted entries are those with eigenvalue sum zero: positions (1,3), (2,2), and (3,1). Invertibility forces all three to be units, giving exactly the endpoint-swapping torus coset.

There are no extra nilpotents or embedded scheme structure: the two coordinate rings are Laurent polynomial rings in three variables. Each piece is a regular codimension-six embedding in GL(W). This description survives arbitrary base change; after a nonreduced base change, reducedness of the total space is of course not asserted.

## 6. Scope of the geometric consequence

Combining this theorem with the two-plane classification gives the set of all zero triples lying in this fixed W: triples spanning at most one dimension; triples with an input zero; and the two independent-frame families above. These are exhaustive because every triple in W has span dimension at most three. More explicitly, the reduced zero support in W³ has exactly six irreducible components:

- the three coordinate-zero linear six-planes {x=0}, {y=0}, {z=0};
- the rank-at-most-one determinantal cone D for a generic 3-by-3 matrix, of dimension five;
- the two linear three-planes L_−=Ce_-×Ce_0×Ce_+ and L_+=Ce_+×Ce_0×Ce_-.

The two three-planes are the closures of the frame families. The standard rank-one parametrization identifies D with the affine cone over P²×P², so it is irreducible of dimension five. None of these six closed irreducible sets contains another. Each coordinate-zero plane has a dense open of rank-two triples outside L_−∪L_+, obtained by removing these proper closed intersections from its rank-two open. This dense open lies outside D as well. The full rank-two open can meet L_− or L_+ at their dependent boundaries; no disjointness of the full boundary strata is asserted. Each three-plane has a dense rank-three open, absent from the other components. The rank-one cone has a dense open with all columns nonzero and a common image line different from each of the three distinguished lines, absent from all five other components. Equivalently these are statements about nonempty universal opens, not evaluations of selected actual inputs. This proves the exact irreducible-component list by the preceding set classification.

This identifies the reduced closed subscheme over C by the Nullstellensatz; it does not claim that the full cubic scheme is reduced, a global primary decomposition, or multiplicities along the dependent boundary in W³. In particular, its seven independent cubic component equations do not imply a complete-intersection claim.

If one invokes the previously established graded-framed filtered-extension representability theorem, its restriction to affine complex families of frames in this fixed W is represented by these same two torus pieces, with the imported uniqueness up to unique graded-framed isomorphism. No new representability theorem, actual physical-class decision, or statement about arbitrary three-planes is claimed.
