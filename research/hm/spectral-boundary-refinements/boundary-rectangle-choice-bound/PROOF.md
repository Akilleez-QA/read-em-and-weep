# Fixed-polar boundary rectangles: zero, one, or three choices

## Assumptions and conclusion

Over C, let dim V=5 and let J be a complex vector space and let f:V³→J be a trilinear map that is outer symmetric, cyclic zero, and globally repeated-input injective: A_w:V/Cw→J, [z]↦f(w,w,z), is injective for every nonzero w. Fix independent nonzero h,u for which P=f(h,u,-) has rank two. Put

    L=C f(h,u,h),     H=P^(-1)(L),     E=H/Ch,     K=J/L.

Then dim H=4, u∉H, and dim E=3. Consider ordered rectangular pairs (X,Y), with dim X=2, dim Y=3, X∩Y=Ch, X+Y=H, and dim f(X,u,Y)≤1.

The number of such pairs is exactly one of 0, 1, or 3. In particular it is at most three. This is a set-theoretic statement; no reducedness claim is made. It does not claim that each of the three cardinalities is realized by an original tensor f.

The proof is independent of global finiteness of the rectangular incidence or the polar-pair locus.

## 1. The induced vector-valued quadratic has no projective zero

The established two-polar-value independence gives that f(h,u,h)=-2A_h(u) and f(h,u,u)=A_u(h) are independent. Thus L is a line, H is four-dimensional, h∈H and u∉H.

Since P(H)⊂L and f is outer symmetric, the symmetric bilinear map f(-,u,-) on H descends modulo L to

    β:E×E→K.

Claim: β(e,e)≠0 for every nonzero e∈E.

If not, choose a lift v∈H of e. Then h,v are independent. The three vectors f(h,u,h), f(h,u,v), f(v,u,v) all lie in L. Consequently f(w,u,w), for w in the two-plane S=span(h,v), is an L-valued binary quadratic form. Its value at h is nonzero, so it is a nonzero quadratic. Over C it has a nontrivial zero w∈S. But w∈H and u∉H, so w,u are independent, whereas

    0=f(w,u,w)=-2A_w(u),

contradicting repeated-input injection. This proves the claim.

## 2. A nondegenerate scalar member exists

For λ∈K*, write q_λ(v,w)=λ(β(v,w)). Choose a scalar member q₀ of maximal rank r in this linear system. Suppose r<3. Choose nonzero k∈rad(q₀) and an r-dimensional subspace W on which q₀ is nondegenerate. For any other scalar member q₁, the restriction of q₀+tq₁ to W⊕Ck has determinant identically zero as a polynomial in t, because every member of the linear system has rank at most r. In a basis of W followed by k, the coefficient of t in this determinant is

    det(q₀|W) q₁(k,k).

Thus q₁(k,k)=0 for every scalar member q₁, contradicting β(k,k)≠0 from Section 1. (For r=0, take W=0 and the same argument is the one-by-one determinant.) Therefore r=3. Fix a nondegenerate member q=λ₀β.

This maximal-rank argument is elementary and uses no Bertini theorem or incidence finiteness.

## 3. Exact common-eigenline description

For each λ∈K*, define T_λ∈End(E) uniquely by

    q(T_λ v,w)=λ(β(v,w)).

Each T_λ is q-selfadjoint. No commutativity or simultaneous diagonalizability is assumed.

The quotient map H→E gives a bijection between the rectangular pairs in the theorem and splittings

    E=a⊕B,    dim a=1, dim B=2,    β(a,B)=0.

Indeed X and Y are the inverse images of a and B. Their mixed f-values are then in L, and the image contains f(h,u,h)≠0, so it is exactly L.

For any such splitting, q(a,B)=0. Nondegeneracy of q implies B=a^⊥ and q|a≠0; otherwise a⊂a^⊥=B. The equations β(a,B)=0 then say exactly that T_λ a⊂a for every λ. Thus every rectangle determines a common eigenline.

Conversely let a=Cv be a common eigenline, so T_λv=μ_λv for every λ. If q(v,v)=0, then λ(β(v,v))=μ_λq(v,v)=0 for all λ, contradicting Section 1. Hence a is nonisotropic, E=a⊕a^⊥, and all scalar coordinates of β(a,a^⊥) vanish. This gives a rectangle.

Therefore the rectangles are in bijection with all common eigenlines of the q-selfadjoint family {T_λ}. Every common eigenline is nonisotropic.

## 4. At most three; two force a third

Take distinct common eigenlines Cv,Cw with respective eigenvalue functionals μ,ν on K*. If μ=ν, all vectors z∈span(v,w) are common eigenvectors with that same eigenvalue functional, and

    λ(β(z,z))=μ_λ q(z,z)  for every λ.

Every complex quadratic form on a two-dimensional vector space has a nontrivial isotropic vector z. For such z, the displayed identity gives β(z,z)=0, a contradiction. Thus μ≠ν. Selfadjointness gives

    (μ_λ−ν_λ)q(v,w)=0

for every λ, so q(v,w)=0. All distinct common eigenlines are therefore pairwise orthogonal and nonisotropic. They are linearly independent, proving the bound three.

If two common eigenlines exist, their sum S is nondegenerate. Its orthogonal complement S^⊥ is one-dimensional and invariant under every T_λ: for z∈S^⊥ and s∈S, q(T_λz,s)=q(z,T_λs)=0. It is therefore a third common eigenline. Exactly two is impossible, proving the asserted 0, 1, or 3 alternatives.

## 5. Structure in the three-choice case

If there are three choices, write E=a₁⊕a₂⊕a₃ and choose nonzero v_i∈a_i. Then β(v_i,v_j)=0 for i≠j. The three vectors c_i=β(v_i,v_i) in K are linearly independent. Otherwise choose a nonzero relation Σt_i c_i=0 and complex square roots s_i²=t_i. The nonzero vector Σs_i v_i would have β(Σs_i v_i,Σs_i v_i)=0, contradicting Section 1.

Thus in this case β is a diagonal vector-valued quadratic with three independent diagonal coefficients. The three rectangles are exactly the three choices of one coordinate line against the sum of the other two.

## Scope

All conclusions follow solely from the original tensor hypotheses and the fixed rank-two polar. No numeric or physical instance, global finiteness assumption, target dimension restriction, or residual-kernel classification is used. The proof is about actual points, not scheme multiplicities.

## Global point-count consequence

Let D be the finite polar-pair support of https://github.com/Akilleez-QA/read-em-and-weep/blob/7f62d4535d0bfca8b2be93b0b4068cfd06fec717/research/hm/middle-surface/extremal-surface-geometry/PROOF.md, and R_boundary the noncomplementary rectangular support. Every boundary triple has a unique intersection line Ch and middle Cu, hence a unique pair in D. The preceding classification bounds each fiber by three. Therefore

    #R_boundary <= 3 #D.

This counts complex geometric points, not scheme lengths. Together with complementary-triple finiteness, it supplies a quantitative refinement of full rectangular-incidence finiteness.
