# Excluding distinct planar factor images

Work over C. Let E have dimension four, K⊂Sym²E have dimension at most five, and S⊂P(K) be an integral surface generically of rank two. Let X be the closed integral closure of an irreducible ordered-factor component above the rank-two open of S. Assume its two factor images are distinct projective planes P(U),P(W). Put H=U∩W, of dimension two. Suppose v:K→E is linear and densely compatible on S, meaning v(ab)∈span(a,b). Square avoidance means v(e²)∉Ce whenever 0≠e²∈K.

**Theorem. These assumptions contradict square avoidance. More precisely, X must be the graph of a projective linear isomorphism P(U)→P(W); its product span has dimension five and a unique normal form described below.**

The graph classification in Sections 1–3 is independent of compatibility. Sections 1–2 prove the stronger reduction from arbitrary distinct planar factor images; the original bounded task assumed the linear graph in advance.

## 1. Three bilinear equations force a linear graph

Let K'=span(S). Symmetric multiplication μ:U⊗W→Sym²E has kernel Λ²H, of dimension one, and image dimension eight. Therefore L=μ⁻¹(K') has dimension dim K'+1≤6. Its annihilator has dimension q≥3. Choose a basis of these bilinear equations. For a∈U their evaluations form a q×3 matrix M(a) of linear forms in a, acting on W. Since X dominates P(U), M has generic rank at most two.

Its generic rank is not zero: otherwise all equations vanish. Its generic rank is not one either. Indeed a linear space of matrices all of rank at most one has a common image line or a common row line. To see this, write a nonzero member u⊗r. Any other nonzero member u'⊗r' must have u' proportional to u or r' proportional to r, since their sum has rank at most one. If both types of nonproportional variations occur, their sum has rank two. Thus one common factor works for the whole space. In the common image-line case all q bilinear equations are constant multiples of one equation, contradicting their independence. In the common row-line case every second factor lies in one fixed kernel plane in W, contradicting dominance onto P(W).

Thus M has generic rank two. Select two rows independent over C(P(U)), and a third row independent of them over C; this is possible since q≥3 and the original equations are independent. The resulting 3×3 linear matrix N has determinant zero and generic rank two. Its adjugate A is nonzero, homogeneous quadratic, and of generic rank one.

Factor A=h c rᵗ, where h is homogeneous and c,r are primitive homogeneous polynomial column vectors. Here primitive means the gcd of the nonzero entries is one. This factorization follows directly from unique factorization: take a nonzero column of A and divide by its homogeneous gcd to get c. Every other column is a rational multiple of c; primitivity forces the multiplier to be a polynomial. Remove the common gcd h of these polynomial multipliers to get r. Consequently

    deg h + deg c + deg r = 2.

The identities NA=AN=0 give Nc=0 and rᵗN=0. Generically the unique kernel line of N, hence of M, is Cc(a). Therefore X is generically the graph of [a]↦[c(a)]. Dominance of the second projection implies deg c≥1. If deg r=0, rᵗN=0 is a nonzero constant linear dependence of the three chosen bilinear equations, impossible. Thus deg r≥1. It follows that deg c=deg r=1 and deg h=0.

The linear map c:U→W is surjective because its projective image is dense in P(W), hence is an isomorphism T. The graph of its projectivization is closed, so X equals that graph. This argument does not assume that planar images alone automatically give a linear graph: the five-dimensional product-span bound supplies the essential three equations.

## 2. Exact span-loss criterion and normal form

For an arbitrary isomorphism T:U→W define

    F:Sym²U→Sym²E,   F(ab)=(aT(b)+bT(a))/2.

Its image is the vector span of aT(a). Embed Sym²U into U⊗U by symmetric tensors and apply id⊗T. The kernel of μ on U⊗W is Λ²H, so dim ker F≤1. In particular dim im F≥5.

A nonzero kernel exists exactly when the inverse image under id⊗T of a generator x⊗y−y⊗x of Λ²H is symmetric. This inverse image is

    Q=x⊗T⁻¹(y)−y⊗T⁻¹(x).

Its first-factor support is H, and its second-factor support is T⁻¹(H); both have dimension two. A symmetric tensor has equal first- and second-factor supports. Hence Q symmetric forces T(H)=H. Conversely, with A=T|H invertible and J=[[0,1],[-1,0]], the matrix of Q is J(A⁻¹)ᵗ. It is symmetric exactly when tr(A⁻¹)=0, equivalently tr(A)=0.

Thus

    dim span{aT(a)}≤5 ⇔ T(H)=H and tr(T|H)=0,

and equality is always five. Since A is invertible and trace zero over C, its eigenvalues are λ and −λ, with λ≠0. Rescale T by λ⁻¹, choose eigenvectors x,y∈H, choose z∈U\H, and set w=T(z). Then x,y,z,w form a basis of E and

    U=<x,y,z>, W=<x,y,w>, Tx=x, Ty=−y, Tz=w.

The product span is exactly

    K₀=<x²,y²,xw+xz,yw−yz,zw>.

These five forms are linearly independent. In the theorem K'=K=K₀ if dim K=5; no smaller K can contain this surface. This space has full support automatically.

## 3. Dense compatibility forces a forbidden square

The identity

    v(aT(a)) ∧ a ∧ T(a)=0

is polynomial in a and holds densely; hence it holds identically. At every a for which a and T(a) are independent it is exactly compatibility, so it applies on the special curves below without assuming they meet the initially specified dense open set.

For a=x+s y with s≠0, the product is x²−s²y² and its support is <x,y>. Passing to s=0 gives v(x²)∈<x,y>.

For a=x+t z with t≠0, the factors are x+t z and x+t w. Their support plane is

    <x+(t/2)(z+w), z−w>,

with limit <x,z−w> as t→0. Thus v(x²)∈<x,z−w>. Intersecting these two limiting planes gives v(x²)∈Cx, contradicting square avoidance. The same conclusion holds for y² by exchanging the roles of the eigenvectors.

## 4. General square-contact criterion

The mechanism applies beyond linear graphs. Suppose an ordered-factor variety passes through a diagonal point ([e],[e]) and dense compatibility holds. Choose local lifts a,b with a=b=e at that point. On its tangent space consider

    D=db−da modulo Ce.

This is independent of changing the local scalar lifts. Differentiating the polynomial identity v(ab)∧a∧b=0 at the diagonal gives

    v(e²) ∧ e ∧ D(ξ)=0

for every tangent vector ξ. If im D has dimension at least two in E/Ce, these equations force v(e²)∈Ce. Thus square avoidance requires rank D≤1 at every such diagonal contact where the product family is defined. In the normal form, at x the y and z directions give −2y and w−z, so rank D=2.

This provides a concrete next test for remaining nonlinear factor surfaces: prove the existence of a diagonal contact with two independent first-order factor differences. It does not establish that such a contact exists in general.

## 5. Coincident planes and the remaining frontier

Assume now dim K=5 and K has full support E. If the two factor images are the same plane P(U), then K'=span(S)⊂Sym²U and 3≤dim K'≤5.

- If dim K'=5, then K'=K, contradicting full support.
- If dim K'=4, apply the abstract square-avoiding ternary-web theorem in /research/hm/normalizer-rank-five/rank-six-cubic-web/REDUCIBLE.md, Result and scope: for any linear v:K'→E with no compatible nonzero square, the compatible rank-two locus has dimension at most one. This theorem allows v to take values in the larger four-dimensional E and does not require K' to be the whole residual kernel. It therefore excludes S.
- If dim K'=3, S is dense in P(K'), so every tensor in K' has rank at most two. By /research/hm/normalizer-rank-five/extremal-kernel-planes/PROOF.md, Section 2, K' is a binary plane Sym²B (dim B=2), or a common-factor plane eU. Both contradict square avoidance. In the binary case compatibility implies v(K')⊂B; the homogeneous binary cubic e∧v(e²) has a nonzero projective root over C. In the common-factor case the two paths e(e+t f), e(e+t g), with e,f,g a basis of U, force v(e²)∈<e,f>∩<e,g>=Ce. These arguments are also recorded in /research/hm/normalizer-rank-five/rank-six-cubic-web/REDUCIBLE.md, Section 1.

Thus both planar factor images are impossible, whether distinct or coincident. Together with the completed point/curve factor reductions in ../nonlinear-curve-factor-exclusion/PROOF.md, any remaining moving-middle full-support rank-five compatible surface case must have both ordered factor projections of dimension two, with at least one image a NONPLANAR surface in P(E). In particular, one planar and one nonplanar image remains outside this proof.

## 6. Scope

The new structural theorem excludes distinct planar factor images under the stated product-span bound and square avoidance. The coincident-plane case is excluded in Section 5 using prior ternary-web and bounded-rank-plane results when K has dimension five and full support. Cases with a nonplanar surface image remain unclassified. No conclusion about all moving-middle components or a completed global theorem follows here.
