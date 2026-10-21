# Two-dimensional defects cannot carry compatible fixed-point derivatives

## Abstract statement

Let D⊂P3 be an integral nondegenerate curve with H0(I_D(2))=0. Write H=O_D(1), let V be the four-dimensional space of restricted ambient linear forms with coordinate basis x0,x1,x2,x3, and let M be a rank-one torsion-free sheaf on D (a line bundle suffices).

Let W⊂H0(M) be a vector subspace of dimension at most two. Suppose antisymmetric elements F_ij∈W satisfy

    x_i F_jk − x_j F_ik + x_k F_ij = 0

in H0(H⊗M), for every three distinct indices i,j,k. Then every F_ij is zero.

The theorem is independent of the degree or genus of D and of the degree of M. It applies even when the chosen sections have base points, including singular base points, and does not require that V=H0(H). It uses no evaluated matrix or selected numerical rank.

## 1. At most one linear relation between two independent sections

Let q,r∈H0(M) be independent. Consider

    R = {(a,b)∈V⊕V : a q+b r=0}.

We prove dim R≤1. Both coordinate projections R→V are injective: if a=0, then b r=0, and nonzero r at the generic point of integral D forces b=0; the other projection is identical.

If R contained two independent pairs (a,b),(c,d), then a,c would be independent in V, as would b,d. At the generic point, the two relations force ad−bc=0. Thus the corresponding quadratic polynomial vanishes on D. Since H0(I_D(2))=0, this is an identity in the ambient polynomial ring Sym(V).

The independent nonzero linear polynomials a,c are coprime. The identity ad=bc therefore forces a to divide b, so b=λa for a scalar λ; substituting back gives d=λc. Then a(q+λr)=0 on integral D implies q+λr=0, contradiction.

Therefore dim R≤1. The argument uses only torsion-freeness of M and integrality of D to pass to its generic point, and the absence of ambient quadrics to pass back to a polynomial identity.

## 2. A nonzero constant two-form produces at least two independent coefficient forms

Let c_ij=−c_ji be scalar coefficients, not all zero. For each triple define the ambient linear form

    A_ijk = c_jk x_i − c_ik x_j + c_ij x_k.

Their span has dimension at least two. Indeed choose a pair i,j with c_ij≠0, and let k,l be the two remaining indices. Modulo the two-dimensional subspace span{x_i,x_j}, the forms A_ijk and A_ijl become c_ij x_k and c_ij x_l respectively. They are independent because the coordinate basis is independent.

This is a universal exterior-algebra observation, not an instance-specific rank calculation. In invariant terms, a nonzero constant two-form cannot have a one-dimensional image under the corresponding Koszul coefficient map in four variables.

## 3. Proof for defect dimension two

If dim W=2, choose its basis q,r and write

    F_ij = c_ij q+d_ij r

with scalar antisymmetric coefficient arrays c,d. The compatibility identity becomes

    A_ijk q+B_ijk r=0,

where A_ijk is formed from c as in Section 2 and B_ijk is formed from d. Hence every pair (A_ijk,B_ijk) belongs to the relation space R from Section 1, which has dimension at most one.

Its first-coordinate image consequently has dimension at most one. But if c were nonzero, Section 2 would make the span of its A_ijk at least two-dimensional. This contradiction forces c=0. Applying the same reasoning to the second projection forces d=0. Therefore F_ij=0 for every pair.

If dim W=1 with generator q, the compatibility identities give A_ijk q=0. Torsion-freeness and nonzero q imply A_ijk=0 on D. Nondegeneracy makes A_ijk the zero ambient linear form, and hence all c_ij=0. Dimension zero is immediate. This proves the theorem.

## 4. Application to quartic defects of a moving cubic-base carrier

Suppose a canonical algebraic family of integral nondegenerate curves D_t⊂H_t=P3 contains the reduced marked points Z_t=C∩H_t, with each marked point smooth on D_t, and the full cubic space through Z_t is contained in I_Dt(3). Assume H0(I_Dt(2))=0 and

    dim image[H0(I_Zt(4))→H0(O_Dt(4)(−Z_t))] ≤2.     (*)

The stronger condition h0(O_Dt(4)(−Z_t))≤2 suffices. No surjectivity of this restriction map or ACM assumption is needed.

Choose affine hyperplane coordinates H_t:{X4=Σt_i X_i}, and local algebraic cubic equations f_a(t,x) generating the carrier ideal near its generic smooth point. Their fixed-point derivatives

    G^a_ij=x_i ∂_(t_j)f_a−x_j ∂_(t_i)f_a

vanish on Z_t, by differentiating the marked intersections with the fixed lines. Their restrictions to D_t therefore lie in the image W_t in (*), after dividing out the common Cartier divisor Z_t. The exact polynomial identity

    x_i G^a_jk−x_j G^a_ik+x_k G^a_ij=0

survives this division and gives the hypothesis of the abstract theorem for each a. Consequently every G^a_ij restricts to zero on D_t.

Thus the fixed-point derivations δ_j=∂_(t_j)−x_j∂_(t_0), on a chart x0=1 after choosing and relabeling a coordinate nonzero at the generic point, annihilate the carrier equations modulo its ideal at the generic point. Where the chosen cubic equations generate its ideal generically, they are tangent to the five-dimensional curve incidence family. They are independent and fix the ambient point, so ambient evaluation has image dimension at most two. Its fibers lie in the three-dimensional space of hyperplanes through a point, forcing image dimension exactly two.

If the family is intrinsic and Heisenberg-equivariant, its reduced image closure is an invariant integral surface S. Equality of the five-dimensional curve incidence with the full incidence over S gives a general hyperplane section with reduced support D_t and generic multiplicity one. Thus deg S=deg D_t. Heisenberg divisibility forces 5|deg D_t. In particular a degree-seven family with (*) cannot occur.

The generic-generation proviso matters: merely knowing that some cubics contain a carrier does not by itself prove that annihilating those cubics makes the derivations tangent to its chosen component if their scheme has a generic thickening. The abstract theorem and the conclusion that all differential quartics vanish on D_t hold without this proviso; the descent application requires generic reducedness or another proof of tangency. For a reduced complete-intersection cubic base or the ACM heptic ideal generated by its cubics, the proviso holds directly. It also holds for any integral degree-seven component of the complete intersection of two coprime cubics: total degree nine forbids generic multiplicity at least two on a degree-seven component. Hence that component is generically reduced, and the two cubics generate its ideal near its generic point, after avoiding other components. This is the relevant b=2 degree count.

## 5. Numerical heptic corollary

For an integral degree-seven curve with arithmetic genus g=3 or 4, the line bundle M=O_D(4)(−Z) has degree three. In both cases h0(M)≤2, without assuming Gorensteinness. Let a=h0(M), b=h1(M)=dim Hom(M,ω_D). Riemann–Roch gives a−b=4−g. If b=0, a≤1. If b>0 and a>0, the multiplication pairing into H0(ω_D) has no zero divisors. The Hopf dimension inequality gives a+b−1≤g. Substituting b=a+g−4 yields 2a−5≤0, hence a≤2. If a=0 the conclusion is immediate.

Therefore any such moving marked heptic with no quadric satisfies (*). Once generic reducedness/tangency of its cubic-base component has been supplied, Section 4 excludes the family by degree-seven surface descent. This gives the requested conditional interface to the separate b=2 carrier geometry, without silently assuming that geometry is already proved.

## Scope

The new theorem extends the one-dimensional-defect Koszul cancellation to every defect of dimension at most two. Its two independent ingredients are the no-quadric linear-relation bound and the universal two-form coefficient lemma. No actual HM/source coefficients, selected evaluations, numerical ranks, scans, local-model experiments, or external writes were used. It does not claim an unconditional exclusion of every b=2 configuration without the carrier and generic-tangency hypotheses.

## 6. Actual two-cubic heptic exclusion

TWO-CUBIC-CARRIER-CLASSIFICATION.md at e0d0c123934f06cb63937225881a83e5e5906cfb supplies every geometric hypothesis in the actual generic b=2 degree-seven alternative: a canonical integral nondegenerate carrier with no quadric, genus three or four, all 25 marked points smooth, and generic multiplicity one in its (3,3) cubic base. Section 5 supplies the small-defect bound and Section 4 then gives the contradiction. Thus that actual degree-seven alternative is excluded, not merely conditionally restated. Together with the degree-six exclusion in the classification note, a surviving generic b=2 carrier is either the ACM degree-eight genus-seven curve or the integral (3,3) degree-nine genus-ten curve. Neither of those alternatives, b=1, b=0, nor full Q4 is settled here.
