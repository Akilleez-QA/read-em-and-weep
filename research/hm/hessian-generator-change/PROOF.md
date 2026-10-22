# Universal generator-change defect and a lift-choice repair

## Scope and source

This is a universal polynomial calculation over characteristic zero, relative to fixed binary coordinates a,b. It uses the Hessian first-normal formula in PR543 at ba4dece8c6f99ea5a7601185c5d341012495e3f6, `research/hm/order-four-quadratic-load/UNIVERSAL-HESSIAN-CORRECTION-FOR-FIRST-NORMAL-NILPOTENCE.md` (blob ff3b30cbdcd4ca44d51b990b791ca26bb17df66d). PR543 was read at its subsequent head 30b46085e31aade78c5b6f3248abe307426ddf03 and PR1 recent coordination comments were read before this derivation; the subsequent note concerns Serre-involution eigensplitting, not this calculation.

No selected HM coefficients or fibers are used. The calculation does not identify a local lift with the actual midpoint, prove global gluing, or evaluate the positive cubic Bockstein.

## Conventions

Let f,g,h have binary degrees 3,5,2. Put R=ℂ[x,y,z], q=xz-y^2, and identify R/(q) with the even binary subring by (x,y,z)=(a^2,ab,b^2). Let C be the symmetric matrix with rows (x,y),(y,z). Write F=grad(f)/3 and G=grad(g)/5, using even lifts to R. The lift F is unique by degree. The lift of G is not unique. Put u=F^t C F, v=F^t C G, w=G^t C G and

N0=[[v,-u],[w,-v]],
T=[[mix(H_f,H_g)/240,-det(H_f)/36],[det(H_g)/400,-mix(H_f,H_g)/240]].

All entries of T need only be specified modulo q. Then N=N0+qT is square-zero modulo q^2. Here mix(U,V)=U11 V22+U22 V11-2 U12 V12.

For the change g'=g+hf, set P=[[1,0],[h,1]], so on the cone N(f,g')=P N(f,g) P^{-1}.

## Exact transported Euler lift

Put k=J(f,h)/15, where J(f,h)=f_a h_b-f_b h_a. Euler's identities give

G' = G+hF+k(-b,a)

on the binary cover. Write k=aK+bL with the canonical choice K=k_a/3,L=k_b/3. Their even degree-two lifts are unique. The compatible off-cone lift used here is

d=(-yK-zL,xK+yL),   G'_can=G+hF+d.

It is essential to specify this lift. The Hessian recipe alone does not do so.

Direct matrix multiplication gives C d=q(-L,K), hence

v'=v+hu+q alpha,
w'=w+2hv+h^2u+q(2 beta+kappa),

where alpha=-F1 L+F2 K, beta=-(G+hF)1 L+(G+hF)2 K, kappa=(K,L) C (K,L)^t. Modulo q, alpha=-J(f,k)/9 and kappa=k^2.

Consequently D=(N(f,g';G'_can)-P N(f,g;G) P^{-1})/q modulo q has upper-right entry zero and diagonal entry

A=-J(f,J(f,h))/135 + mix(H_f,H_(hf))/240 - h det(H_f)/36.

## Simplified defect

The universal identity is

A=-f mix(H_f,H_h)/144.

One coefficient proof, requiring no specialization, writes f=c0 a^3+c1 a^2 b+c2 ab^2+c3 b^3 and h=d0 a^2+d1 ab+d2 b^2. Expansion of the left side is

-f [a(3c0d2-c1d1+c2d0)+b(c1d2-c2d1+3c3d0)]/36,

where the bracket is mix(H_f,H_h)/4. The companion `verify_generator_change.py` checks this identity with algebraically independent coefficients, not selected examples.

Set gamma=-mix(H_f,H_h)/144. Since both compared lifts square to zero modulo q^2, their difference anticommutes with their common cone restriction N(f,g'). For D=[[f gamma,0],[B,-f gamma]], this says f^2 B=2fg' f gamma. In the universal polynomial domain, cancellation gives B=2g' gamma. Thus, universally,

D=[[f gamma,0],[2g' gamma,-f gamma]].

The formula continues under every specialization because it is a polynomial identity. Coprimality is not needed for the identity itself.

## Regular gauge obstruction

Assume f,g' are coprime in ℂ[a,b]. Allow arbitrary regular polynomial matrices X, not just homogeneous ones. Scalar parts commute, so write X=[[A,B],[C,-A]]. The condition [X,N(f,g')]12=0 is Af+Bg'=0. Coprimality gives A=g't, B=-ft. The diagonal commutator is then f(f C-g'^2 t).

It follows that D=[X,N(f,g')] if and only if

gamma belongs to (f,g'^2).

Sufficiency follows from the same formulas, including the lower-left entry. Thus gamma defines an exact obstruction in ℂ[a,b]/(f,g'^2). If gamma is a nonzero degree-one form, it cannot belong to the homogeneous ideal generated in degrees 3 and 10. In particular the displayed canonical transport is generally not related by a regular first-normal gauge I+qX. Nonexistence over the full binary ring also excludes an even-subring gauge. If gamma=0, the defect itself vanishes. The nonexistence also holds in the local ring ℂ[a,b]_(a,b) and its completion ℂ[[a,b]]. Indeed the coprime pair is a regular sequence, and its syzygy description persists under these flat extensions; the same ideal criterion therefore applies. The ideal (f,g′^2) is contained in (a,b)^3, whereas a nonzero gamma has order one. Thus no regular local or formal first-normal gauge exists at the origin. No assertion for noncoprime specialized pairs is made by this criterion.

## A non-gauge lift-choice repair

Put ell=-gamma=mix(H_f,H_h)/144, a linear binary form. Replace the transported Euler lift by

G'_corr=G'_can+q(ell_a,ell_b).

Changing G' this way changes the first-normal N by

q[[f ell,0],[2g' ell,-f ell]],

because modulo q, F^t C grad(ell)=f ell and G'^t C grad(ell)=g' ell. This cancels D exactly modulo q^2. Therefore

N(f,g';G'_corr)=P N(f,g;G) P^{-1} mod q^2.

Equivalently choose K_new=K+b ell, L_new=L-a ell; they still decompose k, and their lifted d changes by q(ell_a,ell_b). This is not a regular gauge relating the original canonical lift to the corrected lift. It is a change of the input off-cone Euler lift, which the original recipe had left arbitrary.

For fixed f and coordinates, the transport G -> G+hF+d(h)+q grad(ell(h)) is additive in h. Thus composing two such unipotent generator changes gives the same transported Euler lift as their sum. This proves compatibility for this restricted unipotent action in fixed coordinates, not for all actual geometric transition data.

## Scalar cubic changes

For a scalar lambda in the coefficient field, f'=lambda f and g'=g, take F'=lambda F and unchanged G. Direct homogeneity gives

N(lambda f,g)=lambda P_lambda N(f,g) P_lambda^{-1},
P_lambda=diag(lambda,1),

for lambda nonzero. This holds modulo q^2, and in fact entrywise for the chosen formula before truncation. The determinant factor lambda is necessary; this is not ordinary conjugation. The identity also holds for units constant with respect to a,b over a coefficient base. It does not cover coordinate-dependent cubic scalings.

## Contribution and remaining gap

The naive canonical Euler transport has an explicit, usually nonzero regular-gauge obstruction. Nevertheless an explicit change of off-cone lift cancels it and is additive for quintic shear changes in fixed binary coordinates. Thus one cannot infer failure of geometric gluing from the canonical defect, nor infer gluing just from nilpotence. What remains is compatibility with the actual bundle transition data, base/coordinate changes and normal parameter conventions, followed by comparison with the uniquely characterized invariant midpoint. Absolute cubic and higher-order lifting claims remain untouched.

Status: authored universal proof, independently mathematically reviewed. Generic symbolic coefficient expansion checks the diagonal identity; independent verification also checked the full lower-left defect. No formal proof-assistant check.
