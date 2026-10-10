# Executed scalar comparison on the legal line refinement

## Result and boundary of the certificate

The dependency-free executable verify-scalar-refinement.js was executed with 552 exact assertions. It constructs an actual scalar cochain map from a specified finite domain on the legal line refinement to an original-cover Laurent domain. It checks the double-Čech correction producing that map, its chain identity, the scalar Laurent contraction, and tensor-complex identities. The resulting compensated first-order coordinates for both N and N^-1 are

-4(q₁q₂+q₃q₄)=16Π.

This is the scalar line-atlas calibration, not the six-carrier HM comparison. The E residual, first-order E primitive and second-order obstruction are not computed here. In particular, this certificate must not be described as an implemented comparison for arbitrary refined rational matrices.

## Covers, rings and one common denominator choice

Write A=C\{∞} and let B be the inverse image of the original 1/x chart. On B set

t=1/x, z=y/x², s=1−t², z²=ts.

The legal line cover is V₀=A and V₁=D(s)⊂B. On B its induced refinement is D(t),D(s). On A and A∩B, the V₀ member already covers the entire intersection.

All expressions used below lie in the common localization R[t^-1,s^-1], where R=Q[t,z]/(z²−t+t³). Their pole orders in t and s are at most one. Multiplication by the fixed weights only increases numerator degrees. Use the single Bézout identity

t·t+s=1

throughout. Thus the two denominator-clearing weights are t² and s; these are a_i f_i^N with f₀=t, f₁=s, N=1, a₀=t, a₁=1. No weights are recomputed separately for individual cochains.

Set

q=z/t=y/x,
c=tz/s=1/y,
w=tz=y/x³,
r=V(log q).

The exact identities checked after cross multiplication are

2r=q+2c,
sq=q−w,
sc=w,
s(2r)=q+w.

The zero-cochain k=(0,c) is legal because c is regular on V₁. Its differential is c. On the original cover, ell=(0,w) is legal because w is regular on B; its differential is w.

## Local contractions and the missing horizontal correction

For an additive vertical Čech one-cochain u, use

h_A(u)=(0,u),
h_B(u)=(−su,t²u).

The corresponding projections on vertical degree zero are

p_A(a,b)=a,
p_B(a,b)=t²a+sb.

They satisfy d_v h=1 in degree one and h d_v+i p=1 in degree zero. Also p h=0 and h i=0. Every asserted identity is an equality of rational functions on the indicated intersections. The identities are checked for q,c,2r, and hence linearly on their span.

Use the double Čech complex, with original degree horizontal and refinement degree vertical, and total differential d_v+(-1)^vertical d_h. The original restriction maps give the horizontal perturbation δ.

The natural augmentation of a refined one-cocycle has vertical-degree-one restrictions to A and B. Its uncorrected projection p is zero. The horizontal difference of its local homotopies is

h_B(u)−h_A(u)=(−su,−su),

a diagonal vertical-degree-zero cochain on A∩B. Therefore the HPL projection

P'=p(1+δh)^-1=p−pδh

sends that refined cocycle to su on the original overlap. There are no longer terms: the original two-chart complex has horizontal degree at most one.

The nonzero term −pδh is essential. Omitting it sends this input to zero.

For a refined zero-cochain (a,b), the same corrected map is

P₀(a,b)=(a,t²a+sb).

For a one-cochain u it is P₁(u)=su. Thus directly

d P₀(a,b)=s(b−a)=P₁ d(a,b).

These formulas are applied only where the displayed denominator-clearing bounds hold.

The finite double-complex domain is the linear span of the augmented input generators below, their restrictions, and their images under d_v,d_h,h,i p and the single correction pδh. These operations terminate in horizontal degrees zero and one and vertical degrees zero and one. In particular h is zero on vertical degree zero and h i=0. The displayed q,c and their s/t² multiples list the only nonconstant rational functions needed by the nonzero vertical homotopies. The common localization and exponent bound above apply to every one of them. This finite operation domain is not an assertion that repeated multiplication by s preserves a finite Laurent cutoff.

## Explicit finite matrices and Laurent projection

Take the refined input complex

degree zero: span{1,k},
degree one: span{q,c},
d(k)=c, d(1)=0.

Here 1 means the diagonal constant section. The original output complex is

degree zero: span{1,ell},
degree one: span{q,w},
d(ell)=w, d(1)=0.

These are actual subcomplexes of the corresponding scalar Čech complexes. The comparison matrices, with columns representing images of basis vectors, are

P₀=identity,
P₁=((1,0),(-1,1)).

Thus P₁q=q−w, P₁c=w, and P₁(2r)=q+w. The executable checks dP=Pd exactly.

In the original Laurent model, q=y x^-1 is the sole odd H¹ basis element for O(-2), while w=y x^-3 belongs to the infinity-chart component. The original finite Laurent contraction keeps 1 and q, kills ell and w, and sends w to ell. Its two contraction identities are checked.

Consequently the composed projection sends q↦q, c↦0, r↦q/2. This composition is also the small refined SDR with homotopy c↦k.

## Four factors and sign calibration

Tensor the scalar complexes in factor order 1,2,3,4, with the usual Koszul differential. The executable checks d²=0 and that the scalar harmonic projection is a chain map on all 256 tensor basis vectors.

In tensor Čech normalization the independent odd classes anticommute strictly. The left-row scalar first-order Moyal defect for the pair (i,j) is represented by −r_i r_j. Its projection is therefore −q_iq_j/4. Subtracting the gerbe cocycle 15q_iq_j/4 gives −4q_iq_j. Negating both logarithmic derivatives for N^-1 leaves the result unchanged.

The short tensor representative and an ordinary-nerve Alexander–Whitney representative must not be silently identified as cochains. The separate verify-line-calibration.js certificate gives the exact ordinary-nerve coboundary: if r_i=q_i/2+δc_i, then

μ_ij+q_i∪q_j/4=−δh_ij,

with h_ij=c_i∪r_j−q_i∪c_j/2 plus the pointwise edge cochain r_i r_j/2. This supplies the ordinary-nerve sign calibration; the present certificate implements the scalar tensor comparison and projection.

## Remaining work

To apply the same machinery to the HM residual, specify the principal opens from the six carrier pivots, their actual Bézout identities on every original affine intersection, a common domain containing the matrix residual and all correction terms, and the full matrix-valued double-Čech map. The scalar result here supplies a tested calibration target and a working instance of the horizontal correction; it does not supply those missing carrier data.
