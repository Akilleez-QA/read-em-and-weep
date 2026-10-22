# A plane-trace obstruction for the Q4 quadratic residual map

## Result and boundary

Let M_d=H^1(I_C(d)) for the 25 disjoint HM lines. Retain I_C(1)=I_C(2)=I_C(3)=0; these follow from the established I_C(4)=0. Then dim M_1=45 and dim M_3=65. Quadratic multiplication q:M_1 -> M_3 is dual, up to the common determinant line, to the quadratic residual map toward H^1(B(4))/P_4. Its kernel is exactly that residual cokernel's dual.

For a product q=ell_1 ell_2 we obtain a symmetric obstruction in a ten-dimensional plane-cubic space. This is a new gluing criterion, not a proof that generic q is injective. It separates section quadrics from compatibility between section cubics, without assuming a lifting theorem for a disconnected curve.

## 1. Proper hyperplane sections and the two elementary kernels

If H=V(ell) contains no component line, ell is a nonzerodivisor on O_C. Writing Z=C intersect H, the ideal restriction sequence is

0 -> I_C(d) --ell--> I_C(d+1) -> I_(Z,H)(d+1) -> 0.

Because I_C(1), I_C(2), and I_C(3) vanish on global sections, the connecting morphisms give canonical identifications

ker(ell:M_1 -> M_2)=H^0(I_(Z,H)(2)),
ker(ell:M_2 -> M_3)=H^0(I_(Z,H)(3)).

For two proper sections, composition therefore gives

0 -> H^0(I_(Z_1,H_1)(2)) -> ker(ell_1 ell_2:M_1 -> M_3)
  -> ell_1 M_1 intersect ker(ell_2:M_2 -> M_3) -> 0.

The intersection is taken inside M_2, with the second kernel identified by its actual connecting morphism. Counting the cubic kernel alone would overestimate this intersection.

## 2. Symmetric gluing along the intersection plane

Choose distinct proper hyperplanes H_1,H_2 such that Pi=H_1 intersect H_2 avoids C. Such pairs form a nonempty open: a general plane in P^4 misses the finite union of lines. Then Z_i consists of 25 reduced points in H_i, disjoint from Pi, and Z_1 and Z_2 are disjoint.

Put

A_i=H^0(I_(Z_i,H_i)(2)),
V_i=H^0(I_(Z_i,H_i)(3)),
T_i=image[V_i -> H^0(O_Pi(3))].

The common target H^0(O_Pi(3)) has dimension ten. The exact criterion is

0 -> A_1 directsum A_2 -> ker(ell_1 ell_2:M_1 -> M_3)
  -> T_1 intersect T_2 -> 0.                         (1)

Proof. Let Q=H_1 union H_2 and Z=C intersect Q=Z_1 disjointunion Z_2. Since q=ell_1 ell_2 is a nonzerodivisor on C,

0 -> I_C(1) --q--> I_C(3) -> I_(Z,Q)(3) -> 0.

The vanishing of the two global ideal spaces identifies ker(q:M_1 -> M_3) with H^0(I_(Z,Q)(3)). The structure-sheaf gluing sequence for Q identifies this last space with

{(f_1,f_2) in V_1 directsum V_2 : f_1|Pi=f_2|Pi}.

Send such a pair to its common trace in T_1 intersect T_2. This is onto by the definition of T_i. Its kernel is the direct sum of the two trace kernels. Since Z_i avoids Pi, those kernels are exactly

ker(V_i -> H^0(O_Pi(3)))=(ell_j|H_i) A_i, j not equal i.

Multiplication by the nonzero equation ell_j|H_i identifies this with A_i. This proves (1). Rescaling either equation merely rescales the corresponding identification; the trace-kernel spaces themselves are intrinsic.

Consequently

q:M_1 -> M_3 is injective
iff A_1=A_2=0 and T_1 intersect T_2=0.              (2)

In particular no cubics on either section is sufficient, but is not necessary for this criterion: nonzero cubic systems can have disjoint traces in the common plane.

## 3. Numerical and openness consequences without evaluating maps

Equation (1) gives the exact defect

dim ker(q)=dim A_1+dim A_2+dim(T_1 intersect T_2).

Since dim T_i=dim V_i-dim A_i,

dim ker(q)>=max(dim A_1+dim A_2, dim V_1+dim V_2-10).

Let a and b be the generic values of h^0(I_(Z,H)(2)) and h^0(I_(Z,H)(3)). For a general pair of proper hyperplanes,

dim ker(ell_1 ell_2:M_1 -> M_3)>=max(2a,2b-10).

Thus product-quadratic injectivity requires a=0 and b<=5; when these numerical conditions hold, the remaining obstruction is the actual intersection of the two cubic trace spaces. Matching dimensions or ordinary expected-transversality reasoning does not prove that intersection zero.

If some proper H has h^0(I_(Z,H)(3))=0, it also has no quadrics, since multiplication by any nonzero linear form embeds its quadric ideal space into its cubic ideal space. Both consecutive ell maps above are then injective, hence ell^2:M_1 -> M_3 is injective. Maximal rank is open in the full space of quadrics, so this would prove generic quadratic residual surjectivity. Likewise, one pair satisfying (2) would suffice: injectivity is an open condition in the full quadratic parameter space, and a reducible quadratic can witness that this open is nonempty. Neither this section hypothesis nor the trace transversality in (2) has been established here.

Conversely, failure for every product does not by itself imply failure for every quadratic: reducible quadrics form a proper closed subset of the full parameter space. The present criterion is a sufficient route to a generic result, not a classification of all quadrics.

## 4. Why the available lifting claims do not close the remaining step

The primary paper inspected for reducible Laudal-type statements is R. Di Nardo, 'Laudal type theorems for algebraic curves', Rend. Sem. Mat. Univ. Pol. Torino 65(3) (2007), Theorem 2:
https://seminariomatematico.polito.it/rendiconti/65-3/301.pdf .

Its reducible result concerns curves in P^3 and assumes that the general plane section has a Hilbert function of decreasing type. It also explains why hypotheses cannot simply be discarded for reducible curves. Our arrangement is a disconnected curve in P^4. Neither a suitable reduction to that theorem nor its additional section hypothesis has been proved. Integral-curve uniform-position results therefore cannot be substituted here.

Likewise, the primitive-partition proof used for scalar residue tuples does not directly apply to these degree-one tuple multipliers. Here the hyperplane-section condition involves the full subspace ell S_(d-1), not one generic hyperplane in S_d^*. The known generic-hyperplane theorem supplies no automatic higher-degree section rank.

The quintic sheaf generators do restrict to generators of the section ideal sheaf, but this does not prohibit nonlifting quadrics or cubics in its saturation. It would be circular to infer their absence from the degrees of those generators.

## Sources and scope

Current PR1 was read before beginning. It records PR543's Q4 constraint at e16586f3058cb02a2aac958ed01282f50385dd2b, including I_C(4)=0, and PR541's exact linear corank at 9ce30d8d783da881be68548d158ebcb48e122850. Neither supplies the missing section-cubic vanishing or plane-trace transversality.

The new output is the exact symmetric plane-trace obstruction (1), its sharp injectivity criterion (2), and the distinction between section-cubic vanishing and the weaker condition actually needed for products. No selected coefficients, ranks, hyperplanes or quadratic instances were evaluated. No generic injectivity or full Q4 vanishing claim is made.
