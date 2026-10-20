# Empty rank-one incidence excludes divisorial four-kernel strata

## Theorem

Work over C. Let B be a smooth variety, S a rank-three vector bundle on B, and K' a rank-four subbundle of End(S) (in particular, it may lie in sl(S)). Suppose every nonzero element in every geometric fiber of K' has rank at least two. In rational Chow theory, writing d=c1(S), b=c2(S), c=c3(S), one has

    c1(K')=0,
    c2(K')=b-d^2/3,
    c3(K')=c4(K')=0,
    27c-9db+2d^3=0.

The last identity is stronger than the undecorated empty-rank-one Porteous identity. It follows from the empty incidence remembering a candidate image line. The proof below does not need to invoke a degeneracy-locus formula.



## Relative application

On Gr(3,C^5), let T:sl(S)⊗det(S) → J⊗O be a bundle map all of whose geometric kernels are rank-one-free and of dimension at most four. Then its kernel-dimension-four locus G4 has dimension at most four. These are explicit hypotheses; this manuscript does not establish them for any named cubic operation.

## 1. An everywhere nonzero universal section

Use the projectivization convention of lines. On

    Z=P_B(K') x_B P_B(S)

let t=c1(O_P(K')(1)) and h=c1(O_P(S)(1)). Pullbacks of bundles on B are implicit. Let L=O_P(S)(-1) be the candidate image line and Q=S/L, of rank two.

The universal endomorphism on P(K') is

    A:S -> S tensor O_P(K')(1).

Compose with the projection to Q. This gives a section of the rank-six bundle

    F=Hom(S,Q) tensor O_P(K')(1).

The section cannot vanish at any geometric point: vanishing means that the image of the nonzero endomorphism A is contained in L, forcing rank at most one. This contradicts the hypothesis. Consequently the section is a line subbundle O_Z -> F, with locally free rank-five quotient. Thus c6(F)=0. This proves the needed vanishing directly, including its behavior on any smooth base obtained by pullback; there is no expected-codimension assumption.

## 2. The universal top Chern calculation

The projective-bundle relation on P(S) is

    h^3+d h^2+b h+c=0.

The quotient bundle has

    c1(Q)=d+h,
    c2(Q)=b+d h+h^2.

If x1,x2,x3 are the formal Chern roots of S, then

    c6(F)=product over i=1,2,3 of
        [(t-x_i)^2+(d+h)(t-x_i)+b+d h+h^2].

Here sum x_i=d, sum_(i<j) x_i x_j=b, and x1 x2 x3=c. Expanding this symmetric product and reducing by the displayed cubic relation in h gives

    c6(F)=P0+h P1+h^2 P2,

where

    P0=t^2[4b^2-bd^2-3cd+(4bd-d^3-9c)t
             +(5b-d^2)t^2+d t^3+t^4],

    P1=t^2[7bd-9c-2d^3+(3b-d^2)t+4d t^2+3t^3],

    P2=2t^2[3b-d^2+3t^2].

This identity can also be checked by taking the resultant, in an indeterminate z, of

    z^3-dz^2+bz-c

and

    (t-z)^2+(d+h)(t-z)+b+d h+h^2,

then reducing modulo h^3+d h^2+b h+c. These are universal formal polynomials, not instances of the structural operation.

The projective-bundle theorem makes 1,h,h^2 a free basis over CH*(P(K'))_Q. Since c6(F)=0, each Pj vanishes separately.

## 3. Recovering Porteous and obtaining the missing relation

Put k_i=c_i(K'). The other projective-bundle relation is

    t^4+k1 t^3+k2 t^2+k3 t+k4=0.

From P2=0 one has

    6t^4+(6b-2d^2)t^2=0.

Reduce t^4 using this relation and compare the free coefficients of 1,t,t^2,t^3 over CH*(B)_Q. It follows that

    k1=0, k2=b-d^2/3, k3=0, k4=0.

Thus, with a=b-d^2/3,

    t^4=-a t^2,  t^5=-a t^3.

This recovers the undecorated empty-rank-one Chern identity while avoiding Porteous.

Now reduce P1:

    P1=3t^5+4d t^4+(3b-d^2)t^3
          +(7bd-9c-2d^3)t^2
       =(3bd-9c-2d^3/3)t^2
       =-(27c-9db+2d^3)t^2/3.

The t^3 coefficient cancels because 3b-d^2=3a. Freeness of 1,t,t^2,t^3 forces

    R:=27c-9db+2d^3=0

on B. For completeness, P0 reduces to

    -(R/3)t^3-(dR/9)t^2,

so it imposes no additional relation beyond this one.

The additional information beyond the undecorated empty-rank-one identity is therefore the coefficient P1, or equivalently the empty image-line incidence decorated by one more projective hyperplane class.

## 4. Application to a possible rank-four-kernel divisor

On G=Gr(3,C^5), let S be tautological, E=sl(S) tensor det S, and T:E -> J tensor O the given bundle map. Its kernels have dimension at most four by hypothesis. Hence the locus G4 where the kernel has dimension four is closed: it is the rank-at-most-four locus of T, and there is no lower-rank locus. Give G4 its reduced structure.

On G4 the map has constant rank four. Locally choose an invertible four-by-four minor and perform invertible row and column operations. The remaining block vanishes on the reduced base because all five-by-five minors do. Consequently K=ker T is a rank-four vector subbundle, and K'=K tensor (det S)^(-1) is a rank-four subbundle of sl(S). Its fibers have no rank-one elements.

Suppose G4 has an integral component Y of dimension five. Resolve it projectively, obtaining a smooth projective X of dimension five and a map g:X -> G, birational onto Y. Pulling back K', S preserves their subbundle inclusions and rank-one exclusion. Sections 1-3 therefore give g^*R=0.

Let H=c1(S*) be the Plucker class. Pic(G)=Z H, so the nonzero effective divisor cycle g_*[X]=[Y] is mH with integer m>0. The standard Schubert intersection numbers are

    integral_G H^6=5,
    integral_G H^4 c2(S)=3,
    integral_G H^3 c3(S)=-1,
    c1(S)=-H.

They follow from Pieri's rule in the 3-by-2 rectangle, as detailed in SINGULAR-NET-LOCUS.md. Therefore

    integral_G R H^3 = -27+27-10=-10.

The projection formula gives the contradiction

    0=integral_X g^*(R H^2)
     =integral_G R H^2 (mH)
     =-10m.

A six-dimensional component is impossible by the same argument, using R H^3 on its resolution and the positive generic degree onto G.  Thus dim G4 <=4.

This argument does not require G4 to be smooth, normal, or reduced in its natural determinantal scheme structure. The reduced structure and a resolution suffice for the dimension claim.

