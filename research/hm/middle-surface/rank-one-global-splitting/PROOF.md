# Canonical nilbundle and nonexistence of a global retraction

## Statement

Retain the canonical cubic setup and the actual rank-ten open square-zero thickening T of U established in /research/hm/middle-surface/rank-one-open-thickening/PROOF.md and AUDIT.md. Write P=P(V), L=O_P(-1), and E=(V tensor O_P)/L, with dim V=5. Let Z be the rank-drop locus of the quadratic normal map and P°=P\Z. Put

    B={u in V\{0} : [u] in P°},
    U=B × G_m²,    (u,s,t) ↦ (su,u,tu),
    q:U→P°.

Then the following strengthen the prior locally split statement:

1. The nilradical has a canonical identification

       N ≅ q*(E*) = q*(Omega_P(1)).

   Here the normalization uses the specified middle input y=u and the uniquely determined ratios x=su, z=tu on U.

2. Let e be the connecting class of 1 for the exact sequence

       0→N→V* tensor O_U --evaluation at u--> O_U→0.

   With the convention that the Cech cocycle of splittings is sigma_j−sigma_i, the square-zero algebra-extension class is

       kappa(T) = e · (s partial_s − t partial_t)
       in H¹(U,T_U tensor N).

3. The class e, and hence kappa(T), is nonzero. Consequently there is NO global regular retraction T→U restricting to the identity on U, and no global isomorphism of the thickening with the split square-zero algebra O_U plus N. This excludes arbitrary retractions, including ones that change the lifted middle input and both lifted torus coordinates.

The obstruction is the pulled-back tautological extension with its tautological line trivialized by the actual nonzero vector u. It is not an unevaluated obstruction symbol: both its explicit Cech representative and its nonvanishing are established below.

## 1. The good open has complement of codimension at least two

The generic-rank-ten conclusion is supplied by /research/hm/local-defect/rank-eight-global-exclusion/PROOF.md. The saturated-image result in /research/hm/normalizer-rank-five/quintic-normalizer-exclusion/COROLLARY.md then gives an exact sequence on P

    0→G→O_P^20→R→0,

with G a rank-fourteen vector bundle and R torsion-free of rank six. At every codimension-one point, R is free over the corresponding discrete valuation ring, so the injection splits and retains fiber rank fourteen. Splitting off the repeated-input rank-four subbundle identifies the remaining map with the rank-ten-to-sixteen quadratic normal map. Thus Z has codimension at least two; this is also explicitly proved in Section 2 of the cited corollary and agrees with /research/hm/middle-surface/rank-ten-fitting-strata/PROOF.md.

Consequently V\B, the affine cone over Z together with the origin, has codimension at least two in V. If Z is empty, its complement is just the origin. Therefore U is an open subset of V×G_m² whose complement has codimension at least two. Normality, or the intersection-of-height-one-local-rings description of a normal domain, gives

    Gamma(U,O_U)=C[u_1,...,u_5,s,s^(-1),t,t^(-1)].

No assertion that Z is empty or has codimension at least three is used.

## 2. Exact transitions in the actual square-zero thickening

Choose a basis of V*, with elements ell_i, and cover U by U_i={ell_i(u)≠0}. The proof of the open-thickening theorem gives actual coordinates, not just completed coordinates,

    x=S_i(u+p_i),    y=u,    z=T_i(u−p_i),
    ell_i(p_i)=0,    (p_i)²=0.

The discarded variable w is quadratic in p and hence is identically zero on T. The capital S_i,T_i are functions on the thickening, reducing to the globally defined base coordinates s,t. They are explicitly S_i=ell_i(x)/ell_i(y) and T_i=ell_i(z)/ell_i(y). These formulas and the nilpotent structure apply on the entire inverse image of U_i: the local ideal identities glue, so no extra auxiliary shrinking changes the square-zero neighborhood.

Set lambda_i=ell_i/ell_i(u), so lambda_i(u)=1. On an overlap put a_ij=lambda_j(p_i). It is a nilpotent function, and all products of nilpotent functions vanish. Direct substitution gives the exact identities in O_T:

    S_j=S_i(1+a_ij),
    T_j=T_i(1−a_ij),
    p_j=p_i−a_ij u.

For example p_j=(u+p_i)/(1+a_ij)−u=p_i−a_ij u. The analogous computation with z gives the displayed expression with −p_j. The middle input u is unchanged.

The quotient classes [p_i] in (V/O_U u) tensor N agree. The residual normal directions are therefore canonically V/O_U u=q*E, and the nilradical, which is their dual, is canonically q*E*. More explicitly, a covector beta annihilating u represents the nilpotent function beta(p_i), independent of i because beta(p_j)=beta(p_i). This map is an isomorphism on every chart: on ker ell_i the four linear coordinates freely generate N. It also agrees with the coordinate-independent cokernel-of-df* characterization in the open-thickening theorem.

The Euler sequence identifies E* with Omega_P(1). The trivialization of q*L used in the displayed evaluation sequence is u itself, so there is no missing line-bundle twist.

## 3. The algebra-extension class

The local retraction defines a C-algebra splitting sigma_i:O_U|U_i→O_T|U_i by

    sigma_i(u)=y,    sigma_i(s)=S_i,    sigma_i(t)=T_i.

Differences of algebra splittings of a square-zero extension are derivations into N. Since lambda_i(p_i)=0,

    a_ij=(lambda_j−lambda_i)(p_i).

Under N=q*E*, a_ij is the section lambda_j−lambda_i. These differences are the Cech representative of e=delta(1) for the exact evaluation sequence in the statement. The transition formulas give

    (sigma_j−sigma_i)(u_k)=0,
    (sigma_j−sigma_i)(s)=s a_ij,
    (sigma_j−sigma_i)(t)=−t a_ij.

Thus the derivation cocycle is precisely a_ij(s partial_s−t partial_t), proving the formula for kappa(T). These statements are equally valid for sheaf cohomology; no acyclicity of the chosen chart cover is assumed.

## 4. Nonvanishing and exclusion of all retractions

If e=0, exactness of the long cohomology sequence would give a global section lambda=(f_1,...,f_5) of V* tensor O_U with lambda(u)=1. By Section 1 all f_i are polynomials in u with Laurent-polynomial dependence on s,t. The identity would read

    sum_i f_i(u,s,t) u_i=1

in C[u_1,...,u_5,s±1,t±1]. Specializing u=0 gives 0=1. Hence e≠0.

Because U is the indicated product open, its tangent bundle has the canonical product decomposition

    T_U = (V tensor O_U) direct-sum O_U(s partial_s) direct-sum O_U(t partial_t).

The globally defined one-form dlog s gives a bundle map T_U tensor N→N. It sends the extension cocycle to a_ij and therefore sends kappa(T) to e. Hence kappa(T)≠0.

A global algebra splitting, of any kind, would make the cocycle of differences between local splittings a coboundary in T_U tensor N. Applying dlog s would make e a coboundary, contradiction. In particular, allowing a putative retraction to modify the lifted u coordinates cannot cancel the obstruction: projection to the dlog s summand still detects it. An isomorphism to a split thickening allowing an automorphism of the reduction would likewise induce a retraction after composing with the inverse reduction automorphism.

## 5. A useful globally defined partial projection

The same formulas show S_j T_j=S_i T_i. Thus the local products glue to a global invertible function h on T reducing to st. Together with the actual middle-input morphism y, this gives a canonical morphism

    T→B×G_m,    (y,h),

extending (u,s,t)↦(u,st) on U. The failure to retract is concentrated in the remaining anti-diagonal torus direction. The existence of this partial projection does not produce a full retraction or contradict the preceding obstruction.

## Scope and novelty

The prior open-thickening theorem stops at the abstract H¹ obstruction; the even-normal-form theorem gives local parity and generic algebra. The new results identify the familiar nilbundle, compute the actual transition class, and prove it nonzero using the existing codimension-two bound. They concern universal rank-one geometry only. They do not evaluate an operation, actual source, model matrix, selected input, jet, residue, or detector, and do not settle the original physical or higher module/connection obstruction. 

## 6. Exact image of the global-function restriction

Write A=C[u_1,...,u_5,s±1,t±1], I=(u_1,...,u_5)A, and E_0=s partial_s−t partial_t. The additive connecting homomorphism for the square-zero extension is

    boundary:A→H¹(U,N),    f↦E_0(f)e.

Indeed the local lifts sigma_i(f) have differences obtained by applying the already computed derivation cocycle to f. The sign convention is the same as in Section 3. The evaluation sequence in the statement has global-section image I; its connecting homomorphism sends g to ge. Hence

    annihilator_A(e)=I.

Exactness for the additive sequence 0→N→O_T→O_U→0 therefore proves

    image[Gamma(T,O_T)→A]
       = {f in A : E_0(f) in I}
       = I + C[(st)±1].

For the last equality, reduce modulo I and use that the kernel of s partial_s−t partial_t on C[s±1,t±1] consists exactly of the Laurent monomials s^m t^m. Thus s and t individually have no global lifts as functions on T, while st and every function in I do lift. This conclusion is stronger than merely excluding a compatible choice of lifts defining a retraction.

For completeness, the nilpotent kernel on global sections is explicitly

    Gamma(U,N)={ (f_1,...,f_5) in A^5 : sum_i f_i u_i=0 }.

It is the usual module of syzygies of the coordinate ideal. The resulting exact sequence of rings has square-zero kernel, but no splitting of that global ring sequence is asserted.

## 7. The ring of global functions is not finitely generated

Set A_0=I+C[h±1], where h=st. The subset I is an ideal of A_0 and A_0/I=C[h±1]. Its square as an A_0-ideal equals its square as an A-ideal: every generator u_i u_j a, a in A, is the product of u_i in I with u_j a in I. Consequently

    I/I² ≅ C[s±1,t±1]^5

as a module over A_0/I=C[h±1]. Since C[s±1,t±1]=C[h±1,s±1], this module has infinite rank over C[h±1]. Thus I cannot be a finitely generated ideal of A_0. The algebra A_0 is non-Noetherian, in particular not finitely generated over C. Since Gamma(T,O_T) surjects onto A_0, it too is non-Noetherian and is not a finitely generated C-algebra.

This is a statement about global sections of a finite-type non-affine scheme; it does not say that T fails to be locally of finite type. The phenomenon comes from gluing the square-zero neighborhood and is independent of any operation evaluation.

## 8. The nilbundle is not globally trivial

Suppose N were isomorphic to O_U^4. Taking global sections and using Gamma(U,O_U)=A would give Gamma(U,N)≅A^4. On the other hand, Section 6 identifies Gamma(U,N) with the syzygy module K of the regular sequence u_1,...,u_5 in A. Its Koszul presentation begins

    A^10 → K → 0,

with relation module the image of A^10=exterior³(A^5), whose matrix entries all lie in (u_1,...,u_5). At the maximal ideal

    m=(u_1,...,u_5,s−1,t−1)

this is a minimal presentation: tensoring the Koszul presentation with A/m gives K/mK≅C^10. Hence K has ten minimal generators at m and cannot be free of rank four. This contradiction proves that N is not globally trivial.

Here localization at m is a test on the global A-module Gamma(U,N). The point m is outside U; the argument neither claims it belongs to U nor extends the vector bundle there. No stable-triviality assertion is made.
