# A one-dimensional quartic defect cannot obstruct differential descent

## Conclusion

The generic marked integral ACM heptic alternative is impossible.

The new observation is not an equality of quartic ideals. The established exact dimensions are h0(I_Z(4))=12 and h0(I_D(4))=11. Nevertheless the exact Koszul identities force every fixed-point differential quartic of every cubic generator to lie in I_D(4). Thus the one-dimensional extra-quartic quotient carries no differential obstruction. Differential descent then produces an invariant degree-seven surface, impossible by Heisenberg degree divisibility.

This excludes the heptic branch without any assumption on the residual degree-three divisor, the canonical point P, normalization genus, Gorensteinness, or smoothness away from Z.

## 1. Setup and the exact quotient

Let T be a dense open of dual P4 parametrizing general hyperplanes H_t. The intrinsic full cubic-base family D_t⊂H_t is geometrically integral of degree seven and arithmetic genus five, contains the 25 reduced marked points Z_t=C∩H_t, and has resolution

    0→O(-4)⊕O(-5)→3O(-3)→I_Dt→0.

It is nondegenerate in H_t=P3. The entire cubic kernel V_t=H0(I_Zt(3)) equals H0(I_Dt(3)) and has dimension three.

The proved unique-extra-quartic result gives

    dim H0(I_Zt(4))/H0(I_Dt(4))=1.                 (1)

Choose a quartic q_t representing a nonzero quotient class. Its restriction to integral D_t is nonzero. Indeed membership in I_Dt is exactly vanishing on that curve. No basepoint-freeness, choice of a smooth zero divisor, or nonvanishing at particular marked points is required.

All families and ranks can be made algebraic on a dense open: normalize a nonzero kernel coordinate for the cubic basis, and choose a local lift of the rank-one quartic quotient after shrinking. Alternatively the next argument can be performed at the generic parameter over its function field, which avoids any need for a global choice of q_t.

## 1.1. Proof that the quartic quotient is exactly one-dimensional

For completeness, the extra-quartic nonvanishing and upper bound are pinned at f9a4ba6633f1a2402d8d729ade30b1197a548d05. Put H=O_D(1), M=O_D(4)(-Z); then deg M=3 and 1<=h0(M)<=2. ACM gives h0(H)=4 and I_D(2)=0. The line bundle H tensor M has degree10, larger than deg omega_D=8, so duality and Riemann–Roch give h0(H tensor M)=6. This uses rank-one torsion-free duality, not Gorensteinness.

If s,t were independent sections of M, multiplication H0(H)^2 -> H0(H tensor M), (a,b) -> as+bt, would have a kernel of dimension at least2. Choose independent kernel pairs (a,b),(c,d). The first projection of that kernel is injective, because t is nonzero at the generic point of integral D; hence a,c are independent ambient linear forms. The two equations imply ad-bc=0 on D. This is a nonzero ambient quadric: if ad-bc were identically zero as a polynomial, coprimality of a,c would force b=lambda a and d=lambda c, whence s+lambda t=0, a contradiction. Thus two sections would contradict I_D(2)=0.

Therefore h0(M)=1. The ACM exact restriction sequence gives h0(I_Z(4))-h0(I_D(4))=h0(M)=1. This proves (1) even if a hypothetical pencil had singular base points; no basepoint-free assumption is needed.

## 2. Fixed-point differential quartics lie in I_Z

On an affine hyperplane chart write

    H_t: X4=Σ_(i=0)^3 t_i X_i.

Use x=[X0:X1:X2:X3] on H_t and choose an algebraic local basis f_a(t,x), a=1,2,3, of V_t. For a fixed cubic f=f_a define

    F_ij=x_i ∂_(t_j)f−x_j ∂_(t_i)f,   i,j∈{0,1,2,3}.

Each F_ij is homogeneous quartic in x. At any marked point p=H_t∩L, a parameter tangent v with Σv_i x_i(p)=0 keeps p fixed to first order, since the fixed line L meets H_t transversely. Differentiating f(t,p(t))=0 implies that the parameter gradient (∂_(t_i)f)(p) is proportional to x(p). Therefore F_ij vanishes at all marked points, and

    F_ij∈H0(I_Zt(4)).

By (1), for fixed t and f there are scalars c_ij (antisymmetric in i,j) with

    F_ij ≡ c_ij q_t  modulo I_Dt(4).             (2)

The coefficients are scalars with respect to x, not linear or rational functions on D_t. This follows because (1) is a one-dimensional vector-space quotient in the same homogeneous degree.

## 3. Koszul compatibility kills every coefficient

For any three distinct indices i,j,k, expansion gives the exact polynomial identity

    x_i F_jk − x_j F_ik + x_k F_ij = 0.          (3)

Indeed each term x_i x_j ∂_(t_k)f cancels with its opposite. Reducing (3) modulo I_Dt and using (2) gives

    (c_jk x_i − c_ik x_j + c_ij x_k) q_t = 0

in the homogeneous coordinate ring of D_t. This ring is an integral domain, and q_t is nonzero in it. Hence

    c_jk x_i − c_ik x_j + c_ij x_k = 0 on D_t.

Nondegeneracy of D_t means no nonzero ambient linear form vanishes on it. Since x_i,x_j,x_k are independent coordinate linear forms, each of c_jk,c_ik,c_ij is zero. Every pair of distinct indices belongs to some triple, so all c_ij vanish.

This applies separately to each cubic generator f_a. Consequently

    x_i ∂_(t_j)f_a−x_j ∂_(t_i)f_a ∈ I_Dt(4)

for every a,i,j at the generic parameter. Notice the logic: the extra-quartic quotient is genuinely nonzero, but its possible classes violate the exact compatibility identity unless all differential classes are zero.

## 4. Descent of the curve incidence to a surface

Let 𝒟 be the reduced irreducible total curve family over a suitable dense T. Its dimension is 4+1=5. The saturated homogeneous ideal of each D_t is generated by its three cubics, so Section 3 asserts that the fixed-point differential derivations preserve its generic family ideal.

More explicitly, on the chart x0=1 put

    δ_j=∂_(t_j)−x_j ∂_(t_0),   j=1,2,3.

These three derivations annihilate the ambient coordinates of the point

    [1:x1:x2:x3:t0+t1x1+t2x2+t3x3].

Their values on each f_a are F_0j, which vanish on the total family at its generic point by Section 3. Thus the δ_j are three independent tangent vectors to 𝒟, and all lie in the differential kernel of ambient evaluation π:𝒟→P4. Characteristic zero gives generic image dimension at most 5−3=2.

Conversely, for a fixed ambient point, hyperplanes containing it form P3, and the original curve incidence has at most one point for each pair (ambient point, hyperplane). Hence fibers of π have dimension at most three. Therefore the image has dimension at least two.

Its reduced closure S is thus an integral surface. Let I_S be the full point/hyperplane incidence over S. It is an irreducible projective-three bundle over S and has dimension five. The closure of 𝒟 in projective incidence is contained in I_S and has the same dimension. Therefore it equals I_S as a reduced closed set.

For general H, the reduced support of S∩H is consequently D_H. A general hyperplane section of an integral surface in characteristic zero is generically reduced; its cycle has multiplicity one along this integral support. Thus

    deg S=deg D_H=7.

This degree assertion needs no global normality or Cohen–Macaulayness of S; any isolated non-Cohen–Macaulay phenomenon does not change the generic hyperplane-section cycle.

## 5. Heisenberg divisibility contradicts degree seven

The full cubic kernel, its entire base D_H, and ambient evaluation are intrinsic to the actual invariant line configuration C. Therefore S is invariant under the projective Heisenberg group. Replace T by the intersection of its finitely many translates if an invariant base open is desired.

For an invariant integral surface, its degree is divisible by five. Briefly, use the linear order-125 Heisenberg lift. In every sufficiently large degree m not divisible by five, its center acts nontrivially on H0(O_S(m)), so this representation has dimension divisible by five. Twice the Hilbert polynomial is an integer-coefficient quadratic polynomial; modulo five it vanishes on all four nonzero residue classes. It must be identically zero over F5, and its leading coefficient deg S is divisible by five.

This contradicts deg S=7. The generic heptic alternative is therefore excluded.

## Dependency boundary

The argument uses the marked-heptic resolution and integrality, the independent proof that h0(O_D(4)(−Z))=1, and the established Heisenberg action. It does not replace the exact one-dimensional quartic defect by an erroneous zero-defect assertion.

Source inputs:

- THREE-CUBIC-SEXTIC-HEPTIC-DICHOTOMY.md, commit 435a20fc680c7ccecc3cbfd762a3d5ae97b76299.
- HEPTIC-EXTRA-QUARTIC-NECESSITY.md, f9a4ba6633f1a2402d8d729ade30b1197a548d05: nonzero quartic defect and the initial fixed-point derivative method.
- Section 1.1 above supplies the basepoint-independent multiplication-syzygy proof of the exact defect dimension, so no unpublished lemma is required.

The proof excludes the marked heptic. Deductions about all of b=3 additionally require the separately established exclusions of its finite-base and integral-sextic alternatives. No claim about b≤2 or full Q4 is made here. No selected source coefficients, evaluations, numerical ranks, scans, experiments, or external writes were used.
